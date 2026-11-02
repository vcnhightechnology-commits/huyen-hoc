from pathlib import Path
from hashlib import sha256
import json
root=Path(__file__).resolve().parent.parent;base=root/'research/liuyao-use-god'
def write(n,d):(base/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda p:sha256(p.read_bytes()).hexdigest()
spans={8:[48,49,50],9:[50,51],10:[51,52,53,54],11:[54,55],12:[55,56]}
write('MANUAL_READINGS.json',{'date':'2026-10-27','sourcePDF':'../liuyao-foundations/NLC416-12jh005345-45344.pdf',
 'sourceSHA256':'caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa','chapterSpans':spans,
 'records':[{'pdfPage':n,'image':f'images/zengshan-{n}.png','imageSHA256':sha(base/f'images/zengshan-{n}.png'),
 'readingLevel':'first-pass-complete-chapters8..12withinboundedheading-spans'if 48<=n<=56 else'bounded-later-context-probe-only',
 'fullPageDiplomaticTranscription':False}for n in [*range(48,57),60,64,68,72]],
 'qaCrop':{'file':'../../qa/liuyao-use-god/need-cast-crop.png','sha256':sha(root/'qa/liuyao-use-god/need-cast-crop.png'),'purpose':'Verify four moving glyphs in5→6,includingcircleatline3andstaticline5;proseexplicitlystates五爻戌土則不變. Crop/2x enlargement inspection only.'},
 'dayContextCrop':{'file':'../../qa/liuyao-use-god/day-context-crop.png','sha256':sha(root/'qa/liuyao-use-god/day-context-crop.png'),'reading':'酉月辛卯日','purpose':'Read literal date without silently replacing卯with亥tofitlater旬空prose.'},
 'counts':{'newRenders':13,'chapterSpanPages':9,'laterBoundedProbes':4,'chaptersFirstPassRead':5,'qaCrops':2},
 'chapterBoundaries':'Chapter8begins48,9begins50,10begins51,11begins54,12begins55,13begins56. Boundary pages include neighboring text;do not claim chapter13orlaterchaptersfullyread.',
 'newHTTPResponses':0,'newOriginalPDFs':0,'ocrUsed':False})

subjects=[
 ('parents','父母',48,'Parent as explicitly named family relation.'),
 ('grandparents','父母',48,'Grandparent within the source parent-generation category.'),
 ('teacher','父母',48,'Teacher/elder in the specifically listed traditional category.'),
 ('document','父母',49,'Written article,book,contract or official document.'),
 ('house','父母',49,'House/shelter as the specifically listed object;not a modern building safety assessment.'),
 ('boat','父母',49,'Boat as a listed shelter/transport object;not travel safety advice.'),
 ('clothing','父母',49,'Garment/cloth as a named covering object.'),
 ('siblings','兄弟',49,'Brother/sister or specifically listed same-generation kin.'),
 ('wife','妻財',49,'Wife in the historical gendered system;not a universal spouse/gender mapping.'),
 ('money','妻財',49,'Money,goods,treasure as named property.'),
 ('husband','官鬼',49,'Wife asking about husband in this traditional wording;not a universal spouse mapping.'),
 ('official-position','官鬼',49,'Traditional功名/官府 context;not automatically every modern career question.'),
 ('thief','官鬼',49,'Named theft/adversary source category;not proof a person committed a crime.'),
 ('children','子孫',50,'Child/descendant category as listed.'),
 ('livestock','子孫',50,'The listed domestic animals/poultry category;not animal-health advice.'),
]
write('SUBJECTS_AND_ROLES.json',{'date':'2026-10-27','subjects':[{'id':i,'desiredKin':k,'pdfPage':p,'qualification':q}for i,k,p,q in subjects],
 'policy':'Only exact named subject ID maps to a kin search,not to a selected line or prediction. Multiple lines/absent kin/changed/calendar candidates stay explicit.',
 'qualifications':[
 {'pdfPage':49,'topic':'sister-husband','sourceDefault':'兄弟','commentator':'兄弟wasnotreliable;應usedinstead','decision':'Do not offer a single automatic mapping for this disputed relation.'},
 {'pdfPage':50,'topic':'子孫','meaning':'Called福神but explicitly disliked for功名;rolelabelcannotbeageneralpositivescore.'},
 {'pdfPages':[48,49,50],'topic':'medical-and-historical-social-categories','decision':'Historical medical,servant,status and gendered claims retained as source content;not modern clinical/legal advice or all-person mappings.'}],
 'roleDefinitions':{'用神':'Explicit selected question-relevant line/element;not inferred from a text question.',
 '元神':'Element generating用神','忌神':'Element controlling用神','仇神':'Element controlling元神andgenerating忌神'},
 'definitionEvidence':{'pdfPage':50,'workedElement':'金','sourceAssignments':{'用神':'金','元神':'土','忌神':'火','仇神':'木'}},
 'unassignedRole':'The remainingelement is returned asother-element;no unprinted universal閑神rule inferred here.',
 'consumerApplied':False})

def ALL(*x):return{'all':list(x)}
def ANY(*x):return{'any':list(x)}
def NOT(x):return{'not':x}
def c(id,role,kind,page,paraphrase,e):return{'id':id,'role':role,'kind':kind,'pdfPage':page,'boundedParaphrase':paraphrase,'expression':e,'consumerApplied':False}
clauses=[
 c('M1','元神','effective',52,'Strong,atday/month,or supported by day/month/moving lines.',ANY('strong','atDayMonth','supportedByDayMonthOrMoving')),
 c('M2','元神','effective',52,'Moving into return-generation or advancement.',ALL('active',ANY('changedReturnGeneration','changedAdvance'))),
 c('M3','元神','effective',52,'Long-life or imperial-prosperity phase relative to the day.','dayLongLifeOrImperialProsperity'),
 c('M4','元神','effective',52,'元神and忌神bothactive.',ALL('active','opposingActive')),
 c('M5','元神','effective',52,'Strong and active while void or changing to void.',ALL('strong','active',ANY('void','changedVoid'))),
 c('MN1','元神','ineffective',53,'Weak and inactive,or active/weak/attacked.',ANY(ALL('weak',NOT('active')),ALL('active','weak','attackedByDayMonthOrMoving'))),
 c('MN2','元神','ineffective',53,'Weak and void or month-broken.',ALL('weak',ANY('void','monthBroken'))),
 c('MN3','元神','ineffective',53,'Weak active line changes into retreat.',ALL('weak','active','changedRetreat')),
 c('MN4','元神','ineffective',53,'Weak and extinct.',ALL('weak','extinct')),
 c('MN5','元神','ineffective',53,'Entering one of the three tomb contexts.','inThreeTombs'),
 c('MN6','元神','ineffective',53,'Weak active line changes into extinction,control,break orscatter.',ALL('weak','active',ANY('changedExtinction','changedReturnControl','changedBreak','changedScatter'))),
 c('K1','忌神','effective',53,'Strong,supported,or atday/month.',ANY('strong','supportedByDayMonthOrMoving','atDayMonth')),
 c('K2','忌神','effective',53,'Moving into return-generation or advancement.',ALL('active',ANY('changedReturnGeneration','changedAdvance'))),
 c('K3','忌神','effective',53,'Strong active line is void or changing to void.',ALL('strong','active',ANY('void','changedVoid'))),
 c('K4','忌神','effective',53,'Day-relative long-life/imperial-prosperity phase.','dayLongLifeOrImperialProsperity'),
 c('K5','忌神','effective',53,'忌神and仇神bothactive.',ALL('active','enemyActive')),
 c('KN1','忌神','ineffective',53,'Weak inactive,or moving weak and attacked.',ANY(ALL('weak',NOT('active')),ALL('active','weak','attackedByDayMonthOrMoving'))),
 c('KN2','忌神','ineffective',53,'Inactive and void or month-broken.',ALL(NOT('active'),ANY('void','monthBroken'))),
 c('KN3','忌神','ineffective',53,'Entering one of the three tomb contexts.','inThreeTombs'),
 c('KN4','忌神','ineffective',53,'Weak active line changing into retreat.',ALL('weak','active','changedRetreat')),
 c('KN5','忌神','ineffective',53,'Weak and extinct.',ALL('weak','extinct')),
 c('KN6','忌神','ineffective',53,'Active line changes into extinction,control,break orscatter.',ALL('active',ANY('changedExtinction','changedReturnControl','changedBreak','changedScatter'))),
 c('KN7','忌神','ineffective',53,'忌神and元神bothactive.',ALL('active','originActive')),
]
facts=['strong','atDayMonth','supportedByDayMonthOrMoving','dayLongLifeOrImperialProsperity','void','weak','attackedByDayMonthOrMoving','monthBroken','extinct','inThreeTombs','changedAdvance','changedRetreat','changedBreak','changedScatter','changedExtinction','darkMovement','originActive','opposingActive','enemyActive','useHasQi']
write('CONDITIONS.json',{'date':'2026-10-27','clauses':clauses,'factualInputs':facts,
 'derivedInputs':['active','changedReturnGeneration','changedReturnControl','changedVoid'],
 'changedVoidPolicy':'Notderivedfromunchartedcalendar;providedseparatelyasresearchfactwhereanactualmovinglineexists.',
 'counterexample':{'pdfPages':[50,51],'meaning':'忌神寅wood暗動and元神午firemoving canformwood→fire→earthusechain;notwooddirectlyharmsuseinallcontexts.'},
 'globalQualification':{'pdfPages':[53,54],'meaning':'Effectiveness of元/忌stilldepends on用神有氣/無根;conditions do not imply an outcome when useful-god root/qi is unspecified.'},
 'unknownPolicy':'Missingpremiseisunknown. Concurrenteffective/ineffective matches stay unresolved;no source priority/score invented.',
 'calendarAndStrengthClassifiersImplemented':False,'outcomeAccuracyEstablished':False})
# changedVoidis an asserted premise,not derived;keep its list explicit.
d=json.loads((base/'CONDITIONS.json').read_text(encoding='utf-8'));d['factualInputs'].append('changedVoid');d['derivedInputs'].remove('changedVoid');write('CONDITIONS.json',d)
write('SOURCE_FIXTURES.json',{'date':'2026-10-27','cases':[
 {'id':'need-to-conflict','pdfPage':48,'values':[9,7,9,6,7,6],'number':5,'changedNumber':6,'movingLines':[1,3,4,6],
  'meaning':'Four moving glyphs;line5戌土explicitlystaticinprose. Originalpalace土basisretained;notanewforecastfixture.'},
 {'id':'qian-coactive-chain','pdfPages':[50,51],'values':[7,7,7,9,7,7],'number':1,'changedNumber':9,'useLine':3,
  'expectedUseElement':'土','originLine':4,'opposingLine':2,'originElement':'火','opposingElement':'木',
  'sourceContext':{'monthBranch':'辰','dayBranch':'申','sourceDarkMovementLine':2},'sourceInterpretation':'寅wood→午fire→辰earthchain;calendar/darkmovementisassertedfromtheprintedexample,notautoderivedhere.'},
 {'id':'dui-to-jie','pdfPage':52,'values':[9,7,8,7,9,8],'number':58,'changedNumber':40,'useLine':2,'originLine':4,
  'sourceContext':{'monthBranch':'酉','dayGanzhi':'辛卯'},
  'meaning':'Printed日辛卯conflictswithlater卯財空/changed寅財空proseunderthestandard甲申旬午未空rule. Keepdate/proseconflictopen;do not infer dark movement of亥waterline4fromthisexample.'},
 {'id':'da-guo-origin-no-root','pdfPage':54,'values':[8,7,7,7,9,6],'number':28,'changedNumber':50,'useLine':4,'originLine':5,'opposingLine':6,
  'sourceContext':{'monthBranch':'巳','dayGanzhi':'乙未'},'meaning':'大過→鼎:亥wateruse,酉metaloriginactive,and未earthopposingactive;sourcequalifies用神根/月破/日沖,notjustpresenceoforigin.'}],
 'structuralFixturesNotValidatedHistoricalOutcomes':True,
 'sourceDateConflict':{'pdfPage':52,'dateAsRead':'酉月辛卯日','laterProse':'卯木財爻空而且破;巳火化空afterchangingto寅wood',
 'standardCycleDay':'辛卯belongs to甲申旬with午未void,not寅卯void','status':'source-date-vs-void-prose-unresolved',
 'possibleAlternative':'辛亥wouldbeinthe甲辰旬with寅卯void,buttheprintedimagewasread辛卯. Thisisahypothesis,notsilentcorrection.',
 'consumerChanged':False}})
print(json.dumps({'images':13,'chapterSpanPages':9,'completeFirstPassChapters':[8,9,10,11,12],'subjectCategories':15,'clauses':23,'factualInputs':21,'sourceCases':4,'newHTTP':0}))

toc=json.loads((root/'research/liuyao-hidden-spirits/B02_TOC_UNITS.json').read_text(encoding='utf-8'))
for u in toc['units']:
 if not u['supplement']and u['printedNumber']in spans:
  u['bodyPDFPages']=spans[u['printedNumber']]
  u['disposition']='first-pass-complete-span-read-partial-private-application'
  u['latestEvidence']='../liuyao-use-god/MANUAL_READINGS.json'
toc['date']='2026-10-27';toc['priorTOCFile']='../liuyao-hidden-spirits/B02_TOC_UNITS.json'
toc['priorTOCSHA256']=sha(root/'research/liuyao-hidden-spirits/B02_TOC_UNITS.json')
toc['currentCounts']={'registeredUnits':135,'headingOnlyBodyUnits':122,'partialFoundationUnits':7,'firstPassCompleteSpanUnits':6,'wholeUnitsApplied':0}
assert sum(u['disposition']=='heading-only-body-extraction-open'for u in toc['units'])==122
write('B02_CURRENT_UNITS.json',toc)
write('VARIANTS_AND_LIMITS.json',{'date':'2026-10-27','items':[
 {'id':'void-date','pdfPage':52,'status':'source-date-vs-void-prose-unresolved','literalDate':'酉月辛卯日','standardDayVoid':'午未',
  'incompatibleProse':'財卯空/changed財寅空','hypothesisNotCorrection':'辛亥wouldfit寅卯voidbuttheprinteddateisread辛卯;keepbothsourceclaimsseparate.'},
 {'id':'four-glyphs','pdfPage':48,'status':'reading-resolved','finding':'需5→訟6moves1,3,4,6;line5isstatic,asexplicitlystatedinprose. Failedfixturewithline5movingyielded64andwascorrectedbyimage/prose,notbychangingengine.'},
 {'id':'da-guo-not-xun','pdfPage':54,'status':'reading-resolved','finding':'Thefigureis大過28→鼎50,moving5/6;do not misassign it as巽57. 用亥4/元酉5/忌未6.'},
 {'id':'and-or-connective','pdfPages':[52,53],'status':'editorial-operationalization','finding':'Within numberedlistitems,enumeratedalternativecontextsarecompiledasany;combinedqualifiersasall. Thisisexplicitimplementationinterpretation,notevidencealllaterexceptionscompleted.'},
 {'id':'kin-role-not-valence','pdfPages':[49,50,51],'status':'source-qualified','finding':'姐夫mappingdisputed,子孫called福神butunfavorablefor功名,and忌+元coactivitycangenerateachain. No universalpositive/negativeroleweights.'},
 {'id':'root-and-calendar','pdfPages':[53,54],'status':'open-premises','finding':'用神有氣/無根,暗動,vượngsuy,day/month/void/tomb/extinction requirecompleteidentifiedrules. Inputsremainexplicit;notfilledfrompartialheadingorbranchalone.'}],
 'historicalMedicalOutcomeClaims':'Recordedashistoricalclaims,notvalidatedcausalityormedicalguidance.',
 'sourceInstructionsAreData':True,'b03ParallelChapterCollated':False,'wholeBookApplied':False})
