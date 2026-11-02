from pathlib import Path
from hashlib import sha256
import json,sys,zipfile
from PIL import Image
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/bazi-jianlu-coordinates';q=r/'qa/bazi-jianlu-coordinates';a=w/'archives/v53-before-bazi-jianlu-coordinates'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda data:sha256(data).hexdigest()
old=read(a/'PACKAGE_MANIFEST.json');m=read(r/'PACKAGE_MANIFEST.json');html=(r/'Huyen_Hoc_Cac.html').read_bytes()
assert len(old['files'])==2901 and(a/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==2017947166
assert len(html)==707411 and sha(html)==m['product']['sha256']==old['product']['sha256']=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html==(w/'Huyen_Hoc_Cac.html').read_bytes()==(r/'site/index.html').read_bytes()==(a/'Huyen_Hoc_Cac.html').read_bytes()
assert [p.name for p in(r/'site').iterdir()]==['index.html']
mutable={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'}
unchanged=0
for f in old['files']:
 if f['file'] not in mutable:
  assert sha((r/f['file']).read_bytes())==f['sha256'],f['file'];unchanged+=1
web=w/'Huyen_Hoc_Cac_V53_web.zip';assert web.stat().st_size==344047 and web.read_bytes()==(a/web.name).read_bytes()
with zipfile.ZipFile(web)as z:assert sorted(z.namelist())==['HUONG_DAN.md','index.html']and z.read('index.html')==html
assert {p.relative_to(r).as_posix()for p in r.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json'}=={f['file']for f in m['files']}
for f in m['files']:
 data=(r/f['file']).read_bytes();assert len(data)==f['bytes']and sha(data)==f['sha256'],f['file']
with zipfile.ZipFile(w/'Huyen_Hoc_Cac_V53_source.zip')as z:
 assert set(z.namelist())=={'v53/'+f['file']for f in m['files']}|{'v53/PACKAGE_MANIFEST.json'}
 assert z.read('v53/PACKAGE_MANIFEST.json')==(r/'PACKAGE_MANIFEST.json').read_bytes()
 for f in m['files']:
  data=z.read('v53/'+f['file']);assert len(data)==f['bytes']and sha(data)==f['sha256'],f['file']
e=read(q/'RESULTS.json');assert len(e['checks'])==9 and all(x['ok']for x in e['checks'])
assert e['summary']=={'actualHHCBaziCalls':120,'actualLunarCalls':120,'sourceTriplets':10,'sourceHourKillContexts':10,'privateMonthContexts':120,'expandedPreviouslyReadPages':2,'newSourcePages':0,'newHTTPRequests':0}
assert e['htmlSHA256']==sha(html) and not e['fullPatternClassifier']
assert len(e['sourceFixtures'])==10 and all(x['sourceCoordinateMatched']and x['hourKillPositions']for x in e['sourceFixtures'])
manual=read(b/'MANUAL_READINGS.json');assert len(manual['rows'])==10 and manual['expandedPreviouslyReadPages']==2 and manual['newSourcePages']==0
assert sha((b/manual['source']).read_bytes())==manual['sourceSHA256'] and sha((b/manual['digitalComparator']).read_bytes())==manual['digitalSHA256']
for rec in manual['readings']:assert sha((b/rec['file']).read_bytes())==rec['sha256']
crop=manual['qaCrop'];assert sha((b/crop['file']).read_bytes())==crop['sha256']
with Image.open(b/crop['sourceFile'])as im:
 expected=im.crop(tuple(crop['box']))
 with Image.open(b/crop['file'])as actual:assert expected.size==actual.size and expected.tobytes()==actual.tobytes()
probe=read(b/'PROBE_RESULTS.json');assert(probe['compatible'],probe['incompatible'],probe['actualHHCBaziCalls'],probe['actualLunarLookupCalls'],probe['actualLunarFixtureCalls'])==(10,0,10,41,10)
assert probe['sourceEmended']==False and read(b/'SOURCE_AUDIT.json')['falseConflictHypothesisRejected']==True
rows=read(b/'SOURCE_ROWS.json')['rows'];assert sum(x['digitalGlyphVariant']for x in rows)==3 and rows[-1]['sourceImages']==[223,224]
st=read(w/'EXHAUSTIVE_WORK_STATE.json');assert st==read(r/'research/EXHAUSTIVE_WORK_STATE.json')and st['status']=='active-not-complete'
assert st['currentWork']['latestResearchReport']=='v53/BAZI_JIANLU_COORDINATES_REPORT.md'and st['currentWork']['catalogueID']=='M01'
assert st['currentWork']['currentB02UnitMap']=='v53/research/liuyao-b02-jinqian/B02_CURRENT_UNITS.json'
cov=read(r/'research/library-current/COVERAGE.json');assert cov['counts']['wholeWorkApplied']==0 and cov['counts']['catalogueRecords']==40 and cov['counts']['newDownloadsThisScope']==0
full=read(r/'research/full-study/WORK_STATE.json');assert full['latestResearchReport']=='BAZI_JIANLU_COORDINATES_REPORT.md'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
assert read(w/'PENDING_RESEARCH_STATE.json')['status']=='Bazi-jianlu-current-scope-active'
prior=read(r/'qa/liuyao-b02-jinqian/RELEASE_RESULTS.json');assert prior['manifestFilesVerified']==2901
for term in[b'bazi-jianlu-coordinates',b'jianlu-reference']:assert term not in html
out={'date':'2026-10-27','checks':9,**e['summary'],'allTenPrintedHoursCompatible':True,'falseSourceConflictHypothesisRejected':True,
 'prior38ClauseMatrixPreserved':True,'nativeCropVerified':True,'wholeCatalogueCompleted':False,'consumerChanged':False,
 'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'previousSourceZIPPreservedBytes':2017947166,
 'unchangedEarlierV53Files':unchanged,'manifestFilesVerified':len(m['files']),'sourceZIPFilesVerified':len(m['files'])+1}
if '--no-write'in sys.argv:assert read(q/'RELEASE_RESULTS.json')==out
else:(q/'RELEASE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
