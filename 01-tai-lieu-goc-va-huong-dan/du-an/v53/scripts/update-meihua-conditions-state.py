from pathlib import Path
import json

root=Path(__file__).resolve().parent.parent
workspace=root.parent
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='MEIHUA_CONDITIONS_REPORT.md'
step=('Quyển 2 PDF55–98 đã có bản đồ52mục/44trang nội dung;48bản ghi trang gồm38nội dung mới/6mở rộng và4ngoài nội dung. '
      'Bộ tham chiếu nội bộ18chủ đề/85mệnh đề trực tiếp,đồ thị quan hệ,mùa và ngoại ứng rõ tiền đề;14kiểm đạt/384cấu trúc quẻ thật. '
      'Năm khác biệt văn bản/ngữ cảnh còn mở;chưa áp ra web,chưa hết sách. Tiếp đủ mệnh đề quyển1/3và đối chứng hỗ/mùa. '
      'HTML703410byte giữ nguyên;candidateThể–Dụng vẫn0browser/PDF,chưa phát hành.')
state=read(workspace/'EXHAUSTIVE_WORK_STATE.json')
state['currentWork'].update(currentStep=step,latestResearchReport='v53/'+report,
                           latestPageNavigation='v53/research/meihua-conditions/UNIT_MAP.json',
                           internalConditionalCompiler='v53/research/meihua-conditions/conditions-reference.mjs')
assert state['status']=='active-not-complete'
for p in [workspace/'EXHAUSTIVE_WORK_STATE.json',root/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,state)
full=read(root/'research/full-study/WORK_STATE.json')
full['latestResearchReport']=report
full['exhaustiveNext']='Continuephysicalvolumes1/3fullconditionalclausecoverage,thenindependentwitnessfornuclear-main/changedcontext,seasonboundaries/priorityandmidday兌conflict. Volume2roles/85directclausesareinternalreference,notcompleteallsubsidiaryrulesorvalidatedpredictions. PendingUIstillrequiresactualbrowser/PDFchecksafterapprovalreviewavailable.'
yi=next(x for x in full['items']if x['id']=='yi')
entry='MaiHoa conditions:48boundedpagerecords(44content,38new/6expanded),52physicalunitlinks,18domains/85directrelationclauses;internalvalidatedcastgraphwith1920nodes/4710edgesfrom384realstructures,10seasoncells/12branchanchors,6Bĩcases,5text/contextvariants.14checks;notconsumerintegrated/notpredictivevalidation.'
if entry not in yi['completed']:yi['completed'].append(entry)
yi['latestScope']='../meihua-conditions/MANUAL_READINGS.json'
rem='Volume2pagecoverage55–98/52unitsand18roles/85directclausesarenowinternalreference. Fullsubsidiaryclauses,volumes1/3,independentvariantsandseasoncalendarpremisesremainopen;do notclaimwholebookapplication.'
if rem not in yi['remaining']:yi['remaining'].append(rem)
write(root/'research/full-study/WORK_STATE.json',full)

p=root/'research/meihua-reading/FUNCTIONAL_BACKLOG.json';d=read(p)
for g in d['groups']:
 if g['id']=='eighteen-subject-domains':
  g.update(status='18-role-premises-and85direct-clauses-internal-compiler-tested',
           remainingOrScope='PhysicalPDF63–74collatedfor18rolesand85directrelationclauses;weatherdoesnotdividebody/use.14scopechecks/384realgraphs. Allsubsidiarytables/timing/observerexceptionsnotfullyextracted;notconsumerprediction.',
           evidence='../meihua-conditions/DOMAIN_RULES.json')
 if g['id']=='body-use-multiple-relations':
  g.update(status='internal-qualitative-graph-tested-conditional-priority-open',
           remainingOrScope='Main/mutualside/changedusegraphkeepsbodyreference;controllerofsupporter/controllerqualifiersfromPDF89,noalgebraiccancellation/score.384actualcasts;Bĩcase2changednuclear37versusmain53keptasvariant.',
           evidence='../meihua-conditions/conditions-reference.mjs')
 if g['id']=='seasonal-conditions':
  g.update(status='internal-explicit-season-branch-evidence-priority-open',
           remainingOrScope='Fiveboundedseasonstrong/oppressedpairs(10cells)and12branchanchorsreadPDF60/84/85/90;month/daykeptseparate,noboundaryorpriorityinferred. Appendix20cells204remainsdistinct.',
           currentEvidence='../meihua-conditions/SEASON_PREMISES.json')
 if g['id']=='external-responses':
  g['currentEvidence']='../meihua-conditions/MANUAL_READINGS.json'
  g['remainingOrScope']='ElevenprintedresponsegroupsPDF83–88mapped;quietroom93hasnoexternals. Internalcompilerrequiresmanualobserveddescription/trigram,nosensorsortextautoclassification. Fullsymbol/timingrulesandmidday兌conflictremainopen.'
