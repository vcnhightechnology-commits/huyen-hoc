from pathlib import Path
import json,hashlib,shutil
w=Path.cwd();b=w/'tmp/bazi-food-six-pillars-staging';r=w/'v53';dst=r/'research/bazi-food-six-pillars';q=r/'qa/bazi-food-six-pillars';assert not dst.exists()and not q.exists();assert json.loads((w/'archives/v53-before-bazi-food-six-pillars/SNAPSHOT.json').read_text())['sourceManifestFiles']==5019;dst.mkdir();q.mkdir();ident=[]
for p in sorted(b.iterdir()):
 if not p.is_file():continue
 if p.name=='REFERENCE_RESULTS.json':target=q/p.name
 elif p.name=='REPORT.md':target=r/'BAZI_FOOD_PILLAR_EXAMPLES_REPORT.md'
 elif p.suffix=='.py'or p.name=='test-six-pillars.mjs':target=dst/('STAGED_'+p.name)
 else:target=dst/p.name
 shutil.copyfile(p,target);assert p.read_bytes()==target.read_bytes();ident.append(dict(file=target.relative_to(w).as_posix(),stagedFile=p.relative_to(w).as_posix(),bytes=target.stat().st_size,sha256=hashlib.sha256(target.read_bytes()).hexdigest()))
s=(b/'test-six-pillars.mjs').read_text(encoding='utf-8')
for old,new in [("from'./source-pillar-example.mjs'","from'../research/bazi-food-six-pillars/source-pillar-example.mjs'"),("const b=resolve(import.meta.dirname),w=resolve(b,'../..'),","const b=resolve(import.meta.dirname,'../research/bazi-food-six-pillars'),w=resolve(b,'../../..'),"),("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/bazi-food-six-pillars/REFERENCE_RESULTS.json')")]:assert s.count(old)==1;s=s.replace(old,new)
(r/'scripts/test-bazi-food-six-pillars.mjs').write_text(s,encoding='utf-8');(dst/'PROMOTION_IDENTITIES.json').write_text(json.dumps(dict(date='2026-10-28',records=ident),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));write=lambda p,j:p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');state=read(dst/'WORK_STATE.json');summary=state['completedStep'];nexts=state['next']
p=r/'research/EXHAUSTIVE_WORK_STATE.json';j=read(p);j['previousHomeMonthGodWork']=j['currentWork'];j['currentWork']=dict(catalogueID='M01',work='Bát tự — sáu ví dụ trụ Thực thần và ranh giới thuật ngữ',sourceDirectory='v53/research/bazi-food-six-pillars',currentStep=summary,latestResearchReport='v53/BAZI_FOOD_PILLAR_EXAMPLES_REPORT.md',sourceLimits='Sixexact甲子examplesonly;rootrole/otherroots/C19score/fullpatternandoutcomesopen');j['inProgressScope']='v53/research/bazi-food-six-pillars/WORK_STATE.json';j['subsequentPriority']=nexts+j['subsequentPriority'];write(p,j);shutil.copyfile(p,w/'EXHAUSTIVE_WORK_STATE.json')
p=r/'research/full-study/WORK_STATE.json';j=read(p);j['latestResearchReport']='BAZI_FOOD_PILLAR_EXAMPLES_REPORT.md';j['exhaustiveNext']=nexts
for x in j['items']:
 if x['id']=='bazi':x['completed'].append(summary);x['remaining']=nexts;x['latestScope']=summary;x['latestResearchReport']='BAZI_FOOD_PILLAR_EXAMPLES_REPORT.md';x['nextFile']='v53/research/bazi-food-six-pillars/WORK_STATE.json'
write(p,j)
p=r/'research/library-current/COVERAGE.json';j=read(p);j['latestFollowup']='BAZI_FOOD_PILLAR_EXAMPLES_REPORT.md: '+summary;j['latestAcquisitionCounts']=dict(scope='BAZI_FOOD_PILLAR_EXAMPLES_REPORT.md',newHTTPRequests=0,newOriginalContainers=0,newIndependentWitnesses=0,newSourcePositions=0,expandedSourcePositions=4,nativeCropsViewedPixelMatched=3,printedCases=6,distinctComparedStemPairs=1,wholeWorksApplied=0);j['counts']['newDownloadsThisScope']=0;j['counts']['newDownloadsThisScopeBasis']='NoHTTP/container/positionnew;4oldimagesexpanded/3nativecrops'
for x in j['catalogue']:
 if x['id']=='M01':
  x['latestFoodPillarExampleScope']=summary;x['previousFoodParentContextSelectionBeforePillarExamples']=x['foodParentContextSelection'];x['foodParentContextSelection']=dict(total=90,parentsWithSelectedModuleOrDeclaredPremiseLinks=43,otherParentsWithoutSuchLinks=47,wholeParentsApplied=0,allSelectedParentsSubsidiaryClausesApplied=False,countingBasis='42previouspartiallinks+1C18exactcaseprovider;not43wholeappliedrules',currentMatrix='v53/research/bazi-food-six-pillars/CURRENT_CONTEXT_COVERAGE.json');x['currentEvidence']+=['v53/BAZI_FOOD_PILLAR_EXAMPLES_REPORT.md']+['v53/research/bazi-food-six-pillars/'+n for n in['WORK_STATE.json','SOURCE_DISPOSITIONS.json','MANUAL_PILLAR_EXAMPLES.json','CONTEXT_AUDIT.json','CURRENT_CONTEXT_COVERAGE.json','source-pillar-example.mjs']]+['v53/qa/bazi-food-six-pillars/REFERENCE_RESULTS.json']
write(p,j)
for name in['v53/NEXT_STEPS.md','v53/research/library-current/COVERAGE.md','PROJECT_RESEARCH_STATE.md']:
 p=w/name;p.write_text('Mốc28/10/2026 — BAZI_FOOD_PILLAR_EXAMPLES_REPORT.md\n\n'+summary+'\n\nTiếp:\n\n'+'\n\n'.join(nexts)+'\n\nCác mốc dưới đây là lịch sử; sáu nhãn trụ không thay bảng Thập thần hoặc thuật luận cách hoàn chỉnh.\n\n'+p.read_text(encoding='utf-8'),encoding='utf-8')
print(json.dumps(dict(promotedIdentities=len(ident),consumerChanged=False,wholeCatalogueCompleted=False)))
