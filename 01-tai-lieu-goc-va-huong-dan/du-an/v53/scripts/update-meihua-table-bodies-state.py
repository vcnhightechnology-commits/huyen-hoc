from pathlib import Path
import json
root=Path(__file__).resolve().parent.parent;workspace=root.parent
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='MEIHUA_TABLE_BODIES_REPORT.md'
step=('Thân216trường/támquái đã đối ảnh PDF33–54:214bản đọc chuẩn hóa không chữ mở,2trường còn một chữ khó;131chuỗi trùng,81khác (gồm dạng chữ/thứ tự),2mục bảnsốthiếu,2chữ mở. '
 '96liên hệ biểu tượng/8thời tự/16tên-số/96lời đoán lịch sử phân loại riêng;không áp lời đoán hoặc suy quy tắc lịch.14kiểm đạt,384cấu trúc engine/2688phép nối/tám ca phương vị. '
 'KhôngHTTP/trang mới;22đọc mở rộng,7render300dpi/12vùng chữQA. HTML707411byte/site/ZIPweb giữ nguyên bản bốn lớp đã hoàn tất98kiểm/PDF4trang. '
 'Tiếp hai chữ/dịbản và mọi mệnh đề phụ5quyển,720nhãn bảng giờ/tiền đề đầu vào,nhân chứng/ranh lịch độc lập;toàn kho chưa hoàn tất.')
p=workspace/'EXHAUSTIVE_WORK_STATE.json';d=read(p);assert d['status']=='active-not-complete';d['date']='2026-10-27'
d['currentWork'].update(currentStep=step,latestResearchReport='v53/'+report,internalTableReference='v53/research/meihua-table-bodies/table-reference.mjs')
for p in [workspace/'EXHAUSTIVE_WORK_STATE.json',root/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=root/'research/full-study/WORK_STATE.json';d=read(p);d['latestResearchReport']=report
d['exhaustiveNext']='All216symbol-tablebodypositions now have normalized readings/dispositions:214clear and2glyph-open. Continue those2glyphs/independent variants and all subsidiary clauses/720hour labels with actual input premises;do not repeat completed navigation/table headers. Four-layer consumer UI already released.'
yi=next(x for x in d['items']if x['id']=='yi')
entry='MaiHoa symbol-tablebodies:216positions/27fields each across8trigrams,214clear normalizedreadings+2glyph-open;131same/81different/2digitalomissions/2glyph-open.96symbol/8time/16name-number/96historicalforecast dispositions.14checks,384engine structures/2688joins+8directioncases.22expandedpages/7nativeQA renders/12crops,0HTTP/newpages;HTML/site/webZIP unchanged.'
if entry not in yi['completed']:yi['completed'].append(entry)
yi['latestScope']='../meihua-table-bodies/BODY_COLLATION.json'
yi['remaining']=[s for s in yi['remaining']if not s.startswith(('FiveMaiHoavolumeshave','FiveMaiHoa','Fivevolumes','Fivenavigationmaps','Expanded castingmethods are live and checked;four-layer'))]
remaining='All216table bodies now have first-pass normalized readings/dispositions,2glyphs remain open. Complete independent textual witness collation,semantic premises and every subsidiary clause of5volumes;96historical forecast fields are not established predictions.720hour labels/input semantics remain open.'
if remaining not in yi['remaining']:yi['remaining'].append(remaining)
write(p,d)
p=root/'research/meihua-reading/FUNCTIONAL_BACKLOG.json';d=read(p);g=next(x for x in d['groups']if x['id']=='object-symbol-tables')
g.update(status='216body-positions-compared-214clear-2glyph-open-not-fully-critical',remainingOrScope='All216body positions read/compared with explicit dispositions;214clear normalized readings,2glyph-open.131same/81different/2digitalomissions/2glyph-open;orthography included. Independent witness/semantic premises remain open;96forecast fields not empirically established.',latestPhysicalScope='../meihua-table-bodies/BODY_COLLATION.json',internalReference='../meihua-table-bodies/table-reference.mjs')
write(p,d)
p=root/'research/meihua/SCAN_STRUCTURE.json';d=read(p);v=next(x for x in d['volumes']if x['volume']==1)
v['currentCoverage']='42boundedpage records/45units,64printedpalace members. All216symbol-tablebody positions now read/compared in separate BODY_COLLATION:214clear+2glyph-open;131same/81different/2digitalomissions/2glyph-open. Not a critical edition or all subsidiary clauses.'
v['latestBodyCollation']='../meihua-table-bodies/BODY_COLLATION.json';d['nextRequirement']='Complete2glyph-open table fields/independent variants and all subsidiary clauses/720hour table labels with input premises;no repeat of finished page navigation or tableheaders.';write(p,d)
p=root/'research/library-current/COVERAGE.json';d=read(p);d['date']='2026-10-27';b=next(x for x in d['catalogue']if x['id']=='B01')
b['latestLocalReadingScope']='216thân trường đối ảnh/214rõ+2chữ mở;131trùng/81khác chuỗi/2thiếu bảnsố/2chữ mở. 22trang đọc mở rộng,0HTTP/trang mới;14kiểm/384cấu trúc thật. Không đồng nghĩa áp hết lời đoán/tác phẩm.'
b['scope']='Tám cách và bốn lớp Thể–Dụng đang phát hành;tham chiếu riêng quyển2/3,64nhóm quẻ và216thân trường vật tượng quyển1. Hai chữ/dị bản,mệnh đề phụ5quyển,bảng720ô/ranh lịch/nhân chứng vẫn mở;toàn sách chưa áp hết.'
for f in ['v53/'+report,'v53/research/meihua-table-bodies/BODY_COLLATION.json','v53/research/meihua-table-bodies/VARIANTS_AND_LIMITS.json','v53/research/meihua-table-bodies/table-reference.mjs']:
 if f not in b['currentEvidence']:b['currentEvidence'].append(f)
d['latestFollowup']=report+':216body positions/214clear+2glyph-open,14checks/384structures/2688joins+8directioncases,0HTTP/newpages. Productbytes unchanged;wholeworkapplied0.'
assert d['counts']['wholeWorkApplied']==0;write(p,d)
note=('Mốc thân bảng27/10/2026: `'+report+'` đối ảnh216vị trí/214bản đọc chuẩn hóa rõ+2chữ mở;131trùng/81khác/2thiếu bảnsố/2chữ mở. 14kiểm,384cấu trúc thật/2688phép nối+tám ca phương vị. '
 '22trang là đọc mở rộng,khôngHTTP/trang mới;7renderQA/12vùng chữ. HTML707411byte/site/ZIPweb giữ bản bốn lớp98kiểm/PDF4trang;candidate đã hoàn tất,không còn chờ duyệt. '
 'Tiếp hai chữ/dịbản,mệnh đề phụ/bảng720ô/tiền đề lịch;toàn kho chưa hoàn tất.\n\n')
for p in [workspace/'PROJECT_RESEARCH_STATE.md',root/'NEXT_STEPS.md',root/'research/library-current/COVERAGE.md']:
 s=p.read_text(encoding='utf-8-sig')
 if not s.startswith('Mốc thân bảng27/10/2026:'):p.write_text(note+s,encoding='utf-8')
print('State updated:216body dispositions,2glyphs and wider source scope remain open.')
