from pathlib import Path
import json
root=Path(__file__).resolve().parent.parent;w=root.parent;base=root/'research/liuyao-b03-book3'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='LIUYAO_B03_BOOK3_REPORT.md';e=read(root/'qa/liuyao-b03-book3/ENGINE_RESULTS.json');s=e['summary']
assert len(e['checks'])==10 and all(c['ok']for c in e['checks'])
step=('Đã đọc phần còn lại sách đóng3 B03: 43 ảnh mới (41 trang nội dung26–66, hai bìa1/67), '
 '8 trang đọc mở rộng (8 và19–25), hai cropQA. Định vị trực tiếp cuối quyển5 ở30, quyển6 ở31–48, quyển7 ở49–66. '
 'Cả67trang đã xem theo phạm vi ghi nhận; 12 khoảng mục đọc lần đầu, trong đó8mục mới/khép khoảng trước, chưa áp dụng hết từng mục. '
 'Thêm20mệnh đề có giới hạn; các đoạn hôn nhân/sinh nở/bệnh tật/thuốc/khấn lễ giữ lịch sử, không biến thành kết luận người dùng. '
 'Bộ riêng kiểm tọa độ ra tuần của chi gốc đã chỉ định; câu nguồn không tự thêm điều kiện động/tĩnh. '
 '10kiểm đạt,64lời gọiHHC thật chỉ số quẻ,180lời gọi lunar thật trên62ngày độc nhất/60mốc canchi; '
 '46080ngữ cảnh riêng,7680cờkhông, mỗi độ lệch1–10ngày có768ngữ cảnh. Chưa chânkhông/ứngkỳ/hiệulực hay ngày dựbáo. '
 '0HTTP/PDFgốc mới. HTML707411byte/site/ZIPweb và10thamchiếutrước giữ nguyên. B02vẫn136/103/26,ngày52mở; toàn kho chưa hoàn tất.')
nexts=[
 'B03book3 all67pages viewed by recorded scope, not every clause applied. Complete condition ledger and reconcile quotations/roles across volumes3/5/6/7 without merging author polemic and quoted positions.',
 'Extend source timing only after checking full premises: monthbreak/current-month boundaries, strength/functional void, near/far day/hour/month horizons, rescue/hidden original spirit and source-specific priority. Raw xun exit is not a predicted event.',
 'Acquire identified B03physicalbook4 once with API/raw/TLS/size/SHA, locate its textual volumes and chapter boundaries. Books4..6 currently unacquired; avoid duplicate acquisitions and unbounded new editions.',
 'Earlier B03book1full384line annotations/prefaces and book2allclauses/triadcompletion remain. B02still103heading-only body units/PDF52date-void conflict, and MaiHoa/Bazi/Tuvi/Home/library gaps remain.'
]
write(base/'WORK_STATE.json',{'date':'2026-10-27','status':'private-raw-xun-exit-complete-book3-first-pass-complete-full-clauses-and-later-books-active',
 'sourceID':'B03-book3','latestReport':'v53/'+report,'privateReference':'xun-exit-reference.mjs','unitMap':'BOOK3_CURRENT_UNITS.json',
 'completedStep':step,'newManualPages':[1]+list(range(26,68)),'expandedManualPages':[8]+list(range(19,26)),
 'all67PagesViewedByRecordedScope':True,'unviewedPages':[],'firstPassRelevantSpanUnits':12,
 'newOrCompletedSpanUnits':8,'allBook3ClausesApplied':False,'newHTTPBodies':0,'newOriginalPDFs':0,
 'newContentRenders':41,'newCoverRenders':2,'QAOnlyRenders':2,'boundedOperationalClauses':20,
 'rawXunExitCoordinateOnly':True,'functionalVoidModel':False,'fullTimingAdjudicator':False,
 'calendarInstantAdapter':False,'consumerChanged':False,'next':nexts,'wholeBookApplied':False,'wholeCatalogueCompleted':False})
d=read(w/'EXHAUSTIVE_WORK_STATE.json')
d['currentWork'].update(currentStep=step,latestResearchReport='v53/'+report,sourceDirectory='v53/research/liuyao-b03-book3',
 internalB03XunExitReference='v53/research/liuyao-b03-book3/xun-exit-reference.mjs',
 currentB03Book3UnitMap='v53/research/liuyao-b03-book3/BOOK3_CURRENT_UNITS.json',
 functionalBacklog='v53/research/liuyao-b03-book3/WORK_STATE.json')
