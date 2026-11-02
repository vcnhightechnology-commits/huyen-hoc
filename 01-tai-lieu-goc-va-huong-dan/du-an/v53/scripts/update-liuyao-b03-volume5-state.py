from pathlib import Path
import json
root=Path(__file__).resolve().parent.parent;w=root.parent;base=root/'research/liuyao-b03-volume5'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='LIUYAO_B03_VOLUME5_REPORT.md';e=read(root/'qa/liuyao-b03-volume5/ENGINE_RESULTS.json');s=e['summary'];a=read(base/'ACQUISITION.json')
assert len(e['checks'])==9 and all(x['ok'] for x in e['checks'])
step=('Sách đóng3 B03 đã giữ byte56.939.817/SHA01859340…/67trang, APIrevision1004714434 +PDF/2body200TLS từ staging, không tải lại. '
 'Đọc24trang2–25: bốn khoảng 天時/年時/國朝/征戰 đọc lần đầu toàn khoảng, 身命 mới19–25. '
 '24ảnh nội dung vào gói (7kế thừa pending,17mới nhịp này),1cropQA300dpi ở8 không tính trang nguồn mới. '
 'Thêm14mệnh đề có giới hạn và bốn phương pháp tọa độ thời điểm trong đoạn 天時7–8. '
 'Tách nhập mộ ngữ cảnh chờ xung chi mộ với tự hóa nhập mộ chờ xung chi Dụng; tiền đề do người nghiên cứu xác nhận, không đoán từ thiếu dữ liệu. '
 '9kiểm/20HHCthật chỉ số quẻ;2880ngữ cảnh riêng/14400tọa độ lục thập, không phải ngày dự báo hoặc ứng nghiệm. '
 'Chưa cả quyển5/sách3, vượng suy/chân không/ứng kỳ đầy đủ; nguồn thiên tai, quốc triều, chiến trận, thọ yểu giữ lịch sử. '
 'HTML707411byte/site/ZIPweb và chín tham chiếu trước giữ nguyên. B02vẫn136/103/26, ngày52 mở; toàn kho chưa hoàn tất.')
nexts=[
 'Continue B03book3 PDF26..67 and cover1. 身命 starts19 but has only19..25 first-pass; locate its ending and later textual-volume headings directly.',
 'Compile remaining timing premises from7..8: dynamic/static void within/out-of-xun, month-break, rescue, appearing hidden/original spirit, near/far horizons and weather-specific 財/父/轉爻. Four coordinate methods are not a full timing adjudicator.',
 'Reconcile volume3 critiques with later 易林補遺 quotations without treating them as author endorsement or consensus. Keep 世/身/卦身 and domain roles separate.',
 'B03books4..6 unacquired; B02still103heading-only/PDF52date-void conflict. Earlier full strength/triad completion and MaiHoa/Bazi/Tuvi/Home/library gaps remain.'
]
write(base/'WORK_STATE.json',{'date':'2026-10-27','status':'private-four-method-timing-coordinate-complete-book3-rest-active',
 'sourceID':'B03-book3','latestReport':'v53/'+report,'privateReference':'timing-reference.mjs','unitMap':'VOLUME5_UNITS.json',
 'completedStep':step,'manualPages':list(range(2,26)),'unviewedPages':[1]+list(range(26,68)),
 'firstPassCompleteRelevantSpanUnits':4,'partialSpanUnits':1,'allVolume5ClausesApplied':False,
 'newOriginalPDFsToRelease':1,'retainedHTTPBodiesNewToRelease':2,'newHTTPBodiesThisHeartbeat':0,
 'contentImagesNewToRelease':24,'inheritedPendingImages':7,'newContentRendersThisHeartbeat':17,'QAOnlyRenders':1,
 'sourceTimingMethods':4,'sourceTimingDomain':'weather-timing-paragraph','calendarInstantAdapter':False,
 'fullTimingAdjudicator':False,'meteorologicalAccuracyValidated':False,'consumerChanged':False,
 'next':nexts,'wholeBookApplied':False,'wholeCatalogueCompleted':False})
