from pathlib import Path
import json
root=Path(__file__).resolve().parent.parent;w=root.parent;base=root/'research/liuyao-b03-book4'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='LIUYAO_B03_BOOK4_REPORT.md';e=read(root/'qa/liuyao-b03-book4/ENGINE_RESULTS.json');s=e['summary']
assert len(e['checks'])==9 and all(c['ok']for c in e['checks'])
step=('Sách đóng 4 B03 đã xem đủ 67 trang theo phạm vi ghi nhận: 65 nội dung, hai bìa; '
 '17 trang kế thừa pending, thêm 48 trang nội dung và hai bìa, hai crop QA. '
 'Ba quyển 8–10 có 11 khoảng mục chính và một mục bổ sung nằm trong Gia trạch; '
 'bốn khoảng kế thừa, bảy mới/khép khoảng trước. Giữ 17 mệnh đề có giới hạn, chưa áp dụng hết từng mục. '
 'Tham chiếu riêng giữ hào 2 là nhà, hào 5 nhân khẩu; hào 4 cần Huynh đệ mới luận hộ, '
 'đại môn còn hợp hào 2, không bắt buộc động; hào 3 Huynh đệ Mão có ngoại lệ giường. '
 '9 kiểm đạt, 64 lời gọi HHC thật kiểm chỉ số quẻ; 4096 ngữ cảnh riêng/12288 chú hào động. '
 '1024 ngữ cảnh có Huynh đệ hào 4, 128 đủ tiền đề đại môn, 64 đủ ngoại lệ giường; '
 'đây là điều kiện tượng quẻ, chưa phải đo mặt bằng hoặc phát hiện vật thật. '
 'Một PDF/2 body TLS từ staging mới vào gói, không HTTP mới nhịp này. '
 'HTML 707411 byte/site/ZIP web và 11 tham chiếu trước giữ nguyên. Toàn kho chưa hoàn tất.')
nexts=[
 'Complete book4 clause-level conditions within all11main units and the nested home supplement; distinguish question roles, primary/changed, relative/time/strength premises and source quotations. Page coverage is not complete application.',
 'Acquire identified physicalbook5 once (NLC892-GBZX0301013045-259423), with API revision/TLS/raw size/SHA. Locate textual-volume/chapter boundaries directly; book6 still unacquired. Do not redownload books1..4.',
 'Home source symbols are not measured floor plans: do not assign a door to every fourth line, discard line3卯brother exception, map line number to storey or manufacture compass recommendations. Supplement attribution/genealogy remains open.',
 'Earlier books1..3allclauses/384annotations/prefaces/strength/functionalvoid/fulltiming/triadcompletion remain; B02PDF52date-void and103heading-only units unresolved. MaiHoa/Bazi/Tuvi/Home and40-source catalogue gaps remain active.'
]
write(base/'WORK_STATE.json',{'date':'2026-10-27','status':'private-home-symbol-premises-complete-book4-first-pass-pages-complete-full-clauses-active',
 'sourceID':'B03-book4','latestReport':'v53/'+report,'privateReference':'home-symbol-reference.mjs','unitMap':'BOOK4_CURRENT_UNITS.json',
 'completedStep':step,'all67PagesViewedByRecordedScope':True,'unviewedPages':[],
 'firstPassMainUnits':11,'firstPassNestedSubsections':1,'newOrCompletedMainSpans':7,'allBook4ClausesApplied':False,
 'newHTTPBodiesThisRun':0,'retainedHTTPBodiesNewToRelease':2,'newOriginalPDFsToRelease':1,
 'newContentRendersThisRun':48,'newCoverRendersThisRun':2,'inheritedPendingContentImages':17,'QAOnlyRenders':2,
 'boundedOperationalClauses':17,'floorPlanAdapter':False,'sourceOutcomeAdjudicator':False,'consumerChanged':False,
 'next':nexts,'wholeBookApplied':False,'wholeCatalogueCompleted':False})
d=read(w/'EXHAUSTIVE_WORK_STATE.json')
d['currentWork'].update(currentStep=step,latestResearchReport='v53/'+report,sourceDirectory='v53/research/liuyao-b03-book4',
 internalB03HomeSymbolReference='v53/research/liuyao-b03-book4/home-symbol-reference.mjs',
 currentB03Book4UnitMap='v53/research/liuyao-b03-book4/BOOK4_CURRENT_UNITS.json',
 functionalBacklog='v53/research/liuyao-b03-book4/WORK_STATE.json')
