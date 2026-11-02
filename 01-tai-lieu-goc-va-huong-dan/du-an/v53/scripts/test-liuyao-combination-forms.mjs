import{readFile,writeFile}from'node:fs/promises';import{createHash}from'node:crypto';import vm from'node:vm';import assert from'node:assert/strict';import{combinationForms as inspect}from'../research/liuyao-combination-context/combination-forms-reference.mjs';
const s=new URL('../research/liuyao-combination-context/',import.meta.url),sha=x=>createHash('sha256').update(x).digest('hex'),checks=[];async function check(name,fn){await fn();checks.push({name,ok:true});}
let calls=0;
await check('Namedsource74Qian-to-TaiandLu-to-Biexecute4actualHHCcalls;derived6/7/8/9encodingsarenotclaimeddirectprintedmovingglyphs',async()=>{
 const c={};c.window=c;vm.createContext(c);vm.runInContext((await readFile(new URL('../../engine.js',s),'utf8')),c);
 for(const[v,a,b]of[[[7,7,7,9,9,9],1,11],[[6,8,7,9,8,7],56,22]]){
  assert.equal(c.HHC_ENGINE.hexNumber(v),a);calls++;assert.equal(c.HHC_ENGINE.hexNumber(v.map(x=>x===9?8:x===6?7:x)),b);calls++;const x=inspect(v);assert.equal(x.chart.primary.number,a);assert.equal(x.changedChartNumber,b);
 }
});
await check('All6namedformsareidentifiedwithseparatelayers;Qian-toTaiisclash-to-combinationandLu-toBiiscombination-to-combination',()=>{
 const a=inspect([7,7,7,9,9,9]),b=inspect([6,8,7,9,8,7]);assert(a.forms[4].coordinatePresent);assert(!a.forms[5].coordinatePresent);assert(b.forms[5].coordinatePresent);assert(!b.forms[4].coordinatePresent);assert(b.forms[3].coordinatePresent);assert.equal(a.forms.length,6);
 const nochange=inspect([8,8,7,7,8,7]);assert(nochange.primarySixCombination);assert(!nochange.forms[5].coordinatePresent);
});
await check('Staticcalendarpairislabelled合起,movingcalendarpair合絆;two-movingpair合好isnotinferredfromone-stationarypair',()=>{
 const a=inspect([7,7,7,7,7,7],{monthBranch:'未'}),b=inspect([7,7,7,9,7,7],{monthBranch:'未'});assert.equal(a.calendarPairs.find(x=>x.line===4).sourceLabel,'合起');assert.equal(b.calendarPairs.find(x=>x.line===4).sourceLabel,'合絆');
 const both=inspect([6,8,8,9,7,7]),one=inspect([8,8,8,9,7,7]);assert(both.movingPairs.some(x=>x.lines.join(',')==='1,4'));assert(!one.movingPairs.some(x=>x.lines.join(',')==='1,4'));assert(one.staticRaisedCoordinates.some(x=>x.staticLine===1&&x.movingLine===4));
});
await check('Ownchangedpairsource74化扶staysseparatefromdeclaredsource51貪合hold;rawpairdoesnotautomaticallyapplyeither',()=>{
 const a=inspect([7,7,7,9,7,7]);assert.deepEqual(a.ownChangedPairs.map(x=>[x.line,x.originalBranch,x.changedBranch,x.sourceLabelPDF74]),[[4,'午','未','化扶']]);assert.equal(a.ownChangedPairs[0].appliedSupport,null);assert.equal(a.ownChangedPairs[0].appliedHold,null);assert.equal(a.automaticHold,null);assert.equal(a.functionalCombination,null);assert.equal(a.practicalOutcome,null);
});
await check('Unknowncalendarcontextandunsupportedmetadataremainexplicit;noGregorianortriadadapteroroutcomefromsixpairpresence',()=>{
 const a=inspect([7,7,7,9,7,7]);assert.equal(a.calendarPairs.length,0);assert.equal(a.releaseDate,null);assert.equal(a.transformationElement,null);assert.equal(a.useLine,null);assert(!a.sourceOutcomeValidated);assert(!a.consumerApplied);
 for(const c of[{monthBranch:'己'},{dayBranch:'子丑'},{dayBranch:null},{date:'2026-10-28'},Object.create({dayBranch:'未'}),{[Symbol('hidden')]:true}])assert.throws(()=>inspect([7,7,7,7,7,7],c));
});
const out={date:'2026-10-28',checks,summary:{actualHHCHexCallsForNamedFigureProjections:calls,namedSourceFigures:2,namedCombinationForms:6,directPrintedMovingGlyphFixtures:0,source74PositiveLabelVs51ExceptionRetained:true,newHTTPRequests:0,newSourcePositions:0,fullFunctionalHoldClassifier:false,consumerChanged:false,wholeCatalogueCompleted:false}};await writeFile(new URL('../../qa/liuyao-combination-context/COMBINATION_RESULTS.json',s),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out));
