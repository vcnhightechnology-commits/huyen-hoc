from pathlib import Path
from collections import Counter
import json
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/home-yangzhai-fuyuan'
q=r/'qa/home-yangzhai-fuyuan';report='HOME_FUYUAN_YOUNIAN_REPORT.md'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
step=('P08 — Phúc nguyên/Đại du niên: xem 48 raw DCT tại34–81, gồm47 vị trí mới và1 ranh đọc lại; '
 '12 crop native khớp pixel. Chép tay180 hàng/360 ô năm–giới và40 chú trung ký trước engine. '
 'Tám khẩu quyết tạo64 tọa độ phương dẫn xuất, không gọi64 ô hình chép độc lập. '
 '8 kiểm hoàn chỉnh đạt; lần cuối180 LunarYear1.8.6/360 trường năm và360 HHC directions thực, '
 '360 cung khớp bảng/2880 so nhãn lặp;64 quan hệ khớp tham chiếu Hiệp Kỷ sau alias. '
 'Một lỗi import Windows sau6 kiểm/360 HHC/180 LunarYear được giữ audit; lần chạy lại không thành chứng cứ độc lập. '
 'Giữ lỗi nháp đọc vị trí tay thành cung6/8; ảnh36/41 và bảng xác định nam1/4/7, nữ5/2/8, chưa dùng nháp sai trong web. '
 'Gốc năm sinh/cửa/tọa hướng/cao thấp tách riêng; thiếu gốc hoặc ngữ cảnh trảnull, không dự đoán bệnh/tử vong/tài sản. '
 '87 vị trí khác nhau đã đọc đầu,108 chưa đọc,4/10 khoảng mục đủ đọc đầu,0 tác phẩm áp hết. '
 'Giữ niên khoản萬曆五十二年 chưa xác minh, ranh năm sinh và mặt bằng hiện đại còn mở. '
 '0 HTTP/container/nhân chứng độc lập mới;79 tệp tiếp nhận đúng byte, module nguyên byte. HTML/site/ZIP web nguyên byte.')
nexts=[
 'P08: tiếp108 vị trí chưa đọc: ngoại hình13–33;玄空裝卦94–100;開門100–105;放水105–111;選擇124–168;符鎮168–195. Ranh chia sẻ đã đọc không đếm mới.',
 'Phúc nguyên/Du niên đã có180 hàng/360 ô và8 khẩu quyết, nhưng chưa khép mọi điều kiện. Cần chép từng ô/cửa/đường/cao thấp của các đồ46–56 và82–93; không chọn chỉ theo quái cửa hoặc coi進 là tầng đứng.',
 'Giữ萬曆五十二年 và điểm tay/cung đúng bản đọc; cần nguồn lịch sử độc lập trước đổi niên khoản. Chưa tự chọn ranh Tết/Lập Xuân hoặc nối ngày sinh/mặt bằng.',
 'Các hướng độc lập còn mở: Nhà Xieji tháng ThủyThổ丙辛11hay11–12/Bắc thực/biên lịch; P03 thiếu ảnh; Bát tự vượng suy/cách cục; Tử vi童限火鈴CanhNhâm/khởi hạn; Dịch hiệu lực/B03/MaiHoa. Không lặp tải nguồn bị chặn.',
 'Nghiên cứu và QA ngoài site. Ứng viên UI Kiến Lộc chờ browser QA khả dụng; không vượt cài đặt, không xuất bản.'
]
state=read(b/'STAGED_WORK_STATE.json')
state.update(status='manual-fuyuan-and-declared-younian-reference-verified-rest-active',latestReport='v53/'+report,
 completedStep=step,next=nexts,sourceDirectory='v53/research/home-yangzhai-fuyuan',
 sourcePDF='v53/research/home-yangzhai-shishu/Tianyige-330000-1705-0007405-yangzhai-shishu.pdf',
 sourceUnitMap='v53/research/home-yangzhai-fuyuan/UNIT_MAP.json',referenceModule='v53/research/home-yangzhai-fuyuan/fuyuan-younian-reference.mjs',
 sourceVerification='v53/qa/home-yangzhai-fuyuan/SOURCE_RESULTS.json',
 releaseVerification='v53/qa/home-yangzhai-fuyuan/RELEASE_RESULTS.json; final --no-write required after package')
write(b/'WORK_STATE.json',state)
d=read(w/'EXHAUSTIVE_WORK_STATE.json');d['previousHomeYangzhaiShishuWork']=d['currentWork']
d.update(date='2026-10-28',inProgressScope='v53/research/home-yangzhai-fuyuan/WORK_STATE.json')
d['currentWork']={'catalogueID':'P08','relatedCatalogueIDs':['P08'],'work':'陽宅十書 — 福元/大遊年',
 'reason':'Resolve birth/gate anchor and complete source year-sex coordinates before room-placement logic.',
 'sourceDirectory':'v53/research/home-yangzhai-fuyuan','currentStep':step,'latestResearchReport':'v53/'+report,
 'functionalBacklog':'v53/research/home-yangzhai-fuyuan/WORK_STATE.json',
 'currentSourceUnitMap':'v53/research/home-yangzhai-fuyuan/UNIT_MAP.json',
 'currentContextMap':'v53/research/home-yangzhai-fuyuan/CONTEXT_READINGS.json',
 'sourceLimits':'87/195 positions read first-pass;4/10 main spans;108 unread/all subsidiary clauses open. Annual software correspondence does not establish historical regnal conversion, birth-date boundary, floor-plan geometry, relative heights or empirical outcomes.',
 'nextSourceLead':{'sourceID':'P08-remaining-main-units','status':'active-not-complete','remaining':' '.join(nexts)}}
