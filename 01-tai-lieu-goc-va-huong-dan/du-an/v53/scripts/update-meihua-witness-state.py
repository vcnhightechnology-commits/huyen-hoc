from pathlib import Path
from hashlib import sha256
import json

root=Path(__file__).resolve().parent.parent
workspace=root.parent
read=lambda p:json.loads(p.read_text(encoding='utf8'))
write=lambda p,d:p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
base=root/'research/meihua-witness'
identity=read(base/'EDITION_IDENTITY.json')
prior=root/'research/meihua-reading/ADDITIONAL_SCAN_NOTES.json'
d=read(prior)
for r in d['records']:
 if r['pdfPage']in[200,220]:
  r.setdefault('historicalPrintedPage',r['printedPage'])
  r['printedPage']='12'if r['pdfPage']==200 else'32'
  r['correctionEvidence']='../meihua-witness/EDITION_IDENTITY.json'
for r in d['candidateVolumeStarts']:
 if r['volume']==4:r.update(verifiedTitlePage=True,verifiedTitlePDFPage=145,evidence='../meihua-witness/EDITION_IDENTITY.json')
 if r['volume']==5:
  r.setdefault('historicalPDFPageCandidate',r['pdfPageCandidate'])
  r.update(pdfPageCandidate=189,verifiedTitlePage=True,verifiedTitlePDFPage=189,basis='Direct title atPDF189;PDF188 is卷四終44. PrintedPDF200=12,220=32.',evidence='../meihua-witness/EDITION_IDENTITY.json')
d['latestCorrection']='2026-10-26: direct title/endleaf/margin reading supersedes earlier inferred volume5 offset;historical values retained.'
write(prior,d)
structure=root/'research/meihua/SCAN_STRUCTURE.json';d=read(structure)
d['status']='five-volume-structure-and-volume4-5-title-boundaries-verified-partial-unit-mapping'
for r in d['volumes']:
 if r['volume']==4:r.update(titlePDFPage=145,endleafPDFPage=188,currentCoverage='Selected first/last unit groups now mapped;35bodypage records acrossvolumes4/5inlatestscope,not full44page reading or a completed glyph classifier. See../meihua-witness/UNIT_MAP.json.')
 if r['volume']==5:r.update(titlePDFPage=189,endleafPDFPage=228,currentCoverage='Selected groups throughPDF208and220mapped;48NạpGiáp assignments,30nạpâm pairs and20seasonal cells extracted. Full printedunitinventory andthelaterchapters remain open. See../meihua-witness/UNIT_MAP.json.')
d['editionIdentity']='../meihua-witness/EDITION_IDENTITY.json'
d['nextRequirement']='Read and map remaining body pages150–178,209–219,221–227 before claiming full printedunit inventory;then complete each clause disposition and variants. Direct colophon now confirms1925-11 for this imprint,not original authorship.'
write(structure,d)
backlog=root/'research/meihua-reading/FUNCTIONAL_BACKLOG.json';d=read(backlog)
for r in d['groups']:
 if r['id']=='mutual-body-use':r.update(status='candidate-calculation-tested-browser-print-pending',remainingOrScope='Four-layer consumer candidate prepared;14checks cover384structures/1536relations with existingcast functions unchanged. Not live:browser launch not executed because automatic approval review hit usage limit. Continue via../meihua-layers/PENDING.json;do not bypass approval review.',currentApplication='../meihua-layers/PENDING.json')
 if r['id']=='volume-four-five':r.update(status='partial-unit-mapping-and-literal-tables-extracted',remainingOrScope='Title starts145/189verified;1925-11colophon231read.34boundedunitgroups,41targetedpages including35bodypages,48NạpGiápcells and30nạpâmpairs.47bodypages remain unmapped/partly surveyed;neitherbook norinventory complete.',evidence='../meihua-witness/UNIT_MAP.json')
 if r['id']=='seasonal-conditions':r['currentEvidence']='../meihua-witness/SEASON_TABLE.json';r['remainingOrScope']='PDF204literal4rows/20cells extracted;no死row printed. Calendar boundaries,day/month priority and fullconditional strength method remain open.'
new=[{'id':'appendix-najia-table','status':'research-compiler-tested-not-public-liuyao','remainingOrScope':'48literalassignments206–207 compiled;64actualhexagrams/384lineassignments,4orientationcontrols. Stillneedidentifiedcomparisonwitness,palace/世應/六親/伏神 andconditional reading. Not a complete LụcHào function.','evidence':'../meihua-witness/NAJIA_TABLE.json'}, {'id':'six-spirit-day-stems','status':'source-starts-and-two-rows-extracted-research-only','remainingOrScope':'Daystemstarts179and2literalrows180read;4additionalrotations explicitderivations. Keepapart from卷五glyph-form六神形式.','evidence':'../meihua-witness/SIX_SPIRITS.json'}]
for r in new:
 if not any(x['id']==r['id']for x in d['groups']):d['groups'].append(r)
