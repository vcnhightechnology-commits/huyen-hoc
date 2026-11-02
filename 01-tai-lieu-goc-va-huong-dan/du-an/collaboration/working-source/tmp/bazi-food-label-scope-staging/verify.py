from pathlib import Path
from hashlib import sha256
import json
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
for r in read(B/'FREEZE.json')['files']+read(B/'REUSE.json')['files']:
 p=W/r['file'];assert p.stat().st_size==r['bytes']and sha256(p.read_bytes()).hexdigest()==r['sha256'],r['file']
m=read(B/'SOURCE_REVIEW.json');c=read(W/'v53/research/bazi-food-source/CONTEXTS.json')['records']
for r in m['contexts']:assert r==next(x for x in c if x['id']==r['id'])
assert m['anchor']in m['contexts'][0]['text']and m['C19Literal']in m['contexts'][1]['text']
assert m['C19Meaning']is None
out={'passed':True,'frozenFiles':3,'retainedSourceImageReexamined':1,'newSourcePositions':0,'newHTTPBodies':0,'newEngineCalls':0,'C19MeaningAdjudicated':False,'consumerChanged':False}
(B/'SOURCE_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
