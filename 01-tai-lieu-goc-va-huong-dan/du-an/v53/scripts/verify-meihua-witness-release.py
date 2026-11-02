from pathlib import Path
from hashlib import sha256
import json,zipfile,sys

root=Path(__file__).resolve().parent.parent
workspace=root.parent
qa=root/'qa/meihua-witness'
base=root/'research/meihua-witness'
archive=workspace/'archives/v53-before-meihua-layers'
sha=lambda b:sha256(b).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf8'))
manifest=read(root/'PACKAGE_MANIFEST.json')
old=read(archive/'PACKAGE_MANIFEST.json')
html=(root/'Huyen_Hoc_Cac.html').read_bytes()
assert html==(root/'site/index.html').read_bytes()==(workspace/'Huyen_Hoc_Cac.html').read_bytes()==(archive/'Huyen_Hoc_Cac.html').read_bytes()
assert len(html)==703410 and sha(html)==old['product']['sha256']==manifest['product']['sha256']=='3800162854742c915d60f0051c65cadb0eb9a1c803f9f937bf1b6a593c96d268'
for f in old['files']:
 if '/'not in f['file']and f['file'].endswith(('.js','.css')):assert sha((root/f['file']).read_bytes())==f['sha256'],f['file']
assert sorted(p.name for p in(root/'site').iterdir())==['index.html']
assert not any(v in html for v in[b'NLC416',b'NAJIA_TABLE',b'EDITION_IDENTITY',b'PENDING.json'])
assert not b'<details class="mh-layers'in html
assert {p.relative_to(root).as_posix()for p in root.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json'}=={f['file']for f in manifest['files']}
for f in manifest['files']:
 b=(root/f['file']).read_bytes();assert len(b)==f['bytes']and sha(b)==f['sha256'],f['file']
web=workspace/'Huyen_Hoc_Cac_V53_web.zip'
assert web.read_bytes()==(archive/web.name).read_bytes()
with zipfile.ZipFile(web)as z:
 assert sorted(z.namelist())==['HUONG_DAN.md','index.html']
 assert z.read('index.html')==html and z.read('HUONG_DAN.md')==(root/'README.md').read_bytes()
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_source.zip')as z:
 assert set(z.namelist())=={'v53/'+f['file']for f in manifest['files']}|{'v53/PACKAGE_MANIFEST.json'}
 assert z.read('v53/PACKAGE_MANIFEST.json')==(root/'PACKAGE_MANIFEST.json').read_bytes()
 for f in manifest['files']:assert sha(z.read('v53/'+f['file']))==f['sha256'],f['file']
assert(archive/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==819897455
with zipfile.ZipFile(archive/'Huyen_Hoc_Cac_V53_source.zip')as z:assert z.read('v53/PACKAGE_MANIFEST.json')==(archive/'PACKAGE_MANIFEST.json').read_bytes()
r=read(qa/'ENGINE_RESULTS.json');assert len(r['checks'])==13 and all(c['ok']for c in r['checks'])and r['htmlSHA256']==sha(html)
layers=read(root/'qa/meihua-layers/ENGINE_RESULTS.json');assert len(layers['checks'])==14 and all(c['ok']for c in layers['checks'])and layers['candidate']
pending=read(root/'research/meihua-layers/PENDING.json');assert pending['released']is False and pending['browserChecksExecuted']==0 and pending['pdfCreated']is False
assert not(root/'qa/meihua-layers/BROWSER_RESULTS.json').exists()and not(root/'qa/meihua-layers/body-use-layers.pdf').exists()
for f in pending['candidateFiles']:assert sha((root/'research/meihua-layers/candidate'/f['file']).read_bytes())==f['sha256']
assert pending['releasedHTMLSHA256']==sha(html)
full=read(root/'research/full-study/WORK_STATE.json');assert full['overallStatus']=='active-not-complete'and full['latestConsumerReport']=='MEIHUA_METHODS_REPORT.md'and full['latestResearchReport']=='MEIHUA_WITNESS_REPORT.md'
assert read(workspace/'EXHAUSTIVE_WORK_STATE.json')==read(root/'research/EXHAUSTIVE_WORK_STATE.json')
coverage=read(root/'research/library-current/COVERAGE.json');assert coverage['counts']['wholeWorkApplied']==0 and coverage['product']['sha256']==sha(html)
idn=read(base/'EDITION_IDENTITY.json');assert idn['imprint']['gregorianYear']==1925 and idn['imprint']['month']==11 and not idn['imprint']['historicalShaoYongAuthorshipEstablished']
units=read(base/'UNIT_MAP.json');assert len(units['units'])==34 and len(units['stillUnmappedBodyPDFPages'])==47 and not units['wholePrintedInventoryCompleted']
manual=read(base/'MANUAL_READINGS.json');assert manual['counts']=={'targetedPageRecords':41,'contentPageRecords':35,'newContentPageRecords':32,'expandedPriorContentPageRecords':3,'endleaves':3,'advertisements':2,'colophon':1}
for row in manual['records']:assert sha((base/row['image']).read_bytes())==row['imageSHA256']
corrected=read(root/'research/meihua-reading/ADDITIONAL_SCAN_NOTES.json')
assert next(x for x in corrected['records']if x['pdfPage']==200)['printedPage']=='12'
assert next(x for x in corrected['records']if x['pdfPage']==220)['printedPage']=='32'
assert next(x for x in corrected['candidateVolumeStarts']if x['volume']==5)['verifiedTitlePDFPage']==189
out={'researchChecks':13,'candidateCalculationChecks':14,'candidateBrowserChecksExecuted':0,'candidatePDFCreated':False,'candidateReleased':False,'najiaAssignments':48,'nayinElementMatches':60,'nayinLabelVariantPairs':2,'sixSpiritLiteralRows':2,'sixSpiritDerivedRotations':4,'seasonalCells':20,'targetedPageRecords':41,'newContentPageReadings':32,'expandedPriorContentReadings':3,'unitGroups':34,'newPNGDerivatives':87,'retainedPNGDerivatives':186,'newHTTPResponses':0,'imprintDateRead':'1925-11','releasedHTMLBytes':len(html),'releasedHTMLSHA256':sha(html),'consumerChanged':False,'webZIPUnchanged':True,'previousReleasePreserved':True,'siteClean':True,'manifestFilesVerified':len(manifest['files']),'sourceZIPFilesVerified':len(manifest['files'])+1,'wholeBookCompleted':False,'wholeCatalogueCompleted':False}
if '--no-write'in sys.argv:assert read(qa/'RELEASE_RESULTS.json')==out
else:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(out,ensure_ascii=False))
