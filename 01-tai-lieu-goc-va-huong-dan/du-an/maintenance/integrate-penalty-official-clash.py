from pathlib import Path
from hashlib import sha256
import json,shutil
W=Path(__file__).resolve().parent.parent;V=W/'v53';R=W/'recovery/research-release';R.mkdir(exist_ok=True)
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def identity(p):return {'file':p.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
assert read(W/'recovery/storage-consolidation/MAINTENANCE.json')['status']=='complete'
assert not (W/'archives').exists()
scopes=['bazi-true-ghost-context','bazi-branch-penalty','bazi-branch-clash']
for name in scopes:
 s=W/'tmp'/f'{name}-staging';r=V/'research'/name;q=V/'qa'/name
 assert read(s/'SOURCE_RESULTS.json')['passed'] and read(s/'REFERENCE_RESULTS.json')['passed'];assert not r.exists() and not q.exists()
 d=read(s/'WORK_STATE.json');d.update(integratedIntoRelease=True,integrationKind='research-only;consumer-unchanged',packageVerificationPointer='recovery/research-release/FINAL_VERIFICATION.json')
 d.pop('currentSourcePackageContainsEarlierReadingOnly',None)
 d['next']=['Close explicit source premises and named voice differences; no automatic efficacy, fortune or medical inference.','Currentvolume2coverageindexremainsincomplete;rotateindependentDịch/Tửvi/Nhàởbacklogorreadunestablishedpositions.','Reuse retained actual runtime batches; obey STORAGE_POLICY.md and one latest comprehensive package.']
 write(s/'WORK_STATE.json',d);shutil.copytree(s,r);q.mkdir(parents=True)
 pairs=[]
 for p in sorted(s.iterdir()):
  if p.is_file():
   target=r/p.name;assert p.read_bytes()==target.read_bytes();pairs.append({'source':p.relative_to(W).as_posix(),'target':target.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()})
 for n in ['SOURCE_RESULTS.json','REFERENCE_RESULTS.json']:shutil.copy2(s/n,q/n)
 write(q/'PROMOTION_IDENTITIES.json',{'byteExactFiles':pairs,'noFullSnapshotCreated':True})
 write(q/'RELEASE_RESULTS.json',{'status':'source-and-reference-verified;comprehensive-package-verification-external','consumerChanged':False,'sourceChecks':read(s/'SOURCE_RESULTS.json'),'referenceTests':read(s/'REFERENCE_RESULTS.json'),'packageVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json','historicalStatePreservation':'recovery/consolidated-history/INDEX.sqlite#revisions','wholeWorkApplied':False})
summary='Tam Mệnh: tích hợp ba phạm vi Quan hương/真官真鬼,三刑và衝擊. 99đơnvịbiêntập/3397codepoint/3405UTF16;không99quytắchoànchỉnh. Quyển5đọc5vịtrí19–23/ngữcảnh論正官;quyển2đọc19vịtrí214–232riêng gồm18mớivà214táidùng. 15hàmnguồn giữba官鄉/tiềnđề真官真鬼,hai giọngtên刑/đủbốnchi/5vídụ刑入/ba vaitrụ,vàcặpxung/nhómđủ/hướng我他/Lộcvớigiớihạnnguồn. Giữ卯寅子,戌丑未未và馬在己chưasửa;khônggộp真五行vớiThậpthần. 24truyvấnbảngthậtđãgiữ/0lá số;6hợpcan,3Nạpâm,12xungtáidùngtheo từngkiểm,có1kếtquảNạpâmđượcdùngở2phạmvi. Ba bộ9nhómkiểmđạt,HTML/site/webnguyênbyte. Chỉmụcquyển2hiện86/232vịtríxemđầu,146chưaxáclập;toànkhovẫnmở.'
nextline='Luânphiên Dịch B02:đọc RESUME_INDEX.json vàmap137khoảng trướcchọnvai Dụng/NguyênKỵCừu,vượngsuy/日月/旬空/飛伏/應期. M01còn146vịtríquyển2chưaxáclậptheochỉmục;真五行/刑入/福聚/用神有氣有扶vàcáccáchưu tiênvẫnmở. Khôngchạy lạibảngthật24truyvấnvừagiữhoặclấytêncáchlàứngnghiệm.'
report='BAZI_PENALTY_OFFICIAL_CLASH_REPORT.md'
body='# Tam Mệnh: 官鄉, 三刑 và 衝擊\n\n'+summary+'\n\n'
for name in scopes:body+='\n\n'+(V/'research'/name/'README.md').read_text(encoding='utf-8')
body+='\n\n## Tiếp tục và lưu trữ\n\n'+nextline+'\n\nGiữ bản trước theo SHA-256 trong chỉ mục hợp nhất và bảng revisions;không tạo full snapshot. PROMOTION_IDENTITIES trong từng QA ghi cặp byte staging→release;nguồn/corpus/QA ở ngoài site. FINAL_VERIFICATION.json là dấu kiểm gói ngoài gói, phải khớp băm manifest V53 hiện hành;không dùng các kiểm snapshot cũ làm kiểm phát hành.\n'
(V/report).write_text(body,encoding='utf-8')
e=read(V/'research/EXHAUSTIVE_WORK_STATE.json');e['previousStarsHarmsWork']=e['currentWork'];e['currentWork']={'catalogueIDs':['M01'],'work':'Tam Mệnh:官鄉/真官真鬼,三刑,衝擊','sourceDirectories':[f'v53/research/{n}'for n in scopes],'currentStep':summary,'latestResearchReport':report,'sourceLimits':[limit for n in scopes for limit in read(V/'research'/n/'WORK_STATE.json')['sourceLimits']],'wholeWorkApplied':False};e['historicalPriorityBeforePenaltyClash']=e['subsequentPriority'];e['subsequentPriority']=[nextline,*[x for x in e['subsequentPriority']if not x.startswith('Tiếp論三刑')]];e['inProgressScope']={'status':'three-selected-source-scopes-integrated','finalVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json'};write(V/'research/EXHAUSTIVE_WORK_STATE.json',e);shutil.copy2(V/'research/EXHAUSTIVE_WORK_STATE.json',W/'EXHAUSTIVE_WORK_STATE.json')
f=read(V/'research/full-study/WORK_STATE.json');h=next(x for x in f['items']if x['id']=='bazi');h['completed'].append(summary);h.update(latestScope=summary,latestResearchReport='v53/'+report,nextFile='v53/research/bazi-branch-clash/WORK_STATE.json');f['latestResearchReport']='v53/'+report;f['exhaustiveNext']=[nextline,*f['exhaustiveNext']];write(V/'research/full-study/WORK_STATE.json',f)
p=V/'research/library-current/TMTH002_NATIVE_POSITION_COVERAGE.json';m=read(p)
for name,positions in [('bazi-branch-penalty',list(range(214,228))),('bazi-branch-clash',list(range(227,233)))]:m['scopes'].append({'scope':name,'evidence':identity(V/'research'/name/'NATIVE_REVIEW.json'),'positions':positions})
seen=sorted({i for s in m['scopes']for i in s['positions']});assert len(seen)==86
m.update(scope='Union of nine explicit scope records; first-pass position viewing only, not all glyphs or rules. End-of-volume reading is not whole-volume coverage.',distinctPositionsViewed=seen,distinctViewedCount=len(seen),remainingNotEstablishedByThisIndex=[i for i in range(1,233)if i not in seen],remainingCount=232-len(seen),duplicateScopePositionClaimsNotCountedTwice=sum(len(x['positions'])for x in m['scopes'])-len(seen));write(p,m)
c=read(V/'research/library-current/COVERAGE.json');c['latestFollowup']=summary;c['latestAcquisitionCounts']={'scope':report,'newHTTPBodies':0,'newOriginalContainers':0,'newIndependentWitnesses':0,'firstPassPositionsNewlyIntegratedThisBatch':23,'newVolume2Positions':18,'volume5SelectedContextPositions':5,'actualTableQueriesNewThisBatch':24,'actualCalendarObjects':0,'actualNatalCharts':0,'wholeWorksApplied':0}
evidence=['v53/'+report]
for name in scopes:evidence.extend([f'v53/research/{name}/WORK_STATE.json',f'v53/research/{name}/MANUAL_SOURCE_TABLES.json',f'v53/qa/{name}/SOURCE_RESULTS.json',f'v53/qa/{name}/REFERENCE_RESULTS.json',f'v53/qa/{name}/RELEASE_RESULTS.json'])
for path in evidence:
 if path not in c['evidenceFiles']:c['evidenceFiles'].append(path)
for x in c['catalogue']:
 if x['id']=='M01':
  for path in evidence:
   if path not in x['currentEvidence']:x['currentEvidence'].append(path)
  x['latestPenaltyOfficialClashResearch']={'report':'v53/'+report,'editorialUnits':99,'wholeChaptersApplied':False,'wholeWorkApplied':False,'consumerChanged':False}
for x in c['features']:
 if x['id']=='bazi':x['latestPenaltyOfficialClashResearch']={'report':'v53/'+report,'wholeWorkApplied':False,'consumerChanged':False}
write(V/'research/library-current/COVERAGE.json',c)
prefix='Mốc29/10/2026 — '+report+'\n\n'+summary+'\n\nTiếp: '+nextline+'\n\n'
for p in [V/'NEXT_STEPS.md',V/'research/library-current/COVERAGE.md',W/'PROJECT_RESEARCH_STATE.md',W/'WORK_RESUME.md']:p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
p=W/'PENDING_RESEARCH_STATE.json';d=read(p);d['previousReleaseBeforePenaltyOfficialClash']=d['latestReleaseVerified'];d.update(status='penalty-official-clash-research-integrated;package-verification-external',workDirectory='v53/research/bazi-branch-clash',currentWorkState='v53/research/bazi-branch-clash/WORK_STATE.json',latestReport='v53/'+report,inProgressStaging=None);d['latestReleaseVerified']={'researchChecksPassed':True,'report':'v53/'+report,'consumerChanged':False,'releasedTMTH002DistinctNativePositions':86,'wholeCatalogueCompleted':False,'comprehensivePackageVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json'}
d['historicalNextBeforePenaltyOfficialClash']=d['next'];d['next']=[nextline,*[x for x in d['next']if not x.startswith(('Nhánh độc lập真官','Tiếp論三刑'))]];write(p,d)
tests=['v53/research/bazi-branch-union/test-union-reference.mjs','v53/research/bazi-branch-triad/test-triad-reference.mjs','v53/research/bazi-triad-stars/test-star-reference.mjs','v53/research/bazi-branch-harm/test-harm-reference.mjs','v53/research/bazi-true-ghost-context/test-official-context.mjs','v53/research/bazi-branch-penalty/test-penalty-reference.mjs','v53/research/bazi-branch-clash/test-clash-reference.mjs']
write(R/'CURRENT_BATCH.json',{'report':'v53/'+report,'scopes':scopes,'tests':tests,'expectedTMTH002DistinctPositions':86,'expectedTMTH002RemainingPositions':146,'editorialUnits':99,'newActualTableQueries':24,'newCalendarObjects':0,'wholeCatalogueCompleted':False,'next':nextline})
write(R/'WORKING_FOLLOWUP.json',{'status':'previous-private-followup-integrated-with-penalty-and-clash','currentBatch':'recovery/research-release/CURRENT_BATCH.json','previousRecordPreservedBySHA':'recovery/consolidated-history/INDEX.sqlite#revisions','wholeCatalogueCompleted':False,'consumerChanged':False})
print(json.dumps({'researchScopesIntegrated':3,'editorialUnits':99,'tmth002NativePositionUnion':86,'newTableQueriesRetained':24,'noFullSnapshotCreated':True,'consumerChanged':False}))
