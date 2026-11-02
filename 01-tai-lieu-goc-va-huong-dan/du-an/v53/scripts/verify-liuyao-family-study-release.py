from pathlib import Path
from hashlib import sha256
import json,sys,zipfile

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/liuyao-family-study';q=r/'qa/liuyao-family-study';a=w/'archives/v53-before-liuyao-family-study'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda data:sha256(data).hexdigest()
prepare='--prepare'in sys.argv;old=read(a/'PACKAGE_MANIFEST.json');html=(r/'Huyen_Hoc_Cac.html').read_bytes();resultFile=q/'RELEASE_RESULTS.json'
assert len(old['files'])==3422 and(a/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==2066330215
assert len(html)==707411 and sha(html)==old['product']['sha256']=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html==(w/'Huyen_Hoc_Cac.html').read_bytes()==(r/'site/index.html').read_bytes()==(a/'Huyen_Hoc_Cac.html').read_bytes()
assert [p.name for p in(r/'site').iterdir()]==['index.html']
mutable={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'}
unchanged=0
for f in old['files']:
 if f['file']not in mutable:assert sha((r/f['file']).read_bytes())==f['sha256'],f['file'];unchanged+=1
web=w/'Huyen_Hoc_Cac_V53_web.zip';assert web.stat().st_size==344047 and web.read_bytes()==(a/web.name).read_bytes()
with zipfile.ZipFile(web)as z:assert sorted(z.namelist())==['HUONG_DAN.md','index.html']and z.read('index.html')==html
qa=read(q/'RESULTS.json');src=read(q/'SOURCE_RESULTS.json');candidate=read(r/'research/bazi-jianlu-context/CANDIDATE_STATUS.json')
assert len(qa['checks'])==8 and all(x['ok']for x in qa['checks'])
expected={'actualHHCHexCalls':2,'printedCastFixtures':1,'sourceKinBranchLabels':6,'namedSourceContexts':10,'sourceClassicCoordinates':5,
 'enumeratedPrivateFigureMotionContexts':5120,'roleEntriesWithinEnumeratedContexts':7168,'boundedClauses':35,'viewedSourcePositions':33,
 'newSourceReadPositions':31,'expandedPriorReadPositions':2,'newNativeContentRenders':31,'newHighResolutionQARenders':2,
 'completeFirstPassChapterSpans':11,'workingTOCLabelsCorrected':1,'newHTTPRequests':0,'newOriginalContainers':0}
assert qa['summary']==expected and src['sourceImageHashesVerified']==33 and src['highResolutionQAViewed']
assert len(src['pixelReproductions'])==4 and all(x['pixelMatch']for x in src['pixelReproductions'])
assert src['workingTOCLabelsCorrected']==1 and src['correctionEvidencePDFPages']==[15,235]and not src['sourceEmended']
assert not qa['sourceOutcomesValidated']and not qa['clinicalOrFertilityOrMarriageOrExamClassifier']
assert not candidate['browserTestsPassed']and not candidate['consumerChanged']
work=read(b/'WORK_STATE.json');assert not work['wholeCatalogueCompleted']and not work['wholeChaptersApplied']
units=read(b/'B02_CURRENT_UNITS.json');assert len(units['units'])==136 and units['currentCounts']['headingOnlyBodyUnits']==81 and units['currentCounts']['firstPassCompleteSpanUnits']==47 and units['currentCounts']['wholeUnitsApplied']==0
assert next(x for x in units['units']if x['id']=='B02-ch040')['normalizedHeading']=='趨避'
st=read(w/'EXHAUSTIVE_WORK_STATE.json');assert st==read(r/'research/EXHAUSTIVE_WORK_STATE.json')and st['status']=='active-not-complete'
assert st['currentWork']['latestResearchReport']=='v53/LIUYAO_FAMILY_STUDY_REPORT.md'
cov=read(r/'research/library-current/COVERAGE.json');assert cov['counts']['catalogueRecords']==40 and cov['counts']['wholeWorkApplied']==0 and cov['counts']['newDownloadsThisScope']==0
full=read(r/'research/full-study/WORK_STATE.json');assert full['latestResearchReport']=='LIUYAO_FAMILY_STUDY_REPORT.md'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
assert read(w/'PENDING_RESEARCH_STATE.json')['status']=='Liuyao-family-study-current-scope-active'
assert read(r/'qa/home-tomb-diagrams/RELEASE_RESULTS.json')['manifestFilesVerified']==3422
for term in[b'liuyao-family-study',b'question-reference',b'b02-ch046-classic']:assert term not in html
files=[p for p in r.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json']
if prepare:count=len(files)+(0 if resultFile.exists()else 1)
else:
 m=read(r/'PACKAGE_MANIFEST.json');assert {p.relative_to(r).as_posix()for p in files}=={f['file']for f in m['files']};assert m['product']['sha256']==sha(html)
 for f in m['files']:
  data=(r/f['file']).read_bytes();assert len(data)==f['bytes']and sha(data)==f['sha256'],f['file']
 with zipfile.ZipFile(w/'Huyen_Hoc_Cac_V53_source.zip')as z:
  assert set(z.namelist())=={'v53/'+f['file']for f in m['files']}|{'v53/PACKAGE_MANIFEST.json'}
  assert z.read('v53/PACKAGE_MANIFEST.json')==(r/'PACKAGE_MANIFEST.json').read_bytes()
  for f in m['files']:
   data=z.read('v53/'+f['file']);assert len(data)==f['bytes']and sha(data)==f['sha256'],f['file']
 count=len(m['files'])
out={'date':'2026-10-28','checks':8,**qa['summary'],'sourceImageHashesVerified':33,'highResolutionQAViewed':True,'pixelReproductionRendersVerified':4,
 'sourceEmended':False,'wholeCatalogueCompleted':False,'wholeChaptersApplied':False,'sourceOutcomesValidated':False,'consumerChanged':False,
 'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'previousSourceZIPPreservedBytes':2066330215,
 'unchangedEarlierV53Files':unchanged,'manifestFilesVerified':count,'sourceZIPFilesVerified':count+1}
if prepare:
 resultFile.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'preparedExpectedPayload':True,'manifestFilesAfterPackage':count,'requiresFinalNoWriteVerification':True}))
elif '--no-write'in sys.argv:assert read(resultFile)==out;print(json.dumps(out,ensure_ascii=False))
else:resultFile.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,ensure_ascii=False))
