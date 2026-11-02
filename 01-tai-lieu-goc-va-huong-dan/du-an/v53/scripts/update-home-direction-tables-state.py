from pathlib import Path
import json

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/home-direction-tables'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
qa=read(r/'qa/home-direction-tables/RESULTS.json');src=read(r/'qa/home-direction-tables/SOURCE_RESULTS.json')
assert len(qa['checks'])==7 and all(x['ok']for x in qa['checks'])
assert src['nativeCropsVerified']==4 and src['losslessRotationsVerified']==6
report='HOME_DIRECTION_TABLES_REPORT.md'
step=('Nhà ở: trích đủ bảng24 tiết khí/phương vị (48 nhãn) và nạp giáp địa lý24 tọa độ thuộc8 quẻ/24 nét hào; '
      'liệt kê8 đoạn văn của hai mục, giữ lời nguồn chưa rõ xuất xứ. '
      '7 kiểm đạt:24 lần HHC_MOUNTAINS,8 quẻ thuần HHC,1 bảng tiết khí lunar1.8.6 và2 đối chiếu Lục hào riêng thực thi thật. '
      'Năm alias tên tiết khí và bốn alias chi/quẻ khai báo riêng; không suy thời điểm thiên văn từ đồ phương vị. '
      'Khảm/Quý và Ly/Nhâm địa lý khác Mậu/Kỷ từng hào; không hợp nhất hai hệ. '
      '5 ảnh đọc mở rộng,4 crop native/6 xoay không nội suy;0 HTTP/container/trang nguồn mới. '
      'HTML/site/ZIP web nguyên byte, toàn kho vẫn chưa hoàn tất.')
nexts=[
 'Xieji đã liệt kê đủ phần văn và bảng của bốn mục hẹp XJ2-03/04/08/09. Chưa có bộ nối chuẩn Bắc/số đo thực; không lặp lại các tâm/ranh/24tiết/8quẻ nếu không đổi logic. Mộ vận còn đồ41/49, lời bình Hồng phạm và các ứng dụng Du Niên/điều kiện từng phái chưa đóng.',
 'Chuyển phần độc lập Bát tự: đọc tiếp đầy đủ các điều kiện cách cục, kiến lộc/dương nhận và dụng thần có tên truyền bản; dùng các tọa độ/quan hệ đã kiểm thay vì lặp lại bảng can. B02 Kinh Dịch còn từ ảnh191 và các mệnh đề phụ B03/Mai Hoa; Tử vi còn nhân chứng Canh/Nhâm/tuổi khởi hạn.',
 'P03 Trạch Kinh chưa có đủ ảnh/đồ, còn24/26, điều cấm, tháng/nhuận và metadata; không coi Hiệp Kỷ là cùng tác phẩm. Danh mục40 còn whole0. Nguồn/lời cổ/giải thích/điểm chưa xác minh giữ ngoài site; không triển khai mạng.'
]
units=read(r/'research/home-rings/CURRENT_VOLUME_UNITS.json')
units['previousMap']='v53/research/home-rings/CURRENT_VOLUME_UNITS.json';units['latestScope']='v53/research/home-direction-tables/WORK_STATE.json'
for x in units['units']:
 if x['id']=='XJ2-08':
  x['extractionStatus']='all-available-heading-prose-and24-direction-labels-enumerated'
  x['disposition']='24 term labels/24 coordinate labels and two prose segments compiled privately; explicit glyph/coordinate aliases and derived ideal angles. No source astronomical instant or complete Qimen algorithm.'
 if x['id']=='XJ2-09':
  x['extractionStatus']='all-available-heading-prose-and24-coordinate-labels-enumerated'
  x['disposition']='24 geographical coordinates/24 manual trigram strokes and six prose segments compiled privately; source unknown-origin criticism retained. Distinct from per-line Liuyao NaJia; historical cited witness not independently collated.'
units['nextAtomicWork']=nexts
write(b/'CURRENT_VOLUME_UNITS.json',units)
write(b/'WORK_STATE.json',{'date':'2026-10-27','status':'two-direction-headings-enumerated-private-functions-verified-rest-active',
 'latestReport':'v53/'+report,'completedStep':step,'summary':qa['summary'],'sourceVerification':src,
 'sourceUnitMap':'v53/research/home-direction-tables/CURRENT_VOLUME_UNITS.json','next':nexts,'consumerChanged':False,
 'astronomicalInstantsVerifiedBySource':False,'historicalCitationIndependentlyVerified':False,'wholeCatalogueCompleted':False})
