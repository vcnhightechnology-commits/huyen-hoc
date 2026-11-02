from pathlib import Path
from hashlib import sha256
from PIL import Image
import json,sys
S=Path(__file__).resolve().parent
W=next(p for p in S.parents if(p/'v53/engine.js').is_file())
d=json.loads((S/'DATE_VARIANT_CROPS.json').read_text(encoding='utf-8'))
for x in d['records']:
 for key in ['raw','crop']:
  p=W/x[key]['file'];b=p.read_bytes();assert len(b)==x[key]['bytes']and sha256(b).hexdigest()==x[key]['sha256']
 assert x['accepted']and x['actuallyViewed']and x['selectedNativeDateReading']=='玄月丙午日'
 with Image.open(W/x['raw']['file'])as im,Image.open(W/x['crop']['file'])as cr:
  a,b,c,e=x['boxXYXY'];assert 0<=a<c<=im.width and 0<=b<e<=im.height
  assert im.crop((a,b,c,e)).convert('RGB').tobytes()==cr.convert('RGB').tobytes()
assert d['dayReadings']==['丙午','丙午']and d['monthGlyphRetained']=='玄月'and not d['monthBranchInferred']
assert d['hypothesizedDayVariantRejected']
out={'passed':True,'selectedParallelCropRGBMatches':2,'selectedDateReadings':['玄月丙午日','玄月丙午日'],'dayVariantEstablished':False,'monthBranchInferred':False,'newSourceImages':0,'newHTTPBodies':0,'newEngineCallsDuringChecks':0,'sourceImageBytesChanged':False,'independentTextualGenealogyEstablished':False,'consumerChanged':False}
if '--write-results'in sys.argv:(S/'PARALLEL_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
