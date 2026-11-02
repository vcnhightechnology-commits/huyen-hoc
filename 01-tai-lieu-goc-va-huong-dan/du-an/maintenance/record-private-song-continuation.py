"""Keep one current continuation pointer; release bytes stay scoped to their verified milestone."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone,timedelta
import json,subprocess,sys
W=Path(__file__).resolve().parent.parent;B=W/'tmp/bazi-food-songs-staging';F=W/'recovery/research-release'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def h(p):return sha256(p.read_bytes()).hexdigest()
assert not(W/'Huyen_Hoc_Cac_V53_source.pending.zip').exists()
audit=read(F/'FINAL_VERIFICATION.json');assert audit['report']=='v53/BAZI_FOOD_RATIONALE_QUANTITY_REPORT.md'and audit['currentResearchGroups']==136
pointer=W/'POST_RELEASE_WORKING_FOLLOWUP.json';assert read(pointer)['status']=='prior-private-C16-C23-C31-adopted;C19-C21-C22-C30-C35-open'
for name in ['SOURCE_RESULTS.json','REFERENCE_RESULTS.json']:assert read(B/name)['passed']
for r in read(B/'POST_INVENTORY_IDENTITIES.json')['files']:
 p=W/r['file'];assert p.stat().st_size==r['bytes']and h(p)==r['sha256']
entries={r['file']:r for r in read(W/'recovery/storage-consolidation/LATEST_PACKAGE_MANIFEST.json')['files']}
assert not any(k.startswith('tmp/bazi-food-songs-staging/')for k in entries)
c22='tmp/bazi-food-return-feeding-staging/SOURCE_DIRECTION_REVIEW.json';assert entries[c22]['sha256']==h(W/c22)
for name in ['PROJECT_RESEARCH_STATE.md','WORK_RESUME.md','PENDING_RESEARCH_STATE.json','EXHAUSTIVE_WORK_STATE.json']:
 assert entries[name]['sha256']==h(W/name)
index=W/'recovery/consolidated-history/INDEX.sqlite';release_index=h(index);old_pointer=h(pointer)
subprocess.run([sys.executable,str(W/'maintenance/preserve-selected-history.py'),'POST_RELEASE_WORKING_FOLLOWUP.json'],check=True)
now=datetime.now(timezone(timedelta(hours=7))).isoformat()
state={'date':'2026-10-30','updatedAt':now,'status':'private-C35-V05-reference-verified-after-released-three-layer-food-batch',
 'releasedReport':audit['report'],'releasedPackageAudit':'recovery/research-release/FINAL_VERIFICATION.json','releaseVerifiedAt':audit['verifiedAt'],
 'releaseSourceZIPSHA256':audit['sourceZIPSHA256'],'releaseCurrentResearchGroups':136,
 'workingReferenceState':'tmp/bazi-food-songs-staging/WORK_STATE.json','workingReferenceNote':'tmp/bazi-food-songs-staging/RESEARCH_NOTE.md',
 'privateFileIdentities':'tmp/bazi-food-songs-staging/POST_INVENTORY_IDENTITIES.json',
 'sourceVerification':'tmp/bazi-food-songs-staging/SOURCE_RESULTS.json','referenceVerification':'tmp/bazi-food-songs-staging/REFERENCE_RESULTS.json',
 'C22DirectionReview':c22,'privateReferenceGroups':7,'privateInspectionFrames':69,'privateNullInvariants':828,
 'poemsPartitioned':12,'editorialSevenCharacterLines':52,'exactParentCodepoints':411,
 'currentParentMatrix':'v53/research/bazi-food-quantity/CURRENT_CONTEXT_COVERAGE.json','parentCoverageCountsUnchanged':[49,41,0],
 'C35SelectedModuleLinkAdded':False,'newEngineCalls':0,'newHTTPBodies':0,'newSourcePositions':0,'consumerChanged':False,'wholeCatalogueCompleted':False,
 'packageBoundary':'The release audit/ZIP verifies the C16/C23/C31 adoption and its as-of root/history bytes. This private C35 directory and updated pointer were created after its inventory; they are not claimed in that V53 manifest/ZIP. No further full ZIP for this small continuation.',
 'historyBoundary':'The prior pointer was preserved by SHA before this private update; its new history revision is after the released INDEX snapshot. Verify the current history index again before the next useful release/package; do not rerun the release finalizer against an intentionally advanced private working index.',
 'next':'Continue C19source-qualified正印meaning and strength/list premises, C21usable-versus-idle and remaining11C35verses. C22direction/皆andC30官specificitystayopen. Do not merge V04財官praise with V05mixture clause, infer adverse fire from an unlisted element, choose a year/day anchor or use engine agreement to resolve grammar. Reuse the retained actual batches and promote with a useful next condition batch.'}
write(pointer,state)
write(F/'POST_PACKAGE_FOOD_SONGS_BOUNDARY.json',{'date':'2026-10-30','createdAt':now,'releaseReport':audit['report'],'releaseVerifiedAt':audit['verifiedAt'],
 'releaseSourceZIPSHA256':audit['sourceZIPSHA256'],'verifiedReleaseIndexSHA256':release_index,'advancedPrivateWorkingIndexSHA256':h(index),
 'priorPointerSHA256Preserved':old_pointer,'currentWorkingPointerSHA256':h(pointer),'workingPointer':'POST_RELEASE_WORKING_FOLLOWUP.json',
 'releasedFourRootStatesRemainByteExact':True,'C22ReviewInReleasePackage':True,'C35PrivateReferenceInReleasePackage':False,
 'additionalFullZIPsCreated':0,'consumerChanged':False,'wholeCatalogueCompleted':False})
print(json.dumps({'privateGroupsPassed':7,'poemsPartitioned':12,'currentMatrixCounts':[49,41,0],'releasedGroups':136,'additionalFullZIPsCreated':0,'consumerChanged':False,'wholeCatalogueCompleted':False}))
