from pathlib import Path
from hashlib import sha256
import json,sys,zipfile
root=Path(__file__).resolve().parent.parent;workspace=root.parent
base=root/'research/meihua-table-bodies';qa=root/'qa/meihua-table-bodies';archive=workspace/'archives/v53-before-meihua-table-bodies'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda b:sha256(b).hexdigest()
html=(root/'Huyen_Hoc_Cac.html').read_bytes();manifest=read(root/'PACKAGE_MANIFEST.json');old=read(archive/'PACKAGE_MANIFEST.json')
assert len(html)==707411 and sha(html)==manifest['product']['sha256']==old['product']['sha256']=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html==(workspace/'Huyen_Hoc_Cac.html').read_bytes()==(root/'site/index.html').read_bytes()==(archive/'Huyen_Hoc_Cac.html').read_bytes()
assert sorted(p.name for p in(root/'site').iterdir())==['index.html']
allowed={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md','research/meihua-reading/FUNCTIONAL_BACKLOG.json','research/meihua/SCAN_STRUCTURE.json'}
immutable=0
for f in old['files']:
 if f['file']not in allowed:assert sha((root/f['file']).read_bytes())==f['sha256'],f['file'];immutable+=1
assert(workspace/'Huyen_Hoc_Cac_V53_web.zip').read_bytes()==(archive/'Huyen_Hoc_Cac_V53_web.zip').read_bytes()
assert(archive/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==840933231
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_web.zip')as z:
 assert sorted(z.namelist())==['HUONG_DAN.md','index.html']and z.read('index.html')==html and z.read('HUONG_DAN.md')==(root/'README.md').read_bytes()
assert {p.relative_to(root).as_posix()for p in root.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json'}=={f['file']for f in manifest['files']}
for f in manifest['files']:
 b=(root/f['file']).read_bytes();assert len(b)==f['bytes']and sha(b)==f['sha256'],f['file']
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_source.zip')as z:
 assert set(z.namelist())=={'v53/'+f['file']for f in manifest['files']}|{'v53/PACKAGE_MANIFEST.json'}
 assert z.read('v53/PACKAGE_MANIFEST.json')==(root/'PACKAGE_MANIFEST.json').read_bytes()
 for f in manifest['files']:
  b=z.read('v53/'+f['file']);assert len(b)==f['bytes']and sha(b)==f['sha256'],f['file']
engine=read(qa/'ENGINE_RESULTS.json');assert len(engine['checks'])==14 and all(c['ok']for c in engine['checks'])and engine['htmlSHA256']==sha(html)
data=read(base/'BODY_COLLATION.json');assert len(data['records'])==216 and data['counts']['normalizedReadingsComplete']==214 and data['counts']['glyphOpenFields']==2
assert data['newHTTPResponses']==data['newContentPages']==0 and data['expandedEarlierPageReadings']==22
assert read(root/'qa/meihua-layers/RELEASE_RESULTS.json')['primaryChecks']==98
pending=read(root/'research/meihua-layers/PENDING.json');assert pending['released']and pending['block']is None
state=read(workspace/'EXHAUSTIVE_WORK_STATE.json');assert state==read(root/'research/EXHAUSTIVE_WORK_STATE.json')and state['status']=='active-not-complete'and state['currentWork']['latestResearchReport']=='v53/MEIHUA_TABLE_BODIES_REPORT.md'
full=read(root/'research/full-study/WORK_STATE.json');assert full['overallStatus']=='active-not-complete'and full['latestResearchReport']=='MEIHUA_TABLE_BODIES_REPORT.md'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
assert read(root/'research/library-current/COVERAGE.json')['counts']['wholeWorkApplied']==0
for token in [b'BODY_COLLATION',b'table-reference',b'VARIANTS_AND_LIMITS']:assert token not in html
out={'sourceAndReferenceChecks':14,'physicalBodyPositions':216,'normalizedReadingsComplete':214,'glyphOpenFields':2,'comparison':data['counts']['comparison'],'disposition':data['counts']['disposition'],
 'actualEngineStructures':384,'sourceFieldJoins':2688,'actualDirectionInspectCases':8,'expandedEarlierPageReadings':22,'newContentPageReadings':0,'newHTTPResponses':0,'nativeQARenders':7,'glyphCrops':12,
 'consumerChanged':False,'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'previousSourceZIPPreservedBytes':840933231,
 'unchangedEarlierV53Files':immutable,'manifestFilesVerified':len(manifest['files']),'sourceZIPFilesVerified':len(manifest['files'])+1,'allGlyphsResolved':False,'fullCriticalEditionComplete':False,
 'allFiveVolumeClausesCompleted':False,'predictiveAccuracyEstablished':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False}
if '--no-write'in sys.argv:assert read(qa/'RELEASE_RESULTS.json')==out
else:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
