from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(n):return json.loads((B/n).read_text(encoding='utf-8-sig'))
def write(n,d):(B/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not(B/'PREIMPLEMENTATION_FREEZE.json').exists()and not(B/'song-reference.mjs').exists()
s=read('CROP_CANDIDATE.json');s['actuallyViewed']=True;s['reading']='CompleteV04 tail and V05including four-element list and source官煞mixture phrase actually viewed.';write('SOURCE_IDENTITIES.json',s)
write('SOURCE_BOUNDARIES.json',{'rawParentPreserved':True,'digitalSeparatorBeforeV06':'(义/)',
 'nativeWorkingSeparatorBeforeV06':'又','status':'Local boundary reading from the fullp182image; digital marker remains byte-exact, not a global glyph correction.',
 'allSourceCharactersDiplomaticallyCollated':False,
 'V04OfficialClause':'惟見財官福更隆','V05WholeMixtureClause':'官煞更無來混雜',
 'neitherBlanketOfficialProhibitionNorPriorityChosen':True,
 'V05FireAdverseJudgmentEstablished':False,'V09PronounSubjectAdjudicated':False,
 'packageBoundary':'Complete private directory created after the three-layer C16/C23/C31 package inventory; outside that released V53 manifest and ZIP.'})
names=['VERSE_PARTITION.json','SELECTED_V05_PREMISES.json','EXPECTED_CASES.json','REUSE_IDENTITIES.json','SOURCE_IDENTITIES.json','SOURCE_BOUNDARIES.json']
write('PREIMPLEMENTATION_FREEZE.json',{'frozenAtUTC':datetime.now(timezone.utc).isoformat(),'referenceAbsentAtFreeze':True,
 'files':[{'file':(B/n).relative_to(W).as_posix(),'bytes':(B/n).stat().st_size,'sha256':sha256((B/n).read_bytes()).hexdigest()}for n in names],
 'manualCases':10,'newEngineCalls':0,'wholeContextApplied':False})
print(json.dumps({'frozenFiles':6,'referenceAbsentAtFreeze':True,'manualCases':10,'newEngineCalls':0}))
