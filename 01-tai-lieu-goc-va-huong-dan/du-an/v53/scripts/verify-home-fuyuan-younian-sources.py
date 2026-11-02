from pathlib import Path
from hashlib import sha256
import json,sys
from PIL import Image
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/home-yangzhai-fuyuan';q=r/'qa/home-yangzhai-fuyuan'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda data:sha256(data).hexdigest()
pdf=r/'research/home-yangzhai-shishu/Tianyige-330000-1705-0007405-yangzhai-shishu.pdf'
assert pdf.stat().st_size==151275796 and sha(pdf.read_bytes())=='b6394102a995bb66df173452b37614b29d58e34ff85e08c43077006572ac48a5'
native=read(q/'NATIVE_RESULTS.json');assert native['rawDCTStreamIdentitiesVerified']==48 and native['nativeLosslessCropsViewedAndPixelVerified']==12
raw=read(b/'RAW_IMAGES.json');assert raw['allExtractedPositionsViewed'] and len(raw['records'])==48
for a in raw['records']:
 data=(b/a['file']).read_bytes();assert len(data)==a['bytes'] and sha(data)==a['sha256'] and a['actuallyViewed'] and a['sourceByteIdentityVerified']
 assert list(Image.open(b/a['file']).size)==a['nativeSize']
for a in read(q/'QA_IMAGES.json'):
 data=(q/a['file']).read_bytes();assert sha(data)==a['sha256'] and a['actuallyViewed'] and a['pixelIdentity']
 expected=Image.open(b/a['source']).convert('RGB').crop(a['box']);actual=Image.open(q/a['file']).convert('RGB')
 assert expected.size==actual.size and expected.tobytes()==actual.tobytes()
table=read(b/'MANUAL_FUYUAN_TABLE.json');assert len(table['rows'])==180 and len({(x['era'],x['ordinal'])for x in table['rows']})==180
assert sum(x[s]['printedCentralAnnotation']for x in table['rows']for s in ['male','female'])==40
assert all(x['sourcePDFPage']in [38,39,40,41]for x in table['rows'])
assert not table['modernYearAdapterEstablished'] and not table['birthYearBoundaryEstablished']
seq=read(b/'MANUAL_YOUNIAN_SEQUENCES.json');assert len(seq['rows'])==8 and all(len(x['tokens'])==7 for x in seq['rows'])
contexts=read(b/'CONTEXT_READINGS.json');assert len(contexts['groups'])==48 and contexts['newSourceReadPositions']==47
assert all(not x['allClausesApplied']and not x['fullGlyphCollation']for x in contexts['groups'])
u=read(b/'UNIT_MAP.json');assert u['fullFirstPassBodySpans']==4 and u['totalDistinctPositionsWithFirstPassRead']==87 and u['unreadContainerPositions']==108
assert not u['all195PositionsRead'] and u['wholeUnitsApplied']==0
old=read(r/'research/home-yangzhai-shishu/UNIT_MAP.json');assert old['fullFirstPassBodySpans']==2
result=read(q/'REFERENCE_RESULTS.json');assert len(result['checks'])==8 and all(x['ok']for x in result['checks'])
expected={'manualSourceRows':180,'manualSexSpecificCells':360,'centralRemaps':40,'compactSequences':8,'derivedCompassCoordinates':64,
 'actualLunarYearObjects':180,'actualLunarAnnualFieldQueries':360,'actualHHCDirectionsExecutions':360,
 'repeatedDirectionLabelComparisons':2880,'priorDifferentWorkRelationComparisons':64}
assert result['summary']==expected and len(result['yearFixtures'])==360
assert result['engineSHA256']==sha((r/'engine.js').read_bytes())=='39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6'
assert result['lunarRuntimeSHA256']==sha((w/'v46/node_modules/lunar-typescript/dist/index.cjs').read_bytes())
audit=read(q/'TEST_FAILURE_AUDIT.json');assert audit['attempt1']['actualHHCDirectionsExecutionsBeforeFailure']==360 and audit['attempt1']['actualLunarYearObjectsBeforeFailure']==180
assert read(b/'READING_CORRECTION_AUDIT.json')['correctPalaceNumbers']=={'male':[1,4,7],'female':[5,2,8]}
ids=read(b/'PROMOTION_IDENTITIES.json');assert len(ids['records'])==79
for a in ids['records']:
 data=(w/a['file']).read_bytes();assert len(data)==a['bytes'] and sha(data)==a['sha256']
test=(b/'STAGED_test-reference.mjs').read_text(encoding='utf-8')
test=test.replace("from './fuyuan-younian-reference.mjs'","from '../research/home-yangzhai-fuyuan/fuyuan-younian-reference.mjs'")
test=test.replace("const b=import.meta.dirname,w=resolve(b,'../..'),r=resolve(w,'v53');","const b=resolve(import.meta.dirname,'../research/home-yangzhai-fuyuan'),w=resolve(b,'../../..'),r=resolve(w,'v53');")
test=test.replace("resolve(b,'REFERENCE_RESULTS.json')","resolve(r,'qa/home-yangzhai-fuyuan/REFERENCE_RESULTS.json')")
assert test==(r/'scripts/test-home-fuyuan-younian.mjs').read_text(encoding='utf-8')
out={'date':'2026-10-28','completeChecks':8,'rawImagesViewedAndHashed':48,'newSourceReadPositions':47,'nativeCropsViewedAndPixelVerified':12,
 **expected,'priorFailedAttemptHHCExecutions':360,'priorFailedAttemptLunarYearObjects':180,
 'historicalTotalHHCExecutions':720,'historicalTotalLunarYearObjects':360,
 'repeatedExecutionsNotIndependentEvidence':True,'promotionIdentities':79,'moduleByteIdenticalToStaging':True,
 'testOnlyThreePathRelocations':True,'manualContextGroups':48,'totalDistinctBookPositionsRead':87,'unreadBookPositions':108,
 'firstPassChapterSpans':4,'newHTTPRequests':0,'newOriginalContainers':0,'newIndependentWitnesses':0,
 'birthYearBoundaryEstablished':False,'historicalRegnalConversionEstablished':False,'modernRoomGeometryAdapter':False,
 'sourceOutcomesValidated':False,'wholeCatalogueCompleted':False,'consumerChanged':False}
if '--no-write'in sys.argv:assert read(q/'SOURCE_RESULTS.json')==out
else:(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
