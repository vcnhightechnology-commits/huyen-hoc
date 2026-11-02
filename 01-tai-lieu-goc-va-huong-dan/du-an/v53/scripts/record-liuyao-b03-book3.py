from pathlib import Path
from hashlib import sha256
import json
root=Path(__file__).resolve().parent.parent;base=root/'research/liuyao-b03-book3';prior=root/'research/liuyao-b03-volume5'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
def write(n,d):(base/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
a=read(prior/'ACQUISITION.json');assert sha(prior/a['file'])==a['sha256']=='01859340e519ffb68a1f40996af73aa7f40beb10a723a7a2a070985201874c61'
topics={1:'Cover only',8:'Expanded timing paragraph: 如旬空候出旬; summary 空出旬; no motion premise in this bounded clause',
19:'Expanded beginning of 身命',20:'Expanded personal question roles and strength qualifications',
21:'Expanded personal historical interpretation',22:'Expanded life horizons and attributed quotation, distinct from author endorsement',
23:'Expanded personal/family narratives',24:'Expanded family counts with strength qualifications',25:'Expanded changed kin and 世/應/身 distinctions',
26:'身命: spirits, moral/social historical assertions, transformation and support',27:'身命: historical role cases, 子孫 condition and 生扶',
28:'身命: historical childhood/education and stage/void claims',29:'身命: study/career stories and 官/父 qualifications',
30:'身命 final support/kin paragraphs; explicit 卜筮正宗卷之五終',
31:'卷之六 title, 婚姻 begins',32:'Marriage: 世應/財官 roles, combinations/clashes, changing question and context',
33:'Marriage: transformed void, intermediaries, multiple relatives and motion',34:'Marriage: subject-specific kin, void and relative 世應',
35:'Marriage: strength/phase and attributed 本命 claims, not a Bazi adapter',36:'Marriage: documents, two candidates, intermediary and source timing',
37:'Marriage: intermediary inner lines and role/purpose',38:'Marriage section ending explicitly covers male asking female and female asking male; 產育 begins',
39:'Birth divination: hidden child, twin and fetal claims, mother/child roles',40:'Birth divination: motion, void and support qualifications',
41:'Birth divination: rescue/support, selected role and alternatives',42:'Birth divination: hidden/visible胎爻 and timing exceptions',
43:'Birth divination: nursing/delivery helper roles and question distinctions',44:'Birth section ending; 進人口 begins with role-specific subject selection',
45:'進人口: subject motion, documents and service context',46:'進人口: 主客, document/intermediary/relative roles and motion',
47:'進人口: intermediaries, changing branches/kin and contract; no generic 文書 fallback',
48:'進人口 final paragraph; explicit 卜筮正宗卷之六終',49:'卷之七 title, 病症 begins: historical organ/symptom classifications',
50:'Symptoms: old/new illness, spirits and hidden/visible relations',51:'Symptoms: transformed kin, inner/outer and motion',
52:'Symptoms: organ/line/branch associations, historical not clinical',53:'Symptoms: tomb/void and recurrence, source conditions',
54:'病症 ends; 病體 begins with relative-specific use-god selection',55:'病體: life/death assertions, rescue and horizon',
56:'病體: rescue, dynamic changes and caller/source subject',57:'病體: hidden/visible layers and medical assertions',
58:'病體 final caveat against fixed reading; 醫藥 begins',59:'醫藥: disease/treatment/physician roles, transformed relationships',
60:'醫藥: absent 官/relative roles and historical prescriptions',61:'醫藥: historical food/drug/五行 assertions',
62:'醫藥 ending, explicit request sincerity in source; not user instructions',63:'鬼神 begins: historical ritual and spirit taxonomy',
64:'鬼神: branch/element/position ritual associations',65:'鬼神: transformed kin, images and ritual interpretation',
66:'鬼神 final paragraph, explicit 卜筮正宗卷之七終',67:'Final cover only'}
pages=[1,8]+list(range(19,68));records=[]
for n in pages:
 new=n==1 or n>=26
 image=f'images/bushi-book3-{n}.png' if new else f'../liuyao-b03-volume5/images/bushi-book3-{n}.png'
 records.append({'pdfPage':n,'image':image,'sha256':sha(base/image),'topic':topics[n],
  'newLocalRender':new,'expandedEarlierReading':not new,'scope':'cover-only' if n in [1,67] else 'first-pass-complete-relevant-span' if new else 'expanded-earlier-reading',
  'entirePageDiplomaticallyTranscribed':False})
write('MANUAL_READINGS.json',{'date':'2026-10-27','sourceID':'B03-book3','sourcePDF':'../liuyao-b03-volume5/'+a['file'],
 'sourceSHA256':a['sha256'],'records':records,'counts':{'manualRecords':51,'newLocalRenders':43,
 'newContentPages':41,'coverPages':2,'expandedEarlierContentPages':8,'QAOnlyRenders':2,
 'physicalBookContentPagesNowFirstPassViewed':65,'physicalBookAllPagesViewedByRecordedScope':67},
 'inheritedFirstPassPages':list(range(2,26)),
 'qaImages':[{'image':'images/void-timing-p8-qa.png','sha256':sha(base/'images/void-timing-p8-qa.png'),
 'pdfPage':8,'dpi':360,'cropPixels':[220,250,2000,1560],'purpose':'Read exact raw-xun exit clause; no moving/static qualification in this bounded sentence.'},
 {'image':'images/marriage-context-p38-qa.png','sha256':sha(base/'images/marriage-context-p38-qa.png'),
 'pdfPage':38,'dpi':360,'cropPixels':[1300,180,1000,1690],'purpose':'Correct bounded reading: 男卜女婚女卜男婚, both question directions; other relationship roles are qualified.'}],
 'directBoundaries':[{'pdfPage':30,'reading':'卜筮正宗卷之五終'},{'pdfPage':31,'reading':'卜筮正宗卷之六'},
 {'pdfPage':48,'reading':'卜筮正宗卷之六終'},{'pdfPage':49,'reading':'卜筮正宗卷之七'},{'pdfPage':66,'reading':'卜筮正宗卷之七終'}],
 'ocrUsed':False,'unviewedPhysicalBookPages':[],'newHTTPBodies':0,'newOriginalPDFs':0,
 'allSourceClausesApplied':False,'entireBookApplied':False})
units=[(5,'天時',2,8),(5,'年時',8,13),(5,'國朝',13,16),(5,'征戰',16,19),(5,'身命',19,30),
 (6,'婚姻',31,38),(6,'產育',38,44),(6,'進人口',44,48),
 (7,'病症',49,54),(7,'病體',54,58),(7,'醫藥',58,62),(7,'鬼神',63,66)]
write('BOOK3_CURRENT_UNITS.json',{'date':'2026-10-27','sourceID':'B03-book3','units':[
 {'textualVolume':v,'heading':h,'pdfPages':list(range(lo,hi+1)),'relevantSpanFirstPassRead':True,
  'entireUnitApplied':False,'inheritedCompleteSpan':hi<=19,'newSpanOrExpandedToEnding':hi>19} for v,h,lo,hi in units],
 'counts':{'registeredUnits':12,'firstPassRelevantSpanReadUnits':12,'previouslyCompleteSpanUnits':4,
 'newOrCompletedSpanUnits':8,'entireUnitApplied':0,'textualVolumesFirstPassRelevantSpans':3},
 'covers':[1,67],'overlapBoundaryPagesAreNotAdditionalUniquePages':True,
 'allPhysicalBookPagesViewedWithScope':True,'allClausesApplied':False,'all14TextualVolumesApplied':False})
ops=[
('body-final',list(range(26,31)),'Thân mệnh có các lời luận xã hội, đạo đức, thời nhỏ và học hành; điều kiện hào/Dụng/vượng suy cần tách khỏi lời phán đã gắn với sử truyện.'),
('body-ending',[30],'Nguồn tách vinh khô trong sáu thân với phép hỏi thọ yểu riêng. Không suy ra toàn bộ đời người từ một cờ hiện/ẩn/không.'),
('marriage-domain',[31,38],'Cuối phần Hôn nhân ghi cả nam hỏi nữ và nữ hỏi nam, rồi yêu cầu phân biệt những quan hệ như chọn dâu/rể, gả em hoặc lấy chị dâu. Không rút thành chỉ nam hỏi hoặc mặc định nam=Thế/nữ=Ứng cho mọi người.'),
('marriage-combine',[32,33],'Sinh hợp, lục hợp/lục xung, quẻ biến không và Thế/Ứng phụ thuộc câu hỏi và thứ tự; quan hệ hình thức chưa là kết quả hôn nhân.'),
('marriage-subject',[34],'Cùng mục hôn nhân, hỏi cho cha/con/anh em phải xét đối tượng khác; nguồn phản đối phát biểu một câu bao hết các đối tượng.'),
('marriage-premises',[35,36],'Bản mệnh, trường sinh, nhiều Tài/Quan, văn thư và hào động được luận riêng; không nhập bản mệnh ở đây thành thuật toán Bát tự.'),
('marriage-intermediary',[36,37],'Nguồn có lúc xét Ứng và hai hào gian cho người môi giới theo vai trò cụ thể; không đặt vĩnh viễn mọi hào gian là môi giới.'),
('birth-subject',[38,39],'Sinh nở hỏi vợ, thai và con chọn vai trò khác nhau. Sinh đôi/nam nữ/khó sinh là lời bói lịch sử, chưa có hiệu lực lâm sàng được xác minh.'),
('birth-horizon',[40,41,42],'Mộ/không/hợp/xung có sinh phù, nguyệt nhật, động tĩnh và kỳ hạn riêng. Không phát ngày sinh hay tiên lượng từ một tọa độ lịch.'),
('birth-nursing',[43,44],'Đoạn hỏi bà đỡ/vú nuôi tách chủ Dụng khỏi hào gian thay vì suy một chủ thể cho mọi câu hỏi.'),
('household-new-person',[44,45],'Tiến nhân khẩu yêu cầu phân biệt thuê người, nhận nuôi hoặc quan hệ đã biết; chọn Dụng theo thân phận và quan hệ, chưa phải bộ dự báo độ tin cậy nhân sự.'),
('contract-context',[46,47,48],'Phụ mẫu/văn thư, người làm chứng, chủ khách và người môi giới có điều kiện; thiếu hào hiện không tự suy hợp đồng không tồn tại trong đời thật.'),
('symptom-taxonomy',list(range(49,55)),'Bệnh chứng gắn ngũ hành, lục thần, hào và chi với bộ phận/triệu chứng theo y bốc cổ. Lưu như lịch sử, không dùng để chẩn đoán hoặc khuyên điều trị.'),
('health-relative',[54],'Đầu Bệnh thể nêu hỏi cha/mẹ, vợ và người khác theo chủ Dụng riêng. Tên Quan quỷ trong đoạn bệnh chứng không tự thay chủ Dụng thân thuộc.'),
('health-qualifiers',[55,56,57,58],'Các lời luận sinh tử, mộ tuyệt và cứu trợ còn thiếu kiểm chứng kết cục độc lập; phần cuối còn yêu cầu không đọc cố định một câu.'),
('medical-separate',[58,59,60],'Y dược phân thuốc, thầy thuốc, người bệnh và nguyên nhân theo cách riêng của nguồn, đồng thời nhắc hiệu lực của Nguyên/Kỵ; không chuyển thành tư vấn y tế.'),
('medical-claims',[60,61,62],'Chỉ dẫn vị thuốc, thức ăn, ngũ hành và lời cầu nguyện/thành tâm là nội dung nguồn, không phải yêu cầu của người dùng hoặc bằng chứng hiệu quả thuốc.'),
('ritual-taxonomy',[63,64,65,66],'Quỷ thần là hệ lấy tượng/khấn lễ lịch sử. Phân thân/sinh/biến và quan hệ theo nguồn, không khẳng định có sự kiện siêu nhiên được kiểm chứng.'),
('xun-exit',[8],'Câu như tuần không chờ ra tuần được giữ thành tọa độ ra khỏi tuần hiện hành; câu giới hạn này không tự quy định động hay tĩnh, không giải quyết chân không/vượng suy hoặc ứng nghiệm.'),
('xun-horizon-not-event',[8],'Không ra tuần thuộc đoạn ứng kỳ có tiền đề và gần/xa/giờ/ngày/tháng. Tọa độ đầu tuần kế không là ngày sự kiện chắc chắn; thiếu ngày can chi giữ chưa rõ.'),
]
write('OPERATIONAL_CLAUSES.json',{'date':'2026-10-27','sourceID':'B03-book3','clauses':[
 {'id':i,'pdfPages':p,'boundedParaphrase':s,'consumerApplied':False,'historicalOutcomesValidated':False} for i,p,s in ops],
 'sourceInstructionsAreData':True,'historicalMedicalClaimsNotClinicalAdvice':True,
 'allBook3ClausesCompiled':False})
write('XUN_EXIT_CLAUSE.json',{'date':'2026-10-27','sourceID':'B03-book3','pdfPage':8,
 'boundedReading':'如旬空候出旬之日應事','summaryReading':'空出旬',
 'motionQualifierInThisBoundedSentence':None,
 'implemented':'Raw selected primary branch and 60-cycle day coordinate only; next xun boundary at 10-positionWithinXun.',
 'inferredCoordinateFormulaIsNotPrintedNumericalAlgorithm':True,
 'notImplemented':['Functional void and strength','All exceptions and relative source priority','Exact Gregorian instant',
 'Day/hour/month horizon selection','Prediction of weather, health, marriage or lifespan'],
 'effectiveSourceConclusionApplied':False,'consumerApplied':False})
write('SOURCE_AUDIT.json',{'date':'2026-10-27','sourceID':'B03-book3','sourcePDF':'../liuyao-b03-volume5/'+a['file'],
 'sourceSHA256':a['sha256'],'acquisitionRecord':'../liuyao-b03-volume5/ACQUISITION.json',
 'requestRecord':'../liuyao-b03-volume5/REQUESTS.json','newHTTPBodies':0,'newOriginalPDFs':0,
 'rawMetadataIsNotAdditionalDirectImprintProof':True,'sameSeriesNotIndependentWitness':True,
 'all67PagesViewedWithRecordedScopes':True,'unviewedPages':[],
 'newOrCompletedSectionSpans':['身命','婚姻','產育','進人口','病症','病體','醫藥','鬼神'],
 'notEstablished':['Every source clause operationalized','Source outcome validation','Full xun/strength/void/timing adjudication',
 'Physical books4..6 retained/read','Independent edition genealogy','B02PDF52date-void conflict resolved'],
 'sourceIsNotUserInstruction':True,'wholeBookApplied':False,'wholeCatalogueCompleted':False})
print('Recorded43newrenders/8expandedreadings;12sectionspansfirst-pass/0entireunitsapplied;20boundedclauses;2QAimagesincludingmarriagedomaincorrection.')
