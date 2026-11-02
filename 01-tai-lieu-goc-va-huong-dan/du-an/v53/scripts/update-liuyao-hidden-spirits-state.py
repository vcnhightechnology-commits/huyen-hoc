from pathlib import Path
import json
root=Path(__file__).resolve().parent.parent;workspace=root.parent;base=root/'research/liuyao-hidden-spirits'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='LIUYAO_HIDDEN_SPIRITS_REPORT.md'
step=('B02mục lụcPDF13–19đăng ký135đơn vị(130số+5mục phụ);127mục vẫn mức đề mục. Đọc lần đầu toànchương28trongPDF108–116,ghi vị trí PhiPhục/11câu điều kiện vàkhác phươngpháp. '
 'Tham chiếu riêng320truy vấn/384vị trí,144trùng chi hiện,56thiếu Lục thân hiện;14kiểm/649lời gọiHHCthật,sáu ca nguồn. Để tiền đề thiếu là chưa biết,giữ khớp hữu/vô dụng đồng thời;không tự chọn Dụng thần. '
 '21render mới+1mục lục mở rộng,0HTTP/PDFgốc mới;HTML707411byte/site/ZIPweb vàthamchiếu nền tảng giữ byte. Tiếp DụngNguyênKỵThù,NhậtNguyệt/vượngsuy/tuầnkhông vàranhlịch,thân các mục/nhânchứngB03;toànkho chưa xong.')
d=read(workspace/'EXHAUSTIVE_WORK_STATE.json');d['date']='2026-10-27';d['currentWork'].update(currentStep=step,latestResearchReport='v53/'+report,
 sourceDirectory='v53/research/liuyao-hidden-spirits',internalHiddenReference='v53/research/liuyao-hidden-spirits/hidden-reference.mjs',
 currentTOC='v53/research/liuyao-hidden-spirits/B02_TOC_UNITS.json',functionalBacklog='v53/research/liuyao-hidden-spirits/WORK_STATE.json')
