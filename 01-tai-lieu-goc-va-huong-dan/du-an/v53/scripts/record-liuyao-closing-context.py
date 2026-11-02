from pathlib import Path
from hashlib import sha256
import json,shutil

r=Path(__file__).resolve().parent.parent;w=r.parent;s1=w/'tmp/liuyao-b02-house-family-staging';s2=w/'tmp/liuyao-b02-closing-staging'
b=r/'research/liuyao-closing-context';q=r/'qa/liuyao-closing-context'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not b.exists()and not q.exists(),'One-shot promotion;preserve staging'
snapshot=read(w/'archives/v53-before-liuyao-closing-context/SNAPSHOT.json');assert snapshot['sourceManifestFiles']==3663 and snapshot['sourceZIPBytes']==2085566508
first,closing=read(s1/'RESULTS.json'),read(s2/'RESULTS.json');assert len(first['checks'])==6 and len(closing['checks'])==8 and all(x['ok']for x in first['checks']+closing['checks'])
b.mkdir();(b/'images').mkdir();q.mkdir();identities=[]
def copy(source,dest):
 shutil.copyfile(source,dest);assert source.read_bytes()==dest.read_bytes()
 identities.append({'file':dest.relative_to(w).as_posix(),'stagingFile':source.relative_to(w).as_posix(),'sha256':sha(dest),'bytes':dest.stat().st_size})

all_images=[];all_qa=[]
for staging,prefix in[(s1,'TRAVELER'),(s2,'CLOSING')]:
 local=read(staging/'LOCAL_RENDERS.json');qa=read(staging/'QA_RENDERS.json')
 for x in local['records']:
  p=staging/x['file'];assert x['actuallyViewed']and sha(p)==x['sha256'];dest=b/'images'/p.name;copy(p,dest);x['inheritedStagingFile']=x['file'];x['file']=dest.relative_to(w).as_posix();x['firstReadInCurrentTurn']=staging==s2
  all_images.append(x)
 for x in qa['records']:
  p=staging/x['file'];assert x['actuallyViewed']and sha(p)==x['sha256'];dest=q/p.name;copy(p,dest);x['inheritedStagingFile']=x['file'];x['file']=dest.relative_to(w).as_posix();all_qa.append(x)
 write(b/(prefix+'_RENDERS.json'),local);write(b/(prefix+'_QA_RENDERS.json'),qa)
 manual=read(staging/'MANUAL_READINGS.json');manual['records']=local['records'];write(b/(prefix+'_MANUAL_READINGS.json'),manual)
 copy(staging/'RESULTS.json',q/(prefix+'_RESULTS.json'))
copy(s1/'TRAVELER_CONTEXT.json',b/'TRAVELER_CONTEXT.json')
copy(s1/'B02_CURRENT_UNITS.json',b/'PRIOR_STAGED_UNITS.json')
copy(s1/'SOURCE_VERIFICATION.json',q/'PRIOR_STAGED_SOURCE_VERIFICATION.json')
for name in['DETAIL_CROP.json','CHART_CROP.json']:
 crop=read(s1/name);copy(s1/crop['file'],q/crop['file']);write(b/name,{**crop,'source':next(x['file']for x in all_qa if x['sourcePage']==334),'file':(q/crop['file']).relative_to(w).as_posix(),'inheritedSourceName':crop['source']})
for name in['B02_CURRENT_UNITS.json','HOUSE_CONTEXTS.json','PRINTED_FIXTURE.json','COLOPHON_AUDIT.json','BOUNDED_CLAUSES.json']:copy(s2/name,b/name)

relocations=[]
for staging,name in[(s1,'traveler-context.mjs'),(s2,'house-context.mjs')]:
 original=b/('STAGED_'+name);copy(staging/name,original)
 old="from'../../v53/research/liuyao-foundations/liuyao-reference.mjs'";new="from'../liuyao-foundations/liuyao-reference.mjs'"
 text=original.read_text(encoding='utf-8');assert text.count(old)==1
 target=b/name;target.write_text(text.replace(old,new),encoding='utf-8')
 relocations.append({'stagedFile':original.relative_to(w).as_posix(),'promotedFile':target.relative_to(w).as_posix(),'stagedSHA256':sha(original),'promotedSHA256':sha(target),'oldImport':old,'newImport':new,'bodyOtherwiseByteIdentical':True})
