from pathlib import Path
import json
root=Path(__file__).resolve().parent.parent;w=root.parent;base=root/'research/liuyao-progress-conditions'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='LIUYAO_PROGRESS_CONDITIONS_REPORT.md';e=read(root/'qa/liuyao-progress-conditions/ENGINE_RESULTS.json');s=e['summary']
assert len(e['checks'])==14 and all(c['ok']for c in e['checks'])
step=('B02 chương29–33 đã đọc lần đầu đủ khoảng PDF116–138; 24 bản ghi gồm23 trang nội dung/1 quảng cáo, '
 '11 trang pending và13 trang mới trong nhịp này; thêm trang mục lục14 đọc mở rộng, 7 renderQA/8 ảnh. '
 'Ma trận hiện hành136 đơn vị/98 thân mục còn đề mục/31 khoảng đọc lần đầu/0 đơn vị áp hết. '
 'Bộ riêng giữ8 mệnh đề tiến–thoái theo tiền đề tường minh và lớp lời bình ngoại lệ riêng; nhận diện độc phát/độc tĩnh không bỏ Dụng. '
 'Tọa độ sao giữ mâu thuẫn庚 ngay trang136 và4 can Lộc chưa thấy trong sáu dòng in. '
 '14 kiểm đạt:4HHC thật cho2 quẻ in,10lunar thật so6 Lộc khớp/4 ô nguồn còn thiếu;64 mẫu động. '
 'Đầu mục兩現 in31 khác mục lục32; sửa vị trí quyển của chương33 trong bản đồ địa phương3→2 sau đối mục lục/thân sách. '
 'Không HTTP/PDF gốc mới; HTML707411byte/site/ZIPweb và15 tham chiếu trước giữ byte. Toàn kho chưa hoàn tất.')
nexts=[
 'Current B02 unit map is research/liuyao-progress-conditions/B02_CURRENT_UNITS.json:136units/98heading-only/31firstpass/7partialfoundations/0fullunits. Chapters29..33 now firstpasscomplete;do not reread just to count. Sourcebody兩現134prints31 whileTOC14prints32;canonicalunit32retained. Chapter33localtocVolume3correctedto2afterTOC14/body136/end138audit,not a sourcevolumeconflict.',
 'Progression matcher preserves 野鶴 list/later李 commentary and inclusive 有一 overlap. Complete strength/functionalvoid/realcalendar/timing/use selection and later reconciliation before any final efficacy output. Tomb chapter30, multiple-use chapter32 and quoted易冒 statements remain only partially compiled;no clinical/historical outcome claims.',
 'Source nobleman庚 conflict136:verse午寅/proseexample丑未;keepambiguous,seek independentwitness. Salary source has6explicitstemrows,丁戊壬癸notfilledfromruntime. Stars/visiblemotiondo not decideoutcome. Verify remainingTOC/body volume divisions and source chapter34onward,withoutredownloadingPDF.',
 'B02PDF52辛卯/寅卯voidconflict remains. B03fullpolarity/gua-shen/prose/strength/void/timing/boatwording/ending and otherMaiHoa/Bazi/Tuvi/Home/40sourcegaps remain;0wholeworksapplied. Keepallcompletedpackages andprivateevidenceoutsideconsumer site.'
]
write(base/'WORK_STATE.json',{'date':'2026-10-27','status':'five-firstpass-spans-and-private-explicit-premise-components-complete-full-clauses-active',
 'sourceID':'B02-ch029-033','latestReport':'v53/'+report,'completedStep':step,'currentB02UnitMap':'B02_CURRENT_UNITS.json',
 'privateReferences':['progression-reference.mjs','star-coordinate-reference.mjs'],'firstPassChapterSpans':5,
 'allChapterClausesApplied':False,'noblemanGengConflictResolved':False,'missingFourSalaryRowsFilled':False,
 'chapter33LocalVolumeMappingCorrected':True,'summary':s,'next':nexts,'consumerChanged':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False})
d=read(w/'EXHAUSTIVE_WORK_STATE.json');d['currentWork'].update(currentStep=step,latestResearchReport='v53/'+report,
 sourceDirectory='v53/research/liuyao-progress-conditions',currentB02UnitMap='v53/research/liuyao-progress-conditions/B02_CURRENT_UNITS.json',
 internalProgressionReference='v53/research/liuyao-progress-conditions/progression-reference.mjs',functionalBacklog='v53/research/liuyao-progress-conditions/WORK_STATE.json')
