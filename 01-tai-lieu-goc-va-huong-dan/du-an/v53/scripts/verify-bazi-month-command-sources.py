from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,sys
r=Path(__file__).resolve().parents[1];w=r.parent;b=r/'research/bazi-month-command';q=r/'qa/bazi-month-command'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda p:sha256(p.read_bytes()).hexdigest()
ident=read(b/'PROMOTION_IDENTITIES.json');assert len(ident['records'])==33
for x in ident['records']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'],x['file']
text=(b/'STAGED_test-month-command.mjs').read_text(encoding='utf-8')
for old,new in [("from './month-command-reference.mjs'","from '../research/bazi-month-command/month-command-reference.mjs'"),("const b=import.meta.dirname,w=resolve(b,'../..'),L=","const b=resolve(import.meta.dirname,'../research/bazi-month-command'),w=resolve(b,'../../..'),L="),("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/bazi-month-command/REFERENCE_RESULTS.json')")]:assert text.count(old)==1;text=text.replace(old,new)
assert text==(r/'scripts/test-bazi-month-command.mjs').read_text(encoding='utf-8')
render=read(b/'LOCAL_RENDERS.json');assert len(render['records'])==9 and sorted(x['page']for x in render['records'])==list(range(65,74))
assert render['source']=='v53/research/bazi-season-strength/CADAL06066038.djvu'
assert sha(w/render['source'])==render['sourceSHA256']=='7a53f35982f0b946281d0e393c5d6ddcce1fd091aea83c11af6a06bcdfe6a85e'
assert sha(w/render['decoder'])==render['decoderSHA256']=='10a831d62cc7ced39c30c7350a11410402d082a0f0a5b073a88d3d7ca662add3'
for x in render['records']:
 p=b/x['file'];im=Image.open(p);assert x['actuallyViewed']and sha(p)==x['sha256']and sha256(im.convert('RGBA').tobytes()).hexdigest()==x['pixelRGBA_SHA256']
qa=read(q/'QA_IMAGES.json');assert len(qa['records'])==6
for x in qa['records']:
 p=q/x['file'];src=b/x['sourceFile'];assert x['actuallyViewed']and not x['resampled']and sha(p)==x['sha256']
 assert ImageChops.difference(Image.open(src).convert('RGB').crop(x['cropBox']),Image.open(p).convert('RGB')).getbbox()is None
table=read(b/'MANUAL_COMMAND_TABLES.json');assert len(table['records'])==24 and sum(len(x['entries'])for x in table['records'])==69
for x in table['records']:assert sum(c['days']for c in x['entries'])==x['arithmeticDayTotal']
assert sum(x['arithmeticDayTotal']for x in table['records']if x['variant']=='chapter-prose')==360
assert sum(x['arithmeticDayTotal']for x in table['records']if x['variant']=='cited-Yujing-table')==358
audit=read(b/'ARITHMETIC_AUDIT.json');assert audit['yujingNonThirtyRows']==[dict(monthBranch='酉',days=32),dict(monthBranch='子',days=26)]
assert audit['source69AnnualCountIntro']['computedTotal']==380 and audit['source69AnnualCountIntro']['printedClaimedTotal']==360
res=read(q/'REFERENCE_RESULTS.json');assert len(res['checks'])==5 and all(x['ok']for x in res['checks'])and len(res['comparisons'])==24
assert sum(x['exactSetMatch']is True for x in res['comparisons'])==6 and sum(x['exactSetMatch']is False for x in res['comparisons'])==16 and sum(x['exactSetMatch']is None for x in res['comparisons'])==2
assert res['summary']['actualLunarHiddenStemTableQueries']==24 and res['summary']['newCalendarChartCalls']==0
source=read(b/'SOURCE_DISPOSITIONS.json');digital=source['retainedDigital'];assert sha(w/digital['file'])==digital['sha256']and sha(b/digital['decodedSliceFile'])==digital['sliceSHA256']
assert source['viewCounts']['totalDistinctVolume2PositionsAcrossTwoScopes']==17
prior=read(r/'research/bazi-season-strength/LOCAL_RENDERS.json');assert len({x['page']for x in prior['records']}|{x['page']for x in render['records']})==17
state=read(b/'WORK_STATE.json');assert not state['wholeCatalogueCompleted']and not state['fullCalendarCommandMethodApplied']
out=dict(date='2026-10-28',promotionIdentities=33,completeRuntimeChecks=5,newNativePositionsViewed=9,totalVolume2PositionsViewed=17,containerPositions=232,
 nativeCropsViewedPixelMatched=6,sourceMonthRows=24,allocationEntries=69,proseTotalDays=360,YujingTotalDays=358,nonThirtyRows=['酉32','子26'],introComputedVersusPrinted=[380,360],
 actualLunarHiddenStemTableQueries=24,canonicalStemSetMatches=6,canonicalStemSetDifferences=16,unresolvedCanonicalSets=2,newCalendarChartCalls=0,
 newHTTPBodies=0,newContainers=0,consumerChanged=False,actualDayOffsetCommandAdapterValidated=False,fullStrengthEstablished=False,wholeCatalogueCompleted=False)
p=q/'SOURCE_RESULTS.json'
if '--no-write'in sys.argv:assert read(p)==out
else:p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