d['currentWork']['sourceLimits']='B03physicalbooks1..4retained, not all6/14textualvolumes. Book4 all67pages viewed with bounded scope,11mainunits+1nestedsubsection first-pass,0entireunitsapplied. Home divination symbols do not establish physical doors/beds/compass plans. Allclauses/strength/functionalvoid/fulltiming/genealogy and B02PDF52conflict remain.'
a=read(base/'ACQUISITION.json')
d['currentWork']['nextSourceLead']={'status':'downloaded-byte-verified-book4-first-pass-page-coverage-complete',
 'sourceID':'B03-book4','file':'v53/research/liuyao-b03-book4/'+a['file'],'sha256':a['sha256'],'bytes':a['bytes'],
 'sourceURL':a['commonsURL'],'remaining':'Book4allclauses/attribution, then identified physicalbook5NLC892-GBZX0301013045-259423 andbook6.'}
d['inProgressScope']='v53/research/liuyao-b03-book4/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in[w/'EXHAUSTIVE_WORK_STATE.json',root/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=root/'research/full-study/WORK_STATE.json';d=read(p);d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts)
yi=next(x for x in d['items']if x['id']=='yi')
entry=('B03book4 all67pages viewed by scope:65content/2covers,17inherited pending/48newcontent/2newcovers/2QA. '
 '11mainspans+1nestedsubsection across textualvolumes8/9/10;17boundedclauses. '
 'Private home-symbol prerequisites retain line4brother+line2combination and line3卯brother bedexception. '
 '9checks/64actualHHCfigurecalls/4096privatecontexts/12288movingannotations; consumer and11priorreferences unchanged. '
 'OnePDF/twoTLSbodiesfromstagingnewtorelease,0HTTPthisrun;notwholebookapplied.')
if entry not in yi['completed']:yi['completed'].append(entry)
yi['latestScope']='../liuyao-b03-book4/BOOK4_CURRENT_UNITS.json'
yi['remaining']=[x for x in yi['remaining']if not x.startswith('LiuYaoB03:books2/3first-passpagescovered')]
yi['remaining'].append('LiuYaoB03:books2/3/4first-passpagescoveredbutallclausesnotapplied;book1full384annotations/prefaces/strength/triadcompletionopen. Books5/6,fulltiming/functionalvoid/rolechoice/sourcequotationcollation remain. Home divination symbols have no physicalfloorplan adapter. B02PDF52and103heading-onlyunitsopen.')
write(p,d)
p=root/'research/library-current/COVERAGE.json';d=read(p);b=next(x for x in d['catalogue']if x['id']=='B03')
b['scope']='Giữ byte sách đóng 1–4. Sách 4 đủ 67 trang xem theo phạm vi, 11 mục chính và một mục bổ sung thuộc quyển 8–10. Có tham chiếu riêng điều kiện tượng nhà/cửa/giường; chưa áp dụng mọi mệnh đề, tổng vượng suy/hiệu lực, phả hệ hoặc sách 5–6.'
possession='Sách đóng 4: PDF 67 trang/57017134 byte/SHA256 5f8bb92f28120fa4c2c4d629ae8bad9f785dc02324f15f285085c99ab7ffadaf; API revision 754088947/TLS/size/SHA1. Đã xem đủ 67 trang theo phạm vi:65 nội dung/2 bìa; chưa áp dụng hết. Cùng bộ sáu sách, không nhân chứng độc lập.'
if len(b['localPossession'])==3:b['localPossession'].append(possession)
else:assert len(b['localPossession'])==4;b['localPossession'][3]=possession
b['latestLocalReadingScope']='67 bản ghi trang,17 kế thừa pending +48 nội dung/2 bìa mới nhịp này,2 crop QA;11 mục chính+1 lồng.17 mệnh đề/9 kiểm/64 HHC thật;4096 ngữ cảnh riêng/12288 chú động. 1 PDF/2 body TLS mới vào gói từ staging;0 HTTP nhịp này. Tượng gia trạch không là dữ kiện đo nhà.'
for f in ['v53/'+report]+['v53/research/liuyao-b03-book4/'+n for n in ['SOURCE_AUDIT.json','MANUAL_READINGS.json','BOOK4_CURRENT_UNITS.json','HOME_SYMBOL_CLAUSES.json','OPERATIONAL_CLAUSES.json','home-symbol-reference.mjs']]+['v53/qa/liuyao-b03-book4/ENGINE_RESULTS.json']:
 if f not in b['currentEvidence']:b['currentEvidence'].append(f)
