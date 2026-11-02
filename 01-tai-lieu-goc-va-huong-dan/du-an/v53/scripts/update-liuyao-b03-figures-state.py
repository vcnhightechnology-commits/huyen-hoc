from pathlib import Path
import json
root=Path(__file__).resolve().parent.parent;workspace=root.parent;base=root/'research/liuyao-b03-figures'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='LIUYAO_B03_FIGURES_REPORT.md'
lead={'status':'discovered-not-downloaded-not-hashverified','sourceTitle':'File:NLC892-GBZX0301013045-259365 卜筮正宗 十四卷 第2冊.pdf',
 'sourceURL':'https://commons.wikimedia.org/wiki/File:NLC892-GBZX0301013045-259365_%E5%8D%9C%E7%AD%AE%E6%AD%A3%E5%AE%97_%E5%8D%81%E5%9B%9B%E5%8D%B7_%E7%AC%AC2%E5%86%8A.pdf',
 'evidenceLevel':'Webprimaryfilepage/searchleadonly,notretainedHTTPbody;requiresCommonsAPIrevision/imageinfo/bytehashanddirectopeningpagesbeforeeditioncontinuityclaims.'}
step=('B03 quyển2/PDF34–59 đọc lần đầu toàn khoảng,64hình támcung định vị;60bìa/kết. 27bản ghi22render mới(21nội dung/1kết)+5mở rộng,2crop. '
 'Thêm13Phụcthần ởbảycung và quy tắc hìnhquẻ hiện/biến có Lục thân cầnxét thì không mặc định traPhục;ví dụ33→13dùng TàiMão biến1 thayTàiDần ẩn2. QA360dpiđọc tiêuđề21筮嗑,giữriêngchuẩnhóa噬嗑;thêm1renderQA/3crop tổng. '
 '9kiểm/79HHCthật,giữsáuthamchiếu trước/HTML707411byte/site/ZIPweb.0HTTP/PDFgốc. Chưađối384chúhào/toànbài/tiềntự/cácsáchsau;B02vẫn136/103đềmục/26khoảng,ngày52mở;toànkho chưa xong.')
nexts=['B03remainingfull384lineannotations/figureparagraphs and heading21variantcomparison(literal筮readat360DPI);prefaces/introductoryunitsstillpartial.',
 'AcquireidentifiednextB03physicalbooksforfullconditionalstrength/functionalvoid/FanFu/卦身andnamedmethodexceptions;firstphysicalbookdoesnotcover14textualvolumes.',
 'B02remaining103heading-onlybodiesand7partialfoundationunits;independentwitnessesforPDF52andotheropenglyphs;calendarinstantsbeforedateadapter.',
 'ContinueallMaiHoa/Bazi/Tuvi/Homeandremaining40recordlibraryitems;noallfour/wholeworkcompletionclaim.']
d=read(workspace/'EXHAUSTIVE_WORK_STATE.json');d['date']='2026-10-27';d['currentWork'].update(currentStep=step,latestResearchReport='v53/'+report,
 sourceDirectory='v53/research/liuyao-b03-figures',internalB03AvailabilityReference='v53/research/liuyao-b03-figures/availability-reference.mjs',
 B03FigureLocator='v53/research/liuyao-b03-figures/FIGURE_LOCATOR.json',functionalBacklog='v53/research/liuyao-b03-figures/WORK_STATE.json')
