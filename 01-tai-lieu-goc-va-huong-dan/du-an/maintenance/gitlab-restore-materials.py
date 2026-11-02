"""Download one GitLab material asset and verify its SHA-256 before making it usable."""
from pathlib import Path
import argparse, hashlib, json, os, urllib.request

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--list',action='store_true')
p.add_argument('--file')
p.add_argument('--destination',type=Path)
a=p.parse_args()
m=json.loads((Path(__file__).resolve().parent/'GITLAB_MATERIALS.json').read_text('utf-8'))
if a.list:
    for x in m['assets']: print(x['file'],x['bytes'],x['sha256'])
elif a.file and a.destination:
    x=next(v for v in m['assets'] if v['file']==a.file)
    a.destination.mkdir(parents=True,exist_ok=True)
    target=a.destination/x['file']
    if target.exists():
        if target.stat().st_size==x['bytes'] and hashlib.file_digest(target.open('rb'),'sha256').hexdigest()==x['sha256']:
            print('Already verified:',target);raise SystemExit(0)
        raise SystemExit('Refusing to replace existing file with different bytes')
    token=os.environ.get('HHC_GITLAB_TOKEN') or os.environ.get('GITLAB_TOKEN')
    headers={'PRIVATE-TOKEN':token} if token else {}
    req=urllib.request.Request(x['url'],headers=headers)
    partial=target.with_suffix(target.suffix+'.partial')
    digest=hashlib.sha256();size=0
    with urllib.request.urlopen(req,timeout=120) as response,partial.open('wb') as out:
        while block:=response.read(1024*1024):
            out.write(block);digest.update(block);size+=len(block)
    if size!=x['bytes'] or digest.hexdigest()!=x['sha256']:
        raise SystemExit('Downloaded bytes failed verification; .partial retained for diagnosis')
    partial.replace(target)
    print('SHA-256 verified:',target)
else:p.error('Use --list or --file NAME --destination DIRECTORY')
