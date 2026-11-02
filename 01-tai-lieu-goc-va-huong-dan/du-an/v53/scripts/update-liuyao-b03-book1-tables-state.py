from pathlib import Path
import json
root=Path(__file__).resolve().parent.parent;w=root.parent;base=root/'research/liuyao-b03-book1-tables'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='LIUYAO_B03_BOOK1_TABLES_REPORT.md';e=read(root/'qa/liuyao-b03-book1-tables/ENGINE_RESULTS.json')
assert len(e['checks'])==8 and all(c['ok']for c in e['checks'])
step=('Sách1 B03: đã khép lượt đọc có giới hạn phần đầu/quyển1 PDF1–33, 33bản ghi/32nội dung/1bìa, '
 '19trang pending và14trang mở rộng, 7renderQA/12crop;57nhóm biên tập, không phải57mục áp hết. '
 'Giữ quán danh吳郡張景松/niên款 và các giọng敘/凡例 riêng; mục lục ghi18hỏiđáp/131ví dụ, chưa đếm đủ quẻ thân sách. '
 'Bảng Nạp âm60tọa độ có60hành khớp,58tên sauchuẩn hóa,甲申/乙酉giữ井泉水 khác泉中水. '
 'Can tháng/can giờ có hai bộ tọa độ riêng, 20neo can đơn trực tiếp/220ô khai triển;8kiểm đạt,240HHC BátTự+300lunar thật. '
 'Định giờ theo mùa/ranh tháng-năm/Tý muộn chưa được hai câu nguồn xác lập. '
 'KhôngHTTP/PDF gốc mới; HTML707411byte/site/ZIPweb và14thamchiếu trước nguyênbyte. '
 'Cả60ảnh sách1 đã xem theo các phạmvi kết hợp nhưng chưa384chúhào/mọi mệnhđề/14quyển hoặc kho40nguồn.')
nexts=[
 'Book1opening/volume1PDF1..33boundedfirstpassnowrecorded;all60physicalimagesviewedbycombinedscopes,notallclauses/384lineannotations. Collate all64printedfigure line branches/kin/shi-ying/hidden and disputed headings before using them as complete fixtures.',
 'Book6TOCstates131examples,notindependentlycountedbodyfigures. Only2printedstructuresverified;continue actualcast/date/premise transcription across18questions,notclaimhistoricaloutcomevalidation.',
 'Month/hour adapters accept confirmedyear/daystem andbranch only;year/monthdayboundaries,23h/lateZiandseasonalwatchverse remain separate. Preserve井泉水/泉中水 lexicalvariant and prefacerulevoices;independentgenealogy/witnessnotestablished.',
 'Source-specific strength/functionalvoid/triadcompletion/timing/supportefficacy,book5boatwording andbook6finalendingremain. B02has136units/103heading-onlybodies/26firstpassspans/0fullunits,PDF52date-voidconflictopen. ContinueMaiHoa/Bazi/Tuvi/Homeand40-sourcecatalogue.'
]
write(base/'WORK_STATE.json',{'date':'2026-10-27','status':'opening-volume1-bounded-read-and-private-table-coordinates-complete-full-clauses-active',
 'sourceID':'B03-book1','latestReport':'v53/'+report,'completedStep':step,'privateReference':'stem-coordinate-reference.mjs',
 'unitMap':'BOOK1_OPENING_UNITS.json','all60PhysicalImagesViewedByCombinedBoundedScopes':True,'all384LineAnnotationsCollated':False,
 'allSourceClausesApplied':False,'TOCStatedExamples':131,'bodyExampleCountIndependentlyEstablished':False,
 'newHTTPBodiesThisRun':0,'newOriginalPDFsToRelease':0,'consumerChanged':False,'summary':e['summary'],
 'next':nexts,'wholeBookApplied':False,'wholeCatalogueCompleted':False})
d=read(w/'EXHAUSTIVE_WORK_STATE.json');d['currentWork'].update(currentStep=step,latestResearchReport='v53/'+report,
 sourceDirectory='v53/research/liuyao-b03-book1-tables',internalB03StemCoordinateReference='v53/research/liuyao-b03-book1-tables/stem-coordinate-reference.mjs',
 currentB03Book1OpeningMap='v53/research/liuyao-b03-book1-tables/BOOK1_OPENING_UNITS.json',functionalBacklog='v53/research/liuyao-b03-book1-tables/WORK_STATE.json')
