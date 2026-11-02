from pathlib import Path
from hashlib import sha256
import json
root=Path(__file__).resolve().parent.parent;w=root.parent;base=root/'research/liuyao-b03-book1-tables'
stage=w/'tmp/liuyao-b03-book1-prefaces-staging'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(n,d):(base/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda p:sha256(p.read_bytes()).hexdigest()
old=read(stage/'MANUAL_READINGS.json');records=old['records']
for r in records:r['image']='images/'+Path(r['image']).name;r['inheritedPendingReading']=True
topics={20:'Coin method/64names',21:'64names/Najia/shi-ying',22:'Shi-ying/six spirits/body/triads/phases',23:'Phases/luck-horse-blade/nobleman',24:'Nobleman/punishment-harm/palace objects-body/intermediate lines/year-month stems',25:'Day-hour stems/seasonal watches/Tongxuan',26:'Tongxuan/Suijin/holding-shi',27:'Holding-shi/shi-ying conditions',28:'Shi-ying/body/hidden/flying/source position on shensha',29:'All-moving/avoided-origin spirits/use absent',30:'Use absent/moving use/day/six kin moving',31:'Six kin moving/changing/six spirits',32:'Six spirits/month-day talismans/trigram matches',33:'Trigram matches/xunvoid/monthbreak/direct volume1 ending'}
for n in range(20,34):
 image=f'images/bushi-book1-{n:02}.png'
 records.append({'pdfPage':n,'image':image,'sha256':sha(base/image),'topic':topics[n],
 'scope':'expanded-bounded-first-pass-volume1','inheritedPendingReading':False,'expandedEarlierBoundedPage':True,
 'entirePageDiplomaticallyTranscribed':False})
qa=[]
for file,page in [('preface-p2-qa.png',2),('preface-p5-qa.png',5),('preface-p13-qa.png',13),('preface-p14-qa.png',14),('preface-p14-ending-qa.png',14),('preface-p14-count-qa.png',14),('nayin-right-qa.png',17),('nayin-left-qa.png',17),('white-wax-qa.png',17),('lamp-qa.png',17),('year-month-stems-p24-qa.png',24),('day-hour-stems-p25-qa.png',25)]:
 qa.append({'pdfPage':page,'image':'images/'+file,'sha256':sha(base/'images'/file),'dpi':360,'actuallyViewed':True,'newSourcePage':False})
write('MANUAL_READINGS.json',{'date':'2026-10-27','sourceID':'B03-book1','sourcePDF':'../liuyao-foundations/NLC892-GBZX0301013045-259368.pdf',
 'sourceSHA256':old['sourceSHA256'],'sourcePDFBytes':50191031,'sourcePDFPages':60,'newHTTPBodies':0,'newOriginalPDFs':0,
 'records':records,'qaImages':qa,'counts':{'manualRecords':33,'contentPages':32,'coverPages':1,'inheritedPendingPages':19,
 'expandedBodyPages':14,'QAOnlySourceRenders':7,'QACrops':12},'directEnding':{'pdfPage':33,'reading':'卜筮正宗卷之一終'},
 'all60Book1PhysicalImagesPreviouslyViewedByBoundedScopes':True,'allSourceClausesApplied':False,'entireBookApplied':False,
 'sourceInstructionsAreData':True,'ocrUsed':False})
groups=[(1,1,'cover'),(2,2,'title-imprint'),(3,5,'敘'),(6,7,'凡例'),(8,14,'目錄'),(15,16,'卜筮格言'),(16,16,'啓蒙節要'),
 (17,17,'六十花甲納音歌'),(17,17,'十天干所屬'),(17,17,'十二地支所屬'),(18,18,'天干地支及八卦方位圖'),
 (18,18,'五行相生相剋'),(18,18,'六親相生相剋'),(18,18,'天干相合'),(19,19,'地支相合相衝'),(19,19,'五行次序'),
 (19,19,'八卦次序'),(19,19,'八卦象例'),(19,19,'八宮所屬'),(19,20,'以錢代蓍之法'),(20,21,'六十四卦名'),
 (21,21,'納甲裝卦歌'),(21,22,'安世應訣'),(22,22,'六獸歌'),(22,22,'六獸起例'),(22,22,'安月卦身訣'),
 (22,22,'三合會局歌'),(22,23,'長生掌訣'),(23,23,'祿馬羊刃歌'),(23,24,'貴人歌訣'),(24,24,'三刑六害歌'),
 (24,24,'八宮諸物'),(24,24,'八宮諸身'),(24,24,'定間爻歌'),(24,24,'年上起月法'),(25,25,'日上起時法'),
 (25,25,'定寅時法'),(25,26,'通玄賦'),(26,26,'碎金賦'),(26,27,'諸爻持世訣'),(27,28,'世應生剋空亡動靜訣'),
 (28,28,'卦身喜忌訣'),(28,28,'飛伏生剋吉凶歌'),(28,28,'斷易勿泥神煞'),(29,29,'六爻亂動訣'),(29,29,'忌神歌'),
 (29,29,'原神歌'),(29,30,'用神不上卦訣'),(30,30,'用神發動訣'),(30,30,'日辰訣'),(30,31,'六親發動訣'),
 (31,31,'六親變化歌'),(31,32,'六獸歌斷 [editorial short label]'),(32,32,'日月建傳符'),(32,33,'八卦相配'),
 (33,33,'六甲旬空起例'),(33,33,'月破定例')]
write('BOOK1_OPENING_UNITS.json',{'date':'2026-10-27','sourceID':'B03-book1','unitCount':len(groups),
 'groupingIsEditorialNotCanonicalTOCCount':True,'records':[{'id':i,'label':title,'pdfPages':list(range(lo,hi+1)),
 'boundedSourceSpanFirstPassRead':True,'entireUnitApplied':False}for i,(lo,hi,title)in enumerate(groups,1)],
 'allClausesApplied':False,'all384LineAnnotationsCollated':False,'allPrintedExamplesVerified':False})
write('STEM_ANCHORS.json',{'date':'2026-10-27','sourceID':'B03-book1','sourcePDFPages':[24,25],
 'yearMonthPairedAnchors':[{'anchorStems':pair,'branch':'寅','targetStem':s}for pair,s in zip(['甲己','乙庚','丙辛','丁壬','戊癸'],'丙戊庚壬甲')],
 'dayHourPairedAnchors':[{'anchorStems':pair,'branch':'子','targetStem':s}for pair,s in zip(['甲己','乙庚','丙辛','丁壬','戊癸'],'甲丙戊庚壬')],
 'fivePairedAnchorsPerTableAreDirect':True,'forwardCycleExpansionIsEditorialApplicationOfPrintedRule':True,
 'printedFull120CellTablesClaimed':False,'seasonalWatchVerseAt25ConvertedToModernClock':False,
 'calendarYearMonthBoundaryAndLateZiPolicyEstablishedByTheseVerses':False,'consumerApplied':False})
clauses=[('coin-method',[19,20],'背面數0/1/2/3與6/7/8/9的結構取值；既有基礎參照另存，不重做4096對以增數。'),
 ('nayin',[17],'30對/60干支標籤與行；井泉水/泉中水保留詞形差，不當成行算錯。'),
 ('month-stem',[24],'以明示年干與月支自寅推月干；不以農曆月份序號或公曆年直接代入。'),
 ('hour-stem',[25],'以明示日干與時支自子推時干；不自定晚子/換日/時區。'),
 ('seasonal-clock',[25],'定寅時法依季節更點的歷史語境；尚不轉為現代民用鐘點。'),
 ('body-framework',[22,28],'卦身保留B03傳本；不與B02不用卦身立場合成單一共識。'),
 ('use-conditions',[26,27,28,29,30,31],'用原忌與六親動變需保留用神、世應、動靜及空破等條件，不自動吉凶評分。'),
 ('spirit-verse',[22,31,32],'六獸象義與神煞取捨保留來源立場；不是疾病、犯罪或真實事件判定。'),
 ('xun-monthbreak',[33],'旬空/月破坐標承接既有核對，非真空/有效用神或應期裁決。'),
 ('edition-voices',[2,3,4,5,6,7,15],'題名/敘/凡例的署名與年款分層；不把第一人稱師承或驗事當獨立史證。')]
write('OPERATIONAL_CLAUSES.json',{'date':'2026-10-27','sourceID':'B03-book1','clauses':[
 {'id':i,'pdfPages':p,'boundedParaphrase':t,'consumerApplied':False,'historicalOutcomesValidated':False}for i,p,t in clauses],
 'sourceInstructionsAreData':True,'allSourceClausesCompiled':False})
for name in ['NAYIN_ROWS.json','TOC_PRINTED_EXAMPLE_COUNTS.json']:
 d=read(base/name)
 for r in d.get('qaImages',[]):r['image']='images/'+Path(r['image']).name
 write(name,d)
write('SOURCE_AUDIT.json',{'date':'2026-10-27','sourceID':'B03-book1','sourcePDF':'../liuyao-foundations/NLC892-GBZX0301013045-259368.pdf',
 'sourceSHA256':old['sourceSHA256'],'bytes':50191031,'pages':60,'newOriginalPDFs':0,'newHTTPBodies':0,
 'rawBytesRetainedFromEarlierVerifiedAcquisition':True,'sameEditionNotIndependentWitness':True,
 'all60PhysicalImagesViewedByCombinedBoundedScopes':True,'fullDiplomaticTranscription':False,'all384AnnotationsCollated':False,
 'sourceIsNotUserInstruction':True,'wholeBookApplied':False,'wholeCatalogueCompleted':False})
print(json.dumps({'manualRecords':len(records),'editorialUnits':len(groups),'QACrops':len(qa)},ensure_ascii=False))