d['inProgressScope']='v53/research/liuyao-hidden-spirits/WORK_STATE.json'
d['subsequentPriority'][0]='B02fullTOCregistered135units;chapter28first-passreadandprivatecandidate/11clausereferencecomplete. Continue complete use-god/opposing-god/day/month/strength/void/calendar-boundary premises and127heading-onlybodyunits;locate B03parallelchapter. Do not auto-select a useful god from placement.'
for p in [workspace/'EXHAUSTIVE_WORK_STATE.json',root/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
write(base/'WORK_STATE.json',{'schema':'hhc.liuyao.hidden-work-state.v1','date':'2026-10-27','status':'private-reference-complete-calendar-and-full-study-active',
 'catalogueID':'B02','latestReport':'v53/'+report,'tocUnits':135,'headingOnlyUnits':127,'firstPassChapterRead':28,'chapterPDFSpan':[108,116],
 'completedStep':step,'privateReference':'hidden-reference.mjs','conditionalClauses':11,'automaticUseGodSelection':False,'consumerChanged':False,
 'next':['Fully read use-god/original/opposing/enemy-god and strength clauses,with counterexamples','Complete day/month/void and calendar-boundary premises before automatic condition facts','Locate and collate B03parallel chapter/remaining physical books','Map actual body spans and extract127heading-only B02units','Keep MaiHoa/Bazi/Tuvi/Homeandremainingcataloguebacklogs active'],
 'wholeBookApplied':False,'wholeCatalogueCompleted':False})
p=root/'research/full-study/WORK_STATE.json';d=read(p);d['latestResearchReport']=report;d['exhaustiveNext']='B02chapter28placement/11conditionalclausesand135TOCunitsrecorded. Continue complete use-god/strength/day/month/void/calendarpremises and127heading-onlybodyunits;B03parallelchapteropen. No automatic selection/prediction.'
yi=next(x for x in d['items']if x['id']=='yi');entry='B02PhiPhuc:completefirst-passchapter28span108..116,11conditionalclauseswithunknown-preservinglogic,6sourcecases andprivateoriginal-palacecandidateAPI.14checks/649actualHHChexcalls,320queries/384rootpositions,144coincidences/56missing-kinqueries. FullTOC135entries=130+5supplements,127heading-only;21newrenders+1expandedTOCpage,0HTTP/newPDF,consumerandfoundationbytesunchanged.'
if entry not in yi['completed']:yi['completed'].append(entry)
yi['latestScope']='../liuyao-hidden-spirits/CONDITIONS.json'
yi['remaining']=[s for s in yi['remaining']if not s.startswith('LiuYao:completeactualchaptermapping')]
r='LiuYao:135B02TOCunitsregistered,127heading-onlybodyunitsremain;chapter28first-passread/privateplacementand11clausegraphdoesnotestablishcalendar/strength/use-godselectionoroutcomeaccuracy. CompleteB03parallelchapters/laterbooksandallsourceexceptions.'
if r not in yi['remaining']:yi['remaining'].append(r)
write(p,d)
p=root/'research/library-current/COVERAGE.json';d=read(p);b=next(x for x in d['catalogue']if x['id']=='B02')
b['scope']='Bộ cấu trúc nội bộ cùngPhiPhục/11mệnhđề điều kiện ba giá trị;đọc lần đầu toàn khoảngchương28. Mục lục135đơn vị,127thân mục còn mức đề mục;không tự chọn Dụng thần/chưa toàn sách hoặc công khai.'
b['latestLocalReadingScope']='PDF108–116chương28;135mục mục lục13–19.14kiểm/649lời gọiHHC/320truy vấn/384vị trí;0HTTP/PDFgốc mới.'
for f in ['v53/'+report]+['v53/research/liuyao-hidden-spirits/'+s for s in ['B02_TOC_UNITS.json','MANUAL_READINGS.json','CONDITIONS.json','PLACEMENT_AND_VARIANTS.json','SOURCE_FIXTURES.json','hidden-reference.mjs']]+['v53/qa/liuyao-hidden-spirits/ENGINE_RESULTS.json']:
 if f not in b['currentEvidence']:b['currentEvidence'].append(f)
d['latestFollowup']=report+':B02chapter28firstpass/privateplacement+11clauses,14checks/649actualHHChexcalls/320queries/384positions.135TOCunits/127heading-only,consumerunchanged;wholeworkapplied0.'
d['latestAcquisitionCounts']={'scope':report,'originalPDFs':0,'retainedHTTP200Bodies':0,'newLocalRenders':21,'expandedPriorTOCPage':1,'fullBooksApplied':0}
assert d['counts']['wholeWorkApplied']==0;write(p,d)
note=('Mốc PhiPhục27/10/2026: `'+report+'` đọc lần đầu toàn khoảngchương28/PDF108–116,ghi11mệnhđề điều kiện vàthamchiếu nội bộ320truy vấn/384vị trí;14kiểm/649lời gọiHHCthật. '
 'Mục lụcB02đủ135đơn vị(130số+5phụ),127thân mục vẫn mức đề mục;21render mới+1mục lục mở rộng,0HTTP/PDFgốc mới. Không tự chọn Dụng thần hoặc dự báo;HTML707411byte/site/ZIPweb giữ byte. Tiếp tiền đề DụngNguyênKỵThù,NhậtNguyệt/vượngsuy/tuầnkhông vàranhlịch;toànkho chưa hoàn tất.\n\n')
for p in [workspace/'PROJECT_RESEARCH_STATE.md',root/'NEXT_STEPS.md',root/'research/library-current/COVERAGE.md']:
 s=p.read_text(encoding='utf-8-sig')
 if not s.startswith('Mốc PhiPhục27/10/2026:'):p.write_text(note+s,encoding='utf-8')
print('Chapter28private reference complete;calendar/full study active;no consumer change.')
