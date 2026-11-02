from pathlib import Path
import json
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/home-you-nian';read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='HOME_YOU_NIAN_REPORT.md'
qa=read(r/'qa/home-you-nian/RESULTS.json');tables=read(r/'qa/home-you-nian/NAMED_TABLE_RESULTS.json');sources=read(r/'qa/home-you-nian/SOURCE_RESULTS.json')
assert all(x['ok']for x in qa['checks']+tables['checks'])and sources['nativePNGAndPixelHashesVerified']==103
step=('Nhà ở: Hiệp Kỷ Biện Phương quyển2 có 103 ảnh nguồn mới đọc/95 nội dung/5 trống/3 ngoại văn, '
 'cộng7 ảnh cũ tạo lượt đọc đầu đủ110 vị trí và12 mục; chưa trích hết mệnh đề/ô bảng. '
 'Bộ riêng Đại/Tiểu Du Niên giữ7 phép đổi hào,64 ô sao đọc trực tiếp và2 bối cảnh cát hung khác nhau. '
 '13 kiểm đạt;8 lời gọi HHC thật khớp64 nhãn hướng nhà có điều kiện cung. '
 'Hai bảng Chính/Hồng phạm đủ48 gán ngũ hành;12 dòng tháng Trạch Kinh chỉ bản chữ, không ghép lịch. '
 'P03 đã đọc6 tệp WYG/HFL,14 nhóm biên tập/10 cặp ngữ cảnh mới;ảnh/đồ còn thiếu. '
 'Ba thân HTTP lỗi giữ đúng byte/SHA/TLS (403,403,503),0 container mới. HTML707411 byte/site/ZIPweb nguyên.')
nexts=[
 'Continue atomic extraction from all12 Xieji volume2 units, now first-pass located: full middle/seam ring coordinate tables/use premises,墓龍變運/yearmonth冠 all cells/examples, five子/納音/solstice boundaries, quoted voices and attribution. Do not redo64direction labels without a change.',
 'Small/Big: seven transformation rules and64small-star cells verified; complete application clauses,坐山/立向/龍 origin selection and384lineglyph figurecollation remain. No universalSmall rating or automaticroomadapter.',
 'P03 retained WYG/HFL digitaltext all read and14editorialgroups mapped, not all clauses applied. Tennewpairedcontexts/threeprior preserved;十干+十二支+四維=26versus24,prohibitionvariant,missingdiagrams,month/leap boundary andHFL1988metadata remain. Three failed URLs retained; no immediate retry.',
 'Otherdomains remain active: Bazi fullpatternconditions/crossreferences;Tuvi independentwitness/age/Canh-Nhâm;Yi B02chapter35from191/B03/MaiHoa clauses. Catalogue40/whole0;source/QA outsideconsumer site.'
]
st={'date':'2026-10-27','status':'named-source-tables-verified-atomic-extraction-active','sourceDirectory':'v53/research/home-you-nian',
 'latestReport':'v53/'+report,'completedStep':step,'sourceSummary':sources,'engineSummary':qa['summary'],'tableSummary':tables['summary'],
 'next':nexts,'consumerChanged':False,'whole110ImageFirstPass':True,'wholeVolumeApplied':False,'wholeCatalogueCompleted':False}
write(b/'WORK_STATE.json',st)
d=read(w/'EXHAUSTIVE_WORK_STATE.json');d['currentWork'].update(catalogueID='P03',relatedCatalogueIDs=['P03'],work='宅經 WYG/HFL and 欽定協紀辨方書卷二',
 reason='Separate complete named tables, source contexts and missing adapters before new dwelling recommendations.',sourceDirectory='v53/research/home-you-nian',currentStep=step,
 latestResearchReport='v53/'+report,functionalBacklog='v53/research/home-you-nian/WORK_STATE.json',internalHomeYouNianReference='v53/research/home-you-nian/you-nian-reference.mjs',
 internalHomeNamedTableReference='v53/research/home-you-nian/named-table-reference.mjs',sourceLimits='First-pass110imagepositions is not allclauses/tablecells orwholeworkapplication. P03digitalonly;40cataloguewhole0.',
 nextSourceLead={'sourceID':'Xieji-volume2/P03','status':'atomic-clauses-and-table-premises-active','file':'v53/research/home-you-nian/VOLUME_UNIT_MAP.json','remaining':' '.join(nexts)})
