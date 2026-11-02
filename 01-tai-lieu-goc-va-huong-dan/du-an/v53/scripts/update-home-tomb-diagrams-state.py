from pathlib import Path
import json

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/home-tomb-diagrams';q=r/'qa/home-tomb-diagrams'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
qa=read(q/'RESULTS.json');src=read(q/'SOURCE_RESULTS.json');assert len(qa['checks'])==8 and all(x['ok']for x in qa['checks'])
report='HOME_TOMB_DIAGRAMS_REPORT.md'
step=('Nhà ở: đối đồ41/49 Hiệp Kỷ quyển2, trích20ô mộvận/24nhãnsơn và50trụ năm,19bộthángđọcrõ/1bộThủyThổ–BínhTân giữhaikhảnăng12hoặc11–12. '
 '8kiểmđạt:60lá số năm+60lá số tháng lunar1.8.6thật,1440tracứunăm/2880tháng riêng;20ô vận/50trụnăm/19bộthángkhớpthamchiếuvăntrước. '
 '4lượtchépnháp tháng sai đượcđốiảnhcropvàsửatrongnghiêncứu,khôngsửasách/web. 5ảnhcũmởrộng,22QAderived(2cropgốc/6xoay/8sector/6detail)khớppixel,0HTTP/container/trangnguồnmới. '
 'ĐồthườngkhôngghèquyướcKimsaĐôngchí;ranhlịch/đoreal/hiệulựcthựctếcònmở. HTML/site/ZIPwebnguyênbyte;toànkhochưahoàntất.')
nexts=[
 'Đồ49cònThủyThổ–丙辛sốthángmờ:12hay11–12;giữnullchotháng11/cảhaiđồngý12đượctra,côngthứctừruntimekhôngdùngkhôiphụcnét. Cầnnhânchứngđộclậphoặcảnhnguyênkhác,khôngphóngđạinộisuyđểtạo nét.',
 'XJ2-06/07đãtríchđồ41/49trongphạmvi20vận/50trụ/19+1bộtháng;chưatoànchữ/lờidẫn/điềukiện. Phépnối ngày→nămnguồn/thángnguồn/Đôngchí-vàKimcầnđịnhnghĩađầyđủ,khôngtrộnlịchâm/Tết/LậpXuân.',
 'B0239chỉđọcmở232,tiếp233nếuđọcnguồn,khôngbộđoántuổithọ;36–38cònmệnhđềphụ/B03/MaiHoa/chữmở. Tửvi火鈴星/CanhNhâm/khởihạn;Báttựcách-vượngsuy-dụngthần;NhàởTrạchKinhảnh/PhiTinh/đoBắcthực cònmở.',
 'ỨngviênUIKiếnLộcchờbrowserQA/TXT/in/PDFngoàisite;khôngvượtsetting. Giữ403T02leadriêng,khôngđềnghịnguồncùngtênlàcùnghệ. Danhmục40/whole0;khôngxuấtbảnmạng.'
]
units=read(r/'research/home-direction-tables/CURRENT_VOLUME_UNITS.json');units['previousMap']='v53/research/home-direction-tables/CURRENT_VOLUME_UNITS.json';units['latestScope']='v53/research/home-tomb-diagrams/WORK_STATE.json'
for x in units['units']:
 if x['id']=='XJ2-06':x['disposition']='Prior20base+5solsticeproserowsplusdiagram41all20ordinarymovementcells/24mountainlabels. Fullcalendar/quotedvoices/completeconditionalmethodopen.';x['extractionStatus']='diagram41-ordinary-coordinates-targeted-collated'
 if x['id']=='XJ2-07':x['disposition']='Priorconstructioncontextsand13examplesplusdiagram49all50listedyearpillars/19resolvedmonthsets/oneambiguous12vs11-12reading. No calendar/physicaladapter or practicaloutcome.';x['extractionStatus']='diagram49-year-list-complete-month19resolved-one-open'
