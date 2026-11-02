from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,sys
r=Path(__file__).resolve().parents[1];w=r.parent;b=r/'research/home-month-gods';q=r/'qa/home-month-gods';read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
ident=read(b/'PROMOTION_IDENTITIES.json');assert len(ident['records'])==29
for x in ident['records']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'],x['file']
s=(b/'STAGED_test-month-gods.mjs').read_text(encoding='utf-8-sig')
for old,new in [("from'./source-month-gods.mjs'","from'../research/home-month-gods/source-month-gods.mjs'"),("const b=resolve(import.meta.dirname),w=resolve(b,'../..'),","const b=resolve(import.meta.dirname,'../research/home-month-gods'),w=resolve(b,'../../..'),"),("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/home-month-gods/REFERENCE_RESULTS.json')")]:assert s.count(old)==1;s=s.replace(old,new)
assert s==(r/'scripts/test-home-month-gods.mjs').read_text(encoding='utf-8')
source=read(b/'SOURCE_DISPOSITIONS.json');p=w/source['sourcePDF']['file'];assert p.stat().st_size==source['sourcePDF']['bytes']==151275796 and sha(p)==source['sourcePDF']['sha256']=='b6394102a995bb66df173452b37614b29d58e34ff85e08c43077006572ac48a5'
assert len(source['sourceRawImages'])==8
for x in source['sourceRawImages']:assert sha(w/x['file'])==x['sha256']and (w/x['file']).stat().st_size==x['bytes']and x['expandedActuallyViewed']and not x['newReadPosition']
qa=read(b/'QA_IMAGES.json');assert len(qa['records'])==13 and sum(bool(x.get('excludedFromLeftTableMonthLabelEvidence'))for x in qa['records'])==1
for x in qa['records']:
 assert x['actuallyViewed']and x['pixelMatch']and not x['resampled']and sha(b/x['file'])==x['sha256'];assert ImageChops.difference(Image.open(w/x['sourceFile']).convert('RGB').crop(x['cropBox']),Image.open(b/x['file']).convert('RGB')).getbbox()is None
native=read(q/'NATIVE_RESULTS.json');assert native['rawDCTImagesByteIdenticalToPDF']==8 and native['nativeCropsViewedPixelMatched']==13 and native['sourcePDFSHA256']==source['sourcePDF']['sha256']
frozen=read(b/'PRE_RUNTIME_TRANSCRIPTION.json');assert frozen['newEngineCallsAtFreeze']==0 and sha(b/frozen['file'])==frozen['sha256'];table=read(b/'MANUAL_MONTH_GOD_TABLES.json');assert len(table['records'])==7 and table['printedCells']==84 and table['clearCells']==82 and table['unresolvedCells']==2
lookup={}
for row in table['records']:
 assert [x['monthOrdinal']for x in row['cells']]==list(range(1,13))
 for cell in row['cells']:lookup[row['id'],cell['monthOrdinal']]=cell
assert sum(x['literal']is not None for x in lookup.values())==82
assert {k for k,v in lookup.items()if v['literal']is None}=={('month-wealth',2),('month-wealth',8)}
assert [lookup['tian-de',m]['literal']for m in[2,5,8,11]]==['坤','乾','艮','巽']
res=read(q/'REFERENCE_RESULTS.json');assert len(res['checks'])==6 and all(x['ok']for x in res['checks'])and len(res['calls'])==20
assert res['summary']['actualLunarStemPartnerLookups']==20 and res['summary']['skippedTrigramBaseCases']==4 and res['summary']['invalidFrameNullQueries']==336
for x in res['calls']:
 assert x['actualPartner']==x['printedPartner'];assert x['table']=='HE_GAN_5'
 for a,z in [('tian-de','tian-de-he'),('month-de','month-de-he')]:
  if lookup[a,x['month']]['literal']==x['sourceBase']and lookup[z,x['month']]['literal']==x['printedPartner']:break
 else:raise AssertionError(x)
for x in source['runtimeProof']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256']
assert read(w/'v46/node_modules/lunar-typescript/package.json')['version']=='1.8.6'
assert len(res['sourceResults'])==84
for x in res['sourceResults']:
 assert x['literal']==lookup[x['god'],x['monthOrdinal']]['literal'];assert x['practicalOutcome']is None and not x['calendarMonthAdapterImplemented']and not x['trigramToBranchAdapterImplemented']and not x['wholeDateSelectionMethodImplemented']
state=read(b/'WORK_STATE.json');assert not state['wholeCatalogueCompleted']and not state['consumerChanged']and not source['fullDateSelectionMethodImplemented']and not source['sourceMonthCalendarBoundaryResolved']
out=dict(date='2026-10-28',promotionIdentities=29,expandedPriorSourcePositions=8,newSourcePositions=0,newHTTPRequests=0,newOriginalContainers=0,newIndependentWitnesses=0,nativeCropsViewedPixelMatched=13,excludedWrongTargetCrops=1,sourceRows=7,printedCells=84,clearCells=82,unresolvedSourceCells=2,completeRuntimeChecks=6,actualLunarStemPartnerLookups=20,skippedTrigramBaseCases=4,invalidFrameNullQueries=336,actualNewHHCCalendarCharts=0,actualNewIztroCharts=0,localRuntimeFilesHashed=3,sourceMonthCalendarBoundaryResolved=False,trigramToBranchAdapterImplemented=False,fullDateSelectionMethodImplemented=False,sourceOutcomesValidated=False,consumerChanged=False,wholeCatalogueCompleted=False)
p=q/'SOURCE_RESULTS.json'
if '--no-write'in sys.argv:assert read(p)==out
else:p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
