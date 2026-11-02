from pathlib import Path
from hashlib import sha256
import json,sys,zipfile
root=Path(__file__).resolve().parent.parent;workspace=root.parent
base=root/'research/liuyao-use-god';qa=root/'qa/liuyao-use-god';archive=workspace/'archives/v53-before-liuyao-use-god'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda b:sha256(b).hexdigest()
html=(root/'Huyen_Hoc_Cac.html').read_bytes();manifest=read(root/'PACKAGE_MANIFEST.json');old=read(archive/'PACKAGE_MANIFEST.json')
assert len(html)==707411 and sha(html)==manifest['product']['sha256']==old['product']['sha256']=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html==(workspace/'Huyen_Hoc_Cac.html').read_bytes()==(root/'site/index.html').read_bytes()==(archive/'Huyen_Hoc_Cac.html').read_bytes()
assert sorted(p.name for p in(root/'site').iterdir())==['index.html']
allowed={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'}
immutable=0
for f in old['files']:
 if f['file']not in allowed:assert sha((root/f['file']).read_bytes())==f['sha256'],f['file'];immutable+=1
web=workspace/'Huyen_Hoc_Cac_V53_web.zip';assert web.read_bytes()==(archive/web.name).read_bytes()and web.stat().st_size==344047
assert(archive/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==940981182
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
s=engine['summary'];assert s['actualHHCHexCalls']==392 and s['graphs']==384 and s['lineRoleBindings']==2304 and s['edges']==5040
assert s['actualReferenceCharts']==1 and s['sourceDateVoidConflicts']==1 and s['conditionalClauses']==23 and s['explicitFactualInputs']==21
assert s['graphDigest']=='57c930c03025183883f1bfa6c9ed79dc683b7d352e300344c889f9f2a24a75f8'
toc=read(base/'B02_CURRENT_UNITS.json');assert len(toc['units'])==135 and toc['currentCounts']=={'registeredUnits':135,'headingOnlyBodyUnits':122,'partialFoundationUnits':7,'firstPassCompleteSpanUnits':6,'wholeUnitsApplied':0}
assert len([u for u in toc['units']if u['disposition']=='heading-only-body-extraction-open'])==122
assert sha((base/toc['priorTOCFile']).read_bytes())==toc['priorTOCSHA256']
manual=read(base/'MANUAL_READINGS.json');assert len(manual['records'])==13 and manual['counts']['chapterSpanPages']==9 and manual['counts']['chaptersFirstPassRead']==5
assert manual['newHTTPResponses']==manual['newOriginalPDFs']==0
assert sha((base/manual['sourcePDF']).read_bytes())==manual['sourceSHA256']
for r in manual['records']:assert sha((base/r['image']).read_bytes())==r['imageSHA256']
for r in [manual['qaCrop'],manual['dayContextCrop']]:assert sha((base/r['file']).read_bytes())==r['sha256']
conditions=read(base/'CONDITIONS.json');assert len(conditions['clauses'])==23 and not conditions['calendarAndStrengthClassifiersImplemented']and not conditions['outcomeAccuracyEstablished']
subjects=read(base/'SUBJECTS_AND_ROLES.json');assert len(subjects['subjects'])==15 and not subjects['consumerApplied']
fixtures=read(base/'SOURCE_FIXTURES.json');assert fixtures['cases'][0]['movingLines']==[1,3,4,6]and fixtures['cases'][3]['number']==28
assert fixtures['sourceDateConflict']['dateAsRead']=='酉月辛卯日'and fixtures['sourceDateConflict']['status']=='source-date-vs-void-prose-unresolved'
state=read(workspace/'EXHAUSTIVE_WORK_STATE.json');assert state==read(root/'research/EXHAUSTIVE_WORK_STATE.json')and state['status']=='active-not-complete'and state['currentWork']['latestResearchReport']=='v53/LIUYAO_USE_GOD_REPORT.md'
full=read(root/'research/full-study/WORK_STATE.json');assert full['overallStatus']=='active-not-complete'and full['latestResearchReport']=='LIUYAO_USE_GOD_REPORT.md'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
coverage=read(root/'research/library-current/COVERAGE.json');assert coverage['counts']['wholeWorkApplied']==0 and coverage['counts']['status']=={'inherited_rule_claim':4,'partial_active':5,'research_only':4,'not_established':27}
work=read(base/'WORK_STATE.json');assert work['status']=='private-reference-complete-full-conditions-and-calendar-active'and work['headingOnlyUnits']==122
assert not work['automaticUseGodSelection']and not work['calendarStrengthClassifier']and not work['wholeBookApplied']
assert read(root/'qa/liuyao-hidden-spirits/RELEASE_RESULTS.json')['manifestFilesVerified']==2050
for t in [b'use-god-reference',b'SUBJECTS_AND_ROLES.json',b'actorConditions']:assert t not in html
out={'date':'2026-10-27','sourceAndRuntimeChecks':14,'newHTTPResponses':0,'newOriginalPDFs':0,'newLocalSourceRenders':13,'qaCrops':2,'chapterSpanPages':9,'chaptersFirstPassRead':[8,9,10,11,12],
 'tocUnits':135,'headingOnlyBodyUnitsRemaining':122,'subjectCategories':15,'conditionalClauses':23,'explicitFactualPremises':21,'roleTables':5,'sourceCases':4,'graphs':384,'lineRoleBindings':2304,'relationEdges':5040,
 'actualHHCHexCalls':392,'actualReferenceCharts':1,'sourceDateVoidConflicts':1,'graphDigest':s['graphDigest'],'automaticUsefulGodSelection':False,'calendarStrengthClassifier':False,
 'consumerChanged':False,'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'previousSourceZIPPreservedBytes':940981182,
 'unchangedEarlierV53Files':immutable,'manifestFilesVerified':len(manifest['files']),'sourceZIPFilesVerified':len(manifest['files'])+1,'priorTwoReferencesPreserved':True,
 'fullLiuYaoImplemented':False,'allBookClausesCompleted':False,'predictiveAccuracyEstablished':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False}
if '--no-write'in sys.argv:assert read(qa/'RELEASE_RESULTS.json')==out
else:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
