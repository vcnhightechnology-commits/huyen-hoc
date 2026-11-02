from pathlib import Path
from hashlib import sha256
import json, sys, zipfile

r=Path(__file__).resolve().parent.parent
w=r.parent
b=r/'research/home-direction-tables'
q=r/'qa/home-direction-tables'
a=w/'archives/v53-before-home-direction-tables'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda data:sha256(data).hexdigest()
prepare='--prepare'in sys.argv
old=read(a/'PACKAGE_MANIFEST.json')
html=(r/'Huyen_Hoc_Cac.html').read_bytes()
resultFile=q/'RELEASE_RESULTS.json'
assert len(old['files'])==3164 and(a/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==2037602853
assert len(html)==707411 and sha(html)==old['product']['sha256']=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html==(w/'Huyen_Hoc_Cac.html').read_bytes()==(r/'site/index.html').read_bytes()==(a/'Huyen_Hoc_Cac.html').read_bytes()
assert [p.name for p in(r/'site').iterdir()]==['index.html']
mutable={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'}
unchanged=0
for f in old['files']:
 if f['file']not in mutable:
  assert sha((r/f['file']).read_bytes())==f['sha256'],f['file']
  unchanged+=1
web=w/'Huyen_Hoc_Cac_V53_web.zip'
assert web.stat().st_size==344047 and web.read_bytes()==(a/web.name).read_bytes()
with zipfile.ZipFile(web)as z:
 assert sorted(z.namelist())==['HUONG_DAN.md','index.html']and z.read('index.html')==html
qa=read(q/'RESULTS.json');src=read(q/'SOURCE_RESULTS.json')
assert len(qa['checks'])==7 and all(x['ok']for x in qa['checks'])
assert qa['summary']=={'termRows': 24, 'termCoordinateLabels': 24, 'najiaCoordinates': 24, 'manualGlyphs': 24, 'contextualProseSegments': 8, 'actualHHCMountainCalls': 24, 'actualHHCPureHexCalls': 8, 'actualLunarTermTableExecutions': 1, 'actualPrivateLiuyaoContrasts': 2, 'newHTTPRequests': 0, 'newSourcePages': 0, 'expandedPreviouslyReadPages': 5}
assert src['nativeCropsVerified']==4 and src['losslessRotationsVerified']==6 and src['nativeImageHashesVerified']==5
assert len(qa['positions'])==24 and len(qa['assignments'])==24 and len(qa['guaGlyphs'])==8 and len(qa['liuyaoContrasts'])==2
assert len(read(b/'SOURCE_TABLES.json')['nextSourceClauses'])==8
assert qa['astronomicalInstantsVerifiedBySource']is False
st=read(w/'EXHAUSTIVE_WORK_STATE.json')
assert st==read(r/'research/EXHAUSTIVE_WORK_STATE.json')and st['status']=='active-not-complete'
assert st['currentWork']['latestResearchReport']=='v53/HOME_DIRECTION_TABLES_REPORT.md'
cov=read(r/'research/library-current/COVERAGE.json')
assert cov['counts']['catalogueRecords']==40 and cov['counts']['wholeWorkApplied']==0 and cov['counts']['newDownloadsThisScope']==0
full=read(r/'research/full-study/WORK_STATE.json')
assert full['latestResearchReport']=='HOME_DIRECTION_TABLES_REPORT.md'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
assert read(w/'PENDING_RESEARCH_STATE.json')['status']=='Home-direction-tables-current-scope-active'
assert read(r/'qa/home-rings/RELEASE_RESULTS.json')['manifestFilesVerified']==3164
for term in[b'home-direction-tables',b'direction-reference',b'xieji-geographical-najia']:
 assert term not in html
files=[p for p in r.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json']
if prepare:
 count=len(files)+(0 if resultFile.exists()else 1)
else:
 m=read(r/'PACKAGE_MANIFEST.json')
 assert {p.relative_to(r).as_posix()for p in files}=={f['file']for f in m['files']}
 assert m['product']['sha256']==sha(html)
 for f in m['files']:
  data=(r/f['file']).read_bytes()
  assert len(data)==f['bytes']and sha(data)==f['sha256'],f['file']
 with zipfile.ZipFile(w/'Huyen_Hoc_Cac_V53_source.zip')as z:
  assert set(z.namelist())=={'v53/'+f['file']for f in m['files']}|{'v53/PACKAGE_MANIFEST.json'}
  assert z.read('v53/PACKAGE_MANIFEST.json')==(r/'PACKAGE_MANIFEST.json').read_bytes()
  for f in m['files']:
   data=z.read('v53/'+f['file'])
   assert len(data)==f['bytes']and sha(data)==f['sha256'],f['file']
 count=len(m['files'])
out={'date':'2026-10-27','checks':7,**qa['summary'],'nativeCropsVerified':4,'losslessRotationsVerified':6,
 'wholeCatalogueCompleted':False,'consumerChanged':False,'physicalCompassAdapterEstablished':False,
 'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,
 'previousSourceZIPPreservedBytes':2037602853,'unchangedEarlierV53Files':unchanged,
 'manifestFilesVerified':count,'sourceZIPFilesVerified':count+1}
if prepare:
 # This expected payload becomes evidence only after the final ZIP verification.
 resultFile.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'preparedExpectedPayload':True,'manifestFilesAfterPackage':count,'requiresFinalNoWriteVerification':True}))
elif '--no-write'in sys.argv:
 assert read(resultFile)==out
 print(json.dumps(out,ensure_ascii=False))
else:
 resultFile.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(out,ensure_ascii=False))
