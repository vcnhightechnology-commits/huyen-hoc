from pathlib import Path
import json

r=Path(__file__).resolve().parent.parent
w=r.parent
b=r/'research/home-rings'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
qa=read(r/'qa/home-rings/RESULTS.json')
src=read(r/'qa/home-rings/SOURCE_RESULTS.json')
assert len(qa['checks'])==10 and all(x['ok']for x in qa['checks'])
assert src['exactNativeCropsVerified']==2 and src['losslessRotationsVerified']==6
report='HOME_RINGS_REPORT.md'
step=('Nhà ở: đã đọc đủ 96 nhãn trên hai đồ trung châm/phùng châm, 24 cung nối đôi và 15 đoạn văn trong hai mục nguồn; '
      'biên dịch riêng 48 phép gán sơn–hành, ba vòng và mô hình góc tường minh. '
      '10 kiểm đạt: 288 lần gọi HHC_MOUNTAINS thật trong 72 tâm, 72 ranh, 144 phía ranh; thêm 72 khoảng bất định. '
      'Giữ cả hai khả năng tại ranh, tách quy ước phần mềm khỏi lời sách. '
      'Cùng tên sơn: bảng đôi khác Chính ngũ hành 16/24 và Hồng phạm 17/24. '
      '6 ảnh đọc mở rộng, 2 crop native/6 xoay không nội suy; 0 HTTP, container hoặc trang nguồn mới. '
      'Chưa có bộ nối số đo thực/Bắc từ–Bắc thật; nguồn không xác minh hiệu quả thực tế. '
      'HTML 707411 byte, site và ZIP web nguyên byte; toàn kho chưa hoàn tất.')
nexts=[
 'Tiếp Xieji ảnh53–54: đủ24 nhãn tiết khí/phương vị và lời tám tiết; tách tên quẻ Khảm/Chấn/Ly/Đoài khỏi chi Tý/Mão/Ngọ/Dậu. Chưa suy ra thời điểm thiên văn hoặc tự chọn cục Kỳ môn.',
 'Tiếp ảnh55–57: 八卦納甲三合, đủ24 tọa độ thuộc8 quẻ,24 nét tượng và các điều kiện/nguồn trích. Phân biệt nạp giáp địa lý với nạp giáp từng hào; giữ riêng lời phê bình chưa rõ xuất xứ. Không lặp lại288 phép gọi vòng châm khi không đổi logic.',
 'Mộ vận còn đồ41/49 và bộ nối niên can/pha Đông chí từ ngày; lời bình/điều kiện Hồng phạm và các ứng dụng Du Niên chưa khai thác hết. P03 Trạch Kinh vẫn thiếu ảnh/đồ, có vấn đề24/26 và quy ước tháng/nhuận; không tải lại ngay ba URL lỗi đã giữ.',
 'Bát tự còn toàn điều kiện cách cục/vượng suy/dụng thần và nhân chứng; Tử vi còn Canh/Nhâm/tuổi khởi hạn; Dịch còn B02 từ ảnh191/B03/Mai Hoa các mệnh đề phụ. Danh mục40: chưa tác phẩm nào áp dụng trọn.'
]
units=read(r/'research/home-source-tables/CURRENT_VOLUME_UNITS.json')
units['previousMap']='v53/research/home-source-tables/CURRENT_VOLUME_UNITS.json'
units['latestScope']='v53/research/home-rings/WORK_STATE.json'
for x in units['units']:
 if x['id']in['XJ2-03','XJ2-04']:
  x['extractionStatus']='all-available-heading-prose-and-ring-labels-enumerated'
  x['disposition']='All paired labels/arcs, four triads, half-position offsets and source uses compiled privately. Numerical angle/endpoints explicitly derived; field compass/north calibration and practical application not established. Interior crossing paths not all traced.'
  x['wholeUnitApplied']=False
units['nextAtomicWork']=nexts
write(b/'CURRENT_VOLUME_UNITS.json',units)
write(b/'WORK_STATE.json',{'date':'2026-10-27','status':'two-ring-headings-enumerated-bounded-private-functions-verified-rest-active',
 'latestReport':'v53/'+report,'completedStep':step,'summary':qa['summary'],'sourceVerification':src,
 'sourceUnitMap':'v53/research/home-rings/CURRENT_VOLUME_UNITS.json','next':nexts,
 'consumerChanged':False,'physicalCompassAdapterEstablished':False,'wholeCatalogueCompleted':False})

d=read(w/'EXHAUSTIVE_WORK_STATE.json')
d['currentWork'].update(catalogueID='P03',relatedCatalogueIDs=['P03'],work='欽定協紀辨方書卷二 — trung châm, phùng châm và đôi sơn',
 sourceDirectory='v53/research/home-rings',currentStep=step,latestResearchReport='v53/'+report,
 functionalBacklog='v53/research/home-rings/WORK_STATE.json',internalHomeRingsReference='v53/research/home-rings/rings-reference.mjs',
 sourceLimits='Two headings:96 ring labels,24 arcs,15 prose segments and48 paired assignments. Derived ideal geometry is not physical north calibration or verified practical outcome; whole110 pages/P03/catalogue remain open.',
 nextSourceLead={'sourceID':'Xieji-volume2-term-directions-and-geographical-najia','status':'five-retained-pages-located-next-atomic-extraction-open',
 'file':'v53/research/home-rings/CURRENT_VOLUME_UNITS.json','remaining':' '.join(nexts)})
