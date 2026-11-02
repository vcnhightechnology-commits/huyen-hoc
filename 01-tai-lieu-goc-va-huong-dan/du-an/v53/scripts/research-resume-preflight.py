from pathlib import Path
from hashlib import sha256
import json,argparse
V53=Path(__file__).resolve().parent.parent
ROOT=V53.parent
def read(path):return json.loads(path.read_text(encoding='utf-8-sig'))
def assess_resume(catalogue,scope=None,index=None,coverage=None):
 index=read(V53/'research/library-current/RESUME_INDEX.json')if index is None else index
 coverage=read(V53/'research/library-current/COVERAGE.json')if coverage is None else coverage
 entry=index['catalogues'].get(catalogue)
 if entry is None:return {'catalogue':catalogue,'scope':scope,'disposition':'catalogue-not-indexed-review-coverage-first','currentMap':None,'newSourceCase':None,'wholeCatalogueCompleted':False,'newEngineCalls':0}
 current=next((x for x in coverage['catalogue']if x['id']==catalogue),None)
 if current is None:raise ValueError('Indexed catalogue absent from coverage.')
 if current['currentB02UnitMap']!=entry['currentMap']:raise ValueError('Current coverage pointer contradicts explicitly indexed released map.')
 target=(ROOT/entry['currentMap']).resolve()
 if not target.is_relative_to(ROOT.resolve()):raise ValueError('Map path outside research workspace.')
 raw=target.read_bytes();identity=entry['currentMapIdentity']
 if target.stat().st_size!=identity['bytes']or sha256(raw).hexdigest()!=identity['sha256']:raise ValueError('Indexed map identity changed; review and update provenance explicitly.')
 units=json.loads(raw.decode('utf-8-sig'))
 for key,value in entry['expectedCounts'].items():
  if units['currentCounts'][key]!=value:raise ValueError('Indexed map count mismatch: '+key)
 if len(units['units'])!=137 or len({x['id']for x in units['units']})!=137 or any(x['entireUnitApplied']for x in units['units']):raise ValueError('137 distinct first-pass units must retain zero entire-unit applications.')
 c=current['currentSourceUnitCounts']
 for actual,expected in [('registeredUnits','registeredUnits'),('firstPassSpans','firstPassCompleteSpanUnits'),('headingOnly','headingOnlyBodyUnits'),('partialFoundation','partialFoundationUnits'),('otherPartial','otherPartialUnits'),('wholeUnitsApplied','wholeUnitsApplied')]:
  if c[actual]!=entry['expectedCounts'][expected]:raise ValueError('Coverage counts contradict released map: '+actual)
 known=entry['knownScopes'].get(scope)
 disposition='current-map-verified'if scope is None else known['disposition']if known else index['unknownScopeDisposition']
 return {'catalogue':catalogue,'scope':scope,'disposition':disposition,'currentMap':entry['currentMap'],'currentMapCounts':entry['expectedCounts'].copy(),'reuseReport':known.get('report')if known else None,'reuseModule':known.get('module')if known else None,'newSourceCase':known.get('newSourceCase')if known else None,'wholeChapterApplied':False,'wholeCatalogueCompleted':False,'newEngineCalls':0,'scopeIndexIsExhaustive':False}
if __name__=='__main__':
 p=argparse.ArgumentParser(description='Read-only bounded research-resume guard; does not execute calculation engines.')
 p.add_argument('--catalogue',required=True);p.add_argument('--scope');args=p.parse_args()
 print(json.dumps(assess_resume(args.catalogue,args.scope),ensure_ascii=False))
