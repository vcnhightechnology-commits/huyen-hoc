from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,sys
r=Path(__file__).resolve().parents[1];w=r.parent;b=r/'research/home-yangzhai-final-spans';q=r/'qa/home-yangzhai-final-spans'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda p:sha256(p.read_bytes()).hexdigest()
promotion=read(b/'PROMOTION_IDENTITIES.json');assert len(promotion['records'])==130
for x in promotion['records']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'],x['file']
moduleRecord=next(x for x in promotion['records']if x['file']=='v53/research/home-yangzhai-final-spans/selection/source-hour-reference.mjs')
assert sha(b/'selection/source-hour-reference.mjs')==moduleRecord['sha256']
old=(b/'selection/STAGED_test-hour-reference.mjs').read_text(encoding='utf-8')
for before,after in [("from './source-hour-reference.mjs'","from '../research/home-yangzhai-final-spans/selection/source-hour-reference.mjs'"),
 ("const b=import.meta.dirname,w=resolve(b,'../..'),r=resolve(w,'v53');","const b=resolve(import.meta.dirname,'../research/home-yangzhai-final-spans/selection'),w=resolve(b,'../../../..'),r=resolve(w,'v53');"),
 ("resolve(b,'REFERENCE_RESULTS.json')","resolve(r,'qa/home-yangzhai-final-spans/selection/REFERENCE_RESULTS.json')")]:assert old.count(before)==1;old=old.replace(before,after)
assert old==(r/'scripts/test-home-final-spans.mjs').read_text(encoding='utf-8')
rawcount=0;unique=set()
for scope,n in [('exterior',22),('selection',45),('talismans',28)]:
 meta=read(b/scope/'RAW_IMAGES.json');assert len(meta['records'])==n
 assert len(read(b/scope/'CONTEXT_READINGS.json')['groups'])==n
 for x in meta['records']:
  p=b/scope/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256']and x['actuallyViewed']
  rawcount+=1;unique.add(x['pdfPage'])
assert rawcount==95 and len(unique)==94
qa=read(q/'selection/QA_IMAGES.json');assert qa['allViewed']and len(qa['crops'])==8
for x in qa['crops']:
 p=q/'selection'/Path(x['file']).name;source=b/'selection'/f"raw-p{x['sourcePDFPage']:03}.jpg"
 assert sha(p)==x['sha256']and x['actuallyViewed']
 assert ImageChops.difference(Image.open(p).convert('RGB'),Image.open(source).convert('RGB').crop(x['cropBox'])).getbbox()is None
results=read(q/'selection/REFERENCE_RESULTS.json');assert len(results['checks'])==8 and all(x['ok']for x in results['checks'])
assert len(results['fixtures'])==132 and results['actualLunarObjects']==144 and results['actualHourLabelQueries']==132
assert sum(x['match']for x in results['fixtures'])==120 and results['literalSimingDifferencesRetained']==12
assert all(x['sourceLabel']=='司命'and x['actualEngineLabel']=='勾陈'for x in results['fixtures']if not x['match'])
unit=read(b/'UNIT_MAP.json');assert unit['totalDistinctPositionsWithFirstPassRead']==195 and unit['fullFirstPassBodySpans']==10
assert unit['wholeUnitsApplied']==0 and not read(b/'WORK_STATE.json')['wholeCatalogueCompleted']
assert {p for x in unit['records']for p in x['actuallyViewedPositions']}|{1,2,3,4,5}==set(range(1,196))
assert len(read(b/'SOURCE_DISPOSITIONS.json')['records'])==10
assert sha(r/'research/home-yangzhai-shishu/Tianyige-330000-1705-0007405-yangzhai-shishu.pdf')=='b6394102a995bb66df173452b37614b29d58e34ff85e08c43077006572ac48a5'
out={'date':'2026-10-28','completeRuntimeChecks':8,'promotionIdentities':130,'rawArtifactRecordsVerified':95,'uniqueRawPositionsThisScope':94,
 'newDistinctReadPositions':92,'totalDistinctBookPositionsRead':195,'firstPassMainSpans':10,'wholeUnitsApplied':0,
 'nativeCropsViewedPixelMatched':8,'manualHourCellsCompared':132,'actualLunarObjects':144,'actualHourLabelQueries':132,
 'matchesAfterExplicitAliases':120,'retainedSourceEngineDifferences':12,'pendingHourCells':12,
 'consumerChanged':False,'wholeCatalogueCompleted':False,'ritualEfficacyValidated':False,'allSourceConditionsApplied':False}
p=q/'SOURCE_RESULTS.json'
if '--no-write'in sys.argv:assert read(p)==out
else:p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
