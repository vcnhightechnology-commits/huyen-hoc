from pathlib import Path
from hashlib import sha256
from PIL import Image
import json,zipfile,sys
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/liuyao-foundation-span';q=r/'qa/liuyao-foundation-span';prepare='--prepare'in sys.argv
assert prepare or'--no-write'in sys.argv
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda x:sha256(x).hexdigest()
m=read(b/'SOURCE_MANIFEST.json');pdf=w/m['sourcePDF'];assert pdf.stat().st_size==m['sourceBytes']==11089308 and sha(pdf.read_bytes())==m['sourceSHA256']=='caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa'
request=next(x for x in read(r/'research/liuyao-foundations/REQUESTS.json')['records']if x['file']==pdf.name);assert request['status']==200 and request['tls']['authorized']and request['sha256']==m['sourceSHA256']
assert[x['pdfPage']for x in m['records']]==list(range(21,49))
for x in m['records']:
 p=w/x['file'];assert x['actuallyViewed']and not x['newSourcePosition']and p.stat().st_size==x['bytes']and sha(p.read_bytes())==x['sha256']and Image.open(p).size==tuple(x['size'])
for x in read(q/'QA_RENDERS.json')['records']:
 a=q/x['qaFile'];c=q/x['cropFile'];assert sha(a.read_bytes())==x['qaSHA256']and sha(c.read_bytes())==x['cropSHA256']and x['cropActuallyViewed']and not x['fullQAActuallyViewed']
 im=Image.open(a).convert('RGB').crop(x['cropBox']);actual=Image.open(c).convert('RGB');assert im.size==actual.size and im.tobytes()==actual.tobytes()
crop=read(q/'MOTION_CROP.json');im=Image.open(w/crop['source']).convert('RGB').crop(crop['cropBox']);actual=Image.open(q/crop['cropFile']).convert('RGB');assert crop['actuallyViewed']and crop['pixelMatch']and sha((w/crop['source']).read_bytes())==crop['sourceSHA256']and sha((q/crop['cropFile']).read_bytes())==crop['cropSHA256']and im.size==actual.size and im.tobytes()==actual.tobytes()
source=read(q/'SOURCE_RESULTS.json');assert len(source['pixelReproductions'])==2
for x in source['pixelReproductions']:
 p=q/x['file'];assert sha(p.read_bytes())==x['sha256']and x['pixelMatch'];target=r/'research/liuyao-foundations/images/zengshan-26.png'if x['pdfPage']==26 else q/'qa360-29.png';a=Image.open(p).convert('RGB');e=Image.open(target).convert('RGB');assert a.size==e.size and a.tobytes()==e.tobytes()
ids=read(b/'PROMOTION_IDENTITIES.json');assert len(ids['records'])==28 and len(ids['referenceImportRelocations'])==2
for x in ids['records']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p.read_bytes())==x['sha256']
for x in ids['referenceImportRelocations']:
 a=w/x['stagedFile'];e=w/x['promotedFile'];assert sha(a.read_bytes())==x['stagedSHA256']and sha(e.read_bytes())==x['promotedSHA256'];t=a.read_text(encoding='utf-8');assert t.count(x['oldImport'])==1 and t.replace(x['oldImport'],x['newImport'])==e.read_text(encoding='utf-8')
comparison=read(q/'DIAGRAM_COMPARISON.json');assert sha((b/'PRINTED_DIAGRAMS.json').read_bytes())==comparison['sourceRowsSHA256'];assert comparison['actualHHCHexCalls']==64 and comparison['printedLineRows']==384 and comparison['workingBranchNormalizations']==32
assert[(x['number'],x['line'],x['field'],x['source'],x['reference'])for x in comparison['differences']]==[(20,3,'element','土','木'),(61,2,'kin','兄弟','官鬼'),(5,1,'kin','父母','妻財')]
assert len(comparison['records'])==64 and len({x['identity']['actualHHCNumber']for x in comparison['records']})==64
for x in comparison['records']:
 a=x['identity'];assert a['sourceNumber']==a['actualHHCNumber']==a['privateNumber']and a['sourcePalace']==a['privatePalace']and a['sourceShi']==a['privateShi']and a['sourceYing']==a['privateYing']
