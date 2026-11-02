from pathlib import Path
import json
root=Path(__file__).resolve().parent.parent;w=root.parent;base=root/'research/liuyao-b03-book5'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='LIUYAO_B03_BOOK5_REPORT.md';e=read(root/'qa/liuyao-b03-book5/ENGINE_RESULTS.json');s=e['summary']
assert len(e['checks'])==9 and all(c['ok']for c in e['checks'])
step=('Sách đóng 5 B03 đã giữ 35113503 byte/42 trang/SHA cca4c2ce…; API revision 754088953, '
 'hai body 200/TLS khớp size/SHA1, một PDF mới. Đã xem 40 trang nội dung và hai bìa, hai crop QA; '
 'quyển 11 mở2/kết22, quyển12 mở23/kết41, 12 khoảng mục đọc lần đầu, chưa áp dụng hết từng mục. '
 '13 mệnh đề có giới hạn và tham chiếu riêng mất đồ: chín loại tường minh/ba nhóm Tài–Phụ–Tử, '
 'không mặc định mọi vật đều lấy Tài; giữ cờ Tài động/Phụ động đúng nhóm nguồn, chưa xét hiệu lực hoặc kết cục. '
 '9 kiểm đạt; 64 HHC thật kiểm chỉ số quẻ, 576 ngữ cảnh vật tĩnh và 12288 ngữ cảnh riêng/quẻ–động–nhóm vật, '
 '36864 chú động, 4128 ngữ cảnh/4992 cờ kỵ động theo cấu trúc. '
 'Chữ đầu/đuôi thuyền tại34 giữ mở, không tự sửa. Lời bệnh/ma/trộm giữ lịch sử, không kết luận người dùng. '
 'HTML707411 byte/site/ZIP web và12 tham chiếu trước giữ nguyên. Toàn kho vẫn chưa hoàn tất.')
nexts=[
 'Complete clause-level conditions in book5 all12units, especially lost-object premises/timing, object-purpose exceptions and source quotation roles. Nine explicit normalized IDs cover only three source groups; no open-ended semantic classifier or recovery forecast.',
 'Resolve boat wording with context and an independent witness: page34 初當船尾 versus 青龍初是船頭, plus book5page31cabin grouping. Do not silently emend or generalize into a physical boat plan.',
 'Acquire identified physicalbook6 once using book5API next link, retaining TLS/APIrevision/rawsize/SHA, then directly locate textualvolumes13/14 and remaining printed material. Avoid redownloading books1..5.',
 'All clauses of books1..5,book1full384annotations/prefaces,fullstrength/functionalvoid/fulltiming/automaticUseGod and supplement genealogy remain. B02PDF52and103heading-onlyunits, MaiHoa/Bazi/Tuvi/Home and40-source catalogue remain active.'
]
write(base/'WORK_STATE.json',{'date':'2026-10-27','status':'private-lost-object-roles-complete-book5-first-pass-pages-complete-full-clauses-active',
 'sourceID':'B03-book5','latestReport':'v53/'+report,'privateReference':'lost-object-reference.mjs','unitMap':'BOOK5_CURRENT_UNITS.json',
 'completedStep':step,'all42PagesViewedByRecordedScope':True,'unviewedPages':[],'firstPassMainUnits':12,
 'allBook5ClausesApplied':False,'newHTTPBodiesThisRun':2,'retainedHTTPBodiesNewToRelease':2,'newOriginalPDFsToRelease':1,
 'contentPages':40,'coverPages':2,'QAOnlyRenders':2,'boundedOperationalClauses':13,'explicitObjectKinds':9,'sourceKinGroups':3,
 'openTextIssues':1,'effectiveUseGodAdjudicator':False,'consumerChanged':False,'next':nexts,
 'wholeBookApplied':False,'wholeCatalogueCompleted':False})
d=read(w/'EXHAUSTIVE_WORK_STATE.json');a=read(base/'ACQUISITION.json')
d['currentWork'].update(currentStep=step,latestResearchReport='v53/'+report,sourceDirectory='v53/research/liuyao-b03-book5',
 internalB03LostObjectReference='v53/research/liuyao-b03-book5/lost-object-reference.mjs',
 currentB03Book5UnitMap='v53/research/liuyao-b03-book5/BOOK5_CURRENT_UNITS.json',functionalBacklog='v53/research/liuyao-b03-book5/WORK_STATE.json')