d['subsequentPriority']=[' '.join(nexts)]+d['subsequentPriority']
for p in [w/'EXHAUSTIVE_WORK_STATE.json',r/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=r/'research/full-study/WORK_STATE.json';d=read(p);d.update(date='2026-10-28',latestResearchReport=report,exhaustiveNext=' '.join(nexts))
item=next(x for x in d['items']if x['id']=='home');assert step not in item['completed'];item['completed'].append(step)
item['remaining'].append(' '.join(nexts));item.update(latestScope='../home-yangzhai-fuyuan/WORK_STATE.json',nextFile='../home-yangzhai-fuyuan/UNIT_MAP.json');write(p,d)
p=r/'research/library-current/COVERAGE.json';d=read(p);d['date']='2026-10-28';e=next(x for x in d['catalogue']if x['id']=='P08')
e.update(currentStatus='research_only',scope='87/195 distinct positions first-pass read,4/10 main spans;180 manually entered year rows/360 sex cells and40 central annotations;8 checks.108 unread/all subsidiary clauses, modern date/geometry/height adapters remain open.',
 latestSourceScope=step,currentSourceUnitCounts={'numberedHeadings':10,'firstPassCompleteBodySpans':4,'wholeUnitsApplied':0,
 'PDFPositions':195,'earlierNativeSizedDerivativePositionsRead':40,'newRawDCTPositionsViewed':48,
 'newDistinctSourcePositionsRead':47,'totalDistinctPositionsRead':87,'unreadPositions':108,
 'manualYearRows':180,'manualSexSpecificCells':360,'centralAnnotations':40,'derivedCompassCells':64},
 latestSourceUnitMap='v53/research/home-yangzhai-fuyuan/UNIT_MAP.json')
for f in ['v53/'+report]+['v53/research/home-yangzhai-fuyuan/'+n for n in ['WORK_STATE.json','UNIT_MAP.json','RAW_IMAGES.json','MANUAL_FUYUAN_TABLE.json','MANUAL_YOUNIAN_SEQUENCES.json','CONTEXT_READINGS.json','READING_CORRECTION_AUDIT.json','PROMOTION_IDENTITIES.json','fuyuan-younian-reference.mjs']]+['v53/qa/home-yangzhai-fuyuan/'+n for n in ['NATIVE_RESULTS.json','REFERENCE_RESULTS.json','TEST_FAILURE_AUDIT.json','SOURCE_RESULTS.json']]:
 if f not in e['currentEvidence']:e['currentEvidence'].append(f)
d['counts']['status']=dict(Counter(x['currentStatus'] for x in d['catalogue']))
assert d['counts']['status']['not_established']==26 and d['counts']['status']['research_only']==5 and d['counts']['wholeWorkApplied']==0
d['counts'].update(newDownloadsThisScope=0,newDownloadsThisScopeBasis='Existing retained PDF only:48 raw-DCT images/47 newly read positions; no HTTP, container or independent witness added.')
d.update(latestFollowup=report+': '+step,latestAcquisitionCounts={'scope':report,'newHTTPRequests':0,'newOriginalRepositoryContainers':0,
 'newIndependentWitnessTextComparisons':0,'newSourceReadPositions':47,'originalDCTImagesViewed':48,'oldBoundaryExpanded':1,
 'nativeLosslessCropsViewed':12,'totalDistinctBookPositionsRead':87,'firstPassChapterSpans':4,'wholeWorksApplied':0});write(p,d)
note='Mốc Phúc nguyên và Đại du niên, 28/10/2026: `'+report+'`. '+step+'\n\n'
for p in [w/'PROJECT_RESEARCH_STATE.md',r/'NEXT_STEPS.md',r/'research/library-current/COVERAGE.md']:
 text=p.read_text(encoding='utf-8-sig');assert not text.startswith(note);p.write_text(note+text,encoding='utf-8')
p=w/'PENDING_RESEARCH_STATE.json';d=read(p)
d.update(date='2026-10-28',status='P08-fuyuan-younian-8checks-verified-rest-active',workDirectory='v53/research/home-yangzhai-fuyuan',
 currentWorkState='v53/research/home-yangzhai-fuyuan/WORK_STATE.json',latestReport='v53/'+report,next=nexts,
 consumerChanged=False,wholeCatalogueCompleted=False,packageVerification='pending-final-no-write')
if 'inProgressStaging' in d:d['previousStaging']={**d.pop('inProgressStaging'),'status':'promoted-awaiting-final-package-verification'}
write(p,d)
print('Updated current coverage:4 source spans,87 read positions,108 unread,0 whole works applied; consumer unchanged.')
