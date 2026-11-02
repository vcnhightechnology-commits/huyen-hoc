from pathlib import Path
import json

root=Path(__file__).resolve().parent.parent
workspace=root.parent
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

new='MEIHUA_VOLUME_MAP_REPORT.md'
step=('Đã thêm47bản ghi ảnh có giới hạn, nối bản đồ vị trí toàn84trang quyển4/5(82nội dung+2kết);'
      '93nhóm/đơn vị,60khóa bảng giờ,9kiểm nguồn/runtime đạt. Chưa chép hết mệnh đề/720ô giờ hoặc áp hết sách. '
      'Tiếp điều kiện đầy đủ quyển1–3 và ngữ nghĩa bảng/quan sát;HTML703410byte giữ nguyên. '
      'CandidateThể–Dụng còn14kiểm phép tính,0browser/PDF,chưa phát hành;không vượt cơ chế duyệt.')
state=read(workspace/'EXHAUSTIVE_WORK_STATE.json')
state['currentWork'].update(currentStep=step,latestResearchReport='v53/'+new,
                           latestPageNavigation='v53/research/meihua-volume-map/UNIT_MAP.json')
assert state['status']=='active-not-complete'
for p in [workspace/'EXHAUSTIVE_WORK_STATE.json',root/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,state)

full=read(root/'research/full-study/WORK_STATE.json')
full['latestResearchReport']=new
full['exhaustiveNext']='Read complete physical-volume1–3conditional units and premises (body/use/mutual/change,18domains,season/threeessentials/tenresponses);then table207–212cells/inputsemantics and remainingglyphvariants. Do not repeat pageheadingcounts as completedclausework. PendingBody/UseUI stillrequires approvalreviewavailable andactualbrowser/PDFchecks.'
yi=next(x for x in full['items'] if x['id']=='yi')
entry='MaiHoa volume4/5page navigation:47new boundedreadings plus retainedrecords cover84pages/82content,93unitgroups,60hourtablerowkeys;720cellpositionsnottranscribed.9source/runtimechecks;9actualenginecontrols. No consumerchange orvalidatedoutcomepredictions;fullbookopen.'
if entry not in yi['completed']:yi['completed'].append(entry)
yi['latestScope']='../meihua-volume-map/MANUAL_READINGS.json'
yi['remaining']=[x for x in yi['remaining'] if '150–178' not in x]
rem='Printedvolumes4/5nowhavecontinuouspagenavigation,notfullclausetranscription. Continueconditionalunits ofvolumes1–3,720hourtablecells/inputsemantics andglyphobserverpremises;93unitlabelsarenot93completedalgorithms.'
if rem not in yi['remaining']:yi['remaining'].append(rem)
write(root/'research/full-study/WORK_STATE.json',full)

p=root/'research/meihua-reading/FUNCTIONAL_BACKLOG.json';d=read(p)
for r in d['groups']:
 if r['id']=='volume-four-five':
  r.update(status='page-navigation-complete-clause-and-premise-work-open',
           remainingOrScope='47newrecordscomplete84page navigation(82content/2endleaves),93boundedgroups. Fullclauses,groupedsubheadings,variantsandquestion/handwritingpremisesremainopen;notwholebookapplied.',
           evidence='../meihua-volume-map/UNIT_MAP.json')
for r in [{'id':'appendix-hour-table','status':'60-row-keys-indexed-cells-and-semantics-open',
           'remainingOrScope':'PDF207–212has60rowkeys/720labelpositions;0literalcelltranscriptioninlatestscope. Do notinterpolateassumedcycle;needvariantreadings,inputscopeandcomparisonwitness.',
           'evidence':'../meihua-volume-map/HOUR_TABLE_INDEX.json'},
          {'id':'glyph-question-and-form','status':'source-premises-and-negative-controls-recorded',
           'remainingOrScope':'Typedtextdoesnotprovidewritingorder,relativeform,brushweight,actualsound/sightorquestioncontext;glyph用神/六神areseparatefromMaiHoa/Bazi/cyclicsystems. Historicallifespan/pregnancy/medicalclaimsnotconsumerprediction.',
           'evidence':'../meihua-volume-map/BOUNDED_EXTRACTS.json'}]:
 if not any(x['id']==r['id'] for x in d['groups']):d['groups'].append(r)