d['currentWork']['sourceLimits']='All6same-seriesB03PDFsretained,notindependentwitnesses. Allbook1physicalimagesviewedbyboundedscopes,not384annotations/fullclauses. TOC131examplesnotbody-countor131checkedfigures. StemcoordinateformulasdonotestablishGregorian/lunaryear-monthboundariesorlateZi/seasonalclock. B02PDF52/boatwording/independentgenealogy/strength/void/timing/all40sourcesremain.'
d['currentWork']['nextSourceLead']={'status':'book1-opening-volume1-covered-by-bounded-read-private-tables-checked',
 'sourceID':'B03-book1','file':'v53/research/liuyao-foundations/NLC892-GBZX0301013045-259368.pdf',
 'sha256':'5dcd7b5005b1e86f441a9350eefb7c0e9e628c47ab926b2a7d1bdd6691a4773d','bytes':50191031,
 'remaining':'384annotations/64figures,allsourceclauses;book6actualbodyexamplesbeyond2;independentwitnessesandothercataloguegaps.'}
d['inProgressScope']='v53/research/liuyao-b03-book1-tables/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in[w/'EXHAUSTIVE_WORK_STATE.json',root/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=root/'research/full-study/WORK_STATE.json';d=read(p);d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts)
yi=next(x for x in d['items']if x['id']=='yi');entry=('B03book1opening/volume1PDF1..33boundedread,57editorialgroups/12QA;all60physicalimagesviewedbycombinedscopes,not384annotations. '
 '8checks240actualHHCBazi+300Lunar;60nayin/120monthstem/120hourstemcoordinates,2lexicalvariantsretained. '
 'TOC131examplesnotbodycount;clockboundaries/genealogyunresolved. Consumer/14priorreferencesunchanged.')
if entry not in yi['completed']:yi['completed'].append(entry)
yi['latestScope']='../liuyao-b03-book1-tables/BOOK1_OPENING_UNITS.json'
yi['remaining']=[x for x in yi['remaining']if not x.startswith('LiuYaoB03:all6same-seriesPDFsretained;book1prefaces/')]
yi['remaining'].append('LiuYaoB03:all6same-seriesPDFsretained/book1all60physicalimagesboundedviewed;384annotations/allclauses/actualbodyfiguresbeyond2/strength/void/timing/clockboundaries/genealogy/boatwording/book6endingremain. B02PDF52and103heading-onlyunitsopen.')
write(p,d)
p=root/'research/library-current/COVERAGE.json';d=read(p);b=next(x for x in d['catalogue']if x['id']=='B03')
b['scope']='Giữ6PDF cùng bộ, không nhânchứng độc lập. Sách1:1–33khép lượt đọc có giới hạn, cả60ảnh đã xem qua các phạmvi kết hợp;57nhóm đầu/quyển1 chưa áp hết. Bảng60Nạpâm/120cantháng/120cangiờ đã đối engine thật; giữ2khácnhãn/ranhgiờ-lịch chưa xáclập. Chưa384chúhào/mọi mệnhđề;18hỏiđáp có131vídụ ghiởmục lục, mới2quẻinđối cấu trúc.'
b['latestLocalReadingScope']='33bản ghi/32nội dung/1bìa/7renderQA12crop;57nhóm biên tập. 8kiểm240HHC BátTự+300lunar thật;20neo can đơn trực tiếp và220tọa độ khai triển. KhôngHTTP/PDFgốc mới, chưaáp hết.'
for f in ['v53/'+report]+['v53/research/liuyao-b03-book1-tables/'+n for n in ['SOURCE_AUDIT.json','MANUAL_READINGS.json','BOOK1_OPENING_UNITS.json','NAYIN_ROWS.json','STEM_ANCHORS.json','TOC_PRINTED_EXAMPLE_COUNTS.json','EDITION_VOICE_LEADS.json','OPERATIONAL_CLAUSES.json','stem-coordinate-reference.mjs']]+['v53/qa/liuyao-b03-book1-tables/ENGINE_RESULTS.json']:
 if f not in b['currentEvidence']:b['currentEvidence'].append(f)
d['latestFollowup']=report+':Book1opening/volume1boundedread/privatecoordinates8checks240HHC+300Lunar;all60physicalimagesviewednot384annotations/fullclauses. Wholework0,consumerunchanged.'
d['latestAcquisitionCounts']={'scope':report,'newOriginalPDFsToRelease':0,'retainedHTTPBodiesNewToRelease':0,'newHTTPBodiesThisRun':0,
 'manualRecords':33,'contentPages':32,'coverPages':1,'inheritedPendingPages':19,'expandedBodyPages':14,
 'QAOnlySourceRenders':7,'QACrops':12,'editorialUnitGroups':57,'fullBooksApplied':0}
