from pathlib import Path
import json
root=Path(__file__).resolve().parent.parent;w=root.parent;base=root/'research/liuyao-b03-book6'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='LIUYAO_B03_BOOK6_REPORT.md';e=read(root/'qa/liuyao-b03-book6/ENGINE_RESULTS.json');s=e['summary']
assert len(e['checks'])==8 and all(c['ok']for c in e['checks'])
step=('Sách đóng 6 B03 đã giữ 55093879 byte/65 trang/SHA1d6c6568…; APIrevision754088957, '
 'hai body200/TLS khớp size/SHA1. Đã xem65 trang theo phạm vi:63 nội dung/2bìa, '
 '7 nội dung/1bìa kế thừa pending,56 nội dung/1bìa mới nhịp này;2crop QA. '
 'Quyển13 mở2, quyển14 mở35;18 khoảng câu hỏi theo nguồn hiện có,18mệnh đề có giới hạn, '
 'không nhận đã thấy ấn ký kết cuối hoặc áp hết từng câu. '
 'Tham chiếu riêng Nguyên thần giữ ứng viên hào gốc sinh Dụng và quan hệ tự biến hồi khắc; '
 'hiệu lực/sinh cứu/vượng suy chưa kết luận. '
 '8kiểm đạt,68HHC thật gồm64danh tính+4lời gọi cho2quẻ in63.4→49/47.3.5→32; '
 '24576ngữ cảnh riêng/28672ứng viên,3328cờ tự biến khắc gốc. '
 'Cả6PDF cùng bộ đã giữ byte nhưng chưa áp hết14quyển/mọi mệnh đề/384chú hào hoặc toàn kho40nguồn. '
 'HTML707411byte/site/ZIPweb và13tham chiếu trước giữ nguyên.')
nexts=[
 'Book6 all65images viewed by bounded scope,18available-question spans;every printed cast/date/annotation and all clauses remain. Add high-resolution source fixtures across questions3..18;two opening structures are only a small subset,never claim all examples checked.',
 'Complete source-specific strength/functionalvoid/triadcompletion/timing and original-support conditions by explicit premises, retaining B03quoted/polemical positions separately. Raw primary generation and own-return control do not adjudicate effective rescue.',
 'All6same-seriesPDFs are retained;do not redownload or count them as independent witnesses. Audit book1prefaces/full384annotations/remainingpages; reconcile boatwording in book5page34 with an independent witness. Finalbook6colophon/unabridged ending not directly established.',
 'B02still136units/103heading-onlybodies/26firstpassspans,PDF52date-voidconflictopen. Continue unresolved MaiHoa/Bazi/Tuvi/Home clauses and40-source catalogue coverage;0wholeworksapplied.'
]
write(base/'WORK_STATE.json',{'date':'2026-10-27','status':'private-support-chain-coordinates-complete-book6-available-page-coverage-complete-full-clauses-active',
 'sourceID':'B03-book6','latestReport':'v53/'+report,'privateReference':'support-chain-reference.mjs','unitMap':'BOOK6_CURRENT_UNITS.json',
 'completedStep':step,'all65PagesViewedByRecordedScope':True,'unviewedPages':[],'firstPassAvailableQuestionSpans':18,
 'allBook6ClausesApplied':False,'newHTTPBodiesThisRun':2,'retainedHTTPBodiesNewToRelease':2,'newOriginalPDFsToRelease':1,
 'contentPages':63,'coverPages':2,'inheritedPendingContentPages':7,'inheritedPendingCoverPages':1,
 'newContentRendersThisRun':56,'newCoverRendersThisRun':1,'QAOnlyRenders':2,'boundedOperationalClauses':18,
 'printedFixtureCount':2,'actualHHCHexCalls':68,'effectiveSupportAdjudicator':False,'directPrintedFinalColophonEstablished':False,
 'allSixSameSeriesPDFsRetained':True,'all14TextualVolumesApplied':False,'consumerChanged':False,
 'next':nexts,'wholeBookApplied':False,'wholeCatalogueCompleted':False})
d=read(w/'EXHAUSTIVE_WORK_STATE.json');a=read(base/'ACQUISITION.json')
d['currentWork'].update(currentStep=step,latestResearchReport='v53/'+report,sourceDirectory='v53/research/liuyao-b03-book6',
 internalB03SupportChainReference='v53/research/liuyao-b03-book6/support-chain-reference.mjs',
 currentB03Book6UnitMap='v53/research/liuyao-b03-book6/BOOK6_CURRENT_UNITS.json',functionalBacklog='v53/research/liuyao-b03-book6/WORK_STATE.json')