write(p,d)

p=root/'research/meihua/SCAN_STRUCTURE.json';d=read(p)
d['status']='five-volume-witness-identified-volume4-5-page-navigation-complete-clauses-open'
for r in d['volumes']:
 if r['volume'] in [4,5]:
  r['currentCoverage']='Continuouspage/unitnavigationthroughallprintedpages,withboundedpremisereadings;notfullclausetranscriptionorcompletedglyphclassifier. See../meihua-volume-map/UNIT_MAP.json.'
d['nextRequirement']='Completephysicalvolumes1–3conditionalrules/premises;volumes4/5stillneedfullclause/variantinventoryandhourtablecells/semantics. Pagenavigationisnotwholebookapplication.'
write(p,d)

p=root/'research/library-current/COVERAGE.json';d=read(p);b=next(x for x in d['catalogue'] if x['id']=='B01')
b['latestLocalReadingScope']='Thêm47bản ghi đọc có giới hạn;quyển4/5nay84trang có bản đồ vị trí,82nội dung/2kết,93nhóm/đơn vị. Chưa phải chép đủ mệnh đề hoặc áp hết sách;60khóa bảng giờkhôngphải720ôđãchép.'
b['scope']='Tám lựa chọn Mai Hoa đã phát hành;quyển4/5có bản đồ vị trí đủtrang và các giới hạn hình chữ/câu hỏi. Điều kiện đầy đủ quyển1–3,bảng giờ,nhân chứng/dị bản còn mở. Bản Thể–Dụng mở rộng chưa phát hành.'
for f in ['v53/research/meihua-volume-map/MANUAL_READINGS.json','v53/research/meihua-volume-map/UNIT_MAP.json','v53/research/meihua-volume-map/HOUR_TABLE_INDEX.json','v53/'+new]:
 if f not in b['currentEvidence']:b['currentEvidence'].append(f)
d['latestFollowup']=new+':9source/runtimechecks;47newboundedpagerecords;consumerbytesunchanged. Wholeworkappliedremains0.'
assert d['counts']['wholeWorkApplied']==0
write(p,d)

note=('Mốc đọc quyển4/5 ngày26/10/2026: `'+new+'` thêm47bản ghi ảnh có giới hạn, nối bản đồ vị trí84trang(82nội dung/2kết),93nhóm/đơn vị. '
      '9kiểm nguồn/runtime đạt. Có60khóa hàng bảng giờ207–212;720vị trí nhãn chưa chép/đối chứng đủ. Không nhận bản đồ đề mục là đọc hoặc áp hết sách. '
      'Tiếp điều kiện quyển1–3 và tiền đề bảng/hình chữ. HTML703410byte/SHA380016… cùngJS/CSS/site/ZIPweb giữ nguyên. '
      'CandidateThể–Dụng vẫn chờ kiểmbrowser/PDF,không vượt cơ chế duyệt;toàn kho active-not-complete.\n\n')
for p in [workspace/'PROJECT_RESEARCH_STATE.md',root/'NEXT_STEPS.md']:
 s=p.read_text(encoding='utf-8-sig')
 if not s.startswith('Mốc đọc quyển4/5'):p.write_text(note+s,encoding='utf-8')
p=root/'research/library-current/COVERAGE.md';s=p.read_text(encoding='utf-8-sig')
if not s.startswith('Mốc bản đồ quyển4/5'):p.write_text('Mốc bản đồ quyển4/5: xem `../../'+new+'`;đủ vị trí84trang không đồng nghĩa đủmệnh đề/áp hết tác phẩm. Toàn kho chưa hoàn tất.\n\n'+s,encoding='utf-8')
print('Updated bounded volume-map state;live consumer files and historical reports retained.')
