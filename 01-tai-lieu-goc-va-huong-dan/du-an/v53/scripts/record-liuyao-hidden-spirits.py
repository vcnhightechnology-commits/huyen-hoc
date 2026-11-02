from pathlib import Path
from hashlib import sha256
import json
root=Path(__file__).resolve().parent.parent;base=root/'research/liuyao-hidden-spirits'
def write(name,d):(base/name).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda p:sha256(p.read_bytes()).hexdigest()
# Normalized headings, not a diplomatic transcription of every allograph/章 suffix.
groups=[
 (13,1,1,'八卦 卦象圖 八宮 渾天甲子 六親歌 世應 動變 用神 用神元神忌神仇神 元神忌神衰旺 五行相生 五行相克 克處逢生 動靜生克 動靜生克沖合 四時旺相 月將'.split()),
 (14,2,18,'六神 六合 六沖 三刑 暗動 動散 變卦生克墓絕 反伏 旬空 月破 飛伏神 進神退神 隨鬼入墓 獨發 兩現 星煞'.split()),
 (15,4,34,'增刪黃金策千金賦 天時 身命 終身財福 終身功名有無 壽元 超遷 父母壽元 兄弟 夫婦 子嗣 學業 治經 延師 求名 童試 歲考科考 增廩 考遺才 發案掛榜 廷試 鄉試會試'.split()),
 (16,4,56,'陞選何方 在任吉凶 援例 武試 投牒效用入武從軍 署印謀差 面聖上書叩閽獻策條陳劾奏 養親告病辭官 修陵修河一切營造公務防患 僧官道紀醫官雜職陰陽等官 功名到何品級 子占父功名 求財 謁貴求財 為貴人奔走效力求財 開行開店及各色舖面'.split()),
 (17,5,72,'投行損益 買貨賣貨 賣貨宜守宜動 在何方買賣 買何貨為吉 借貸 放債索債 買賣六畜 博戲 請會搖會 行險求財 此婚子嗣有無 此婚有宜於父母否 納寵 取離婦跳娼婦 胎孕 問產婦安否 產期 嬰童否泰 出行 舟行 同舟共行 行人'.split()),
 (18,6,95,'防非避訟 鬥毆爭競 興詞舉訟 已定重罪 疾病 痘疹 病源 鬼神 延醫 醫卜往治 家宅 蓋造買宅賣宅 創造宮室 修方動土 遷居進火 歸宅入火 入宅六親吉凶 馬房豬圈 舊宅 同居 蓋造官衙 占衙宇'.split()),
 (19,6,117,'蓋造寺院 塋葬 尋地 占地形勢 卜得地於何時 得地於何方 占地師 點穴 謀地偷葬 祖塋舊塚 因何事所傷 修補秘法 再占修補吉凶 新亡附葬祖塋'.split()),
]
units=[]
for page,volume,start,titles in groups:
 for i,title in enumerate(titles):
  n=start+i;vol=3 if n==33 else 5 if 62<=n<=94 else volume
  units.append({'id':f'B02-ch{n:03}','printedNumber':n,'supplement':False,'normalizedHeading':title,'tocPDFPage':page,'tocVolume':vol,
   'bodyPDFPages':[108,109,110,111,112,113,114,115,116]if n==28 else None,
   'disposition':'full-chapter-first-pass-read-partial-private-application'if n==28 else'partial-foundation-reading-private-structure'if n<=7 else'heading-only-body-extraction-open',
   'entireUnitApplied':False})
for key,title,page,volume,n in [
 ('a','生旺墓絕',14,2,26),('b','各門類題頭總註',14,2,26),('c','各門類應期總註',14,2,26),('d','歸魂遊魂',14,2,26),('a','陞選候補',16,4,55)]:
 units.append({'id':f'B02-ch{n:03}-supp-{key}','printedNumber':n,'supplement':True,'printedLabelQualification':'又'+str(n),
  'normalizedHeading':title,'tocPDFPage':page,'tocVolume':volume,'bodyPDFPages':None,
  'disposition':'heading-only-body-extraction-open','entireUnitApplied':False})
assert len(units)==135 and len({u['id']for u in units})==135
assert sorted(u['printedNumber']for u in units if not u['supplement'])==list(range(1,131))
write('B02_TOC_UNITS.json',{'schema':'hhc.liuyao.b02.toc.v1','date':'2026-10-27','sourcePDF':'../liuyao-foundations/NLC416-12jh005345-45344.pdf',
 'sourceSHA256':'caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa','contentTOCPages':[13,14,15,16,17,18,19],'tocEndleafPDFPage':20,
 'regularNumberedUnits':130,'supplementalRepeatedNumberUnits':5,'units':sorted(units,key=lambda u:(u['printedNumber'],u['id'])),
 'policy':'Headings normalized for retrieval,not a diplomatic allograph edition. TOC volume labels are not yet physical body spans. Heading registration is not reading or implementation.',
 'b03CompleteTOC':False,'fullBookApplied':False})

