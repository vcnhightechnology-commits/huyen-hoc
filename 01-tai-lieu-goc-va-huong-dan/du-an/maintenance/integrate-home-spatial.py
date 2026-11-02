"""Promote bounded home source-context research using one current release, no snapshots."""
from pathlib import Path
from hashlib import sha256
import json,shutil
W=Path(__file__).resolve().parent.parent;V=W/'v53';F=W/'recovery/research-release'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
specs=[('home-p08-grid-priority','tmp/home-p08-grid-priority-staging',['SOURCE_RESULTS.json','TEST_RESULTS.json']),('home-month-spatial','tmp/home-month-spatial-staging',['SOURCE_RESULTS.json','REFERENCE_RESULTS.json']),('home-p08-related-selection-locator','tmp/home-p08-gjts-grid-witness-staging',['SOURCE_RESULTS.json'])]
assert read(W/'recovery/storage-consolidation/MAINTENANCE.json')['status']=='complete'
assert not(W/'archives').exists()and not(W/'Huyen_Hoc_Cac_V53_source.pending.zip').exists()
f=read(V/'research/full-study/WORK_STATE.json');assert any(x['id']=='home'for x in f['items'])
c=read(V/'research/library-current/COVERAGE.json');assert any(x['id']=='P08'for x in c['catalogue'])
for name,stage,results in specs:
 assert not(V/'research'/name).exists()and not(V/'qa'/name).exists()
 for result in results:assert read(W/stage/result)['passed']
report='HOME_SPATIAL_CONTEXT_REPORT.md'
summary='P08 và 選擇要略: tiếp nhận hai ngữ cảnh 建破魁罡 ngày/phương cùng ba đơn vị Nguyệt luận về đồng vị và một vị cát thần đến. Giữ riêng tầng năm/tháng/ngày; một quan sát thuận cục bộ không xóa lời kiêng ở đoạn khác. Hai bộ14nhóm kiểm/3725khung tiền đề biên tập đạt,không phải ca nguồn hay phép tính sao. Thực thi môđun 萬通火星 đã giữ để kiểm giao thoa,0lịch/HHC mới. Ba vị trí ITKC241/244/245 và P08-131 được xem mở rộng;5cropđúngRGB. Chín ảnh locator từ container CổKim đã giữ,1cropRGB:không thấy bảng720ô ở khoảng Tuyểntrạch96–101,khôngsuykhôngcóbảngởmọinơi. P08 vẫn500nhãn đọc/220chưa rõ,195vịtríđọcđầu/0áp trọn;khôngđổiweb.'
nextline='Luân phiên Tử vi: đọc trạng thái/các khoảng chưa mã hóa trước khi chọn điều kiện; ưu tiên 童限,火鈴CanhNhâm hoặc khởi hạn theo từng truyền bản. Nhà ở còn220nhãnP08 mờ, lịch vị trí sao/tháng/nhuận/ưu tiên và hình học; không điền theo mẫu hay lấy cát thần của một đoạn làm phép chung. B02 căn khí/vượng suy và Tam Mệnh vượng suy/cách cục vẫn mở.'
for name,stage,results in specs:
 s=W/stage;d=V/'research'/name;q=V/'qa'/name
 state=read(s/'WORK_STATE.json');state.update(status='bounded-source-research-integrated;whole-work-open',integratedIntoRelease=True,latestResearchReport='v53/'+report,packageVerificationPointer='recovery/research-release/FINAL_VERIFICATION.json')
 state['historicalPrivateStage']=stage
 if name=='home-p08-related-selection-locator':state['currentReleaseBoundary']='Previously private after earlier package inventory; now promoted into this research batch. Original pre-promotion state is retained in SHA-indexed history.'
 write(s/'WORK_STATE.json',state);shutil.copytree(s,d);q.mkdir(parents=True)
 identities=[]
 for p in sorted(s.iterdir()):
  if p.is_file():
   target=d/p.name;assert p.read_bytes()==target.read_bytes();identities.append({'source':p.relative_to(W).as_posix(),'target':target.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()})
 for result in results:shutil.copy2(s/result,q/result)
 write(q/'PROMOTION_IDENTITIES.json',{'byteExactFiles':identities,'noWholeSnapshotCreated':True})
 write(q/'RELEASE_RESULTS.json',{'status':'source-and-reference-verified;package-verification-external','scope':name,'checks':[read(s/result)for result in results],'consumerChanged':False,'wholeSourceMethodApplied':False,'packageVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json'})

