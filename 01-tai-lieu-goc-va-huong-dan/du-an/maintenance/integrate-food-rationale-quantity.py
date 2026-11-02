"""Adopt three coherent food-source layers; preserve frozen historical maps and private states."""
from pathlib import Path
from hashlib import sha256
import json,subprocess,sys,shutil
W=Path(__file__).resolve().parent.parent;V=W/'v53';F=W/'recovery/research-release'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def h(p):return sha256(p.read_bytes()).hexdigest()
specs=[('bazi-food-transformation','transformation-reference.mjs','FOOD-00-C16','verify-source-runtime.py'),
 ('bazi-food-quantity','quantity-reference.mjs','FOOD-00-C23','verify-source.py'),
 ('bazi-food-fire-exception','fire-exception-reference.mjs','FOOD-00-C31','verify-source.py')]
assert read(W/'recovery/storage-consolidation/MAINTENANCE.json')['status']=='complete'
assert not(W/'Huyen_Hoc_Cac_V53_source.pending.zip').exists()and not(W/'archives').exists()
for name,module,parent,script in specs:
 b=W/f'tmp/{name}-staging';assert not(V/'research'/name).exists()and not(V/'qa'/name).exists()
 assert read(b/'SOURCE_RESULTS.json')['passed']and read(b/'REFERENCE_RESULTS.json')['passed']
oldpaths=['PROJECT_RESEARCH_STATE.md','WORK_RESUME.md','PENDING_RESEARCH_STATE.json','EXHAUSTIVE_WORK_STATE.json','POST_RELEASE_WORKING_FOLLOWUP.json',
 'v53/research/EXHAUSTIVE_WORK_STATE.json','v53/research/full-study/WORK_STATE.json','v53/research/library-current/COVERAGE.json',
 'v53/research/library-current/COVERAGE.md','v53/NEXT_STEPS.md','v53/PACKAGE_MANIFEST.json','recovery/research-release/CURRENT_BATCH.json']
subprocess.run([sys.executable,str(W/'maintenance/preserve-selected-history.py'),*oldpaths],check=True)
report='BAZI_FOOD_RATIONALE_QUANTITY_REPORT.md'
summary=('Thực thần C16/C23/C31: ba lớp nguồn riêng—vòng cặp hóa khí theo希尹, ví dụ lượng chữ theo壺中子 và điều kiện戊日庚時不宜火旺theo秘訣. '
 '22nhóm/695khung/8446bất biến null đạt. C16 so20tọa độ can:10食神/5正官/5正印, tái dùng14cặp và10bạn hợp,6HHC+6lunarđã chạy một lần ở mốc riêng; '
 'C23/C31 tái dùng hai chiếu cặp core,0engine lúc tiếp nhận. C23 xét chung các khả năng của trụ thiếu, không mất tương quan hoặc tự chọn nhật chủ; '
 'C31 chỉ điều kiện can ngày戊/can giờ庚và hiệu lực Hỏa khai báo, không cấm Hỏa toàn hệ. C19/C21/C30 giữ ledger chưa áp. '
 'Bốn crop native/5vị trí cũ đọc mở rộng,0HTTP/vị trí nguồn/lịch/chart mới. C31 có seal sau triển khai được ghi ngoại lệ rõ, không gọi freeze trước mã. '
 'Ma trận90cha49liên kết phần/41chưa/0áp trọn; bản46/44cũ giữ nguyênSHA. Web nguyên byte,toàn kho còn mở.')
nextline=('Tiếp C19/C21 đầy đủ điều kiện hiệu lực và danh sách福聚/禍聚; C22返哺 còn hướng gốc và nghĩa皆/adjacent-all, '
 'C30官còn正官hay官煞, C35còn12bài/điều kiện từng giọng. Không chọn năm/ngày, số lượng thành sức lực, hệ số3/giảm nửa hoặc đổi巳toàn kho. '
 'Không chạy lại6HHC/6lunar,14cặp/10bạn hợp của C16; không lặpC13/C14. Luân phiên B02/P08/Tửvi nếu hướng này tắc; toàn kho chưa hoàn tất.')
