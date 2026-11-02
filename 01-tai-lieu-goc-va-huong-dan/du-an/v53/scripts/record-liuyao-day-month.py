from pathlib import Path
from hashlib import sha256
import json
root=Path(__file__).resolve().parent.parent;base=root/'research/liuyao-day-month'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(n,d):(base/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda p:sha256(p.read_bytes()).hexdigest()
records=[]
for n in [13,*range(56,72),*range(73,81)]:
 folder='liuyao-foundations'if n==13 else'liuyao-use-god'if n in[56,60,64,68]else'liuyao-hidden-spirits'if n==80 else'liuyao-day-month'
 p=root/f'research/{folder}/images/zengshan-{n}.png'
 level='expanded-TOC-numbering-correction'if n==13 else'full-span-first-pass-chapters13..17plus-repeated15'if 56<=n<=69 else'volume1endleaf-only'if n==70 else'chapter18adjacent-heading-only'if n==71 else'chapter19bounded-rules-and-examples-ending-not-fully-settled'if 73<=n<=79 else'expanded-six-clash-literal-pairs-only'
 records.append({'pdfPage':n,'image':f'../{folder}/images/{p.name}'if folder!='liuyao-day-month'else f'images/{p.name}',
  'imageSHA256':sha(p),'readingLevel':level,'newLocalRender':folder=='liuyao-day-month','entirePageDiplomaticallyTranscribed':False})
assert len(records)==25 and sum(r['newLocalRender']for r in records)==19
spans={'13':[56,57],'14':[57,58],'15':[58,59],'15-supp-a':[59,60],'16':list(range(60,67)),'17':[66,67,68,69]}
write('MANUAL_READINGS.json',{'date':'2026-10-27','sourcePDF':'../liuyao-foundations/NLC416-12jh005345-45344.pdf',
 'sourceSHA256':'caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa',
 'records':records,'chapterSpans':spans,'counts':{'records':25,'newLocalRenders':19,'expandedPreviouslyRetainedPages':6,'completeChapterSpanContentPages':14,'newContentPageReadings':17,'expandedContentPages':6,'newEndleafPages':1,'adjacentHeadingPages':1,'partialChapter19Pages':7},
 'boundaryPolicy':'Read chapter13beginning insidePDF56and chapter17endingPDF69. PDF70is volume1endleaf;71starts18. Chapter19selected rules/examples73..79read,but final transition not asserted as a fully collated chapter.',
 'newHTTPResponses':0,'newOriginalPDFs':0,'ocrUsed':False})

raw=[
 (1,'寅','木',['寅'],['卯'],'火',None,'休囚',59),
 (2,'卯','木',['卯'],['寅'],'火',None,'休囚',59),
 (3,'辰','土',['辰'],['丑','未'],'金','木','休囚',59),
 (4,'巳','火',['巳'],['午'],'土',None,'休囚',60),
 (5,'午','火',['午'],['巳'],'土',None,'休囚',60),
 (6,'未','土',['未'],['辰','戌'],'金','火','休囚',60),
 (7,'申','金',['申'],['酉'],'水',None,'休囚',60),
 (8,'酉','金',['酉'],['申'],'水',None,'休囚',60),
 (9,'戌','土',['戌'],['丑','未'],'金',None,'休囚',60),
 (10,'亥','水',['亥'],['子'],'木',None,'休囚',60),
 (11,'子','水',['子'],['亥'],'木',None,'衰',60),
 (12,'丑','土',['丑'],['辰','戌'],'金','水','休囚',60),
]
rows=[]
for ordinal,branch,element,primary,secondary,xiang,residual,rest,page in raw:
 cells=[{'element':e,'reading':'旺'if e==element else'相'if e==xiang else'餘氣'if e==residual else rest,
         'exactSeparateDegreeNotClaimed':True}for e in'木火土金水']
 rows.append({'sourceMonthOrdinal':ordinal,'monthBranch':branch,'primaryElement':element,'primaryBranches':primary,
 'secondaryBranchesAsRead':secondary,'xiangElement':xiang,'residualElement':residual,'remainingLabelAsRead':rest,'cells':cells,'pdfPage':page})
write('MONTH_PHASE_ROWS.json',{'date':'2026-10-27','heading':'四時旺相章第又十五','rows':rows,'elementCells':60,'explicitPrimaryBranchSlots':12,'explicitSecondaryBranchSlots':16,'residualNotes':3,
 'phasePolicy':'Source literal qualitative labels;not a numeric strength score. Same-elementsecondarybranchis次,not a different element相. 辰wood/未fire/丑waterretain餘氣;子monthretains衰forother3elements.',
 'inputPolicy':'Explicit printed month branch or source month ordinal only. No Gregorian/lunar/solar-term boundary adapter inferred.',
 'calendarBoundariesEstablished':False,'consumerApplied':False})

write('PAIR_TABLES.json',{'date':'2026-10-27',
 'sixClashes':{'pdfPage':80,'pairs':[['子','午'],['丑','未'],['寅','申'],['卯','酉'],['辰','戌'],['巳','亥']]},
 'sixCombinations':{'pdfPage':73,'pairs':[['子','丑'],['寅','亥'],['卯','戌'],['辰','酉'],['巳','申'],['午','未']]},
 'threeCombinations':{'pdfPage':77,'records':[{'branches':['申','子','辰'],'element':'水'},{'branches':['巳','酉','丑'],'element':'金'},{'branches':['寅','午','戌'],'element':'火'},{'branches':['亥','卯','未'],'element':'木'}],
 'implementation':'Table identity only. Full合局applicationdepends on motion/void/tomb/use-lineconditions;not automatically a transformation or good outcome.'},
 'chapter19SixNamedKinds':{'pdfPages':[73,74,76],'kinds':['日月合爻','爻與爻合','動爻化合','卦逢六合','六沖變六合','六合變六合'],
 'scope':'Classification retained separately;no generic合=auspicious score. Source itself distinguishes useful-god vitality,question context and有凶有吉.'},
 'pairDirection':'Symmetric relation;not evidence of automatic element transformation or causal priority.'})

def c(id,page,meaning,effect,requires=None):return{'id':id,'pdfPage':page,'boundedParaphrase':meaning,'effect':effect,'requires':requires or[],'consumerApplied':False}
clauses=[
 c('S1',57,'A strong static line can generate or control a weak static line;the reverse is not granted by mere relation.','static-effect-conditional',['actorStrong','targetWeak']),
 c('S2',58,'Moving lines can act on static lines;weakness/activity/effectiveness still need premises.','primary-edge-candidate-not-verdict'),
 c('T1',58,'Changed line acts by generation/control/clash/combination on its own original position.','changed-to-own-primary-only'),
 c('T2',58,'Changed line does not act on other primary or changed lines.','block-changed-cross-position'),
 c('T3',58,'Other primary lines do not act on a changed line.','block-primary-to-changed'),
 c('T4',59,'Day/month can act on moving/static/hidden/flying/changed lines;those lines cannot injure day/month.','calendar-to-line-only'),
 c('M1',61,'Month clash marks month break;month combination has a use-related context.','separate-raw-month-relations'),
 c('M2',61,'Month can affect both visible and hidden/changed candidates;month not appearing as a line does not make it absent.','explicit-context-separate-from-figure'),
 c('M3',61,'Month matching a line gives当權even if旬空;the author disputes reading all旬內 as empty.','month-occupancy-void-qualification',['monthOccupancy','void']),
 c('M4',62,'A void desired line may still be旬內empty and become usable on leaving旬;do not erase all temporary void.','temporary-vs-terminal-void-distinction',['void']),
 c('M5',63,'Even month-matching line can be restrained by own changed return-control;other supports may rescue.','month-occupancy-not-invulnerability'),
 c('M6',66,'Month-clashed line supported by day can retain use depending on context;day/month interaction is not a simple score.','keep-day-month-evidence-separate'),
 c('D1',67,'Strong static line clashed by day is暗動.','dark-movement',['dayClash','static','strongBeforeDay']),
 c('D2',67,'Weak static line clashed by day is日破.','day-break',['dayClash','static','weakBeforeDay']),
 c('D3',67,'Strong moving line clashed by day becomes more active.','movement-reinforced',['dayClash','moving','strongBeforeDay']),
 c('D4',67,'Weak moving line clashed by day is散.','movement-scattered',['dayClash','moving','weakBeforeDay']),
 c('D5',67,'Day clash with a void line can起/實;day clash with a combined line canopenit.','raw-relation-not-universal-destruction',['dayClash']),
 c('D6',68,'Day-matching line is not broken by month clash and is not automatically weak by season.','day-occupancy-month-break-qualification',['dayOccupancy','monthClash']),
 c('D7',68,'Day-monthsupportdoesnoteraseallothermoving,return-controlorstrongopposingconditions.','no-single-axis-final-verdict'),
 c('D8',69,'Author says日沖散wasnotuniversallyconfirmed;movingstronglinesnotautomaticallyscattered.','explicit-author-qualification'),
 c('H1',74,'Static line meeting合mayrise;moving line meeting合maybind.','combination-not-always-free-activity'),
 c('H2',76,'六合and六合變六合need用神旺/有氣andquestion-context;not unconditional good outcome.','no-harmony-score'),
 c('H3',78,'三合局needs explicit moving/static/dark/void/tomb/use-line membership conditions.','three-branch-presence-not-full-transformation'),
 c('H4',79,'Source discusses 世應/inner-outer and disputes one universalapplication.','retain-conflicting-application-context'),
]
write('OPERATIONAL_CLAUSES.json',{'date':'2026-10-27','clauses':clauses,'scope':'Layer permissions,qualitative month table and qualified day-clash labels,not a complete strength/calendar/use-god classifier.',
 'notEstablished':['Gregorian/lunar/solar-term month boundary','Automatic旺相/休囚before day intervention','旬空/tomb/extinctioncompletealgorithm','Complete三合conditionsandpriority','Empirical outcome accuracy'],
 'sourceAdvicePolicy':'Historical medical/fortune/determinism/ritual statements are source content,not user instructions or clinical guidance.'})

write('SOURCE_FIXTURES.json',{'date':'2026-10-27','cases':[
 {'id':'kun-static-spring-generation','pdfPage':57,'number':2,'values':[8,8,8,8,8,8],'changedNumber':2,'monthBranch':'寅','dayBranch':'卯',
  'focusLine':3,'targetLine':2,'expectedBranch':'卯','focusStrengthBeforeDay':'旺相','meaning':'Static卯wood3generates巳fireparent2inprintedpure坤example;source supplies springcontext,not Gregorianadapter.'},
 {'id':'dui-weak-moving-controls-strong','pdfPage':58,'number':58,'values':[7,7,8,7,9,8],'changedNumber':54,'monthBranch':'寅','dayBranch':None,
  'focusLine':5,'targetLine':2,'meaning':'酉metalexplicitmovingcancontrolstrong卯woodunderprintedexample;do not apply staticweakness prohibition to all movinglines.'},
 {'id':'kun-return-control-layer','pdfPages':[58,59],'number':2,'values':[8,8,8,6,8,6],'changedNumber':35,'monthBranch':'子','dayBranch':'卯','focusLine':6,
  'expectedChangedElement':'火','expectedOriginalElement':'金','meaning':'Changed巳fire6controlsown酉metal6,notchanged酉metal4.Primary丑earth4can generateprimary酉metal6butnotchanged酉metal4.Month子watercancontrolchanged巳fire6;day卯canclashchanged酉4.'},
 {'id':'day-dark-movement-source','pdfPage':63,'number':52,'values':[6,8,9,8,8,7],'changedNumber':27,'monthBranch':'寅','dayBranch':'申','focusLine':6,
  'meaning':'寅wood官line2matchesmonthandisdayclashed;strong static→暗動. Printedinterpretationalsohasreturn-control/three-combinationpremiseskeptseparate.'},
 {'id':'qian-day-strength-not-destroyed','pdfPage':68,'number':33,'values':[8,6,7,7,7,7],'changedNumber':44,'monthBranch':'申','dayBranch':'午','focusLine':4,
  'meaning':'午fireline4matchesdaydespite申month. Targetcannotbeclassifiedweakfrommonthalone. Exactmovingglyphscheckedseparately.'},
 {'id':'guai-clashed-month-day-occupancy','pdfPage':69,'number':43,'values':[7,7,9,7,7,6],'changedNumber':10,'monthBranch':'巳','dayBranch':'亥','focusLine':4,
  'meaning':'Printed夬43→履10financialstory;亥water4isclashedbymonthbutoccupiesday.Hour/late-Zi/calendarpremisesnotderived,andoutcomeisnotvalidation.'},
],
 'syntheticControlsAreNotPrintedCases':True,'historicalOutcomesValidated':False})

old=root/'research/liuyao-use-god/B02_CURRENT_UNITS.json';toc=read(old)
fixes=[]
for u in toc['units']:
 n=u['printedNumber']
 if not u['supplement']and n==15:u['normalizedHeading']='動變生克沖合'
 if not u['supplement']and n in[16,17]:
  before=u['normalizedHeading'];u['normalizedHeading']='月將'if n==16 else'日辰';fixes.append({'id':u['id'],'oldHeading':before,'correctHeading':u['normalizedHeading']})
 if not u['supplement']and n in[13,14,15,16,17]:
  u['bodyPDFPages']=spans[str(n)];u['disposition']='first-pass-complete-span-read-partial-private-application';u['latestEvidence']='../liuyao-day-month/MANUAL_READINGS.json'
 if not u['supplement']and n==19:
  u['bodyPDFPages']=list(range(73,80));u['disposition']='partial-rule-and-example-reading-final-transition-open';u['latestEvidence']='../liuyao-day-month/PAIR_TABLES.json'
toc['units'].append({'id':'B02-ch015-supp-a','printedNumber':15,'supplement':True,'printedLabelQualification':'第又十五','normalizedHeading':'四時旺相','tocPDFPage':13,'tocVolume':1,
 'bodyPDFPages':[59,60],'disposition':'first-pass-complete-span-read-partial-private-application','entireUnitApplied':False,'latestEvidence':'../liuyao-day-month/MONTH_PHASE_ROWS.json'})
toc['units']=sorted(toc['units'],key=lambda u:(u['printedNumber'],u['id']))
toc['date']='2026-10-27';toc['supplementalRepeatedNumberUnits']=6;toc['priorTOCFile']='../liuyao-use-god/B02_CURRENT_UNITS.json';toc['priorTOCSHA256']=sha(old)
toc['currentCounts']={'registeredUnits':136,'regularNumberedUnits':130,'supplements':6,'headingOnlyBodyUnits':116,'partialFoundationUnits':7,'otherPartialUnits':1,'firstPassCompleteSpanUnits':12,'wholeUnitsApplied':0}
assert len(toc['units'])==136 and sum(u['disposition']=='heading-only-body-extraction-open'for u in toc['units'])==116
toc['numberingCorrection']={'pdfPages':[13,59,60,66],'addedRepeated15':'四時旺相第又十五','correctedHeadings':fixes,
 'reason':'Prior135unitindexomittedrepeated15,misassigned四時旺相to16and月將to17,andthereforemissed日辰17. Correct current layer only;retain historical files/hashes. Thisisindexingcorrection,not newfoundbookcontentorproductbug.'}
write('B02_CURRENT_UNITS.json',toc)
write('WORK_STATE.json',{'date':'2026-10-27','status':'active-reference-development','latestCompletedResearch':'../liuyao-use-god/WORK_STATE.json','currentTarget':'Compile month/day qualified context and changed-line layer permissions;verify exact source fixtures before completion.',
 'firstPassReadNewUnitIDs':['13','14','15','15-supp-a','16','17'],'partialChapter19':True,'registeredTOCUnits':136,'headingOnlyBodyUnits':116,
 'consumerChanged':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False})
print(json.dumps({'records':25,'newRenders':19,'newContentPages':17,'expandedPriorPages':6,'completeSpanPages':14,'newFirstPassUnits':6,'tocUnits':136,'headingOnlyUnits':116,'clauses':24,'monthCells':60,'newHTTP':0}))