d=read(w/'EXHAUSTIVE_WORK_STATE.json')
d['currentWork'].update(catalogueID='P03',relatedCatalogueIDs=['P03'],work='欽定協紀辨方書卷二 — tiết khí/phương vị và nạp giáp địa lý',
 sourceDirectory='v53/research/home-direction-tables',currentStep=step,latestResearchReport='v53/'+report,
 functionalBacklog='v53/research/home-direction-tables/WORK_STATE.json',internalHomeDirectionReference='v53/research/home-direction-tables/direction-reference.mjs',
 sourceLimits='Two more source headings enumerated:24 terms/24 geographical coordinates/24 manual strokes/8 contextual segments. Not astronomical event instants, whole110 pages, P03 text or whole catalogue.',
 nextSourceLead={'sourceID':'Bazi-complete-conditional-patterns-and-crossrefs','status':'open-read-latest-bazi-state-before-selecting-next-unit',
 'file':'v53/research/bazi-jianlu-coordinates/WORK_STATE.json','remaining':' '.join(nexts)})
d['inProgressScope']='v53/research/home-direction-tables/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in[w/'EXHAUSTIVE_WORK_STATE.json',r/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=r/'research/full-study/WORK_STATE.json';d=read(p);d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts)
item=next(x for x in d['items']if x['id']=='home');item['completed'].append(step);item['remaining'].append(' '.join(nexts));item['latestScope']='../home-direction-tables/WORK_STATE.json';write(p,d)
p=r/'research/library-current/COVERAGE.json';d=read(p);entry=next(x for x in d['catalogue']if x['id']=='P03');entry['latestRelatedIndependentSourceScope']=step
for f in['v53/'+report]+['v53/research/home-direction-tables/'+n for n in['WORK_STATE.json','CURRENT_VOLUME_UNITS.json','SOURCE_TABLES.json','direction-reference.mjs','PRIOR_STAGED_PROBE.json']]+['v53/qa/home-direction-tables/RESULTS.json','v53/qa/home-direction-tables/SOURCE_RESULTS.json']:
 if f not in entry['currentEvidence']:entry['currentEvidence'].append(f)
d['latestFollowup']=report+': '+step
d['latestAcquisitionCounts']={'scope':report,'newHTTPRequests':0,'newOriginalContainers':0,'newSourcePages':0,'expandedPreviouslyReadPages':5,
 'nativeQACrops':4,'losslessRotations':6,'termLabels':24,'termCoordinateLabels':24,'geographicalNaJiaCoordinates':24,'manualGlyphs':24,'sourceProseSegments':8,'wholeWorksApplied':0}
