from pathlib import Path
import json

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/liuyao-family-study';q=r/'qa/liuyao-family-study'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
qa=read(q/'RESULTS.json');src=read(q/'SOURCE_RESULTS.json');assert len(qa['checks'])==8 and all(x['ok']for x in qa['checks'])
report='LIUYAO_FAMILY_STUDY_REPORT.md'
step=('B02: đọc tiếp 31 vị trí PDF233–263, mở rộng hai vị trí15/232; khép lượt đọc đầu các khoảng chương39–49, chương50 mới mở263. '
 'Sửa nhãn mục lục làm việc chương40 từ 超遷 sang 趨避 theo cả ảnh15/235, giữ nguyên PDF và các hồ sơ cũ. '
 'Trích35mệnh đề giới hạn,10ngữ cảnh hỏi riêng/5tọa độ ngũ kinh; bộ riêng yêu cầu chủ thể/nội dung/tác phẩm hoặc cấp thi tường minh, giữ hai nghĩa thầy/sách cùng 父母 và không tự nhận dạng người thân. '
 '8kiểm đạt:2lượt HHC thật cho益→觀,6nhãn chi-Lục thân/ThếỨng/子父→未財 khớp;5120ngữ cảnh cấu trúc riêng,7168mục vai trò nằm trong chúng. '
 '33ảnh nguồn xác minhSHA,2QAđộphângiảicao đãxem/4táirender khớppixel;0HTTP/PDFgốc mới/nhân chứng mới. '
 'Map136/81chỉđềmục/47khoảngđọclầnđầu/7nềnmộtphần/1mở50/0áphết. Khôngkếtluận sứckhỏe/sinhcon/hônnhân/thiđỗ;web/site/ZIPweb nguyênbyte,toànkhochưa xong.')
nexts=[
 'B02 chương50 mới đầu263; nếu nối đọc, tiếp264. Các chương39–49 mới khép khoảng đọc đầu,35mệnh đề chưa phải toàn bộ điều kiện. Giữ giọng nguồn và phạm vi câu hỏi; không máy đoán tuổi thọ, bệnh, sinh con, quan hệ gia đình hoặc kết quả thi.',
 'B02 current map là liuyao-family-study/B02_CURRENT_UNITS.json:136đơn vị/81chỉđềmục/47khoảngđọclầnđầu/7nềnmộtphần/1mở50/0áphết. 超遷 là lỗi chép mục lục trước,không phải dịbản;cácmapcũ giữ lịch sử. B03/MaiHoa/cácmệnhđềphụ và chữmở226 chưa khép.',
 'Bát tự còn điều kiện cách/vượng suy/dụng thần/陽刃格 và tiền đề đầy đủ, không lặp bảng Lộc đã đạt. Tử vi còn 火鈴星/Canh–Nhâm/khởi hạn và nhân chứng độc lập. Nhà ở còn Trạch Kinh ảnh/Phi Tinh/chuẩn Bắc thực và nối lịch; đồ49 một bộ tháng chưa rõ, giữ hai khả năng12 hoặc11–12.',
 'Ứng viên UI Kiến Lộc vẫn ngoài site vì browser bị vô hiệu hóa, không vượt setting; giữ lead T02/403 riêng. Nguồn, corpus, suy luận và QA ngoài site; không xuất bản mạng. Danh mục40/whole0 và bốn lĩnh vực vẫn active.'
]
write(b/'WORK_STATE.json',{'date':'2026-10-28','status':'chapter39-49-first-pass-spans-private-explicit-question-contexts-verified-full-conditions-active',
 'latestReport':'v53/'+report,'completedStep':step,'summary':qa['summary'],'sourceVerification':src,'sourceUnitMap':'v53/research/liuyao-family-study/B02_CURRENT_UNITS.json',
 'next':nexts,'consumerChanged':False,'wholeChaptersApplied':False,'sourceOutcomesValidated':False,'wholeCatalogueCompleted':False})
