from pathlib import Path
from hashlib import sha256
import json, shutil

root=Path(__file__).resolve().parent.parent; workspace=root.parent
base=root/'research/meihua-layers'; qa=root/'qa/meihua-layers'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
html=(root/'Huyen_Hoc_Cac.html').read_bytes(); product={'file':'v53/Huyen_Hoc_Cac.html','bytes':len(html),'sha256':sha256(html).hexdigest()}
assert product['bytes']==707411 and product['sha256']=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html==(base/'candidate/Huyen_Hoc_Cac.html').read_bytes()
engine=read(qa/'ENGINE_RESULTS.json'); browser=read(qa/'BROWSER_RESULTS.json'); pdf=read(qa/'PDF_RESULTS.json'); core=read(root/'qa/test-results.json')
for d,n in [(engine,14),(browser,34),(core,50)]:assert len(d['checks'])==n and all(c['ok']for c in d['checks'])
assert browser['pdfCreated'] and not browser['errors'] and not browser['http'] and pdf['pages']==4
for name in ['test-results.json','tuvi-parity.json']:shutil.copyfile(root/'qa'/name,qa/('core-'+name))
attempts=[]
for n,meaning in [(1,'Wrong pure-Khun fixture:count8/hour1 is11;corrected to count8/hour8=2. pdfCreated:true was a runner metadata bug;no PDF existed at this failure.'),
 (2,'Artificial beforeprint followed immediately by PDF caused duplicate beforeprint. Runner now finishes manual lifecycle before the independent actual PDF lifecycle;app.js unchanged.'),
 (3,'34checks passed but PDF used screen media and had5pages. Visual QA caught this;retained as attempt3,not the final print artifact.')]:
 d=read(qa/f'BROWSER_ATTEMPT_{n}.json');attempts.append({'attempt':n,'executedChecks':len(d['checks']),'passedChecks':sum(c['ok']for c in d['checks']),'interpretation':meaning})
write(qa/'EXECUTION_NOTES.json',{'date':'2026-10-27','attempts':attempts,'finalAttempt':{'checks':34,'passed':34,'pdfCreated':True,'pages':4,'pdfSHA256':pdf['pdfSHA256'],'printMedia':True,'allRenderedPagesVisuallyReviewed':True},
 'candidateBytesUnchangedAcrossAttempts':True,'productDefectFound':False,'approvalReview':'Earlier usage-limit block retained historically;current require_escalated browser commands were reviewed and executed without bypass.',
 'counting':'Final14calculation+34candidatebrowser+50integratedcore=98primarychecks. PDFcontent assertions and packaging identity counted separately;failed/superseded attempts not added.'})
source=read(root/'research/meihua-reading/MANUAL_READINGS.json')
write(base/'SOURCE_APPLICATION.json',{'schema':'hhc.meihua-layers.source-application.v1','date':'2026-10-27','newHTTPResponses':0,'newPageReadings':0,
 'reusedImages':[r for r in source['records']if r['pdfPage']in[95,96,108,109]],
 'sourceRule':'Mutual Body/Use sides follow original main Body/Use sides;original Body is the reference. Existing pure-Qian/Khun changed-nuclear convention is retained.',
 'implemented':'Four separately named relationships and editorial reflection prompts;no combined score,priority rule or prediction date.',
 'editorialNotLiteralTranslation':True,'unresolvedPrintedContext':'觀梅恒卦 is not identified with the earlier plum-story49 or used as an oracle.',
 'notEstablished':['predictive accuracy','universal seasonal priority','full-book application','independent witness pedigree']})
p=base/'PENDING.json';d=read(p)
if d.get('block'):d['historicalBlock']=d['block']
d.update(date='2026-10-27',status='released-calculation-browser-pdf-and-integration-verified',previousReleasedHTMLSHA256='3800162854742c915d60f0051c65cadb0eb9a1c803f9f937bf1b6a593c96d268',
 releasedHTMLSHA256=product['sha256'],browserChecksExecuted=34,pdfCreated=True,pdfPages=4,pdfVisuallyReviewed=True,integratedCoreChecks=50,released=True,block=None,
 report='../../MEIHUA_LAYERS_REPORT.md',qa='../../qa/meihua-layers/RELEASE_RESULTS.json',
 next=['Consumer candidate has been integrated;do not rerun the old parking script or treat historical usage-limit block as current.','Continue full source extraction:216field bodies,subsidiary clauses,720hour labels and independent witness/calendar premises.'])
write(p,d)
report='MEIHUA_LAYERS_REPORT.md'
step=('Đã tích hợp bốn lớp Thể–Dụng từ candidate đúng byte sau14kiểm phép tính,34UI và50hồi quy lõi;PDF4trang đã xem đủ. HTML707411byte/SHA549cb415…;nguồn và phép lập quẻ cũ giữ riêng/giữ byte. '
 'Trở ngại duyệt ngày26/10 đã qua,candidate đã phát hành;không lặp parking hoặc gọi là chưa kiểm UI. Quyển1có216đề mục/214trường số,64tên quẻ in;đủ vị trí năm quyển không phải đủ thân bảng/mệnh đề. '
 'Tiếp thân216trường,mọi mệnh đề phụ,720nhãn bảng giờ và nhân chứng/ranh lịch độc lập;toàn kho chưa hoàn tất.')
