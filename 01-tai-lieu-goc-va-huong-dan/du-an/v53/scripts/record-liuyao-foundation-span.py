from pathlib import Path
from hashlib import sha256
import json,shutil
w=Path(__file__).resolve().parent.parent;r=w/'v53';s=w/'tmp/liuyao-b02-foundation-span-staging';b=r/'research/liuyao-foundation-span';q=r/'qa/liuyao-foundation-span'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not b.exists()and not q.exists(),'One-shot;preserve all prior releases'
snap=read(w/'archives/v53-before-liuyao-foundation-span/SNAPSHOT.json');assert snap['sourceManifestFiles']==3778 and snap['sourceZIPBytes']==2095344337
tests=read(s/'RESULTS.json');assert len(tests['checks'])==7 and all(x['ok']for x in tests['checks'])
assert read(s/'SOURCE_RESULTS.json')['retainedImageHashesVerified']==28
b.mkdir();q.mkdir();ids=[];relocations=[]
def copy(src,dest):
 shutil.copyfile(src,dest);assert src.read_bytes()==dest.read_bytes();ids.append({'file':dest.relative_to(w).as_posix(),'stagingFile':src.relative_to(w).as_posix(),'bytes':dest.stat().st_size,'sha256':sha(dest)})
for name in['SOURCE_MANIFEST.json','MANUAL_READINGS.json','FOUNDATIONAL_CONTEXTS.json','MOTION_FIXTURES.json','PRINTED_DIAGRAMS.json','SOURCE_ANOMALIES.json','B02_CURRENT_UNITS.json']:copy(s/name,b/name)
for name in['DIAGRAM_COMPARISON.json','RESULTS.json','SOURCE_RESULTS.json','QA_RENDERS.json','MOTION_CROP.json','qa360-26.png','qa360-29.png','qa360-33.png','anomaly-crop-26.png','anomaly-crop-29.png','anomaly-crop-33.png','motion-crop-48.png','redecode-26-230.png','redecode-29-360.png']:copy(s/name,q/name)
for name in['motion-reference.mjs','diagram-reference.mjs']:
 original=b/('STAGED_'+name);copy(s/name,original);old="from'../../v53/research/liuyao-foundations/liuyao-reference.mjs'";new="from'../liuyao-foundations/liuyao-reference.mjs'";t=original.read_text(encoding='utf-8');assert t.count(old)==1;target=b/name;target.write_text(t.replace(old,new),encoding='utf-8');relocations.append({'stagedFile':original.relative_to(w).as_posix(),'promotedFile':target.relative_to(w).as_posix(),'stagedSHA256':sha(original),'promotedSHA256':sha(target),'oldImport':old,'newImport':new,'bodyOtherwiseIdentical':True})
for name in['audit-diagrams.mjs','test-foundation-span.mjs','record-span.py','verify-source.py']:copy(s/name,b/('STAGED_'+name))
copy(Path(__file__),r/'scripts/record-liuyao-foundation-span.py')
audit=(s/'audit-diagrams.mjs').read_text(encoding='utf-8').replace("from'../../v53/research/liuyao-foundations/liuyao-reference.mjs'","from'../research/liuyao-foundations/liuyao-reference.mjs'").replace("s=new URL('./',import.meta.url)","s=new URL('../research/liuyao-foundation-span/',import.meta.url)").replace("new URL('../../v53/engine.js',s)","new URL('../../engine.js',s)").replace("new URL('DIAGRAM_COMPARISON.json',s)","new URL('../../qa/liuyao-foundation-span/DIAGRAM_COMPARISON.json',s)")
(r/'scripts/audit-liuyao-printed-diagrams.mjs').write_text(audit,encoding='utf-8')
test=(s/'test-foundation-span.mjs').read_text(encoding='utf-8').replace("from'./motion-reference.mjs'","from'../research/liuyao-foundation-span/motion-reference.mjs'").replace("from'./diagram-reference.mjs'","from'../research/liuyao-foundation-span/diagram-reference.mjs'").replace("s=new URL('./',import.meta.url),read=async n=>JSON.parse(await readFile(new URL(n,s),'utf8'))","s=new URL('../research/liuyao-foundation-span/',import.meta.url),q=new URL('../../qa/liuyao-foundation-span/',s),read=async n=>JSON.parse(await readFile(new URL(n,n==='DIAGRAM_COMPARISON.json'?q:s),'utf8'))").replace("new URL('../../'+m.sourcePDF,s)","new URL('../../../'+m.sourcePDF,s)").replace("new URL('../../'+x.file,s)","new URL('../../../'+x.file,s)").replace("new URL('../../v53/engine.js',s)","new URL('../../engine.js',s)").replace("new URL('RESULTS.json',s)","new URL('RESULTS.json',q)")
(r/'scripts/test-liuyao-foundation-span.mjs').write_text(test,encoding='utf-8')
write(b/'PROMOTION_IDENTITIES.json',{'date':'2026-10-28','records':ids,'referenceImportRelocations':relocations,'localIdentitiesNotPublisherSignatures':True,'oldSourceImagesReferencedNotDuplicated':28,'allChecksExecutedInStagingNotRerunForCounts':True})
print(json.dumps({'newIdentityRecords':len(ids),'moduleImportOnlyRelocations':len(relocations),'sourceRows':384,'oldImagesReferenced':28,'scope':'liuyao-foundation-span'}))
