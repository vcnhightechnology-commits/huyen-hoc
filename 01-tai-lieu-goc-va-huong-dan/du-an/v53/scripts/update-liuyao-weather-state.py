from pathlib import Path
import json

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/liuyao-weather';q=r/'qa/liuyao-weather'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
qa=read(q/'RESULTS.json');src=read(q/'SOURCE_RESULTS.json');assert len(qa['checks'])==7 and all(x['ok']for x in qa['checks'])
report='LIUYAO_WEATHER_ROLES_REPORT.md'
step=('B02: khép lượt đọc đầu chương35 Thiên thời/PDF188–211, thêm21trang nội dung191–211 vàhai vịtrí212kếtquyển3/213mởquyển4-chương36. '
 'Đối mục tiêu16mệnhđề,giữ2giọngchọnvai trò/5câuhỏi;覺子191nắnglấyTửtônkhácđoạntóm201choTửtônhoặcTài. '
 '7kiểm đạt/2HHC thật cho恒→大過,mộtquẻin/sáunhãnchi-Lụcthân;20480ngữcảnhriêng,3072bốicảnhnắngkháccandidate. '
 '30vịtrírenders/23đãxem/7ảnh214–220chưaxem,1renderQA360và2táirenderkhớppixel;0HTTP/PDFgốcmới. '
 'Địnhvị213mởquyển4nhưnggiữmâu thuẫnmụclụcxếp35vào4;map136/95chỉđềmục/33đọckhoảng/7nềnmộtphần/1mộtphầnkhác/0áphết. '
 'Khôngdựbáokhítượng/tínhngàyhoặcđồngnhấtlờicổ. HTML/site/ZIPwebnguyênbyte;toànkhochưahoàntất.')
nexts=[
 'B02 chương36 身命 mớiđọctrang213;214–220đãrender ởresearch/liuyao-weather/images nhưngchưaxem. Tiếpđọctoànkhoảng,liệtkêđiềukiệnvàgiọngnguồn;khôngluậntrọnđờitừmộtquẻ hoặcđưa lời bệnh/thọyểu thànhkếtquảngườidùng.',
 'Chương35đãđọckhoảng188–211,có16mệnhđềgiớihạn/5selector;chưa mọicâu/phụchú/vượngsuy/ứngkỳ. Khônglặp20480contexts/2HHC nếu logicchưađổi;quẻin khác cầntríchđộc lập,khôngđiềnnét từengine. Mụclục35quyển4 khác thânquyển3,4mở213.',
 'B03cácmệnhđềphụ/MaiHoa/chữmở;Tửvi火鈴星/CanhNhâm/khởihạn/dịbản;Báttựđầycách/vượngsuy/dụngthần;NhàởPhiTinh/đoreal/TrạchKinhảnh đều cònmở. T02ĐạoTạngleadriêng ởtmp/tuvi-daozang-staging,403khônggọilàđãtảisách/khôngvượtchặn.',
 'ỨngviênUIKiếnLộc ởresearch/bazi-jianlu-context/consumer-candidate vẫnđợibrowserQA/TXT/in/PDF. Nguồn/corpus/suyluậnngoàisite;40hồsơwhole0;khôngxuấtbảnmạng.'
]
write(b/'WORK_STATE.json',{'date':'2026-10-27','status':'weatherchapter-first-span-and-named-role-candidates-verified-fullconditions-active',
 'latestReport':'v53/'+report,'completedStep':step,'summary':qa['summary'],'sourceVerification':src,'next':nexts,
 'currentTOC':'v53/research/liuyao-weather/B02_CURRENT_UNITS.json','consumerChanged':False,'meteorologicalModelValidated':False,'wholeChapterApplied':False,'wholeCatalogueCompleted':False})
d=read(w/'EXHAUSTIVE_WORK_STATE.json');d['currentWork'].update(catalogueID='B02',relatedCatalogueIDs=['B02'],work='增刪卜易 — Thiên thời và câu hỏi theo giọng nguồn',
 reason='Complete the chapter span and preserve conflicting role-selection premises before deriving anything from a cast.',sourceDirectory='v53/research/liuyao-weather',
 currentStep=step,latestResearchReport='v53/'+report,functionalBacklog='v53/research/liuyao-weather/WORK_STATE.json',
 currentTOC='v53/research/liuyao-weather/B02_CURRENT_UNITS.json',currentB02UnitMap='v53/research/liuyao-weather/B02_CURRENT_UNITS.json',internalWeatherReference='v53/research/liuyao-weather/weather-reference.mjs',
 sourceLimits='Firstspan188–211,16boundedclauses/5selectors/notallclauses.213onlychapter36opening;214–220renderedunread. No realweather/dateprediction.',
 nextSourceLead={'sourceID':'B02-ch036','status':'opening213read-next214alreadyrendered','file':'v53/research/liuyao-weather/images/zengshan-214.png','remaining':' '.join(nexts)})
