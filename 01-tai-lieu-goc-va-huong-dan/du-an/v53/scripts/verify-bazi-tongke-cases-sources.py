from pathlib import Path
from hashlib import sha256
from PIL import Image
import json,subprocess,sys
v=Path(__file__).resolve().parent.parent;w=v.parent;r=v/'research/bazi-tongke-cases';q=v/'qa/bazi-tongke-cases';read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def digest(p):
 h=sha256()
 with p.open('rb')as stream:
  for block in iter(lambda:stream.read(4*1024*1024),b''):h.update(block)
 return h.hexdigest()
ids=read(r/'PROMOTION_IDENTITIES.json');assert len(ids['files'])==15
for x in ids['files']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and digest(p)==x['sha256'],x['file']
assert ids['excludedTrialCropCount']==3 and not ids['trialCropsPromoted']
for x in read(r/'SOURCE_IDENTITIES.json')['files']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and digest(p)==x['sha256'],x['file']
assert digest(v/'research/bazi-pattern-witness/CADAL06066041.djvu')=='013ce4861680a2bf08b811050c45a45bb2d3ce9d164f7e2341d7070bd5cb2c1a'
native=read(r/'NATIVE_CROPS.json');assert len(native['records'])==3 and native['allRecordsViewed']
for x in native['records']:
 p=w/x['source']['file'];crop=r/Path(x['crop']['file']).name;im=Image.open(p);assert list(im.size)==x['sourceSize'];a=im.crop(x['boxXYXY']).convert('RGB');b=Image.open(crop).convert('RGB');assert a.size==b.size and a.tobytes()==b.tobytes();assert x['viewed']and x['accepted']
 tamper=b.copy();rgb=tamper.getpixel((0,0));tamper.putpixel((0,0),((rgb[0]+1)%256,rgb[1],rgb[2]));assert a.tobytes()!=tamper.tobytes()
res=subprocess.run(['node',str(r/'test-evidence.mjs'),'--no-write'],cwd=w,capture_output=True,text=True,encoding='utf-8');assert res.returncode==0,res.stdout+res.stderr;actual=json.loads(res.stdout);assert actual==read(r/'TEST_RESULTS.json')['summary']
freeze=read(r/'TRANSCRIPTION_FREEZE.json');assert freeze['beforeFirstActualBatch']and freeze['allManualExpectedCasesFrozen'];a=read(r/'ACTUAL_RUNTIME.json');assert digest(r/'TRANSCRIPTION_FREEZE.json')==a['freezeSHA256']
c=read(r/'CURRENT_CONTEXT_COVERAGE.json');s=c['summary'];assert s['totalContexts']==90 and s['parentsWithSelectedModuleOrDeclaredPremiseLinks']==43 and s['otherParentsWithoutSuchLinks']==47 and s['wholeParentsApplied']==0
c03=next(x for x in c['records']if x['id']=='FOOD-05-C03');assert c03['selectedModuleLinks']==[]and c03['printedCaseRoleAudit']['cases']==3 and not c03['printedCaseRoleAudit']['functionalRuleLinked']
lib=read(v/'research/library-current/COVERAGE.json');m=next(x for x in lib['catalogue']if x['id']=='M01');assert m['foodParentContextSelection']['currentMatrix']=='v53/research/bazi-tongke-cases/CURRENT_CONTEXT_COVERAGE.json';assert lib['counts']['wholeWorkApplied']==0
html=(v/'site/index.html').read_bytes();assert len(html)==707411 and sha256(html).hexdigest()=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857';assert sorted(p.name for p in(v/'site').iterdir())==['index.html']
assert digest(v/'content.js')=='c4f9c12dd2fdc703909dc9ab98e26c718f11af18f5fbba3e5c4dce88f58911a1'
out={'date':'2026-10-29','promotionIdentities':15,'sourcePositionsExpanded':2,'newSourcePositions':0,'newHTTPRequests':0,'newOriginalContainers':0,'newIndependentWitnesses':0,'nativeCropsRGBMatched':3,'trialCropsExcluded':3,'RGBTamperPositiveControl':True,'completeChecks':6,'printedCases':3,'directedRoleFrames':36,'distinctStemPairs':23,'actualDirectHHCGodCalls':36,'actualLunarTenGodTableQueries':36,'actualHHCInspectCalls':3,'runtimeBatches':1,'newEngineCallsFromReplay':0,'actualNatalCharts':0,'actualIztroCharts':0,'blindDaySubstitutionChanges':2,'reversedCandidatePairsNotMatched':3,'newReferenceAPIs':0,'parentPartialLinks':43,'parentNoRuleLinks':47,'wholeParentsApplied':0,'newPrintedCaseAuditParentsNotCountedAsApplied':1,'consumerChanged':False,'wholeCatalogueCompleted':False}
if '--no-write'not in sys.argv:(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
else:assert read(q/'SOURCE_RESULTS.json')==out
print(json.dumps(out))
