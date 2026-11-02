from pathlib import Path
import json
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/home-source-tables';read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='HOME_SOURCE_TABLES_REPORT.md';qa=read(r/'qa/home-source-tables/RESULTS.json');src=read(r/'qa/home-source-tables/SOURCE_RESULTS.json')
assert len(qa['checks'])==9 and all(x['ok']for x in qa['checks'])and src['manualGlyphs']==384
step=('Nhà ở: hoàn thiện bộ riêng25 dòng mộ vận (20 cơ sở/5 sau Đông chí),480 ngữ cảnh và phép khắc có điều kiện xây mới/sửa nền. '
 'Đối8 nhóm ví dụ in/13 trụ ứng viên/312 so sơn với28 lá số lunar1.8.6 thật;64 quẻ/384 nét hào đọc trực tiếp khớp64 HHC hexNumber thật vàvị trí Bát cung. '
 '9 kiểm đạt;65 mẫu pixel không rõ giữlượtđọc tay,319 mẫu rõkhớp,64 crop/2sheet/2xoayQA. '
 '13 trangđọcmởrộng,0HTTP/container/trangnguồnmới. Giữ62 tênliteral+1alias无/無 đã khai báo+1恒/恆. '
 'Sửa ghi chú nghiên cứu冠/crown thành尅 (khắc),khôngsửa nguồn/web. HTML707411byte/site/ZIPweb nguyên;toànkho chưahoàntất.')
nexts=[
 'Xieji sourcecoordinates25rows,constructionapplicability and384lineglyphs complete in boundedprivate scope; do not repeat480contexts/64figures withoutnewlogic. Modern date→sourceyearstem/solsticephase adapter, exact49diagramcells andotherquotedconditions remain open.',
 'Prioritize full middle/seam needle pairedmountain tables, explicithalfposition offsets,三合group membership andsourceuse(龍versus砂水); separate tables from regular/Hongfan before any newconsumerfeature.',
 'P03WYG/HFL sixdigitalartifacts/14editorialgroups stillnotfacsimile,missingdiagrams/26versus24/sourceprohibition/monthandleapboundary/HFL1988metadata open;threefailedURLsnotimmediatelyretried.',
 'Bazi fullpatternconditions/crossrefs,Tuvi independentwitness/Canh-Nhâm/ageboundaries,Yi B02chapter35from191/B03/MaiHoa clauses remain active. Forty fixedcataloguewhole0. Researchoutsideconsumer site.'
]
units=read(r/'research/home-you-nian/VOLUME_UNIT_MAP.json');units['previousMap']='v53/research/home-you-nian/VOLUME_UNIT_MAP.json';units['latestScope']='v53/research/home-source-tables/WORK_STATE.json'
for x in units['units']:
 if x['id']=='XJ2-06':x['disposition']='20base+5solstice coordinate rows,explicitfiveZi/NaYin mechanism andunknownphase handling compiled;source41diagramcells/quotedvoices/moderndateadapter notfull.'
 if x['id']=='XJ2-07':x['disposition']='尅 (overcoming),constructionapplicability,8printedexamplegroups/13pillars andday/hourconditionalextension compiled;49diagramallcells andmodernadapter open. Supersedesoldcrownmisreading.'
 if x['id']=='XJ2-12':x['disposition']='64names and384lineglyphs directlycollated withcrop/nativepixels;all64sourcepalace/stage structuresmatch. Remainingfullapplication/quotedclauses notclosed.'
units['nextAtomicWork']=nexts;write(b/'CURRENT_VOLUME_UNITS.json',units)
write(b/'WORK_STATE.json',{'date':'2026-10-27','status':'bounded-source-coordinate-functions-and384glyphs-verified-rest-active','latestReport':'v53/'+report,'completedStep':step,
 'summary':qa['summary'],'sourceVerification':src,'next':nexts,'sourceUnitMap':'v53/research/home-source-tables/CURRENT_VOLUME_UNITS.json','consumerChanged':False,'calendarAdapterEstablished':False,'wholeCatalogueCompleted':False})
d=read(w/'EXHAUSTIVE_WORK_STATE.json');d['currentWork'].update(catalogueID='P03',relatedCatalogueIDs=['P03'],work='欽定協紀辨方書卷二 — mộ vận/khắc sơn gia và Bát cung',
 sourceDirectory='v53/research/home-source-tables',currentStep=step,latestResearchReport='v53/'+report,functionalBacklog='v53/research/home-source-tables/WORK_STATE.json',
 internalHomeTombReference='v53/research/home-source-tables/tomb-reference.mjs',internalHomeFigureReference='v53/research/home-source-tables/eight-palace-reference.mjs',
 sourceLimits='Complete384glyph/64figure structuralcollation andbounded25movementrows only;notall110pageclauses/P03facsimile/moderncalendarorwholecatalogue.',
 nextSourceLead={'sourceID':'Xieji-volume2-middle-seam-rings','status':'allpairedcoordinates-anduses-open','file':'v53/research/home-source-tables/CURRENT_VOLUME_UNITS.json','remaining':' '.join(nexts)})