result=read(q/'RESULTS.json');assert len(result['checks'])==7 and all(x['ok']for x in result['checks']);assert result['summary']['totalActualHHCHexCallsThisScope']==66 and result['summary']['sourceChangedLabels']==4
f=read(b/'MOTION_FIXTURES.json');assert f['sixLineExample']['values']==[9,7,9,6,7,6]and len(f['threeLineExamples'])==4
assert f['sixLineExample']['primaryBranchKinBottomToTop'][0]==['子','妻財']and f['sixLineExample']['baseLine1MatchesReferenceButDiffersFromTable33']
u=read(b/'B02_CURRENT_UNITS.json');assert len(u['units'])==137 and u['currentCounts']['firstPassCompleteSpanUnits']==137 and u['currentCounts']['partialFoundationUnits']==0 and all(not x['entireUnitApplied']for x in u['units']);assert len(read(b/'MANUAL_READINGS.json')['chapterRanges'])==7
assert len(read(b/'FOUNDATIONAL_CONTEXTS.json')['clauses'])==27
assert read(r/'research/liuyao-closing-context/B02_CURRENT_UNITS.json')['currentCounts']['partialFoundationUnits']==7
current=read(r/'research/library-current/COVERAGE.json');assert current['counts']['catalogueRecords']==40 and current['counts']['wholeWorkApplied']==0;assert next(x for x in current['catalogue']if x['id']=='B02')['currentSourceUnitCounts']['firstPassSpans']==137
rootstate=read(w/'EXHAUSTIVE_WORK_STATE.json');assert rootstate==read(r/'research/EXHAUSTIVE_WORK_STATE.json')and rootstate['currentWork']['latestResearchReport']=='v53/LIUYAO_FOUNDATION_SPAN_REPORT.md'
archive=w/'archives/v53-before-liuyao-foundation-span';snapshot=read(archive/'SNAPSHOT.json');assert snapshot['sourceManifestFiles']==3778 and snapshot['sourceZIPBytes']==2095344337
for x in snapshot['files']:
 p=archive/x['file'];assert p.stat().st_size==x['bytes']and sha(p.read_bytes())==x['sha256']
old=read(archive/'PACKAGE_MANIFEST.json');allowed={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'};unchanged=0
for x in old['files']:
 if x['file']in allowed:continue
 p=r/x['file'];assert p.stat().st_size==x['bytes']and sha(p.read_bytes())==x['sha256'],x['file'];unchanged+=1
html=(r/'Huyen_Hoc_Cac.html').read_bytes();assert len(html)==707411 and sha(html)=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'and html==(w/'Huyen_Hoc_Cac.html').read_bytes()==(r/'site/index.html').read_bytes();assert sorted(p.name for p in(r/'site').iterdir())==['index.html']
assert sha((r/'engine.js').read_bytes())=='39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6';assert(w/'Huyen_Hoc_Cac_V53_web.zip').read_bytes()==(archive/'Huyen_Hoc_Cac_V53_web.zip').read_bytes()
with zipfile.ZipFile(w/'Huyen_Hoc_Cac_V53_web.zip')as z:assert sorted(z.namelist())==['HUONG_DAN.md','index.html']and z.read('index.html')==html
candidate=read(r/'research/bazi-jianlu-context/CANDIDATE_STATUS.json');assert not candidate['browserTestsPassed']and not candidate['consumerChanged']
for term in[b'liuyao-foundation-span',b'inspectPrintedDiagram',b'readMotion']:assert term not in html
payload=q/'RELEASE_RESULTS.json';files=[p for p in r.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json']
if prepare:count=len(files)+(0 if payload.exists()else 1)
else:
 manifest=read(r/'PACKAGE_MANIFEST.json');assert{p.relative_to(r).as_posix()for p in files}=={x['file']for x in manifest['files']}
 for x in manifest['files']:
  data=(r/x['file']).read_bytes();assert len(data)==x['bytes']and sha(data)==x['sha256'],x['file']
 with zipfile.ZipFile(w/'Huyen_Hoc_Cac_V53_source.zip')as z:
  assert set(z.namelist())=={'v53/'+x['file']for x in manifest['files']}|{'v53/PACKAGE_MANIFEST.json'};assert z.read('v53/PACKAGE_MANIFEST.json')==(r/'PACKAGE_MANIFEST.json').read_bytes()
  for x in manifest['files']:
   data=z.read('v53/'+x['file']);assert len(data)==x['bytes']and sha(data)==x['sha256'],x['file']
 count=len(manifest['files'])
out={'date':'2026-10-28','newChecks':7,'summary':result['summary'],'retainedSourceImageHashesVerified':28,'nativeAndQACropsViewedAndPixelVerified':4,'pixelReproductionsVerified':2,'promotionIdentityHashesVerified':28,'moduleBodiesIdenticalExceptImports':2,'unchangedEarlierV53Files':unchanged,'wholeUnitsApplied':0,'allImageCharactersCollated':False,'fullConditionalRulesEncoded':False,'sourceOutcomesValidated':False,'consumerChanged':False,'wholeCatalogueCompleted':False,'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'previousSourceZIPPreservedBytes':2095344337,'manifestFilesVerified':count,'sourceZIPFilesVerified':count+1}
if prepare:payload.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'preparedExpectedPayload':True,'manifestFilesAfterPackage':count,'requiresFinalNoWriteVerification':True}))
else:assert read(payload)==out;print(json.dumps({'finalReadOnlyVerificationPassed':True,**out},ensure_ascii=False))
