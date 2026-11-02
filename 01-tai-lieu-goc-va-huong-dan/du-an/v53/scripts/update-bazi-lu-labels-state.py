from pathlib import Path
import json

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/bazi-lu-labels';q=r/'qa/bazi-lu-labels'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
qa=read(q/'RESULTS.json');src=read(q/'SOURCE_RESULTS.json')
assert len(qa['checks'])==9 and all(x['ok']for x in qa['checks'])
assert src['nativeTableRows']==50 and src['digitalContextUnits']==28
report='BAZI_LU_LABELS_REPORT.md'
step=('Bát tự: chép đủ50cặp can–trụ được gán nhãn Lộc trên ảnh4–8 quyển3 và8mệnh đề chung có phạmvi biêntập tườngminh; '
 'thêm10tọađộ khoLộc từảnh13, khôngghép thuật mộhành thường. Chia2217Unicodecodepoint thân bản số thành28ngữcảnh có xửtrí; '
 'có2218UTF16unit vìchữ𤣥, offsetgiữ codepoint. 9kiểm đạt/600tracứunhãn+120tọađộkho riêng,60lượtgetJiaZiIndex lunar1.8.6 thật;0lá số sinh mới vì không đổi phép lịch. '
 '6ảnh cũ mởrộng,0HTTP/container/trangnguồn mới;giữriêng甲土/丙水 và丁木/辛水, nhãn截路空亡 khôngtựthành tính旬空. '
 'Khoảngnhãn bảng đãtrích không có nghĩa áp hếtLu/vượngsuy/dụngthần. Web/site/ZIPweb nguyênbyte;ứngviênUIKiếnLộc vẫnriêng chờbrowser. Toànkhochưa xong.')
nexts=[
 'Lộc:28ngữcảnh đã cóxửtrí/50nhãn/10kho, còn đầyđủtiềnđề cho眞祿/進退/貴神/祿堂/建向近合 vàvượngsuy. Cácvídụ明合/暗合/虛拱/實拱 chỉchiếu tậpchi甲;兩傍/thờivị cònmở. Khônglặp600tracứu/10tọađộthángđãđạt nếu khôngđổi logic.',
 'Giữ hai cáchDươngnhận đãđốiảnh riêng,tiếp điều kiện chương陽刃格 vàcácngoạilệ thayvìthêmcặpcan. KiếnLộc44ngữcảnh cònchưaFullcompiler. Cần nhânchứngđộclập/phảhệ/niênđại;khônggọicùngWYG hai bảnđộclập.',
 'ỨngviênUI ởresearch/bazi-jianlu-context/consumer-candidate chưaQAhiểnthị/TXT/in/PDF vìbrowserdisabled; khôngvượtsetting. Tiếp phầntàiliệuđộclập: TửviCanh/Nhâm/khởihạn,NhàởPhiTinh/đoreal/TrạchKinhảnh,B02từ191/B03cácmệnhđềphụ/MaiHoa/chữmở.',
 'Danhmục40/whole0 cònactive;nguồn/lờicổ/suyluận ngoài site,khôngxuấtbảnmạng. Ghi sai trướcrằng toàn50hàngởảnh5–8 được đínhchính: hàng甲bắtđầuảnh4,bađoạnvắttrang4→5/5→6/6→7.'
]
write(b/'WORK_STATE.json',{'date':'2026-10-27','status':'fifty-labels-ten-storage-and28-contexts-verified-full-conditions-active',
 'latestReport':'v53/'+report,'completedStep':step,'summary':qa['summary'],'sourceVerification':src,
 'sourceContextMap':'v53/research/bazi-lu-labels/LU_SECTION_CONTEXTS.json','sourceTable':'v53/research/bazi-lu-labels/SOURCE_ROWS.json',
 'internalReference':'v53/research/bazi-lu-labels/lu-label-reference.mjs','next':nexts,
 'consumerChanged':False,'modernTenGodEquivalenceEstablished':False,'wholeLuSectionApplied':False,'wholeCatalogueCompleted':False})
