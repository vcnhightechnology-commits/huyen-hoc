from pathlib import Path
import json

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/bazi-jianlu-context';q=r/'qa/bazi-jianlu-context'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
qa=read(q/'RESULTS.json');src=read(q/'SOURCE_RESULTS.json');decode=read(q/'VOLUME3_DECODE_RESULTS.json')
assert len(qa['checks'])==9 and all(x['ok']for x in qa['checks'])
assert src['newVolume3NativePositionsVerified']==26 and len(decode['records'])==2
report='BAZI_JIANLU_CONTEXT_REPORT.md'
step=('Bát tự: chia đủ1223chữ thân bản số Kiến Lộc thành44ngữ cảnh có xử trí riêng; không đồng nghĩa đối hết từng chữ ảnh hay áp hết điều kiện. '
 'Đã giữ nguyên byte quyển3 CADAL06066039 (10619960byte/230ảnh), khớp SHA1/size mô tả Commons,2body200/TLS; '
 'đọc26vịtrí mới (24nội dung Lộc–Dươngnhận/2ngoại văn-ranh), thêmảnh226 kếtquyển5 vàmởrộng10ảnh cũ. '
 'Đối mục tiêu8tọađộ được dẫn vàphânbiệt5dương/5âm ở118–119; bộriêng giữ13dòng/240ngữcảnh,16mẫu chi của vídụ甲 giữ tiềnđề兩傍 chưa xác lập. '
 'Một entity&KR0339; đọcảnh là嗤, không sửa byte bản số. 9kiểm đạt:14HHC BátTự/10lunar thật;120ngữcảnh tháng riêng, không cộng probe cũ. '
 'Ứng viên giao diện Kiến Lộc đã kiểm chức năng nhưng chưa QA trình duyệt/in; giữ riêng vì browser bị vô hiệu hóa, web đang dùng nguyên byte. '
 'Chưavượngsuy/dụngthần/hiệulực hay toàn kho.')
nexts=[
 'Tiếp50 dòng trụ Lộc ởquyển3 ảnh5–8: chép đủnhãn/điều kiện theoảnh, giữ異體 và giọng nguồn; không tự đổi甲土/丙水 sang ngũhành can thường hoặc gọi財 ấy làThậpthần hiện đại.',
 'KiếnLộc44ngữcảnh mới códisposition, chưafullconditionalcompiler:財官印食, quá nhiều sát, căn/mùa/vượngsuy và各傳 bản còn mở. Nghiêncứu quét230ảnh không có nghĩa đãđọc230; cùnghọWYG không thànhnhânchứngđộclập.',
 'Khi browser được phép dùng, kiểm ứngviên consumer-candidate (ảnh desktop/mobile, TXT/in/PDF/restore) rồi mới tíchhợp. Không vượt Work setting hoặc coi testchuỗiHTML làQAhiểnthị. Tronglúc đó tiếp nghiêncứuđộclập.',
 'Nhàở còn đo thực/Bắc/ba vòng, đồmộvận41/49, TrạchKinhảnh vàPhiTinhđầyđủ; B02 từ191/B03cácmệnhđềphụ/MaiHoa/chữmở; TửviCanh–Nhâm/khởihạn/dịbản. Danhmục40 vẫnwhole0; không công bốmạng.'
]
state={'date':'2026-10-27','status':'context-dispositions-and-native-crossreference-verified-fullconditions-active',
 'sourceID':'M01-WYG-003-005-lu-jianlu-blade','latestReport':'v53/'+report,'completedStep':step,
 'summary':qa['summary'],'sourceVerification':src,'candidateStatus':'v53/research/bazi-jianlu-context/CANDIDATE_STATUS.json',
 'sourceContextMap':'v53/research/bazi-jianlu-context/JIANLU_CONTEXTS.json','facsimileReadings':'v53/research/bazi-jianlu-context/FACSIMILE_CROSSREF_READINGS.json',
 'next':nexts,'consumerChanged':False,'fullPatternClassifier':False,'allSourceImageCharactersCollated':False,'wholeSectionApplied':False,'wholeCatalogueCompleted':False}