d['inProgressScope']='v53/research/home-source-tables/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in[w/'EXHAUSTIVE_WORK_STATE.json',r/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=r/'research/full-study/WORK_STATE.json';d=read(p);d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts);item=next(x for x in d['items']if x['id']=='home');item['completed'].append(step);item['remaining'].append(' '.join(nexts));item['latestScope']='../home-source-tables/WORK_STATE.json';write(p,d)
p=r/'research/library-current/COVERAGE.json';d=read(p);entry=next(x for x in d['catalogue']if x['id']=='P03');entry['latestRelatedIndependentSourceScope']=step
for f in ['v53/'+report]+['v53/research/home-source-tables/'+n for n in ['WORK_STATE.json','CURRENT_VOLUME_UNITS.json','MANUAL_READINGS.json','MANUAL_FIGURES.json','FIGURE_NAMES.json','TOMB_MOVEMENT_ROWS.json','OVERCOMING_RULE.json','tomb-reference.mjs','eight-palace-reference.mjs']]+['v53/qa/home-source-tables/RESULTS.json','v53/qa/home-source-tables/SOURCE_RESULTS.json']:
 if f not in entry['currentEvidence']:entry['currentEvidence'].append(f)
d['latestFollowup']=report+': '+step;d['latestAcquisitionCounts']={'scope':report,'newHTTPRequests':0,'newOriginalContainers':0,'newSourcePages':0,'expandedPreviouslyReadPages':13,'nativeQACrops':64,'nativeScaleContactSheets':2,'losslessRotations':2,'manualGlyphs':384,'sourceBaseRows':20,'sourceSolsticeRows':5,'wholeWorksApplied':0}
d['counts']['newDownloadsThisScope']=0;d['counts']['newDownloadsThisScopeBasis']='Allsourcecontainers/pages retained;13expandedreadings,68localQAderivatives,noHTTPorneworiginal.';assert d['counts']['wholeWorkApplied']==0;write(p,d)
note='Mốc nhà ở–Bảng nguồn và nét hào, 27/10/2026: `'+report+'`. '+step+'\n\n'
for p in[w/'PROJECT_RESEARCH_STATE.md',r/'NEXT_STEPS.md',r/'research/library-current/COVERAGE.md']:
 t=p.read_text(encoding='utf-8-sig')
 if p.name=='PROJECT_RESEARCH_STATE.md'and t.startswith('Phần nối tiếp đã chuẩn bị ngoài gói:'):t=t.split('\n\n',1)[1]
 p.write_text(note+t,encoding='utf-8')
write(w/'PENDING_RESEARCH_STATE.json',{'date':'2026-10-27','status':'Home-source-tables-current-scope-active','workDirectory':'v53/research/home-source-tables',
 'currentWorkState':'v53/research/home-source-tables/WORK_STATE.json','latestReport':'v53/'+report,'next':nexts,'consumerChanged':False,'wholeCatalogueCompleted':False})
