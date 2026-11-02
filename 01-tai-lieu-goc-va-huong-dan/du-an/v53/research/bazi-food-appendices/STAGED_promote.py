from pathlib import Path
from hashlib import sha256
import json,shutil
w=Path.cwd();r=w/'v53';s=w/'tmp/bazi-food-appendices-staging';b=r/'research/bazi-food-appendices';q=r/'qa/bazi-food-appendices'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not b.exists() and not q.exists()
assert read(w/'archives/v53-before-bazi-food-appendices/SNAPSHOT.json')['sourceManifestFiles']==4623
assert len(read(s/'REFERENCE_RESULTS.json')['checks'])==9
b.mkdir();q.mkdir();records=[]
qa_names={x['file']for x in read(s/'QA_IMAGES.json')['records']}|{'QA_IMAGES.json','REFERENCE_RESULTS.json'}
for p in sorted(s.iterdir()):
 if not p.is_file():continue
 if p.name=='REPORT.md':out=r/'BAZI_FOOD_APPENDICES_REPORT.md'
 elif p.name in qa_names:out=q/p.name
 elif p.suffix in ['.py','.mjs'] and p.name!='appendix-reference.mjs':out=b/('STAGED_'+p.name)
 else:out=b/p.name
 shutil.copyfile(p,out);assert p.read_bytes()==out.read_bytes()
 records.append(dict(file=out.relative_to(w).as_posix(),stagingFile=p.relative_to(w).as_posix(),bytes=out.stat().st_size,sha256=sha256(out.read_bytes()).hexdigest()))
text=(s/'test-appendices.mjs').read_text(encoding='utf-8')
for old,new in [
 ("from './appendix-reference.mjs'","from '../research/bazi-food-appendices/appendix-reference.mjs'"),
 ("const b=import.meta.dirname,w=resolve(b,'../..'),ctx={};","const b=resolve(import.meta.dirname,'../research/bazi-food-appendices'),w=resolve(b,'../../..'),ctx={};"),
 ("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/bazi-food-appendices/REFERENCE_RESULTS.json')")]:
 assert text.count(old)==1;text=text.replace(old,new)
(r/'scripts/test-bazi-food-appendices.mjs').write_text(text,encoding='utf-8')
write(b/'PROMOTION_IDENTITIES.json',dict(date='2026-10-28',records=records,moduleByteIdenticalToStaging=True,testOnlyThreePathRelocations=True,runtimeTestsNotRerunOnPromotion=True))
state=read(b/'WORK_STATE.json');summary=state['completedStep'];nexts=state['next']
ex=read(w/'EXHAUSTIVE_WORK_STATE.json');ex['previousBaziFoodOwlExceptionsWork']=ex['currentWork']
ex['currentWork']=dict(catalogueID='M01',work='Tam Mệnh Thông Hội — sáu mục kèm Thực Thần và ma trận90 ngữ cảnh',
 sourceDirectory=state['sourceDirectory'],currentStep=summary,latestResearchReport=state['latestReport'],
 internalHourReference='v53/research/home-hour-alignment/source-hour-reference.mjs',
 sourceLimits='32partial-or-declared-premise-links/58unlinked/0whole-contexts-applied;sourceanchors/joins/effectivenessremainopen')
ex['inProgressScope']=state['sourceDirectory']+'/WORK_STATE.json'
ex['subsequentPriority']=[' '.join(nexts)]+ex['subsequentPriority']
write(w/'EXHAUSTIVE_WORK_STATE.json',ex);(r/'research/EXHAUSTIVE_WORK_STATE.json').write_bytes((w/'EXHAUSTIVE_WORK_STATE.json').read_bytes())
p=r/'research/full-study/WORK_STATE.json';full=read(p);full['latestResearchReport']=state['latestReport'];full['exhaustiveNext']=' '.join(nexts)
x=next(x for x in full['items']if x['id']=='bazi');x['completed'].append(summary);x['latestResearchReport']=state['latestReport'];x['latestScope']='../bazi-food-appendices/WORK_STATE.json';x['nextFile']='../bazi-food-appendices/CURRENT_CONTEXT_COVERAGE.json';write(p,full)
p=r/'research/library-current/COVERAGE.json';coverage=read(p);coverage['counts']['newDownloadsThisScope']=0
coverage['counts']['newDownloadsThisScopeBasis']='Sixappendices/17contexts/23coordinate-records;5expandedoldpositions/6nativecrops;0HTTP/newcontainers/positions/witnesses.'
x=next(x for x in coverage['catalogue']if x['id']=='M01');x['latestFoodAppendicesScope']=summary
x['previousFoodParentContextSelection']=x['foodParentContextSelection']
x['foodParentContextSelection']=dict(total=90,parentsWithSelectedModuleOrDeclaredPremiseLinks=32,otherParentsWithoutSuchLinks=58,
 wholeParentsApplied=0,allSelectedParentsSubsidiaryClausesApplied=False,
 countingBasis='10core/seats/owl+13previousspecial-foodprovenancelinks+9newappendixparents;32linksarenot32fullyappliedrules',
 currentMatrix=state['sourceDirectory']+'/CURRENT_CONTEXT_COVERAGE.json')
x['currentEvidence'] += [state['latestReport'],state['sourceDirectory']+'/WORK_STATE.json',state['sourceDirectory']+'/EXPLICIT_COORDINATES.json',
 state['sourceDirectory']+'/CLAUSE_DISPOSITIONS.json',state['sourceDirectory']+'/CURRENT_CONTEXT_COVERAGE.json',
 state['sourceDirectory']+'/SOURCE_DISPOSITIONS.json',state['sourceDirectory']+'/appendix-reference.mjs','v53/qa/bazi-food-appendices/REFERENCE_RESULTS.json'];write(p,coverage)
for p in [r/'NEXT_STEPS.md',r/'research/library-current/COVERAGE.md',w/'PROJECT_RESEARCH_STATE.md']:
 old=p.read_text(encoding='utf-8-sig')
 p.write_text('Mốc sáu mục kèm Thực Thần, 28/10/2026: `BAZI_FOOD_APPENDICES_REPORT.md`. '+summary+'\n\nTiếp: '+' '.join(nexts)+'\n\nCác mốc bên dưới là lịch sử; tổng liên kết ngữ cảnh hiện tại dùng ma trận32/58 nêu trên.\n\n'+old,encoding='utf-8')
p=w/'PENDING_RESEARCH_STATE.json';pending=read(p);pending.update(status=state['status'],workDirectory=state['sourceDirectory'],
 currentWorkState=state['sourceDirectory']+'/WORK_STATE.json',latestReport=state['latestReport'],next=nexts,
 packageVerification='appendices-promotion-awaiting-final-no-write',
 inProgressStaging=dict(file='tmp/bazi-food-appendices-staging/WORK_STATE.json',status='promoted;packageverificationpending',catalogueID='M01'))
write(p,pending)
print(json.dumps(dict(promotionIdentities=len(records),runtimeChecks=9,actualHHCTenGodQueries=86,partialLinkedParents=32,consumerChanged=False)))
