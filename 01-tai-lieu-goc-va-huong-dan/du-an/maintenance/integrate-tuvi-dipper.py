"""Promote source-label/time-window cross-reference and bounded digital witness ledger."""
from pathlib import Path
from hashlib import sha256
import shutil,json
W=Path(__file__).resolve().parent.parent;V=W/'v53';F=W/'recovery/research-release'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
specs=[('tuvi-dipper-windows','tmp/tuvi-dipper-windows-staging',['SOURCE_RESULTS.json','REFERENCE_RESULTS.json']),('tuvi-shidian-witness','tmp/tuvi-shidian-witness-staging',['SOURCE_RESULTS.json'])]
assert read(W/'recovery/storage-consolidation/MAINTENANCE.json')['status']=='complete'
assert not(W/'archives').exists()and not(W/'Huyen_Hoc_Cac_V53_source.pending.zip').exists()
for name,stage,results in specs:
 assert not(V/'research'/name).exists()and not(V/'qa'/name).exists()
 for n in results:assert read(W/stage/n)['passed']
report='TUVI_DIPPER_WINDOWS_REPORT.md'
summary='T01: nối14nhãn chính tinh ở giọng bảng Quyển3 với4cửa sổ văn bản hành hạn Quyển5;11nhãn đơn(5Bắc/6Nam),3nhãn ghép chưa phân định. 8nhóm/1718khung/13328bất biến null đạt;giữ đủ vị trí và vai trò sinh/hạn,khôngchọnnửa hạn chung. Tái dùng2HHC+2iztro2.6.2 thật/28tọa độ chính tinh của2ca hiệnđại,56chiếu nhãn khôngphải56chart mới;0engine/HTTP/ảnh mới nhịp tích hợp. Baảnh cũ xem mở rộng/3cropRGB. Đồng tiếp nhận7đoạn chép số Shidian đã lưu:1HTML200/992096byte và10client hỗ trợ ở nhịp trước,0ảnh gốc/0truyền bản độc lập. Nhãn thư việnNộiCácNhật/NamDươngĐường là thuộc tính nền tảng,chưachứngbảnriêng;童限/火鈴/CanhNhâm/khởihạn vẫn mở. Web/HTML nguyênbyte,toànkho chưa xong.'
nextline='Luân phiên Tam Mệnh: dùng ma trận Thực thần hiện hành44liên kết phần/46chưa/0áp trọn hoặc ngữ cảnh vượng suy/cách cục có ảnh đã giữ; không tải/kiểm lại24truy vấn cũ. Tử vi còn nhãn ghép/phụ tinh/đếm18, đầy đủ tiền đề hạn/tuổi/ranh lịch và nguồn độc lập; P08 vẫn220nhãn mờ, B02 căn khí/vượng suy/hiệu lực vẫn mở.'
for name,stage,results in specs:
 s=W/stage;d=V/'research'/name;q=V/'qa'/name
 # Do not rewrite frozen historical WORK_STATE in the digital ledger.
 adoption={'date':'2026-10-29','status':'bounded-research-integrated;whole-work-open','catalogueID':'T01','historicalStage':stage,'workState':'v53/research/'+name+'/WORK_STATE.json','latestResearchReport':'v53/'+report,'packageVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json','consumerChanged':False,'wholeCatalogueCompleted':False,'historicalFrozenPrivateStatePreserved':name=='tuvi-shidian-witness'}
 write(s/'RELEASE_ADOPTION.json',adoption);shutil.copytree(s,d);q.mkdir(parents=True)
 identities=[]
 for p in sorted(s.iterdir()):
  if p.is_file():
   t=d/p.name;assert t.read_bytes()==p.read_bytes();identities.append({'source':p.relative_to(W).as_posix(),'target':t.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()})
 for n in results:shutil.copy2(s/n,q/n)
 write(q/'PROMOTION_IDENTITIES.json',{'byteExactFiles':identities,'noWholeSnapshotCreated':True})
 write(q/'RELEASE_RESULTS.json',{'status':'source-and-reference-verified;package-verification-external','checks':[read(s/n)for n in results],'consumerChanged':False,'wholeCatalogueCompleted':False,'packageVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json'})
