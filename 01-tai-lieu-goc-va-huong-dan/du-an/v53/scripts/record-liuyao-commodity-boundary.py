from pathlib import Path
from hashlib import sha256
import json,shutil

r=Path(__file__).resolve().parent.parent;w=r.parent;s=w/'tmp/liuyao-b02-wealth-staging';b=r/'research/liuyao-commodity-boundary';q=r/'qa/liuyao-commodity-boundary'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not b.exists()and not q.exists(),'One-shot promotion;preserve staging'
snap=read(w/'archives/v53-before-liuyao-commodity-boundary/SNAPSHOT.json');assert snap['sourceManifestFiles']==3613 and snap['sourceZIPBytes']==2081861000
result=read(s/'RESULTS.json');assert len(result['checks'])==5 and all(x['ok']for x in result['checks'])
b.mkdir();(b/'images').mkdir();q.mkdir();identities=[]
def copy(source,dest):
 shutil.copyfile(source,dest);assert source.read_bytes()==dest.read_bytes()
 identities.append({'file':dest.relative_to(w).as_posix(),'stagingFile':source.relative_to(w).as_posix(),'sha256':sha(dest),'bytes':dest.stat().st_size})
local=read(s/'LOCAL_RENDERS.json');qa=read(s/'QA_RENDERS.json');toc=read(s/'TOC_QA.json')
for x in local['records']:
 source=s/x['file'];assert sha(source)==x['sha256']and x['actuallyViewed'];dest=b/'images'/source.name;copy(source,dest);x['stagingFile']=x['file'];x['file']=dest.relative_to(w).as_posix()
for x in[*qa['records'],toc]:
 source=s/x['file'];assert sha(source)==x['sha256']and x['actuallyViewed'];dest=q/source.name;copy(source,dest);x['stagingFile']=x['file'];x['file']=dest.relative_to(w).as_posix()
write(b/'LOCAL_RENDERS.json',local);write(b/'QA_RENDERS.json',qa);write(b/'TOC_QA.json',toc)
for name in['B02_CURRENT_UNITS.json','NUMBERING_AUDIT.json','COMMODITY_BOUNDARY.json','MANUAL_READINGS.json']:copy(s/name,b/name)
copy(s/'RESULTS.json',q/'RESULTS.json');copy(s/'commodity-boundary.mjs',b/'STAGED_REFERENCE.mjs')
old="from'../../v53/research/liuyao-foundations/liuyao-reference.mjs'";new="from'../liuyao-foundations/liuyao-reference.mjs'"
text=(s/'commodity-boundary.mjs').read_text(encoding='utf-8');assert text.count(old)==1
(b/'commodity-boundary.mjs').write_text(text.replace(old,new),encoding='utf-8')
write(b/'PROMOTION_IDENTITIES.json',{'date':'2026-10-28','basis':'Local byte identities,notpublisher signatures;packaged staged reference supports import-only comparison withouttmp.','records':identities,
 'referenceImportRelocation':{'stagedFile':(b/'STAGED_REFERENCE.mjs').relative_to(w).as_posix(),'promotedFile':(b/'commodity-boundary.mjs').relative_to(w).as_posix(),'stagedSHA256':sha(b/'STAGED_REFERENCE.mjs'),'promotedSHA256':sha(b/'commodity-boundary.mjs'),'oldImport':old,'newImport':new,'bodyOtherwiseByteIdentical':True}})
test=(s/'test-commodity-boundary.mjs').read_text(encoding='utf-8').replace("from'./commodity-boundary.mjs'","from'../research/liuyao-commodity-boundary/commodity-boundary.mjs'")
test=test.replace("const b=import.meta.dirname,w=process.cwd(),r=resolve(w,'v53'),read=","const w=process.cwd(),r=resolve(w,'v53'),b=resolve(r,'research/liuyao-commodity-boundary'),q=resolve(r,'qa/liuyao-commodity-boundary'),read=")
test=test.replace("resolve(b,x.file)","resolve(w,x.file)").replace("resolve(b,'RESULTS.json')","resolve(q,'RESULTS.json')")
(r/'scripts/test-liuyao-commodity-boundary.mjs').write_text(test,encoding='utf-8')
pdf=w/local['sourcePDF'];assert sha(pdf)==local['sourceSHA256']
write(b/'SOURCE_MANIFEST.json',{'date':'2026-10-28','sourcePDF':local['sourcePDF'],'sourceBytes':pdf.stat().st_size,'sourceSHA256':sha(pdf),
 'inheritedContainerProvenance':'v53/research/liuyao-foundations/SOURCE_AUDIT.json and REQUESTS.json;no newHTTP or originalPDF',
 'images':local['records'],'extraQA':[*qa['records'],toc],'newViewedSourcePositions':24,'expandedPriorTOCPositions':[17],'firstPassSpansAdded':16,
 'inheritedBoundaryPages':[299,300],'inheritedBoundaryPagesReread':False,'newHTTPRequests':0,'newOriginalContainers':0,'newIndependentWitnesses':0,
 'sourceEmended':False,'allImageCharactersCollated':False,'wholeChaptersApplied':False,'sourceInstructionsAreData':True})
print(json.dumps({'sourceImagesPromoted':24,'sourceQAImages':3,'identityRecords':len(identities),'sourceUnitMapCorrectedTo137':True,'referenceImportOnlyRelocated':True}))