d['inProgressScope']='v53/research/home-rings/WORK_STATE.json'
d['subsequentPriority'][0]=' '.join(nexts)
for p in[w/'EXHAUSTIVE_WORK_STATE.json',r/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)

p=r/'research/full-study/WORK_STATE.json'
d=read(p);d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts)
item=next(x for x in d['items']if x['id']=='home')
item['completed'].append(step);item['remaining'].append(' '.join(nexts));item['latestScope']='../home-rings/WORK_STATE.json'
write(p,d)
p=r/'research/library-current/COVERAGE.json'
d=read(p);entry=next(x for x in d['catalogue']if x['id']=='P03')
entry['latestRelatedIndependentSourceScope']=step
evidence=['v53/'+report]+['v53/research/home-rings/'+n for n in ['WORK_STATE.json','CURRENT_VOLUME_UNITS.json','MANUAL_READINGS.json','DIAGRAM_LABELS.json','SOURCE_CLAUSES.json','PAIRED_ELEMENT_ROWS.json','ANGULAR_MODEL.json','rings-reference.mjs']]+['v53/qa/home-rings/RESULTS.json','v53/qa/home-rings/SOURCE_RESULTS.json']
for f in evidence:
 if f not in entry['currentEvidence']:entry['currentEvidence'].append(f)
d['latestFollowup']=report+': '+step
d['latestAcquisitionCounts']={'scope':report,'newHTTPRequests':0,'newOriginalContainers':0,'newSourcePages':0,
 'expandedPreviouslyReadPages':6,'nativeQACrops':2,'losslessRotations':6,'manualDiagramLabels':96,'manualPairArcs':24,'sourceProseSegments':15,'wholeWorksApplied':0}
d['counts']['newDownloadsThisScope']=0
d['counts']['newDownloadsThisScopeBasis']='All sources retained:6 expanded image readings,2 native crops/6 lossless rotations; no HTTP or new original.'
assert d['counts']['catalogueRecords']==40 and d['counts']['wholeWorkApplied']==0
write(p,d)

