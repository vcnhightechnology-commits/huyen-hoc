from pathlib import Path
import json
root=Path(__file__).resolve().parent.parent;workspace=root.parent
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='MEIHUA_EXTERNAL_REPORT.md'
step=('Quyển3PDF103–144đã đọc liên tục42trang có giới hạn(41nội dung,27mới/14mởrộng+1kết),26mục ảnh. '
      '13đối chiếu vật thực/hình tượng,động/tĩnh tách tiền đề vàvai trò địa phương có bộ tham chiếu nội bộ;11kiểm/104cặp quẻ-bối cảnh/12tổ hợp động tĩnh đạt. '
      'Hai ví dụ11.1→46và50.6→32đúng engine;giảthuyết50→32haihào bịbácbỏ. Bảy vấnđề văn bản/ngữcảnh cònmở,khôngtựđổi vai trò chung. '
      'Tiếp đủ vị trí/điều kiện quyển1rồi mệnhđề phụ2/3và bảng4/5. HTML703410byte/site/webZIPgiữnguyên;candidateThể–Dụng vẫnchưaUI/PDF,chưapháthành.')
state=read(workspace/'EXHAUSTIVE_WORK_STATE.json');assert state['status']=='active-not-complete'
state['date']='2026-10-27';state['currentWork'].update(currentStep=step,latestResearchReport='v53/'+report,
 latestPageNavigation='v53/research/meihua-external/UNIT_MAP.json',internalExternalReference='v53/research/meihua-external/external-reference.mjs')
for p in [workspace/'EXHAUSTIVE_WORK_STATE.json',root/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,state)
full=read(root/'research/full-study/WORK_STATE.json');full['latestResearchReport']=report
full['date']='2026-10-27';full['exhaustiveNext']='Completevolume1physicalnavigationandconditionalclauses,thenallsubsidiaryrules2/3andtablefields4/5. Volume3boundedreadingisnotfulltranscription. Material/motionreferenceisprivate,noempiricalweights. Actualengineconfirms50.6→32,rejectingprovisionaltwo-linehypothesis. PendingUIrequiresactualapprovedbrowser/PDFvalidation.'
yi=next(i for i in full['items']if i['id']=='yi')
entry='MaiHoa volume3:42boundedpages/41content(27new/14expanded+1endleaf),26physicalunitlinks;13materialcontrasts,12motioncontexts,4separaterolepolicies and10namedresponses.11checks/104actualcastcontexts;11.1→46and50.6→32confirmed.7text/contextissuesopen;no consumerchange orvalidatedprediction.'
yi['completed']=[s for s in yi['completed']if not s.startswith('MaiHoa volume3:42boundedpages/')]
yi['completed'].append(entry)
yi['latestScope']='../meihua-external/MANUAL_READINGS.json'
remain='Volume3page/unitnavigationcomplete103–144butfulltable-field/clausecollationopen;source-specificmaterial/motionqualifiersareinternal,notfinishedprognosticclassifier. Completevolume1navigation,allsubsidiaryclauses2/3andtables4/5.'
if remain not in yi['remaining']:yi['remaining'].append(remain)
write(root/'research/full-study/WORK_STATE.json',full)

p=root/'research/meihua-reading/FUNCTIONAL_BACKLOG.json';d=read(p)
for g in d['groups']:
 if g['id']=='external-responses':g.update(status='internal-material-motion-premises-tested-full-rules-open',
  remainingOrScope='Volume3continuous42pagerecords/26units,13materialcontrasts and12motioncontexts;manualcase/trigram/observationsrequired.104actualcastcontexts/11checks;nostrengthweights/eventdates. Tenvol3namesdistinctfromelevenvol2groups;fullsymbols/selection/priorityopen.',
  currentEvidence='../meihua-external/CONTEXT_PREMISES.json')
 if g['id']=='object-symbol-tables':g['latestPhysicalScope']='../meihua-external/MANUAL_READINGS.json';g['remainingOrScope']='214digitalfieldsstillnotallphysicallycollated. Volume3tables133–143visuallynavigatedwithboundednotes;notfullfieldtranscription. Localobjectrolepolicies126–127keptdistinct.'
