from pathlib import Path
from hashlib import sha256
import json,sys,zipfile
root=Path(__file__).resolve().parent.parent;w=root.parent;base=root/'research/liuyao-b03-book6';qa=root/'qa/liuyao-b03-book6'
archive=w/'archives/v53-before-liuyao-b03-book6';read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda b:sha256(b).hexdigest()
old=read(archive/'PACKAGE_MANIFEST.json');manifest=read(root/'PACKAGE_MANIFEST.json');html=(root/'Huyen_Hoc_Cac.html').read_bytes()
assert len(html)==707411 and sha(html)==old['product']['sha256']==manifest['product']['sha256']=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html==(w/'Huyen_Hoc_Cac.html').read_bytes()==(root/'site/index.html').read_bytes()==(archive/'Huyen_Hoc_Cac.html').read_bytes()
assert sorted(p.name for p in(root/'site').iterdir())==['index.html']
mutable={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'}
unchanged=0
for f in old['files']:
 if f['file']not in mutable:assert sha((root/f['file']).read_bytes())==f['sha256'],f['file'];unchanged+=1
assert len(old['files'])==2599 and(archive/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==1711630083
web=w/'Huyen_Hoc_Cac_V53_web.zip';assert web.stat().st_size==344047 and web.read_bytes()==(archive/web.name).read_bytes()
with zipfile.ZipFile(web)as z:
 assert sorted(z.namelist())==['HUONG_DAN.md','index.html']and z.read('index.html')==html and z.read('HUONG_DAN.md')==(root/'README.md').read_bytes()
assert{p.relative_to(root).as_posix()for p in root.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json'}=={f['file']for f in manifest['files']}
for f in manifest['files']:
 b=(root/f['file']).read_bytes();assert len(b)==f['bytes']and sha(b)==f['sha256'],f['file']
with zipfile.ZipFile(w/'Huyen_Hoc_Cac_V53_source.zip')as z:
 assert set(z.namelist())=={'v53/'+f['file']for f in manifest['files']}|{'v53/PACKAGE_MANIFEST.json'}
 assert z.read('v53/PACKAGE_MANIFEST.json')==(root/'PACKAGE_MANIFEST.json').read_bytes()
 for f in manifest['files']:
  b=z.read('v53/'+f['file']);assert len(b)==f['bytes']and sha(b)==f['sha256'],f['file']
e=read(qa/'ENGINE_RESULTS.json');s=e['summary'];assert len(e['checks'])==8 and all(c['ok']for c in e['checks'])and e['htmlSHA256']==sha(html)
assert s=={'actualHHCHexCalls':68,'actualHHCIdentityCalls':64,'printedFixtureCount':2,'printedHHCHexCalls':4,
 'privateSelectedLineMotionContexts':24576,'candidateOrigins':28672,'staticOrigins':14336,'movingOrigins':14336,
 'ownChangeControlCautions':3328,'changedOnlySupportNotSubstituted':9920,
 'graphDigest':'b06fdde14f7891a441ace820e9d6dfd6127d6c819680b6e53d50c5005d1f3398','manualRecords':65,
 'contentPages':63,'coverPages':2,'inheritedPendingContentPages':7,'inheritedPendingCoverPages':1,
 'newContentRendersThisRun':56,'newCoverRendersThisRun':1,'QAOnlyRenders':2,'firstPassAvailableQuestionSpans':18,'boundedOperationalClauses':18}
manual=read(base/'MANUAL_READINGS.json');assert [r['pdfPage']for r in manual['records']]==list(range(1,66))
assert manual['counts']=={'manualRecords':65,'contentPages':63,'coverPages':2,'inheritedPendingContentPages':7,
 'inheritedPendingCoverPages':1,'newContentRendersThisRun':56,'newCoverRendersThisRun':1,'QAOnlyRenders':2}
for r in manual['records']+manual['qaImages']:assert sha((base/r['image']).read_bytes())==r['sha256']
assert sha((base/manual['sourcePDF']).read_bytes())==manual['sourceSHA256']=='1d6c656828533ac52ae1fd4ff06cc3c025db98ae5458dc686eda2a6b1d11f07f'
assert manual['unviewedPages']==[]and not manual['entireBookApplied']and not manual['directPrintedFinalColophonEstablished']
units=read(base/'BOOK6_CURRENT_UNITS.json');assert len(units['units'])==18 and all(u['availableSourceSpanFirstPassRead']and not u['entireUnitApplied']for u in units['units'])
assert not units['allSourceClausesApplied']and len(read(base/'OPERATIONAL_CLAUSES.json')['clauses'])==18
assert read(base/'PRINTED_FIXTURES.json')['fixtureCount']==2
state=read(w/'EXHAUSTIVE_WORK_STATE.json');assert state==read(root/'research/EXHAUSTIVE_WORK_STATE.json')and state['status']=='active-not-complete'
assert state['currentWork']['latestResearchReport']=='v53/LIUYAO_B03_BOOK6_REPORT.md'and state['currentWork']['nextSourceLead']['status']=='all-six-same-series-PDFs-retained-book6-available-page-coverage-complete'
full=read(root/'research/full-study/WORK_STATE.json');assert full['overallStatus']=='active-not-complete'and full['latestResearchReport']=='LIUYAO_B03_BOOK6_REPORT.md'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
coverage=read(root/'research/library-current/COVERAGE.json');assert coverage['counts']['wholeWorkApplied']==0 and coverage['counts']['newDownloadsThisScope']==1
assert coverage['counts']['status']=={'inherited_rule_claim':4,'partial_active':5,'research_only':4,'not_established':27}
assert len(next(c for c in coverage['catalogue']if c['id']=='B03')['localPossession'])==6
work=read(base/'WORK_STATE.json');assert work['all65PagesViewedByRecordedScope']and work['allSixSameSeriesPDFsRetained']and not work['wholeBookApplied']and not work['wholeCatalogueCompleted']
assert read(w/'PENDING_RESEARCH_STATE.json')['status']=='book6-available-pages-complete-current-scope-active'
toc=read(root/'research/liuyao-void-motion/B02_CURRENT_UNITS.json')['currentCounts'];assert(toc['registeredUnits'],toc['headingOnlyBodyUnits'],toc['firstPassCompleteSpanUnits'])==(136,103,26)
assert read(root/'qa/liuyao-b03-book5/RELEASE_RESULTS.json')['manifestFilesVerified']==2599
for token in[b'support-chain-reference.mjs',b'BOOK6_CURRENT_UNITS.json',b'SUPPORT_CHAIN_CLAUSE.json']:assert token not in html
out={'date':'2026-10-27','checks':8,**s,'newHTTPBodiesThisRun':2,'retainedHTTPBodiesNewToRelease':2,'newOriginalPDFsToRelease':1,
 'all65Book6ImagesViewedByScope':True,'allSixSameSeriesPDFsRetained':True,'wholeBookApplied':False,'wholeCatalogueCompleted':False,
 'directPrintedFinalColophonEstablished':False,'effectiveSupportAdjudicator':False,'consumerChanged':False,
 'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'priorThirteenReferencesPreserved':True,
 'previousSourceZIPPreservedBytes':1711630083,'unchangedEarlierV53Files':unchanged,
 'manifestFilesVerified':len(manifest['files']),'sourceZIPFilesVerified':len(manifest['files'])+1}
if '--no-write'in sys.argv:assert read(qa/'RELEASE_RESULTS.json')==out
else:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