pages=[13,14,15,16,17,18,19,20,80,100,104,108,109,110,111,112,113,114,115,116,120,140]
records=[]
for n in pages:
 p=root/'research/liuyao-foundations/images/zengshan-13.png'if n==13 else base/f'images/zengshan-{n}.png'
 level='expanded-toc-heading-reading'if n==13 else'new-toc-heading-reading'if 14<=n<=19 else'chapter28-first-pass-full-span'if 108<=n<=116 else'endleaf-only'if n==20 else'advertisement-only'if n==140 else'bounded-body-navigation-probe'
 records.append({'pdfPage':n,'image':('../liuyao-foundations/images/zengshan-13.png'if n==13 else f'images/zengshan-{n}.png'),
  'imageSHA256':sha(p),'readingLevel':level,'newPageReading':n!=13,'entirePageTranscribed':False})
write('MANUAL_READINGS.json',{'date':'2026-10-27','records':records,'counts':{'records':22,'newRetainedSourceRenders':21,'expandedPriorTOCPage':1,'chapterSpanPages':9,'tocContentPages':7,'boundedNavigationProbes':4,'advertisements':1,'tocEndleaves':1},
 'chapterBoundary':{'heading':'飛伏神章第二十八','startPDFPage':108,'nextHeading':'進神退神章第二十九','nextHeadingPDFPage':116,'scope':'Onlychapter28textwithinbothboundarypages;neighboring27/29clausesnotclaimedcomplete.'},
 'newHTTPResponses':0,'newOriginalPDFs':0,'ocrUsed':False})

def clause(id,kind,p,paraphrase,expr):return{'id':id,'sourceClass':kind,'pdfPage':p,'boundedParaphrase':paraphrase,'expression':expr,'consumerApplied':False}
clauses=[
 clause('U1','six-listed-useful',110,'Hidden spirit receives generation from day/month.','hiddenDayMonthGenerated'),
 clause('U2','six-listed-useful',110,'Hidden spirit is flourishing/strong.','hiddenStrong'),
 clause('U3','six-listed-useful',110,'Covering flying line generates hidden spirit.','flyingGeneratesHidden'),
 clause('U4','six-listed-useful',110,'A moving line generates hidden spirit.','hiddenMovingGenerated'),
 clause('U5','six-listed-useful',110,'Day/month/moving lines clash with or control covering flying line.','flyingDayMonthMovingAttacked'),
 clause('U6','six-listed-useful',110,'Covering flying line is void,month-broken,weak,in tomb or extinct.',{'any':['flyingVoid','flyingMonthBroken','flyingWeak','flyingTomb','flyingExtinct']}),
 clause('N1','five-listed-unusable',111,'Hidden spirit weak and without qi.','hiddenWeakWithoutQi'),
 clause('N2','five-listed-unusable',111,'Hidden spirit clashed with or controlled by day/month.','hiddenDayMonthAttacked'),
 clause('N3','five-listed-unusable',111,'Strong covering flying line controls hidden spirit.',{'all':['flyingStrong','flyingControlsHidden']}),
 clause('N4','five-listed-unusable',111,'Hidden spirit at tomb/extinction relative to day/month/flying line.','hiddenTombOrExtinctAtDayMonthFlying'),
 clause('N5','five-listed-unusable',111,'Weak hidden spirit is void or month-broken.',{'all':['hiddenWeak',{'any':['hiddenVoid','hiddenMonthBroken']}]}),
]
write('CONDITIONS.json',{'date':'2026-10-27','sourceChapter':28,'sourcePDFPages':list(range(108,117)),'clauses':clauses,
 'factualInputs':['hiddenDayMonthGenerated','hiddenStrong','hiddenMovingGenerated','flyingDayMonthMovingAttacked','flyingVoid','flyingMonthBroken','flyingWeak','flyingTomb','flyingExtinct','hiddenWeakWithoutQi','hiddenDayMonthAttacked','flyingStrong','hiddenTombOrExtinctAtDayMonthFlying','hiddenWeak','hiddenVoid','hiddenMonthBroken'],
 'structuralInputs':['flyingGeneratesHidden','flyingControlsHidden'],'missingInputs':'unknown,notfalse',
 'conflictPolicy':'Return every matched/contradicted/pending clause and concurrent positive/negative matches;do not invent source priority or a final fortune verdict.',
 'limits':['No automatic use-god selection','No Gregorian/month/day-boundary adapter','No strength/tomb/void classifier from these clauses alone','No medical/lifespan/death predictions','No empirical efficacy established']})