oldmap=V/'research/bazi-food-strength/CURRENT_CONTEXT_COVERAGE.json';matrix=read(oldmap)
assert matrix['counts']['parentsWithSelectedModuleOrDeclaredPremiseLinks']==46
matrix['previousMatrix']=oldmap.relative_to(W).as_posix();matrix['previousMatrixSHA256']=h(oldmap);matrix['previousCounts']=matrix['counts'].copy();matrix['previousCountingCorrection']=matrix['countingCorrection'];matrix['date']='2026-10-30'
for name,module,parent,script in specs:
 row=next(x for x in matrix['records']if x['id']==parent);assert row['selectedModuleLinks']==[]
 row['selectedModuleLinks'].append({'module':f'v53/research/{name}/{module}','sha256':h(W/f'tmp/{name}-staging'/module),
 'scope':'Named source layer and selected literal coordinates/premises only; not a full-context rule, strength method or outcome.', 'wholeContextApplied':False})
matrix['counts'].update(parentsWithSelectedModuleOrDeclaredPremiseLinks=49,parentsWithoutSuchLinks=41,previousScopeLinkedParents=46,newRationaleQuantityFireParents=3)
matrix['summary'].update(parentsWithSelectedModuleOrDeclaredPremiseLinks=49,otherParentsWithoutSuchLinks=41,countingBasis='46previouspartiallinks+3selectedC16/C23/C31modules;not49fullyappliedrules')
matrix['countingCorrection']='46previouspartiallinks+3selectedC16/C23/C31parents=49partiallinks,41unlinked,0wholeparents.'
assert sum(bool(x['selectedModuleLinks'])for x in matrix['records'])==49 and not any(x['wholeContextApplied']for x in matrix['records'])
write(W/'tmp/bazi-food-quantity-staging/CURRENT_CONTEXT_COVERAGE.json',matrix)
for name,module,parent,script in specs:
 b=W/f'tmp/{name}-staging';d=V/'research'/name;q=V/'qa'/name
 write(b/'RELEASE_ADOPTION.json',{'date':'2026-10-30','status':'bounded-source-layer-integrated;whole-context-open',
 'catalogueID':'M01','parentContext':parent,'historicalPrivateStatePreserved':True,
 'sourceChecksReferenceHistoricalUnlinkedMatrix':True,'currentParentMatrix':'v53/research/bazi-food-quantity/CURRENT_CONTEXT_COVERAGE.json',
 'currentPartialLinkedParents':49,'unlinkedParents':41,'wholeParentsApplied':0,'sourceSealSequenceException':name=='bazi-food-fire-exception',
 'allScopesHavePreimplementationFreeze':False,'latestResearchReport':'v53/'+report,
 'packageVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json','newEngineCallsThisIntegration':0,'consumerChanged':False,'wholeCatalogueCompleted':False})
 shutil.copytree(b,d);q.mkdir(parents=True);identities=[]
 for p in sorted(b.iterdir()):
  if p.is_file():
   t=d/p.name;assert t.read_bytes()==p.read_bytes();identities.append({'source':p.relative_to(W).as_posix(),'target':t.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':h(p)})
 for n in ['SOURCE_RESULTS.json','REFERENCE_RESULTS.json']:shutil.copy2(b/n,q/n)
 write(q/'PROMOTION_IDENTITIES.json',{'byteExactFiles':identities,'noWholeSnapshotCreated':True})
 write(q/'RELEASE_RESULTS.json',{'status':'source-and-reference-verified;package-verification-external','checks':[read(b/n)for n in ['SOURCE_RESULTS.json','REFERENCE_RESULTS.json']],
 'historicalPrivateStatePreserved':True,'sourceSealSequenceException':name=='bazi-food-fire-exception',
 'currentParentMatrix':'v53/research/bazi-food-quantity/CURRENT_CONTEXT_COVERAGE.json',
 'consumerChanged':False,'wholeCatalogueCompleted':False,'packageVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json'})
(V/report).write_text('''# Thực thần: tầng giải thích, lượng chữ và điều kiện Hỏa riêng

'''+summary+'''

## Nguồn và các lớp được chọn

Giữ bản số Kanripo WYG ghim commit và ảnh CADAL06066041 đã có byte/SHA. Ba parentC16/C23/C31là62/102/19codepoint;8chữ ở C31được chọn thành điều kiện ngày/giờ/Hỏa. Mọi chỉ số này là phạm vi chữ/điều kiện biên tập, không phải183quy tắc hay ba parentáp trọn. Năm vị trí176/177/178/179/181là đọc mở rộng, không trang hoặc nhân chứng mới; bốn crop native khớp RGB.

C16giữ tên quy thuộc希尹, chưa xác minh căn cước tác giả. Vòng chữ nguồn甲巳化土→丙辛化水→戊癸化火→庚乙化金→壬丁化木→甲巳giữ đúng thứ tự cặp. Chỉ chính sách được nêu rõ native-working-己mới bật bản đọc甲己ở đúng hai chỗ; literal-onlygiữ甲巳và để so can chưa rõ. Không emend mọi巳. Các hành hóa là lời nguồn, không phải đã hóa thực tế trong một mệnh cục.

So biên tập hai thành viên mỗi cặp với hai thành viên cặp đích cho20tọa độ:10Thực thần/5Chính quan/5Chính ấn. Đây không phải20phát biểu từng can được in trong nguồn và cũng không tự bác lời giải thích theo cặp/khí. Tái dùng14payload can thật và10bạn hợp từ core/C07/Đồng khoa/appendix/true-ghost; sáu tọa độ còn thiếu đã chạy đúng một lần6HHCgod+6bảnglunar1.8.6. Tiếp nhận và test không chạy lại. Bảng bạn hợp chỉ hỗ trợ nhận dạng cặp, không chứng thực hành hóa hoặc hiệu lực.

C23giữ giọng壺中子:甲人得兩丙三丙và柱中兩甲止有一丙. Gốc甲chưa có vai trò năm/ngày; đối tọa độ chữ không được ép về nhật chủ. Bốn trụ chuẩn hoặc nullcho miền số Giáp/Bính có ràng buộc chung bốn vị trí.甲+丙+丙+nullchắc còn haihoặcbaBínhdù hai đích đúnghai/đúngbađều riêng lẻ chưa rõ.甲+hai can khác+nullkhông thể đồng thời thêm đủ haiGiápvàmộtBính.256khung ký hiệu được kiểm bằng khai triển cách điền từng trụ, không dùng AND/ORđộc lập làm mất tương quan. Không tính tàng can hoặc suy nhiều/ít hiệu lực. C19/C21còn điều kiện và giọng riêng;福聚/禍聚/増培/減半không thành điểm/hệ số/phẩm chất con người. Chínđầu vào sai/sáukhung ngoài miền giữ riêng.

C31là lời秘訣có can ngày戊và can giờ庚rõ. API chỉ xét đúng hai vai trò và hiệu lực Hỏa khai báo; không suy Hỏa vượng từ mùa/chữ, không dựng giờ chi/lịch sinh và không coi khôngcó điều kiện bất lợi là tốt.363đầu vào hai can/null×Hỏa boolean/null được kiểm;8ca thủ công cho371khung. Không gộp thành cấm Hỏa cho mọi Thực thần hoặc ghi đè C13夏月/東南/火土俱旺. C30官và C31một vị còn chưa giải đầy đủ. C23/C31mỗi scope tái dùng một cặp core, hai phép chiếu này không tăng số tọa độ độc lập của C16.

## Trình tự niêm phong và ngoại lệ C31

C16có8tệp và C23có5tệp freeze trước triển khai. C23có một rà kỳ vọng trước mã về tương quan trụ thiếu, giữ ledger đầy đủ. C31đã ghi mã trước khi gọi freeze: guard từ chối đúng; test ban đầu không ghi bộ kết quả đạt vì thiếu freeze. Không xóa/di chuyển mã để vượt guard hoặc giả freeze trước mã. SOURCE_EXPECTATIONS_SEALcủa C31là seal sau triển khai với cờ rõ;8kỳ vọng và module không đổi sau lần chạy đầu. SEQUENCE_EXCEPTIONgiữ byte/SHA/thứ tự, ba script ban đầu được giữ trong chỉ mục SHA lịch sử. Verifier sau đó sửa lỗi so hậu tố tên làm trúng cả tệp test; bản trước sửa cũng được giữ. Kiểm hiện hành xác nhận nguyên source/expectation/module, crop RGB và toàn miền. Không gọi mọi scope đã freeze trước mã; ngoại lệ này chỉ tiếp nhận dưới dạng nghiên cứu nội bộ.

## Kiểm chứng và đồng bộ

Ba suite8+8+6nhóm,695khung/8446bất biến null đạt;0engine lúc kiểm. Ma trận mới49liên kết phần/41chưa/0áp trọn, chỉ thêmC16/C23/C31; bản46/44ởbazi-food-strengthgiữ nguyên vì các chứng cứ ghim byte. C19/C21/C30chỉ ledger, chưa thêm liên kết module. WORK_STATEvà các note riêng vẫn là lịch sử trước tiếp nhận; RELEASE_ADOPTIONlà trạng thái áp nhận hiện hành.

Nguồn/QA/đối engine ở ngoài site. HTML/site/webZIP giữ nguyên byte. Không tạo full snapshot hoặc phiên bản mới, chỉ thay nguyên tử một ZIP nguồn tổng hợp sau batch có ích này; lịch sử chat giữ nguyên. Chỉ gọi gói đã đồng bộ khi FINAL_VERIFICATIONkhớp report/manifest hiện hành; lúc đang dựng, audit cũ chỉ xác nhận mốc cũ. Chưa kiểm hiệu lực bói đoán, vượng suy trọn, lịch/giờ thật hoặc toàn tác phẩm.

Tiếp: '''+nextline+'\n',encoding='utf-8')
e=read(V/'research/EXHAUSTIVE_WORK_STATE.json');e['previousFoodStrengthSubjectWork']=e['currentWork'];e['date']='2026-10-30';e['currentWork']={'catalogueIDs':['M01'],'work':'Thực thần:C16cặp hóa khí/C23lượng chữ/C31điều kiện Hỏa riêng','sourceDirectory':'v53/research/bazi-food-quantity','currentStep':summary,'latestResearchReport':report,'currentFoodMatrix':'v53/research/bazi-food-quantity/CURRENT_CONTEXT_COVERAGE.json','wholeWorkApplied':False};e['inProgressScope']={'status':'three-food-source-layers-integrated;package-verification-external','packageVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json'};e['subsequentPriority']=[nextline,*e['subsequentPriority']];write(V/'research/EXHAUSTIVE_WORK_STATE.json',e);shutil.copy2(V/'research/EXHAUSTIVE_WORK_STATE.json',W/'EXHAUSTIVE_WORK_STATE.json')
f=read(V/'research/full-study/WORK_STATE.json');f['latestResearchReport']='v53/'+report;f['exhaustiveNext']=[nextline,*f['exhaustiveNext']];b=next(x for x in f['items']if x['id']=='bazi');b['completed'].append(summary);b.update(latestScope=summary,latestResearchReport='v53/'+report,nextFile='v53/research/bazi-food-quantity/RELEASE_ADOPTION.json');write(V/'research/full-study/WORK_STATE.json',f)
c=read(V/'research/library-current/COVERAGE.json');c.update(date='2026-10-30',latestFollowup=summary,latestAcquisitionCounts={'scope':report,'newHTTPBodiesThisIntegration':0,'newSourcePositions':0,'newIndependentEditions':0,'newEngineCallsThisIntegration':0,'previousPrivateHHCGodCallsAdopted':6,'previousPrivateLunarTableQueriesAdopted':6,'retainedComponentPairsReused':14,'retainedPartnerCoordinatesReused':10,'selectedFoodPairProjectionsReused':2,'nativeCrops':4,'wholeWorksApplied':0})
m=next(x for x in c['catalogue']if x['id']=='M01');m['previousFoodParentSelectionBeforeRationaleQuantity']=m['foodParentContextSelection'];m['foodParentContextSelection']={'total':90,'parentsWithSelectedModuleOrDeclaredPremiseLinks':49,'otherParentsWithoutSuchLinks':41,'wholeParentsApplied':0,'allSelectedParentsSubsidiaryClausesApplied':False,'countingBasis':matrix['countingCorrection'],'currentMatrix':'v53/research/bazi-food-quantity/CURRENT_CONTEXT_COVERAGE.json','printedCaseAuditDoesNotAddImplementedRule':True}
scope={'report':'v53/'+report,'selectedParents':[x[2]for x in specs],'referenceGroups':22,'inspectionFrames':695,'sourceSealSequenceExceptionC31':True,'wholeContextApplied':False,'consumerChanged':False};m['latestFoodRationaleQuantityScope']=scope;next(x for x in c['features']if x['id']=='bazi')['latestFoodRationaleQuantityScope']=scope
evidence=['v53/'+report,'v53/research/bazi-food-quantity/CURRENT_CONTEXT_COVERAGE.json']
for name,module,parent,script in specs:evidence.extend([f'v53/research/{name}/RELEASE_ADOPTION.json',f'v53/research/{name}/{module}',f'v53/qa/{name}/RELEASE_RESULTS.json'])
for p in evidence:
 if p not in c['evidenceFiles']:c['evidenceFiles'].append(p)
 if p not in m['currentEvidence']:m['currentEvidence'].append(p)
write(V/'research/library-current/COVERAGE.json',c)
prefix='Mốc30/10/2026 — '+report+'\n\n'+summary+'\n\nTiếp: '+nextline+'\n\n'
for p in [V/'NEXT_STEPS.md',V/'research/library-current/COVERAGE.md']:p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
for p in [W/'PROJECT_RESEARCH_STATE.md',W/'WORK_RESUME.md']:
 old=p.read_text(encoding='utf-8-sig');base=old[old.index('Đọc STORAGE_POLICY.md'):];base=base.replace('Mốc phát hành: v53/BAZI_FOOD_STRENGTH_SUBJECT_REPORT.md.','Mốc phát hành: v53/'+report+'.');p.write_text('# Tiếp tục Huyền Học Các\n\nToàn kho đang làm, chưa hoàn thành. Nguồn/QA ngoài site, không xuất bản mạng.\n\n'+prefix+base,encoding='utf-8')
p=W/'PENDING_RESEARCH_STATE.json';d=read(p);d['previousReleaseBeforeFoodRationaleQuantity']=d['latestReleaseVerified'];d.update(date='2026-10-30',status='food-rationale-quantity-fire-integrated;package-verification-external',workDirectory='v53/research/bazi-food-quantity',currentWorkState='v53/research/bazi-food-quantity/RELEASE_ADOPTION.json',latestReport='v53/'+report,inProgressStaging=None,integrationInProgress=False,privateVerifiedResearchScopes=[],nextIndependentScope=nextline);d['latestReleaseVerified']={'researchChecksPassed':True,'report':'v53/'+report,'consumerChanged':False,'wholeCatalogueCompleted':False,'comprehensivePackageVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json'};d['currentScopeChecks']={'newReferenceGroups':22,'inspectionFrames':695,'nullInvariants':8446,'sourceSealSequenceExceptionC31':True,'newEngineCallsDuringVerification':0,'consumerChanged':False,'wholeCatalogueCompleted':False};d['next']=[nextline,*d['next']];d['previousPrivateScopeDisposition']={'status':'C16-C23-C31-integrated','currentAdoption':'v53/research/bazi-food-quantity/RELEASE_ADOPTION.json','historicalPrivatePointersRetained':True};d['currentPrivatePackageBoundary']='Prior C16/C23 private boundary is historical; these scopes are now adopted. Current comprehensive package is verified only when the external audit names this report.';write(p,d)
batch=read(F/'CURRENT_BATCH.json');batch.update(report='v53/'+report,scopes=[x[0]for x in specs],next=nextline,sourceCounters=c['latestAcquisitionCounts'],newActualTableQueries=0,retainedActualCastQueries=0)
batch['tests'].extend(['v53/research/bazi-food-transformation/test-transformation-reference.mjs','v53/research/bazi-food-quantity/test-quantity-reference.mjs','v53/research/bazi-food-fire-exception/test-fire-exception-reference.mjs']);write(F/'CURRENT_BATCH.json',batch)
d['privateNewReferenceGroups']=0;d['latestPrivateResearchNote']=None;write(p,d)
write(W/'POST_RELEASE_WORKING_FOLLOWUP.json',{'date':'2026-10-30','status':'prior-private-C16-C23-C31-adopted;C19-C21-C22-C30-C35-open','releasedReport':'v53/'+report,'currentBatch':'recovery/research-release/CURRENT_BATCH.json','releasedPackageAudit':'recovery/research-release/FINAL_VERIFICATION.json','currentMatrix':'v53/research/bazi-food-quantity/CURRENT_CONTEXT_COVERAGE.json','parentCoverageCounts':[49,41,0],'currentAdoptions':[f'v53/research/{x[0]}/RELEASE_ADOPTION.json'for x in specs],'packageBoundary':'Current audit must name this report and manifest before the new ZIP is called verified. Older private boundaries are historical adoption evidence.','next':nextline,'consumerChanged':False,'wholeCatalogueCompleted':False})
print(json.dumps({'integratedScopes':[x[0]for x in specs],'referenceGroupsAdded':22,'currentMatrixCounts':[49,41,0],'C31PostImplementationSealExplicit':True,'newEngineCallsThisIntegration':0,'consumerChanged':False,'noFullSnapshotCreated':True}))