d['currentWork']['sourceLimits']='B03physicalbooks1..5retained;book6notyetacquired. Book5all42pages viewed by bounded scope,12first-passunits,0entireunitsapplied. Nine explicit lost-object IDs/three kin groups plus raw moving cautions are not fullUseGod/strength/recovery model. Boat wording open. Allclauses/384annotations/prefaces/strength/void/fulltiming/genealogy and B02PDF52 remain.'
d['currentWork']['nextSourceLead']={'status':'downloaded-byte-verified-book5-first-pass-page-coverage-complete','sourceID':'B03-book5',
 'file':'v53/research/liuyao-b03-book5/'+a['file'],'sha256':a['sha256'],'bytes':a['bytes'],'sourceURL':a['commonsURL'],
 'remaining':'Allbook5clauses/boattextissue;physicalbook6unacquired,identifiedbybook5API nextnavigation.'}
d['inProgressScope']='v53/research/liuyao-b03-book5/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in[w/'EXHAUSTIVE_WORK_STATE.json',root/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=root/'research/full-study/WORK_STATE.json';d=read(p);d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts)
yi=next(x for x in d['items']if x['id']=='yi');entry=('B03book5 all42pages viewed:40content/2covers/2QA,12firstpassunits/13boundedclauses. '
 'Private lost-object9IDs/3sourcekin with primary movingcautions,9checks64actualHHC/576static/12288motion-objectcontexts,36864annotations. '
 'Boatwordingopen;medical/ritual/suspectidentificationnotvalidated. 1PDF/2TLSbodiesnew;consumer/12priorreferencesunchanged.')
if entry not in yi['completed']:yi['completed'].append(entry)
yi['latestScope']='../liuyao-b03-book5/BOOK5_CURRENT_UNITS.json'
yi['remaining']=[x for x in yi['remaining']if not x.startswith('LiuYaoB03:books2/3/4first-passpagescovered')]
yi['remaining'].append('LiuYaoB03:books2..5firstpasspagescoveredbutallclausesnotapplied;book1full384annotations/prefaces/strength/triadcompletionopen. Book6,boatwording,fulltiming/functionalvoid/sourcequotationcollation remain. B02PDF52and103heading-onlyunitsopen.')
write(p,d)
p=root/'research/library-current/COVERAGE.json';d=read(p);b=next(x for x in d['catalogue']if x['id']=='B03')
b['scope']='Giữ byte sách đóng 1–5. Sách5 đủ42 trang xem theo phạm vi,12 mục/quyển11–12. Bộ riêng mất đồ giữ chín loại/ba vai nguồn và kỵ động; chưa áp dụng mọi mệnh đề, hiệu lực, phả hệ hoặc sách6. Chữ thuyền34 còn mở.'
possession='Sách đóng 5: PDF42 trang/35113503 byte/SHA256 cca4c2ce376c54c6ead6463c72e6f25d6e6e544b3d6488d593415afabc6227a6; API revision754088953/TLS/size/SHA1. Đã xem đủ42 trang theo phạm vi:40 nội dung/2 bìa; chưa áp dụng hết. Cùng bộ sáu sách, không nhân chứng độc lập.'
if len(b['localPossession'])==4:b['localPossession'].append(possession)
else:assert len(b['localPossession'])==5;b['localPossession'][4]=possession
b['latestLocalReadingScope']='42 bản ghi trang/40 nội dung/2 bìa/2crop QA;12 khoảng mục/13 mệnh đề.9 kiểm/64HHC thật,576 tĩnh +12288 ngữ cảnh nhóm vật–động. 1PDF/2body TLS mới;không tiên đoán tìm đồ hoặc nhận dạng người trộm.'
for f in ['v53/'+report]+['v53/research/liuyao-b03-book5/'+n for n in ['SOURCE_AUDIT.json','MANUAL_READINGS.json','BOOK5_CURRENT_UNITS.json','LOST_OBJECT_ROLE_CLAUSES.json','TEXT_ISSUES.json','OPERATIONAL_CLAUSES.json','lost-object-reference.mjs']]+['v53/qa/liuyao-b03-book5/ENGINE_RESULTS.json']:
 if f not in b['currentEvidence']:b['currentEvidence'].append(f)