body='''# Ngữ cảnh ngày/phương, đồng vị và cát thần trong nguồn nhà ở

'''+summary+'''

## Phạm vi tiếp nhận

- `research/home-p08-grid-priority`: hai đoạn P08-131 và ITKC244. Các tên 建破魁罡 giống nhau không khiến khung ngày trở thành khung phương. Caption về ba đế tinh ở P08 được giữ nhưng chưa chốt thứ tự khi cùng xuất hiện với lời kiêng.
- `research/home-month-spatial`: ba đơn vị MONTH-03/12/13 ở ITKC241/245. Nguồn ghi rõ 或 cho 月獨火 và 日家 cho cặp 月遊火/飛天獨火. Đoạn năm nhãn 飛宮/地軸/帝舍/帝車/帝輅 ghi 其中但得一位; phép tồn tại chỉ áp vào quan sát được xác lập đủ tư cách và đến đúng chỗ, không thay bằng cờ cát thần chung.
- `research/home-p08-related-selection-locator`: chín ảnh định vị95–102/105 của container Cổ Kim đã giữ. Khoảng96–101 có Tuyển trạch,102 mở Phù trấn; mảnh ghi chú `另見選擇部故不錄` không được mở rộng thành chứng cứ thiếu bảng trên toàn bộ công trình. Không đối chứng tế bào hoặc emend P08 từ hướng tra này.

## Kiểm chứng và giới hạn

14 nhóm kiểm mới gồm36khung ngày/phương và3689khung Nguyệt luận,29764bất biến null,12khung không hỗ trợ/21đầu vào sai. Các khung là tổ hợp tiền đề biên tập, không phải ca lịch sử hay lá số nguồn. Bảy tệp freeze của hai môđun giữ kỳ vọng trước triển khai. Hai bộ nguồn đối byte/SHA/pixel năm crop; ba crop thử cắt đề mục giữ riêng. Locator kiểm byte/RGBA chín PNG và crop thứ sáu; không giải mã lại ảnh chỉ để tăng số.

Hàm cũ 萬通火星 được gọi thật trong kiểm mới và vẫn giữ lời kiêng cục bộ. Mệnh đề thuận nguồn khác không xóa nó; chưa có ưu tiên toàn tác phẩm. Không có phép tính lịch, sao bay, phương tọa hoặc dự đoán cháy/thiệt hại mới. Mệnh đề 丙丁二字 được giữ nguyên khối, không nhận một chữ thay thế. Danh sách quan sát chưa đầy đủ không chứng minh vắng mặt; ID trùng và mảng thưa bị từ chối. Giới hạn64quan sát là kỹ thuật, không phải số sao cổ.

NLC/ITKC/P08 byte gốc không sửa. 兎 của ảnh được giữ; audit chữ兔 cũ của phạm vi trước không bị xóa. ITKC và Cổ Kim là tác phẩm liên quan, chưa xác lập chúng như hai bản độc lập của P08. Tổng vị trí P08/ITKC đọc đầu không tăng; chín vị trí Cổ Kim chỉ được ghi là locator, không hiệu khảo trọn trang.

HTML/site/webZIP không đổi byte; site vẫn chỉ có index.html. Nguồn/thuật tham chiếu/QA ở ngoài site. Manifest và gói nguồn tổng hợp sẽ kiểm lại rồi thay nguyên tử, không tạo full snapshot. Trạng thái trước sửa giữ theo SHA-256 tại chỉ mục hợp nhất, chat Codex không đụng tới.

Tiếp: '''+nextline+'''

Audit gói: `recovery/research-release/FINAL_VERIFICATION.json` phải khớp manifest V53 hiện hành. Các báo cáo phát hành cũ là lịch sử, không đòi dựng lại ZIP đã hợp nhất.
'''
(V/report).write_text(body,encoding='utf-8')
e=read(V/'research/EXHAUSTIVE_WORK_STATE.json');e['previousMultipleUseWork']=e['currentWork'];e['currentWork']={'catalogueIDs':['P08'],'work':'P08/選擇要略:ngữcảnh ngày/phương,đồngvị,cátthần','sourceDirectory':'v53/research/home-month-spatial','latestResearchReport':report,'currentStep':summary,'wholeWorkApplied':False};e['inProgressScope']={'status':'bounded-home-spatial-research-integrated','finalVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json'};e['subsequentPriority']=[nextline,*e['subsequentPriority']];write(V/'research/EXHAUSTIVE_WORK_STATE.json',e);shutil.copy2(V/'research/EXHAUSTIVE_WORK_STATE.json',W/'EXHAUSTIVE_WORK_STATE.json')
f['latestResearchReport']='v53/'+report;f['exhaustiveNext']=[nextline,*f['exhaustiveNext']];home=next(x for x in f['items']if x['id']=='home');home['completed'].append(summary);home.update(latestScope=summary,latestResearchReport='v53/'+report,nextFile='v53/research/home-month-spatial/WORK_STATE.json');write(V/'research/full-study/WORK_STATE.json',f)
c['latestFollowup']=summary;c['latestAcquisitionCounts']={'scope':report,'newHTTPBodies':0,'newOriginalContainers':0,'newIndependentP08Editions':0,'newP08SourcePositions':0,'newITKCSourcePositions':0,'relatedCompilationNewLocatorPositions':9,'newEngineCalls':0,'newCalendarObjects':0,'wholeWorksApplied':0}
evidence=['v53/'+report]
for name,stage,results in specs:evidence.extend(['v53/research/'+name+'/WORK_STATE.json','v53/qa/'+name+'/RELEASE_RESULTS.json'])
for p in evidence:
 if p not in c['evidenceFiles']:c['evidenceFiles'].append(p)
