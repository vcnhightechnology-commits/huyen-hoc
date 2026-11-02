from pathlib import Path
from collections import Counter
import json,hashlib

root=Path(__file__).resolve().parent.parent
workspace=root.parent
out=root/'research/library-current'
out.mkdir(exist_ok=True)
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old=root/'research/library-audit/COVERAGE.json'
historical=read(old)
probe=read(out/'RUNTIME_PROBE.json')
oldcatalog=read(root/'research/library-audit/LEGACY_CATALOGUE.json')
assert len(historical['catalogue'])==40 and len(historical['moduleSources'])==16
changes={
 'F01':('partial_active','Đã dùng 64 quẻ, hào động/quẻ biến và 384 lời gợi mở riêng, hai bổ sung Càn–Khôn. Nguồn bản số gắn từng hào; lời Việt biên tập, chưa dịch sát/hiệu khảo ảnh toàn bộ hoặc giải quyết bảy khác dạng.',['v53/yi-lines.js','v53/yi-complete-data.js','v53/research/four-items/YI_REVIEW.json','v49/data/yi_research.json']),
 'M01':('partial_active','Đã dùng một phần căn cứ Thập thần từ Tam Mệnh Thông Hội bản số Kanripo WYG ghim commit; đọc quyển 5 và phân biệt bảng tư lệnh quyển 2. Chưa áp toàn cách cục/dụng thần; URL Wikisource danh mục cũ không được coi là đã tải/kiểm chỉ vì có bản Kanripo.',['v53/research/four-items/BAZI_SOURCE_AUDIT.json','v53/research/four-items/sources/KR3g0042_005.txt','v53/bazi-relations.js']),
 'M04':('partial_active','Đã đọc 12 tập hợp tàng can từ scan Uyên Hải 1926, PDF trang 54/trang in 三六, có thư mục NTL. UI đã có can lộ/tàng can và Thập thần; chưa hiệu khảo toàn sách. Scan thay thế bổ sung căn cứ, không xác thực ngược mọi lời dẫn từ trang thảo luận/Wikisource thiếu.',['v53/research/four-items/BAZI_SOURCE_AUDIT.json','v53/research/four-items/sources/yuanhai-NTL-v1.pdf','v53/bazi-relations.js']),
 'T01':('partial_active','Đã có lá số, đọc 14 chính tinh/cung đối diện và vận hạn ngày/tháng: đại hạn, lưu niên, lưu nguyệt, Tiểu hạn, Tứ Hóa, bảng các tháng. Có đoạn ảnh cơ quan lưu trữ; giữ khác biệt Canh/Nhâm và khởi hạn. Chưa áp toàn phú/tổ hợp sao/miếu hãm hoặc thống nhất mọi truyền bản.',['v53/engine.js','v53/content.js','v53/fortune.js','v53/fortune-months.js','v53/research/fortune-followup/WITNESS_AUDIT.json']),
 'M07':('inherited_rule_claim','Lập trụ theo tiết khí/ngày/giờ đang chạy. URL website cũ chưa có chuỗi byte/đoạn đã kiểm tương ứng trong kho; kiểm lịch/engine khác không nâng website này thành sách đã xác minh toàn bộ.',['v53/engine.js','v53/BIRTH_TIME_REPORT.md']),
 'M08':('inherited_rule_claim','Bảng và lời đọc tàng can đã có trên UI; 12 tập hợp có đối chứng scan Uyên Hải và thư viện chạy thật. Đây là căn cứ khác, không chứng minh trang hidden-stems cũ đã đọc/xác thực.',['v53/bazi-relations.js','v53/research/four-items/BAZI_SOURCE_AUDIT.json']),
 'X02':('inherited_rule_claim','Bảng tám hướng/cung phi đang dùng; 64 nhãn của tám đồ hình NDL đã so engine. NDL là bản Nhật chuyển biên, không xác minh mọi quy ước năm→cung phi hoặc nguồn website amlichvn cũ.',['v53/engine.js','v53/research/four-items/HOME_64_READINGS.json','v53/qa/four-items/home-64-comparison.json']),
 'X03':('inherited_rule_claim','60 can chi/30 nạp âm có trên web và một số lời sách đã đọc; URL web kế thừa chưa có chuỗi toàn văn/đoạn kiểm nguồn độc lập. Không coi một bảng tính đúng là đã áp hết sách.',['v53/engine.js','v50/data/rule_text_audit.json']),
}
records=[]
for r in historical['catalogue']:
 r={**r,'historicalStatus':r['currentStatus'],'historicalScope':r['scope']}
 if r['id'] in changes:
  status,scope,evidence=changes[r['id']];r.update(currentStatus=status,scope=scope,currentEvidence=evidence)
 else:r['currentEvidence']=[]
 r['wholeWorkApplied']=False
 r['originalURLIndependentlyValidatedByAlternateWitness']=False
 records.append(r)
