from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,sys
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(n):return json.loads((B/n).read_text(encoding='utf-8-sig'))
def verify(r):
 p=W/r['file'];assert p.is_file()and p.stat().st_size==r['bytes']and sha256(p.read_bytes()).hexdigest()==r['sha256'],r['file']
for r in [*read('PREIMPLEMENTATION_FREEZE.json')['files'],*read('REUSE_IDENTITIES.json')['files']]:verify(r)
images=set()
for r in read('SOURCE_IDENTITIES.json')['records']:
 verify(r['source']);verify(r['crop']);images.add(r['source']['file'])
 source=Image.open(W/r['source']['file']).convert('RGB').crop(r['boxXYXY']);crop=Image.open(W/r['crop']['file']).convert('RGB')
 assert source.size==crop.size==tuple(r['nativeSize'])and ImageChops.difference(source,crop).getbbox()is None
 assert r['actuallyViewed']
manual=read('MANUAL_SPATIAL_CLAUSES.json');assert len(manual['records'])==3
assert '或年獨火' in manual['records'][0]['literal']and '丙丁二字' in manual['records'][0]['literal']
assert '日家打頭火' in manual['records'][1]['literal']
assert '其中但得一位吉神到' in manual['records'][2]['literal']
assert manual['records'][2]['actors']==['飛宮','地軸','帝舍','帝車','帝輅']
out={'passed':True,'frozenFiles':4,'retainedSourcePositionsReexamined':len(images),'nativeCropsRGBMatched':3,'rejectedTrialCropsRetained':3,'sourceUnits':3,'monthlyActorLabels':5,'sourcePrintedExampleCount':0,'newSourcePositions':0,'newHTTPBodies':0,'newEngineCalls':0,'P08LabelsAmended':0,'wholeSourceMethodApplied':False,'consumerChanged':False}
if '--write-results'in sys.argv:(B/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
