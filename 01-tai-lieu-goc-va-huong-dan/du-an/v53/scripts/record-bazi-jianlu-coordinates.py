from pathlib import Path
from hashlib import sha256
import json,shutil
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/bazi-jianlu-coordinates';s=w/'tmp/bazi-jianlu-hours-staging'
b.mkdir(exist_ok=True);read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
def write(n,d):(b/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
d=read(s/'MANUAL_READINGS.json');d.update(status='bounded-source-coordinates-verified-no-complete-pattern-classifier',
 source='../bazi-pattern-witness/CADAL06066041.djvu',sourceSHA256='013ce4861680a2bf08b811050c45a45bb2d3ce9d164f7e2341d7070bd5cb2c1a',
 digitalComparator='../four-items/sources/KR3g0042_005.txt',digitalSHA256='1ebdd92feaa57496b702f962ad6fafd4f19c17e98c38a94b40f626ef321dd997',
 newSourcePages=0,newHTTPRequests=0,newOriginalContainers=0,expandedPreviouslyReadPages=2)
d['readings']=[{**x,'file':f'../bazi-pattern-extension/images/p{x["image"]}.png'}for x in d['readings']]
d['qaCrop']['sourceFile']='../bazi-pattern-extension/images/p223.png'
d['rejectedHypothesis']=read(s/'PROBE_RESULTS.json')['rejectedResearchHypothesis'];d.pop('suspectedConflict');d.pop('next')
digital=['甲日寅月宜壬申時','乙日卯月宜辛巳時','丙日巳月宜巳亥時','丁日午月宜庚子時','戊日巳月宜甲寅時','巳日午月宜乙丑時','庚日申月宜丙戌時','辛日酉月宜丁酉時','壬日亥月宜戊申時','癸日子月宜巳未時']
for i,row in enumerate(d['rows']):
 row.update(sourceImages=[223,224]if i==9 else[223],digitalTripletAsRetained=digital[i],imageTripletNormalized=row['dayStem']+'日'+row['monthBranch']+'月宜'+row['printedHourPillar']+'時')
 row['digitalGlyphVariant']=row['digitalTripletAsRetained']!=row['imageTripletNormalized']
write('MANUAL_READINGS.json',d);shutil.copy2(s/'p223-hour-column-qa.png',b/'p223-hour-column-qa.png')
write('SOURCE_ROWS.json',{'sourceID':'TamMenh-WYG-volume5-jianlu','rows':d['rows'],
 'sourceTerm':'建禄','interpretation':'Printed day-stem/monthbranch/hourtriplets marked宜,subject to adjacent conditions;coordinate match isnot成格 orgoodfortune.',
 'directDayMonthRows':10,'directHourPillars':10,'allHourCoordinatesExecutable':True,
 'fiveRatsArithmeticBasis':'Existing separately retained late-Zi source discussion57b/58a and engine conventions;not inferred from宜 alone.',
 'modernDateAdapterForSourceChapterEstablished':False,'consumerApplied':False,'sourceInstructionsAreData':True})
write('PROBE_RESULTS.json',read(s/'PROBE_RESULTS.json'))
write('SOURCE_AUDIT.json',{'date':'2026-10-27','sourceSHA256':d['sourceSHA256'],'digitalSHA256':d['digitalSHA256'],
 'newSourcePages':0,'expandedPages':[223,224],'qaCrops':1,'newHTTPBodies':0,'newOriginalContainers':0,'wholeSectionApplied':False,
 'previousTargetedClauseCount38Unchanged':True,'previousTenHeadingMatrixNotRewritten':True,
 'glyphPolicy':'Print己 in己亥/己未 iskept;retaineddigital巳atstemslots is notsilentlychanged. Branch巳 retained atmonth/hourbranchslots.',
 'falseConflictHypothesisRejected':True,'sourceHourEmended':False,'textualIndependenceEstablished':False,
 'dateAndContainerCompletenessStillOpen':'NCL-0000022031915/487versus486and226pagevolumecontainer identity limits inherited;no new resolution.',
 'consumerChanged':False,'wholeCatalogueCompleted':False})
print('Recorded ten source coordinates;allten compatible;no source or product correction.')
