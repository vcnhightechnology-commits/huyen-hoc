import{readFile,writeFile}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';import vm from'node:vm';import assert from'node:assert/strict';
import{lifeSourceContext as inspect}from'../research/liuyao-life-context/life-context-reference.mjs';import{catalogue}from'../research/liuyao-foundations/liuyao-reference.mjs';
const r=resolve(import.meta.dirname,'..'),w=resolve(r,'..'),b=resolve(r,'research/liuyao-life-context'),q=resolve(r,'qa/liuyao-life-context'),read=async p=>JSON.parse(await readFile(p,'utf8')),sha=x=>createHash('sha256').update(x).digest('hex'),checks=[];
async function check(name,fn){await fn();checks.push({name,ok:true});}
const source=await read(resolve(b,'SOURCE_MANIFEST.json')),methods=(await read(resolve(b,'SOURCE_CONTEXTS.json'))).methods,fixture=(await read(resolve(b,'PRINTED_FIXTURES.json'))).fixtures[0];
await check('Source PDF and20 directly viewed source positions match retained identities without redownloading',async()=>{
 assert.equal(sha(await readFile(resolve(w,source.sourcePDF))),source.sourceSHA256);assert.equal(source.images.length,20);
 for(const x of source.images){assert(x.actuallyViewed);assert.equal(sha(await readFile(resolve(w,x.file))),x.sha256);}
 assert.equal(source.images.filter(x=>x.newlyRenderedThisStage).length,12);assert.equal(source.images.filter(x=>x.previouslyRenderedButUnread).length,7);
});
let hhcCalls=0;const c={};c.window=c;vm.createContext(c);vm.runInContext(await readFile(resolve(r,'engine.js'),'utf8'),c);
await check('復→頤 printedcase executes two actual HHC calls and matches six independent kin/branch readings and top酉→寅',()=>{
 assert.equal(c.HHC_ENGINE.hexNumber(fixture.valuesBottomToTop),24);hhcCalls++;
 assert.equal(c.HHC_ENGINE.hexNumber(fixture.valuesBottomToTop.map(v=>v===6?7:v===9?8:v)),27);hhcCalls++;
 const out=inspect(fixture.valuesBottomToTop,{system:methods[0].id,subject:'self'});
 assert.deepEqual(out.chart.lines.map(x=>({branch:x.branch,kin:x.kin})),fixture.sourceBaseLabelsBottomToTop);
 assert.deepEqual(out.chart.movingLines,[6]);assert.equal(out.chart.lines[5].changed.branch,'寅');assert.equal(out.selfLine,1);
 assert.equal(out.chart.lines[5].kin,'子孫');assert.equal(out.chart.lines[5].changed.kin,'官鬼');
});
await check('Wealth/self/blessing and office/writing source actors remain separate, with derived edges rather than outcome priority',()=>{
 const v=fixture.valuesBottomToTop,a=inspect(v,{system:methods[0].id,subject:'self'}),b=inspect(v,{system:methods[1].id,subject:'self'});
 assert.deepEqual(a.groups.map(x=>[x.id,x.originalLines]),[['wealth',[1,5]],['blessing',[6]]]);
 assert.deepEqual(a.edges.map(x=>[x.fromLine,x.toLine,x.relation]),[[6,1,'generates'],[6,5,'generates']]);
 assert.deepEqual(b.groups.map(x=>[x.id,x.originalLines,x.changedLines]),[['office',[2],[6]],['writing',[],[]]]);
 assert(a.nodes.filter(x=>!x.visibleMoving).every(x=>x.active===null));assert.equal(a.nodes.find(x=>x.line===6).active,true);
 assert.equal(a.ownChanges[0].effectiveReturnRelation,null);
});
let contexts=0,edges=0,ownChanges=0,groupEntries=0;
await check('8192 explicit figure/motion/source contexts preserve candidate identities, no self-loops, unknown static activity and unselected use-line',()=>{
 for(const h of catalogue())for(let mask=0;mask<64;mask++){
  const values=h.bits.map((bit,i)=>(mask>>i)&1?(bit?9:6):(bit?7:8));
  for(const method of methods){
   const out=inspect(values,{system:method.id,subject:'self'});assert.equal(out.selfLine,h.shi);
   assert.equal(new Set(out.nodes.map(x=>x.line)).size,out.nodes.length);
   for(const g of out.groups){assert.deepEqual(g.originalLines,out.chart.lines.filter(x=>x.kin===g.kin).map(x=>x.line));assert.deepEqual(g.changedLines,out.chart.lines.filter(x=>x.changed?.kin===g.kin).map(x=>x.line));groupEntries++;}
   for(const e of out.edges){assert.notEqual(e.fromLine,e.toLine);assert.equal(e.effectiveRelation,null);assert.equal(e.priority,null);edges++;}
   for(const n of out.nodes){assert.equal(n.active,n.visibleMoving?true:null);assert.equal(n.hasQi,null);}
   assert.equal(out.ownChanges.length,out.chart.movingLines.length);ownChanges+=out.ownChanges.length;
   for(const k of['useLineSelected','selfHasQi','wealthHasQi','blessingHasQi','careerResult','financialResult','healthResult','lifespan'])assert.equal(out[k],null);
   assert.equal(out.datePremisesApplied,false);contexts++;
  }
 }assert.equal(contexts,8192);
});
await check('Explicit source/subject required; no free-text, other-person or longevity inference and no mutation of inputs or source groups',()=>{
 const v=fixture.valuesBottomToTop.slice(),before=v.slice(),base={system:methods[0].id,subject:'self'};
 for(const x of[undefined,null,[],{}, {...base,subject:undefined},{...base,subject:'spouse'},{...base,system:'longevity'},{...base,question:'Will I be rich?'},{...base,calendar:'today'},{...base,[Symbol('x')]:true}])assert.throws(()=>inspect(v,x),TypeError);
 for(const x of[[],Array(6),[7,7,7,7,7,'6']])assert.throws(()=>inspect(x,base),TypeError);
 const a=inspect(v,base);a.groups[0].originalLines.push(99);a.separateQuestionCategories.length=0;
 assert.deepEqual(inspect(v,base).groups[0].originalLines,[1,5]);assert.equal(inspect(v,base).separateQuestionCategories.length,7);assert.deepEqual(v,before);
});
await check('Three further chapterspans have first readings, shared boundary pages and an explicit partial39; zero whole-applied units',async()=>{
 const map=await read(resolve(b,'B02_CURRENT_UNITS.json')),manual=await read(resolve(b,'MANUAL_READINGS.json'));
 assert.deepEqual(map.currentCounts,{registeredUnits:136,regularNumberedUnits:130,supplements:6,headingOnlyBodyUnits:92,partialFoundationUnits:7,otherPartialUnits:1,firstPassCompleteSpanUnits:36,wholeUnitsApplied:0});
 assert.equal(map.units.filter(x=>x.disposition==='heading-only-body-extraction-open').length,92);
 for(const [number,range]of[[36,[213,214]],[37,[214,229]],[38,[229,232]]]){const u=map.units.find(x=>x.id===`B02-ch${number}`.replace('ch','ch0'));assert.equal(u.bodyPDFPages[0],range[0]);assert.equal(u.bodyPDFPages.at(-1),range[1]);assert.equal(u.entireUnitApplied,false);}
 assert.equal(manual.chapterRanges['39'].wholeFirstPassRead,false);assert.equal((await read(resolve(b,'BOUNDED_CLAUSES.json'))).clauses.length,20);
});
await check('Public engine, directions, calendar, fortune and HTML are unchanged from the last fully verified package',async()=>{
 const old=await read(resolve(w,'archives/v53-before-liuyao-life-context/PACKAGE_MANIFEST.json'));
 for(const f of['engine.js','app.js','content.js','fortune.js','Huyen_Hoc_Cac.html','site/index.html'])assert.equal(sha(await readFile(resolve(r,f))),old.files.find(x=>x.file===f).sha256);
});
const out={date:'2026-10-27',checks,summary:{actualHHCHexCalls:hhcCalls,printedCastFixtures:1,sourceKinBranchLabels:6,namedStructuralContexts:2,separateSourceQuestionCategories:7,privateMotionContexts:contexts,derivedEdgeContexts:edges,ownChangeContexts:ownChanges,roleGroupQueries:groupEntries,
 boundedClauses:20,viewedSourcePositions:20,newSourceReadPositions:19,expandedPriorReadPositions:1,newRenderedAndReadPositions:12,previousRenderedNowReadPositions:7,completeFirstPassChapterSpans:3,newHTTPRequests:0,newOriginalContainers:0},
 consumerChanged:false,wholeChaptersApplied:false,sourceOutcomesValidated:false,lifespanOrClinicalClassifier:false,wholeCatalogueCompleted:false};
await writeFile(resolve(q,'RESULTS.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({checks:checks.length,...out.summary}));
