from pathlib import Path
from hashlib import sha256
import json,re

root=Path(__file__).resolve().parent.parent
base=root/'research/meihua-conditions';base.mkdir(exist_ok=True)
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(name,d):
 (base/name).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda p:sha256(p.read_bytes()).hexdigest()

notes={
55:'卷二title/printed1;心易占卜玄機 and占卜總訣 opening. Repeated hexagram must not force the same literal plum/horse story. Read line text before other conditional evidence.',
56:'占卜總訣 continues;body/use/external signs/self-motion;占卜論理訣 rejects a literal dragon for food and conditions winter thunder. No deterministic event-time output.',
57:'先天後天論:casting uses乾1兌2離3震4巽5坎6艮7坤8rather than nine-palace numbers. Printed乾為戌亥 differs from retained digital坤為戌亥. Calendar-election魁/破敗亡滅跡is explicitly rejected here.',
58:'先天後天論 concludes;卦斷遺論 begins. Same-element/one-use verdicts have stated contextual counterexamples; story testimony is not independent empirical validation.',
59:'卦斷遺論 concludes;八卦心易體用訣;體用總訣 opening. Mutual is intermediate and changed is later; historical authority/secrecy statements are source content only.',
60:'體用總訣:five seasonal strong/oppressed pairs,body/use directional relations and same-element parties. Main use and changed use may give contrasting stages; no weights or probability formula.',
61:'體用總訣:generating-body trigram narratives乾坤震巽坎離. Direction/person/material gains are historical alternatives, not automatic identity or financial forecasts.',
62:'體用總訣 continues艮/兌support,thencontroller narratives乾坤震巽. Multiple alternatives and social stereotypes remain historical; not unique predicted events.',
63:'體用總訣 concludes坎離艮兌controller narratives;天時占第一 begins. Explicit不分體用;whole hexagram/mutual/change/weather/season qualifications.',
64:'天時占第一 continues numerous weather combinations. Includes seasonal/context exceptions; no modern measured weather accuracy is established.',
65:'天時占第一 concludes;人事占第二. 人事requiresbody/use,mutual/change,strength;the five direct relations are not all conditional rules.',
66:'家宅占第三/屋舍占第四/婚姻占第五 opening. Household versus dwelling distinct. Marriagebody-controls-use may be possible but delayed, unlike a blanket immediate favourable verdict.',
67:'婚姻concludes including historical appearance/social stereotypes;生產占第六;飲食占第七 opening. Birthrolesbody=mother/use=birth,mutual generation benefits different parties. Historical pregnancy/sex claims not consumerdeterminations.',
68:'飲食continues;求謀占第八 and求名占第九. Body-controls-use obstructs dining but permits delayed plans/status;subject changes semantics.',
69:'求名concludes;求財占第十/交易占第十一/出行占第十二 begins. Printed交易body-controls-use says交易成遲;digital retained text says有財and use=財 rather than printed交易之應.',
70:'出行concludes;行人占第十三/謁見占第十四;失物占第十五 heading. Travel and absent traveller are distinct:body-controls-use may favour travel but delay return.',
71:'失物:direct relations plus changed-trigram locations;疾病占第十六 opening. Location analogies are not a search service;health claims remain historical.',
72:'疾病continues with role/strength/rescue qualifications,medicinal hot/cold and ghost claims;these are not diagnosis,treatment or lifespan functionality.',
73:'疾病has six乾上坤下line-change examples,then官訟占第十七 starts. Case2printed互巽離matches changed nuclear,not the main nuclear巽艮;retain mixed context rather than overwrite the general mutual rule.',
74:'官訟concludes;墳墓占第十八,then十八chapter summary;三要靈應篇序 opens. Printed體生用葬之主貧退 differs digital主運退. No proof of burial outcomes.',
75:'三要靈應篇序 concludes with named-transmission assertions;三要靈應篇 begins. Ear/eye/heart and intentional attention are premises,not sensors the app possesses.',
76:'三要靈應篇:cosmology/named historical figures and emphasis on observation;favourable/unfavourable forms remain historical symbolic claims.',
77:'三要靈應篇 continues weather,terrain,people and bodily movements as analogies. No modern meteorology or behavioural classifier follows from these passages.',
78:'三要靈應篇 continues person/action/implement signs;future outcome claims depend on selected observations,not typed question text alone.',
79:'三要靈應篇 continues implements,plants,animals and auspicious/inauspicious claims. Keep historical omen narratives separate from validated functions.',
80:'三要靈應篇 continues miscellaneous objects,glyph components and homophones;not a general modern Chinese/Vietnamese automatic pun resolver.',
81:'三要靈應篇 concludes self-state/speech/inner-and-outer conditions;source instruction to transmit secretly is quoted-source content,not an instruction to the developer.',
82:'三要closing;十應奧論 begins with counterexamples:preciousmetal can controlwood and weapons can generatewater. Do not attach intrinsic fixed good/bad valence to every object.',
83:'十應目論 and復明天時之應;復明地理 heading. Text explicitly says十一類under十應. Midday離with坤兌printed favourable leaves a兌fire-controls-metal contradiction;do not silently repair to艮.',
84:'復明地理/復明人事/復明時令之應. Branchseasonclause:寅卯wood,巳午fire,申酉metal,亥子water,辰戌丑未earth;month/day are stated butpriority/boundaries notspecified.',
85:'復明方卦之應 and復明動物 opening. Direction ofperson/source is an explicitobservedpremise;avoid using personalbirthorientation as a substitute.',
86:'復明動物concludes;復明靜物/復明言語之應. Both symbol/element route and literal-observation route occur;crowded unintelligiblespeechis notdecidable.',
87:'復明言語concludes;復明聲音/復明五色/復明寫字之應. Fivecolour→element mappings are symboliccategories;handwriting errors require actual form/ink observations.',
88:'復明寫字concludes;遺論 and體用 begin. Repeated plum/peony hex doesnot guarantee samehuman event;internalbody/use hasmain,mutual,changed and externalresponses.',
89:'體用 continues:controller ofsupporter can lessen support;controller ofcontroller can ease opposition. No algebraic cancellation or fixedweights printed. 體用論 begins.',
90:'體用論concludes;衰旺論 and內外論 opening. Seasonal state is partialstrong/oppressed qualification;body/support/controller have different desired states.',
91:'內外論 concludes;動靜 begins. Metal/weapon/child/coffin examples reverse simpleomen valence underdifferentbodyelement;notvalidmedical orpregnancy predictions.',
92:'動靜 concludes withobserverselection,paceanddelay;向背 begins. Approaching/receding is temporalcontext,notcompassdirection or deterministicdate.',
93:'向背concludes;靜占 and觀物洞玄歌 opening. Explicitquietroom/nothingheardorseen→noexternalhexagram;do notinvent externalobservations.',
94:'觀物洞玄歌 continuation,household/animal/plant/behaviour omens. Not a room-layout/flying-star specification or objectivejudgment of a household.',
95:'觀物洞玄歌 concludes;起卦加數例 explicit surnameoffsets. Earlier arithmeticfixtures reused,notcountedagain asnewvalidation.',
96:'起卦加數例 concludes;屋宅之占訣 begins. 井example includes互兌control ofwood and離control ofmetal;context qualifies a single-body/use reading,notverifiedbuildinglifespan.',
97:'屋宅之占訣 concludes;器物占 begins. 兌destruction symbolism has explicit坎/乾bodyexceptions;not a universal器物prognosis.',
98:'器物占 concludes,卷二終printed44. Duration unitsyear/month/day depend on theobjectcontext,not uniquelydeterminedbyquẻsum.',
99:'Advertisementfor現代論文叢刊and新文選;notpartofMaiHoa doctrine andnotanotherbook acquired/read.',
100:'Advertisementfor梁任公白話文鈔and胡適之白話文鈔;notMaiHoa ruleunits orauthenticated separatecopies.',
101:'Publisherlogo/blanktransitionpage;not a doctrinalpage ordateimprint.',
102:'梅花易數下冊cover,publisher上海文明書局. Physical冊boundary,not卷二content or卷三firstdoctrinalpage.'}
old={x['pdfPage']for x in read(root/'research/meihua/MANUAL_READINGS.json')['pageRecords']}
old|={x['pdfPage']for x in read(root/'research/meihua-reading/MANUAL_READINGS.json')['records']}
oldrender=read(root.parent/'archives/v53-before-meihua-conditions/EXTRACTED_PAGES.json')
records=[]
for n,note in notes.items():
 kind='content'if n<=98 else'advertisement'if n<=100 else'logo'if n==101 else'physical-book-cover'
 records.append({'pdfPage':n,'printedPage':n-54 if n<=98 else None,'kind':kind,
                 'image':f'../meihua/images/p{n:03}.png','imageSHA256':sha(root/f'research/meihua/images/p{n:03}.png'),
                 'expandedEarlierReading':n in old,'readingLevel':'bounded-visual-clauses-and-unit-navigation-not-complete-line-transcription','note':note})
