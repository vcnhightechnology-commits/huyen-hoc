from pathlib import Path
from hashlib import sha256
import json,zipfile,sys,runpy,contextlib,io
v=Path(__file__).resolve().parent.parent;w=v.parent;q=v/'qa/home-month-witness';read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));prepare='--prepare'in sys.argv;assert prepare or '--no-write'in sys.argv

def digest(p):
 h=sha256()
 with p.open('rb')as stream:
  for block in iter(lambda:stream.read(4*1024*1024),b''):h.update(block)
 return h.hexdigest()
args=sys.argv[:]
try:
 sys.argv=['verify-home-month-witness-sources.py','--no-write']
 with contextlib.redirect_stdout(io.StringIO()):runpy.run_path(str(v/'scripts/verify-home-month-witness-sources.py'))
finally:sys.argv=args
source=read(q/'SOURCE_RESULTS.json');a=w/'archives/v53-before-home-month-witness';snap=read(a/'SNAPSHOT.json');assert snap['sourceManifestFiles']==5410 and snap['sourceZIPBytes']==2882810993
for x in snap['files']:assert (a/x['file']).stat().st_size==x['bytes']and digest(a/x['file'])==x['sha256']
allowed={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'};unchanged=0
for x in read(a/'PACKAGE_MANIFEST.json')['files']:
 if x['file']in allowed:continue
 p=v/x['file'];assert p.stat().st_size==x['bytes']and digest(p)==x['sha256'],x['file'];unchanged+=1
assert unchanged==5405
assert (w/'EXHAUSTIVE_WORK_STATE.json').read_bytes()==(v/'research/EXHAUSTIVE_WORK_STATE.json').read_bytes();coverage=read(v/'research/library-current/COVERAGE.json');assert coverage['counts']['wholeWorkApplied']==0
assert next(x for x in coverage['catalogue']if x['id']=='T01')['lowerItemCounts']['positionsRetainedAndViewed']==137
assert not read(v/'research/bazi-jianlu-context/CANDIDATE_STATUS.json')['browserTestsPassed']
html=(v/'Huyen_Hoc_Cac.html').read_bytes();h=sha256(html).hexdigest();assert len(html)==707411 and h=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857';assert html==(w/'Huyen_Hoc_Cac.html').read_bytes()==(v/'site/index.html').read_bytes();assert sorted(p.name for p in(v/'site').iterdir())==['index.html']
web=w/'Huyen_Hoc_Cac_V53_web.zip';assert digest(web)==digest(a/web.name)
with zipfile.ZipFile(web)as z:assert sorted(z.namelist())==['HUONG_DAN.md','index.html']and z.read('index.html')==html
payload=q/'RELEASE_RESULTS.json';files=[p for p in v.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json']
if prepare:count=len(files)+(0 if payload.exists()else 1)
else:
 m=read(v/'PACKAGE_MANIFEST.json');assert {p.relative_to(v).as_posix()for p in files}=={x['file']for x in m['files']};assert m['product']['sha256']==h
 for x in m['files']:
  p=v/x['file'];assert p.stat().st_size==x['bytes']and digest(p)==x['sha256'],x['file']
 with zipfile.ZipFile(w/'Huyen_Hoc_Cac_V53_source.zip')as z:
  assert set(z.namelist())=={'v53/'+x['file']for x in m['files']}|{'v53/PACKAGE_MANIFEST.json'};assert z.read('v53/PACKAGE_MANIFEST.json')==(v/'PACKAGE_MANIFEST.json').read_bytes()
  for x in m['files']:
   data=z.read('v53/'+x['file']);assert len(data)==x['bytes']and sha256(data).hexdigest()==x['sha256'],x['file']
 count=len(m['files'])
out={'date':'2026-10-29','sourceVerification':source,'consumerChanged':False,'wholeCatalogueCompleted':False,'htmlBytes':len(html),'htmlSHA256':h,'siteClean':True,'webZIPUnchanged':True,'previousSourceZIPPreservedBytes':2882810993,'unchangedEarlierV53Files':unchanged,'manifestFilesVerified':count,'sourceZIPFilesVerified':count+1}
if prepare:payload.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'preparedExpectedPayload':True,'manifestFilesAfterPackage':count,'requiresFinalNoWriteVerification':True}))
else:assert read(payload)==out;print(json.dumps({'finalReadOnlyVerificationPassed':True,'sourceZIPBytes':(w/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size,**out}))
