from pathlib import Path
import json
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/bazi-jianlu-coordinates'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='BAZI_JIANLU_COORDINATES_REPORT.md';result=read(r/'qa/bazi-jianlu-coordinates/RESULTS.json');assert len(result['checks'])==9 and all(x['ok']for x in result['checks'])
step=('Bát tự: chép đủ10bộ canngày–chitháng–trụgiờ trong Kiến Lộc ảnh223–224/tờ113a–b, '
 'hai trang mở rộng lượtđọc cũ/1cropQA,0trangnguồn/HTTP/container mới. '
 'Giữ3dịdạng己/巳 giữa ảnh vàbảnsố;hàng癸vắtqua hai ảnh. '
 '9kiểm đạt:120HHC BátTự+120lunar thật trên10ngày×12giờ,10giờnguồn đều khảthi/cóThấtSát ởcanlộ hoặctàngtrụgiờ;120ngữcảnhtháng riêng. '
 'Tham chiếu riêng phânbiệt khớptọađộ/thànhcách/vượngsuy/dụngthần,thiếugiờgiữnull. '
 'Nghi vấn丙日己亥 do tínhnhẩm banđầu đãbịruntime bácbỏ;không sửa sách. '
 '38mệnhđề/ma trận10đềmục cũ giữbyte;chưa đầyđủđiềukiệncáchcục/toànkho. HTML707411byte/site/ZIPweb nguyên.')
nexts=[
 'Bazi Jianlu ten day/month/hour sourcecoordinates are extracted;do notrepeat120charts or38priorclauses withoutlogicchange. Need fullcondition extraction around财官印食/too-many杀/strength/monthroots/yearhourlocation,with explicit sourcevoices;宜 isnot unconditional success.',
 'Read complete source sections and crossreferences前論禄/羊刄煞 in otherretainedvolumes;identify independentfacsimile/editiondate and486/487pageissue,notonlysameWYGtext. No automatic strength/usefulgod orhighstakes outcome inferred.',
 'Otherdomains stillopen: Tuvi independentwitness/Canh-Nhâm/ageboundaries;Home completeflyingstars/contextmodel;Yi B02chapter35from191/runningvolumeconflict/B03fullclauses/MaiHoa. Current B02mapremains136/96/32/7+1partial/0full.',
 'Preserve B02Japan7bodies/403/TLSnullflags/gengambiguity;whole40catalogue andfourdomainsactive. Keepresearchoutsideconsumer site.'
]
write(b/'WORK_STATE.json',{'date':'2026-10-27','status':'ten-source-coordinate-rows-and-private-matcher-verified-fullpatternconditions-active',
 'sourceID':'M01-WYG-005-jianlu','latestReport':'v53/'+report,'completedStep':step,'summary':result['summary'],'next':nexts,
 'sourceHourConflictFound':False,'sourceHourEmended':False,'wholeSectionApplied':False,'consumerChanged':False,'wholeCatalogueCompleted':False})
d=read(w/'EXHAUSTIVE_WORK_STATE.json');d['currentWork'].update(catalogueID='M01',relatedCatalogueIDs=['M01','M02'],work='三命通會 — Kiến Lộc ngày/tháng/giờ',
 reason='Completing explicit source coordinates and premises before a pattern classifier.',sourceDirectory='v53/research/bazi-jianlu-coordinates',currentStep=step,
 latestResearchReport='v53/'+report,functionalBacklog='v53/research/bazi-jianlu-coordinates/WORK_STATE.json',internalJianluReference='v53/research/bazi-jianlu-coordinates/jianlu-reference.mjs',
 sourceLimits='Ten source coordinate rows/two expandedpreviouspages only;no fullpattern/strength/usefulgod. Prior38clauses unchanged;40cataloguewhole0.',
 nextSourceLead={'sourceID':'M01-WYG','status':'fullconditions-and-crossreferences-open','file':'v53/research/bazi-pattern-witness/CADAL06066041.djvu','remaining':' '.join(nexts)})
d['inProgressScope']='v53/research/bazi-jianlu-coordinates/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in[w/'EXHAUSTIVE_WORK_STATE.json',r/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=r/'research/full-study/WORK_STATE.json';d=read(p);d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts)
item=next(x for x in d['items']if x['id']=='bazi');item['completed'].append(step);item['remaining'].append(' '.join(nexts));item['latestScope']='../bazi-jianlu-coordinates/WORK_STATE.json';write(p,d)
p=r/'research/library-current/COVERAGE.json';d=read(p);entry=next(x for x in d['catalogue']if x['id']=='M01');entry['latestJianluScope']=step
for f in ['v53/'+report]+['v53/research/bazi-jianlu-coordinates/'+n for n in ['SOURCE_ROWS.json','MANUAL_READINGS.json','SOURCE_AUDIT.json','WORK_STATE.json','jianlu-reference.mjs']]+['v53/qa/bazi-jianlu-coordinates/RESULTS.json']:
 if f not in entry['currentEvidence']:entry['currentEvidence'].append(f)
d['latestFollowup']=report+': '+step;d['latestAcquisitionCounts']={'scope':report,'newHTTPRequestsThisRun':0,'retainedHTTPBodiesNewToRelease':0,'newOriginalContainers':0,'newSourcePages':0,'expandedPreviouslyReadPages':2,'QACrops':1,'sourceTriplets':10,'wholeWorksApplied':0}
d['counts']['newDownloadsThisScope']=0;d['counts']['newDownloadsThisScopeBasis']='Existing226pageDjVu andtwoalreadyretainednativeimages expanded;one localQAcrop,noHTTP,newcontainerornewsourcepage.'
assert d['counts']['wholeWorkApplied']==0;write(p,d)
note='Mốc Bát tự–Tọa độ Kiến Lộc, 27/10/2026: `'+report+'`. '+step+'\n\n'
for p in[w/'PROJECT_RESEARCH_STATE.md',r/'NEXT_STEPS.md',r/'research/library-current/COVERAGE.md']:
 t=p.read_text(encoding='utf-8-sig')
 if not t.startswith(note):p.write_text(note+t,encoding='utf-8')