write('MANUAL_READINGS.json',{'schema':'hhc.meihua.conditions-readings.v1','sourcePDF':'../meihua/NLC416-12jh005426-44577.pdf','sourcePDFSHA256':sha(root/'research/meihua/NLC416-12jh005426-44577.pdf'),
      'date':'2026-10-26','records':records,'counts':{'pageRecords':48,'contentPages':44,'newContentPageRecords':38,'expandedPriorContentPageRecords':6,'advertisements':2,'logo':1,'physicalBookCover':1,'newPNGDerivatives':28,'retainedPNGDerivatives':214,'newHTTPResponses':0},
      'boundaryPage54Reinspected':True,'volume2NavigationComplete':True,'wholeBookRead':False,'wholeBookApplied':False})
write('SOURCE_BASELINE.json',{'beforeExtractionIndex':'../../../archives/v53-before-meihua-conditions/EXTRACTED_PAGES.json','previousRenderedRecords':oldrender['pages'],
      'policy':'All186oldderivatives retainedexactly;28newonesarePoppler2000pxderivativesnotoriginalembeddedbytes. Renderingisnotreading. Oldreportsremainhistoricalcheckpoints.'})

# Each of the52digital sections now has a physical-page range, with its own limits.
ranges=[(55,55),(55,56),(56,57),(57,58),(58,59),(59,59),(59,63),
        (63,65),(65,65),(66,66),(66,66),(66,67),(67,67),(67,68),(68,68),(68,69),(69,69),(69,69),(69,70),(70,70),(70,70),(70,71),(71,73),(73,74),(74,74),
        (74,75),(75,82),(82,83),(83,83),(83,83),(83,84),(84,84),(84,85),(85,85),(85,86),(86,86),(86,87),(87,87),(87,87),(87,88),(88,88),(88,89),(89,90),(90,90),(90,91),(91,92),(92,93),(93,93),(93,95),(95,96),(96,97),(97,98)]
