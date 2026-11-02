from pathlib import Path
from hashlib import sha256
import json,shutil
w=Path.cwd();assert(w/'v53/engine.js').exists();r=w/'v53';s=w/'tmp/bazi-food-core-staging';b=r/'research/bazi-food-core';q=r/'qa/bazi-food-core'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not b.exists()and not q.exists(),'One-shot promotion,preserveearlierfiles'
snap=read(w/'archives/v53-before-bazi-food-core/SNAPSHOT.json');assert snap['sourceManifestFiles']==3927 and snap['sourceZIPBytes']==2107724336
results=[read(s/n)for n in ['RESULTS.json','TEN_RELATION_RESULTS.json']];assert sum(len(x['checks'])for x in results)==8 and all(c['ok']for x in results for c in x['checks'])
b.mkdir();q.mkdir();ids=[];relocations=[]
def copy(name,dest):
    src=s/name;shutil.copyfile(src,dest);assert src.read_bytes()==dest.read_bytes();ids.append({'file':dest.relative_to(w).as_posix(),'stagingFile':src.relative_to(w).as_posix(),'bytes':dest.stat().st_size,'sha256':sha(dest)})
for n in ['SELECTED_PREDICATES.json','core-reference.mjs']:copy(n,b/n)
for n in ['WORK_STATE.json','test-core.mjs','test-ten-relations.mjs','build-selected.py']:copy(n,b/('STAGED_'+n))
for n in ['RESULTS.json','TEN_RELATION_RESULTS.json']:copy(n,q/n)
for name,target in [('test-core.mjs','test-bazi-food-core.mjs'),('test-ten-relations.mjs','test-bazi-food-ten-relations.mjs')]:
    t=(s/name).read_text(encoding='utf-8');a=t.replace("from'./core-reference.mjs'","from'../research/bazi-food-core/core-reference.mjs'").replace("s=new URL('./',import.meta.url)","s=new URL('../qa/bazi-food-core/',import.meta.url)").replace("new URL('TEN_RELATION_RESULTS.json',import.meta.url)","new URL('../qa/bazi-food-core/TEN_RELATION_RESULTS.json',import.meta.url)").replace('archives/v53-before-bazi-food-source/','archives/v53-before-bazi-food-core/')
    dest=r/'scripts'/target;dest.write_text(a,encoding='utf-8');relocations.append({'staged':(b/('STAGED_'+name)).relative_to(w).as_posix(),'promoted':dest.relative_to(w).as_posix(),'onlyImportOutputAndSnapshotPathsChanged':True})
write(b/'PROMOTION_IDENTITIES.json',{'date':'2026-10-28','records':ids,'referenceModuleByteIdentical':True,'testPathRelocations':relocations,'passedTestsNotRerunForCounts':True,'localIdentitiesNotPublisherSignatures':True})
staged=read(s/'WORK_STATE.json');write(b/'SOURCE_MANIFEST.json',{'date':'2026-10-28','catalogueID':'M01','sourceContextFile':staged['sourceContextFile'],'sourceContextSHA256':staged['sourceContextSHA256'],'sourceCorpus':'v53/research/bazi-food-source/CONTEXTS.json','sourceImageManifest':'v53/research/bazi-food-source/SOURCE_MANIFEST.json','sourceContinuityGapAudit':'v53/research/bazi-food-source/CONTINUITY_AUDIT.json','selectedSourceParentContexts':8,'selectedClauses':12,'selectedCodepoints':135,'subordinateClausesOfSelectedParentsStillOpen':True,'otherUnselectedParentContexts':82,'actualModules':staged['actualModules'],'newHTTPRequests':0,'newOriginalContainers':0,'newIndependentWitnesses':0,'newViewedSourcePositions':0,'consumerChanged':False})
shutil.copyfile(Path(__file__),r/'scripts/record-bazi-food-core.py')
print(json.dumps({'promotionIdentities':len(ids),'moduleByteIdentical':True,'checks':8,'newSourcePositions':0}))
