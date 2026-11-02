from pathlib import Path
from hashlib import sha256
import json,shutil
w=Path.cwd();r=w/'v53';s=w/'tmp/home-xuankong-lines-staging';b=r/'research/home-xuankong-lines';q=r/'qa/home-xuankong-lines'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not b.exists()and not q.exists()
assert read(w/'archives/v53-before-home-xuankong-lines/SNAPSHOT.json')['sourceManifestFiles']==4696
assert len(read(s/'REFERENCE_RESULTS.json')['checks'])==7
b.mkdir();q.mkdir();records=[]
qa_names={x['file']for x in read(s/'QA_IMAGES.json')['records']}|{'QA_IMAGES.json','REFERENCE_RESULTS.json'}
for p in sorted(s.iterdir()):
 if not p.is_file():continue
 if p.name=='REPORT.md':out=r/'HOME_XUANKONG_LINES_REPORT.md'
 elif p.name in qa_names:out=q/p.name
 elif p.suffix in ['.py','.mjs']and p.name!='source-room-lines.mjs':out=b/('STAGED_'+p.name)
 else:out=b/p.name
 shutil.copyfile(p,out);assert p.read_bytes()==out.read_bytes()
 records.append(dict(file=out.relative_to(w).as_posix(),stagingFile=p.relative_to(w).as_posix(),bytes=out.stat().st_size,sha256=sha256(out.read_bytes()).hexdigest()))
text=(s/'test-room-lines.mjs').read_text(encoding='utf-8')
for old,new in [
 ("from './source-room-lines.mjs'","from '../research/home-xuankong-lines/source-room-lines.mjs'"),
 ("const b=import.meta.dirname,w=resolve(b,'../..'),ctx={};","const b=resolve(import.meta.dirname,'../research/home-xuankong-lines'),w=resolve(b,'../../..'),ctx={};"),
 ("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/home-xuankong-lines/REFERENCE_RESULTS.json')")]:
 assert text.count(old)==1;text=text.replace(old,new)
(r/'scripts/test-home-xuankong-lines.mjs').write_text(text,encoding='utf-8')
write(b/'PROMOTION_IDENTITIES.json',dict(date='2026-10-28',records=records,moduleByteIdenticalToStaging=True,testOnlyThreePathRelocations=True,runtimeTestsNotRerunOnPromotion=True))
state=read(b/'WORK_STATE.json');summary=state['completedStep'];nexts=state['next']
ex=read(w/'EXHAUSTIVE_WORK_STATE.json');ex['previousBaziFoodFlyingWork']=ex['currentWork']
ex['currentWork']=dict(catalogueID='P08',work='Dương Trạch Thập Thư — năm đơn vị phòng và hào cửa',sourceDirectory=state['sourceDirectory'],
 currentStep=summary,latestResearchReport=state['latestReport'],internalHourReference='v53/research/home-hour-alignment/source-hour-reference.mjs',
 sourceLimits='Twoexpandedoldpositions/fournativecrops/sevenselectedreadings;declaredlast-fiveorderingonly;gatecomplement/initialphase/modernplanremainopen')
ex['inProgressScope']=state['sourceDirectory']+'/WORK_STATE.json';ex['subsequentPriority']=[' '.join(nexts)]+ex['subsequentPriority']
write(w/'EXHAUSTIVE_WORK_STATE.json',ex);(r/'research/EXHAUSTIVE_WORK_STATE.json').write_bytes((w/'EXHAUSTIVE_WORK_STATE.json').read_bytes())
p=r/'research/full-study/WORK_STATE.json';full=read(p);full['latestResearchReport']=state['latestReport'];full['exhaustiveNext']=' '.join(nexts)
x=next(x for x in full['items']if x['id']=='home');x['completed'].append(summary);x['latestResearchReport']=state['latestReport'];x['latestScope']='../home-xuankong-lines/WORK_STATE.json';x['nextFile']='../home-xuankong-lines/MANUAL_READINGS.json';write(p,full)
p=r/'research/library-current/COVERAGE.json';coverage=read(p);coverage['counts']['newDownloadsThisScope']=0
coverage['counts']['newDownloadsThisScopeBasis']='TwoexpandedretainedrawPDFpositions94–95/fournativecrops;0HTTP/newcontainers/sourcepositions.'
x=next(x for x in coverage['catalogue']if x['id']=='P08');x['latestXuankongLineScope']=summary
assert x['currentSourceUnitCounts']['totalDistinctPositionsRead']==195
x['currentEvidence'] += [state['latestReport'],state['sourceDirectory']+'/WORK_STATE.json',state['sourceDirectory']+'/MANUAL_READINGS.json',
 state['sourceDirectory']+'/RELATED_CONTEXT.json',state['sourceDirectory']+'/SOURCE_DISPOSITIONS.json',
 state['sourceDirectory']+'/source-room-lines.mjs','v53/qa/home-xuankong-lines/REFERENCE_RESULTS.json'];write(p,coverage)
for p in [r/'NEXT_STEPS.md',r/'research/library-current/COVERAGE.md',w/'PROJECT_RESEARCH_STATE.md']:
 old=p.read_text(encoding='utf-8-sig')
 p.write_text('Mốc thứ tự phòng và hào cửa,28/10/2026: `HOME_XUANKONG_LINES_REPORT.md`. '+summary+'\n\nTiếp: '+' '.join(nexts)+'\n\nCác mốc bên dưới là lịch sử; chưa có phương pháp nhà ở hoàn chỉnh hoặc mặt bằng đo hiện đại được xác lập.\n\n'+old,encoding='utf-8')
p=w/'PENDING_RESEARCH_STATE.json';pending=read(p);pending.update(status=state['status'],workDirectory=state['sourceDirectory'],
 currentWorkState=state['sourceDirectory']+'/WORK_STATE.json',latestReport=state['latestReport'],next=nexts,
 packageVerification='xuankong-lines-promotion-awaiting-final-no-write',
 inProgressStaging=dict(file='tmp/home-xuankong-lines-staging/WORK_STATE.json',status='promoted;packageverificationpending',catalogueID='P08'),
 currentScopeChecks=dict(runtimeChecks=7,actualHHCHexNumberCalls=64,expandedSourcePositions=2,newSourcePositions=0,nativeCrops=4,newHTTP200Bodies=0,wholeMethodsApplied=False))
write(p,pending)
print(json.dumps(dict(promotionIdentities=len(records),runtimeChecks=7,actualHHCHexNumberCalls=64,consumerChanged=False)))
