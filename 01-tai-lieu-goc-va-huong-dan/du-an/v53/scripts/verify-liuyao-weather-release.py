from pathlib import Path
from hashlib import sha256
import json,sys,zipfile

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/liuyao-weather';q=r/'qa/liuyao-weather';a=w/'archives/v53-before-liuyao-weather'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda data:sha256(data).hexdigest()
prepare='--prepare'in sys.argv;old=read(a/'PACKAGE_MANIFEST.json');html=(r/'Huyen_Hoc_Cac.html').read_bytes();resultFile=q/'RELEASE_RESULTS.json'
assert len(old['files'])==3295 and(a/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==2058366890
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
assert len(qa['checks'])==7 and all(x['ok']for x in qa['checks'])
expected={'actualHHCHexCalls':2,'printedCastFixtures':1,'sourceBranchKinLabels':6,'namedSourceMethods':2,'namedQuestionSelectors':5,'privateMotionQuestionContexts':20480,'clearCandidateContrastContexts':3072,
 'boundedClauses':16,'fullChapter35BodyPositions':24,'newWeatherContentPositionsRead':21,'newParatextPositionsRead':1,'newNextChapterOpeningPositionsRead':1,'renderedNotReadPositions':7,'highResolutionQARenders':1,'newHTTPRequests':0,'newOriginalContainers':0}
assert qa['summary']==expected
assert src['sourceImageHashesVerified']==34 and src['promotedViewedPositions']==23 and len(src['reproductions'])==2 and all(x['pixelMatch']for x in src['reproductions'])
assert not candidate['browserTestsPassed']and not candidate['consumerChanged']
assert not qa['wholeChapterApplied']and not qa['meteorologicalModelValidated']
units=read(b/'B02_CURRENT_UNITS.json');assert len(units['units'])==136 and units['currentCounts']['headingOnlyBodyUnits']==95 and units['currentCounts']['firstPassCompleteSpanUnits']==33 and units['currentCounts']['wholeUnitsApplied']==0
st=read(w/'EXHAUSTIVE_WORK_STATE.json');assert st==read(r/'research/EXHAUSTIVE_WORK_STATE.json')and st['status']=='active-not-complete'
assert st['currentWork']['latestResearchReport']=='v53/LIUYAO_WEATHER_ROLES_REPORT.md'
cov=read(r/'research/library-current/COVERAGE.json');assert cov['counts']['catalogueRecords']==40 and cov['counts']['wholeWorkApplied']==0 and cov['counts']['newDownloadsThisScope']==0
full=read(r/'research/full-study/WORK_STATE.json');assert full['latestResearchReport']=='LIUYAO_WEATHER_ROLES_REPORT.md'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
assert read(w/'PENDING_RESEARCH_STATE.json')['status']=='Liuyao-weather-current-scope-active'
assert read(r/'qa/tuvi-masters/RELEASE_RESULTS.json')['manifestFilesVerified']==3295
for term in[b'liuyao-weather',b'weather-reference',b'B02-ch035-JueZi']:assert term not in html
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
out={'date':'2026-10-27','checks':7,**qa['summary'],'sourceImageHashesVerified':34,'pixelReproductionRendersVerified':2,
 'wholeCatalogueCompleted':False,'wholeChapterApplied':False,'meteorologicalModelValidated':False,'consumerChanged':False,
 'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'previousSourceZIPPreservedBytes':2058366890,
 'unchangedEarlierV53Files':unchanged,'manifestFilesVerified':count,'sourceZIPFilesVerified':count+1}
if prepare:
 resultFile.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'preparedExpectedPayload':True,'manifestFilesAfterPackage':count,'requiresFinalNoWriteVerification':True}))
elif '--no-write'in sys.argv:assert read(resultFile)==out;print(json.dumps(out,ensure_ascii=False))
else:resultFile.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,ensure_ascii=False))