d['inProgressScope']='v53/research/liuyao-weather/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in[w/'EXHAUSTIVE_WORK_STATE.json',r/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=r/'research/full-study/WORK_STATE.json';d=read(p);d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts)
item=next(x for x in d['items']if x['id']=='yi')
if step not in item['completed']:item['completed'].append(step)
if ' '.join(nexts)not in item['remaining']:item['remaining'].append(' '.join(nexts))
item['latestScope']='../liuyao-weather/WORK_STATE.json';write(p,d)
p=r/'research/library-current/COVERAGE.json';d=read(p);entry=next(x for x in d['catalogue']if x['id']=='B02');entry['latestWeatherScope']=step
for f in['v53/'+report]+['v53/research/liuyao-weather/'+n for n in['WORK_STATE.json','SOURCE_MANIFEST.json','MANUAL_READINGS.json','SOURCE_BOUNDARIES.json','B02_CURRENT_UNITS.json','BOUNDED_CLAUSES.json','QUESTION_ROLES.json','PRINTED_FIXTURES.json','weather-reference.mjs']]+['v53/qa/liuyao-weather/RESULTS.json','v53/qa/liuyao-weather/SOURCE_RESULTS.json']:
 if f not in entry['currentEvidence']:entry['currentEvidence'].append(f)
d['latestFollowup']=report+': '+step
d['latestAcquisitionCounts']={'scope':report,'newHTTPRequests':0,'newOriginalContainers':0,'newSourceReadPositions':23,'newWeatherBodyPositionsRead':21,'newParatextPositionsRead':1,'newNextChapterOpeningPositionsRead':1,
 'expandedPriorBodyPositions':3,'renderedPositions':30,'renderedNotReadPositions':7,'highResolutionQARenders':1,'pixelReproductionRenders':2,'boundedClauses':16,'wholeWorksApplied':0}
d['counts']['newDownloadsThisScope']=0;d['counts']['newDownloadsThisScopeBasis']='RetainedPDF;21newbodyreadpositions+endleaf212+opening213;30rendered/7unread. NoHTTP/neworiginal. Renderpositionsnotnewbooks.'
assert d['counts']['wholeWorkApplied']==0 and d['counts']['catalogueRecords']==40;write(p,d)
note='Mốc Dịch — Thiên thời và vai trò theo câu hỏi, 27/10/2026: `'+report+'`. '+step+'\n\n'
for p in[w/'PROJECT_RESEARCH_STATE.md',r/'NEXT_STEPS.md',r/'research/library-current/COVERAGE.md']:
 t=p.read_text(encoding='utf-8-sig')
 if t.startswith('Phần đang tiếp ngoài gói:'):t='Ghi chú dở trước mốc mới (đã tiếp nhận vào báo cáo trên): '+t
 if not t.startswith(note):p.write_text(note+t,encoding='utf-8')
write(w/'PENDING_RESEARCH_STATE.json',{'date':'2026-10-27','status':'Liuyao-weather-current-scope-active','workDirectory':'v53/research/liuyao-weather','currentWorkState':'v53/research/liuyao-weather/WORK_STATE.json',
 'latestReport':'v53/'+report,'next':nexts,'nextRetainedUnreadImages':'v53/research/liuyao-weather/images/zengshan-214.png through220',
 'separateBlockedSourceLead':'tmp/tuvi-daozang-staging/WORK_STATE.json','pendingConsumerCandidate':'v53/research/bazi-jianlu-context/CANDIDATE_STATUS.json',
 'consumerChanged':False,'wholeCatalogueCompleted':False})