write(b/'WORK_STATE.json',state)
d=read(w/'EXHAUSTIVE_WORK_STATE.json')
d['currentWork'].update(catalogueID='M01',relatedCatalogueIDs=['M01'],work='三命通會卷三/五 — Lộc, Kiến Lộc và hai bảng Dương nhận',
 reason='Preserve the full context and named-source distinctions before compiling conditions or consumer interpretations.',
 sourceDirectory='v53/research/bazi-jianlu-context',currentStep=step,latestResearchReport='v53/'+report,
 functionalBacklog='v53/research/bazi-jianlu-context/WORK_STATE.json',
 internalBladeReference='v53/research/bazi-jianlu-context/blade-reference.mjs',internalLuIllustrationReference='v53/research/bazi-jianlu-context/lu-illustration-reference.mjs',
 sourceLimits='44 contiguous digital contexts/targeted native collation,26 first-read volume3 positions+ending226. Not all230 pages, complete strength/pattern rules or an independent edition. Candidate not deployed.',
 nextSourceLead={'sourceID':'M01-WYG003-Lu-fifty-labelled-entries','status':'native-pages-retained-first-read-transcription-open','file':'v53/research/bazi-jianlu-context/volume3/images/p005.png','remaining':' '.join(nexts)})
d['inProgressScope']='v53/research/bazi-jianlu-context/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in[w/'EXHAUSTIVE_WORK_STATE.json',r/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=r/'research/full-study/WORK_STATE.json';d=read(p);d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts)
item=next(x for x in d['items']if x['id']=='bazi')
if step not in item['completed']:item['completed'].append(step)
if ' '.join(nexts) not in item['remaining']:item['remaining'].append(' '.join(nexts))
item['latestScope']='../bazi-jianlu-context/WORK_STATE.json';write(p,d)
p=r/'research/library-current/COVERAGE.json';d=read(p);entry=next(x for x in d['catalogue']if x['id']=='M01');entry['latestJianluScope']=step
for f in['v53/'+report]+['v53/research/bazi-jianlu-context/'+n for n in['WORK_STATE.json','SOURCE_MANIFEST.json','JIANLU_CONTEXTS.json','BLADE_TABLES.json','FACSIMILE_CROSSREF_READINGS.json','blade-reference.mjs','lu-illustration-reference.mjs','CANDIDATE_STATUS.json']]+['v53/qa/bazi-jianlu-context/RESULTS.json','v53/qa/bazi-jianlu-context/SOURCE_RESULTS.json']:
 if f not in entry['currentEvidence']:entry['currentEvidence'].append(f)
d['latestFollowup']=report+': '+step
d['latestAcquisitionCounts']={'scope':report,'newHTTPRequests':2,'httpStatuses':[200,200],'newOriginalContainers':1,'newOriginalBytes':10619960,
 'newSourcePages':27,'newVolume3Positions':26,'newVolume3ContentPositions':24,'newVolume5EndTitlePositions':1,'expandedPreviouslyReadPages':10,
 'sourceContextUnits':44,'directBladeRows':13,'nativeEntityQACrops':1,'wholeWorksApplied':0}
d['counts']['newDownloadsThisScope']=1;d['counts']['newDownloadsThisScopeBasis']='One volume3 original DjVu;two200 bodies (description+original),TLS/SHA/size verified.27new nativepositions include26volume3+1volume5ending;not230readpages.'
assert d['counts']['catalogueRecords']==40 and d['counts']['wholeWorkApplied']==0;write(p,d)
note='Mốc Bát tự — Ngữ cảnh Kiến Lộc và đối ảnh Lộc–Dương nhận, 27/10/2026: `'+report+'`. '+step+'\n\n'
for p in[w/'PROJECT_RESEARCH_STATE.md',r/'NEXT_STEPS.md',r/'research/library-current/COVERAGE.md']:
 t=p.read_text(encoding='utf-8-sig')
 if t.startswith('Phần nối tiếp đã chuẩn bị ngoài gói:'):
  t='Ghi chú dở trước phạm vi mới (đã được tiếp nhận ở báo cáo trên): '+t
 if not t.startswith(note):p.write_text(note+t,encoding='utf-8')
write(w/'PENDING_RESEARCH_STATE.json',{'date':'2026-10-27','status':'Bazi-jianlu-context-current-scope-active','workDirectory':'v53/research/bazi-jianlu-context',
 'currentWorkState':'v53/research/bazi-jianlu-context/WORK_STATE.json','latestReport':'v53/'+report,'next':nexts,
 'consumerChanged':False,'wholeCatalogueCompleted':False,'pendingConsumerCandidate':'v53/research/bazi-jianlu-context/CANDIDATE_STATUS.json'})
