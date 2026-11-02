from pathlib import Path
from hashlib import sha256
import json,zipfile,sys

root=Path(__file__).resolve().parent.parent
workspace=root.parent
base=root/'research/meihua-conditions'
qa=root/'qa/meihua-conditions'
archive=workspace/'archives/v53-before-meihua-conditions'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda b:sha256(b).hexdigest()
manifest=read(root/'PACKAGE_MANIFEST.json');old=read(archive/'PACKAGE_MANIFEST.json')
html=(root/'Huyen_Hoc_Cac.html').read_bytes()
assert len(html)==703410 and sha(html)==old['product']['sha256']==manifest['product']['sha256']=='3800162854742c915d60f0051c65cadb0eb9a1c803f9f937bf1b6a593c96d268'
assert html==(workspace/'Huyen_Hoc_Cac.html').read_bytes()==(root/'site/index.html').read_bytes()
assert sorted(p.name for p in (root/'site').iterdir())==['index.html']
for f in old['files']:
 if '/' not in f['file'] and f['file'].endswith(('.js','.css')):assert sha((root/f['file']).read_bytes())==f['sha256'],f['file']
for name in [b'conditions-reference',b'DOMAIN_RULES.json',b'VARIANTS_AND_GAPS',b'SOURCE_BASELINE',b'<details class="mh-layers']:
 assert name not in html,name
web=workspace/'Huyen_Hoc_Cac_V53_web.zip'
assert web.read_bytes()==(workspace/'archives/v53-before-meihua-layers'/web.name).read_bytes()
with zipfile.ZipFile(web)as z:
 assert sorted(z.namelist())==['HUONG_DAN.md','index.html']
 assert z.read('index.html')==html and z.read('HUONG_DAN.md')==(root/'README.md').read_bytes()
assert {p.relative_to(root).as_posix()for p in root.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json'}=={f['file']for f in manifest['files']}
for f in manifest['files']:
 b=(root/f['file']).read_bytes();assert len(b)==f['bytes']and sha(b)==f['sha256'],f['file']
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_source.zip')as z:
 assert set(z.namelist())=={'v53/'+f['file']for f in manifest['files']}|{'v53/PACKAGE_MANIFEST.json'}
 assert z.read('v53/PACKAGE_MANIFEST.json')==(root/'PACKAGE_MANIFEST.json').read_bytes()
 for f in manifest['files']:assert sha(z.read('v53/'+f['file']))==f['sha256'],f['file']
assert (archive/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==831586307
with zipfile.ZipFile(archive/'Huyen_Hoc_Cac_V53_source.zip')as z:
 assert z.read('v53/PACKAGE_MANIFEST.json')==(archive/'PACKAGE_MANIFEST.json').read_bytes()
 for name in ['MEIHUA_VOLUME_MAP_REPORT.md','research/meihua-volume-map/MANUAL_READINGS.json','research/meihua-volume-map/UNIT_MAP.json','qa/meihua-volume-map/RELEASE_RESULTS.json','research/meihua-witness/MANUAL_READINGS.json']:
  assert z.read('v53/'+name)==(root/name).read_bytes(),name
baseline=read(base/'SOURCE_BASELINE.json');index=read(root/'research/meihua/EXTRACTED_PAGES.json')
assert len(index['pages'])==214 and len(baseline['previousRenderedRecords'])==186
for f in baseline['previousRenderedRecords']:assert next(r for r in index['pages']if r['pdfPage']==f['pdfPage'])==f
manual=read(base/'MANUAL_READINGS.json');assert len(manual['records'])==48 and manual['counts']['newContentPageRecords']==38
for f in manual['records']:assert sha((base/f['image']).read_bytes())==f['imageSHA256']
r=read(qa/'ENGINE_RESULTS.json');assert len(r['checks'])==14 and all(c['ok']for c in r['checks']) and r['htmlSHA256']==sha(html)
assert r['summary']['realCastGraphStructures']==384 and r['summary']['directRelationCells']==85
assert len(read(base/'DOMAIN_RULES.json')['domains'])==18
assert len(read(base/'UNIT_MAP.json')['units'])==52 and not read(base/'UNIT_MAP.json')['allConditionalClausesExtracted']
pending=read(root/'research/meihua-layers/PENDING.json');assert not pending['released']and pending['browserChecksExecuted']==0 and not pending['pdfCreated']
for f in pending['candidateFiles']:assert sha((root/'research/meihua-layers/candidate'/f['file']).read_bytes())==f['sha256']
assert not(root/'qa/meihua-layers/BROWSER_RESULTS.json').exists()and not(root/'qa/meihua-layers/body-use-layers.pdf').exists()
state=read(workspace/'EXHAUSTIVE_WORK_STATE.json');assert state==read(root/'research/EXHAUSTIVE_WORK_STATE.json')and state['status']=='active-not-complete'
full=read(root/'research/full-study/WORK_STATE.json');assert full['latestResearchReport']=='MEIHUA_CONDITIONS_REPORT.md'and full['latestConsumerReport']=='MEIHUA_METHODS_REPORT.md'and full['overallStatus']=='active-not-complete'
coverage=read(root/'research/library-current/COVERAGE.json');assert coverage['counts']['wholeWorkApplied']==0 and coverage['product']['sha256']==sha(html)
structure=read(root/'research/meihua/SCAN_STRUCTURE.json');v=next(v for v in structure['volumes']if v['volume']==2)
assert(v['titlePDFPage'],v['endPDFPage'],v['lastPrintedPage'])==(55,98,44)and structure['physicalLowerBookCoverPDFPage']==102
out={'sourceAndReferenceChecks':14,'sourcePageRecords':48,'contentPages':44,'newContentPageRecords':38,'expandedPriorContentPageRecords':6,'physicalUnits':52,'domains':18,'directRelationCells':85,'realCastGraphStructures':384,'graphNodes':1920,'graphEdges':4710,'piContextCases':6,'textContextVariants':5,'newPNGDerivatives':28,'retainedPNGDerivatives':214,'newHTTPResponses':0,'consumerChanged':False,'releasedHTMLBytes':len(html),'releasedHTMLSHA256':sha(html),'webZIPUnchanged':True,'siteClean':True,'previousSourceZIPPreserved':True,'previousSourceZIPBytes':831586307,'candidateReleased':False,'candidateBrowserChecksExecuted':0,'candidatePDFCreated':False,'manifestFilesVerified':len(manifest['files']),'sourceZIPFilesVerified':len(manifest['files'])+1,'predictiveAccuracyEstablished':False,'allVolume2ClausesCompleted':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False}
if '--no-write'in sys.argv:assert read(qa/'RELEASE_RESULTS.json')==out
else:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
