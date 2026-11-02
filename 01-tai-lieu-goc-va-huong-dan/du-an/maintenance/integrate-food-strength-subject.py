"""Adopt the C13/C14 bounded source modules and fork the pinned parent matrix."""
from pathlib import Path
from hashlib import sha256
import json,shutil,subprocess,sys
W=Path(__file__).resolve().parent.parent;V=W/'v53';F=W/'recovery/research-release'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def identity(p):return {'file':p.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
specs=[('bazi-food-strength','tmp/bazi-food-strength-staging','strength-reference.mjs','FOOD-00-C13'),
       ('bazi-food-luck-subject','tmp/bazi-food-luck-subject-staging','subject-reference.mjs','FOOD-00-C14')]
assert read(W/'recovery/storage-consolidation/MAINTENANCE.json')['status']=='complete'
assert not(W/'Huyen_Hoc_Cac_V53_source.pending.zip').exists() and not(W/'archives').exists()
for name,stage,module,parent in specs:
 assert not(V/'research'/name).exists() and not(V/'qa'/name).exists()
 assert read(W/stage/'SOURCE_RESULTS.json')['passed'] and read(W/stage/'REFERENCE_RESULTS.json')['passed']
oldpaths=['PROJECT_RESEARCH_STATE.md','WORK_RESUME.md','PENDING_RESEARCH_STATE.json','EXHAUSTIVE_WORK_STATE.json',
 'v53/research/EXHAUSTIVE_WORK_STATE.json','v53/research/full-study/WORK_STATE.json','v53/research/library-current/COVERAGE.json',
 'v53/research/library-current/COVERAGE.md','v53/NEXT_STEPS.md','v53/PACKAGE_MANIFEST.json',
 'recovery/research-release/CURRENT_BATCH.json','POST_RELEASE_WORKING_FOLLOWUP.json']
subprocess.run([sys.executable,str(W/'maintenance/preserve-selected-history.py'),*oldpaths],check=True)
report='BAZI_FOOD_STRENGTH_SUBJECT_REPORT.md'
summary=('Thực thần C13/C14: tách điều kiện nguồn Giáp/Bính/Hỏa/Thổ và chủ ngữ các pha Canh/Nhâm/Giáp. '
 'C13 có6cụm chọn/99codepoint, bộ quét đủ bốn trụ hoặc null tìm đúng壬癸亥子; thiếu trụ không thành vắng, '
 'không suy hiệu lực nước hoặc vượng suy từ chữ/mùa/phương vận. Sinh旺向祿 giữ điều kiện ghép với chủ ngữ chưa chốt. '
 'C14 giữ chủ ngữ dài đầu chưa rõ, bốn câu sau đúng chủ ngữ riêng;敗→沐浴 chỉ dưới chính sách giọng SanmingTiyao được nêu. '
 '16nhóm/385khung/4564bất biến null đạt. Bốn getDiShi đã chạy ở nhịp riêng trước được giữ, tái dùng2tọa độ pha '
 'và1cặp Thực thần HHC/lunar từ batch cũ;0gọi engine lúc tích hợp,0lá số/lịch/HTTP/vị trí mới. '
 'Ma trận90cha nay46liên kết phần/44chưa/0áp trọn; bản44/46 cũ giữ nguyên SHA để kiểm lịch sử. '
 'Nguồn/QA ngoài site, HTML và ZIPweb nguyên byte; toàn kho còn mở.')
nextline=('Tiếp FOOD-00-C16: giải thích hóa khí theo giọng希尹, giữ khác quan hệ Thập thần, kiểm chữ巳/己 bằng ảnh005-87b đã giữ. '
 'C13 hiệu lực/căn khí và chủ ngữ生旺向祿, C14長生/nghĩa金庫/toàn vận, các cha chưa liên kết vẫn mở. '
 'Không chạy lại4tọa độ mới/2tọa độ tái dùng hoặc11+11+5truy vấn C07. Luân phiên B02/P08/Tửvi khi hướng này bị tắc.')
stage=W/specs[0][1]
write(stage/'WORK_STATE.json',{'date':'2026-10-30','status':'bounded-C13-premise-reference-verified;whole-source-open',
 'catalogueID':'M01','parentContext':'FOOD-00-C13','sourceReading':'MANUAL_PREMISES.json','reference':'strength-reference.mjs',
 'sourceVerification':'SOURCE_RESULTS.json','referenceVerification':'REFERENCE_RESULTS.json','sourceClausesSelected':6,
 'newEngineCalls':0,'retainedActualFoodPairReused':1,'newHTTPBodies':0,'newSourcePositions':0,'consumerChanged':False,
 'wholeContextApplied':False,'wholeCatalogueCompleted':False,'next':nextline})
matrix=read(V/'research/bazi-food-chain/CURRENT_CONTEXT_COVERAGE.json')
previous=identity(V/'research/bazi-food-chain/CURRENT_CONTEXT_COVERAGE.json')
assert matrix['counts']['parentsWithSelectedModuleOrDeclaredPremiseLinks']==44
matrix['date']='2026-10-30';matrix['previousMatrix']=previous['file'];matrix['previousMatrixSHA256']=previous['sha256']
matrix['previousCounts']=matrix['counts'].copy();matrix['previousCountingCorrection']=matrix['countingCorrection']
for name,st,module,parent in specs:
 row=next(x for x in matrix['records'] if x['id']==parent);assert row['selectedModuleLinks']==[] and not row['wholeContextApplied']
 row['selectedModuleLinks'].append({'module':f'v53/research/{name}/{module}','sha256':identity(W/st/module)['sha256'],
  'scope':'Selected explicit source premises/subjects only; no full-context rule, grammar adjudication or efficacy.',
  'wholeContextApplied':False})
matrix['counts'].update(parentsWithSelectedModuleOrDeclaredPremiseLinks=46,parentsWithoutSuchLinks=44,previousScopeLinkedParents=44,newStrengthAndSubjectParents=2)
matrix['summary'].update(parentsWithSelectedModuleOrDeclaredPremiseLinks=46,otherParentsWithoutSuchLinks=44,
 countingBasis='44 previously linked parents plus C13 selected strength premises and C14 named source-coordinate inspection; not46whole rules.')
matrix['countingCorrection']='44 previous partial links +2selected C13/C14 modules;46partial links,44unlinked,0wholeparents.'
assert sum(bool(x['selectedModuleLinks']) for x in matrix['records'])==46
assert sum(bool(x['wholeContextApplied']) for x in matrix['records'])==0
write(stage/'CURRENT_CONTEXT_COVERAGE.json',matrix)
for name,st,module,parent in specs:
 s=W/st;d=V/'research'/name;q=V/'qa'/name
 write(s/'RELEASE_ADOPTION.json',{'date':'2026-10-30','status':'bounded-source-reference-integrated;whole-context-open',
 'catalogueID':'M01','parentContext':parent,'historicalPrivateStatePreserved':name=='bazi-food-luck-subject',
 'priorSourceResultsReferenceHistoricalUnlinkedMatrix':True,
 'currentParentMatrix':'v53/research/bazi-food-strength/CURRENT_CONTEXT_COVERAGE.json',
 'currentPartialLinkedParents':46,'unlinkedParents':44,'wholeParentsApplied':0,
 'latestResearchReport':'v53/'+report,'packageVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json',
 'newEngineCallsThisIntegration':0,'consumerChanged':False,'wholeCatalogueCompleted':False})
 shutil.copytree(s,d);q.mkdir(parents=True)
 identities=[]
 for p in sorted(s.iterdir()):
  if p.is_file():
   target=d/p.name;assert target.read_bytes()==p.read_bytes()
   identities.append({'source':p.relative_to(W).as_posix(),'target':target.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':identity(p)['sha256']})
 for n in ['SOURCE_RESULTS.json','REFERENCE_RESULTS.json']:shutil.copy2(s/n,q/n)
 write(q/'PROMOTION_IDENTITIES.json',{'byteExactFiles':identities,'noWholeSnapshotCreated':True})
 write(q/'RELEASE_RESULTS.json',{'status':'source-and-reference-verified;package-verification-external',
 'checks':[read(s/n) for n in ['SOURCE_RESULTS.json','REFERENCE_RESULTS.json']],
 'historicalFrozenParentMatrix':previous,'currentParentMatrix':'v53/research/bazi-food-strength/CURRENT_CONTEXT_COVERAGE.json',
 'consumerChanged':False,'wholeCatalogueCompleted':False,'packageVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json'})
body='''# Thực thần: điều kiện vượng suy và đúng chủ ngữ

'''+summary+'''

## C13 — điều kiện nguồn không phải bảng chấm sức mạnh

Nguồn số Kanripo WYG và ảnh CADAL06066041/005-86a đã giữ được dùng theo giọng lời dẫn `又曰`. Sáu cụm được chọn trước triển khai, không coi99codepoint là mọi nghĩa đã giải quyết. Crop đầu thiếu cột mở được giữ là trial; crop hoàn chỉnh native được xem và khớp RGB. Không có vị trí nguồn hay truyền bản độc lập mới. Chữ số `巳身`/`戊巳` giữ nguyên byte; bản đọc làm việc từ ảnh `己身`/`戊己` nằm riêng trong ledger.

`inspectFoodStrengthContext` buộc nguồn, khung, bốn trụ đúng cặp can–chi hoặc null, mùa/phương vận theo từ vựng nguồn được khai báo và bảy tiền đề boolean/null. Bộ quét đánh dấu cả vị trí trụ và can/chi của壬癸亥子. Có chữ là có tọa độ chữ; thiếu trụ không chứng minh vắng. Không tự đọc tàng can hoặc suy hiệu lực của水氣 từ tập chữ ấy.

Khung điều kiện tiếp nối cần khai báo không bị nước chế và cả cụm生旺向祿 đã được thỏa; chủ ngữ của cụm vẫn null. Nhánh mùa hạ cần riêng夏月/東南/Hỏa vượng/Thổ vượng. Nhánh ba tháng xuân tách甲旺,丙火得生 và戊巳氣薄; nhánh tiếp nối cần南方/火土俱旺, không đồng nhất東南với南方. Các phép nối ba giá trị chỉ kiểm sự khớp tiền đề được khai báo, không chứng thực dùng Tài dày, phát phúc hoặc hiệu lực cách cục. Bốn trụ trong test là ví dụ cấu trúc, không phải ca lịch sử hay chart đã dựng.

Một cặp甲→丙 thật của batch C07 được tái dùng nguyên payload HHC `Thực Thần`/lunar1.8.6 `食神`; kiểm SHA engine, bảng quan hệ và thư viện. Không chạy lại11+11+5truy vấn cũ. Mười nhóm kiểm C13 gồm11ca kỳ vọng freeze,240lượt quét mọi trụ chuẩn ở bốn vị trí,16mẫu thiếu trụ,81tổ hợp điều kiện hạ và kiểm phân biệt chủ ngữ/miền/đầu vào.371khung/4452bất biến null đạt;0engine trong test.

## C14 — chủ ngữ pha và lựa chọn từ vựng có tên

Giữ `庚以壬為食長生於申` với chủ ngữ長生 chưa được văn pháp phân định. Hai giả thuyết khai báo壬/庚 được đối chiếu riêng:壬申長生 là tọa độ cũ tái dùng,庚申臨官 là đối giả thuyết biên tập; sự khớp engine không quyết định chữ nguồn. Các câu sau có chủ ngữ壬酉敗,庚子死,甲子敗,甲丑冠帶; không gán cả bốn về nhật chủ庚.

Bốn truy vấn getDiShi thật đã lưu ở nhịp riêng trước:壬酉沐浴/甲子沐浴/甲丑冠带/庚申临官. Hai tọa độ壬申长生/庚子死 tái dùng batch cũ. Các lời gọi này dùng stem-carrier của hàm thư viện, không có natal/calendar object. Không thực thi lại khi tiếp nhận. `敗` chỉ được so `沐浴` khi người gọi chọn chính sách có tên theo giọng reported-SanmingTiyao có neo `五曰沐浴又曰敗`; giọng literal-only giữ so sánh chưa rõ. Không nhận equivalence toàn pha hoặc mọi chữ敗. Sáu nhóm kiểm/14khung/112bất biến null đạt.

SOURCE_RESULTS/WORK_STATE/REFERENCE_CONTINUATION của C14 ở mốc riêng còn ghi44/46/unlinked. Đó là lịch sử freeze đã giữ nguyên; RELEASE_ADOPTION và ma trận mới mới là trạng thái tiếp nhận hiện hành. Ma trận cũ nằm ở bazi-food-chain không bị sửa vì nhiều kiểm lịch sử ghim byte. Ma trận mới thêm đúng hai liên kết có SHA và vẫn giữ mọi cờ wholeContextApplied=false.

## Đồng bộ và phạm vi còn mở

Hai mô-đun, QA, báo cáo và ma trận được tiếp nhận trong V53; nguồn/corpus/engine comparison không đưa vào consumer. HTML/site/webZIP giữ nguyên byte, không tạo snapshot toàn ZIP, không động lịch sử chat. ZIP nguồn tổng hợp chỉ được gọi đã đồng bộ khi FINAL_VERIFICATION.json khớp manifest và report này; trước đó audit chỉ xác nhận mốc cũ.

Chưa tính tổng vượng suy, căn khí, hiệu lực sinh Tài, lịch/vận thật, 金之庫, chữ己丑 hoặc kết quả dự báo. Hai parent có liên kết phần không đồng nghĩa hai quy tắc đầy đủ. Không tuyên bố toàn kho xong.

Tiếp: '''+nextline+'\n'
(V/report).write_text(body,encoding='utf-8')
e=read(V/'research/EXHAUSTIVE_WORK_STATE.json');e['previousTuviDipperWork']=e['currentWork'];e['date']='2026-10-30'
e['currentWork']={'catalogueIDs':['M01'],'work':'Thực thần:C13điều kiện/C14chủ ngữ pha','sourceDirectory':'v53/research/bazi-food-strength',
 'currentStep':summary,'latestResearchReport':report,'currentFoodMatrix':'v53/research/bazi-food-strength/CURRENT_CONTEXT_COVERAGE.json','wholeWorkApplied':False}
e['inProgressScope']={'status':'bounded-food-premises-and-subjects-integrated;package-verification-external','packageVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json'}
e['subsequentPriority']=[nextline,*e['subsequentPriority']];write(V/'research/EXHAUSTIVE_WORK_STATE.json',e);shutil.copy2(V/'research/EXHAUSTIVE_WORK_STATE.json',W/'EXHAUSTIVE_WORK_STATE.json')
f=read(V/'research/full-study/WORK_STATE.json');f['latestResearchReport']='v53/'+report;f['exhaustiveNext']=[nextline,*f['exhaustiveNext']]
x=next(x for x in f['items'] if x['id']=='bazi');x['completed'].append(summary);x.update(latestScope=summary,latestResearchReport='v53/'+report,nextFile='v53/research/bazi-food-strength/RELEASE_ADOPTION.json');write(V/'research/full-study/WORK_STATE.json',f)
c=read(V/'research/library-current/COVERAGE.json');c['date']='2026-10-30';c['latestFollowup']=summary
c['latestAcquisitionCounts']={'scope':report,'newHTTPBodiesThisIntegration':0,'newOriginalContainers':0,'newSourceImages':0,
 'newSourcePositions':0,'newIndependentEditions':0,'newEngineCallsThisIntegration':0,'previousPrivateActualPhaseCallsAdopted':4,
 'retainedPhaseCoordinatesReused':2,'retainedActualHHCAndLunarFoodPairReused':1,'wholeWorksApplied':0}
evidence=['v53/'+report,'v53/research/bazi-food-strength/CURRENT_CONTEXT_COVERAGE.json']
for name,st,module,parent in specs:evidence.extend([f'v53/research/{name}/RELEASE_ADOPTION.json',f'v53/research/{name}/{module}',f'v53/qa/{name}/RELEASE_RESULTS.json'])
m=next(x for x in c['catalogue'] if x['id']=='M01');m['previousFoodParentContextSelectionBeforeStrengthSubject']=m['foodParentContextSelection']
m['foodParentContextSelection']={'total':90,'parentsWithSelectedModuleOrDeclaredPremiseLinks':46,'otherParentsWithoutSuchLinks':44,'wholeParentsApplied':0,
 'allSelectedParentsSubsidiaryClausesApplied':False,'countingBasis':matrix['countingCorrection'],'currentMatrix':'v53/research/bazi-food-strength/CURRENT_CONTEXT_COVERAGE.json','printedCaseAuditDoesNotAddImplementedRule':True}
scope={'report':'v53/'+report,'selectedParents':['FOOD-00-C13','FOOD-00-C14'],'referenceGroups':16,'declaredInspectionFrames':385,'wholeContextApplied':False,'consumerChanged':False}
m['latestFoodStrengthSubjectScope']=scope;next(x for x in c['features'] if x['id']=='bazi')['latestFoodStrengthSubjectScope']=scope
for p in evidence:
 if p not in c['evidenceFiles']:c['evidenceFiles'].append(p)
 if p not in m['currentEvidence']:m['currentEvidence'].append(p)
write(V/'research/library-current/COVERAGE.json',c)
prefix='Mốc30/10/2026 — '+report+'\n\n'+summary+'\n\nTiếp: '+nextline+'\n\n'
for p in [V/'NEXT_STEPS.md',V/'research/library-current/COVERAGE.md']:p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
for p in [W/'PROJECT_RESEARCH_STATE.md',W/'WORK_RESUME.md']:
 old=p.read_text(encoding='utf-8-sig');base=old[old.index('Đọc STORAGE_POLICY.md'):]
 base=base.replace('Mốc phát hành: v53/TUVI_DIPPER_WINDOWS_REPORT.md.','Mốc phát hành: v53/'+report+'.')
 p.write_text('# Tiếp tục Huyền Học Các\n\nTrạng thái toàn kho: đang làm, chưa hoàn thành. Nguồn và QA ngoài site; không xuất bản mạng.\n\n'+prefix+base,encoding='utf-8')
p=W/'PENDING_RESEARCH_STATE.json';d=read(p);d['previousReleaseBeforeFoodStrengthSubject']=d['latestReleaseVerified']
d.update(date='2026-10-30',status='food-strength-subject-integrated;package-verification-external',workDirectory='v53/research/bazi-food-strength',
 currentWorkState='v53/research/bazi-food-strength/RELEASE_ADOPTION.json',latestReport='v53/'+report,inProgressStaging=None,integrationInProgress=False,nextIndependentScope=nextline)
d['latestReleaseVerified']={'researchChecksPassed':True,'report':'v53/'+report,'consumerChanged':False,'wholeCatalogueCompleted':False,'comprehensivePackageVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json'}
d['next']=[nextline,*d['next']];d['currentScopeChecks']={'date':'2026-10-30','scopes':{name:{n:read(W/st/n)for n in ['SOURCE_RESULTS.json','REFERENCE_RESULTS.json']}for name,st,module,parent in specs},
 'newReferenceGroups':16,'newEngineCallsDuringVerification':0,'newSourcePositions':0,'consumerChanged':False,'wholeCatalogueCompleted':False,
 'packageVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json'};write(p,d)
batch=read(F/'CURRENT_BATCH.json');batch.update(report='v53/'+report,scopes=[x[0]for x in specs],next=nextline,
 sourceCounters=c['latestAcquisitionCounts'],newActualTableQueries=0,retainedActualCastQueries=0)
batch['tests'].extend(['v53/research/bazi-food-strength/test-strength-reference.mjs','v53/research/bazi-food-luck-subject/test-subject-reference.mjs']);write(F/'CURRENT_BATCH.json',batch)
write(W/'POST_RELEASE_WORKING_FOLLOWUP.json',{'date':'2026-10-30','status':'prior-private-C13-C14-integrated;next-source-C16-open','releasedReport':'v53/'+report,
 'currentBatch':'recovery/research-release/CURRENT_BATCH.json','releasedPackageAudit':'recovery/research-release/FINAL_VERIFICATION.json',
 'currentMatrix':'v53/research/bazi-food-strength/CURRENT_CONTEXT_COVERAGE.json','parentCoverageCounts':[46,44,0],
 'packageBoundary':'Research files integrated; comprehensive package is only verified when external audit matches this report/manifest.',
 'next':nextline,'consumerChanged':False,'wholeCatalogueCompleted':False})
print(json.dumps({'integratedScopes':[x[0]for x in specs],'newReferenceGroups':16,'currentMatrixCounts':[46,44,0],'newEngineCallsDuringIntegration':0,'consumerChanged':False,'noWholeSnapshotCreated':True}))
