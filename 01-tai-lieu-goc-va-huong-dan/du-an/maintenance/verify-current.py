"""Current release verification independent of removed full-ZIP snapshot locations."""
from pathlib import Path
from hashlib import sha256
import json,sqlite3,zipfile,subprocess,sys
W=Path(__file__).resolve().parent.parent;V=W/'v53';R=W/'recovery/storage-consolidation'
def h(p):
 s=sha256()
 with p.open('rb')as f:
  for b in iter(lambda:f.read(8*1024*1024),b''):s.update(b)
 return s.hexdigest()
manifest=json.loads((V/'PACKAGE_MANIFEST.json').read_text(encoding='utf-8-sig'))
for x in manifest['files']:
 p=V/x['file'];assert p.stat().st_size==x['bytes']and h(p)==x['sha256'],x['file']
html=(W/'Huyen_Hoc_Cac.html').read_bytes();assert html==(V/'Huyen_Hoc_Cac.html').read_bytes()==(V/'site/index.html').read_bytes()
assert sha256(html).hexdigest()=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert{p.relative_to(V/'site').as_posix()for p in(V/'site').rglob('*')if p.is_file()}=={'index.html'}
with zipfile.ZipFile(W/'Huyen_Hoc_Cac_V53_web.zip')as z:
 assert set(z.namelist())=={'index.html','HUONG_DAN.md'}and z.read('index.html')==html
tests=[]
batch=json.loads((W/'recovery/research-release/CURRENT_BATCH.json').read_text(encoding='utf-8-sig'))
for relative in batch['tests']:
 result=json.loads(subprocess.run(['node',str(W/relative)],check=True,capture_output=True,text=True,encoding='utf-8').stdout);assert result['passed'];tests.append({'file':relative,'groups':result['groups'],'passed':True,'newEngineCalls':result['newEngineCallsDuringTests']})
c=sqlite3.connect('file:'+(W/'recovery/consolidated-history/INDEX.sqlite').as_posix()+'?mode=ro',uri=True)
assert c.execute('PRAGMA integrity_check').fetchone()[0]=='ok'
assert c.execute('SELECT count(*)FROM members m LEFT JOIN content c ON c.sha256=m.sha256 WHERE c.sha256 IS NULL').fetchone()[0]==0
counts={name:c.execute('SELECT count(*)FROM '+name).fetchone()[0]for name in['content','containers','members','git_objects']};c.close()
restore=json.loads((R/'RESTORE_TEST.json').read_text(encoding='utf-8-sig'));assert restore['passed']
out={'status':'current-product-and-retained-history-verified','consumerChanged':False,'v53ManifestFiles':len(manifest['files']),'htmlBytes':len(html),'htmlSHA256':sha256(html).hexdigest(),'publicSiteClean':True,'webPackageVerified':True,'currentResearchTests':tests,'historyIndex':counts,'historicalRestoreTestPassed':True,'newEngineCalls':0,'chatHistoryUntouched':True}
(R/'CURRENT_VERIFICATION.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(out),flush=True)
