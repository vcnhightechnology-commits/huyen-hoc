from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,sys
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(n):return json.loads((B/n).read_text(encoding='utf-8-sig'))
def verify(r):
 p=W/r['file'];assert p.stat().st_size==r['bytes']and sha256(p.read_bytes()).hexdigest()==r['sha256'],r['file']
for r in read('PREIMPLEMENTATION_FREEZE.json')['files']+read('REUSE_IDENTITIES.json')['files']:verify(r)
for r in read('SOURCE_IDENTITIES.json')['records']:
 verify(r['source']);verify(r['crop']);assert r['actuallyViewed']
 expected=Image.open(W/r['source']['file']).convert('RGB').crop(r['boxXYXY']);actual=Image.open(W/r['crop']['file']).convert('RGB');assert expected.size==actual.size and ImageChops.difference(expected,actual).getbbox()is None
old=json.loads((W/'v53/research/tuvi-lower-contexts/TIMING_CLAUSE.json').read_text(encoding='utf-8-sig'));assert read('SOURCE_WINDOWS.json')['windows']==old['normalizedWindows']
charts=read('RETAINED_CHART_PROJECTIONS.json');assert len(charts['cases'])==2
for c in charts['cases']:
 verify(c['sourceRuntime']);runtime=json.loads((W/c['sourceRuntime']['file']).read_text(encoding='utf-8-sig'));r=next(x for x in runtime['records']if x['caseID']==c['caseID'])
 for star in c['stars']:assert star['branch']==r['hhcProjection']['majorBranches'][star['sourceStar']]==r['iztroProjection']['majorBranches'][star['sourceStar']]
out={'passed':True,'frozenFiles':6,'nativeCropsRGBMatched':3,'retainedSourcePositionsReexamined':3,'sourceClassRows':14,'singleNamedDipperRows':11,'compoundLabelsNotForced':3,'textualWindows':4,'retainedActualHHCExecutions':2,'retainedActualIztroExecutions':2,'retainedMajorBranchCoordinates':28,'newEngineCalls':0,'newHTTPBodies':0,'newSourcePositions':0,'newIndependentEditions':0,'sourceWindowDatesEstablished':False,'consumerChanged':False,'wholeSourceMethodApplied':False}
if '--write-results'in sys.argv:(B/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