d['currentWork']['sourceLimits']='B02chapters29..33firstpassread/privatecomponentspartial;notfullstrength/void/timing/oracle. 136units98heading-only31firstpass0full. 庚noblemanwithin-pageconflict/4missingLurootrows/printed兩現31vsTOC32remain. Localchapter33volumemapcorrectedto2,notasourceconflict. B02PDF52andB03allclauses/other40sourcegapsremain.'
d['currentWork']['nextSourceLead']={'status':'B02-ch029-033-firstpass-complete-fullconditions-and-laterunits-open','sourceID':'B02',
 'file':'v53/research/liuyao-foundations/NLC416-12jh005345-45344.pdf','bytes':11089308,
 'sha256':'caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa',
 'remaining':'IndependentGengnoblemanwitness/fullconditions/TOCvolumedivisions/chapter34onward andothercataloguegaps;noPDFredownload.'}
d['inProgressScope']='v53/research/liuyao-progress-conditions/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in[w/'EXHAUSTIVE_WORK_STATE.json',root/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=root/'research/full-study/WORK_STATE.json';d=read(p);d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts)
yi=next(x for x in d['items']if x['id']=='yi');entry=('B02chapters29..33fullfirstpassspans116..138,136units98heading-only31firstpass0full;19boundedclauses/explicitprogressionlayers/visiblemotion/partialstarcoordinates. '
 '14checks4actualHHC2printedcasts10Lunar6Lurootagreements4unfilled/64motionpatterns. 庚within-pageconflict/兩現printed31vsTOC32preserved;chapter33localvolumemap3→2corrected. Consumer/15priorrefsunchanged.')
if entry not in yi['completed']:yi['completed'].append(entry)
yi['latestScope']='../liuyao-progress-conditions/CHAPTER_SPANS.json'
yi['remaining'].append('LiuYaoB02 currentmap now136/98heading-only/31firstpass;chapters29..33notfullyapplied. Fullstrength/void/timing/quotedpositions/multipleuse/tomb/independent庚witness/TOCvolumesaudit/ch34onwardandPDF52remain.')
write(p,d)
p=root/'research/library-current/COVERAGE.json';d=read(p);b=next(x for x in d['catalogue']if x['id']=='B02')
b['scope']='Tham chiếu riêng cấu trúc/Phi Phục/Dụng/Nhật Nguyệt/Không–Động và8 mệnh đề tiến–thoái có tiền đề; độc phát/độc tĩnh và bảng sao giới hạn. Chỉ mục136,98 thân mục còn đề mục,31 khoảng đọc lần đầu,0 đơn vị áp hết. Giữ庚 mâu thuẫn cùng trang và4 ô Lộc chưa in rõ; chưa tổng vượng suy/chân không/ứng kỳ/chọn Dụng/dự báo công khai.'
b['latestLocalReadingScope']='Chương29–33/PDF116–138:23 nội dung+1quảng cáo139,1trangTOC14 mở rộng;7renderQA8ảnh/19mệnh đề.14kiểm4HHCthật(2quẻin)+10lunar/6Lộc khớp4nguồn thiếu;64mẫu động. Không HTTP/PDF mới; phần ứng dụng vẫn giới hạn.'
b['currentB02UnitMap']='v53/research/liuyao-progress-conditions/B02_CURRENT_UNITS.json'
for f in ['v53/'+report]+['v53/research/liuyao-progress-conditions/'+n for n in ['SOURCE_AUDIT.json','MANUAL_READINGS.json','CHAPTER_SPANS.json','B02_CURRENT_UNITS.json','STAR_COORDINATES.json','PRINTED_FIXTURES.json','OPERATIONAL_CLAUSES.json','progression-reference.mjs','star-coordinate-reference.mjs']]+['v53/qa/liuyao-progress-conditions/ENGINE_RESULTS.json']:
 if f not in b['currentEvidence']:b['currentEvidence'].append(f)
d['latestFollowup']=report+':B02fivefirstpassspans/currentmap136-98-31-0;14checks/4HHC10Lunar,sourceconditions/starambiguitypreserved. Wholework0/consumerunchanged.'
d['latestAcquisitionCounts']={'scope':report,'newOriginalPDFsToRelease':0,'retainedHTTPBodiesNewToRelease':0,'newHTTPBodiesThisRun':0,
 'manualRecords':24,'contentPages':23,'advertisementPages':1,'additionalTOCAuditReadings':1,'inheritedPendingPages':11,
 'newContentReadingsThisRun':12,'newAdvertisementReadingsThisRun':1,'QAOnlySourceRenders':7,'QAImages':8,'firstPassChapterSpans':5,'fullBooksApplied':0}
d['counts']['newDownloadsThisScope']=0;d['counts']['newDownloadsThisScopeBasis']='Existing original PDF/images reused;only local renders and source-coordinate work.'
assert d['counts']['wholeWorkApplied']==0;write(p,d)
note='Mốc B02–Điều kiện tiến thoái, 27/10/2026: `'+report+'`. '+step+'\n\n'
for p in[w/'PROJECT_RESEARCH_STATE.md',root/'NEXT_STEPS.md',root/'research/library-current/COVERAGE.md']:
 t=p.read_text(encoding='utf-8-sig')
 if t.startswith('Công việc tiếp sau B03–Nhãn hào:'):t=t.split('\n\n',1)[1]
 if t.startswith('Mốc B02–Điều kiện tiến thoái, 27/10/2026:'):t=t.split('\n\n',1)[1]
 p.write_text(note+t,encoding='utf-8')
