"""Build the one latest comprehensive source package; no full archive snapshots."""
from pathlib import Path
from hashlib import sha256
import json,zipfile,os,sys

W=Path(__file__).resolve().parent.parent;R=W/'recovery/storage-consolidation'
target=W/'Huyen_Hoc_Cac_V53_source.zip';pending=W/'Huyen_Hoc_Cac_V53_source.pending.zip'
assert not pending.exists(),'A pending package exists; inspect before retry.'
assert '--verified-consolidation'in sys.argv,'Run consolidation verification before replacing the current ZIP.'
state=json.loads((R/'COLLECTION_STATE.json').read_text(encoding='utf-8-sig'))
assert state['status']=='all-retained-content-sha256-verified'
excluded={'.git','archives','v47','v48','v49','v50','v51','v52'}
# Preserve historical tmp evidence in the package; skip only duplicate release-transfer/check bundles and the downloaded CLI.
temporary_transfer_dirs={'materials-handoff','materials-remote-check','materials-http-check','materials-local-check','materials-range-check','github-tools'}
files=[]
for root,dirs,names in os.walk(W):
 base=Path(root);relative=base.relative_to(W)
 dirs[:]=[name for name in dirs if name not in excluded and name!='__pycache__']
 if relative==Path('tmp'):dirs[:]=[name for name in dirs if name not in temporary_transfer_dirs]
 for name in names:
  p=base/name;parts=p.relative_to(W).parts
  if len(parts)==1 and p.suffix=='.zip':continue
  if p.suffix=='.pyc':continue
  if p.name.endswith(('.sqlite-journal','.sqlite-wal','.sqlite-shm')):continue
  if p in {R/'MAINTENANCE.json',R/'LATEST_PACKAGE_MANIFEST.json',R/'COMPLETION_RESULT.json'}:continue
  if p==W/'recovery/research-release/FINAL_VERIFICATION.json':continue
  if p.name=='incoming-content.tmp':continue
  files.append(p)
print(json.dumps({'stage':'building-single-latest-source-package','files':len(files)}),flush=True)
manifest=[]
with zipfile.ZipFile(pending,'x',zipfile.ZIP_DEFLATED,compresslevel=1,allowZip64=True)as z:
 for i,p in enumerate(sorted(files),1):
  before=p.stat();h=sha256();size=0
  info=zipfile.ZipInfo.from_file(p,p.relative_to(W).as_posix());info.compress_type=zipfile.ZIP_DEFLATED;info._compresslevel=1
  with p.open('rb')as src,z.open(info,'w',force_zip64=True)as dst:
   for block in iter(lambda:src.read(8*1024*1024),b''):dst.write(block);h.update(block);size+=len(block)
  after=p.stat();assert before.st_size==size==after.st_size and before.st_mtime_ns==after.st_mtime_ns,p
  manifest.append({'file':p.relative_to(W).as_posix(),'bytes':size,'sha256':h.hexdigest()})
  if i%2000==0:print(json.dumps({'stage':'source-package-written','files':i}),flush=True)
with zipfile.ZipFile(pending)as z:
 assert set(z.namelist())=={p.relative_to(W).as_posix()for p in files}
 assert z.read('v53/Huyen_Hoc_Cac.html')==(W/'Huyen_Hoc_Cac.html').read_bytes()
 assert z.read('recovery/consolidated-history/INDEX.sqlite')==(W/'recovery/consolidated-history/INDEX.sqlite').read_bytes()
expected={x['file']:x for x in manifest}
with zipfile.ZipFile(pending)as z:
 for checked,info in enumerate(z.infolist(),1):
  h=sha256();size=0
  with z.open(info)as f:
   for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b);size+=len(b)
  assert expected[info.filename]['bytes']==size and expected[info.filename]['sha256']==h.hexdigest(),info.filename
  if checked%2000==0:print(json.dumps({'stage':'source-package-members-verified','files':checked}),flush=True)
os.replace(pending,target)
out={'status':'latest-source-package-member-sha256-verified','files':manifest,'sourceZIPBytes':target.stat().st_size,'policy':'Single comprehensive latest package replaces old whole-ZIP snapshots. Historical unique bytes are retained once and mapped by consolidated-history/INDEX.sqlite.'}
(R/'LATEST_PACKAGE_MANIFEST.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'stage':'single-latest-source-package-verified','files':len(files),'sourceZIPBytes':target.stat().st_size}),flush=True)