d['inProgressScope']='v53/research/home-you-nian/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in[w/'EXHAUSTIVE_WORK_STATE.json',r/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=r/'research/full-study/WORK_STATE.json';d=read(p);d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts)
entry=next(x for x in d['items']if x['id']=='home');entry['completed'].append(step);entry['remaining'].append(' '.join(nexts));entry['latestScope']='../home-you-nian/WORK_STATE.json';write(p,d)
p=r/'research/library-current/COVERAGE.json';d=read(p);entry=next(x for x in d['catalogue']if x['id']=='P03')
entry['latestDigitalReadingScope']=step
entry['scope']='Six retained WYG/HFL digital artifacts read;14editorialgroups/12monthrows and10newpairedcontexts anchored. Facsimile/diagrams/atomicclauses/modernadapters open; no dwelling advice applied.'
for f in ['v53/'+report]+['v53/research/home-you-nian/'+n for n in ['WORK_STATE.json','VOLUME_UNIT_MAP.json','MANUAL_READINGS.json','SOURCE_AUDIT.json','SOURCE_RELATIONS.json','SMALL_DIRECT_STARS.json','SOURCE_POLICIES.json','NAMED_MOUNTAIN_ELEMENTS.json','you-nian-reference.mjs','named-table-reference.mjs','zhaijing/DIGITAL_UNIT_MAP.json','zhaijing/TRANSMISSION_COMPARISON.json','zhaijing/REQUESTS.json']]+['v53/qa/home-you-nian/RESULTS.json','v53/qa/home-you-nian/NAMED_TABLE_RESULTS.json','v53/qa/home-you-nian/SOURCE_RESULTS.json']:
 if f not in entry['currentEvidence']:entry['currentEvidence'].append(f)
d['latestFollowup']=report+': '+step;d['latestAcquisitionCounts']={'scope':report,'newHTTPRequestsThisTurn':1,'retainedFailedHTTPBodiesNewToRelease':3,'failedStatuses':[403,403,503],
 'newSuccessfulHTTPBodies':0,'newOriginalContainers':0,'newlyReadSourceImagePages':103,'newNativePNGDerivatives':103,'contentPages':95,'blankPages':5,'paratextPages':3,'priorPageReadings':7,'combinedFirstPassPositions':110,'wholeWorksApplied':0}
d['counts']['newDownloadsThisScope']=0;d['counts']['newDownloadsThisScopeBasis']='No new successful original source body/container;3errorbodies retained;103localPNG derivatives from existing110pageDjVu.'
assert d['counts']['wholeWorkApplied']==0;write(p,d)
note='Mốc nhà ở–Đại/Tiểu Du Niên, 27/10/2026: `'+report+'`. '+step+'\n\n'
for p in[w/'PROJECT_RESEARCH_STATE.md',r/'NEXT_STEPS.md',r/'research/library-current/COVERAGE.md']:
 t=p.read_text(encoding='utf-8-sig')
 if p.name=='PROJECT_RESEARCH_STATE.md'and t.startswith('Phần tiếp theo: `tmp/home-zhaijing-staging/'):
  t=t.split('\n\n',1)[1]
 p.write_text(note+t,encoding='utf-8')
write(w/'PENDING_RESEARCH_STATE.json',{'date':'2026-10-27','status':'Home-you-nian-atomic-extraction-active','workDirectory':'v53/research/home-you-nian',
 'currentWorkState':'v53/research/home-you-nian/WORK_STATE.json','latestReport':'v53/'+report,'next':nexts,'consumerChanged':False,'wholeCatalogueCompleted':False})