d['currentWork']['sourceLimits']='B03physicalbooks1/2/3retained, not all6/14textualvolumes. Book2 all49pages and book3 all67pages viewed by recorded scopes; not all clauses applied. Book3 textualvolumes5/6/7 have12first-pass relevant section spans,0entireunitsapplied. Raw xun exit and prior4timingtargets do not establish efficacy/fulltiming. B02PDF52date-void and independent pedigree remain unresolved.'
d['currentWork']['nextSourceLead'].update(status='downloaded-byte-verified-book3-first-pass-page-coverage-complete',
 remaining='Book3allclauses/conditional model and independent collation; physicalbooks4..6notyetacquired.')
d['inProgressScope']='v53/research/liuyao-b03-book3/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in[w/'EXHAUSTIVE_WORK_STATE.json',root/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=root/'research/full-study/WORK_STATE.json';d=read(p);d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts)
yi=next(x for x in d['items']if x['id']=='yi')
entry=('B03book3remaining43pages now read:41content/2covers plus8expanded/2QAcrops. Direct boundaries volume5end30/volume6start31end48/volume7start49end66. '
 'All67pages viewed by recorded scope;12first-passsectionspans/8neworcompleted/0entireunitsapplied.20boundedclauses and private rawxunexit reference. '
 '10checks/64actualHHCfigurecalls/180actualLunarcallson62distinctnoondates,46080privatecontexts/7680rawvoids. '
 'No functionalvoid/timing/prediction promotion;consumer/10priorreferencesunchanged.0HTTP/newPDF.')
if entry not in yi['completed']:yi['completed'].append(entry)
yi['latestScope']='../liuyao-b03-book3/BOOK3_CURRENT_UNITS.json'
yi['remaining']=[x for x in yi['remaining']if not x.startswith('LiuYaoB03:book1full384annotations/')]
yi['remaining'].append('LiuYaoB03:books2/3first-passpagescoveredbutallclausesnotapplied;book1full384annotations/prefaces/strength/triadcompletionopen. Fulltiming/functionalvoid/horizons/rolechoice/sourcequotationcollation and books4..6remain. B02PDF52and103heading-onlyunitsopen.')
write(p,d)
p=root/'research/library-current/COVERAGE.json';d=read(p);b=next(x for x in d['catalogue']if x['id']=='B03')
b['scope']='Giữ byte sách đóng1/2/3. Sách2 đủ49trang vàsách3 đủ67trang xem theo phạmvi; sách3 quyển5/6/7 có12khoảngmục đọc lầnđầu. Bộ riêng thêm tọađộ raw tuầnkhông/ratuần. Chưaápdụngmọimệnhđề/384chúhào/tiềntự/tổngvượngsuy/hiệulực hoặc sách4–6.'
b['localPossession'][2]='Sách đóng3: PDF67trang/56939817byte/SHA01859340e519ffb68a1f40996af73aa7f40beb10a723a7a2a070985201874c61; APIrevision1004714434/TLS/size/SHA1/SHA256. Đãxem67trangtheophạmvi:65nộidung/2bìa. Khôngđồngnghĩaápdụnghếtnộidung; cùngbộ6sách,khôngnhânchứngđộclập.'
b['latestLocalReadingScope']='43ảnhmới (41nộidung/2bìa),8đọcmởrộng/2cropQA;đủ12khoảngmụcquyển5–7,8mớikhépkhoảng.20mệnhđề/10kiểm/64HHCthật+180lunar trên62ngày,46080ngữcảnhriêng/7680rawkhông.0HTTP/PDFmới;khôngdựbáo.'
for f in ['v53/'+report]+['v53/research/liuyao-b03-book3/'+n for n in ['SOURCE_AUDIT.json','MANUAL_READINGS.json','BOOK3_CURRENT_UNITS.json','XUN_EXIT_CLAUSE.json','OPERATIONAL_CLAUSES.json','xun-exit-reference.mjs']]+['v53/qa/liuyao-b03-book3/ENGINE_RESULTS.json']:
 if f not in b['currentEvidence']:b['currentEvidence'].append(f)
d['latestFollowup']=report+':B03book3all67pagesviewedwithscope/12sectionspansfirstpass,notallclauses;rawxunexit/10checks64HHC180Lunar.0HTTP/PDF,consumerunchanged/wholework0.'
d['latestAcquisitionCounts']={'scope':report,'newOriginalPDFs':0,'newHTTPBodies':0,'newLocalRenders':43,
 'newContentPages':41,'newCoverPages':2,'expandedEarlierContentPages':8,'QAOnlyRenders':2,
 'manualRecords':51,'totalBook3PagesViewedByScope':67,'firstPassRelevantSpanUnits':12,'newOrCompletedSpanUnits':8,'fullBooksApplied':0}