write(backlog,d)
full=root/'research/full-study/WORK_STATE.json';d=read(full)
d['latestResearchReport']='MEIHUA_WITNESS_REPORT.md'
d['exhaustiveNext']='Continue the47unmapped/partial body pages inprintedvolumes4/5 andfullclause dispositions. Complete the pendingBody/Use browser/PDF verification only after approval review is available;do not bypass it. NạpGiáp basecompiler is internal and not a completeLụcHào product.'
yi=next(x for x in d['items']if x['id']=='yi')
entry='MaiHoa witness:direct1925-11imprint231;volume4/5starts145/189withcorrectedPDF200/220printed12/32.41boundedreadingrecords/34unitgroups;48NạpGiápcells,30nạpâmpairs,2literal6spiritrows,20seasonalcells.13source/runtimechecks,64actualcasts/384assignments and60realnạpâmmatches,2labelvariants. Product unchanged;fullbook open.'
if entry not in yi['completed']:yi['completed'].append(entry)
yi['latestScope']='../meihua-witness/MANUAL_READINGS.json'
yi['pendingConsumerCandidate']='../meihua-layers/PENDING.json'
yi['remaining'][0]='Expanded castingmethods are live and checked;four-layer Body/Use candidate has14calculationchecks but browser/print pending after automaticreview usage-limit failure. Do not call candidate released.'
yi['remaining'].append('Volume4/5title boundaries and1925-11imprint now directly read. Read remaining150–178,209–219,221–227andcompleteunits;fivevolumes still not fully exploited.')if not any('150–178'in s for s in yi['remaining'])else None
write(full,d)
state=read(workspace/'EXHAUSTIVE_WORK_STATE.json')
state['currentWork'].update(currentStep='Live release703410bytes retains8MaiHoa choices and62checks. Internal4-layerBody/Use candidate14checks is waiting for browser/PDF because approvalreview hitusage limit;notreleased. Independent sourcefollowup completed13checks:41boundedpagerecords,34unitgroups,48NạpGiáp cells,60nạpâm elementmatches/2labelvariants. Continue47unmapped/partialbodypages and fullconditionalrules.',sourceLimits='DirectPDF231imprint now confirms1925-11 and文明書局;notShaoYonghistoricalauthorship/firstedition. Five textual卷 and全二冊 physicalformat;3digitalvolumes remain incomplete. NLCcatalogTLSfailure retained.',latestResearchReport='v53/MEIHUA_WITNESS_REPORT.md',pendingConsumerCandidate='v53/research/meihua-layers/PENDING.json')
for p in[workspace/'EXHAUSTIVE_WORK_STATE.json',root/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,state)
coverage=root/'research/library-current/COVERAGE.json';d=read(coverage);entry=next(x for x in d['catalogue']if x['id']=='B01')
entry['scope']='Tám lựa chọn lập Mai Hoa đã áp dụng; chữ có bốn phân kiểu, đầu vào nét/âm/đo tường minh. Chưa hết năm quyển. Đã đọc trực tiếp trang xuất bản1925-11;34nhóm đơn vị có giới hạn và bảng Nạp Giáp/nạp âm/sáu thần/mùa trong hồ sơ riêng. Bản Thể–Dụng mở rộng còn chờ kiểm giao diện/in, chưa phát hành.'
for f in['v53/research/meihua-witness/EDITION_IDENTITY.json','v53/research/meihua-witness/MANUAL_READINGS.json','v53/research/meihua-witness/NAJIA_TABLE.json','v53/MEIHUA_WITNESS_REPORT.md']:
 if f not in entry['currentEvidence']:entry['currentEvidence'].append(f)
entry['latestLocalReadingScope']='41bản ghi trang có mục tiêu:35nội dung(32mới/3mởrộng),3trang kết,2quảng cáo,1trang xuất bản. Không cộng87ảnh render thành87trang đã đọc.'
entry['editionIdentityStatus']='Direct imprint1925-11;historical authorship/firstedition andindependentNLCcatalogauthenticationremainopen.'
d['latestFollowup']='MEIHUA_WITNESS_REPORT.md:13source/runtimechecks;liveHTMLunchanged,candidateBody/Uselayerpendingbrowserreviewavailability. Wholeworkapplied remains0.'
assert d['counts']['wholeWorkApplied']==0
write(coverage,d)
note='''Mốc nghiên cứu26/10/2026: `MEIHUA_WITNESS_REPORT.md` đọc trực tiếp trang xuất bản231(1925-11/Văn Minh), xác nhận đầu quyển4ở145/quyển5ở189 và sửa trang in200=12/220=32. Có41bản ghi trang có mục tiêu,34nhóm đơn vị;48ô Nạp Giáp/30cặp nạp âm/hai hàng sáu thần/20ô mùa.13kiểm nguồn/runtime đạt;HTML đang dùng vẫn703410byte/SHA380016… Không coi đọc đề mục/bảng là khai thác hết sách. Thể–Dụng mở rộng tách ở`research/meihua-layers/PENDING.json`:14kiểm phép tính,kiểmUI/PDF chưa chạy vì bộ duyệt tự động hết hạn mức;chưa đưa vào bản đang dùng. Tiếp47trang thân sách còn chưa lập bản đồ đủ và mọi điều kiện còn mở.\n\n'''
for p in[root/'NEXT_STEPS.md',workspace/'PROJECT_RESEARCH_STATE.md']:
 s=p.read_text(encoding='utf8')
 if not s.startswith('Mốc nghiên cứu26/10/2026: `MEIHUA_WITNESS_REPORT.md`'):p.write_text(note+s,encoding='utf8')
coverage_md=root/'research/library-current/COVERAGE.md'
s=coverage_md.read_text(encoding='utf8')
if not s.startswith('Cập nhật nhân chứng26/10/2026:'):coverage_md.write_text('Cập nhật nhân chứng26/10/2026: xem `../../MEIHUA_WITNESS_REPORT.md` và `../meihua-witness/EDITION_IDENTITY.json`. Niên đại bản Mai Hoa1925-11 đã có trang xuất bản;toàn tác phẩm vẫn chưa áp hết. CandidateThể–Dụng đang chờ kiểmUI/PDF vàkhông nằm trongsite.\n\n'+s,encoding='utf8')
print('Updated current research state and preserved historical values;consumer release unchanged.')