d['counts']['newDownloadsThisScope']=0;d['counts']['newDownloadsThisScopeBasis']='Existing retained original reused;no new HTTP or original PDF.'
assert d['counts']['wholeWorkApplied']==0;write(p,d)
note='Mốc B03–Bảng sách1, 27/10/2026: `'+report+'`. '+step+'\n\n'
for p in[w/'PROJECT_RESEARCH_STATE.md',root/'NEXT_STEPS.md',root/'research/library-current/COVERAGE.md']:
 t=p.read_text(encoding='utf-8-sig')
 if t.startswith('Công việc tiếp sau B03–Sách6:'):t=t.split('\n\n',1)[1]
 if t.startswith('Mốc B03–Bảng sách1, 27/10/2026:'):t=t.split('\n\n',1)[1]
 p.write_text(note+t,encoding='utf-8')
write(w/'PENDING_RESEARCH_STATE.json',{'date':'2026-10-27','status':'book1-opening-tables-current-scope-active','sourceID':'B03-book1',
 'workDirectory':'v53/research/liuyao-b03-book1-tables','currentWorkState':'v53/research/liuyao-b03-book1-tables/WORK_STATE.json',
 'latestReport':'v53/'+report,'checks':'v53/qa/liuyao-b03-book1-tables/ENGINE_RESULTS.json',
 'next':nexts,'consumerChanged':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False})