write(w/'PENDING_RESEARCH_STATE.json',{'date':'2026-10-27','status':'Bazi-jianlu-current-scope-active','workDirectory':'v53/research/bazi-jianlu-coordinates',
 'currentWorkState':'v53/research/bazi-jianlu-coordinates/WORK_STATE.json','latestReport':'v53/'+report,'checks':'v53/qa/bazi-jianlu-coordinates/RESULTS.json',
 'next':nexts,'consumerChanged':False,'wholeCatalogueCompleted':False})
(r/report).write_text('''# Bát tự: mười tọa độ Kiến Lộc và tiền đề giờ

Đã trích đủ mười hàng can ngày/chi tháng/trụ giờ từ đoạn Kiến Lộc ở ảnh DjVu223–224, tờ WYG113a–b. Đây là mở rộng hai trang đã giữ và đã đọc có mục tiêu; **0trang nguồn mới,0HTTP/container mới**. Một crop QA từ byte native223 xác nhận 己亥. Hàng癸 nằm qua223–224,không gán toàn câu cho một tờ. Container226trang giữSHA013ce4861680a2bf08b811050c45a45bb2d3ce9d164f7e2341d7070bd5cb2c1a; bản sốSHA1ebdd92feaa57496b702f962ad6fafd4f19c17e98c38a94b40f626ef321dd997. Hai vật mang cùng họ WYG không được coi là hai truyền bản độc lập.

| Can ngày | Chi tháng nguồn | Trụ giờ in |
|---|---|---|
|甲|寅|壬申|
|乙|卯|辛巳|
|丙|巳|己亥|
|丁|午|庚子|
|戊|巳|甲寅|
|己|午|乙丑|
|庚|申|丙戌|
|辛|酉|丁酉|
|壬|亥|戊申|
|癸|子|己未|

Ba chỗ bản số giữ巳 trong vị trí can (丙…巳亥,巳日…,癸…巳未) trong khi ảnh/chuẩn hóa theo vai trò là己. Lưu literal bản số riêng,không sửa byte so khớp. Các vị trí chi巳 vẫn giữ巳. Nghi vấn tính nhẩm ban đầu rằng丙日己亥 bất khả thi **đã bị bác bỏ**: khởi戊子 và đếm đến亥 cho己亥. Không có lỗi sách hay lỗi sản phẩm cần sửa; dùng乙亥 chỉ làm đối chứng âm tính.

## Tham chiếu và kiểm chứng thực thi

`jianlu-reference.mjs` là công cụ riêng so tọa độ, yêu cầu khai báo rõ can ngày. Chi tháng hoặc giờ chưa biết trảnull; sai tọa độ trảfalse. Có kiểm khả năng phối can ngày/can giờ theo quy ước Ngũ Thử Độn đã lưu nguồn riêng trước đây,không suy phép này từ riêng chữ宜. Đủ ba trường chỉ nghĩa khớp dòng nguồn;thành cách/vượng suy/dụng thần/kết quả vẫnnull. Không tự chọn ranh lịch hiện đại cho chương cổ. Lời liền sau về見煞 và không quá nhiều sát vẫn là tiền đề,chưa trở thành phép chấm tốt/xấu.

**9kiểm đạt**,có120lời gọi HHC Bát tự và120lời gọi lunar-typescript1.8.6 thật trên10ngày hiện đại×12giờ,bốn trụ khớp toàn mẫu. Runtime được kiểm byte theo audit đã giữ. Mỗi hàng giờ nguồn có một fixture thực thi khớp đầy đủ can ngày/chi tháng/trụ giờ. Cả10cóThấtSát tại can lộ hoặc tàng chi trụ giờ theo bảng cấu trúc đang dùng;không từ đó suy sát hữu lực hay phú quý. 120ngữcảnh canngày×chitháng riêng phân biệt đúng10tọađộ tháng;đây không phải120lời gọi thư viện khác. Thiếu/sai/null,đầu vào không hợp lệ và bảo toàn dữ liệu được kiểm.

Probe dò fixture trước bộkiểm giữ riêng:10HHC,41lunar dò ngày và10lunar sofixture;không cộng gộp chúng thành ca nguồn độc lập hoặc gọi phép đối runtime là chứng cứ nghiệm lý. Ngày2020chỉ dựng ví dụ cho phép tính,không phải ngày sinh lịch sử. Bảng38mệnhđề vàma trận10đềmục trước giữ nguyênbyte;phạm vi mới thêm10hàng tọa độ,không đổi38thành48mệnhđề hay tuyên bốđãhếtchương.

## Bảo toàn và tiếp tục

Snapshot trước giữ2901tệp/sourceZIP2017947166byte ở`archives/v53-before-bazi-jianlu-coordinates/`. RootHTML/V53/site707411byte/SHA549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857,ZIPweb344047byte giữnguyên;site chỉindex.html. Nguồn/QA ởngoài site;không xuất bản mạng.

Tiếp trọn điều kiện từng cách/mùa/căn/thân/tài-quan-ấn-thực/chế-hợp vàthamchiếu trước về禄/羊刄煞 trong đúng truyền bản;niênđại/độđủcontainer/NCL1915và487–486còn mở. Tửvi/Nhàở/KinhDịch vàtoàn40nguồn vẫn**active-not-complete**.
''',encoding='utf-8')
print('Current research updated;full pattern and catalogue remain open.')