d=read(w/'EXHAUSTIVE_WORK_STATE.json')
d['currentWork'].update(currentStep=step,latestResearchReport='v53/'+report,
 sourceDirectory='v53/research/liuyao-b03-volume5',internalB03TimingReference='v53/research/liuyao-b03-volume5/timing-reference.mjs',
 currentB03Volume5UnitMap='v53/research/liuyao-b03-volume5/VOLUME5_UNITS.json',
 functionalBacklog='v53/research/liuyao-b03-volume5/WORK_STATE.json')
d['currentWork']['sourceLimits']='B03physicalbooks1/2/3retained, not all6/14textualvolumes. Book2 all49pages viewed by recorded scope, not all clauses applied. Book3 onlyPDF2..25read; four section spans complete first-pass/身命partial. Four timing targets require caller-asserted source premises; no Gregorian dates/outcome, strength or full timing model. B02PDF52date-void and independent pedigree remain open.'
d['currentWork']['nextSourceLead']={'status':'downloaded-byte-verified-partial-volume5-read','sourceID':'B03-book3',
 'file':'v53/research/liuyao-b03-volume5/'+a['file'],'sha256':a['sha256'],'bytes':a['bytes'],'sourceURL':a['commonsURL'],
 'remaining':'Book3PDF26..67 and cover1 not viewed. Physicalbooks4..6notacquired; earlier clause/efficacy questions remain.'}
d['inProgressScope']='v53/research/liuyao-b03-volume5/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in [w/'EXHAUSTIVE_WORK_STATE.json',root/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=root/'research/full-study/WORK_STATE.json';d=read(p);d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts)
yi=next(x for x in d['items'] if x['id']=='yi')
entry=('B03book3 acquired earlier in pending and now promoted without redownload:56939817bytes/67pages/SHA01859340../APIrevision1004714434. '
 '24contentpages2..25first-pass:天時/年時/國朝/征戰complete relevant spans,身命partial.24new-to-releaseimages/1QA crop,14boundedclauses. '
 'Private4timingmethods distinguish contextual tomb clash from own-transformed-tomb subject clash;9checks/20actualHHCfigure calls/2880privatecontexts14400cyclecoordinates. '
 'No forecast/complete source efficacy;consumer/nine prior references unchanged.')
if entry not in yi['completed']:yi['completed'].append(entry)
yi['latestScope']='../liuyao-b03-volume5/TIMING_CLAUSES.json'
yi['remaining']=[x for x in yi['remaining'] if not x.startswith('LiuYaoB03:book1full384annotations/')]
yi['remaining'].append('LiuYaoB03:book1full384annotations/prefaces/allbook2clauses and strength/triad efficacy still open. Book3only2..25read;身命19..25partial,26..67/cover1unread. Fulltiming/void/horizons/rolechoice and books4..6remain. B02PDF52and103heading-onlyunitsopen.')
write(p,d)
p=root/'research/library-current/COVERAGE.json';d=read(p);b=next(x for x in d['catalogue'] if x['id']=='B03')
b['scope']='Giữ byte sách đóng1/2/3. Sách2 đủ49trang xem theo phạmvi nhưng chưaápdụnghết. Sách3/67trang mới2–25: bốn khoảng 天時/年時/國朝/征戰 đọc lầnđầu, 身命 một phần. Bộ riêng4tọađộứngkỳ/phânbiệtmộvàtựhóamộ, khônghiệulực/dựbáo. Cácsách4–6vàmọimệnhđềcònmở.'
book3='Sách đóng3: PDF67trang/56939817byte/SHA'+a['sha256']+';APIrevision1004714434/TLS/size/SHA1/SHA256. Chỉ PDF2–25đãxem,1/26–67cònmở. Cùngbộ6sách,khôngtínhlànhânchứngđộclập.'
if len(b['localPossession'])==2:b['localPossession'].append(book3)
else:b['localPossession'][2]=book3
b['latestLocalReadingScope']='Sách3 PDF2–25/24trangnộidung,4khoảngđọclầnđầuvà1phần;7ảnhpending+17mới/1cropQA.14mệnhđề/4phươngphápứngkỳcógiới hạn,9kiểm/20HHCthật/2880ngữcảnhriêng. Nguồn2bodytừnhịptrước,0HTTPnhịpnày;khôngdựbáo.'
for f in ['v53/'+report]+['v53/research/liuyao-b03-volume5/'+n for n in ['ACQUISITION.json','REQUESTS.json','SOURCE_AUDIT.json','PDF_CONTAINER_CHECKS.json','MANUAL_READINGS.json','VOLUME5_UNITS.json','TIMING_CLAUSES.json','OPERATIONAL_CLAUSES.json','timing-reference.mjs']]+['v53/qa/liuyao-b03-volume5/ENGINE_RESULTS.json']:
 if f not in b['currentEvidence']:b['currentEvidence'].append(f)
