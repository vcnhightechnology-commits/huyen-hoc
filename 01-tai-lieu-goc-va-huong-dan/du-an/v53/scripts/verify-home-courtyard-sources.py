from pathlib import Path
from hashlib import sha256,sha1
from PIL import Image,ImageChops
import json,sys
r=Path(__file__).resolve().parents[1];w=r.parent;b=r/'research/home-yangzhai-courtyards';q=r/'qa/home-yangzhai-courtyards'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda p:sha256(p.read_bytes()).hexdigest()
meta=read(b/'PROMOTION_IDENTITIES.json');assert len(meta['records'])==76
for x in meta['records']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'],x['file']
for name,pairs in {
 'test-courtyard-reference.mjs':[("from './courtyard-reference.mjs'","from '../research/home-yangzhai-courtyards/courtyard-reference.mjs'"),("const b=import.meta.dirname,w=resolve(b,'../..'),system=COURTYARD_SYSTEM;","const b=resolve(import.meta.dirname,'../research/home-yangzhai-courtyards'),w=resolve(b,'../../..'),system=COURTYARD_SYSTEM;"),("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/home-yangzhai-courtyards/REFERENCE_RESULTS.json')")],
 'test-courtyard-context.mjs':[("from './courtyard-context-reference.mjs'","from '../research/home-yangzhai-courtyards/courtyard-context-reference.mjs'"),("new URL('./CONTEXT_RESULTS.json',import.meta.url)","new URL('../qa/home-yangzhai-courtyards/CONTEXT_RESULTS.json',import.meta.url)")]}.items():
 text=(b/('STAGED_'+name)).read_text(encoding='utf-8')
 for old,new in pairs:assert text.count(old)==1;text=text.replace(old,new)
 assert text==(r/'scripts'/('test-home-'+name.removeprefix('test-'))).read_text(encoding='utf-8')
checks=0
for name,n in [('REFERENCE_RESULTS.json',6),('CONTEXT_RESULTS.json',4)]:
 x=read(q/name);assert len(x['checks'])==n and all(c['ok']for c in x['checks']);checks+=n
runtime=read(q/'REFERENCE_RESULTS.json');assert runtime['actualExistingLayerComponentCalls']==75 and len(runtime['comparisons'])==69 and len(runtime['alternative'])==6
assert sum(x['match']for x in runtime['comparisons'])==65
cells=read(b/'MANUAL_DIAGRAM_CELLS.json')['records'];assert len(cells)==12 and sum(len(x['printedLayerCells'])for x in cells)==69
assert [x['sourcePDFPage']for x in cells if len(x['printedLayerCells'])==5]==[82,86,92]
assert sum(x['sourceStar']is None for c in cells for x in c['printedLayerCells'])==4
requests=read(b/'REQUESTS.json')['records'];assert len(requests)==5
for x in requests:
 p=b/x['file'];assert x['status']==200 and x['TLSCertificateValidationEnabled']and p.stat().st_size==x['bytes']and sha(p)==x['sha256']
dj=b/'Gujin-Tushu-Jicheng-Volume476.djvu';assert dj.stat().st_size==33681249 and sha(dj)=='e819d6f430065e4f63c121390d74ad6d3bc36457cfb8e59fb7a2cea6483130de'
assert sha1(dj.read_bytes()).hexdigest()=='6ca45586afcba3c6b7880ec0b6795f2ca2ad2c56'
render=read(b/'GJTS_LOCAL_RENDERS.json');assert render['containerPages']==135 and len(render['records'])==4
assert sha(w/render['decoder'])==render['decoderSHA256']=='10a831d62cc7ced39c30c7350a11410402d082a0f0a5b073a88d3d7ca662add3'
for x in render['records']:
 p=b/x['file'];assert x['actuallyViewed']and sha(p)==x['sha256']
 im=Image.open(p);assert im.size==(x['width'],x['height'])and sha256(im.convert('RGBA').tobytes()).hexdigest()==x['pixelRGBA_SHA256']
count=0
for name,old in [('QA_IMAGES.json',True),('GJTS_QA_IMAGES.json',False)]:
 for x in read(q/name)['records']:
  p=q/Path(x['file']).name;src=w/x['sourceFile']if old else b/x['sourceFile'];im=Image.open(src).convert('RGB').crop(x['cropBox'])
  if x['transpose']=='ROTATE_180':im=im.transpose(Image.Transpose.ROTATE_180)
  assert x['actuallyViewed']and not x['resampled']and sha(p)==x['sha256']
  assert ImageChops.difference(im,Image.open(p).convert('RGB')).getbbox()is None;count+=1
assert count==25
collation=read(b/'SELECTED_WITNESS_COLLATION.json');assert len(collation['records'])==6 and all(x['matchesTianyigeLiteral']for x in collation['records'])
assert [x['manualEntry']['sourceElement']for x in collation['records']]==['木','木','火','土','金','木']and not collation['all69CellsCollatedAcrossWitnesses']
assert not read(b/'WORK_STATE.json')['wholeCatalogueCompleted']
out=dict(date='2026-10-28',promotionIdentities=76,completeRuntimeChecks=checks,literalCourtyardCells=69,unlabelledStarCells=4,actualExistingLayerComponentCalls=75,actualHHCChartOrCalendarCalls=0,
 newHTTP200TLSBodies=5,repositoryDjvuBytes=33681249,comparisonWitnessPositionsViewed=4,wholeComparisonPagesFullyCollated=0,selectedWitnessCells=6,untranscribedWitnessCells=63,nativeCropsViewedPixelMatched=25,newTianyigeSourcePositions=0,totalTianyigeFirstPassPositions=195,wholeUnitsApplied=0,consumerChanged=False,allConditionsApplied=False)
p=q/'SOURCE_RESULTS.json'
if '--no-write'in sys.argv:assert read(p)==out
else:p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
