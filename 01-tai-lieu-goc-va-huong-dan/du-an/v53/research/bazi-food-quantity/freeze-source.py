from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
B=Path(__file__).resolve().parent
def read(n):return json.loads((B/n).read_text(encoding='utf-8-sig'))
def write(n,d):(B/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not(B/'PREIMPLEMENTATION_FREEZE.json').exists()and not(B/'quantity-reference.mjs').exists()
# Native crops already inspected. Retain explicit reasoning behind the manual expectation correction.
write('PRE_FREEZE_REVIEW.json',{'case':'missing-slot','earlierProvisionalSurplusLiteralMatch':None,'reviewedExpectedValue':True,
 'reason':'Known甲+two丙 with one unknown always has甲 and exactlytwo orthree丙; the two uncertain exact-count predicates share the same unknown slot. Do not use independent null-OR.',
 'jointImpossibleCaseAdded':'Known甲+twootherstems+oneunknown cannot simultaneously reach exactlytwo甲andone丙.',
 'reviewedBeforeReferenceImplementation':True,'newEngineCalls':0})
crop=read('CROP_CANDIDATES.json')
for r in crop['records']:r['actuallyViewed']=True
write('SOURCE_IDENTITIES.json',crop)
names=['MANUAL_CONTEXTS.json','EXPECTED_CASES.json','REUSE_IDENTITIES.json','SOURCE_IDENTITIES.json','PRE_FREEZE_REVIEW.json']
W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
write('PREIMPLEMENTATION_FREEZE.json',{'frozenAtUTC':datetime.now(timezone.utc).isoformat(),'files':[{'file':(B/n).relative_to(W).as_posix(),'bytes':(B/n).stat().st_size,'sha256':sha256((B/n).read_bytes()).hexdigest()}for n in names],
 'referenceAbsentAtFreeze':True,'manualCases':8,'sourceOutcomesImplemented':False})
print(json.dumps({'frozenFiles':5,'manualCases':8,'newEngineCalls':0}))