updates={
 'SRC_M_01':('partial_active_witnessed','Quy tắc an sao/Mệnh–Thân/nạp âm/Tứ Hóa dùng một phần; ảnh quyển 3 không đánh đồng cách chia quyển với bản số quyển 2; dị bản giữ riêng.'),
 'SRC_T_01':('partial_active_witnessed','Đã thêm vận hạn theo ngày/tháng và đoạn ảnh có mục tiêu. Không hiệu khảo toàn lãm hay toàn bộ phối hợp sao.'),
 'SRC_T_03':('editorial_paraphrase_partial','14 chính tinh và 12 chủ đề cung có lời biên tập; chưa gắn toàn bộ từng câu tiếng Việt với mọi đoạn Chư tinh vấn đáp.'),
 'SRC_M_02':('inherited_url_with_alternate_witness','Có Tam Mệnh Kanripo ghim commit và đoạn Thập thần đã đọc; chưa vì vậy xác nhận URL CText nạp âm hoặc toàn sách.'),
 'SRC_M_04':('inherited_url_with_alternate_witness','Có64 nhãn từ bản Nhật NDL; chưa áp toàn Bát Trạch Trung Quốc hoặc xác thực URL keepds/nguồn chữ kế thừa.'),
 'SRC_B_04':('original_url_quality_warning_alternate_scan_applied','Wikisource Uyên Hải vẫn có giới hạn đã ghi; scan 1926 NTL định danh rõ đã dùng cho 12 tập hợp tàng can, không thay mức chứng cứ của trang cũ.'),
 'SRC_Q_01':('partial_active_individual_readings','Đã có 64 quẻ/384 lời theo hào; bản số gắn vị trí, chưa hiệu khảo ảnh trọn bộ.'),
 'SRC_Q_02':('partial_active_individual_readings','Sáu hào Càn và Dụng Cửu có lời riêng trong phạm vi đã ghi; không suy thành toàn bộ Chu Dịch đã giải xong.'),
}
module=[]
for r in historical['moduleSources']:
 r={**r,'historicalAuditStatus':r['auditStatus']}
 if r['id'] in updates:r['auditStatus'],r['currentScope']=updates[r['id']]
 else:r['currentScope']='Giữ mức chứng cứ trước: '+r['auditStatus']+'. Chưa tìm thấy cải tiến sau kiểm kê làm thay đổi nguồn dẫn cụ thể này.'
 r['wholeWorkApplied']=False;module.append(r)
