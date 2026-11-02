from pathlib import Path
from hashlib import sha256
from PIL import Image
import json,subprocess,sys
v=Path(__file__).resolve().parent.parent;w=v.parent;r=v/'research/home-day-hour-scopes';q=v/'qa/home-day-hour-scopes';read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def digest(p):
 h=sha256()
 with p.open('rb')as f:
  for b in iter(lambda:f.read(4*1024*1024),b''):h.update(b)
 return h.hexdigest()
ids=read(r/'PROMOTION_IDENTITIES.json')
for x in ids['files']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and digest(p)==x['sha256'],x['file']
requests=read(r/'REQUESTS.json');assert len(requests)==17
for x in requests:
 p=r/x['file'];assert x['status']==200 and x['standardTLSValidation'];assert p.stat().st_size==x['bytes']and digest(p)==x['sha256'];assert x['url'].startswith('https://db.itkc.or.kr/')
positions=[247,248,249,250,251,252,253,255,256]
for n in positions:
 im=Image.open(r/f'ITKC_BT_1508A_V002_{n}.JPG');assert im.format=='JPEG'and im.size==(1640,2180)
for file,idx,img,end in [('itkc-day-image-node-pwsh.json',230,247,253),('itkc-hour-image-node.json',238,255,256)]:
 n=read(r/file);assert int(n['imginfo']['imgCur'])==idx and n['imginfo']['imgFile']==f'ITKC_BT_1508A_V002_{img}';assert n['rellist']['이미지']['연계종료']==f'ITKC_BT_1508A_V002_{end}'
for kind,indices in [('day',range(231,237)),('hour',[239])]:
 for idx in indices:
  n=read(r/f'itkc-{kind}-image-index-{idx}.json');assert int(n['imginfo']['imgCur'])==idx and n['imginfo']['imgFile']==f'ITKC_BT_1508A_V002_{idx+17}'
native=read(r/'NATIVE_CROPS_REVISED.json');assert len(native['records'])==8 and native['allFinalCropsViewed']and native['excludedInitialCrops']==9 and native['postFreezeMarginCorrectionCount']==1
for x in native['records']:
 s=r/Path(x['source']['file']).name;p=r/Path(x['crop']['file']).name;assert digest(s)==x['source']['sha256']and digest(p)==x['crop']['sha256'];assert x['viewed']and x['accepted'];a=Image.open(s).crop(x['boxXYXY']).convert('RGB');b=Image.open(p).convert('RGB');assert a.size==b.size and a.tobytes()==b.tobytes();t=b.copy();c=t.getpixel((0,0));t.putpixel((0,0),((c[0]+1)%256,c[1],c[2]));assert a.tobytes()!=t.tobytes()
margin=read(r/'CROP_MARGIN_CORRECTION.json');assert margin['detectedAfterInitialPassingTests']and not margin['consumerAffected']and margin['newEngineCalls']==0;assert digest(r/Path(margin['oldCrop']['file']).name)==margin['oldCrop']['sha256']
for x in read(r/'SOURCE_IDENTITIES.json')['retainedFiles']+read(r/'FUNCTION_REUSE_AUDIT.json')['retainedModules']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and digest(p)==x['sha256']
assert digest(r/'ITKC_BT_1508A_V002_247.JPG')==digest(v/'research/home-time-premises/ITKC_BT_1508A_V002_247.JPG')
assert read(r/'LOCAL_INVOCATION_FAILURE.json')['HTTPResponseRetainedForFailure']is False
res=subprocess.run(['node',str(r/'test-reference.mjs'),'--no-write'],cwd=w,capture_output=True,text=True,encoding='utf-8');assert res.returncode==0,res.stdout+res.stderr;summary=read(r/'REFERENCE_RESULTS.json')['summary'];assert json.loads(res.stdout)==summary
contexts=read(r/'CONTEXT_DISPOSITIONS.json');assert len(contexts['records'])==22 and all(not x['wholeClauseApplied']for x in contexts['records']);assert contexts['dailyHeadings']==18 and contexts['hourHeadings']==4
reading=read(r/'READING_AUDIT.json');assert len(reading['positions'])==9 and reading['newPositionsActuallyViewed']==8 and reading['reusedPositionsReexamined']==1
runtime=read(r/'RETAINED_SCOPE_EXECUTIONS.json');assert runtime['actualRetainedAPICalls']==15 and runtime['newCalendarEngineCalls']==0
lib=read(v/'research/library-current/COVERAGE.json');assert lib['counts']['catalogueRecords']==40 and lib['counts']['moduleSourceRecords']==16 and lib['counts']['wholeWorkApplied']==0;p08=next(x for x in lib['catalogue']if x['id']=='P08');assert p08['latestDayHourClauseCounts']['selectedPrivateFunctions']==2 and not p08['wholeWorkApplied']
html=(v/'Huyen_Hoc_Cac.html').read_bytes();assert len(html)==707411 and sha256(html).hexdigest()=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857';assert html==(w/'Huyen_Hoc_Cac.html').read_bytes()==(v/'site/index.html').read_bytes();assert sorted(p.name for p in(v/'site').iterdir())==['index.html'];assert b'ITKC-GO1508A.'not in html
out={'date':'2026-10-29','promotionIdentities':len(ids['files']),'HTTP200BodiesWithTLS':17,'newRelatedSourceImagePositions':8,'reusedSourcePosition':247,'newIndependentP08Editions':0,'newOriginalMasterContainers':0,'nativeCropsRGBMatched':8,'excludedTrialCrops':9,'onePostFreezeCropMarginRefined':True,'manualCasesChangedAfterFreeze':0,'RGBTamperPositiveControl':True,'firstPassDayAndHourSectionDispositions':22,'selectedPrivateFunctions':2,'selectedDayPatterns':2,**summary,'actualRetainedP08APICalls':15,'actualNewLunarObjects':0,'newHHCCharts':0,'newIztroCharts':0,'sourceCalendarAdapterImplemented':False,'combinedHourPriorityResolved':False,'sourceTimezoneAssigned':False,'wholeCatalogueCompleted':False}
if '--no-write'not in sys.argv:(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
else:assert read(q/'SOURCE_RESULTS.json')==out
print(json.dumps(out))
