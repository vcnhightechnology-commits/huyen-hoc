"""Current three-layer source adoption, including the explicit late-seal exception."""
from pathlib import Path
from hashlib import sha256
import json,sqlite3,subprocess,sys,copy
W=Path(__file__).resolve().parent.parent
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def h(p):return sha256(p.read_bytes()).hexdigest()
specs=[('bazi-food-transformation','FOOD-00-C16','verify-source-runtime.py'),('bazi-food-quantity','FOOD-00-C23','verify-source.py'),('bazi-food-fire-exception','FOOD-00-C31','verify-source.py')]
checks={};identities=0;prefix_identities=0
for name,parent,script in specs:
 b=W/'v53/research'/name;q=W/'v53/qa'/name
 for row in read(q/'PROMOTION_IDENTITIES.json')['byteExactFiles']:
  p=W/row['target'];assert p.stat().st_size==row['bytes']and h(p)==row['sha256'];assert p.read_bytes()==(W/row['source']).read_bytes();identities+=1
 if(b/'POST_INVENTORY_IDENTITIES.json').exists():
  for row in read(b/'POST_INVENTORY_IDENTITIES.json')['files']:
   p=W/row['file'];assert p.stat().st_size==row['bytes']and h(p)==row['sha256'];prefix_identities+=1
 result=json.loads(subprocess.run([sys.executable,str(b/script)],check=True,capture_output=True,text=True,encoding='utf-8').stdout)
 assert result['passed']and result['newEngineCallsDuringVerification']==0;checks[name]=result
 a=read(b/'RELEASE_ADOPTION.json');assert a['currentPartialLinkedParents']==49 and a['unlinkedParents']==41 and a['wholeParentsApplied']==0
matrix=read(W/'v53/research/bazi-food-quantity/CURRENT_CONTEXT_COVERAGE.json');old=read(W/matrix['previousMatrix']);assert h(W/matrix['previousMatrix'])==matrix['previousMatrixSHA256']
assert len(matrix['records'])==90 and sum(bool(r['selectedModuleLinks'])for r in matrix['records'])==49
assert sum(not r['selectedModuleLinks']for r in matrix['records'])==41
assert not any(r['wholeContextApplied']or r['sourceOutcomeValidated']for r in matrix['records'])
for r,before in zip(matrix['records'],old['records']):
 expected=copy.deepcopy(before);assert r['id']==before['id']
 if r['id']in [x[1]for x in specs]:
  assert before['selectedModuleLinks']==[]and len(r['selectedModuleLinks'])==1;link=r['selectedModuleLinks'][0];assert h(W/link['module'])==link['sha256']and not link['wholeContextApplied'];expected['selectedModuleLinks'].append(link)
 assert expected==r,r['id']
c=sqlite3.connect('file:'+(W/'recovery/consolidated-history/INDEX.sqlite').as_posix()+'?mode=ro',uri=True)
assert c.execute('PRAGMA integrity_check').fetchone()[0]=='ok';old_scripts=0
exception=read(W/'v53/research/bazi-food-fire-exception/SEQUENCE_EXCEPTION.json')
for row in exception['initialFiles']:
 if Path(row['file']).name in ['freeze-source.py','test-fire-exception-reference.mjs','verify-source.py']:
  content=c.execute('SELECT path,bytes FROM content WHERE sha256=?',(row['sha256'],)).fetchone();assert content and content[1]==row['bytes'];assert h(W/content[0])==row['sha256']
  assert c.execute('SELECT 1 FROM revisions WHERE path=?and sha256=?',(row['file'],row['sha256'])).fetchone();old_scripts+=1
c.close();assert old_scripts==3
assert read(W/'v53/research/bazi-food-fire-exception/SOURCE_EXPECTATIONS_SEAL.json')['preimplementationFreezeEstablished']is False
coverage=read(W/'v53/research/library-current/COVERAGE.json');m=next(x for x in coverage['catalogue']if x['id']=='M01');assert m['foodParentContextSelection']['currentMatrix']=='v53/research/bazi-food-quantity/CURRENT_CONTEXT_COVERAGE.json'
assert m['foodParentContextSelection']['parentsWithSelectedModuleOrDeclaredPremiseLinks']==49 and not m['wholeWorkApplied']
html=(W/'Huyen_Hoc_Cac.html').read_bytes();assert h(W/'Huyen_Hoc_Cac.html')=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html==(W/'v53/Huyen_Hoc_Cac.html').read_bytes()==(W/'v53/site/index.html').read_bytes()
out={'passed':True,'promotedByteIdentities':identities,'historicalPrivatePrefixIdentitiesVerified':prefix_identities,'sourceChecks':checks,
 'currentMatrixCounts':[49,41,0],'previousFrozenMatrixUnchanged':True,'lateSealC31ExceptionExplicit':True,
 'initialC31ScriptRevisionsVerifiedInSHAIndex':old_scripts,'newEngineCallsDuringVerification':0,'consumerChanged':False,'wholeCatalogueCompleted':False}
(W/'v53/qa/bazi-food-quantity/INTEGRATION_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items()if k!='sourceChecks'}))
