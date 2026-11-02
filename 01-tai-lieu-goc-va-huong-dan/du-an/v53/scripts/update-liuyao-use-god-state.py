from pathlib import Path
import json
root=Path(__file__).resolve().parent.parent;workspace=root.parent;base=root/'research/liuyao-use-god'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='LIUYAO_USE_GOD_REPORT.md'
step=('B02đọc lần đầu toàn khoảng5chương8–12/PDF48–56;tham chiếu15nhóm đối tượng,năm bảng vai trò và23câu điều kiện Nguyên/Kỵ. '
 '14kiểm/392lời gọiHHCthật,384đồthị/2304gán hào/5040cạnh;bốn ví dụ vàmột lá sốlunar thật kiểm ngàyTânMão thuộcGiápThân/khôngNgọMùi. '
 'PDF52ngàyTânMão vàlời khôngDầnMão giữ mâu thuẫn mở;5→6động1/3/4/6,28→50động5/6. Tiềnđề thiếu là chưa biết,không tự chọn Dụng/thangđiểm/dựbáo. '
 '13render mới/2crop,0HTTP/PDFgốc mới;HTML707411byte/site/ZIPweb vàhai thamchiếu trước giữ byte. Mục lục135đơn vị,còn122thân mục mức đề mục. Tiếpchương13–17/lịch/tuầnkhông,mộ,tuyệt/B03;toànkho chưa xong.')
d=read(workspace/'EXHAUSTIVE_WORK_STATE.json');d['date']='2026-10-27';d['currentWork'].update(currentStep=step,latestResearchReport='v53/'+report,
 sourceDirectory='v53/research/liuyao-use-god',internalUseGodReference='v53/research/liuyao-use-god/use-god-reference.mjs',
 currentTOC='v53/research/liuyao-use-god/B02_CURRENT_UNITS.json',functionalBacklog='v53/research/liuyao-use-god/WORK_STATE.json')
