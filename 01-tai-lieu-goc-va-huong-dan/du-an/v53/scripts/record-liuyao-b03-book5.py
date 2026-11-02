from pathlib import Path
from hashlib import sha256
import json
base=Path(__file__).resolve().parent.parent/'research/liuyao-b03-book5'
def write(n,d):(base/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda n:sha256((base/n).read_bytes()).hexdigest()
topics={1:'Opening cover only',2:'Direct volume11 opening / 避亂: historical refuge context and subject/inner/outer roles',
3:'避亂: motion/control/hidden/void premises and source direction imagery',4:'避亂: primary/changed, combination and near/far contexts',
5:'避亂: relative/financial loss/element hazard claims historical',6:'避亂: source kin/strength/void and arrest claims historical',
7:'避亂: concluding conditional cautions and no-general-outcome conclusion',8:'避亂 concludes; 逃亡 begins: source wanted-person context',
9:'逃亡: hidden/visible kin, movement, place/time qualification',10:'逃亡: motion/clash/combination and source position imagery',
11:'逃亡: returning/wandering soul, documents, concealment, raw structure is not efficacy',
12:'逃亡 concludes; 失脫 with 附盜賊 / 捕盜捉賊 headings; lost-object default wealth and motion/void conditions',
13:'失脫: element/object/place, static/moving, tomb and hidden-branch claims',
14:'失脫: hidden kin versus family/outsider/sex/appearance claims; historical not identification',
15:'失脫/盜賊: multiple people/element and occupation imagery, no suspect profiling validation',
16:'失脫/捕盜: source strength/capture/hidden conditions, no modern evidence',
17:'失脫 concludes with explicit non-wealth exceptions; 新增痘疹 begins',
18:'新增痘疹: child/relative roles, source strength/void; historical not clinical',
19:'新增痘疹: medical/food/drug claims historical only',20:'新增痘疹: timing/six figures/support/hidden source qualifications',
21:'新增痘疹: bodily disease-element and eight-trigram imagery historical only',
22:'新增痘疹 concludes; direct volume11 end; source five-element versus spirit prioritization statement',
23:'Direct volume12 opening / 出行: source baggage/wealth and self role',
24:'出行: 世/應, companion/interval, movement and date premises',
25:'出行: source directions, career contexts, land/water and kin/spirit claims',
26:'出行: companion/hostile/intermediate and conditional cautions',27:'出行 concludes; 行人 begins: relative subject/return questions',
28:'行人: combined/void/near-far timing, hidden/visible and unknown calendar premises',
29:'行人: kin/combination/role narratives and no single return rule',
30:'行人: document use, returning/wandering soul and source timing alternatives',
31:'行人 concludes; 舟船 begins: boat versus crew, six-line cabin grouping',
32:'舟船 concludes; 娼家 begins with historical sex-work/household context',
33:'娼家: historical household role/illness/money/family claims',
34:'娼家 concludes; 船家宅章 starts; bow/stern line1 wording remains text-context issue',
35:'船家宅章 concludes; 何知章 begins: conditional question-answer verses',
36:'何知章: household fortune/property/work/patronage verses, not independent observations',
37:'何知章: household fire/spirits/crime/illness verses historical',
38:'何知章 concludes; 妖孽賦 begins',39:'妖孽賦 concludes; 搜鬼論 begins with branch/location verses',
40:'搜鬼論: branch-keyed household/ritual claims historical only',
41:'搜鬼論 concludes; direct 卜筮正宗卷之十二終',42:'Closing cover only'}
write('MANUAL_READINGS.json',{'date':'2026-10-27','sourceID':'B03-book5','sourcePDF':'NLC892-GBZX0301013045-259423.pdf',
 'sourceSHA256':'cca4c2ce376c54c6ead6463c72e6f25d6e6e544b3d6488d593415afabc6227a6',
 'records':[{'pdfPage':n,'image':f'images/bushi-book5-{n:02}.png','sha256':sha(f'images/bushi-book5-{n:02}.png'),
 'topic':topics[n],'scope':'cover-only'if n in[1,42]else'first-pass-relevant-span',
 'entirePageDiplomaticallyTranscribed':False}for n in range(1,43)],
 'qaImages':[{'pdfPage':n,'image':image,'sha256':sha(image),'dpi':360,'cropPixels':crop,
 'purpose':purpose}for n,image,crop,purpose in[
 (17,'images/lost-role-p17-qa.png',[0,140,1180,1880],'Read object-role exceptions directly'),
 (34,'images/boat-p34-qa.png',[1160,150,2304,1800],'Retain unresolved bow/stern wording; no global ordinal map')]],
 'directBoundaries':[{'pdfPage':2,'reading':'卜筮正宗卷之十一'},{'pdfPage':22,'reading':'卜筮正宗卷之十一終'},
 {'pdfPage':23,'reading':'卜筮正宗卷之十二'},{'pdfPage':41,'reading':'卜筮正宗卷之十二終'}],
 'counts':{'manualRecords':42,'contentPages':40,'coverPages':2,'QAOnlyRenders':2},
 'ocrUsed':False,'unviewedPages':[],'allClausesApplied':False,'entireBookApplied':False})
units=[(11,'避亂',2,8),(11,'逃亡',8,12),(11,'失脫',12,17),(11,'新增痘疹',17,22),
 (12,'出行',23,27),(12,'行人',27,31),(12,'舟船',31,32),(12,'娼家',32,34),
 (12,'船家宅章',34,35),(12,'何知章',35,38),(12,'妖孽賦',38,39),(12,'搜鬼論',39,41)]
write('BOOK5_CURRENT_UNITS.json',{'date':'2026-10-27','sourceID':'B03-book5','units':[
 {'textualVolume':v,'heading':h,'pdfPages':list(range(lo,hi+1)),'relevantSpanFirstPassRead':True,'entireUnitApplied':False}for v,h,lo,hi in units],
 'nestedHeadingAt12':['附盜賊','捕盜捉賊'],'countingNote':'Nested labels preserved without inventing disjoint page spans or new main units.',
 'counts':{'mainUnits':12,'textualVolumes':2,'firstPassMainSpans':12,'entireUnitsApplied':0},
 'all42PagesViewedWithRecordedScope':True,'allSourceClausesApplied':False,'wholeBookApplied':False})
write('LOST_OBJECT_ROLE_CLAUSES.json',{'date':'2026-10-27','sourceID':'B03-book5',
 'context':'B03-volume11-lost-objects','defaultWealthContextPDFPage':12,'exceptionPDFPage':17,
 'boundedReading':'失脫不可專以財為用神','parentObjectReading':'若失舟車衣帽文章奏疏則以父母為用爻',
 'parentMovingCautionReading':'故忌財動','childObjectReading':'若失飛禽走獸則以子孫為用爻',
 'childMovingCautionReading':'故忌父爻動','notEveryLostThingIsWealth':True,
 'sourceCategories':{'wealth':['cash'],'父母':['boat','vehicle','garment','headwear','document','memorial'],
 '子孫':['bird','beast']},'categoryIDsAreEditorialNormalization':True,
 'movingCautionIsNotOutcomeAdjudication':True,'notEstablished':['All modern object types','Physical search location',
 'Suspect identity','Capture outcome','Full lost-object and timing rules'],'consumerApplied':False})
ops=[('refuge',[2,3,4,5,6,7,8],'Tránh loạn có vai trò/ngày tháng/động biến riêng; giữ lịch sử, không thay hướng dẫn an toàn thực tế.'),
('fugitive',[8,9,10,11,12],'Chủ tượng, ẩn hiện, hợp xung và quẻ hồi hồn/du hồn có tiền đề; không dùng để né hoặc bảo đảm bắt người.'),
('lost-object',[12,13,17],'Đồ mất không mặc định đều lấy Tài. Tiền, giấy tờ/y phục/xe thuyền và chim thú có vai nguồn riêng.'),
('moving-cautions',[17],'Nhóm Phụ mẫu kỵ Tài động, nhóm Tử tôn kỵ Phụ động theo câu nguồn; cờ cấu trúc chưa xét mạnh yếu hoặc kết cục.'),
('no-suspect-identification',[14,15,16,17],'Lấy tượng giới/ngoại hình/nghề/người quen để luận trộm chưa có kiểm chứng; không nhận dạng hoặc buộc tội người thật.'),
('pox-history',[17,18,19,20,21,22],'Mục bệnh trẻ và lời thuốc, ăn uống, sống chết là y học/thuật số lịch sử, không hướng dẫn điều trị hoặc tiên lượng.'),
('travel',[23,24,25,26,27],'Đi lại tách người hỏi, hành lý, bạn đồng hành và dụng theo mục đích, không lấy tên quẻ làm bảo đảm an toàn.'),
('traveller',[27,28,29,30,31],'Hỏi người đi xa cần vai thân thuộc và điều kiện thời điểm; gần/xa, tĩnh/động, ngày tháng chưa có bộ phân xử đầy đủ.'),
('boat',[31,32,34,35],'Tượng thuyền/hành khách/nhà thuyền cần ngữ cảnh; chữ đầu/đuôi ở34 còn vấn đề, không sửa nguồn hoặc làm bản đồ toàn cục.'),
('historical-household',[32,33,34],'Mục 娼家 giữ trong bối cảnh xã hội lịch sử, không biến ngũ hành thành phán đoán đạo đức hoặc thuộc tính người dùng.'),
('question-verses',[35,36,37,38],'何知章 là câu đối đáp có điều kiện, chưa là danh mục mọi kết luận hộ gia đình đã xác minh.'),
('spirit-claims',[38,39,40,41],'妖孽賦/搜鬼論 là lời tượng nghi lễ, chưa bằng chứng có ma/tà hoặc chỉ dẫn thực hiện nghi lễ.'),
('source-method',[22,30,34,41],'Lời mệnh lệnh trong nguồn là dữ liệu; tiêu chí nguồn/diễn giải/chưa xác minh phải tách, không giả là chỉ thị của người dùng.')]
write('OPERATIONAL_CLAUSES.json',{'date':'2026-10-27','sourceID':'B03-book5','clauses':[
 {'id':i,'pdfPages':pages,'boundedParaphrase':t,'consumerApplied':False,'historicalOutcomesValidated':False}for i,pages,t in ops],
 'sourceInstructionsAreData':True,'allBook5ClausesCompiled':False})
write('TEXT_ISSUES.json',{'date':'2026-10-27','issues':[{'id':'boat-bow-stern-ordinal','pdfPages':[31,34],
 'readings':['初二爻為前倉','五六爻為後艙','初當船尾','青龍初是船頭','六為後艄'],
 'scope':'Readings cross boat/boat-house contexts; page34 itself retains different line1 wording.',
 'status':'open-text-context-and-independent-witness-collation','correctionApplied':False,
 'unverifiedExplanation':'No claim that context alone resolves the differing wording; no ordinal map generalized.'}]})
write('SOURCE_AUDIT.json',{'date':'2026-10-27','sourceID':'B03-book5','sourcePDF':'NLC892-GBZX0301013045-259423.pdf',
 'rawPDFBytes':35113503,'rawPDFPages':42,'sourceSHA256':'cca4c2ce376c54c6ead6463c72e6f25d6e6e544b3d6488d593415afabc6227a6',
 'APIRevision':754088953,'newOriginalPDFsToRelease':1,'retainedHTTPBodiesNewToRelease':2,'newHTTPBodiesThisRun':2,
 'sameSeriesNotIndependentWitness':True,'catalog1904IsNotNewDirectImprintProof':True,
 'all42PagesViewedWithRecordedScope':True,'unviewedPages':[],'sourceIsNotUserInstruction':True,
 'notEstablished':['Every clause applied','Medical/ritual/crime identification claims validated','Full strength/void/timing',
 'Boat wording resolved','Supplement genealogy','Book6 acquired','B02PDF52conflict resolved'],
 'wholeBookApplied':False,'wholeCatalogueCompleted':False})
print('Recorded42pages/12mainspans/13boundedclauses; lost-object role exceptions and open boat wording retained.')
