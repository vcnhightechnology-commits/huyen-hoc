from pathlib import Path
import json
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/home-yangzhai-door-water';report='HOME_DOOR_WATER_REPORT.md'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
step=('P08: đọc18 raw DCT94–111,16 vị trí mới95–110/2 ranh mở rộng,12 crop native khớp pixel. '
 'Khép3 khoảng đọc đầu玄空裝卦/開門/放水, tổng103/195 vị trí/7trên10khoảng mục,92 vị trí chưa đọc và mọi điều kiện phụ còn mở. '
 'Chép24 hàng phóng thủy:46 mục dấu phương chính/8 dòng chú bên16 mục dấu,không gộp. '
 'Nhóm âm-dương12/12 dấu riêng,4 alias chính phương tường minh. Bộ tra cứu đòi gốc山龍 và nước đi; '
 'gốc năm sinh/hướng cửa/chưa rõ hoặc nước đến trảnull,không biến không-liệt-kê thành xấu. '
 '8 kiểm đạt/72 chiều nước/72 gốc thay thế;8 HHCdirections thật khớp4 cặp phòng延年chiếu2chiều,0lịch mới. '
 'Không so sao phóng thủy với cung hiện đại giả định. 48 tệp tiếp nhận đúngbyte/module nguyênbyte; '
 'giữ audit cropđích sai/sửa và đườngdẫn test sửa trước chạy bản tiếp nhận,không chạylại runtime để tăngsố. '
 'Thước cửa/ngày tháng/đổi hào đủ điều kiện/Bắc thực/hình học/thủy lực/hiệu quả nguồn chưa xác lập. '
 '0HTTP/container/nhânchứngđộclậpmới. HTML/site/ZIPweb nguyênbyte,toànkho active.')
nexts=[
 'P08:92 vị trí chưa đọc gồm ngoại hình13–33, tuyển trạch125–167, phù trấn168–195.124 là ranh đã đọc;không tính lại. Khép lượt đọc trước khi tự công bố toàn tác phẩm.',
 'Các mục đã đọc còn nhiều điều kiện: toàn phép交門/換象/初爻94–100; bảng lịch/mặt-thước/đơn vị cửa100–104;gốcphóngthủy/FukYuan-gate/đồ111;12đồphânviện/cao-thấp46–56và82–93. Không biến tiến trình đọc thành áp hết.',
 'Niên khoản萬曆五十二年 chưa xác minh,ranh Tết/LậpXuân,Bắc từ–Bắc thật và mặt bằng hiện đại chưa thiết lập. Khó chốt một hướng thì tiếp phần độc lập.',
 'Nhà Xieji/P03,Bát tự vượng suy/cách cục,Tử vi童限火鈴CanhNhâm/khởi hạn,Dịchhiệu lực/B03/MaiHoa còn mở. Không lặp tải nguồn bị chặn hoặc kiểm đã đạt.',
 'Nghiên cứu/QA ngoài site. UIKiếnLộc chờbrowserQAkhảdụng;khôngvượtcàiđặt,khôngxuấtbản.'
]
s=read(b/'STAGED_WORK_STATE.json');s.update(status='three-new-spans-source-water-lookup-8checks-verified-rest-active',
 latestReport='v53/'+report,completedStep=step,next=nexts,sourceDirectory='v53/research/home-yangzhai-door-water',
 sourceUnitMap='v53/research/home-yangzhai-door-water/UNIT_MAP.json',
 sourceVerification='v53/qa/home-yangzhai-door-water/SOURCE_RESULTS.json',
 releaseVerification='v53/qa/home-yangzhai-door-water/RELEASE_RESULTS.json; final no-write required after package');write(b/'WORK_STATE.json',s)
d=read(w/'EXHAUSTIVE_WORK_STATE.json');d['previousHomeFuyuanYounianWork']=d['currentWork'];d.update(date='2026-10-28',inProgressScope='v53/research/home-yangzhai-door-water/WORK_STATE.json')
d['currentWork']={'catalogueID':'P08','relatedCatalogueIDs':['P08'],'work':'陽宅十書 — 玄空裝卦/開門/放水',
 'reason':'Finish missing chapter spans and separate literal outflow table, source polarity and opposite-room relation contexts.',
 'sourceDirectory':'v53/research/home-yangzhai-door-water','currentStep':step,'latestResearchReport':'v53/'+report,
 'functionalBacklog':'v53/research/home-yangzhai-door-water/WORK_STATE.json','currentSourceUnitMap':'v53/research/home-yangzhai-door-water/UNIT_MAP.json',
 'currentContextMap':'v53/research/home-yangzhai-door-water/CONTEXT_READINGS.json',
 'sourceLimits':'103/195 positions first-pass read;7/10mainspans;92unread/allsubsidiaryclausesopen. No complete first-draw exchange, ruler/calendar, geometry/north or hydraulic/predictive adapter.',
 'nextSourceLead':{'sourceID':'P08-remaining-main-units','status':'active-not-complete','remaining':' '.join(nexts)}}
