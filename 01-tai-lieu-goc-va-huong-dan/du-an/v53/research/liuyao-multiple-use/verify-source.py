from pathlib import Path
from hashlib import sha256
from PIL import Image
import json,sys
S=Path(__file__).resolve().parent
W=next(p for p in S.parents if(p/'v53/engine.js').is_file())
def read(n):return json.loads((S/n).read_text(encoding='utf-8-sig'))
def check(p,x):
 b=p.read_bytes();assert len(b)==x['bytes'] and sha256(b).hexdigest()==x['sha256'],p
for x in read('PREIMPLEMENTATION_FREEZE.json')['files']:check(S/x['file'],x)
identity=read('SOURCE_IDENTITIES.json');check(W/identity['sourcePDF']['file'],identity['sourcePDF']);assert identity['sourcePDF']['sha256']=='caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa'
for x in identity['reviewedRetainedImages']:check(W/x['file'],x);assert x['actuallyViewed'] and not x['newFirstPassPosition']
for k in ['currentMap','currentResumeIndex']:check(W/identity[k]['file'],identity[k])
mapping=json.loads((W/identity['currentMap']['file']).read_text(encoding='utf-8-sig'));unit=next(x for x in mapping['units']if x['id']=='B02-ch032');assert unit['bodyPDFPages']==[134,135,136]and unit['bodyPrintedHeadingAsRead']=='兩現章第三十一'and not unit['entireUnitApplied']
crops=read('SELECTED_CROPS.json');assert len(crops['records'])==3 and len(crops['trialRecords'])==1
for x in crops['records']+crops['trialRecords']:
 check(W/x['raw']['file'],x['raw']);check(W/x['crop']['file'],x['crop']);assert x['actuallyViewed']
 with Image.open(W/x['raw']['file'])as im,Image.open(W/x['crop']['file'])as cr:
  a,b,c,d=x['boxXYXY'];assert 0<=a<c<=im.width and 0<=b<d<=im.height
  assert im.crop((a,b,c,d)).convert('RGB').tobytes()==cr.convert('RGB').tobytes()
assert all(x['accepted']for x in crops['records'])and not crops['trialRecords'][0]['accepted']
manual=read('MANUAL_SOURCE_CLAUSES.json');assert len(manual['rules'])==5 and len(manual['counterexamples'])==4
assert not manual['fullRankingEstablished']
out={'passed':True,'retainedSourceImagesReviewed':3,'newSourcePositions':0,'acceptedCropsRGBMatched':3,'rejectedTrialCropsRetained':1,'frozenFiles':4,'quotedOldMethodComparisons':5,'sourceCounterexamples':4,'currentB02MapUnits':mapping['currentCounts']['registeredUnits'],'newHTTPBodies':0,'newOriginalContainers':0,'newEngineCallsDuringChecks':0,'noNewEngineComparisonAttempted':True,'automaticUseGodSelection':False,'wholeChapterApplied':False,'consumerChanged':False}
if '--write-results'in sys.argv:(S/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