digital=read(root/'research/meihua-reading/DIGITAL_UNIT_DISPOSITIONS.json')
sections=[r for r in digital['records']if r['volume']=='二'];assert len(sections)==len(ranges)==52
units=[]
for r,(first,last)in zip(sections,ranges):
 units.append({'id':r['id'],'heading':r['heading'],'evidencePDFPages':list(range(first,last+1)),
               'digitalSourceFile':r['sourceFile'],'digitalSourceSliceSHA256':r['sourceSliceSHA256'],
               'scope':'visualunit-and-bounded-clause-collation','wholeUnitApplied':False,'fullLineTranscriptionCompleted':False})
write('UNIT_MAP.json',{'schema':'hhc.meihua.conditions-unit-map.v1','units':units,'titlePDFPage':55,'endPDFPage':98,'printedLastPage':44,
      'excludedFromDoctrinalVolume2':[99,100,101,102],'physicalLowerBookCoverPDFPage':102,
      'pageNavigationComplete':True,'allConditionalClausesExtracted':False,'wholeBookApplied':False})

# Exactly five direct relations per non-weather domain. The stored phrases are
# traditional source assertions, never empirical outcome probabilities.
rels=['body-controls-use','use-controls-body','body-generates-use','use-generates-body','same']
domain_rows=[
 ('human',2,'人事','主','賓',[65],['吉','不宜','耗失之患','進益之喜','謀為吉利']),
 ('household',3,'家宅','主','家宅',[66],['家宅多吉','家宅多凶','多耗散','多進益','家宅安穩']),
 ('dwelling',4,'屋舍','主','屋舍',[66],['居之吉','居之凶','資財冷退','門戶興隆','自然安穩']),
 ('marriage',5,'婚姻','所占之家','所婚之家',[66,67],['可成但成之遲','不可成成亦有害','婚難成或因婚有失','婚易成或因婚有得','婚姻吉利']),
 ('birth',6,'生產','母','生',[67],['不利於子','不利於母','利於子','利於母','生育順快']),
 ('dining',7,'飲食','主','飲食',[67,68],['飲食有阻','飲食必無','飲食難就','飲食必豐','飲食豐足']),
 ('planning',8,'求謀','主','所謀之應',[68],['謀雖可成但成遲','求謀不成成亦有害','多謀少遂','不謀而成','求謀稱意']),
 ('status',9,'求名','主','名',[68,69],['名可成但成遲','名不可成','名不可就或因名有喪','名易成或因名有得','功名稱意']),
 ('wealth',10,'求財','主','財',[69],['有財','無財','財有損耗之憂','財有進益之喜','財利快意']),
 ('trade',11,'交易','主','交易之應',[69],['交易成遲','不成','難成或有交易之失','即成成必有財','易成']),
 ('travel',12,'出行','主','所行之應',[69,70],['可行所至多得意','出則有禍','出行有破耗之失','有意外之財','出行順快']),
 ('traveller',13,'行人','主','行人',[70],['行人歸遲','行人不歸','行人未歸','行人即歸','歸期不日']),
 ('meeting',14,'謁見','主','所見之人',[70],['可見','不見','難見見之無益','可見見之且有得','歡然相見']),
 ('lost-object',15,'失物','主','失物',[71],['可尋遲得','不可尋','物難見','物易尋','物不失']),
 ('illness',16,'疾病','病人','病症',[71,72,73],['病易安','雖藥無功','遷延難好','即愈','疾病易安']),
 ('litigation',17,'官訟','主','對辭之人與官訟之應',[73,74],['己勝人','人勝己','非為失理或因官有所喪','不止得理或因訟有得','主和之義']),
 ('grave',18,'墳墓','主','墳墓',[74],['葬之吉','葬之凶','葬之主貧退','主興隆有陰益後嗣','乃為吉地'])]