d=read(w/'EXHAUSTIVE_WORK_STATE.json')
d['currentWork'].update(catalogueID='M01',relatedCatalogueIDs=['M01'],work='三命通會卷三 — toàn bảng50nhãnLộc và khoLộc',
 reason='Extract bounded source labels while preserving semantic differences, unknown premises and complete section dispositions.',
 sourceDirectory='v53/research/bazi-lu-labels',currentStep=step,latestResearchReport='v53/'+report,
 functionalBacklog='v53/research/bazi-lu-labels/WORK_STATE.json',internalLuLabelReference='v53/research/bazi-lu-labels/lu-label-reference.mjs',
 sourceLimits='50namedpairs/8scopedclaims/10storagecoordinates/28digitalcontexts. Not full source mechanics,modernTenGod equivalence or source outcomes. Prior UIcandidate remains undeployed.',
 nextSourceLead={'sourceID':'named-conditional-rules-and-independent-witnesses','status':'open-select-nonduplicating-next-atomic-scope','file':'v53/research/bazi-lu-labels/WORK_STATE.json','remaining':' '.join(nexts)})
d['inProgressScope']='v53/research/bazi-lu-labels/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in[w/'EXHAUSTIVE_WORK_STATE.json',r/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=r/'research/full-study/WORK_STATE.json';d=read(p);d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts)
item=next(x for x in d['items']if x['id']=='bazi')
if step not in item['completed']:item['completed'].append(step)
if ' '.join(nexts)not in item['remaining']:item['remaining'].append(' '.join(nexts))
item['latestScope']='../bazi-lu-labels/WORK_STATE.json';write(p,d)
p=r/'research/library-current/COVERAGE.json';d=read(p);entry=next(x for x in d['catalogue']if x['id']=='M01');entry['latestLuScope']=step
for f in['v53/'+report]+['v53/research/bazi-lu-labels/'+n for n in['WORK_STATE.json','SOURCE_MANIFEST.json','SOURCE_ROWS.json','LU_SECTION_CONTEXTS.json','LU_STORAGE_TABLE.json','lu-label-reference.mjs']]+['v53/qa/bazi-lu-labels/RESULTS.json','v53/qa/bazi-lu-labels/SOURCE_RESULTS.json']:
 if f not in entry['currentEvidence']:entry['currentEvidence'].append(f)
d['latestFollowup']=report+': '+step
d['latestAcquisitionCounts']={'scope':report,'newHTTPRequests':0,'newOriginalContainers':0,'newSourcePages':0,'expandedPreviouslyReadPages':6,
 'sourceLabelRows':50,'sharedSourceClaims':8,'directLuStorageCoordinates':10,'digitalContextUnits':28,'wholeWorksApplied':0}
d['counts']['newDownloadsThisScope']=0;d['counts']['newDownloadsThisScopeBasis']='Six retainednativepages expanded;50source-labelledpairs,8scopedclaims,10storagecoordinates. No new HTTP/original/sourcepage.'
assert d['counts']['catalogueRecords']==40 and d['counts']['wholeWorkApplied']==0;write(p,d)
note='Mốc Bát tự — Bảng50nhãnLộc và28ngữcảnh, 27/10/2026: `'+report+'`. '+step+'\n\n'
for p in[w/'PROJECT_RESEARCH_STATE.md',r/'NEXT_STEPS.md',r/'research/library-current/COVERAGE.md']:
 t=p.read_text(encoding='utf-8-sig')
 if not t.startswith(note):p.write_text(note+t,encoding='utf-8')
write(w/'PENDING_RESEARCH_STATE.json',{'date':'2026-10-27','status':'Bazi-lu-labels-current-scope-active','workDirectory':'v53/research/bazi-lu-labels',
 'currentWorkState':'v53/research/bazi-lu-labels/WORK_STATE.json','latestReport':'v53/'+report,'next':nexts,'consumerChanged':False,'wholeCatalogueCompleted':False,
 'pendingConsumerCandidate':'v53/research/bazi-jianlu-context/CANDIDATE_STATUS.json'})
