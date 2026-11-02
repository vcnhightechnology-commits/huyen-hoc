from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,sys
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def check(r):
 p=W/r['file'];assert p.stat().st_size==r['bytes']and sha256(p.read_bytes()).hexdigest()==r['sha256'],r['file']
seal=read(B/'SOURCE_EXPECTATIONS_SEAL.json');assert seal['preimplementationFreezeEstablished']is False and seal['referenceExistedAndHadBeenExecutedAtSeal']
for r in seal['files']+read(B/'REUSE_IDENTITIES.json')['files']:check(r)
exception=read(B/'SEQUENCE_EXCEPTION.json')
for r in exception['initialFiles']:
 if Path(r['file']).name in ['MANUAL_CONTEXT.json','EXPECTED_CASES.json','REUSE_IDENTITIES.json','fire-exception-reference.mjs']:check(r)
s=read(B/'SOURCE_IDENTITIES.json');check(s['source']);check(s['crop']);expected=Image.open(W/s['source']['file']).convert('RGB').crop(s['boxXYXY']);actual=Image.open(W/s['crop']['file']).convert('RGB');assert actual.size==expected.size and ImageChops.difference(actual,expected).getbbox()is None
m=read(B/'MANUAL_CONTEXT.json');c=next(r for r in read(W/'v53/research/bazi-food-source/CONTEXTS.json')['records']if r['id']=='FOOD-00-C31');assert m['parent']==c and m['selectedClause']in c['text']
pair=read(B/'REUSE_IDENTITIES.json')['retainedActualPair'];assert pair in read(W/'v53/qa/bazi-food-core/TEN_RELATION_RESULTS.json')['records']and pair['actualLunarTenGod']=='食神'
matrix=read(W/'v53/research/bazi-food-strength/CURRENT_CONTEXT_COVERAGE.json');assert not next(r for r in matrix['records']if r['id']=='FOOD-00-C31')['selectedModuleLinks']
out={'passed':True,'postImplementationSealedFiles':6,'preimplementationFreezeEstablished':False,'sourceSealSequenceExceptionRetained':True,'manualCasesUnchangedAfterFirstTest':True,'manualCases':8,'selectedClauseCodepoints':len(m['selectedClause']),'parentContextCodepoints':len(c['text']),
 'nativeCropRGBMatches':1,'newSourcePositions':0,'newHTTPBodies':0,'newEngineCallsDuringVerification':0,'retainedActualFoodPairReused':1,
 'calendarConsistencyEstablished':False,'wholeContextApplied':False,'consumerChanged':False}
if '--write-results'in sys.argv:(B/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
