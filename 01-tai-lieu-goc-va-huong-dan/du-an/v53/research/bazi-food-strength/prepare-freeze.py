"""Freeze selected C13 source premises and manual expectations before implementation."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
B=Path(__file__).resolve().parent
W=next(p for p in B.parents if (p/'v53/engine.js').is_file())
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(n,d):(B/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def identity(p):return {'file':p.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
assert not (B/'PREIMPLEMENTATION_FREEZE.json').exists()
assert not (B/'strength-reference.mjs').exists()
context=next(x for x in read(W/'v53/research/bazi-food-source/CONTEXTS.json')['records'] if x['id']=='FOOD-00-C13')
assert len(context['text'])==99 and context['voice']=='quoted-voice'
manual={'sourceID':'TMTH005-FOOD-C13','parentContext':context,'image':'v53/research/bazi-food-source/p173.png','folio':'005-86a',
 'clauses':[
 {'id':'opening-literal','literal':'甲日食丙柱中無壬癸亥子方好','subjects':{'day':'甲','food':'丙'},'literalWaterMarkers':['壬','癸','亥','子'],'boundary':'Visible literal coordinates only; missing pillars do not prove absence, hidden stems and effective water are not computed.'},
 {'id':'water-restraint','literal':'如有水氣丙自受制','subject':'丙','boundary':'水氣 is a source functional premise, not automatically equal to any visible marker.'},
 {'id':'continuing','literal':'如無此制又要生旺向禄','subject':None,'boundary':'Additional compound condition, not automatically resolved to丙,甲 or a specific twelve-phase label.'},
 {'id':'summer','literal':'如丙生夏月運厯東南火土俱旺','subjects':['丙','火','土'],'boundary':'夏月 and東南 do not themselves establish火土俱旺; no conversion from a Gregorian/lunar month or luck pillar.'},
 {'id':'spring-contrast','literal':'若生三春甲旺丙火雖得生不知戊巳氣薄','subjects':['甲','丙火','戊巳'],'boundary':'Three distinct predicates; source digital巳 is not silently changed to己.'},
 {'id':'spring-continuation','literal':'須厯南方火土俱旺方許發福','subjects':['火','土'],'boundary':'Selected conditions only;發福 is not an implemented or validated outcome.'}],
 'glyphReadings':[{'digital':'巳身','imageWorkingReading':'己身','status':'native-image local working reading, digital bytes unchanged'},
 {'digital':'戊巳','imageWorkingReading':'戊己','status':'native-image local working reading, glyph policy explicit; no all-context emendation'}],
 'outcomePhrasesUnimplemented':['屈伏於人','不能卓立','生物以養其父','用財必厚','方許發福'],
 'subjectBindingOfShengWangXiangLu':None,'calendarAdapter':False,'wholeContextApplied':False,'sourceOutcomeValidated':False,'consumerApplied':False}
write('MANUAL_PREMISES.json',manual)
facts=['bingWaterRestraintAbsent','continuingShengWangXiangLuSatisfied','fireStrong','earthStrong','jiaStrong','bingReceivesGeneration','wuJiQiThin']
write('DECLARED_FRAME.json',{'sourceID':manual['sourceID'],'frameID':'declared-source-strength-context','pillarOrder':['year','month','day','hour'],
 'pillars':'Exactly four sexagenary-canonical two-character stems/branches or explicit null; no hidden stems.',
 'sourceBirthSeason':['summer','three-spring','other',None],'sourceLuckRegion':['東南','南方','other',None],
 'requiredFacts':facts,'factValues':[True,False,None],
 'factMeaning':{'bingWaterRestraintAbsent':'Declared absence of functional water restraint on丙, separate from visible water markers.',
 'continuingShengWangXiangLuSatisfied':'Declared satisfaction of the whole source compound生旺向祿, subject binding still unresolved.',
 'fireStrong':'Declared火旺, not inferred from夏月/東南.', 'earthStrong':'Declared土旺, separate from火旺.',
 'jiaStrong':'Declared甲旺, not identical to丙受生.', 'bingReceivesGeneration':'Declared丙火得生, not identical to戊己氣厚.',
 'wuJiQiThin':'Declared spring contrast戊巳氣薄 (working image戊己); no element score.'},
 'allFieldsMustBeExplicit':True,'missingMeansUnknownOnlyWhenExplicitNull':True,'premiseMatchesAreNotOutcomes':True})
def case(id,season,region,updates,expected):return {'id':id,'season':season,'region':region,'facts':updates,'expected':expected}
write('EXPECTED_CASES.json',{'basePillars':['甲寅','丙寅','甲子','戊辰'],'baseFacts':{k:None for k in facts},'cases':[
 case('all-unknown',None,None,{}, {'continuingRequirements':None,'summerRequirements':None,'springContrast':None,'springSouthernRequirements':None}),
 case('summer-attributes-without-strength','summer','東南',{}, {'summerRequirements':None}),
 case('summer-explicit-complete','summer','東南',dict.fromkeys(facts[:4],True),{'continuingRequirements':True,'summerRequirements':True,'springContrast':False,'springSouthernRequirements':False}),
 case('summer-earth-missing','summer','東南',{'bingWaterRestraintAbsent':True,'continuingShengWangXiangLuSatisfied':True,'fireStrong':True},{'summerRequirements':None}),
 case('summer-earth-false','summer','東南',{'bingWaterRestraintAbsent':True,'continuingShengWangXiangLuSatisfied':True,'fireStrong':True,'earthStrong':False},{'summerRequirements':False}),
 case('summer-compound-missing','summer','東南',{'bingWaterRestraintAbsent':True,'fireStrong':True,'earthStrong':True},{'continuingRequirements':None,'summerRequirements':None}),
 case('spring-contrast-only','three-spring',None,{'jiaStrong':True,'bingReceivesGeneration':True,'wuJiQiThin':True},{'springContrast':True,'springSouthernRequirements':None}),
 case('spring-southern-requirements','three-spring','南方',dict.fromkeys(facts[:4],True),{'springSouthernRequirements':True,'springContrast':None}),
 case('spring-east-south-is-not-south','three-spring','東南',dict.fromkeys(facts[:4],True),{'springSouthernRequirements':False}),
 case('known-restraint-blocks','summer','東南',{'bingWaterRestraintAbsent':False,'continuingShengWangXiangLuSatisfied':True,'fireStrong':True,'earthStrong':True},{'continuingRequirements':False,'summerRequirements':False,'waterRestraintBranch':True}),
 case('jia-strength-alone','three-spring','南方',{'jiaStrong':True},{'springContrast':None,'springSouthernRequirements':None})],
 'absentVisibleWaterDoesNotEstablishEffectiveAbsence':True,'phaseLabelsDoNotEstablishStrength':True,'noOutcomeExpected':True})
paths=['v53/research/bazi-food-source/CONTEXTS.json','v53/research/bazi-food-source/p173.png',
 'v53/research/bazi-food-chain/CURRENT_CONTEXT_COVERAGE.json','v53/research/bazi-food-chain/ACTUAL_RUNTIME.json',
 'v53/research/bazi-food-chain/PREIMPLEMENTATION_FREEZE.json','v53/engine.js','v53/bazi-relations.js',
 'v46/node_modules/lunar-typescript/dist/index.cjs','v53/research/bazi-food-core/core-reference.mjs']
runtime=read(W/paths[3]);pair=next(x for x in runtime['pairs'] if x['root']=='甲' and x['target']=='丙')
assert pair['actualHHCTenGod']=='Thực Thần' and pair['actualLunarTenGod']=='食神'
write('REUSE_IDENTITIES.json',{'files':[identity(W/p) for p in paths], 'retainedActualPair':pair,'reuseFrom':paths[3],
 'actualNewEngineCalls':0,'actualNewCalendarObjects':0,'fixedRelationDoesNotEstablishStrength':True,'parentMatrixHistoricalCounts':[44,46,0]})
write('SOURCE_IDENTITIES.json',{'source':identity(W/paths[1]),'acceptedCrop':identity(B/'C13-entry-complete-native.png'),
 'boxXYXY':[335,295,1715,2895],'actuallyViewed':True,'nativeNoResampling':True,
 'rejectedTrial':{'file':'C13-complete-native.png','boxXYXY':[335,295,1440,2895],'reason':'Initial又曰甲日食 column absent; viewed and retained as trial, not complete proof.'},
 'newHTTPBodies':0,'newSourcePositions':0,'newIndependentWitnesses':0})
write('PREIMPLEMENTATION_FREEZE.json',{'frozenAtUTC':datetime.now(timezone.utc).isoformat(),
 'scope':'Selected C13 premises and manual expected cases, before reference implementation',
 'files':[identity(B/n)for n in ['MANUAL_PREMISES.json','DECLARED_FRAME.json','EXPECTED_CASES.json','REUSE_IDENTITIES.json','SOURCE_IDENTITIES.json']],
 'referenceImplementationAbsentAtFreeze':True,'wholeContextApplied':False})
print(json.dumps({'frozenFiles':5,'parent':'FOOD-00-C13','manualCases':11,'newEngineCalls':0}))
