from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,subprocess,sys
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not(B/'WORK_STATE.json').exists()
assert read(B/'RESULTS.json')['passed']and read(B/'SOURCE_RESULTS.json')['passed']
state={'date':'2026-10-30','status':'private-WenzhangYin-ten-literal-pairs-and-retained-runtime-verified;mechanisms-open',
 'sourceID':'TMTH003-WenzhangYin-literal-pairs','sourceUnit':'S04','sourceReading':'MANUAL.json','note':'RESEARCH_NOTE.md',
 'reference':'literary-seal.mjs','referenceTests':'RESULTS.json','sourceVerification':'SOURCE_RESULTS.json','preimplementationFreeze':'FREEZE.json','actualRuntime':'ACTUAL_RUNTIME.json',
 'groups':6,'inspectionFrames':3624,'nullInvariants':39864,'sourcePairs':10,'sourceGroups':2,
 'actualNewNaYinQueriesAlreadyRetained':8,'actualNewStemElementQueriesAlreadyRetained':3,'retainedNaYinQueriesReused':7,'retainedStemElementsReused':7,'retainedBranchPartnerRows':12,
 'newEngineCallsDuringVerification':0,'newCalendarObjects':0,'newNatalCharts':0,'newHTTPBodies':0,'newSourceImages':0,
 'sourceYiHaiRenChenUnemended':True,'sourceMechanismControlDirectionAdjudicated':False,
 'currentFoodParentCountsUnchanged':[49,41,0],'newParentLinks':0,'consumerChanged':False,'wholeContextApplied':False,'wholeCatalogueCompleted':False,
 'packageBoundary':'Private files created after released C16/C23/C31packageinventory; outside that V53manifest/ZIP. No additional fullZIP for this bounded module.',
 'next':['Do not rerun8newNAYIN/3newstemlookupsor7+7reusedcoordinates/12branchpartners; source/runtime verification reuses retained payload.',
 'Keep two source mechanism groups separate and乙亥/壬辰literal; ordinary coordinate comparisons do not adjudicate original grammar or authorize emendation.',
 'Continue source-role and full-premise inspection of S06鳳凰啣印 andS08–S12without importing ordinaryTenGodor modernselfpenaltynames. C19binding and completefiveelementsealanchor remain open.',
 'Integrate the private source-qualified label/seal/chapter/songs modules as a useful combined batch; do not build a wholeZIPper pair or incrementversion for counts.']}
write(B/'WORK_STATE.json',state)
rows=[{'file':p.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}for p in sorted(B.iterdir())if p.is_file()]
write(B/'IDENTITIES.json',{'files':rows,'privateAfterReleaseInventory':True})
subprocess.run([sys.executable,str(W/'maintenance/preserve-selected-history.py'),'POST_RELEASE_WORKING_FOLLOWUP.json'],check=True)
p=W/'POST_RELEASE_WORKING_FOLLOWUP.json';d=read(p);assert d['privateReferenceGroups']==22;d['previousPrivateChapterConditions']=d['workingReferenceState'];d.update(updatedAtUTC=datetime.now(timezone.utc).isoformat(),status=state['status'],workingReferenceState='tmp/bazi-literary-seal-staging/WORK_STATE.json',workingReferenceNote='tmp/bazi-literary-seal-staging/RESEARCH_NOTE.md',sourceVerification='tmp/bazi-literary-seal-staging/SOURCE_RESULTS.json',referenceVerification='tmp/bazi-literary-seal-staging/RESULTS.json',privateFileIdentities='tmp/bazi-literary-seal-staging/IDENTITIES.json',privateReferenceGroups=28,privateInspectionFrames=8542,latestPrivateNullInvariants=39864,newEngineCalls=11,newEngineCallMeaning='8newNaYin+3newstemtablequeriesexecutedonceinlatestprivatebatch;tests0;nocharts',next=' '.join(state['next']));d['packageBoundary']=state['packageBoundary'];write(p,d)
print(json.dumps({'groupsAdded':6,'privateGroupsTotal':28,'privateFramesTotal':8542,'actualNewTableCallsAlreadyRetained':11,'newEngineCallsDuringVerification':0,'additionalWholeZIPs':0,'consumerChanged':False}))
