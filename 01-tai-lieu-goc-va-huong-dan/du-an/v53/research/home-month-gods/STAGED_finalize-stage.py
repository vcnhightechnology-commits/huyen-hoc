from pathlib import Path
import json,hashlib
b=Path('tmp/home-month-gods-staging');wr=lambda n,x:(b/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
raw=json.loads(Path('v53/research/home-yangzhai-final-spans/selection/RAW_IMAGES.json').read_text());imgs=[]
for x in raw['records']:
 if x['pdfPage']in[131,132,133,134,144,145,146,147]:imgs.append(dict(file='v53/research/home-yangzhai-final-spans/selection/'+x['file'],sourcePDFPage=x['pdfPage'],sha256=x['sha256'],bytes=x['bytes'],sourceImageID=x['sourceImageID'],expandedActuallyViewed=True,newReadPosition=False))
proof=[]
for f in ['v46/node_modules/lunar-typescript/package.json','v46/node_modules/lunar-typescript/dist/index.cjs','v46/node_modules/lunar-typescript/dist/lib/LunarUtil.mjs']:
 p=Path(f);proof.append(dict(file=f,bytes=p.stat().st_size,sha256=sha(p),actualCJSBatchEntry=f.endswith('index.cjs'),supplementalModuleNotExecutedByCJSBatch=f.endswith('LunarUtil.mjs')))
wr('SOURCE_DISPOSITIONS.json',dict(date='2026-10-28',sourcePDF=dict(file=raw['sourcePDF'],bytes=Path(raw['sourcePDF']).stat().st_size,sha256=raw['sourcePDFSHA256'],physicalPositions=195),sourceRawImages=imgs,sourceInstitutionalProvenance='Retained Tianyige institutional-sourcePDF; same existing witness, not a newly independent edition',selectedTablePage=146,sourceRows=7,printedCells=84,clearCells=82,unresolvedCells=2,sourceMonthCalendarBoundaryResolved=False,sourceRowDomainsNotCollapsed=True,fullDateSelectionMethodImplemented=False,newHTTPRequests=0,newContainers=0,newIndependentWitnesses=0,newReadSourcePositions=0,runtimeProof=proof,runtimeVersion='1.8.6',runtimeProofKind='Installed local package files hashed; not new publisher-signature or independently retrieved package proof',actualLunarStemPairLookups=20,diagnosticRuntimeProbe=dict(HE_GAN_5Reads=1,HE_ZHI_6Reads=1,POSITION_DESCReads=1,newChartCalls=0,probeUsedToInspectArrayShapeNotCountedAsSourceMatches=True),actualHHCCalendarCharts=0,actualIztroCharts=0,sourceEfficacyValidated=False,wholeSourceApplied=False))
summary='P08 nhà ở: đọc mở rộng8ảnh đãgiữ và13cropnative khớppixel,1cropnhầm cộttháng loại khỏi chứngbảngtrái. Chép7hàng月方吉神 tại146/84ô:82rõ,2ô月財tháng2/8giữnull(乙/丑chưachốt). APItra nguồn với thángkhai báo,phânbiệt phương/can/chi/quẻ;4ô天德坤乾艮巽khôngtựđổi申亥寅巳.20cặpcan(8天德合+12月德合)khớp bảngHE_GAN_5lunar-typescript1.8.6thật;4gốcquẻkhônggánphépthay.6kiểm đạt1lượt,336khungsaimonthbasis trảnull;0chartHHC/iztro/0HTTP/vịtrí/container mới. Chưa ranh tháng/nhuận/lịchchọnngày/hiệulực hợp/cáthung. Bảng720ô vàcáclớpnăm/thángkhácvẫnmở;webnguyênbyte,toànkhoactive.'
nexts=['P08:7hàng月方吉神 đượcchép84ô/82rõ2chưachốt;tiếp nhânchứng cho月財tháng2/8,không điền từ côngthức hoặc bảnghiệnđại. Giữ4gốcquẻ天德 riêng với can/chi của thiênđứchợp;chưa tựgán坤=申/乾=亥/艮=寅/巽=巳 cho phươngđo.', 'Phân định tháng nguồn theo lịch/tiếtkhí/nhuận,ngàycôngviệc/hoạtđộng,phương/gốc và ưu tiêncác lớp trước ứngdụng chọnngày. 20cặpcan chỉkhớp tọađộ hợp,khôngchứnghợphóa hoặc tácdụng. Bảng逐月吉凶日131–134vẫn720ôchưachép,12tháng60can chi cótênthầnghépnhiềuchữkhôngphảichỉ6nhãnđơn.', 'Tiếp完整交門/換象/初爻 vàgốcphòng/cửa,cáclớp年生命/太歲/月建,cáctrục南北vàtoàntuổithước;69ônhânchứng64đủ5hànhmờ. Bảnggiờ144ôđãđínhchínhkhớp,khôngđiềutradịbản司命do lỗi cột cũ.', 'Luânphiên Báttự48cha/mọitiềnđềphụ;Tửvi129ảnhitem上đãđọcđầu nhưngchưaápđủbody1–3hoặc4–6,CanhNhâm/童限/火鈴/khởihạn/nhuậncònmở;DịchB02/B03/MaiHoa. Nguồn/QA ngoài site,UIKiếnLộcchờbrowserQA,khôngxuấtbản/khôngtuyênbốtoànkhohoànthành.']
j=json.loads((b/'WORK_STATE.json').read_text());j.update(status='seven-month-god-tables-and20actual-stem-pairs-verified;calendar-and-two-glyphs-open',sourceDirectory='v53/research/home-month-gods',latestReport='v53/HOME_MONTH_GODS_REPORT.md',completedStep=summary,next=nexts,completeRuntimeChecks=6,actualLunarStemPartnerLookups=20,actualHHCCalendarCharts=0,actualIztroCharts=0,invalidFrameNullQueries=336,sourceOutcomesValidated=False,wholeCatalogueCompleted=False);wr('WORK_STATE.json',j)
report='''# Bảy bảng thần theo tháng trong phần nhà ở

Ngày28/10/2026. '''+summary+'''

## Nguồn và phép đọc

Dùng byte PDF Thiên Nhất Các đã giữ,195vị trí/SHA256b6394102a995bb66df173452b37614b29d58e34ff85e08c43077006572ac48a5,151275796byte. Không tải nguồn mới. Tám ảnh131–134/144–147 mở rộng bối cảnh,không cộng vào số trang mới. Ảnh146bêntrái có月方吉神:天道/天德/月德/天德合/月德合/月空/月財;12cộtthángđượcbiểudiễnthành12hàngtra.13cropnativeđãxem,khớppixel/khôngresample;cropmonth-labelsđầulấynhầmcộtcungởbảngphảivàđãloạikhỏichứngcứthángbảngtrái,trướcchép/kiểm.

MANUAL_MONTH_GOD_TABLES ghi84ô,82rõ và2ô月財tháng2/8chưachốt乙/丑. Không ép chữ theo bảng hiệnđại hoặc mẫu lặp. Bảng được băm trước gọi thư viện. ThiênĐạo dùng phương8hướng;ThiênĐức dùng8can+4quẻ坤乾艮巽;ThiênĐứchợp dùngcan/chi;nguyệtđức/hợp và月空dùngcan;月財dùngchi/2chữmở. Nhãnquẻkhôngtựthếchihoặcđộla bàn.

Câu以上宜百事大吉đặtbên月德合:giữtuyênbốlịchsử,khôngtựchọnphạmvihợpcáclớpAND/OR. 月空宜修造,月財宜修方造作làphạmvicôngviệcnguồn,khôngkhuyênngàylàmnhà hoặc dựbáotàilộc. Bốicảnh131cóđiềukiệntránh建破魁罡dùgặp吉星,khôngthểlấymộtnhãnthànhphánđoáncuối. Các câu dài trongCONTEXT_READINGSđọcchọn/tạm,chưalàhiệukhảotừngchữtoànchương.

## Chức năng và đối chiếu

sourceMonthGodbuộctênnguồn,tênhàng,tháng1–12hoặcnullvàmonthBasis. Chỉdeclared-source-ordinalđượctra;calendar-date/birth-year/door-direction/unknowntrảnull,khônggánsinhniên/hướngcửa thànhtháng. Giátrịvượtmiền bịtừchối. Kếtquảgiữloạiphương/can/chi/quẻ,chữmởtrảnull/candidatesvàkhôngđoánhiệulực. ChưachốtthángnguồnlàranhTết/tiết/nhuận hoặc đổiNgàyDương→thángnguồn.

Lunar-typescript1.8.6thậtcó20đọcbảngHE_GAN_5:8cặp天德cógốccan→天德合và12cặp月德→月德合khớp. Bốngốcquẻkhôngđượcápbảnghợpcan,nênkhôngbáođãso24cặp. Đây làquan hệcan,chưachứngminhhợphóahayphươngpháptuyểnngày. Cóprobeđọc3bảngđểbiếtdạngmảng;khôngđếmprobethànhcặpnguồnhoặcchart. Localpackage.json/index.cjsđượcbămSHA;LunarUtil.mjsgiữthêmdạngmodulethamkhảo,khôngphảientrybatchCJS. Khôngmô tảlàpackagepublisherđãđượctảimớixácminh.0HHCchart/0iztrochartvìkhôngsothuậtlịchsinhhoặcanTửvi.

Sáukiểmđạt1lượt:84ô/2null,8cặp+12cặpengine,336khungsaitrảnull,kiểuđầuvào/miềnkhônggộp vàbyteconsumer/crop. Phầnkiểmpixel/PDF/DCT/SHA đượcxácminhbổsungbằngscriptnguồn. Khôngchạylạibộgiờ144ôhoặcđồTửvi150đãđạt.

## Phần tiếp

'''+ '\n\n'.join(nexts)+'\n\nWeb/HTML707411byte/ZIPweb344047bytegiữnguyên. Nghiêncứu/QA ngoài site,khôngchuyểncáthunglịchsửthànhkếtquảđãchứngminh. Snapshot4984tệp/sourceZIP2755958650bytegiữtrướctiếpnhận.\n'
(b/'REPORT.md').write_text(report,encoding='utf-8');wr('PREPARATION_ATTEMPTS.json',dict(note='First metadata preparation stopped before writing output because nonexistent per-lib LunarUtil.cjs was requested. Actual CJS entry is bundled dist/index.cjs; corrected proof and supplemental .mjs explicitly separated. No runtime rerun or consumer impact.',actualRuntimeBatchInvocations=1));print('Prepared full evidence/report for seven source rows; no new runtime charts or downloads.')