d['latestFollowup']=report+':B03book4all67pagesviewed/11main+1nestedspansfirstpass,notallclauses;home-symbolpremises/9checks64HHC4096privatecontexts. Consumerunchanged/wholework0.'
d['latestAcquisitionCounts']={'scope':report,'newOriginalPDFsToRelease':1,'retainedHTTPBodiesNewToRelease':2,
 'newHTTPBodiesThisRun':0,'newContentRendersThisRun':48,'newCoverRendersThisRun':2,'inheritedPendingContentImages':17,
 'contentImagesNewToRelease':65,'coverImagesNewToRelease':2,'QAOnlyRenders':2,'manualRecords':67,
 'firstPassMainUnits':11,'firstPassNestedSubsections':1,'newOrCompletedMainSpans':7,'fullBooksApplied':0}
d['counts']['newDownloadsThisScope']=1;d['counts']['newDownloadsThisScopeBasis']='One original PDF from pending staging newly enters release; zero network download in this run.'
assert d['counts']['wholeWorkApplied']==0;write(p,d)
note='Mốc B03–Sách 4, 27/10/2026: `'+report+'`. '+step+'\n\n'
for p in[w/'PROJECT_RESEARCH_STATE.md',root/'NEXT_STEPS.md',root/'research/library-current/COVERAGE.md']:
 text=p.read_text(encoding='utf-8-sig')
 if text.startswith('Công việc đang triển khai sau B03–Sách3:'):text=text.split('\n\n',1)[1]
 if text.startswith('Mốc B03–Sách 4, 27/10/2026:'):text=text.split('\n\n',1)[1]
 p.write_text(note+text,encoding='utf-8')
pending={'date':'2026-10-27','status':'book4-first-pass-pages-complete-current-scope-active','sourceID':'B03-book4',
 'workDirectory':'v53/research/liuyao-b03-book4','acquisition':a,'currentWorkState':'v53/research/liuyao-b03-book4/WORK_STATE.json',
 'latestReport':'v53/'+report,'manualReadings':'v53/research/liuyao-b03-book4/MANUAL_READINGS.json',
 'checks':'v53/qa/liuyao-b03-book4/ENGINE_RESULTS.json','manualPages':list(range(1,68)),
 'all67PagesViewedByRecordedScope':True,'next':nexts,'consumerChanged':False,
 'wholeBookApplied':False,'wholeCatalogueCompleted':False}