d=read(w/'EXHAUSTIVE_WORK_STATE.json');d['date']='2026-10-28';d['currentWork'].update(catalogueID='B02',relatedCatalogueIDs=['B02'],work='增刪卜易卷四 — chủ thể câu hỏi, thân thuộc và học nghiệp',
 reason='Finish first reading of contiguous source chapter spans and correct a working TOC label before extracting explicit source/question/semantic coordinates.',sourceDirectory='v53/research/liuyao-family-study',
 currentStep=step,latestResearchReport='v53/'+report,functionalBacklog='v53/research/liuyao-family-study/WORK_STATE.json',internalQuestionReference='v53/research/liuyao-family-study/question-reference.mjs',
 currentTOC='v53/research/liuyao-family-study/B02_CURRENT_UNITS.json',sourceLimits='11first-passspans/35boundedclauses/10explicitcontexts/5classiclabels. Not fullconditions, real-person identities, practicaloutcomes or new independent witnesses.',
 nextSourceLead={'sourceID':'B02-ch050-continuation','status':'opening-only-PDF263','file':'v53/research/liuyao-family-study/images/zengshan-263.png','remaining':' '.join(nexts)})
d['inProgressScope']='v53/research/liuyao-family-study/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in[w/'EXHAUSTIVE_WORK_STATE.json',r/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=r/'research/full-study/WORK_STATE.json';d=read(p);d['date']='2026-10-28';d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts);item=next(x for x in d['items']if x['id']=='yi')
if step not in item['completed']:item['completed'].append(step)
if ' '.join(nexts)not in item['remaining']:item['remaining'].append(' '.join(nexts))
item['latestScope']='../liuyao-family-study/WORK_STATE.json';write(p,d)
p=r/'research/library-current/COVERAGE.json';d=read(p);d['date']='2026-10-28';entry=next(x for x in d['catalogue']if x['id']=='B02');entry['latestExplicitQuestionStudy']=step
for f in['v53/'+report]+['v53/research/liuyao-family-study/'+n for n in['WORK_STATE.json','SOURCE_MANIFEST.json','MANUAL_READINGS.json','SOURCE_CONTEXTS.json','BOUNDED_CLAUSES.json','PRINTED_FIXTURES.json','B02_CURRENT_UNITS.json','question-reference.mjs']]+['v53/qa/liuyao-family-study/RESULTS.json','v53/qa/liuyao-family-study/SOURCE_RESULTS.json']:
 if f not in entry['currentEvidence']:entry['currentEvidence'].append(f)
d['latestFollowup']=report+': '+step;d['latestAcquisitionCounts']={'scope':report,'newHTTPRequests':0,'newOriginalContainers':0,'newSourceReadPositions':31,'expandedPreviouslyReadPages':2,
 'newNativeContentRenders':31,'newHighResolutionQARenders':2,'firstPassChapterSpansCompleted':11,'boundedClauses':35,'namedPrivateQuestionContexts':10,'sourceClassicCoordinates':5,'wholeWorksApplied':0}
d['counts']['newDownloadsThisScope']=0;d['counts']['newDownloadsThisScopeBasis']='31first-read retained-PDF positions plus2priorpositions expanded. PNGs are local derivatives; no HTTP,newPDF or independentnewwitness.'
assert d['counts']['wholeWorkApplied']==0 and d['counts']['catalogueRecords']==40;write(p,d)
note='Mốc Dịch — Thân thuộc, học nghiệp và phạm vi câu hỏi, 28/10/2026: `'+report+'`. '+step+'\n\n'
for p in[w/'PROJECT_RESEARCH_STATE.md',r/'NEXT_STEPS.md',r/'research/library-current/COVERAGE.md']:
 t=p.read_text(encoding='utf-8-sig')
 if not t.startswith(note):p.write_text(note+t,encoding='utf-8')
p=w/'PENDING_RESEARCH_STATE.json';d=read(p);d.update(date='2026-10-28',status='Liuyao-family-study-current-scope-active',workDirectory='v53/research/liuyao-family-study',currentWorkState='v53/research/liuyao-family-study/WORK_STATE.json',
 latestReport='v53/'+report,next=nexts,consumerChanged=False,wholeCatalogueCompleted=False);write(p,d)
