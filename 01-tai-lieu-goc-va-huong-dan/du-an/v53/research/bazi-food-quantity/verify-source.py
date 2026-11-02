from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,sys
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def check(r):
 p=W/r['file'];assert p.stat().st_size==r['bytes']and sha256(p.read_bytes()).hexdigest()==r['sha256'],r['file']
for r in read(B/'PREIMPLEMENTATION_FREEZE.json')['files']+read(B/'REUSE_IDENTITIES.json')['files']:check(r)
s=read(B/'SOURCE_IDENTITIES.json')
for r in s['records']:
 check(r['source']);check(r['crop']);expected=Image.open(W/r['source']['file']).convert('RGB').crop(r['boxXYXY']);actual=Image.open(W/r['crop']['file']).convert('RGB');assert actual.size==expected.size and ImageChops.difference(actual,expected).getbbox()is None
for r in s['fullSourceImagesActuallyViewed']:check(r)
m=read(B/'MANUAL_CONTEXTS.json');contexts=read(W/'v53/research/bazi-food-source/CONTEXTS.json')['records']
for r in m['records']:assert r==next(x for x in contexts if x['id']==r['id'])
c=next(r for r in m['records']if r['id']=='FOOD-00-C23');assert len(c['text'])==102 and all(s in c['text']for s in m['selectedQuantityPhrases'])
assert m['C21SeparateVoice']['literal']in next(r for r in m['records']if r['id']=='FOOD-00-C21')['text']
pair=read(B/'REUSE_IDENTITIES.json')['actualRetainedPair'];assert pair in read(W/'v53/qa/bazi-food-core/TEN_RELATION_RESULTS.json')['records']and pair['actualLunarTenGod']=='食神'and pair['actualHHCTenGod']=='Thực Thần'
matrix=read(W/'v53/research/bazi-food-strength/CURRENT_CONTEXT_COVERAGE.json')
for id in ['FOOD-00-C19','FOOD-00-C21','FOOD-00-C23']:assert not next(r for r in matrix['records']if r['id']==id)['selectedModuleLinks']
assert m['sourceAnchorRole']is None and not m['C23EffectiveFoodSufficiencyCalculated']and not m['sourceOutcomeValidated']
out={'passed':True,'frozenFiles':5,'manualCases':8,'sourceContextsRetained':3,'C23Codepoints':102,'nativeCropsRGBMatched':2,'retainedImagesReexamined':3,
 'newHTTPBodies':0,'newSourcePositions':0,'newEngineCallsDuringVerification':0,'retainedActualFoodPairReused':1,'anchorRoleChosen':False,'wholeContextApplied':False,'consumerChanged':False}
if '--write-results'in sys.argv:(B/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
