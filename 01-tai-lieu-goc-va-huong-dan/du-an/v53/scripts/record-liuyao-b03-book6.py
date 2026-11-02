from pathlib import Path
from hashlib import sha256
import json
root=Path(__file__).resolve().parent.parent;base=root/'research/liuyao-b03-book6'
read=lambda n:json.loads((base/n).read_text(encoding='utf-8-sig'))
def write(n,d):(base/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda n:sha256((base/n).read_bytes()).hexdigest()
questions=[(1,13,2,4,'三傳年月與生剋'),(2,13,4,9,'回頭剋'),(3,13,9,11,'原神生用而有凶'),
 (4,13,11,17,'三合成局'),(5,13,17,19,'反吟'),(6,13,19,21,'伏吟'),(7,13,21,28,'旬空'),
 (8,13,28,31,'月破'),(9,13,31,34,'伏神得出不得出'),(10,14,35,37,'進退神'),
 (11,14,37,41,'沖中逢合合處逢沖'),(12,14,41,47,'四生墓絕'),(13,14,47,52,'六沖六合'),
 (14,14,52,53,'三刑六害'),(15,14,53,57,'獨靜獨發'),(16,14,57,59,'盡靜盡發'),
 (17,14,59,62,'用神多現'),(18,14,62,64,'誠占不驗與所問之意')]
records=[]
for n in range(1,66):
 qs=[q[0]for q in questions if q[2]<=n<=q[3]]
 records.append({'pdfPage':n,'image':f'images/bushi-book6-{n:02}.png','sha256':sha(f'images/bushi-book6-{n:02}.png'),
 'scope':'cover-only'if n in[1,65]else'first-pass-available-question-span',
 'questionGroups':qs,'topic':'Cover only'if n in[1,65]else' / '.join(q[4]for q in questions if q[0]in qs),
 'inheritedPendingReading':n<=8,'newLocalRenderThisRun':n>=9,
 'allPrintedCoinFiguresTranscribed':False,'entirePageDiplomaticallyTranscribed':False})
write('MANUAL_READINGS.json',{'date':'2026-10-27','sourceID':'B03-book6','sourcePDF':'NLC892-GBZX0301013045-259424.pdf',
 'sourceSHA256':'1d6c656828533ac52ae1fd4ff06cc3c025db98ae5458dc686eda2a6b1d11f07f','records':records,
 'counts':{'manualRecords':65,'contentPages':63,'coverPages':2,'inheritedPendingContentPages':7,
 'inheritedPendingCoverPages':1,'newContentRendersThisRun':56,'newCoverRendersThisRun':1,'QAOnlyRenders':2},
 'qaImages':[{'pdfPage':n,'image':f'images/printed-p{n}-qa.png','sha256':sha(f'images/printed-p{n}-qa.png'),
 'dpi':360,'purpose':'Read bounded printed moving marks/branches directly, not another source page.'}for n in[2,3]],
 'directOpenings':[{'pdfPage':2,'reading':'卜筮正宗卷之十三'},{'pdfPage':35,'reading':'卜筮正宗卷之十四'}],
 'lastContentImage':64,'directPrintedFinalColophonEstablished':False,'unviewedPages':[],
 'ocrUsed':False,'allClausesApplied':False,'entireBookApplied':False})
write('BOOK6_CURRENT_UNITS.json',{'date':'2026-10-27','sourceID':'B03-book6','heading':'十八問答附占驗',
 'units':[{'question':i,'textualVolume':v,'pdfPages':list(range(lo,hi+1)),'editorialTopic':h,
 'availableSourceSpanFirstPassRead':True,'entireUnitApplied':False,
 'terminalAvailableImageNotProofOfUnabridgedEnding':i==18}for i,v,lo,hi,h in questions],
 'counts':{'questionGroups':18,'textualVolumes':2,'firstPassAvailableQuestionSpans':18,'entireUnitsApplied':0},
 'all65PagesViewedWithRecordedScope':True,'allSourceClausesApplied':False,'wholeBookApplied':False})
ops=[('three-transmissions',[2,3,4],'年/月/日與動變生剋需分層；書例不是無條件規則。'),
('return-control',[4,5,6,7,8,9],'爻變回剋、卦變回剋及原用二神的例外分開；不把一個變支跨位剋所有爻。'),
('original-support',[9,10,11],'生用爻先作原神候選；原神動而變剋、退絕墓破及日月制約仍可失去生用前提，非見生即救。'),
('triad',[11,12,13,14,15,16,17],'三合局受原/用/忌角色、動靜、空破和成局時點限制；完整成員不等於效力。'),
('fanyin',[17,18,19],'反吟有爻/卦變和用神受沖剋程度；保留反覆與例外，不給固定凶分。'),
('fuyin',[19,20,21],'伏吟與用神、內外及對象相連；靜態坐標不自動推結果。'),
('void',[21,22,23,24,25,26,27,28],'旬空分無生受剋/有生待時；出旬、值日、填實、沖起等須各自前提。近病/久病等歷史生死語不作臨床推斷。'),
('monthbreak',[28,29,30,31],'月破有動靜、生扶和出破、填實、合破的條件；不以單一對沖剔除所有用神。'),
('hidden',[31,32,33,34],'伏神得出與不得出各列四端；不把純宮伏位存在當成有效用神已出。'),
('advance-retreat',[35,36,37],'進退分旺相乘勢/待時/空破待補等；本支與自變支的八對只完成坐標層。'),
('event-order',[37,38,39,40,41],'合處逢沖與沖中逢合涉及先後/當下機括；同時存在沖合不自推順序。'),
('phases',[41,42,43,44,45,46,47],'生墓絕可由日辰、飛爻、動變形成；不能混為同一層或同一強度。'),
('figure-relations',[47,48,49,50,51,52],'六沖六合和其變化有對象、用神與日月等例外，醫療/人命敘事保持歷史。'),
('punishment-harm',[52,53],'原文對三刑六害的取捨是該書立場，不算跨書共識或驗證。'),
('single-motion',[53,54,55,56,57],'獨發、獨靜及暗動需分；僅一爻明動不代表所有問事都可捨用神。'),
('all-static-moving',[57,58,59],'盡靜盡發仍分日沖/用神/強弱；整齊動靜不單獨代表吉凶。'),
('multiple-use',[59,60,61,62],'多現依動靜、月破/旬空、有病之間等問題語境取用，未編成自動唯一排序。'),
('intent',[62,63,64],'誠與否之外，所問不同可改主用；書中命令與驗事敘事為資料，並非使用者指令或獨立真實結局證據。')]
write('OPERATIONAL_CLAUSES.json',{'date':'2026-10-27','sourceID':'B03-book6','clauses':[
 {'id':i,'pdfPages':p,'boundedParaphrase':t,'consumerApplied':False,'historicalOutcomesValidated':False}for i,p,t in ops],
 'sourceInstructionsAreData':True,'allBook6ClausesCompiled':False})
write('SUPPORT_CHAIN_CLAUSE.json',{'date':'2026-10-27','sourceID':'B03-book6','question':3,'pdfPages':[9,10,11],
 'editorialQuestionTopic':'原神生用而有凶','boundedReading':'原神或被日月相剋或化退神或化絕變墓月破日沖',
 'boundedPriorPhrase':'或動而變剋','meaning':'A structurally generating original spirit may lack efficacy because of its own change or other premises.',
 'compiledLayer':'Primary generating candidates and actual own-change-to-own-primary control relation only.',
 'notCompiled':['Full strength/functional void/monthbreak','Retreat/extinction/tomb eligibility','Hidden original support',
 'Day/month/year adapter and priorities','Effective rescue or outcome'],'consumerApplied':False})
write('SOURCE_AUDIT.json',{'date':'2026-10-27','sourceID':'B03-book6','sourcePDF':'NLC892-GBZX0301013045-259424.pdf',
 'sourceSHA256':'1d6c656828533ac52ae1fd4ff06cc3c025db98ae5458dc686eda2a6b1d11f07f','rawPDFBytes':55093879,
 'rawPDFPages':65,'APIRevision':754088957,'newOriginalPDFsToRelease':1,'retainedHTTPBodiesNewToRelease':2,
 'newHTTPBodiesThisRun':2,'sameSeriesNotIndependentWitness':True,'catalog1904IsNotNewDirectImprintProof':True,
 'all65PagesViewedWithRecordedScope':True,'directPrintedFinalColophonEstablished':False,'unviewedPages':[],
 'notEstablished':['Every printed cast/annotation collated','All source clauses applied','Full original-support efficacy',
 'Source historical outcomes independently verified','Gregorian dates reconstructed','Unabridged final ending/genealogy'],
 'sourceIsNotUserInstruction':True,'wholeBookApplied':False,'wholeCatalogueCompleted':False})
print('Recorded65pages/18availablequestion-spans/18boundedclauses;nofullapplication or finalcolophon claim.')