units['nextAtomicWork']=nexts;write(b/'CURRENT_VOLUME_UNITS.json',units)
write(b/'WORK_STATE.json',{'date':'2026-10-28','status':'two-diagrams-targeted-coordinate-extraction-verified-one-month-reading-and-methods-active',
 'latestReport':'v53/'+report,'completedStep':step,'summary':qa['summary'],'sourceVerification':src,'sourceUnitMap':'v53/research/home-tomb-diagrams/CURRENT_VOLUME_UNITS.json',
 'next':nexts,'consumerChanged':False,'calendarAdapterEstablished':False,'sourceAmbiguityRestored':False,'wholeUnitsApplied':False,'wholeCatalogueCompleted':False})
d=read(w/'EXHAUSTIVE_WORK_STATE.json');d['date']='2026-10-28';d['currentWork'].update(catalogueID='P03',relatedCatalogueIDs=['P03'],work='欽定協紀辨方書卷二 — đồ Mộ long biến vận và năm/tháng khắc sơn',
 reason='Complete direct diagram cells and retain unresolved small numerals before a modern-calendar or dwelling adapter.',sourceDirectory='v53/research/home-tomb-diagrams',
 currentStep=step,latestResearchReport='v53/'+report,functionalBacklog='v53/research/home-tomb-diagrams/WORK_STATE.json',internalHomeDiagramReference='v53/research/home-tomb-diagrams/diagram-reference.mjs',
 sourceLimits='20movementcells/50listedyearpillars/19resolvedmonthsets+oneambiguous. Not sourcecalendarinstants,solsticeadapter,physicalcompass or validatedconstructionoutcome.',
 nextSourceLead={'sourceID':'XJ2-diagram49-one-month-range','status':'open-native-numeralambiguity-not-restoredfromruntime','file':'v53/research/home-tomb-diagrams/p049-water-month-detail.png','remaining':' '.join(nexts)})
d['inProgressScope']='v53/research/home-tomb-diagrams/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in[w/'EXHAUSTIVE_WORK_STATE.json',r/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=r/'research/full-study/WORK_STATE.json';d=read(p);d['date']='2026-10-28';d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts);item=next(x for x in d['items']if x['id']=='home')
if step not in item['completed']:item['completed'].append(step)
if ' '.join(nexts)not in item['remaining']:item['remaining'].append(' '.join(nexts))
item['latestScope']='../home-tomb-diagrams/WORK_STATE.json';write(p,d)
p=r/'research/library-current/COVERAGE.json';d=read(p);d['date']='2026-10-28';entry=next(x for x in d['catalogue']if x['id']=='P03');entry['latestRelatedIndependentSourceDiagrams']=step
for f in['v53/'+report]+['v53/research/home-tomb-diagrams/'+n for n in['WORK_STATE.json','SOURCE_MANIFEST.json','MANUAL_READINGS.json','DIAGRAM_TABLES.json','CURRENT_VOLUME_UNITS.json','diagram-reference.mjs']]+['v53/qa/home-tomb-diagrams/RESULTS.json','v53/qa/home-tomb-diagrams/SOURCE_RESULTS.json']:
 if f not in entry['currentEvidence']:entry['currentEvidence'].append(f)
d['latestFollowup']=report+': '+step;d['latestAcquisitionCounts']={'scope':report,'newHTTPRequests':0,'newOriginalContainers':0,'newSourcePages':0,'expandedPreviouslyReadPages':5,
 'nativeDiagramCrops':2,'losslessRotations':6,'nativeSectorCrops':8,'nativeDetailCrops':6,'sourceMovementCells':20,'sourceYearEntries':50,'resolvedMonthSets':19,'unresolvedMonthSets':1,'wholeWorksApplied':0}
d['counts']['newDownloadsThisScope']=0;d['counts']['newDownloadsThisScopeBasis']='Five retainedsourcepages expanded;22native/losslessQAderivatives.20movementcells/50yearentries/19+1monthsets;noHTTPornewcontainer/page.'
assert d['counts']['wholeWorkApplied']==0 and d['counts']['catalogueRecords']==40;write(p,d)
note='Mốc Nhà ở — Đồ mộ vận và năm/tháng khắc sơn, 28/10/2026: `'+report+'`. '+step+'\n\n'
for p in[w/'PROJECT_RESEARCH_STATE.md',r/'NEXT_STEPS.md',r/'research/library-current/COVERAGE.md']:
 t=p.read_text(encoding='utf-8-sig')
 if not t.startswith(note):p.write_text(note+t,encoding='utf-8')
