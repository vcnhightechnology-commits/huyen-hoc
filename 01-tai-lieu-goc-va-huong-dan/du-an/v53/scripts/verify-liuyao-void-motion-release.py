from pathlib import Path
from hashlib import sha256
import json,sys,zipfile
root=Path(__file__).resolve().parent.parent;workspace=root.parent;qa=root/'qa/liuyao-void-motion';base=root/'research/liuyao-void-motion';archive=workspace/'archives/v53-before-liuyao-void-motion'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda b:sha256(b).hexdigest()
manifest=read(root/'PACKAGE_MANIFEST.json');old=read(archive/'PACKAGE_MANIFEST.json');html=(root/'Huyen_Hoc_Cac.html').read_bytes()
assert len(html)==707411 and sha(html)==manifest['product']['sha256']==old['product']['sha256']=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html==(workspace/'Huyen_Hoc_Cac.html').read_bytes()==(root/'site/index.html').read_bytes()==(archive/'Huyen_Hoc_Cac.html').read_bytes()
assert sorted(p.name for p in(root/'site').iterdir())==['index.html']
allowed={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'}
immutable=0
for f in old['files']:
 if f['file']not in allowed:assert sha((root/f['file']).read_bytes())==f['sha256'],f['file'];immutable+=1
assert(archive/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==944353384
web=workspace/'Huyen_Hoc_Cac_V53_web.zip';assert web.stat().st_size==344047 and web.read_bytes()==(archive/web.name).read_bytes()
with zipfile.ZipFile(web)as z:assert sorted(z.namelist())==['HUONG_DAN.md','index.html']and z.read('index.html')==html and z.read('HUONG_DAN.md')==(root/'README.md').read_bytes()
assert{p.relative_to(root).as_posix()for p in root.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json'}=={f['file']for f in manifest['files']}
for f in manifest['files']:
 b=(root/f['file']).read_bytes();assert len(b)==f['bytes']and sha(b)==f['sha256'],f['file']
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_source.zip')as z:
 assert set(z.namelist())=={'v53/'+f['file']for f in manifest['files']}|{'v53/PACKAGE_MANIFEST.json'}
 assert z.read('v53/PACKAGE_MANIFEST.json')==(root/'PACKAGE_MANIFEST.json').read_bytes()
 for f in manifest['files']:
  b=z.read('v53/'+f['file']);assert len(b)==f['bytes']and sha(b)==f['sha256'],f['file']
engine=read(qa/'ENGINE_RESULTS.json');s=engine['summary'];assert len(engine['checks'])==16 and all(c['ok']for c in engine['checks'])
assert s=={'actualHHCHexCalls':140,'actualLunarNoonCharts':60,'referenceDistinctDays':60,'branchComparisons':720,'chartContexts':3840,'lineFlags':46080,'voidFlags':7680,'motionContexts':72,'operationalClauses':36,'explicitPremises':16,'phasePositions':18,'unknownFireSlots':2,'graphDigest':'5c18d2063a7b0ea72e7d07cfa6bb7e875b1fbf370208bc8450de8bd49a957192'}
assert engine['htmlSHA256']==sha(html)
manual=read(base/'MANUAL_READINGS.json');assert manual['counts']=={'manualRecordsThisScope':33,'newLocalRenders':25,'expandedPreviouslyRetainedPages':8,'qaCrops':2,'firstPassSpanUnits':14,'uniqueSpanPagesIncludingInherited':38}
assert sha((base/manual['sourcePDF']).read_bytes())==manual['sourceSHA256']
for r in manual['records']:assert sha((base/r['image']).read_bytes())==r['imageSHA256']
for r in manual['qaCrops']:assert sha((base/r['file']).read_bytes())==r['sha256']
toc=read(base/'B02_CURRENT_UNITS.json');assert len(toc['units'])==136 and toc['currentCounts']=={'registeredUnits':136,'regularNumberedUnits':130,'supplements':6,'headingOnlyBodyUnits':103,'partialFoundationUnits':7,'otherPartialUnits':0,'firstPassCompleteSpanUnits':26,'wholeUnitsApplied':0}
assert sha((base/toc['priorTOCFile']).read_bytes())==toc['priorTOCSHA256'];assert read(base/toc['priorTOCFile'])['currentCounts']['headingOnlyBodyUnits']==116
assert next(u for u in toc['units']if u['id']=='B02-ch022')['bodyPrintedHeadingAsRead']=='靜動章第二十二'
requests=read(base/'REQUESTS.json')['records'];assert len(requests)==12 and len([r for r in requests if r.get('error')])==1
for r in requests:
 if r.get('status')==200:
  b=(base/r['file']).read_bytes();assert len(b)==r['bytes']and sha(b)==r['sha256']and r['tls']['authorized']
 else:assert r['error']=='timeout'and not r['responseBodyRetained']and not(base/r['file']).exists()
w=read(base/'INDEPENDENT_WITNESS.json');assert w['transport']['retainedHTTP200Bodies']==11 and w['transport']['retainedBodyBytes']==4810253
assert len(w['manualBoundedSpreadReadings'])==5 and not w['wholeBookRead']and w['comparisonFindings'][-1]['status']=='unresolved'
for r in[*w['manualBoundedSpreadReadings'],*w['navigationOnlyImages'],w['qaCrop']]:assert sha((base/r['file']).read_bytes())==r['sha256']
state=read(workspace/'EXHAUSTIVE_WORK_STATE.json');assert state==read(root/'research/EXHAUSTIVE_WORK_STATE.json')and state['status']=='active-not-complete'and state['currentWork']['latestResearchReport']=='v53/LIUYAO_VOID_MOTION_REPORT.md'
full=read(root/'research/full-study/WORK_STATE.json');assert full['overallStatus']=='active-not-complete'and full['latestResearchReport']=='LIUYAO_VOID_MOTION_REPORT.md'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
coverage=read(root/'research/library-current/COVERAGE.json');assert coverage['counts']['wholeWorkApplied']==0 and coverage['counts']['newDownloadsThisScope']==11 and coverage['counts']['status']=={'inherited_rule_claim':4,'partial_active':5,'research_only':4,'not_established':27}
work=read(base/'WORK_STATE.json');assert work['status']=='private-reference-complete-full-adjudication-and-parallel-sources-active'and work['headingOnlyBodyUnits']==103 and not work['wholeBookApplied']and not work['functionalVoidAdjudication']
assert read(root/'qa/liuyao-day-month/RELEASE_RESULTS.json')['manifestFilesVerified']==2118
for token in[b'void-motion-reference',b'CYCLE_TABLES.json',b'functionalVoidModel',b'INDEPENDENT_WITNESS.json']:assert token not in html
out={'date':'2026-10-27','checks':16,**s,'newOriginalPDFs':0,'newLocalRenders':25,'expandedPriorRecords':8,'manualRecords':33,'qaCrops':3,
 'registeredTOCUnits':136,'newFirstPassUnits':14,'totalFirstPassSpanUnits':26,'headingOnlyBodyUnitsRemaining':103,'retainedNewHTTP200Bodies':11,'HTTPTimeoutsWithoutBody':1,
 'newWitnessRegisteredCanvases':51,'newWitnessBoundedSpreads':5,'PDF52DateVoidConflict':'unresolved','consumerChanged':False,'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,
 'previousSourceZIPPreservedBytes':944353384,'unchangedEarlierV53Files':immutable,'manifestFilesVerified':len(manifest['files']),'sourceZIPFilesVerified':len(manifest['files'])+1,
 'priorFourReferencesPreserved':True,'calendarAdapter':False,'overallStrengthModel':False,'functionalVoidAdjudication':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False}
if '--no-write'in sys.argv:assert read(qa/'RELEASE_RESULTS.json')==out
else:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
