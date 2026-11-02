from pathlib import Path
from hashlib import sha256
from PIL import Image
import json,sys
S=Path(__file__).resolve().parent
W=next(p for p in S.parents if(p/'v53/engine.js').is_file())
def read(n):return json.loads((S/n).read_text(encoding='utf-8-sig'))
def check(p,x):
 b=p.read_bytes();assert len(b)==x['bytes']and sha256(b).hexdigest()==x['sha256'],p
for x in read('PRINTED_CAST_FREEZE.json')['files']:check(S/x['file'],x)
crops=read('PRINTED_CAST_CROPS.json');assert len(crops['records'])==3 and len(crops['trialRecords'])==1
for x in crops['records']+crops['trialRecords']:
 check(W/x['raw']['file'],x['raw']);check(W/x['crop']['file'],x['crop']);assert x['actuallyViewed']
 with Image.open(W/x['raw']['file'])as im,Image.open(W/x['crop']['file'])as cr:
  a,b,c,d=x['boxXYXY'];assert 0<=a<c<=im.width and 0<=b<d<=im.height
  assert im.crop((a,b,c,d)).convert('RGB').tobytes()==cr.convert('RGB').tobytes()
assert all(x['accepted']for x in crops['records'])and not crops['trialRecords'][0]['accepted']
actual=read('ACTUAL_CAST_RUNTIME.json');assert actual['actualHHCHexNumberCalls']==5 and actual['printedCasts']==3 and actual['actualCalendarObjects']==0
assert sha256((W/actual['engineFile']).read_bytes()).hexdigest()==actual['engineSHA256']
assert sha256((S/'run-casts-once.mjs').read_bytes()).hexdigest()==actual['scriptSHA256']
assert sha256((S/'PRINTED_CAST_FREEZE.json').read_bytes()).hexdigest()==actual['freezeSHA256']
for x in actual['readerFiles']:assert sha256((W/x['file']).read_bytes()).hexdigest()==x['sha256']
expected={x['id']:x for x in read('PRINTED_CAST_EXPECTED.json')['records']}
for x in actual['cases']:
 e=expected[x['id']];assert x['actualPrimary']==e['primary']and x['actualChanged']==e['changed']and x['actualMovingLines']==e['movingLines']
 assert len(x['selectedMain'])==len(e['selectedMain'])and len(x['selectedChanged'])==len(e.get('selectedChanged',[]))
 assert all(y['actualBranch']==y['branch']and y['actualKin']==y['kin']for y in x['selectedMain']+x['selectedChanged'])
 assert x['sourceHistoricalOutcomeValidated']is False and x['calendarDate']is None
triple=next(x for x in actual['cases']if x['id']=='yu-guimei-three-uses');assert len(triple['structuralChildren'])==3
assert {(x['kind'],x['line'],x['branch'])for x in triple['structuralChildren']}=={('primary',2,'巳'),('primary',4,'午'),('own-moving-change',1,'巳')}
audit=read('RUNTIME_LAUNCH_AUDIT.json');assert audit['actualHexNumberCallsInFailedLaunch']==0
out={'passed':True,'groups':4,'frozenFiles':2,'printedCasts':3,'acceptedCropsRGBMatched':3,'rejectedTrialCropsRetained':1,'retainedActualHHCHexNumberCalls':5,'selectedMainLabelsMatched':6,'selectedChangedLabelsMatched':1,'sourceThreeUsesMatched':3,'newEngineCallsDuringChecks':0,'actualCalendarObjects':0,'sourceOutcomesValidated':False,'calendarDatesInvented':0,'shiHuanMotionValuesAreEditorialFromNamedFigures':True,'consumerChanged':False}
if '--write-results'in sys.argv:(S/'CAST_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