d['inProgressScope']='v53/research/liuyao-use-god/WORK_STATE.json'
d['subsequentPriority'][0]='B02chapters8..12and28first-passread/privateconditionreferencescomplete;122heading-onlybodyunitsremain. Continue chapters13..17andvoid/tomb/extinction/calendarboundarypremises;collateB03andPDF52date/voidconflict. No automaticuse-godselection/forecast.'
for p in [workspace/'EXHAUSTIVE_WORK_STATE.json',root/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
write(base/'WORK_STATE.json',{'schema':'hhc.liuyao.use-god-work-state.v1','date':'2026-10-27','status':'private-reference-complete-full-conditions-and-calendar-active',
 'catalogueID':'B02','latestReport':'v53/'+report,'currentUnits':'B02_CURRENT_UNITS.json','tocUnits':135,'headingOnlyUnits':122,
 'firstPassChapterRead':[8,9,10,11,12],'chapterPDFSpan':[48,56],'completedStep':step,'privateReference':'use-god-reference.mjs',
 'conditionalClauses':23,'sourceDateVoidConflicts':1,'automaticUseGodSelection':False,'calendarStrengthClassifier':False,'consumerChanged':False,
 'next':['Chapters13..17completeconditionalcases/day-monthstrengthandboundaries','Void/tomb/extinctionandchanged-linephaseswithnamedmethod','B03parallelchapter/laterbooksandPDF52date-voidwitness','Remaining122heading-onlyB02unitsandothercataloguebranches'],
 'wholeBookApplied':False,'wholeCatalogueCompleted':False})
p=root/'research/full-study/WORK_STATE.json';d=read(p);d['latestResearchReport']=report;d['exhaustiveNext']='B02chapters8..12private15subject/5role/23conditionreferencecomplete,122heading-onlybodyunitsremain. Continue13..17andcalendar/strength/void/tomb/extinctionpremises;B03parallelchapter/PDF52date-voidconflictopen. No automaticselection/forecast.'
yi=next(x for x in d['items']if x['id']=='yi');entry='B02use-godchapters8..12first-passreadPDF48..56:15exactsubjectcategories,5elementroletables,23conditionalclauses/21explicitpremises,private384graphs/2304linebindings/5040edges.14checks/392actualHHChexcalls+1realreferencechart;4sourcefiguresand辛卯-vs-voidproseconflictretained.13newrenders/2crops,0HTTP/PDF;consumerandtwoearlierreferencesunchanged.122heading-onlyTOCunitsremain,noautomaticselection/prediction.'
if entry not in yi['completed']:yi['completed'].append(entry)
yi['latestScope']='../liuyao-use-god/CONDITIONS.json'
yi['remaining']=[s for s in yi['remaining']if not s.startswith('LiuYao:135B02TOCunitsregistered')]
r='LiuYao:B02chapters8..12and28first-passread/privateconditionsonly;122heading-onlybodyunitsremain.Complete13..17andcalendar/strength/void/tomb/extinctionpremises,B03parallelchapters/laterbooks,sourceexceptionsandPDF52date-voidconflict. No automaticuse-godselectionoroutcomeaccuracyestablished.'
if r not in yi['remaining']:yi['remaining'].append(r)
write(p,d)
p=root/'research/library-current/COVERAGE.json';d=read(p);b=next(x for x in d['catalogue']if x['id']=='B02')
b['scope']='Bộ nội bộ cấu trúc/PhiPhục/11câu vàDụngNguyênKỵThù/23câu;đọc lần đầu toàn khoảngchương8–12,28.135đơnvị mục lục,còn122thân mục mức đề mục;không tự chọn Dụng/vượngsuy/dựbáo,chưa toàn sách hoặc công khai.'
b['latestLocalReadingScope']='PDF48–56chương8–12,14kiểm/392HHC+1lunar thật,384đồ thị;PDF52ngày/tuầnkhông giữ mâu thuẫn mở;0HTTP/PDFgốc mới.'
for f in ['v53/'+report]+['v53/research/liuyao-use-god/'+s for s in ['B02_CURRENT_UNITS.json','MANUAL_READINGS.json','CONDITIONS.json','SUBJECTS_AND_ROLES.json','SOURCE_FIXTURES.json','VARIANTS_AND_LIMITS.json','use-god-reference.mjs']]+['v53/qa/liuyao-use-god/ENGINE_RESULTS.json']:
 if f not in b['currentEvidence']:b['currentEvidence'].append(f)
d['latestFollowup']=report+':B02chapters8..12private15subjects/5roles/23clauses,14checks/392actualHHChexcalls+1reference/384graphs;122heading-onlyunitsremain,consumerunchanged,wholeworkapplied0.'
d['latestAcquisitionCounts']={'scope':report,'originalPDFs':0,'retainedHTTP200Bodies':0,'newLocalRenders':13,'qaCrops':2,'fullBooksApplied':0};assert d['counts']['wholeWorkApplied']==0;write(p,d)
note=('Mốc DụngNguyênKỵ27/10/2026: `'+report+'` đọc lần đầu toàn khoảngchương8–12/PDF48–56,thamchiếu15nhóm đối tượng/năm bảng vai trò/23câu điều kiện. '
 '14kiểm/392HHC+1lunar thật,384đồ thị/2304gán hào/5040cạnh. PDF52ngàyTânMão/lời tuầnkhông giữ mâu thuẫn mở;không tự sửa ngày. '
 '13render/2crop mới,0HTTP/PDFgốc;HTML707411byte/site/ZIPweb giữ byte. Mục lục135đơn vị,còn122thân mục mức đề mục;tiếp13–17,tiềnđề lịch/vượngsuy/tuầnkhông/mộ/tuyệt vàB03. Toànkho chưa hoàn tất.\n\n')
for p in [workspace/'PROJECT_RESEARCH_STATE.md',root/'NEXT_STEPS.md',root/'research/library-current/COVERAGE.md']:
 s=p.read_text(encoding='utf-8-sig')
 if s.startswith('Mốc DụngNguyênKỵ27/10/2026:'):p.write_text(note+s.split('\n\n',1)[1],encoding='utf-8')
 else:p.write_text(note+s,encoding='utf-8')
print('Chapters8..12private reference complete;122heading-onlyunits remain;consumerunchanged.')
