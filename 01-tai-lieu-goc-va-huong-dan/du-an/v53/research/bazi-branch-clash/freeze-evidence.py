from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
S=Path(__file__).resolve().parent;W=S.parent.parent
def read(n):return json.loads((S/n).read_text(encoding='utf-8'))
def save(n,d):(S/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not (S/'PREIMPLEMENTATION_FREEZE.json').exists()
d=read('SELECTED_CROPS.json')
for x in d['records']:x.update(actuallyViewed=True,accepted=True)
save('SELECTED_CROPS.json',d)
m=read('MANUAL_SOURCE_TABLES.json');horse=next(x for x in m['namedBreakings']if x['id']=='horse');horse['nativeSelectedGlyph']='己';horse['declaredSourceHorseBranch']=None;horse['glyphRoleUnresolved']=True;horse['fullRuleImplemented']=False;horse['note']='Selectednativealsohas己-shapedglyph;do not silentlynormalize巳. Preserveasopenliteral.';save('MANUAL_SOURCE_TABLES.json',m)
e=read('EXPECTED_BEFORE_IMPLEMENTATION.json');e['horseExample']=['unresolved-native-己-glyph','亥'];e['newEngineQueriesExpected']=6;e['reason']='Reuse2specificNaYinlookupsfromverifiedtrue-ghostcontextand12actualCHONGrowsfromharm.6otherpillarNaYinvaluesarenotcoveredbytheseselectedruntimeevidencefiles;querytheseonce.';e['newNaYinExpected']={k:v for k,v in e['newNaYinExpected'].items()if k not in ['己卯','己酉']};e['reusedNaYinExpected']={'己卯':'城头土','己酉':'大驿土'};save('EXPECTED_BEFORE_IMPLEMENTATION.json',e)
reuse=[]
for name,purpose in [('tmp/bazi-true-ghost-context-staging/ACTUAL_RUNTIME.json','Reuse己卯/己酉only'),('v53/research/bazi-branch-harm/ACTUAL_RUNTIME.json','Reuse12CHONGrows')]:
 p=W/name;reuse.append({'file':name,'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest(),'purpose':purpose,'queriesRerun':0})
save('REUSED_ACTUAL_EVIDENCE.json',{'records':reuse,'newEngineCallsInReuse':0})
files=['NATIVE_REVIEW.json','SELECTED_CROPS.json','CHAPTER_DISPOSITIONS.json','MANUAL_SOURCE_TABLES.json','EXPECTED_BEFORE_IMPLEMENTATION.json','REUSED_ACTUAL_EVIDENCE.json']
save('PREIMPLEMENTATION_FREEZE.json',{'frozenAtUTC':datetime.now(timezone.utc).isoformat(),'files':[{'file':n,'bytes':(S/n).stat().st_size,'sha256':sha256((S/n).read_bytes()).hexdigest()}for n in files],'purpose':'Readingsincludingunresolvedhorse己/repeated未,expectationsandruntimereusesfrozenbeforeimplementation.'})
print('Six evidence files frozen;horse glyph retained unresolved.')
