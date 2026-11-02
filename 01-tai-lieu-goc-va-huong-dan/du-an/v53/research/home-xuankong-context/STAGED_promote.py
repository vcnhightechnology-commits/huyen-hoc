from pathlib import Path
from hashlib import sha256
import json,shutil
w=Path.cwd();r=w/'v53';s=w/'tmp/home-xuankong-context-staging';c=w/'tmp/home-courtyard-collation-staging';b=r/'research/home-xuankong-context';q=r/'qa/home-xuankong-context'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda p,o:p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not b.exists()and not q.exists()
assert read(w/'archives/v53-before-home-xuankong-context/SNAPSHOT.json')['sourceManifestFiles']==4464
assert read(s/'WORK_STATE.json')['completeRuntimeChecks']==5 and read(c/'WORK_STATE.json')['fullyResolvedMatches']==64
b.mkdir();q.mkdir();identities=[]
def copy(p,d):
 d.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,d);assert p.read_bytes()==d.read_bytes()
 identities.append(dict(file=d.relative_to(w).as_posix(),stagingFile=p.relative_to(w).as_posix(),bytes=d.stat().st_size,sha256=sha256(d.read_bytes()).hexdigest()))
for stage,sub in [(s,''),(c,'collation')]:
 for p in sorted(stage.iterdir()):
  if not p.is_file():continue
  if p.name=='REPORT.md':dest=r/'HOME_XUANKONG_CONTEXT_REPORT.md'
  elif p.suffix=='.png'or p.name in ['QA_IMAGES.json','REFERENCE_RESULTS.json']:dest=q/sub/p.name
  elif p.suffix in ['.py','.mjs']and p.name!='xuankong-context-reference.mjs':dest=b/sub/('STAGED_'+p.name)
  else:dest=b/sub/p.name
  copy(p,dest)
text=(s/'test-xuankong-context.mjs').read_text(encoding='utf-8')
for old,new in [("from './xuankong-context-reference.mjs'","from '../research/home-xuankong-context/xuankong-context-reference.mjs'"),("const b=import.meta.dirname,w=resolve(b,'../..'),checks=[],fixtures=[];","const b=resolve(import.meta.dirname,'../research/home-xuankong-context'),w=resolve(b,'../../..'),checks=[],fixtures=[];"),("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/home-xuankong-context/REFERENCE_RESULTS.json')")]:assert text.count(old)==1;text=text.replace(old,new)
(r/'scripts/test-home-xuankong-context.mjs').write_text(text,encoding='utf-8')
write(b/'PROMOTION_IDENTITIES.json',dict(date='2026-10-28',records=identities,moduleByteIdenticalToStaging=True,testOnlyThreePathRelocations=True,passedRuntimeTestsNotRerunOnPromotion=True))
state=read(b/'WORK_STATE.json');summary=state['completedStep'];nexts=state['next']
p=w/'EXHAUSTIVE_WORK_STATE.json';ex=read(p);ex['previousHomeHourAlignmentWork']=ex['currentWork']
ex['currentWork']=dict(catalogueID='P08',work='陽宅十書 — 玄空語境與圖格對勘',sourceDirectory=state['sourceDirectory'],currentStep=summary,latestResearchReport=state['latestReport'],internalHourReference='v53/research/home-hour-alignment/source-hour-reference.mjs',sourceLimits='Named frame labels/declared count comparison only;69witnesscells64resolved5partial;fullfirst-drawexchangeandmoderngeometryopen')
ex['inProgressScope']=state['sourceDirectory']+'/WORK_STATE.json';ex['subsequentPriority']=[' '.join(nexts)]+ex['subsequentPriority'];write(p,ex);(r/'research/EXHAUSTIVE_WORK_STATE.json').write_bytes(p.read_bytes())
p=r/'research/full-study/WORK_STATE.json';full=read(p);full['latestResearchReport']=state['latestReport'];full['exhaustiveNext']=' '.join(nexts)
x=next(x for x in full['items']if x['id']=='home');x['completed'].append(summary);x['latestResearchReport']=state['latestReport'];x['latestScope']='../home-xuankong-context/WORK_STATE.json';write(p,full)
p=r/'research/library-current/COVERAGE.json';coverage=read(p);coverage['counts']['newDownloadsThisScope']=0;coverage['counts']['newDownloadsThisScopeBasis']='7expandedretainedrawreviews/69witnesscelldispositions/9nativecrops;0HTTP/newcontainers/positions/witnesses.'
x=next(x for x in coverage['catalogue']if x['id']=='P08');x['scope']='195/195firstpass/0wholeunits;144correctedhourcoordinates/0differences. XuanKongnamedpolarityframes5checks8HHC+8watercalls;69witnesscells64fullymatched5partial;fullmethodopen.';x['latestSourceScope']=summary
x['currentSourceUnitCounts'].update(selectedSecondWitnessCells=69,fullyResolvedSecondWitnessMatches=64,partialSecondWitnessCells=5)
x['currentEvidence'] += [state['latestReport'],state['sourceDirectory']+'/WORK_STATE.json',state['sourceDirectory']+'/MANUAL_SOURCE_ANCHORS.json',state['sourceDirectory']+'/RAW_REVIEW.json',state['sourceDirectory']+'/xuankong-context-reference.mjs',state['sourceDirectory']+'/collation/MANUAL_WITNESS_CELLS.json','v53/qa/home-xuankong-context/REFERENCE_RESULTS.json'];write(p,coverage)
for p,title in [(r/'NEXT_STEPS.md','Mốc tách khung trang quái'),(r/'research/library-current/COVERAGE.md','Mốc đối chiếu từng ô đồ nhà'),(w/'PROJECT_RESEARCH_STATE.md','Mốc trang quái và 69 ô nhân chứng')]:
 old=p.read_text(encoding='utf-8-sig');p.write_text(f'{title},28/10/2026: `HOME_XUANKONG_CONTEXT_REPORT.md`. {summary}\n\nTiếp: '+' '.join(nexts)+'\n\nBảng giờ hiện hành là144ô/0khác sau đính chính; các ghi chép12khác司命/12勾陳chưachép ở phía dưới là lịch sử đã rút lại.\n\n'+old,encoding='utf-8')
p=w/'PENDING_RESEARCH_STATE.json';pending=read(p);pending.update(status=state['status'],workDirectory=state['sourceDirectory'],currentWorkState=state['sourceDirectory']+'/WORK_STATE.json',latestReport=state['latestReport'],next=nexts,packageVerification='xuankong-context-promotion-awaiting-final-no-write',inProgressStaging=dict(file='tmp/home-xuankong-context-staging/WORK_STATE.json',status='promoted;packageverificationpending',catalogueID='P08'),otherPendingStaging=[]);write(p,pending)
print(json.dumps(dict(promotionIdentities=len(identities),runtimeChecks=5,actualHHCDirections=8,actualWaterReference=8,witnessCells=69,fullyResolvedMatches=64,partialCells=5,consumerChanged=False)))
