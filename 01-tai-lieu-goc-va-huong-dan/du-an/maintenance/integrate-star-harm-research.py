"""Integrate one useful research batch under the consolidated storage policy."""
from pathlib import Path
from hashlib import sha256
import json,shutil
W=Path(__file__).resolve().parent.parent;V=W/'v53'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def identity(p):return {'file':p.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
assert read(W/'recovery/storage-consolidation/MAINTENANCE.json')['status']=='complete'
assert not (W/'archives').exists(),'Do not recreate historical whole-package snapshots.'
html=sha256((W/'Huyen_Hoc_Cac.html').read_bytes()).hexdigest();assert html=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
for name in ['bazi-triad-stars','bazi-branch-harm']:
 s=W/'tmp'/f'{name}-staging';r=V/'research'/name;q=V/'qa'/name
 assert read(s/'SOURCE_RESULTS.json')['passed'] and read(s/'REFERENCE_RESULTS.json')['passed']
 assert not r.exists() and not q.exists()
 state=read(s/'WORK_STATE.json');state.update(integratedIntoRelease=True,integrationKind='research-only;consumer-unchanged',packageVerificationPointer='recovery/research-release/FINAL_VERIFICATION.json')
 state['next']=['Continue論三刑 at214 already viewed as boundary; inspect215 onward.','Resolve true-five-element/true-ghost source roles with native context before a calendar adapter.','Keep one latest comprehensive package; do not create archives/v53-before-* or repeat retained engine queries.']
 write(s/'WORK_STATE.json',state);shutil.copytree(s,r);q.mkdir(parents=True)
 pairs=[]
 for p in sorted(s.iterdir()):
  if p.is_file():
   dst=r/p.name;assert dst.read_bytes()==p.read_bytes();pairs.append({'source':p.relative_to(W).as_posix(),'target':dst.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()})
 for filename in ['SOURCE_RESULTS.json','REFERENCE_RESULTS.json']:shutil.copy2(s/filename,q/filename)
 write(q/'PROMOTION_IDENTITIES.json',{'byteExactFiles':pairs,'noFullSnapshotCreated':True})
 write(q/'RELEASE_RESULTS.json',{'status':'source-and-reference-verified;comprehensive-package-verification-external','consumerChanged':False,'sourceChecks':read(s/'SOURCE_RESULTS.json'),'referenceTests':read(s/'REFERENCE_RESULTS.json'),'packageVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json','historicalStatePreservation':'recovery/consolidated-history/INDEX.sqlite#revisions','wholeWorkApplied':False})
summary='Tam Mệnh quyển2: tích hợp nghiên cứu將星華蓋/咸池/六害 trong một batch. 11vị trí native204–214 riêng;9đọc đầu mới vào bản hiện hành(4từstaging cũ/5mới lượt này),209 chia sẻ. 71đơn vị biên tập/1616codepoint/1621UTF16,không71quy tắc hoàn chỉnh. Hàm tọa độ sao,điều kiện咸池 và ba hàm Lục hại giữ cặp danh nghĩa/chiều nguồn/bốn tiền đề khai báo/ví dụ乙酉→戊戌. Không ghi đè戌→酉無災 bằng hình học hợp-xung. 20truy vấn bảng đã giữ(4cũ/16mới),12Lục hợp tái dùng,0lá số. Hai bộ8+9nhóm kiểm và source checks đạt;nguồn/QA ngoài site,HTML/web nguyênbyte. Quyển2 hiện68/232vị trí xem đầu theo chỉ mục,164chưa xác lập;toànkho vẫn mở.'
nextline='Tiếp論三刑 từ214 đã xem ranh;215trở đi chưa đọc trong phạm vi này. Giữ các tên刑 theo từng giọng,đừng lấy nhãn dân gian hiện hành ghi đè nguồn. Đầu mối真五行/真鬼 quyển5/10 mới là bản số chưa đối ảnh;không tự ghép Nạp âm,Thập thần hoặc hành can. Không gọi lại20truy vấn bảng/12Lục hợp đã giữ.'
report=V/'BAZI_STARS_HARMS_REPORT.md'
report.write_text('# Tam Mệnh: 將星華蓋, 咸池 và 六害\n\n'+summary+'\n\n'+(V/'research/bazi-triad-stars/README.md').read_text(encoding='utf-8').split('\n',1)[1]+'\n\n'+(V/'research/bazi-branch-harm/README.md').read_text(encoding='utf-8').split('\n',1)[1]+'\n\n## Lưu trữ và kiểm hiện hành\n\nKhông giữ full ZIP trước sửa. Nội dung trạng thái/manifest trước thay đổi đã được gom theo SHA-256 tại chỉ mục lịch sử và bảng revisions. Mỗi thư mục nghiên cứu có PROMOTION_IDENTITIES trong QA. Dùng maintenance/verify-current.py và recovery/research-release/FINAL_VERIFICATION.json; các lệnh snapshot trong báo cáo cũ chỉ là lịch sử. Staging được tiếp nhận đúng byte; các hướng dẫn tạo snapshot cũ bên trong README được thay bởi STORAGE_POLICY.md.\n\nTiếp: '+nextline+'\n',encoding='utf-8')
e=read(V/'research/EXHAUSTIVE_WORK_STATE.json');e['previousBranchCombinationWork']=e['currentWork'];e['currentWork']={'catalogueIDs':['M01'],'work':'Tam Mệnh: 將星華蓋/咸池/六害 theo nguồn','sourceDirectories':['v53/research/bazi-triad-stars','v53/research/bazi-branch-harm'],'currentStep':summary,'latestResearchReport':report.name,'sourceLimits':read(V/'research/bazi-branch-harm/WORK_STATE.json')['sourceLimits'],'wholeWorkApplied':False};e['subsequentPriority']=[nextline,*e['subsequentPriority']];e['inProgressScope']={'status':'three-chapter-selected-research-integrated','finalVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json'};write(V/'research/EXHAUSTIVE_WORK_STATE.json',e);shutil.copy2(V/'research/EXHAUSTIVE_WORK_STATE.json',W/'EXHAUSTIVE_WORK_STATE.json')
f=read(V/'research/full-study/WORK_STATE.json');h=next(x for x in f['items'] if x['id']=='bazi');h['completed'].append(summary);h.update(latestScope=summary,latestResearchReport='v53/'+report.name,nextFile='v53/research/bazi-branch-harm/WORK_STATE.json');f['latestResearchReport']='v53/'+report.name;f['exhaustiveNext']=[nextline,*f['exhaustiveNext']];write(V/'research/full-study/WORK_STATE.json',f)
c=read(V/'research/library-current/COVERAGE.json');c['latestFollowup']=summary;c['latestAcquisitionCounts']={'scope':report.name,'newHTTPBodies':0,'newOriginalContainers':0,'newIndependentWitnesses':0,'firstPassPositionsNewlyIntegrated':9,'newPositionsActuallyViewedThisTurn':5,'actualTableQueriesNewThisTurn':16,'previousStagedTableQueriesReused':4,'priorUnionQueriesReused':12,'newCalendarObjects':0,'newNatalCharts':0,'wholeWorksApplied':0}
evidence=['v53/'+report.name]
for name in ['bazi-triad-stars','bazi-branch-harm']:
 evidence.extend([f'v53/research/{name}/WORK_STATE.json',f'v53/research/{name}/CHAPTER_DISPOSITIONS.json',f'v53/qa/{name}/SOURCE_RESULTS.json',f'v53/qa/{name}/REFERENCE_RESULTS.json',f'v53/qa/{name}/RELEASE_RESULTS.json'])
for path in evidence:
 if path not in c['evidenceFiles']:c['evidenceFiles'].append(path)
for x in c['catalogue']:
 if x['id']=='M01':
  for path in evidence:
   if path not in x['currentEvidence']:x['currentEvidence'].append(path)
  x['latestStarsHarmsResearch']={'report':'v53/'+report.name,'editorialUnits':71,'wholeChaptersApplied':False,'wholeWorkApplied':False,'consumerChanged':False}
for x in c['features']:
 if x['id']=='bazi':x['latestStarsHarmsResearch']={'report':'v53/'+report.name,'wholeWorkApplied':False,'consumerChanged':False}
write(V/'research/library-current/COVERAGE.json',c)
p=V/'research/library-current/TMTH002_NATIVE_POSITION_COVERAGE.json';m=read(p)
for name,positions in [('bazi-triad-stars',list(range(204,210))),('bazi-branch-harm',list(range(209,215)))]:m['scopes'].append({'scope':name,'evidence':identity(V/'research'/name/'NATIVE_REVIEW.json'),'positions':positions})
seen=sorted({i for scope in m['scopes'] for i in scope['positions']});assert len(seen)==68
m.update(scope='Union of seven explicitly indexed scope records; first-pass position viewing only, not all glyphs or rules.',distinctPositionsViewed=seen,distinctViewedCount=len(seen),remainingNotEstablishedByThisIndex=[i for i in range(1,233) if i not in seen],remainingCount=232-len(seen),duplicateScopePositionClaimsNotCountedTwice=sum(len(x['positions']) for x in m['scopes'])-len(seen));write(p,m)
prefix='Mốc29/10/2026 — '+report.name+'\n\n'+summary+'\n\nTiếp: '+nextline+'\n\n'
for p in [V/'NEXT_STEPS.md',V/'research/library-current/COVERAGE.md',W/'PROJECT_RESEARCH_STATE.md',W/'WORK_RESUME.md']:p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
p=W/'PENDING_RESEARCH_STATE.json';d=read(p);d['previousReleaseBeforeStarsHarms']=d['latestReleaseVerified'];d.update(status='stars-harms-research-integrated;package-verification-external',workDirectory='v53/research/bazi-branch-harm',currentWorkState='v53/research/bazi-branch-harm/WORK_STATE.json',latestReport='v53/'+report.name,packageVerification='Read recovery/research-release/FINAL_VERIFICATION.json and compare its V53 manifest SHA-256 to the current manifest.',inProgressStaging=None)
d['latestReleaseVerified']={'researchChecksPassed':True,'report':'v53/'+report.name,'consumerChanged':False,'releasedTMTH002DistinctNativePositions':68,'wholeCatalogueCompleted':False,'comprehensivePackageVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json'};d['next']=[nextline,*d['next']];write(p,d)
assert sha256((V/'Huyen_Hoc_Cac.html').read_bytes()).hexdigest()==html==sha256((V/'site/index.html').read_bytes()).hexdigest()
print(json.dumps({'researchScopesIntegrated':2,'editorialUnits':71,'nativePositionUnion':68,'noFullSnapshotCreated':True,'consumerChanged':False}))
