import{readFile,writeFile}from'node:fs/promises';import{createHash}from'node:crypto';import vm from'node:vm';import assert from'node:assert/strict';import{inspectOriginSupport as inspect}from'../research/liuyao-combination-context/origin-support-reference.mjs';
const s=new URL('../research/liuyao-combination-context/',import.meta.url),read=async n=>JSON.parse(await readFile(new URL(n,s),'utf8')),sha=x=>createHash('sha256').update(x).digest('hex'),checks=[];async function check(name,fn){await fn();checks.push({name,ok:true});}
const fixtures=await read('../liuyao-use-god/SOURCE_FIXTURES.json'),f=fixtures.cases.find(x=>x.id==='qian-coactive-chain'),v=f.values,premises={strong:true,opposingActive:true,useHasQi:true};
await check('Retainedsource51andtwo nativecrops preserveexactsourcebytes/pixels;inheritedcastnotcountedasnewsourceexample',async()=>{
 const m=await read('SOURCE_MANIFEST.json');assert.equal(m.newHTTPRequests,0);assert.equal(m.newSourcePositions,0);assert.equal(m.inheritedPrintedCast,true);assert.equal(m.independentNewPrintedCasts,0);
 for(const x of m.images)assert.equal(sha(await readFile(new URL('../../../'+x.file,s))),x.sha256);
 assert(m.exception.workingSourceAnchor.includes('午火貪合不能生辰土'));assert.equal(m.sourceOutcomesValidated,false);
});
let actualHHC=0;
await check('Source1to9reexecutes2actualHHCcallsfornewexceptionprojection;originalroot/sourceclinicaloutcomeisnotvalidated',async()=>{
 const code=await readFile(new URL('../../engine.js',s));assert.equal(sha(code),'39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6');const c={};c.window=c;vm.createContext(c);vm.runInContext(code.toString(),c);
 assert.equal(c.HHC_ENGINE.hexNumber(v),1);actualHHC++;assert.equal(c.HHC_ENGINE.hexNumber(v.map(x=>x===9?8:x===6?7:x)),9);actualHHC++;
 const x=inspect(v,3,4,{premises,changedCombinationHold:true});assert.equal(x.conditions.actorRole,'元神');assert.equal(x.conditions.graph.nodes[3].branch,'午');assert.equal(x.changedBranch,'未');assert.equal(x.clinicalOutcome,null);
});
await check('M4coactivityandM1strongclausescanmatchwhiletheexplicitdeclaredsource51combinationholdblocksunconditionalsupport',()=>{
 const x=inspect(v,3,4,{premises,changedCombinationHold:true});assert(x.matchedEffectiveClausesBeforeCaveat.includes('M1'));assert(x.matchedEffectiveClausesBeforeCaveat.includes('M4'));assert.equal(x.source51Blocker,true);assert.equal(x.unconditionalSupportClaimAllowed,false);assert.equal(x.supportVerdict,null);assert.equal(x.practicalOutcome,null);
});
await check('Rawown-changedcombinationdoesnotitselfestablishahold;falseholdandmissingrootalsodonotassertsupport',()=>{
 const unknown=inspect(v,3,4,{premises}),declaredFree=inspect(v,3,4,{premises,changedCombinationHold:false});assert(unknown.ownChangedCombination);assert.equal(unknown.source51Blocker,null);assert.equal(unknown.unconditionalSupportClaimAllowed,null);assert.equal(declaredFree.source51Blocker,false);assert.equal(declaredFree.supportVerdict,null);
 const noRoot=inspect(v,3,4,{changedCombinationHold:false});assert.equal(noRoot.conditions.useHasQi,null);assert.equal(noRoot.supportVerdict,null);assert.equal(noRoot.overallStrength,null);assert.equal(noRoot.releaseFromHold,null);
});
await check('Staticorunpairedoriginandnon-originrolescannotacceptafabricatedheld-changedpremise',()=>{
 assert.throws(()=>inspect([7,7,7,7,7,7],3,4,{changedCombinationHold:true}));
 assert.throws(()=>inspect(v,3,2,{changedCombinationHold:true}));assert.throws(()=>inspect(v,3,4,{changedCombinationHold:'true'}));assert.throws(()=>inspect(v,3,4,{changedCombinationHold:0}));
 for(const bad of[null,[],{outcome:true},{premises:Object.create({strong:true})},{[Symbol('hidden')]:true}])assert.throws(()=>inspect(v,3,4,bad));
});
const out={date:'2026-10-28',checks,summary:{sourcePositionsReviewed:5,newSourcePositions:0,newHTTPRequests:0,inheritedPrintedCasts:1,independentNewPrintedCasts:0,actualHHCHexCallsForNewExceptionProjection:actualHHC,sourceExceptionProjections:1,sourceOutcomeValidation:false,consumerChanged:false,wholeCatalogueCompleted:false}};await writeFile(new URL('../../qa/liuyao-combination-context/RESULTS.json',s),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out));