write(b/'PROMOTION_IDENTITIES.json',{'date':'2026-10-28','basis':'Local byte identities,notpublisher signatures;packaged provenance copies allow import-only comparison withouttmp.','records':identities,'referenceImportRelocations':relocations})
for staging,oldname,newname,ref,result,manifest,qa_name in[
 (s1,'test-traveler-context.mjs','test-liuyao-traveler-context.mjs','traveler-context','TRAVELER_RESULTS.json','TRAVELER_RENDERS.json','TRAVELER_QA_RENDERS.json'),
 (s2,'test-house-context.mjs','test-liuyao-house-context.mjs','house-context','CLOSING_RESULTS.json','CLOSING_RENDERS.json','CLOSING_QA_RENDERS.json')]:
 text=(staging/oldname).read_text(encoding='utf-8').replace("from'./"+ref+".mjs'","from'../research/liuyao-closing-context/"+ref+".mjs'")
 text=text.replace("const b=import.meta.dirname,w=process.cwd(),r=resolve(w,'v53'),read=","const w=process.cwd(),r=resolve(w,'v53'),b=resolve(r,'research/liuyao-closing-context'),q=resolve(r,'qa/liuyao-closing-context'),read=")
 text=text.replace("resolve(b,'LOCAL_RENDERS.json')","resolve(b,'"+manifest+"')").replace("resolve(b,'QA_RENDERS.json')","resolve(b,'"+qa_name+"')")
 text=text.replace("resolve(b,x.file)","resolve(w,x.file)").replace("resolve(b,x.source)","resolve(w,x.source)").replace("resolve(b,'RESULTS.json')","resolve(q,'"+result+"')")
 text=text.replace("resolve(r,'PACKAGE_MANIFEST.json')","resolve(w,'archives/v53-before-liuyao-closing-context/PACKAGE_MANIFEST.json')")
 if staging==s1:
  text=text.replace("resolve(b,'B02_CURRENT_UNITS.json')","resolve(b,'PRIOR_STAGED_UNITS.json')").replace("resolve(b,'MANUAL_READINGS.json')","resolve(b,'TRAVELER_MANUAL_READINGS.json')")
 else:text=text.replace("resolve(b,'MANUAL_READINGS.json')","resolve(b,'CLOSING_MANUAL_READINGS.json')")
 (r/'scripts'/newname).write_text(text,encoding='utf-8')

pdf=w/local['sourcePDF'];assert sha(pdf)==local['sourceSHA256']
write(b/'SOURCE_MANIFEST.json',{'date':'2026-10-28','sourcePDF':local['sourcePDF'],'sourceBytes':pdf.stat().st_size,'sourceSHA256':sha(pdf),
 'inheritedContainerProvenance':'v53/research/liuyao-foundations/SOURCE_AUDIT.json and REQUESTS.json;no newHTTP orPDF',
 'images':all_images,'extraQA':all_qa,'priorStagedPositionsPromoted':26,'priorStagedBodyPositions':25,'priorStagedNonRuleLeaves':[338],
 'newViewedPositionsThisTurn':44,'newBodyPositionsThisTurn':40,'currentTurnNonRuleLeaves':[391,392,393,394],'expandedPriorTOCPositions':[18,19],
 'uniqueImagePositionsPromoted':70,'uniqueBodyPositionsPromoted':65,'allNonRuleLeavesPromoted':[338,391,392,393,394],
 'newFirstPassSpansThisTurn':28,'inheritedPriorStagingSpans':20,'firstPassSpansNewlyPackaged':48,
 'newHTTPRequests':0,'newOriginalContainers':0,'newIndependentWitnesses':0,'sourceEmended':False,'allImageCharactersCollated':False,'wholeChaptersApplied':False,'sourceInstructionsAreData':True})
print(json.dumps({'imagesPromoted':len(all_images),'QAImagesPromoted':len(all_qa),'nativeCrops':2,'identityRecords':len(identities),'referenceImportRelocations':2,'currentFirstPassSpans':130,'wholeUnitsApplied':0}))