(r/report).write_text('''# Bát tự: giữ toàn ngữ cảnh Kiến Lộc, đối ảnh Lộc–Dương nhận

Ngày27/10/2026. Chín kiểm chức năng đạt; đối byte/pixel nguồn đạt. Phạm vi này hoàn thiện hồ sơ44ngữ cảnh Kiến Lộc và đối mục tiêu hai đoạn trước vềLộc/Dươngnhận. **Không phải toàn bộ điều kiện cách cục đã được áp dụng.** Web đang dùng giữ nguyênbyte; ứngviên phần giải thích tháng sinh còn trong nghiêncứu chờQAhiểnthị.

## Vật mang và lượt đọc

Quyển5 tái dùng CADAL06066041.djvu/SHA256`013ce4861680a2bf08b811050c45a45bb2d3ce9d164f7e2341d7070bd5cb2c1a`. Támảnh218–225 được đọc mở rộng toàn khoảng KiếnLộc;198/202 mở rộng các câuDươngnhận. Ảnh226 mới giải mã và xem trực tiếp là trangkết **三命通會卷五**, không thêm điều kiện. Bộ giải mã nguyênbyte đã tái tạo đúngpixel226.

Mới giữ [bản quyển3 trên Commons](https://commons.wikimedia.org/wiki/File:CADAL06066039_%E4%B8%89%E5%91%BD%E9%80%9A%E6%9C%83%C2%B7%E5%8D%B7%E4%B8%89.djvu), qua liên kết tệp gốc của trang mô tả. Hai phản hồiHTTPS200/TLSauthorized ghi đủbyte/hash/header. Original10619960byte/SHA1`61fee880e39b5df646278c51d1b62532a47e4422` khớp mô tảrevision1207461000; SHA256`2334006e3a46b16bdbf0bf6a79512d8d0c4b87a2ce2e8e1ff503121d8f2cffdc`. Decoder xác nhận230ảnh. Commons quy nguồnCADAL/Zhejiang; chưa lấy hồ sơ cơ quan trực tiếp, chưa xác minh niênđại hoặc phả hệ độc lập.

Đã xem26vịtrí quyển3: ảnh2ngoại văn;3–18/trang1a–8b toàn khoảng論十干祿;19đầu luận金轝 làm ranh;112–119/trang55b–59a toàn khoảng論羊刃,119đồng thời có đầu論空亡. **24vịtrí nội dung/2ngoại văn-ranh**, không phảiđọc230ảnh. Tái giải mã113/119 bằngdecoder nguyênbyte chođúngpixel;26PNG/RGBA và1crop嗤 đốibyte/pixel. Log lúcrender giữ nguyên; hồsơđọc tay ghi riêng sauđó, không gán việc giải mã là đọc tựđộng.

Tổngphạm vi **2HTTPbody/1container mới/27vịtrí nguồn mới/10ảnh cũ mởrộng**. 27gồm26quyển3+1trangkếtquyển5;24trang nội dung mới. Bản số ghimcommit đãgiữ: quyển3SHA`267fda36d206bfd153d9377441adb5f99f96c39a594a5f7ebdf3e4dd226e9b87`,quyển5SHA`1ebdd92feaa57496b702f962ad6fafd4f19c17e98c38a94b40f626ef321dd997`. CùnghọWYG không tựthành hai nhânchứngđộclập. `CROSSREF_READINGS.json` giữ trạngthái lịch sử đọc số trướcđốiảnh; cậpnhật hiệnhành ở`FACSIMILE_CROSSREF_READINGS.json`.

## Tách ngữ cảnh và điều kiện

Thân bản số KiếnLộc1223chữ chuẩn hóa khoảngtrắng/dấu¶/mốcfolio,được chia44đơnvị liên tục vàgánxửtrí cho từngđơnvị. Cóđủ khoảngphủbảnsố không đồngnghĩa đãđối mỗi chữ ảnh hoặc biêndịch hết điều kiện. Giữphânbiệt giọngnguồn/câu dẫn/thơ/vídụ/quyướcphầnmềm vàchưa xácminh.

Ngoạilệ ởảnh221:戊日巳月 có nhiềuHỏa hoặcẤn dùkhôngTàiQuan vẫnđược nguồnnói吉. Vìvậy không dùng mộtquytắc “mọiKiếnLộc bắtbuộcTàiQuan”. Ảnh224nói **是見煞取貴然亦不可太多** nhưngchưađịnh số “quá nhiều”; thơ yêu cầu xem năm/giờ vàkhuyên không cốchấpđềmục. Không suyđếmđơnthuần thànhvượngsuy/chọndụngthần hoặc gánlời phúquý/tuổithọ chongườidùng.

Támtọađộ được dẫn ởquyển3/113:甲卯、乙辰、丙午、丁未、庚酉、辛戌、壬子、癸丑. **戊/己 không được liệt kê trực tiếp trongtámcâu**. Ảnh118–119chính nguồnphânbiệtTửBình:甲丙戊庚壬nămdươngcó刃;乙丁己辛癸nămâmkhông刃 vàdẫnđến陽刃格 ởsau. Quyển5/198/202cótọađộ nămcan甲卯、丙午、戊午、庚酉、壬子. Giữhaihệtênriêng,13dòngtrựctiếp,khônggộpthànhbảngmườicanhoặc lấpôthiếu. Phạmvi nhãn không xácđịnh cách/thânvượng/hiệulực/kếtquả.

Ảnh4nói **甲土尅丙水為財**. Giữliteral;không tựsửathành甲木/丙火 hoặcđồngnhất財 ấyvớiThậpthầncanngàyhiệnđại. Giảthuyết hệhànhchuyểnhóa mới làhướngnghiêncứu. Ảnh13–14minhhọa甲祿寅: có寅/亥 gọi明合;không寅có亥暗合;không寅có丑卯兩傍虛拱;có寅và丑卯兩傍實拱. Thamchiếuriêng chỉchiếu sựhiệndiệnchi trongvídụ甲;tiềnđề位置“兩傍” chưađược xáclập,khôngtrảthànhcách hoặc suyra cả10can. Thiếuđộđủbốicảnh trảnull,khôngcoithiếulàkhôngcó.

Entity`&KR0339;` trongbảnchữLuđượcảnh18/cropnative đọc **嗤**,câu虛名虛譽足堪嗤是嫌亡也. Bảnchữgốc giữnguyên;ghiđốichiếuriêng chođúngnhânchứng. Khônggọimộtchữđãđọc làhiệuđínhtrọnbộ. Cácđiềukiện/nhãncổ khác,50dòngtrụLộcảnh5–8 vàkhácbiệthệquychiếu cònmở.

## Kiểm chức năng và ứng viên giao diện

9kiểm đạt:14lầnHHC BátTự/10lầnlunar-typescript1.8.6thật;10fixture khớp4trụ vàtrạngtháitháng临官,quan hệcanlộnăm/giờđốiLunarUtil.SHI_SHEN. 120ngữcảnh tháng,240ngữcảnhDươngnhận,16mẫuchi Luđượckiểmriêng;đây làcácngữcảnhhữu hạn,khôngphải376lá số nguồnhoặc chứngcứứngnghiệm. Thiếugiờ/ranh mơhồ/khôngkhớp khôngđiền giả. Khôngsửadụngthần hoặcphéptínhđạivận.

Ví dụin丙戌 丁酉 辛酉 乙未cómộtngàyhiệnđạikhảthi từprobeđãgiữ (61lầnlunar dò/1HHC),táchkhỏisốtestlần này. Khônggánngàydươnghiệnđạichongườitrongsách,khôngxácminhtuổi48/壬寅運/壬申年/kếtcục.

Ứngviên trong`research/bazi-jianlu-context/consumer-candidate/` thêmđọcgọnKiếnLộc theothángsinh vàcanlộnăm/giờ,detailgậpmặcđịnh,dùngluồngTXT/in hiệncó. Đãkiểm chức năngvàchuỗiHTML; **chưa testtrìnhduyệt/ảnh/PDF**. Playwrightbị`spawn EPERM`;CƯA báoLocalbrowserusedisabledinWorksettings. Khôngvượt setting;đãkhôiphụctoànbộnguồnwebvềsnapshot. KhôngcoitrởngạiQA làlỗicủabảnđangdùnghoặcđãcóUIcậpnhật.

RootHTML/V53/site707411byte/SHA`549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`;ZIPweb344047bytegiữnguyên;sitechỉindex.html. Snapshot trướcgiữ3188tệp/sourceZIP2038218043byte ở`archives/v53-before-bazi-jianlu-context/`. Gói mới chỉthêmnghiêncứu/ứngviênriêng,khôngxuấtbảnmạng. Kếtquảmanifest/ZIPđốiđầysauđónggói ở`qa/bazi-jianlu-context/RELEASE_RESULTS.json`.

Tái kiểm: `node v53/scripts/test-bazi-jianlu-context.mjs`; `python v53/scripts/verify-bazi-jianlu-context-sources.py`; `node v53/scripts/redecode-bazi-volume3-crossref.mjs`; `python v53/scripts/verify-bazi-jianlu-context-release.py --no-write`. QAtrìnhduyệtcònchờđiềukiệnthựcthi. Kho40hồsơvàbốnlĩnhvực chưahoàntất.
''',encoding='utf-8')
print('Current source contexts, facsimile evidence and private candidate recorded; released product unchanged and exhaustive work active.')
