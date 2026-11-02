from pathlib import Path
from hashlib import sha256
import json,sys
from PIL import Image
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/home-yangzhai-door-water';q=r/'qa/home-yangzhai-door-water'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda data:sha256(data).hexdigest()
pdf=r/'research/home-yangzhai-shishu/Tianyige-330000-1705-0007405-yangzhai-shishu.pdf'
assert pdf.stat().st_size==151275796 and sha(pdf.read_bytes())=='b6394102a995bb66df173452b37614b29d58e34ff85e08c43077006572ac48a5'
native=read(q/'NATIVE_RESULTS.json');assert native['rawDCTStreamIdentitiesVerified']==18 and native['nativeLosslessCropsViewedAndPixelVerified']==12
raw=read(b/'RAW_IMAGES.json');assert len(raw['records'])==18 and raw['allExtractedPositionsViewed']
for a in raw['records']:
 data=(b/a['file']).read_bytes();assert len(data)==a['bytes']and sha(data)==a['sha256']and a['actuallyViewed']and a['sourceByteIdentityVerified']
 assert list(Image.open(b/a['file']).size)==a['nativeSize']
for a in read(q/'QA_IMAGES.json'):
 assert sha((q/a['file']).read_bytes())==a['sha256']and a['actuallyViewed']
 expected=Image.open(b/a['source']).convert('RGB').crop(a['box']);actual=Image.open(q/a['file']).convert('RGB')
 assert expected.size==actual.size and expected.tobytes()==actual.tobytes()
assert read(q/'CROP_TARGET_AUDIT.json')['actual']=='丙/午 columns'
assert not read(q/'PROMOTION_PATH_CORRECTION.json')['publishedTestExecutedBeforeCorrection']
t=read(b/'MANUAL_WATER_TABLE.json');assert len(t['rows'])==24 and len({x['mountain']for x in t['rows']})==24
assert sum(len(x['mainText']['targets'])for x in t['rows'])==46
assert sum(x['marginalText']is not None for x in t['rows'])==8
assert sum(len(x['marginalText']['targets'])for x in t['rows']if x['marginalText'])==16
assert all(x['sourcePDFPage']in[109,110]and not x['courtyardMeaningEncoded']for x in t['rows'])
p=read(b/'MANUAL_SOURCE_POLARITY.json');assert len(p['yangMarks'])==len(p['yinMarks'])==12 and len(set(p['yangMarks']+p['yinMarks']))==24
room=read(b/'MANUAL_ROOM_PAIR_ANCHORS.json');assert len(room['rows'])==4 and not room['fullFirstDrawExchangeEncoded']
c=read(b/'CONTEXT_READINGS.json');assert len(c['groups'])==18 and c['newSourceReadPositions']==16
assert all(not x['fullGlyphCollation']and not x['allClausesApplied']for x in c['groups'])
u=read(b/'UNIT_MAP.json');assert u['fullFirstPassBodySpans']==7 and u['totalDistinctPositionsWithFirstPassRead']==103 and u['unreadContainerPositions']==92
assert u['wholeUnitsApplied']==0 and not u['all195PositionsRead']
assert read(r/'research/home-yangzhai-fuyuan/UNIT_MAP.json')['fullFirstPassBodySpans']==4
result=read(q/'REFERENCE_RESULTS.json');assert len(result['checks'])==8 and all(x['ok']for x in result['checks'])
expected={'manualMainRows':24,'mainTargetEntries':46,'marginalRows':8,'marginalTargetEntries':16,'sourcePolarityMarks':24,
 'flowContexts':72,'alternateAnchorContexts':72,'printedOppositeRoomPairs':4,'projectedRoomContexts':8,
 'actualHHCDirectionsExecutions':8,'newCalendarExecutions':0}
assert result['summary']==expected and len(result['roomFixtures'])==8
assert result['engineSHA256']==sha((r/'engine.js').read_bytes())=='39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6'
ids=read(b/'PROMOTION_IDENTITIES.json');assert len(ids['records'])==48
for a in ids['records']:
 data=(w/a['file']).read_bytes();assert len(data)==a['bytes']and sha(data)==a['sha256']
test=(b/'STAGED_test-water-reference.mjs').read_text(encoding='utf-8')
test=test.replace("from './source-water-reference.mjs'","from '../research/home-yangzhai-door-water/source-water-reference.mjs'")
test=test.replace("const b=import.meta.dirname,w=resolve(b,'../..'),r=resolve(w,'v53')","const b=resolve(import.meta.dirname,'../research/home-yangzhai-door-water'),w=resolve(b,'../../..'),r=resolve(w,'v53')")
test=test.replace("resolve(b,'REFERENCE_RESULTS.json')","resolve(r,'qa/home-yangzhai-door-water/REFERENCE_RESULTS.json')")
assert test==(r/'scripts/test-home-door-water.mjs').read_text(encoding='utf-8')
out={'date':'2026-10-28','completeChecks':8,'originalDCTImagesViewedAndHashed':18,'newSourceReadPositions':16,
 'oldBoundariesExpanded':2,'nativeCropsViewedAndPixelVerified':12,**expected,'manualContextGroups':18,
 'totalDistinctBookPositionsRead':103,'unreadBookPositions':92,'firstPassMainSpans':7,'promotionIdentities':48,
 'moduleByteIdenticalToStaging':True,'publishedTestOnlyThreePathRelocations':True,'staticPromotionPathCorrectionRetained':True,
 'newHTTPRequests':0,'newOriginalContainers':0,'newIndependentWitnesses':0,'modernWaterGeometryOrDegreesAdapter':False,
 'engineeringGuidanceEstablished':False,'doorRulerOrCalendarAdapterEstablished':False,'sourceOutcomesValidated':False,
 'wholeCatalogueCompleted':False,'consumerChanged':False}
if '--no-write'in sys.argv:assert read(q/'SOURCE_RESULTS.json')==out
else:(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
