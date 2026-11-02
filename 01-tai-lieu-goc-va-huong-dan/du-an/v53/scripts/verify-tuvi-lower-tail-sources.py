from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,sys,subprocess
v=Path(__file__).resolve().parent.parent;w=v.parent;b=v/'research/tuvi-lower-tail';q=v/'qa/tuvi-lower-tail';read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def digest(p):
 h=sha256()
 with p.open('rb')as stream:
  for block in iter(lambda:stream.read(4*1024*1024),b''):h.update(block)
 return h.hexdigest()
ident=read(b/'PROMOTION_IDENTITIES.json')
for r in ident['records']:
 p=v/r['file'];assert p.stat().st_size==r['bytes']and digest(p)==r['sha256'],r['file']
assert {r['file']for r in ident['records']}=={p.relative_to(v).as_posix()for p in b.iterdir()if p.is_file()and p.name!='PROMOTION_IDENTITIES.json'}|{'qa/tuvi-lower-tail/RESULTS.json','TUVI_LOWER_TAIL_REPORT.md','scripts/verify-tuvi-lower-tail-sources.py'}
sel=read(b/'SELECTION.json');assert digest(w/sel['manifestFile'])==sel['manifestSHA256'];man=read(w/sel['manifestFile'])['sequences'][0]['canvases'];req=read(b/'REQUESTS.json');acq=read(b/'ACQUISITION.json');assert len(req)==len(sel['records'])==len(acq['records'])==59
expected=set(range(74,80))|set(range(81,100))|set(range(101,120))|set(range(121,136));assert{r['canvas']for r in req}==expected
for r in req:
 p=b/r['file'];im=Image.open(p);im.verify();assert Image.open(p).size==(2200,1659);url=man[r['canvas']-1]['images'][0]['resource']['service']['@id'].rstrip('/')+'/full/2200,/0/native.jpg';assert r['url']==url and r['status']==200 and r['TLSCertificateValidationEnabled'];assert p.stat().st_size==r['bytes']and digest(p)==r['sha256'];assert any('jpeg'in x for x in r['headers']['Content-Type'])
 assert next(x for x in sel['records']if x['canvas']==r['canvas'])['url']==url
 assert next(x for x in acq['records']if x['canvas']==r['canvas'])['sha256']==r['sha256']
ledger=read(b/'FIRST_PASS_READINGS.json')['records'];assert{r['canvas']for r in ledger}==expected;assert all(r['actuallyViewed']and not r['allRulesApplied']and not r['wholePageDiplomaticallyTranscribed']for r in ledger)
coverage=read(b/'LOWER_POSITION_COVERAGE.json');assert len(coverage['records'])==137 and {r['canvas']for r in coverage['records']}==set(range(1,138))
for r in coverage['records']:
 p=w/r['file'];assert p.stat().st_size==r['bytes']and digest(p)==r['sha256'];assert r['firstPassActuallyViewed']and not r['allClausesApplied']
assert not coverage['wholeSourceApplied']and not coverage['bodyOrColophonCompletenessEstablished']
crops=read(b/'NATIVE_CROPS.json')['records']+read(b/'POST_RUNTIME_CROPS.json')['records'];assert len(crops)==8 and sum(r['acceptedForLiteralProof']for r in crops)==6
for r in crops:
 assert r['actuallyViewed']and digest(b/r['file'])==r['sha256']and digest(b/r['sourceFile'])==r['sourceSHA256'];assert ImageChops.difference(Image.open(b/r['sourceFile']).crop(r['box']).convert('RGB'),Image.open(b/r['file']).convert('RGB')).getbbox() is None
im=Image.open(b/crops[0]['file']).convert('RGB');changed=im.copy();p=changed.getpixel((0,0));changed.putpixel((0,0),((p[0]+1)%256,p[1],p[2]));assert ImageChops.difference(im,changed).getbbox()is not None
volume=read(b/'VOLUME_MAP.json');assert not volume['formalJuan6OpeningEstablished']and not volume['datedColophonEstablished'];assert next(x for x in volume['boundaries']if x['position']=='121right')['literal']is None;assert next(x for x in volume['boundaries']if x['position']=='121left')['literal'].endswith('卷之七')
units=read(b/'CURRENT_UNITS.json');assert len(units['sectionDispositions'])==10 and all(not x['wholeUnitApplied']for x in units['sectionDispositions']);assert units['sectionDispositions'][0]['physicalPanels']==114 and units['sectionDispositions'][0]['casesWithSelectedNatalCoordinatesCompared']==5
p=subprocess.run(['node',str(b/'test-reference.mjs'),'--no-write'],cwd=w,capture_output=True,text=True,encoding='utf-8');assert p.returncode==0,p.stdout+p.stderr;tests=json.loads(p.stdout);assert tests==read(q/'RESULTS.json')
assert (w/'EXHAUSTIVE_WORK_STATE.json').read_bytes()==(v/'research/EXHAUSTIVE_WORK_STATE.json').read_bytes();c=read(v/'research/library-current/COVERAGE.json');t=next(x for x in c['catalogue']if x['id']=='T01');assert t['lowerItemCounts']['positionsRetainedAndViewed']==137 and t['lowerItemCounts']['positionsStillUnread']==0 and not t['lowerItemCounts']['allRulesApplied']and c['counts']['wholeWorkApplied']==0
html=v/'Huyen_Hoc_Cac.html';assert html.stat().st_size==707411 and digest(html)=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857';assert html.read_bytes()==(w/'Huyen_Hoc_Cac.html').read_bytes()==(v/'site/index.html').read_bytes();assert sorted(p.name for p in(v/'site').iterdir())==['index.html']
out=dict(date='2026-10-29',promotionIdentities=len(ident['records']),newHTTP200JPEGDerivativeBodies=59,newDistinctPositionsViewed=59,lowerPhysicalPositionsFirstPassViewed=137,unviewedPhysicalPositions=0,wholeWorkApplied=False,nativeCropsRGBMatched=8,acceptedLiteralCrops=6,excludedLiteralCrops=2,RGBTamperPositiveControl=True,formalJuan7Opening='121left',formalJuan6EndingEstablished=False,sectionDispositions=10,wholeUnitsApplied=0,completeRuntimeChecks=tests['completeChecks'],actualHHCTuviCalls=3,actualIztroNatalCalls=3,actualConsumerPalaceReads=3,runtimeBatches=1,initialProjectionChecks=30,initialProjectionMatches=28,initialProjectionMismatches=2,uniqueManualFieldsCorrected=1,reconciledProjectionChecks=30,reconciledProjectionMismatches=0,consumerComparisons=10,testsRerunCharts=0,newOriginalJP2Bodies=0,newIndependentEditions=0,consumerChanged=False,wholeCatalogueCompleted=False)
if '--no-write'in sys.argv:assert read(q/'SOURCE_RESULTS.json')==out
else:(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
