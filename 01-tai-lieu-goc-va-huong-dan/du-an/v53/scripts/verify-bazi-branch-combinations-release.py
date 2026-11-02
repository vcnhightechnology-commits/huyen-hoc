from pathlib import Path
from hashlib import sha256
import json,subprocess,zipfile,sys

v=Path(__file__).resolve().parent.parent;w=v.parent;q=v/'qa/bazi-branch-combinations'
q.mkdir(exist_ok=True,parents=True)
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
prepare='--prepare'in sys.argv
def digest(p):
 h=sha256()
 with p.open('rb')as f:
  for b in iter(lambda:f.read(4*1024*1024),b''):h.update(b)
 return h.hexdigest()
scopes={}
for name,testfile in [('bazi-branch-union','test-union-reference.mjs'),('bazi-branch-triad','test-triad-reference.mjs')]:
 r=v/'research'/name;qa=v/'qa'/name
 for x in read(qa/'PROMOTION_IDENTITIES.json')['byteExactFiles']:
  p=w/x['target'];assert p.stat().st_size==x['bytes']and digest(p)==x['sha256'],x['target']
 tests=json.loads(subprocess.run(['node',str(r/testfile)],check=True,capture_output=True,text=True,encoding='utf-8').stdout)
 source=json.loads(subprocess.run([sys.executable,str(r/'verify-source.py')],check=True,capture_output=True,text=True,encoding='utf-8').stdout)
 assert tests==read(qa/'REFERENCE_RESULTS.json')and source==read(qa/'SOURCE_RESULTS.json')
 scopes[name]={'sourceChecks':source,'referenceTests':tests}
a=w/'archives/v53-before-bazi-branch-union';snap=read(a/'SNAPSHOT.json');assert snap['sourceManifestFiles']==5941
for x in snap['files']:assert(a/x['file']).stat().st_size==x['bytes']and digest(a/x['file'])==x['sha256'],x['file']
assert next(x for x in snap['files']if x['file']=='Huyen_Hoc_Cac_V53_source.zip')['sha256']=='9140177e4f230b49f60875b60cf82ef4d19af8e75d7898c90437319d9fe2e95d'
allowed={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'}
old=read(a/'PACKAGE_MANIFEST.json')['files'];assert len(old)==5941
for x in old:
 if x['file']not in allowed:assert(v/x['file']).stat().st_size==x['bytes']and digest(v/x['file'])==x['sha256'],x['file']
assert(w/'EXHAUSTIVE_WORK_STATE.json').read_bytes()==(v/'research/EXHAUSTIVE_WORK_STATE.json').read_bytes()
assert digest(w/'Huyen_Hoc_Cac_V53_web.zip')==digest(a/'Huyen_Hoc_Cac_V53_web.zip')
html=(v/'Huyen_Hoc_Cac.html').read_bytes();assert html==(w/'Huyen_Hoc_Cac.html').read_bytes()==(v/'site/index.html').read_bytes()
assert sha256(html).hexdigest()=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert{p.relative_to(v/'site').as_posix()for p in(v/'site').rglob('*')if p.is_file()}=={'index.html'}
c=read(v/'research/library-current/COVERAGE.json');assert c['conclusion']=='NOT_ALL_APPLIED'and c['counts']['wholeWorkApplied']==0 and c['counts']['catalogueRecords']==40
b02=next(x for x in c['catalogue']if x['id']=='B02');assert b02['currentUnitMap']=='v53/research/liuyao-foundation-span/B02_CURRENT_UNITS.json'
p08=next(x for x in c['catalogue']if x['id']=='P08');assert p08['currentMonthLabelState']=='v53/research/home-month-labels/WORK_STATE.json'
food=read(v/'research/bazi-food-chain/CURRENT_CONTEXT_COVERAGE.json')['counts'];assert food['parentsWithSelectedModuleOrDeclaredPremiseLinks']==44 and food['parentsWithoutSuchLinks']==46 and food['wholeParentsApplied']==0
union=read(v/'research/bazi-branch-union/NATIVE_REVIEW.json');triad=read(v/'research/bazi-branch-triad/NATIVE_REVIEW.json')
newPositions={r['page']for r in union['records']if r['actuallyViewed']}|set(triad['firstPassNewPositions']);assert newPositions==set(range(191,206))
assert [r['page']for r in union['records']if not r['actuallyViewed']]==[200,201,202]
for page in [199,200,201,202]:assert(v/f'research/bazi-branch-union/p{page}.png').read_bytes()==(v/f'research/bazi-branch-triad/p{page}.png').read_bytes()
assert scopes['bazi-branch-union']['referenceTests']['digitalCleanCodepoints']+scopes['bazi-branch-triad']['referenceTests']['digitalCleanCodepoints']==1894
positionIndex=read(v/'research/library-current/TMTH002_NATIVE_POSITION_COVERAGE.json')
indexed=set()
for item in positionIndex['scopes']:
 x=item['evidence'];p=w/x['file'];assert p.stat().st_size==x['bytes']and digest(p)==x['sha256'],x['file']
 indexed.update(item['positions'])
assert indexed==set(positionIndex['distinctPositionsViewed'])and len(indexed)==59
assert positionIndex['remainingNotEstablishedByThisIndex']==[i for i in range(1,233)if i not in indexed]
assert positionIndex['remainingCount']==173 and not positionIndex['wholeVolumeApplied']
files=[p for p in v.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json'];payload=q/'RELEASE_RESULTS.json'
if prepare:count=len(files)+(not payload.exists())
else:
 m=read(v/'PACKAGE_MANIFEST.json');count=len(m['files']);assert{p.relative_to(v).as_posix()for p in files}=={x['file']for x in m['files']}
 with zipfile.ZipFile(w/'Huyen_Hoc_Cac_V53_source.zip')as z:
  assert set(z.namelist())=={'v53/'+x['file']for x in m['files']}|{'v53/PACKAGE_MANIFEST.json'}
  assert z.read('v53/PACKAGE_MANIFEST.json')==(v/'PACKAGE_MANIFEST.json').read_bytes()
  for x in m['files']:
   p=v/x['file'];assert p.stat().st_size==x['bytes']and digest(p)==x['sha256'],x['file'];h=sha256();size=0
   with z.open('v53/'+x['file'])as f:
    for b in iter(lambda:f.read(4*1024*1024),b''):h.update(b);size+=len(b)
   assert size==x['bytes']and h.hexdigest()==x['sha256'],x['file']
out={'date':'2026-10-29','scopes':scopes,'uniqueSourcePositionsNewlyViewed':15,'editorialChapterUnits':36,
 'digitalCleanCodepoints':1894,'digitalUTF16Units':1897,'retainedActualHHCTenGodCalls':20,
 'retainedActualLunarPartnerTableQueries':12,'retainedActualLunarLuQueries':3,
 'oldV53FilesUnchanged':len(old)-len(allowed),'manifestFiles':count,'sourceZIPEntries':count+1,
 'wholeCatalogueCompleted':False,'consumerChanged':False,'publicSiteOnlyIndex':True,
 'newEngineCallsDuringVerification':0,'newHTTPBodiesDuringScope':0,'newNatalCharts':0}
if prepare:payload.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'prepared':True,'manifestFiles':count}),flush=True)
else:assert read(payload)==out;print(json.dumps({'finalReadOnlyVerificationPassed':True,**out}),flush=True)
