from pathlib import Path
from html.parser import HTMLParser
from collections import Counter
from urllib.parse import unquote, urlsplit
import hashlib, json, re

root=Path(__file__).resolve().parent.parent
workspace=root.parent
out=root/'research/library-audit'
out.mkdir(parents=True,exist_ok=True)
legacy=workspace/'v46/inputs/Huyen_Hoc_Cac_V45.html'
body=legacy.read_text(encoding='utf-8')
sha=lambda b:hashlib.sha256(b).hexdigest()
catalog,_=json.JSONDecoder().raw_decode(body.split('const BOOKS=',1)[1])
blocks={}
for attrs,text in re.findall(r'<script\b([^>]*)>([\s\S]*?)</script>',body):
    match=re.search(r'\bid=["\x27]([^"\x27]+)',attrs)
    if match and 'application/json' in attrs:
        blocks[match[1]]=json.loads(text)
legacy_sources=blocks['hhc4Data']['sources']
assert len(catalog)==40 and len(legacy_sources)==16

class Text(HTMLParser):
    def __init__(self):super().__init__();self.parts=[]
    def handle_data(self,x):self.parts.append(x)
def plain(file):
    parser=Text();parser.feed(file.read_text(encoding='utf-8'));return ' '.join(parser.parts)

kinds={
 'M07':'modern_reference','M08':'modern_reference','F01':'digital_book','F02':'digital_book','F03':'general_portal',
 'M01':'digital_book','M02':'scan_catalogue','M03':'digital_book','M04':'discussion_catalogue','M05':'general_portal','M06':'discussion_catalogue',
 'T01':'digital_book','T02':'digital_book','B01':'digital_book','B02':'digital_book','B03':'digital_book',
 'P01':'digital_book','P02':'digital_book','P03':'digital_book','P04':'scan_catalogue','P05':'digital_book','P06':'scan_catalogue','P07':'scan_catalogue','P08':'discussion_catalogue',
 'N01':'scan_catalogue','N02':'direct_pdf_link','N03':'academic_article_listing','L01':'digital_book','L02':'image_category',
 'S01':'digital_book','S02':'digital_book','S03':'digital_book','V01':'institution','V02':'digital_library','V03':'publisher_listing','V04':'secondary_book_listing',
 'X01':'scholarly_reference','X02':'modern_reference','X03':'modern_reference','X04':'digital_book'}
usage={
 'F01':('partial_active','64 quẻ/thứ tự/âm dương/động biến đang dùng. Chính văn 384 hào đã đối chiếu ở V49, nhưng V53 dùng 6 lời gợi mở theo vị trí, chưa dùng văn bản từng hào.','v49/data/yi_research.json; v53/scripts/extract-yi.mjs; v53/yi-content.js; v53/app.js'),
 'T01':('partial_active','An sao/nạp âm/Mệnh–Thân và một số bảng đã dùng, có đối chiếu engine và đoạn cổ thư. Không bao phủ toàn bộ các thiên phú/luận tổ hợp hoặc vận hạn trên V53.','v50/data/rule_text_audit.json; v52/data/facsimile_collation.json; v53/engine.js; v53/content.js'),
 'M07':('inherited_rule_claim','Quy tắc Lập Xuân/tiết khí/giờ Tý có thực thi; nguồn website được lớp cũ viện dẫn, chưa có byte trang gốc được xác thực trong kho tìm được.','legacy:hhc4Data/SRC_B_02; v53/engine.js/baziCalcData'),
 'M08':('inherited_rule_claim','Bảng tàng can có trong hằng số, hiện thống kê dùng can đầu của chi; chưa có bản đọc tàng can đầy đủ. Không coi URL tra cứu là sách đã kiểm.','legacy:hhc4Data/modules/bazi/hidden_stems_12; v53/engine.js/BAZI_HIDDEN'),
 'M01':('inherited_rule_claim','Nạp âm được lớp cũ dẫn Tam Mệnh, nhưng chưa chứng minh bằng byte/ảnh chính cuốn này. Chưa áp toàn bộ cách cục/dụng thần.','legacy:hhc4Data/SRC_M_02; legacy:BOOKS/M01; v53/engine.js/NAYIN'),
 'M04':('inherited_rule_claim','Lớp cũ dẫn Uyên Hải cho Thập thần/tàng can. Engine có god cho can nhưng UI chưa trình bày. Trang Wikisource mới kiểm có cảnh báo thiếu nội dung và nguồn chưa rõ.','legacy:hhc4Data/SRC_B_04; v53/research/library-audit/RUNTIME_PROBE.json; new-sources/wikisource-yuanhai.html'),
 'X02':('inherited_rule_claim','Bảng tám hướng/cung phi đang dùng; website tham khảo không thay cho ảnh sách. Đã thêm đối chứng 32 nhãn hướng từ 4 đồ hình NDL, không kiểm công thức năm sinh bằng sách đó.','v53/engine.js/KUAS; v53/research/library-audit/NDL_ENGINE_COMPARISON.json'),
 'X03':('inherited_rule_claim','Chu kỳ 60 can chi/30 nạp âm đang dùng; nguồn web được viện dẫn cũ, không có toàn văn sách riêng từ URL này.','legacy:BOOKS/X03; v53/engine.js/NAYIN'),
 'M02':('research_only','Đã lấy metadata mới: đúng Tam Mệnh Thông Hội quyển một, mục CADAL/Zhejiang. Chưa tải hoặc đọc nội dung ảnh; bản PDF của mục này không đại diện đủ 12 quyển.','new-sources/archive-06066037-metadata.json'),
 'P03':('research_only','Đã tải trang số và hai nhân chứng chép Trạch Kinh gắn WYG/HFL ở commit cố định; chưa đưa quy tắc sách này vào tư vấn phòng.','new-sources/wikisource-zhaijing.html; new-sources/REVISIONS.json; TEXT_WITNESS_CHECK.json')
}
held={
 'F01':['v48/evidence/yi/01.html … 64.html','v49/data/yi_research.json','legacy:hhcDeepYi'],
 'T01':['v47/tuvi/sources/quanshu-juan2.html','v50/evidence/quanshu.html','v52/evidence/scans/ (17 ảnh, chỉ vài đoạn đã đọc trực tiếp)'],
 'M01':['legacy:hhc4Data (bảng và lời dẫn, không phải toàn văn Tam Mệnh)'],
 'M04':['legacy:hhc4Data (bảng và lời dẫn)','new-sources/wikisource-yuanhai.html (bản thiếu/có cảnh báo)'],
 'M02':['new-sources/archive-06066037-metadata.json (chỉ metadata)'],
 'P03':['new-sources/wikisource-zhaijing.html','new-sources/KR3g0019-*.txt','new-sources/KR5a0294-*.txt']}
