from pathlib import Path
from hashlib import sha256
import json,zipfile,sys,runpy,contextlib,io
r=Path(__file__).resolve().parent.parent;w=r.parent;q=r/'qa/home-yangzhai-fuyuan'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda data:sha256(data).hexdigest()
prepare='--prepare'in sys.argv;assert prepare or '--no-write'in sys.argv
def filehash(p):
 h=sha256()
 with p.open('rb')as stream:
  for block in iter(lambda:stream.read(4*1024*1024),b''):h.update(block)
 return h.hexdigest()
args=sys.argv[:]
try:
 sys.argv=['verify-home-fuyuan-younian-sources.py','--no-write']
 with contextlib.redirect_stdout(io.StringIO()):runpy.run_path(str(r/'scripts/verify-home-fuyuan-younian-sources.py'))
finally:sys.argv=args
source=read(q/'SOURCE_RESULTS.json');assert source['completeChecks']==8 and source['promotionIdentities']==79
a=w/'archives/v53-before-home-yangzhai-fuyuan';snap=read(a/'SNAPSHOT.json')
assert snap['sourceManifestFiles']==4074 and snap['sourceZIPBytes']==2340565337
for x in snap['files']:assert (a/x['file']).stat().st_size==x['bytes'] and filehash(a/x['file'])==x['sha256']
allowed={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json',
 'research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'}
unchanged=0
for x in read(a/'PACKAGE_MANIFEST.json')['files']:
 if x['file']in allowed:continue
 p=r/x['file'];assert p.stat().st_size==x['bytes']and filehash(p)==x['sha256'],x['file'];unchanged+=1
assert unchanged==4069
assert (w/'EXHAUSTIVE_WORK_STATE.json').read_bytes()==(r/'research/EXHAUSTIVE_WORK_STATE.json').read_bytes()
assert read(r/'research/library-current/COVERAGE.json')['counts']['wholeWorkApplied']==0
assert not read(r/'research/bazi-jianlu-context/CANDIDATE_STATUS.json')['browserTestsPassed']
html=(r/'Huyen_Hoc_Cac.html').read_bytes()
assert len(html)==707411 and sha(html)=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html==(w/'Huyen_Hoc_Cac.html').read_bytes()==(r/'site/index.html').read_bytes()
assert sorted(p.name for p in(r/'site').iterdir())==['index.html']
for term in [b'home-yangzhai-fuyuan',b'sourceFuyuan',b'YZSS-Tianyige-fuyuan-dayounian']:assert term not in html
web=w/'Huyen_Hoc_Cac_V53_web.zip';assert filehash(web)==filehash(a/web.name)
with zipfile.ZipFile(web)as z:assert sorted(z.namelist())==['HUONG_DAN.md','index.html']and z.read('index.html')==html
payload=q/'RELEASE_RESULTS.json';files=[p for p in r.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json']
if prepare:count=len(files)+(0 if payload.exists()else 1)
else:
 m=read(r/'PACKAGE_MANIFEST.json');assert {p.relative_to(r).as_posix()for p in files}=={x['file']for x in m['files']}
 assert m['product']['sha256']==sha(html)
 for x in m['files']:
  p=r/x['file'];assert p.stat().st_size==x['bytes']and filehash(p)==x['sha256'],x['file']
 with zipfile.ZipFile(w/'Huyen_Hoc_Cac_V53_source.zip')as z:
  assert set(z.namelist())=={'v53/'+x['file']for x in m['files']}|{'v53/PACKAGE_MANIFEST.json'}
  assert z.read('v53/PACKAGE_MANIFEST.json')==(r/'PACKAGE_MANIFEST.json').read_bytes()
  for x in m['files']:
   data=z.read('v53/'+x['file']);assert len(data)==x['bytes']and sha(data)==x['sha256'],x['file']
 count=len(m['files'])
out={'date':'2026-10-28','sourceVerification':source,'sourcePassingChecks':8,'rawSourceImagesViewed':48,
 'newSourceReadPositions':47,'manualYearRows':180,'manualSexSpecificCells':360,'centralAnnotations':40,
 'derivedCompassCells':64,'finalRunHHCDirections':360,'finalRunLunarYearObjects':180,
 'runtimeFailureAndRepeatAuditRetained':True,'birthDateBoundaryEstablished':False,'modernRoomGeometryAdapter':False,
 'sourceOutcomesValidated':False,'wholeCatalogueCompleted':False,'consumerChanged':False,
 'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,
 'previousSourceZIPPreservedBytes':2340565337,'unchangedEarlierV53Files':unchanged,
 'manifestFilesVerified':count,'sourceZIPFilesVerified':count+1}
if prepare:payload.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'preparedExpectedPayload':True,'manifestFilesAfterPackage':count,'requiresFinalNoWriteVerification':True}))
else:assert read(payload)==out;print(json.dumps({'finalReadOnlyVerificationPassed':True,'sourceZIPBytes':(w/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size,**out},ensure_ascii=False))