d['counts']['newDownloadsThisScope']=0;assert d['counts']['wholeWorkApplied']==0;write(p,d)
note='Mốc B03–Sách3 27/10/2026: `'+report+'`. '+step+'\n\n'
for p in [w/'PROJECT_RESEARCH_STATE.md',root/'NEXT_STEPS.md',root/'research/library-current/COVERAGE.md']:
 text=p.read_text(encoding='utf-8-sig')
 if text.startswith('Mốc B03–Sách3 27/10/2026:'):text=text.split('\n\n',1)[1]
 p.write_text(note+text,encoding='utf-8')
p=w/'PENDING_RESEARCH_STATE.json';pending=read(p)
pending.update(status='book3-first-pass-pages-complete-current-scope-active',workDirectory='v53/research/liuyao-b03-book3',
 currentResearchScope='v53/research/liuyao-b03-book3',currentWorkState='v53/research/liuyao-b03-book3/WORK_STATE.json',
 latestReport='v53/'+report,manualReadings='v53/research/liuyao-b03-book3/MANUAL_READINGS.json',
 checks='v53/qa/liuyao-b03-book3/ENGINE_RESULTS.json',manualPages=list(range(1,68)),next=nexts,
 all67PagesViewedByRecordedScope=True,partialSection=None)
write(p,pending)