labels={'partial_active':'Dùng một phần, có dấu vết trực tiếp','inherited_rule_claim':'Có quy tắc/lời dẫn kế thừa; nguồn sách chưa chứng minh đầy đủ','research_only':'Đã thu/kiểm thêm, chưa áp vào web','not_established':'Chưa tìm thấy bằng chứng áp dụng'}
def canonical(url):
    u=urlsplit(unquote(url));p=u.path.replace('/zh-hant/','/wiki/').rstrip('/')
    return u.netloc+p+('?' + u.query if u.query else '')
records=[]
for book in catalog:
    id=book['id'];status,scope,evidence=usage.get(id,('not_established','Hồ sơ tham khảo/liên kết; chưa tìm được chuỗi từ chương/đoạn có xác minh tới quy tắc hoặc kết quả V53.','legacy:BOOKS/'+id))
    if id=='F03' or id=='M05':scope='URL là cổng Khoa học kỹ thuật chung, không định danh một bản sách; không thể tính là toàn văn đã có.'
    if id in ['P01','P02','P05','P06']:scope+=' Tư liệu hình thế/âm trạch không tự chuyển thành lời tư vấn phòng trong nhà hiện đại.'
    if id in ['N01','N02','N03']:scope+=' Ngoài năm công cụ hiện tại; chỉ lưu tư liệu lịch sử, không suy tính cách từ mặt người dùng.'
    records.append({**book,'resourceKind':kinds[id],'currentStatus':status,'scope':scope,'evidence':evidence,'localPossession':held.get(id,['Liên kết/lời dẫn danh mục; chưa tìm được bản gốc trong lần rà soát này']),'wholeWorkApplied':False,'inheritedAccessLabelIsVerified':False})

source_records=[]
matches={
 'SRC_M_01':'rule_audited_partial_active','SRC_T_01':'rule_audited_partial_active','SRC_T_03':'editorial_paraphrase_partial',
 'SRC_M_02':'inherited_claim_without_original','SRC_M_03':'inherited_method_with_later_calendar_checks',
 'SRC_M_04':'inherited_text_without_facsimile','SRC_T_02':'catalogue_only','SRC_B_01':'catalogue_only',
 'SRC_B_02':'inherited_rule_claim','SRC_B_03':'later_official_data_audited',
 'SRC_B_04':'inherited_rule_claim_new_quality_warning','SRC_Q_01':'partial_active_text_collated','SRC_Q_02':'partial_active_text_collated',
 'SRC_Q_03':'separate_school_not_implemented','SRC_Q_04':'separate_school_not_implemented','SRC_Q_05':'inherited_mapping_reference'}
