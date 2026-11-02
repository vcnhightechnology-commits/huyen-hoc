"""Upload materials to the explicitly authorized public destination; verify server SHA-256."""
from pathlib import Path
from hashlib import sha256
import argparse, json, subprocess

W = Path(__file__).resolve().parent.parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--gh', default='gh')
args = parser.parse_args()
m = json.loads((W/'collaboration/materials/MANIFEST.json').read_text(encoding='utf-8'))
repo = m['repository']; tag = m['releaseTag']
assert repo == 'dedaithien-sudo/huyen-hoc' and tag == 'materials-v53'

def gh(*cmd):
    r = subprocess.run([args.gh, *cmd], capture_output=True, text=True, check=True)
    return json.loads(r.stdout)

assert gh('api', 'repos/'+repo)['private'] is False, 'Destination visibility must match the user-authorized PUBLIC repository.'
releases = gh('api', f'repos/{repo}/releases?per_page=100')
release = next(r for r in releases if r['tag_name'] == tag)
rid = release['id']
existing = {a['name']: a for a in gh('api', f'repos/{repo}/releases/{rid}/assets?per_page=100')}
assets = list(m['bundles'])
meta = W/'collaboration/materials/MANIFEST.json'
assets.append({'file': 'MANIFEST.json', 'bytes': meta.stat().st_size, 'sha256': sha256(meta.read_bytes()).hexdigest()})
verified = []
for a in assets:
    name = a['file']
    if name not in existing:
        p = meta if name == 'MANIFEST.json' else W/'tmp/materials-handoff'/name
        assert p.is_file() and p.stat().st_size == a['bytes']
        print(json.dumps({'stage': 'uploading', 'asset': name, 'bytes': a['bytes']}), flush=True)
        subprocess.run([args.gh, 'release', 'upload', tag, str(p), '--repo', repo], check=True)
        existing = {x['name']: x for x in gh('api', f'repos/{repo}/releases/{rid}/assets?per_page=100')}
    remote = existing[name]
    assert remote['state'] == 'uploaded' and remote['size'] == a['bytes'], name
    assert remote.get('digest') == 'sha256:'+a['sha256'], 'Remote SHA-256 does not match: '+name
    verified.append({'file': name, 'bytes': a['bytes'], 'sha256': a['sha256'], 'assetID': remote['id'], 'serverDigestVerified': True})
    print(json.dumps({'stage': 'uploaded-and-verified', 'asset': name, 'completed': len(verified), 'total': len(assets)}), flush=True)
out = {'status': 'all-private-release-assets-uploaded-and-server-sha256-verified', 'repository': repo, 'releaseTag': tag, 'releaseID': rid, 'assets': verified, 'sourceFiles': len(m['files']), 'uniqueObjects': len(m['objects']), 'releasePublished': not release['draft']}
(W/'collaboration/materials/UPLOAD_VERIFICATION.json').write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'stage': 'ready-to-publish', 'assets': len(verified), 'sourceFiles': len(m['files'])}), flush=True)
