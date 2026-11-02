from pathlib import Path
from hashlib import sha256
import json, zipfile, sys

root=Path(__file__).resolve().parent.parent
workspace=root.parent
base=root/'research/meihua-volume-map'
qa=root/'qa/meihua-volume-map'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda b:sha256(b).hexdigest()
manifest=read(root/'PACKAGE_MANIFEST.json')
archive=workspace/'archives/v53-before-meihua-volume-map'
old=read(archive/'PACKAGE_MANIFEST.json')
html=(root/'Huyen_Hoc_Cac.html').read_bytes()
assert len(html)==703410 and sha(html)==old['product']['sha256']==manifest['product']['sha256']=='3800162854742c915d60f0051c65cadb0eb9a1c803f9f937bf1b6a593c96d268'
assert html==(workspace/'Huyen_Hoc_Cac.html').read_bytes()==(root/'site/index.html').read_bytes()
assert sorted(p.name for p in (root/'site').iterdir())==['index.html']
for f in old['files']:
 if '/' not in f['file'] and f['file'].endswith(('.js','.css')):
  assert sha((root/f['file']).read_bytes())==f['sha256'],f['file']
for tag in [b'MANUAL_READINGS.json',b'HOUR_TABLE_INDEX',b'NLC416',b'mh-layers']:
 assert tag not in html,tag
web=workspace/'Huyen_Hoc_Cac_V53_web.zip'
assert web.read_bytes()==(workspace/'archives/v53-before-meihua-layers'/web.name).read_bytes()
with zipfile.ZipFile(web) as z:
 assert sorted(z.namelist())==['HUONG_DAN.md','index.html']
 assert z.read('index.html')==html and z.read('HUONG_DAN.md')==(root/'README.md').read_bytes()
assert {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.name!='PACKAGE_MANIFEST.json'}=={r['file'] for r in manifest['files']}
for r in manifest['files']:
 b=(root/r['file']).read_bytes();assert len(b)==r['bytes'] and sha(b)==r['sha256'],r['file']
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_source.zip') as z:
 assert set(z.namelist())=={'v53/'+r['file'] for r in manifest['files']}|{'v53/PACKAGE_MANIFEST.json'}
 assert z.read('v53/PACKAGE_MANIFEST.json')==(root/'PACKAGE_MANIFEST.json').read_bytes()
 for r in manifest['files']:assert sha(z.read('v53/'+r['file']))==r['sha256'],r['file']
assert (archive/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==831546206
with zipfile.ZipFile(archive/'Huyen_Hoc_Cac_V53_source.zip') as z:
 assert z.read('v53/PACKAGE_MANIFEST.json')==(archive/'PACKAGE_MANIFEST.json').read_bytes()
 for f in ['research/meihua-witness/MANUAL_READINGS.json','research/meihua-witness/UNIT_MAP.json','qa/meihua-witness/RELEASE_RESULTS.json']:
  assert z.read('v53/'+f)==(root/f).read_bytes(),f
r=read(qa/'SOURCE_RESULTS.json');assert len(r['checks'])==9 and all(c['ok'] for c in r['checks']) and r['htmlSHA256']==sha(html)
manual=read(base/'MANUAL_READINGS.json');assert len(manual['records'])==47
for r in manual['records']:assert sha((base/r['image']).read_bytes())==r['imageSHA256']
units=read(base/'UNIT_MAP.json');assert len(units['units'])==93 and len(units['mappedPDFPages'])==84 and units['contentPages']==82 and units['volumeFourFivePageNavigationComplete'] and not units['wholeBookApplied']
hours=read(base/'HOUR_TABLE_INDEX.json');assert len(hours['rows'])==60 and hours['labelCellPositions']==720 and hours['literalLabelCellsTranscribed']==0
pending=read(root/'research/meihua-layers/PENDING.json');assert not pending['released'] and pending['browserChecksExecuted']==0 and not pending['pdfCreated']
for f in pending['candidateFiles']:assert sha((root/'research/meihua-layers/candidate'/f['file']).read_bytes())==f['sha256']
assert not (root/'qa/meihua-layers/BROWSER_RESULTS.json').exists() and not (root/'qa/meihua-layers/body-use-layers.pdf').exists()
full=read(root/'research/full-study/WORK_STATE.json');assert full['overallStatus']=='active-not-complete' and full['latestConsumerReport']=='MEIHUA_METHODS_REPORT.md' and full['latestResearchReport']=='MEIHUA_VOLUME_MAP_REPORT.md'
state=read(workspace/'EXHAUSTIVE_WORK_STATE.json');assert state==read(root/'research/EXHAUSTIVE_WORK_STATE.json') and state['status']=='active-not-complete'
coverage=read(root/'research/library-current/COVERAGE.json');assert coverage['counts']['wholeWorkApplied']==0 and coverage['product']['sha256']==sha(html)
out={'sourceChecks':9,'actualEngineControls':9,'newBoundedPageRecords':47,'volume4and5NavigationPages':84,'contentPages':82,'endleafPages':2,'priorUnitGroups':34,'newUnitGroups':59,'totalUnitGroups':93,'hourTableRowHeaders':60,'hourTableCellPositions':720,'literalLabelCellsTranscribed':0,'newHTTPResponses':0,'newRenderedDerivatives':0,'consumerChanged':False,'releasedHTMLBytes':len(html),'releasedHTMLSHA256':sha(html),'webZIPUnchanged':True,'previousSourceZIPPreserved':True,'previousSourceZIPBytes':831546206,'siteClean':True,'candidateReleased':False,'candidateBrowserChecksExecuted':0,'candidatePDFCreated':False,'manifestFilesVerified':len(manifest['files']),'sourceZIPFilesVerified':len(manifest['files'])+1,'wholeBookRead':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False}
if '--no-write' in sys.argv:assert read(qa/'RELEASE_RESULTS.json')==out
else:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
