from pathlib import Path
from hashlib import sha256
from PIL import Image
import json,re,sys
S=Path(__file__).resolve().parent;W=next(p for p in S.parents if (p/'v53/engine.js').is_file())
def read(n):return json.loads((S/n).read_text(encoding='utf-8-sig'))
def check(p,x):
 b=p.read_bytes();assert len(b)==x['bytes'] and sha256(b).hexdigest()==x['sha256'],p
for x in read('PREIMPLEMENTATION_FREEZE.json')['files']:check(S/x['file'],x)
n=read('NATIVE_REVIEW.json')
for key in ['retainedContainer','decoder']:check(W/n[key]['file'],n[key])
assert n['positionsActuallyViewed']==list(range(209,215)) and n['newPositionsActuallyViewed']==list(range(210,215))
for x in n['records']:
 check(S/x['file'],x);assert x['actuallyViewed']
 with Image.open(S/x['file']) as im:assert im.size==(x['width'],x['height']) and sha256(im.convert('RGBA').tobytes()).hexdigest()==x['pixelRGBA_SHA256']
for x in read('NATIVE_CROPS.json')['records']:
 check(S/x['raw']['file'],x['raw']);check(S/x['crop']['file'],x['crop']);assert x['actuallyViewed'] and x['accepted']
 with Image.open(S/x['raw']['file']) as raw,Image.open(S/x['crop']['file']) as crop:
  a,b,c,d=x['boxXYXY'];assert 0<=a<c<=raw.width and 0<=b<d<=raw.height
  assert raw.crop((a,b,c,d)).convert('RGB').tobytes()==crop.convert('RGB').tobytes()
d=read('CHAPTER_DISPOSITIONS.json');check(W/d['sourceDigital']['file'],d['sourceDigital']);raw=(W/d['sourceDigital']['file']).read_text(encoding='utf-8-sig');a=raw.index('　　論六害');z=raw.index('　　論三刑',a)
assert raw[a:z]==(S/'DIGITAL_CHAPTER_LOCATOR.txt').read_text(encoding='utf-8')
clean=re.sub(r'[\s¶]','',re.sub(r'<pb:[^>]+>','',raw[a:z]));assert clean==(S/'CHAPTER_CLEAN.txt').read_text(encoding='utf-8')
assert clean==''.join(x['literalDigital'] for x in d['records']) and len(clean)==717 and len(d['records'])==33
assert sha256(clean.encode()).hexdigest()==d['cleanSHA256'] and len(clean.encode('utf-16-le'))//2==719
m=read('MANUAL_TABLES.json');assert len(m['pairs'])==6 and len(m['directedClauses'])==7 and len(m['causalRows'])==6 and len(m['conditions'])==4
assert m['literalExample']['literal'] in clean
actual=read('ACTUAL_RUNTIME.json');assert actual['actualNewClashQueries']==12 and actual['actualNewNaYinQueries']==2 and actual['actualNewStemElementQueries']==2
assert sha256((S/'run-actual-once.mjs').read_bytes()).hexdigest()==actual['scriptSHA256']
assert sha256((S/'PREIMPLEMENTATION_FREEZE.json').read_bytes()).hexdigest()==actual['freezeSHA256']
assert all(x['expected']==x['actual'] for x in actual['clashes']) and all(x['naYin']==x['actualNaYin'] and x['stemElement']==x['actualStemElement'] for x in actual['pillars'])
assert sha256((W/actual['libraryFile']).read_bytes()).hexdigest()==actual['librarySHA256']
assert sha256((W/actual['reusedUnionEvidence']['file']).read_bytes()).hexdigest()==actual['reusedUnionEvidence']['sha256']
out={'passed':True,'nativePositionsActuallyViewed':6,'newPositionsActuallyViewed':5,'priorPositionReused':1,'nativePNGRGBAHashesMatched':6,'selectedCropsRGBMatched':2,'editorialUnits':33,'digitalCodepoints':717,'digitalUTF16Units':719,'frozenFiles':5,'retainedNewRuntimeQueries':16,'reusedUnionQueries':12,'newEngineCallsDuringChecks':0,'newHTTPBodies':0,'newContainers':0,'wholeChapterApplied':False,'consumerChanged':False}
if '--write-results' in sys.argv:(S/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
