from pathlib import Path
from hashlib import sha256
import json,sys,zipfile

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/home-tomb-diagrams';q=r/'qa/home-tomb-diagrams';a=w/'archives/v53-before-home-tomb-diagrams'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda data:sha256(data).hexdigest()
prepare='--prepare'in sys.argv;old=read(a/'PACKAGE_MANIFEST.json');html=(r/'Huyen_Hoc_Cac.html').read_bytes();resultFile=q/'RELEASE_RESULTS.json'
assert len(old['files'])==3378 and(a/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==2065012551
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
expected={'movementCells':20,'mountainLabels':24,'sourceYearEntries':50,'resolvedMonthSets':19,'unresolvedMonthSets':1,
 'actualLunarYearCharts':60,'actualLunarMonthCharts':60,'privateYearContexts':1440,'privateMonthContexts':2880,
 'expandedPreviouslyReadPages':5,'newHTTPRequests':0,'newOriginalContainers':0,'newSourcePages':0}
assert qa['summary']==expected and src['nativeSourceImageHashesVerified']==5 and src['totalQADerivativesVerified']==22
assert src['exactNativeDiagramCrops']==2 and src['losslessRotationsVerified']==6 and src['nativeSectorCropsVerified']==8 and src['nativeDetailCropsVerified']==6
assert src['targetedWorkingTranscriptionCorrections']==4 and not src['sourceEmended'] and not src['practicalOutcomesValidated']
assert not candidate['browserTestsPassed']and not candidate['consumerChanged']
work=read(b/'WORK_STATE.json');assert not work['wholeCatalogueCompleted']and not work['calendarAdapterEstablished']and not work['sourceAmbiguityRestored']
assert work['summary']['unresolvedMonthSets']==1
st=read(w/'EXHAUSTIVE_WORK_STATE.json');assert st==read(r/'research/EXHAUSTIVE_WORK_STATE.json')and st['status']=='active-not-complete'
assert st['currentWork']['latestResearchReport']=='v53/HOME_TOMB_DIAGRAMS_REPORT.md'
cov=read(r/'research/library-current/COVERAGE.json');assert cov['counts']['catalogueRecords']==40 and cov['counts']['wholeWorkApplied']==0 and cov['counts']['newDownloadsThisScope']==0
full=read(r/'research/full-study/WORK_STATE.json');assert full['latestResearchReport']=='HOME_TOMB_DIAGRAMS_REPORT.md'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
assert read(w/'PENDING_RESEARCH_STATE.json')['status']=='Home-tomb-diagrams-current-scope-active'
assert read(r/'qa/liuyao-life-context/RELEASE_RESULTS.json')['manifestFilesVerified']==3378
for term in[b'home-tomb-diagrams',b'diagram-reference',b'xieji41-49-ordinary-diagram']:assert term not in html
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
out={'date':'2026-10-28','checks':8,**qa['summary'],'nativeSourceImageHashesVerified':5,'totalQADerivativesVerified':22,
 'targetedWorkingTranscriptionCorrections':4,'sourceEmended':False,'calendarAdapterEstablished':False,
 'wholeCatalogueCompleted':False,'practicalOutcomesValidated':False,'consumerChanged':False,
 'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'previousSourceZIPPreservedBytes':2065012551,
 'unchangedEarlierV53Files':unchanged,'manifestFilesVerified':count,'sourceZIPFilesVerified':count+1}
if prepare:
 resultFile.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'preparedExpectedPayload':True,'manifestFilesAfterPackage':count,'requiresFinalNoWriteVerification':True}))
elif '--no-write'in sys.argv:assert read(resultFile)==out;print(json.dumps(out,ensure_ascii=False))
else:resultFile.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,ensure_ascii=False))
