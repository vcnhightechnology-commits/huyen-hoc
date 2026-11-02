"""Promote selected B02 comparisons and occurrence handling, without whole snapshots."""
from pathlib import Path
from hashlib import sha256
import json,shutil
W=Path(__file__).resolve().parent.parent;V=W/'v53';F=W/'recovery/research-release'
S=W/'tmp/liuyao-multiple-use-staging';D=V/'research/liuyao-multiple-use';Q=V/'qa/liuyao-multiple-use'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def ident(p):return {'file':p.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
assert read(W/'recovery/storage-consolidation/MAINTENANCE.json')['status']=='complete'
assert not (W/'archives').exists() and not D.exists() and not Q.exists()
results=['SOURCE_RESULTS.json','REFERENCE_RESULTS.json','CAST_RESULTS.json','PARALLEL_RESULTS.json','OCCURRENCE_RESULTS.json','OCCURRENCE_SOURCE_RESULTS.json']
for n in results:assert read(S/n)['passed']
state=read(S/'WORK_STATE.json');state.update(status='selected-old-method-comparisons-and-source-occurrence-inspection-integrated-research-only',integratedIntoRelease=True,occurrenceReference='occurrence-reference.mjs',occurrenceTests='OCCURRENCE_RESULTS.json',occurrenceSourceChecks='OCCURRENCE_SOURCE_RESULTS.json',packageVerificationPointer='recovery/research-release/FINAL_VERIFICATION.json',newExternalEngineCallsThisIntegration=0)
state.pop('currentPackageContainsEarlierReadingOnly',None)
state['sourceLimits']=['Five quoted preference criteria are not a total author-adopted ranking; all five agreeing does not select the use.','Changing/primary occurrences use the primary palace; no all-transformed-lines activity or temporal concurrency assumed.','Three uses stay three occurrences even when two share a branch; pairwise inspection is editorial, not a complete three-use selection method.','玄月丙午日 retained literally; no month-branch or Gregorian date inferred.','Previous/linked casts and changed question-subject context remain explicit; no independently validated clinical or historical outcomes.']
state['next']=['Review independent source premises: selected use/root qualification, day-month strength, functional void, hidden spirits, timing and linked-cast context.','No repeat of retained five HHC calls or three printed fixture projections unless a new calculation question arises.','Rotate independent Nhà ở/Tử vi/Dịch backlog; do not claim the 137 first-pass spans are fully applied.','Update one comprehensive latest package after a useful batch; no full archive snapshots.']
write(S/'WORK_STATE.json',state)
(S/'README.md').write_text('''# B02 Lưỡng hiện: so tiền đề và giữ đủ vị trí

Khoảng nguồn B02-ch032 nằm ở PDF134–136, đề mục thân sách in “兩現章第三十一”. Bản đồ hiện hành vẫn là 137 khoảng đã đọc lượt đầu, không có mục nào được xác nhận áp trọn. Nhịp này xem mở rộng ba ảnh cũ và ảnh Nhật canvas50 đã giữ; không tăng số vị trí đọc đầu, không tải thêm PDF/ảnh hay xác lập thêm truyền bản độc lập.

`multiple-use-reference.mjs` giữ năm cặp cổ pháp được dẫn: bỏ hưu tù dùng vượng tướng, bỏ tĩnh dùng động, bỏ nguyệt phá dùng không phá, bỏ tuần không dùng không không, bỏ bị thương dùng không thương. Tất cả tiền đề phải khai báo rõ hoặc null. Ngay sau danh sách, nguồn có phản ví dụ dùng Không, dùng Phá, trường hợp ba Dụng và lời dựa trên các quẻ đã hỏi trước. Vì thế các phép so không thành điểm số hoặc bộ chọn Dụng duy nhất; ngay cả năm tiêu chí cùng hướng vẫn không cho kết luận chọn.

`occurrence-reference.mjs` tiếp nhận sáu hào có thứ tự, một Lục thân do người nghiên cứu khai báo và gốc Lục thân theo cung quẻ chính. Mỗi hào gốc có một định danh; chỉ hào thực động mới có thêm định danh chính vị trí biến của nó. Không lấy cả sáu hào quẻ biến làm các tác nhân cùng hoạt động. Trong 豫→歸妹, hai vị trí gốc 巳/午 và một vị trí biến 巳 là ba xuất hiện, dù chỉ có hai chữ chi khác nhau. Hàm so nhiều vị trí giữ đủ tập ứng viên và mọi cặp không thứ tự; việc chiếu phép so hai ứng viên lên từng cặp là công cụ biên tập, chưa phải thuật xếp ưu tiên hoàn chỉnh của sách.

Ba ví dụ nguồn đã được đối chiếu một batch thật gồm năm lời gọi HHC hexNumber: 小畜9→9, 師7→渙59 và 豫16→歸妹54. Sáu nhãn gốc và một nhãn biến chọn khớp bộ đọc Nạp giáp. Giá trị động của 師→渙 được suy từ tên hai quẻ in, không tuyên bố đã đọc độc lập dấu 6/9. Batch được tái dùng; các kiểm sau không gọi lại HHC/lunar/iztro hoặc dựng ngày sinh. Lỗi khởi chạy ESM trên Windows đầu tiên xảy ra trước lời gọi engine, được ghi audit và sửa bằng pathToFileURL.

Các crop NLC135 và Nhật50 đều đọc “玄月丙午日”. Giữ nguyên chữ 玄月, không đổi sang chi tháng hoặc lịch dương. Ấn tượng đọc ngày 丙子/giải tháng 亥 ban đầu đã bị đối ảnh bác bỏ và lưu amendment; byte ảnh gốc không đổi. Crop thiếu đoạn kết/dấu quẻ được giữ như trial bị loại; tám crop chọn trước đó được kiểm RGB, gồm ba ngữ cảnh, ba quẻ và hai đối chiếu ngày.

Hai bộ freeze gốc và freeze vị trí mới giữ kỳ vọng trước triển khai. Bộ so: 59.049 tổ hợp, 10.320 tổ hợp có tiêu chí chỉ về cả hai phía, 9 khung khai báo hai Dụng. Bộ vị trí: 4.096 cấu hình hào × 5 Lục thân = 20.480 lượt biên dịch tham chiếu riêng, không phải 20.480 ca nguồn hay lời gọi HHC mới; kiểm 184.320 bản ghi vị trí và giữ đủ ba Dụng của ví dụ. Tổng hai bộ 16 nhóm kiểm, ngoài bốn nhóm kiểm quẻ và các kiểm nguồn/crop. Mọi dự đoán sự kiện, sức khỏe, Không/Phá hiệu lực và việc chọn Dụng vẫn chưa xác lập.

Nguồn, báo cáo và môđun này chỉ ở nghiên cứu nội bộ, ngoài site. Tiếp điều kiện căn khí/vượng suy/nhật nguyệt/phi phục/ứng kỳ theo đúng giọng; không lấy phản ví dụ lịch sử làm chứng cứ ứng nghiệm độc lập. Gói nguồn tổng hợp được thay nguyên tử theo STORAGE_POLICY.md, không tạo full ZIP trước sửa.
''',encoding='utf-8')
shutil.copytree(S,D);Q.mkdir(parents=True)
identities=[]
for p in sorted(S.iterdir()):
 if p.is_file():
  target=D/p.name;assert target.read_bytes()==p.read_bytes();identities.append({'source':p.relative_to(W).as_posix(),'target':target.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()})
for n in results:shutil.copy2(S/n,Q/n)
write(Q/'PROMOTION_IDENTITIES.json',{'byteExactFiles':identities,'noFullSnapshotCreated':True})
write(Q/'RELEASE_RESULTS.json',{'status':'selected-source-and-reference-verified;package-verification-external','sourceResults':[read(S/n)for n in results],'actualHHCInvocationCountRetained':5,'actualHHCInvocationCountThisIntegration':0,'wholeChapterApplied':False,'consumerChanged':False,'packageVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json'})
summary='B02 Lưỡng hiện: tích hợp năm phép so cổ pháp và bộ giữ đủ vị trí Dụng theo cung quẻ chính. Đọc mở rộng134–136/Nhật50 đã có,0vịtrí đọc đầu/HTTP mới. Giữ ba Dụng của 豫→歸妹 gồm2gốc/1biến dù chỉ2chikhácnhau;khôngrút còn2hoặc xếpưu tiên. 59049tổhợptiềnđề/10320mâuthuẫnchiều,4096cấuhình×5Lụcthân/184320bảnghivịtrí;16nhómthamchiếuđạt. Tái dùng5HHCthật của3quẻ/7nhãnchọn,4nhómkiểmquẻđạt;ảnhNLC135/Nhật50cùng玄月丙午日,khôngquychi/thángdương. Nguồn/QA ngoài site,HTML/webnguyênbyte;137khoảngB02đọcđầu/0áp trọn,toànkho vẫn mở.'
nextline='Luân phiên nhà ở: tiếp P08 nhãn tháng/ngày hoặc các điều kiện 隔/phi tinh theo ma trận; tái dùng ảnh và bảng lịch đã giữ. B02 còn căn khí, Dụng/NguyênKỵCừu, chức năng Không/Phá, ưu tiên/ngữ cảnh hỏi trước; không lấy năm cổ pháp hoặc số lần hiện làm bộ chọn Dụng tự động.'
report='LIUYAO_MULTIPLE_USE_REPORT.md';(V/report).write_text('# Lưỡng hiện: tiền đề, phản ví dụ và vị trí gốc/biến\n\n'+summary+'\n\n'+(D/'README.md').read_text(encoding='utf-8').split('\n',1)[1]+'\n\nTiếp: '+nextline+'\n\nBằng chứng gói hiện hành tại recovery/research-release/FINAL_VERIFICATION.json; phải khớp băm manifest V53. PROMOTION_IDENTITIES ghi byte tiếp nhận; bản trạng thái trước sửa giữ theo SHA-256 tại chỉ mục hợp nhất.\n',encoding='utf-8')
e=read(V/'research/EXHAUSTIVE_WORK_STATE.json');e['previousPenaltyOfficialClashWork']=e['currentWork'];e['currentWork']={'catalogueIDs':['B02'],'work':'增刪卜易:兩現, phản ví dụ và vị trí Dụng','sourceDirectory':'v53/research/liuyao-multiple-use','currentStep':summary,'latestResearchReport':report,'sourceLimits':state['sourceLimits'],'wholeWorkApplied':False};e['inProgressScope']={'status':'selected-multiple-use-research-integrated','finalVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json'};e['subsequentPriority']=[nextline,*e['subsequentPriority']];write(V/'research/EXHAUSTIVE_WORK_STATE.json',e);shutil.copy2(V/'research/EXHAUSTIVE_WORK_STATE.json',W/'EXHAUSTIVE_WORK_STATE.json')
f=read(V/'research/full-study/WORK_STATE.json');f['latestResearchReport']='v53/'+report;f['exhaustiveNext']=[nextline,*f['exhaustiveNext']]
item=next(x for x in f['items']if x['id']=='yi');item['completed'].append(summary);item.update(latestScope=summary,latestResearchReport='v53/'+report,nextFile='v53/research/liuyao-multiple-use/WORK_STATE.json');write(V/'research/full-study/WORK_STATE.json',f)
c=read(V/'research/library-current/COVERAGE.json');c['latestFollowup']=summary;c['latestAcquisitionCounts']={'scope':report,'newHTTPBodies':0,'newOriginalContainers':0,'newIndependentWitnesses':0,'newSourcePositions':0,'retainedHHCExecutions':5,'newHHCExecutionsThisIntegration':0,'actualCalendarObjects':0,'wholeWorksApplied':0}
evidence=['v53/'+report,'v53/research/liuyao-multiple-use/WORK_STATE.json','v53/research/liuyao-multiple-use/OCCURRENCE_MANUAL.json','v53/research/liuyao-multiple-use/MANUAL_SOURCE_CLAUSES.json',*[f'v53/qa/liuyao-multiple-use/{n}'for n in results],'v53/qa/liuyao-multiple-use/RELEASE_RESULTS.json']
for p in evidence:
 if p not in c['evidenceFiles']:c['evidenceFiles'].append(p)
for x in c['catalogue']:
 if x['id']=='B02':
  for p in evidence:
   if p not in x['currentEvidence']:x['currentEvidence'].append(p)
  x['latestMultipleUseResearch']={'report':'v53/'+report,'sourceUnit':'B02-ch032','wholeUnitApplied':False,'automaticUseSelection':False,'consumerChanged':False}
for x in c['features']:
 if x['id']=='yi':x['latestMultipleUseResearch']={'report':'v53/'+report,'wholeWorkApplied':False,'consumerChanged':False}
positions=read(V/'research/library-current/TMTH002_NATIVE_POSITION_COVERAGE.json')
c['currentTMTH002NativePositionIndex']={'file':'v53/research/library-current/TMTH002_NATIVE_POSITION_COVERAGE.json','distinctViewedCount':positions['distinctViewedCount'],'remainingCount':positions['remainingCount'],'wholeVolumeApplied':False}
c['coverageMetadataSync']['latestIndexedTMTH002CountsFromAuthoritativeFile']=ident(V/'research/library-current/TMTH002_NATIVE_POSITION_COVERAGE.json');write(V/'research/library-current/COVERAGE.json',c)
prefix='Mốc29/10/2026 — '+report+'\n\n'+summary+'\n\nTiếp: '+nextline+'\n\n'
for p in [V/'NEXT_STEPS.md',V/'research/library-current/COVERAGE.md',W/'PROJECT_RESEARCH_STATE.md',W/'WORK_RESUME.md']:p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
p=W/'PENDING_RESEARCH_STATE.json';d=read(p);d['previousReleaseBeforeMultipleUse']=d['latestReleaseVerified'];d.update(status='multiple-use-source-occurrence-research-integrated;package-verification-external',workDirectory='v53/research/liuyao-multiple-use',currentWorkState='v53/research/liuyao-multiple-use/WORK_STATE.json',latestReport='v53/'+report,inProgressStaging=None);d['latestReleaseVerified']={'researchChecksPassed':True,'report':'v53/'+report,'consumerChanged':False,'wholeCatalogueCompleted':False,'comprehensivePackageVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json'};d['historicalNextBeforeMultipleUse']=d['next'];d['next']=[nextline,*[x for x in d['next']if not x.startswith('B02兩現:')]];d['previousScopeChecksBeforeMultipleUse']=d['currentScopeChecks'];d['currentScopeChecks']={'date':'2026-10-29','scopes':{'liuyao-multiple-use':{n.removesuffix('.json'):read(S/n)for n in results}},'uniqueSourcePositionsNewlyViewed':0,'retainedActualHHCHexNumberCalls':5,'newEngineCallsDuringVerification':0,'newHTTPBodiesDuringScope':0,'newNatalCharts':0,'consumerChanged':False,'wholeCatalogueCompleted':False,'packageVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json','currentBatch':'recovery/research-release/CURRENT_BATCH.json'};write(p,d)
batch=read(F/'CURRENT_BATCH.json');batch.update(report='v53/'+report,scopes=['liuyao-multiple-use'],next=nextline,sourceCounters={'firstPassPositionsAdded':0,'newHTTPBodies':0,'newEngineCallsThisIntegration':0,'retainedEngineCalls':5},newActualTableQueries=0,retainedActualCastQueries=5,newCalendarObjects=0);batch.pop('editorialUnits',None);batch['tests']=[*batch['tests'],'v53/research/liuyao-multiple-use/test-multiple-use.mjs','v53/research/liuyao-multiple-use/test-occurrences.mjs'];write(F/'CURRENT_BATCH.json',batch)
write(F/'WORKING_FOLLOWUP.json',{'status':'previous-private-multiple-use-followup-integrated','currentBatch':'recovery/research-release/CURRENT_BATCH.json','wholeCatalogueCompleted':False,'consumerChanged':False,'next':nextline})
print(json.dumps({'researchScopeIntegrated':'liuyao-multiple-use','preservedPromotionFiles':len(identities),'twoReferenceSuitesGroups':16,'newEngineCalls':0,'publicChanged':False,'noFullSnapshotCreated':True}))
