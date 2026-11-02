from pathlib import Path
from hashlib import sha256
import json,shutil

r=Path(__file__).resolve().parent.parent;w=r.parent;s=w/'tmp/liuyao-b02-exams-staging'
b=r/'research/liuyao-exam-intent';q=r/'qa/liuyao-exam-intent'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda p:sha256(p.read_bytes()).hexdigest()
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not b.exists() and not q.exists(),'One-shot promotion,keep staging'
snapshot=read(w/'archives/v53-before-liuyao-exam-intent/SNAPSHOT.json')
assert snapshot['sourceManifestFiles']==3549 and snapshot['sourceZIPBytes']==2075808140
result=read(s/'RESULTS.json');assert len(result['checks'])==8 and all(x['ok']for x in result['checks'])
b.mkdir();(b/'images').mkdir();q.mkdir();identities=[]
def copy(source,dest):
 shutil.copyfile(source,dest);assert source.read_bytes()==dest.read_bytes()
 identities.append({'file':dest.relative_to(w).as_posix(),'stagingFile':source.relative_to(w).as_posix(),'sha256':sha(dest),'bytes':dest.stat().st_size})
local=read(s/'LOCAL_RENDERS.json');qa=read(s/'QA_RENDERS.json')
for x in local['records']:
 source=s/x['file'];assert sha(source)==x['sha256'] and x['actuallyViewed']
 dest=b/'images'/source.name;copy(source,dest);x['stagingFile']=x['file'];x['file']=dest.relative_to(w).as_posix()
 if x['pdfPage']==300:x['note']='Chapter68 continuation with printed static 革 example. Role-chain distinctions do not imply a profit forecast;chapter68 remains open,next301.'
for x in qa['records']:
 source=s/x['file'];assert sha(source)==x['sha256'] and x['actuallyViewed']
 dest=q/source.name;copy(source,dest);x['stagingFile']=x['file'];x['file']=dest.relative_to(w).as_posix()
write(b/'LOCAL_RENDERS.json',local);write(b/'QA_RENDERS.json',qa)
manual=read(s/'MANUAL_READINGS.json');manual['records']=local['records']
write(b/'MANUAL_READINGS.json',manual)
for name in ['SOURCE_CONTEXTS.json','BOUNDED_CLAUSES.json','PRINTED_FIXTURE.json']:copy(s/name,b/name)
copy(s/'B02_CURRENT_UNITS.json',b/'STAGED_UNITS.json')
old_evidence='tmp/liuyao-b02-exams-staging/LOCAL_RENDERS.json;263inheritedfromfamily-study'
new_evidence='v53/research/liuyao-exam-intent/LOCAL_RENDERS.json;263inheritedfromfamily-study'
unit_text=(b/'STAGED_UNITS.json').read_text(encoding='utf-8');assert unit_text.count(old_evidence)==19
(b/'B02_CURRENT_UNITS.json').write_text(unit_text.replace(old_evidence,new_evidence),encoding='utf-8')
copy(s/'RESULTS.json',q/'RESULTS.json')
copy(s/'intent-reference.mjs',b/'STAGED_REFERENCE.mjs')
old_import="from'../../v53/research/liuyao-foundations/liuyao-reference.mjs'"
new_import="from'../liuyao-foundations/liuyao-reference.mjs'"
old=(s/'intent-reference.mjs').read_text(encoding='utf-8');assert old.count(old_import)==1
new=old.replace(old_import,new_import);(b/'intent-reference.mjs').write_text(new,encoding='utf-8')
assert new.replace(new_import,old_import)==old
write(b/'PROMOTION_IDENTITIES.json',{'date':'2026-10-28','basis':'Local byte identities,not publisher signatures;packaged provenance copy enables exact import-path-only comparison withouttmp.',
 'records':identities,'referenceImportRelocation':{'stagedFile':(b/'STAGED_REFERENCE.mjs').relative_to(w).as_posix(),'promotedFile':(b/'intent-reference.mjs').relative_to(w).as_posix(),'stagedSHA256':sha(b/'STAGED_REFERENCE.mjs'),'promotedSHA256':sha(b/'intent-reference.mjs'),'oldImport':old_import,'newImport':new_import,'bodyOtherwiseByteIdentical':True},
 'unitMapEvidenceRelocation':{'oldEvidence':old_evidence,'newEvidence':new_evidence,'replacements':19,'promotedSHA256':sha(b/'B02_CURRENT_UNITS.json')}})
test=(s/'test-intent-reference.mjs').read_text(encoding='utf-8').replace("from'./intent-reference.mjs'","from'../research/liuyao-exam-intent/intent-reference.mjs'")
test=test.replace("const b=import.meta.dirname,w=process.cwd(),r=resolve(w,'v53'),read=", "const w=process.cwd(),r=resolve(w,'v53'),b=resolve(r,'research/liuyao-exam-intent'),q=resolve(r,'qa/liuyao-exam-intent'),read=")
test=test.replace("resolve(b,x.file)","resolve(w,x.file)").replace("resolve(b,'RESULTS.json')","resolve(q,'RESULTS.json')")
test=test.replace("resolve(r,'PACKAGE_MANIFEST.json')","resolve(w,'archives/v53-before-liuyao-exam-intent/PACKAGE_MANIFEST.json')")
(r/'scripts/test-liuyao-exam-intent.mjs').write_text(test,encoding='utf-8')
pdf=w/local['sourcePDF'];assert sha(pdf)==local['sourceSHA256']
write(b/'SOURCE_MANIFEST.json',{'date':'2026-10-28','sourcePDF':local['sourcePDF'],'sourceBytes':pdf.stat().st_size,'sourceSHA256':sha(pdf),
 'inheritedContainerProvenance':'v53/research/liuyao-foundations/SOURCE_AUDIT.json and REQUESTS.json;v53/research/liuyao-family-study/SOURCE_MANIFEST.json;retainedoriginalPDF,no newdownload',
 'images':local['records'],'extraQA':qa['records'],'inheritedOpeningPDFPage':263,'nativePositionsActuallyViewed':37,'contentPositionsActuallyViewed':34,
 'nonRuleLeaves':[286,287,288],'firstPassSpansAdded':19,'newHTTPRequests':0,'newOriginalContainers':0,'newIndependentWitnesses':0,'sourceEmended':False,'allImageCharactersCollated':False,'wholeChaptersApplied':False,'sourceInstructionsAreData':True})
print(json.dumps({'imagesPromoted':37,'highResolutionQA':3,'identityRecords':len(identities),'referenceImportOnlyRelocated':True,'inheritedStagingChecks':8}))