write(w/'PENDING_RESEARCH_STATE.json',{'date':'2026-10-28','status':'Home-tomb-diagrams-current-scope-active','workDirectory':'v53/research/home-tomb-diagrams','currentWorkState':'v53/research/home-tomb-diagrams/WORK_STATE.json',
 'latestReport':'v53/'+report,'next':nexts,'separateBlockedSourceLead':'tmp/tuvi-daozang-staging/WORK_STATE.json','pendingConsumerCandidate':'v53/research/bazi-jianlu-context/CANDIDATE_STATUS.json',
 'consumerChanged':False,'wholeCatalogueCompleted':False})
(r/report).write_text('''# Nhà ở: đối đồ mộ vận và các tọa độ năm/tháng khắc sơn

Ngày28/10/2026. Hai đồ41/49 của Hiệp Kỷ quyển2 đã được đối mục tiêu:20ôvận,24nhãnsơn,50trụnăm và19bộtháng rõ;**một bộ số tháng còn mở**. 8kiểm đạt,thêm bộ tra riêng không nối ngày hoặc kết quả thực tế. Web nguyên byte.

## Byte và ảnh

Tái dùng CADAL06056503.djvu/SHA256`bfd3b76c55d62324919ab161c8c2ba2ecb129b3b2c59a3ab0428807e8f8278db`. Hai ảnh41/49 đã được giữ và đọc trong phạm vi nhà ở trước;nhịp này mở rộng hai đồ cùng văn50–52,tổng5ảnh cũ. **0HTTP/container/trang nguồn mới.** Hai cropnative,6xoay90/180/270độ không nội suy,8cropsector và6cropdetail,tổng22derivativeQA đượcxem vàso đúngpixel. KhôngOCR,khôngphụcchế nét hoặc gọi22ảnhQA là22trangnguồn.

Đồ41 có bốn nhóm sơn13ThủyThổ/4Hỏa/3Mộc/4Kim,total24nhãn và5nhóm can năm cho từngnhóm,tổng20ôhànhvận. Nhãncan-năm vànhãnvận trongcung đồ nằm xen nhau,cần đọc theo cột đôi,khôngcoichữ壬nhỏnhư土đểtựtạomâu thuẫn. 20tọađộ thường khớp bộvăn20cơsở trước;5ngoạilệKimsaĐôngchíkhôngđượcđồthườngthaythế.

Đồ49 có20cột nhóm sơn×can-năm,50trụnăm liệtkê. Việc không thấy một năm trongđồchỉlàkhôngliệtkê,tránhbiếnthànhbảođảmantoànxâydựng. Các bộtháng1–2/3–4/5–6/7–8/9–10 và11–12đượcchuẩntheonhãnnguồn;khôngtựcoilàthángdương/âm/Jiehaythờiđiểmthiênvăn. Trong19bộtháng rõ,có ba bộ gồm bốn tháng(1,2,9,10):Mộc–戊癸,Kim–甲己 vàKim–乙庚;khôngépmọihàngchỉhaitháng.

ÔThủyThổ–丙辛 cósốnhỏđọcnhư十二月尅 hoặc十一二月尅 khi đọc cột xen. Giữ hai khả năng `[12]` và `[11,12]`,khôngdùngcôngthứctừruntimeđiềnnét. Tratháng11trảchưabiết;tháng12được cảhaikhảnăng đồngý,nhưngcờđãđọcrõcảbộvẫnfalse. Cầnnhânchứngkhác hoặcảnhkhácđúngvậtmang;nộisuyphóngđạikhôngtạochứngcứmới.

## So engine và sửa lượt chép làm việc

60lá số năm và60lá số tháng **lunar-typescript1.8.6thật** cung cấptrụ/nạpâm ởtọađộhiệnđạiđãnêurõ. 60năm1984–2043/tọađộ15/6;60tháng5năm-nhóm×12thángdùngngày20đểlấytrụthángtrongđoạnJie. Chúng chỉđốitọađộcan/chi/nạpâm;khôngxácnhậnranhlịchcủacổbảnhoặcchophépcoingàyfixturelàngàyxâynhà. ĐặcbiệtthángChạpfixturehiệnđạiởsaĐôngchí,nhưngphépsobảngthườngkhôngápquyướcphaseđịa lýtừchínhngàyđó;đâylàđốitọađộ,khôngadapterngàyhoànchỉnh.

50trụnămtrongđồkhớpquanhệnạpâmkhắcvậnthường của bộvăn trước;19bộthángrõkhớp. CôngthứcsuyôThủyThổ–丙辛 là11–12,đượcghiởtrườngđốichiếuriêngvàkhôngphụcnguyênôảnh. Phépsotrongcùngtácphẩmvàthưviệnhiệnđạikhôngphảinhânchứngđộclập vềhiệuquảthựctế.

Bakiểmchạyđầuđãbắt lệchnhãn ởcáclượtchéplàmviệc. Cropnativebổsung xácnhậnbốnsửa: Hỏa–丁壬 thành3–4;Mộc–丁壬 thành7–8;Mộc–戊癸đủ1,2,9,10;Kim–戊癸 thành11–12. Lưuđọccũ/đọcmới/cropchứngcứtrong`transcriptionCorrections`;chỉsửanghiêncứu,khôngsửasách/web. Runtimechỉgiúppháthiệnchỗcầnđốilại,khônglàquyềnchépđápánlênảnh. Lầntestcuốicó120lá sốthật,kếtquảchínhthứckhôngcộnggộpcáclầnsailặpđểtăngca.

Bộ`diagramYear/diagramMonth` yêu cầu tênhệ,nhãnsơnnguồn,cannăm/trụnăm,thángnguồnhoặcnull vàphasesa/trướcĐôngchíđượckhaibáo. 1440truyvấnnăm và2880tracứuthángriêngkiểmdanhmục/null/saitọađộ/haikhảnăng/bảotoànđầuvào. ĐốivớinhómKim,khôngbiếtphasegiữchưabiết;biếtđangsaĐôngchíthìbảngthườngkhôngápvàkhôngtrảphủđịnhtoànphép. Trườnghợp壬申saĐôngchícủavăntrướcvẫnđượcgiữ,côngthứcthườngkhôngghèngoạilệ.

8kiểmđạt;nguồn22QAderivativekhớppixel. Khôngđộngđếnphéptínhgốchoặclạichạy480ngữcảnhcũ/13vídụ/384nétquẻ nếu logicđókhôngđổi. Sốtracứuriêngkhôngphảilá sốnguồnhaycaứngnghiệm. Cáctìnhhuốngxâymới/sửanền/chuẩnBắc/sốđothựccònthuộcadaptervàquytắcriêng,trangoàisốnhãnkhôngđủđểkhuyênngườidùngxâynhàhaytránhngày.

## Bảo toàn và tiếp tục

Snapshottrước`archives/v53-before-home-tomb-diagrams/`giữ3378tệp/sourceZIP2065012551byte. HTMLroot/V53/site707411byte/SHA`549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`,ZIPweb344047bytegiữnguyên;sitechỉindex.html. Nguồn/corpus/QAngoàisite,khôngtăngphiênbảnhoặctựxuấtbản. PhạmviDịchtrướcvẫngiữnguyênbyte,39mớiđầunộidung232;UIKiếnLộcvẫncandidatechờbrowserQA.

Tái kiểm:`node v53/scripts/test-home-tomb-diagrams.mjs`;`python v53/scripts/verify-home-tomb-diagrams-sources.py`;`python v53/scripts/verify-home-tomb-diagrams-release.py --no-write`. Cònmộtđọcthángmở,cácđiềukiệnnguồn vànốiđo/lịchchưađủ;khôngcoikhépđồtốađộlàđãápdụnghếtHiệpKỷ/P03TrạchKinhhoặc40hồsơ.
''',encoding='utf-8')
print('Two source diagrams, bounded direct coordinates and one explicit month-reading ambiguity recorded; exhaustive study active.')
