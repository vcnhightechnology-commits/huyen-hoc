from pathlib import Path
import json

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/bazi-yangren-conditions';q=r/'qa/bazi-yangren-conditions'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
qa=read(q/'RESULTS.json');src=read(q/'SOURCE_RESULTS.json');coord=read(q/'COORDINATE_RESULTS.json')
assert len(qa['checks'])==6 and all(x['ok']for x in qa['checks'])and len(coord['checks'])==5 and all(x['ok']for x in coord['checks'])
report='BAZI_YANGREN_CONDITIONS_REPORT.md'
step=('Tam Mệnh quyển5 mục Dương Nhận: tiếp nhận21vịtrí198–218 từ staging(13đọclầnđầu mới vào gói/8đọc mở rộng trước),nhịp này đối mục tiêu8ảnh cũ;0HTTP/container/trangnguồn mới. '
 '55ngữ cảnh biên tập phủ3467codepoint gồm15đề mục/3452thân,UTF16là3474;khôngđồngnghĩa áp hết điều kiện. '
 'Tách8ngữ cảnh hỗn hợp thành59tiểuđoạn/1180codepoint và28phép kiểm tiềnđề riêng:6tọađộ tự xác định/55khái niệm chỉ nhận khai báo nghiên cứu,chưacóthướcđo vượng suy. '
 '6kiểm mới đạt/81ngữ cảnh ba giá trị,2HHC thật dựng lại2ví dụ218 cho phép chiếu mới;giữ kết quả thực tếnull. '
 '5kiểm tọa độ kế thừa giữ10nhãn ngày3/3/4 và8cặp ngày–giờ phủđịnh,8HHC/8lunarforward sau60lunarsearch,196tracứu riêng;2ví dụ218 đã có2HHC/lunar-feasibility riêng trước,khôngcộnglượt lặp thành vídụ mới. '
 '21ảnhSHA/13RGBA/2buffer giải mã lại/2crop khớppixel. Giữ AND/ORchưa rõ,nhánh Ấn cóthểthu hẹp lời trước,官旺 khác無官;khôngtựchọn độ ưu tiên/hiệu lực/kết quả. HTML/site/ZIPweb nguyên byte,toàn kho active.')
nexts=[
 'Dương Nhận:55ngữ cảnh có xử trí;8ngữ cảnh hỗn hợp đã tách59tiểuđoạn/28phép kiểm tiềnđề,còn47ngữcảnh vàcácmệnhđềphụ chưa mãhóa đầy đủ. Khônglặp8cặp/10nhãn/2vídụ/81ngữcảnh đãđạt nếu logic/nguồn khôngđổi.',
 'Cần định nghĩa truyền bản/đơn vị đo cho旺弱/有氣/多/微/有效合化制,ranh nguyêncục–tuế–vận và độ ưu tiên. Giữ sourceReadingResolved=false cho AND/OR傷官財星;chữ亥中午/壬水 và巳/己 tronglời giải chưa tựphục nguyên. 官旺 và無官 không là phủđịnh nhau;không dùng else đểchọn vận.',
 'Các mục KiếnLộc44ngữcảnh/Lộc28ngữcảnh và9mục cách khác vẫn chưa fullcompiler;nguồn cùngWYG không thànhnhânchứng độc lập. B02 map47khoảngđọclầnđầu/81chỉđềmục/chương50mở263,tiếp264;B03/MaiHoa/chữmở còn. Tửvi火鈴星/CanhNhâm/khởihạn vàNhàởPhiTinh/lịch/Bắc thực/đồ49mộtbộtháng cònmở.',
 'Ứng viên UI KiếnLộc vẫn riêng do browser bị vôhiệu hóa,khôngvượtsetting. Nguồn/corpus/suyluận/QA ngoài site;khôngxuấtbản mạng. Danhmục40/whole0,bốn lĩnhvực active;khôngtuyênbốhếtkho.'
]
write(b/'WORK_STATE.json',{'date':'2026-10-28','status':'source-span-and-bounded-predicate-audits-verified-full-conditions-active','latestReport':'v53/'+report,'completedStep':step,
 'summary':qa['summary'],'inheritedCoordinateSummary':{k:coord[k]for k in['actualLunarSearchEightCharCalls','actualLunarForwardEightCharCalls','actualHHCBaziCalls','sourceDayHourExamples','sourceDaySetEntries','privateCoordinateLookups']},
 'sourceVerification':src,'sourceUnitMap':'v53/research/bazi-yangren-conditions/CURRENT_PATTERN_READING_MATRIX.json','next':nexts,'consumerChanged':False,'fullConditionalClassifier':False,'strengthMethodValidated':False,'sourceOutcomesValidated':False,'wholeCatalogueCompleted':False})
