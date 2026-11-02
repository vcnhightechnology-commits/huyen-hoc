from pathlib import Path
import json
root=Path(__file__).resolve().parent.parent;w=root.parent;base=root/'research/liuyao-b03-line-labels'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='LIUYAO_B03_LINE_LABELS_REPORT.md';e=read(root/'qa/liuyao-b03-line-labels/ENGINE_RESULTS.json')
assert len(e['checks'])==8 and all(c['ok']for c in e['checks'])
step=('B03 sách1/quyển2: chép ảnh riêng64hình/384dòng canchi–Lụcthân/128vịtrí ThếỨng/56tọađộ Phụcthần. '
 '26trang34–59 mởrộng,2renderQA/2crop;6hình có cột nhãn kéo qua trang. '
 'Sách6 thêm3trang/3renderQA4crop cho bốn quẻin câu3. '
 '8kiểm đạt,72HHC thật (64danh tính+8cho4quẻin câu3),4lunar thật;384dòng và56Phục khớp bộthamchiếuriêng,320truyvấn vai trò tườngminh. '
 'Không lấy申金quái thân ở隨 làmPhục; không nhận đã đối hết nét âm-dương/quái thân hoặc mọi câu luậnđoán. '
 'KhôngHTTP/PDFgốc mới;HTML707411byte/site/ZIPweb và15thamchiếu trước nguyênbyte. '
 'Câu3 có4quẻin quan sát/đối cấu trúc, cộng2quẻ cũ là6; mục lục131vídụ chưađếm toànthân sách. '
 '384nhãn gốc đãđối không cónghĩa mọi384chú/câu/quẻbiến hoặc kho40nguồn đãxong.')
nexts=[
 'Book1volume2nowhas64manuallyreadfigures/384primaryheavenlystem-branchandkinrows/128shi-yingmarkers/56hiddenkincoordinatesverified. Do not repeat this matrix. All384diagram polaritymarks/gua-shenlabels/proseclauses/changed annotationsstillnotfullycollated;heading筮/噬 remains separate.',
 'Book6TOC131examplesnotindependentbodydiagramcount. Sixactualprintedcaststructureschecked(twoearlier+fourquestion3),notallannotations. Question3fourobserveddiagramsagreeitsTOCcount4;continueotherquestions/sourcecast/day/premises. Source-outcomesnotvalidated,fullcalendar datesnotreconstructed.',
 'Source-specific strength/functionalvoid/triadcompletion/timing/supportefficacy/gua-shencontext andindependentwitnessesremain. Book5boatwording/book6ending/openB02PDF52date-voidconflict/103heading-onlybodiesremain.',
 'Continue remainingMaiHoa/Bazi/Tuvi/Homeconditionsand40-sourcecatalogue. Neither all60book1imagesviewed nor384primarylabelscollated means wholebook/full14volumes/catalogueapplied.'
]
write(base/'WORK_STATE.json',{'date':'2026-10-27','status':'64-printed-figure-primary-label-fixtures-complete-full-clauses-active',
 'sourceID':'B03-book1-volume2','latestReport':'v53/'+report,'completedStep':step,'sourceFixtures':'PRINTED_LINE_ROWS.json',
 'all384PrimaryStemBranchKinRowsCollated':True,'all128ShiYingPositionsCollated':True,'all56PrintedHiddenKinCoordinatesCollated':True,
 'all384AnnotationsCollated':False,'allDiagramPolarityMarksDiplomaticallyCollated':False,'allGuaShenLabelsCollated':False,
 'allSourceClausesApplied':False,'question3PrintedCastFixtureCount':4,'cumulativeBook6PrintedCastFixtureCount':6,
 'all131Book6ExamplesIndependentlyCounted':False,'summary':e['summary'],'consumerChanged':False,'next':nexts,'wholeBookApplied':False,'wholeCatalogueCompleted':False})
d=read(w/'EXHAUSTIVE_WORK_STATE.json');d['currentWork'].update(currentStep=step,latestResearchReport='v53/'+report,
 sourceDirectory='v53/research/liuyao-b03-line-labels',currentB03PrintedLineFixtures='v53/research/liuyao-b03-line-labels/PRINTED_LINE_ROWS.json',
 functionalBacklog='v53/research/liuyao-b03-line-labels/WORK_STATE.json')
