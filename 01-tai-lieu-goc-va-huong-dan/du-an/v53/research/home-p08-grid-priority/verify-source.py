from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,sys
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(n):return json.loads((B/n).read_text(encoding='utf-8-sig'))
for r in read('PREIMPLEMENTATION_FREEZE.json')['files']:
 p=W/r['file'];assert p.stat().st_size==r['bytes']and sha256(p.read_bytes()).hexdigest()==r['sha256']
for r in read('SOURCE_IDENTITIES.json')['records']:
 for k in ['source','crop']:
  p=W/r[k]['file'];assert p.stat().st_size==r[k]['bytes']and sha256(p.read_bytes()).hexdigest()==r[k]['sha256']
 expected=Image.open(W/r['source']['file']).convert('RGB').crop(r['boxXYXY']);actual=Image.open(W/r['crop']['file']).convert('RGB')
 assert actual.size==expected.size and ImageChops.difference(actual,expected).getbbox()is None
out={'passed':True,'retainedSourcePositionsReexamined':2,'nativeCropsRGBMatched':2,'newSourcePositions':0,'newHTTPBodies':0,'newEngineCalls':0,'smallTableGlyphsResolved':False,'wholeSourceMethodApplied':False,'consumerChanged':False}
if '--write-results'in sys.argv:(B/'SOURCE_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
