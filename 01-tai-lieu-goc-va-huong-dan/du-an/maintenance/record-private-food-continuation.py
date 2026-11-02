"""Record private progress after the verified release without rebuilding its full ZIP."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone,timedelta
import json,subprocess,sys,sqlite3
W=Path(__file__).resolve().parent.parent
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not(W/'Huyen_Hoc_Cac_V53_source.pending.zip').exists()
audit=read(W/'recovery/research-release/FINAL_VERIFICATION.json');assert audit['report']=='v53/BAZI_FOOD_STRENGTH_SUBJECT_REPORT.md'and audit['currentResearchGroups']==114
root=W/'POST_RELEASE_WORKING_FOLLOWUP.json';assert read(root)['status']=='prior-private-C13-C14-integrated;next-source-C16-open'
scopes=['bazi-food-transformation','bazi-food-quantity']
checks={}
for scope in scopes:
 b=W/f'tmp/{scope}-staging';assert read(b/'SOURCE_RESULTS.json')['passed']and read(b/'REFERENCE_RESULTS.json')['passed']
 checks[scope]={'source':read(b/'SOURCE_RESULTS.json'),'reference':read(b/'REFERENCE_RESULTS.json')}
 seal=b/'POST_INVENTORY_IDENTITIES.json';assert not seal.exists()
 files=[{'file':p.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}for p in sorted(b.iterdir())if p.is_file()]
 write(seal,{'scope':scope,'files':files,'createdAfterReleasePackageInventory':True,'notInReleasedV53ManifestOrSourceZIP':True})
names=['POST_RELEASE_WORKING_FOLLOWUP.json','PROJECT_RESEARCH_STATE.md','WORK_RESUME.md','PENDING_RESEARCH_STATE.json']
subprocess.run([sys.executable,str(W/'maintenance/preserve-selected-history.py'),*names],check=True)
now=datetime.now(timezone(timedelta(hours=7))).isoformat()
summary=('Việc riêng sau gói C13/C14: C16 đã có tham chiếu cặp hóa khí và20so tọa độ (14tái dùng,6HHC+6lunar mới đã lưu một lần); '
 'C23 đã có tham chiếu ví dụ lượng chữ với ràng buộc chung của trụ thiếu. Hai mô-đun riêng đạt16nhóm/324khung/4736bất biến null, '
 'không thêm liên kết ma trận46/44/0 hoặc đổi HTML. C19/C21 còn ledger điều kiện, C22 chưa chọn cách nối vai trò. '
 'Đọc POST_RELEASE_WORKING_FOLLOWUP.json trước khi nối phiên; không chạy lại engine hoặc đóng ZIP toàn kho cho mỗi mô-đun.')
state={'date':'2026-10-30','updatedAt':now,'status':'private-C16-C23-verified-after-released-C13-C14;next-conditions-open',
 'releasedReport':audit['report'],'releasedPackageAudit':'recovery/research-release/FINAL_VERIFICATION.json','releaseVerifiedAt':audit['verifiedAt'],
 'releaseSourceZIPSHA256':audit['sourceZIPSHA256'],'releaseCurrentResearchGroups':114,
 'workingReferenceStates':[f'tmp/{s}-staging/WORK_STATE.json'for s in scopes],
 'workingReferenceNotes':[f'tmp/{s}-staging/RESEARCH_NOTE.md'for s in scopes],
 'privateFileIdentities':[f'tmp/{s}-staging/POST_INVENTORY_IDENTITIES.json'for s in scopes],
 'privateVerification':checks,'privateReferenceGroups':16,'privateInspectionFrames':324,'privateNullInvariants':4736,
 'newHHCGodCallsAlreadyRetained':6,'newLunarTenGodQueriesAlreadyRetained':6,'retainedC16RelationPairsReused':14,
 'retainedC16PartnerCoordinatesReused':10,'C23FoodPairReusesAnAlreadyRetainedCoordinate':True,
 'parentCoverageCountsUnchanged':[46,44,0],'privateParentLinksAdded':0,
 'newSourcePositions':0,'newHTTPBodies':0,'newCalendarObjects':0,'consumerChanged':False,'wholeCatalogueCompleted':False,
 'packageBoundary':'C16/C23 directories and this continuation update are after the C13/C14 package inventory. The verified source ZIP/audit applies to that release only, not every current private file or subsequently appended history-index revision. No additional full ZIP created.',
 'preservationBoundary':'Four mutable continuation files were preserved by SHA before this update. The history index may have new revisions after the package audit; verify the current index again before the next useful release/package.',
 'next':'Continue C19/C21 full effective-strength and list premises, C22 role/direction alternatives; preserve separate voices. Promote C16/C23 with a useful next source-condition batch. Do not rerun6HHC/6lunar or14retained pairs/10partner coordinates; do not universalize many/few, emend all巳, choose day/year or implement wealth/health/character outcomes.'}
write(root,state)
prefix='Việc riêng sau mốc gói — '+now+'\n\n'+summary+'\n\n'
for name in ['PROJECT_RESEARCH_STATE.md','WORK_RESUME.md']:
 p=W/name;p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
p=W/'PENDING_RESEARCH_STATE.json';d=read(p)
d.update(date='2026-10-30',status='private-C16-C23-source-references-verified;released-C13-C14-package-kept',
 workDirectory='tmp/bazi-food-quantity-staging',currentWorkState='tmp/bazi-food-quantity-staging/WORK_STATE.json',
 inProgressStaging='tmp/bazi-food-quantity-staging',integrationInProgress=False,
 latestPrivateResearchNote='tmp/bazi-food-quantity-staging/RESEARCH_NOTE.md',currentPrivateContinuation='POST_RELEASE_WORKING_FOLLOWUP.json',
 privateVerifiedResearchScopes=scopes,privateNewReferenceGroups=16,nextIndependentScope=state['next'])
d['currentPrivatePackageBoundary']=state['packageBoundary'];d['next']=[state['next'],*d['next']];write(p,d)
c=sqlite3.connect('file:'+(W/'recovery/consolidated-history/INDEX.sqlite').as_posix()+'?mode=ro',uri=True)
assert c.execute('PRAGMA integrity_check').fetchone()[0]=='ok';revisions=c.execute('SELECT count(*)FROM revisions').fetchone()[0];c.close()
print(json.dumps({'privateScopes':scopes,'groups':16,'currentMatrixCounts':[46,44,0],'historyRevisions':revisions,'additionalFullZIPsCreated':0,'consumerChanged':False,'wholeCatalogueCompleted':False}))