write(p,d)
p=root/'research/meihua/SCAN_STRUCTURE.json';d=read(p);v=next(v for v in d['volumes']if v['volume']==3)
v.update(titlePDFPage=103,lastContentPDFPage=143,endleafPDFPage=144,lastPrintedPage=42,
 currentCoverage='Continuous42boundedpagerecords/41content(27new/14expanded+1endleaf),26pinneddigitalunits.13materialcontrasts andmotion/localrolepremises compiledprivately;notfullclause/tabletranscription. See../meihua-external/UNIT_MAP.json.')
d['nextRequirement']='Completevolume1navigationandconditionalclauses;thenremainingvolume2/3subsidiaryrulesand4/5tablefields. Noautomaticmaterialclassification,calendarpriorityorvalidatedpredictions.'
write(p,d)
p=root/'research/library-current/COVERAGE.json';d=read(p);b=next(b for b in d['catalogue']if b['id']=='B01')
b['latestLocalReadingScope']='Quyển3:42bảnghitrang/41nộidung,27mới/14mởrộng+1kết,26mụcảnh;13đốichiếuvậtthựchìnhtượng,12tổhợpđộngtĩnh.11kiểm/104cặpquẻ-bốicảnh;2vídụinđúngengine. Chưađủphiênâm/từngtrườngbảng/toànsách.'
for f in ['v53/'+report,'v53/research/meihua-external/CONTEXT_PREMISES.json','v53/research/meihua-external/WORKED_EXAMPLES.json','v53/research/meihua-external/external-reference.mjs']:
 if f not in b['currentEvidence']:b['currentEvidence'].append(f)
b['scope']='Tám cách Mai Hoa đang phát hành;tham chiếu nội bộ quyển2/3về chủđề,mùa,quan hệ,vật tượng vàđộngtĩnh. Khôngtựđổi vai trò chung hoặcáp dự báo đã kiểm nghiệm. Quyển1vàmọi mệnhđề phụ/bảng/dịbản còn mở;toàn sách chưa áp hết.'
d['latestFollowup']=report+':11source/runtimechecks;42boundedpages/0newHTTP/0renders;13materialcontrasts/104actualcastcontexts/12motioncontexts. Productbytesunchanged;wholeworkapplied0.'
assert d['counts']['wholeWorkApplied']==0;write(p,d)
note=('Mốc ngoại ứng Mai Hoa27/10/2026: `'+report+'` đọc42trang quyển3(41nội dung,27mới/14mởrộng+1kết),26mụcảnh. '
 '13đối chiếu vật thực/hình tượng,động/tĩnh vàvai trò địa phương có thamchiếu nộibộ đạt11kiểm/104cặpquẻ-bốicảnh/12tổhợpđộngtĩnh. '
 '11.1→46và50.6→32đúngengine;giảthuyết50→32haihàođãbịbácbỏ. Bảyvấnđềvănbản/ngữcảnhvẫnmở. '
 'HTML703410byte/site/webZIPgiữbyte;candidateThể–DụngvẫnchưakiểmUI/PDF,chưapháthành. Tiếpquyển1vàmọimệnhđềphụ/bảngcònmở;toànkhochưahoàntất.\n\n')
for p in [workspace/'PROJECT_RESEARCH_STATE.md',root/'NEXT_STEPS.md']:
 s=p.read_text(encoding='utf-8-sig')
 if s.startswith('Mốc ngoại ứng Mai Hoa27'):s=s.split('\n\n',1)[1]
 p.write_text(note+s,encoding='utf-8')
p=root/'research/library-current/COVERAGE.md';s=p.read_text(encoding='utf-8-sig')
if not s.startswith('Mốc ngoại ứng Mai Hoa27'):p.write_text('Mốc ngoại ứng Mai Hoa27/10/2026: xem `../../'+report+'`;42bảnghitrang/13mệnhđề và11kiểm làtiếnđộnộibộ,khôngphảihếtsáchhoặcđộđúngtiênđoán.\n\n'+s,encoding='utf-8')
print('Internalstate updated;allfourdirections andwholecatalogue remainactive-not-complete.')
