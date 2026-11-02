from pathlib import Path
import json

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/liuyao-life-context';q=r/'qa/liuyao-life-context'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
qa=read(q/'RESULTS.json');src=read(q/'SOURCE_RESULTS.json');assert len(qa['checks'])==7 and all(x['ok']for x in qa['checks'])
report='LIUYAO_LIFE_CONTEXT_REPORT.md'
step=('B02: tiếp nhận lượt đọc đầu ba khoảng chương36/PDF213–214,37/214–229,38/229–232;39 mới đầu232. '
 '20 vị trí từ staging (19đọc đầu mới vào gói/213đãgiữ),4trang đọc mởrộng mục tiêu;12render đãchuẩnbị/7render cũ đãđọc,0HTTP/PDFgốc mới. '
 '20mệnhđềgiới hạn,7loạicâuhỏi cần phânbiệt và2phépchiếu riêng Thế–Tài–Phúc/Tửtôn hoặc Thế–Quan–Phụ. '
 '7kiểm đạt/2HHC thật cho復→頤/sáunhãnchi-Lụcthân;8192ngữcảnhriêng,21312cạnhsinhkhắc dẫn xuất/24576hàobiến trongcácngữcảnh ấy,khônglàcađộclập. '
 'QA360ảnh215đãxem/2táirenderkhớppixel. Map136/92chỉđềmục/36khoảngđọclầnđầu/7nềnmộtphần/1mộtphần39/0áphết. '
 'KhôngchọnDụng/vượngsuy/kếtquảtiềnbạc/nghề/sứckhỏe/tuổithọ;web/site/ZIPwebnguyênbyte,toànkhochưahoàntất.')
nexts=[
 'B02 chương39 壽元 mớiđọcmở232,tiếp233 đểkhép khoảngnguồn;giữlời bệnh/thọyểu lịch sử,khôngxâydựngbộđoántuổithọ. 36–38đãđọckhoảngnhưng20mệnhđềchưaphảitríchhếttừngcâu/vídụ/điềukiện.',
 'Chương37 cònđọcmụctiêuchữđầuquẻ226trông允/兌,chưađịnhđược thìkhôngtựchọnsốquẻ. Cácngưỡngvượngsuy/khôngphá/ứngkỳ,chữnguồnvàgiọngbìnhđầyđủchưaxong. Khônglặp8192contexts/2HHCnếu logicchưađổi.',
 'Cácnhánhkhác cònmở:B03phụ/MaiHoa/chữmở;Tửvi火鈴星/CanhNhâm/khởihạn/dịbản;Báttựcách/vượngsuy/dụngthần;NhàởPhiTinh/đoreal/TrạchKinhảnh. T02ĐạoTạng403vẫnleadriêng,khôngvượtchặn/khônggọilàđãtảisách.',
 'ỨngviênUIKiếnLộc chờbrowserQA/TXT/in/PDF ngoài site;khôngvượtsetting. Danhmục40/whole0,nguồn/corpus/lờicổ/suyluậnngoàisite;khôngxuấtbảnmạng.'
]
write(b/'WORK_STATE.json',{'date':'2026-10-27','status':'three-life-focus-spans-and-private-structural-contexts-verified-fullconditions-active','latestReport':'v53/'+report,
 'completedStep':step,'summary':qa['summary'],'sourceVerification':src,'currentTOC':'v53/research/liuyao-life-context/B02_CURRENT_UNITS.json','next':nexts,
 'consumerChanged':False,'wholeChaptersApplied':False,'sourceOutcomesValidated':False,'lifespanOrClinicalClassifier':False,'wholeCatalogueCompleted':False})
d=read(w/'EXHAUSTIVE_WORK_STATE.json');d['currentWork'].update(catalogueID='B02',relatedCatalogueIDs=['B02'],work='增刪卜易 — Thân mệnh, tài phúc và công danh theo câu hỏi',
 reason='Keep a specific question, source roles and derived element edges separate from unverified whole-life claims.',sourceDirectory='v53/research/liuyao-life-context',
 currentStep=step,latestResearchReport='v53/'+report,functionalBacklog='v53/research/liuyao-life-context/WORK_STATE.json',
 currentTOC='v53/research/liuyao-life-context/B02_CURRENT_UNITS.json',currentB02UnitMap='v53/research/liuyao-life-context/B02_CURRENT_UNITS.json',internalLifeContextReference='v53/research/liuyao-life-context/life-context-reference.mjs',
 sourceLimits='36–38firstspan/read only20boundedclauses;notallrules.39onlyopening232. No wealth/career/clinical/lifespan outcome.',
 nextSourceLead={'sourceID':'B02-ch039','status':'onlyopening232read-next233','file':'v53/research/liuyao-foundations/NLC416-12jh005345-45344.pdf','remaining':' '.join(nexts)})
