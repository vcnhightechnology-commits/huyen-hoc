"""Retain source-package member variants absent from the current live handoff."""
from pathlib import Path
from hashlib import sha256
import json, zipfile

W = Path(__file__).resolve().parent.parent
P = W/'collaboration/materials/MANIFEST.json'
m = json.loads(P.read_text(encoding='utf-8'))
assert 'historicalSourcePackageCoverage' not in m
old_path = W/'recovery/storage-consolidation/LATEST_PACKAGE_MANIFEST.json'
old = json.loads(old_path.read_text(encoding='utf-8'))
assert old['status'] == 'latest-source-package-member-sha256-verified'
missing = [r for r in old['files'] if r['sha256'] not in m['objects']]
unique = {r['sha256']: r for r in missing}
assert sum(r['bytes'] for r in unique.values()) < 440*1024*1024, 'Inspect larger history supplement explicitly.'
name = f"hhc-materials-{len(m['bundles'])+1:03d}.zip"
out = W/'tmp/materials-handoff'/name
if missing:
    with zipfile.ZipFile(W/'Huyen_Hoc_Cac_V53_source.zip') as source, zipfile.ZipFile(out, 'x', zipfile.ZIP_DEFLATED, compresslevel=1) as z:
        for digest, r in unique.items():
            h = sha256(); size = 0
            with source.open(r['file']) as src, z.open('objects/'+digest, 'w') as dst:
                for b in iter(lambda: src.read(8*1024*1024), b''): dst.write(b); h.update(b); size += len(b)
            assert h.hexdigest() == digest and size == r['bytes'], r['file']
            m['objects'][digest] = {'bytes': size, 'bundle': name, 'member': 'objects/'+digest}
    with zipfile.ZipFile(out) as z:
        for digest, r in unique.items():
            h = sha256()
            with z.open('objects/'+digest) as src:
                for b in iter(lambda: src.read(8*1024*1024), b''): h.update(b)
            assert h.hexdigest() == digest
    h = sha256()
    with out.open('rb') as src:
        for b in iter(lambda: src.read(8*1024*1024), b''): h.update(b)
    m['bundles'].append({'file': name, 'bytes': out.stat().st_size, 'sha256': h.hexdigest()})
    for r in missing:
        m['files'].append({'file': 'recovery/materials-historical-source-package/'+r['file'], 'bytes': r['bytes'], 'sha256': r['sha256'], 'originalArchiveMember': r['file']})
assert all(r['sha256'] in m['objects'] for r in old['files'])
m['historicalSourcePackageCoverage'] = {'container': 'Huyen_Hoc_Cac_V53_source.zip', 'memberManifest': old_path.relative_to(W).as_posix(), 'memberManifestSHA256': sha256(old_path.read_bytes()).hexdigest(), 'members': len(old['files']), 'allMemberContentHashesRepresented': True, 'missingLiveVariantsAdded': len(missing), 'uniqueVariantObjectsAdded': len(unique), 'archiveWrapperBytesNotDuplicated': True, 'restoredVariantPathPrefix': 'recovery/materials-historical-source-package/'}
P.write_text(json.dumps(m, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(m['historicalSourcePackageCoverage']), flush=True)
