from pathlib import Path
from hashlib import sha256
import json
root=Path(__file__).resolve().parent.parent; base=root/'research/liuyao-b03-volume5'
sha=lambda p:sha256(p.read_bytes()).hexdigest()
def write(n,d):(base/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
a=json.loads((base/'ACQUISITION.json').read_text(encoding='utf-8'))
assert a['sha256']==sha(base/a['file'])=='01859340e519ffb68a1f40996af73aa7f40beb10a723a7a2a070985201874c61'
topics={2:'卷五 title; 天時 opening',3:'Weather roles and seasons',4:'Three-branch groups, void and sequence',
5:'Weather subject, support, tomb and void',6:'Day-clash timing and imagery',7:'Weather imagery; timing-method paragraph begins',
8:'Timing-method paragraph concludes; 年時 begins',9:'Annual national/population roles and 太歲',
10:'Annual symbolic weather/disaster and spirit claims',11:'Annual historical anomaly narratives',
12:'Annual branch/territory and inside/outside mappings',13:'Annual ending; 國朝 begins',
14:'Dynastic historical narratives and role assignments',15:'Dynastic historical examples continue',
16:'國朝 ending; 征戰 begins',17:'Battle roles and historical cases',18:'Battle historical cases and exceptions',
19:'Battle ending; 身命 begins',20:'Body/fate question, void, support and combinations',
21:'Personal historical fate, relationship and social-role narratives',22:'Life horizons and mutual figure quotation attributed to 易林補遺',
23:'Personal relationship historical narratives and inner/outer distinctions',24:'Family counts and 生旺休囚 qualifications',
25:'Relationships, changed kin and 世/應/身 distinctions; section continues beyond this page'}
records=[{'pdfPage':n,'image':f'images/bushi-book3-{n}.png','sha256':sha(base/f'images/bushi-book3-{n}.png'),
 'topic':topics[n], 'newToRelease':True,'newLocalRenderThisHeartbeat':n>=9,
 'inheritedFromPriorPendingRead':n<=8,'entirePageDiplomaticallyTranscribed':False} for n in range(2,26)]
write('MANUAL_READINGS.json',{'date':'2026-10-27','sourceID':'B03-book3','sourcePDF':a['file'],'sourceSHA256':a['sha256'],
 'records':records,'counts':{'manualRecords':24,'contentImagesNewToRelease':24,'inheritedPendingContentImages':7,
 'newContentRendersThisHeartbeat':17,'QAOnlyRenders':1,'newOriginalPDFsToRelease':1,
 'retainedHTTPBodiesNewToRelease':2,'newHTTPBodiesThisHeartbeat':0},
 'QAOnlyImages':[{'image':'images/timing-p8-qa.png','sha256':sha(base/'images/timing-p8-qa.png'),
 'pdfPage':8,'dpi':300,'cropPixels':[650,270,1240,1260],'purpose':'Read exact timing distinctions; not a new source page.'}],
 'opening':{'pdfPage':2,'literalTitle':'卜筮正宗卷之五','literalSection':'天時'},
 'ocrUsed':False,'physicalBookAllPagesViewed':False,'allVolume5ClausesApplied':False,
 'unviewedPhysicalBookPages':[1]+list(range(26,68))})
write('VOLUME5_UNITS.json',{'date':'2026-10-27','sourceID':'B03-book3','textualVolume':5,
 'units':[{'heading':h,'pdfPages':pages,'firstPassRelevantSpanComplete':complete,
 'entireUnitApplied':False} for h,pages,complete in [
 ('天時',list(range(2,9)),True),('年時',list(range(8,14)),True),('國朝',list(range(13,17)),True),
 ('征戰',list(range(16,20)),True),('身命',list(range(19,26)),False)]],
 'firstPassCompleteRelevantSpanUnits':4,'partialSpanUnits':1,'fullTextualVolumeRead':False,
 'overlappingBoundaryPagesNotAdditionalUniquePages':True})

methods=[
 {'id':'moving-no-other-cause','pdfPage':8,'boundedNormalizedReading':'用神動而無他故者候逢合之日應事',
  'motion':'moving','requiresBoolean':'noOtherCauseConfirmed','target':'combine-subject'},
 {'id':'static-combined','pdfPage':8,'boundedNormalizedReading':'靜而逢合者皆候沖日應事',
  'motion':'static','requiresBoolean':'combinationConfirmed','target':'clash-subject'},
 {'id':'enters-context-tomb','pdfPage':8,'boundedNormalizedReading':'用神入墓于日辰者候沖開墓庫之日應事',
  'motion':None,'requiresBoolean':'tombPremiseConfirmed','target':'clash-tomb'},
 {'id':'self-change-tomb','pdfPage':8,'boundedNormalizedReading':'用神自化入墓者候沖用神之日應事',
  'motion':'moving','requiresBoolean':'tombPremiseConfirmed','target':'clash-subject',
  'requiresOwnChangedBranchEqualsExplicitTomb':True},
]
write('TIMING_CLAUSES.json',{'date':'2026-10-27','sourceID':'B03-book3','pdfPages':[7,8],
 'sourceContext':'weather-timing-paragraph','methods':methods,
 'scope':'Four explicitly bounded target-branch coordinates, not a complete 應期 model.',
 'tombAndOtherCausePremisesAreExplicitCallerAssertionsNotInferredTruth':True,
 'sixClashPairs':[list(x) for x in ['子午','丑未','寅申','卯酉','辰戌','巳亥']],
 'sixCombinationPairs':[list(x) for x in ['子丑','寅亥','卯戌','辰酉','巳申','午未']],
 'notCompiled':['旬內/出旬 void horizons','Month-break fill/combine and out-of-month conditions',
 'Source-relative 生旺/墓絕 classification','Hidden original-spirit appearance',
 'Near/far question and 月/日 horizons','Weather 財/父 subject changes and 轉爻'],
 'allTimingPremisesCompiled':False,'meteorologicalPredictionAccuracyEstablished':False,'consumerApplied':False})

clauses=[
('weather-role',[2,3],'天時中父雨財晴、兄風雲、子日月、官雷電等屬傳統取象，須按問晴雨及動靜時令，不是現代氣象效度證明。'),
('weather-sequence',[4,5],'先後動變、入墓、休囚生扶與三合等另有條件，不能把父現即雨/財現即晴當定論。'),
('weather-timing',[6,7,8],'候合/候沖、動靜旬空、月破、墓與自化入墓、原神伏藏均分開；本次只編四種目標支座標。'),
('rain-turn',[8],'雨宜兼察財爻及財伏不伏、原神與轉爻，不能把晴雨問題的選用直接推廣到所有占問。'),
('annual-scale',[8,9],'年時談國家人物與年尺度，太歲、五六爻等位置取象不等於日常個人流年引擎。'),
('annual-narrative',[10,11,12],'國家災異、地震、刑害、神獸及史例為歷史文本，沒有獨立驗證事件或風險機率。'),
('territory',[12],'地支分野以古國方域為例，不能無校勘投射成現代地理區域。'),
('dynastic',[13,14,15,16],'國朝以太歲/世/應及君臣等取象配史例，屬作者敘事，並非已確認的事前預測資料。'),
('battle',[16,17,18,19],'征戰的軍師/糧草/主客用神及史例不轉成現實戰術或勝敗預測；保留生扶/受制和角色條件作史料。'),
('body-framework',[19,20],'身命論世爻、身、卦宮及時令，並非八字或紫微同名概念的替代算法。'),
('life-support',[20,21],'身世空墓、旺衰、生扶等關係有上下文；來源的富貴貧夭說不直接輸出給使用者。'),
('life-horizon-quotation',[22],'身命段引易林補遺正互變三十年/小限等說；卷三另有批評，不把卷內引文與作者立場或跨書共識混合。'),
('kin-counts',[23,24],'家庭關係與五行生成數/倍減等說需按來源及生旺休囚分辨，尚未驗證人口或子女數準確率。'),
('changed-kin',[25],'化父化子、世應生合與身爻等仍依問事/親疏/位置；僅讀到25，未聲稱身命全篇完成。'),
]
write('OPERATIONAL_CLAUSES.json',{'date':'2026-10-27','sourceID':'B03-book3','clauses':[
 {'id':i,'pdfPages':pages,'boundedParaphrase':s,'consumerApplied':False,'historicalOutcomesValidated':False} for i,pages,s in clauses],
 'sourceInstructionsAreData':True,'allVolume5ClausesCompiled':False})
write('SOURCE_AUDIT.json',{'date':'2026-10-27','sourceID':'B03-book3','acquisitionRevision':1004714434,
 'rawPDFSHA256':a['sha256'],'rawPDFBytes':56939817,'rawPDFPages':67,
 'originalBytesAreCommonsLibraryScanNotDirectNewNLCRetrieval':True,
 'catalog1904MetadataIsNotNewDirectImprintProof':True,
 'sameSeriesNotAnIndependentWitness':True,'sourceIsNotUserInstruction':True,
 'historicalExamplesAreNotIndependentOutcomeValidation':True,
 'earlierSourceCriticismsNotAutomaticallyResolvedByLaterQuotation':True,
 'firstPassPages':list(range(2,26)),'unviewedPages':[1]+list(range(26,68)),
 'notEstablished':['All source conditions and timing model','Complete textual volume5',
 'Remaining physical books4..6','Independent source pedigree','B02PDF52date-void issue resolved'],
 'wholeBookApplied':False,'wholeCatalogueCompleted':False})
print('Recorded 24 content pages, four complete first-pass section spans and one partial span; four timing methods bounded.')