d['inProgressScope']='v53/research/liuyao-life-context/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in[w/'EXHAUSTIVE_WORK_STATE.json',r/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=r/'research/full-study/WORK_STATE.json';d=read(p);d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts);item=next(x for x in d['items']if x['id']=='yi')
if step not in item['completed']:item['completed'].append(step)
if ' '.join(nexts)not in item['remaining']:item['remaining'].append(' '.join(nexts))
item['latestScope']='../liuyao-life-context/WORK_STATE.json';write(p,d)
p=r/'research/library-current/COVERAGE.json';d=read(p);entry=next(x for x in d['catalogue']if x['id']=='B02');entry['latestLifeContextScope']=step
for f in['v53/'+report]+['v53/research/liuyao-life-context/'+n for n in['WORK_STATE.json','SOURCE_MANIFEST.json','MANUAL_READINGS.json','SOURCE_CONTEXTS.json','B02_CURRENT_UNITS.json','BOUNDED_CLAUSES.json','PRINTED_FIXTURES.json','life-context-reference.mjs']]+['v53/qa/liuyao-life-context/RESULTS.json','v53/qa/liuyao-life-context/SOURCE_RESULTS.json']:
 if f not in entry['currentEvidence']:entry['currentEvidence'].append(f)
d['latestFollowup']=report+': '+step;d['latestAcquisitionCounts']={'scope':report,'newHTTPRequests':0,'newOriginalContainers':0,'firstReadPositionsNewToReleaseFromStaging':19,'alreadyIntegratedPositionExpanded':1,
 'inheritedNewRenderPositions':12,'inheritedRetainedRendersNowRead':7,'targetedExpandedReadPositions':4,'newHighResolutionQARenders':1,'pixelReproductionRenders':2,'boundedClauses':20,'completeFirstPassSpans':3,'wholeWorksApplied':0}
d['counts']['newDownloadsThisScope']=0;d['counts']['newDownloadsThisScopeBasis']='NoHTTP/PDForiginal;19firstpasspositions stagedbeforethisheartbeatpromoted,4targetedexpandedreadings,1new360dpiQA/2pixelreproductions. Not19newbooks/downloads.'
assert d['counts']['wholeWorkApplied']==0 and d['counts']['catalogueRecords']==40;write(p,d)
note='Mốc Dịch — Thân mệnh và câu hỏi cụ thể, 27/10/2026: `'+report+'`. '+step+'\n\n'
for p in[w/'PROJECT_RESEARCH_STATE.md',r/'NEXT_STEPS.md',r/'research/library-current/COVERAGE.md']:
 t=p.read_text(encoding='utf-8-sig')
 if t.startswith('Phần tiếp đang ngoài gói:'):t='Ghi chú staging trước mốc mới (đã tiếp nhận ở báo cáo trên): '+t
 if not t.startswith(note):p.write_text(note+t,encoding='utf-8')
write(w/'PENDING_RESEARCH_STATE.json',{'date':'2026-10-27','status':'Liuyao-life-context-current-scope-active','workDirectory':'v53/research/liuyao-life-context','currentWorkState':'v53/research/liuyao-life-context/WORK_STATE.json',
 'latestReport':'v53/'+report,'next':nexts,'separateBlockedSourceLead':'tmp/tuvi-daozang-staging/WORK_STATE.json','pendingConsumerCandidate':'v53/research/bazi-jianlu-context/CANDIDATE_STATUS.json',
 'consumerChanged':False,'wholeCatalogueCompleted':False})
