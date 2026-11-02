from pathlib import Path
from hashlib import sha256
import json, shutil

r = Path(__file__).resolve().parent.parent
w = r.parent
b = r / 'research/tuvi-void-child'
q = r / 'qa/tuvi-void-child'
read = lambda p: json.loads(p.read_text(encoding='utf-8-sig'))
sha = lambda p: sha256(p.read_bytes()).hexdigest()
def write(p, d):
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

assert not b.exists() and not q.exists(), 'One-shot promotion; preserve staging'
snapshot = read(w/'archives/v53-before-tuvi-void-child/SNAPSHOT.json')
assert snapshot['sourceManifestFiles'] == 3521 and snapshot['sourceZIPBytes'] == 2073696063
assert len(read(r/'PACKAGE_MANIFEST.json')['files']) == 3521
child = w/'tmp/tuvi-child-limit-staging'
void = w/'tmp/tuvi-void-coordinates-staging'
cr, vr = read(child/'RESULTS.json'), read(void/'RESULTS.json')
assert len(cr['checks']) == 5 and len(vr['checks']) == 7
assert all(x['ok'] for x in cr['checks']+vr['checks'])
b.mkdir(); (b/'images').mkdir(); q.mkdir()
identities = []
def copy(source, dest):
    shutil.copyfile(source, dest)
    assert source.read_bytes() == dest.read_bytes()
    identities.append({'file':dest.relative_to(w).as_posix(), 'stagingFile':source.relative_to(w).as_posix(), 'sha256':sha(dest), 'bytes':dest.stat().st_size})

for folder, names in [(child,['ordinal-reference.mjs','SOURCE_ORDINALS.json','RESPONSE.json','SEARCH_LEADS.json','official-080-max-response.bin']), (void,['void-reference.mjs','SOURCE_TABLES.json'])]:
    for name in names: copy(folder/name, b/name)
for folder, prefix in [(child,'CHILD'), (void,'VOID')]:
    copy(folder/'SOURCE_MANIFEST.json', b/(prefix+'_SOURCE_MANIFEST.json'))
    copy(folder/'CROP.json', b/(prefix+'_CROP.json'))
    crop = read(folder/'CROP.json')
    copy(folder/crop['file'], b/'images'/crop['file'])
    copy(folder/'RESULTS.json', q/(prefix+'_RESULTS.json'))

write(b/'PROMOTION_IDENTITIES.json', {'date':'2026-10-28','basis':'Local byte-identity hashes at promotion, not publisher signatures. Audit uses packaged files without requiring tmp staging.','records':identities})
for folder, reference, script, manifest, result in [
    (child,'ordinal-reference','test-tuvi-child-ordinals.mjs','CHILD_SOURCE_MANIFEST.json','CHILD_RESULTS.json'),
    (void,'void-reference','test-tuvi-void-pairs.mjs','VOID_SOURCE_MANIFEST.json','VOID_RESULTS.json')]:
    source = folder/('test-ordinal-reference.mjs' if folder == child else 'test-void-reference.mjs')
    text = source.read_text(encoding='utf-8-sig')
    text = text.replace("from'./"+reference+".mjs'", "from'../research/tuvi-void-child/"+reference+".mjs'")
    text = text.replace("b=import.meta.dirname,req=", "b=resolve(r,'research/tuvi-void-child'),q=resolve(r,'qa/tuvi-void-child'),req=")
    text = text.replace("resolve(b,'SOURCE_MANIFEST.json')", "resolve(b,'"+manifest+"')")
    text = text.replace("resolve(b,'RESULTS.json')", "resolve(q,'"+result+"')")
    text = text.replace("resolve(r,'PACKAGE_MANIFEST.json')", "resolve(w,'archives/v53-before-tuvi-void-child/PACKAGE_MANIFEST.json')")
    (r/'scripts'/script).write_text(text, encoding='utf-8')

write(b/'MANUAL_READINGS.json', {
    'date':'2026-10-28', 'sourceCanvasOrdinal':80, 'canvasIsNotPrintedFolio':True,
    'retainedImage':'v53/research/fortune-followup/official-080.jpg',
    'retainedImageSHA256':'ef453337cd2255b4539053c78c89556ca47536ec9bd3cf476730532e63b32e37',
    'uniquePriorSourcePositionsExpanded':1, 'nativeCropsActuallyViewed':2,
    'units':[
        {'heading':'安截路空亡訣','scopeLiteral':'論本生年','sourceRows':5,'canonicalWorkingBranchCoordinates':10,'graphicSiOccurrencesNormalizedExplicitly':1,'fullTableCoordinateExtraction':True,'calendarBoundaryEstablished':False,'singleSoftwareStarSelectionAttested':False},
        {'heading':'安旬中空亡訣','scopeLiteral':'論本生年','sourceRows':6,'canonicalWorkingBranchCoordinates':12,'graphicSiOccurrencesNormalizedExplicitly':1,'fullTableCoordinateExtraction':True,'calendarBoundaryEstablished':False,'singleSoftwareStarSelectionAttested':False},
        {'heading':'童限','sourcePrintedOrdinalsExtracted':[1,2,3,4,5,6],'workingReading':'一命二財三疾厄 四妻五福六官祿','tail':'餘年一□順流行 / 十五大命宮看端的','tailMeaningResolved':False,'ageCalendarAdapterEstablished':False,'wholePassageTranscribed':False}
    ],
    'cropRecords':['CHILD_CROP.json','VOID_CROP.json'], 'wholeCanvasApplied':False,
    'newHTTPRequestsThisHeartbeat':0, 'inheritedFailedHigherResolutionRequests':1,
    'newOriginalContainers':0, 'newSourcePositions':0, 'sourceInstructionsAreData':True,
    'method':'Exact native crops inspected; no OCR, resampling or glyph restoration from engine agreement.'
})
write(b/'CURRENT_UNITS.json', {
    'date':'2026-10-28','catalogueID':'T01','sourceItem':'NAJ4468520',
    'scope':'Three bounded headings within one previously read canvas, not a complete book/table of contents.',
    'units':[
        {'id':'canvas80-jielu','heading':'安截路空亡訣','status':'named-birthyear-pair-coordinates-verified-with-explicit-orthography-policy','reference':'void-reference.mjs','consumerApplied':False},
        {'id':'canvas80-xunzhong','heading':'安旬中空亡訣','status':'named-birthyear-pair-coordinates-verified-with-explicit-orthography-policy','reference':'void-reference.mjs','consumerApplied':False},
        {'id':'canvas80-child-ordinals','heading':'童限','status':'six-printed-ordinals-extracted-tail-and-age-semantics-open','reference':'ordinal-reference.mjs','consumerApplied':False}
    ],
    'relatedPriorStudy':'../tuvi-masters/WORK_STATE.json','wholeBookApplied':False,
    'remaining':['Child verse tail/age counting and link to first major period','Birth-year calendar boundary of these two source tables','Whether another independently acquired witness specifies single-star/parity selection','Body-master 火鈴星 at 子午 and anchor; Canh/Nham transformations; first-major-period variants','Remaining source combination verses and full chapter-level coverage']
})
print(json.dumps({'copiedIdentityRecords':len(identities),'referenceModules':2,'sourceTables':2,'preservedQAResults':2,'consumerChanged':False}))
