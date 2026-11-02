from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(n,d):(B/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def ident(p):return {'file':p.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
assert not(B/'PREIMPLEMENTATION_FREEZE.json').exists()and not(B/'transformation-reference.mjs').exists()and not(B/'ACTUAL_RUNTIME.json').exists()
crop=read(B/'CROP_CANDIDATE.json');crop['actuallyViewed']=True;crop['reading']='Whole C16 question/answer visible across four columns, with preceding/following text kept as boundaries.'
write('SOURCE_IDENTITIES.json',crop)
partner_file='v53/research/bazi-true-ghost-context/ACTUAL_RUNTIME.json';appendix_file='v53/qa/bazi-food-appendices/REFERENCE_RESULTS.json'
partners=[]
for i,r in enumerate(read(W/partner_file)['partners']):partners.append({'stem':r['stem'],'actualPartner':r['actual'],'file':partner_file,'array':'partners','index':i})
for i,r in enumerate(read(W/appendix_file)['mechanisms']):
 if r['kind']=='combination':partners.append({'stem':r['foodStem'],'actualPartner':r['actualPartner'],'file':appendix_file,'array':'mechanisms','index':i})
assert len(partners)==10 and len({x['stem']for x in partners})==10
rows=read(B/'MANUAL_PAIR_CYCLE.json')['rows']
for r in rows:
 a,b=r['nativeImageWorkingPair'];assert next(x for x in partners if x['stem']==a)['actualPartner']==b and next(x for x in partners if x['stem']==b)['actualPartner']==a
write('REUSED_PARTNERS.json',{'rows':partners,'identities':[ident(W/p)for p in [partner_file,appendix_file]],
 'newPartnerQueries':0,'sourceTransformedElementValidatedByPartnerTable':False,'pairIdentityDoesNotEstablishEffectiveNatalCombination':True})
write('EXPECTED_INSPECTIONS.json',{'cases':[{'pairID':r['id'],'glyphPolicy':policy,
 'ordinaryCoordinateComparisonAvailable':policy=='retained-native-working-己'or r['id']not in ['jia-ji','ren-ding'],
 'ordinaryFoodGodRelations':2 if policy=='retained-native-working-己'or r['id']not in ['jia-ji','ren-ding']else None,
 'ordinaryNonFoodRelations':2 if policy=='retained-native-working-己'or r['id']not in ['jia-ji','ren-ding']else None,
 'allComponentRelationsAreFoodGod':False if policy=='retained-native-working-己'or r['id']not in ['jia-ji','ren-ding']else None,
 'effectiveTransformation':None,'sourceOutcome':None}for policy in ['digital-literal-only','retained-native-working-己']for r in rows],
 'expectedFullNativeCycle':['土','水','火','金','木'],'sourceVoiceName':'希尹','noGlobalGlyphEmendation':True,'noInferenceOfNatalTransformation':True})
write('ENGINE_IDENTITIES.json',{'files':[ident(W/p)for p in ['v53/engine.js','v53/bazi-relations.js','v46/node_modules/lunar-typescript/dist/index.cjs',
 'v53/research/bazi-food-source/CONTEXTS.json','v53/research/bazi-food-source/SOURCE_MANIFEST.json','v53/research/bazi-pattern-witness/CADAL06066041.djvu',
 'v53/research/bazi-food-strength/CURRENT_CONTEXT_COVERAGE.json']], 'engineVersion':'HHC retained V53','lunarVersion':'1.8.6','sourceMatrixCountsRemain':[46,44,0]})
names=['SOURCE_CONTEXT.json','MANUAL_PAIR_CYCLE.json','EXPECTED_RELATIONS.json','RUNTIME_PLAN.json','SOURCE_IDENTITIES.json','REUSED_PARTNERS.json','EXPECTED_INSPECTIONS.json','ENGINE_IDENTITIES.json']
write('PREIMPLEMENTATION_FREEZE.json',{'frozenAtUTC':datetime.now(timezone.utc).isoformat(),'files':[ident(B/n)for n in names],
 'referenceAndActualRuntimeAbsentAtFreeze':True,'newHHCRelationCallsPlanned':6,'newLunarTenGodTableQueriesPlanned':6,
 'retainedPairsPlanned':14,'retainedPartnerCoordinates':10,'consumerChanged':False,'wholeContextApplied':False})
print(json.dumps({'frozenFiles':8,'manualInspections':10,'retainedRelationPairs':14,'missingPairsToExecuteOnce':6,'retainedPartnerCoordinates':10}))
