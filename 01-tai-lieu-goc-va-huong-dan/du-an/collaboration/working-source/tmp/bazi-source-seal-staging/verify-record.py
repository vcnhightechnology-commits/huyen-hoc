from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,subprocess,sys
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for r in read(B/'FREEZE.json')['files']+read(B/'SOURCE_IDENTITIES.json')['files']:
 p=W/r['file'];assert p.stat().st_size==r['bytes']and sha256(p.read_bytes()).hexdigest()==r['sha256']
raw=(W/'v53/research/bazi-relations/sources/KR3g0042_003.txt').read_text(encoding='utf-8');excerpt=(B/'RETAINED_EXCERPT.txt').read_text(encoding='utf-8');assert excerpt in raw
assert '正印者乃五行之正庫'in excerpt and '有華蓋印如亥卯未得癸未之類'in excerpt
assert read(B/'RESULTS.json')['passed']
write(B/'SOURCE_RESULTS.json',{'passed':True,'byteIdentitiesVerified':True,'retainedDigitalExcerptOnly':True,'newEngineCalls':0,'newHTTPBodies':0,'newImagesViewed':0,'C19MeaningAdjudicated':False})
state={'date':'2026-10-30','status':'private-volume3-digital-crossreference-verified;facsimile-and-C19binding-open',
 'sourceReading':'MANUAL.json','digitalExcerpt':'RETAINED_EXCERPT.txt','reference':'source-seal.mjs','checks':['RESULTS.json','SOURCE_RESULTS.json'],
 'groups':4,'frames':247,'newEngineCalls':0,'currentParentCountsUnchanged':[49,41,0],'newParentLinks':0,
 'wholeContextApplied':False,'wholeCatalogueCompleted':False,'consumerChanged':False,
 'finding':'Volume3論正印explicitlydefines五行之正庫andprints華蓋印example. This provides an intrawork lexical candidate for C19, not a verified identification or independent transmission.',
 'remaining':['Read retained/identifiedvolume3facsimile43b-44a before calling this image-collated; do not fetch a whole book merely for two folios.',
 'Water/earth targets壬辰/丙辰are kept as one literal source group; do not assign them separately by modern convention.',
 'Resolve sourceanchor命andC19localmeaning; C21strength and remainingC35verses stay open.'],
 'packageBoundary':'Private work after released C16/C23/C31inventory; not in that manifest/ZIP. No full package rebuild for this small cross-reference.'}
write(B/'WORK_STATE.json',state)
subprocess.run([sys.executable,str(W/'maintenance/preserve-selected-history.py'),'POST_RELEASE_WORKING_FOLLOWUP.json'],check=True)
p=W/'POST_RELEASE_WORKING_FOLLOWUP.json';d=read(p);d['previousPrivateLabelScope']=d['workingReferenceState'];d.update(status='private-volume3-source-seal-crossreference-verified;C19binding-open',workingReferenceState='tmp/bazi-source-seal-staging/WORK_STATE.json',workingReferenceNote='tmp/bazi-source-seal-staging/MANUAL.json',sourceVerification='tmp/bazi-source-seal-staging/SOURCE_RESULTS.json',referenceVerification='tmp/bazi-source-seal-staging/RESULTS.json',updatedAtUTC=datetime.now(timezone.utc).isoformat(),privateReferenceGroups=16,privateInspectionFrames=3926,next='Locate/read volume3facsimile43b-44a for retaineddigital論正印crossreference, preserving grouped水土and unresolvedC19binding. ContinueC21strength/remainingC35verses independently. No engine reruns or fullZIP per small scope.');d['privateFileIdentities']='tmp/bazi-source-seal-staging/IDENTITIES.json';d['packageBoundary']=state['packageBoundary'];write(p,d)
rows=[{'file':p.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}for p in sorted(B.iterdir())if p.is_file()]
write(B/'IDENTITIES.json',{'files':rows,'privateAfterReleaseInventory':True})
print(json.dumps({'passed':True,'newGroups':4,'privateGroupsTotal':16,'currentParentCounts':[49,41,0],'newEngineCalls':0,'newWholeZIPs':0}))
