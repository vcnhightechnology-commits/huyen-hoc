from pathlib import Path
from hashlib import sha256
import json,sys,zipfile
root=Path(__file__).resolve().parent.parent;w=root.parent
base=root/'research/liuyao-b03-book4';qa=root/'qa/liuyao-b03-book4';archive=w/'archives/v53-before-liuyao-b03-book4'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda b:sha256(b).hexdigest()
old=read(archive/'PACKAGE_MANIFEST.json');manifest=read(root/'PACKAGE_MANIFEST.json');html=(root/'Huyen_Hoc_Cac.html').read_bytes()
assert len(html)==707411 and sha(html)==old['product']['sha256']==manifest['product']['sha256']=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html==(w/'Huyen_Hoc_Cac.html').read_bytes()==(root/'site/index.html').read_bytes()==(archive/'Huyen_Hoc_Cac.html').read_bytes()
assert sorted(p.name for p in(root/'site').iterdir())==['index.html']
mutable={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'}
unchanged=0
for f in old['files']:
 if f['file']not in mutable:
  assert sha((root/f['file']).read_bytes())==f['sha256'],f['file'];unchanged+=1
assert len(old['files'])==2441 and(archive/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==1391617952
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
e=read(qa/'ENGINE_RESULTS.json');s=e['summary']
assert len(e['checks'])==9 and all(c['ok']for c in e['checks'])and e['htmlSHA256']==sha(html)
assert s=={'actualHHCHexCalls':64,'privatePrimaryMotionContexts':4096,'movingAnnotations':12288,
 'doorKinContexts':1024,'principalDoorContexts':128,'bedContexts':64,'combinationWithoutKinContexts':256,
 'changedBrotherWithoutPrimaryKinContexts':280,'graphDigest':'b1c03df37eee4d47140e7ca24b143444a8bf85ed562035fa949caae678283fc8',
 'manualRecords':67,'contentImagesNewToRelease':65,'coverImagesNewToRelease':2,'inheritedPendingContentImages':17,
 'newContentRendersThisRun':48,'newCoverRendersThisRun':2,'QAOnlyRenders':2,'firstPassMainUnits':11,
 'firstPassNestedSubsections':1,'newOrCompletedMainSpans':7,'boundedOperationalClauses':17}
manual=read(base/'MANUAL_READINGS.json');assert len(manual['records'])==67
assert manual['counts']=={'manualRecords':67,'contentImagesNewToRelease':65,'coverImagesNewToRelease':2,
 'inheritedPendingContentImages':17,'newContentRendersThisRun':48,'newCoverRendersThisRun':2,'QAOnlyRenders':2,
 'newOriginalPDFsToRelease':1,'retainedHTTPBodiesNewToRelease':2,'newHTTPBodiesThisRun':0}
for r in manual['records']+manual['qaImages']:assert sha((base/r['image']).read_bytes())==r['sha256']
assert sha((base/manual['sourcePDF']).read_bytes())==manual['sourceSHA256']=='5f8bb92f28120fa4c2c4d629ae8bad9f785dc02324f15f285085c99ab7ffadaf'
assert [r['pdfPage']for r in manual['records']]==list(range(1,68))and manual['unviewedPages']==[]and not manual['entireBookApplied']
assert len(read(base/'OPERATIONAL_CLAUSES.json')['clauses'])==17
units=read(base/'BOOK4_CURRENT_UNITS.json');assert len(units['units'])==11 and len(units['subsections'])==1
assert all(u['relevantSpanFirstPassRead']and not u['entireUnitApplied']for u in units['units'])and not units['allSourceClausesApplied']
assert units['counts']['newOrCompletedMainSpans']==7
audit=read(base/'SOURCE_AUDIT.json');assert audit['all67PagesViewedWithRecordedScope']and not audit['wholeBookApplied']and audit['unviewedPages']==[]
state=read(w/'EXHAUSTIVE_WORK_STATE.json');assert state==read(root/'research/EXHAUSTIVE_WORK_STATE.json')and state['status']=='active-not-complete'
assert state['currentWork']['latestResearchReport']=='v53/LIUYAO_B03_BOOK4_REPORT.md'and state['currentWork']['nextSourceLead']['status']=='downloaded-byte-verified-book4-first-pass-page-coverage-complete'
full=read(root/'research/full-study/WORK_STATE.json');assert full['overallStatus']=='active-not-complete'and full['latestResearchReport']=='LIUYAO_B03_BOOK4_REPORT.md'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
coverage=read(root/'research/library-current/COVERAGE.json');assert coverage['counts']['wholeWorkApplied']==0 and coverage['counts']['newDownloadsThisScope']==1
assert coverage['counts']['status']=={'inherited_rule_claim':4,'partial_active':5,'research_only':4,'not_established':27}
assert len(next(c for c in coverage['catalogue']if c['id']=='B03')['localPossession'])==4
work=read(base/'WORK_STATE.json');assert work['all67PagesViewedByRecordedScope']and not work['wholeBookApplied']and not work['wholeCatalogueCompleted']
assert read(w/'PENDING_RESEARCH_STATE.json')['status']=='book4-first-pass-pages-complete-current-scope-active'
toc=read(root/'research/liuyao-void-motion/B02_CURRENT_UNITS.json')['currentCounts'];assert(toc['registeredUnits'],toc['headingOnlyBodyUnits'],toc['firstPassCompleteSpanUnits'])==(136,103,26)
assert read(root/'qa/liuyao-b03-book3/RELEASE_RESULTS.json')['manifestFilesVerified']==2441
for token in[b'home-symbol-reference.mjs',b'BOOK4_CURRENT_UNITS.json',b'HOME_SYMBOL_CLAUSES.json']:assert token not in html
out={'date':'2026-10-27','checks':9,**s,'newHTTPBodiesThisRun':0,'retainedHTTPBodiesNewToRelease':2,
 'newOriginalPDFsToRelease':1,'all67Book4PagesViewedByScope':True,'wholeBookApplied':False,
 'wholeCatalogueCompleted':False,'floorPlanAdapter':False,'sourceOutcomeAdjudicator':False,'consumerChanged':False,
 'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'priorElevenReferencesPreserved':True,
 'previousSourceZIPPreservedBytes':1391617952,'unchangedEarlierV53Files':unchanged,
 'manifestFilesVerified':len(manifest['files']),'sourceZIPFilesVerified':len(manifest['files'])+1}
if '--no-write'in sys.argv:assert read(qa/'RELEASE_RESULTS.json')==out
else:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
