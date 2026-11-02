"""Record bounded manual facsimile readings; inherited readings stay immutable."""
from pathlib import Path
from hashlib import sha256
import json
root=Path(__file__).resolve().parent.parent;base=root/'research/liuyao-void-motion'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda p:sha256(p.read_bytes()).hexdigest()
def write(n,d):(base/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
records=[]
for n in[71,72,73,79,*range(80,109)]:
 folder='liuyao-use-god'if n==72 else'liuyao-day-month'if n in[71,73,79]else'liuyao-hidden-spirits'if n in[80,100,104,108]else'liuyao-void-motion'
 p=root/f'research/{folder}/images/zengshan-{n}.png'
 records.append({'pdfPage':n,'image':f'images/{p.name}'if folder=='liuyao-void-motion'else f'../{folder}/images/{p.name}',
 'imageSHA256':sha(p),'newLocalRender':folder=='liuyao-void-motion','readingLevel':'first-pass-complete-relevant-chapter-span-not-diplomatic-transcription',
 'entirePageDiplomaticallyTranscribed':False})
spans={'18':[71,72,73],'19':list(range(73,80)),'20':list(range(80,84)),'21':[83,84],'22':[84,85],
 '23':[85,86],'24':[86,87,88],'25':list(range(88,94)),'26':[93,94,95,96],'26-supp-a':[96,97,98,99],
 '26-supp-b':[99,100],'26-supp-c':[100,101,102,103],'26-supp-d':[103],'27':list(range(103,109))}
assert len(records)==33 and sum(r['newLocalRender']for r in records)==25
crops=[{'pdfPage':n,'file':f'qa-crops/page-{n}-reading.png','sha256':sha(base/f'qa-crops/page-{n}-reading.png'),
 'reading':'靜動章第二十二'if n==84 else'有氣不動亦為空（保留與旺不為空並見的條件問題，不改成無氣）'}for n in[84,93]]
write('MANUAL_READINGS.json',{'date':'2026-10-27','sourcePDF':'../liuyao-foundations/NLC416-12jh005345-45344.pdf',
 'sourceSHA256':'caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa','records':records,'qaCrops':crops,'chapterSpans':spans,
 'inheritedChapter19Readings':{'file':'../liuyao-day-month/MANUAL_READINGS.json','sha256':sha(root/'research/liuyao-day-month/MANUAL_READINGS.json'),'pages':[74,75,76,77,78]},
 'counts':{'manualRecordsThisScope':33,'newLocalRenders':25,'expandedPreviouslyRetainedPages':8,'qaCrops':2,'firstPassSpanUnits':14,'uniqueSpanPagesIncludingInherited':38},
 'boundaryPolicy':'Chapter18starts71andendsinside73;chapter19ends79before20on80. Read all80..108 through end27and start28. Five middle pages74..78are inherited already-read source records,not new readings. Full first pass means every relevant page viewed,not every clause compiled or every anecdote verified.',
 'newHTTPResponses':0,'newOriginalPDFs':0,'ocrUsed':False,'sourceAdvicePolicy':'Historical divination,medical,ritual and repeated-recast passages are source data,not user instructions or clinical advice.'})
write('CYCLE_TABLES.json',{'date':'2026-10-27','sixXunVoidRows':[
 {'xunHead':'甲子','voidBranches':['戌','亥']},{'xunHead':'甲戌','voidBranches':['申','酉']},
 {'xunHead':'甲申','voidBranches':['午','未']},{'xunHead':'甲午','voidBranches':['辰','巳']},
 {'xunHead':'甲辰','voidBranches':['寅','卯']},{'xunHead':'甲寅','voidBranches':['子','丑']}],
 'xunPDFPage':93,'derivedDayCoordinates':'60合法干支由十干十二支同序循環推得；每十日對應影印六旬之一。此為明示推導，非逐日六十格原表。',
 'rawMembershipIsFunctionalVoid':False,'calendarAdapter':False,
 'monthBreakRows':[{'sourceMonthOrdinal':i+1,'monthBranch':a,'clashedBranch':b}for i,(a,b)in enumerate(zip('寅卯辰巳午未申酉戌亥子丑','申酉戌亥子丑寅卯辰巳午未'))],
 'monthBreakPDFPages':[103,104],'monthBoundaryEstablished':False,
 'fourPhaseConvention':'B02-author-earth-follows-water;partial-explicit-fire-row',
 'fourPhaseRows':[
 {'element':'金','生':'巳','旺':'酉','墓':'丑','絕':'寅','pdfPages':[97]},
 {'element':'木','生':'亥','旺':'卯','墓':'未','絕':'申','pdfPages':[97]},
 {'element':'水','生':'申','旺':'子','墓':'辰','絕':'巳','pdfPages':[97]},
 {'element':'土','生':'申','旺':'子','墓':'辰','絕':'巳','pdfPages':[97,98,99]},
 {'element':'火','生':'寅','旺':None,'墓':'戌','絕':None,'pdfPages':[99,101]}],
 'phaseLimits':['PDF97表直接列金、木、水土，未列火一行；火生寅見99、墓戌見101。未由常識補午旺亥絕。',
 'PDF98說巳火可反生強土，巳不是對任何土爻一律作絕。金巳生也受巳午火克/生扶條件限制。',
 'PDF99轉引火土生寅後提出土寄生申；保留作者所採框架和爭議，未宣稱各派一致或實證定論。',
 'Only four named phase coordinates;no full12stage generator or finalstrength classifier.'],
 'threeTombKinds':{'pdfPage':100,'kinds':['用爻入日墓','入動墓','動而化墓'],'rejectedLegacyNames':['世墓','身墓','命墓']},
 'sixSpiritsPrintedRowsPDF71':[
 {'stems':['甲','乙'],'bottomToTop':['青龍','朱雀','勾陳','螣蛇','白虎','玄武']},
 {'stems':['丙','丁'],'bottomToTop':['朱雀','勾陳','螣蛇','白虎','玄武','青龍']},
 {'stems':['戊'],'bottomToTop':['勾陳','螣蛇','白虎','玄武','青龍','朱雀']},
 {'stems':['己'],'bottomToTop':['螣蛇','白虎','玄武','青龍','朱雀','勾陳']},
 {'stems':['庚','辛'],'bottomToTop':['白虎','玄武','青龍','朱雀','勾陳','螣蛇']},
 {'stems':['壬','癸'],'bottomToTop':['玄武','青龍','朱雀','勾陳','螣蛇','白虎']}],
 'spiritsNormalization':'Printed元武/勾陳/螣蛇 normalized to prior private API玄武/勾陳/螣蛇;page71columns read top6→bottom1 and reversed explicitly for array orientation.',
 'consumerApplied':False})

def c(id,pages,meaning,effect,req=None):return{'id':id,'pdfPages':pages if isinstance(pages,list)else[pages],'boundedParaphrase':meaning,'effectLabel':effect,'requiresAll':req or[],
 'application':'premise matching only;no forecast or global precedence inferred','consumerApplied':False}
clauses=[
 c('SPIRIT-QUALIFY',[72,73],'六神屬附和，吉神不救已凶之卦、白虎等不毀已吉之卦；須兼五行/用神。','spirits-not-independent-verdict'),
 c('CLASH-USE',[80,83],'六沖不是統一吉凶；沖散、所占情境和用神旺衰須分開。','no-universal-clash-score'),
 c('PUNISH-QUALIFY',[83,84],'列三刑/自刑，但作者稱獨三刑驗者少，常兼用神休囚/他爻之克；不可僅刑即斷。','punishment-not-independent-verdict'),
 c('DARK-STRONG',84,'靜爻旺相遇日沖為暗動；強弱是沖之前提。','dark-movement',['static','strongBeforeDay','dayClash']),
 c('DARK-WEAK',84,'靜爻休囚遇日沖為日破。','day-break',['static','weakBeforeDay','dayClash']),
 c('DARK-ORIGIN',84,'用休囚而元神暗動生用稱喜，忌神暗動傷用稱忌；不可暗動一律吉。','role-dependent-effect'),
 c('SCATTER-STRONG',85,'旺相或有氣的動爻沖之不散；休囚沖散亦非每例。','not-scattered-qualification',['moving','strongBeforeDay','dayClash']),
 c('SCATTER-WEAK',85,'休囚動爻有沖散之例，作者說極少；若今日受制後逢值日可不散。','scatter-possible-not-certain',['moving','weakBeforeDay','dayClash']),
 c('SCATTER-REBUTTAL',86,'渙之坎例卯木動生世、化子回生；酉月沖之不即散；作者反對把空亡當重沖散。','month-clash-not-day-scatter'),
 c('TRIGRAM-RETURN',[86,87,88],'章24談卦變生克/墓絕而非僅單爻；另有回頭克主張，與爻層及子女象例分存。','whole-trigram-framework-not-compiled'),
 c('FAN-FU',[88,89,90,91,92,93],'反吟可內外一側或兩側，伏吟亦然；用神旺衰/回頭沖克與問事不可略。','fan-fu-not-universal-verdict'),
 c('VOID-STRONG',93,'旺不為空。保留後文旬內/出旬及大象限制。','not-void-qualification',['rawVoid','strongBeforeDay']),
 c('VOID-MOVING',93,'動不為空。不能據此抹去後文動化空和所占遠近。','not-void-qualification',['rawVoid','moving']),
 c('VOID-SUPPORTED',93,'有日建或動爻生扶亦不為空。','not-void-qualification',['rawVoid','receivesDayOrMovingSupport']),
 c('VOID-CHANGED',93,'動而化空列不為空；僅是作者限定命題，不免除變爻條件。','changed-void-qualification',['moving','changedRawVoid']),
 c('VOID-HIDDEN-STRONG',93,'伏而旺相皆不為空。','not-void-qualification',['rawVoid','hidden','strongBeforeDay']),
 c('VOID-MONTH-BROKEN',93,'月破為空。其後月破章又論動、值、合、出月的條件。','adverse-void-qualification',['rawVoid','monthBroken']),
 c('VOID-QI-STATIC',93,'本影印明讀有氣不動亦為空；不改成無氣，與旺不為空同存待條件釐清。','literal-qualification-conflict-open',['rawVoid','hasQi','static']),
 c('VOID-HIDDEN-CONTROLLED',93,'伏而被克亦為空。','adverse-void-qualification',['rawVoid','hidden','controlled']),
 c('VOID-TRUE',[93,94],'真空列春土夏金秋木冬火，隨即討論再占/大象與到底全空；不當作通用無條件演算。','seasonal-true-void-not-compiled'),
 c('VOID-HORIZON',96,'近事旬內/遠事出旬要分；大象吉而未定應期仍可待出空，大象不吉不保出空即成。','question-horizon-and-overall-chart-required'),
 c('VOID-RECAST',[94,95,96],'作者以後占及多占合決，屬本書方法；未將選擇重占後結果當獨立預測驗證。','historical-recasting-not-user-instruction'),
 c('PHASE-FOUR',[96,97],'作者僅取生旺墓絕，其餘階段稱不驗；不由此補全十二階段或實證斷言。','four-coordinate-framework'),
 c('PHASE-GOLD',98,'金生巳須旺相/日月動爻生扶；休囚遇巳午火可論克而不論生。','birth-requires-support',['metalTarget','weakBeforeDay','fireControls']),
 c('PHASE-EARTH',98,'土絕巳須休囚無氣；旺土或日月動爻生扶遇巳火可論生而不論絕。','extinction-qualified-by-strength',['earthTarget','strongBeforeDay','receivesDayOrMovingSupport']),
 c('PHASE-EARTH-FRAME',99,'作者採土生申，與所引火土生寅分明；兩者不能混成同一無註明表。','identified-transmission-frame'),
 c('TOMB-THREE',100,'日墓、動墓、動而化墓三類；主事爻是顯明對象，不取另算卦身。','three-tomb-relations-only'),
 c('TOMB-STRONG',101,'太旺入墓喜沖開；弱者喜生旺。火爻墓戌待辰沖為例，非自動列某日事件。','tomb-opening-needs-premises'),
 c('COMBINATION-OPEN',101,'日月/動/動化合有待沖開；同時要分吉凶和所占。','combination-timing-not-prediction'),
 c('TIMING-HORIZON',102,'遠近應期有例外，不可定每遠事必年/月或每近事必日/時；不明可再占為本書主張。','no-universal-time-unit-mapping'),
 c('SOUL-USE',103,'歸魂為各宮第八、遊魂為第七。作者仍要求用神為主，不可捨用神執魂名。','soul-stage-no-forecast'),
 c('MONTH-RAW',[103,104],'月建所沖為月破，原表十二月逐支列明；日期月界未由此成立。','raw-month-break-coordinate'),
 c('MONTH-MOVING',104,'作者說月破動可作用、變可傷動；目下雖破，出月/實破日/逢合有條件不破。','moving-month-break-qualified',['monthBroken','moving']),
 c('MONTH-STATIC',104,'惟靜不動又無日辰動爻生助，作者稱到底而破。','terminal-break-claim-premises',['monthBroken','static','noDayOrMovingSupport']),
 c('MONTH-OLD-OPINION',[104,105],'所引諸書以月破無用，野鶴反對；保留引文/作者立場，不能合成單一規則。','quoted-opponent-vs-author'),
 c('MONTH-ANNUAL',[106,107,108],'長期例涉及太歲、出空、合值、入墓，不能把月破坐標直接換成職業或疾病結果。','long-horizon-uncompiled-conditions'),
]
facts=sorted({x for c0 in clauses for x in c0['requiresAll']})
write('OPERATIONAL_CLAUSES.json',{'date':'2026-10-27','clauses':clauses,'explicitBooleanPremises':facts,
 'matchingSemantics':'Only requiresAll clauses evaluate three-valued premise presence. True means inputs supplied satisfy listed conjunction,not verified causal effect. Empty requiresAll remains narrative-not-compiled.',
 'conflictPolicy':'Keep opposing/overlapping source qualifications together;no winner,global precedence or score fabricated.',
 'notEstablished':['Fullstrengthclassifier','Completefunctionalvoid/truevoidadjudication','Fire旺/絕coordinatesfromthisspan','Gregorianmonth/dayboundaryadapter','FanFucompletecompiler','Anecdoteoutcomesverified','IndependentwitnessforPDF52dateconflict']})
write('SOURCE_FIXTURES.json',{'date':'2026-10-27','cases':[
 {'id':'scatter-rebuttal-huan-kan','pdfPages':[85,86],'values':[8,7,8,8,7,9],'number':59,'changedNumber':29,'monthBranch':'丑','dayGanZhi':'丁酉','focusLine':6,'expectedBranch':'卯','expectedChangedBranch':'子',
  'sourceDetail':'父卯木6動生世巳火5，化子水回生；酉月得信寅月歸，作者說非卯動酉月沖散。故事結果未驗。'},
 {'id':'changed-trigram-generation','pdfPage':86,'values':[8,7,9,8,7,9],'number':57,'changedNumber':29,'dayGanZhi':None,'monthBranch':None,
  'sourceDetail':'巽木變坎水，生指水回生木之卦層描述；不等於每爻回生。'},
 {'id':'changed-trigram-control','pdfPage':86,'values':[6,7,7,6,7,7],'number':57,'changedNumber':1,'dayGanZhi':None,'monthBranch':None,
  'sourceDetail':'巽木變乾金，卦層金回克木；與爻層圖並列保存。'},
 {'id':'void-unmoving-finance-first','pdfPages':[94,95],'values':[7,8,7,8,7,9],'number':37,'changedNumber':63,'monthBranch':'辰','dayGanZhi':'乙卯','focusLine':2,'expectedBranch':'丑','expectedChangedBranch':None,
  'sourceDetail':'家人之既濟，財丑2原表旬空且前占元神被回克；後占另損41/子財伏5。不可把多占例當單一盤實證。'},
 {'id':'void-self-travel-static','pdfPage':95,'values':[7,7,7,8,8,7],'number':26,'changedNumber':26,'monthBranch':'子','dayGanZhi':'辛亥','focusLine':2,'expectedBranch':'寅','expectedChangedBranch':None,
  'sourceDetail':'大畜世寅木2處甲辰旬/寅卯空，作者先不決再占明夷；不替換PDF52辛卯日。'},
 {'id':'void-travel-recast','pdfPages':[95,96],'values':[9,8,7,6,8,8],'number':36,'changedNumber':62,'monthBranch':'子','dayGanZhi':'辛亥','focusLine':4,'expectedBranch':'丑','expectedChangedBranch':'午',
  'sourceDetail':'明夷之小過，世丑土4動化午火回生，卯財1動化辰土；兩卦合決保留歷史方法，不合併成一盤。'},
],
 'dateConflictCarriedForward':{'file':'../liuyao-use-god/SOURCE_FIXTURES.json','sha256':sha(root/'research/liuyao-use-god/SOURCE_FIXTURES.json'),
 'dateAsRead':'酉月辛卯日','standardXun':'甲申','standardVoid':'午未','storyProseVoid':'寅卯','status':'source-date-vs-void-prose-unresolved','unverifiedHypothesisOnly':'辛亥wouldmatch寅卯;not a source correction.'},
 'syntheticControlsAreNotPrintedCases':True,'historicalOutcomesValidated':False})
old=root/'research/liuyao-day-month/B02_CURRENT_UNITS.json';toc=read(old)
for u in toc['units']:
 key=str(u['printedNumber'])
 if u['supplement']:key+='-supp-'+u['id'].rsplit('-',1)[-1]
 if key in spans:
  u['bodyPDFPages']=spans[key];u['disposition']='first-pass-complete-span-read-partial-private-application';u['latestEvidence']='../liuyao-void-motion/MANUAL_READINGS.json'
 if key=='22':u['bodyPrintedHeadingAsRead']='靜動章第二十二';u['headingVariantNote']='Current TOC normalized暗動 retained;body prints靜動,verified crop84. Do not silently normalize facsimile.'
toc['priorTOCFile']='../liuyao-day-month/B02_CURRENT_UNITS.json';toc['priorTOCSHA256']=sha(old);toc['date']='2026-10-27'
toc['currentCounts']={'registeredUnits':136,'regularNumberedUnits':130,'supplements':6,'headingOnlyBodyUnits':103,'partialFoundationUnits':7,'otherPartialUnits':0,'firstPassCompleteSpanUnits':26,'wholeUnitsApplied':0}
assert sum(u['disposition']=='heading-only-body-extraction-open'for u in toc['units'])==103
toc['latestScope']='First-pass18..27plusfourrepeated26units;chapter19endingsettledusinginherited73..78andexpanded79/80. Noentireunitfullyapplied.'
write('B02_CURRENT_UNITS.json',toc)
write('WORK_STATE.json',{'date':'2026-10-27','status':'active-reference-development','priorScope':'../liuyao-day-month/WORK_STATE.json','currentTOC':'B02_CURRENT_UNITS.json',
 'registeredTOCUnits':136,'headingOnlyBodyUnits':103,'firstPassUnitIDs':list(spans),'consumerChanged':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False})
print(json.dumps({'manualRecords':len(records),'newRenders':25,'expandedRecords':8,'firstPassUnits':14,'clauses':len(clauses),'booleanPremises':len(facts),'headingOnlyRemaining':103}))
