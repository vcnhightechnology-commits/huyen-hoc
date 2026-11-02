"""Verify retained locator bytes/pixels; does not decode or re-read a source position."""
from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
d=json.loads((B/'SOURCE_AND_VIEW_AUDIT.json').read_text(encoding='utf-8-sig'))
for r in [d['retainedContainer'],d['decoder']]:
 p=W/r['file'];assert p.stat().st_size==r['bytes']and sha256(p.read_bytes()).hexdigest()==r['sha256']
for r in d['records']:
 p=B/r['file'];assert p.stat().st_size==r['bytes']and sha256(p.read_bytes()).hexdigest()==r['sha256']
 im=Image.open(p).convert('RGBA');assert im.size==(r['width'],r['height'])and sha256(im.tobytes()).hexdigest()==r['pixelRGBA_SHA256']
r=d['selectedNativeCrop'];actual=Image.open(B/Path(r['file']).name).convert('RGB');expected=Image.open(B/'gjts-p96.png').convert('RGB').crop(r['boxXYXY'])
assert actual.size==expected.size and ImageChops.difference(actual,expected).getbbox()is None
assert sha256((B/Path(r['file']).name).read_bytes()).hexdigest()==r['sha256']
print(json.dumps({'passed':True,'retainedPNGsByteAndRGBAMatched':len(d['records']),'selectedCropRGBMatched':1,'newSourceRenders':0,'newHTTPBodies':0,'newEngineCalls':0,'P08LabelsAmended':0,'independentP08EditionEstablished':False}))
