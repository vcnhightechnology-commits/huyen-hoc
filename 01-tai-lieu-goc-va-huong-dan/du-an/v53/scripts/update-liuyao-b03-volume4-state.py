from pathlib import Path
import json
root=Path(__file__).resolve().parent.parent
workspace=root.parent
base=root/'research/liuyao-b03-volume4'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='LIUYAO_B03_VOLUME4_REPORT.md'
e=read(root/'qa/liuyao-b03-volume4/ENGINE_RESULTS.json'); s=e['summary']
assert len(e['checks'])==9 and all(c['ok'] for c in e['checks'])
step=('Đã đọc lần đầu toàn khoảng quyển bốn, PDF30–48 sách đóng B03 thứ hai, và bìa cuối49; '
      '20 bản ghi =17 ảnh mới (16 nội dung/1 bìa)+3 trang mở rộng. 30 mệnh đề có giới hạn. '
      'Tham chiếu riêng Tam hợp/Tam hình xét đủ ba thành viên và ít nhất hai hào động trong cùng bộ ba; '
      '9 kiểm đạt, 64 lời gọi HHC thật và4096 ngữ cảnh riêng/24576 nhóm; 2048 nhóm đủ thành viên,1120 qua tiền đề động. '
      'Hai nhóm Tam hình không thể đủ trong riêng sáu chi bản quẻ theo danh mục; đây là suy ra hữu hạn, '
      'không phải nguồn phủ nhận Tam hình. Chưa ghép chi biến/nhật nguyệt hoặc xét hiệu lực, vượng suy/tổng dự báo. '
      'Đã xem hết49 trang sách đóng2 theo các phạm vi ghi nhận; chưa áp dụng hết nội dung. '
      'HTML707411 byte/site/ZIPweb và tám tham chiếu trước giữ nguyên. B02 vẫn136/103/26, ngày52 còn mâu thuẫn. Toàn kho chưa xong.')
nexts=[
 'Compile remaining full conditional premises in B03 volumes3/4: strength, functional void, horizons, rescue, coexistence; preserve conflicting author positions.',
 'Determine source-explicit completion by changed lines/day/month for 三合/三刑 before expanding primary-only gates; 子卯/self-punishments remain separate.',
 'Acquire identified physical books3..6 once, with API/raw/TLS/SHA and direct reading; do not count book2 first-pass coverage as all14volumes applied.',
 'B02 still103heading-only body units/7partial foundations; independent PDF52 date-void witness and other MaiHoa/Bazi/Tuvi/Home catalogue gaps remain.'
]
write(base/'WORK_STATE.json',{'date':'2026-10-27','status':'private-primary-triad-prerequisites-complete-full-premises-and-later-books-active',
 'sourceID':'B03-book2','latestReport':'v53/'+report,'privateReference':'triad-reference.mjs','completedStep':step,
 'volume4RelevantSpanFirstPassRead':True,'allVolume4ClausesApplied':False,
 'physicalBook2AllPagesViewedWithRecordedScope':True,'unreadPhysicalBook2Pages':[],
 'newOriginalPDFs':0,'newHTTPBodies':0,'newLocalRenders':17,'expandedReadings':3,
 'manualPages':list(range(30,50)),'operationalClauses':30,
 'primaryOnly':True,'changedOrCalendarCompletion':False,'effectiveTriadModel':False,
 'next':nexts,'consumerChanged':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False})
d=read(workspace/'EXHAUSTIVE_WORK_STATE.json')
d['currentWork'].update(currentStep=step,latestResearchReport='v53/'+report,
 sourceDirectory='v53/research/liuyao-b03-volume4',
 internalB03TriadReference='v53/research/liuyao-b03-volume4/triad-reference.mjs',
 currentB03Volume4PassageMap='v53/research/liuyao-b03-volume4/MANUAL_READINGS.json',
 functionalBacklog='v53/research/liuyao-b03-volume4/WORK_STATE.json')
d['currentWork']['sourceLimits']='B03 physical books1/2 retained and hash-verified, not all6books/14textualvolumes. Book2 all49pages viewed by recorded scope: covers1/49, volume3 PDF2..29, volume4 PDF30..48; first-pass coverage is not exhaustive clause application. Primary-only triads lack changed/day/month completion and effective formation. B02 PDF52 date-void inconsistency and independent pedigree remain open.'
d['currentWork']['nextSourceLead'].update(status='downloaded-byte-verified-first-pass-page-coverage-complete',
 remaining='Book2 remaining clauses and independent collation; physical books3..6 not yet acquired.')