text=f'''# B03: khép lượt đọc sách đóng thứ ba và tọa độ ra tuần

Ngày 27/10/2026. Hồ sơ nghiên cứu nội bộ; không thêm nguồn hoặc bảng kiểm vào site người dùng.

## Phạm vi và nhận dạng

Tái sử dụng PDF sách đóng thứ ba đã giữ byte ở phạm vi trước: **56.939.817 byte / 67 trang**, SHA-256 `01859340e519ffb68a1f40996af73aa7f40beb10a723a7a2a070985201874c61`. Không có HTTP hoặc PDF gốc mới. API revision 1004714434, TLS và đối chiếu size/SHA-1/SHA-256 được giữ nguyên ở `research/liuyao-b03-volume5/`. Cùng bộ sáu sách không được tính thành nhân chứng độc lập. Niên đại theo siêu dữ liệu không là bằng chứng ấn ký mới được đọc trực tiếp.

Đã xem 43 trang còn lại: nội dung26–66 và bìa1/67. Đọc mở rộng tám trang đã có (8 và19–25); hai crop QA360dpi ở8 và38 không cộng thành trang nguồn. Toàn sách3 hiện có65trang nội dung đã đọc lần đầu theo khoảng liên quan và hai bìa đã xem. Không OCR hoặc chép ngoại giao toàn trang; đọc hết khoảng không đồng nghĩa mọi mệnh đề đã áp dụng.

Các ranh trực tiếp: quyển5 kết ở30; quyển6 mở31, kết48; quyển7 mở49, kết66. `BOOK3_CURRENT_UNITS.json` ghi12mục: 天時,年時,國朝,征戰,身命; 婚姻,產育,進人口; 病症,病體,醫藥,鬼神. Bốn khoảng đầu kế thừa; lần này khép 身命19–30 và đọc bảy khoảng sau. Trang ranh trùng không cộng thêm trang độc nhất. **0mục được đánh dấu đã áp dụng toàn bộ**.

## Nội dung khai thác

20mệnh đề có giới hạn được ghi vào `OPERATIONAL_CLAUSES.json`. Nguồn phân chủ Dụng theo người hỏi và người được hỏi: cùng hôn nhân, sinh nở hay bệnh tật cũng có nhiều đối tượng. Đối ảnh phóng toPDF38 xác nhận câu kết nói cả nam hỏi nữ và nữ hỏi nam (`男卜女婚女卜男婚`), rồi yêu cầu phân biệt các quan hệ khác; không giới hạn sai thành chỉ nam hỏi. Bản nháp nghiên cứu trước đóng gói cuối đã được sửa theo ảnh, không thay nguồn hoặc đưa ra đồng thuận cho mọi loại quan hệ. Chưa hợp nhất thành quy tắc giới tính cố định cho tất cả người dùng.

Các phân loại bệnh chứng, thuốc, sinh tử, thai/con và nghi lễ giữ như văn bản lịch sử, không dùng để chẩn đoán, lựa chọn thuốc hoặc tiên lượng. Các câu yêu cầu thành tâm/cầu khấn trong nguồn là dữ liệu nguồn, không phải lệnh người dùng. Những đoạn trích sách khác và quan hệ với lời phê ở quyển3 chưa được tự động coi là đồng thuận hay đã hiệu khảo xong.

## Chức năng riêng mới

`xun-exit-reference.mjs` bổ sung **tọa độ raw tuần không và ranh ra tuần hiện hành** của hào gốc đã chỉ định. NguồnPDF8 có câu `如旬空候出旬之日應事` và tóm lược `空出旬`. Câu giới hạn này không kèm tiền đề động/tĩnh; không tự thêm một điều kiện chưa được in vào câu.

Đầu vào là sáu giá trị6/7/8/9, hào Dụng đã chọn, ngữ cảnh đoạn ứng kỳ 天時 được xác nhận và ngày canchi hợp lệ nếu có. Không tự chọn Dụng hoặc chuyển thời điểm Gregory. Thiếu ngày giữ chưa rõ; chi không nằm raw tuần không không được phát ranh ra tuần theo phương pháp này. Hào biến không thay chi gốc. Công thức `10-vịtrítrongtuần` là chuẩn hóa tọa độ của chu kỳ, được ghi rõ là suy ra, không giả làm công thức số được in trong sách.

Kết quả gồm đoạn tọa độ từ ngày đầu vào đến cuối tuần đang xét và tọa độ đầu tiên ngoài tuần. Đây **không là ngày ứng nghiệm**, không kết luận chân không/hiệu lực. Các điều kiện vượng suy, nguyệt phá, sinh cứu, gần/xa và ưu tiên giữa những câu ứng kỳ còn mở; chức năng không xuất dự báo thời tiết, y tế, hôn nhân hoặc tuổi thọ.

## Kiểm chứng

Đạt **10kiểm**. 64lời gọi HHC thật kiểm danh tính64quẻ. Thực thi lunar-typescript1.8.6 có byte runtime đã ghim: 180lời gọi gồm60mốc canchi và120điểm cuối-trong/đầu-ngoài tuần, trên **62ngày trưa độc nhất**. Việc thử bằng giờ trưa là quy ước bài kiểm, không suy ra múi giờ cổ bản. Các mốc cuối-trong vẫn thuộc tuần cũ; đầu-ngoài thuộc tuần kế và khởi bằngGiáp.

46080ngữ cảnh riêng (60ngày×64quẻ×6hào×hai trạng thái động/tĩnh cho hào đang xét) so với các dãy Nạp Giáp literal riêng và kết quả lunar thực. 7680ngữ cảnh có raw tuần không; độ lệch1–10ngày, mỗi loại768ngữ cảnh. Đây không phải46080lời gọi HHC mới hoặc tỷ lệ tiên đoán đúng. Digest `{s['graphDigest']}`.

Ca dựng: chiDần hào2 củaCàn tạiGiápThìn ra khỏi tuần sau10tọa độ ngày; tạiQuýSửu sau1tọa độ tớiGiápDần. Khi hào2động đổi thànhSửu, việc Sửu không nằm raw tuần không hiện tại không làm mất cờ củaDần gốc. Giữ nguyên tham chiếu bốn phương pháp thời điểm trước đó, không ghi đè lịch sử của nó.

## Bảo toàn phát hành và phần mở

HTML707411byte/SHA`549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`, site, ZIPweb và10tham chiếu trước giữbyte. Snapshot trước ở `archives/v53-before-liuyao-b03-book3/` có sourceZIP1299612174byte/2381tệp manifest. Gói nguồn đồng bộ nghiên cứu riêng, kiểm byte toàn manifest/ZIP; không đưa corpus vào site hoặc xuất bản mạng.

Sách đóng4–6chưa tải; sách1còn384chúhào/tiềntự và mọi mệnhđề của sách2/3 chưa hoàn tất. Chưa có tổng vượng suy, chân không, tự chọn Dụng hoặc ứng kỳ đầy đủ. B02vẫn136đơn vị/103thân mục mức đềmục/26khoảng đọc lần đầu; mâu thuẫn ngày–tuầnkhông PDF52 chưa giải quyết. Toàn kho40tài liệu và bốn mục lớn tiếp tục active, không đánh dấu khai thác hết.
'''
(root/report).write_text(text,encoding='utf-8')
print('Book3 page coverage and raw-xun coordinates recorded; all-library work remains active.')
