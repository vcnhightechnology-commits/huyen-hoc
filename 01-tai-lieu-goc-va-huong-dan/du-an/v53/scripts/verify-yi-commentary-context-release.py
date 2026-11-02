from pathlib import Path
from hashlib import sha256
import json, zipfile, sys

root = Path(__file__).resolve().parent.parent
workspace = root.parent
archive = workspace/'archives/v53-before-yi-context-refinement'
base = root/'research/yi-commentary-context'
qa = root/'qa/yi-commentary-context'
sha = lambda b: sha256(b).hexdigest()
read_json = lambda p: json.loads(p.read_text(encoding='utf8'))
m = read_json(root/'PACKAGE_MANIFEST.json')
old = read_json(archive/'PACKAGE_MANIFEST.json')
html = (root/'Huyen_Hoc_Cac.html').read_bytes()
assert html == (workspace/'Huyen_Hoc_Cac.html').read_bytes() == (root/'site/index.html').read_bytes()
assert len(html) == m['product']['bytes'] == 678173
assert sha(html) == m['product']['sha256'] == '57850abfad4a3c92069de448e3d654d427a4bd778d100b08925e5ba1c8330d8e'
assert [p.name for p in (root/'site').iterdir()] == ['index.html']
assert b'<script src=' not in html and b'<link rel="stylesheet"' not in html
assert (root/'yi-complete-data.js').read_bytes().strip() in html
assert not any(x in html for x in [b'NCL-00037',b'MANUAL_READINGS.json',b'57850abfad4a3c9'])
assert {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.name != 'PACKAGE_MANIFEST.json'} == {f['file'] for f in m['files']}
for f in m['files']:
    b = (root/f['file']).read_bytes()
    assert len(b) == f['bytes'] and sha(b) == f['sha256'], f['file']
for f in old['files']:
    if ('/' not in f['file'] and f['file'].endswith(('.js','.css','.md')) and f['file'] not in ['yi-complete-data.js','FULL_STUDY_REPORT.md','NEXT_STEPS.md','YI_CONTEXT_REFINEMENT_REPORT.md']) or f['file'] in ['index.html','scripts/build.mjs'] or f['file'].startswith(('assets/','research/yi-second-witness/','research/full-study/yi/')):
        assert sha((root/f['file']).read_bytes()) == f['sha256'], f['file']
assert sha((archive/'Huyen_Hoc_Cac.html').read_bytes()) == old['product']['sha256'] == 'eb1425292f680ac60dd1af57ac805f6312d209ad92d72c4f6499de0502d9ff22'
assert (archive/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size == 798324448
with zipfile.ZipFile(archive/'Huyen_Hoc_Cac_V53_source.zip') as z:
    assert z.read('v53/PACKAGE_MANIFEST.json') == (archive/'PACKAGE_MANIFEST.json').read_bytes()
    assert z.read('v53/yi-complete-data.js') == (archive/'yi-complete-data.js').read_bytes()
with zipfile.ZipFile(archive/'Huyen_Hoc_Cac_V53_web.zip') as z:
    assert z.read('index.html') == (archive/'Huyen_Hoc_Cac.html').read_bytes()
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_web.zip') as z:
    assert sorted(z.namelist()) == ['HUONG_DAN.md','index.html']
    assert z.read('index.html') == html and z.read('HUONG_DAN.md') == (root/'README.md').read_bytes()
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_source.zip') as z:
    assert set(z.namelist()) == {'v53/'+f['file'] for f in m['files']} | {'v53/PACKAGE_MANIFEST.json'}
    assert z.read('v53/PACKAGE_MANIFEST.json') == (root/'PACKAGE_MANIFEST.json').read_bytes()
    for f in m['files']:
        assert sha(z.read('v53/'+f['file'])) == f['sha256'], f['file']
for file,count in [('ENGINE_RESULTS.json',15),('BROWSER_RESULTS.json',26)]:
    r = read_json(qa/file)
    assert len(r['checks']) == count and all(x['ok'] for x in r['checks'])
    assert not r.get('errors') and not r.get('http')
engine = read_json(qa/'ENGINE_RESULTS.json')
assert engine['htmlSHA256'] == sha(html)
assert engine['summary']['actualEngineTargetCases'] == len(engine['casts']) == 24
assert engine['summary']['consumerRecordsRefined'] == 6 and engine['summary']['unchangedOrdinaryReadings'] == 378
for key,file in [('manualSHA256','MANUAL_READINGS.json'),('changesSHA256','CONSUMER_CHANGES.json'),('imageAuditSHA256','IMAGE_AUDIT.json')]:
    assert engine[key] == sha((base/file).read_bytes())
images = read_json(qa/'IMAGE_RESULTS.json')
assert images['exactJPEGsVerified'] == 8 and images['newExtraction'] == 1 and images['textExtractionCharacters'] == 0 and not images['ocrUsed']
assert images['imageAuditSHA256'] == engine['imageAuditSHA256']
for p in read_json(base/'IMAGE_AUDIT.json')['pages']:
    b = (base/p['file']).read_bytes()
    assert len(b) == p['bytes'] and sha(b) == p['sha256'] and p['size'] == [1713,1240]
for r in read_json(base/'CONSUMER_CHANGES.json')['changes']:
    txt = (qa/f"reading-{r['hexagram']}-{r['position']}.txt").read_text(encoding='utf8')
    assert r['after']['text'] in txt and r['after']['tip'] in txt
for f in ['trung-phu-390.png','trung-phu-1440.png','khon-390.png']:
    assert (qa/f).stat().st_size > 10000
state = read_json(root/'research/full-study/WORK_STATE.json')
assert state['overallStatus'] == 'active-not-complete'
assert next(x for x in state['items'] if x['id']=='yi')['latestScope'] == '../yi-commentary-context/MANUAL_READINGS.json'
assert state['latestConsumerReport'] == 'YI_CONTEXT_REFINEMENT_REPORT.md'
result = {
    'htmlBytes':len(html),'htmlSHA256':sha(html),'automatedScopeChecks':41,
    'sourceRuntimeChecks':15,'browserChecks':26,'actualEngineTargetCases':24,
    'commentaryUnits':7,'sourceImages':8,'newEmbeddedJPEGExtractions':1,
    'newYaoCollations':0,'consumerRecordsRefined':6,'otherOrdinaryReadingsPreserved':378,
    'newExternalResponses':0,'calculationsAndChineseCorpusUnchanged':True,
    'siteClean':True,'priorReleasePreserved':True,'newPDFCreated':False,
    'manifestFilesVerified':len(m['files']),'sourceZIPFilesVerified':len(m['files'])+1,
    'fourResearchDirections':state['overallStatus']
}
if '--no-write' not in sys.argv:
    (qa/'RELEASE_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
else:
    assert read_json(qa/'RELEASE_RESULTS.json') == result
print(json.dumps(result,ensure_ascii=False))