d['currentWork']['sourceLimits']='All6same-seriesB03PDFsretained,notindependentwitnesses,noteveryclauseapplied. Book6all65imagesviewed/18available-question-spans;twoopeningprintedfigurestructureschecked,notallfigures/annotations. Finalcolophon/unabridgedendingnotdirectlyestablished. Book1remainingpages/prefaces/384annotations,allclauses/strength/functionalvoid/fulltiming/genealogy,B05boatwordingandB02PDF52remain.'
d['currentWork']['nextSourceLead']={'status':'all-six-same-series-PDFs-retained-book6-available-page-coverage-complete','sourceID':'B03-book6',
 'file':'v53/research/liuyao-b03-book6/'+a['file'],'sha256':a['sha256'],'bytes':a['bytes'],'sourceURL':a['commonsURL'],
 'remaining':'No new same-series acquisition needed. Allbook6printedfigures/clauses/ending;book1prefaces/384annotations and independent collation remain.'}
d['inProgressScope']='v53/research/liuyao-b03-book6/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in[w/'EXHAUSTIVE_WORK_STATE.json',root/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=root/'research/full-study/WORK_STATE.json';d=read(p);d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts)
yi=next(x for x in d['items']if x['id']=='yi');entry=('B03book6all65imagesviewed/63content2covers,18availablequestions/18boundedclauses;two printed structures63.4→49/47.3.5→32checked. '
 '8checks68actualHHC/24576privatecontexts/28672candidateorigins/3328ownreturncontrolcautions. '
 'All6same-seriesPDFsretained,notall14volumes/clausesapplied. Consumer/13priorreferencesunchanged.')
if entry not in yi['completed']:yi['completed'].append(entry)
yi['latestScope']='../liuyao-b03-book6/BOOK6_CURRENT_UNITS.json'
yi['remaining']=[x for x in yi['remaining']if not x.startswith('LiuYaoB03:books2..5firstpasspagescovered')]
yi['remaining'].append('LiuYaoB03:all6same-seriesPDFsretained;book1prefaces/remainingpages/384annotations andallclausesnotapplied. Book6printedfixturesbeyond2,finalending/strength/void/timing/genealogy,book5boatwordingopen. B02PDF52and103heading-onlyunitsopen.')
write(p,d)
p=root/'research/library-current/COVERAGE.json';d=read(p);b=next(x for x in d['catalogue']if x['id']=='B03')
b['scope']='Giữ byte đủ6sách cùngbộ, không nhânchứngđộc lập. Sách6 đủ65ảnh xem theo phạmvi,18 khoảngcâu hỏi/quyển13–14;2quẻinđối cấu trúc, chưa mọi quẻ/chú. Có thamchiếuriêng NguyênthầnsinhDụng/hồi khắc, chưa hiệu lực/mọi mệnhđề/384chúhào/tiềntự/kếtcuối hoặc phảhệ.'
possession='Sách đóng6: PDF65trang/55093879byte/SHA256 1d6c656828533ac52ae1fd4ff06cc3c025db98ae5458dc686eda2a6b1d11f07f; APIrevision754088957/TLS/size/SHA1. Đãxem65ảnh theo phạmvi:63nội dung/2bìa; chưa áp hết. Cùngbộ6sách, không nhânchứng độc lập; chưa trực tiếp xác lập ấn ký kết cuối.'
if len(b['localPossession'])==5:b['localPossession'].append(possession)
else:assert len(b['localPossession'])==6;b['localPossession'][5]=possession
b['latestLocalReadingScope']='65bản ghi/63nội dung/2bìa/2cropQA,18khoảngcâu hỏi/18mệnhđề.8kiểm/68HHCthật(64danh tính+4cho2quẻin);24576ngữcảnhriêng/3328cờ tự biếnkhắc gốc. 1PDF/2bodyTLS mới;chưa sinh cứu cóhiệulực.'
for f in ['v53/'+report]+['v53/research/liuyao-b03-book6/'+n for n in ['SOURCE_AUDIT.json','MANUAL_READINGS.json','BOOK6_CURRENT_UNITS.json','PRINTED_FIXTURES.json','SUPPORT_CHAIN_CLAUSE.json','OPERATIONAL_CLAUSES.json','support-chain-reference.mjs']]+['v53/qa/liuyao-b03-book6/ENGINE_RESULTS.json']:
 if f not in b['currentEvidence']:b['currentEvidence'].append(f)
