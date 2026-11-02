from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(n,d):(B/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def identity(p):return {'file':p.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
assert not(B/'FREEZE.json').exists()and not(B/'label-scope.mjs').exists()
c=read(W/'v53/research/bazi-food-source/CONTEXTS.json')['records']
contexts=[next(r for r in c if r['id']==id)for id in ['FOOD-00-C18','FOOD-00-C19']]
write('SOURCE_REVIEW.json',{'contexts':contexts,'imageActuallyViewed':identity(W/'v53/research/bazi-food-source/p177.png'),
 'anchor':'丙辰為正印','C19Literal':'若有華葢正印雖少増培無學堂驛馬雖多減半',
 'C18Meaning':'Source whole-pillar label for甲子/丙辰, not ordinary stem TenGod正印.',
 'C19Meaning':None,'C19SameAsC18NotEstablished':True,'C19SameAsOrdinaryTenGodNotEstablished':True,
 'C19ListSegmentationAdjudicated':False,'compoundClausesDoNotEstablishANumericHalfMultiplier':True,
 'sourceLabelsAreNotUniversalNamespaces':True,'consumerChanged':False,'wholeContextApplied':False})
write('EXPECTED.json',{'cases':[{'id':'source-exact','contextID':'FOOD-00-C18','root':'甲子','target':'丙辰','basis':'declared-source-example','literalLabel':'正印','ordinaryRelation':'食神'},
 {'id':'source-other-target','contextID':'FOOD-00-C18','root':'甲子','target':'丙寅','basis':'declared-source-example','literalLabel':None,'ordinaryRelation':'食神'},
 {'id':'source-day-not-assigned','contextID':'FOOD-00-C18','root':'甲子','target':'丙辰','basis':'natal-day','literalLabel':None,'ordinaryRelation':None},
 {'id':'source-missing','contextID':'FOOD-00-C18','root':'甲子','target':None,'basis':'declared-source-example','literalLabel':None,'ordinaryRelation':None},
 {'id':'C19-unresolved','contextID':'FOOD-00-C19','root':None,'target':None,'basis':'unresolved-source-clause','literalLabel':None,'ordinaryRelation':None}]})
paths=['v53/research/bazi-food-source/CONTEXTS.json','v53/research/bazi-food-source/p177.png',
 'v53/research/bazi-food-six-pillars/source-pillar-example.mjs','v53/research/bazi-food-six-pillars/MANUAL_PILLAR_EXAMPLES.json',
 'v53/qa/bazi-food-six-pillars/REFERENCE_RESULTS.json','v53/research/bazi-food-quantity/CURRENT_CONTEXT_COVERAGE.json']
write('REUSE.json',{'files':[identity(W/p)for p in paths], 'actualRelation':read(W/paths[4])['uniqueRelation'],
 'newEngineCalls':0,'currentParentCounts':[49,41,0]})
write('FREEZE.json',{'atUTC':datetime.now(timezone.utc).isoformat(),'referenceAbsent':True,
 'files':[identity(B/n)for n in ['SOURCE_REVIEW.json','EXPECTED.json','REUSE.json']],
 'actualNewEngineCallsPlanned':0,'C19SemanticResolution':None})
print(json.dumps({'frozenFiles':3,'cases':5,'newEngineCalls':0}))
