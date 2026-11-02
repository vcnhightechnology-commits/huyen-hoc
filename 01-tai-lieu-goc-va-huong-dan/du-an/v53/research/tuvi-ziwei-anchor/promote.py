from pathlib import Path
import json,shutil,hashlib
w=Path.cwd();b=w/'tmp/tuvi-upper-remaining-staging';r=w/'v53';dest=r/'research/tuvi-ziwei-anchor';qa=r/'qa/tuvi-ziwei-anchor';assert not dest.exists()and not qa.exists();assert json.loads((w/'archives/v53-before-tuvi-ziwei-anchor/SNAPSHOT.json').read_text())['sourceManifestFiles']==4895
dest.mkdir();qa.mkdir();ident=[]
for p in sorted(b.iterdir()):
 if not p.is_file():continue
 if p.name=='REFERENCE_RESULTS.json':target=qa/p.name
 elif p.name=='REPORT.md':target=r/'TUVI_ZIWEI_ANCHOR_REPORT.md'
 elif p.name in ['snapshot.py','test-ziwei-anchor.mjs']:target=dest/('STAGED_'+p.name)
 else:target=dest/p.name
 shutil.copyfile(p,target);assert target.read_bytes()==p.read_bytes();ident.append(dict(file=target.relative_to(w).as_posix(),stagedFile=p.relative_to(w).as_posix(),bytes=target.stat().st_size,sha256=hashlib.sha256(target.read_bytes()).hexdigest()))
text=(b/'test-ziwei-anchor.mjs').read_text(encoding='utf-8')
for old,new in [("from'./source-ziwei-anchor.mjs'","from'../research/tuvi-ziwei-anchor/source-ziwei-anchor.mjs'"),("const b=resolve(import.meta.dirname),w=resolve(b,'../..'),","const b=resolve(import.meta.dirname,'../research/tuvi-ziwei-anchor'),w=resolve(b,'../../..'),"),("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/tuvi-ziwei-anchor/REFERENCE_RESULTS.json')")]:
 assert text.count(old)>=1,(old,text.count(old));text=text.replace(old,new)
(r/'scripts/test-tuvi-ziwei-anchor.mjs').write_text(text,encoding='utf-8')
(dest/'PROMOTION_IDENTITIES.json').write_text(json.dumps(dict(date='2026-10-28',records=ident),ensure_ascii=False,indent=2),encoding='utf-8')
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));write=lambda p,j:p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');state=read(dest/'WORK_STATE.json');summary=state['completedStep'];nexts=state['next']
p=r/'research/EXHAUSTIVE_WORK_STATE.json';j=read(p);j['previousTuviMingShenWork']=j['currentWork'];j['historicalSupersededTuviUpperMissingImagePriorities']=j['subsequentPriority'][:3];j['currentWork']=dict(catalogueID='T01',work='Tử vi — năm đồ an Tử Vi và bản đồ đủ ảnh tập trên',sourceDirectory='v53/research/tuvi-ziwei-anchor',currentStep=summary,latestResearchReport='v53/TUVI_ZIWEI_ANCHOR_REPORT.md',sourceLimits='129physicalpositionsfirstpassnotallrules;150day-cucanchorsonly;all6juan/generaldate-cucassignment/outcomesopen');j['inProgressScope']='v53/research/tuvi-ziwei-anchor/WORK_STATE.json';j['subsequentPriority']=nexts+j['subsequentPriority'][3:];write(p,j);shutil.copyfile(p,w/'EXHAUSTIVE_WORK_STATE.json')
p=r/'research/full-study/WORK_STATE.json';j=read(p);j['latestResearchReport']='TUVI_ZIWEI_ANCHOR_REPORT.md';j['exhaustiveNext']=nexts
for x in j['items']:
 if x['id']=='tuvi':x['completed'].append(summary);x['remaining']=nexts
write(p,j)
p=r/'research/library-current/COVERAGE.json';j=read(p);j['latestFollowup']='TUVI_ZIWEI_ANCHOR_REPORT.md: '+summary;j['latestAcquisitionCounts']=dict(scope='TUVI_ZIWEI_ANCHOR_REPORT.md',newHTTP200JPEGDerivativeBodies=43,newDistinctPositions=40,higherResolutionSamePositions=3,newOriginalJP2Bodies=0,newIndependentEditions=0,sourceCoordinates=150,wholeWorksApplied=0);j['counts']['newDownloadsThisScope']=43;j['counts']['newDownloadsThisScopeBasis']='40missingpositionJPEGs+3higherresolutionJPEGs;43TLS200headerSHA;0JP2original/independentedition'
for x in j['catalogue']:
 if x['id']=='T01':
  x['latestZiweiAnchorScope']=summary;x['currentSourceUnitCounts']=dict(physicalItem='4468520 upper item',manifestPositions=129,distinctRetainedPositions=129,newFirstPassReadPositions=40,continuousFirstPassPositionsIncludingPrior=129,remainingUnretainedPositions=0,priorRetainedPositions=89,priorPositionsExpanded=16,bodyLastCanvas=127,endpaperFragmentCanvas=128,blankRearSurfaceCanvas=129,allFirstPassChaptersApplied=False,allSixJuanBodyPresent=False)
  x['currentEvidence']+=['v53/TUVI_ZIWEI_ANCHOR_REPORT.md']+['v53/research/tuvi-ziwei-anchor/'+n for n in ['WORK_STATE.json','SOURCE_MANIFEST.json','CURRENT_CANVAS_INVENTORY.json','FIRST_PASS_READINGS.json','ZIWEI_DAY_DIAGRAMS.json','READING_CORRECTIONS.json','source-ziwei-anchor.mjs']]+['v53/qa/tuvi-ziwei-anchor/REFERENCE_RESULTS.json']
write(p,j)
p=r/'research/library-current/COVERAGE.md';p.write_text('Mốc 28/10/2026 — TUVI_ZIWEI_ANCHOR_REPORT.md\n\n'+summary+'\n\n'+'\n\n'.join(nexts)+'\n\nCác mốc dưới đây là lịch sử; nguồn ảnh đủ không đồng nghĩa áp hết.\n\n'+p.read_text(encoding='utf-8'),encoding='utf-8')
p=r/'NEXT_STEPS.md';p.write_text('Mốc 28/10/2026 — Năm đồ hình an Tử Vi\n\n'+summary+'\n\nTiếp:\n\n'+'\n\n'.join(nexts)+'\n\nCác mốc dưới đây là lịch sử; 129 ảnh vật lý đã xem đầu, mọi điều kiện chưa áp hết.\n\n'+p.read_text(encoding='utf-8'),encoding='utf-8')
p=w/'PROJECT_RESEARCH_STATE.md';p.write_text('Mốc 28/10/2026 — TUVI_ZIWEI_ANCHOR_REPORT.md\n\n'+summary+'\n\nTiếp:\n\n'+'\n\n'.join(nexts)+'\n\nCác mốc dưới đây là lịch sử; không tái tải129ảnh hoặc coi toàn kho đã xong.\n\n'+p.read_text(encoding='utf-8'),encoding='utf-8')
print(json.dumps({'promotedIdentities':len(ident),'wholeCatalogueCompleted':False,'consumerChanged':False}))
