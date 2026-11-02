from pathlib import Path
from hashlib import sha256
from PIL import Image
import json
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(n,d):(B/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def ident(p):return {'file':p.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
assert not(B/'PREIMPLEMENTATION_FREEZE.json').exists()and not(B/'fire-exception-reference.mjs').exists()
contexts=read(W/'v53/research/bazi-food-source/CONTEXTS.json')['records']
write('MANUAL_CONTEXT.json',{'sourceID':'TMTH005-FOOD-C31-Mijue','parent':next(r for r in contexts if r['id']=='FOOD-00-C31'),
 'selectedClause':'戊日庚時不宜火旺','sourceVoice':'秘訣','explicitDayStem':'戊','explicitHourStem':'庚',
 'unimplementedPrecedingPhrase':'食神一位勝似財官','singlePlaceDoesNotAutomaticallyMeanVisibleCountOne':True,
 'effectiveFireStrengthMustBeDeclared':True,'noAutomaticFireClassificationFromSummerOrVisibleStem':True,
 'neighborC30':{'context':next(r for r in contexts if r['id']=='FOOD-00-C30'),
 'hourOfficialMeaningUnresolved':True,'strictZhengguanVersusGenericGuanShaNotChosen':True,'implemented':False},
 'C13FireEarthStrengthConditionsHaveDifferentSourceContext':True,'notUniversalFoodGodFireProhibition':True,
 'wholeContextApplied':False,'sourceOutcomeValidated':False,'consumerApplied':False})
write('EXPECTED_CASES.json',{'cases':[
 {'day':'戊子','hour':'庚子','fire':True,'roleMatch':True,'fireContraindication':True},
 {'day':'戊寅','hour':'庚辰','fire':False,'roleMatch':True,'fireContraindication':False},
 {'day':'戊辰','hour':'庚午','fire':None,'roleMatch':True,'fireContraindication':None},
 {'day':'庚子','hour':'戊子','fire':True,'roleMatch':False,'fireContraindication':False},
 {'day':'甲子','hour':'庚子','fire':True,'roleMatch':False,'fireContraindication':False},
 {'day':None,'hour':'庚子','fire':True,'roleMatch':None,'fireContraindication':None},
 {'day':None,'hour':'甲子','fire':None,'roleMatch':False,'fireContraindication':False},
 {'day':None,'hour':None,'fire':False,'roleMatch':None,'fireContraindication':False}],
 'sourceID':'TMTH005-FOOD-C31-Mijue','frameID':'source-explicit-day-hour-fire-premise','booleanFalseIsNotGoodFortune':True})
p=W/'v53/research/bazi-food-source/p181.png';box=[1390,300,1840,2840];Image.open(p).convert('RGB').crop(box).save(B/'C31-native.png')
write('CROP_CANDIDATE.json',{'source':ident(p),'crop':ident(B/'C31-native.png'),'boxXYXY':box,'actuallyViewed':False,'newSourcePosition':False})
pair=next(r for r in read(W/'v53/qa/bazi-food-core/TEN_RELATION_RESULTS.json')['records']if r['declaredCoordinatePair']==['戊子','庚子'])
write('REUSE_IDENTITIES.json',{'files':[ident(W/p)for p in ['v53/research/bazi-food-source/CONTEXTS.json','v53/qa/bazi-food-core/TEN_RELATION_RESULTS.json',
 'v53/research/bazi-food-strength/CURRENT_CONTEXT_COVERAGE.json']], 'retainedActualPair':pair,'newEngineCalls':0,
 'pairDoesNotEstablishEffectiveStrengthOrFireContraindication':True,'currentMatrixCountsRemain':[46,44,0]})
print(json.dumps({'manualCases':8,'sourceID':'TMTH005-FOOD-C31-Mijue','newEngineCalls':0,'cropAwaitView':True}))
