"""Record the failed before-code freeze honestly; never manufacture an earlier seal."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
assert not(B/'PREIMPLEMENTATION_FREEZE.json').exists()and not(B/'SOURCE_EXPECTATIONS_SEAL.json').exists()
names=['MANUAL_CONTEXT.json','EXPECTED_CASES.json','REUSE_IDENTITIES.json','fire-exception-reference.mjs','test-fire-exception-reference.mjs','freeze-source.py','verify-source.py']
rows=[{'file':(B/n).relative_to(W).as_posix(),'bytes':(B/n).stat().st_size,'sha256':sha256((B/n).read_bytes()).hexdigest(),'mtimeNS':(B/n).stat().st_mtime_ns}for n in names]
out={'recordedUTC':datetime.now(timezone.utc).isoformat(),'status':'implementation-was-written-before-freeze-command;preimplementation-freeze-not-established',
 'observedFailure':'freeze-source.py correctly refused because fire-exception-reference.mjs already existed. The shell continued to test; its final group failed because the expected freeze did not exist. No passing REFERENCE_RESULTS was written.',
 'manualCasesWereWrittenBeforeCodeInThisToolSequence':True,'manualCasesCryptographicallyFrozenBeforeCode':False,
 'referenceHasAlreadyBeenExecutedBeforeSeal':True,'sourceIdentityLedgerWillBePostImplementationSeal':True,
 'initialFiles':rows,'initialVerifierAndTestRevisionsPreservedInConsolidatedSHAIndex':True,
 'correction':'Preserve original script bytes; use a truthfully dated post-implementation source-expectation seal, independent exhaustive domain checks and an explicit sequencing exception. Do not delete or move code to make an absence guard pass.',
 'consumerChanged':False,'wholeContextApplied':False}
(B/'SEQUENCE_EXCEPTION.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'preimplementationFreezeEstablished':False,'postImplementationSealRequired':True,'manualCasesModifiedAfterFirstTest':False}))
