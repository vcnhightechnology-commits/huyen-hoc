from pathlib import Path
from hashlib import sha256
import json,sys,zipfile
root=Path(__file__).resolve().parent.parent;workspace=root.parent
base=root/'research/liuyao-day-month';qa=root/'qa/liuyao-day-month';archive=workspace/'archives/v53-before-liuyao-day-month'
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
assert(archive/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==942482353
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
s=engine['summary'];assert s['actualHHCHexCalls']==140 and s['graphs']==64 and s['edges']==11648 and s['allowed']==3840 and s['blocked']==7808
assert s['graphDigest']=='b76ce9e44f0e8d5d01ef72fe63d1af30c8c3fe38b3b1c2b421da81a3abbfcdd6'
assert s['operationalClauses']==24 and s['monthElementCells']==60 and s['pairComparisons']==144 and s['sourceCases']==6
toc=read(base/'B02_CURRENT_UNITS.json');assert len(toc['units'])==136 and toc['currentCounts']=={'registeredUnits':136,'regularNumberedUnits':130,'supplements':6,'headingOnlyBodyUnits':116,'partialFoundationUnits':7,'otherPartialUnits':1,'firstPassCompleteSpanUnits':12,'wholeUnitsApplied':0}
assert sha((base/toc['priorTOCFile']).read_bytes())==toc['priorTOCSHA256']
assert read(base/toc['priorTOCFile'])['currentCounts']['registeredUnits']==135
assert toc['units'][0]['printedNumber']==1 and len({u['id']for u in toc['units']})==136
manual=read(base/'MANUAL_READINGS.json');assert len(manual['records'])==25 and sum(r['newLocalRender']for r in manual['records'])==19
assert manual['newHTTPResponses']==manual['newOriginalPDFs']==0 and manual['counts']['completeChapterSpanContentPages']==14
assert sha((base/manual['sourcePDF']).read_bytes())==manual['sourceSHA256']
for r in manual['records']:assert sha((base/r['image']).read_bytes())==r['imageSHA256']
month=read(base/'MONTH_PHASE_ROWS.json');assert len(month['rows'])==12 and sum(len(r['cells'])for r in month['rows'])==60
assert not month['calendarBoundariesEstablished']and not month['consumerApplied']
assert month['explicitPrimaryBranchSlots']==12 and month['explicitSecondaryBranchSlots']==16 and month['residualNotes']==3
pairs=read(base/'PAIR_TABLES.json');assert len(pairs['sixClashes']['pairs'])==len(pairs['sixCombinations']['pairs'])==6 and len(pairs['threeCombinations']['records'])==4
clauses=read(base/'OPERATIONAL_CLAUSES.json');assert len(clauses['clauses'])==24
state=read(workspace/'EXHAUSTIVE_WORK_STATE.json');assert state==read(root/'research/EXHAUSTIVE_WORK_STATE.json')and state['status']=='active-not-complete'and state['currentWork']['latestResearchReport']=='v53/LIUYAO_DAY_MONTH_REPORT.md'
full=read(root/'research/full-study/WORK_STATE.json');assert full['overallStatus']=='active-not-complete'and full['latestResearchReport']=='LIUYAO_DAY_MONTH_REPORT.md'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
coverage=read(root/'research/library-current/COVERAGE.json');assert coverage['counts']['wholeWorkApplied']==0 and coverage['counts']['status']=={'inherited_rule_claim':4,'partial_active':5,'research_only':4,'not_established':27}
work=read(base/'WORK_STATE.json');assert work['status']=='private-reference-complete-full-strength-and-calendar-active'and work['headingOnlyBodyUnits']==116
assert not work['calendarAdapter']and not work['overallStrengthModel']and not work['wholeBookApplied']
assert read(root/'qa/liuyao-use-god/RELEASE_RESULTS.json')['manifestFilesVerified']==2082
for t in[b'day-month-reference',b'MONTH_PHASE_ROWS.json',b'monthClashQualifiedByDayOccupancy']:assert t not in html
out={'date':'2026-10-27','sourceAndRuntimeChecks':14,'newHTTPResponses':0,'newOriginalPDFs':0,'newLocalRenders':19,'expandedPriorRecords':6,'manualImageRecords':25,
 'newContentPageReadings':17,'completeSpanContentPages':14,'newFirstPassUnitIDs':['13','14','15','15-supp-a','16','17'],'partialChapter19':True,
 'currentTOCUnits':136,'regularNumbers':130,'supplements':6,'headingOnlyBodyUnitsRemaining':116,'sourceCases':6,'operationalClauses':24,'monthElementCells':60,'monthBranchSlots':28,'residualNotes':3,
 'branchPairComparisons':144,'threeCombinationIdentities':4,'graphs':64,'directedNodePairs':11648,'layerAllowedPairs':3840,'layerBlockedPairs':7808,'actualHHCHexCalls':140,'graphDigest':s['graphDigest'],
 'calendarAdapter':False,'overallStrengthModel':False,'automaticUseGodSelection':False,'consumerChanged':False,'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,
 'previousSourceZIPPreservedBytes':942482353,'unchangedEarlierV53Files':immutable,'manifestFilesVerified':len(manifest['files']),'sourceZIPFilesVerified':len(manifest['files'])+1,'priorThreeReferencesPreserved':True,
 'allBookClausesCompleted':False,'historicalOutcomesValidated':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False}
if '--no-write'in sys.argv:assert read(qa/'RELEASE_RESULTS.json')==out
else:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