(root/report).write_text('''# B03: phần đầu, quyển một và bảng can tháng/can giờ

Ngày 27/10/2026. Nguồn, bản đọc và tham chiếu riêng nằm ngoài site.

## Byte nguồn và phạm vi đọc

Tái dùng PDF sách đóng1 đã giữ từ phạm vi nền: **50.191.031 byte/60 trang**, SHA256 `5dcd7b5005b1e86f441a9350eefb7c0e9e628c47ab926b2a7d1bdd6691a4773d`. Không HTTP hoặc PDF gốc mới; không nhân đôi PDF. SHA xác định byte tại máy, không là chữ ký nhà xuất bản. Sách1–6 cùng bộ không là sáu nhân chứng độc lập.

Khép lượt đọc có giới hạn PDF1–33: 33bản ghi,32nội dung/1bìa;19trang pending và14trang20–33 mở rộng từ ảnh đã có. Bảy render QA360dpi cho12crop, không thêm trang nguồn. Có57nhóm biên tập gồm bìa/tiêu đề/tựa/mục lục/bảng/câu; không gọi là57đơn vị áp dụng hết. Quyển1 kết trực tiếp ở33: `卜筮正宗卷之一終`. Kết hợp các phạm vi cũ, cả60ảnh vật lý sách1 đã được xem có giới hạn; **chưa chép ngoại giao toàn trang, chưa đối hết384chúhào hoặc áp hết mọi mệnh đề**.

## Tựa, mục lục và các lớp chứng cứ

Trang2 ghi `光緒甲辰新鐫 / 王洪緒輯 / 文成堂存板`; trang5 ghi `康熙己丑歲冬十月吳郡張景松書於蓉江草堂`; trang6–7 là lời tự thuật về thầy 新安楊廣含 và18hỏiđáp; trang15 có dạng tên 王維德洪緒輯. Giữ từng giọng và năm literal. Sửa nháp chưa phát hành 安郡 thành **吳郡** sau QA; không chuyển năm sang Gregory hoặc nhận đã xác minh độc lập phả hệ/đồng nhất mọi giọng.

Mục lục13–14 ghi số ví dụ cho18câu:5/11/4/12/5/4/14/7/6/5/8/13/11/4/7/4/5/6, tổng **131**. Đây là tổng số **sách tự ghi ở mục lục**, chưa là đếm đủ sơ đồ thân sách hoặc131quẻ đã chạy engine. Bản phát hành trước mới kiểm cấu trúc hai quẻ in ở đầu sách6; không tăng con số này bằng bảng hoặc tọa độ dựng riêng.

Các đoạn đạo đức, nghi lễ, trị bệnh, sự kiện nghiệm thuật và phê nguồn giữ là dữ liệu lịch sử của sách; không là chỉ thị người dùng hoặc chứng minh kết cục thực tế. Khung 卦身 của B03 vẫn riêng với lập trường B02. Mười mệnh đề có giới hạn nằm trong `OPERATIONAL_CLAUSES.json`; mọi điều kiện phụ chưa hoàn tất.

## Ba bảng có thể thực thi

Trang17:30cặp Nạp âm/60can chi. Đọc QA giữ **白蠟金**, **覆燈火**. Sáu mươi tọa độ đều khớp hành với lunar-typescript1.8.6;58tên khớp sau phép đổi chữ phồn–giản được ghi tường minh. Hai tọa độ **甲申/乙酉** giữ nguồn **井泉水**, runtime **泉中水**. Đây là khác tên; chưa chứng minh lỗi tính hoặc tương đương qua các nhân chứng lịch sử.

Trang24 `年上起月法`: năm 甲己 khởi 丙寅,乙庚戊寅,丙辛庚寅,丁壬壬寅,戊癸甲寅 rồi thuận hành. Trang25 `日上起時法`: ngày 甲己 khởi 甲子,乙庚丙子,丙辛戊子,丁壬庚子,戊癸壬子 rồi thuận hành. Có mười neo theo **cặp** in trực tiếp; khi tách từng can là20neo đơn,220tọa độ còn lại do biên tập khai triển theo quy tắc thuận hành. Không gọi240ô đều được in thành bảng đầy đủ trong sách.

`stem-coordinate-reference.mjs` cung cấp hai hàm riêng: **can năm + chi tháng đã xác nhận → can tháng**; **can ngày + chi giờ đã xác nhận → can giờ**. Đầu vào không nhận số tháng âm, giờ đồng hồ, múi giờ hoặc sức mạnh. Không tự chọn ranh Tết/Lập Xuân/tiết khí, đổi ngày lúc23h, Tý muộn hoặc thời gian chân thái dương. `定寅時法` trang25 có bối cảnh mùa/canh/điểm; chưa có căn cứ quy đổi đủ sang giờ dân dụng hiện đại, nên chưa thêm bộ quy đổi.

## Kiểm thực thi và bảo toàn

**8kiểm đạt**, với **240lời gọi HHC BátTự thật +300lunar thật**:120tọa độ can năm–chi tháng,120tọa độ can ngày–chi giờ,60Nạp âm. Kiểm tháng dùng ngày15trưa trong mười năm2000–2009; kiểm giờ dùng mười ngày1–10/1/2026 tại12chi với phút30, tránh23h. Nạp âm dùng60ngày liên tiếp lúc trưa chỉ để duyệt vòng canchi. Đây là bộ ca hữu hạn kiểm các tọa độ, không dựng ngày cổ hoặc chứng minh các quy ước lịch ở ranh. HHC và lunar có phụ thuộc liên quan, không gọi là hai nguồn học thuật độc lập. Tọa độ tháng/giờ đầu vào được xác nhận từ lịch thật chỉ phục vụ đối chiếu; bộ nguồn không trở thành adapter lịch.

Đủ120cặp đầu vào độc nhất ở mỗi bảng, khớp cột canchi của HHC và lunar; phiên bản/runtime giữ hash. Kiểm sai đầu vào/khóa thừa, bảo toàn đầu vào và14thamchiếu Lục hào trước. Ca và digest ở `qa/liuyao-b03-book1-tables/`. Không lặp4096bộ quẻ khi logic Nạp Giáp không thay đổi.

HTML độc lập/root/site giữ **707411byte**, SHA256 `549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`; ZIPweb giữ344047byte. Snapshot trước `archives/v53-before-liuyao-b03-book1-tables/` giữ sourceZIP1899259205byte và2688tệp manifest. Kiểm toàn byte manifest/sourceZIP nằm trong `RELEASE_RESULTS.json`; không phát hành mạng.

Tiếp đối đủ64hình/384chúhào và quẻ/ngày/tiền đề thân18hỏiđáp; mạnh yếu/chân không/ứng kỳ/hiệu lực sinh cứu vẫn mở. Chữ thuyền sách5, kết cuối sách6 và nhân chứng độc lập/phả hệ chưa giải quyết. B02 vẫn136đơn vị/103thân mục mức đềmục/26khoảng đọc lầnđầu; ngày–tuầnkhông52mâu thuẫn. **0toàn sách được nhận đã áp hết; kho40nguồn/bốn hướng còn đang làm.**
''',encoding='utf-8')
print('Book1opening/tables checkpoint recorded;wholecatalogue remains active.')