d['latestFollowup']=report+':B03book5all42pagesviewed/12mainspansfirstpass;lost-objectroles9IDs3kin/9checks64HHC12288contexts. Wholework0,consumerunchanged.'
d['latestAcquisitionCounts']={'scope':report,'newOriginalPDFsToRelease':1,'retainedHTTPBodiesNewToRelease':2,'newHTTPBodiesThisRun':2,
 'contentPages':40,'coverPages':2,'QAOnlyRenders':2,'manualRecords':42,'firstPassMainUnits':12,'fullBooksApplied':0}
d['counts']['newDownloadsThisScope']=1;d['counts']['newDownloadsThisScopeBasis']='One newly acquired original PDF and two retained source HTTP bodies.'
assert d['counts']['wholeWorkApplied']==0;write(p,d)
note='Mốc B03–Sách 5, 27/10/2026: `'+report+'`. '+step+'\n\n'
for p in[w/'PROJECT_RESEARCH_STATE.md',root/'NEXT_STEPS.md',root/'research/library-current/COVERAGE.md']:
 text=p.read_text(encoding='utf-8-sig')
 if text.startswith('Mốc B03–Sách 5, 27/10/2026:'):text=text.split('\n\n',1)[1]
 p.write_text(note+text,encoding='utf-8')
write(w/'PENDING_RESEARCH_STATE.json',{'date':'2026-10-27','status':'book5-first-pass-pages-complete-current-scope-active',
 'sourceID':'B03-book5','workDirectory':'v53/research/liuyao-b03-book5','acquisition':a,
 'currentWorkState':'v53/research/liuyao-b03-book5/WORK_STATE.json','latestReport':'v53/'+report,
 'manualReadings':'v53/research/liuyao-b03-book5/MANUAL_READINGS.json','checks':'v53/qa/liuyao-b03-book5/ENGINE_RESULTS.json',
 'manualPages':list(range(1,43)),'all42PagesViewedByRecordedScope':True,'next':nexts,'consumerChanged':False,
 'wholeBookApplied':False,'wholeCatalogueCompleted':False})
