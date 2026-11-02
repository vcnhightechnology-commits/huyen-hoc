from pathlib import Path
from hashlib import sha256
import json,sys,zipfile
root=Path(__file__).resolve().parent.parent;w=root.parent;base=root/'research/liuyao-b03-line-labels';qa=root/'qa/liuyao-b03-line-labels'
archive=w/'archives/v53-before-liuyao-b03-all-annotations';read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda b:sha256(b).hexdigest()
old=read(archive/'PACKAGE_MANIFEST.json');manifest=read(root/'PACKAGE_MANIFEST.json');html=(root/'Huyen_Hoc_Cac.html').read_bytes()
assert len(html)==707411 and sha(html)==old['product']['sha256']==manifest['product']['sha256']=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html==(w/'Huyen_Hoc_Cac.html').read_bytes()==(root/'site/index.html').read_bytes()==(archive/'Huyen_Hoc_Cac.html').read_bytes()
assert sorted(p.name for p in(root/'site').iterdir())==['index.html']
mutable={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'}
unchanged=0
for f in old['files']:
 if f['file']not in mutable:assert sha((root/f['file']).read_bytes())==f['sha256'],f['file'];unchanged+=1
assert len(old['files'])==2751 and(archive/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==1988642475
web=w/'Huyen_Hoc_Cac_V53_web.zip';assert web.stat().st_size==344047 and web.read_bytes()==(archive/web.name).read_bytes()
with zipfile.ZipFile(web)as z:assert sorted(z.namelist())==['HUONG_DAN.md','index.html']and z.read('index.html')==html
assert{p.relative_to(root).as_posix()for p in root.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json'}=={f['file']for f in manifest['files']}
for f in manifest['files']:
 b=(root/f['file']).read_bytes();assert len(b)==f['bytes']and sha(b)==f['sha256'],f['file']
with zipfile.ZipFile(w/'Huyen_Hoc_Cac_V53_source.zip')as z:
 assert set(z.namelist())=={'v53/'+f['file']for f in manifest['files']}|{'v53/PACKAGE_MANIFEST.json'}
 assert z.read('v53/PACKAGE_MANIFEST.json')==(root/'PACKAGE_MANIFEST.json').read_bytes()
 for f in manifest['files']:
  b=z.read('v53/'+f['file']);assert len(b)==f['bytes']and sha(b)==f['sha256'],f['file']
e=read(qa/'ENGINE_RESULTS.json');s=e['summary'];assert len(e['checks'])==8 and all(c['ok']for c in e['checks'])and e['htmlSHA256']==sha(html)
assert s=={'actualHHCHexCalls':72,'privatePrimaryRows':384,'sourceFigures':64,'shiYingPositions':128,'hiddenKinCoordinates':56,
 'privateAvailabilityQueries':320,'expandedBook1SourcePages':26,'expandedBook6SourcePages':3,'QAOnlySourceRenders':5,'QACrops':6,'splitColumnFigures':6,
 'newBook6PrintedCastFixtures':4,'actualHHCPrintedCastCalls':8,'printedOwnChangeBranchCoordinates':6,'privateSupportContextChecks':5,
 'actualLunarCalls':4,'cumulativeBook6PrintedCastFixtures':6}
manual=read(base/'MANUAL_READINGS.json');assert [r['pdfPage']for r in manual['records']]==list(range(34,60))
for r in manual['records']+manual['qaImages']:assert sha((base/r['image']).read_bytes())==r['sha256']
assert sha((base/manual['sourcePDF']).read_bytes())==manual['sourceSHA256']=='5dcd7b5005b1e86f441a9350eefb7c0e9e628c47ab926b2a7d1bdd6691a4773d'
source=read(base/'PRINTED_LINE_ROWS.json');assert len(source['records'])==64 and sum(len(r['hidden'])for r in source['records'])==56
assert source['all384PrimaryStemBranchKinRowsCollated']and not source['all384AnnotationsCollated']and not source['allGuaShenLabelsCollated']
q3=read(base/'BOOK6_QUESTION3_FIXTURES.json');assert len(q3['fixtures'])==4 and q3['TOCQuestion3StatedCount']==4
for r in q3['manualImages']+q3['qaImages']:assert sha((base/r['image']).read_bytes())==r['sha256']
assert sha((base/q3['sourcePDF']).read_bytes())==q3['sourcePDFSHA256']=='1d6c656828533ac52ae1fd4ff06cc3c025db98ae5458dc686eda2a6b1d11f07f'
assert not q3['sourceHistoricalOutcomesValidated']and not q3['all131Book6ExamplesIndependentlyCounted']
state=read(w/'EXHAUSTIVE_WORK_STATE.json');assert state==read(root/'research/EXHAUSTIVE_WORK_STATE.json')and state['status']=='active-not-complete'
assert state['currentWork']['latestResearchReport']=='v53/LIUYAO_B03_LINE_LABELS_REPORT.md'
full=read(root/'research/full-study/WORK_STATE.json');assert full['overallStatus']=='active-not-complete'and full['latestResearchReport']=='LIUYAO_B03_LINE_LABELS_REPORT.md'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
coverage=read(root/'research/library-current/COVERAGE.json');assert coverage['counts']['wholeWorkApplied']==0 and coverage['counts']['newDownloadsThisScope']==0
assert coverage['counts']['status']=={'inherited_rule_claim':4,'partial_active':5,'research_only':4,'not_established':27}
assert len(next(c for c in coverage['catalogue']if c['id']=='B03')['localPossession'])==6
assert read(w/'PENDING_RESEARCH_STATE.json')['status']=='book1-primary-line-label-fixtures-current-scope-active'
assert not read(base/'WORK_STATE.json')['wholeBookApplied']
toc=read(root/'research/liuyao-void-motion/B02_CURRENT_UNITS.json')['currentCounts'];assert(toc['registeredUnits'],toc['headingOnlyBodyUnits'],toc['firstPassCompleteSpanUnits'])==(136,103,26)
assert read(root/'qa/liuyao-b03-book1-tables/RELEASE_RESULTS.json')['manifestFilesVerified']==2751
for token in[b'PRINTED_LINE_ROWS.json',b'liuyao-b03-line-labels']:assert token not in html
out={'date':'2026-10-27','checks':8,**s,'newHTTPBodiesThisRun':0,'newOriginalPDFsToRelease':0,
 'all384PrimaryLineLabelsCollated':True,'all384AnnotationsCollated':False,'allGuaShenLabelsCollated':False,
 'wholeBookApplied':False,'wholeCatalogueCompleted':False,'consumerChanged':False,
 'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'priorFifteenReferencesPreserved':True,
 'previousSourceZIPPreservedBytes':1988642475,'unchangedEarlierV53Files':unchanged,
 'manifestFilesVerified':len(manifest['files']),'sourceZIPFilesVerified':len(manifest['files'])+1}
if '--no-write'in sys.argv:assert read(qa/'RELEASE_RESULTS.json')==out
else:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