(r/report).write_text('''# Nhà ở: mộ vận, khắc sơn gia và đủ384 nét hào Bát cung

Ngày27/10/2026. Chín kiểm chức năng/nguồn đạt, cùng kiểm pixel từng crop. HTML/site/ZIPweb giữ nguyên. Đây là bộ tham chiếu riêng có điều kiện, chưa là tư vấn chọn ngày hoặc bố trí phòng trên web. Bốn hướng và toàn40 nguồn vẫn chưa hoàn tất.

## Căn cứ và điều kiện

Dùng lại container欽定協紀辨方書卷二/CADAL06056503,3.433.014byte/SHA-256`bfd3b76c55d62324919ab161c8c2ba2ecb129b3b2c59a3ab0428807e8f8278db`.0HTTP/container/trang nguồn mới. Mở rộng13 ảnh đã đọc:41–47,49–52,107–108; giữ SHA ảnh gốc.64crop native,2sheet ở tỉ lệ native,2ảnh xoay90° không nội suy phục vụ đối chữ. Không OCR hoặc chỉnh nguồn.

Đã chép20 hàng cơ sở theo năm cặp can甲己/乙庚/丙辛/丁壬/戊癸 và bốn nhóm墓辰/戌/未/丑, cùng5 ngoại lệ sauĐông chí của nhóm kim. Chương nói đến五子元遁 và納音; công cụ tính trụ mộ từ can năm nguồn và chi mộ, giữ hành/khắc theo bảng in. Trong480 ngữ cảnh24sơn×10can×2pha,40 vị trí nhóm kim đổi giữa hai pha. Thiếu pha nhóm kim trảnull cùnghai phương án, không tự chọn. Đây là đầu vào truyền thống tường minh, **không là bộ đổi ngày hiện đại**, không xác nhận năm cung phi đổiĐông chí.

Ảnh50–52 phân biệt xây nhà mới/lập mộ mới với sửa dựng không động nền hoặc phụ táng mộ cũ. `sourceOvercoming` giữ khả năng áp dụng của bối cảnh tách khỏi quan hệ hành; thiếu bối cảnh giữnull, loại trừ thìfalse. Người dùng không bị ép kết luận từ một quan hệ chưa đủ tiền đề. Các chữ忌/尅 là phân loại của nguồn, không chứng minh kết quả thực tế.

**Sửa một cách đọc trong ghi chú trước:** chữ ở tiêu đề/nội dung là尅/克, nghĩa khắc; “冠/crown” trong một số ghi chú nghiên cứu cũ là đọc nhầm, không phải một thuật ngữ hay dị bản. Dữ liệu nguồn và báo cáo lịch sử giữ nguyên byte; báo cáo này thay thế cách diễn giải đó. Sản phẩm trước không dùng thuật toán này nên không có lỗi kết quả người dùng cần sửa.

Đủ8 nhóm ví dụ chữ in với13 trụ ứng viên: năm甲子; các tháng丙寅/丁卯,戊辰/己巳,庚午/辛未,壬申/癸酉,丙子/丁丑; năm壬申 trước/sauĐông chí.28 lá số lunar-typescript1.8.6 thật (20 trụ mộ và8 trụ ứng viên khác nhau sau tái dùng cache) khớp tọa độ/nạp âm.312 so sơn trong ví dụ khớp, gồm trường hợp **không có sơn bị khắc**; không biến mọi đầu vào thành kết luận bất lợi. Phần日尅/時尅 được nguồn nói làm tương tự, chỉ hỗ trợ phép so khi đã cung cấp nạp âm và bối cảnh, không dựng lịch.

## Đối đủ hình Bát cung

Ảnh107–108 đã chép đủ64 tên và **384 nét âm/dương**. Mỗi crop giữ box native/SHA và được xem trực tiếp trong hai sheet; ghi thứ tự trên xuống riêng với đầu vào engine dưới lên. Bộ dò pixel cục bộ chỉ là ứng viên:319 mẫu rõ khớp lượt đọc tay,65 mẫu không rõ được giữnull trong kết quả dò và đọc trực tiếp; không lấy đáp án engine lấp nét thiếu.

64 lần `HHC_ENGINE.hexNumber` thật cho64 số khác nhau, toàn384 nét phù hợp tên trên ảnh và vị trí cung/giai đoạn. `eight-palace-reference.mjs` lập chỉ mục từ bảng nét đọc trực tiếp, trả đúng64 cung/giai đoạn và hai nhãn Đại/Tiểu Du Niên; không suy dự báo từ quẻ. Thiếu nét giữnull; tên hệ và thứ tự đầu vào bắt buộc.

Giữ kết quả probe tên trước:62 tên trùngliteral,1alias无/無 đã khai báo từ trước,1chỗ恒/恆 cùng tọa độ雷風/số32 được ghi riêng. Không tự sửa chữ nguồn hoặc thay số quẻ để làm tròn số khớp.64 lần probe tên trước và20 lá số probe mộ vận trước lưu riêng, không cộng vào số thực thi của bộ kiểm mới.

## Giới hạn và tiếp tục

Chưa đối toàn bộ chữ nhỏ trên đồ49/41, chưa đóng toàn bộ lời bình/quy tắc ứng dụng trong110 ảnh; chưa có adapter niên can/phaĐông chí/nhuận từ ngày hiện đại. Chưa áp trọnP03 Trạch Kinh hoặc giải quyết ảnh/đồ còn thiếu. Tiếp bảng Trung châm/Phùng châm, các đôi sơn và mục đích龍/砂水; giữ riêng từng hệ trước khi giao chức năng người dùng. Tửvi/Báttự/KinhDịch vẫn có phạm vi mở theo ma trận.

Snapshot trước ở`archives/v53-before-home-source-tables/`:3051tệp,sourceZIP2036215467byte. HTML707411byte/SHA549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857,ZIPweb344047byte; site chỉindex.html. Nguồn vàQA ngoài site, không phát hành mạng hoặc tăng phiên bản. Kết quả cuối ở`qa/home-source-tables/RELEASE_RESULTS.json`.

Tái kiểm: `node v53/scripts/test-home-source-tables.mjs`; `python v53/scripts/verify-home-source-tables-sources.py`; `python v53/scripts/verify-home-source-tables-release.py --no-write`. Bản đồ hiện hành`research/home-source-tables/CURRENT_VOLUME_UNITS.json`; bản đồ12mục trước giữ nguyên byte.
''',encoding='utf-8')
print('Current source-table report/state updated; cataloguewhole0 andconsumerunchanged.')
