from pathlib import Path
import json,hashlib,shutil
w=Path.cwd();b=w/'tmp/tuvi-lower-item-staging';r=w/'v53';dst=r/'research/tuvi-lower-printed-cases';q=r/'qa/tuvi-lower-printed-cases';assert not dst.exists()and not q.exists();assert json.loads((w/'archives/v53-before-tuvi-lower-printed-cases/SNAPSHOT.json').read_text())['sourceManifestFiles']==5069;dst.mkdir();q.mkdir();ident=[]
for p in sorted(b.iterdir()):
 if not p.is_file():continue
 if p.name=='REFERENCE_RESULTS.json':target=q/p.name
 elif p.name=='REPORT.md':target=r/'TUVI_LOWER_PRINTED_CASES_REPORT.md'
 elif p.suffix=='.py'or p.name in['run-printed-cases.mjs','test-printed-cases.mjs']:target=dst/('STAGED_'+p.name)
 else:target=dst/p.name
 shutil.copyfile(p,target);assert p.read_bytes()==target.read_bytes();ident.append(dict(file=target.relative_to(w).as_posix(),stagedFile=p.relative_to(w).as_posix(),bytes=target.stat().st_size,sha256=hashlib.sha256(target.read_bytes()).hexdigest()))
for filename in ['run-printed-cases.mjs','test-printed-cases.mjs']:
 s=(b/filename).read_text(encoding='utf-8')
 for old,new in[("from'./printed-case-reference.mjs'","from'../research/tuvi-lower-printed-cases/printed-case-reference.mjs'"),("const b=resolve(import.meta.dirname),w=resolve(b,'../..'),","const b=resolve(import.meta.dirname,'../research/tuvi-lower-printed-cases'),w=resolve(b,'../../..'),")]:assert s.count(old)==1;s=s.replace(old,new)
 if filename.startswith('test'):
  old="resolve(b,'REFERENCE_RESULTS.json')";assert s.count(old)==1;s=s.replace(old,"resolve(w,'v53/qa/tuvi-lower-printed-cases/REFERENCE_RESULTS.json')")
 (r/'scripts'/filename.replace('printed-cases','tuvi-lower-printed-cases')).write_text(s,encoding='utf-8')
(dst/'PROMOTION_IDENTITIES.json').write_text(json.dumps(dict(date='2026-10-28',records=ident),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
rd=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));wr=lambda p,j:p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');state=rd(dst/'WORK_STATE.json');summary=state['completedStep'];nexts=state['next']
p=r/'research/EXHAUSTIVE_WORK_STATE.json';j=rd(p);j['previousB03TriadClauseWork']=j['currentWork'];j['currentWork']=dict(catalogueID='T01',work='Tử vi — tập dưới và hai lá số in',sourceDirectory='v53/research/tuvi-lower-printed-cases',currentStep=summary,latestResearchReport='v53/TUVI_LOWER_PRINTED_CASES_REPORT.md',sourceLimits='12of137positions;38fieldspereachengine;1glyphunresolved;notbiographicaldates/outcomes;lowerending七literal');j['inProgressScope']='v53/research/tuvi-lower-printed-cases/WORK_STATE.json';j['subsequentPriority']=nexts+j['subsequentPriority'];wr(p,j);shutil.copyfile(p,w/'EXHAUSTIVE_WORK_STATE.json')
p=r/'research/full-study/WORK_STATE.json';j=rd(p);j['latestResearchReport']='TUVI_LOWER_PRINTED_CASES_REPORT.md';j['exhaustiveNext']=nexts
for x in j['items']:
 if x['id']=='tuvi':x['completed'].append(summary);x['remaining']=nexts;x['latestScope']=summary;x['latestResearchReport']='TUVI_LOWER_PRINTED_CASES_REPORT.md';x['nextFile']='v53/research/tuvi-lower-printed-cases/WORK_STATE.json'
wr(p,j)
p=r/'research/library-current/COVERAGE.json';j=rd(p);j['latestFollowup']='TUVI_LOWER_PRINTED_CASES_REPORT.md: '+summary;j['latestAcquisitionCounts']=dict(scope='TUVI_LOWER_PRINTED_CASES_REPORT.md',newHTTP200Bodies=16,newOriginalContainers=0,newIndependentWitnesses=0,newSourcePositions=12,newJPEGDerivatives=13,nativeCropsViewedPixelMatched=8,matchedSourceFieldsPerEngine=38,actualHHCTuviCalls=2,actualIztroNatalCalls=2,wholeWorksApplied=0);j['counts']['newDownloadsThisScope']=16;j['counts']['newDownloadsThisScopeBasis']='3institutionalHTML/JSON+13JPEGderivativesfor12positions;not16booksor13independentwitnesses'
for x in j['catalogue']:
 if x['id']=='T01':
  x['latestLowerPrintedCaseScope']=summary;x['lowerItemCounts']=dict(manifestPositions=137,positionsRetainedAndViewed=12,positionsStillUnread=125,allSevenJuanBodyPresentEstablished=False,endingLiteral='卷之七終');x['currentEvidence']+=['v53/TUVI_LOWER_PRINTED_CASES_REPORT.md']+['v53/research/tuvi-lower-printed-cases/'+n for n in ['WORK_STATE.json','SOURCE_MANIFEST.json','FIRST_PASS_READINGS.json','VOLUME_NUMBERING_AUDIT.json','MANUAL_PRINTED_CASES.json','TRANSCRIPTION_FREEZE.json','READING_CORRECTIONS.json','RUNTIME_PROOF.json','printed-case-reference.mjs','CROP_VERIFICATION_AUDIT.json']]+['v53/qa/tuvi-lower-printed-cases/REFERENCE_RESULTS.json'];x['localPossession'].append('Tập下cơquanNhậtitem4469314manifest137vịtrí;12vịtríđãgiữ/đọcmốc,13JPEGderivative/0JP2gốc;chưađọchết/ápđủ,cuốiliteral卷之七終.')
wr(p,j)
for name in ['v53/NEXT_STEPS.md','v53/research/library-current/COVERAGE.md','PROJECT_RESEARCH_STATE.md']:
 p=w/name;p.write_text('Mốc28/10/2026 — TUVI_LOWER_PRINTED_CASES_REPORT.md\n\n'+summary+'\n\nTiếp:\n\n'+'\n\n'.join(nexts)+'\n\nCác mốc dưới đây là lịch sử; tập下kết七終khôngđượcép4–6từkỳvọngcũ,38trườngso khôngphảilịchsử/tiênđoánđãchứngminh.\n\n'+p.read_text(encoding='utf-8'),encoding='utf-8')
print(json.dumps(dict(promotedIdentities=len(ident),consumerChanged=False,wholeCatalogueCompleted=False)))