d['subsequentPriority']=[' '.join(nexts)]+d['subsequentPriority']
for p in [w/'EXHAUSTIVE_WORK_STATE.json',r/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=r/'research/full-study/WORK_STATE.json';d=read(p);d.update(date='2026-10-28',latestResearchReport=report,exhaustiveNext=' '.join(nexts));i=next(x for x in d['items']if x['id']=='home')
assert step not in i['completed'];i['completed'].append(step);i['remaining'].append(' '.join(nexts));i.update(latestScope='../home-yangzhai-door-water/WORK_STATE.json',nextFile='../home-yangzhai-door-water/UNIT_MAP.json');write(p,d)
p=r/'research/library-current/COVERAGE.json';d=read(p);d['date']='2026-10-28';e=next(x for x in d['catalogue']if x['id']=='P08')
e.update(currentStatus='research_only',scope='103/195 distinct positions first-pass read,7/10mainspans;24manual outflow rows/46main+16marginaltargetentries;24polaritymarks;8checks/8actualHHCdirectioncalls.92unread/fullconditions/ruler/date/geometry/hydraulicsremainopen.',
 latestSourceScope=step,currentSourceUnitCounts={'numberedHeadings':10,'firstPassCompleteBodySpans':7,'wholeUnitsApplied':0,'PDFPositions':195,
 'earlierDistinctPositionsRead':87,'newRawDCTPositionsViewed':18,'newDistinctSourcePositionsRead':16,'totalDistinctPositionsRead':103,'unreadPositions':92,
 'manualOutflowRows':24,'mainTargetEntries':46,'marginalRows':8,'marginalTargetEntries':16,'sourcePolarityMarks':24},latestSourceUnitMap='v53/research/home-yangzhai-door-water/UNIT_MAP.json')
for f in ['v53/'+report]+['v53/research/home-yangzhai-door-water/'+n for n in ['WORK_STATE.json','UNIT_MAP.json','RAW_IMAGES.json','CONTEXT_READINGS.json','MANUAL_WATER_TABLE.json','MANUAL_SOURCE_POLARITY.json','MANUAL_ROOM_PAIR_ANCHORS.json','source-water-reference.mjs','PROMOTION_IDENTITIES.json']]+['v53/qa/home-yangzhai-door-water/'+n for n in ['REFERENCE_RESULTS.json','NATIVE_RESULTS.json','SOURCE_RESULTS.json','CROP_TARGET_AUDIT.json','PROMOTION_PATH_CORRECTION.json']]:
 if f not in e['currentEvidence']:e['currentEvidence'].append(f)
assert d['counts']['wholeWorkApplied']==0
d['counts'].update(newDownloadsThisScope=0,newDownloadsThisScopeBasis='Existing retained PDF only;18rawJPEGs/16newpositions/2expandedboundaries.NoHTTP/container/independentwitness.')
d.update(latestFollowup=report+': '+step,latestAcquisitionCounts={'scope':report,'newHTTPRequests':0,'newOriginalRepositoryContainers':0,
 'newIndependentWitnessTextComparisons':0,'newSourceReadPositions':16,'originalDCTImagesViewed':18,'oldBoundariesExpanded':2,
 'nativeLosslessCropsViewed':12,'totalDistinctBookPositionsRead':103,'firstPassChapterSpans':7,'wholeWorksApplied':0});write(p,d)
note='Mốc Trang quái, cửa và phóng thủy,28/10/2026: `'+report+'`. '+step+'\n\n'
for p in [w/'PROJECT_RESEARCH_STATE.md',r/'NEXT_STEPS.md',r/'research/library-current/COVERAGE.md']:
 text=p.read_text(encoding='utf-8-sig');assert not text.startswith(note);p.write_text(note+text,encoding='utf-8')
p=w/'PENDING_RESEARCH_STATE.json';d=read(p);d.update(date='2026-10-28',status='P08-door-water-8checks-verified-rest-active',
 workDirectory='v53/research/home-yangzhai-door-water',currentWorkState='v53/research/home-yangzhai-door-water/WORK_STATE.json',
 latestReport='v53/'+report,next=nexts,consumerChanged=False,wholeCatalogueCompleted=False,packageVerification='pending-final-no-write')
if 'inProgressStaging'in d:d['previousStaging']={**d.pop('inProgressStaging'),'status':'promoted-awaiting-finalpackageverification'}
write(p,d)
print('Coverage103/195read;7/10spans;92unread;0wholeworksapplied;consumerunchanged.')
