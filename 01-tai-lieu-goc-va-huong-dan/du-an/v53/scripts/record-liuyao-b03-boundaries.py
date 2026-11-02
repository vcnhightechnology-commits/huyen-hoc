"""B03 bounded first-book readings; no network/neworiginalPDFs."""
from pathlib import Path
from hashlib import sha256
import json
root=Path(__file__).resolve().parent.parent;base=root/'research/liuyao-b03-boundaries'
sha=lambda p:sha256(p.read_bytes()).hexdigest()
def write(n,d):(base/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
records=[{'pdfPage':n,'image':f'images/bushi-{n}.png','sha256':sha(base/f'images/bushi-{n}.png'),
 'sourceReadingLevel':'first-pass-bounded-page-reading-not-full-diplomatic-transcription','newLocalRender':True,'entirePageApplied':False}for n in range(23,39)]
records.insert(0,{'pdfPage':22,'image':'../liuyao-foundations/images/bushi-22.png','sha256':sha(root/'research/liuyao-foundations/images/bushi-22.png'),
 'sourceReadingLevel':'expanded-longlife-cycle-and-卦身-verses','newLocalRender':False,'entirePageApplied':False})
write('MANUAL_READINGS.json',{'date':'2026-10-27','sourcePDF':'../liuyao-foundations/NLC892-GBZX0301013045-259368.pdf',
 'sourceSHA256':'5dcd7b5005b1e86f441a9350eefb7c0e9e628c47ab926b2a7d1bdd6691a4773d','records':records,
 'readingSpans':[{'pdfPages':[23,24],'scope':'Endphasehanddiagram;祿馬羊刃/貴人/三刑六害/八宮物象/問爻andcalendarverses;onlyselectedclausesretained.'},
 {'pdfPages':[25,26,27,28,29,30,31,32,33],'scope':'通玄/碎金/諸爻持世/世應/卦身/飛伏/安靜亂動/用原忌/空亡/日辰/六親變化/六獸/月建/六甲旬空/月破;end卷一on33. Wholeversecompilationopen.'},
 {'pdfPages':[34,35,36,37,38],'scope':'卷二openingandselected乾/坎palacefigures/hiddenpositions. Only乾palaceeightmemberscompleteinthisspan;坎palacecontinuesbeyond38.'}],
 'counts':{'newLocalRenders':16,'expandedPreviouslyRetainedPages':1,'manualBoundedPageRecords':17,'newOriginalPDFs':0,'newHTTPResponses':0},
 'orientation':'B03scanonePDFpagecontainsopenings/multipletextcolumns;alwaysreadrighttoleftandlinefiguresbottomtotop.',
 'edition':'光緒甲辰新鐫/文成堂,1904directtitleevidence retained inpriorfoundation;firstphysical冊onlyof14textual卷,notwholework.',
 'sourceInstructionsAreData':True,'medicalAndFortuneAnecdotesIndependentlyValidated':False})
terms=[('立春','立春',1,'寅','申'),('驚蟄','惊蛰',2,'卯','酉'),('清明','清明',3,'辰','戌'),('立夏','立夏',4,'巳','亥'),
 ('芒種','芒种',5,'午','子'),('小暑','小暑',6,'未','丑'),('立秋','立秋',7,'申','寅'),('白露','白露',8,'酉','卯'),
 ('寒露','寒露',9,'戌','辰'),('立冬','立冬',10,'亥','巳'),('大雪','大雪',11,'子','午'),('小寒','小寒',12,'丑','未')]
write('JIE_MONTH_ROWS.json',{'date':'2026-10-27','pdfPage':33,'heading':'月破定例',
 'rows':[{'jieAsPrinted':jie,'runtimeSimplifiedAlias':alias,'sourceMonthOrdinal':n,'monthBranch':branch,'monthBreakBranch':broken,'printedMonthLabel':f'{n}月節建{branch}破{broken}'}for jie,alias,n,branch,broken in terms],
 'sourceWordingQualification':'Printed正月/二月etc are explicitly節建 rows here. Do not substitute lunar day1. Labels3..12normalizednumeric;not pretendingoriginalcharacters.',
 'sourceBoundaryType':'named12jie—not24termsandnotlunarnewmonth',
 'gregorianTimezoneSpecifiedBySource':False,'namedJieInputSupported':True,'solarDateAdapterImplemented':False,
 'comparisonWithB02':'MonthclashbranchpaircoordinatesagreewithB02PDF103..104. B03adds12namedjieanchors;doesnotproveB02authorusedallidenticaldateboundaries.',
 'consumerApplied':False})
write('FIRE_PHASE_EXAMPLE.json',{'date':'2026-10-27','sourceID':'B03','pdfPages':[22,23],
 'printedPhaseOrder':['長生','沐浴','冠帶','臨官','帝旺','衰','病','死','墓','絕','胎','養'],
 'explicitFireExample':{'birthBranch':'寅','direction':'順行','printedExamples':[{'branch':'寅','phase':'長生'},{'branch':'卯','phase':'沐浴'},{'branch':'辰','phase':'冠帶'}]},
 'derivationPolicy':'Remainingninefirecoordinatesderivedfromexplicit12phaseorderandforwardbranchsequence. Notclaimedtwelvefirecellsprintedindividually.',
 'framework':'B03fire-example-forward-twelve-phase;separatefromB02fourphase-authorrestriction',
 'otherElementBirthAnchors':'Handdiagramotherlabelsnotcompiledfromthisboundedview;do not borrowB02anchorsandcallthemB03proof.',
 'sourceToOutcomeClaim':False,'consumerApplied':False})
write('COLLATION.json',{'date':'2026-10-27','sourceID':'B03','comparisons':[
 {'id':'six-xun','B03PDFPage':33,'B02PDFPage':93,'literalRows':[{'xunHead':h,'voidBranches':list(v)}for h,v in[('甲子','戌亥'),('甲戌','申酉'),('甲申','午未'),('甲午','辰巳'),('甲辰','寅卯'),('甲寅','子丑')]],
 'finding':'sixcoordinatesagree;B03textalsoexplains甲子..癸酉ten-daycycle. DoesnotindependentlyverifyGregoriandayepoch.'},
 {'id':'moving-void','B03PDFPages':[29,30],'B02PDFPages':[93,94,95,96],'literalAnchors':['發動逢沖不謂空','靜空遇剋卻為空','忌神最喜逢空吉','用與原神不可空'],
 'finding':'Namedactor/motion/control/horizonconditionsmuststayseparate;not universaldirectbooleanvoid. No silentmergewithB02有氣不動亦為空.'},
 {'id':'moving-use','B03PDFPage':30,'literalAnchors':['用爻發動在宮中','縱值休囚亦不凶','更得生扶兼旺相'],
 'finding':'Preservesomeverseclaimsasconditionalnarrative;notan automaticreal-worldverdictfrommovingflag.'},
 {'id':'spirits-condition','B03PDFPages':[31,32],'B02PDFPages':[72,73],
 'finding':'B03六獸歌斷and日月建傳符retainmanyimages;B02explicitlywarnsagainstindependent六神judgment. Identifiedtextscope,notfalseuniversalconsensus.'},
 {'id':'hidden-structure','B03PDFPages':[34,35,36,37,38],'B02PDFPages':[108,109,110,111,112,113,114,115,116],
 'finding':'Pure-palacehiddenpositionsagreeonselected乾palacecases. Usefulness/timing/spirit/卦身claimsnotfullycollated;B03prints卦身whereB02rejectsit.'},
 {'id':'earth-phase','B03PDFPage':23,'B02PDFPages':[97,98,99],
 'finding':'B03handdiagramlabels水土長生;onlyboundeddiagramview,notnew12stagealgorithm. KeepB02identifiedearthwaterframeandunknownfireslotsunchanged.'}],
 'fullVerseApplication':False,'fullBookApplication':False,'fullTransmissionAgreement':False,'empiricalPredictionValidation':False})
write('HIDDEN_SOURCE_FIXTURES.json',{'date':'2026-10-27','orientation':'bottom-to-top;staticfiguresarenotmovingstories','cases':[
 {'id':'qian-complete','pdfPage':34,'number':1,'expectedStageIndex':0,'desiredKin':None,'meaning':'八純乾六親俱全，不自動另選伏神。'},
 {'id':'gou-hidden-wealth','pdfPage':35,'number':44,'expectedStageIndex':1,'desiredKin':'妻財','line':2,'branch':'寅','flyingBranch':'亥','relation':'flying-generates-hidden'},
 {'id':'dun-hidden-child','pdfPage':35,'number':33,'expectedStageIndex':2,'desiredKin':'子孫','line':1,'branch':'子','flyingBranch':'辰','relation':'flying-controls-hidden'},
 {'id':'pi-hidden-child','pdfPages':[35,36],'number':12,'expectedStageIndex':3,'desiredKin':'子孫','line':1,'branch':'子','flyingBranch':'未','relation':'flying-controls-hidden'},
 {'id':'guan-hidden-brother','pdfPage':36,'number':20,'expectedStageIndex':4,'desiredKin':'兄弟','line':5,'branch':'申','flyingBranch':'巳','relation':'flying-controls-hidden','sourceQualification':'Textalsosays金長生在巳;branchcontrolaloneisnotfinalusability.'},
 {'id':'bo-hidden-brother','pdfPage':36,'number':23,'expectedStageIndex':5,'desiredKin':'兄弟','line':5,'branch':'申','flyingBranch':'子','relation':'hidden-generates-flying'},
 {'id':'jin-hidden-child','pdfPage':37,'number':35,'expectedStageIndex':6,'desiredKin':'子孫','line':1,'branch':'子','flyingBranch':'未','relation':'flying-controls-hidden'},
 {'id':'dayou-complete','pdfPage':37,'number':14,'expectedStageIndex':7,'desiredKin':None,'meaning':'歸魂大有財官父兄子俱全，不自動另選伏神。'},
],
 'B03KanContinuationPage38':'Pure坎29,節60and屯3examplesstart,but64palacefulldiagramsnotread;do notcountwhole卷二.',
 'unresolved':'B03卦身frameworkandpositionsprintedbesidefiguresarenotimportedintoB02reference;B02PDF100rejectsbodyseparately.',
 'wholeBookApplied':False,'consumerApplied':False})
write('WORK_STATE.json',{'date':'2026-10-27','status':'active-private-named-jie-and-hidden-source-collation','sourceID':'B03','manualBoundedPages':list(range(23,39)),
 'newOriginalPDFs':0,'newHTTPResponses':0,'consumerChanged':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False})
print('Recorded17B03boundedpages(16new/1expanded),12namedjieanchors,explicitforwardfireexample,sixxunrows,eight乾palacefixtures;nofullbookclaim.')