(r/report).write_text('''# Lục hào: tách câu hỏi cụ thể và các vai trò trong ba chương Thân mệnh

Ngày 27/10/2026. Tiếp nhận lượt đọc đầu ba khoảng chương36 Thân mệnh/PDF213–214,37 Tài phúc/214–229,38 Công danh/229–232. Bộ tham chiếu riêng giữ các nhóm Thế–Tài–Tử tôn hoặc Thế–Quan–Phụ và quan hệ ngũ hành dẫn xuất. Không chọn Dụng, hiệu lực, sự kiện hoặc kết quả cả đời. **7 kiểm đạt; web nguyên byte.**

## Nguồn và độ phủ

Tái dùng PDF NLC416-12jh005345-45344,11089308byte/SHA256`caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa`. Không HTTP hoặc PDF gốc mới. Staging đã đọc20vị trí213–232 trước nhịp này:19vị trí đọc đầu mới vào gói,213đã giữ;12render221–232 đã chuẩn bị và7render214–220 trước chỉ định vị nay đã đọc. Nhịp này mở rộng mục tiêu213/214/215/229;không gọi19vị trí staging là19lượt tải hay19trang mới đọc trong chính heartbeat. 20SHA ảnh được kiểm.

Trang214 kết chương36 trước đầu37;229 kết37 trước đầu38;232 kết38 trước đầu39 壽元. Ranh có trang dùng chung, không cộng2+16+4 thành22trang độc nhất: tổng213–232 là20vị trí. Chương39 chỉ đoạn mở, không nhận đọc toàn chương. Map hiện136đơn vị/92chỉ đề mục/36khoảng đọc đầu/7nền một phần/1phần39/0áp hết. Bản đồ cũ và các cờ “214–220chưa đọc” được giữ như lịch sử, bản đồ mới tiếp nhận lượt đọc sau.

## Quy tắc và giới hạn

Chương36 phê cách dùng một quẻ để luận chung mọi mặt cuộc đời, nêu việc tách câu hỏi cha mẹ, anh em, tài phúc, công danh, vợ chồng, con cái và thọ nguyên. Bảy loại là dữ liệu phương pháp nguồn; không phải chỉ thị tự gieo quẻ thêm hoặc suy ý riêng tư từ lời người dùng. Các lời kể đoán sang tai họa hay công danh không được biến thành cơ chế tự đổi câu hỏi.

Chương37 nêu ba vai trò **Thế, Tài, Tử tôn**;Tử tôn được gọi nguồn của Tài. Giữ nhóm Tài và nhóm Phúc/Tử tôn riêng;không đồng nhất có hào với vượng/có khí/không mất hãm. Chương38 đặt **Quan và Phụ** thành hai nhóm công danh/văn tự. Đây là nhóm song song;không phát minh quy tắc “Phụ luôn sinh Quan”. Mọi mũi tên sinh/khắc trong bộ riêng được tính từ hành của các hào đã định danh, ghi rõ là dẫn xuất cấu trúc, không là lời trích hay ưu tiên nhân quả của sách.

`lifeSourceContext` yêu cầu tên hệ và chủ thể `self`;từ chối đối tượng khác hoặc ý hỏi tự do ngoài phạm vi. Kết quả giữ vị trí hào gốc, nhóm hào biến, chuyển hóa riêng từng hào và các cạnh sinh/khắc. Hào tĩnh có hoạt động chưa biết vì chưa nhận tiền đề ám động;không mặc định tĩnh là hoàn toàn vô lực. Các trường có khí, hiệu lực, ưu tiên, Dụng, ngày, kết quả tiền bạc/công việc/sức khỏe và tuổi thọ đều đểchưa xác định. Không ghép hào biến vào nhóm gốc để tự tạo chuỗi sinh cứu.

20mệnh đề giới hạn được gán giọng nguồn/xửtrí, gồm tách câu hỏi, ba vai trò, tài/phúc, động-không, nhập mộ, Lục hợp/Lục xung, bối cảnh Phụ trì Thế, tài không tự là vợ, Quan–Phụ, lời nhân sự/nghề/ngũ thần và các lời bình phản bác. Chưa liệt kê hết mệnh đề phụ, các ngưỡng vượng suy, chânkhông/ứngkỳ hoặc mọi ví dụ. Chữ đầu quẻ ở226 trông允/兌 còn mở;không tự chọn số quẻ. Lời bệnh, thọ yểu và khuôn mẫu xã hội được giữ lịch sử, không áp cho người dùng.

## Kiểm chứng thực thi

Quẻ in215 **復→頤**, trên cùng 酉金Tử tôn động sang寅. Sáu nhãn gốc từ dưới lên:Tài子、Quỷ寅、Huynh辰、Huynh丑、Tài亥、Tử酉. Hai lời gọi HHC.hexNumber thật cho24/27;nhãn sáu hào và hào6động/酉→寅 khớp. Bản6/7/8/9 là mã phần mềm được khai báo, không ngày sinh hay lịch hiện đại của người trong sách. Câu nguồn “福神破而化絕” được lưu;không tự kết luận破/絕 từ riêng sáu nhãn. QA360dpi trang215 đã được xem;hai táirender144/360dpi khớp từngpixel.

7kiểm đạt trên8192ngữ cảnh riêng (64quẻ×64mẫu động×2hệ). Trong đó có21312cạnh sinh/khắc và24576hào có biến,16384truy vấn nhóm;những số này là thành phần trong8192ngữ cảnh, không các ca hay lời gọi engine độc lập. Cả hai nhóm giữ vai trò gốc/biến riêng, không vòng tự nối, không chọn kết quả. Trường sai/thiếu, đối tượng ngoài phạm vi, dữ liệu biến dạng và bảo toàn đầu vào đều được kiểm. Không chạy/cộng lại20480ngữ cảnh Thiên thời hay các bộ64quẻ trước nếu chưa đổi logic.

## Bảo toàn và tiếp tục

Snapshottrước`archives/v53-before-liuyao-life-context/`giữ3346tệp/sourceZIP2062254777byte. HTMLroot/V53/site707411byte/SHA`549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`,ZIPweb344047bytegiữnguyên;sitechỉindex.html. Nguồn/QA/bộthamchiếu chỉ trong gói nghiên cứu;không tăng phiên bản hoặc xuất bản mạng. UIKiếnLộc vẫn chờ trìnhduyệtQA theo trạngthái riêng.

Tái kiểm:`node v53/scripts/test-liuyao-life-context.mjs`;`python v53/scripts/verify-liuyao-life-context-sources.py`;`python v53/scripts/verify-liuyao-life-context-release.py --no-write`. Toàn kho40hồ sơ/whole0 vẫn mở. Tiếp nội dung chưa đủ trong36–38, đoạn39từ233 và các nhánh độc lập;không gọi ba lượt đọc đầu là ba chương đã áp hết.
''',encoding='utf-8')
print('Three source spans and bounded multi-role contexts recorded; full source coverage and all four domains remain active.')
