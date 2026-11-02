from pathlib import Path
from hashlib import sha256
import json,shutil
w=Path.cwd();r=w/'v53';s=w/'tmp/bazi-month-command-staging';b=r/'research/bazi-month-command';q=r/'qa/bazi-month-command'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda p,o:p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not b.exists()and not q.exists()
assert read(w/'archives/v53-before-bazi-month-command/SNAPSHOT.json')['sourceManifestFiles']==4557
res=read(s/'REFERENCE_RESULTS.json');assert len(res['checks'])==5 and all(x['ok']for x in res['checks'])
cropNames={x['file']for x in read(s/'QA_IMAGES.json')['records']}
b.mkdir();q.mkdir();identities=[]
for p in sorted(s.iterdir()):
 if not p.is_file():continue
 if p.name=='REPORT.md':out=r/'BAZI_MONTH_COMMAND_REPORT.md'
 elif p.name in cropNames or p.name in ['QA_IMAGES.json','REFERENCE_RESULTS.json']:out=q/p.name
 elif p.suffix in ['.py','.mjs']and p.name!='month-command-reference.mjs':out=b/('STAGED_'+p.name)
 else:out=b/p.name
 shutil.copyfile(p,out);assert p.read_bytes()==out.read_bytes()
 identities.append(dict(file=out.relative_to(w).as_posix(),stagingFile=p.relative_to(w).as_posix(),bytes=out.stat().st_size,sha256=sha256(out.read_bytes()).hexdigest()))
text=(s/'test-month-command.mjs').read_text(encoding='utf-8')
for old,new in [("from './month-command-reference.mjs'","from '../research/bazi-month-command/month-command-reference.mjs'"),("const b=import.meta.dirname,w=resolve(b,'../..'),L=","const b=resolve(import.meta.dirname,'../research/bazi-month-command'),w=resolve(b,'../../..'),L="),("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/bazi-month-command/REFERENCE_RESULTS.json')")]:assert text.count(old)==1;text=text.replace(old,new)
(r/'scripts/test-bazi-month-command.mjs').write_text(text,encoding='utf-8')
write(b/'PROMOTION_IDENTITIES.json',dict(date='2026-10-28',records=identities,moduleByteIdenticalToStaging=True,testOnlyThreePathRelocations=True,passedRuntimeTestsNotRerunOnPromotion=True,tableOnlyPageMetadataCorrectionAfterTest=True))
state=read(b/'WORK_STATE.json');summary=state['completedStep'];nexts=state['next']
p=w/'EXHAUSTIVE_WORK_STATE.json';ex=read(p);ex['previousBaziSeasonalLabelWork']=ex['currentWork'];ex['currentWork']=dict(catalogueID='M01',work='Tam Mệnh Thông Hội — Nhân nguyên tư sự: hai danh sách và dị số',sourceDirectory=state['sourceDirectory'],currentStep=summary,latestResearchReport=state['latestReport'],internalHourReference='v53/research/home-hour-alignment/source-hour-reference.mjs',sourceLimits='24source-monthrows69allocations;32/26/380vs360retained;0actualcalendarcommandmethod;17of232volume2positionsviewed')
ex['inProgressScope']=state['sourceDirectory']+'/WORK_STATE.json';ex['subsequentPriority']=[' '.join(nexts)]+ex['subsequentPriority'];write(p,ex);(r/'research/EXHAUSTIVE_WORK_STATE.json').write_bytes(p.read_bytes())
p=r/'research/full-study/WORK_STATE.json';full=read(p);full['latestResearchReport']=state['latestReport'];full['exhaustiveNext']=' '.join(nexts)
x=next(x for x in full['items']if x['id']=='bazi');x['completed'].append(summary);x['latestResearchReport']=state['latestReport'];x['latestScope']='../bazi-month-command/WORK_STATE.json';x['nextFile']='../bazi-month-command/SOURCE_DISPOSITIONS.json';write(p,full)
p=r/'research/library-current/COVERAGE.json';coverage=read(p);coverage['counts']['newDownloadsThisScope']=0;coverage['counts']['newDownloadsThisScopeBasis']='Retainedvolume2native9newpositions/2lists24rows69entries;0HTTP/newcontainers/witnesses.'
x=next(x for x in coverage['catalogue']if x['id']=='M01');x['latestMonthCommandScope']=summary;x['selectedSeasonalSourceCounts']['positionsViewedAcrossCurrentVolume2Scopes']=17
x['selectedMonthCommandCounts']=dict(sourceVariants=2,monthRows=24,allocationEntries=69,actualLunarHiddenStemTableQueries=24,setMatches=6,setDifferences=16,unresolvedSets=2,actualDateCommandMethodValidated=False)
x['currentEvidence'] += [state['latestReport'],state['sourceDirectory']+'/WORK_STATE.json',state['sourceDirectory']+'/SOURCE_DISPOSITIONS.json',state['sourceDirectory']+'/MANUAL_COMMAND_TABLES.json',state['sourceDirectory']+'/ARITHMETIC_AUDIT.json',state['sourceDirectory']+'/month-command-reference.mjs','v53/qa/bazi-month-command/REFERENCE_RESULTS.json'];write(p,coverage)
for p,title in [(r/'NEXT_STEPS.md','Mốc Nhân nguyên tư sự'),(r/'research/library-current/COVERAGE.md','Mốc hai bảng phân ngày tháng'),(w/'PROJECT_RESEARCH_STATE.md','Mốc bảng tư sự và số ngày chưa thống nhất')]:
 old=p.read_text(encoding='utf-8-sig');p.write_text(f'{title},28/10/2026: `BAZI_MONTH_COMMAND_REPORT.md`. {summary}\n\nTiếp: '+' '.join(nexts)+'\n\n'+old,encoding='utf-8')
p=w/'PENDING_RESEARCH_STATE.json';pending=read(p);pending.update(status=state['status'],workDirectory=state['sourceDirectory'],currentWorkState=state['sourceDirectory']+'/WORK_STATE.json',latestReport=state['latestReport'],next=nexts,packageVerification='month-command-promotion-awaiting-final-no-write',inProgressStaging=dict(file='tmp/bazi-month-command-staging/WORK_STATE.json',status='promoted;packageverificationpending',catalogueID='M01'));write(p,pending)
print(json.dumps(dict(promotionIdentities=len(identities),runtimeChecks=5,actualLunarTableQueries=24,sourcePositionsViewed=9,sourceRows=24,allocationEntries=69,consumerChanged=False)))
