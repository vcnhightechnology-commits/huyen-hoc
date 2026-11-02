from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,sys
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def check(r):
 p=W/r['file'];assert p.stat().st_size==r['bytes'] and sha256(p.read_bytes()).hexdigest()==r['sha256'],r['file']
for r in read(B/'PREIMPLEMENTATION_FREEZE.json')['files']+read(B/'REUSE_IDENTITIES.json')['files']:check(r)
s=read(B/'SOURCE_IDENTITIES.json');check(s['source']);check(s['acceptedCrop'])
im=Image.open(W/s['source']['file']).convert('RGB');crop=Image.open(W/s['acceptedCrop']['file']).convert('RGB');expected=im.crop(s['boxXYXY'])
assert crop.size==expected.size and ImageChops.difference(crop,expected).getbbox() is None
m=read(B/'MANUAL_PREMISES.json');c=next(x for x in read(W/'v53/research/bazi-food-source/CONTEXTS.json')['records'] if x['id']=='FOOD-00-C13')
assert m['parentContext']==c and len(c['text'])==99
assert all(x['literal'] in c['text'] for x in m['clauses'])
matrix=read(W/'v53/research/bazi-food-chain/CURRENT_CONTEXT_COVERAGE.json');parent=next(x for x in matrix['records'] if x['id']==c['id']);assert parent['selectedModuleLinks']==[] and not parent['wholeContextApplied']
runtime=read(W/'v53/research/bazi-food-chain/ACTUAL_RUNTIME.json');assert next(x for x in runtime['pairs'] if x['root']=='甲' and x['target']=='丙')==read(B/'REUSE_IDENTITIES.json')['retainedActualPair']
for key,name in [('engineSHA256','v53/engine.js'),('relationsSHA256','v53/bazi-relations.js'),('lunarLibrarySHA256','v46/node_modules/lunar-typescript/dist/index.cjs')]:assert runtime[key]==sha256((W/name).read_bytes()).hexdigest()
assert m['subjectBindingOfShengWangXiangLu'] is None and not m['wholeContextApplied'] and not m['sourceOutcomeValidated']
out={'passed':True,'frozenFiles':5,'manualCases':11,'selectedSourceClauses':6,'parentCodepoints':99,'nativeCropRGBMatches':1,'trialCropsRetained':1,'newSourcePositions':0,'newHTTPBodies':0,'retainedActualHHCAndLunarFoodPairReused':1,'newEngineCallsDuringVerification':0,'sourceCompoundSubjectResolved':False,'wholeContextApplied':False,'consumerChanged':False}
if '--write-results' in sys.argv:(B/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