d['currentWork']['sourceLimits']='B03book1all384primaryganZhi/kinlabels+128roles+56hiddenverified,notallpolarity/gua-shen/prose/changedlineannotations. Sixsplit-columnchartsidentified. TOC131examplesnotwholebodycount;sixbook6printedcastscheckedincludingallfourquestion3structures. Source-specificstrength/functionalvoid/timing/genealogy/independentwitnesses/boatwording/finalending/B02PDF52and40-sourcegapsremain.'
d['currentWork']['nextSourceLead']={'status':'book1-primary-line-label-fixtures-complete-full-annotation-fields-and-book6-casts-open',
 'sourceID':'B03','file':'v53/research/liuyao-b03-line-labels/PRINTED_LINE_ROWS.json',
 'remaining':'Book1polarity/gua-shen/allprose,book6actualbodyexamplesandexplicitconditions,independentwitnesses/othercataloguegaps.'}
d['inProgressScope']='v53/research/liuyao-b03-line-labels/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in[w/'EXHAUSTIVE_WORK_STATE.json',root/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=root/'research/full-study/WORK_STATE.json';d=read(p);d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts)
yi=next(x for x in d['items']if x['id']=='yi');entry=('B03book1volume2:64sourcefigures/384primaryganZhi-kinrows/128roles/56hidden verified,8checks72actualHHC(64identity+8for4question3casts)/4Lunar/320privateavailabilityqueries. '
 'Sixsplitcolumns/2QA. Noallpolarity/gua-shen/proseclaim;consumer/15priorreferencesunchanged.')
yi['completed']=[x for x in yi['completed']if not x.startswith('B03book1volume2:64sourcefigures/')]
if entry not in yi['completed']:yi['completed'].append(entry)
yi['latestScope']='../liuyao-b03-line-labels/PRINTED_LINE_ROWS.json'
yi['remaining']=[x for x in yi['remaining']if not x.startswith('LiuYaoB03:all6same-seriesPDFsretained/book1all60physicalimagesboundedviewed;')]
yi['remaining']=[x for x in yi['remaining']if not x.startswith('LiuYaoB03:384primarylabels/128roles/56hiddenverified;')]
yi['remaining'].append('LiuYaoB03:384primarylabels/128roles/56hiddenverified;fullpolarity/gua-shen/prose/changedannotationsnotcomplete. Sixbook6casts(4question3)checked;othercasts/strength/void/timing/clockboundaries/genealogy/boatwording/endingremain. B02PDF52and103heading-onlyunitsopen.')
write(p,d)
p=root/'research/library-current/COVERAGE.json';d=read(p);b=next(x for x in d['catalogue']if x['id']=='B03')
b['scope']='Giữ6PDFcùngbộ/khôngnhânchứngđộc lập. Sách1:toàn60ảnh xem cógiới hạn;64hình đối384dòng canchi–Lụcthân/128dấu ThếỨng/56Phụcthần, chưa toànnét âm-dương/quái thân/chúgiải/quẻbiến. 60Nạpâm/120cantháng/120cangiờ đãđối thật. 131vídụ do mụclục ghi;thân sách6 có6quẻđối cấu trúc(4câu3), chưa toànbộ. Chưa áp hết14quyển/mọi mệnhđề.'
b['latestLocalReadingScope']='26trang sách1+3trang sách6 mởrộng/5renderQA6crop;64hình/384dòng/128dấu/56Phục+4quẻin câu3.8kiểm72HHCthật/4lunar/320truyvấn riêng;6hình qua trang. KhôngHTTP/PDFgốc mới;chưaquái thân/toàncâu.'
for f in ['v53/'+report]+['v53/research/liuyao-b03-line-labels/'+n for n in ['SOURCE_AUDIT.json','MANUAL_READINGS.json','PRINTED_LINE_ROWS.json','BOOK6_QUESTION3_FIXTURES.json']]+['v53/qa/liuyao-b03-line-labels/ENGINE_RESULTS.json']:
 if f not in b['currentEvidence']:b['currentEvidence'].append(f)
d['latestFollowup']=report+':64printedfigures/384primarylabels128roles56hiddenverified;4question3castsadded/6cumulativebook6.8checks72HHC4Lunar320privatequeries. Fullclauses/polarity/gua-shen/othercastsopen;wholework0/consumerunchanged.'
d['latestAcquisitionCounts']={'scope':report,'newOriginalPDFsToRelease':0,'retainedHTTPBodiesNewToRelease':0,'newHTTPBodiesThisRun':0,
 'expandedBook1SourcePages':26,'expandedBook6SourcePages':3,'QAOnlySourceRenders':5,'QACrops':6,'printedFigures':64,
 'primaryLineLabelRows':384,'shiYingMarkers':128,'hiddenKinCoordinates':56,'newBook6PrintedCastFixtures':4,'cumulativeBook6PrintedCastFixtures':6,'fullBooksApplied':0}