d['inProgressScope']='v53/research/liuyao-b03-figures/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
d['currentWork']['nextSourceLead']=lead
for p in[workspace/'EXHAUSTIVE_WORK_STATE.json',root/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
write(base/'WORK_STATE.json',{'date':'2026-10-27','status':'private-figure-locator-availability-complete-further-B03-active','sourceID':'B03','latestReport':'v53/'+report,
 'completedStep':step,'privateReference':'availability-reference.mjs','figureLocator':'FIGURE_LOCATOR.json','figureHeadings':64,'palaces':8,'volume2RelevantSpanRead':True,
 'all384LineAnnotationsCollated':False,'newLocalRenders':22,'additionalQAPageRenders':1,'expandedPriorRecords':5,'newContentPages':21,'newEndleafPages':1,'qaCrops':3,
 'additionalHiddenCases':13,'next':nexts,'nextSourceLead':lead,'newOriginalPDFs':0,'newHTTPResponses':0,'consumerChanged':False,'wholePhysicalBookRead':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False})
p=root/'research/full-study/WORK_STATE.json';d=read(p);d['latestResearchReport']=report;d['exhaustiveNext']='B03full384lineannotations/remainingfigureclauses/heading21variant(literal筮readat360DPI),first-bookprefaces/introductionandidentifiednextphysicalbooks;fullstrength/functionalvoid/FanFu/卦身methodexceptions. B02counts136/103/26unchanged;otherlibrarygapsremain.'
yi=next(x for x in d['items']if x['id']=='yi');entry='B03volume2spanPDF34..59first-pass26contentpages+60endleaf:64figurelocators/eightpalaces,13newhiddenfixtures/sevennon乾palaces;PDF59shownprimary/changeddesiredkinavailabilitygate,33→13changed卯1overhidden寅2.9checks/79actualHHChexcalls.27images22new5expanded+1QA360DPIrender/3crops,literalheading21筮separatefromnormalized噬;0HTTP/PDF;consumerandsixpriorreferencesunchanged. Notall384annotations/allbookclauses/prefaces/wholework.'
if entry not in yi['completed']:yi['completed'].append(entry)
yi['latestScope']='../liuyao-b03-figures/AVAILABILITY_RULES.json'
yi['remaining']=[s for s in yi['remaining']if not s.startswith('LiuYaoB03:afterPDF38/')]
yi['completed']=[s for s in yi['completed']if not(s.startswith('B03volume2spanPDF34..59first-pass')and s!=entry)]
yi['remaining']=[s for s in yi['remaining']if not s.startswith('LiuYaoB03:volume2spanread/')]
yi['remaining'].append('LiuYaoB03:volume2spanread/64headingslocatedbut384lineannotationsandallconditionalclausesnotcollated;heading21literal筮read/independentvariantcomparisonopen,prefaces/introductionpartial,nextphysicalbooksneeded. Fullstrength/void/FanFu/卦身/dateboundariesnotintegrated;B02still103heading-onlyunits.')
write(p,d)
p=root/'research/library-current/COVERAGE.json';d=read(p);b=next(x for x in d['catalogue']if x['id']=='B03')
b['scope']='B03quyển2/PDF34–59 đọc lầnđầu toàn khoảng/64hình támcung địnhvị;13Phụcthần thêm vàcổng hiện/biến trước tìmPhục,ví dụ33→13. Trướcđó12tiết kiến tháng/Hỏa12pha riêng. Chưa384chúhào/toànbài/tiềntự/cácsáchsau/vượngsuy/chânkhông/côngkhai.'
b['latestLocalReadingScope']='27bản ghi22render(21nội dung1kết)+5mởrộng,thêm1renderQA360dpi/3crop;đọcđầuđề21筮riêngchuẩnhóa噬,9kiểm79HHC thật;0HTTP/PDFgốc. Dịbản/quái thân/lịch/hiệulực giữmở;khôngtoànsách.'
files=['v53/'+report]+['v53/research/liuyao-b03-figures/'+n for n in['MANUAL_READINGS.json','FIGURE_LOCATOR.json','SOURCE_FIXTURES.json','AVAILABILITY_RULES.json','availability-reference.mjs']]+['v53/qa/liuyao-b03-figures/ENGINE_RESULTS.json']
for f in files:
 if f not in b['currentEvidence']:b['currentEvidence'].append(f)
d['latestFollowup']=report+':B03volume2spanread/64figurelocators,13newhiddenfixtures/availabilitygate;9checks/79HHC.27images22new5expanded,0HTTP/PDF. Consumerunchanged/wholework0;further384lineclauses/prefaces/laterbooksactive.'
d['latestAcquisitionCounts']={'scope':report,'originalPDFs':0,'retainedHTTP200Bodies':0,'newLocalRenders':22,'additionalQAPageRenders':1,'expandedPriorRecords':5,'newContentPageReadings':21,'newEndleafPages':1,'manualImageRecords':27,'fullBooksApplied':0};d['counts']['newDownloadsThisScope']=0
assert d['counts']['wholeWorkApplied']==0;write(p,d)
note=('Mốc B03–Hình 27/10/2026: `'+report+'` khép lượtđọc khoảngquyển2/PDF34–59,64hình támcung địnhvị;60kết.27bản ghi22render(21nội dung1kết)+5mởrộng/2crop. '
 'Thêm13Phụcthần ởbảycung vàcổng hiện/biến trước tìmPhục;33→13chọnTàiMão biến1 thayTàiDần ẩn2.9kiểm/79HHC thật,0HTTP/PDFgốc;HTML707411byte/site/ZIPweb/sáuthamchiếu trước giữbyte. '
 'Thêm1renderQA360dpi/3crop tổng,đọcđầuđề21筮riêngchuẩnhóa噬;chưa384chúhào/toànbài/tiềntự/cácsáchsau/dịbản. B02vẫn136/103đềmục/26khoảng,ngày52mở. Tiếpxửlýphầncònlại,toànkho chưa hoàn tất.\n\n')
for p in[workspace/'PROJECT_RESEARCH_STATE.md',root/'NEXT_STEPS.md',root/'research/library-current/COVERAGE.md']:
 s=p.read_text(encoding='utf-8-sig')
 if s.startswith('Mốc B03–Hình 27/10/2026:'):s=s.split('\n\n',1)[1]
 p.write_text(note+s,encoding='utf-8')
print('B03figure/availabilityscope recorded;all-library work remains active.')