state=read(workspace/'EXHAUSTIVE_WORK_STATE.json');assert state['status']=='active-not-complete'
state['date']='2026-10-27';state['currentWork'].update(currentStep=step,latestReport='v53/'+report,pendingConsumerCandidate='v53/research/meihua-layers/PENDING.json')
for p in [workspace/'EXHAUSTIVE_WORK_STATE.json',root/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,state)
p=root/'research/full-study/WORK_STATE.json';d=read(p);d['date']='2026-10-27';d['latestConsumerReport']=report
d['exhaustiveNext']='Four-layer consumer UI is released after98primarychecks and4visually reviewed print pages. Five-volume navigation is complete;continue all subsidiary clauses/216field bodies,720hour labels and independent witnesses/calendar premises. Do not rerun navigation or the historical parking step.'
yi=next(x for x in d['items']if x['id']=='yi')
yi['completed'].append('MaiHoa four separate Body/Use layers released:14calculation+34candidateUI+50integratedcore checks;384structures/1536relations,12pure cases,4visually reviewed print pages;all casting functions and other JS/CSS unchanged. Sources reused,0HTTP/0newpage readings.')
yi['remaining']=[s for s in yi['remaining']if 'approval'not in s.lower() and 'pendingconsumer'not in s.lower()]
write(p,d)
p=root/'research/meihua-reading/FUNCTIONAL_BACKLOG.json';d=read(p)
g=next(g for g in d['groups']if g['id']=='mutual-body-use')
g.update(status='released-four-layers-conditional-priority-open',remainingOrScope='Four-layer interface released after98primarychecks/4pagevisualQA. Each relationship retained separately;seasonal priority,combined verdicts and full clause extraction remain open.',currentApplication='../meihua-layers/PENDING.json')
write(p,d)
p=root/'research/library-current/COVERAGE.json';d=read(p);d['date']='2026-10-27';d['product']=product;b=next(x for x in d['catalogue']if x['id']=='B01')
b['scope']='Tám cách Mai Hoa và bốn lớp Thể–Dụng đang phát hành;tham chiếu nội bộ quyển2/3 và64nhóm quẻ quyển1. Đủ vị trí năm quyển;thân216trường,mệnh đề phụ,bảng,dị bản/ranh lịch vẫn mở;chưa áp hết sách.'
for f in ['v53/'+report,'v53/research/meihua-layers/SOURCE_APPLICATION.json','v53/qa/meihua-layers/RELEASE_RESULTS.json']:
 if f not in b['currentEvidence']:b['currentEvidence'].append(f)
d['latestFollowup']=report+':98primarychecks,384structures/1536relations,4pagePDFvisualQA;candidatebytes==integratedHTML.0HTTP/0newpage readings;wholeworkapplied0.'
assert d['counts']['wholeWorkApplied']==0;write(p,d)
note=('Mốc tích hợp27/10/2026: `'+report+'` đưa bốn lớp Thể–Dụng vào web;98/98kiểm chính vàPDF4trang đã xem đủ. HTML707411byte/SHA549cb415…trùng candidate đã kiểm;trở ngại duyệt cũ không còn hiện hành. '
 'Nguồn/QA ngoài site,không thêm HTTP hoặc trang đọc mới. Phần này hoàn tất;thân216trường,mệnh đề phụ5quyển,bảng720ô/nhân chứng vẫn mở. Các đoạn bên dưới là mốc lịch sử,không dùng trạng thái candidate cũ làm việc hiện tại.\n\n')
for p in [workspace/'PROJECT_RESEARCH_STATE.md',root/'NEXT_STEPS.md',root/'research/library-current/COVERAGE.md']:
 s=p.read_text(encoding='utf-8-sig')
 if not s.startswith('Mốc tích hợp27/10/2026:'):p.write_text(note+s,encoding='utf-8')
(base/'README.md').write_text('# Bốn lớp Thể–Dụng đã tích hợp — 27/10/2026\n\nCandidate giữ nguyên byte tại `candidate/` và trùng HTML đang dùng. `PENDING.json` nay là điểm nối lịch sử đã giải quyết:14kiểm phép tính,34UI,50hồi quy lõi;PDF4trang đã render/xem đủ. Xem `../../MEIHUA_LAYERS_REPORT.md`, `SOURCE_APPLICATION.json` và `../../qa/meihua-layers/EXECUTION_NOTES.json`.\n\nNguồn95–96/108–109 tái dùng,không có HTTP/trang đọc mới. Vai trò hỗ theo vị trí Thể/Dụng quẻ chủ;Thể gốc là điểm tựa. Bốn lời gợi mở tách riêng,không kết luận tổng/ngày ứng nghiệm. Ngữ cảnh觀梅恒卦 vẫn chưa phân định.\n\nHạn mức duyệt của26/10 chỉ là lịch sử;trình duyệt lượt sau đã chạy qua cơ chế duyệt hiện hành. Không chạy lại `park-meihua-layers.py`,không lặp markerPDF. Tiếp thân216trường,mệnh đề phụ,bảng720ô và nhân chứng độc lập;toàn sách/toàn kho chưa hoàn tất.\n',encoding='utf-8')
print('State updated:consumer layers integrated;source/catalogue work remains active-not-complete.')
