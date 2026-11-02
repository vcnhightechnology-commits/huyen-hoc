from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,sys
r=Path(__file__).resolve().parents[1];w=r.parent;b=r/'research/home-xuankong-context';q=r/'qa/home-xuankong-context'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda p:sha256(p.read_bytes()).hexdigest()
ident=read(b/'PROMOTION_IDENTITIES.json');assert len(ident['records'])==25
for x in ident['records']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'],x['file']
text=(b/'STAGED_test-xuankong-context.mjs').read_text(encoding='utf-8')
for old,new in [("from './xuankong-context-reference.mjs'","from '../research/home-xuankong-context/xuankong-context-reference.mjs'"),("const b=import.meta.dirname,w=resolve(b,'../..'),checks=[],fixtures=[];","const b=resolve(import.meta.dirname,'../research/home-xuankong-context'),w=resolve(b,'../../..'),checks=[],fixtures=[];"),("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/home-xuankong-context/REFERENCE_RESULTS.json')")]:assert text.count(old)==1;text=text.replace(old,new)
assert text==(r/'scripts/test-home-xuankong-context.mjs').read_text(encoding='utf-8')
raw=read(b/'RAW_REVIEW.json');assert len(raw['records'])==7 and raw['newTianyigePositions']==0
for x in raw['records']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256']and x['fullRawImageActuallyViewed']and not x['newReadPosition']
count=0
for sub in ['', 'collation']:
 for x in read(q/sub/'QA_IMAGES.json')['records']:
  p=q/sub/x['file'];src=w/x['sourceFile'];assert x['actuallyViewed']and not x['resampled']and sha(p)==x['sha256']
  if 'sourceSHA256'in x:assert sha(src)==x['sourceSHA256']
  assert ImageChops.difference(Image.open(src).convert('RGB').crop(x['cropBox']),Image.open(p).convert('RGB')).getbbox()is None;count+=1
assert count==9
cells=read(b/'collation/MANUAL_WITNESS_CELLS.json');assert len(cells['records'])==69 and cells['fullyResolvedFourFieldMatches']==64 and cells['partialCells']==5
original=read(r/'research/home-yangzhai-courtyards/MANUAL_DIAGRAM_CELLS.json');lookup={(d['id'],c['ordinal']):c for d in original['records']for c in d['printedLayerCells']}
full=0;partial=[]
for x in cells['records']:
 old=lookup[x['caseID'],x['ordinal']]
 for field in ['sourceElement','sourceLabel','sourceStar','sourceSizeHeightWord']:
  if field in x['uncertainFields']:assert x[field]is None
  else:assert x[field]==old[field]
 if x['uncertainFields']:partial.append((x['caseID'],x['ordinal']))
 else:full+=1
assert full==64 and partial==[('YZSS-C86',3),('YZSS-C87',2),('YZSS-C89',3),('YZSS-C90',1),('YZSS-C90',6)]
res=read(q/'REFERENCE_RESULTS.json');assert len(res['checks'])==5 and all(x['ok']for x in res['checks'])
assert res['actualHHCDirectionsCalls']==res['actualWaterReferenceCalls']==8 and len(res['fixtures'])==8
assert sum(x['birthGroupWouldDiffer']for x in res['fixtures'])==sum(x['waterClassificationDiffers']for x in res['fixtures'])==4
assert read(b/'MANUAL_SOURCE_ANCHORS.json')['records'][0]['literalYangMarks']==list('乾坎艮震')
coverage=read(r/'research/library-current/COVERAGE.json');p08=next(x for x in coverage['catalogue']if x['id']=='P08')
assert p08['currentSourceUnitCounts']['manualHourCells']==144 and p08['currentSourceUnitCounts']['retainedHourDifferences']==0
assert not read(b/'WORK_STATE.json')['wholeCatalogueCompleted']and not cells['all69FullyTranscribedOrMatched']
out=dict(date='2026-10-28',promotionIdentities=25,completeRuntimeChecks=5,expandedRawSourcePositionsReviewed=7,newSourcePositions=0,newHTTPBodies=0,
 nativeCropsViewedPixelMatched=9,witnessCellsDispositioned=69,fullyResolvedFourFieldMatches=64,partialElementReadings=5,actualHHCDirectionsCalls=8,actualWaterReferenceCalls=8,
 differingBirthGroupProjections=4,differingWaterPolarityProjections=4,differencesAreNamedFrameDistinctionsNotEngineBugs=True,
 correctedHourTableStill144CellsZeroDifferences=True,consumerChanged=False,wholeXuanKongExchangeApplied=False,modernRoomGeometryAdapterValidated=False,wholeCatalogueCompleted=False)
p=q/'SOURCE_RESULTS.json'
if '--no-write'in sys.argv:assert read(p)==out
else:p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