d['latestFollowup']=report+':B03book3raw67pages/2..25read;4fullfirst-passsectionspans/1partial,4timingcoordinates/9checks. Stagedrawpromotedwithoutredownload,consumerunchanged/wholework0.'
d['latestAcquisitionCounts']={'scope':report,'originalPDFsNewToRelease':1,'retainedHTTPBodiesNewToRelease':2,'newHTTPBodiesThisHeartbeat':0,
 'contentImagesNewToRelease':24,'inheritedPendingContentImages':7,'newContentRendersThisHeartbeat':17,'QAOnlyRenders':1,
 'manualImageRecords':24,'firstPassCompleteRelevantSpanUnits':4,'partialSpanUnits':1,'fullBooksApplied':0}
d['counts']['newDownloadsThisScope']=2;assert d['counts']['wholeWorkApplied']==0;write(p,d)
note='Mốc B03–Luận5 27/10/2026: `'+report+'`. '+step+'\n\n'
for p in [w/'PROJECT_RESEARCH_STATE.md',root/'NEXT_STEPS.md',root/'research/library-current/COVERAGE.md']:
 text=p.read_text(encoding='utf-8-sig')
 if text.startswith('Công việc đang triển khai sau bản B03–Luận4:'):text=text.split('\n\n',1)[1]
 if text.startswith('Mốc B03–Luận5 27/10/2026:'):text=text.split('\n\n',1)[1]
 p.write_text(note+text,encoding='utf-8')
p=w/'PENDING_RESEARCH_STATE.json';pending=read(p)
pending.update(status='promoted-into-current-research-scope',currentResearchScope='v53/research/liuyao-b03-volume5',
 currentWorkState='v53/research/liuyao-b03-volume5/WORK_STATE.json',latestReport='v53/'+report,
 manualPages=list(range(2,26)),next=nexts)
write(p,pending)

