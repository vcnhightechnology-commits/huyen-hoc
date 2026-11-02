from pathlib import Path
from hashlib import sha256
from PIL import Image
import json,re,shutil
S=Path(__file__).resolve().parent;W=S.parent.parent
assert not (S/'PREIMPLEMENTATION_FREEZE.json').exists(),'Existing frozen evidence must not be overwritten.'
def save(name,value):(S/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def identity(p):
 b=p.read_bytes();return {'file':p.relative_to(S if p.is_relative_to(S) else W).as_posix(),'bytes':len(b),'sha256':sha256(b).hexdigest()}
digital=W/'v53/research/bazi-relations/sources/KR3g0042_002.txt';text=digital.read_text(encoding='utf-8-sig');a=text.index('　　論六害');z=text.index('　　論三刑',a);extract=text[a:z]
(S/'DIGITAL_CHAPTER_LOCATOR.txt').write_text(extract,encoding='utf-8')
clean=re.sub(r'[\s¶]','',re.sub(r'<pb:[^>]+>','',extract));(S/'CHAPTER_CLEAN.txt').write_text(clean,encoding='utf-8')
anchors=[('論六害','heading'),('因晝夜','etiological-preface'),('子未相害者','pair-definition'),('丑午相害者','pair-and-open-true-ghost-condition'),('寅巳相害者','pair-and-open-ghost-penalty-condition'),('卯辰相害者','pair-and-open-true-ghost-condition'),('申亥相害者','bidirectional-pair-and-nayin-condition'),('酉戍相害者','directional-exception-and-literal-example'),('又云六六親','historical-kin-outcome'),('子未直上','causal-explanation-six-rows'),('凡人𢃄此','open-additional-star-condition'),('又曰寅巳亥申','historical-vitality-personality'),('值死絶則多謀','historical-vitality-personality'),('入貴格則有操守','historical-status-personality'),('入賤格則多詐','historical-status-personality'),('又云申亥重得','historical-injury-claims'),('卯辰午丑如生旺','historical-vitality-personality'),('死絶主毒害','historical-vitality-outcome'),('入貴格則主大權','historical-status-outcome'),('入賤格謀生','historical-status-outcome'),('子未生旺死絶','historical-kin-outcome'),('入貴格多妻妾','historical-status-family'),('入賤格孤獨','historical-status-family'),('戍酉如生旺','historical-vitality-personality'),('死絶酷狠','historical-vitality-personality'),('入貴格羅忮','historical-status-outcome'),('入賤格殘害','historical-status-personality'),('凡六害入命','historical-generic-outcome'),('兼起命宫','open-palace-premises'),('珞琭子云','attributed-historical-outcome'),('金書訣曰','attributed-historical-injury-outcome'),('可見命犯六害','open-stem-branch-and-pillar-priority'),('便是貴格','historical-independent-effects-no-cancellation')]
starts=[];cursor=0
for anchor,kind in anchors:
 start=clean.index(anchor,cursor);starts.append((start,anchor,kind));cursor=start+len(anchor)
records=[]
for i,(start,anchor,kind) in enumerate(starts):
 end=starts[i+1][0] if i+1<len(starts) else len(clean)
 records.append({'id':f'H{i:02d}','startCodepoint':start,'endCodepoint':end,'literalDigital':clean[start:end],'disposition':kind,'implementedAs':'source-coordinate-or-declared-premise-only' if 2<=i<=7 or i==9 else 'source-record-only','predictiveEfficacyValidated':False})
save('CHAPTER_DISPOSITIONS.json',{'sourceDigital':identity(digital),'chapter':'論六害','editorialSegmentationNotSourceParagraphs':True,'cleanCodepoints':len(clean),'cleanUTF16Units':len(clean.encode('utf-16-le'))//2,'cleanSHA256':sha256(clean.encode()).hexdigest(),'digitalEntityCodesPreserved':True,'records':records,'wholeChapterApplied':False})
native=[]
shutil.copy2(W/'tmp/bazi-triad-stars-staging/p209.png',S/'p209.png')
for page in range(209,215):
 p=S/f'p{page}.png'
 with Image.open(p) as im:native.append({'page':page,**identity(p),'width':im.width,'height':im.height,'pixelRGBA_SHA256':sha256(im.convert('RGBA').tobytes()).hexdigest(),'actuallyViewed':True,'viewing':'Full native image visually inspected in this scope; selected coordinates additionally cropped below.'})
save('NATIVE_REVIEW.json',{'retainedContainer':identity(W/'v53/research/bazi-season-strength/CADAL06066038.djvu'),'decoder':identity(W/'v53/research/bazi-pattern-extension/tooling/djvu.js'),'records':native,'positionsActuallyViewed':list(range(209,215)),'priorPositionReused':209,'newPositionsActuallyViewed':list(range(210,215)),'endBoundaryCorrection':'Initial210–213 selection omitted the ending.214 decoded and inspected before freeze; end is before論三刑 on214.','wholeChapterFirstPassViewed':True,'fullGlyphCollation':False,'newHTTPBodies':0,'newContainers':0,'newIndependentWitnesses':0})
crops=[]
for page,name,box in [(211,'direction-and-true-metal-fire',[800,310,1590,2870]),(214,'stem-branch-pillar-priority',[1230,310,2050,2860])]:
 raw=S/f'p{page}.png';out=S/f'p{page}-{name}.png'
 with Image.open(raw) as im:
  assert 0<=box[0]<box[2]<=im.width and 0<=box[1]<box[3]<=im.height
  im.crop(box).save(out)
 crops.append({'page':page,'raw':identity(raw),'crop':identity(out),'boxXYXY':box,'actuallyViewed':False,'accepted':False})
save('NATIVE_CROPS.json',{'records':crops,'fullPageContext':'NATIVE_REVIEW.json','note':'Mark viewed/accepted only after inspecting generated crops.'})
pairs=[{'id':'zi-wei','branches':['子','未'],'sourceLabel':'勢家相害'}, {'id':'chou-wu','branches':['丑','午'],'sourceLabel':'官鬼相害'}, {'id':'yin-si','branches':['寅','巳'],'sourceLabel':'各恃臨官'}, {'id':'mao-chen','branches':['卯','辰'],'sourceLabel':'以少淩長'}, {'id':'shen-hai','branches':['申','亥'],'sourceLabel':'競嫉才能'}, {'id':'you-xu','branches':['酉','戌'],'sourceLabel':'嫉妬相害'}]
directed=[['子','未','source-harm-wording'],['丑','午','source-harm-wording'],['辰','卯','source-harm-wording'],['申','亥','source-harm-wording'],['亥','申','source-harm-wording'],['酉','戌','source-adverse-wording'],['戌','酉','source-no-disaster-wording']]
causes=[['子','午','未'],['丑','未','午'],['寅','申','巳'],['卯','酉','辰'],['申','寅','亥'],['酉','卯','戌']]
conditions=[{'id':'chou-wu-true-ghost','allowedOrderedPairs':[['丑','午']],'literal':'午更帶丑干之真鬼','premiseRole':'Source predicate must be declared, not calculated from modern stem element or ten-god name.'},{'id':'yin-si-travel-ghost','allowedOrderedPairs':[['寅','巳'],['巳','寅']],'literal':'若干神往来有鬼者尢甚','premiseRole':'No unproved parity, ten-god or strength rule.'},{'id':'chen-mao-true-ghost','allowedOrderedPairs':[['辰','卯']],'literal':'卯更帶辰干真鬼','premiseRole':'True ghost, source pillar role and direction require further source work.'},{'id':'shen-hai-nayin-overcoming','allowedOrderedPairs':[['申','亥'],['亥','申']],'literal':'更納音相尅者重','premiseRole':'Which source pillar pair and direction of overcoming are not automatically chosen.'}]
save('MANUAL_TABLES.json',{'sourceID':'TMTH-WYG-002-LIUHAI','frameID':'declared-source-coordinate-v1','branches':list('子丑寅卯辰巳午未申酉戌亥'),'normalization':[{'digital':'戍','nativeSelectedReading':'戌','inputToken':'戌','scope':'Branch token only; original digital bytes unchanged.'}],'pairs':pairs,'directedClauses':[{'anchor':a,'other':b,'wording':label} for a,b,label in directed],'causalRows':[{'anchor':a,'clash':c,'other':b} for a,c,b in causes],'clashPartners':dict(zip('子丑寅卯辰巳午未申酉戌亥','午未申酉戌亥子丑寅卯辰巳')),'unionPartners':dict(zip('子丑寅卯辰巳午未申酉戌亥','丑子亥戌酉申未午巳辰卯寅')),'conditions':conditions,'literalExample':{'anchorPillar':'乙酉','otherPillar':'戊戌','literal':'若乙酉人得戊戌乙為真金戊為真火為害尢甚','trueElementLabels':['金','火'],'elementSystemNotAdjudicated':True},'allResultsAreSourceTextCoordinates':True,'calendarAdapter':False,'predictiveOutcome':None})
save('EXPECTED_BEFORE_IMPLEMENTATION.json',{'purpose':'Manual expected cases frozen before reference implementation or runtime batch.','nominalPairs':['子未','丑午','寅巳','卯辰','申亥','酉戌'],'directedException':{'酉戌':'source-adverse-wording','戌酉':'source-no-disaster-wording'},'positiveExample':['乙酉','戊戌'],'negativeReversedExample':['戊戌','乙酉'],'causalRows':causes,'declaredPremiseValues':[True,False,None],'actualLibraryExpected':{'clashPartners':dict(zip('子丑寅卯辰巳午未申酉戌亥','午未申酉戌亥子丑寅卯辰巳')),'newPillarLookups':[{'pillar':'乙酉','naYin':'泉中水','stemElement':'木'},{'pillar':'戊戌','naYin':'平地木','stemElement':'土'}]},'invariants':['No automatic year/day anchor','No predicted disaster/personality/health/sex/wealth','No cancellation from mechanical cause','True金/火 are not silently NaYin or ordinary stem elements','Unknown additional predicates stay null']})
print(json.dumps({'editorialUnits':len(records),'codepoints':len(clean),'utf16':len(clean.encode('utf-16-le'))//2,'nativePositions':len(native),'newPositions':5,'cropsAwaitingInspection':2}))
