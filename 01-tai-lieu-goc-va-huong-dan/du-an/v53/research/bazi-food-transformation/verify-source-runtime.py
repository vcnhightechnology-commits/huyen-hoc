from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,sys
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def digest(p):return sha256(p.read_bytes()).hexdigest()
def check(r):
 p=W/r['file'];assert p.stat().st_size==r['bytes']and digest(p)==r['sha256'],r['file']
freeze=read(B/'PREIMPLEMENTATION_FREEZE.json');plan=read(B/'RUNTIME_PLAN.json');p=read(B/'REUSED_PARTNERS.json')
for r in freeze['files']+read(B/'ENGINE_IDENTITIES.json')['files']+plan['retainedPayloadIdentities']+p['identities']:check(r)
s=read(B/'SOURCE_IDENTITIES.json');check(s['source']);check(s['crop']);expected=Image.open(W/s['source']['file']).convert('RGB').crop(s['boxXYXY']);actual=Image.open(W/s['crop']['file']).convert('RGB');assert actual.size==expected.size and ImageChops.difference(actual,expected).getbbox()is None
c=read(B/'SOURCE_CONTEXT.json')['parent'];assert c==next(x for x in read(W/'v53/research/bazi-food-source/CONTEXTS.json')['records']if x['id']==c['id'])
cycle=read(B/'MANUAL_PAIR_CYCLE.json');assert len(c['text'])==62 and all(r['sourceClause']in c['text']for r in cycle['rows'])
run=read(B/'ACTUAL_RUNTIME.json');assert run['scriptSHA256']==digest(B/'run-actual-once.mjs')and run['freezeSHA256']==digest(B/'PREIMPLEMENTATION_FREEZE.json')
for key,file in [('engineSHA256','v53/engine.js'),('relationsSHA256','v53/bazi-relations.js'),('lunarLibrarySHA256','v46/node_modules/lunar-typescript/dist/index.cjs')]:assert run[key]==digest(W/file)
assert len(run['newRows'])==run['actualNewHHCGodCalls']==run['actualNewLunarTenGodTableQueries']==6
assert len(run['reusedRows'])==run['retainedRelationPairsReused']==14
assert not run['transformationValidated']and not run['sourceOutcomeValidated']and run['actualCalendarObjects']==run['actualNatalCharts']==0
for actual,e in zip(run['newRows'],plan['missing']):
 assert all(actual[k]==v for k,v in e.items())and actual['actualHHC']==e['expectedHHC']and actual['actualLunar']==e['expectedLunar']and actual['newCall']
for actual,e in zip(run['reusedRows'],plan['reuse']):
 assert all(actual[k]==v for k,v in e.items())and not actual['newCall']
 r=e['retained'];original=read(W/r['file'])[r['array']][r['index']]
 if 'declaredCoordinatePair'in original:a,t=(x[0]for x in original['declaredCoordinatePair'])
 elif 'rootPillar'in original:a,t=original['rootPillar'][0],original['targetPillar'][0]
 else:a,t=original['root'],original['target']
 assert a==r['root']and t==r['target']and original['actualHHCTenGod']==actual['actualHHC']and original['actualLunarTenGod']==actual['actualLunar']
all_rows=run['newRows']+run['reusedRows'];assert len({(r['root'],r['target'])for r in all_rows})==20
assert sum(r['actualLunar']=='食神'for r in all_rows)==10
assert sum(r['actualLunar']=='正官'for r in all_rows)==5 and sum(r['actualLunar']=='正印'for r in all_rows)==5
for r in p['rows']:
 original=read(W/r['file'])[r['array']][r['index']]
 assert (original['stem'],original['actual'])==(r['stem'],r['actualPartner'])if r['array']=='partners'else (original['foodStem'],original['actualPartner'])==(r['stem'],r['actualPartner'])
matrix=read(W/'v53/research/bazi-food-strength/CURRENT_CONTEXT_COVERAGE.json');parent=next(x for x in matrix['records']if x['id']=='FOOD-00-C16');assert not parent['selectedModuleLinks']and not parent['wholeContextApplied']
out={'passed':True,'frozenFiles':8,'sourceClauses':5,'digitalCodepoints':62,'nativeCropRGBMatches':1,'sourceGlyphsGloballyEmended':False,
 'retainedActualComponentCoordinates':20,'previouslyNewPairsRunOnce':6,'newHHCQueriesAtThatRun':6,'newLunarQueriesAtThatRun':6,
 'retainedRelationPairsReused':14,'retainedPartnerCoordinatesReused':10,'newEngineCallsDuringVerification':0,
 'newHTTPBodies':0,'newSourcePositions':0,'wholeContextApplied':False,'sourceTransformationValidated':False,'consumerChanged':False}
if '--write-results'in sys.argv:(B/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
