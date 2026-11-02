from pathlib import Path
from hashlib import sha256
import json,shutil
r=Path(__file__).resolve().parent.parent;w=r.parent;s=w/'tmp/home-zhaijing-staging';b=r/'research/home-you-nian'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
def write(n,d):(b/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert len(read(w/'archives/v53-before-home-you-nian/PACKAGE_MANIFEST.json')['files'])==2915
b.mkdir(exist_ok=False);(b/'images').mkdir();(b/'zhaijing').mkdir()
renders=read(s/'XIEJI_RENDERS.json');assert len(renders['records'])==57 and renders['calibration']['nativePixelEqualityWithPriorBrowserPNG']
for x in renders['records']:
 p=s/x['file'];assert sha(p)==x['sha256'];shutil.copy2(p,b/'images'/p.name);x['file']='images/'+p.name
shutil.copy2(s/'decoder-calibration-p223.png',b/'decoder-calibration-p223.png');write('RENDERS.json',renders)
for name in ['DIGITAL_UNIT_MAP.json','TRANSMISSION_COMPARISON.json','REQUESTS.json','commons-imageinfo.json.403.txt','CADAL06054151.djvu.403.txt','waseda-i04_00600_0162.pdf.503.txt']:
 shutil.copy2(s/name,b/'zhaijing'/name)
notes={54:'Previous solar-term discussion ending, before current section; no new calendar adapter.',55:'八卦納甲三合 diagram located; not used as proof of all NaJia/combination rules.',56:'NaJia prose and source attribution; 巳/己 glyph near branch slots requires separate collation.',57:'小遊年變卦 heading: 天父 from乾, 地母 from坤; uses, borrowed marriage rule and star order.',58:'Eight star names/elements and relation names; 地理家 from龍 and 選擇家 from向 give different good/bad star sets.',59:'Continuation of selection-family classification; meanings differ by use. Not a universal rating.',60:'Ruled blank.',61:'天定卦 diagram: four opposed trigram pairs.',62:'天定卦 explanation; 本卦上爻/opposed trigram and two alternative diagrams discussed.',63:'天父卦 diagram, eight direct stars with origin乾.',64:'天父 from乾 named upper/middle/lower successive changes and return, also旁起旁止.',65:'地母卦 diagram, eight direct stars with origin坤.',66:'地母 sequence and 青囊經 attribution; 三吉六秀 context begins.',67:'Source quotations and commentary distinguish direction, dragon, yin/yang and mountain/water contexts.',68:'三合/九六衝和/八貴十二吉 discussion, not a modern dwelling rule.',69:'End of commentary: named diagrams used as examples; not all application conditions compiled.',70:'Ruled blank.',71:'兌宮翻卦 diagram, eight direct stars.',72:'兌 sequence prose.',73:'巽宮翻卦 diagram, eight direct stars.',74:'巽 sequence prose.',75:'坎宮翻卦 diagram, eight direct stars.',76:'坎 sequence and 天父 convention commentary.',77:'艮宮翻卦 diagram, eight direct stars.',78:'艮 sequence prose.',79:'震宮翻卦 diagram, eight direct stars.',80:'震 sequence prose.',81:'離宮翻卦 diagram, eight direct stars.',82:'離 sequence followed by general named-line transformations.',83:'General 小遊年 relations; 本宮/伏位/輔弼 terms; commentary on坐山 versus立向 conventions.',84:'Historical attribution and source-family discussion; not proof of author identity.',85:'Source-family commentary on 陰/陽/純卦 and paired changes.',86:'Continuation of critiques; source reasoning retained as source commentary.',87:'End of 小遊年; 大遊年變卦 heading and residence/宅長行年配合修造 context.',88:'大遊年 star order and named successive changes from乾; contrasted with小遊年.',89:'東四/西四 grouping and named line-change commentary.',90:'八宮 stages: 本宮伏位, 初禍害, 二天醫, 三延年, 四五鬼, 五生氣, 遊魂六煞, 歸魂絶命.',91:'上一爻變 diagram: 小生氣吉 / 大生氣吉; four trigram pairs.',92:'Commentary on upper-only transformation.',93:'One-line continuation ending 生氣也; not blank.',94:'Ruled blank.',95:'上二爻變 diagram: 小天醫吉 / 大五鬼凶; four trigram pairs.',96:'Named pairs and commentary for upper two lines.',97:'下一爻變 diagram: 小五鬼凶 / 大禍害凶.',98:'Named pairs and commentary for lower-only change.',99:'下二爻變 diagram: 小福德吉 / 大天醫吉.',100:'Named pairs and commentary for lower two lines.',101:'上下二爻變 diagram: 小遊魂凶 / 大六煞凶.',102:'Explicit pairs乾坎/兌巽/離艮/震坤 and commentary; distinguish middle-only pairs.',103:'中一爻變 diagram: 小絶命凶 / 大絶命凶.',104:'Explicit pairs乾離/兌震/巽艮/坎坤 and commentary.',105:'三爻俱變 diagram: 小絶體凶 / 大延年吉.',106:'All-three change commentary; no empirical efficacy inferred.',107:'八宮六十四卦圖: eight row headers for both systems, first three palace columns; individual 384 line strokes not collated.',108:'Remaining five palace columns; figures located, not a complete glyph-by-glyph collation.',109:'Seal only, no rule text.',110:'Volume end 欽定協紀辨方書卷二.'}
write('MANUAL_READINGS.json',{'date':'2026-10-27','source':renders['source'],'sourceSHA256':renders['sourceSHA256'],
 'sourceInstructionsAreData':True,'method':'Direct visual reading of native page renders; no OCR. Page means one-based DjVu image, not printed folio.',
 'newlyReadImagePages':57,'contentPages':52,'ruledBlankPages':[60,70,94],'paratextPages':[109,110],
 'firstPassSpans':[{'name':'context before小遊年','pages':[54,56]},{'name':'小遊年變卦','pages':[57,87]},{'name':'大遊年/contrasts/eightpalacefigures/end','pages':[87,110]}],
 'readings':[{'page':n,'file':f'images/p{n:03}.png','sha256':next(x['sha256']for x in renders['records']if x['page']==n),'scope':notes[n],'directlyViewed':True,'allAtomicClausesExtracted':False}for n in range(54,111)],
 'priorReadings2to8Unmodified':True,'whole110PageVolumeRead':False,'wholeBookApplied':False})
rows=[(4,'上一爻變',91,92,'生氣','生氣','吉','吉',['乾兌','巽坎','艮坤','離震']),
 (6,'上二爻變',95,96,'天醫','五鬼','吉','凶',['乾震','兌離','巽坤','坎艮']),
 (1,'下一爻變',97,98,'五鬼','禍害','凶','凶',['乾巽','兌坎','離艮','震坤']),
 (3,'下二爻變',99,100,'福德','天醫','吉','吉',['乾艮','兌坤','離巽','震坎']),
 (5,'上下二爻變',101,102,'遊魂','六煞','凶','凶',['乾坎','兌巽','離坤','震艮']),
 (2,'中一爻變',103,104,'絶命','絶命','凶','凶',['乾離','兌震','巽艮','坎坤']),
 (7,'三爻俱變',105,106,'絶體','延年','凶','吉',['乾坤','兌艮','離坎','震巽'])]
write('SOURCE_RELATIONS.json',{'source':'欽定協紀辨方書卷二, retained CADAL06056503',
 'bitEncoding':'Modern bottom/middle/top weights1/2/4, not a claim about historical binary arithmetic.',
 'selfRelation':{'mask':0,'small':'輔弼','big':'伏位','pages':[83,90,107],'literalNamesEqual':False,'samePalaceRoleOnly':True},
 'rows':[dict(mask=m,namedChangedLines=n,diagramPage=p,prosePage=q,small=sm,big=bg,smallDiagramRating=sr,bigDiagramRating=br,directUnorderedPairs=pairs)for m,n,p,q,sm,bg,sr,br,pairs in rows],
 'stageHeaders':{'pages':[107,108],'small':['輔弼','五鬼','福德','絶體','天醫','生氣','遊魂','絶命'],'big':['伏位','禍害','天醫','延年','五鬼','生氣','六煞','絶命']},
 'literalEqualNonselfMasks':[2,4],'differentNonselfMasks':[1,3,5,6,7],
 'samePalaceIsNotLiteralSynonymClaim':True,'consumerApplied':'Only 大遊年 is compared with current directions table; no new 小遊年 mode enabled.'})
order=list('乾艮坎震離巽坤兌')
stars=[('乾',63,'輔武文巨破廉祿貪'),('坤',65,'祿貪破廉文巨輔武'),('兌',71,'貪祿廉破巨文武輔'),('巽',73,'廉破貪祿武輔巨文'),('坎',75,'文巨輔武祿貪破廉'),('艮',77,'武輔巨文廉破貪祿'),('震',79,'巨文武輔貪祿廉破'),('離',81,'破廉祿貪輔武文巨')]
write('SMALL_DIRECT_STARS.json',{'sourcePages':[63,65,71,73,75,77,79,81],'targetOrder':order,
 'readings':[{'origin':n,'page':p,'starsByTarget':[{'target':t,'printedAbbreviation':v}for t,v in zip(order,st)]}for n,p,st in stars],
 'directCells':64,'abbreviations':{'貪':'貪狼','巨':'巨門','祿':'祿存','文':'文曲','廉':'廉貞','武':'武曲','破':'破軍','輔':'輔弼'},
 'goodBadUniversal':False})
write('SOURCE_POLICIES.json',{'pages':[57,58,59],'namesAreSourceContextsNotEmpiricalValidation':True,
 'policies':[{'id':'geography-from-dragon','sourceTerm':'地理家從龍上起','auspiciousStars':['貪狼','巨門','武曲','廉貞'],'otherFour':'凶'},
 {'id':'date-selection-from-facing','sourceTerm':'選擇家從向上起','auspiciousStars':['貪狼','巨門','武曲','文曲'],'otherFour':'凶'}],
 'contrastDiagramLayer':'小遊年 comparison diagrams mark 五鬼/廉貞凶 and 遊魂/文曲凶. This differs from one favorable star in each named use; do not merge into one universal score.',
 'noDefaultOrigin':'No adapter chooses龍,坐山,立向 or birth year from a modern dwelling.',
 'sourceAttributesNotEstablishedAsHistoricalFacts':['青囊經 attribution','邱公頌 transmission','author identity of 黃帝宅經']})
write('SOURCE_AUDIT.json',{'date':'2026-10-27','retainedOriginalContainer':renders['source'],'sourceBytes':3433014,'sourceSHA256':renders['sourceSHA256'],
 'sourcePages':110,'newOriginalContainers':0,'newSuccessfulHTTPBodies':0,'retainedFailedHTTPBodies':3,'newHTTPRequestsThisTurn':1,
 'failedStatuses':[403,403,503],'TLSAuthorizedAllFailedRequests':True,'failedBodiesNotSourceBooks':True,
 'newNativePageDerivatives':57,'newlyReadSourceImagePages':57,'decoderCalibrationNewSourcePage':False,
 'decoderMethod':renders['method'],'decoderNativePixelCalibration':True,'P03DigitalArtifactsRead':6,'P03NewPairedContexts':10,
 'P03FacsimileResolved':False,'XiejiFirstPassSmallBigSpansRead':True,'allClausesApplied':False,'consumerChanged':False,'wholeCatalogueCompleted':False})
print('Recorded 57 direct readings, seven paired transformations, 64 direct small-system star cells and six digital artifacts.')
