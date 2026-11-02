import{readFile,writeFile,mkdir}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';
import{createRequire}from'node:module';import assert from'node:assert/strict';import vm from'node:vm';
import{progressionClauses,visibleMotionPattern}from'../research/liuyao-progress-conditions/progression-reference.mjs';
import{sourceStarCoordinates}from'../research/liuyao-progress-conditions/star-coordinate-reference.mjs';
import{compile}from'../research/liuyao-foundations/liuyao-reference.mjs';
const root=resolve(import.meta.dirname,'..'),w=resolve(root,'..'),base=resolve(root,'research/liuyao-progress-conditions'),qa=resolve(root,'qa/liuyao-progress-conditions'),
 archive=resolve(w,'archives/v53-before-liuyao-progress-conditions'),read=async p=>JSON.parse(await readFile(p,'utf8')),
 sha=b=>createHash('sha256').update(b).digest('hex'),checks=[];
function test(name,fn){fn();checks.push({name,ok:true});console.log('PASS',name);}
const manual=await read(resolve(base,'MANUAL_READINGS.json')),spans=await read(resolve(base,'CHAPTER_SPANS.json')),
 units=await read(resolve(base,'B02_CURRENT_UNITS.json')),ops=await read(resolve(base,'OPERATIONAL_CLAUSES.json')),
 fixtures=await read(resolve(base,'PRINTED_FIXTURES.json')),stars=await read(resolve(base,'STAR_COORDINATES.json')),
 pdf=await readFile(resolve(base,manual.sourcePDF));
