import{readFile,writeFile}from'node:fs/promises';import{createHash}from'node:crypto';import vm from'node:vm';import assert from'node:assert/strict';
import{readMotion}from'./motion-reference.mjs';import{inspectPrintedDiagram}from'./diagram-reference.mjs';
const s=new URL('./',import.meta.url),read=async n=>JSON.parse(await readFile(new URL(n,s),'utf8')),sha=x=>createHash('sha256').update(x).digest('hex'),checks=[];
async function check(name,fn){await fn();checks.push({name,ok:true});}
await check('28retainedsourcepositionsand7exactspans;137firstpassunitsdoesnotmeanwholeapplication',async()=>{
 const m=await read('SOURCE_MANIFEST.json'),spans=(await read('MANUAL_READINGS.json')).chapterRanges,u=await read('B02_CURRENT_UNITS.json');
 assert.equal(sha(await readFile(new URL('../../'+m.sourcePDF,s))),m.sourceSHA256);assert.deepEqual(m.records.map(x=>x.pdfPage),Array.from({length:28},(_,i)=>21+i));
 for(const x of m.records){assert(x.actuallyViewed);assert.equal(sha(await readFile(new URL('../../'+x.file,s))),x.sha256);}
 assert.deepEqual(spans.map(x=>[x.printedNumber,x.firstPDFPosition,x.lastPDFPosition]),[[1,21,21],[2,21,24],[3,24,45],[4,45,46],[5,46,47],[6,47,47],[7,47,48]]);
 assert.equal(u.currentCounts.firstPassCompleteSpanUnits,137);assert.equal(u.currentCounts.partialFoundationUnits,0);assert(u.units.every(x=>!x.entireUnitApplied));assert.equal(m.newHTTPRequests,0);
});
await check('64actualHHCstaticidentitiesand384manualrowsretain3sourcecellsand32explicitbranchglyphnormalizations',async()=>{
 const a=await read('DIAGRAM_COMPARISON.json'),b=await readFile(new URL('PRINTED_DIAGRAMS.json',s));assert.equal(sha(b),a.sourceRowsSHA256);assert.equal(a.actualHHCHexCalls,64);assert.equal(a.printedLineRows,384);assert.equal(a.workingBranchNormalizations,32);
 assert.deepEqual(a.differences.map(x=>[x.number,x.line,x.field,x.source,x.reference]),[[20,3,'element','土','木'],[61,2,'kin','兄弟','官鬼'],[5,1,'kin','父母','妻財']]);
 assert.equal(a.records.length,64);assert.equal(new Set(a.records.map(x=>x.identity.actualHHCNumber)).size,64);
 for(const x of a.records){assert.equal(x.identity.sourceNumber,x.identity.actualHHCNumber);assert.equal(x.identity.sourceNumber,x.identity.privateNumber);assert.equal(x.identity.sourcePalace,x.identity.privatePalace);assert.equal(x.identity.sourceShi,x.identity.privateShi);assert.equal(x.identity.sourceYing,x.identity.privateYing);}
});
await check('SourcecomparisonAPIpreservesliteralsinstead ofsilentlyrewriting3anomaliesanddoesnotleakmutablecatalogue',()=>{
 const a=inspectPrintedDiagram(20),b=inspectPrintedDiagram(61),c=inspectPrintedDiagram(5);
 assert.deepEqual(a.differences,[{line:3,field:'element',literal:'土',computed:'木'}]);assert.deepEqual(b.differences,[{line:2,field:'kin',literal:'兄弟',computed:'官鬼'}]);assert.deepEqual(c.differences,[{line:1,field:'kin',literal:'父母',computed:'妻財'}]);
 assert.equal(c.lines.find(x=>x.line===1).printed.kin,'父母');assert.equal(c.lines.find(x=>x.line===1).computed.kin,'妻財');c.literal.kinAbbreviations='XXXXXX';assert.equal(inspectPrintedDiagram(5).literal.kinAbbreviations,'妻兄子兄官父');
 assert.equal(inspectPrintedDiagram(1).differences.length,0);assert.equal(a.sourceEmended,false);assert.equal(a.consumerApplied,false);assert.equal(a.practicalOutcome,null);
 for(const bad of[null,undefined,0,65,1.5,'20',NaN])assert.throws(()=>inspectPrintedDiagram(bad));
});
let trigramCases=0;
await check('FourprintedTHREElineexamplesremaintrigrams;allthreeKunlinesmovingisnotonlythirdline orfullsixlineQian',async()=>{
 const fixtures=(await read('MOTION_FIXTURES.json')).threeLineExamples;
 for(const f of fixtures){const x=readMotion(f.values,{width:3});assert.equal(x.original.trigram,f.primary);assert.equal(x.changed.trigram,f.changed);assert.equal(x.sixLineChart,null);assert.equal(x.hexagramNumber,null);assert.equal(x.companionTrigram,null);assert.equal(x.practicalOutcome,null);trigramCases++;}
 assert.deepEqual(readMotion([6,6,6],{width:3}).movingLines,[1,2,3]);assert.deepEqual(readMotion([8,8,6],{width:3}).changed.bits,[0,0,1]);assert.equal(readMotion([8,8,6],{width:3}).changed.trigram,'艮');
});
let actualHHCNewCalls=0;
await check('Printed48XutoSongexecutes2actualHHCcallsandmatches6baselabelsplus4changedlabelsunderoriginalKunpalace;table33Father isnotcopied',async()=>{
 const f=(await read('MOTION_FIXTURES.json')).sixLineExample,c={};c.window=c;vm.createContext(c);const code=await readFile(new URL('../../v53/engine.js',s));assert.equal(sha(code),'39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6');vm.runInContext(code.toString(),c);
 const x=readMotion(f.values,{width:6}).sixLineChart;assert.equal(c.HHC_ENGINE.hexNumber(f.values),5);actualHHCNewCalls++;assert.equal(c.HHC_ENGINE.hexNumber(f.values.map(v=>v===6?7:v===9?8:v)),6);actualHHCNewCalls++;
 assert.equal(x.primary.palace,'坤');assert.equal(x.changed.ownPalaceDiagnostic,'離');assert.deepEqual(x.movingLines,[1,3,4,6]);assert.deepEqual(x.lines.map(l=>[l.branch,l.kin]),f.primaryBranchKinBottomToTop);assert.deepEqual(x.lines.filter(l=>l.moving).map(l=>({line:l.line,branch:l.changed.branch,kin:l.changed.kin})),f.changedBranchKin);
 assert.equal(x.lines[0].kin,'妻財');assert.equal(inspectPrintedDiagram(5).lines.find(l=>l.line===1).printed.kin,'父母');assert(x.lines.filter(l=>l.moving).every(l=>l.changed.kinBasisPalace==='坤'));
});
await check('Explicitwidthandsixlinearityrequired;missing,sparse,string,symbol,extrafieldandprototypeinputsrejected',()=>{
 for(const bad of[undefined,null,{},[],{width:4},{width:'3'},{width:3,companion:0},{width:3,[Symbol('hidden')]:true},Object.create({width:3})])assert.throws(()=>readMotion([7,7,7],bad));
 for(const bad of[[7,7],Array(3),[7,7,undefined],['7',7,7],[NaN,7,7],new Uint8Array([7,7,7]),[7,7,7,7,7,7]])assert.throws(()=>readMotion(bad,{width:3}));assert.throws(()=>readMotion([7,7,7],{width:6}));
});
await check('Outlinequalificationandcalendarmissingpremisesareexplicit;firstpassreadingdoesnotauthorizesimplifiedcategoricaloutcomes',async()=>{
 const a=await read('FOUNDATIONAL_CONTEXTS.json');assert.equal(a.clauses.length,27);assert(a.clauses.find(x=>x.topic==='qualification').workingSourceAnchor.includes('不可以此為法'));assert(a.clauses.find(x=>x.topic==='progressive-outline').workingSourceAnchor.includes('後卷各章'));assert.equal(a.sourceOutcomesValidated,false);assert.equal(a.consumerApplied,false);assert(a.missingPremises.includes('effective-strength'));
});
const out={date:'2026-10-28',checks,summary:{retainedPositionsReviewed:28,newSourcePositions:0,firstPassSpansAdded:7,firstPassUnitsCurrent:137,wholeUnitsApplied:0,printedDiagrams:64,sourceLineRows:384,actualHHCHexCallsFromDiagramAudit:64,actualHHCHexCallsForInheritedMovingFixtureThroughNewReader:actualHHCNewCalls,totalActualHHCHexCallsThisScope:64+actualHHCNewCalls,printedMovingFixturesNewlyCollatedThisScope:1,independentNewPrintedCasts:0,priorCast48ReexecutedForNewReader:true,sourceChangedLabels:4,trigramExamples:trigramCases,sourceMismatchingCellsRetained:3,explicitBranchGlyphNormalizations:32,boundedContextGroups:27,newHTTPRequests:0,newOriginalContainers:0,consumerChanged:false,wholeCatalogueCompleted:false}};
await writeFile(new URL('RESULTS.json',s),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out));
