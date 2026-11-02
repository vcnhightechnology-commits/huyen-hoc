from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,subprocess,sys
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert read(B/'RESULTS.json')['passed']and read(B/'SOURCE_RESULTS.json')['passed']
assert not(B/'WORK_STATE.json').exists()
state={'date':'2026-10-30','status':'private-source-qualified-label-bridge-verified;C19meaning-open',
 'sourceReview':'SOURCE_REVIEW.json','reference':'label-scope.mjs','referenceResults':'RESULTS.json','sourceResults':'SOURCE_RESULTS.json',
 'frozenExpectations':'FREEZE.json','groups':5,'inspectionFrames':3610,'nullInvariants':28880,
 'newEngineCalls':0,'newSourcePositions':0,'newHTTPBodies':0,'currentParentCountsUnchanged':[49,41,0],
 'parentLinksAdded':0,'consumerChanged':False,'wholeContextApplied':False,'wholeCatalogueCompleted':False,
 'finding':'C18whole-pillar正印andordinary甲→丙食神coexist. Neither reading resolves the namespace ofC19華葢正印. The bridge executes the existing source lookup and reuses retained actual relation payload; it does not classifyC19fromaTenGodfield.',
 'next':'ContinueC19list segmentation and source-qualified meanings/strength; C21usable-idle and remainingC35verses. Do not infer numeric増培/減半 or transfer C18label toC19. Seek a defined explanatory witness before claiming C19meaning resolved.',
 'packageBoundary':'Private working directory created after the latest C16/C23/C31 package inventory; not in released V53 manifest/ZIP. No full ZIP for this bounded continuation.'}
write(B/'WORK_STATE.json',state)
rows=[{'file':p.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}for p in sorted(B.iterdir())if p.is_file()]
write(B/'IDENTITIES.json',{'files':rows,'privateAfterReleaseInventory':True})
subprocess.run([sys.executable,str(W/'maintenance/preserve-selected-history.py'),'POST_RELEASE_WORKING_FOLLOWUP.json'],check=True)
p=W/'POST_RELEASE_WORKING_FOLLOWUP.json';d=read(p);d['previousPrivateSongScope']={k:d[k]for k in ['workingReferenceState','privateFileIdentities','referenceVerification']}
d.update(updatedAtUTC=datetime.now(timezone.utc).isoformat(),status='private-C19-label-scope-bridge-verified;meaning-and-strength-open',
 workingReferenceState='tmp/bazi-food-label-scope-staging/WORK_STATE.json',privateFileIdentities='tmp/bazi-food-label-scope-staging/IDENTITIES.json',
 referenceVerification='tmp/bazi-food-label-scope-staging/RESULTS.json',sourceVerification='tmp/bazi-food-label-scope-staging/SOURCE_RESULTS.json',
 workingReferenceNote='tmp/bazi-food-label-scope-staging/SOURCE_REVIEW.json',privateReferenceGroups=12,privateInspectionFrames=3679,privateNullInvariants=29708,
 next=state['next']);d['privateParentLinksAdded']=0;d['packageBoundary']=state['packageBoundary'];write(p,d)
print(json.dumps({'groupsAdded':5,'privateGroupsTotal':12,'parentCounts':[49,41,0],'newEngineCalls':0,'additionalFullZIPs':0,'consumerChanged':False}))