d=read(w/'EXHAUSTIVE_WORK_STATE.json');d['date']='2026-10-28';d['currentWork'].update(catalogueID='M01',relatedCatalogueIDs=['M01'],work='三命通會卷五 — 陽刃條件、例外與具名規則範圍',
 reason='Separate literal blade coordinates from conditional source claims, explicit unknown strength and competing source scopes before any consumer interpretation.',sourceDirectory='v53/research/bazi-yangren-conditions',
 currentStep=step,latestResearchReport='v53/'+report,functionalBacklog='v53/research/bazi-yangren-conditions/WORK_STATE.json',internalYangrenPredicateReference='v53/research/bazi-yangren-conditions/predicate-reference.mjs',
 currentPatternMatrix='v53/research/bazi-yangren-conditions/CURRENT_PATTERN_READING_MATRIX.json',sourceLimits='21first-passpositions/55editorialcontexts;8deepenedcontexts/59subcontexts/28localpredicateaudits.Only6day/hourfactsderived;55researchdeclarationconcepts not source-strengthalgorithm or validatedoutcomes.',
 nextSourceLead={'sourceID':'M01-yangren-full-conditions','status':'47editorialcontexts-plus-subordinate-premises-and-voices-active','file':'v53/research/bazi-yangren-conditions/CONTEXT_REVIEW.json','remaining':' '.join(nexts)})
d['inProgressScope']='v53/research/bazi-yangren-conditions/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in[w/'EXHAUSTIVE_WORK_STATE.json',r/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=r/'research/full-study/WORK_STATE.json';d=read(p);d['date']='2026-10-28';d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts);item=next(x for x in d['items']if x['id']=='bazi')
if step not in item['completed']:item['completed'].append(step)
if ' '.join(nexts)not in item['remaining']:item['remaining'].append(' '.join(nexts))
item['latestScope']='../bazi-yangren-conditions/WORK_STATE.json';write(p,d)
p=r/'research/library-current/COVERAGE.json';d=read(p);d['date']='2026-10-28';entry=next(x for x in d['catalogue']if x['id']=='M01');entry['latestYangrenConditionalStudy']=step
for f in['v53/'+report]+['v53/research/bazi-yangren-conditions/'+n for n in['WORK_STATE.json','SOURCE_MANIFEST.json','MANUAL_READINGS.json','CONTEXT_REVIEW.json','SELECTED_SUBCONTEXTS.json','SOURCE_COORDINATES.json','PREDICATE_MATRIX.json','CURRENT_PATTERN_READING_MATRIX.json','coordinate-reference.mjs','predicate-reference.mjs']]+['v53/qa/bazi-yangren-conditions/'+n for n in['RESULTS.json','SOURCE_RESULTS.json','COORDINATE_RESULTS.json','SOURCE_EXAMPLES_PROBE.json','DECODE_RESULTS.json']]:
 if f not in entry['currentEvidence']:entry['currentEvidence'].append(f)
d['latestFollowup']=report+': '+step;d['latestAcquisitionCounts']={'scope':report,'newHTTPRequests':0,'newOriginalContainers':0,'newSourcePositionsThisHeartbeat':0,'inheritedFirstReadPositionsPromoted':13,'inheritedExpandedPriorPositions':8,'currentScopeTargetedRereadPositions':8,'editorialContexts':55,'selectedSubcontexts':59,'selectedCodepoints':1180,'localPredicateAudits':28,'wholeWorksApplied':0}
d['counts']['newDownloadsThisScope']=0;d['counts']['newDownloadsThisScopeBasis']='Promoted priorstaging13first-read PNGs/8priorpositions;thisscope reread8positions.Newpredicatefunction,0HTTP/container/newsourceposition.'
assert d['counts']['catalogueRecords']==40 and d['counts']['wholeWorkApplied']==0;write(p,d)
note='Mốc Bát tự — Dương Nhận: điều kiện, ngoại lệ và phạm vi, 28/10/2026: `'+report+'`. '+step+'\n\n'
for p in[w/'PROJECT_RESEARCH_STATE.md',r/'NEXT_STEPS.md',r/'research/library-current/COVERAGE.md']:
 t=p.read_text(encoding='utf-8-sig')
 if not t.startswith(note):p.write_text(note+t,encoding='utf-8')
