from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,sys
r=Path(__file__).resolve().parents[1];w=r.parent;b=r/'research/home-xuankong-lines';q=r/'qa/home-xuankong-lines'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda p:sha256(p.read_bytes()).hexdigest()
ident=read(b/'PROMOTION_IDENTITIES.json');assert len(ident['records'])==16
for x in ident['records']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'],x['file']
text=(b/'STAGED_test-room-lines.mjs').read_text(encoding='utf-8')
for old,new in [
 ("from './source-room-lines.mjs'","from '../research/home-xuankong-lines/source-room-lines.mjs'"),
 ("const b=import.meta.dirname,w=resolve(b,'../..'),ctx={};","const b=resolve(import.meta.dirname,'../research/home-xuankong-lines'),w=resolve(b,'../../..'),ctx={};"),
 ("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/home-xuankong-lines/REFERENCE_RESULTS.json')")]:
 assert text.count(old)==1;text=text.replace(old,new)
assert text==(r/'scripts/test-home-xuankong-lines.mjs').read_text(encoding='utf-8')
source=read(b/'SOURCE_DISPOSITIONS.json');p=w/source['sourcePDF']['file']
assert p.stat().st_size==source['sourcePDF']['bytes']==151275796
assert sha(p)==source['sourcePDF']['sha256']=='b6394102a995bb66df173452b37614b29d58e34ff85e08c43077006572ac48a5'
assert [x['sourcePDFPage']for x in source['sourceRawImages']]==[94,95]
for x in source['sourceRawImages']:assert sha(w/x['file'])==x['sha256']and x['expandedActuallyViewed']and not x['newReadPosition']
qa=read(q/'QA_IMAGES.json');assert len(qa['records'])==4
for x in qa['records']:
 assert x['actuallyViewed']and not x['resampled']and sha(w/x['sourceFile'])==x['sourceSHA256']and sha(q/x['file'])==x['sha256']
 assert ImageChops.difference(Image.open(w/x['sourceFile']).convert('RGB').crop(x['cropBox']),Image.open(q/x['file']).convert('RGB')).getbbox()is None
manual=read(b/'MANUAL_READINGS.json');assert len(manual['records'])==7
assert {x['id']for x in manual['records']}=={'carry-pair','first-room','fixed-gate','room-sides','five-units','old-new-unit','poem-flip'}
assert not manual['wholeExchangeMethodApplied']and not manual['sourcePhysicalPlanInferenceValidated']
related=read(b/'RELATED_CONTEXT.json');assert sha(w/related['file'])==related['sha256']and related['text']==(w/related['file']).read_text(encoding='utf-8-sig')
res=read(q/'REFERENCE_RESULTS.json');assert len(res['checks'])==7 and all(x['ok']for x in res['checks'])
assert len(res['coordinates'])==64 and len({x['bitsBottomToTop']for x in res['coordinates']})==64
assert {x['actualHHCHexagramNumber']for x in res['coordinates']}==set(range(1,65))
assert all(not x['sourceHouseInterpretationValidated']for x in res['coordinates'])
for bits,num in [('111111',1),('000000',2),('101010',63),('010101',64)]:assert next(x for x in res['coordinates']if x['bitsBottomToTop']==bits)['actualHHCHexagramNumber']==num
assert sha(w/res['actualEngine']['file'])==res['actualEngine']['sha256']=='39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6'
assert source['runtimeRuns']==1 and source['actualHHCHexNumberCalls']==64
assert not source['gateComplementResolved']and not source['lessThanFiveRoomCarryInsertionPhaseImplemented']
assert not source['repeatedPhysicalRoomRepairCountingResolved']and not source['modernPlanAdapterEstablished']
state=read(b/'WORK_STATE.json');assert not state['wholeCatalogueCompleted']and not state['fullXuanKongExchangeMethodApplied']
out=dict(date='2026-10-28',promotionIdentities=16,completeRuntimeChecks=7,expandedRetainedSourcePositions=[94,95],
 nativeCropsViewedPixelMatched=4,selectedSourceReadings=7,sourcePrintedRelocationExamples=2,
 actualHHCHexNumberCalls=64,uniqueHexNumbersMatched=64,orientationAnchors=['111111=1','000000=2','101010=63','010101=64'],
 orderedLastFiveToUpperLinesIsDeclaredEditorialModel=True,gateComplementResolved=False,
 initialLessThanFiveRoomPhaseImplemented=False,repeatedPhysicalRepairCountingEstablished=False,
 modernMeasuredPlanAdapterImplemented=False,fullSourceExchangeApplied=False,
 newHTTPBodies=0,newContainers=0,newReadSourcePositions=0,newCalendarChartCalls=0,
 consumerChanged=False,wholeCatalogueCompleted=False)
p=q/'SOURCE_RESULTS.json'
if '--no-write'in sys.argv:assert read(p)==out
else:p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