note='Mốc nhà ở — Ba vòng châm, 27/10/2026: `'+report+'`. '+step+'\n\n'
for p in[w/'PROJECT_RESEARCH_STATE.md',r/'NEXT_STEPS.md',r/'research/library-current/COVERAGE.md']:
 p.write_text(note+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
write(w/'PENDING_RESEARCH_STATE.json',{'date':'2026-10-27','status':'Home-rings-current-scope-active',
 'workDirectory':'v53/research/home-rings','currentWorkState':'v53/research/home-rings/WORK_STATE.json',
 'latestReport':'v53/'+report,'next':nexts,'consumerChanged':False,'wholeCatalogueCompleted':False})

(r/report).write_text('''# Nhà ở: trung châm, phùng châm và hệ tọa độ đôi sơn

Ngày 27/10/2026. Đã hoàn tất kiểm tra hai mục nguồn trong phạm vi bảng và tọa độ: 10 kiểm chức năng đạt, đối byte/pixel nguồn đạt. Bộ tham chiếu riêng phân biệt ba vòng, tra 48 vị trí sơn–hành trên trung châm/phùng châm và giữ các khả năng tại ranh. Chưa đưa phép này thành tư vấn bố trí phòng hoặc hiệu quả thực tế. Toàn kho và cả bốn hướng nghiên cứu vẫn chưa hoàn tất.

## Chứng cứ đọc trực tiếp

Dùng lại 欽定協紀辨方書卷二/CADAL06056503.djvu, 3.433.014 byte, SHA-256 `bfd3b76c55d62324919ab161c8c2ba2ecb129b3b2c59a3ab0428807e8f8278db`. Sáu ảnh11–16 đã có trong lần đọc trước được đọc mở rộng; không HTTP, container hoặc trang nguồn mới. Hai crop native và sáu bản xoay90/180/270° giữ nguyên pixel, được kiểm lại từ ảnh nguồn. Không OCR, nội suy hoặc lấy đáp án engine để điền chữ.

Đủ96 nhãn của hai vòng trên hai đồ11/13 và24 cung nối đôi được đọc trực tiếp. Đã liệt kê toàn bộ phần văn của hai tiêu đề 中針雙山五行/縫針三合五行 thành15 đoạn, kể cả bốn chữ kết ởảnh16. Các đường tam hợp giao nhau trong tâm hình chưa được lần theo toàn bộ; thành viên bốn nhóm lấy từ lời văn rõ ởảnh14–15, không gọi các đường giao là đã hiệu khảo từng nét.

## Tọa độ và phép tính

Ảnh12: vòng ngoài là chính châm, vòng trong là trung châm; Tý trung châm nằm giữa Nhâm/Tý chính châm, đi trước nửa vị trí; nguồn nói dùng 格龍. Ảnh14–15: Tý phùng châm nằm giữa Tý/Quý chính châm, đi sau nửa vị trí; dùng 消砂納水. Chính châm dùng 定向. Hai vòng trong lệch nhau một vị trí. Lý do đến/đi, khí/chất là giải thích truyền thống được ghi riêng, chưa phải cơ chế thực nghiệm.

Cả hai dùng các đôi壬子、癸丑、艮寅、甲卯、乙辰、巽巳、丙午、丁未、坤申、庚酉、辛戌、乾亥 theo **tên tọa độ của vòng được chọn**. Bốn nhóm sáu sơn: thủy坤申壬子乙辰; mộc乾亥甲卯丁未; hỏa艮寅丙午辛戌; kim巽巳庚酉癸丑. Không có nhóm thổ trong bảng này. Cùng chữ sơn chưa đồng nghĩa cùng hành: bảng đôi khác Chính ngũ hành16/24 và Hồng phạm17/24; các thay tên chi/quẻ khi so Hồng phạm được khai báo rõ.

`pairedElement` yêu cầu tên hệ và vòng; không nhận nhầm chính châm như một tọa độ đôi sơn. `namedCenter`/`ringCoordinates` yêu cầu mô hình góc, vòng, quy ước ranh và bất định tường minh. Mô hình đều24 vị trí, Tý=0°, tăng theo Tý→Quý→Sửu dẫn đến15°/vị trí, trung châm−7,5° và phùng châm+7,5°; **các con số độ là phép dựng hình phần mềm**, không là số độ nguyên văn trong sáu ảnh. Chưa xác định chuẩn Bắc vật lý hoặc phép nối số đo la bàn thực từ đoạn này.

Ví dụ trong mô hình, góc10° cho Quý/kim ở trung châm và Tý/thủy ở phùng châm. Góc0° trung châm chạm Tý/Quý nên giữ cả thủy/kim; góc0° phùng châm chạm Nhâm/Tý cùng đôi thủy nên có thể biết hành dù chưa có một tên sơn duy nhất. Đầu vào chưa biết trảnull; bất định không bị ép thành một kết luận thuận/nghịch. Không gắn dự báo sức khỏe, tiền tài, sự kiện hoặc tự chọn cách bố trí phòng.

## Kiểm chứng và giới hạn

10 kiểm đạt. Đối48 gán sơn–hành; 72 tâm (ba vòng×24),72 ranh,144 phía ranh và72 khoảng bất định. Thực thi **288 lần HHC_MOUNTAINS.inspect thật**, đúng module đang nhúng HTML; đây là đối tọa độ sau phép chuyển vòng đã khai báo, không là288 phép hiệu chuẩn độc lập. Bộ đang dùng có quy ước ranh nửa mở theo chiều kim đồng hồ; tham chiếu riêng cố ý giữ cả hai khi chạm ranh, và kiểm rõ khác biệt quy ước đó. Khoảng180° giữ đủ24 khả năng; 0°/360° đồng nhất. Không cần chạy lại iztro/lịch vì không sửa hai engine đó.

HTML gốc/V53/site707411 byte giữ SHA `549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`; ZIP web344047 byte giữ nguyên, site chỉindex.html. Tài liệu nghiên cứu và bộ tham chiếu ngoài site. Snapshot `archives/v53-before-home-rings/` giữ bản nguồn trước3139 tệp/ZIP2037105170 byte; gói mới và manifest được kiểm từng byte ở`qa/home-rings/RELEASE_RESULTS.json`. Không tăng phiên bản hoặc xuất bản mạng.

Hai tiêu đề đã được liệt kê đủ phần văn/bảng trong phạm vi này; bộ nối phép đo thực và ứng dụng địa lý vẫn mở. Không suy ra đã áp dụng hết cả110ảnh, P03Trạch Kinh hoặc40 hồ sơ. Tiếp bảng tiết khí/phương vị ảnh53–54 và nạp giáp địa lý ảnh55–57; không lẫn nạp giáp theo hướng với nạp giáp từng hào. Mộ vận, Hồng phạm, Du Niên, ba lĩnh vực khác và các nhân chứng còn mở được giữ trong bản đồ hiện hành.

Tái kiểm: `node v53/scripts/test-home-rings.mjs`; `python v53/scripts/verify-home-rings-sources.py`; `python v53/scripts/verify-home-rings-release.py --no-write`. Bản đồ12 mục mới kế thừa mọi kết quả trước ở`research/home-rings/CURRENT_VOLUME_UNITS.json`; lịch sử giữ nguyên byte.
''',encoding='utf-8')
print('Recorded ring source scope, current unit map, report and ongoing backlog; whole catalogue remains incomplete.')