added=[
 {'id':'A01','title':'Tam Mệnh Thông Hội, WYG / Kanripo KR3g0042','kind':'pinned_digital_witness','url':'https://github.com/kanripo/KR3g0042/tree/7db72e5553de6ee4c45ed3980c6c67f8a6e451bf','possession':'Readme và13 tệp đề yếu/quyển 0–12 ở commit cố định.','reviewed':'Quyển5 1a–4b,5a; quyển 2 33a–36a để phân biệt bảng phân ngày.','applied':'Căn cứ quan hệ Thập thần; không gộp tư lệnh thành tàng can cố định.','remaining':'Đối chiếu ảnh WYG, cách cục, đại vận, dụng thần; lưu đủ tệp không có nghĩa đã đọc đủ.','evidence':['v53/research/four-items/BAZI_SOURCE_AUDIT.json','v53/research/four-items/sources/MANIFEST.json']},
 {'id':'A02','title':'Uyên Hải / Tử Bình Chân Thuyên v.1, NTL-9900014379','kind':'catalogued_scan','url':'https://taiwanebook.ncl.edu.tw/zh-tw/book/NTL-9900014379','possession':'PDF 207 trang đã giữ byte; metadata nguồn lưu/ảnh NTL,1926 theo thư mục.','reviewed':'PDF54/trang in 三六, 又地支藏遁歌:12 tập hợp.','applied':'Tàng can trong kết quả Bát tự.','remaining':'206 trang còn lại chưa có dấu vết đọc mục tiêu tương đương; tên ghép không chứng minh Tử Bình Chân Thuyên đã được khai thác.','evidence':['v53/research/four-items/BAZI_SOURCE_AUDIT.json']},
 {'id':'A03','title':'八宅明鏡図解 / NDL 760737, bản Nhật 1881','kind':'institutional_scan','url':'https://ndlsearch.ndl.go.jp/books/R100000039-I760737','possession':'21/23 JPEG hợp lệ đã lưu; hai phản hồi 400 là lỗi.','reviewed':'Tám đồ hình, 64 nhãn theo tên quái; Nam trên/Đông trái được ánh xạ rõ.','applied':'Đối chứng bảng tám hướng đang dùng; không là thuật toán đặt mọi phòng.','remaining':'Quy ước năm/cung phi,24 sơn, nguyên bản Trung Quốc, tư vấn phòng theo đo đạc.','evidence':['v53/research/four-items/HOME_64_READINGS.json','v53/qa/four-items/home-64-comparison.json']},
 {'id':'A04','title':'Tử Vi Toàn Thư / 国立公文書館 子060-0001','kind':'institutional_scan','url':'https://www.digital.archives.go.jp/file/1078787','possession':'Metadata/IIIF sách đóng1 với 129 canvas;13 JPEG chính thức 2200 px mục tiêu trong hai lượt, không phải JP2 nguyên bản.','reviewed':'Sáu đoạn ở 74–80; một vùng đồ 88 được phân loại, không phải bảng mười can.','applied':'Củng cố một phần Xương–Khúc/Tả–Hữu/Đẩu Quân/Tiểu hạn/Nhâm Hóa Khoa; công khai quy ước dùng trong kết quả.','remaining':'Canh Hóa Khoa/Kỵ, tuổi/cung khởi đại hạn, toàn phú/tổ hợp/miếu hãm; không áp đồ 88 làm điểm số.','evidence':['v53/research/fortune-followup/WITNESS_AUDIT.json','v53/research/fortune-table/DIAGRAM_AUDIT.json']},
]
features=[
 {'id':'yi','active':'64 quẻ,384 lời gợi mở riêng theo hào, hai bổ sung; lưu/xuất/in.','missing':'Hiệu khảo ảnh 384 hào, bảy khác dạng, chú giải đầy đủ theo nhân chứng; Mai Hoa/Lục Hào không tự có vì dùng sáu hào.'},
 {'id':'bazi','active':'Tứ trụ, Nhật chủ, Thập thần, 12 bảng tàng can; xử lý chưa biết giờ.','missing':'Cách cục,vượng suy, dụng thần, đại vận; không chọn dụng thần từ đếm hành.'},
 {'id':'tuvi','active':'12 cung,14 chính tinh,đọc cung đối diện; đại hạn/năm/tháng,Tiểu hạn/Tứ Hóa,bảng tháng năm âm.','missing':'Luận phối hợp sao đầy đủ, miếu hãm theo từng bản,giải quyết Canh/Nhâm và khởi hạn; chưa dự đoán tổng hợp sự kiện.'},
 {'id':'home','active':'Cung phi/tám hướng, 64 nhãn đối chứng, 7 khu vực và đọc góc/Bắc/bất định.','missing':'Nguyên bản Bát Trạch/Dương Trạch định danh rõ,quy ước năm→cung phi,24 sơn,Phi tinh,mặt bằng có kích thước/Bắc/cửa/phòng.'},
 {'id':'other','active':'Chưa có công cụ riêng cho các phương pháp khác.','missing':'Mai Hoa, Lục Hào/Nạp Giáp, trạch nhật, Kỳ Môn, Lục Nhâm, Thái Ất; nhiều mục chỉURL/cổng danh mục.'}
]
evidence_files=set()
for r in records:evidence_files.update(r['currentEvidence'])
for r in added:evidence_files.update(r['evidence'])
evidence_files.update(['v53/research/library-current/RUNTIME_PROBE.json','v53/research/four-items/COVERAGE_UPDATE.json','v53/research/month-boundaries/VERIFICATION.json'])
evidence=[]
for f in sorted(evidence_files):
 p=workspace/f;assert p.is_file(),f;evidence.append({'file':f,'bytes':p.stat().st_size,'sha256':sha(p)})
