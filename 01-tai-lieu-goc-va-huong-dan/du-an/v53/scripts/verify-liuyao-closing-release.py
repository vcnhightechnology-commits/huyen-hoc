from pathlib import Path
from hashlib import sha256
import json,sys,zipfile
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/liuyao-closing-context';q=r/'qa/liuyao-closing-context';a=w/'archives/v53-before-liuyao-closing-context'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda data:sha256(data).hexdigest()
assert '--prepare'in sys.argv or '--no-write'in sys.argv
prepare='--prepare'in sys.argv;old=read(a/'PACKAGE_MANIFEST.json');assert len(old['files'])==3663 and(a/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==2085566508
html=(r/'Huyen_Hoc_Cac.html').read_bytes();assert len(html)==707411 and sha(html)==old['product']['sha256']=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html==(w/'Huyen_Hoc_Cac.html').read_bytes()==(r/'site/index.html').read_bytes()==(a/'Huyen_Hoc_Cac.html').read_bytes()
assert[p.name for p in(r/'site').iterdir()]==['index.html']
mutable={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'}
unchanged=0
for f in old['files']:
 if f['file']not in mutable:
  data=(r/f['file']).read_bytes();assert len(data)==f['bytes']and sha(data)==f['sha256'],f['file'];unchanged+=1
web=w/'Huyen_Hoc_Cac_V53_web.zip';assert web.stat().st_size==344047 and web.read_bytes()==(a/web.name).read_bytes()
with zipfile.ZipFile(web)as z:assert sorted(z.namelist())==['HUONG_DAN.md','index.html']and z.read('index.html')==html
closing=read(q/'CLOSING_RESULTS.json');traveler=read(q/'TRAVELER_RESULTS.json');src=read(q/'SOURCE_RESULTS.json')
assert len(closing['checks'])==8 and len(traveler['checks'])==6 and all(x['ok']for x in closing['checks']+traveler['checks'])
expected={'newViewedSourcePositions':44,'newBodyPositions':40,'nonRuleLeaves':4,'expandedPriorTOCPositions':2,'highResolutionQAViewed':4,'newFirstPassSpans':28,'inheritedPriorStagingSpans':20,'currentFirstPassSpans':130,'partialFoundationUnits':7,'wholeUnitsApplied':0,'actualHHCHexCalls':2,'printedCastFixtures':1,'sourceKinBranchLabels':6,'sourceChangedKinBranchLabels':1,'namedHouseContexts':13,'explicitMissingScopeCases':26,'colophonSourcePDFPage':393,'colophonRepublicYear':14,'colophonCommonEraYear':1925,'colophonPrintedMonth':11,'newHTTPRequests':0,'newOriginalContainers':0}
assert closing['summary']==expected and traveler['summary']['actualHHCHexCalls']==2 and traveler['summary']['firstPassSpansAdded']==20
assert src['sourceImagesPromotedVerified']==70 and src['priorStagingImagesPromoted']==26 and src['newViewedSourcePositionsThisTurn']==44
assert src['bodyPositionsPromoted']==65 and src['allNonRuleLeavesPromoted']==5 and src['highResolutionQAViewed']==6
assert len(src['pixelReproductions'])==3 and src['inheritedPriorStagingPixelReproductions']==2 and src['nativeCropsPixelVerified']==2
assert src['promotionIdentityHashesVerified']==90 and src['referenceBodiesIdenticalExceptImportPaths']==2
assert src['firstPassSpansNewlyPackaged']==48 and src['retainedTOCBodyTitleDifferencesAdded']==2 and src['chapter100HeadingUnresolved']
assert not src['sourceEmended']and not src['allImageCharactersCollated']and not src['fullConditionalRulesEncoded']and not src['sourceOutcomesValidated']
assert read(r/'qa/liuyao-commodity-boundary/RELEASE_RESULTS.json')['manifestFilesVerified']==3663
units=read(b/'B02_CURRENT_UNITS.json');assert units['currentCounts']=={'registeredUnits':137,'regularNumberedUnits':130,'supplements':7,'headingOnlyBodyUnits':0,'partialFoundationUnits':7,'otherPartialUnits':0,'firstPassCompleteSpanUnits':130,'wholeUnitsApplied':0}
assert len(units['units'])==137 and all(not x['entireUnitApplied']for x in units['units'])
colophon=read(b/'COLOPHON_AUDIT.json');assert colophon['sourcePDFPage']==393 and colophon['calendarConversion']['commonEraYear']==1925 and not colophon['editionIndependentlyNewWitness']
work=read(b/'WORK_STATE.json');assert not work['wholeCatalogueCompleted']and not work['fullConditionalRulesEncoded']and not work['consumerChanged']
state=read(w/'EXHAUSTIVE_WORK_STATE.json');assert state==read(r/'research/EXHAUSTIVE_WORK_STATE.json')and state['status']=='active-not-complete'
assert state['currentWork']['latestResearchReport']=='v53/LIUYAO_CLOSING_CONTEXT_REPORT.md'and state['currentWork']['catalogueID']=='B02'
coverage=read(r/'research/library-current/COVERAGE.json');assert coverage['counts']['catalogueRecords']==40 and coverage['counts']['wholeWorkApplied']==0 and coverage['counts']['newDownloadsThisScope']==0
entry=next(x for x in coverage['catalogue']if x['id']=='B02');assert entry['currentSourceUnitCounts']['firstPassSpans']==130 and entry['currentSourceUnitCounts']['partialFoundation']==7 and entry['latestColophonEvidence']['sourcePDFPage']==393
full=read(r/'research/full-study/WORK_STATE.json');assert full['latestResearchReport']=='LIUYAO_CLOSING_CONTEXT_REPORT.md'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
assert read(w/'PENDING_RESEARCH_STATE.json')['status']=='Liuyao-closing-context-current-scope-active'
candidate=read(r/'research/bazi-jianlu-context/CANDIDATE_STATUS.json');assert not candidate['browserTestsPassed']and not candidate['consumerChanged']
for term in[b'liuyao-closing-context',b'explicitHouseContext',b'explicitTravelerContext']:assert term not in html
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
out={'date':'2026-10-28','newClosingChecks':8,'inheritedTravelerChecks':6,'closingSummary':expected,'inheritedTravelerSummary':traveler['summary'],
 'sourceImagesPromotedVerified':70,'priorStagingImagesPromoted':26,'bodyPositionsPromoted':65,'highResolutionQAViewed':6,'nativeCropsPixelVerified':2,'newPixelReproductionsVerified':3,'inheritedPriorStagingPixelReproductions':2,
 'promotionIdentityHashesVerified':90,'referenceBodiesIdenticalExceptImportPaths':2,'firstPassSpansNewlyPackaged':48,'retainedTOCBodyTitleDifferencesAdded':2,'chapter100HeadingUnresolved':True,
 'wholeUnitsApplied':0,'allImageCharactersCollated':False,'fullConditionalRulesEncoded':False,'sourceOutcomesValidated':False,'consumerChanged':False,'wholeCatalogueCompleted':False,
 'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'previousSourceZIPPreservedBytes':2085566508,
 'unchangedEarlierV53Files':unchanged,'manifestFilesVerified':count,'sourceZIPFilesVerified':count+1}
if prepare:
 result.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'preparedExpectedPayload':True,'manifestFilesAfterPackage':count,'requiresFinalNoWriteVerification':True}))
else:
 assert read(result)==out;print(json.dumps({'finalReadOnlyVerificationPassed':True,**out},ensure_ascii=False))