d['inProgressScope']='v53/research/liuyao-b03-volume4/WORK_STATE.json'
d['subsequentPriority'][0]=' '.join(nexts)
for p in [workspace/'EXHAUSTIVE_WORK_STATE.json',root/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=root/'research/full-study/WORK_STATE.json'; d=read(p)
d['latestResearchReport']=report
d['exhaustiveNext']='B03book2 all49pages now viewed by recorded scopes; compile all remaining volume3/4premises and changed/calendar triad completion, acquire books3..6. B02counts136/103/26unchanged; other library gaps remain.'
yi=next(x for x in d['items'] if x['id']=='yi')
entry=('B03 volume4 PDF30..48 first-pass relevant span read,49cover;20records/17newrenders/3expanded. '
       '30bounded clauses and private primary triad prerequisite reference;9checks/64actualHHC/4096privatecontexts,2048completegroups/1120motion-qualified. '
       'Three-member punishments have0completeprimary-onlygroups; source efficacy/calendar/changed-line completion not established. Consumer/eight prior references unchanged.')
if entry not in yi['completed']:yi['completed'].append(entry)
yi['latestScope']='../liuyao-b03-volume4/OPERATIONAL_CLAUSES.json'
yi['remaining']=[x for x in yi['remaining'] if not x.startswith('LiuYaoB03:book1full384lineannotations/')]
yi['remaining'].append('LiuYaoB03:book1full384annotations/prefaces and all book2 volume3/4clauses not applied; first-pass page coverage of book2 complete. Primary triads do not yet include changed/day/month completion, 子卯/self-punishments, strength/efficacy/timing. Books3..6unacquired. B02still103heading-only/PDF52date-voidconflict.')
write(p,d)
p=root/'research/library-current/COVERAGE.json';d=read(p);b=next(x for x in d['catalogue'] if x['id']=='B03')
b['scope']='Giữ byte sách đóng1/2. Sách2 đã xem49trang theo phạm vi: quyển3 PDF2–29 vàquyển4 PDF30–48 đọc lầnđầu toàn khoảng,1/49bìa. Quyển4 thêm30mệnhđề vàcổng tiềnđề Tamhợp/Tamhình riêng. Chưa áp dụng mọi mệnhđề/384chúhào/tiềntự/cácsách3–6 hoặc dựbáo.'
b['localPossession'][1]='Sách đóng2: PDF49trang/41224832byte/SHA c1e1027331d43769733c6011b4fe99e90928e9fde013fce563c8e9bad81c04bf; APIrevision754088942/TLS/hash. Đã xem hết49trang theo phạmvi ghi nhận, không đồng nghĩa áp dụng hết nội dung.'
b['latestLocalReadingScope']='Quyển4 PDF30–48 vàbìa49:20bản ghi,17ảnhmới/3mởrộng,30mệnhđề cógiớihạn.9kiểm/64HHCthật/4096ngữcảnh riêng;hiệulực/chibiến/nhậtnguyệt chưaápdụng.0HTTP/PDFgốc mới.'
for f in ['v53/'+report]+['v53/research/liuyao-b03-volume4/'+n for n in ['MANUAL_READINGS.json','TRIAD_TABLES.json','OPERATIONAL_CLAUSES.json','SOURCE_AUDIT.json','triad-reference.mjs']]+['v53/qa/liuyao-b03-volume4/ENGINE_RESULTS.json']:
 if f not in b['currentEvidence']:b['currentEvidence'].append(f)
d['latestFollowup']=report+':19volume4contentpages/cover first-pass,30clauses,9checks/64HHC/4096primarymotioncontexts. Book2 pagecoverage complete, not wholebook applied. Consumer unchanged.'
d['latestAcquisitionCounts']={'scope':report,'originalPDFs':0,'retainedHTTP200Bodies':0,'newLocalRenders':17,
 'manualImageRecords':20,'newContentPages':16,'expandedEarlierPages':3,'coverPages':1,'volume4ContentSpanPages':19,'fullBooksApplied':0}
d['counts']['newDownloadsThisScope']=0
assert d['counts']['wholeWorkApplied']==0;write(p,d)
note='Mốc B03–Luận4 27/10/2026: `'+report+'`. '+step+'\n\n'
for p in [workspace/'PROJECT_RESEARCH_STATE.md',root/'NEXT_STEPS.md',root/'research/library-current/COVERAGE.md']:
 text=p.read_text(encoding='utf-8-sig')
 if text.startswith('Mốc B03–Luận4 27/10/2026:'):text=text.split('\n\n',1)[1]
 p.write_text(note+text,encoding='utf-8')

report_text=f'''# B03: quyển bốn và tiền đề Tam hợp/Tam hình

Ngày 27/10/2026. Đây là nghiên cứu nội bộ; không đưa nguồn hoặc phòng kiểm định vào site.

## Phạm vi đọc và bằng chứng

Tái sử dụng byte PDF sách đóng thứ hai đã tải ở phạm vi trước: 41.224.832 byte, 49 trang, SHA-256 `{read(base/'SOURCE_AUDIT.json')['sourceSHA256']}`. Không có HTTP hoặc PDF gốc mới. Hồ sơ API revision754088942/TLS/raw ở `research/liuyao-b03-volume3/` được giữ nguyên.

Đã xem lần đầu toàn khoảng quyển bốn, PDF30–48, và bìa49: 20 bản ghi, 17 ảnh mới (16 nội dung và một bìa), ba ảnh30–32 mở rộng phần đọc trước. PDF30 in `卜筮正宗卷之四`, `黃金策總斷千金賦直解`; PDF48 có `卜筮正宗卷之四終`. Sách đóng2 hiện đủ49trang đã xem theo phạm vi ghi nhận, gồm phần quyển ba ở hồ sơ trước. Không có OCR, bản chép ngoại giao toàn trang hoặc tuyên bố mọi câu đều được áp dụng.

`MANUAL_READINGS.json` giữ chủ đề và SHA ảnh từng trang. `OPERATIONAL_CLAUSES.json` ghi30mệnh đề có giới hạn, tách hỏi gì, đối tượng, vượng suy, thời hạn, động/tĩnh và cứu hộ. Nguồn nói về thành tín, thần minh hoặc y bệnh là dữ liệu lịch sử; không phải chỉ thị từ người dùng hay bằng chứng kiểm nghiệm khả năng dự đoán.

## Chức năng riêng mới

`triad-reference.mjs` nhận sáu giá trị6/7/8/9 từ dưới lên. Theo đoạn PDF39, bốn nhóm Tam hợp và hai nhóm Tam hình ba thành viên được kiểm tra: đủ mỗi chi trong riêng sáu hào bản quẻ, sau đó có ít nhất hai hào động trong cùng một bộ ba. Cách hiểu “ít nhất hai” là chuẩn hóa thao tác có ghi rõ, không giả làm một câu nguyên văn bổ sung.

Mỗi chi được gắn với đúng vị trí hào; hai bản sao của cùng một chi không thay thế chi còn thiếu. Kết quả chỉ là tiền đề cấu trúc. Chưa bổ sung chi biến, nhật/nguyệt, 子卯 hoặc tự hình; chưa kết luận hợp hóa, hiệu lực, cát hung hoặc ứng kỳ. Những trường đó giữ `null`. Hào tĩnh không bị gán giả chi biến. Đối số lịch/vượng suy không hỗ trợ bị từ chối rõ ràng.

## Kiểm chứng

Đạt9kiểm: {s['actualHHCHexCalls']} lời gọi HHC thật cho64số quẻ; đối chiếu Nạp Giáp bằng các dãy độc lập; {s['privateFigureMotionContexts']}ngữ cảnh quẻ/động riêng so bằng cách chọn20bộ ba vị trí, khác với thuật toán tích Descartes của chức năng. Đây không phải4096lời gọi HHC mới hoặc tỷ lệ ứng nghiệm.

Trong24576nhóm/ngữ cảnh, có{s['completeGroups']}nhóm đủ thành viên, {s['qualifyingGroups']}nhóm qua tiền đề động, {s['witnesses']}bộ ba chứng kiến. 22dạng bản quẻ có chi lặp; kiểm tra đã loại trường hợp dùng lặp chi để bù thành viên thiếu. Digest `{s['graphDigest']}`.

Điểm giới hạn quan trọng: cả hai Tam hình ba thành viên có0nhóm đủ trong riêng sáu chi bản quẻ trên danh mục64quẻ. Đây là suy ra hữu hạn từ cấu trúc Nạp Giáp đã kiểm, không phải khẳng định sách phủ nhận Tam hình. Muốn xét các trường hợp của sách phải đọc và xác minh cách ghép chi biến/nhật nguyệt trước; không tự thêm chúng để tạo kết quả.

HTML vẫn707411byte/SHA`549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`; site và ZIPweb giữ nguyên. Tám tham chiếu cũ và bản phát hành trước được bảo tồn ở `archives/v53-before-liuyao-b03-volume4/`. Gói nguồn được đồng bộ riêng, kiểm manifest/ZIP và byte trước đó.

## Phần còn mở

Mọi mệnh đề quyển ba/bốn chưa được biên dịch đầy đủ; chưa có mô hình tổng vượng suy, chân không, tự chọn Dụng thần hoặc thời điểm/dự báo hoàn chỉnh. Sách đóng3–6 chưa tải. B02 còn136đơn vị đăng ký/103thân mục mức đề mục/26khoảng đọc lần đầu; mâu thuẫn ngày–tuần không PDF52 chưa giải quyết. Toàn kho40tài liệu và cả bốn mục lớn chưa hoàn tất.
'''
(root/report).write_text(report_text,encoding='utf-8')
print('Updated current state; no whole-book or whole-catalogue completion claim.')