body='''# Tử vi: hệ Đẩu, cửa sổ văn bản và tầng chứng cứ

'''+summary+'''

## Nhãn và điều kiện được tiếp nhận

`research/tuvi-dipper-windows` giữ giọng bảng thuộc tính ở item上4468520/canvas82–83. Các nhãn Bắc/Nam được tra theo chữ nguồn, không từ hành hoặc vị trí sao. 紫微 giữ 中天星南北斗, 太陽/太陰 giữ 南北斗; ba nhãn này không bị ép sang một phía. Chưa giải toàn danh sách phụ tinh hoặc cách đếm 一十八星.

Ở item下4469314/canvas35, Bắc/Đại hạn giữ 上五年, Bắc/Tiểu hạn 上半年, Nam/Đại hạn 下五年, Nam/Tiểu hạn 下半年. Đây là nhãn thời đoạn trong lời nguồn. Câu mở về âm/dương nam/nữ được chép riêng, chưa mã hóa thành thuận lợi. Không suy tuổi/cung khởi hạn, ngày dương hoặc sự kiện từ 上/下. Vị trí lá số gốc và vị trí hạn khai báo có vai trò riêng; tập có cả Bắc/Nam/nhãn ghép không có một cửa sổ chung tự chọn.

Tám nhóm kiểm gồm14nhãn/4cửa sổ,1718khung và13328bất biến chưa rõ. Hai ca hiện đại của batch đã lưu2HHC+2iztro được tái dùng cho28tọa độ và56chiếu nhãn; không chạy lại chart hoặc gọi đó là ca ứng nghiệm lịch sử. Ba ảnh nguồn cũ mở rộng, ba crop native khớp RGB. Các engine/consumer và nguồn gốc giữ nguyên SHA-256.

## Hồ sơ chép số và xuất xứ

`research/tuvi-shidian-witness` giữ HTML công khai của SDZJ0170 cùng header/byte/SHA, mười tệp client công khai và bảy đoạn chọn. Metadata nền tảng ghi 日本内阁文库, 南阳堂刊本/明 và528trang. Đây không phải528trang đã đọc, ngày in được xác minh hay một truyền bản độc lập mới. Quan hệ với hai item Nhật đang dùng còn mở.

Các lớp dữ liệu gốc JSON, chữ hiển thị và lời dịch hiện đại được tách. 童限 ở bản số đọc餘年一泒/十五命宫, trong khi bản đọc ảnh cũ còn□/十五大命宮: chưa đủ để sửa chữ hoặc chốt tuổi15. 身主 vẫn có火鈴星; lời dịch hiện đại gọi命主星 dưới nhan đề身主 không được dùng thay vai trò trong nguyên văn. Canh/Nhâm chưa có nhân chứng độc lập mới.

Lượt Python ban đầu bị từ chối kết nối tại sandbox; lượt host được phép dùng TLS thường đã tải HTML200, không tắt TLS. Các tệp trình xem công khai cho thấy đường ảnh yêu cầu token/decrypt; không tạo token, không chạy decrypt, không gọi API ảnh hoặc thử vượt hạn chế. Không thử lại ảnh max Nhật403 đã giữ. Ledger/byte checks tái tạo đúng bảy đoạn từ HTML và giữ nguồn/engine/consumer gốc nguyênbyte.

WORK_STATE của ledger chép số được freeze ở mốc riêng chưa tiếp nhận, giữ nguyên như lịch sử. RELEASE_ADOPTION.json là trạng thái tiếp nhận hiện hành. Không sửa freeze để che trình tự; toàn bộ module và hồ sơ này vẫn ở ngoài site.

Gói tổng hợp chỉ được xác nhận khi FINAL_VERIFICATION.json khớp PACKAGE_MANIFEST hiện hành. Không tạo full snapshot hoặc ZIP theo từng cải tiến nhỏ; trạng thái trước sửa được giữ trong chỉ mục SHA-256. HTML/site/webZIP không thay, lịch sử chat Codex giữ nguyên.

Tiếp: '''+nextline+'\n'
(V/report).write_text(body,encoding='utf-8')
e=read(V/'research/EXHAUSTIVE_WORK_STATE.json');e['previousHomeSpatialWork']=e['currentWork'];e['currentWork']={'catalogueIDs':['T01'],'work':'Tửvi:hệĐẩu/cửa sổvăn bản/chépsố','sourceDirectory':'v53/research/tuvi-dipper-windows','currentStep':summary,'latestResearchReport':report,'wholeWorkApplied':False};e['inProgressScope']={'status':'bounded-tuvi-source-cross-reference-integrated','packageVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json'};e['subsequentPriority']=[nextline,*e['subsequentPriority']];write(V/'research/EXHAUSTIVE_WORK_STATE.json',e);shutil.copy2(V/'research/EXHAUSTIVE_WORK_STATE.json',W/'EXHAUSTIVE_WORK_STATE.json')
f=read(V/'research/full-study/WORK_STATE.json');f['latestResearchReport']='v53/'+report;f['exhaustiveNext']=[nextline,*f['exhaustiveNext']];x=next(x for x in f['items']if x['id']=='tuvi');x['completed'].append(summary);x.update(latestScope=summary,latestResearchReport='v53/'+report,nextFile='v53/research/tuvi-dipper-windows/RELEASE_ADOPTION.json');write(V/'research/full-study/WORK_STATE.json',f)
c=read(V/'research/library-current/COVERAGE.json');c['latestFollowup']=summary;c['latestAcquisitionCounts']={'scope':report,'newHTTPBodiesThisIntegration':0,'inheritedSuccessfulDigitalHTMLBodies':1,'inheritedSuccessfulClientSupportBodies':10,'newOriginalContainers':0,'newSourceImages':0,'newSourcePositions':0,'newIndependentEditions':0,'newEngineCalls':0,'retainedHHCExecutions':2,'retainedIztroExecutions':2,'wholeWorksApplied':0}
evidence=['v53/'+report]
for name,stage,results in specs:evidence.extend(['v53/research/'+name+'/RELEASE_ADOPTION.json','v53/qa/'+name+'/RELEASE_RESULTS.json'])
for p in evidence:
 if p not in c['evidenceFiles']:c['evidenceFiles'].append(p)