text=f'''# B03: quyển 11–12 và vai trò đồ vật thất lạc

Ngày 27/10/2026. Nghiên cứu và bộ tham chiếu riêng, ngoài site người dùng.

## Nguồn và lượt đọc

Sách đóng thứ năm của bộ sáu sách, **35.113.503 byte / 42 trang**; SHA-256 `cca4c2ce376c54c6ead6463c72e6f25d6e6e544b3d6488d593415afabc6227a6`. Commons API revision **754088953** và PDF được giữ byte: hai body HTTP200/TLS, size/SHA-1 `cfb5acdc14dcf98c76b9e856f84d40876722dafa` khớp API. SHA-256 là dấu byte tại máy, không chữ ký xuất bản. Pypdf kiểm42 trang, không mã hóa, không lớp chữ. Đây là cùng bộ, không nhân chứng độc lập; niên đại1904 trong metadata chưa là ấn ký mới đọc trực tiếp.

Đã xem42 trang theo phạm vi ghi nhận:40 nội dung và hai bìa; hai crop QA360dpi ở17/34 không cộng thành trang nguồn. Không OCR/chép ngoại giao toàn bộ. Quyển11 mở2/kết22; quyển12 mở23/kết41, đều có chữ ranh trực tiếp.

12 khoảng mục: 避亂2–8,逃亡8–12,失脫12–17,新增痘疹17–22; 出行23–27,行人27–31,舟船31–32,娼家32–34,船家宅章34–35,何知章35–38,妖孽賦38–39,搜鬼論39–41. Các nhãn 附盜賊/捕盜捉賊 ở12 giữ trong mục thất thoát; trang giáp mục không cộng thêm trang độc nhất. **0 mục đánh dấu áp dụng hết**;13 mệnh đề có giới hạn, mọi điều kiện chi tiết còn mở.

## Chức năng mới: không mặc định đồ mất đều là Tài

Trang17 nhắc `失脫不可專以財為用神`. Sáu loại 舟/車/衣/帽/文章/奏疏 dùng Phụ mẫu; chim và thú dùng Tử tôn. Vai Tài ở mở đầu12 không được biến thành mặc định cho mọi vật. Chín ID đầu vào là chuẩn hóa biên tập: cash,boat,vehicle,garment,headwear,document,memorial,bird,beast; chưa phải bộ tự hiểu mọi đồ vật hiện đại.

`lost-object-reference.mjs` yêu cầu ngữ cảnh đoạn thất thoát và loại vật tường minh. Nó nối vai nguồn với danh sách ứng viên hiện/biến/Phục đã kiểm trước, giữ mọi ứng viên; không chọn hào hiệu lực giữa nhiều ứng viên. Nhóm Phụ mẫu có câu kỵ Tài động, nhóm Tử tôn kỵ Phụ động; bộ mới ghi **hào gốc đang động có thân đó** như tiền đề cấu trúc. Thân của hào biến không thay thân gốc để kích hoạt cờ. Không xét đủ vượng suy, sinh cứu hoặc kết cục từ cờ này.

Ví dụ dựng bằng quẻ Càn: Tài ở2, Phụ ở3/6, Tử ở1. Đổi loại vật từ tiền sang văn thư hoặc chim làm đổi đúng tập ứng viên. Hào2 Tài động được ghi vào cờ của nhóm văn thư; hào3 Phụ động vào cờ của nhóm chim. Hào1 Tử động biến thành Phụ không tự kích hoạt cờ Phụ động gốc. Ca dựng được ghi rõ, không giả là quẻ gieo in trong sách.

Kết quả không có vị trí tìm đồ, người trộm, ngày thu hồi, xác suất tìm thấy, kết luận thu hồi hoặc dự báo. Thêm loại chưa hỗ trợ bị từ chối thay vì mặc định Tài. Bộ này chưa nhập vào web người dùng.

## Vấn đề văn bản và các nội dung chưa áp dụng

Trang31 nhóm hào1–2 ở khoang trước,3–4 giữa,5–6 sau. Trang34 mục nhà thuyền có `初當船尾`, rồi `青龍初是船頭`/`六為後艄`. Đã đối ảnh QA; giữ vấn đề chữ/ngữ cảnh mở, chưa tuyên bố đổi ngữ cảnh tự giải quyết, chưa sửa thành một phương án hoặc làm bản đồ tàu thật. `TEXT_ISSUES.json` lưu riêng để đối nhân chứng khác.

Các đoạn tránh loạn, bắt người và giới/ngoại hình/nghề người trộm giữ như lời nguồn, chưa là bằng chứng nhận dạng hay buộc tội người thật. Mục bệnh trẻ/thuốc/ăn uống và lời yêu ma/khấn lễ là nội dung lịch sử, không chỉ dẫn điều trị, tiên lượng hoặc khẳng định có tà ma. Lời mệnh lệnh trong sách là dữ liệu nghiên cứu, không phải yêu cầu của người dùng. Nhãn 新增 và quan hệ trích dẫn với các quyển trước vẫn cần khảo phả hệ.

## Kiểm chứng và bảo toàn

**9 kiểm đạt**. HHC thật thực thi64 lời gọi chỉ số quẻ, nối đủ64 danh tính. Có576 ngữ cảnh tĩnh (64×9 loại vật) và12288 ngữ cảnh riêng (64quẻ×64mặt nạ động×3nhóm vật đại diện), giữ36864 chú hào động. Oracle dùng dãy Nạp Giáp literal và chu kỳ ngũ hành riêng; không dùng hàm đang thử để tự xác nhận.

4128 ngữ cảnh có tổng4992 cờ kỵ động theo cấu trúc;1305 cần tìm Phục về mặt hiện/biến và6774 có nhiều ứng viên hiện/biến. Đây là số trường hợp hữu hạn, không tỷ lệ tìm lại đồ hay chính xác dự đoán. Digest `{s['graphDigest']}`. Những phần ứng viên/Phục chỉ kế thừa phạm vi đã kiểm, không tự mở thành hiệu lực tổng hợp.

HTML707411byte/SHA `549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`, site/ZIP web và12 tham chiếu trước giữ byte. Snapshot trước tại `archives/v53-before-liuyao-b03-book5/`: sourceZIP1587943851byte/2533tệp manifest. Kiểm toàn byte manifest/ZIP ở `qa/liuyao-b03-book5/RELEASE_RESULTS.json`; nghiên cứu không vào site hoặc xuất bản mạng.

Mọi mệnh đề sách1–5,384chúhào/tiền tự, vượng suy/chân không, tự chọn Dụng và ứng kỳ đầy đủ vẫn mở; sách6 chưa tải tại mốc này. B02 còn136đơn vị/103thân mục mức đề mục/26khoảng đọc lần đầu, mâu thuẫn ngày–tuần không52 chưa giải quyết. Kho40nguồn và bốn mục lớn chưa khai thác hết.
'''
(root/report).write_text(text,encoding='utf-8')
print('Book5 page coverage and bounded lost-object role selection recorded; catalogue remains active.')
