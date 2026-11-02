"""Upload existing, user-authorized source bytes to the selected GitLab Generic Package Registry."""
from pathlib import Path
import hashlib, json, os, urllib.request, urllib.error

W=Path(__file__).resolve().parent.parent
plan=json.loads((W/'tmp/gitlab-upload-plan.json').read_text('utf-8'))
OUT=Path(plan['checkout'])
token=os.environ.get('HHC_GITLAB_TOKEN') or os.environ.get('GITLAB_TOKEN')
if not token and os.name=='nt':
    import winreg
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER,'Environment') as key:
            token=winreg.QueryValueEx(key,'HHC_GITLAB_TOKEN')[0]
    except FileNotFoundError:pass
if not token:raise SystemExit('HHC_GITLAB_TOKEN is missing; do not paste it into chat.')
API='https://gitlab.com/api/v4/projects/hung-group7524844%2Fhuyen-hoc-project'
headers={'PRIVATE-TOKEN':token}
def get(url):
    with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=120) as response:return json.load(response)
project=get(API)
assert project['path_with_namespace']=='hung-group7524844/huyen-hoc-project'
def remote_files():
    packages=get(API+'/packages?package_type=generic&package_name=hhc-materials&per_page=100')
    found={}
    for package in packages:
        if package['name']=='hhc-materials' and package['version']=='2026-11-02':
            page=1
            while True:
                rows=get(API+f"/packages/{package['id']}/package_files?per_page=100&page={page}")
                for row in rows:found[row['file_name']]=row
                if len(rows)<100:break
                page+=1
    return found
verified=[]
for asset in plan['assets']:
    path=Path(asset['local']);name=asset['file']
    assert path.stat().st_size==asset['bytes'],name
    assert hashlib.file_digest(path.open('rb'),'sha256').hexdigest()==asset['sha256'],name
    remote=remote_files().get(name)
    if remote:
        assert remote['size']==asset['bytes'] and remote['file_sha256']==asset['sha256'],'Remote name has different bytes: '+name
    else:
        print(json.dumps({'stage':'uploading','file':name,'bytes':asset['bytes']}),flush=True)
        with path.open('rb') as stream:
            req=urllib.request.Request(asset['url'],data=stream,method='PUT',headers={**headers,'Content-Type':'application/octet-stream','Content-Length':str(asset['bytes'])})
            with urllib.request.urlopen(req,timeout=1800) as response:response.read()
        remote=remote_files().get(name)
        assert remote and remote['size']==asset['bytes'] and remote['file_sha256']==asset['sha256'],'Server digest not confirmed: '+name
    verified.append({'file':name,'bytes':asset['bytes'],'sha256':asset['sha256'],'serverSha256Verified':True,'url':asset['url']})
    report={'date':'2026-11-02','project':plan['project'],'status':'upload-in-progress','assets':verified,'gitPushed':False,'binaryAssetsUploaded':len(verified)==len(plan['assets'])}
    (OUT/'PUBLICATION_STATUS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'stage':'server-digest-verified','file':name,'completed':len(verified),'total':len(plan['assets'])}),flush=True)
report['status']='all-material-assets-uploaded-and-server-sha256-verified'
(OUT/'PUBLICATION_STATUS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('All material assets uploaded and verified.',flush=True)
