from pathlib import Path
from hashlib import sha256
import json,shutil
w=Path.cwd();r=w/'v53';s=w/'tmp/home-yangzhai-final-spans-staging'
b=r/'research/home-yangzhai-final-spans';q=r/'qa/home-yangzhai-final-spans'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda p,o:p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not b.exists()and not q.exists()
snapshot=read(w/'archives/v53-before-home-yangzhai-final-spans/SNAPSHOT.json');assert snapshot['sourceManifestFiles']==4218
result=read(w/'tmp/home-yangzhai-selection-staging/REFERENCE_RESULTS.json');assert len(result['checks'])==8 and all(x['ok']for x in result['checks'])
assert read(s/'NATIVE_RESULTS.json')['newDistinctReadPositions']==92
b.mkdir();q.mkdir();identities=[]
def copy(p,d):
 d.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,d);assert p.read_bytes()==d.read_bytes()
 identities.append({'file':d.relative_to(w).as_posix(),'stagingFile':p.relative_to(w).as_posix(),'bytes':d.stat().st_size,'sha256':sha256(d.read_bytes()).hexdigest()})
for scope in ['exterior','selection','talismans']:
 stage=w/f'tmp/home-yangzhai-{scope}-staging'
 for p in sorted(stage.rglob('*')):
  if not p.is_file():continue
  rel=p.relative_to(stage)
  if rel.parts[0]=='qa':target=q/scope/rel.name
  elif p.name in ['QA_IMAGES.json','REFERENCE_RESULTS.json']:target=q/scope/p.name
  elif p.name=='WORK_STATE.json':target=b/scope/'STAGED_WORK_STATE.json'
  elif p.suffix in ['.py','.mjs']and p.name!='source-hour-reference.mjs':target=b/scope/('STAGED_'+p.name)
  else:target=b/scope/rel
  copy(p,target)
for p in sorted(s.iterdir()):
 if not p.is_file():continue
 if p.name=='REPORT.md':target=r/'HOME_FINAL_SPANS_REPORT.md'
 elif p.name=='NATIVE_RESULTS.json':target=q/p.name
 elif p.name=='promote.py':target=b/'STAGED_promote.py'
 else:target=b/p.name
 copy(p,target)
copy(w/'tmp/verify-home-final-native.py',b/'STAGED_verify-native.py')
test=(w/'tmp/home-yangzhai-selection-staging/test-hour-reference.mjs').read_text(encoding='utf-8')
replacements=[("from './source-hour-reference.mjs'","from '../research/home-yangzhai-final-spans/selection/source-hour-reference.mjs'"),
 ("const b=import.meta.dirname,w=resolve(b,'../..'),r=resolve(w,'v53');","const b=resolve(import.meta.dirname,'../research/home-yangzhai-final-spans/selection'),w=resolve(b,'../../../..'),r=resolve(w,'v53');"),
 ("resolve(b,'REFERENCE_RESULTS.json')","resolve(r,'qa/home-yangzhai-final-spans/selection/REFERENCE_RESULTS.json')")]
for old,new in replacements:assert test.count(old)==1;test=test.replace(old,new)
(r/'scripts/test-home-final-spans.mjs').write_text(test,encoding='utf-8')
write(b/'PROMOTION_IDENTITIES.json',{'date':'2026-10-28','records':identities,'moduleByteIdenticalToStaging':True,'testOnlyThreePathRelocations':True,'passedRuntimeTestsNotRerunOnPromotion':True,'localIdentitiesNotPublisherSignatures':True})
state=read(b/'WORK_STATE.json');summary=state['completedStep'];nexts=state['next']
p=w/'EXHAUSTIVE_WORK_STATE.json';ex=read(p);ex['previousHomeDoorWaterWork']=ex['currentWork']
ex['currentWork']={'catalogueID':'P08','relatedCatalogueIDs':['P08'],'work':'陽宅十書 — 全部十論首次通讀與定時表',
 'reason':'Close remaining first-pass spans while retaining source differences and bounded functional extraction.',
 'sourceDirectory':state['sourceDirectory'],'currentStep':summary,'latestResearchReport':state['latestReport'],
 'sourceLimits':'195/195positions firstpass;0wholeunits applied;132hourcells/12pending/12source-engine differences;all remaining clauses explicit.',
 'sourceUnitMap':state['sourceUnitMap'],'internalHourReference':state['sourceDirectory']+'/selection/source-hour-reference.mjs'}
