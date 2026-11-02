"""Check promoted byte identities, source verifiers and the new parent map without engine reruns."""
from pathlib import Path
from hashlib import sha256
import json,subprocess,sys,copy
W=Path(__file__).resolve().parent.parent
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def digest(p):return sha256(p.read_bytes()).hexdigest()
scopes=[('bazi-food-strength','verify-source.py','FOOD-00-C13'),('bazi-food-luck-subject','verify-source-runtime.py','FOOD-00-C14')]
results={};identities=0
for name,script,parent in scopes:
 b=W/'v53/research'/name;q=W/'v53/qa'/name
 for row in read(q/'PROMOTION_IDENTITIES.json')['byteExactFiles']:
  p=W/row['target'];assert p.stat().st_size==row['bytes']and digest(p)==row['sha256'];assert p.read_bytes()==(W/row['source']).read_bytes();identities+=1
 result=json.loads(subprocess.run([sys.executable,str(b/script)],check=True,capture_output=True,text=True,encoding='utf-8').stdout)
 assert result['passed'] and result['newEngineCallsDuringVerification']==0;results[name]=result
 adoption=read(b/'RELEASE_ADOPTION.json');assert adoption['currentPartialLinkedParents']==46 and adoption['unlinkedParents']==44 and adoption['wholeParentsApplied']==0
matrix=read(W/'v53/research/bazi-food-strength/CURRENT_CONTEXT_COVERAGE.json');old=read(W/matrix['previousMatrix'])
assert digest(W/matrix['previousMatrix'])==matrix['previousMatrixSHA256']
assert len(matrix['records'])==90 and [r['id'] for r in matrix['records']]==[r['id']for r in old['records']]
assert sum(bool(r['selectedModuleLinks'])for r in matrix['records'])==46
assert sum(not bool(r['selectedModuleLinks'])for r in matrix['records'])==44
assert not any(r['wholeContextApplied']or r['sourceOutcomeValidated']for r in matrix['records'])
added=[]
for r,before in zip(matrix['records'],old['records']):
 expected=copy.deepcopy(before)
 if r['id'] in ['FOOD-00-C13','FOOD-00-C14']:
  assert before['selectedModuleLinks']==[] and len(r['selectedModuleLinks'])==1
  link=r['selectedModuleLinks'][0];assert not link['wholeContextApplied']and digest(W/link['module'])==link['sha256']
  expected['selectedModuleLinks'].append(link);added.append(r['id'])
 assert r==expected,r['id']
coverage=read(W/'v53/research/library-current/COVERAGE.json');m=next(x for x in coverage['catalogue']if x['id']=='M01')
assert m['foodParentContextSelection']['currentMatrix']=='v53/research/bazi-food-strength/CURRENT_CONTEXT_COVERAGE.json'
assert m['foodParentContextSelection']['parentsWithSelectedModuleOrDeclaredPremiseLinks']==46
assert not m['wholeWorkApplied']
html=(W/'Huyen_Hoc_Cac.html').read_bytes();assert digest(W/'Huyen_Hoc_Cac.html')=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html==(W/'v53/Huyen_Hoc_Cac.html').read_bytes()==(W/'v53/site/index.html').read_bytes()
out={'passed':True,'promotedByteIdentities':identities,'sourceChecks':results,'newParentLinks':added,'currentMatrixCounts':[46,44,0],
 'previousFrozenMatrixBytesUnchanged':True,'newEngineCallsDuringVerification':0,'consumerChanged':False,'wholeCatalogueCompleted':False}
(W/'v53/qa/bazi-food-strength/INTEGRATION_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items()if k!='sourceChecks'}))
