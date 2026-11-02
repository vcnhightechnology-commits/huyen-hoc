from pathlib import Path
from hashlib import sha256
import json
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def digest(p):return sha256(p.read_bytes()).hexdigest()
def check(r):
 p=W/r['file'];assert p.stat().st_size==r['bytes']and digest(p)==r['sha256'],r['file']
for r in read(B/'FREEZE.json')['files']+read(B/'PLAN.json')['sources']+read(B/'IDENTITY_INPUTS.json')['files']:check(r)
m=read(B/'MANUAL.json');unit=next(r for r in read(W/'tmp/bazi-seal-conditions-staging/CHAPTER_UNITS.json')['units']if r['id']=='S04');assert m['chapterUnit']==unit
for r in m['rows']:assert r['root']+r['sourceConnective']+r['target']in unit['text']
run=read(B/'ACTUAL_RUNTIME.json');plan=read(B/'PLAN.json');assert run['scriptSHA256']==digest(B/'run-once.mjs')and run['freezeSHA256']==digest(B/'FREEZE.json');assert run['librarySHA256']==digest(W/'v46/node_modules/lunar-typescript/dist/index.cjs')
for actuals,expected in [(run['newNaYin'],plan['missingNaYin']),(run['newStemElements'],plan['missingStemElements'])]:
 assert len(actuals)==len(expected)
 for a,e in zip(actuals,expected):assert all(a[k]==v for k,v in e.items())and a['actual']==e['expected']and a['newCall']
for a in run['reusedNaYin']+run['reusedStemElements']:
 r=a['retained'];src=read(W/r['file']);value=src[r['array']][r['index']][r['field']]if 'array'in r else src[r['object']][r['key']];assert value==a['actual']==a['expected']and not a['newCall']
assert run['reusedBranchPartners']==read(W/plan['branchPartnerPayload'])['partners']
assert run['newNaYinQueries']==8 and run['newStemElementQueries']==3 and len(run['reusedNaYin'])==7 and len(run['reusedStemElements'])==7
assert run['actualCalendarObjects']==run['actualNatalCharts']==0 and not run['sourceMechanismsAdjudicated']
out={'passed':True,'frozenFiles':4,'sourcePrintedPairs':10,'sourceUnitCodepoints':len(unit['text']),'previouslyNewNaYinQueriesRetained':8,'previouslyNewStemElementQueriesRetained':3,'retainedNaYinQueriesReused':7,'retainedStemElementsReused':7,'retainedBranchPartnerRows':12,'newEngineCallsDuringVerification':0,'newHTTPBodies':0,'sourceMechanismsAdjudicated':False,'consumerChanged':False}
(B/'SOURCE_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