d['counts']['newDownloadsThisScope']=0;d['counts']['newDownloadsThisScopeBasis']='Existing rawPDF/images reused;five QA renders only,zero new HTTP/originalPDF.'
assert d['counts']['wholeWorkApplied']==0;write(p,d)
note='Mốc B03–Nhãn hào, 27/10/2026: `'+report+'`. '+step+'\n\n'
for p in[w/'PROJECT_RESEARCH_STATE.md',root/'NEXT_STEPS.md',root/'research/library-current/COVERAGE.md']:
 t=p.read_text(encoding='utf-8-sig')
 if t.startswith('Mốc B03–Nhãn hào, 27/10/2026:'):t=t.split('\n\n',1)[1]
 p.write_text(note+t,encoding='utf-8')
write(w/'PENDING_RESEARCH_STATE.json',{'date':'2026-10-27','status':'book1-primary-line-label-fixtures-current-scope-active','sourceID':'B03-book1-volume2',
 'workDirectory':'v53/research/liuyao-b03-line-labels','currentWorkState':'v53/research/liuyao-b03-line-labels/WORK_STATE.json',
 'latestReport':'v53/'+report,'checks':'v53/qa/liuyao-b03-line-labels/ENGINE_RESULTS.json','next':nexts,
 'consumerChanged':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False})