d['counts']['newDownloadsThisScope']=0;d['counts']['newDownloadsThisScopeBasis']='Retained5 source images;4 native crops/6 lossless rotations; no HTTP or new original.'
assert d['counts']['catalogueRecords']==40 and d['counts']['wholeWorkApplied']==0;write(p,d)
note='Mốc nhà ở — Tiết khí và nạp giáp địa lý, 27/10/2026: `'+report+'`. '+step+'\n\n'
for p in[w/'PROJECT_RESEARCH_STATE.md',r/'NEXT_STEPS.md',r/'research/library-current/COVERAGE.md']:p.write_text(note+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
write(w/'PENDING_RESEARCH_STATE.json',{'date':'2026-10-27','status':'Home-direction-tables-current-scope-active','workDirectory':'v53/research/home-direction-tables',
 'currentWorkState':'v53/research/home-direction-tables/WORK_STATE.json','latestReport':'v53/'+report,'next':nexts,'consumerChanged':False,'wholeCatalogueCompleted':False})
(r/report).write_text('''# Nhà ở: đủ24 tiết khí/phương vị và nạp giáp địa lý

Ngày27/10/2026. Bảy kiểm chức năng đạt; đối byte và pixel nguồn đạt. Hai mục 二十四節氣方位/八卦納甲三合 được liệt kê đủ phần bảng, tượng và văn trong phạm vi ảnh53–57. Bộ tham chiếu riêng tra phương vị theo tên tiết khí nguồn hoặc quẻ địa lý theo tọa độ nguồn. HTML/site/ZIPweb giữ nguyên; bốn lĩnh vực và toàn kho vẫn chưa hoàn tất.

## Chứng cứ và nội dung

Tái dùng 欽定協紀辨方書卷二/CADAL06056503.djvu,3.433.014byte, SHA-256`bfd3b76c55d62324919ab161c8c2ba2ecb129b3b2c59a3ab0428807e8f8278db`. Năm ảnh53–57 đã đọc được mở rộng;0HTTP/container/trang nguồn mới. Hai đồ53/55 được xem ở bốn hướng xoay, thêm hai crop chữ54/56; tổng4crop native/6xoay không nội suy được so lại từng pixel. Không OCR hoặc điền nét từ đáp án engine. Nguồn và ghi chép ngoài site.

Đồ53 có24 tên tiết khí/24 tọa độ; lời ảnh54 khớp đủ24 cặp. Đồ dùng Khảm/Chấn/Ly/Đoài tại bốn phương chính, không ghi Tý/Mão/Ngọ/Dậu; bốn thay tên tọa độ khi nối mô hình được khai báo. Năm alias tên tiết khí với thư viện hiện đại cũng khai báo riêng, không sửa chữ ảnh. Các phương vị độ là mô hình đều24vị trí đã nêu trong phạm vi trước, không là kinh độ Mặt Trời hoặc phép suy thời điểm thiên văn.

Nguồn nói bốn Lập/hai Phân/hai Chí ứng tám quẻ và nhắc Kỳ môn chín cục. Câu dẫn này chưa cung cấp đủ quy tắc chọn cục; không tạo tính năng Kỳ môn chỉ từ24 nhãn hướng.

Đồ55 và văn56 gồm:乾甲、坤乙、艮丙、巽辛、震庚亥未、兌丁巳丑、坎癸申辰、離壬寅戌. Tổng24 tọa độ thuộc8 quẻ; đọc đủ24 nét tượng. Sáu đoạn văn nạp giáp, kể cả dòng nối đầuảnh57, giữ riêng lời phê bình **其法不知所自來** (nguồn nói không biết phép ấy từ đâu tới), phần trích 啓蒙附論 và lý giải tiên/hậu thiên. Chưa đối riêng nhân chứng của sách được trích, không biến lập luận khí/chất/nước/lửa thành kết quả thực nghiệm.

Nạp giáp này thuộc tọa độ địa lý, khác gán can–chi từng hào: Khảm nhận Quý và Ly nhận Nhâm; Lục hào hiện có dùng Mậu/Kỷ cho hai quẻ tương ứng. `geographicalNaJia` yêu cầu tên hệ và một ký tự đúng bảng; không tự nhận Tý/Mão/Ngọ/Dậu hay Mậu/Kỷ thay tọa độ nguồn. Kết quả không sinh can–chi từng hào, lịch, phòng ở hoặc dự báo. Câu dẫn Cửu tinh/tịnh âm tịnh dương ởảnh57 chỉ được ghi nhận, chưa là toàn thuật toán của những phép ấy.

## Kiểm chứng

7 kiểm đạt:24 lần `HHC_MOUNTAINS.inspect` thật đối phương vị của mô hình;8 lần `HHC_ENGINE.hexNumber` thật đối24nét tượng/tám quẻ thuần;1 bảng tiết khí lunar-typescript1.8.6 thật đối tên/thứ tự24mục;2 lá số Lục hào tham chiếu riêng thực thi để kiểm Mậu/Kỷ không bị lẫn Quý/Nhâm. Không gọi phép so tên/thứ tự là hiệu chuẩn24 thời điểm tiết khí; không có thời điểm nguồn để đối. Đã kiểm đủ24 gán nạp giáp, tên hệ/alias tường minh, trảnull khi chưa biết và không sửa đầu vào. Probe khi còn ởtmp được lưu riêng; các lượt đó không cộng vào số thực thi tích hợp mới.

HTML gốc/V53/site707411byte giữ SHA`549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`; ZIPweb344047byte giữ nguyên, site chỉindex.html. Snapshot trước`archives/v53-before-home-direction-tables/` giữ3164tệp/ZIP2037602853byte. Gói nguồn mới và manifest được đối byte sau đóng gói, kết quả`qa/home-direction-tables/RELEASE_RESULTS.json`. Không tăng phiên bản, xuất bản mạng hoặc sửa lịch sử.

Bản đồ12mục hiện hành kế thừa ba phạm vi nhà ở trước; bốn mục hẹp03/04/08/09 đã liệt kê phần văn/bảng, còn ứng dụng đo thực và những chương khác. Không coi Hiệp Kỷ là đã áp dụng trọnP03 Trạch Kinh. Chuyển khoảng trống độc lập Bát tự/cách cục và các điều kiện đầy đủ; Dịch/Tửvi còn theo backlog,40 hồ sơ vẫn whole0.

Tái kiểm: `node v53/scripts/test-home-direction-tables.mjs`; `python v53/scripts/verify-home-direction-tables-sources.py`; `python v53/scripts/verify-home-direction-tables-release.py --no-write`.
''',encoding='utf-8')
print('Updated two more source headings, private reference report and open four-domain backlog; whole catalogue remains incomplete.')