t=next(x for x in c['catalogue']if x['id']=='T01')
for p in evidence:
 if p not in t['currentEvidence']:t['currentEvidence'].append(p)
t['latestDipperWindowScope']={'report':'v53/'+report,'selectedPrincipalStarDescriptors':14,'singleDipperLabels':11,'compoundLabelsUnresolved':3,'textualWindows':4,'newSourcePositions':0,'wholeWorkApplied':False,'consumerChanged':False};t['latestDigitalWitnessLedger']={'file':'v53/research/tuvi-shidian-witness/DIGITAL_PASSAGE_LEDGER.json','digitalParagraphsInspected':7,'newIndependentEditionEstablished':False,'platformTotalPagesNotReadCount':528,'workState':'v53/research/tuvi-shidian-witness/RELEASE_ADOPTION.json'};next(x for x in c['features']if x['id']=='tuvi')['latestDipperWindowScope']=t['latestDipperWindowScope'];write(V/'research/library-current/COVERAGE.json',c)
prefix='Mốc29/10/2026 — '+report+'\n\n'+summary+'\n\nTiếp: '+nextline+'\n\n'
for p in [V/'NEXT_STEPS.md',V/'research/library-current/COVERAGE.md']:p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
for p in [W/'PROJECT_RESEARCH_STATE.md',W/'WORK_RESUME.md']:
 old=p.read_text(encoding='utf-8-sig');boundary=old.index('Đọc STORAGE_POLICY.md');base=old[boundary:];base=base.replace('Mốc phát hành: v53/HOME_SPATIAL_CONTEXT_REPORT.md.','Mốc phát hành: v53/'+report+'.');p.write_text('# Tiếp tục Huyền Học Các\n\nTrạng thái toàn kho: đang làm, chưa hoàn thành. Nguồn và QA ngoài site; không xuất bản mạng.\n\n'+prefix+base,encoding='utf-8')
p=W/'PENDING_RESEARCH_STATE.json';d=read(p);d['previousReleaseBeforeTuviDipper']=d['latestReleaseVerified'];d.update(status='tuvi-dipper-text-and-digital-ledger-integrated;package-verification-external',workDirectory='v53/research/tuvi-dipper-windows',currentWorkState='v53/research/tuvi-dipper-windows/RELEASE_ADOPTION.json',latestReport='v53/'+report,inProgressStaging=None,integrationInProgress=False,nextIndependentScope=nextline);d['latestReleaseVerified']={'researchChecksPassed':True,'report':'v53/'+report,'consumerChanged':False,'wholeCatalogueCompleted':False,'comprehensivePackageVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json'};d['next']=[nextline,*d['next']];d['currentScopeChecks']={'date':'2026-10-29','scopes':{name:{n.removesuffix('.json'):read(W/stage/n)for n in results}for name,stage,results in specs},'newReferenceGroups':8,'newEngineCallsDuringVerification':0,'newSourcePositions':0,'newIndependentEditions':0,'consumerChanged':False,'wholeCatalogueCompleted':False,'packageVerificationPointer':'recovery/research-release/FINAL_VERIFICATION.json'};write(p,d)
batch=read(F/'CURRENT_BATCH.json');batch.update(report='v53/'+report,scopes=[x[0]for x in specs],next=nextline,sourceCounters={'newSourcePositions':0,'newHTTPBodiesThisIntegration':0,'retainedDigitalHTMLBodies':1,'retainedPublicClientSupportBodies':10,'newEngineCallsThisIntegration':0,'retainedHHCExecutions':2,'retainedIztroExecutions':2},newActualTableQueries=0,retainedActualCastQueries=0);batch['tests']=[*batch['tests'],'v53/research/tuvi-dipper-windows/test-dipper-windows.mjs'];write(F/'CURRENT_BATCH.json',batch)
for p in [F/'WORKING_FOLLOWUP.json',F/'PRIVATE_TUVI_FOLLOWUP.json',W/'CURRENT_WORKING_FOLLOWUP.json']:write(p,{'date':'2026-10-29','status':'prior-private-tuvi-digital-ledger-integrated','report':'v53/'+report,'currentBatch':'recovery/research-release/CURRENT_BATCH.json','next':nextline,'consumerChanged':False,'wholeCatalogueCompleted':False})
print(json.dumps({'integratedScopes':[x[0]for x in specs],'newReferenceGroups':8,'sourceDescriptors':14,'compoundUnresolved':3,'newEngineCalls':0,'consumerChanged':False,'noWholeSnapshotCreated':True}))
