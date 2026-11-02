from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(n):return json.loads((B/n).read_text(encoding='utf-8-sig'))
def write(n,d):(B/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not(B/'PREIMPLEMENTATION_FREEZE.json').exists()and not(B/'SOURCE_EXPECTATIONS_SEAL.json').exists()
assert (B/'fire-exception-reference.mjs').exists()and read('SEQUENCE_EXCEPTION.json')['manualCasesCryptographicallyFrozenBeforeCode']is False
s=read('CROP_CANDIDATE.json');s['actuallyViewed']=True;write('SOURCE_IDENTITIES.json',s)
names=['MANUAL_CONTEXT.json','EXPECTED_CASES.json','REUSE_IDENTITIES.json','SOURCE_IDENTITIES.json','SEQUENCE_EXCEPTION.json','fire-exception-reference.mjs']
write('SOURCE_EXPECTATIONS_SEAL.json',{'sealedAtUTC':datetime.now(timezone.utc).isoformat(),'files':[{'file':(B/n).relative_to(W).as_posix(),'bytes':(B/n).stat().st_size,'sha256':sha256((B/n).read_bytes()).hexdigest()}for n in names],
 'preimplementationFreezeEstablished':False,'referenceExistedAndHadBeenExecutedAtSeal':True,'sequenceException':'SEQUENCE_EXCEPTION.json',
 'actualCalendarPremisesAbsent':True,'inputScope':'Declared day/hour stems only; no date or hour-branch mapping.',
 'newEngineCalls':0,'wholeContextApplied':False})
print(json.dumps({'postImplementationSealedFiles':6,'preimplementationFreezeEstablished':False,'manualCases':8,'newEngineCalls':0}))