for(const r of [...manual.records,...manual.qaImages,...manual.additionalTOCAuditReadings])assert.equal(sha(await readFile(resolve(base,r.image))),r.sha256);
test('Reused11089308byte394page source/24readings/8QAimages retainSHA;zeroHTTP ornewPDF',()=>{
 assert.equal(pdf.length,11089308);assert.equal(sha(pdf),'caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa');
 assert.equal(manual.sourceSHA256,sha(pdf));assert.equal(manual.sourcePDFPages,394);assert.equal(manual.newHTTPBodies,0);
 assert.deepEqual(manual.records.map(r=>r.pdfPage),Array.from({length:24},(_,i)=>i+116));assert.equal(manual.qaImages.length,8);
 assert.equal(new Set(manual.qaImages.map(r=>r.pdfPage)).size,7);assert.equal(manual.records.at(-1).scope,'publisher-advertisement-only');
});
test('Five first-pass spans/136units98heading-only31firstpass;duplicate32→printed31 andvolume2end preserved',()=>{
 assert.deepEqual(spans.units.map(u=>[u.id,u.pdfPages[0],u.pdfPages.at(-1)]),[['B02-ch029',116,124],['B02-ch030',124,130],['B02-ch031',130,134],['B02-ch032',134,136],['B02-ch033',136,138]]);
 assert.equal(spans.numberingConflict.bodyPrintedNumberAsRead,31);assert.equal(spans.numberingConflict.TOCNumber,32);
 assert.equal(spans.volumeMappingCorrection.status,'local-map-corrected-after-TOC-and-body-audit-not-a-source-volume-conflict');
 assert.equal(units.units.find(r=>r.id==='B02-ch033').tocVolume,2);
 assert.equal(manual.directEnd.reading,'增刪卜易卷二終');assert.equal(units.currentCounts.registeredUnits,136);
 assert.equal(units.currentCounts.headingOnlyBodyUnits,98);assert.equal(units.currentCounts.firstPassCompleteSpanUnits,31);assert.equal(units.currentCounts.wholeUnitsApplied,0);
 assert.equal(ops.clauses.length,19);assert.equal(ops.eightModesAreNotExclusiveCategories,true);assert.equal(ops.sourceInstructionsAreData,true);
});
const ctx={};ctx.window=ctx;vm.createContext(ctx);const engine=await readFile(resolve(root,'engine.js'));vm.runInContext(engine.toString('utf8'),ctx);
let hhcCalls=0;const printed=[];
test('Two printed cast structures32.5→28 and13.6→49 execute4actualHHC calls;darkmotion isnot anothercastmark',()=>{
 assert.equal(fixtures.fixtures.length,2);
 for(const f of fixtures.fixtures){const p=ctx.HHC_ENGINE.hexNumber(f.values),c=ctx.HHC_ENGINE.hexNumber(f.values.map(v=>v===6?7:v===9?8:v));hhcCalls+=2;
  const r=compile(f.values);assert.equal(p,f.primary);assert.equal(c,f.changed);assert.deepEqual(r.movingLines,f.movingLines);
  for(const s of f.selectedChanges){const l=r.lines[s.line-1];assert.equal(l.branch,s.primaryBranch);assert.equal(l.changed.branch,s.changedBranch);}
  if(f.sourcePrimaryTopBranch){assert.equal(r.lines[5].branch,f.sourcePrimaryTopBranch);assert.equal(r.lines[5].kin,f.sourcePrimaryTopKin);}
  printed.push({id:f.id,pdfPage:f.page,primary:p,changed:c,movingLines:r.movingLines,historicalOutcomeValidated:false});
 }
 assert.deepEqual(fixtures.fixtures[0].additionalSourceDarkMotionNotConvertedToCastMark.line,3);assert.equal(hhcCalls,4);
});
const a=fixtures.fixtures[0].values,c={sourceContext:'B02-ch029',line:5};
test('Unknownsourcepremisesstayunknown inall4advancemodes, no favorabledefault ormissingpriority',()=>{
 const r=progressionClauses(a,c);assert.equal(r.structuralPair,'申酉');assert.equal(r.structuralKind,'advance');
 assert.equal(r.unknownClauseIDs.length,4);assert.equal(r.matchedClauseIDs.length,0);assert.equal(r.effectiveProgression,null);assert.equal(r.predictedDate,null);
 assert.equal(r.sourcePriorityInvented,false);assert.equal(r.laterCommentaryCautionMatched,false);
});
test('Bothweak overlapadvance2/3;bothstrong matchadvance1 withoutassertingmissingvoid/break',()=>{
 const weak=progressionClauses(a,{...c,originalStrength:'休囚',changedStrength:'休囚'}),strong=progressionClauses(a,{...c,originalStrength:'旺相',changedStrength:'旺相'});
 assert.deepEqual(weak.matchedClauseIDs,['advance2','advance3']);assert.equal(weak.exclusiveClassification,false);
 assert.deepEqual(strong.matchedClauseIDs,['advance1']);assert.deepEqual(strong.unknownClauseIDs,['advance4']);
});
test('Near-termexplicitpremise gatesretreat1 even withsupport;unknownstrength isnotinferredfromsupport',()=>{
 const r=[8,7,7,7,9,8],near=progressionClauses(r,{...c,nearTerm:true,hasDayMonthOrMovingSupport:true}),far=progressionClauses(r,{...c,nearTerm:false,hasDayMonthOrMovingSupport:true});
 assert.equal(near.structuralKind,'retreat');assert(near.matchedClauseIDs.includes('retreat1'));assert(!far.matchedClauseIDs.includes('retreat1'));assert.equal(near.assertedPremises.originalStrength,null);
});
test('Latercommentarycaution andlistwaitingcondition canbothmatch;noautomaticoverride orfinalefficacy',()=>{
 const r=progressionClauses(a,{...c,originalAtDayOrMonth:true,changedVoid:true});
 assert(r.matchedClauseIDs.includes('advance4'));assert.equal(r.laterCommentaryCautionMatched,true);assert.equal(r.concurrentListAndLaterCaution,true);
 assert.equal(r.sourcePriorityInvented,false);assert.equal(r.fullChapterReconciliationComplete,false);assert.equal(r.effectiveProgression,null);
 const no=progressionClauses(a,{...c,originalAtDayOrMonth:false,changedVoid:true});assert.equal(no.laterCommentaryCautionMatched,false);
 const unknown=progressionClauses(a,{...c,changedVoid:true});assert.equal(unknown.laterCommentaryCautions[0].result,null);
});
test('False isdistinctfromunknown;staticselectedlinehasnotransformation;strictcontextandinputpreservation',()=>{
 const f=progressionClauses(a,{...c,originalVoid:false,changedVoid:false,originalBroken:false,changedBroken:false});assert.equal(f.clauses[3].result,false);
 assert.equal(progressionClauses([8,7,7,7,8,8],c).structuralKind,null);
 for(const bad of[null,{}, {...c,line:'5'},{...c,originalStrength:'strong'},{...c,changedVoid:1},{...c,monthBranch:'申'},{...c,[Symbol('x')]:1}])assert.throws(()=>progressionClauses(a,bad));
 assert.throws(()=>progressionClauses(a,c,null));const before=a.slice();progressionClauses(a,c);assert.deepEqual(a,before);
});
let patterns=0,uniqueMoving=0,uniqueStationary=0;
test('64motionpatterns yield6unique-moving and6unique-staticpositions,withoutdroppingDụngor inventingdarkmotion',()=>{
 for(let mask=0;mask<64;mask++){const v=Array.from({length:6},(_,i)=>(mask>>i)&1?9:7),r=visibleMotionPattern(v),n=v.filter(x=>x===9).length;
  assert.equal(r.uniqueVisibleMovingLine!==null,n===1);assert.equal(r.uniqueVisibleStationaryLine!==null,n===5);
  assert.equal(r.useGodMayBeDiscarded,false);assert.equal(r.darkMotionDerived,false);if(n===1)uniqueMoving++;if(n===5)uniqueStationary++;patterns++;
 }assert.equal(uniqueMoving,6);assert.equal(uniqueStationary,6);assert.equal(patterns,64);
 assert.throws(()=>visibleMotionPattern(Array(6)));assert.throws(()=>visibleMotionPattern(a,null));
});
test('庚noblemankeepstwoconflicting sourcealternatives;fourunprintedLustemsstaynull',()=>{
 const g=sourceStarCoordinates({dayStem:'庚'});assert.equal(g.nobleman.status,'within-page-conflict');assert.equal(g.nobleman.branches,null);
 assert.deepEqual(g.nobleman.alternatives.map(a=>a.branches),[['午','寅'],['丑','未']]);assert.equal(g.nobleman.effectiveChoice,null);
 for(const s of stars.salary.notExplicitInTheseSixStemLines)assert.equal(sourceStarCoordinates({dayStem:s}).salary.branch,null);
 assert.equal(Object.keys(stars.salary.explicitRows).length,6);
 for(const s of[...'甲乙丙丁戊己辛壬癸'])assert.equal(sourceStarCoordinates({dayStem:s}).nobleman.status,'single-reading-in-retained-source-fields');
});
test('12explicitdaybranchesand4seasonsmaptoretainedhorse/joycoordinateswithoutcalendar orluckscore',()=>{
 for(const row of stars.horse.groups)for(const b of row.dayBranches){const r=sourceStarCoordinates({dayBranch:b});assert.equal(r.horse.branch,row.target);assert.equal(r.calendarAdapter,false);assert.equal(r.positiveScore,null);}
 for(const[s,b]of Object.entries(stars.joy.explicitSeasonRows))assert.equal(sourceStarCoordinates({season:s}).joy.branch,b);
 for(const bad of[{},null,{yearStem:'庚'},{dayStem:1},{dayStem:'甲乙'},{dayBranch:'X'},{season:'summer'},{dayStem:'甲',[Symbol('x')]:1}])assert.throws(()=>sourceStarCoordinates(bad));
 assert.throws(()=>sourceStarCoordinates({dayStem:'甲'},null));
});
test('Editing returnedsource-coordinatearrays cannotchange subsequent source readings orcallerinput',()=>{
 const input={dayStem:'庚',dayBranch:'申'},before=JSON.stringify(input),r=sourceStarCoordinates(input);
 r.nobleman.alternatives[0].branches[0]='X';r.nobleman.alternatives[1].branches.push('X');r.horse.sourceGroup[0]='X';
 const again=sourceStarCoordinates(input);assert.deepEqual(again.nobleman.alternatives.map(a=>a.branches),[['午','寅'],['丑','未']]);
 assert.deepEqual(again.horse.sourceGroup,['申','子','辰']);assert.equal(JSON.stringify(input),before);
});
const req=createRequire(import.meta.url),runtime=await read(resolve(root,'research/bazi-late-zi/VERIFICATION.json'));
for(const r of runtime.runtime)assert.equal(sha(await readFile(resolve(w,r.file))),r.sha256);
const L=req(resolve(w,'v46/node_modules/lunar-typescript'));assert.equal(req(resolve(w,'v46/node_modules/lunar-typescript/package.json')).version,'1.8.6');
const luCases=[];let lunarCalls=0,explicitLuAgreements=0,unfilledLuRows=0;
test('10actualLunarcallscompare6explicitLurootcoordinates;4sourcemissingrowsarenotfilledfromruntime',()=>{
 for(let d=1;d<=10;d++){const l=L.Solar.fromYmdHms(2026,1,d,12,0,0).getLunar(),e=l.getEightChar();e.setSect(2);const day=e.getDay(),lu=l.getDayLu(),r=sourceStarCoordinates({dayStem:day[0]});lunarCalls++;
  if(r.salary.branch!==null){assert(lu.startsWith(r.salary.branch));explicitLuAgreements++;}else unfilledLuRows++;
  luCases.push({noonEnumerationDate:[2026,1,d],day,actualLunarDayLu:lu,sourceSalary:r.salary,historicalDateReconstructed:false});
 }assert.equal(new Set(luCases.map(c=>c.day[0])).size,10);assert.equal(explicitLuAgreements,6);assert.equal(unfilledLuRows,4);
});
const old=await read(resolve(archive,'PACKAGE_MANIFEST.json')),html=await readFile(resolve(root,'Huyen_Hoc_Cac.html')),
 refs=old.files.filter(f=>/research\/liuyao-[^/]+\/.*reference\.mjs$/.test(f.file));
