from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,sys,subprocess
v=Path(__file__).resolve().parent.parent;w=v.parent;b=v/'research/tuvi-lower-contexts';q=v/'qa/tuvi-lower-contexts'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def digest(p):
 h=sha256()
 with p.open('rb')as stream:
  for block in iter(lambda:stream.read(4*1024*1024),b''):h.update(block)
 return h.hexdigest()
ids=read(b/'PROMOTION_IDENTITIES.json')['files']
for x in ids:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and digest(p)==x['sha256'],x['file']
a=read(b/'ACQUISITION.json');manifest=w/a['manifestFile'];assert digest(manifest)==a['manifestSHA256'];canvases=read(manifest)['sequences'][0]['canvases'];assert len(canvases)==137
assert len(a['records'])==67;positions=set()
for x in a['records']:
 p=b/x['file'];assert x['status']==200 and x['TLSCertificateValidationEnabled']
 assert p.stat().st_size==x['bytes']and digest(p)==x['sha256'];width=3000 if '3000'in x['file']else 2200
 assert x['url']==canvases[x['canvas']-1]['images'][0]['resource']['@id'].replace('/full/max/',f'/full/{width},/')
 with Image.open(p)as im:assert im.size==(x['actualWidth'],x['actualHeight'])and im.width==width and im.format=='JPEG'
 if width==2200:positions.add(x['canvas'])
assert positions==set(range(5,74))-{20,40,60}and len(positions)==66
r=read(b/'FIRST_PASS_READINGS.json')['records'];assert len(r)==66 and {x['canvas']for x in r}==positions and all(x['actuallyViewed']and not x['allRulesApplied']for x in r)
previous=read(v/'research/tuvi-lower-printed-cases/WORK_STATE.json');assert previous['newDistinctPositionsViewed']==12
prior={1,2,3,4,20,40,60,80,100,120,136,137};assert len(prior|positions)==78 and set(range(1,74))<=(prior|positions)
crops=read(b/'NATIVE_CROPS.json')['records'];assert len(crops)==9;accepted=0
for x in crops:
 source=w/x['sourceFile'];p=b/x['file'];assert digest(source)==x['sourceSHA256']and digest(p)==x['sha256']and p.stat().st_size==x['bytes'];assert x['actuallyViewed']and not x['resampled']
 with Image.open(source)as original,Image.open(p)as saved:
  native=original.crop(x['cropBox']).convert('RGB');assert native.size==saved.size==(x['width'],x['height']);assert ImageChops.difference(native,saved.convert('RGB')).getbbox()is None
 accepted+=bool(x['acceptedForLiteralProof'])
assert accepted==4
with Image.open(b/crops[0]['file'])as im:
 native=im.convert('RGB');tampered=native.copy();r,g,blue=tampered.getpixel((0,0));tampered.putpixel((0,0),(r^1,g,blue));assert ImageChops.difference(native,tampered).getbbox()is not None
f=read(b/'TRANSCRIPTION_FREEZE.json');assert f['beforeActualChartCalls']
for x in f['files']:assert digest(b/x['file'])==x['sha256']
source=read(b/'SOURCE_FLANKING_CLAUSE.json');assert source['sourceSHA256']==digest(b/source['sourceFile'])and source['orderedAssignmentForBothMonthsNotAsserted']
run=read(b/'ACTUAL_RUNTIME.json');assert run['actualHHCTuviCalls']==run['actualIztroNatalCalls']==3 and run['actualRuntimeBatchInvocations']==1 and run['engineSHA256']==digest(v/'engine.js')
probe=subprocess.run(['node',str(b/'test-reference.mjs'),'--no-write'],cwd=w,capture_output=True,text=True,encoding='utf-8');assert probe.returncode==0,probe.stderr
results=json.loads(probe.stdout);assert results==read(q/'RESULTS.json')and results['completeTests']==6 and results['testsInvokeCharts']==0
corr=read(b/'VOLUME_CORRECTION.json');assert corr['oldClaimRetracted']and corr['oldClaim']['runningTitle']=='卷之六'and corr['canvas60ReplacementLiteral']is None
assert read(w/corr['oldAuditPreserved'])['newDirectReadings'][2]['runningTitle']=='卷之六'
assert len(read(b/'CURRENT_UNITS.json')['units'])==19 and not read(b/'CURRENT_UNITS.json')['wholeWorkApplied']
assert len(read(b/'TIMING_CLAUSE.json')['normalizedWindows'])==4 and not run['consumerChanged']
html=(w/'Huyen_Hoc_Cac.html').read_bytes();assert html==(v/'Huyen_Hoc_Cac.html').read_bytes()==(v/'site/index.html').read_bytes();assert len(html)==707411 and sha256(html).hexdigest()=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857';assert sorted(x.name for x in(v/'site').iterdir())==['index.html']
for term in [b'tuvi-lower-contexts',b'inspectLeftRightFlanking',b'NAJ-4469314-juan5-left-right-flanking']:assert term not in html
output={'date':'2026-10-29','promotionIdentities':len(ids),'newHTTP200JPEGDerivativeBodies':67,'newDistinctPositionsRead':66,'lowerPositionsRetainedAndViewed':78,'remainingUnreadPositions':59,'nativeCropsRGBPixelMatched':9,'cropsAcceptedForLiteralProof':4,'cropsExcludedForLiteralProof':5,'RGBTamperPositiveControl':True,'source60VolumeClaimRetracted':True,'sectionDispositions':19,'wholeUnitsApplied':0,'completeRuntimeChecks':6,'geometricEdgeCases':108,'actualHHCTuviCalls':3,'actualIztroNatalCalls':3,'runtimeBatches':1,'testsRerunCharts':0,'newOriginalJP2Bodies':0,'newIndependentEditions':0,'consumerChanged':False,'wholeCatalogueCompleted':False}
payload=q/'SOURCE_RESULTS.json'
if '--no-write'in sys.argv:assert read(payload)==output
else:payload.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(output))