p=w/'PENDING_RESEARCH_STATE.json';d=read(p);d.update(date='2026-10-28',status='Bazi-yangren-conditions-current-scope-active',workDirectory='v53/research/bazi-yangren-conditions',currentWorkState='v53/research/bazi-yangren-conditions/WORK_STATE.json',latestReport='v53/'+report,next=nexts,consumerChanged=False,wholeCatalogueCompleted=False)
if'inProgressStaging'in d:d['previousStaging']={**d.pop('inProgressStaging'),'status':'promoted-to-v53-bazi-yangren-conditions-fullconditions-active'}
write(p,d)
(r/report).write_text('''# Dương Nhận: điều kiện, ngoại lệ và giới hạn của phép tra

Ngày 28/10/2026. Đã tiếp nhận khoảng đọc đầu mục 論陽刃, giữ riêng các loại Nhận và bổ sung bộ kiểm tiền đề có ba giá trị. Đây là công cụ nghiên cứu nội bộ; chưa phải bộ nhận diện trọn cách cục hoặc phương pháp vượng suy đã xác lập. Web giữ nguyên byte.

## Nguồn và độ phủ thực tế

Tái dùng `research/bazi-pattern-witness/CADAL06066041.djvu`,226ảnh,SHA-256`013ce4861680a2bf08b811050c45a45bb2d3ce9d164f7e2341d7070bd5cb2c1a`;bản số WYG quyển5 SHA`1ebdd92feaa57496b702f962ad6fafd4f19c17e98c38a94b40f626ef321dd997`. Hồ sơ byte/TLS/giải mã trước giữ nguyên. Cùng họ WYG không trở thành hai nhân chứng độc lập.

21vị trí198–218 được đọc đầu trong staging:13vị trí mới vào gói và8vị trí cũ đọc mở rộng. Nhịp này đối mục tiêu8ảnh204–209/215–216;không cộng thành29trang và không gọi13PNG là13lượt tải mới. Có0HTTP,0container mới,0vị trí nguồn đọc đầu mới trong nhịp tiếp nhận. Hai cropnative204/205 đãxem/so đúngpixel;13PNG khớpRGBA vàhai buffer205/208 được giải mã lại bằng đúng decoder cũ. Không dùng trình duyệt,OCR hoặc nội suy nét.

55ngữ cảnh biên tập phủ3467Unicode codepoint,gồm15đề mục/chỉ dẫn chéo và3452thân phần trích. UTF16 có3474unit,không dùng độ dài này làm offset codepoint. Việc có xử trí cho mọi ký tự của phần bản số không có nghĩa đã đối từng chữ ảnh hoặc mã hóa hết điều kiện. Tám ngữ cảnh hỗn hợp14–17/45–48 được tách thành59tiểuđoạn liên tục,phủ1180codepoint;47ngữ cảnh khác và nhiều tiền đề phụ còn cần khai thác.

## Các chức năng riêng và điều đã sửa trong mô hình

Bảng tọa độ giữ riêng 日刃3ngày,自刃3ngày,飛刃4ngày và8cặp ngày–giờ được lời nguồn phủ định cục bộ. Không ghép các bảng này vào một bảng Nhận mười can,không ghi đè giới hạn năm dương can của bảng thường. `listedCoordinateMatches=false` chỉ là không có trong bảng đang hỏi;không đủ kết luận có/không Nhận trên toàn mệnh. Dạng 巳未 ở bản số được giữ cạnh 己未 ở ảnh208,không sửa byte gốc.

28phép kiểm tiền đề mới giữ rõ tên hệ và tiểuđoạn nguồn. Sáu thông tin chỉ lấy từ tọa độ ngày/giờ chuẩn;55khái niệm còn lại chỉ nhận khai báo nghiên cứu `true/false/null`. Không biến số lượng ngũ hành thành 旺弱,多,微 hay hiệu lực 合/化/制. Một phép kiểm chỉ cho biết tiền đề đã khai báo có khớp một mệnh đề cục bộ;không khẳng định các tiền đề ấy đã được xác minh cho người thật.

Đoạn `若命元有煞刄歲運又逄` dùng chung kết từ `俱發大禍` ở nhánh tiếp theo;nên ghi liên kết hai tiểuđoạn,không đọc một mảnh bị cắt thành quy tắc đủ điều kiện. Nhánh có Nhận/không Sát/gặp Sát vận và nhánh thêm Ấn có thể cùng khớp các dữ kiện khai báo mà mang lời luận khác nhau. Bộ kiểm giữ các nhánh cùng hiện và đánh dấu khả năng thu hẹp,không lấy thứ tự mảng làm độ ưu tiên hoặc tự gọi đây là mâu thuẫn toàn sách.

Cụm `原帶傷官財星` còn hai cách liên kết biên tập AND/OR. Hai cách cho kết quả khác nhau thì trảnull;cùng cho true/false vẫn giữ `sourceReadingResolved=false`. Đây là các khả năng giải cú trong một bản nguồn,chưa phải hai dị bản và không phải phục nguyên chữ bằng engine.

`官旺` khác `無官`:Quan có nhưng yếu có thể không thuộc cả hai nhánh. Bộ kiểm không dùng một nhánh else sau khi kiểm旺 thất bại để tự chọn `申子辰`. Các nhãn vận/đồ nguồn được giữ như nhãn nghiên cứu,không thành lời khuyên đi lại hay kết quả vận hạn. Đoạn ưu tiên nguyệt lệnh/cách khác khi đã thực sự thành cách cũng được giữ riêng;nhãn 日刃 đơn lẻ không đủ loại bỏ nó.

Các lời về bệnh,tử vong,ngoại hình,đạo đức,người thân,tài sản và địa vị là lời truyền thống của nguồn,chưa được xác nhận về kết quả thực tế. Không dùng chúng để dựng bộ dự báo sức khỏe,hôn nhân,tuổi thọ hoặc tài chính. Chữ `亥中午/壬水` và 巳/己 trong lời giải tàng can còn giới hạn đọc;không sửa ảnh/bản số theo bảng tàng can hiện đại.

## Kiểm chứng và giới hạn của số ca

Sáu kiểm mới đạt. 81ngữ cảnh khai báo ba giá trị được so với phép liệt kê các hoàn tất Boolean,kiểm unknown khác false và trường hợp nhánh hẹp chưa biết. Hai ví dụ in218 được thực thi HHC thật cho phép chiếu mới,khớp cả bốn trụ;chỉ tọa độ được xác lập,`火多`,vượng suy,thành cách,chế hóa và kết quả vẫnnull. Đây là dựng lại hai ví dụ đã có,không thêm hai người hay hai ca ứng nghiệm mới.

Năm kiểm tọa độ kế thừa đã đạt trước khi tiếp nhận:8HHC/8lunarforward sau60lunarsearch cho8cặp phủ định,196tracứu riêng cho8cặp và10nhãn ngày. Hai ví dụ218 trước đó có2fromBaZi/2EightChar/2HHC để tìm dữ liệu lịch khả thi. Các lượt thực thi được ghi theo từng mục đích,không cộng các lần dựng lại thành số ví dụ nguồn khác nhau. Không gán ngày dương tìm được cho nhân vật lịch sử hoặc xác nhận ứng nghiệm.

Hai module thực thi và dữ liệu phép kiểm được tiếp nhận đúng byte từ staging đã kiểm;sau khi chuyển thư mục,đã kiểm cú pháp hai script và nạp module để xác nhận28hàng với dữ kiện chưa khai báo giữnull. Các tệp QA gốc được bảo toàn. Xác minh nguồn đối21ảnhSHA,13RGBA,2buffer giải mã lại,2crop đúngpixel,các offset và toàn bộ liên kết tiểuđoạn. Không lặp lại các kiểm tọa độ cũ khi logic không đổi.

## Gói và phần tiếp

Snapshot `archives/v53-before-bazi-yangren-conditions/` giữ gói đã đối3476tệp/sourceZIP2070081817byte. HTMLroot/V53/site707411byte/SHA`549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`,ZIPweb344047byte giữ nguyên. Site chỉ cóindex.html;nguồn/corpus/suy luận/QA ngoài site. Ứng viênUI KiếnLộc vẫn riêng vì browser bị vô hiệu hóa;không dùng kiểm chuỗi thay kiểm hiển thị và không vượt setting.

Tái kiểm phần mới:`node v53/scripts/test-bazi-yangren-predicates.mjs`;nguồn:`node v53/scripts/redecode-bazi-yangren.mjs` rồi `python v53/scripts/verify-bazi-yangren-sources.py`;đối gói cuối:`python v53/scripts/verify-bazi-yangren-release.py --no-write`. Tệp release dự kiến chỉ là dự kiến đến khi lần đối gói cuối thành công.

Tiếp47ngữ cảnh chưa tách sâu,các tiền đề phụ của59tiểuđoạn,giọng dẫn và phương pháp vượng suy/hiệu lực/ranh tuế-vận;không lặp fixture cũ để tăng số. Chín mục cách khác,KiếnLộc/Lộc,Tử vi dị bản/khởi hạn,Nhà ở Phi Tinh/lịch/đo Bắc vàB02 từ264/B03/Mai Hoa vẫn còn mở. Danh mục40có0sách được tuyên bố áp dụng trọn;không coi khép khoảng đọc đầu một mục là hết kho.
''',encoding='utf-8')
print('Yangren source promotion and bounded predicate audits recorded;fullconditions andfourdomains remainactive.')
