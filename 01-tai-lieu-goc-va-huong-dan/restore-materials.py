"""Download one handoff release asset and verify its SHA-256."""
from pathlib import Path
import argparse,hashlib,json,subprocess,urllib.request

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--list',action='store_true');p.add_argument('--file');p.add_argument('--destination',type=Path)
p.add_argument('--anonymous',action='store_true');p.add_argument('--gh',default='gh')
a=p.parse_args()
m=json.loads((Path(__file__).resolve().parent/'GITHUB_MATERIALS.json').read_text('utf-8'))
if a.list:
    for x in m['assets']:print(x['file'],x['bytes'],x['sha256'])
elif a.file and a.destination:
    x=next(v for v in m['assets'] if v['file']==a.file)
    a.destination.mkdir(parents=True,exist_ok=True);target=a.destination/x['file']
    if target.exists():
        assert target.stat().st_size==x['bytes'] and hashlib.file_digest(target.open('rb'),'sha256').hexdigest()==x['sha256'],'Existing file has different bytes'
        print('Already verified:',target);raise SystemExit(0)
    pending=a.destination/(x['file']+'.partial')
    if a.anonymous:
        with urllib.request.urlopen(urllib.request.Request(x['url'],headers={'User-Agent':'HHC-Materials'}),timeout=120) as src,pending.open('wb') as dst:
            while block:=src.read(1024*1024):dst.write(block)
    else:
        subprocess.run([a.gh,'release','download',m['releaseTag'],'--repo',m['repository'],'--pattern',x['file'],'--output',str(pending)],check=True)
    assert pending.stat().st_size==x['bytes'] and hashlib.file_digest(pending.open('rb'),'sha256').hexdigest()==x['sha256'],'Downloaded bytes failed verification; partial file retained'
    pending.replace(target);print('SHA-256 verified:',target)
else:p.error('Use --list or --file NAME --destination DIRECTORY')
