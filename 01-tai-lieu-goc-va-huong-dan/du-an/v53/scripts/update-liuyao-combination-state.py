from pathlib import Path
import json
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/liuyao-combination-context';q=r/'qa/liuyao-combination-context'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='LIUYAO_COMBINATION_CONTEXT_REPORT.md'
step=('B02: đọc mở rộng12vịtrícũ50–54/73–79,0HTTP/vịtrínguồn/container/nhânchứngmới;map137khoảngđọcđầu/0áphếtgiữ. Ba module riêng:ngoạilệNguyênthần51,sáudạngLụchợp73–74,Tamhợp77–79theođúnglớp. '
'Giữ51午→未貪合khôngsinhriêngvới74化扶;rawcặphợpkhôngtựthànhgiữ/trợ/giảihợp. 78đọcrõ一爻動bằngcrop230/420,khôngsửa三hoặcnhậpngưỡngB03;dạngđầuchưaphânđịnh. Dạng2đúnghaihoạtđộng/mộtbấtđộngcầnbiếtámđộng;dạng3/4chỉnhómđầucuốinội1/3ngoại4/6vàchibiến,khôngtrộncả6hào. '
'16kiểmđạt;8HHCthànhcôngởcáclầnchạyđạtcuối(2cặpkếthừa1→9quaphépchiếumới,4haicặptên1→11/56→22,2vídụ79Ly→Khôn30→2). 4HHCtênquẻđãchạythànhcôngtronglầnkiểmvectorlỗitrước;giữFAILURE_AUDIT,tổng12thựcthithànhcônggồm4lặpkhôngchứngcứđộclập. '
'Ví dụ79sáunhãngốc/bốnbiến/Thế6Ứng3khớp,giữứngviênnộiMộc/ngoạiKim;khôngthànhđịađiểm/kiệntụng/giađạo/kếtquảydược. 6cropđãxemkhớppixel/1táirender420/26identity/3modulechỉđổiimport. Hợpgiữ/giảihợp/vượngsuy/cănkhí/thànhcục/ưu tiêncònmở;HTML/site/ZIPwebnguyênbyte,toànkhoactive.')
nexts=[
'B02:137khoảngđọclầnđầu/0áphết;tiếpcácđiềukiệnhoànchỉnhchọnDụng/NguyênKỵCừu,cănkhí/vượngsuy,hiệulực/ưu tiên/phảnvídụ,giọngnguồn. Ba moduleLục–Tamhợpchỉtọađộ/tiềnđề,chưaenginehợpgiữ/giảihợp/thànhhóa đầyđủ.',
'Nguồn78literal一爻動đãđọcrõ;nghĩathànhcụcdạngđầuchưaxáclập,khôngsửa三từthônglệhoặcB03. Tìmđúngnhânchứngsonghànhkhicóthểtruycập;khônglặptảiảnhcũ/vượtchặn. 51貪合khôngsinhvà74化扶giữriêng,khôngtựđặtưu tiên.',
'Khônglặp16kiểm/8HHCcuối/4HHCtestvectorlỗicũhoặc64đồ/384dòngnếulogicnguồngiữ. Tamhợpcầnphânbiệtngày/thángđiềnthực,xungmộ,ámđộng,ThếDụngtrongcục vànộingoại;chưathànhngàyứngnghiệm/kếtquảthực.',
'Cácphầnkhácactive:Tửvi童限/火鈴/CanhNhâm/khởihạn;BátTự47ngữcảnhDươngNhận/9cáchkhác/vượngsuy;nhàPhiTinh/ranhlịch/Bắcthực;B03/MaiHoa/chữmở. BrowserUIvôhiệuhóa,khôngvượtsetting;nghiêncứu/QAngoàisite,khôngxuấtbản. Danhmục40/whole0.'
]
write(b/'WORK_STATE.json',{'date':'2026-10-28','status':'source-specific-origin-combination-triad-components-verified-full-conditions-active','catalogueID':'B02','latestReport':'v53/'+report,'completedStep':step,'sourceVerification':read(q/'SOURCE_RESULTS.json'),'sourceUnitMap':'v53/research/liuyao-foundation-span/B02_CURRENT_UNITS.json','next':nexts,'passingChecks':16,'successfulHHCCallsInPassingRuns':8,'earlierFailedTestRunSuccessfulRepeatedHHCCalls':4,'firstModeLiteralRead':True,'firstModeAdjudicated':False,'fullFunctionalRulesEncoded':False,'sourceOutcomesValidated':False,'consumerChanged':False,'wholeCatalogueCompleted':False,'releaseVerification':'v53/qa/liuyao-combination-context/RELEASE_RESULTS.json;expecteduntilfinal--no-write'})
d=read(w/'EXHAUSTIVE_WORK_STATE.json');d['date']='2026-10-28';d['currentWork'].update(work='增刪卜易 — 六合/三合與元神貪合例外',reason='Separate source-specific structural forms,conditional exceptions and withheldfirstmode interpretation instead of automatic nominalcombinationeffect.',sourceDirectory='v53/research/liuyao-combination-context',currentStep=step,latestResearchReport='v53/'+report,functionalBacklog='v53/research/liuyao-combination-context/WORK_STATE.json',internalOriginSupportReference='v53/research/liuyao-combination-context/origin-support-reference.mjs',internalCombinationFormsReference='v53/research/liuyao-combination-context/combination-forms-reference.mjs',internalB02TriadReference='v53/research/liuyao-combination-context/triad-context-reference.mjs',sourceLimits='137firstpass/0whole.12retainedpositionsreviewed/6crops;16checks/8HHCpassingrun+4priorfailed-testrepeatcalls.78literal一notemended;firstmode/fullhold-release/formationunresolved.',nextSourceLead={'sourceID':'B02-source-specific-combination-prerequisites','status':'full-conditions-and-exactparallel-firstmode-witness-open','file':'v53/research/liuyao-combination-context/WORK_STATE.json','remaining':' '.join(nexts)})
d['inProgressScope']='v53/research/liuyao-combination-context/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in[w/'EXHAUSTIVE_WORK_STATE.json',r/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=r/'research/full-study/WORK_STATE.json';d=read(p);d['date']='2026-10-28';d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts);i=next(x for x in d['items']if x['id']=='yi')
if step not in i['completed']:i['completed'].append(step)
if ' '.join(nexts)not in i['remaining']:i['remaining'].append(' '.join(nexts))
i['latestScope']='../liuyao-combination-context/WORK_STATE.json';i['nextFile']='../liuyao-foundation-span/B02_CURRENT_UNITS.json';write(p,d)
p=r/'research/library-current/COVERAGE.json';d=read(p);d['date']='2026-10-28';entry=next(x for x in d['catalogue']if x['id']=='B02');entry['latestCombinationContextScope']=step
for f in['v53/'+report]+['v53/research/liuyao-combination-context/'+n for n in['WORK_STATE.json','SOURCE_MANIFEST.json','COMBINATION_SOURCE_MANIFEST.json','TRIAD_FIXTURE.json','FAILURE_AUDIT.json','PROMOTION_IDENTITIES.json','origin-support-reference.mjs','combination-forms-reference.mjs','triad-context-reference.mjs']]+['v53/qa/liuyao-combination-context/'+n for n in['RESULTS.json','COMBINATION_RESULTS.json','TRIAD_RESULTS.json','SOURCE_RESULTS.json']]:
 if f not in entry['currentEvidence']:entry['currentEvidence'].append(f)