write(w/'PENDING_RESEARCH_STATE.json',{'date':'2026-10-27','status':'B02-progress-conditions-current-scope-active','sourceID':'B02-ch029-033',
 'workDirectory':'v53/research/liuyao-progress-conditions','currentWorkState':'v53/research/liuyao-progress-conditions/WORK_STATE.json',
 'latestReport':'v53/'+report,'checks':'v53/qa/liuyao-progress-conditions/ENGINE_RESULTS.json','next':nexts,
 'consumerChanged':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False})
(root/report).write_text('''# B02: điều kiện tiến–thoái, độc phát và tọa độ sao theo nguồn

Ngày 27/10/2026. Bản đọc, nguồn và các bộ tham chiếu nằm ngoài site người dùng.

## Phạm vi và byte nguồn

Tái dùng PDF B02 đã xác thực trước: **11.089.308 byte / 394 trang**, SHA256 `caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa`. Không HTTP hoặc PDF gốc mới; SHA xác định byte tại máy, không là chữ ký nhà xuất bản. Cùng một ấn bản không được tính thành nhân chứng độc lập. Niên khoản tựa không tự chứng minh năm in.

Đọc lần đầu đủ khoảng năm chương: 29 Tiến thần–Thoái thần PDF116–124; 30 Tùy quỷ nhập mộ124–130; 31 Độc phát130–134; 32 Lưỡng hiện134–136; 33 Tinh sát136–138. Các trang giáp dùng chung không tính hai lần. Có24 bản ghi:23 nội dung và quảng cáo139;11 trang pending116–126, thêm12 nội dung127–138 và quảng cáo139. Trong phần pending có hai trang116/120 đã đọc giới hạn trước đó được mở rộng; chín trang còn lại là bản đọc pending chưa phát hành. Thêm mục lục14 đọc mở rộng để kiểm vị trí quyển. Bảy renderQA360dpi và một crop tạo8 ảnh, không thêm trang nguồn.

Cuối138 in trực tiếp `增刪卜易卷二終`. Thân mục Lưỡng hiện134 in **第三十一**, trong khi mục lục14 ghi **第三十二**; giữ hai trường, không đổi mã mục32 hoặc đếm thêm mục. Bản đồ địa phương cũ đặt chương33 ở quyển3; sau đối mục lục14 và thân136/kết138, bản đồ hiện hành sửa thành **quyển2**. Đây là sửa bản đồ địa phương, không gọi là mâu thuẫn giữa mục lục và thân sách.

`B02_CURRENT_UNITS.json` mới giữ136 đơn vị: **98 thân mục còn mức đề mục,31 khoảng đọc lần đầu,7 phần nền tảng đọc một phần,0 đơn vị nhận áp dụng hết**. Tệp lịch sử trước giữ nguyên. Đọc đủ khoảng chương không có nghĩa đã đối mọi quẻ/ngày/chú hoặc biên dịch hết mọi mệnh đề.

## Chức năng riêng đã hoàn thiện trong giới hạn tiền đề

`progression-reference.mjs` giữ tám cặp tiến và tám cặp thoái đọc tại116; chỉ xét chi gốc và chi tự biến thật của hào được người nghiên cứu chỉ định. Hào tĩnh không tự có biến. Tám mệnh đề ở123 được trả bằng logic ba giá trị: đúng/sai/chưa rõ. Vượng tương, hưu tù, Không, Phá, sinh phù và hỏi việc gần đều là tiền đề tường minh; không suy điểm sức mạnh hoặc lịch từ dữ liệu thiếu.

Danh sách mở bằng `野鶴曰` và lời bình sau mở bằng `李我平日` được giữ hai lớp. Có thể đồng thời khớp câu chờ điền thực và cảnh báo không phủ định tiến–thoái chỉ vì hào biến Không/Phá khi hào gốc lâm nhật nguyệt. Bộ không tự đặt thứ tự ghi đè. Cách hiểu “有一” bao hàm ít nhất một trường hợp là diễn giải biên tập được ghi rõ; hai mệnh đề có thể cùng khớp, không giả thành bốn nhóm loại trừ nhau. Chưa có phán quyết tiến–thoái hiệu lực, ngày ứng hoặc kết cục.

Hàm `visibleMotionPattern` nhận diện một hào **minh động** hoặc một hào tĩnh giữa năm hào minh động. Nó không suy ám động và không cho phép bỏ Dụng thần. Các câu trích từ 易冒 và lời phê về việc trọng động/khinh Dụng nằm riêng trong19 mệnh đề có giới hạn; không biến lời nguồn được trích thành một chỉ thị vô điều kiện của sách đang đọc. Chương30 phân biệt nhật mộ/động mộ/hóa mộ, Thế/thân/mệnh/Dụng và mạnh yếu; chương32 còn có ví dụ ngược thứ tự ưu tiên cổ pháp, nên chưa đưa thành bộ chọn Dụng duy nhất.

## Tọa độ sao và điểm chưa được phép điền

`star-coordinate-reference.mjs` nhận can ngày, chi ngày hoặc mùa đã xác nhận. Nó không chọn quy ước lịch, gán điểm cát hoặc dự báo.

Ngay trang136, ca quyết ghi **庚辛逢馬虎** (庚 theo 午/寅), nhưng ví dụ có can **庚** lại dùng **丑/未**. Chữ giữa甲 và庚 trong ví dụ còn hình dạng 戊/戌 chưa chốt; can庚 và hai chi丑未 đọc rõ. Hàm trả hai phương án theo lớp nguồn cho庚 và giữ lựa chọn hiệu lực `null`, không sửa một lớp cho khớp lớp kia. Chưa có nhân chứng độc lập giải quyết mâu thuẫn cùng trang.

Sáu dòng Lộc in rõ chỉ có **甲寅、乙卯、丙巳、己午、庚申、辛酉**. **丁、戊、壬、癸** không được điền từ bảng nhớ hoặc runtime vào trường nguồn. Bảng Mã có bốn nhóm chi ngày, khai triển12 đầu vào; Thiên hỷ có bốn ô mùa 春戌/夏丑/秋辰/冬未. Nguồn cũng nói sao chỉ có thể trợ Dụng, không tự quyết họa phúc. Các lời bệnh/sinh tử, nghi lễ và nghiệm thuật giữ là nội dung lịch sử, chưa kiểm chứng kết cục thực tế.

## Kiểm thực thi

**14 kiểm đạt**. Bốn lời gọi HHC thật kiểm hai cấu trúc in:32 hào5→28 ở117 và13 hào6→49 ở131. Ca117 có câu nói về ám động hào3; đây không là một dấu gieo6/9 khác. Ca131 không in tên cặp quẻ trong đoạn đầu; số13/49 là chuẩn hóa biên tập từ hình, sáu nhãn và dấu hào6, không tự thêm tên nguồn. Nhãn gốc hào6 là戌/子孫. Bản nháp chưa phát hành từng thêm sai tên剝 và giá trị; QA131 đã loại bỏ trước khi đóng gói. Chưa đối mọi chú của hai ca hoặc chuyển ngày cổ sang Gregory.

Mười lời gọi lunar-typescript1.8.6 thật tại mười ngày trưa liên tiếp chỉ duyệt đủ mười can: sáu ô Lộc nguồn rõ khớp nhánh mở đầu của `getDayLu()`, bốn ô nguồn thiếu vẫn `null`. Đây là so tọa độ sáu ô, không xác thực toàn bộ ý nghĩa Lộc hoặc các sao khác. Runtime giữ phiên bản/SHA. Không gọi HHC và thư viện có liên quan là hai nguồn học thuật độc lập.

64 mặt nạ động trên một cực tính cố định có sáu trường hợp độc phát và sáu độc tĩnh; không lặp4096 quẻ khi logic không phụ thuộc cực tính. Kiểm riêng thiếu tiền đề/khác sai, giao thoa các câu, cảnh báo lớp bình, đầu vào sai, bảo toàn đầu vào và sửa mảng kết quả không làm hỏng bảng nguồn. Các ca và digest ở `qa/liuyao-progress-conditions/`.

## Bảo toàn và phần còn mở

HTML độc lập/root/site giữ **707411 byte**, SHA256 `549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`; ZIPweb344047 byte,15 tham chiếu Lục hào trước giữ byte. Snapshot trước `archives/v53-before-liuyao-progress-conditions/` giữ sourceZIP2002252441 byte/2770 tệp manifest. Kiểm toàn byte manifest và sourceZIP mới ở `RELEASE_RESULTS.json`. Site chỉ cóindex.html; không xuất bản mạng.

Tiếp đầy đủ mạnh yếu/chân không/ứng kỳ, cách chọn Dụng/ngoại lệ các chương đã đọc; chương34 trở đi và rà vị trí quyển trong mục lục còn lại. Giữ mâu thuẫn ngàyB02PDF52 (辛卯 so lời寅卯空),庚 trang136 và các khoảng trống B03/Mai Hoa/Bát tự/Tử vi/Nhà ở. **Toàn kho40 nguồn và bốn hướng vẫn chưa hoàn tất.**
''',encoding='utf-8')
print('Recorded five first-pass spans/private source-layer components;whole catalogue remains active.')
