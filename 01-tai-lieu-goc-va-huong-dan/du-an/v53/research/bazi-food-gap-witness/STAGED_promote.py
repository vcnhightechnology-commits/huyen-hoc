from pathlib import Path
from hashlib import sha256
import json,shutil
w=Path.cwd();r=w/'v53';s=w/'tmp/bazi-food-gap-witness-staging';b=r/'research/bazi-food-gap-witness';q=r/'qa/bazi-food-gap-witness'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not b.exists()and not q.exists()
assert read(w/'archives/v53-before-bazi-food-gap-witness/SNAPSHOT.json')['sourceManifestFiles']==4650
assert len(read(s/'REFERENCE_RESULTS.json')['checks'])==8
b.mkdir();q.mkdir();records=[]
qa_names={x['file']for x in read(s/'QA_IMAGES.json')['records']}|{'QA_IMAGES.json','REFERENCE_RESULTS.json'}
for p in sorted(s.iterdir()):
 if not p.is_file():continue
 if p.name=='REPORT.md':out=r/'BAZI_FOOD_FLYING_REPORT.md'
 elif p.name in qa_names:out=q/p.name
 elif p.suffix in ['.py','.mjs']and p.name!='flying-reference.mjs':out=b/('STAGED_'+p.name)
 else:out=b/p.name
 shutil.copyfile(p,out);assert p.read_bytes()==out.read_bytes()
 records.append(dict(file=out.relative_to(w).as_posix(),stagingFile=p.relative_to(w).as_posix(),bytes=out.stat().st_size,sha256=sha256(out.read_bytes()).hexdigest()))
text=(s/'test-flying.mjs').read_text(encoding='utf-8')
for old,new in [
 ("from './flying-reference.mjs'","from '../research/bazi-food-gap-witness/flying-reference.mjs'"),
 ("const b=import.meta.dirname,w=resolve(b,'../..'),ctx={};","const b=resolve(import.meta.dirname,'../research/bazi-food-gap-witness'),w=resolve(b,'../../..'),ctx={};"),
 ("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/bazi-food-gap-witness/REFERENCE_RESULTS.json')")]:
 assert text.count(old)==1;text=text.replace(old,new)
(r/'scripts/test-bazi-food-flying.mjs').write_text(text,encoding='utf-8')
write(b/'PROMOTION_IDENTITIES.json',dict(date='2026-10-28',records=records,moduleByteIdenticalToStaging=True,testOnlyThreePathRelocations=True,runtimeTestsNotRerunOnPromotion=True))
state=read(b/'WORK_STATE.json');summary=state['completedStep'];nexts=state['next']
ex=read(w/'EXHAUSTIVE_WORK_STATE.json');ex['previousBaziFoodAppendicesWork']=ex['currentWork']
ex['currentWork']=dict(catalogueID='M01',work='Tam Mệnh Thông Hội — ảnh bù94a–95b và Phi Thiên/Đảo Xung',sourceDirectory=state['sourceDirectory'],
 currentStep=summary,latestResearchReport=state['latestReport'],internalHourReference='v53/research/home-hour-alignment/source-hour-reference.mjs',
 sourceLimits='Fourgapfacesavailableinnew230-positioncopy;9positionsread/notindependentedition;42partiallinks48unlinked0wholeapplied')
