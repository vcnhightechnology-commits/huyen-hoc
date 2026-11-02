from pathlib import Path
from hashlib import sha256,sha1
from PIL import Image,ImageChops
import json,sys
r=Path(__file__).resolve().parents[1];w=r.parent;b=r/'research/bazi-season-strength';q=r/'qa/bazi-season-strength'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda p:sha256(p.read_bytes()).hexdigest()
ident=read(b/'PROMOTION_IDENTITIES.json');assert len(ident['records'])==37
for x in ident['records']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'],x['file']
text=(b/'STAGED_test-season-labels.mjs').read_text(encoding='utf-8')
for old,new in [("from './season-label-reference.mjs'","from '../research/bazi-season-strength/season-label-reference.mjs'"),("new URL('./MANUAL_SEASON_TABLE.json',import.meta.url)","new URL('../research/bazi-season-strength/MANUAL_SEASON_TABLE.json',import.meta.url)"),("new URL('./REFERENCE_RESULTS.json',import.meta.url)","new URL('../qa/bazi-season-strength/REFERENCE_RESULTS.json',import.meta.url)")]:assert text.count(old)==1;text=text.replace(old,new)
assert text==(r/'scripts/test-bazi-season-labels.mjs').read_text(encoding='utf-8')
req=read(b/'REQUESTS.json')['records'];assert len(req)==3
for x in req:
 p=b/x['file'];assert x['status']==200 and x['TLSCertificateValidationEnabled']and p.stat().st_size==x['bytes']and sha(p)==x['sha256']
dj=b/'CADAL06066038.djvu';assert dj.stat().st_size==10858550 and sha(dj)=='7a53f35982f0b946281d0e393c5d6ddcce1fd091aea83c11af6a06bcdfe6a85e'and sha1(dj.read_bytes()).hexdigest()=='7ee461bd944fbf23fcf0a0011aff5882214bca5c'
acq=read(b/'ACQUISITION.json');assert not acq['institutionOriginalBytesDownloaded']and not acq['independentInstitutionCatalogueVerified']
render=read(b/'LOCAL_RENDERS.json');assert render['containerPages']==232 and len(render['records'])==8
assert sha(w/render['decoder'])==render['decoderSHA256']=='10a831d62cc7ced39c30c7350a11410402d082a0f0a5b073a88d3d7ca662add3'
for x in render['records']:
 p=b/x['file'];im=Image.open(p);assert x['actuallyViewed']and p.stat().st_size==x['bytes']and sha(p)==x['sha256']and im.size==(x['width'],x['height'])and sha256(im.convert('RGBA').tobytes()).hexdigest()==x['pixelRGBA_SHA256']
 assert 'observedFolio'not in x and 'folioBasis'in x
qa=read(q/'QA_IMAGES.json');assert len(qa['records'])==6
for x in qa['records']:
 src=b/x['sourceFile'];p=q/x['file'];assert x['actuallyViewed']and not x['resampled']and sha(p)==x['sha256']
 assert ImageChops.difference(Image.open(src).convert('RGB').crop(x['cropBox']),Image.open(p).convert('RGB')).getbbox()is None
table=read(b/'MANUAL_SEASON_TABLE.json');assert len(table['records'])==25 and sum(x['recognizedState']is not None for x in table['records'])==24
unknown=[x for x in table['records']if x['recognizedState']is None];assert len(unknown)==1 and unknown[0]['phase']=='summer'and unknown[0]['element']=='水'and unknown[0]['literalState']=='因'
res=read(q/'REFERENCE_RESULTS.json');assert len(res['checks'])==5 and all(x['ok']for x in res['checks'])and len(res['coordinates'])==25 and res['actualCalendarOrHHCEngineCalls']==0
state=read(b/'WORK_STATE.json');assert state['actuallyViewedPositions']==list(range(109,117))and not state['sourceWholeVolumeRead']and not state['wholeCatalogueCompleted']
assert read(b/'TEST_METADATA_EDIT_AUDIT.json')['doNotAggregateAsTenIndependentChecks']
out=dict(date='2026-10-28',promotionIdentities=37,completeRuntimeChecks=5,HTTP200TLSBodies=3,repositoryDjvuBytes=10858550,containerPositions=232,positionsViewed=8,
 nativeCropsViewedPixelMatched=6,sourceSeasonSlots=25,recognizedStateSlots=24,unclassifiedLiteralSlots=1,literalSummerWaterPreserved='因',actualCalendarOrHHCEngineCalls=0,
 institutionOriginalDownload=False,independentEditionEstablished=False,sourceWholeVolumeRead=False,dateToSourcePhaseAdapterValidated=False,fullNatalStrengthEstablished=False,consumerChanged=False,wholeCatalogueCompleted=False)
p=q/'SOURCE_RESULTS.json'
if '--no-write'in sys.argv:assert read(p)==out
else:p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
