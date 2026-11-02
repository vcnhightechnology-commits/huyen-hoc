from pathlib import Path
from hashlib import sha256
import json
root=Path(__file__).resolve().parent.parent;base=root/'research/liuyao-b03-book4'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
def write(n,d):(base/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
a=read(base/'ACQUISITION.json');assert sha(base/a['file'])==a['sha256']=='5f8bb92f28120fa4c2c4d629ae8bad9f785dc02324f15f285085c99ab7ffadaf'
prior=read(root.parent/'tmp/liuyao-b03-book4-staging/MANUAL_READINGS.json')
topics={r['pdfPage']:r['topic']for r in prior['records']}
topics.update({1:'Opening cover only',19:'仕宦: role/strength/void and source consequences',20:'仕宦: office/context-specific role selection',
21:'仕宦 ending, direct 卜筮正宗卷之八終',22:'卷之九 title, 求財 begins',23:'求財: 福/財, hidden/visible and support',
24:'求財: asking approach and limits, transactions and transformed kin',25:'求財: waiting, combination/clash and time conditions',
26:'求財: subject roles by item/context, joint trade and loans',27:'求財: stock/travel/transactions and loss narratives',
28:'求財 ends; 家宅 begins, explicit second house/fifth occupants/inner and outer',29:'家宅: building/property, transformations and main role',
30:'家宅: gates/roads symbolic relations, changed void, monthbreak',31:'家宅: primary/changed and 世/應, supports and qualifications',
32:'家宅: illness/death and 本命 historical claims, no validated health predictions',33:'家宅: household relations and 世/應/身 distinctions',
34:'家宅: spouse/children/parents roles and intervening branches',35:'家宅: household relationship historical statements',
36:'家宅: changing household relations, source subject and kin',37:'家宅: historical ritual/disaster assertions',
38:'家宅 main section ends; 新增家宅搜精分別六爻斷法 subheading begins',39:'House supplement: structural symbols, source qualifications',
40:'House supplement: third line/卯 brothers bed exception, conditional symbols',41:'House supplement: fourth brothers gate; combination to second principal gate',
42:'House supplement: conditions/void/monthbreak and distinction from literal doors',43:'House supplement: roles, structural symbols and family-image caveats',
44:'House supplement ending; direct 卜筮正宗卷之九終',45:'卷之十 title, 墳墓 begins',46:'Burial divination: symbolic 穴/世應/山水 relations',
47:'Burial divination: symbolic bearings and branches, not a measured location',48:'Burial divination: structures/spirits and source premises',
49:'Burial divination: water/roads/neighbors, same/divination time relations',50:'Burial divination: tomb/void and shared site narratives',
51:'Burial divination: placement boundaries/reburial historical assertions',52:'Burial divination: offspring/lineage historical claims',
53:'Burial divination: life/health/fire claims, historical not verified events',54:'墳墓 ends; 求師 begins',
55:'求師: document/subject, source kin and teacher context',56:'求師: 世/應 and relative roles by question',57:'求師 ends; 學館 begins',
58:'學館: student/teacher/client roles, 束修 historical terms',59:'學館: documents, strength, support and empty role',
60:'學館: recommendations/student/domain conditions',61:'學館: funding and role/purpose',62:'學館 ends; 詞訟 begins',
63:'詞訟: claimant/respondent, evidence and public-official roles',64:'詞訟: branches/kin and evidence claims',
65:'詞訟: authority and strengths, source timing',66:'詞訟 ends; direct 卜筮正宗卷之十終',67:'Closing cover only'})
records=[{'pdfPage':n,'image':f'images/bushi-book4-{n}.png','sha256':sha(base/f'images/bushi-book4-{n}.png'),
 'topic':topics[n],'scope':'cover-only'if n in[1,67]else'first-pass-complete-relevant-span',
 'inheritedPendingReading':2<=n<=18,'newLocalRenderThisRun':n==1 or n>=19,
 'entirePageDiplomaticallyTranscribed':False}for n in range(1,68)]
write('MANUAL_READINGS.json',{'date':'2026-10-27','sourceID':'B03-book4','sourcePDF':a['file'],'sourceSHA256':a['sha256'],
 'records':records,'counts':{'manualRecords':67,'contentImagesNewToRelease':65,'coverImagesNewToRelease':2,
 'inheritedPendingContentImages':17,'newContentRendersThisRun':48,'newCoverRendersThisRun':2,'QAOnlyRenders':2,
 'newOriginalPDFsToRelease':1,'retainedHTTPBodiesNewToRelease':2,'newHTTPBodiesThisRun':0},
 'qaImages':[{'image':f'images/home-p{n}-qa.png','sha256':sha(base/f'images/home-p{n}-qa.png'),'pdfPage':n,
 'dpi':360,'cropPixels':[30,160,1280,1700]if n==40 else[20,160,1100,1700],
 'purpose':'Read conditional bed exception and fourth-line kin/gate qualification; not another source page.'}for n in[40,41]],
 'directBoundaries':[{'pdfPage':2,'reading':'卜筮正宗卷之八'},{'pdfPage':21,'reading':'卜筮正宗卷之八終'},
 {'pdfPage':22,'reading':'卜筮正宗卷之九'},{'pdfPage':44,'reading':'卜筮正宗卷之九終'},
 {'pdfPage':45,'reading':'卜筮正宗卷之十'},{'pdfPage':66,'reading':'卜筮正宗卷之十終'}],
 'ocrUsed':False,'unviewedPages':[],'allClausesApplied':False,'entireBookApplied':False})
units=[(8,'種作',2,6),(8,'蠶桑',6,9),(8,'六畜',9,13),(8,'求名',13,17),(8,'仕宦',17,21),
 (9,'求財',22,28),(9,'家宅',28,44),(10,'墳墓',45,54),(10,'求師',54,57),(10,'學館',57,62),(10,'詞訟',62,66)]
write('BOOK4_CURRENT_UNITS.json',{'date':'2026-10-27','sourceID':'B03-book4','units':[
 {'textualVolume':v,'heading':h,'pdfPages':list(range(lo,hi+1)),'relevantSpanFirstPassRead':True,
 'inheritedCompletePendingSpan':hi<=17,'entireUnitApplied':False}for v,h,lo,hi in units],
 'subsections':[{'heading':'新增家宅搜精分別六爻斷法','parent':'家宅','pdfPages':list(range(38,45)),
 'relevantSpanFirstPassRead':True,'notAdditionalDisjointContentPages':True,'entireUnitApplied':False}],
 'counts':{'mainUnits':11,'subsections':1,'firstPassMainSpans':11,'firstPassSubsectionSpans':1,
 'inheritedCompletePendingMainSpans':4,'newOrCompletedMainSpans':7,'entireUnitsApplied':0,'textualVolumes':3},
 'covers':[1,67],'all67PagesViewedWithRecordedScope':True,'allSourceClausesApplied':False,'wholeBookApplied':False})
write('HOME_SYMBOL_CLAUSES.json',{'date':'2026-10-27','sourceID':'B03-book4','sourceContext':'B03-volume9-home-divination',
 'anchors':{'house':{'line':2,'sourceSymbol':'宅','pdfPage':28},'occupants':{'line':5,'sourceSymbol':'人口','pdfPage':28},
 'inner':{'lines':[1,2,3],'pdfPage':28},'outer':{'lines':[4,5,6],'pdfPage':28}},
 'fourthLineDoor':{'pdfPage':41,'boundedReading':'四爻兄弟方言戶',
 'commentaryBoundedReading':'無兄弟臨之不可便言門戶如臨兄弟方以戶斷',
 'principalDoorBoundedReading':'第四爻或動或靜與第二爻相合者當以大門決斷',
 'kinPrerequisite':'兄弟','primaryLinesCompared':[4,2],'motionRequirement':None,
 'structuralCombinationUsesPreviouslyCollatedSixCombinationTable':True},
 'thirdLineBedException':{'pdfPage':40,'boundedReading':'兄弟卯爻床榻論',
 'commentaryBoundedReading':'如兄弟是卯爻不可言門戶當以床榻論之','line':3,'kin':'兄弟','branch':'卯'},
 'scope':'Source divination symbols only, not compass-based house planning or physical object detection.',
 'notCompiled':['Full other third-line/door conditions','Other line-element/stem/season/kin alternatives',
 'Original author versus added supplement attribution pedigree','All strength/void/day/month/outcome conditions'],
 'floorPlanAdapter':False,'consumerApplied':False})
ops=[
('crop-context',[2,3,4,5,6],'Trồng trọt phân Tài/Phúc/Phụ và đất/mùa/cây, ngày tháng/động biến; lời mùa màng không là kiểm chứng nông học.'),
('sericulture',[6,7,8,9],'Tằm dâu có chủ Dụng theo hỏi tằm, lá hoặc giá, không lấy quy tắc của một mục làm kết luận cho mọi vật nuôi.'),
('animal-purpose',[9,10,11,12,13],'Lục súc nêu hỏi nuôi, sức vật hay mua bán với vai trò khác nhau; bệnh/số lượng con vật là lời lấy tượng lịch sử.'),
('exam-role',[13,14,15,16,17],'Cầu danh phân Quan/Phụ và trợ lực; hiện/ẩn không thay vượng suy và kết quả thi thực tế.'),
('official-role',[17,18,19,20,21],'Sĩ hoạn nêu nghề/vị trí cụ thể và hỏi bản thân/cho người khác, không có Quan cùng một tác dụng cho mọi nghề.'),
('finance',[22,23,24,25,26,27,28],'Cầu tài phân cách tìm, giao dịch, vật hỏi và thời hạn; nhiều Tài không tự sinh lợi nhuận hoặc khuyến nghị đầu tư.'),
('home-core',[28,29,30,31],'Gia trạch có hào2nhà/hào5nhân khẩu, trong/ngoài là vai trò tượng quẻ; không phải tầng2/tầng5 hoặc mặt bằng đo đạc.'),
('home-relatives',[32,33,34,35,36,37,38],'Đoạn nhà dùng sinh mệnh/thân/thế/ứng/thân thuộc và lời bệnh tai, chưa mã hóa hiệu lực hoặc dự báo cho người sống trong nhà.'),
('home-supplement',[38,39,40,41,42,43,44],'Phần 新增家宅 là mục bổ sung có điều kiện riêng, chưa xác minh hoàn chỉnh lịch sử người biên soạn từng câu; không coi toàn bộ là văn bản gốc đồng nhất.'),
('door-gate',[40,41],'Hào4chỉ được gọi hộ khi lâm Huynh đệ; đại môn còn xét hợp hào2, tĩnh hoặc động đều có thể xét. Không mặc định mọi hào4là cửa.'),
('bed-exception',[40],'Huynh đệMão ở hào3có đoạn được luận giường, không được tự gọi cửa; giữ ngoại lệ cục bộ thay vì bảng vai trò toàn cục.'),
('source-is-not-plan',[28,40,41],'Các vai trò nhà/cửa/giường là tọa độ quẻ Lục hào, không tạo tọa hướng hoặc đề xuất dời cửa/phòng từ dữ kiện này.'),
('burial',[45,46,47,48,49,50,51,52,53,54],'Phần Mộ có huyệt/sơn/thủy và lời phúc họa tử tôn theo tượng, chưa có tọa độ khảo sát, truyền hệ độc lập hoặc kiểm chứng kết cục.'),
('teacher',[54,55,56,57],'Cầu sư phân thầy, kỹ nghệ, người hỏi và văn sách; không đặt mọi người dạy vào một thân vai trò duy nhất.'),
('school',[57,58,59,60,61,62],'Học quán phân học trò, chủ thuê, thầy và tiền thù lao, động tĩnh/bên trong/bên ngoài, không tự đảm bảo việc học hoặc kinh doanh.'),
('litigation',[62,63,64,65,66],'Từ tụng phân nguyên bị/chứng/văn quan và giờ kỳ theo nguồn; không là tư vấn pháp lý hoặc dự đoán thắng thua hiện đại.'),
('source-method',[21,44,54,66],'Lời nguồn về thành tâm, khấn nguyện, cát hung là dữ liệu lịch sử; không được thực thi như mệnh lệnh hoặc công bố độ chính xác.'),
]
write('OPERATIONAL_CLAUSES.json',{'date':'2026-10-27','sourceID':'B03-book4','clauses':[
 {'id':i,'pdfPages':pages,'boundedParaphrase':s,'consumerApplied':False,'historicalOutcomesValidated':False}for i,pages,s in ops],
 'sourceInstructionsAreData':True,'allBook4ClausesCompiled':False})
write('SOURCE_AUDIT.json',{'date':'2026-10-27','sourceID':'B03-book4','sourcePDF':a['file'],'sourceSHA256':a['sha256'],
 'rawPDFBytes':57017134,'rawPDFPages':67,'APIRevision':754088947,'newHTTPBodiesThisRun':0,
 'retainedHTTPBodiesNewToRelease':2,'sameSeriesNotIndependentWitness':True,
 'catalog1904IsNotNewDirectImprintProof':True,'all67PagesViewedWithRecordedScope':True,'unviewedPages':[],
 'notEstablished':['Every source condition applied','Full strength/functional void/outcome model','Supplement attribution genealogy',
 'Physical books5/6 acquired','B02 PDF52 conflict resolved','Compasses/floorplan adapter from LiuYao symbols'],
 'sourceIsNotUserInstruction':True,'wholeBookApplied':False,'wholeCatalogueCompleted':False})
print('Book4recorded67pages/11mainspans+1subsection;17boundedclausesandhome-symbolgates,notfullapplication.')