(r/report).write_text('''# Lục hào: khép lượt đọc Thiên thời, giữ các giọng chọn vai trò riêng

Ngày27/10/2026. Khép lượt đọc đầu khoảng chương35 Thiên thời ởPDF188–211;đọc thêm21trang nội dung191–211,trangkếtquyển212 vàđầuquyển4/chương36 tại213. Bộthamchiếu riêng nhận tên phương pháp/câu hỏi rõ đểtrảcác hào ứng viên,khôngtrảdựbáokhítượng. 7kiểm đạt,webnguyênbyte.

## Chứng cứ và ranh nguồn

Tái dùngPDF`research/liuyao-foundations/NLC416-12jh005345-45344.pdf`,11089308byte/SHA256`caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa`. **0HTTP/0PDFgốc mới.** 188–190 đã đọc trongphạmvi trước,nhịp này mởrộng3trang đó vàđọc21trangtiếp. 30vịtrí191–220 đãrender144dpi;23vịtrí191–213 đãxem,7vịtrí214–220 **chưaxem**. Chuyểncả7render vào hồsơđểđọc tiếp,khôngtínhlàkiếnthứcđãđọc. 191cóthêmrenderQA360dpiđãxem;hai lượt táirender191ở144/360dpikhớptừngpixel,nênkhôngphảihai trangnguồn mới. 34hashảnh gồm30render+3ảnhcũ+1QA,khôngphải34trangnội dungmớiđọc.

Thiênthời kếtthúc211,trang212ghi卷三終;trang213mở增刪卜易卷四 và身命章第三十六. Mụclục xếp35sauđầuquyển4,nhưng thân188–211vẫnquyển3. Đãđịnhvịranhquyển4thựctại213;khôngsửamụclục haylấp mâu thuẫn. BảnđồB02hiện136đơnvị:95chỉđềmục,33khoảngđọclầnđầu,7nềnmộtphần,1mộtphầnkhác,0ápdụnghết. Chương36mới213;khônggọilàđãđọctoànquyển4.

## Quy tắc được giữ theo giọng nguồn

16mệnhđềgiớihạngồm phạmvicâuhỏi/địaphương,cha–con/Tài,khôngđộng,vượngsuy,theomùa,sươngtuyết,QuanQuỷ,tamhợp,trướcsauđộng,tháng,tiếnthoái,khôngphá,lặpbói,vàlờibàncuối. Đây khôngphảiliệtkêhếttừngcâu/bìnhchú/vídụ hoặcxácminhkếtcụcthờitiết.

**覺子ở191:** mưalấyPhụmẫu,nắnglấyTửtôn;lờiliềnkềphêviệcdùngTài/ThếỨngnhưtiềnđềchung. **Đoạntómở201:** Phụmẫumưa,QuanQuỷmâyđậm/sấmchớp,TửtônhoặcTàinắng. Bộtracóhai tênhệriêng/nămselector,khônghợpnhấtlờitrướcvàlờisau. Trong4096bốicảnhquẻ–mẫuđộng,có3072bốicảnhnắng chênhứngviênTài;đólàkhácphạmvingữcảnh,khôngphải3072lỗienginehaynghiệmthờitiết.

Lờicổ/bìnhcũ/野鶴/覺子 cóbấtđồngvềvượngsuytheomùa,Phụmẫuđươngtháng,mây–mưa/sương–tuyết,Quỷđộngcóphảisấmhaykhông vàđộngtrướcsau. Cácđiềukiệnkhông/phá/hợp/xung/ngày/giờ/chânkhông/cókhí chưađủđểtựchọnứngkỳ. Câukhuyên bóilạichỉghi nhưlờinguồn;khôngphảichỉthị tựbóithêmhoặcthaycâuhỏingườidùng. Lờidùngthờitiếtlàmtươngtựchonhânsựchưathànhtươngđồngđãchứngminh.

`weatherRoleCandidates` buộctênhệvàcâuhỏithuộcdanhmục;nullgiữchưabiết. Nếuhệ覺子khôngnêuvaitròmây/sấm,khôngmượnhệ201đểđiền. Trảứngviênhàogốc,hàođộnggốcvàhàobiếnriêng;khôngtựtìmlờihàophục/đặthiệulực/chọnDụng/địnhngày. KhôngchọnmộthàogốcchỉvìlàThế/Ứng,khônglấysựcómặtTàihayQuanQuỷlàmnhãnhiệntượngthực. `predictedWeather/useLineSelected/availabilityEstablished`đềunull. Chưacóđốidữliệukhítượngquansát;nguồnchỉlàcácquytắclịchsử.

## Đối thực thi và bảo toàn

Mộtquẻin191 **恒→大過**: sáuchigốctừdướilên丑亥酉午申戌/LụcthânTài–Phụ–Quỷ–Tử–Quỷ–Tàiđượcđọcriêng từbảng;vănnguồnnêu申鬼明動化進神 và世酉鬼. Vịtrí5động đượcsuyratườngminhtừhào申duynhất+vănđộng+haidanhquẻ;khôngnhậnđãđốihếtdấunétbảng. Bộ6/7/8/9làchuẩnhóaphầnmềmriêng. Hai lầnHHC.hexNumberthậtcho32/28,sáunhãnchi–Lụcthânvà申→酉khớp. Khônggắnngàydươnghiệnđạihoặcgọicáclờimưanắnglàkếtquảđãxácminh.

7kiểmđạt:nguồn/ranh/haigiọng/thiếu-saidữliệu/bảotoànvà20480ngữcảnhriêng (64quẻ×64mẫuđộng×5selector). Chỉ2lờigọiHHCmớiđểđốiquẻin;khôngchạy/cộnglạibảng64quẻhay120láBáttựđãkiểm. Tấtcảcácngữcảnhriêngkhôngđượctínhlà20480quẻnguồnhoặclờigọiengineđộc lập.

Snapshottrước`archives/v53-before-liuyao-weather/`giữ3295tệp/ZIPnguồn2058366890byte. HTMLroot/V53/site707411byte/SHA`549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`,ZIPweb344047bytegiữnguyên;sitechỉindex.html. Gói chỉthêmnghiêncứu/QA,khôngxuấtbảnmạnghoặctăngphiênbản. ỨngviênKiếnLộccònchờbrowserQA;khôngvượtsetting. Chỉcậpnhậtgói nguồn sauđốimanifest/ZIP.

Tái kiểm:`node v53/scripts/test-liuyao-weather.mjs`;`python v53/scripts/verify-liuyao-weather-sources.py`;`python v53/scripts/verify-liuyao-weather-release.py --no-write`. Kho40hồsơ/whole0vẫncònmở;tiếpchương36vàcácđiềukiệnchưađủ.
''',encoding='utf-8')
print('Weather source span, named selectors and chapter36 continuation recorded; four-domain study remains active.')