write(p,d)

p=root/'research/meihua/SCAN_STRUCTURE.json';d=read(p)
v=next(v for v in d['volumes']if v['volume']==2)
v.update(titlePDFPage=55,endPDFPage=98,lastPrintedPage=44,
         currentCoverage='All44printedcontentpages55–98visuallymappedto52digitalunits;18roles/85directrelationclausesandboundedseason/interactionpremisescompiledinternally. Fullsubsidiaryclausesremainopen. See../meihua-conditions/UNIT_MAP.json.')
d['physicalLowerBookCoverPDFPage']=102
d['excludedBetweenVolumes2and3']={'advertisements':[99,100],'logo':[101],'lowerBookCover':[102]}
d['nextRequirement']='Continuevolumes1/3fullconditionalclausesandindependentvariants. Volume2fullsubsidiaryrulesandvolumes4/5clausetranscriptionsnotcomplete;noautomaticcalendarpriorityorvalidatedpredictions.'
write(p,d)

p=root/'research/library-current/COVERAGE.json';d=read(p);b=next(x for x in d['catalogue']if x['id']=='B01')
b['latestLocalReadingScope']='Quyển2:48bảnghitrang/44nộidung,38mới/6mởrộng,52mụcảnh;18chủđề/85mệnhđềtrựctiếp.14kiểmthamchiếu,384quẻthật;chưathànhdựbáo/nghiệmvụweb. Quyển4/5giữbảnđồ84trang93nhómtrước.'
for f in ['v53/'+report,'v53/research/meihua-conditions/DOMAIN_RULES.json','v53/research/meihua-conditions/VARIANTS_AND_GAPS.json','v53/research/meihua-conditions/conditions-reference.mjs']:
 if f not in b['currentEvidence']:b['currentEvidence'].append(f)
b['scope']='Tám cách Mai Hoa đang phát hành;đã thêm bộ tham chiếu điều kiện nội bộ18chủ đề và quan hệ nhiều lớp,chưa tích hợp giao diện. Mệnh đề phụ,quyển1/3,dị bản và tiền đề mùa còn mở;toàn sách chưa áp hết.'
d['latestFollowup']=report+':14source/runtimechecks;48boundedpagerecords;28newlocalPNGderivatives/0HTTP. Productbytesunchanged;wholeworkapplied0.'
assert d['counts']['wholeWorkApplied']==0
write(p,d)

note=('Mốc điều kiện Mai Hoa26/10/2026: `'+report+'` đọc48trang/44nội dung quyển2(38mới/6mởrộng),nối52mục ảnh. '
      'Bộ tham chiếu nội bộ18chủđề/85mệnhđề trực tiếp và đồ thị quan hệ có điều kiện đạt14kiểm/384quẻ thật;10ô mùa/12mốc chi,6ca Bĩ và5khác biệt giữ riêng. '
      'Không áp kết luận dự báo ra web hoặc nhận đã hết mệnh đề phụ/toàn sách. Quyển2kếtPDF98,in44;99–100quảngcáo/101logo/102bìa下冊. '
      'HTML703410byte/SHA380016… giữ nguyên;candidateThể–Dụng vẫn0browser/PDF,chưa phát hành. Tiếp quyển1/3và nhânchứng/ranhlịch còn mở.\n\n')
for p in [workspace/'PROJECT_RESEARCH_STATE.md',root/'NEXT_STEPS.md']:
 s=p.read_text(encoding='utf-8-sig')
 if not s.startswith('Mốc điều kiện Mai Hoa'):p.write_text(note+s,encoding='utf-8')
p=root/'research/library-current/COVERAGE.md';s=p.read_text(encoding='utf-8-sig')
if not s.startswith('Mốc điều kiện Mai Hoa'):p.write_text('Mốc điều kiện Mai Hoa: xem `../../'+report+'`;18vai trò/85mệnh đề và384quẻ tham chiếu là tiến độ nội bộ,còn quy tắc phụ/dịbản/ranh lịch. Toàn kho chưa hoàn tất.\n\n'+s,encoding='utf-8')
print('Updated internal conditional work state;consumer product and historical snapshots retained.')
