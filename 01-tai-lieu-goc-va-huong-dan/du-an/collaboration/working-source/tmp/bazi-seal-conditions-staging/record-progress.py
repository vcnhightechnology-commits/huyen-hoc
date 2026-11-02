from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,subprocess,sys
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not(B/'WORK_STATE.json').exists()
assert read(B/'RESULTS.json')['passed']and read(B/'SOURCE_RESULTS.json')['passed']
state={'date':'2026-10-30','status':'private-full-seal-chapter-span-viewed;selected-five-position-premises-verified;whole-chapter-open',
 'sourceID':'TMTH003-FujuYin-selected','chapterMap':'CHAPTER_UNITS.json','sourceReview':'RESEARCH_NOTE.md','reference':'fuju-reference.mjs',
 'sourceVerification':'SOURCE_RESULTS.json','referenceVerification':'RESULTS.json','preimplementationFreeze':'FREEZE.json',
 'fullChapterNativePositionsViewed':[88,89,90,91,92,93],'folios':['43b','44a','44b','45a','45b','46a'],'nextHeading':'論徳秀',
 'editorialUnits':13,'cleanDigitalCodepoints':690,'groups':6,'inspectionFrames':992,'nullInvariants':11904,
 'newNativeDerivativesThisContinuation':3,'globallyNewViewedPositionsCount':None,'newHTTPBodies':0,'newOriginalContainers':0,'newEngineCalls':0,
 'currentFoodParentMatrix':'v53/research/bazi-food-quantity/CURRENT_CONTEXT_COVERAGE.json','currentFoodParentCountsUnchanged':[49,41,0],
 'wholeChapterApplied':False,'C19MeaningAdjudicated':False,'consumerChanged':False,'wholeCatalogueCompleted':False,
 'next':['Source命anchor semantics and whole-pillar/nayin versus daystem frames remain explicit. Do not choose year/day silently.',
 'Keep S03亥卯未/癸未join open; continue named印S08–S12with full premises and source-specific labels. C19華葢正印binding remains a documented lexical lead.',
 'Five-position reference does not derive fetalpillar/strength/seal positions. Do not re-run retained engine batches just to increase counts.',
 'Integrate private song/label/seal scopes together after a useful next condition batch; no fullZIP for each small step.'],
 'packageBoundary':'Private working files after C16/C23/C31releaseinventory; outside that V53manifest/ZIP. Latest release audit remains as-of its verified bytes.'}
write(B/'WORK_STATE.json',state)
rows=[{'file':p.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}for p in sorted(B.iterdir())if p.is_file()]
write(B/'IDENTITIES.json',{'files':rows,'privateAfterReleaseInventory':True})
subprocess.run([sys.executable,str(W/'maintenance/preserve-selected-history.py'),'POST_RELEASE_WORKING_FOLLOWUP.json'],check=True)
p=W/'POST_RELEASE_WORKING_FOLLOWUP.json';d=read(p);d['previousPrivateSealCrossReference']=d['workingReferenceState'];d.update(updatedAtUTC=datetime.now(timezone.utc).isoformat(),status=state['status'],workingReferenceState='tmp/bazi-seal-conditions-staging/WORK_STATE.json',workingReferenceNote='tmp/bazi-seal-conditions-staging/RESEARCH_NOTE.md',sourceVerification='tmp/bazi-seal-conditions-staging/SOURCE_RESULTS.json',referenceVerification='tmp/bazi-seal-conditions-staging/RESULTS.json',privateFileIdentities='tmp/bazi-seal-conditions-staging/IDENTITIES.json',privateReferenceGroups=22,privateInspectionFrames=4918,nativeSourceReview='tmp/bazi-seal-conditions-staging/SOURCE_IDENTITIES.json',nativePositionsReviewed=[88,89,90,91,92,93],globallyNewViewedPositionsCount=None,next=' '.join(state['next']));d['packageBoundary']=state['packageBoundary'];d['privateNullInvariantsEarlierScopesOnly']=d.pop('privateNullInvariants',None);d['latestPrivateNullInvariants']=11904;write(p,d)
print(json.dumps({'groupsAdded':6,'privateGroupsTotal':22,'nativeChapterSpan':[88,93],'chapterUnits':13,'foodMatrixCounts':[49,41,0],'newEngineCalls':0,'additionalWholeZIPs':0,'consumerChanged':False}))
