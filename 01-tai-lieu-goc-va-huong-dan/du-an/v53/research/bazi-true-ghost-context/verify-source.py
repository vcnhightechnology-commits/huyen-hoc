from pathlib import Path
from hashlib import sha256
from PIL import Image
import json,re,sys
S=Path(__file__).resolve().parent;W=next(p for p in S.parents if(p/'v53/engine.js').is_file())
def read(n):return json.loads((S/n).read_text(encoding='utf-8-sig'))
def check(p,x):
 raw=p.read_bytes();assert len(raw)==x['bytes'] and sha256(raw).hexdigest()==x['sha256'],p
for x in read('PREIMPLEMENTATION_FREEZE.json')['files']:check(S/x['file'],x)
n=read('NATIVE_REVIEW.json');check(W/n['source']['file'],n['source']);check(W/n['decoder']['file'],n['decoder'])
for x in n['records']:
 check(S/x['file'],x);assert x['actuallyViewed']
 with Image.open(S/x['file']) as im:assert im.size==(x['width'],x['height']) and sha256(im.convert('RGBA').tobytes()).hexdigest()==x['pixelRGBA_SHA256']
assert n['positionsActuallyViewed']==list(range(19,24))
for x in read('SELECTED_CROPS.json')['records']:
 check(S/x['raw']['file'],x['raw']);check(S/x['crop']['file'],x['crop']);assert x['accepted'] and x['actuallyViewed']
 with Image.open(S/x['raw']['file']) as im,Image.open(S/x['crop']['file']) as crop:
  a,b,c,d=x['boxXYXY'];assert 0<=a<c<=im.width and 0<=b<d<=im.height
  assert im.crop((a,b,c,d)).convert('RGB').tobytes()==crop.convert('RGB').tobytes()
c=read('CONTEXT_DISPOSITIONS.json');check(W/c['digitalSource']['file'],c['digitalSource']);raw=(W/c['digitalSource']['file']).read_text(encoding='utf-8-sig');a=raw.index('又云㸔官星有天');z=raw.index('喜忌篇云',a)
assert raw[a:z]==(S/'DIGITAL_CONTEXT.txt').read_text(encoding='utf-8')
clean=re.sub(r'[\s¶]','',re.sub(r'<pb:[^>]+>','',raw[a:z]));assert clean==(S/'CONTEXT_CLEAN.txt').read_text(encoding='utf-8')==''.join(x['literalDigital']for x in c['records']);assert len(clean)==439 and len(c['records'])==12
assert sha256(clean.encode()).hexdigest()==c['cleanSHA256']
actual=read('ACTUAL_RUNTIME.json');assert sha256((W/actual['libraryFile']).read_bytes()).hexdigest()==actual['librarySHA256'];assert sha256((S/'run-actual-once.mjs').read_bytes()).hexdigest()==actual['scriptSHA256'];assert sha256((S/'PREIMPLEMENTATION_FREEZE.json').read_bytes()).hexdigest()==actual['freezeSHA256']
reused=read('REUSED_ACTUAL_EVIDENCE.json');check(W/reused['file'],reused);assert all(x['actual']==x['expected']for x in actual['partners']+actual['naYin'])
out={'passed':True,'nativePositionsActuallyViewed':5,'selectedCropsRGBMatched':3,'digitalEditorialUnits':12,'digitalCodepoints':439,'frozenFiles':6,'newEngineCallsDuringChecks':0,'retainedActualNewTableQueries':10,'reusedPartnerQueries':6,'newHTTPBodies':0,'newContainers':0,'wholeChapterApplied':False,'consumerChanged':False}
if '--write-results' in sys.argv:(S/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