text=f'''# B03: quyển năm, bốn khoảng đầu và tọa độ ứng kỳ

Ngày 27/10/2026. Nghiên cứu nội bộ, không thêm nội dung kiểm định lên site.

## Nguồn và phạm vi

Đưa nguồn staging đã tải trước vào gói, không tải lại. Sách đóng3: **56.939.817byte,67trang**, SHA-256`{a['sha256']}`, SHA-1`{a['sha1']}`. APIrevision1004714434 vàPDF là hai body200/TLS đã lưu; API size/SHA1 và byte SHA256 khớp. Nhịp này0HTTP. Đây là cùng bộ sách6cuốn, chưa phải nhân chứng độc lập hay chứng cứ mới trực tiếp cho niên đạiấn bản1904. PDFkhông có lớp văn bản; khôngOCR.

Đã xem24trang2–25, gồm7ảnh từ côngviệc pending trước và17ảnh mới. Một cropQA300dpi ởPDF8 giúp đọc đúng đoạn ứng kỳ, không cộng thành trang nguồn mới. Tiêu đềPDF2 là `卜筮正宗卷之五`/`天時`. Bốn khoảng đã đọc lầnđầu toàn khoảng: 天時2–8,年時8–13,國朝13–16,征戰16–19. 身命 mới19–25, chưa biết cuối khoảng. Các trang ranh trùng nhau không cộng thêm trang độc nhất. Bìa1 và26–67chưa xem; chưa hoàn tất quyển5 hoặc sách3.

14mệnh đề có giới hạn được ghi riêng. Các câu về thời tiết, thiên tai, quốc triều, chiến trận, thọ yểu, quan hệ hay số con là văn bản lịch sử và phép lấy tượng của nguồn; chưa kiểm chứng khả năng dự báo sự kiện. PDF22 trích 易林補遺 về chính/hỗ/biến và thời hạn; quyển3 có lời phê khác. Giữ riêng tầng trích dẫn/tác giả/bình luận, chưa coi đã hòa giải hoặc đồng thuận. Tài liệu nguồn không phải lệnh yêu cầu người dùng hành động.

## Chức năng tham chiếu riêng

`timing-reference.mjs` chỉ nhận sáu hào và hào Dụng đã được chỉ định. Nó không tự chọn Dụng thần. Phải chỉ rõ ngữ cảnh đoạn ứng kỳ 天時 và một trong bốn phương pháp đã giới hạn: động không có nguyên nhân khác chờ hợp; tĩnh bị hợp chờ xung; vào mộ ngữ cảnh chờ xung chi mộ; tựhóa nhập mộ chờ xung chi gốc Dụng.

Các tiền đề hợp/mộ/không nguyên nhân khác là khẳng định có chủ ý từ người nghiên cứu, **chưa được mô hình này tự xác minh**. Thiếu tiền đề giữ trạng thái chưa rõ; sai động/tĩnh hoặc chi tựbiến không khớp chi mộ được chỉđịnh thì không thỏa phương pháp. Hai loại nhập mộ không bị gộp thành cùng một chi chờ. Tọa độ được chuẩn hóa từ đoạn nguồn và bảngxung/hợp đã có, không là mô hình đầyđủ hiệu lực ứngkỳ.

Nếu cung cấp mốc canchi hợp lệ, kết quả liệt kê các vị trí tương ứng trong60tọađộ ngày, bắtđầu bằng mốc được cungcấp. Không có chuyển đổi thờiđiểm lịchGregory, không ngày dựbáo, không dựbáo khí tượng; không mặcđịnh mởrộng sang thânmệnh, bát tự, tử vi hoặc mọi loại câu hỏi. Các quy tắc旬內/出旬, nguyệtphá, vượngsuy, Nguyên/Phụcthần, gần/xa và chuyểnhào cònmở.

## Kiểm chứng

Đạt9kiểm. **20lời gọi HHC thật chỉ kiểm số quẻ**: bốn ca dựng để kiểm bốn phươngpháp, mỗi ca bản/biến, và12đại diện chi. Các ca này không phải láquẻ có niênngày/đồngtiền in sẵn trong sách, và không kiểm chứng ứngnghiệm.

Ca dựng Càn1→ĐạiSúc26, hào4 Ngọhỏa→Tuất: mộ trongngữcảnh chờThìn, tựhóa mộ chờTý. Tại mốcGiápTuất, hai tọađộ đầu là6và2ngày. Tọađộ mộHỏaTuất còn được đối cùng thamchiếu B03 trước; không áp quyước Thổ của nguồnB02 sangnguồnB03.

2880ngữcảnh riêng (60mốc×12chi×4phươngpháp) và14400vịtrí so với phép toán chi và chu kỳ độc lập. Chúng không phải2880lời gọiHHC mới hoặc14400ngày dựbáo. Digest`{s['graphDigest']}`. Kiểm thêm thiếu/sai tiềnđề, ngữcảnh sai miền, ngàykhônghợplệ, kiểu dữliệu và bảo toàn nguồn trước.

HTML707411byte/SHA`549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`,site/ZIPweb/chín thamchiếucũ giữbyte. Bảntrước bảo tồn ở `archives/v53-before-liuyao-b03-volume5/` (sourceZIP1191709090byte/2333tệp manifest). Nguồn và kiểmthử giữngoài site; gói nguồn được đồngbộ và so toànmanifest/ZIP.

## Tiếp tục

Đọc26–67/bìa1, địnhvị cuối 身命/các quyển sau; biên dịch đầyđủ điều kiện ứngkỳ, nguồn trích và khác biệt truyền bản. Sáchđóng4–6chưa tải. Các câu/tiềnđề quyển3/4,384chúhào sách1, vượngsuy/hiệulực, B02PDF52 và103thânmục mức đềmục cùng toànkho40tài liệu vẫn mở. Không đánh dấu cả bốn mục hay toàn kho hoàn tất.
'''
(root/report).write_text(text,encoding='utf-8')
print('Promoted staged source and four bounded timing methods; whole catalogue remains active.')
