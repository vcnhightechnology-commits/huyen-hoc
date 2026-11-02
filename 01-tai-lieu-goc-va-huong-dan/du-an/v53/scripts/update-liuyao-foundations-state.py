from pathlib import Path
from collections import Counter
import json
root=Path(__file__).resolve().parent.parent;workspace=root.parent;base=root/'research/liuyao-foundations'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='LIUYAO_FOUNDATIONS_REPORT.md'
step=('B02/B03 có hai PDF gốc394/60trang,6phản hồi200/TLS/hash và2lỗiTLS NLC giữ riêng;28bản ghi đọc ảnh có giới hạn,84ảnh nhỏ chỉ định vị. '
 'Bộ tham chiếu nội bộ đủ64cung/48NạpGiáp/25Lục thân/8ThếỨng/sáu thần với can ngày rõ,chú chỉ hào động vàgiữ Lục thân theo cung gốc. '
 '16kiểm đạt,8260lời gọiHHCthật/4096cặp/12288chú hào động;43→44hai hào Thổ vẫn Huynhđệ theo KhônThổ. Hai hình63/64đầu sách là nhận dạng quẻ chính,không phải cặp biến. '
 'HTML707411byte/site/ZIPweb giữ byte;chưa có tính năng LụcHào công khai,chưa áp hết hai sách/toàn kho. Tiếp bản đồ chương,Phục thần vàđiều kiện NhậtNguyệt/vượng suy/DụngNguyênKỵtheo từng bản.')
d=read(workspace/'EXHAUSTIVE_WORK_STATE.json');prior=d['currentWork']
if prior.get('catalogueID')=='B01':d['previousMaiHoaWork']=prior
d['date']='2026-10-27';d['status']='active-not-complete'
d['currentWork']={'catalogueID':'B02','relatedCatalogueIDs':['B02','B03'],'work':'增刪卜易 / 卜筮正宗 — Lục Hào',
 'reason':'A substantial source-function gap now has actual facsimile-backed private structure compilation;deeper source extraction remains active.',
 'sourceDirectory':'v53/research/liuyao-foundations','currentStep':step,
 'sourceLimits':'B03onlyfirstphysicalbook;B02preface1925notverifiedprintdate;Wikisource卷01missing;Japanonlycatalog;NLCdirectcatalogTLSfailuresretained;independenttextualpedigreeopen.',
 'latestReport':'v53/MEIHUA_LAYERS_REPORT.md','latestResearchReport':'v53/'+report,
 'internalReference':'v53/research/liuyao-foundations/liuyao-reference.mjs',
 'functionalBacklog':'v53/research/liuyao-foundations/FUNCTIONAL_BACKLOG.json'}
d['inProgressScope']='v53/research/liuyao-foundations/WORK_STATE.json'
d['subsequentPriority']=[
 'Complete actual chapter/unit mapping and PhiPhuc/hidden-spirit rules with printed cases in B02/B03;then named calendar/strength/useful-god conditional rules. Private baseline is not fullLiuYao.',
 'MaiHoa:three open glyphs,independent witnesses,calendar/table-label/input semantics and all subsidiary clauses of5volumes;do not recopy completed216/720positions.',
 'Full conditional Bazi pattern/strength/useful-god extraction with named method and counterexamples.',
 'Tuvi conflicting transformations/status/onset traditions and remaining combination verses.',
 'Home flying-star complete rule set/year boundaries and explicit nonrectangular/multifloor models.',
 'Remaining Yi commentary/variants and other fixed-catalogue branches;do not count portals/downloads as applied books.']
