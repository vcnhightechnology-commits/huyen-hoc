"""Prepare one deduplicated, hash-verified GitHub materials handoff (no source deletion)."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import os, json, re, zipfile

W = Path(__file__).resolve().parent.parent
OUT = W / 'tmp/materials-handoff'
META = W / 'collaboration/materials'
assert not OUT.exists(), 'Inspect an existing handoff before creating another.'
OUT.mkdir(parents=True)
META.mkdir(parents=True, exist_ok=True)
excluded_dirs = {'.git', '.codex', '.aws', 'archives', '__pycache__'}
excluded_prefixes = ('tmp/github-tools/', 'tmp/github-validation/', 'tmp/materials-handoff/', 'tmp/materials-tests/', 'tmp/materials-remote-check/', 'tmp/materials-http-check/', 'tmp/materials-restore-check/', 'tmp/materials-range-check/', 'collaboration/materials/')
excluded_names = {'.env', '.env.local', 'accounts.json', 'cookies.json'}
patterns = [re.compile(p) for p in [rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----', rb'gh[pousr]_[A-Za-z0-9]{25,}', rb'github_pat_[A-Za-z0-9_]{35,}', rb'AKIA[0-9A-Z]{16}']]
paths = []
omitted = []
for base, dirs, names in os.walk(W):
    dirs[:] = sorted(d for d in dirs if d not in excluded_dirs)
    for name in sorted(names):
        p = Path(base) / name
        rel = p.relative_to(W).as_posix()
        if rel.startswith(excluded_prefixes):
            continue
        if (p.parent == W and p.suffix.lower() == '.zip') or name.endswith(('.pyc', '.sqlite-wal', '.sqlite-shm', '.sqlite-journal')):
            omitted.append(rel)
            continue
        if name in excluded_names or name.endswith(('.pem', '.key')):
            raise RuntimeError('Credential-like filename requires inspection: ' + rel)
        assert not p.is_symlink(), rel
        paths.append((rel, p))
files = []
objects = {}
for n, (rel, p) in enumerate(sorted(paths), 1):
    before = p.stat()
    h = sha256()
    prefix = b''
    with p.open('rb') as f:
        for b in iter(lambda: f.read(8 * 1024 * 1024), b''):
            h.update(b)
            if len(prefix) < 8 * 1024 * 1024:
                prefix += b[:8 * 1024 * 1024 - len(prefix)]
    after = p.stat()
    assert (before.st_size, before.st_mtime_ns) == (after.st_size, after.st_mtime_ns), rel
    if any(rx.search(prefix) for rx in patterns):
        raise RuntimeError('Potential credential content requires inspection: ' + rel)
    digest = h.hexdigest()
    files.append({'file': rel, 'bytes': after.st_size, 'sha256': digest})
    objects.setdefault(digest, {'source': p, 'bytes': after.st_size, 'mtime': after.st_mtime_ns})
    if n % 3000 == 0:
        print(json.dumps({'stage': 'inventory', 'files': n, 'uniqueObjects': len(objects)}), flush=True)

shards = []
objrows = {}
limit = 440 * 1024 * 1024
z = None
used = 0
def close_shard():
    global z
    if z is None:
        return
    z.close()
    p = OUT / shards[-1]['file']
    h = sha256()
    with p.open('rb') as f:
        for b in iter(lambda: f.read(8 * 1024 * 1024), b''): h.update(b)
    shards[-1].update(bytes=p.stat().st_size, sha256=h.hexdigest())
    assert p.stat().st_size < 512 * 1024 * 1024
    print(json.dumps({'stage': 'bundle-written', **shards[-1]}), flush=True)
    z = None

for digest, row in sorted(objects.items()):
    assert row['bytes'] < limit, 'Single source needs explicit splitting: ' + str(row['source'])
    if z is None or used + row['bytes'] > limit:
        close_shard()
        name = f'hhc-materials-{len(shards)+1:03d}.zip'
        shards.append({'file': name})
        z = zipfile.ZipFile(OUT / name, 'x', zipfile.ZIP_DEFLATED, compresslevel=1)
        used = 0
    p = row['source']; st = p.stat()
    assert (st.st_size, st.st_mtime_ns) == (row['bytes'], row['mtime'])
    h = sha256()
    member = 'objects/' + digest
    with p.open('rb') as src, z.open(member, 'w') as dst:
        for b in iter(lambda: src.read(8 * 1024 * 1024), b''): dst.write(b); h.update(b)
    assert h.hexdigest() == digest
    objrows[digest] = {'bytes': row['bytes'], 'bundle': shards[-1]['file'], 'member': member}
    used += row['bytes']
close_shard()

verified = 0
for shard in shards:
    with zipfile.ZipFile(OUT / shard['file']) as archive:
        for item in archive.infolist():
            digest = item.filename.split('/')[-1]; h = sha256(); size = 0
            with archive.open(item) as src:
                for b in iter(lambda: src.read(8 * 1024 * 1024), b''): h.update(b); size += len(b)
            assert h.hexdigest() == digest and size == objrows[digest]['bytes']
            verified += 1
    print(json.dumps({'stage': 'bundle-members-verified', 'bundle': shard['file'], 'objects': verified}), flush=True)
assert verified == len(objects)
manifest = {'schema': 'hhc-materials-v1', 'date': '2026-10-31', 'createdUTC': datetime.now(timezone.utc).isoformat(), 'repository': 'dedaithien-sudo/huyen-hoc', 'releaseTag': 'materials-v53', 'files': files, 'objects': objrows, 'bundles': shards, 'excluded': {'rootGeneratedZIPs': 'Their material content is represented by current individual files, not uploaded a second time as full ZIP snapshots.', 'directories': sorted(excluded_dirs), 'prefixes': list(excluded_prefixes), 'otherFiles': omitted}, 'privateRepositoryRequired': True, 'allObjectMembersSHA256Verified': True, 'localSourcesDeleted': False}
(META / 'MANIFEST.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'stage': 'ready', 'files': len(files), 'uniqueObjects': len(objects), 'bundleCount': len(shards), 'uploadBytes': sum(x['bytes'] for x in shards)}), flush=True)