write('PLACEMENT_AND_VARIANTS.json',{'date':'2026-10-27','rules':[
 {'id':'P1','pdfPages':[108,109,110],'meaning':'When desired kin is absent,read corresponding lines of the original palace pure hexagram;the current same-position line covers it as飛神.'},
 {'id':'P2','pdfPages':[108,109,110],'meaning':'Source first considers day/month candidates when desired kin is not in the figure;calendar usefulness and strength premises remain explicit and unevaluated here.'},
 {'id':'P3','pdfPages':[112],'meaning':'Other cited methods search another palace or a returning-soul fourth figure when a pure primary hexagram has a damaged desired kin. The commentator rejects automatically taking those alternatives;do not silently mix methods.'},
 {'id':'P4','pdfPages':[113,114,115],'meaning':'Historical repeated-cast anecdotes and medical/death claims retained as historical claims,not outcome validation or instructions to user.'},
 {'id':'P5','pdfPages':[115],'meaning':'困→兌example compares damaged visible午fire,hidden巳fire and changed巳fire. A visible kin does not prove the entire source discussion inapplicable;changed-line candidates must remain visible and no automatic hidden-only decision is made.'},
 {'id':'P6','pdfPages':[115,116],'meaning':'Commentator disputes an exclusive focus on hidden/changed placement and cites month or changing-line usefulness. Candidate placement is separate from choosing a useful god.'}],
 'candidateAPI':'Return pure-palace structural locations for an explicit desired kin,visible/changed/day-month availability,and relationships;always usefulnessSelection=null. No automatic fallback selection.',
 'sourceInstructionsAreData':True,'independentB03ChapterCollation':False,'fullChapterFirstPassRead':True,'allHistoricalClaimsEstablished':False})

write('SOURCE_FIXTURES.json',{'date':'2026-10-27','cases':[
 {'id':'gou-hidden-wealth','pdfPages':[108,109],'number':44,'desiredKin':'妻財','hidden':[{'line':2,'branch':'寅','element':'木','flyingBranch':'亥','relation':'flying-generates-hidden'}],'visibleLines':[]},
 {'id':'dun-hidden-child','pdfPages':[109,110],'number':33,'desiredKin':'子孫','hidden':[{'line':1,'branch':'子','element':'水','flyingBranch':'辰','relation':'flying-controls-hidden'}],'visibleLines':[]},
 {'id':'bi-hidden-parent','pdfPages':[111],'number':22,'desiredKin':'父母','hidden':[{'line':2,'branch':'午','element':'火','flyingBranch':'丑','relation':'hidden-generates-flying'}],'visibleLines':[]},
 {'id':'sheng-hidden-child','pdfPages':[112],'number':46,'desiredKin':'子孫','hidden':[{'line':4,'branch':'午','element':'火','flyingBranch':'丑','relation':'hidden-generates-flying'}],'visibleLines':[]},
 {'id':'sun-visible-parent','pdfPages':[113],'number':41,'desiredKin':'父母','hidden':[{'line':2,'branch':'午','element':'火','flyingBranch':'卯','relation':'flying-generates-hidden'}],'visibleLines':[1],
  'hiddenExpectationEvidence':'Derived comparison from the pure-palace placement rule,not a printed hidden-parent annotation in this figure. Printed prose instead identifies visible巳fireparenton first line.'},
 {'id':'kun-to-dui-competing-fire','pdfPages':[115],'number':47,'movingLines':[1],'changedNumber':58,'desiredKin':'官鬼','hidden':[{'line':1,'branch':'巳','element':'火','flyingBranch':'寅','relation':'flying-generates-hidden'}],'visibleLines':[3],
  'changedKinLines':[1],'meaning':'Keep hidden/visible/changed candidates separate;not automaticuse-godselection.'}],
 'readingClarification':'PDF113first figure is損41,with visible巳fireparenton first line. The later heading漸之巽is a separate recast53→57;do not assign its figure to the earlier初爻prose or invent a source position contradiction.'})
print(json.dumps({'tocUnits':135,'regularNumbers':130,'repeatedNumberSupplements':5,'imageRecords':22,'chapterSpanPages':9,'conditionalClauses':11,'sourceCases':6,'newHTTP':0}))
