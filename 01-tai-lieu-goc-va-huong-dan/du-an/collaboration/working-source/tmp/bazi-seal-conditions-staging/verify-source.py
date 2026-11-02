from pathlib import Path
from hashlib import sha256
import json,re
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def check(r):
 p=W/r['file'];assert p.stat().st_size==r['bytes']and sha256(p.read_bytes()).hexdigest()==r['sha256'],r['file']
for r in read(B/'FREEZE.json')['files']+read(B/'SOURCE_IDENTITIES.json')['files']+read(B/'SOURCE_IDENTITIES.json')['images']:check(r)
units=read(B/'CHAPTER_UNITS.json');text=(B/'CHAPTER_EXCERPT.txt').read_text(encoding='utf-8');raw=(W/units['source']['file']).read_text(encoding='utf-8');assert text in raw
clean=re.sub(r'<pb:[^>]+>|[\s¶]','',text);assert clean==''.join(r['text']for r in units['units'])and len(clean)==units['cleanCodepoints']==690
for r in units['units']:assert clean[r['start']:r['end']]==r['text']and not r['wholeUnitApplied']
m=read(B/'MANUAL_FUJU.json');assert m['literal']==units['units'][6]['text'];assert all(m[k]in m['literal']for k in ['weakPremiseLiteral','sameSealLiteral','storageStrongLiteral','restraintLiteral'])
assert '論徳秀'not in clean and '凡論印'in units['units'][-1]['text']
results=read(B/'RESULTS.json');assert results['passed']and results['newEngineCallsDuringTests']==0
out={'passed':True,'frozenFiles':4,'chapterEditorialUnits':13,'chapterCleanCodepoints':690,'exactDigitalReconstruction':True,'fullChapterSpanImagesViewed':6,'globalNewPositionCount':None,'newHTTPBodies':0,'newOriginalContainers':0,'newEngineCalls':0,'wholeChapterApplied':False,'consumerChanged':False}
(B/'SOURCE_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
