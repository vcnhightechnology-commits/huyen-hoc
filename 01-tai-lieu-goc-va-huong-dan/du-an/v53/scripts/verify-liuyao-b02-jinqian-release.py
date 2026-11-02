from pathlib import Path
from hashlib import sha256
import json,sys,zipfile
from PIL import Image
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/liuyao-b02-jinqian';q=r/'qa/liuyao-b02-jinqian';a=w/'archives/v53-before-liuyao-b02-jinqian'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda data:sha256(data).hexdigest()
old=read(a/'PACKAGE_MANIFEST.json');m=read(r/'PACKAGE_MANIFEST.json');html=(r/'Huyen_Hoc_Cac.html').read_bytes()
assert len(old['files'])==2820 and(a/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==2008820927
assert len(html)==707411 and sha(html)==m['product']['sha256']==old['product']['sha256']=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html==(w/'Huyen_Hoc_Cac.html').read_bytes()==(r/'site/index.html').read_bytes()==(a/'Huyen_Hoc_Cac.html').read_bytes()
assert [p.name for p in(r/'site').iterdir()]==['index.html']
mutable={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'}
unchanged=0
for f in old['files']:
 if f['file'] not in mutable:
  assert sha((r/f['file']).read_bytes())==f['sha256'],f['file'];unchanged+=1
refs=[f for f in old['files']if f['file'].startswith('research/liuyao-')and f['file'].endswith('reference.mjs')];assert len(refs)==17
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
e=read(q/'ENGINE_RESULTS.json');assert len(e['checks'])==8 and all(x['ok']for x in e['checks'])
assert e['engineSHA256']==sha((r/'engine.js').read_bytes()) and e['htmlSHA256']==sha(html)
assert e['summary']=={'actualHHCHexCalls':4,'newPrintedCastFixtures':2,'privateMotionContexts':4096,'manualRecords':50,'chapter34Pages':46,'witnessHTTPBodies':7}
manual=read(b/'MANUAL_READINGS.json')
for rec in manual['records']:assert sha((b/rec['image']).read_bytes())==rec['sha256']
assert sha((b/manual['sourcePDF']).read_bytes())==manual['sourceSHA256']
u=read(b/'B02_CURRENT_UNITS.json');assert u['currentCounts']['headingOnlyBodyUnits']==96 and u['currentCounts']['firstPassCompleteSpanUnits']==32
assert sum(u['currentCounts'][k]for k in ['headingOnlyBodyUnits','firstPassCompleteSpanUnits','partialFoundationUnits','otherPartialUnits'])==136
assert u['priorTOCSHA256']==sha((r/'research/liuyao-progress-conditions/B02_CURRENT_UNITS.json').read_bytes())
req=read(b/'witness/REQUESTS.json');wr=read(b/'witness/MANUAL_READINGS.json');man=read(b/'witness/japan-volume2-manifest.json')
assert man['label']=='増刪卜易２' and len(man['sequences'][0]['canvases'])==53
assert '4756814' in(r/'research/liuyao-foundations/japan-zengshan-catalog.html').read_text(encoding='utf-8')
for rec in req['records']:
 data=(b/'witness'/rec['file']).read_bytes();assert len(data)==rec['bytes'] and sha(data)==rec['sha256']
assert [x['tls']['authorized']for x in req['records'][:2]]==[None,None]
assert sum(x['status']==403 for x in req['records'])==1 and sum(x['status']==200 for x in req['records'])==6
for rec in wr['records']:
 p=b/'witness'/rec['file'];assert sha(p.read_bytes())==rec['sha256']
 with Image.open(p)as im:assert list(im.size)==rec['servedImagePixels']==[3000,2073]
 canvas=man['sequences'][0]['canvases'][rec['canvasOrdinal1']-1]
 assert canvas['@id']==rec['canvasID'] and canvas['images'][0]['resource']['@id']==rec['resourceURL']
 assert [canvas['width'],canvas['height']]==rec['canvasMetadataPixels']==[6150,4250]
for rec in wr['qaImages']:assert sha((b/'witness'/rec['file']).read_bytes())==rec['sha256']
st=read(w/'EXHAUSTIVE_WORK_STATE.json');assert st==read(r/'research/EXHAUSTIVE_WORK_STATE.json')and st['status']=='active-not-complete'
assert st['currentWork']['latestResearchReport']=='v53/LIUYAO_B02_JINQIAN_REPORT.md' and st['currentWork']['currentB02UnitMap']=='v53/research/liuyao-b02-jinqian/B02_CURRENT_UNITS.json'
cov=read(r/'research/library-current/COVERAGE.json');assert cov['counts']['wholeWorkApplied']==0 and cov['counts']['catalogueRecords']==40
assert cov['latestAcquisitionCounts']['retainedHTTPBodiesNewToRelease']==7 and cov['latestAcquisitionCounts']['newHTTPRequestsThisRun']==0
full=read(r/'research/full-study/WORK_STATE.json');assert full['latestResearchReport']=='LIUYAO_B02_JINQIAN_REPORT.md'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
assert read(w/'PENDING_RESEARCH_STATE.json')['status']=='B02-jinqian-current-scope-active'
for term in[b'liuyao-b02-jinqian',b'interposed-reference',b'japan-volume2-manifest']:assert term not in html
out={'date':'2026-10-27','checks':8,**e['summary'],'witnessActualPixelsVerified':True,'retained403NotSourceImage':True,'uncapturedTLSFlagsRemainNull':True,
 'chapter34LocalTOCVolumeCorrected':True,'chapter35TOCBodyVolumeConflictPreserved':True,'gengConflictResolved':False,'wholeCatalogueCompleted':False,
 'consumerChanged':False,'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'previousSourceZIPPreservedBytes':2008820927,
 'previousReferenceFilesPreserved':len(refs),'unchangedEarlierV53Files':unchanged,'manifestFilesVerified':len(m['files']),'sourceZIPFilesVerified':len(m['files'])+1}
if '--no-write'in sys.argv:assert read(q/'RELEASE_RESULTS.json')==out
else:(q/'RELEASE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
