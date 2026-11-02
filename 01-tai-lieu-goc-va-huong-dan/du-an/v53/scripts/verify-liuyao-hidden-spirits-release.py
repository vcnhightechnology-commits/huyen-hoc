from pathlib import Path
from hashlib import sha256
import json,sys,zipfile
root=Path(__file__).resolve().parent.parent;workspace=root.parent
base=root/'research/liuyao-hidden-spirits';qa=root/'qa/liuyao-hidden-spirits';archive=workspace/'archives/v53-before-liuyao-hidden-spirits'
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
assert(archive/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==939193715
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
s=engine['summary'];assert s['actualHHCHexCalls']==649 and s['queries']==320 and s['rootPositions']==384 and s['coincidences']==144 and s['missingKinQueries']==56
assert s['graphDigest']=='8aa15279f12cc062ba126cedf22d738eaaf099d6e832a8ef66d70cc96978c4ca'
toc=read(base/'B02_TOC_UNITS.json');assert len(toc['units'])==135 and len([u for u in toc['units']if not u['supplement']])==130
assert len([u for u in toc['units']if u['disposition']=='heading-only-body-extraction-open'])==127
assert sha((base/toc['sourcePDF']).read_bytes())==toc['sourceSHA256']
manual=read(base/'MANUAL_READINGS.json');assert len(manual['records'])==22 and manual['counts']['newRetainedSourceRenders']==21
assert manual['newHTTPResponses']==manual['newOriginalPDFs']==0
for r in manual['records']:assert sha((base/r['image']).read_bytes())==r['imageSHA256']
conditions=read(base/'CONDITIONS.json');assert len(conditions['clauses'])==11 and len(conditions['factualInputs'])==16
fixtures=read(base/'SOURCE_FIXTURES.json');assert len(fixtures['cases'])==6 and fixtures['cases'][4]['number']==41 and fixtures['cases'][4]['visibleLines']==[1]
state=read(workspace/'EXHAUSTIVE_WORK_STATE.json');assert state==read(root/'research/EXHAUSTIVE_WORK_STATE.json')and state['status']=='active-not-complete'and state['currentWork']['latestResearchReport']=='v53/LIUYAO_HIDDEN_SPIRITS_REPORT.md'
assert state['previousMaiHoaWork']['latestResearchReport']=='v53/MEIHUA_HOUR_TABLE_REPORT.md'
full=read(root/'research/full-study/WORK_STATE.json');assert full['overallStatus']=='active-not-complete'and full['latestResearchReport']=='LIUYAO_HIDDEN_SPIRITS_REPORT.md'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
coverage=read(root/'research/library-current/COVERAGE.json');assert coverage['counts']['wholeWorkApplied']==0 and coverage['counts']['status']=={'inherited_rule_claim':4,'partial_active':5,'research_only':4,'not_established':27}
assert read(base/'WORK_STATE.json')['status']=='private-reference-complete-calendar-and-full-study-active'
prior=read(root/'qa/liuyao-foundations/RELEASE_RESULTS.json');assert prior['sourceAndRuntimeChecks']==16 and prior['manifestFilesVerified']==2013 and not prior['wholeBooksApplied']
for t in [b'hidden-reference',b'flyingGeneratesHidden',b'B02_TOC_UNITS.json']:assert t not in html
out={'date':'2026-10-27','sourceAndRuntimeChecks':14,'newHTTPResponses':0,'newOriginalPDFs':0,'newLocalSourceRenders':21,'expandedPriorTOCPage':1,'manualImageRecords':22,
 'tocEntries':135,'regularNumberedUnits':130,'repeatedNumberSupplements':5,'headingOnlyBodyUnitsRemaining':127,'firstPassChapter':28,'chapterSpanPages':9,
 'sourceCases':6,'hexagramKinQueries':320,'rootReferencePositions':384,'coincidentVisibleBranches':144,'queriesWithMissingVisibleKin':56,'actualHHCHexCalls':649,
 'conditionClauses':11,'explicitFactualPremises':16,'threeValuedUnknownPreserved':True,'automaticUsefulGodSelection':False,'graphDigest':s['graphDigest'],
 'consumerChanged':False,'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'previousSourceZIPPreservedBytes':939193715,
 'unchangedEarlierV53Files':immutable,'manifestFilesVerified':len(manifest['files']),'sourceZIPFilesVerified':len(manifest['files'])+1,
 'priorFoundationPreserved':True,'fullLiuYaoImplemented':False,'allBookClausesCompleted':False,'outcomeClaimsValidated':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False}
if '--no-write'in sys.argv:assert read(qa/'RELEASE_RESULTS.json')==out
else:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