ex['inProgressScope']=state['sourceDirectory']+'/WORK_STATE.json'
old=[x for x in ex['subsequentPriority']if '94a'in x or '95b'in x]
ex['historicalSupersededImageGapPriorities']=old
ex['subsequentPriority']=[' '.join(nexts)]+[x for x in ex['subsequentPriority']if x not in old]
write(w/'EXHAUSTIVE_WORK_STATE.json',ex);(r/'research/EXHAUSTIVE_WORK_STATE.json').write_bytes((w/'EXHAUSTIVE_WORK_STATE.json').read_bytes())
p=r/'research/full-study/WORK_STATE.json';full=read(p);full['latestResearchReport']=state['latestReport'];full['exhaustiveNext']=' '.join(nexts)
x=next(x for x in full['items']if x['id']=='bazi');x['completed'].append(summary);x['latestResearchReport']=state['latestReport'];x['latestScope']='../bazi-food-gap-witness/WORK_STATE.json';x['nextFile']='../bazi-food-gap-witness/CURRENT_CONTEXT_COVERAGE.json';write(p,full)
p=r/'research/library-current/COVERAGE.json';coverage=read(p);coverage['counts']['newDownloadsThisScope']=3
coverage['counts']['newDownloadsThisScopeBasis']='ThreeHTTP200TLSbodies:CommonsAPI,pinneddescription,DjVu;one230-positioncontainer/9actuallyviewed/4novelgapfaces/6nativecrops.'
x=next(x for x in coverage['catalogue']if x['id']=='M01');x['latestFoodFlyingScope']=summary;x['previousFoodAppendixParentContextSelection']=x['foodParentContextSelection']
x['foodParentContextSelection']=dict(total=90,parentsWithSelectedModuleOrDeclaredPremiseLinks=42,otherParentsWithoutSuchLinks=48,
 wholeParentsApplied=0,allSelectedParentsSubsidiaryClausesApplied=False,
 countingBasis='32previouspartiallinks+10newsource-coordinate-or-engine-comparisonparents;not42wholeappliedrules',
 currentMatrix=state['sourceDirectory']+'/CURRENT_CONTEXT_COVERAGE.json')
x['currentFoodSourceImageGap']=dict(previouslyOpenFaces=['005-94a','005-94b','005-95a','005-95b'],
 nowAvailableInRetainedCopy='v53/research/bazi-food-gap-witness/CADAL06056481.djvu',newContainerPages=[189,190,191,192],
 earlier226ContainerUnchanged=True,independentEditionEstablished=False,evidence=state['sourceDirectory']+'/FOLIO_MAPPING.json')
x['currentEvidence'] += [state['latestReport'],state['sourceDirectory']+'/WORK_STATE.json',state['sourceDirectory']+'/ACQUISITION.json',
 state['sourceDirectory']+'/REQUESTS.json',state['sourceDirectory']+'/FOLIO_MAPPING.json',state['sourceDirectory']+'/DAY_AND_COORDINATE_TABLES.json',
 state['sourceDirectory']+'/CLAUSE_DISPOSITIONS.json',state['sourceDirectory']+'/CURRENT_CONTEXT_COVERAGE.json',
 state['sourceDirectory']+'/SOURCE_DISPOSITIONS.json',state['sourceDirectory']+'/flying-reference.mjs','v53/qa/bazi-food-gap-witness/REFERENCE_RESULTS.json'];write(p,coverage)
for p in [r/'NEXT_STEPS.md',r/'research/library-current/COVERAGE.md',w/'PROJECT_RESEARCH_STATE.md']:
 old=p.read_text(encoding='utf-8-sig')
 p.write_text('Mốc ảnh bù và Phi Thiên–Đảo Xung,28/10/2026: `BAZI_FOOD_FLYING_REPORT.md`. '+summary+'\n\nTiếp: '+' '.join(nexts)+'\n\nCác mốc bên dưới là lịch sử; khoảng ảnh94a–95b và tổng liên kết dùng bản cập nhật ở trên.\n\n'+old,encoding='utf-8')
p=w/'PENDING_RESEARCH_STATE.json';pending=read(p);pending.update(status=state['status'],workDirectory=state['sourceDirectory'],
 currentWorkState=state['sourceDirectory']+'/WORK_STATE.json',latestReport=state['latestReport'],next=nexts,
 packageVerification='flying-promotion-awaiting-final-no-write',
 inProgressStaging=dict(file='tmp/bazi-food-gap-witness-staging/WORK_STATE.json',status='promoted;packageverificationpending',catalogueID='M01'),
 currentScopeChecks=dict(runtimeChecks=8,actualHHCTenGodQueries=10,actualLunarTableQueries=22,newSourcePositionsViewed=9,novelGapFaces=4,nativeCrops=6,newHTTP200Bodies=3,wholeMethodsApplied=False))
write(p,pending)
print(json.dumps(dict(promotionIdentities=len(records),runtimeChecks=8,actualHHCTenGodQueries=10,sourceHTTPBodies=3,recoveredFaces=4,partialLinkedParents=42,consumerChanged=False)))