ex['inProgressScope']=state['sourceDirectory']+'/WORK_STATE.json';ex['subsequentPriority']=[' '.join(nexts)]+ex['subsequentPriority'];ex['date']='2026-10-28'
write(p,ex);(r/'research/EXHAUSTIVE_WORK_STATE.json').write_bytes(p.read_bytes())
p=r/'research/full-study/WORK_STATE.json';full=read(p);full['latestResearchReport']=state['latestReport'];full['exhaustiveNext']=' '.join(nexts)
for x in full['items']:
 if x['id']in ['home','fengshui','directions']:
  x.setdefault('completed',[]).append(summary);x['latestResearchReport']=state['latestReport']
write(p,full)
p=r/'research/library-current/COVERAGE.json';coverage=read(p)
coverage['counts']['newDownloadsThisScope']=0;coverage['counts']['newDownloadsThisScopeBasis']='RetainedPDF;95rawrecords/94uniquepositions/92newreads;0HTTP/container/independentwitness.'
item=next(x for x in coverage['catalogue']if x['id']=='P08')
item['scope']='195/195distinctpositions and10/10mainspans firstpass,0wholeunitsapplied.132manualhourcells/120aliasmatches/12retainedSimingdifferences/12GouChenpending;8checks/144actualLunarobjects. Fullcalendar/geometry/sourceoutcomesremainopen;ritualreservedhistorical.'
item['latestSourceScope']=summary;item['latestSourceUnitMap']=state['sourceUnitMap']
item['currentSourceUnitCounts'].update(firstPassCompleteBodySpans=10,wholeUnitsApplied=0,earlierDistinctPositionsRead=103,newRawDCTPositionsViewed=94,newRawArtifactRecords=95,newDistinctSourcePositionsRead=92,totalDistinctPositionsRead=195,unreadPositions=0,manualHourCells=132,pendingHourCells=12,retainedHourDifferences=12)
item['currentEvidence'] += [state['latestReport'],state['sourceUnitMap'],state['sourceDirectory']+'/SOURCE_DISPOSITIONS.json',state['sourceDirectory']+'/selection/MANUAL_HOUR_TABLE.json',state['sourceDirectory']+'/selection/READING_CORRECTION_AUDIT.json',state['sourceDirectory']+'/selection/source-hour-reference.mjs','v53/qa/home-yangzhai-final-spans/selection/REFERENCE_RESULTS.json']
write(p,coverage)
for p,title in [(r/'NEXT_STEPS.md','Mốc khép lượt đọc đầu P08'),(r/'research/library-current/COVERAGE.md','Mốc độ phủ P08'),(w/'PROJECT_RESEARCH_STATE.md','Mốc khép lượt đọc đầu Dương Trạch Thập Thư')]:
 old=p.read_text(encoding='utf-8-sig');p.write_text(f'{title},28/10/2026: `HOME_FINAL_SPANS_REPORT.md`. {summary}\n\nTiếp: '+ ' '.join(nexts)+'\n\n'+old,encoding='utf-8')
pending=read(w/'PENDING_RESEARCH_STATE.json')
pending.update(status=state['status'],workDirectory=state['sourceDirectory'],currentWorkState=state['sourceDirectory']+'/WORK_STATE.json',latestReport=state['latestReport'],next=nexts,
 packageVerification='final-spans-promotion-awaiting-package-final-no-write',inProgressStaging={'file':'tmp/home-yangzhai-final-spans-staging/WORK_STATE.json','status':'promoted; source/release verification pending','catalogueID':'P08'})
pending['otherPendingStaging']=[]
write(w/'PENDING_RESEARCH_STATE.json',pending)
print(json.dumps({'promotionIdentities':len(identities),'completeRuntimeChecks':8,'newDistinctReadPositions':92,'totalBookFirstPassPositions':195,'consumerChanged':False}))
