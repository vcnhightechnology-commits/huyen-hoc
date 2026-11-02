from pathlib import Path
from hashlib import sha256
import json
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
assert not(B/'POST_INVENTORY_IDENTITIES.json').exists()
for name in ['SOURCE_RESULTS.json','REFERENCE_RESULTS.json']:assert json.loads((B/name).read_text(encoding='utf-8'))['passed']
rows=[{'file':p.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}for p in sorted(B.iterdir())if p.is_file()]
(B/'POST_INVENTORY_IDENTITIES.json').write_text(json.dumps({'files':rows,'createdAfterThreeLayerPackageInventory':True,
 'notInThatReleasedV53ManifestOrZIP':True,'wholeContextApplied':False},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'sealedPrivateFiles':len(rows),'newEngineCalls':0,'additionalFullZIPsCreated':0}))