for source in legacy_sources:
    source_records.append({**source,'auditStatus':matches[source['id']],'legacyVerifiedFieldIsHistoricalClaim':True,'wholeWorkApplied':False})

embedded={k:{'type':type(v).__name__,'topKeys':list(v) if isinstance(v,dict) else None,'items':len(v) if isinstance(v,list) else None} for k,v in blocks.items()}
probe=json.loads((out/'RUNTIME_PROBE.json').read_text(encoding='utf-8'))
yi=blocks['hhcDeepYi'];old_hao=sum(len(x.get('hao',[])) for x in yi['hexagrams'])
assert len(yi['hexagrams'])==64 and old_hao==384
for f in probe['files']:assert sha((root/f['file']).read_bytes())==f['sha256']
nds=json.loads((out/'new-sources/MANIFEST.json').read_text(encoding='utf-8'))
for f in nds['files']:
    if 'sha256' in f:assert sha((out/'new-sources'/f['file']).read_bytes())==f['sha256']
source_bytes=sum(f.get('bytes',0) for f in nds['files'] if f.get('usable'))
manifest52=json.loads((workspace/'v52/evidence/source_manifest.json').read_text(encoding='utf-8'))
old_verified=[]
for f in manifest52['files']:
    if '/scans/' in f.get('file',''):
        p=workspace/'v52'/f['file'];assert sha(p.read_bytes())==f['sha256'];old_verified.append(f['file'])
collated=json.loads((workspace/'v49/data/yi_research.json').read_text(encoding='utf-8'))
manifest48=json.loads((workspace/'v48/evidence/yi_manifest.json').read_text(encoding='utf-8'))
entries=manifest48.get('files',manifest48.get('downloads',[])) if isinstance(manifest48,dict) else manifest48
yi_verified=[]
for f in entries:
    name=f.get('file','')
    if name and 'sha256' in f:
        p=workspace/'v48'/name
        if p.exists():assert sha(p.read_bytes())==f['sha256'];yi_verified.append(name)

