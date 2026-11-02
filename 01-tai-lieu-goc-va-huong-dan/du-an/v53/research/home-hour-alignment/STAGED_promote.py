from pathlib import Path
from hashlib import sha256
import json,shutil
w=Path.cwd();r=w/'v53';s=w/'tmp/home-hour-gouchen-staging';b=r/'research/home-hour-alignment';q=r/'qa/home-hour-alignment'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda p,o:p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not b.exists()and not q.exists()
assert read(w/'archives/v53-before-home-hour-alignment/SNAPSHOT.json')['sourceManifestFiles']==4438
assert read(s/'CORRECTION_RESULTS.json')['labelsMatchedAfterAliases']==144
b.mkdir();q.mkdir();identities=[]
def copy(p,d):
 shutil.copyfile(p,d);assert p.read_bytes()==d.read_bytes()
 identities.append(dict(file=d.relative_to(w).as_posix(),stagingFile=p.relative_to(w).as_posix(),bytes=d.stat().st_size,sha256=sha256(d.read_bytes()).hexdigest()))
for p in sorted(s.iterdir()):
 if not p.is_file():continue
 if p.name=='REPORT.md':dest=r/'HOME_HOUR_ALIGNMENT_REPORT.md'
 elif p.name=='QA_IMAGES.json':dest=b/'INITIAL_QA_IMAGES.json'
 elif p.name=='p135-gouchen-column-native.png':dest=q/('INITIAL_'+p.name)
 elif p.suffix=='.png'or p.name in ['CORRECTION_QA_IMAGES.json','REFERENCE_RESULTS.json','CORRECTION_RESULTS.json']:dest=q/p.name
 elif p.suffix in ['.py','.mjs']and p.name!='source-hour-reference.mjs':dest=b/('STAGED_'+p.name)
 else:dest=b/p.name
 copy(p,dest)
test=(s/'test-corrected-hour-reference.mjs').read_text(encoding='utf-8')
pairs=[("from './source-hour-reference.mjs'","from '../research/home-hour-alignment/source-hour-reference.mjs'"),("const b=import.meta.dirname,w=resolve(b,'../..'),system=SOURCE_HOUR_SYSTEM;","const b=resolve(import.meta.dirname,'../research/home-hour-alignment'),w=resolve(b,'../../..'),system=SOURCE_HOUR_SYSTEM;"),("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/home-hour-alignment/REFERENCE_RESULTS.json')")]
for old,new in pairs:assert test.count(old)==1;test=test.replace(old,new)
(r/'scripts/test-home-hour-alignment.mjs').write_text(test,encoding='utf-8')
write(b/'PROMOTION_IDENTITIES.json',dict(date='2026-10-28',records=identities,moduleByteIdenticalToStaging=True,testOnlyThreePathRelocations=True,passedRuntimeTestsNotRerunOnPromotion=True))
state=read(b/'WORK_STATE.json');summary=state['completedStep'];nexts=state['next']
p=w/'EXHAUSTIVE_WORK_STATE.json';ex=read(p);ex['previousHomeCourtyardsWork']=ex['currentWork']
ex['currentWork']=dict(catalogueID='P08',work='陽宅十書 — 定時表欄位校正',sourceDirectory=state['sourceDirectory'],currentStep=summary,latestResearchReport=state['latestReport'],internalHourReference=state['sourceDirectory']+'/source-hour-reference.mjs',sourceLimits='144correctedhourcoordinates/0source-enginedifferencesafteraliases;neighbor日guidesemantics/fullcalendarselectionopen')
ex['inProgressScope']=state['sourceDirectory']+'/WORK_STATE.json'
retracted=[x for x in ex['subsequentPriority']if '司命'in x or '勾陳'in x]
ex['historicalRetractedHourColumnPriorities']=dict(reason='Wrong column alignment, not edition discrepancy; see HOME_HOUR_ALIGNMENT_REPORT.md',items=retracted)
ex['subsequentPriority']=[' '.join(nexts)]+[x for x in ex['subsequentPriority']if x not in retracted]
write(p,ex);(r/'research/EXHAUSTIVE_WORK_STATE.json').write_bytes(p.read_bytes())
p=r/'research/full-study/WORK_STATE.json';full=read(p);full['latestResearchReport']=state['latestReport'];full['exhaustiveNext']=' '.join(nexts)
x=next(x for x in full['items']if x['id']=='home');x['completed'].append(summary);x['latestResearchReport']=state['latestReport'];x['latestScope']='../home-hour-alignment/WORK_STATE.json';x['currentHourReference']='../home-hour-alignment/source-hour-reference.mjs';x['hourColumnCorrectionSupersedesPriorDiscrepancyClaims']=True
write(p,full)
p=r/'research/library-current/COVERAGE.json';c=read(p);c['counts']['newDownloadsThisScope']=0;c['counts']['newDownloadsThisScopeBasis']='Native-header alignment correction of retained135;0HTTP/containers/newpositions.'
x=next(x for x in c['catalogue']if x['id']=='P08');x['scope']='195/195firstpass/0wholeunits;hourtablecorrected144coordinates144matches/0differences/0pendingcolumns;12priorSimingdifferencesretractedascolumntranscriptionerror. Courtyards69cells/6selectedsecondwitnesscells;fullpremisesopen.';x['latestSourceScope']=summary
x['currentSourceUnitCounts'].update(manualHourCells=144,pendingHourCells=0,retainedHourDifferences=0);x['currentHourReference']=state['sourceDirectory']+'/source-hour-reference.mjs'
x['hourColumnCorrectionSupersedesPriorClaims']=True
x['currentEvidence'] += [state['latestReport'],state['sourceDirectory']+'/WORK_STATE.json',state['sourceDirectory']+'/READING_CORRECTION_AUDIT.json',state['sourceDirectory']+'/MANUAL_HOUR_TABLE.json',state['sourceDirectory']+'/source-hour-reference.mjs','v53/qa/home-hour-alignment/CORRECTION_RESULTS.json'];write(p,c)
for p,title in [(r/'NEXT_STEPS.md','Đính chính bảng giờ hiện hành'),(r/'research/library-current/COVERAGE.md','Đính chính độ phủ bảng giờ'),(w/'PROJECT_RESEARCH_STATE.md','Đính chính đọc cột Tư Mệnh–Câu Trần')]:
 old=p.read_text(encoding='utf-8-sig');p.write_text(f'{title},28/10/2026: `HOME_HOUR_ALIGNMENT_REPORT.md`. {summary}\n\nƯu tiên hiện hành: '+' '.join(nexts)+'\n\nCác ghi chép phía dưới về12khác司命/12勾陳chưađọc là lịch sử đã rút lại vì lệch cột,không phải dữ liệu hiện hành.\n\n'+old,encoding='utf-8')
p=w/'PENDING_RESEARCH_STATE.json';pending=read(p);pending.update(status=state['status'],workDirectory=state['sourceDirectory'],currentWorkState=state['sourceDirectory']+'/WORK_STATE.json',latestReport=state['latestReport'],next=nexts,packageVerification='hour-alignment-promotion-awaiting-final-no-write',inProgressStaging=dict(file='tmp/home-hour-gouchen-staging/WORK_STATE.json',status='promoted;packageverificationpending',catalogueID='P08'));write(p,pending)
print(json.dumps(dict(promotionIdentities=len(identities),runtimeChecks=6,actualLunarObjects=144,correctedCoordinates=144,consumerChanged=False)))