d['latestFollowup']=report+':All6same-seriesPDFsretained;book6all65imagesviewed/18availablequestions,notallclauses. Supportchaincoordinates/8checks68HHC24576contexts. Wholework0,consumerunchanged.'
d['latestAcquisitionCounts']={'scope':report,'newOriginalPDFsToRelease':1,'retainedHTTPBodiesNewToRelease':2,'newHTTPBodiesThisRun':2,
 'contentPages':63,'coverPages':2,'inheritedPendingContentPages':7,'inheritedPendingCoverPages':1,
 'newContentRendersThisRun':56,'newCoverRendersThisRun':1,'QAOnlyRenders':2,'manualRecords':65,
 'firstPassAvailableQuestionSpans':18,'allSixSameSeriesPDFsRetained':True,'fullBooksApplied':0}
d['counts']['newDownloadsThisScope']=1;d['counts']['newDownloadsThisScopeBasis']='One newly acquired original PDF and two retained source HTTP bodies.'
assert d['counts']['wholeWorkApplied']==0;write(p,d)
note='Mốc B03–Sách6, 27/10/2026: `'+report+'`. '+step+'\n\n'
for p in[w/'PROJECT_RESEARCH_STATE.md',root/'NEXT_STEPS.md',root/'research/library-current/COVERAGE.md']:
 text=p.read_text(encoding='utf-8-sig')
 if text.startswith('Công việc tiếp sau B03–Sách5:'):text=text.split('\n\n',1)[1]
 if text.startswith('Mốc B03–Sách6, 27/10/2026:'):text=text.split('\n\n',1)[1]
 p.write_text(note+text,encoding='utf-8')
write(w/'PENDING_RESEARCH_STATE.json',{'date':'2026-10-27','status':'book6-available-pages-complete-current-scope-active',
 'sourceID':'B03-book6','workDirectory':'v53/research/liuyao-b03-book6','acquisition':a,
 'currentWorkState':'v53/research/liuyao-b03-book6/WORK_STATE.json','latestReport':'v53/'+report,
 'manualReadings':'v53/research/liuyao-b03-book6/MANUAL_READINGS.json','checks':'v53/qa/liuyao-b03-book6/ENGINE_RESULTS.json',
 'manualPages':list(range(1,66)),'all65PagesViewedByRecordedScope':True,'allSixSameSeriesPDFsRetained':True,
 'next':nexts,'consumerChanged':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False})
