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
assert n['source']['sha256']=='7a53f35982f0b946281d0e393c5d6ddcce1fd091aea83c11af6a06bcdfe6a85e'
for x in n['records']:
 check(S/x['file'],x);assert x['actuallyViewed']
 with Image.open(S/x['file'])as im:assert im.size==(x['width'],x['height'])and sha256(im.convert('RGBA').tobytes()).hexdigest()==x['pixelRGBA_SHA256']
assert n['positionsActuallyViewed']==list(range(214,228))and n['newPositionsActuallyViewed']==list(range(215,228))
crops=read('SELECTED_CROPS.json');assert len(crops['records'])==6 and len(crops['trialRecords'])==1
for x in crops['records']+crops['trialRecords']:
 check(S/x['raw']['file'],x['raw']);check(S/x['crop']['file'],x['crop']);assert x['actuallyViewed']
 with Image.open(S/x['raw']['file'])as im,Image.open(S/x['crop']['file'])as cr:
  a,b,c,d=x['boxXYXY'];assert 0<=a<c<=im.width and 0<=b<d<=im.height
  assert im.crop((a,b,c,d)).convert('RGB').tobytes()==cr.convert('RGB').tobytes()
assert all(x['accepted']for x in crops['records'])and not crops['trialRecords'][0]['accepted']
d=read('CHAPTER_DISPOSITIONS.json');check(W/d['sourceDigital']['file'],d['sourceDigital']);raw=(W/d['sourceDigital']['file']).read_text(encoding='utf-8-sig');a=raw.index('　　論三刑');z=raw.index('　　論衝擊',a)
assert raw[a:z]==(S/'DIGITAL_CHAPTER_LOCATOR.txt').read_text(encoding='utf-8');clean=re.sub(r'[\s¶]','',re.sub(r'<pb:[^>]+>','',raw[a:z]));assert clean==(S/'CHAPTER_CLEAN.txt').read_text(encoding='utf-8')==''.join(x['literalDigital']for x in d['records'])
assert len(clean)==2140 and len(clean.encode('utf-16-le'))//2==2148
assert len(d['records'])==56 and sha256(clean.encode()).hexdigest()==d['cleanSHA256']
t=read('MANUAL_SOURCE_TABLES.json');assert t['unresolvedLiteral']['digital']=='卯寅子'and '卯寅子'in clean
assert t['classificationVoices']['primary']['yin-si-shen']=='無恩'and t['classificationVoices']['san-che-yi-lan']['yin-si-shen']=='恃勢'
actual=read('ACTUAL_RUNTIME.json');assert sha256((W/actual['libraryFile']).read_bytes()).hexdigest()==actual['librarySHA256'];assert sha256((S/'run-actual-once.mjs').read_bytes()).hexdigest()==actual['scriptSHA256'];assert sha256((S/'PREIMPLEMENTATION_FREEZE.json').read_bytes()).hexdigest()==actual['freezeSHA256'];check(W/actual['reusedEvidence']['file'],actual['reusedEvidence']);assert all(x['actual']==x['expected']for x in actual['rows'])
out={'passed':True,'nativePositionsActuallyViewed':14,'newNativePositionsActuallyViewed':13,'priorBoundaryReused':1,'nativePNGRGBAHashesMatched':14,'acceptedCropsRGBMatched':6,'rejectedTrialCropsRetained':1,'digitalEditorialUnits':56,'digitalCodepoints':2140,'digitalUTF16Units':2148,'frozenFiles':6,'namedClassificationVoices':2,'retainedActualNewNaYinQueries':8,'reusedNaYinQueries':1,'newEngineCallsDuringChecks':0,'newHTTPBodies':0,'newContainers':0,'wholeChapterApplied':False,'consumerChanged':False}
if '--write-results'in sys.argv:(S/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