write(w/'PENDING_RESEARCH_STATE.json',pending)
text=f'''# B03: quyển 8–10 và điều kiện tượng gia trạch

Ngày 27/10/2026. Hồ sơ nghiên cứu nội bộ, ngoài site người dùng.

## Nguồn và phạm vi đọc

Sách đóng thứ tư, cùng bộ sáu sách 卜筮正宗: **57.017.134 byte / 67 trang**; SHA-256 `5f8bb92f28120fa4c2c4d629ae8bad9f785dc02324f15f285085c99ab7ffadaf`. PDF và Commons API revision **754088947** đã tải trong staging trước, hai body HTTP 200/TLS được giữ byte. SHA-1 `81df815ecbbfac0526e6b630c73533bafc08155c` và size khớp API; SHA-256 là định danh byte tại máy, không chữ ký nhà xuất bản. **Một PDF/hai body mới vào gói phát hành; không HTTP mới trong nhịp đọc này**. Bản ghi 1904 trong siêu dữ liệu chưa thành kiểm chứng ấn ký mới; cùng bộ không tính nhân chứng độc lập.

Đã xem cả 67 trang theo phạm vi ghi nhận: 65 trang nội dung và hai bìa. Có 17 trang kế thừa pending, thêm 48 trang nội dung và hai bìa được render/xem; hai crop QA 360dpi tại 40–41 không cộng thành trang nguồn. Không OCR hoặc chép ngoại giao đầy đủ. Ranh trực tiếp: quyển 8 mở ở 2, kết ở 21; quyển 9 mở 22, kết 44; quyển 10 mở 45, kết 66.

11 mục chính: 種作2–6, 蠶桑6–9, 六畜9–13, 求名13–17, 仕宦17–21; 求財22–28, 家宅28–44; 墳墓45–54, 求師54–57, 學館57–62, 詞訟62–66. Bốn khoảng đầu kế thừa; bảy khoảng mới/khép phần trước. Mục lồng 新增家宅搜精分別六爻斷法38–44 thuộc Gia trạch, không phải bảy trang độc nhất hoặc mục chính thứ 12. **0 mục đánh dấu áp dụng hết**.

## Chức năng riêng và đối ảnh

`home-symbol-reference.mjs` giữ tọa độ tượng quẻ của đoạn Gia trạch. Trang 28 nêu hào 2 là nhà, hào 5 là nhân khẩu, trong/ngoài; không lấy số thứ tự hào làm tầng nhà. Thế/Ứng giữ của bản quẻ, không đổi thành hai vai này.

Trang 41 nêu `四爻兄弟方言戶` và giải thích thiếu Huynh đệ thì không được lập tức luận cửa. Đại môn còn xét hào 4 hợp hào 2; câu nguồn nói rõ động hoặc tĩnh đều được xét. Tham chiếu dùng bảng lục hợp đã đối trước, **không gán mọi hào 4 là cửa** và không thêm tiền đề động chưa có trong câu này. Trang 40, trong đoạn hào 3, có `兄弟卯爻床榻論`: Huynh đệ Mão được luận giường, không tự gọi cửa. Crop QA đã xem trực tiếp cho cả hai điều kiện.

Đầu vào chỉ nhận sáu giá trị 6/7/8/9 từ dưới lên và ngữ cảnh đoạn nguồn xác nhận. Kết quả trả chi/thân của hào gốc, tiền đề từng tượng và quan hệ cấu trúc. Hào biến giữ riêng theo cung gốc; Huynh đệ biến không thay Huynh đệ gốc để thỏa điều kiện cửa. Không đủ tiền đề chỉ nghĩa chưa đủ cho tượng này, **không chứng minh nhà thực không có cửa**. Không có góc la bàn, tọa độ phòng, số tầng, vị trí cửa/giường thật, khuyến nghị dời đồ hoặc cát hung thực tế. Chưa đưa tham chiếu vào web người dùng.

17 mệnh đề có giới hạn trong `OPERATIONAL_CLAUSES.json` phân mục nông nghiệp/tằm/vật nuôi, thi cử/chức vị, cầu tài, gia trạch, mộ, thầy/học quán và kiện tụng. Vai trò phụ thuộc vật và người được hỏi. Các lời bệnh/tai họa/tử tôn/khấn lễ/sinh lợi là dữ liệu văn bản lịch sử; không phải chỉ dẫn người dùng, kiểm chứng kết cục hoặc tư vấn hiện đại. Danh tính người thêm từng đoạn 新增 và phả hệ chưa hiệu khảo xong.

## Kiểm chứng thực thi

Đạt **9 kiểm**. HHC thật thực thi **64 lời gọi chỉ số quẻ**, nối đúng danh tính 64 quẻ. Bộ riêng chạy **4096 ngữ cảnh** (64 bản quẻ × 64 mặt nạ động), giữ **12288 chú hào động**. Đối chiếu riêng bằng dãy Nạp Giáp literal, chu kỳ ngũ hành và sáu cặp lục hợp, không lấy chính hàm đang thử làm oracle.

Trong tập hữu hạn này: 1024 ngữ cảnh có Huynh đệ hào 4; 128 đồng thời hợp hào 2; 64 có ngoại lệ giường hào 3. Có 256 ngữ cảnh hợp 4–2 nhưng thiếu Huynh đệ gốc, và 280 có Huynh đệ biến ở hào 4 nhưng thiếu Huynh đệ gốc: cả hai không qua tiền đề đại môn. Điều kiện tượng giữ bất biến khi chỉ đổi động/tĩnh; chú hào biến vẫn được giữ. Đây là số trường hợp cấu trúc, không tỷ lệ đoán đúng hoặc phát hiện đồ vật. Digest `{s['graphDigest']}`.

Năm ca dương/âm do bộ kiểm chọn theo tiền đề nguồn được ghi rõ **ca dựng**, không giả là quẻ gieo in trong sách. Đầu vào sai/thiếu ngữ cảnh, extra la bàn/phòng/vượng suy, mảng thưa hoặc giá trị sai đều bị từ chối. HTML và 11 tham chiếu trước giữ byte.

## Phát hành và phần mở

HTML 707411 byte/SHA `549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`; root/site/ZIP web giữ nguyên. Snapshot trước ở `archives/v53-before-liuyao-b03-book4/`: source ZIP 1391617952 byte / 2441 tệp manifest. Nghiên cứu nằm trong gói nguồn, ngoài site; kiểm toàn byte manifest/ZIP được ghi ở `qa/liuyao-b03-book4/RELEASE_RESULTS.json`.

Chưa xử lý mọi mệnh đề của sách 1–4, 384 chú hào/tiền tự, vượng suy, chân không, tự chọn Dụng hoặc ứng kỳ đầy đủ. Sách đóng 5–6 chưa tải tại mốc này; sách 5 được định danh từ liên kết điều hướng trong API sách 4, chưa được tính đã đọc. B02 còn 103 thân mục mức đề mục/136 đơn vị, 26 khoảng đọc lần đầu; ngày–tuần không PDF52 còn mâu thuẫn. Kho 40 tài liệu và bốn mục lớn vẫn active, chưa khai thác hết.
'''
(root/report).write_text(text,encoding='utf-8')
print('Book4 source gates, page coverage and open work recorded.')
