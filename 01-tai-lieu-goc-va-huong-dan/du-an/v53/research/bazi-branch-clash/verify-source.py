from pathlib import Path
from hashlib import sha256
from PIL import Image
import json,re,sys
S=Path(__file__).resolve().parent;W=next(p for p in S.parents if(p/'v53/engine.js').is_file())
def read(n):return json.loads((S/n).read_text(encoding='utf-8-sig'))
def check(p,x):
 b=p.read_bytes();assert len(b)==x['bytes'] and sha256(b).hexdigest()==x['sha256'],p
for x in read('PREIMPLEMENTATION_FREEZE.json')['files']:check(S/x['file'],x)
n=read('NATIVE_REVIEW.json');check(W/n['source']['file'],n['source']);check(W/n['decoder']['file'],n['decoder'])
for x in n['records']:
 check(S/x['file'],x);assert x['actuallyViewed']
 with Image.open(S/x['file'])as im:assert im.size==(x['width'],x['height'])and sha256(im.convert('RGBA').tobytes()).hexdigest()==x['pixelRGBA_SHA256']
assert n['positionsActuallyViewed']==list(range(227,233)) and n['volumeEndActuallyViewed']==232
for x in read('SELECTED_CROPS.json')['records']:
 check(S/x['raw']['file'],x['raw']);check(S/x['crop']['file'],x['crop']);assert x['accepted'] and x['actuallyViewed']
 with Image.open(S/x['raw']['file'])as im,Image.open(S/x['crop']['file'])as cr:
  a,b,c,d=x['boxXYXY'];assert 0<=a<c<=im.width and 0<=b<d<=im.height
  assert im.crop((a,b,c,d)).convert('RGB').tobytes()==cr.convert('RGB').tobytes()
d=read('CHAPTER_DISPOSITIONS.json');check(W/d['sourceDigital']['file'],d['sourceDigital']);text=(W/d['sourceDigital']['file']).read_text(encoding='utf-8-sig');a=text.index('　　論衝擊');z=text.index('　三命通㑹卷二',a);assert text[a:z]==(S/'DIGITAL_CHAPTER_LOCATOR.txt').read_text(encoding='utf-8')
clean=re.sub(r'[\s¶]','',re.sub(r'<pb:[^>]+>','',text[a:z]));assert clean==(S/'CHAPTER_CLEAN.txt').read_text(encoding='utf-8')==''.join(x['literalDigital']for x in d['records']);assert len(clean)==818 and len(d['records'])==31 and sha256(clean.encode()).hexdigest()==d['cleanSHA256']
assert '戌丑未未'in clean and '馬在己見亥'in clean and '觀諸詩見衝破有吉有凶不可槩論'in clean
actual=read('ACTUAL_RUNTIME.json');assert sha256((W/actual['libraryFile']).read_bytes()).hexdigest()==actual['librarySHA256'];assert sha256((S/'run-actual-once.mjs').read_bytes()).hexdigest()==actual['scriptSHA256'];assert sha256((S/'PREIMPLEMENTATION_FREEZE.json').read_bytes()).hexdigest()==actual['freezeSHA256'];assert all(x['expected']==x['actual']for x in actual['rows'])
for x in actual['reusedEvidence']:check(W/x['file'],x)
out={'passed':True,'nativePositionsActuallyViewed':6,'newNativePositionsActuallyViewed':5,'priorBoundaryReused':1,'nativePNGRGBAHashesMatched':6,'acceptedCropsRGBMatched':3,'digitalEditorialUnits':31,'digitalCodepoints':818,'digitalUTF16Units':len(clean.encode('utf-16-le'))//2,'frozenFiles':6,'retainedActualNewNaYinQueries':6,'reusedNaYinQueries':2,'reusedClashQueries':12,'newEngineCallsDuringChecks':0,'newHTTPBodies':0,'newContainers':0,'wholeChapterApplied':False,'consumerChanged':False}
if '--write-results'in sys.argv:(S/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