runtime_text=(root/'app.js').read_text(encoding='utf-8')
features=[
 {'id':'yi','title':'Kinh Dịch','active':'64 quẻ, quẻ biến, hào động; lời gợi mở biên tập.','storedButInactive':'64 quái từ/384 hào từ; 54 mục từ; bảng hiệu khảo 377 trùng và 7 khác dạng.','gap':'Diễn giải riêng theo văn bản từng hào; dịch/chú giải theo nhân chứng.','evidence':['v53/scripts/extract-yi.mjs','v53/yi-content.js','v53/app.js','v49/data/yi_research.json']},
 {'id':'bazi','title':'Bát tự','active':'Trụ năm/tháng/ngày/giờ, Nhật chủ và hành chính; Thập thần của can được tính trong dữ liệu.','storedButInactive':'Đọc Thập thần, tàng can đầy đủ, các quy tắc đại vận và đồng hồ Mặt Trời ở bản nghiên cứu cũ.','gap':'Bản đọc chưa phản ánh hết dữ liệu; cách cục/dụng thần chưa có căn cứ hiệu khảo đủ.','evidence':['v53/engine.js/baziCalcData','v53/engine-runtime.js/bazi','v53/app.js','v47/research/bazi.md','v48/RESEARCH_REPORT_V48.md']},
 {'id':'tuvi','title':'Tử vi','active':'12 cung, 52 sao trong đầu ra mẫu thực thi, các cờ; 14 chính tinh có mô tả; liên kết cung đối diện.','storedButInactive':'Các lớp vận hạn/Phi Hóa/đối chiếu và một số chức năng của bản nghiên cứu cũ; thuộc tính daHanStart còn trong cung.','gap':'Luồng vận hạn chưa có trên V53; luận tổ hợp sao/độ sáng chưa hiệu khảo toàn sách.','evidence':['v53/engine.js','v53/content.js','v53/app.js','v50/data/rule_text_audit.json','v52/data/facsimile_collation.json']},
 {'id':'home','title':'Phong thủy nhà ở','active':'Cung phi/tám hướng và 7 gợi ý khu vực theo quan sát; phân biệt phương vị/hướng.','storedButInactive':'Phần lớn thư mục phong thủy; Trạch Kinh mới thu dùng nghiên cứu; không có mặt bằng có kích thước.','gap':'Chưa áp toàn sách Bát Trạch/Trạch Kinh, Phi tinh hay chọn vị trí phòng bằng tọa hướng thực.','evidence':['v53/home-content.js','v53/home-guide.js','v53/research/home/RESEARCH_NOTES.md','v53/research/library-audit/NDL_ENGINE_COMPARISON.json']},
 {'id':'other','title':'Các nhánh khác','active':'Chưa có công cụ riêng.','storedButInactive':'Mai Hoa, Lục Hào/Nạp Giáp, trạch nhật, Kỳ Môn, Lục Nhâm, Thái Ất; nhiều mục mới là URL.','gap':'Không trộn thành phương pháp hiện tại; trước tiên xác định phạm vi, bản sách và quy tắc kiểm thử.','evidence':['legacy:BOOKS/B01-B03,L01-L02,S01-S03','legacy:hhc4Data/modules/boique/separate_schools']}
]
report={'schema':'hhc.library.coverage-audit.v1','date':'2026-10-25','conclusion':'NOT_ALL_APPLIED','scope':'All 40 legacy BOOKS records, all 16 linked module source records, embedded source/rule blocks, later archived evidence and actual V53 runtime/UI routes. Absence means no traceable evidence found in this workspace, not proof a rule has never been read. This is not a percentage of all knowledge in these books.','legacyInput':{'file':str(legacy.relative_to(workspace)),'sha256':sha(legacy.read_bytes())},'counts':{'catalogueRecords':len(catalog),'moduleSourceRecords':len(legacy_sources),'canonicalCatalogueURLs':len(set(canonical(x['url']) for x in catalog)),'status':dict(Counter(x['currentStatus'] for x in records)),'embeddedHexagrams':len(yi['hexagrams']),'embeddedLineTexts':old_hao,'activeActualLineTexts':0,'newUsableHTTPBodies':sum(bool(f.get('usable')) for f in nds['files']),'newFailedHTTPBodies':sum(not f.get('usable') for f in nds['files']),'newUsableBytes':source_bytes,'olderScanFilesHashChecked':len(old_verified),'olderYiFilesHashChecked':len(yi_verified)},'resourceKinds':dict(Counter(kinds.values())),'features':features,'catalogue':records,'moduleSources':source_records,'embeddedBlocks':embedded,'notes':['F02 and X04 duplicate one CText URL. F03 and M05 point to the same general portal after language-path normalization.','Linked access labels such as Toàn văn were not promoted to possession or completed review.','No record is marked as an entire work fully implemented. Reliable provenance is separate from predictive validity.','The 16 source records overlap with the 40 catalogue entries and must not be advertised as 56 different books.']}
(out/'COVERAGE.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(out/'LEGACY_CATALOGUE.json').write_text(json.dumps({'books':catalog,'moduleSources':legacy_sources},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
md=['# Ma trận kiểm kê và sử dụng kho sách','', 'Ngày 25/10/2026. **Chưa áp dụng hết.** Đây là hồ sơ nội bộ, không phải nội dung trang người dùng.','', '40 hồ sơ danh mục và 16 lời dẫn nguồn của mô-đun được rà riêng; có trùng lặp và nhiều mục không phải sách. Không đo tỷ lệ kiến thức bằng số URL.','', '| ID | Hồ sơ | Loại tài nguyên | Mức sử dụng V53 | Phạm vi / phần còn thiếu |','| --- | --- | --- | --- | --- |']
for x in records:md.append('| '+ ' | '.join([x['id'],f"[{x['title_vi']}]({x['url']})",x['resourceKind'],labels[x['currentStatus']],x['scope'].replace('|','/')] )+' |')
md+=['','## 16 nguồn mô-đun kế thừa','', 'Trường `verified` cũ chỉ được giữ làm lời ghi nhận lịch sử; không tự nâng thành byte hoặc hiệu khảo toàn văn.','', '| Mã | Nguồn | Kết quả rà |','| --- | --- | --- |']
for x in source_records:md.append(f"| {x['id']} | {x['title_vi']} | {x['auditStatus']} |")
md+=['','## Khoảng trống theo công cụ','', '| Công cụ | Đang dùng | Có trong kho / còn thiếu trên web |','| --- | --- | --- |']
for x in features:md.append(f"| {x['title']} | {x['active']} | {x['storedButInactive']} {x['gap']} |")
md+=['','Dấu vết tệp, các khối dữ liệu nhúng và số đếm có thể tái lập trong `COVERAGE.json`, `LEGACY_CATALOGUE.json`, `RUNTIME_PROBE.json`. Mọi mô tả “chưa tìm thấy” chỉ có giá trị trong workspace đã rà.']
(out/'COVERAGE.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
print(json.dumps(report['counts'],ensure_ascii=False,indent=2))
