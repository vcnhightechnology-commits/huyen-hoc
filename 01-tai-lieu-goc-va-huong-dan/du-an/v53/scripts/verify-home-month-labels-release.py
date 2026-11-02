from pathlib import Path
from hashlib import sha256
import json,subprocess,zipfile,sys
v=Path(__file__).resolve().parent.parent;w=v.parent;q=v/'qa/home-month-labels';r=v/'research/home-month-labels';read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));prepare='--prepare'in sys.argv
def digest(p):
 h=sha256()
 with p.open('rb')as f:
  for b in iter(lambda:f.read(4*1024*1024),b''):h.update(b)
 return h.hexdigest()
for x in read(q/'PROMOTION_IDENTITIES.json')['byteExactFiles']:
 p=w/x['target'];assert p.stat().st_size==x['bytes']and digest(p)==x['sha256'],x['target']
tests=json.loads(subprocess.run(['node',str(r/'test-labels.mjs')],check=True,capture_output=True,text=True,encoding='utf-8').stdout);assert tests==read(q/'TEST_RESULTS.json')and tests['readableCellLabels']==500 and tests['unresolvedCellLabels']==220
assert read(q/'SOURCE_RESULTS.json')['nativeCropsRGBMatched']==11
a=w/'archives/v53-before-home-month-labels';snap=read(a/'SNAPSHOT.json');assert snap['sourceManifestFiles']==5863
for x in snap['files']:assert(a/x['file']).stat().st_size==x['bytes']and digest(a/x['file'])==x['sha256']
allowed={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'}
for x in read(a/'PACKAGE_MANIFEST.json')['files']:
 if x['file']not in allowed:assert(v/x['file']).stat().st_size==x['bytes']and digest(v/x['file'])==x['sha256'],x['file']
assert(w/'EXHAUSTIVE_WORK_STATE.json').read_bytes()==(v/'research/EXHAUSTIVE_WORK_STATE.json').read_bytes()
assert digest(w/'Huyen_Hoc_Cac_V53_web.zip')==digest(a/'Huyen_Hoc_Cac_V53_web.zip')
html=(v/'Huyen_Hoc_Cac.html').read_bytes();assert html==(w/'Huyen_Hoc_Cac.html').read_bytes()==(v/'site/index.html').read_bytes();assert sha256(html).hexdigest()=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
files=[p for p in v.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json'];payload=q/'RELEASE_RESULTS.json'
if prepare:count=len(files)+(not payload.exists())
else:
 m=read(v/'PACKAGE_MANIFEST.json');count=len(m['files']);assert{p.relative_to(v).as_posix()for p in files}=={x['file']for x in m['files']}
 with zipfile.ZipFile(w/'Huyen_Hoc_Cac_V53_source.zip')as z:
  assert set(z.namelist())=={'v53/'+x['file']for x in m['files']}|{'v53/PACKAGE_MANIFEST.json'};assert z.read('v53/PACKAGE_MANIFEST.json')==(v/'PACKAGE_MANIFEST.json').read_bytes()
  for x in m['files']:
   p=v/x['file'];assert p.stat().st_size==x['bytes']and digest(p)==x['sha256'],x['file'];h=sha256();size=0
   with z.open('v53/'+x['file'])as f:
    for b in iter(lambda:f.read(4*1024*1024),b''):h.update(b);size+=len(b)
   assert size==x['bytes']and h.hexdigest()==x['sha256'],x['file']
out={'date':'2026-10-29','sourceChecks':read(q/'SOURCE_RESULTS.json'),'referenceTests':tests,'oldV53FilesUnchanged':5858,'manifestFiles':count,'sourceZIPEntries':count+1,'wholeCatalogueCompleted':False,'consumerChanged':False,'newEngineCallsDuringVerification':0}
if prepare:payload.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'prepared':True,'manifestFiles':count}))
else:assert read(payload)==out;print(json.dumps({'finalReadOnlyVerificationPassed':True,**out}))
