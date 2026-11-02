import{readFile,writeFile}from'node:fs/promises';import{createHash}from'node:crypto';import vm from'node:vm';import assert from'node:assert/strict';import{triadContexts as inspect}from'./triad-context-reference.mjs';
const s=new URL('./',import.meta.url),checks=[];async function check(name,fn){await fn();checks.push({name,ok:true});}let calls=0;
const values=[9,8,9,9,8,9],dark=Object.fromEntries([1,2,3,4,5,6].map(n=>[n,false]));
await check('Printed79LitoKunexecutes2actualHHCcallsandretains4movingglyphs6baseand4changedbranchkinlabels',async()=>{
 const fixture=JSON.parse(await readFile(new URL('TRIAD_FIXTURE.json',s),'utf8')),code=await readFile(new URL('../../v53/engine.js',s));assert.equal(createHash('sha256').update(code).digest('hex'),'39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6');const c={};c.window=c;vm.createContext(c);vm.runInContext(code.toString(),c);
 assert.equal(c.HHC_ENGINE.hexNumber(values),30);calls++;assert.equal(c.HHC_ENGINE.hexNumber(values.map(v=>v===9?8:v)),2);calls++;
 const chart=inspect(values).chart;assert.deepEqual(chart.movingLines,[1,3,4,6]);assert.deepEqual(chart.lines.map(l=>[l.branch,l.kin]),fixture.primaryBranchKinBottomToTop);assert.deepEqual(chart.lines.filter(l=>l.moving).map(l=>[l.line,l.changed.branch,l.changed.kin]),fixture.changedBranchKin);assert.equal(chart.primary.shi,6);assert.equal(chart.primary.ying,3);
});
await check('Source79innerWoodandouterMetalwitnessesuseonlytheirmovingendpointpoolsandneitherimplyactualvillagesorpropertyoutcome',()=>{
 const x=inspect(values,{darkMovementByLine:dark}),wood=x.groups.find(g=>g.id==='wood'),metal=x.groups.find(g=>g.id==='metal');
 const inside=wood.sides.find(x=>x.side==='inner'),outside=metal.sides.find(x=>x.side==='outer');assert(inside.coordinateCandidatePresent);assert(outside.coordinateCandidatePresent);
 assert(inside.candidateWitnesses.every(w=>w.nodes.every(n=>[1,3].includes(n.line))));assert(outside.candidateWitnesses.every(w=>w.nodes.every(n=>[4,6].includes(n.line))));assert(inside.candidateWitnesses.every(w=>new Set(w.nodes.map(n=>n.branch)).size===3));
 assert.equal(x.sourceInnerOuterOutcome,null);assert.equal(x.practicalOutcome,null);assert(x.mixedAllSixLinePoolNotUsed);
});
await check('Source78literal一爻firstmodeiskeptunadjudicated;B03atleasttwogateisnotimportedintoB02',()=>{
 const x=inspect(values);assert.equal(x.firstModeLiteral,'一卦之內有一爻動而合局者一也');assert.equal(x.firstModeCountInterpretation,null);assert(x.firstModeNotSilentlyEmended);for(const g of x.groups)for(const w of g.primaryWitnesses)assert.equal(w.sourceMode1Adjudication,null);
});
await check('Exactlytwoknownactiveandoneinactiveprimarymembersisdistinctfrommissingdarkactivityorallthreeactive',()=>{
 // PureKun has亥5/卯3/未1. Choose5and1moving;3is static.
 const two=[6,8,8,8,6,8],known=inspect(two,{darkMovementByLine:dark}),unknown=inspect(two),allthree=inspect([6,8,6,8,6,8],{darkMovementByLine:dark});
 assert(known.groups.find(g=>g.id==='wood').primaryWitnesses.some(w=>w.sourceMode2TwoActiveOneInactive===true));assert(unknown.groups.find(g=>g.id==='wood').primaryWitnesses.some(w=>w.sourceMode2TwoActiveOneInactive===null));assert(allthree.groups.find(g=>g.id==='wood').primaryWitnesses.every(w=>w.sourceMode2TwoActiveOneInactive===false));
});
await check('Voidbreakandtombpremisesdelaycandidatecompletionwithoutinventingadateorusingnominalcandidateasformedgroup',()=>{
 const a=inspect(values,{voidOrMonthBrokenByNode:{p3:true}}),w=a.groups.find(g=>g.id==='wood').sides.find(x=>x.side==='inner').candidateWitnesses.find(w=>w.nodes.some(n=>n.node==='p3'));assert(w);assert.equal(w.sourceCompletionDeferred,true);assert.equal(w.sourceFillOrOpenDate,null);assert.equal(w.effectiveFormation,null);
 const b=inspect(values,{tombByNode:{c4:true}});assert(b.groups.find(g=>g.id==='metal').sides.find(x=>x.side==='outer').candidateWitnesses.some(w=>w.tombPresent===true&&w.sourceCompletionDeferred===true));
 const c=inspect(values);for(const g of c.groups)for(const side of g.sides)for(const q of side.candidateWitnesses)assert.equal(q.sourceCompletionDeferred,null);
});
await check('Stationaryendpoints,crosslayerfabrication,duplicatebranchcompletion,wrongnodepredicatesandimplicitcalendarcontextareblocked',()=>{
 const x=inspect([7,8,7,7,8,7]);assert(x.groups.every(g=>g.sides.every(s=>!s.coordinateCandidatePresent)));const q=inspect([7,7,7,7,7,7]);assert(q.groups.find(g=>g.id==='wood').primaryWitnesses.length===0);
 for(const c of[{dayBranch:'未'},{tombByNode:{c2:true}},{voidOrMonthBrokenByNode:{p8:true}},{darkMovementByLine:{1:true}},Object.create({darkMovementByLine:{1:true}})])assert.throws(()=>inspect(values,c));assert.throws(()=>inspect(values,{darkMovementByLine:{2:'true'}}));
});
const out={date:'2026-10-28',checks,summary:{actualHHCHexCallsForPrinted79:calls,printedCastNewlyCollatedThisScope:1,newSourcePositions:0,sourcePrimaryLabels:6,sourceChangedLabels:4,triadNamedGroups:4,sourceModesRecorded:4,firstModeAdjudicated:false,sourceInnerOuterGroups:2,fullFunctionalFormation:false,consumerChanged:false,wholeCatalogueCompleted:false}};await writeFile(new URL('TRIAD_RESULTS.json',s),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out));