labels={'partial_active':'Dùng một phần, có dấu vết trực tiếp','inherited_rule_claim':'Chức năng/quy tắc có dùng; nguồn dẫn cũ còn cần củng cố','research_only':'Đã thu/kiểm, chưa áp vào web','not_established':'Chưa có dấu vết áp dụng xác định'}
report={'schema':'hhc.library.coverage-current.v1','date':'2026-10-26','conclusion':'NOT_ALL_APPLIED','scope':'Current use of 40 historical catalogue records and 16 overlapping module-source records after the four-item improvements. Catalogue entries include portals, institutions and duplicate URLs; not 56 books and not a percentage of all knowledge. Unchanged records preserve historical findings; no fresh full-book reading claimed.','historicalAudit':{'file':'v53/research/library-audit/COVERAGE.json','sha256':sha(old)},'counts':{'catalogueRecords':len(records),'moduleSourceRecords':len(module),'canonicalCatalogueURLs':historical['counts']['canonicalCatalogueURLs'],'status':dict(Counter(r['currentStatus'] for r in records)),'wholeWorkApplied':0,'additionalWitnessGroups':len(added),'newDownloadsThisScope':0},'product':probe['product'],'catalogue':records,'moduleSources':module,'additionalWitnesses':added,'features':features,'evidenceFiles':evidence,'priorities':[{'rank':1,'subject':'Bát tự','work':'Khai thác từng đoạn đã định danh trong scan Uyên Hải và Tam Mệnh; trước khi thêm đại vận/cách cục cần công thức và ví dụ kiểm được.'},{'rank':2,'subject':'Nhà ở','work':'Xác minh quy ước năm/cung phi và tìm đúng ấn bản Trung Quốc cho Bát Trạch/Dương Trạch, giữ khác biệt với bản Nhật.'},{'rank':3,'subject':'Tử vi','work':'Nhân chứng khác cho can Canh và tuổi/cung khởi hạn; chưa tự đổi bảng đang dùng hoặc nhận đồ 88 là bảng mười can.'},{'rank':4,'subject':'Kinh Dịch','work':'Hiệu khảo ảnh theo trang/tờ, rà dị bản/ý nghĩa; không coi384 lời biên tập là học xong toàn Chu Dịch.'}],'decision':'The condition that all stored book knowledge has been applied is false. Prioritize extracting/verifying unused existing material; acquire an additional witness only for a defined provenance/text/rule gap. No bulk new-book download in this audit.','limits':['A saved full text or PDF is not proof it has all been read or implemented.','Alternate witnesses do not automatically validate original legacy URLs.','Institutional provenance supports identification and textual checking, not divinatory efficacy.','Source/corpus/research stay outside consumer HTML/site.']}
(out/'COVERAGE.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
md=['# Ma trận sử dụng kho nguồn hiện tại — 26/10/2026','','**Chưa áp dụng hết.** Không mục nào được đánh dấu đã áp toàn tác phẩm. Đây là cập nhật sau bốn mục và các lượt hiệu khảo/vận hạn, thay cho việc đọc ma trận 25/10 như trạng thái hiện tại.','','40 hồ sơ danh mục + 16 nguồn mô-đun có trùng lặp; 38 URL chuẩn hóa, có portal/cơ quan/trang bán sách. Không cộng thành 56 cuốn hoặc phần trăm kiến thức.','','| ID | Hồ sơ | Mức chứng cứ sử dụng hiện tại | Phạm vi và phần còn lại |','|---|---|---|---|']
for r in records:md.append(f"| {r['id']} | {r['title_vi']} | {labels[r['currentStatus']]} | {r['scope']} |")
md+=['','## Nguồn mô-đun','','| ID | Nguồn dẫn | Phạm vi hiện tại |','|---|---|---|']
for r in module:md.append(f"| {r['id']} | {r['title_vi']} | {r['currentScope']} |")
md+=['','## Nhân chứng bổ sung đã có','','Đây là nhóm nhân chứng, không phải bốn sách mới tải trong lượt kiểm kê này.','','| Mã | Nhân chứng | Đã đọc/dùng | Chưa dùng đủ |','|---|---|---|---|']
for r in added:md.append(f"| {r['id']} | [{r['title']}]({r['url']}) | {r['reviewed']} {r['applied']} | {r['remaining']} |")
md+=['','Số đếm và hash căn cứ ở `COVERAGE.json`; thực thi module nhúng bản HTML hiện hành tại `RUNTIME_PROBE.json`. Ma trận cũ được giữ như lịch sử, không sửa số liệu cũ thành kết quả mới.']
(out/'COVERAGE.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
print(json.dumps(report['counts'],ensure_ascii=False,indent=2))
