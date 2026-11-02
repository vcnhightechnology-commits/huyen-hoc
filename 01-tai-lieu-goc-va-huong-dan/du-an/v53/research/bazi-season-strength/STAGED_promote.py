from pathlib import Path
from hashlib import sha256
import json,shutil
w=Path.cwd();r=w/'v53';s=w/'tmp/bazi-season-strength-staging';b=r/'research/bazi-season-strength';q=r/'qa/bazi-season-strength'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda p,o:p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not b.exists()and not q.exists()
assert read(w/'archives/v53-before-bazi-season-strength/SNAPSHOT.json')['sourceManifestFiles']==4514
res=read(s/'REFERENCE_RESULTS.json');assert len(res['checks'])==5 and all(x['ok']for x in res['checks'])
cropNames={x['file']for x in read(s/'QA_IMAGES.json')['records']}
b.mkdir();q.mkdir();identities=[]
for p in sorted(s.iterdir()):
 if not p.is_file():continue
 if p.name=='REPORT.md':out=r/'BAZI_SEASON_LABELS_REPORT.md'
 elif p.name in cropNames or p.name in ['QA_IMAGES.json','REFERENCE_RESULTS.json']:out=q/p.name
 elif p.suffix in ['.py','.mjs']and p.name!='season-label-reference.mjs':out=b/('STAGED_'+p.name)
 else:out=b/p.name
 shutil.copyfile(p,out);assert p.read_bytes()==out.read_bytes()
 identities.append(dict(file=out.relative_to(w).as_posix(),stagingFile=p.relative_to(w).as_posix(),bytes=out.stat().st_size,sha256=sha256(out.read_bytes()).hexdigest()))
text=(s/'test-season-labels.mjs').read_text(encoding='utf-8')
for old,new in [("from './season-label-reference.mjs'","from '../research/bazi-season-strength/season-label-reference.mjs'"),("new URL('./MANUAL_SEASON_TABLE.json',import.meta.url)","new URL('../research/bazi-season-strength/MANUAL_SEASON_TABLE.json',import.meta.url)"),("new URL('./REFERENCE_RESULTS.json',import.meta.url)","new URL('../qa/bazi-season-strength/REFERENCE_RESULTS.json',import.meta.url)")]:assert text.count(old)==1;text=text.replace(old,new)
(r/'scripts/test-bazi-season-labels.mjs').write_text(text,encoding='utf-8')
write(b/'PROMOTION_IDENTITIES.json',dict(date='2026-10-28',records=identities,moduleByteIdenticalToStaging=True,testOnlyThreePathRelocations=True,passedRuntimeTestsNotRerunOnPromotion=True))
state=read(b/'WORK_STATE.json');summary=state['completedStep'];nexts=state['next']
p=w/'EXHAUSTIVE_WORK_STATE.json';ex=read(p);ex['previousBaziFoodSeatWork']=ex['currentWork'];ex['currentWork']=dict(catalogueID='M01',work='Tam Mệnh Thông Hội quyển hai — nhãn mùa vụ và giới hạn vượng suy',sourceDirectory=state['sourceDirectory'],currentStep=summary,latestResearchReport=state['latestReport'],internalHourReference='v53/research/home-hour-alignment/source-hour-reference.mjs',sourceLimits='8of232facsimilepositions;25seasonalslots/24recognized/1literal因unknown;nofullstrengthorcalendarphaseadapter')
ex['inProgressScope']=state['sourceDirectory']+'/WORK_STATE.json';ex['subsequentPriority']=[' '.join(nexts)]+ex['subsequentPriority'];write(p,ex);(r/'research/EXHAUSTIVE_WORK_STATE.json').write_bytes(p.read_bytes())
p=r/'research/full-study/WORK_STATE.json';full=read(p);full['latestResearchReport']=state['latestReport'];full['exhaustiveNext']=' '.join(nexts)
x=next(x for x in full['items']if x['id']=='bazi');x['completed'].append(summary);x['latestResearchReport']=state['latestReport'];x['latestScope']='../bazi-season-strength/WORK_STATE.json';x['nextFile']='../bazi-season-strength/READING_AUDIT.json';write(p,full)
p=r/'research/library-current/COVERAGE.json';coverage=read(p);coverage['counts']['newDownloadsThisScope']=3;coverage['counts']['newDownloadsThisScopeBasis']='3HTTP200TLSbodies incl1repositoryvolume2DjVu10858550bytes;8of232positions/25selectedslots,notwholework.'
x=next(x for x in coverage['catalogue']if x['id']=='M01');x['latestSeasonalLabelScope']=summary;x['selectedSeasonalSourceCounts']=dict(containerPositions=232,positionsViewed=8,seasonalSlots=25,recognizedStateSlots=24,unclassifiedLiteralSlots=1,wholeVolumeRead=False,wholeWorkApplied=False)
x['currentEvidence'] += [state['latestReport'],state['sourceDirectory']+'/WORK_STATE.json',state['sourceDirectory']+'/ACQUISITION.json',state['sourceDirectory']+'/REQUESTS.json',state['sourceDirectory']+'/LOCAL_RENDERS.json',state['sourceDirectory']+'/MANUAL_SEASON_TABLE.json',state['sourceDirectory']+'/READING_AUDIT.json',state['sourceDirectory']+'/season-label-reference.mjs','v53/qa/bazi-season-strength/REFERENCE_RESULTS.json'];write(p,coverage)
for p,title in [(r/'NEXT_STEPS.md','Mốc nhãn mùa vụ quyển hai'),(r/'research/library-current/COVERAGE.md','Mốc25ô/24nhãn/1chữgiữmở'),(w/'PROJECT_RESEARCH_STATE.md','Mốc đối ảnh vượng–tướng–hưu–tù–tử')]:
 old=p.read_text(encoding='utf-8-sig');p.write_text(f'{title},28/10/2026: `BAZI_SEASON_LABELS_REPORT.md`. {summary}\n\nTiếp: '+' '.join(nexts)+'\n\n'+old,encoding='utf-8')
p=w/'PENDING_RESEARCH_STATE.json';pending=read(p);pending.update(status=state['status'],workDirectory=state['sourceDirectory'],currentWorkState=state['sourceDirectory']+'/WORK_STATE.json',latestReport=state['latestReport'],next=nexts,packageVerification='season-labels-promotion-awaiting-final-no-write',inProgressStaging=dict(file='tmp/bazi-season-strength-staging/WORK_STATE.json',status='promoted;packageverificationpending',catalogueID='M01'));write(p,pending)
print(json.dumps(dict(promotionIdentities=len(identities),runtimeChecks=5,HTTP200TLSBodies=3,sourcePositionsViewed=8,seasonSlots=25,recognized=24,unclassified=1,consumerChanged=False)))