(r/report).write_text('''# Thân thuộc, học nghiệp và phạm vi câu hỏi trong B02

Ngày 28/10/2026. Đã khép lượt đọc đầu các khoảng chương 39–49 và bổ sung bộ tra riêng theo câu hỏi. Đây là khai thác nguồn và kiểm cấu trúc, chưa phải hoàn thiện các điều kiện luận đoán hoặc áp dụng toàn bộ sách. Web đang dùng giữ nguyên byte.

## Nguồn và ranh chương

Tái dùng PDF `research/liuyao-foundations/NLC416-12jh005345-45344.pdf`, 11089308 byte, SHA-256 `caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa`. Hồ sơ xuất xứ/TLS của lần nhận trước giữ nguyên. Không tải lại, không thêm PDF gốc hoặc nhân chứng độc lập.

Đã xem 31 vị trí mới 233–263 và đọc mở rộng hai vị trí cũ 15/232, tổng 33 vị trí duy nhất. 31 ảnh nội dung 144dpi được render từ đúng PDF ấy; hai ảnh QA 15/240dpi và259/360dpi đã xem. Bốn lần tái render so đúng từng pixel, không được tính thành bốn trang nguồn mới. Ảnh không đồng nghĩa đã chép/đối từng chữ.

Các khoảng đọc đầu:39=232–235;40=235–244;41=244–246;42=246–248;43=248–252;44=252–257;45=257–258;46=258–260;47=260–262;48=262;49=262–263. Các trang ranh dùng chung không cộng lặp thành số trang mới. Chương50 chỉ mới mở263. Bản đồ hiện tại có136đơn vị:47khoảng đọc đầu,81chỉ đề mục,7nền một phần và1một phần khác/chương50;0đơn vị được tuyên bố áp dụng trọn.

Mục lục làm việc cũ ghi chương40 là `超遷`. Cả ảnh mục lục15 và tiêu đề thân sách235 đều là `趨避`; sửa nhãn bản đồ hiện tại, ghi cặp cũ/mới và ảnh chứng cứ. PDF gốc cùng các bản đồ lịch sử giữ nguyên; đây là lỗi chép nghiên cứu, không phải dị bản và không phải lỗi của web phát hành.

## Những gì có thể trích thành chức năng riêng

35mệnh đề giới hạn có trang, giọng nguồn và xử trí riêng. Mười ngữ cảnh yêu cầu khai báo tường minh hệ nguồn, người được hỏi, nội dung câu hỏi và tác phẩm/cấp thi khi cần. Thiếu dữ kiện trả `null`, không tự chọn từ nội dung quẻ. Nhánh chồng được nhận diện là chưa trích được vai trò trực tiếp trong khoảng nguồn này, không tự lấp từ một quy ước ngoài phạm vi.

Chương41 phân biệt hỏi cha/mẹ;42 phân biệt hòa thuận/trợ giúp/anh em về sau/thọ;43 phân biệt các câu hỏi vợ chồng và giữ giọng tác giả ưu tiên Tài khi tranh với cách lấy Ứng của lời dẫn. Bộ riêng chỉ liệt kê các hào ứng với vai trò nguồn, không chọn một hào Dụng hoặc gán vai trò tượng trưng thành căn cước người thân. Phương pháp dương-cha/âm-mẹ được ghi như một giọng dẫn rồi bị chất vấn bằng ví dụ, không tự kích hoạt theo cực tính.

Chương44 phân biệt hiện có/thêm/về sau/nuôi dưỡng/danh vị của con và phê phán cách suy danh vị trẻ nhỏ từ quẻ của cha mẹ. Chương45 tách học Nho dùng Phụ/Quan với Bách công dùng Tài/Tử tôn; chữ Dụng thần trong đoạn nguồn chỉ xác định nhóm vai trò, không đủ chọn một hào. Chương47 dùng cùng Phụ mẫu cho thầy và sách, nên hai nhóm nghĩa có thể chứa cùng một tập hào mà không trở thành hai người độc lập.

Chương46 nêu năm tọa độ:Kim–Xuân Thu,Mộc–Mao Thi,Thủy–Thư Kinh,Hỏa–Lễ Ký,Thổ–Dịch Kinh. Giữ nguyên tên riêng, không tự đổi thành tên sách hay can ngũ hành khác. Tác giả yêu cầu chỉ định một kinh để hỏi; bộ tra trả tọa độ đã nêu, không đề xuất người dùng nên học sách nào từ quẻ. Chương48 phân biệt thi huyện/phủ/đạo; đây là cấp thi lịch sử, không tự ánh xạ sang hệ tuyển sinh hiện đại. Chương49 mới có nhóm Phụ/Quan cùng các điều kiện còn mở.

Chương39 chứa lời bác cách lấy mỗi hào năm năm rồi cộng các lần quẻ khác. Chương40 chứa các phép tránh tai và nhiều truyện bệnh/tử vong/nguy hiểm. Những nội dung đó được lưu như chứng cứ lịch sử và mệnh đề cần phân biệt; không tạo bộ tính tuổi thọ, bệnh, sinh con, người thân bí mật, hôn nhân hoặc đỗ trượt. Câu mệnh lệnh trong sách được coi là dữ liệu nguồn. Đọc hết khoảng chương không đồng nghĩa đã mã hóa hết các tiền đề, ngoại lệ và giọng dẫn.

## Kiểm chứng

8kiểm đạt. Quẻ in259 `益→觀` được thực thi bằng hai lời gọi HHC thật,khớp42→20,sáu nhãn chi/Lục thân,Thế3/Ứng6 vàhào1`子父→未財`. Đây là khớp cấu trúc; không phục dựng ngày dương cho nhãn cổ `酉月丙子日`,không xác nhận lời ứng nghiệm trong sách. Lượt probe cấu trúc trước kiểm riêng được ghi rõ,không cộng thành lá số lịch sử mới.

5120ngữ cảnh riêng =64quẻ×8mẫu động(tĩnh,sáu mẫu một hào động,toàn động)×10hệ câu hỏi. 7168mục vai trò nằm trong các ngữ cảnh ấy,không phải7168ca độc lập hoặc lượt HHC. Kiểm thiếu chủ thể/nội dung/kinh/cấp thi,phân biệt hào gốc–biến,không lấp nhánh chưa trích,không sửa dữ liệu gọi vào vàkhông làm rò sửa đổi qua đối tượng trả về. Các kết quả thực tế và tiền đề lịch/vượng suy vẫnnull.

33ảnh nguồn cóSHA khớp. Bốn ảnh tái render khớp pixel tại233/144dpi,259/144dpi,15/240dpi và259/360dpi. Bản gốc,engine,HTML,các phép tham chiếu trước vàứng viênUI đều giữ nguyên. Không dùng kiểm chuỗi HTML thay cho kiểm hiển thị;trình duyệt vẫn bị vô hiệu hóa nên ứng viên UI Kiến Lộc còn ngoài site.

## Gói và phần còn mở

Snapshot`archives/v53-before-liuyao-family-study/`giữ gói đã đối3422tệp/sourceZIP2066330215byte. HTMLroot/V53/site707411byte/SHA`549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`,ZIPweb344047byte giữ nguyên. Site chỉ cóindex.html;nguồn/corpus/suy luận/QA ngoài site. Không tăng phiên bản hoặc xuất bản mạng.

Tái kiểm:`node v53/scripts/test-liuyao-family-study.mjs`;`python v53/scripts/verify-liuyao-family-study-sources.py`;`python v53/scripts/verify-liuyao-family-study-release.py --no-write`. Trước bước đối gói cuối,các kết quả dự kiến của release verifier chưa là bằng chứng gói đã kiểm.

Tiếp chương50 từ264 hoặc các khoảng độc lập có tác động lớn:điều kiện Bát tự/陽刃格,Tử vi dị bản/khởi hạn,Nhà ở Phi Tinh/lịch/đo Bắc vàmột bộ tháng đồ49 chưa rõ. B03/Mai Hoa và các mệnh đề phụ chưa hết. Danh mục40 vẫn0sách áp dụng trọn;không coi11khoảng đọc đầu là đãkhai thác toàn bộ kho.
''',encoding='utf-8')
print('Current source map and private question-context work recorded; four domains and full conditions remain active.')