text=f'''# B03: 18 hỏi đáp và điều kiện Nguyên thần sinh Dụng

Ngày27/10/2026. Phần nghiên cứu và bộ tham chiếu riêng nằm ngoài site.

## Nguồn, phạm vi và giới hạn

Sách đóng6: **55.093.879byte/65trang**, SHA256 `1d6c656828533ac52ae1fd4ff06cc3c025db98ae5458dc686eda2a6b1d11f07f`; CommonsAPI revision754088957. Hai bodyHTTP200/TLS giữ byte, size/SHA1 `30da3dcd634c1a109b0d7a3891657e95d053471a` khớpAPI. SHA256 là định danhbyte tại máy, không chữ ký nhà xuất bản. Không lớp chữ, không mã hóa. Cả sáuPDF cùng bộ đã giữ; điều này **không là sáu nhân chứng độc lập hoặc áp dụng hết14quyển**. Metadata1904 chưa thành chứng cứ ấn ký mới.

Đã xem65ảnh theo phạmvi ghi nhận:63nội dung/2bìa. Bảy nội dung2–8 và bìa1 kế thừa pending;56nội dung9–64 vàbìa65 mới;2cropQA360dpi tại2/3 không cộng thành trangnguồn. KhôngOCR/chép ngoại giao toàn bộ. Đầu quyển13 ở2, quyển14 ở35 đọc trực tiếp. Ảnh nội dung cuối64 không có chứng cứ ấn ký kết cuối được xác lập; không nhận là đã chứng minh bản in không thiếu cuối.

`BOOK6_CURRENT_UNITS.json` giữ18khoảng câu hỏi:1三傳2–4,2回頭剋4–9,3原神9–11,4三合11–17,5反吟17–19,6伏吟19–21,7旬空21–28,8月破28–31,9伏神31–34;10進退35–37,11沖合先後37–41,12生墓絕41–47,13六沖六合47–52,14刑害52–53,15獨靜獨發53–57,16盡靜盡發57–59,17多現59–62,18所問之意62–64. Tên rút gọn là nhãn biên tập. Trang giáp không tính thêm trang độc nhất; câu18 chỉ nhận khoảng ảnh còn có, không chứng minh kết văn bản đầy đủ. **0mục đánh dấu áp dụng hết**.

18mệnh đề cógiới hạn giữ điều kiện theo từng câu. Sinh/khắc, nguyên/dụng/kỵ, tĩnh/động/ámđộng, tuầnkhông/nguyệtphá, biến/Phục và thứtự sựviệc không được gộp thành cát hung cốđịnh. Lời phê nguồn và trích dẫn không tự thành đồngthuận nhiều truyềnbản. Các truyện bệnh/sinh tử/kiện tụng/tiền bạc là lời sách, chưa có kiểmchứng kếtcục độc lập; câu mệnhlệnh là dữliệu, không phải chỉthị người dùng.

## Chức năng riêng mới

`support-chain-reference.mjs` chuẩn hóa một phần câu3: nguyên thần sinh Dụng còn có thể bị chính hào biến khắc lại hoặc bị các điều kiện khác. Đầu vào cần sáu giátrị6/7/8/9, ngữcảnh câu3 và hào Dụng **do người nghiên cứu chỉ định**. Bộ mới nhận diện hào gốc có hành sinh hào Dụng, rồi xét **chi biến thật ở cùng vị trí → chi gốc của chính hào đó**. Đây là hai quan hệ khác lớp; không dùng chi biến thay chi gốc để tạo ứng viên sinh Dụng, không cho biến chi tác động tùy ý sang vị trí khác.

Trả ứng viên, quan hệ sinh gốc, trạng thái động, tự biến và cờ tự biến khắc gốc. Hào tĩnh không có tự biến giữ `null`, không giả là đã đủ điều kiện kích hoạt. Không có ứng viên hiện không chứng minh không có sinh cứu: Phục thần và ámđộng chưa được tìm/xét trong hàm này. Thiếu tháng/ngày/mạnhyếu/không/phá/tiếnthoái/mộ/tuyệt và ưu tiên nguồn giữ chưa rõ. Không chọn Nguyên thần cóhiệulực, không kếtluận đã cứu Dụng, không dựbáo người dùng.

## Quẻ in và kiểm thực thi

Hai quẻ mở đầu được đối ảnhQA: trang2 `既濟之革`, 63hào4→49, ngàyBínhThân/thángThìn được giữ theo chữnguồn; trang3 `困之恆`,47hào3/5→32, ngàyĐinhMùi/thángNgọ. Ba chi tự biến được kiểm:申→亥 ở63.4;午→酉 và酉→申 ở47.3/5. Chữ ngày/tháng không được dựng thành ngàyGregory; mọi chúhào chưa hiệu khảo hết, lời kể y tế/pháp lý chưa được xác minh thực tế.

**8kiểm đạt**. HHCthật chạy68lời gọi chỉsốquẻ:64danh tính và4cho hai quẻin(gốc+biến). Hai quẻin cũng qua thamchiếu cấu trúc riêng; đó không phải68quẻin đã được đối. Bộ riêng chạy24576ngữcảnh (64quẻ×64mặt nạ động×6hào Dụng chỉđịnh), so dãyNạpGiáp literal và quan hệ ngũhành độc lập.

Có28672ứng viên sinh gốc,14336tĩnh/14336động,3328cờ tự biến khắc gốc;9920tọa độ chỉ chi biến mới sinh Dụng không được thay thế ứngviên gốc. Đây là đếm cấu trúc hữu hạn, không tỷ lệ đúng hoặc hiệu lực sinh cứu. Digest `{s['graphDigest']}`. Ca dựng riêng có đủ tĩnh/động/hồi khắc/không hồi khắc/biến sinh khác gốc. Đầu vào sai/mảngthưa/extra mạnhyếu-thángngày hoặc ngữcảnh khác bị từchối, không đoán tiềnđề còn thiếu.

## Bảo toàn và công việc còn mở

HTML707411byte/SHA `549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`, root/site/ZIPweb và13thamchiếu trước giữbyte. Snapshot trước tại `archives/v53-before-liuyao-b03-book6/`: sourceZIP1711630083byte/2599tệp manifest. Kiểm toàn byte manifest/ZIP ghi ở `qa/liuyao-b03-book6/RELEASE_RESULTS.json`. Không đưa nguồn/QA vào site hoặc xuấtbản mạng.

Tiếp kiểm mọi quẻin/ngày/chúhào trong18hỏiđáp; hiệu lực Nguyênthần/tổngvượngsuy/chânkhông/ứngkỳ chưa hoàn chỉnh. Sách1 còn tiền tự/trang chưa đọc đầyđủ/384chúhào; mọi mệnhđề sách1–6,phảhệ/kếtcuối chưa xong. Chữ thuyền sách5trang34 giữ mở. B02vẫn136đơn vị/103thânmục mứcđềmục/26khoảng đọc lầnđầu và ngày–tuầnkhông52mâu thuẫn. Kho40nguồn/bốn mục lớn chưa khai thác hết.
'''
(root/report).write_text(text,encoding='utf-8')
print('Book6boundedpagecoverage/18questions/supportchain recorded; allcatalogue work remains active.')
