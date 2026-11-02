"""List, download, verify and restore selected HHC source materials from a private release."""
from pathlib import Path, PurePosixPath
from hashlib import sha256
import argparse, json, os, subprocess, zipfile, re

W = Path(__file__).resolve().parent.parent

def digest(path):
    h = sha256()
    with path.open('rb') as f:
        for b in iter(lambda: f.read(8 * 1024 * 1024), b''): h.update(b)
    return h.hexdigest()

def safe_relative(name):
    p = PurePosixPath(name)
    if p.is_absolute() or not p.parts or any(x in {'..', '.', '.git', '.aws', '.codex'} for x in p.parts) or '\\' in name or ':' in name:
        raise ValueError('Unsafe material path: ' + name)
    return p

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, default=W/'collaboration/materials/MANIFEST.json')
    parser.add_argument('--prefix', action='append', default=[], help='Original source directory prefix; repeatable')
    parser.add_argument('--path', action='append', default=[], help='Exact original source path; repeatable')
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--list', action='store_true', help='List selected original files without downloading')
    parser.add_argument('--download', action='store_true', help='Use authenticated GitHub CLI to download required bundles')
    parser.add_argument('--gh', default='gh', help='Path to GitHub CLI; credentials are never written to the repository')
    parser.add_argument('--cache', type=Path, default=W/'tmp/materials-handoff')
    parser.add_argument('--destination', type=Path, help='Restore files into this workspace or an independent evidence directory')
    args = parser.parse_args()
    m = json.loads(args.manifest.read_text(encoding='utf-8'))
    assert m['schema'] == 'hhc-materials-v1'
    if not (args.all or args.prefix or args.path): parser.error('Choose --all, --prefix or --path explicitly.')
    selected = [r for r in m['files'] if args.all or r['file'] in args.path or any(r['file'].startswith(p) for p in args.prefix)]
    if not selected: parser.error('No matching material paths.')
    for name in args.path:
        if not any(r['file'] == name for r in selected): parser.error('Unknown exact path: ' + name)
    for r in selected:
        safe_relative(r['file'])
        assert re.fullmatch('[0-9a-f]{64}', r['sha256'])
    if args.list:
        for r in selected: print(json.dumps(r, ensure_ascii=False))
        return
    if args.destination is None: parser.error('Set --destination explicitly, or use --list.')
    dest = args.destination.resolve()
    needed = {m['objects'][r['sha256']]['bundle'] for r in selected}
    bundles = {r['file']: r for r in m['bundles']}
    cache = args.cache.resolve(); cache.mkdir(parents=True, exist_ok=True)
    for name in sorted(needed):
        assert name in bundles and re.fullmatch(r'hhc-materials-[0-9]{3}\.zip', name)
        p = cache/name
        if not p.exists():
            if not args.download: raise FileNotFoundError(f'{p}: use --download with an authenticated GitHub CLI, or download this release asset manually.')
            subprocess.run([args.gh, 'release', 'download', m['releaseTag'], '--repo', m['repository'], '--pattern', name, '--dir', str(cache)], check=True, timeout=180)
        assert p.stat().st_size == bundles[name]['bytes'] and digest(p) == bundles[name]['sha256'], 'Bundle checksum mismatch: '+name
    restored = 0
    # Preflight every existing destination before any write. Never replace local work.
    for r in selected:
        dst = (dest/r['file']).resolve()
        assert dst.is_relative_to(dest), r['file']
        if dst.exists():
            assert dst.is_file() and dst.stat().st_size == r['bytes'] and digest(dst) == r['sha256'], 'Existing file differs: '+str(dst)
    grouped = {}
    for r in selected: grouped.setdefault(m['objects'][r['sha256']]['bundle'], []).append(r)
    for name, rows in grouped.items():
        with zipfile.ZipFile(cache/name) as archive:
            for r in rows:
                dst = (dest/r['file']).resolve()
                if dst.exists(): continue
                info = m['objects'][r['sha256']]
                assert info['member'] == 'objects/'+r['sha256'] and info['bytes'] == r['bytes']
                dst.parent.mkdir(parents=True, exist_ok=True)
                pending = dst.with_name(dst.name+'.hhc-pending')
                h = sha256(); size = 0
                try:
                    with archive.open(info['member']) as src, pending.open('xb') as out:
                        for b in iter(lambda: src.read(8 * 1024 * 1024), b''): out.write(b); h.update(b); size += len(b)
                    assert h.hexdigest() == r['sha256'] and size == r['bytes'], r['file']
                    # Hard-link creation refuses an existing destination, including a racing writer.
                    os.link(pending, dst)
                    restored += 1
                finally:
                    if pending.exists(): pending.unlink()
        print(json.dumps({'bundle': name, 'verifiedAndRestoredSoFar': restored}), flush=True)
    print(json.dumps({'selectedFiles': len(selected), 'requiredBundles': len(needed), 'restored': restored, 'allSelectedSHA256Verified': True}))

if __name__ == '__main__': main()
