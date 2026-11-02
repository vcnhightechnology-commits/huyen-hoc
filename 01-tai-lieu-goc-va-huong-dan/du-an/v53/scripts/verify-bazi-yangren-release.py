from pathlib import Path
from hashlib import sha256
import json,sys,zipfile

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/bazi-yangren-conditions';q=r/'qa/bazi-yangren-conditions';a=w/'archives/v53-before-bazi-yangren-conditions'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda data:sha256(data).hexdigest()
prepare='--prepare'in sys.argv;old=read(a/'PACKAGE_MANIFEST.json');html=(r/'Huyen_Hoc_Cac.html').read_bytes();resultFile=q/'RELEASE_RESULTS.json'
assert len(old['files'])==3476 and(a/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==2070081817
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
assert len(qa['checks'])==6 and all(x['ok']for x in qa['checks'])
expected={'selectedParentContexts':8,'selectedSubcontexts':59,'selectedCodepoints':1180,'localPredicateAudits':28,'coordinateFacts':6,'declaredOnlyFacts':55,
 'ternaryDeclarationContexts':81,'actualNewHHCBaziCalls':2,'previouslyReadPrintedExamplesReexecuted':2,'newSourcePages':0,'newHTTPRequests':0,'newOriginalContainers':0,'expandedPreviouslyReadSourcePositions':8}
assert qa['summary']==expected and src['sourceImageHashesVerified']==21 and src['nativePNGPixelBuffersVerified']==13
assert src['redecodedNativePixelBuffersVerified']==2 and src['inheritedExactNativeCropsVerified']==2 and src['promotionIdentityHashesVerified']==8
assert not src['sourceEmended']and not src['allImageCharactersCollated']and not src['fullConditionalClassifier']
coord=read(q/'COORDINATE_RESULTS.json');assert len(coord['checks'])==5 and all(x['ok']for x in coord['checks'])and coord['actualHHCBaziCalls']==8 and coord['privateCoordinateLookups']==196
assert not qa['practicalOutcomesValidated']and not qa['automaticStrengthMethodValidated']and not qa['automaticPrecedenceEstablished']and not qa['realPersonDeclaredFactsValidated']
assert not candidate['browserTestsPassed']and not candidate['consumerChanged']
work=read(b/'WORK_STATE.json');assert not work['wholeCatalogueCompleted']and not work['fullConditionalClassifier']and not work['strengthMethodValidated']
units=read(b/'CURRENT_PATTERN_READING_MATRIX.json');yang=next(x for x in units['records']if x['section']=='論陽刃');assert yang['currentFullFirstPassSpan']['editorialContexts']==55 and not yang['currentFullFirstPassSpan']['fullConditionalClassifier']
st=read(w/'EXHAUSTIVE_WORK_STATE.json');assert st==read(r/'research/EXHAUSTIVE_WORK_STATE.json')and st['status']=='active-not-complete'
assert st['currentWork']['latestResearchReport']=='v53/BAZI_YANGREN_CONDITIONS_REPORT.md'
cov=read(r/'research/library-current/COVERAGE.json');assert cov['counts']['catalogueRecords']==40 and cov['counts']['wholeWorkApplied']==0 and cov['counts']['newDownloadsThisScope']==0
full=read(r/'research/full-study/WORK_STATE.json');assert full['latestResearchReport']=='BAZI_YANGREN_CONDITIONS_REPORT.md'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
assert read(w/'PENDING_RESEARCH_STATE.json')['status']=='Bazi-yangren-conditions-current-scope-active'
assert read(r/'qa/liuyao-family-study/RELEASE_RESULTS.json')['manifestFilesVerified']==3476
for term in[b'bazi-yangren-conditions',b'predicate-reference',b'TMTH005-selected-explicit-predicate-audit']:assert term not in html
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
out={'date':'2026-10-28','newPredicateChecks':6,'inheritedCoordinateChecks':5,**qa['summary'],'sourceImageHashesVerified':21,'nativePNGPixelBuffersVerified':13,
 'redecodedNativePixelBuffersVerified':2,'inheritedExactNativeCropsVerified':2,'promotionIdentityHashesVerified':8,'inheritedFirstReadPositionsPromoted':13,
 'sourceEmended':False,'wholeCatalogueCompleted':False,'fullConditionalClassifier':False,'strengthMethodValidated':False,'automaticPrecedenceEstablished':False,'practicalOutcomesValidated':False,'consumerChanged':False,
 'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'previousSourceZIPPreservedBytes':2070081817,
 'unchangedEarlierV53Files':unchanged,'manifestFilesVerified':count,'sourceZIPFilesVerified':count+1}
if prepare:
 resultFile.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'preparedExpectedPayload':True,'manifestFilesAfterPackage':count,'requiresFinalNoWriteVerification':True}))
elif '--no-write'in sys.argv:assert read(resultFile)==out;print(json.dumps(out,ensure_ascii=False))
else:resultFile.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,ensure_ascii=False))
