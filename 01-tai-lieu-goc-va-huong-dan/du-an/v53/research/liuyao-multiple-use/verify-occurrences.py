from pathlib import Path
from hashlib import sha256
import json,sys
S=Path(__file__).resolve().parent;W=next(p for p in S.parents if(p/'v53/engine.js').is_file())
def read(n):return json.loads((S/n).read_text(encoding='utf-8-sig'))
def check(p,x):
 b=p.read_bytes();assert len(b)==x['bytes'] and sha256(b).hexdigest()==x['sha256'],p
for x in read('OCCURRENCE_FREEZE.json')['files']:check(S/x['file'],x)
m=read('OCCURRENCE_MANUAL.json')
for key in ['retainedRuntime','reader','readerRules','priorComparisonReference']:check(W/m[key]['file'],m[key])
actual=read('ACTUAL_CAST_RUNTIME.json');assert actual['actualHHCHexNumberCalls']==5
triple=next(x for x in actual['cases']if x['id']==m['sourceExample']['fixtureID'])
assert len(triple['structuralChildren'])==3
assert {(x['kind'],x['line'],x['branch'])for x in triple['structuralChildren']}=={(x['layer'],x['line'],x['branch'])for x in m['sourceExample']['expectedOccurrences']}
assert m['kinBasis']=='primary-palace' and m['layerScope']=='primary-and-own-moving-changes'
assert not m['fullSelectionMethodEstablished']
e=read('OCCURRENCE_EXPECTED.json');assert e['threeUseOccurrenceCount']==3 and e['threeUseDistinctBranchCount']==2
out={'passed':True,'frozenFiles':2,'retainedPrintedCastFixtures':3,'retainedActualHHCHexNumberCalls':5,'sourceThreeUseOccurrences':3,'distinctBranchTokens':2,'newExternalEngineCalls':0,'newSourcePositions':0,'newHTTPBodies':0,'sourceAllChangedLinesActTogetherEstablished':False,'sourceTotalRankingEstablished':False,'wholeChapterApplied':False,'consumerChanged':False}
if '--write-results'in sys.argv:(S/'OCCURRENCE_SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