p08=next(x for x in c['catalogue']if x['id']=='P08')
for p in evidence:
 if p not in p08['currentEvidence']:p08['currentEvidence'].append(p)
p08['latestSpatialConditionalScope']={'report':'v53/'+report,'selectedSourceUnits':5,'newP08SourcePositions':0,'newITKCSourcePositions':0,'relatedCompilationLocatorPositions':9,'P08WorkingReadableLabels':500,'P08UnresolvedLabels':220,'wholeWorkApplied':False,'consumerChanged':False}
next(x for x in c['features']if x['id']=='home')['latestSpatialConditionalScope']=p08['latestSpatialConditionalScope'];write(V/'research/library-current/COVERAGE.json',c)
prefix='Mốc29/10/2026 — '+report+'\n\n'+summary+'\n\nTiếp: '+nextline+'\n\n'
for p in [V/'NEXT_STEPS.md',V/'research/library-current/COVERAGE.md']:p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
# Replace repetitive root narration with current continuation pointers; prior text already sealed in history.
root='''# Tiếp tục Huyền Học Các

Trạng thái toàn kho: đang làm, chưa hoàn thành. Yêu cầu người dùng: tự tiếp nghiên cứu/phát triển, chỉ hỏi khi thật sự thiếu quyết định; nguồn và QA ngoài site, không xuất bản mạng.

'''+prefix+'''Đọc STORAGE_POLICY.md trước đóng gói/dọn. Khóa bảo trì hiện complete; chỉ giữ một gói nguồn tổng hợp mới nhất, một gói web, HTML vận hành. Không tạo archives/v53-before-*; không đưa ZIP/binary lớn vào Git. Nguồn duy nhất và lịch sử chat giữ nguyên; các trạng thái cũ được tra recovery/consolidated-history/INDEX.sqlite.

Mốc phát hành: v53/HOME_SPATIAL_CONTEXT_REPORT.md. Kiểm bằng recovery/research-release/FINAL_VERIFICATION.json, v53/PACKAGE_MANIFEST.json và recovery/storage-consolidation/LATEST_PACKAGE_MANIFEST.json. Trong lúc cập nhật gói, audit cũ chỉ xác nhận mốc cũ; không gọi trạng thái mới là đã đóng gói khi audit chưa khớp.

Ma trận hiện hành: v53/research/library-current/COVERAGE.json; việc dở toàn kho: EXHAUSTIVE_WORK_STATE.json và v53/research/full-study/WORK_STATE.json. B02 dùng RESUME_INDEX.json và map137/137/0, không dùng map cũ103mục; Tam Mệnh quyển2 hiện86vịtríxem/146chưaxác lập. P08 195/195đọc đầu không đồng nghĩa áp hết; 500nhãn/220mờ giữ riêng với720dấu建破 cũ.

Không chạy lại các batch lịch/engine đã giữ chỉ để tăng số. Khi so một tính toán mới, thực thi engine phù hợp và giữ payload; các phép nối văn bản không tự dựng lá số hoặc đổi vị trí sao khác truyền thống. Theo dõi Kiến Lộc browserQA và các nguồn bị chặn theo trạng thái riêng; không bỏ qua cài đặt hoặc tải lặp.
'''
(W/'PROJECT_RESEARCH_STATE.md').write_text(root,encoding='utf-8');(W/'WORK_RESUME.md').write_text(root,encoding='utf-8')
p=W/'PENDING_RESEARCH_STATE.json';d=read(p);d['previousReleaseBeforeHomeSpatial']=d['latestReleaseVerified'];d.update(status='home-spatial-source-conditions-integrated;package-verification-external',workDirectory='v53/research/home-month-spatial',currentWorkState='v53/research/home-month-spatial/WORK_STATE.json',latestReport='v53/'+report,inProgressStaging=None,integrationInProgress=False,nextIndependentScope=nextline);d['latestReleaseVerified']={'researchChecksPassed':True,'report':'v53/'+report,'consumerChanged':False,'wholeCatalogueCompleted':False,'comprehensivePackageVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json'};d['next']=[nextline,*d['next']];d['currentScopeChecks']={'date':'2026-10-29','scopes':{name:{r.removesuffix('.json'):read(W/stage/r)for r in results}for name,stage,results in specs},'referenceGroups':14,'sourceUnits':5,'newP08SourcePositions':0,'newITKCSourcePositions':0,'relatedCompilationLocatorPositions':9,'newHTTPBodies':0,'newEngineCallsDuringVerification':0,'consumerChanged':False,'wholeCatalogueCompleted':False,'packageVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json'};write(p,d)
batch=read(F/'CURRENT_BATCH.json');batch.update(report='v53/'+report,scopes=[x[0]for x in specs],next=nextline,newActualTableQueries=0,retainedActualCastQueries=0,sourceCounters={'newP08SourcePositions':0,'newITKCSourcePositions':0,'relatedCompilationLocatorPositions':9,'newHTTPBodies':0,'newEngineCallsThisIntegration':0,'sourceUnits':5});batch['tests']=[*batch['tests'],'v53/research/home-p08-grid-priority/test-context.mjs','v53/research/home-month-spatial/test-monthly-spatial.mjs'];write(F/'CURRENT_BATCH.json',batch)
for p in ['WORKING_FOLLOWUP.json','PRIVATE_FOLLOWUP.json','POST_PACKAGE_FOLLOWUP.json']:write(F/p,{'status':'prior-private-home-context-and-locator-followups-integrated','currentBatch':'recovery/research-release/CURRENT_BATCH.json','report':'v53/'+report,'next':nextline,'consumerChanged':False,'wholeCatalogueCompleted':False})
print(json.dumps({'integratedScopes':[x[0]for x in specs],'newReferenceGroups':14,'sourceUnits':5,'consumerChanged':False,'noWholeSnapshotCreated':True}))