domains=[{'id':'weather','ordinal':1,'heading':'天時','evidencePDFPages':[63,64,65],'bodyUseApplicable':False,'bodyRole':None,'useRole':None,'directRelations':{},
          'missingPremises':['season','prior-weather-context'],'prognosticClaimsValidated':False}]
for idn,n,h,br,ur,pages,phrases in domain_rows:
 domains.append({'id':idn,'ordinal':n,'heading':h,'evidencePDFPages':pages,'bodyUseApplicable':True,'bodyRole':br,'useRole':ur,
                 'directRelations':{k:{'printedBoundedPhrase':v,'basis':'literal-or-close-normalization-of-printed-clause','notFinalVerdict':True}for k,v in zip(rels,phrases)},
                 'missingPremises':['mutual-and-changed-relations','strength-and-season','observations-if-any'],
                 'prognosticClaimsValidated':False,'consumerAutomated':False})
write('DOMAIN_RULES.json',{'schema':'hhc.meihua.conditions-domains.v1','edition':'1925-11文明書局retainedwitness','scope':'18domainrolepremisesand85directrelationclauses;fullsubsidiaryrulesandvariantsremainopen. Historicalsourceassertions,notvalidatedpredictions.',
                         'domains':domains,'relationCells':85,'consumerApplied':False})