for(const f of refs)assert.equal(sha(await readFile(resolve(root,f.file))),f.sha256);
test('707411byteconsumer/15priorreferencesunchanged;privateconditionsandstarconflictsabsentfromsite',()=>{
 assert.equal(refs.length,15);assert.equal(html.length,707411);assert.equal(sha(html),old.product.sha256);
 for(const t of['progression-reference.mjs','STAR_COORDINATES.json','liuyao-progress-conditions'])assert.equal(html.includes(Buffer.from(t)),false);
});
await mkdir(qa,{recursive:true});const cases={date:'2026-10-27',printed,luCases,
 representativeLayerConflict:progressionClauses(a,{...c,originalAtDayOrMonth:true,changedVoid:true}),
 gengSourceConflict:sourceStarCoordinates({dayStem:'庚'}),historicalOutcomesValidated:false};
await writeFile(resolve(qa,'SOURCE_CASE_RESULTS.json'),JSON.stringify(cases,null,2)+'\n');
const summary={actualHHCHexCalls:hhcCalls,printedCastFixtures:2,actualLunarCalls:lunarCalls,explicitLuAgreements,unfilledLuRows,
 motionPatterns:patterns,uniqueMovingPatterns:uniqueMoving,uniqueStationaryPatterns:uniqueStationary,
 manualRecords:24,firstPassChapterSpans:5,boundedClauses:19,QAOnlySourceRenders:7,QAImages:8,
 B02RegisteredUnits:136,B02HeadingOnlyBodyUnits:98,B02FirstPassUnits:31};
await writeFile(resolve(qa,'ENGINE_RESULTS.json'),JSON.stringify({date:'2026-10-27',checks,summary,engineSHA256:sha(engine),htmlSHA256:sha(html),
 caseDigest:sha(Buffer.from(JSON.stringify(cases))),consumerChanged:false,wholeBookApplied:false,wholeCatalogueCompleted:false},null,2)+'\n');
console.log(JSON.stringify({checks:checks.length,...summary}));
