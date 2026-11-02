from pathlib import Path
from hashlib import sha256
import json
root=Path(__file__).resolve().parent.parent;base=root/'research/liuyao-b03-volume3'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
def write(n,d):(base/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
a=read(base/'ACQUISITION.json');assert sha(base/a['file'])==a['sha256']
records=[{'pdfPage':n,'image':f'images/bushi-book2-{n}.png','sha256':sha(base/f'images/bushi-book2-{n}.png'),
 'scope':'cover-only'if n==1 else'full-first-pass-eighteen-discussions-relevant-span'if n<=13 else'full-first-pass-volume3-polemic-relevant-span'if n<=29 else'volume4-adjacent-heading-and-bounded-incipit-only',
 'newLocalRender':True,'entirePageDiplomaticallyTranscribed':False}for n in range(1,33)]
write('MANUAL_READINGS.json',{'date':'2026-10-27','sourcePDF':a['file'],'sourceSHA256':a['sha256'],'records':records,
 'counts':{'manualRecords':32,'newLocalRenders':32,'newEighteenDiscussionContentPages':12,'volume3PolemicPages':16,'coverPages':1,'boundedNextVolumePages':3,'completeVolume3RelevantSpanPages':28},
 'boundaries':'十八論startsPDF2andendsPDF13;polemicsection14..29endswith卷之三終inside29. 卷之四starts30;30..32readboundedincipitonly. Book2has49pages;33..49notclaimedread.',
 'sourceOpeningEvidence':{'pdfPage':2,'physicalBookOrdinalFromCatalog':2,'textualVolumeAsRead':'卜筮正宗卷之三','sectionAsRead':'十八論',
 'compilerLineBoundedReading':'王維德洪緒纂著','editionDateDirectlyReadInThisBook':False,
 'catalog1904SixPhysicalBooksIsMetadataNotNewImprintProof':True},
 'newOriginalPDFs':1,'newRetainedHTTP200Bodies':2,'ocrUsed':False,'historicalFortuneOrMedicalOutcomesValidated':False})
units=[(1,'用神分類定例',[2,3]),(2,'世應論用神',[3]),(3,'用神問答',[3,4]),(4,'原忌仇神論',[4,5,6]),(5,'飛神正論',[6]),(6,'伏神正傳',[6,7]),
 (7,'六獸評論',[7]),(8,'四生逐位論',[7,8]),(9,'月破論',[8]),(10,'旬空論',[8,9]),(11,'反吟卦定例',[9,10]),(12,'伏吟卦定例',[10]),
 (13,'旺相休囚論',[10,11]),(14,'合中帶克論',[11]),(15,'合處逢沖沖中逢合論',[11,12]),(16,'絕處逢生克處逢生論',[12]),
 (17,'變出進退神論',[12,13]),(18,'卦有驗不驗論',[13])]
write('VOLUME3_UNITS.json',{'date':'2026-10-27','sourceID':'B03-book2','textualVolume':3,'units':[
 {'ordinal':n,'heading':heading,'pdfPages':pages,'disposition':'first-pass-complete-span-read-partial-private-application','entireUnitApplied':False}for n,heading,pages in units],
 'polemicUnits':[{'id':'B03-v3-polemic-'+str(i+1),'normalizedHeading':h,'pdfPages':pages,'disposition':'first-pass-complete-span-read-not-all-clauses-compiled','entireUnitApplied':False}for i,(h,pages)in enumerate([
 ('闢增刪卜易之謬',[14,15]),('闢易林補遺伏神之謬',[15,16,17]),('闢卜筮全書世身之謬',[17,18]),('辯天醫星之謬',[18]),
 ('闢妄論本命之謬',[18,19]),('辯卜筮全書神煞之謬',[19]),('辯貴人祿馬之謬',[19,20]),('辯易林補遺應為他人之謬',[20,21]),
 ('闢易林補遺月破旬空之謬',[21]),('辯互卦',[21,22,23]),('闢易林補遺終身大小限之謬',[23,24,25]),
 ('闢易林補遺家宅之謬',[25,26]),('闢易林補遺婚姻嫁娶之謬',[26,27,28]),('辯六爻諸占之謬',[28,29])])],
 'laterPolemicStartsPDF14':True,'volume3RelevantSpanFirstPassRead':True,'allVolume3ClausesApplied':False,'entirePhysicalBookRead':False,'all14TextualVolumesApplied':False})
write('LAYER_TABLES.json',{'date':'2026-10-27','sourceID':'B03-book2',
 'trigramFanYin':{'pdfPages':[9,10],'pairs':[['乾','巽'],['坎','離'],['艮','坤'],['震','兌']],
 'kind':'source-directional-trigram-opposition','notEquivalentToNaJiaBranchClash':True,
 'boundedSourceDirectionNotes':['乾西北/戌亥與巽東南/辰巳相對','坎北子與離南午相對','艮東北丑寅與坤西南未申相對','震東卯與兌西酉相對'],
 'normalizationNote':'Boundedparaphraseofsourcecompasscoordinates,notmeasuredhousebearings;notanassertionofNaJiaidentity.'},
 'lineFanYin':{'pdfPage':10,'pairs':[['子','午'],['丑','未'],['寅','申'],['卯','酉'],['辰','戌'],['巳','亥']],
 'scope':'Actuallymovinglinechangesbranchtoitsopposite;notall6positionsinchangedfigureannotations.'},
 'fuYin':{'pdfPage':10,'criterion':'A changedinner/outertrigramhasallthreematchingNaJiabranchesatsamepositions;stemidentitynotrequired. Unchangedtrigramnotautomaticallycountedas伏吟.',
 'explicitTrigramPair':['乾','震'],'notEquivalentToSameHexagram':True},
 'advanceRetreat':{'pdfPages':[12,13],'advancePairs':[['亥','子'],['丑','辰'],['寅','卯'],['辰','未'],['巳','午'],['未','戌'],['申','酉'],['戌','丑']],
 'retreatPairs':[['子','亥'],['辰','丑'],['卯','寅'],['未','辰'],['午','巳'],['戌','未'],['酉','申'],['丑','戌']],
 'scope':'Actuallymovinglineonly;structural進/退coordinate,notinherentlygood/badandnotstrengthadjudication.'},
 'calendarAndStrengthAdapter':False,'consumerApplied':False})
clauses=[
 ('visible-not-hidden',[6,7],'伏神正傳以本卦缺所需用神才查本宮首卦；已有用神即使旬空/月破仍看原線條件，不以缺效力偷換缺出現。'),
 ('role-chain',[4,5],'忌神動而原神同動可轉生原神再生用；仇制原/生忌，必區分角色及動靜，不作固定負分。'),
 ('spirits-secondary',[7],'六獸須隨生用/附忌之情，作者反對以吉神凶宿一概推禍福。'),
 ('phase-not-single-axis',[7,8],'四生逐位例把火臨官/帝旺等與生克/合沖/進退並看，不能用十二階段名吞掉其他關係。'),
 ('monthbreak-conditional',[8],'月破動爻仍可生克，出月或值日/合填等分別處理；靜弱再受傷另論，不一律無用。'),
 ('void-conditional',[8,9],'旺動/生扶之空與休囚靜受克/月破等空分開；原文仍有出旬/值日/沖實等時限，未編完整真空判定。'),
 ('fanyin-two-layers',[9,10],'卦之反吟用相對方位之卦，爻之反吟用變爻支相沖；二者不等同。'),
 ('fuyin-branches',[10],'乾變震等子寅辰復化子寅辰/午申戌復化午申戌，支同而干可不同，且卦形可以不同。'),
 ('strength-season',[10,11],'春木旺火相/夏火旺土相/秋金旺水相/冬水旺木相/四季土旺金相；再看日月動爻生克，不自動產生總強弱。'),
 ('combination-control',[11],'子丑合/卯戌合帶克；旺得生扶可合、休囚受克要分，不能六合一律吉。'),
 ('clash-combination',[11,12],'六合變六沖、日月沖/動化沖等與六沖變六合/日月合/動化合分三類，時序/用神未被一個總分代替。'),
 ('extinction-rescue',[12],'絕處/克處逢生有具體生扶與受制條件；土化巳可回生，酉日寅木被克又有水動生，不能僅絕名推結果。'),
 ('advance-not-fortune',[12,13],'進退皆可增減吉凶之勢，不把進固定為吉、退固定為凶。'),
 ('historical-validity-claims',[13],'卦有驗不驗論屬作者誠敬/提問/代占/重占方法主張；不當成現代實證準確率或要求使用者照做。'),
 ('polemic-b02',[14],'闢增刪卜易之謬直接批評李文輝增刪卜易及點竅秘法；這是本書立場，非已經獨立證明前書錯誤。'),
 ('polemic-hidden',[15,16],'另批易林補遺飛伏法，明言同本宮首卦查所缺用神；引文/被批者/作者立場需分層。'),
 ('世身-versus-卦身',[17,18],'批卜筮全書世身之謬涉及子午世身初等另一套身法；不可與前冊安月卦身訣混成同名算法。'),
 ('medical-polemic-data',[18,19],'辯天醫星/本命/神煞的醫卜說屬歷史文本，不能當診療建議或驗證死生準確性。'),
 ('proxy-polemic',[19,20],'親屬/代他人/應爻取用爭論需按對象分層，不把全用應爻或全取指定親屬視為一致共識。'),
 ('proxy-polemic-end',[20,21],'同文續讀：作者區分親屬及常人代占、並舉父子爭訟，仍要求對象/問事，不把作者自身批評算為已驗共識。'),
 ('monthvoid-polemic',[21],'作者批易林月破旬空說過於一刀切，舉動旺、生合、旬空同現等反駁；所引他書原文未另校，只有B03作者的轉述層。'),
 ('mutual-polemic',[21,22,23],'辯互卦描述體象/用象/事象和中間爻互體，又說錢卜宜財官父兄子生克動靜空破，不可把不同術式混成統一應驗保證。'),
 ('lifetime-polemic',[23,24,25],'作者反對按初爻起限/每爻五年一歲等固定大小限推終身，並論應期需辨所問；這是傳統方法內批評，不是有對照組的統計證據。'),
 ('house-polemic',[25,26],'以震巽坎離/季令全圖直接斷家中人口財官的說法被批；作者要求用神生克等。不能把批評或被批話語當現代居家實測規範。'),
 ('marriage-polemic',[26,27,28],'婚姻段分男女自占、長輩代問及問嫁妹等角色，不許一律固定世男應女；未自動以任何通用人物角色替使用者選Dụng。'),
 ('multi-topic-polemic',[28,29],'末段逐題批六爻固定職能概括，天時/生產/行人等各有目標；禁止把後續問事的類比任意疊加成同一吉凶分數。'),
 ('volume4-incipit',[30,31,32],'卷四黃金策總斷千金賦直解開頭談動靜、過不及、生扶拱合及日辰；僅讀有界開頭，未視整卷完成。'),
]
write('OPERATIONAL_CLAUSES.json',{'date':'2026-10-27','clauses':[{'id':id,'pdfPages':pages,'boundedParaphrase':text,'consumerApplied':False}for id,pages,text in clauses],
 'notEstablished':['Fullstrengthclassifier','Functionallyvoid/truevoid/horizons','Everypolemicclausefullycompiled','卦身and世身methodsfullycollated','Sourceanecdoteoutcomes','Fullsourcegenealogy','Volume4afterboundedincipit'],
 'sourceInstructionsAreData':True,'historicalMedicalClaimsNotClinicalAdvice':True})
fanyin=[('pure-qian-xun',1,57),('gou-xiaoxu',44,9),('kan-li',29,30),('jiji-weiji',63,64),('gen-kun',52,2),('qian-bo',15,23),('zhen-dui',51,58),('guimei-sui',54,17)]
fuyin=[('qian-zhen',1,51,'both'),('gou-heng',44,32,'outer'),('daxu-yi',26,27,'inner'),('dun-xiaoguo',33,62,'outer')]
write('SOURCE_FIXTURES.json',{'date':'2026-10-27','trigramFanYinExamples':[{'id':id,'number':a,'changedNumber':b,'pdfPages':[9,10],'expectedDirectionalFanYin':'both'}for id,a,b in fanyin],
 'fuYinExamples':[{'id':id,'number':a,'changedNumber':b,'pdfPage':10,'expectedFuYin':which}for id,a,b,which in fuyin],
 'valuesPolicy':'Movingpositionsreconstructedfromprintednamedbefore/afterfigures;notpretendingbookprintedcoinvaluesordates.',
 'syntheticControlsNotPrintedExamples':True,'historicalOutcomesValidated':False})
write('SOURCE_AUDIT.json',{'date':'2026-10-27','acquisition':a,'container':read(base/'PDF_CONTAINER_CHECKS.json'),
 'apiFile':'b03-book2-commons-api.json','apiSHA256':sha(base/'b03-book2-commons-api.json'),'transportFile':'REQUESTS.json',
 'directReadOpeningPDF2':'卷之三/十八論;compilerline王維德洪緒纂著. Bibliographicconnectiontob03book1supportedbyseriesID/metadataandopening,butnoindependenthistoricalpedigreeproof.',
 'classification':'Downloadedunmodifiedmechanicalscanofprintedbook—notauthorautographorfirsteditionassertion. Metadata1904/6冊notnewdirectimprintreading.',
 'manualReadPages':list(range(1,33)),'unreadPages':list(range(33,50)),'wholeBookApplied':False})
write('WORK_STATE.json',{'date':'2026-10-27','status':'active-eighteen-discussions-layer-reference','sourceID':'B03-book2','latestAcquisition':'ACQUISITION.json',
 'textualVolume':3,'firstPassEighteenUnits':18,'firstPassPolemicUnits':14,'volume3RelevantSpanFirstPassRead':True,'allVolume3ClausesApplied':False,
 'volume4BoundedPages':[30,31,32],'wholeBookApplied':False,'consumerChanged':False})
print(json.dumps({'originalPDFs':1,'retainedHTTP200Bodies':2,'manualPages':32,'eighteenUnitsFirstPass':18,'polemicFirstPassUnits':14,'boundedClauses':len(clauses)}))
