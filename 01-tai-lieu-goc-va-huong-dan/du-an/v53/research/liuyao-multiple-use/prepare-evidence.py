from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from PIL import Image
import json
S=Path(__file__).resolve().parent;W=S.parent.parent
def read(n):return json.loads((S/n).read_text(encoding='utf-8'))
def save(n,d):
 p=S/n;assert not p.exists(),n;p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not (S/'PREIMPLEMENTATION_FREEZE.json').exists()
def ident(p):return {'file':p.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
p=S/'SELECTED_CROPS.json';d=read(p.name)
old=d['records'].pop();old.update(actuallyViewed=True,accepted=False,rejectionReason='Lastcolumnparagraphendingoutsidecrop;retainedasrejectedtrialnotcompletecross-castconclusion.')
raw=W/old['raw']['file'];out=S/'p136-linked-cast-complete.png';box=[535,150,825,1210]
with Image.open(raw)as im:im.crop(box).save(out)
d['trialRecords']=[old]
for x in d['records']:x.update(actuallyViewed=True,accepted=True)
d['records'].append({'page':136,'raw':ident(raw),'crop':ident(out),'boxXYXY':box,'actuallyViewed':False,'accepted':False})
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
rules=[{'id':'strength','field':'sourceStrength','discard':'休囚','prefer':'旺相','literal':'舍其休囚而用旺相','page':134},{'id':'motion','field':'sourceMotion','discard':'靜','prefer':'動','literal':'舍其靜爻而用動爻','page':134},{'id':'month-break','field':'sourceMonthBroken','discard':True,'prefer':False,'literal':'舍其月破而用不破','page':134},{'id':'void','field':'sourceVoid','discard':True,'prefer':False,'literal':'舍其旬空而用不空','page':134},{'id':'injury','field':'sourceInjured','discard':True,'prefer':False,'literal':'舍其被傷而用不傷','page':134}]
save('MANUAL_SOURCE_CLAUSES.json',{'sourceID':'B02-NLC45344-CH032-LIANGXIAN','frameID':'quoted-old-method-two-declared-use-candidates','canonicalUnit':'B02-ch032','printedBodyHeading':'兩現章第三十一','headingMismatchIsNotNewUnit':True,'rules':rules,'sourceLayer':'quoted古法;notunconditionalauthoradoptedranking','counterexamples':[{'id':'void-used','page':134,'literal':'舍其不空而用旬空'},{'id':'broken-used','page':134,'literal':'舍其不破而用月破'},{'id':'three-uses','page':135,'literal':'此乃卦中用神三現而用月破也'},{'id':'linked-repeat-casts','page':136,'literal':'合前二卦故敢竟許巳年'}],'fullRankingEstablished':False,'independentClinicalOutcomeValidated':False,'automaticUseSelection':False,'sourcePredicatesAreDeclaredNotCalculated':True,'scopeLimit':'Onlythefivequoteddichotomouscomparisonsfortwodeclaredcandidates.Nostars,calendar,vitalityorfinalpriority.'})
state=read('WORK_STATE.json');records=state['sourceRecords']
save('SOURCE_IDENTITIES.json',{'sourcePDF':ident(W/'v53/research/liuyao-foundations/NLC416-12jh005345-45344.pdf'),'reviewedRetainedImages':records,'newFirstPassSourcePositions':0,'method':'Visualrereadingofalreadyretainedchapterimages;nonewPDF/HTTP/renderoffullsourcepages.','currentMap':ident(W/'v53/research/liuyao-foundation-span/B02_CURRENT_UNITS.json'),'currentResumeIndex':ident(W/'v53/research/library-current/RESUME_INDEX.json')})
save('EXPECTED_BEFORE_IMPLEMENTATION.json',{'candidateFields':['candidateID','declaredUse','sourceStrength','sourceMotion','sourceMonthBroken','sourceVoid','sourceInjured'],'cases':[{'name':'five-agree-A','A':{'declaredUse':True,'sourceStrength':'旺相','sourceMotion':'動','sourceMonthBroken':False,'sourceVoid':False,'sourceInjured':False},'B':{'declaredUse':True,'sourceStrength':'休囚','sourceMotion':'靜','sourceMonthBroken':True,'sourceVoid':True,'sourceInjured':True},'prefersA':5,'prefersB':0,'conflictingKnownDirections':False},{'name':'strength-A-motion-B','A':{'declaredUse':True,'sourceStrength':'旺相','sourceMotion':'靜','sourceMonthBroken':False,'sourceVoid':False,'sourceInjured':False},'B':{'declaredUse':True,'sourceStrength':'休囚','sourceMotion':'動','sourceMonthBroken':False,'sourceVoid':False,'sourceInjured':False},'prefersA':1,'prefersB':1,'conflictingKnownDirections':True}],'comparisonTruth':{'worse-better':{'preferLeft':False,'preferRight':True},'better-worse':{'preferLeft':True,'preferRight':False},'same-known':{'preferLeft':False,'preferRight':False},'both-unknown':{'preferLeft':None,'preferRight':None}},'doNotResolve':['allfivevotesagree-doesnotestablishselecteduse','quotedmethodvscounterexamples','three-usecandidates','recasthistoricaloutcomes','strength/functionalvoid/monthbreak/injuryfacts'],'newEngineCallsExpected':0,'reason':'Newmoduleacceptsexplicitsourcepremisesandcomparesquotedrules;doesnotcalculatecharts,calendarorcompareareimplementedengine.'})
print('Manualclausesandexpectedcasesprepared;expandedconclusioncroprequiresinspectionbeforefreeze.')
