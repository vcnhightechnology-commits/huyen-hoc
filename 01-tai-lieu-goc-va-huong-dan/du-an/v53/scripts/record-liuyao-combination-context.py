from pathlib import Path
from hashlib import sha256
import json,shutil
w=Path(__file__).resolve().parent.parent;r=w/'v53';s=w/'tmp/liuyao-b02-effectiveness-staging';b=r/'research/liuyao-combination-context';q=r/'qa/liuyao-combination-context'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not b.exists()and not q.exists(),'One-shot;allpriorreleasespreserved'
snapshot=read(w/'archives/v53-before-liuyao-combination-context/SNAPSHOT.json');assert snapshot['sourceManifestFiles']==3816 and snapshot['sourceZIPBytes']==2097811576
results=[read(s/n)for n in['RESULTS.json','COMBINATION_RESULTS.json','TRIAD_RESULTS.json']];assert sum(len(x['checks'])for x in results)==16 and all(c['ok']for x in results for c in x['checks'])
b.mkdir();q.mkdir();ids=[];relocations=[]
def copy(src,dest):
 shutil.copyfile(src,dest);assert src.read_bytes()==dest.read_bytes();ids.append({'file':dest.relative_to(w).as_posix(),'stagingFile':src.relative_to(w).as_posix(),'bytes':dest.stat().st_size,'sha256':sha(dest)})
for n in['SOURCE_MANIFEST.json','COMBINATION_SOURCE_MANIFEST.json','TRIAD_FIXTURE.json','FAILURE_AUDIT.json']:copy(s/n,b/n)
for n in['RESULTS.json','COMBINATION_RESULTS.json','TRIAD_RESULTS.json','CROP.json','TRIAD_CROP.json','TRIAD_FIXTURE_CROP.json','RENDER_REPRODUCTION.json','combination-caveat-51.png','combination-context-51.png','triad-modes-78.png','qa420-78.png','triad-modes-78-420.png','inner-outer-cast-79.png','inner-outer-cast-79-expanded.png','redecode-78-420.png']:copy(s/n,q/n)
for name in['origin-support-reference.mjs','combination-forms-reference.mjs','triad-context-reference.mjs']:
 original=b/('STAGED_'+name);copy(s/name,original);t=original.read_text(encoding='utf-8');a=t.replace("from'../../v53/research/liuyao-use-god/use-god-reference.mjs'","from'../liuyao-use-god/use-god-reference.mjs'").replace("from'../../v53/research/liuyao-day-month/day-month-reference.mjs'","from'../liuyao-day-month/day-month-reference.mjs'").replace("from'../../v53/research/liuyao-foundations/liuyao-reference.mjs'","from'../liuyao-foundations/liuyao-reference.mjs'")
 assert a!=t;dest=b/name;dest.write_text(a,encoding='utf-8');relocations.append({'stagedFile':original.relative_to(w).as_posix(),'promotedFile':dest.relative_to(w).as_posix(),'stagedSHA256':sha(original),'promotedSHA256':sha(dest),'bodyOtherwiseIdentical':True,'onlyChange':'three allowed relative import prefixes'})
for name in['test-origin-support.mjs','test-combination-forms.mjs','test-triad-context.mjs']:
 copy(s/name,b/('STAGED_'+name));t=(s/name).read_text(encoding='utf-8')
 t=t.replace("from'./origin-support-reference.mjs'","from'../research/liuyao-combination-context/origin-support-reference.mjs'").replace("from'./combination-forms-reference.mjs'","from'../research/liuyao-combination-context/combination-forms-reference.mjs'").replace("from'./triad-context-reference.mjs'","from'../research/liuyao-combination-context/triad-context-reference.mjs'").replace("s=new URL('./',import.meta.url)","s=new URL('../research/liuyao-combination-context/',import.meta.url)")
 t=t.replace("read('../../v53/research/liuyao-use-god/SOURCE_FIXTURES.json')","read('../liuyao-use-god/SOURCE_FIXTURES.json')").replace("new URL('../../v53/engine.js',s)","new URL('../../engine.js',s)").replace("new URL('../../'+x.file,s)","new URL('../../../'+x.file,s)")
 for n in['RESULTS.json','COMBINATION_RESULTS.json','TRIAD_RESULTS.json']:t=t.replace("new URL('"+n+"',s)","new URL('../../qa/liuyao-combination-context/"+n+"',s)")
 (r/'scripts'/('test-liuyao-'+name[5:])).write_text(t,encoding='utf-8')
copy(Path(__file__),r/'scripts/record-liuyao-combination-context.py')
write(b/'PROMOTION_IDENTITIES.json',{'date':'2026-10-28','records':ids,'referenceImportRelocations':relocations,'oldSourceImagesReferencedNotDuplicated':12,'localIdentitiesNotPublisherSignatures':True,'passedTestsExecutedInStagingNotRerunForCounts':True})
print(json.dumps({'promotionIdentityRecords':len(ids),'importOnlyModules':3,'passingChecks':16,'sourceImagesReferenced':12,'sourceOriginalBytesChanged':False}))