for p in [workspace/'EXHAUSTIVE_WORK_STATE.json',root/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
d=read(base/'WORK_STATE.json');d['status']='foundation-complete-deeper-study-active';d['foundationComplete']=True
d['latestResearchReport']='v53/'+report;d['currentTarget']='Enumerate full source units and extract complete PhiPhuc/hidden-spirit rules and printed cases;then named date/strength/conditional reading premises.'
d['completedStep']=step;d['privateReference']='liuyao-reference.mjs';d['next']=['Full actual chapter mapping,not headings-as-full-reading','Hidden spirits and source examples','Calendar/strength/useful-god conditions and counterexamples','Consumer feature only after complete supported result/interpretation flow and integration QA'];write(base/'WORK_STATE.json',d)
p=root/'research/full-study/WORK_STATE.json';d=read(p);d['latestResearchReport']=report
d['exhaustiveNext']='B02/B03private structural foundation complete;continue full unit mapping/PhiPhucandcalendar/strength/useful-godconditions. MaiHoa threeglyphs/label/input/independentwitnesses and allotherbookclauses remain open.'
yi=next(x for x in d['items']if x['id']=='yi');yi['status']='partial-active-expanded-to-maihua-and-liuyao'
entry='LiuYaoB02/B03:twooriginalPDFs394/60pages,6retainedHTTP200bodies/2TLSfailures,28boundedimagerecords/84navigation-onlypages. Private64palaces/48NaJia/25kin/8roles/sixspiritstarts;changedkinbasedonprimarypalaceandmovingannotationsonly.16checks,8260actualHHChexcalls/4096structures/12288movingannotations;43→44sourcecounterexample. Consumerbytesunchanged,nofullbookoroutcomevalidationclaim.'
if entry not in yi['completed']:yi['completed'].append(entry)
yi['latestScope']='../liuyao-foundations/RULES.json'
r='LiuYao:completeactualchaptermapping,alllaterB03physicalbooks,PhiPhuc/hidden-spiritcases,dateboundary/month/day/void/strengthanduseful-godconditionalrules;currentprivatebaselineisnotafinishedconsumerfeature.'
if r not in yi['remaining']:yi['remaining'].append(r)
write(p,d)
p=root/'research/library-current/COVERAGE.json';d=read(p);d['date']='2026-10-27'
for id in ['B02','B03']:
 b=next(x for x in d['catalogue']if x['id']==id);b['currentStatus']='research_only';b['wholeWorkApplied']=False
 b['scope']='Bộ tham chiếu LụcHào nội bộ có ảnh/quy tắc/16kiểm;64cung,48NạpGiáp,25Lục thân,8ThếỨng vàhào biến theo cung gốc. Chưa công khai/chưa toàn chương hoặc toàn tác phẩm.'
 b['localPossession']=['PDF byte gốc394trang/11.089.308byte,APICommons/hash/TLS;21bản ghi ảnh có giới hạn. Tựa1925không thay cho năm in xác minh.'if id=='B02'else'PDF byte gốc60trang/50.191.031byte,chỉ sách đóng1của14quyển;APICommons/hash/TLS,7bản ghi ảnh có giới hạn. Bìa1904,卷01Wikisourcekhông tồn tại.']
 b['currentEvidence']=['v53/'+report]+['v53/research/liuyao-foundations/'+f for f in ['SOURCE_AUDIT.json','MANUAL_READINGS.json','RULES.json','SOURCE_FIXTURES.json','liuyao-reference.mjs','FUNCTIONAL_BACKLOG.json']]+['v53/qa/liuyao-foundations/ENGINE_RESULTS.json']
 b['latestLocalReadingScope']='Selectedoperationalfoundationsonly;notall394/60pagesread,notall14B03volumesheld.'
 b['inheritedAccessLabelIsVerified']=False;b['originalURLIndependentlyValidatedByAlternateWitness']=False
d['counts']['status']=dict(Counter(b['currentStatus']for b in d['catalogue']));d['counts']['wholeWorkApplied']=sum(b['wholeWorkApplied']for b in d['catalogue'])
assert d['counts']['status']=={'inherited_rule_claim':4,'partial_active':5,'research_only':4,'not_established':27}
d['latestAcquisitionCounts']={'scope':report,'originalPDFs':2,'retainedHTTP200Bodies':6,'failedTLSAttempts':2,'fullBooksApplied':0}
d['latestFollowup']=report+':B02/B03research_only,16checks/8260actualHHChexcalls/4096structures/12288movingannotations.28boundedimagerecords,consumerbytesunchanged;wholeworkapplied0.'
for f in d['features']:
 if f['id']=='other':f.update(active='MaiHoa công khai:tám cách lập quẻ vàbốn lớp ThểDụng;LụcHào mới có bộ cấu trúc nội bộ,không là tính năng web.',missing='LụcHào đầy đủ điều kiện/lời đọc,trạch nhật,KỳMôn,LụcNhâm,TháiẤt;mọi nội dung sách còn mở không tự thành thuật toán.')
write(p,d)
note=('Mốc LụcHào27/10/2026: `'+report+'` có hai PDF gốc394/60trang,28bản ghi đọc ảnh có giới hạn;84ảnh nhỏ chỉ định vị. '
 'Bộ nội bộ64cung/48NạpGiáp/25Lục thân/8ThếỨng/sáu thần/chú hào biến theo cung gốc đạt16kiểm,8260lời gọiHHCthật/4096cặp/12288chú. '
 'B02/B03lênresearch_only;chưa tính năng công khai hoặc hết sách. HTML707411byte/site/ZIPweb giữ byte. Tiếp bản đồ chương,Phục thần vàđiều kiện NhậtNguyệt/vượng suy/DụngNguyênKỵ;toàn kho active-not-complete.\n\n')
for p in [workspace/'PROJECT_RESEARCH_STATE.md',root/'NEXT_STEPS.md',root/'research/library-current/COVERAGE.md']:
 s=p.read_text(encoding='utf-8-sig')
 if not s.startswith('Mốc LụcHào27/10/2026:'):p.write_text(note+s,encoding='utf-8')
print('B02/B03research_only;foundationcomplete,deeperstudyactive;no consumer change;wholeworkapplied0.')