(r/report).write_text('''# Nhà ở: phân biệt Đại/Tiểu Du Niên và các bảng theo tên nguồn

Ngày 27/10/2026. Tài liệu nội bộ; không đưa nguồn hoặc phòng kiểm định vào site người dùng. Đây là mở rộng căn cứ và bộ tham chiếu riêng; HTML/engine đang dùng không đổi. Toàn kho và bốn hướng vẫn chưa hoàn tất.

## Nguồn ảnh và phạm vi đã đọc

Container **欽定協紀辨方書卷二**, CADAL06056503 đã giữ từ trước: **3.433.014 byte**, SHA-256 `bfd3b76c55d62324919ab161c8c2ba2ecb129b3b2c59a3ab0428807e8f8278db`, 110 vị trí ảnh. Không tải lại hoặc tính là sách mới. Metadata/bìa Tứ Khố không chứng minh bản đầu hay tác giả đích thực của mọi lời được dẫn.

Đã giải mã và trực tiếp xem **103 ảnh mới** (1,9–110):95 trang nội dung,5 trang trống,3 ngoại văn/bìa/kết. Cộng với7 ảnh2–8 đã đọc và giữ báo cáo trước, đủ110 vị trí có lượt đọc đầu. 49–50 là ảnh nằm ngang trong container, mỗi ảnh vẫn chỉ một vị trí. `VOLUME_UNIT_MAP.json` định vị12 mục; các khoảng giao trang không được cộng thành số trang độc lập. **Đọc đủ vị trí ảnh không có nghĩa đã trích hết mọi mệnh đề, ô bảng hoặc áp hết quyển.**

Decoder DjVu.js0.5.4 giữ nguyên byte, SHA `10a831d62cc7ced39c30c7350a11410402d082a0f0a5b073a88d3d7ca662add3`. Node chỉ cung cấp bộ chứa ImageData và cờ hiện diện document cho nhánh giải mã đồng bộ; không trình duyệt/worker/OCR/network. Một trang hiệu chuẩn Bát tự223 cho mảng RGBA trùng từng pixel với PNG đã giải mã trong trình duyệt; không tính thêm trang nguồn. Giải mã lại58/101 khớp mảng pixel;103 PNG có SHA byte, kích thước và SHA RGBA riêng. Việc trình duyệt thử khởi chạy bị EPERM được giải quyết bằng nhánh decoder cục bộ, không nâng quyền.

## Quy tắc đã làm thành tham chiếu riêng

- `you-nian-reference.mjs` bắt buộc chọn tên hệ Đại hoặc Tiểu Du Niên và quẻ gốc/đích rõ ràng. Thiếu một quẻ giữnull. Bảy phép đổi hào có28 cặp không thứ tự/56 cặp có hướng, cộng8 tự cung cho64 quan hệ mỗi hệ.
- Ở ảnh91–106, năm phép đổi cho tên khác nhau giữa hai hệ: đổi dưới,hai hào dưới,hai hào trên,trên+dưới,cả ba. Tổng40 cặp khác tên;16 cặp không tự cung trùng literal. Tám tự cung giữ hai tên **輔弼/伏位**, chỉ cùng vai trò bản cung; không cộng thành24 literal trùng tên. Trọng số hào1/2/4 vàXOR là mã hóa hiện đại.
- Ảnh63/65/71/73/75/77/79/81 cho đủ64 ô viết tắt sao Tiểu Du Niên; chép trực tiếp và đối riêng với phép biến hào. Ảnh57–59 phân biệt 地理家從龍上起 và 選擇家從向上起: tập sao được nguồn gọi吉 khác nhau. Bộ riêng chỉ trả đánh giá theo bối cảnh được chọn tường minh, mặc địnhnull. Lớp đồ hình so sánh còn có cách đánh giá riêng; không hợp nhất thành điểm tốt/xấu phổ quát.
- `named-table-reference.mjs` giữ **hai bảng24sơn** Chính ngũ hành/洪範五行 từ ảnh10/18.48 gán hành được kiểm độc lập theo bản ghi nguồn. Ví dụ壬 là水 ở Chính nhưng火 ở Hồng phạm,辛 là金 ở Chính nhưng水 ở Hồng phạm. Không lấy một bảng thay mọi bảng.
- Cùng bộ riêng giữ12 dòng 月生氣/死氣 của **bản chữ WYG Trạch Kinh**, bắt buộc số tháng nguồn1–12 và tên nhân chứng. Không đổi từ ngày hiện đại, không mặc định ranh tháng/nhuận và không coi sinh khí tháng là sao Bát Trạch. HFL có已/巳 ở dòng cuối chưa đối ảnh, chưa được tự sửa hoặc hỗ trợ như bảng đã giải quyết.

**13 kiểm đạt**:9 kiểm Du Niên/byte và4 kiểm bảng theo tên. Thực thi **8 lời gọi `HHC_ENGINE.directions` thật** với các đầu vào truy cập8 hàng cung đã biết, đối64 nhãn với quy tắc mới đọc trên ảnh;64/64 khớp. Đây là kiểm quan hệ có điều kiện trên cung, không xác nhận năm→cung phi, ranh Tết/Lập Xuân, tọa/hướng thực tế hay vị trí phòng.128 quan hệ riêng,128 bối cảnh chính sách và48 gán hành là phép kiểm nội bộ, không phải thêm lời gọi engine. Không cần lặp các bộ hình học/cung phi trước khi chúng không đổi.

Bản nháp chép hai cặp ở ảnh102 bị kiểm trùng/mask phát hiện; xem lại trực tiếp cả hình101 và chữ102 cho **離坤/震艮**, thay bản nháp離艮/震坤. Đây là lỗi bản nháp nghiên cứu được sửa trước phát hành, không sửa sách hoặc sản phẩm. Nhật ký giữ trong `SOURCE_AUDIT.json`.

## Trạch Kinh: đã đọc gì và còn thiếu gì

Sáu tệp đã giữ gồm WYG(KR3g0019,commit306f7650b38ab309e648b7a64ecd3b3d8cd5884a) vàHFL(KR5a0294,commitc4a5508d8d672dd4e62713f577f90ed64a17c3c5), mỗi nhóm3 tệp. Đã đọc toàn bộ chữ giữ được;14 nhóm là **nhóm biên tập để phân loại**, không phải14 chương nguồn. Thêm10 cặp ngữ cảnh có mốc tờ:9 chỗ khác nghĩa/chữ và1 vấn đề chung về kiểm kê; ba đối chiếu mở đầu trước vẫn nguyên byte. Giữ literal và chỉ bỏ khoảng trắng/¶/dấu xuống dòng lời chú khi neo chuỗi; không gộp chữ dị thể.

Hai bản đều nói十干+十二支+乾艮坤巽=24 trong khi phép cộng là26. Không mượn tám can của sách khác để sửa. Câu ngày kiêng cũng khác; thiếu đồ hình, nghĩa âm/dương theo di chuyển/bảng đối ứng, ranh tháng/nhuận vàHFL/header1988 còn mở. Tên黃帝 vàlời quy tác giả trong sách là dữ liệu khảo cứu, không bằng chứng lịch sử tác quyền.

Ba response lỗi giữ nguyên:2HTTP403 từCommons và1HTTP503 từkhoWaseda, đềuTLS được xác thực. Các file `.403.txt`/`.503.txt` là thân lỗi với byte/SHA, **không là PDF/DjVu tải thành công**. Hai request403 ở nhịp staging trước, chỉ1 requestWaseda mới trong lượt nối tiếp; tổng3 thân lỗi mới đưa vào gói. Không thử lại URL bị lỗi, đổi danh tính hoặc vượt chặn.0container nguồn mới.

## Phần phải tiếp tục

Trích đủ các bảng 中針/縫針, quy tắc ứng dụng riêng, mọi ô墓龍變運/年月尅山家 và ví dụ có mùa Đông chí/五子/納音; đối từng384 nét hào của bảng八宮; điều kiện坐山/立向/龍 và nguồn dẫn. Quyển này có cả lời bình phản bác các lý giải cổ; không chuyển ví dụ y học/địa lý tượng trưng thành lời khuyên sức khỏe hay mô hình vật lý. Chưa có thuật toán Phi tinh9cung hoàn chỉnh từ các đoạn này.

Snapshot trước: `archives/v53-before-home-you-nian/`,2915 tệp/sourceZIP2018013895 byte. HTML root/V53/site707411 byte/SHA549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857 vàZIPweb344047 byte giữ nguyên; site chỉindex.html. Gói nguồn/manifest cập nhật để giữ bằng chứng và mã mới. Không công bố mạng, không tăng số phiên bản. Kết quả kiểm cuối ở `qa/home-you-nian/RELEASE_RESULTS.json`.

Lệnh kiểm: `node v53/scripts/test-home-you-nian.mjs`; `node v53/scripts/test-home-named-tables.mjs`; `node v53/scripts/redecode-home-you-nian.mjs`; `python v53/scripts/verify-home-you-nian-sources.py`. Không chạy lại script ghi đè dữ liệu lịch sử ở full-study/home.
''',encoding='utf-8')
print('Updated currentHome state and report; fullatomicextraction and catalogue remain active.')