(r/report).write_text('''# Bát tự: đủ 50 cặp nhãn Lộc, bảng kho Lộc và bản đồ ngữ cảnh

Ngày 27/10/2026. Đã trích đủ 50 cặp can–trụ được gán nhãn trong đoạn Lộc của Tam Mệnh Thông Hội quyển ba, thêm 10 tọa độ kho Lộc. Chín kiểm đạt. Bộ tra riêng trả đúng nhãn nguồn và giữ các tiền đề chưa rõ; không sinh kết luận vận mệnh. Web hiện hành nguyên byte.

## Chứng cứ và phạm vi

Tái dùng CADAL06066039.djvu/10619960 byte/230 ảnh, SHA256`2334006e3a46b16bdbf0bf6a79512d8d0c4b87a2ce2e8e1ff503121d8f2cffdc`; lượt tải, mô tả và TLS ở `research/bazi-jianlu-context/volume3/`. Nguồn này đã được giữ và đọc trong phạm vi trước. **0HTTP,0container,0trang nguồn mới**; mở rộng sáu ảnh cũ 4–8 và13. Không sao chép lại ảnh/PDF, không gọi sáu lượt đọc mở rộng là sáu nguồn mới. Đã so sáu SHA PNG và pixel RGBA với log giải mã nguyên byte.

Bảng bắt đầu ở ảnh4, tờ1b; tiếp ảnh5–8 đến đầu tờ3b. Ghi chú trước rằng cả50hàng nằm ở5–8 được đính chính tại đây: hàng甲 bắt đầu4,甲寅 vắt4→5; câu đa凶 của丁戊午 vắt5→6;庚申長生祿大吉 vắt6→7;癸壬子 nằm8. Lưu folio/ảnh từng hàng. Nhận diện các hàng không dựa vào việc tất cả phải giống vòng quay của thư viện.

Bản số đã giữ tại commit ghim, SHA256`267fda36d206bfd153d9377441adb5f99f96c39a594a5f7ebdf3e4dd226e9b87`. Trích đoạn bảng giữ nguyên marker/literal. Nhãn có trường tìm kiếm chuẩn hóa凶/㓙/㐫、德/徳、值/値;己/巳 chỉ chuẩn theo vai trò can/chi, không thay toàn văn. Đây là đọc đối nhãn và câu mục tiêu, chưa phải bản chép ngoại giao mọi chữ ảnh. Cùng họWYG chưa thành nhân chứng độc lập.

## Những gì được áp dụng riêng

`SOURCE_ROWS.json` có10nhóm×5trụ, đủ50cặp và8câu chung. Nhãn và mệnh đề nguyên ý được giữ như lời nguồn, không là dự báo đã xác minh. Câu俱吉/俱凶 được gán nhóm biên tập tường minh; riêng câu cuối nhóm戊 có giới hạn phạm vi: ít nhất hai mục cuối乙巳/丁巳, chưa xác lập nó bao trùm mọi mục trước. Những mục không ghi mệnh đề riêng giữ chuỗi rỗng, không lấp kết luận từ hàng bên cạnh:丙辛巳、乙己卯、戊辛巳、己丙午.

Mỗi truy vấn buộc tên hệ, một can nguồn và trụ ứng viên hợp lệ; không nhận甲丑 hoặc thiếu trường. `null` là chưa biết; một trụ hợp lệ không có trong nhóm trảkhông-có-cặp-này-trong-bảng, không phải lời xấu. Can nguồn không tự gán năm/ngày sinh. Cùng癸巳 có hai tên/câu khác nhau ở丙 và戊; giữ cả hai theo can được người gọi khai báo.

Giữ nguyên khác biệt ngữ nghĩa: **甲土/丙水為財** ởảnh4 và**丁木/辛水** ởảnh7 chưa phải hệ hành can thông thường. Không sửa thành甲木/丙火/丁火/辛金 hoặc gọi財 ấy làThập thần hiện đại. `截路空亡` ởbảng chỉ là nhãn nguồn; không tự tính旬空 hiện đại để “sửa” nhãn. Lời chủ phú quý, nghèo, nghề, giới tính hoặc đời sống cá nhân giữ lịch sử, không chuyển thành kết quả người dùng.

Ảnh13/tờ6a nêu bốn nhóm khoLộc:甲乙→未、丙丁→戌、戊己壬癸→辰、庚辛→丑, đủ10tọa độ. `luStorage` yêu cầu tên hệ riêng; đây không tự thành mộ ngũ hành thường, tam hợp mộ hoặc phép chấm vận. Câu ví dụ甲乙亥多而得未 có chữ“nhiều” chưa định lượng; khớp nhánh kho chưa trảđã thỏa toàn câu hay tốt xấu.

Thân bản số luậnLộc có **2217Unicodecodepoint** sau bỏ khoảng trắng/¶/marker folio, được chia **28ngữ cảnh liên tục** và gán xửtrí toàn khoảng. Có2218UTF16unit vì𤣥 là mộtcodepoint/two code units; offset phải tính codepoint. Bộ kiểm ban đầu đã bắt chênh lệch này, được sửa trong kiểm hồ sơ, không đổi nguồn hay phần mềm người dùng. Entity`&KR0339;` vẫn nằm trong thân bản số; lượt đốiảnh trước đọc嗤 giữ riêng, không âm thầm sửa byte.

28ngữ cảnh gồm định nghĩa, bảng, các loại生成/名位/眞/進退/會合/食神/祿頭/旬中/天祿/干支合/互換/朝元/夾合/祿堂/建向近合, kho/hợp/củng, lời bàn ngựa và giới hạn. Có xửtrí hết một bản đồ văn bản không có nghĩa đã biên dịch đầy đủ điều kiện hoặc xác minh các sách được trích. Những tiền đề như兩傍, thai/thời vị, thần phụ, vượng suy, khí hóa và định nghĩa “nhiều” vẫn mở. Bảng50nhãn đã trích đủ không phải cả luậnLộc hoặc toàn tác phẩm đã áp hết.

## Kiểm chứng và bảo toàn

9kiểm đạt:600truy vấn riêng (10can×60trụ) có đúng50cặp trong bảng;120ngữ cảnh riêng khoLộc;null/sai trường/trụ bất khả thi/bảo toàn dữ liệu;8nhóm câu chung và28khoảng văn bản. Thực thi thật60lượt`LunarUtil.getJiaZiIndex` từlunar-typescript1.8.6 đã kiểm byte, xác nhận các ứng viên đều thuộc vòng60trụ. Không gọi tra chỉ số này là60lá số sinh, nguồn độc lập về ý nghĩaLộc hoặc chứng cứ ứng nghiệm. **0lời gọi lá số sinh mới** vì phạm vi tra nhãn không đổi ranh lịch/can ngày/phép vận;10tọa độtháng và14HHC/10lunar của phạm vi trước không chạy/cộng lại.

Snapshot trước giữ3262tệp/sourceZIP2055857311byte ở`archives/v53-before-bazi-lu-labels/`. RootHTML/V53/site707411byte giữ SHA`549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`;ZIPweb344047byte nguyên;site chỉindex.html. UIKiếnLộc trước vẫn ở thư mục ứng viên nghiên cứu, chưaQA trìnhduyệt/in vì browser bị tắt; không vượt setting và không coi UI đã phát hành. Nguồn/QA ngoài site, không đổi số phiên bản hoặc xuất bản mạng. Gói mới được đốimanifest/ZIP sau đóng gói.

Tái kiểm: `node v53/scripts/test-bazi-lu-labels.mjs`; `python v53/scripts/verify-bazi-lu-labels-sources.py`; `python v53/scripts/verify-bazi-lu-labels-release.py --no-write`. Cácđiều kiện Bát tự, Tửvi, Nhàở, Dịch và40hồ sơ vẫn active/whole0.
''',encoding='utf-8')
print('Fifty source labels/ten storage coordinates/28 context dispositions recorded; full methods and four-domain study remain active.')