write('SEASON_PREMISES.json',{'schema':'hhc.meihua.season-premises.v1','evidencePDFPages':[60,84,85,90],
 'seasons':{'spring':{'strong':'Mộc','oppressed':'Thổ'},'summer':{'strong':'Hỏa','oppressed':'Kim'},'autumn':{'strong':'Kim','oppressed':'Mộc'},'winter':{'strong':'Thủy','oppressed':'Hỏa'},'earth-months':{'strong':'Thổ','oppressed':'Thủy'}},
 'branchStrong':{'子':'Thủy','丑':'Thổ','寅':'Mộc','卯':'Mộc','辰':'Thổ','巳':'Hỏa','午':'Hỏa','未':'Thổ','申':'Kim','酉':'Kim','戌':'Thổ','亥':'Thủy'},
 'calendarBoundaryEstablished':False,'monthDayPriorityEstablished':False,
 'unspecifiedElementsNotAssignedAFullFiveStateTable':True,'gregorianDateAutoConverted':False,
 'desiredStateByRole':{'body':'strong','supporter':'strong','controller':'oppressed'},'consumerApplied':False})
write('VARIANTS_AND_GAPS.json',{'schema':'hhc.meihua.conditions-variants.v1','variants':[
 {'id':'qian-time-branches','pdfPages':[57],'printed':'乾為戌亥','digital':'坤為戌亥','disposition':'retainboth;notanindependentcalendarboundaryverification'},
 {'id':'trade-role-and-control','pdfPages':[69],'printed':'用為交易之應／體剋用交易成遲','digital':'用為財／體克用有財','disposition':'materialsubject-specificdifference;matrixfollowsthisprintedwitness,nosilentcorrectionofrawdigitaltext'},
 {'id':'burial-retreat','pdfPages':[74],'printed':'主貧退','digital':'主運退','disposition':'retainboundedreading;nochangeofcorpus'},
 {'id':'midday-dui','pdfPages':[83],'printed':'離之時坤兌為體則吉','digital':'離之時坤兌為體則吉','disposition':'source-internalconflictwithfirecontrolsmetal;doNOTsilentlysubstitute艮for兌'},
 {'id':'pi-case2-mutual','pdfPages':[73],'printed':'第二爻動…互見巽離','digital':'第二爻動…互見巽離','disposition':'Matcheschangednuclear37(upper巽/lower離);mainnuclear53is巽艮. Sourceusesmixedcontext;notgeneralruleoverride.'}],
 'open':['Allsubsidiaryclauses,visualuncertaintiesandsecond-witnesscollationremainopen;18roledefinitions/85clausesarenotwholevolumeapplication.',
         'NochoiceofGregorian/lunar/solar-seasonboundaryorprioritybetweenmonthanddayislicensedbythesefewclauses.',
         'Body/use relationalgraphisqualitative;weights,thresholdsandautomaticcancellationnotestablished.',
         'Weather,medical,pregnancy,burial,legalandfinancialoutcomeclaimsarenotvalidatedforecasts;medicalprescriptionsandghost/lifespanclaimsremainhistorical.',
         'Quietroomwithnothingheardorseenexplicitlyhasnoexternalhexagram;do notinventanomen.']})
print(json.dumps({'records':48,'newContentPages':38,'expandedContentPages':6,'units':52,'domains':18,'directRelationCells':85,'retainedRenders':214},ensure_ascii=False))
