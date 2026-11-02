from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,sys
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(n):return json.loads((B/n).read_text(encoding='utf-8-sig'))
def digest(p):return sha256(p.read_bytes()).hexdigest()
for r in read('PREIMPLEMENTATION_FREEZE.json')['files']+read('REUSE_IDENTITIES.json')['files']:
 p=W/r['file'];assert p.stat().st_size==r['bytes']and digest(p)==r['sha256']
source=read('SOURCE_IDENTITIES.json')
for r in source['records']:
 for k in ['source','crop']:
  p=W/r[k]['file'];assert p.stat().st_size==r[k]['bytes']and digest(p)==r[k]['sha256']
 actual=Image.open(W/r['crop']['file']).convert('RGB');expected=Image.open(W/r['source']['file']).convert('RGB').crop(r['boxXYXY']);assert actual.size==expected.size and ImageChops.difference(actual,expected).getbbox()is None
for r in source['fullImagesActuallyViewed']:
 p=W/r['file'];assert p.stat().st_size==r['bytes']and digest(p)==r['sha256']
run=read('ACTUAL_RUNTIME.json');e=read('EXPECTED_COORDINATES.json')
assert run['scriptSHA256']==digest(B/'run-actual-once.mjs')and run['freezeSHA256']==digest(B/'PREIMPLEMENTATION_FREEZE.json')
assert run['librarySHA256']==digest(W/run['libraryFile'])
assert run['actualNewCoordinateCalls']==len(run['rows'])==4 and run['actualReusedCoordinateCalls']==len(run['reused'])==2
for row,expected in zip(run['rows'],e['newCalls']):
 assert all(row[k]==v for k,v in expected.items())and row['actual']==expected['expectedLunar']
for row,expected in zip(run['reused'],e['reuse']):
 assert all(row[k]==v for k,v in expected.items())and row['actual']==expected['expectedLunar']and not row['newCall']
assert next(x for x in run['reused']if x['stem']=='壬')['actual']=='长生'
assert next(x for x in run['rows']if x['id']=='alternative-geng-shen')['actual']=='临官'
lexicon=json.loads((W/'v53/research/bazi-life-stage/MANUAL_TERMS.json').read_text(encoding='utf-8-sig'))
assert lexicon['explicitAliasAnchors']['沐浴']=='五曰沐浴又曰敗'
matrix=json.loads((W/'v53/research/bazi-food-chain/CURRENT_CONTEXT_COVERAGE.json').read_text(encoding='utf-8-sig'));assert len(matrix['records'])==90
parent=next(x for x in matrix['records']if x['id']=='FOOD-00-C14');assert parent['selectedModuleLinks']==[] and not parent['wholeContextApplied']
assert not run['implicitSourceSubjectResolved']and not run['sourceEfficacyValidated']and run['actualNatalCharts']==0
out={'passed':True,'frozenFiles':4,'acceptedNativeCropsRGBMatched':2,'trialCropsRetained':2,'retainedImagesReexamined':3,'retainedActualNewCoordinateCallsVerified':4,'retainedCoordinateCallsReused':2,'newEngineCallsDuringVerification':0,'actualNatalCharts':0,'implicitSourceSubjectResolved':False,'C14ParentCoverageRaised':False,'wholeContextApplied':False,'newHTTPBodies':0,'newSourcePositions':0,'consumerChanged':False}
if '--write-results'in sys.argv:(B/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
