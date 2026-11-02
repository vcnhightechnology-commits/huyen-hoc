from pathlib import Path
from hashlib import sha256
import json,re
from PIL import Image
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/home-you-nian';q=r/'qa/home-you-nian'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda data:sha256(data).hexdigest()
d=read(b/'RENDERS.json');manual=read(b/'MANUAL_READINGS.json')
assert sorted(x['page']for x in d['records'])==[1]+list(range(9,111))
assert len(manual['readings'])==103 and all(x['directlyViewed']for x in manual['readings'])
assert manual['contentPages']==95 and manual['ruledBlankPages']==[40,48,60,70,94]and manual['paratextPages']==[1,109,110]
prior=read(r/'research/full-study/home/READINGS.json');assert {x['page']for x in prior['readings']}==set(range(2,9))
assert {x['page']for x in manual['readings']}|{x['page']for x in prior['readings']}==set(range(1,111))
unitmap=read(b/'VOLUME_UNIT_MAP.json');assert len(unitmap['units'])==12 and not unitmap['allClausesAndTablesApplied']
for x in d['records']:
 p=b/x['file'];assert len(p.read_bytes())==x['bytes']and sha(p.read_bytes())==x['sha256']
 with Image.open(p)as im:assert im.size==(x['width'],x['height'])and sha(im.convert('RGBA').tobytes())==x['pixelRGBA_SHA256']
 assert next(a['sha256']for a in manual['readings']if a['page']==x['page'])==x['sha256']
with Image.open(b/'decoder-calibration-p223.png')as x,Image.open(w/d['calibration']['compareWith'])as y:
 assert x.size==y.size and x.convert('RGBA').tobytes()==y.convert('RGBA').tobytes()
assert d['calibration']['nativePixelEqualityWithPriorBrowserPNG']
cmp=read(b/'zhaijing/TRANSMISSION_COMPARISON.json');assert len(cmp['comparisons'])==10
def text_at(file,marker):
 t=(r/'research/library-audit/new-sources'/file).read_text(encoding='utf-8-sig');i=t.index(marker);j=t.find('<pb:',i+len(marker));return re.sub(r'¶|/|\s','',t[i:None if j<0 else j])
for row in cmp['comparisons']:
 for witness,group,repo in [('WYG','WYG','KR3g0019'),('HFL','HFL','KR5a0294')]:
  x=row[witness];assert x['boundedReading']in text_at(x['file'],f'<pb:{repo}_{group}_{x["folio"]}>'),row['id']
 assert not row['facsimileResolved']and not row['consumerApplied']
assert sum(x['WYG']['boundedReading']!=x['HFL']['boundedReading']for x in cmp['comparisons'])==10 # includes 爲/為 in shared inventory wording
unit=read(b/'zhaijing/DIGITAL_UNIT_MAP.json');assert len(unit['sources'])==3
redecode=read(b/'REDECODE_CHECK.json');assert len(redecode['checks'])==2 and all(x['match']for x in redecode['checks'])
out={'date':'2026-10-27','nativePNGAndPixelHashesVerified':103,'nativeContentPages':95,'blankPages':5,'paratextPages':3,
 'priorImagesRetainedRead':7,'combinedFirstPassImagePositions':110,'sourceUnitsLocated':12,
 'decoderCalibrationPixelEqual':True,'redecodedPixelArrays':2,'newSourcePagesFromRedecode':0,
 'P03ArtifactsHashed':6,'newBoundedTextPairsAnchored':10,'P03FacsimileResolved':False,
 'allSourceClausesApplied':False,'wholeCatalogueCompleted':False}
(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