d['latestFollowup']=report+': '+step;d['latestAcquisitionCounts']={'scope':report,'newHTTPRequests':0,'newOriginalContainers':0,'newViewedSourcePositionsThisTurn':0,'retainedPositionsReviewed':12,'sourceCropsViewed':6,'sourcePixelReproductions':1,'sourceSpecificComponents':3,'wholeWorksApplied':0};d['counts']['newDownloadsThisScope']=0;d['counts']['newDownloadsThisScopeBasis']='12retainedpositions50–54/73–79expanded;6crops/1QApage/1redecode.0HTTP/newpositions/containers/independentwitness.16checks,notwholeapplication.';assert d['counts']['wholeWorkApplied']==0;write(p,d)
note='Mốc Dịch — Lục hợp, Tam hợp và ngoại lệ sinh trợ,28/10/2026: `'+report+'`. '+step+'\n\n'
for p in[w/'PROJECT_RESEARCH_STATE.md',r/'NEXT_STEPS.md',r/'research/library-current/COVERAGE.md']:
 t=p.read_text(encoding='utf-8-sig')
 if not t.startswith(note):p.write_text(note+t,encoding='utf-8')
p=w/'PENDING_RESEARCH_STATE.json';d=read(p);d.update(date='2026-10-28',status='B02-combination-context-full-conditions-active',workDirectory='v53/research/liuyao-combination-context',currentWorkState='v53/research/liuyao-combination-context/WORK_STATE.json',latestReport='v53/'+report,next=nexts,consumerChanged=False,wholeCatalogueCompleted=False)
if'inProgressStaging'in d:d['previousStaging']={**d.pop('inProgressStaging'),'status':'promoted-awaiting-finalpackageverification'}
write(p,d)
print('Recorded16checksandthreeprivatecomponents;sourcefirstmodeandfullconditionsremainopen.')
