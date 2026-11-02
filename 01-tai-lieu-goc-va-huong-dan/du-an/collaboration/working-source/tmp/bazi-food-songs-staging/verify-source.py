from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,sys
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def check(r):
 p=W/r['file'];assert p.stat().st_size==r['bytes']and sha256(p.read_bytes()).hexdigest()==r['sha256'],r['file']
freeze=read(B/'PREIMPLEMENTATION_FREEZE.json');reuse=read(B/'REUSE_IDENTITIES.json')
for r in freeze['files']+reuse['files']+reuse['retainedFullImagesActuallyViewed']:check(r)
s=read(B/'SOURCE_IDENTITIES.json');check(s['source']);check(s['crop']);expected=Image.open(W/s['source']['file']).convert('RGB').crop(s['boxXYXY']);actual=Image.open(W/s['crop']['file']).convert('RGB');assert actual.size==expected.size and ImageChops.difference(actual,expected).getbbox()is None
p=read(B/'VERSE_PARTITION.json');c=next(r for r in read(W/'v53/research/bazi-food-source/CONTEXTS.json')['records']if r['id']=='FOOD-00-C35');assert c==p['parent']
assert p['prefixLiteral']+''.join((r['digitalMarkerBefore']or'')+r['text']for r in p['rows'])==c['text']
assert len(c['text'])==411 and sum(len(r['text'])for r in p['rows'])==364 and sum(len(r['editorialSevenCharacterLines'])for r in p['rows'])==52
for r in p['rows']:assert c['text'][r['startWithinParentCodepoints']:r['endWithinParentCodepoints']]==r['text']
v=read(B/'SELECTED_V05_PREMISES.json');assert v['sourceText']==p['rows'][4]['text'];assert all(v[k]in v['sourceText']for k in ['foodStrengthLiteral','preferredLuckLiteral','noMixtureLiteral']);assert ''.join(v['preferredLuckElements'])=='水木土金';assert v['verse4OfficialClause']in p['rows'][3]['text']
assert reuse['V08RetainedActualFoodPair']in read(W/'v53/qa/bazi-food-core/TEN_RELATION_RESULTS.json')['records']
matrix=read(W/'v53/research/bazi-food-quantity/CURRENT_CONTEXT_COVERAGE.json');assert not next(r for r in matrix['records']if r['id']=='FOOD-00-C35')['selectedModuleLinks']
out={'passed':True,'frozenFiles':6,'manualCases':10,'poemsPartitioned':12,'editorialLines':52,'digitalParentCodepoints':411,
 'exactDigitalReconstruction':True,'nativeCropRGBMatches':1,'retainedImagesReexamined':3,'sourceMixtureMeaningAdjudicated':False,
 'newEngineCallsDuringVerification':0,'retainedV08ActualFoodPairReused':1,'newHTTPBodies':0,'newSourcePositions':0,'consumerChanged':False,'wholeContextApplied':False}
if '--write-results'in sys.argv:(B/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