(root/report).write_text('''# B03: đối đủ nhãn hào trong 64 hình tám cung

Ngày27/10/2026. Dữ liệu ảnh và bộ đối chiếu nằm ngoài site.

## Nguồn và bản đọc

Tái dùng sách đóng1 B03: **50.191.031byte/60trang**, SHA256 `5dcd7b5005b1e86f441a9350eefb7c0e9e628c47ab926b2a7d1bdd6691a4773d`. Không HTTP/PDF gốc mới hoặc nhân chứng khác. Cả26ảnh PDF34–59 được đọc mở rộng cho cột nhãn; không cộng26trang nguồn mới. Hai renderQA360dpi/2crop ở46/49 kiểm vị trí chú nhỏ và cột qua trang, giữ SHA.

`PRINTED_LINE_ROWS.json` chép thủ công theo ảnh: **64hình,384dòng can chi–Lục thân,128vị trí Thế/Ứng và56tọa độ Phục thần**. Chuỗi theo thứ tự ảnh trên xuống ứng với hào6→1. Nhãn 父/兄/官/財/子 là viết tắt biên tập cho 父母/兄弟/官鬼/妻財/子孫; không gọi là chép ngoại giao mọi chữ. Dòng nguồn không sinh bằng kết quả engine. Không sửa nhãn nguồn để làm khớp máy.

Sáu hình có cột qua trang:隨17ở46–47,蠱18ở49–50,蒙4ở51–52,大壯34ở54–55,萃45ở56–57,歸妹54ở58–59. Trang đầu đề có thể khác trang canchi; không lấy vị trí đầu đề làm vị trí mọi trường. Ảnh46 phân biệt申金chú quái thân ở隨 với午火子孫Phục ởhào4. Ảnh49giữ巳火子孫Phục ởhào5蠱; quái thân không thay vai trò Lục thân.

## Đối chiếu thực thi

**8kiểm đạt**. HHC thật gọi72lần:64lần kiểm danh tính sốquẻ cho64bộ giá trị tĩnh và8lần cho bốn quẻin câu3(gốc+biến). Bộ Lục hào riêng thực thi384gán canchi/Lụcthân,128vịtríThếỨng và **320truy vấn vai trò tường minh** (64×5vai trò). Bốn lớp này cần phân biệt: HHC kiểm sốquẻ; bộ riêng kiểm nhãn; nguồn in cung cấp chuẩn đối; không cộng chúng thành số quẻin độc lập hoặc engine dựbáo đã được xác thực.

Toàn384dòng canchi/Lục thân và128dấu khớp bộ riêng. 56tọa độ Phục in khớp cổng tìm Phục theo cung gốc khi vai trò cần hỏi không hiện trong sáu hào tĩnh. So cả vịtrí,chi,hành vàvai trò; không chỉ so tổng số. Kiểm không lấy quái thân申 ở隨 làm Phục, và giữ đúng巳 ở蠱. Không chỉ định Dụng có hiệu lực, không xét vượngsuy/khôngphá/ámđộng, không suy số Phục từ mọi mục tiêu không được hỏi. Mọi nguồn dòng/ca/digest nằm trong `research/liuyao-b03-line-labels` và `qa/liuyao-b03-line-labels`.

Không lặp4096mặt nạ động khi engine không đổi. Các ca ở đây là64hình in tĩnh; **chú hào biến, toàn bộ nét âm–dương, nhãn quái thân và mọi câu văn giải thích chưa được nhận đã đối hết**. Nhãn384dòng gốc không thay thế các trường ấy. Dị đầu đề筮/噬giữ hồ sơ cũ, không tự sửa theo tên quẻ chuẩn. Không xác minh kết cục chiêm nghiệm hoặc dựng ngàyGregory từ các hình.

## Bốn quẻ in của câu hỏi thứ ba

Đọc mở rộng sách6 PDF9–11, ba renderQA360dpi/bốn crop; cả bốn sơ đồ nằm trong khoảng câu3, khớp con số4của riêng câu3 trong mục lục. Không tính sơ đồ câu2còn ở bên phải trang9. `BOOK6_QUESTION3_FIXTURES.json` giữ ngày/tháng vàgiátrị hào động đọc từ ảnh:

- 申月戊辰日: 同人13hào5→離30;申→未.
- 卯月甲寅日: 困47hào1/4→節60;寅→巳,亥→申.
- 丑月戊子日: 同人13hào1/5→旅56;卯→辰,申→未.
- 寅月乙丑日: 升46hào3→師7;酉→午.

Tám lời gọi HHC xác nhận gốc/biến, bộ riêng kiểm sáu tọa độ tự biến vànăm ngữcảnh Dụng chỉđịnh. Ca升giữ cảhai vịtrí父亥2/5 để kiểm tọađộ, không tự chọn một; nguyên thần酉hào3động tự biến午hồi khắc được nhận diện với cảhai ngữcảnh. Không nhận điều này đã quyết hiệu lực cứu Dụng, chọn thời điểm hoặc xác minh lời bệnh/sinh tử của sách. Ca困có申do chính hào亥biến thành; không sửa quy tắc nguyên thần gốc thành trộn chi biến tùy ý. Bốn lời gọi lunar thật kiểm nhãn ngày vàtuầnkhông(戌亥/子丑/午未/戌亥) tại các mốc trưa dùng để duyệt vòng canchi; **không quy đổi ngày cổ sang Gregory**.

Sáu quẻin sách6 đã đối cấu trúc gồm hai ca phát hành trước vàbốn ca mới câu3; chưa đối hết mọi chú hào/điều kiện của sáu ca. Tổng131do mục lục ghi chưa là đếm toànthân sách hoặc131ca đãkiểm.

## Bảo toàn và phần tiếp theo

HTML707411byte/SHA256 `549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`,root/site/ZIPweb và15thamchiếu Lục hào trước giữbyte. Site chỉ cóindex.html; nguồn vàQA nằm ngoài. Snapshot trước `archives/v53-before-liuyao-b03-all-annotations/` giữ sourceZIP1988642475byte/2751tệp manifest. `RELEASE_RESULTS.json` kiểm toànbyte manifest vàsourceZIP mới. Không xuất bản mạng.

Không tiếp tục gọi384dòng canchi/Lục thân/128dấu/56Phục là phần chưa làm. Tiếp các trường âm–dương/quái thân vàmệnhđề đầy đủ; sáu quẻin thực tế của18hỏiđáp đãđối cấu trúc, gồm4câu3. Tổng131là con số mục lục, chưa đếm toànthân sách. Mạnhyếu/chânkhông/ứngkỳ/hiệu lực Nguyênthần, chữthuyền sách5/kếtcuối sách6/nhânchứng độclập và ngàyB02PDF52 còn mở. B02vẫn136đơn vị/103thânmục đềmục/26khoảng đọc lầnđầu. **Chưa áp hết14quyển B03 hoặc toànkho40nguồn/bốn hướng.**
''',encoding='utf-8')
print('Printedprimarylabels scope recorded;allotherclauses/catalogue remain active.')
