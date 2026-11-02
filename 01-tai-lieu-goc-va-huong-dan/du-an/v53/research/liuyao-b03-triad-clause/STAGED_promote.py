from pathlib import Path
import json,hashlib,shutil
w=Path.cwd();b=w/'tmp/liuyao-b03-triad-clause-staging';r=w/'v53';dst=r/'research/liuyao-b03-triad-clause';q=r/'qa/liuyao-b03-triad-clause';assert not dst.exists()and not q.exists();assert json.loads((w/'archives/v53-before-liuyao-b03-triad-clause/SNAPSHOT.json').read_text())['sourceManifestFiles']==5041;dst.mkdir();q.mkdir();ident=[]
for p in sorted(b.iterdir()):
 if not p.is_file():continue
 if p.name=='REFERENCE_RESULTS.json':target=q/p.name
 elif p.name=='REPORT.md':target=r/'LIUYAO_B03_TRIAD_CLAUSE_REPORT.md'
 elif p.suffix=='.py'or p.name in['test-triad-clause.mjs','triad-clause-reference.mjs']:target=dst/('STAGED_'+p.name)
 else:target=dst/p.name
 shutil.copyfile(p,target);assert p.read_bytes()==target.read_bytes();ident.append(dict(file=target.relative_to(w).as_posix(),stagedFile=p.relative_to(w).as_posix(),bytes=target.stat().st_size,sha256=hashlib.sha256(target.read_bytes()).hexdigest()))
s=(b/'triad-clause-reference.mjs').read_text(encoding='utf-8');old="from'../../v53/research/liuyao-foundations/liuyao-reference.mjs'";assert s.count(old)==1;s=s.replace(old,"from'../liuyao-foundations/liuyao-reference.mjs'");(dst/'triad-clause-reference.mjs').write_text(s,encoding='utf-8')
s=(b/'test-triad-clause.mjs').read_text(encoding='utf-8')
for old,new in[("from'./triad-clause-reference.mjs'","from'../research/liuyao-b03-triad-clause/triad-clause-reference.mjs'"),("from'../../v53/research/liuyao-b03-volume4/triad-reference.mjs'","from'../research/liuyao-b03-volume4/triad-reference.mjs'"),("const b=resolve(import.meta.dirname),w=resolve(b,'../..'),","const b=resolve(import.meta.dirname,'../research/liuyao-b03-triad-clause'),w=resolve(b,'../../..'),"),("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/liuyao-b03-triad-clause/REFERENCE_RESULTS.json')")]:assert s.count(old)==1;s=s.replace(old,new)
(r/'scripts/test-liuyao-b03-triad-clause.mjs').write_text(s,encoding='utf-8');(dst/'PROMOTION_IDENTITIES.json').write_text(json.dumps(dict(date='2026-10-28',records=ident),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));write=lambda p,j:p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');state=read(dst/'WORK_STATE.json');summary=state['completedStep'];nexts=state['next']
p=r/'research/EXHAUSTIVE_WORK_STATE.json';j=read(p);j['previousBaziFoodPillarExampleWork']=j['currentWork'];j['currentWork']=dict(catalogueID='B03',work='Lục hào — nguyên câu Tam hình/Tam hợp và tiền đề hoạt động',sourceDirectory='v53/research/liuyao-b03-triad-clause',currentStep=summary,latestResearchReport='v53/LIUYAO_B03_TRIAD_CLAUSE_REPORT.md',sourceLimits='Corrected full clause only;three-active/darkactivity/calendarcompletion/efficacy/outcomesopen');j['inProgressScope']='v53/research/liuyao-b03-triad-clause/WORK_STATE.json';j['subsequentPriority']=nexts+j['subsequentPriority'];write(p,j);shutil.copyfile(p,w/'EXHAUSTIVE_WORK_STATE.json')
p=r/'research/full-study/WORK_STATE.json';j=read(p);j['latestResearchReport']='LIUYAO_B03_TRIAD_CLAUSE_REPORT.md';j['exhaustiveNext']=nexts
for x in j['items']:
 if x['id']=='yi':x['completed'].append(summary);x['remaining'].append(nexts[0]);x['latestScope']='../liuyao-b03-triad-clause/WORK_STATE.json';x['nextFile']='../liuyao-b03-triad-clause/WORK_STATE.json'
write(p,j)
p=r/'research/library-current/COVERAGE.json';j=read(p);j['latestFollowup']='LIUYAO_B03_TRIAD_CLAUSE_REPORT.md: '+summary;j['latestAcquisitionCounts']=dict(scope='LIUYAO_B03_TRIAD_CLAUSE_REPORT.md',newHTTPRequests=0,newOriginalContainers=0,newIndependentWitnesses=0,newSourcePositions=0,expandedSourcePositions=2,nativeCropsViewedPixelMatched=4,localDeclaredContexts=162,actualHHCHexNumberCalls=4,wholeWorksApplied=0);j['counts']['newDownloadsThisScope']=0;j['counts']['newDownloadsThisScopeBasis']='NoHTTP/container/positionnew;2oldimagesexpanded/4nativecrops'
for x in j['catalogue']:
 if x['id']=='B03':
  x['latestTriadClauseScope']=summary;x['sourceReadingCorrections']=[dict(previousFile='v53/research/liuyao-b03-volume4/TRIAD_TABLES.json',correction='v53/research/liuyao-b03-triad-clause/READING_CORRECTION.json',scope='literalquotationand>=2operationalinterpretation;consumerunchanged')];x['currentEvidence']+=['v53/LIUYAO_B03_TRIAD_CLAUSE_REPORT.md']+['v53/research/liuyao-b03-triad-clause/'+n for n in['WORK_STATE.json','SOURCE_MANIFEST.json','FULL_CLAUSE.json','READING_CORRECTION.json','RENDER_RECORD.json','QA_IMAGES.json','triad-clause-reference.mjs']]+['v53/qa/liuyao-b03-triad-clause/REFERENCE_RESULTS.json']
write(p,j)
for name in['v53/NEXT_STEPS.md','v53/research/library-current/COVERAGE.md','PROJECT_RESEARCH_STATE.md']:
 p=w/name;p.write_text('Mốc28/10/2026 — LIUYAO_B03_TRIAD_CLAUSE_REPORT.md\n\n'+summary+'\n\nTiếp:\n\n'+'\n\n'.join(nexts)+'\n\nCác mốc dưới đây là lịch sử; dùng đính chính nguyên câu B03 mới thay trích rút皆須/得成 cũ, không suy thành cục hoặc kết quả.\n\n'+p.read_text(encoding='utf-8'),encoding='utf-8')
print(json.dumps(dict(promotedIdentities=len(ident),consumerChanged=False,wholeCatalogueCompleted=False)))
