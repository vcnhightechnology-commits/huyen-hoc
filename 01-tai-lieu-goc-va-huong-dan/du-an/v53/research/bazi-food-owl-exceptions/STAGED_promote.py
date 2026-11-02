from pathlib import Path
from hashlib import sha256
import json,shutil
w=Path.cwd();r=w/'v53';s=w/'tmp/bazi-food-owl-exceptions-staging';b=r/'research/bazi-food-owl-exceptions';q=r/'qa/bazi-food-owl-exceptions'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda p,o:p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not b.exists()and not q.exists()
assert read(w/'archives/v53-before-bazi-food-owl-exceptions/SNAPSHOT.json')['sourceManifestFiles']==4596
res=read(s/'REFERENCE_RESULTS.json');assert len(res['checks'])==5 and all(x['ok']for x in res['checks'])
cropNames={x['file']for x in read(s/'QA_IMAGES.json')['records']}
b.mkdir();q.mkdir();identities=[]
for p in sorted(s.iterdir()):
 if not p.is_file():continue
 if p.name=='REPORT.md':out=r/'BAZI_FOOD_OWL_EXCEPTIONS_REPORT.md'
 elif p.name in cropNames or p.name in ['QA_IMAGES.json','REFERENCE_RESULTS.json','TEST_FAILURE_AUDIT.json']:out=q/p.name
 elif p.suffix in ['.py','.mjs']and p.name!='owl-exception-reference.mjs':out=b/('STAGED_'+p.name)
 else:out=b/p.name
 shutil.copyfile(p,out);assert p.read_bytes()==out.read_bytes()
 identities.append(dict(file=out.relative_to(w).as_posix(),stagingFile=p.relative_to(w).as_posix(),bytes=out.stat().st_size,sha256=sha256(out.read_bytes()).hexdigest()))
text=(s/'test-owl-exceptions.mjs').read_text(encoding='utf-8')
for old,new in [("from'./owl-exception-reference.mjs'","from'../research/bazi-food-owl-exceptions/owl-exception-reference.mjs'"),("const b=import.meta.dirname,w=resolve(b,'../..'),ctx={};","const b=resolve(import.meta.dirname,'../research/bazi-food-owl-exceptions'),w=resolve(b,'../../..'),ctx={};"),("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/bazi-food-owl-exceptions/REFERENCE_RESULTS.json')")]:assert text.count(old)==1;text=text.replace(old,new)
(r/'scripts/test-bazi-food-owl-exceptions.mjs').write_text(text,encoding='utf-8')
write(b/'PROMOTION_IDENTITIES.json',dict(date='2026-10-28',records=identities,moduleByteIdenticalToStaging=True,testOnlyThreePathRelocations=True,passedRuntimeTestsNotRerunOnPromotion=True))
state=read(b/'WORK_STATE.json');summary=state['completedStep'];nexts=state['next']
p=w/'EXHAUSTIVE_WORK_STATE.json';ex=read(p);ex['previousBaziMonthCommandWork']=ex['currentWork'];ex['currentWork']=dict(catalogueID='M01',work='Tam Mệnh Thông Hội — C15 ngoại lệ Thực Thần–Thiên Ấn',sourceDirectory=state['sourceDirectory'],currentStep=summary,latestResearchReport=state['latestReport'],internalHourReference='v53/research/home-hour-alignment/source-hour-reference.mjs',sourceLimits='213codepoints10units/8selectedpremiseaudits;sourceanchor/effectivecombination/priorityunresolved;10foodparentsselectedpartly80remaining')
ex['inProgressScope']=state['sourceDirectory']+'/WORK_STATE.json'
old=[x for x in ex['subsequentPriority']if '81'in x and ('Thực'in x or 'ThựcThần'in x)]
ex['historicalSupersededFoodNineParentPriorities']=old;ex['subsequentPriority']=[' '.join(nexts)]+[x for x in ex['subsequentPriority']if x not in old]
write(p,ex);(r/'research/EXHAUSTIVE_WORK_STATE.json').write_bytes(p.read_bytes())
p=r/'research/full-study/WORK_STATE.json';full=read(p);full['latestResearchReport']=state['latestReport'];full['exhaustiveNext']=' '.join(nexts)
x=next(x for x in full['items']if x['id']=='bazi');x['completed'].append(summary);x['latestResearchReport']=state['latestReport'];x['latestScope']='../bazi-food-owl-exceptions/WORK_STATE.json';x['nextFile']='../bazi-food-owl-exceptions/SOURCE_DISPOSITIONS.json';write(p,full)
p=r/'research/library-current/COVERAGE.json';coverage=read(p);coverage['counts']['newDownloadsThisScope']=0;coverage['counts']['newDownloadsThisScopeBasis']='C15retained213codepoints/2expandednativeimages/4crops;0HTTP/newcontainers/positions/witnesses.'
x=next(x for x in coverage['catalogue']if x['id']=='M01');x['latestFoodOwlExceptionsScope']=summary;x['foodParentContextSelection']=dict(total=90,parentsWithSelectedClauses=10,otherParentsNotSelected=80,allSelectedParentsSubsidiaryClausesApplied=False)
x['currentEvidence'] += [state['latestReport'],state['sourceDirectory']+'/WORK_STATE.json',state['sourceDirectory']+'/CLAUSE_PARTITION.json',state['sourceDirectory']+'/SELECTED_READING_AUDIT.json',state['sourceDirectory']+'/SOURCE_DISPOSITIONS.json',state['sourceDirectory']+'/owl-exception-reference.mjs','v53/qa/bazi-food-owl-exceptions/REFERENCE_RESULTS.json','v53/qa/bazi-food-owl-exceptions/TEST_FAILURE_AUDIT.json'];write(p,coverage)
for p,title in [(r/'NEXT_STEPS.md','Mốc ngoại lệ C15'),(r/'research/library-current/COVERAGE.md','Mốc tám câu Thiên Ấn'),(w/'PROJECT_RESEARCH_STATE.md','Mốc vai câu và tiền đề ngoại lệ Thực Thần')]:
 old=p.read_text(encoding='utf-8-sig');p.write_text(f'{title},28/10/2026: `BAZI_FOOD_OWL_EXCEPTIONS_REPORT.md`. {summary}\n\nTiếp: '+' '.join(nexts)+'\n\n'+old,encoding='utf-8')
p=w/'PENDING_RESEARCH_STATE.json';pending=read(p);pending.update(status=state['status'],workDirectory=state['sourceDirectory'],currentWorkState=state['sourceDirectory']+'/WORK_STATE.json',latestReport=state['latestReport'],next=nexts,packageVerification='owl-exceptions-promotion-awaiting-final-no-write',inProgressStaging=dict(file='tmp/bazi-food-owl-exceptions-staging/WORK_STATE.json',status='promoted;packageverificationpending',catalogueID='M01'));write(p,pending)
print(json.dumps(dict(promotionIdentities=len(identities),runtimeChecks=5,actualHHCTenGodQueries=8,actualLunarTableQueries=8,ternaryContexts=162,consumerChanged=False)))
