from pathlib import Path
from hashlib import sha256
import json,shutil
w=Path.cwd();r=w/'v53';s=w/'tmp/bazi-food-seats-staging';b=r/'research/bazi-food-seats';q=r/'qa/bazi-food-seats'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda p,o:p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not b.exists()and not q.exists()
assert read(w/'archives/v53-before-bazi-food-seats/SNAPSHOT.json')['sourceManifestFiles']==4495
result=read(s/'REFERENCE_RESULTS.json');assert len(result['checks'])==5 and all(x['ok']for x in result['checks'])
b.mkdir();q.mkdir();identities=[]
for p in sorted(s.iterdir()):
 if not p.is_file():continue
 if p.name=='REPORT.md':out=r/'BAZI_FOOD_SEATS_REPORT.md'
 elif p.suffix=='.png'or p.name in ['QA_IMAGES.json','REFERENCE_RESULTS.json']:out=q/p.name
 elif p.suffix in ['.py','.mjs']and p.name!='food-seat-reference.mjs':out=b/('STAGED_'+p.name)
 else:out=b/p.name
 shutil.copyfile(p,out);assert p.read_bytes()==out.read_bytes()
 identities.append(dict(file=out.relative_to(w).as_posix(),stagingFile=p.relative_to(w).as_posix(),bytes=out.stat().st_size,sha256=sha256(out.read_bytes()).hexdigest()))
text=(s/'test-food-seats.mjs').read_text(encoding='utf-8')
for old,new in [("from './food-seat-reference.mjs'","from '../research/bazi-food-seats/food-seat-reference.mjs'"),("const b=import.meta.dirname,w=resolve(b,'../..'),c={};","const b=resolve(import.meta.dirname,'../research/bazi-food-seats'),w=resolve(b,'../../..'),c={};"),("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/bazi-food-seats/REFERENCE_RESULTS.json')")]:assert text.count(old)==1;text=text.replace(old,new)
(r/'scripts/test-bazi-food-seats.mjs').write_text(text,encoding='utf-8')
write(b/'PROMOTION_IDENTITIES.json',dict(date='2026-10-28',records=identities,moduleByteIdenticalToStaging=True,testOnlyThreePathRelocations=True,passedRuntimeTestsNotRerunOnPromotion=True,dataMetadataOnlyEditorialClarificationAfterTest=True,computationalFiveRowsUnchanged=True))
state=read(b/'WORK_STATE.json');summary=state['completedStep'];nexts=state['next']
p=w/'EXHAUSTIVE_WORK_STATE.json';ex=read(p);ex['previousHomeXuanKongContextWork']=ex['currentWork']
ex['currentWork']=dict(catalogueID='M01',work='Tam Mệnh Thông Hội — Thực Thần C20: các tọa độ sinh vượng',sourceDirectory=state['sourceDirectory'],currentStep=summary,latestResearchReport=state['latestReport'],internalHourReference='v53/research/home-hour-alignment/source-hour-reference.mjs',sourceLimits='5canonicalfamilyrows/20branchmemberships;9selectedparents/81notselected;fullstrengthandclauseconditionsopen')
ex['inProgressScope']=state['sourceDirectory']+'/WORK_STATE.json'
old=[x for x in ex['subsequentPriority']if '82'in x and 'Thực'in x]
ex['historicalSupersededFoodParentPriorities']=old;ex['subsequentPriority']=[' '.join(nexts)]+[x for x in ex['subsequentPriority']if x not in old]
write(p,ex);(r/'research/EXHAUSTIVE_WORK_STATE.json').write_bytes(p.read_bytes())
p=r/'research/full-study/WORK_STATE.json';full=read(p);full['latestResearchReport']=state['latestReport'];full['exhaustiveNext']=' '.join(nexts)
x=next(x for x in full['items']if x['id']=='bazi');x['completed'].append(summary);x['latestResearchReport']=state['latestReport'];x['latestScope']='../bazi-food-seats/WORK_STATE.json';write(p,full)
p=r/'research/library-current/COVERAGE.json';coverage=read(p);coverage['counts']['newDownloadsThisScope']=0;coverage['counts']['newDownloadsThisScopeBasis']='RetainedCADALrenders177–178expanded/C20fivecanonicalgroups;0HTTP/container/positions/witnesses.'
x=next(x for x in coverage['catalogue']if x['id']=='M01');x['latestFoodSeatScope']=summary;x['foodParentContextSelection']=dict(total=90,parentsWithSelectedClauses=9,otherParentsNotSelected=81,allSelectedParentsSubsidiaryClausesApplied=False)
x['currentEvidence'] += [state['latestReport'],state['sourceDirectory']+'/WORK_STATE.json',state['sourceDirectory']+'/MANUAL_SEAT_CLAUSE.json',state['sourceDirectory']+'/food-seat-reference.mjs',state['sourceDirectory']+'/SOURCE_DISPOSITIONS.json','v53/qa/bazi-food-seats/REFERENCE_RESULTS.json'];write(p,coverage)
for p,title in [(r/'NEXT_STEPS.md','Mốc Thực Thần C20'),(r/'research/library-current/COVERAGE.md','Mốc tọa độ can–chi C20'),(w/'PROJECT_RESEARCH_STATE.md','Mốc Thực Thần kiến sinh vượng')]:
 old=p.read_text(encoding='utf-8-sig');p.write_text(f'{title},28/10/2026: `BAZI_FOOD_SEATS_REPORT.md`. {summary}\n\nTiếp: '+' '.join(nexts)+'\n\n'+old,encoding='utf-8')
p=w/'PENDING_RESEARCH_STATE.json';pending=read(p);pending.update(status=state['status'],workDirectory=state['sourceDirectory'],currentWorkState=state['sourceDirectory']+'/WORK_STATE.json',latestReport=state['latestReport'],next=nexts,packageVerification='food-seat-promotion-awaiting-final-no-write',inProgressStaging=dict(file='tmp/bazi-food-seats-staging/WORK_STATE.json',status='promoted;packageverificationpending',catalogueID='M01'));write(p,pending)
print(json.dumps(dict(promotionIdentities=len(identities),runtimeChecks=5,actualHHCTenGodQueries=100,actualHHCBaziCharts=2,coordinateContexts=600,sourceMemberships=20,consumerChanged=False)))
