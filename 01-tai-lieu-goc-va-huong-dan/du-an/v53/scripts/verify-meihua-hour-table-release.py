from pathlib import Path
from hashlib import sha256
import json,sys,zipfile
root=Path(__file__).resolve().parent.parent;workspace=root.parent
base=root/'research/meihua-hour-table';qa=root/'qa/meihua-hour-table';archive=workspace/'archives/v53-before-meihua-hour-table'
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
web=workspace/'Huyen_Hoc_Cac_V53_web.zip';assert web.read_bytes()==(archive/web.name).read_bytes()and web.stat().st_size==344047
assert(archive/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==843408029
with zipfile.ZipFile(web)as z:
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
data=read(base/'HOUR_TABLE.json');assert len(data['rows'])==60 and sum(len(r['cells'])for r in data['rows'])==720
assert data['counts']['status']=={'annotation-read':707,'visibly-unannotated':12,'glyph-open':1}and data['counts']['multiGlyphPositions']==13 and data['counts']['readGlyphs']==721
assert data['newHTTPResponses']==data['newContentPageReadings']==0 and not data['completeSourceInputSemantics']and not data['predictiveAccuracyEstablished']
assert sha((base/data['physicalTranscriptionFile']).read_bytes())==data['physicalTranscriptionSHA256']
assert sha((base/data['historicalIndex']).read_bytes())==data['historicalIndexSHA256']
assert read(root/'research/meihua-volume-map/HOUR_TABLE_INDEX.json')['literalLabelCellsTranscribed']==0
fixtures=read(qa/'CALENDAR_COORDINATE_FIXTURES.json');assert len(fixtures['fixtures'])==fixtures['actualHHCCharts']==fixtures['actualReferenceCharts']==720 and fixtures['notPredictiveValidation']
assert len({f['rowKey']+'/'+f['hourBranch']for f in fixtures['fixtures']})==720
diag=read(qa/'DIAGNOSTICS.json');assert diag['branchOnlyHypothesis']['same']==188 and diag['branchOnlyHypothesis']['different']==388 and diag['introAnchorTransferHypothesis']['matched']==15
assert sum(not r['fullyRead']for r in diag['sourceCenterPositions'])==1
state=read(workspace/'EXHAUSTIVE_WORK_STATE.json');assert state==read(root/'research/EXHAUSTIVE_WORK_STATE.json')and state['status']=='active-not-complete'and state['currentWork']['latestResearchReport']=='v53/MEIHUA_HOUR_TABLE_REPORT.md'
full=read(root/'research/full-study/WORK_STATE.json');assert full['overallStatus']=='active-not-complete'and full['latestResearchReport']=='MEIHUA_HOUR_TABLE_REPORT.md'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
assert read(root/'research/library-current/COVERAGE.json')['counts']['wholeWorkApplied']==0
assert read(root/'research/meihua-layers/PENDING.json')['released']
for t in [b'hour-reference',b'HOUR_TABLE.json',b'PHYSICAL_CELLS',b'SOURCE_PREMISES_AND_GAPS']:assert t not in html
out={'sourceAndReferenceChecks':14,'hourTableRows':60,'branchColumns':12,'recordedPositions':720,'readAnnotationPositions':707,'visiblyUnannotatedPositions':12,'glyphOpenPositions':1,
 'multiGlyphPositions':13,'knownReadGlyphs':721,'confirmedNonSingleCenterRows':9,'rowsWithOpenCenterCount':1,'actualHHCCharts':720,'actualReferenceCharts':720,'sourcePositionsVisited':720,
 'branchOnlyHypothesisComparisons':576,'branchOnlyHypothesisSame':188,'branchOnlyHypothesisDifferent':388,'introAnchorTransferHypothesisMatches':15,'introAnchorTransferHypothesisTotal':20,
 'expandedTablePages':6,'boundedContextPages':2,'newContentPageReadings':0,'newHTTPResponses':0,'nativeQARenders':6,'qaCropsAndNearestZooms':20,
 'consumerChanged':False,'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'previousSourceZIPPreservedBytes':843408029,
 'unchangedEarlierV53Files':immutable,'manifestFilesVerified':len(manifest['files']),'sourceZIPFilesVerified':len(manifest['files'])+1,'allPositionsDispositionRecorded':True,
 'allLiteralAnnotationGlyphsResolved':False,'completeSourceInputSemantics':False,'allFiveVolumeClausesCompleted':False,'predictiveAccuracyEstablished':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False}
if '--no-write'in sys.argv:assert read(qa/'RELEASE_RESULTS.json')==out
else:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
