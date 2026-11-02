from pathlib import Path
from hashlib import sha256
import json,zipfile,sys

root=Path(__file__).resolve().parent.parent;workspace=root.parent
qa=root/'qa/meihua-external';base=root/'research/meihua-external'
archive=workspace/'archives/v53-before-meihua-external'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda b:sha256(b).hexdigest()
manifest=read(root/'PACKAGE_MANIFEST.json');old=read(archive/'PACKAGE_MANIFEST.json')
html=(root/'Huyen_Hoc_Cac.html').read_bytes()
assert len(html)==703410 and sha(html)==old['product']['sha256']==manifest['product']['sha256']=='3800162854742c915d60f0051c65cadb0eb9a1c803f9f937bf1b6a593c96d268'
assert html==(workspace/'Huyen_Hoc_Cac.html').read_bytes()==(root/'site/index.html').read_bytes()
assert sorted(p.name for p in (root/'site').iterdir())==['index.html']
for f in old['files']:
 if '/' not in f['file'] and f['file'].endswith(('.js','.css')):assert sha((root/f['file']).read_bytes())==f['sha256'],f['file']
 if f['file'].startswith(('research/meihua-conditions/','qa/meihua-conditions/','research/meihua-layers/')):assert sha((root/f['file']).read_bytes())==f['sha256'],f['file']
for s in [b'external-reference',b'MATERIAL_PREMISES',b'CONTEXT_PREMISES',b'WORKED_EXAMPLES.json',b'<details class="mh-layers']:assert s not in html,s
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
assert (archive/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==835660582
with zipfile.ZipFile(archive/'Huyen_Hoc_Cac_V53_source.zip')as z:
 assert z.read('v53/PACKAGE_MANIFEST.json')==(archive/'PACKAGE_MANIFEST.json').read_bytes()
 for name in ['MEIHUA_CONDITIONS_REPORT.md','research/meihua-conditions/conditions-reference.mjs','qa/meihua-conditions/RELEASE_RESULTS.json','research/meihua/EXTRACTED_PAGES.json','research/meihua-layers/PENDING.json']:
  assert z.read('v53/'+name)==(root/name).read_bytes(),name
index=read(root/'research/meihua/EXTRACTED_PAGES.json');assert len(index['pages'])==214
for r in index['pages']:
 b=(root/'research/meihua'/r['file']).read_bytes();assert len(b)==r['bytes']and sha(b)==r['sha256']
manual=read(base/'MANUAL_READINGS.json');assert len(manual['records'])==42 and manual['counts']['newContentPageRecords']==27
for r in manual['records']:assert sha((base/r['image']).read_bytes())==r['imageSHA256']
assert len(read(base/'UNIT_MAP.json')['units'])==26
assert len(read(base/'MATERIAL_PREMISES.json')['cases'])==13
r=read(qa/'ENGINE_RESULTS.json');assert len(r['checks'])==11 and all(c['ok']for c in r['checks'])and r['summary']['actualCastContexts']==104
assert r['summary']['matchedMaterialClauses']==22 and r['summary']['motionContexts']==12
examples=read(base/'WORKED_EXAMPLES.json');assert len(examples['examples'])==2
assert examples['researchCorrection']['status']=='hypothesis-rejected-before-publication'
assert len(read(base/'VARIANTS_AND_GAPS.json')['records'])==7
pending=read(root/'research/meihua-layers/PENDING.json');assert not pending['released']and pending['browserChecksExecuted']==0 and not pending['pdfCreated']
for f in pending['candidateFiles']:assert sha((root/'research/meihua-layers/candidate'/f['file']).read_bytes())==f['sha256']
assert not(root/'qa/meihua-layers/BROWSER_RESULTS.json').exists()and not(root/'qa/meihua-layers/body-use-layers.pdf').exists()
state=read(workspace/'EXHAUSTIVE_WORK_STATE.json');assert state==read(root/'research/EXHAUSTIVE_WORK_STATE.json')and state['status']=='active-not-complete'
assert state['currentWork']['latestResearchReport']=='v53/MEIHUA_EXTERNAL_REPORT.md'
full=read(root/'research/full-study/WORK_STATE.json');assert full['latestResearchReport']=='MEIHUA_EXTERNAL_REPORT.md'and full['latestConsumerReport']=='MEIHUA_METHODS_REPORT.md'and full['overallStatus']=='active-not-complete'
coverage=read(root/'research/library-current/COVERAGE.json');assert coverage['counts']['wholeWorkApplied']==0 and coverage['product']['sha256']==sha(html)
v=next(v for v in read(root/'research/meihua/SCAN_STRUCTURE.json')['volumes']if v['volume']==3)
assert(v['titlePDFPage'],v['lastContentPDFPage'],v['endleafPDFPage'],v['lastPrintedPage'])==(103,143,144,42)
out={'sourceAndReferenceChecks':11,'sourcePageRecords':42,'contentPages':41,'newContentPageRecords':27,'expandedContentPageRecords':14,'expandedEndleafRecords':1,
 'physicalUnitLinks':26,'materialClauses':13,'actualCastContexts':104,'matchedMaterialClauses':22,'motionContexts':12,'newPrintedArithmeticExamples':2,'openTextContextIssues':7,
 'newHTTPResponses':0,'newPNGDerivatives':0,'retainedPNGDerivatives':214,'consumerChanged':False,'releasedHTMLBytes':len(html),'releasedHTMLSHA256':sha(html),'webZIPUnchanged':True,'siteClean':True,
 'previousSourceZIPPreserved':True,'previousSourceZIPBytes':835660582,'conditionsReferenceUnchanged':True,'candidateReleased':False,'candidateBrowserChecksExecuted':0,'candidatePDFCreated':False,
 'manifestFilesVerified':len(manifest['files']),'sourceZIPFilesVerified':len(manifest['files'])+1,'predictiveAccuracyEstablished':False,'allVolume3ClausesCompleted':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False}
if '--no-write'in sys.argv:assert read(qa/'RELEASE_RESULTS.json')==out
else:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
