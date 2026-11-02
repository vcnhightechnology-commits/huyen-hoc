from pathlib import Path
from hashlib import sha256
import json,sys,zipfile

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/liuyao-exam-intent';q=r/'qa/liuyao-exam-intent';a=w/'archives/v53-before-liuyao-exam-intent'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda data:sha256(data).hexdigest()
assert '--prepare'in sys.argv or '--no-write'in sys.argv
prepare='--prepare'in sys.argv;old=read(a/'PACKAGE_MANIFEST.json');assert len(old['files'])==3549
assert(a/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==2075808140
html=(r/'Huyen_Hoc_Cac.html').read_bytes()
assert len(html)==707411 and sha(html)==old['product']['sha256']=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html==(w/'Huyen_Hoc_Cac.html').read_bytes()==(r/'site/index.html').read_bytes()==(a/'Huyen_Hoc_Cac.html').read_bytes()
assert[p.name for p in(r/'site').iterdir()]==['index.html']
mutable={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'}
unchanged=0
for f in old['files']:
 if f['file']not in mutable:
  data=(r/f['file']).read_bytes();assert len(data)==f['bytes']and sha(data)==f['sha256'],f['file'];unchanged+=1
web=w/'Huyen_Hoc_Cac_V53_web.zip';assert web.stat().st_size==344047 and web.read_bytes()==(a/web.name).read_bytes()
with zipfile.ZipFile(web)as z:assert sorted(z.namelist())==['HUONG_DAN.md','index.html']and z.read('index.html')==html
qa=read(q/'RESULTS.json');src=read(q/'SOURCE_RESULTS.json')
assert len(qa['checks'])==8 and all(x['ok']for x in qa['checks'])
expected={'actualHHCHexCalls':2,'printedCastFixtures':1,'sourceKinBranchLabels':6,'sourceChangedBranchLabels':1,'namedSourceContexts':19,'listedPetitionIntentsNotEncoded':5,'explicitMissingScopeCases':58,'newViewedSourcePositions':37,'contentPositions':34,'nonRuleLeaves':3,'firstPassSpansAdded':19,'boundedSourceClauses':31,'highResolutionQAViewed':3,'newHTTPRequests':0,'newOriginalContainers':0}
assert qa['summary']==expected
assert src['sourceImageHashesVerified']==37 and src['highResolutionQAViewed']==3 and len(src['pixelReproductions'])==2
assert src['promotionIdentityHashesVerified']==46 and src['referenceBodyIdenticalExceptImportPath']and src['unitMapEvidenceOnlyRelocated']==19
assert src['firstPassSpansCurrent']==66 and src['remainingHeadingOnlyUnits']==62 and src['otherPartialUnits']==1 and src['chapter68Partial']
assert not src['wholeImageCharactersCollated']and not src['fullConditionalRulesEncoded']and not src['sourceOutcomesValidated']
assert read(r/'qa/tuvi-void-child/RELEASE_RESULTS.json')['manifestFilesVerified']==3549
units=read(b/'B02_CURRENT_UNITS.json');assert units['currentCounts']=={'registeredUnits':136,'regularNumberedUnits':130,'supplements':6,'headingOnlyBodyUnits':62,'partialFoundationUnits':7,'otherPartialUnits':1,'firstPassCompleteSpanUnits':66,'wholeUnitsApplied':0}
assert all(not x['entireUnitApplied']for x in units['units'])
work=read(b/'WORK_STATE.json');assert not work['wholeCatalogueCompleted']and not work['fullConditionalRulesEncoded']and not work['consumerChanged']
state=read(w/'EXHAUSTIVE_WORK_STATE.json');assert state==read(r/'research/EXHAUSTIVE_WORK_STATE.json')and state['status']=='active-not-complete'
assert state['currentWork']['latestResearchReport']=='v53/LIUYAO_EXAM_INTENT_REPORT.md'and state['currentWork']['catalogueID']=='B02'
coverage=read(r/'research/library-current/COVERAGE.json');assert coverage['counts']['catalogueRecords']==40 and coverage['counts']['wholeWorkApplied']==0 and coverage['counts']['newDownloadsThisScope']==0
full=read(r/'research/full-study/WORK_STATE.json');assert full['latestResearchReport']=='LIUYAO_EXAM_INTENT_REPORT.md'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
assert read(w/'PENDING_RESEARCH_STATE.json')['status']=='Liuyao-exam-intent-current-scope-active'
candidate=read(r/'research/bazi-jianlu-context/CANDIDATE_STATUS.json');assert not candidate['browserTestsPassed']and not candidate['consumerChanged']
for term in[b'liuyao-exam-intent',b'intent-reference',b'b02-ch065-practitioner']:assert term not in html
result=q/'RELEASE_RESULTS.json';files=[p for p in r.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json']
if prepare:count=len(files)+(0 if result.exists()else 1)
else:
 manifest=read(r/'PACKAGE_MANIFEST.json');assert{p.relative_to(r).as_posix()for p in files}=={f['file']for f in manifest['files']}
 assert manifest['product']['sha256']==sha(html)
 for f in manifest['files']:
  data=(r/f['file']).read_bytes();assert len(data)==f['bytes']and sha(data)==f['sha256'],f['file']
 with zipfile.ZipFile(w/'Huyen_Hoc_Cac_V53_source.zip')as z:
  assert set(z.namelist())=={'v53/'+f['file']for f in manifest['files']}|{'v53/PACKAGE_MANIFEST.json'}
  assert z.read('v53/PACKAGE_MANIFEST.json')==(r/'PACKAGE_MANIFEST.json').read_bytes()
  for f in manifest['files']:
   data=z.read('v53/'+f['file']);assert len(data)==f['bytes']and sha(data)==f['sha256'],f['file']
 count=len(manifest['files'])
out={'date':'2026-10-28','newChecks':8,**expected,'originalRetainedHTTP200AndTLSVerified':True,'sourceImageHashesVerified':37,'pixelReproductionsVerified':2,'promotionIdentityHashesVerified':46,'referenceBodyIdenticalExceptImportPath':True,
 'firstPassSpansCurrent':66,'remainingHeadingOnlyUnits':62,'partialFoundationUnits':7,'otherPartialUnits':1,'wholeUnitsApplied':0,
 'chapter68Partial':True,'wholeImageCharactersCollated':False,'fullConditionalRulesEncoded':False,'sourceOutcomesValidated':False,'consumerChanged':False,'wholeCatalogueCompleted':False,
 'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'previousSourceZIPPreservedBytes':2075808140,
 'unchangedEarlierV53Files':unchanged,'manifestFilesVerified':count,'sourceZIPFilesVerified':count+1}
if prepare:
 result.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'preparedExpectedPayload':True,'manifestFilesAfterPackage':count,'requiresFinalNoWriteVerification':True}))
else:
 assert read(result)==out;print(json.dumps({'finalReadOnlyVerificationPassed':True,**out},ensure_ascii=False))
