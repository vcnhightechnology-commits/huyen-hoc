from pathlib import Path
from hashlib import sha256
import json,zipfile,sys
root=Path(__file__).resolve().parent.parent;workspace=root.parent
base=root/'research/meihua-volume1';qa=root/'qa/meihua-volume1';archive=workspace/'archives/v53-before-meihua-volume1'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda b:sha256(b).hexdigest()
manifest=read(root/'PACKAGE_MANIFEST.json');old=read(archive/'PACKAGE_MANIFEST.json');html=(root/'Huyen_Hoc_Cac.html').read_bytes()
assert len(html)==703410 and sha(html)==manifest['product']['sha256']==old['product']['sha256']=='3800162854742c915d60f0051c65cadb0eb9a1c803f9f937bf1b6a593c96d268'
assert html==(workspace/'Huyen_Hoc_Cac.html').read_bytes()==(root/'site/index.html').read_bytes()
assert sorted(p.name for p in (root/'site').iterdir())==['index.html']
changed_old={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md','research/meihua-reading/FUNCTIONAL_BACKLOG.json','research/meihua/SCAN_STRUCTURE.json','research/meihua/EXTRACTED_PAGES.json'}
immutable=0
for f in old['files']:
 if f['file']not in changed_old:assert sha((root/f['file']).read_bytes())==f['sha256'],f['file'];immutable+=1
for t in [b'palace-reference',b'PALACE_ROWS',b'FIVE_VOLUME_NAVIGATION',b'TABLE_FIELDS.json',b'<details class="mh-layers']:assert t not in html,t
web=workspace/'Huyen_Hoc_Cac_V53_web.zip';assert web.read_bytes()==(workspace/'archives/v53-before-meihua-layers'/web.name).read_bytes()
with zipfile.ZipFile(web)as z:
 assert sorted(z.namelist())==['HUONG_DAN.md','index.html'];assert z.read('index.html')==html;assert z.read('HUONG_DAN.md')==(root/'README.md').read_bytes()
assert {p.relative_to(root).as_posix()for p in root.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json'}=={f['file']for f in manifest['files']}
for f in manifest['files']:
 b=(root/f['file']).read_bytes();assert len(b)==f['bytes']and sha(b)==f['sha256'],f['file']
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_source.zip')as z:
 assert set(z.namelist())=={'v53/'+f['file']for f in manifest['files']}|{'v53/PACKAGE_MANIFEST.json'}
 assert z.read('v53/PACKAGE_MANIFEST.json')==(root/'PACKAGE_MANIFEST.json').read_bytes()
 for f in manifest['files']:assert sha(z.read('v53/'+f['file']))==f['sha256'],f['file']
assert(archive/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==835703686
with zipfile.ZipFile(archive/'Huyen_Hoc_Cac_V53_source.zip')as z:
 assert z.read('v53/PACKAGE_MANIFEST.json')==(archive/'PACKAGE_MANIFEST.json').read_bytes()
 assert z.read('v53/MEIHUA_EXTERNAL_REPORT.md')==(root/'MEIHUA_EXTERNAL_REPORT.md').read_bytes()
 assert z.read('v53/qa/meihua-external/RELEASE_RESULTS.json')==(root/'qa/meihua-external/RELEASE_RESULTS.json').read_bytes()
 assert z.read('v53/research/meihua/EXTRACTED_PAGES.json')==(archive/'EXTRACTED_PAGES.json').read_bytes()
index=read(root/'research/meihua/EXTRACTED_PAGES.json');baseline=read(base/'SOURCE_BASELINE.json')
assert len(index['pages'])==232 and len(baseline['previousRenderedRecords'])==214
for f in baseline['previousRenderedRecords']:assert next(p for p in index['pages']if p['pdfPage']==f['pdfPage'])==f
manual=read(base/'MANUAL_READINGS.json');assert len(manual['records'])==42 and manual['counts']['newPageRecords']==23
for f in manual['records']:assert sha((base/f['image']).read_bytes())==f['imageSHA256']
assert len(read(base/'UNIT_MAP.json')['units'])==45
fields=read(base/'TABLE_FIELDS.json');assert len(fields['records'])==216 and fields['counts']['pinnedDigitalFields']==214
rows=read(base/'PALACE_ROWS.json');assert len(rows['rows'])==8 and sum(len(r['members'])for r in rows['rows'])==64 and rows['differentNamePositions']==7
engine=read(qa/'ENGINE_RESULTS.json');assert len(engine['checks'])==10 and all(c['ok']for c in engine['checks'])
assert engine['summary']['actualEngineCompositions']==64 and engine['summary']['missingDigitalFields']==2
pending=read(root/'research/meihua-layers/PENDING.json');assert not pending['released']and pending['browserChecksExecuted']==0 and not pending['pdfCreated']
for f in pending['candidateFiles']:assert sha((root/'research/meihua-layers/candidate'/f['file']).read_bytes())==f['sha256']
assert not(root/'qa/meihua-layers/BROWSER_RESULTS.json').exists()and not(root/'qa/meihua-layers/body-use-layers.pdf').exists()
state=read(workspace/'EXHAUSTIVE_WORK_STATE.json');assert state==read(root/'research/EXHAUSTIVE_WORK_STATE.json')and state['status']=='active-not-complete'
assert state['currentWork']['latestResearchReport']=='v53/MEIHUA_VOLUME1_REPORT.md'
full=read(root/'research/full-study/WORK_STATE.json');assert full['latestResearchReport']=='MEIHUA_VOLUME1_REPORT.md'and full['latestConsumerReport']=='MEIHUA_METHODS_REPORT.md'and full['overallStatus']=='active-not-complete'
assert read(root/'research/library-current/COVERAGE.json')['counts']['wholeWorkApplied']==0
nav=read(base/'FIVE_VOLUME_NAVIGATION.json');assert nav['counts']['volumeSpanPages']==212 and nav['counts']['contentPagesIncludingTitleAndClosing']==209
out={'sourceAndReferenceChecks':10,'sourcePageRecords':42,'newPageRecords':23,'expandedEarlierReadings':19,'newPNGDerivatives':18,'retainedPNGDerivatives':232,'digitalUnitLinks':45,
 'physicalHeaderPositions':216,'pinnedDigitalFields':214,'missingDigitalFields':2,'differentHeaderSlots':8,'differentPalaceNamePositions':7,'printedPalaceRows':8,'printedPalaceMembers':64,'actualEngineCompositions':64,'inverseBitKeys':64,
 'fiveVolumeSpanPages':212,'fiveVolumeContentPages':209,'fiveVolumeEndleaves':3,'newHTTPResponses':0,'consumerChanged':False,'releasedHTMLBytes':len(html),'releasedHTMLSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,
 'previousSourceZIPPreserved':True,'previousSourceZIPBytes':835703686,'unchangedEarlierV53Files':immutable,'candidateReleased':False,'candidateBrowserChecksExecuted':0,'candidatePDFCreated':False,
 'manifestFilesVerified':len(manifest['files']),'sourceZIPFilesVerified':len(manifest['files'])+1,'allFieldBodiesCollated':False,'allFiveVolumeClausesCompleted':False,'predictiveAccuracyEstablished':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False}
if '--no-write'in sys.argv:assert read(qa/'RELEASE_RESULTS.json')==out
else:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
