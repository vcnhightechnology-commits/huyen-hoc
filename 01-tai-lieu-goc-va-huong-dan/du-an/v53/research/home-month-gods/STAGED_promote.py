from pathlib import Path
import json,hashlib,shutil
w=Path.cwd();b=w/'tmp/home-month-gods-staging';r=w/'v53';dst=r/'research/home-month-gods';q=r/'qa/home-month-gods';assert not dst.exists()and not q.exists();assert json.loads((w/'archives/v53-before-home-month-gods/SNAPSHOT.json').read_text())['sourceManifestFiles']==4984;dst.mkdir();q.mkdir();ident=[]
for p in sorted(b.iterdir()):
 if not p.is_file():continue
 if p.name in ['REFERENCE_RESULTS.json','NATIVE_RESULTS.json']:target=q/p.name
 elif p.name=='REPORT.md':target=r/'HOME_MONTH_GODS_REPORT.md'
 elif p.suffix=='.py'or p.name=='test-month-gods.mjs':target=dst/('STAGED_'+p.name)
 else:target=dst/p.name
 shutil.copyfile(p,target);assert p.read_bytes()==target.read_bytes();ident.append(dict(file=target.relative_to(w).as_posix(),stagedFile=p.relative_to(w).as_posix(),bytes=target.stat().st_size,sha256=hashlib.sha256(target.read_bytes()).hexdigest()))
s=(b/'test-month-gods.mjs').read_text(encoding='utf-8-sig')
for old,new in [("from'./source-month-gods.mjs'","from'../research/home-month-gods/source-month-gods.mjs'"),("const b=resolve(import.meta.dirname),w=resolve(b,'../..'),","const b=resolve(import.meta.dirname,'../research/home-month-gods'),w=resolve(b,'../../..'),"),("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/home-month-gods/REFERENCE_RESULTS.json')")]:assert s.count(old)==1;s=s.replace(old,new)
(r/'scripts/test-home-month-gods.mjs').write_text(s,encoding='utf-8');(dst/'PROMOTION_IDENTITIES.json').write_text(json.dumps(dict(date='2026-10-28',records=ident),ensure_ascii=False,indent=2),encoding='utf-8')
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));write=lambda p,j:p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');state=read(dst/'WORK_STATE.json');summary=state['completedStep'];nexts=state['next']
p=r/'research/EXHAUSTIVE_WORK_STATE.json';j=read(p);j['previousTuviZiweiAnchorWork']=j['currentWork'];j['currentWork']=dict(catalogueID='P08',work='Nhà ở — bảy bảng thần theo tháng',sourceDirectory='v53/research/home-month-gods',currentStep=summary,latestResearchReport='v53/HOME_MONTH_GODS_REPORT.md',sourceLimits='84cells82clear2unresolved;20stempairsnotdate-selection/efficacy;source-month/trigramadaptersopen');j['inProgressScope']='v53/research/home-month-gods/WORK_STATE.json';j['subsequentPriority']=nexts+j['subsequentPriority'];write(p,j);shutil.copyfile(p,w/'EXHAUSTIVE_WORK_STATE.json')
p=r/'research/full-study/WORK_STATE.json';j=read(p);j['latestResearchReport']='HOME_MONTH_GODS_REPORT.md';j['exhaustiveNext']=nexts
for x in j['items']:
 if x['id']=='home':x['completed'].append(summary);x['remaining']=nexts
write(p,j)
p=r/'research/library-current/COVERAGE.json';j=read(p);j['latestFollowup']='HOME_MONTH_GODS_REPORT.md: '+summary;j['latestAcquisitionCounts']=dict(scope='HOME_MONTH_GODS_REPORT.md',newHTTPRequests=0,newOriginalContainers=0,newIndependentWitnesses=0,newSourcePositions=0,expandedSourcePositions=8,nativeCropsViewedPixelMatched=13,sourceRows=7,printedCells=84,clearCells=82,unresolvedCells=2,wholeWorksApplied=0);j['counts']['newDownloadsThisScope']=0;j['counts']['newDownloadsThisScopeBasis']='NoHTTP/container/positionnew;8oldimagesexpanded/13nativecrops'
for x in j['catalogue']:
 if x['id']=='P08':x['latestMonthGodScope']=summary;x['currentEvidence']+=['v53/HOME_MONTH_GODS_REPORT.md']+['v53/research/home-month-gods/'+n for n in ['WORK_STATE.json','SOURCE_DISPOSITIONS.json','MANUAL_MONTH_GOD_TABLES.json','CONTEXT_READINGS.json','source-month-gods.mjs']]+['v53/qa/home-month-gods/REFERENCE_RESULTS.json','v53/qa/home-month-gods/NATIVE_RESULTS.json']
write(p,j)
for name in ['v53/NEXT_STEPS.md','v53/research/library-current/COVERAGE.md','PROJECT_RESEARCH_STATE.md']:
 p=w/name;p.write_text('Mốc28/10/2026 — HOME_MONTH_GODS_REPORT.md\n\n'+summary+'\n\nTiếp:\n\n'+'\n\n'.join(nexts)+'\n\nCác mốc dưới đây là lịch sử; tọa độ can/quẻ không thay thuật chọn ngày hoàn chỉnh.\n\n'+p.read_text(encoding='utf-8'),encoding='utf-8')
print(json.dumps(dict(promotedIdentities=len(ident),consumerChanged=False,wholeCatalogueCompleted=False)))
