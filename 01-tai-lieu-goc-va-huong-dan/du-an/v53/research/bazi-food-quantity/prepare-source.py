"""Freeze the source quantity contrasts; no general strength threshold or outcome score."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from PIL import Image
import json
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(n,d):(B/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def ident(p):return {'file':p.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
assert not(B/'PREIMPLEMENTATION_FREEZE.json').exists()and not(B/'quantity-reference.mjs').exists()
contexts=read(W/'v53/research/bazi-food-source/CONTEXTS.json')['records'];selected=[next(r for r in contexts if r['id']==id)for id in ['FOOD-00-C19','FOOD-00-C21','FOOD-00-C23']]
write('MANUAL_CONTEXTS.json',{'records':selected,'sourceID':'TMTH005-FOOD-C23-Huzhongzi','sourceVoice':'壺中子',
 'selectedQuantityPhrases':['有餘如甲人得兩丙三丙','不足如柱中兩甲止有一丙之類'],
 'sourceAnchorStem':'甲','sourceAnchorRole':None,'notAutomaticallyDayStem':True,
 'C21SeparateVoice':{'name':'指迷賦','literal':'食神一處當用一代於三若遇休閑三重不逮於一',
 'usableAndIdleAreAdditionalSourcePremises':True,'notNumericalMultiplierThree':True,'implementedAsQuantityRule':False},
 'C19OpenLists':{'literal':selected[0]['text'],'listSegmentationFullyAdjudicated':False,'neitherWealthScoreNorMoralRank':True,'implemented':False},
 'literalQuantityMatchIsNotGeneralSurplusShortageDefinition':True,'C23EffectiveFoodSufficiencyCalculated':False,
 'sourceOutcomeValidated':False,'wholeContextApplied':False,'consumerApplied':False})
cases=[('two-bing',['甲子','丙子','丙寅','戊辰'],True,False,True,False),
 ('three-bing',['甲子','丙子','丙寅','丙辰'],False,True,True,False),
 ('two-jia-one-bing',['甲子','甲寅','丙辰','戊午'],False,False,False,True),
 ('not-day-anchor',['甲子','丙寅','乙卯','丙午'],True,False,True,False),
 ('no-jia',['戊子','丙子','丙寅','庚辰'],True,False,False,False),
 ('missing-slot',['甲子','丙子','丙寅',None],None,None,True,False),
 ('joint-impossible',['甲子','戊子','戊寅',None],False,False,False,False),
 ('all-unknown',[None,None,None,None],None,None,None,None)]
write('EXPECTED_CASES.json',{'cases':[{'id':id,'pillars':p,'exactlyTwoBing':b2,'exactlyThreeBing':b3,'sourceSurplusLiteralExample':s,'sourceShortageLiteralExample':d}for id,p,b2,b3,s,d in cases],
 'frameID':'visible-literal-quantity-examples','sourceAnchorRole':'unassigned-in-source',
 'missingPillarsConstrainRangesNotExactCounts':True,'noStrengthOrFortuneThreshold':True})
records=[]
for n,box,name in [(178,[330,300,1160,2860],'C21-native.png'),(179,[550,290,1810,2860],'C23-native.png')]:
 p=W/f'v53/research/bazi-food-source/p{n}.png';Image.open(p).convert('RGB').crop(box).save(B/name)
 records.append({'source':ident(p),'crop':ident(B/name),'boxXYXY':box,'actuallyViewed':False})
write('CROP_CANDIDATES.json',{'records':records,'fullSourceImagesActuallyViewed':[ident(W/f'v53/research/bazi-food-source/p{n}.png')for n in [177,178,179]],'newSourcePositions':0})
pair=next(r for r in read(W/'v53/qa/bazi-food-core/TEN_RELATION_RESULTS.json')['records']if r['declaredCoordinatePair']==['甲子','丙子'])
write('REUSE_IDENTITIES.json',{'files':[ident(W/p)for p in ['v53/research/bazi-food-source/CONTEXTS.json','v53/qa/bazi-food-core/TEN_RELATION_RESULTS.json',
 'v53/research/bazi-food-strength/CURRENT_CONTEXT_COVERAGE.json']], 'actualRetainedPair':pair,'newEngineCalls':0,'newCalendarObjects':0,
 'relationCoordinateDoesNotDefineEffectiveQuantity':True,'currentMatrixCountsRemain':[46,44,0]})
print(json.dumps({'manualCases':8,'sourceContexts':3,'newEngineCalls':0,'cropsAwaitView':2}))
