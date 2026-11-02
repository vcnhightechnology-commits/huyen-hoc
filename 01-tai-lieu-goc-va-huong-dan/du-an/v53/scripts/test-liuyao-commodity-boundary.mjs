import{readFile,writeFile}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';import vm from'node:vm';import assert from'node:assert/strict';
import{explicitCommodityBoundary as inspect}from'../research/liuyao-commodity-boundary/commodity-boundary.mjs';
const w=process.cwd(),r=resolve(w,'v53'),b=resolve(r,'research/liuyao-commodity-boundary'),q=resolve(r,'qa/liuyao-commodity-boundary'),read=async p=>JSON.parse(await readFile(p,'utf8')),sha=x=>createHash('sha256').update(x).digest('hex'),checks=[];
async function check(name,fn){await fn();checks.push({name,ok:true});}
const source=await read(resolve(b,'COMMODITY_BOUNDARY.json')),fixture=source.figureFixture,values=fixture.valuesBottomToTop,ctx=commodityLabel=>({system:source.system,commodityLabel});
await check('24 inspected source positions,retainedTOC17 reread and2 high-resolution commodity images preserve recorded bytes;no newHTTP/container',async()=>{
 const local=await read(resolve(b,'LOCAL_RENDERS.json')),toc=await read(resolve(b,'TOC_QA.json')),qa=await read(resolve(b,'QA_RENDERS.json'));
 assert.equal(sha(await readFile(resolve(w,local.sourcePDF))),local.sourceSHA256);assert.equal(local.records.length,24);assert(local.records.every(x=>x.actuallyViewed));assert(toc.actuallyViewed);assert(toc.expandedPriorReadNotNewSourcePosition);
 for(const x of[...local.records,toc,...qa.records]){assert(x.actuallyViewed);assert.equal(sha(await readFile(resolve(w,x.file))),x.sha256);}
 assert.equal(local.newHTTPRequests,0);assert.equal(local.newOriginalContainers,0);
});
let hhcCalls=0;
await check('One actual HHC call confirms printed static旅56;6 source kin/branch labels,Self1/Response4 and two metalWealth coordinates match',async()=>{
 const c={};c.window=c;vm.createContext(c);const engine=await readFile(resolve(r,'engine.js'));assert.equal(sha(engine),'39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6');vm.runInContext(engine.toString(),c);
 assert.equal(c.HHC_ENGINE.hexNumber(values),56);hhcCalls++;
 const out=inspect(values,ctx('檀香'));assert.equal(out.chart.primary.number,56);assert.equal(out.chart.changed.number,56);assert.deepEqual(out.chart.movingLines,[]);
 assert.deepEqual(out.chart.lines.map(x=>({branch:x.branch,kin:x.kin})),fixture.sourceBaseLabelsBottomToTop);assert.equal(out.chart.primary.shi,1);assert.equal(out.chart.primary.ying,4);
 assert.deepEqual(out.wealthCoordinates,[{line:3,branch:'申',element:'金'},{line:4,branch:'酉',element:'金'}]);
});
await check('Quoted metal-to-jewels rule is explicitly rejected by named author and cannot override caller commodity or silently turn翠毛 into modernjade翡翠',()=>{
 assert(source.authorCritique.automaticCommodityInferenceRejected);assert(source.oldMappingsAreSelectedBoundedExcerptsNotCompleteFiveElementTable);
 const unknown=inspect(values,ctx(null));assert.equal(unknown.questionScopeComplete,false);assert.equal(unknown.explicitCommodityLabel,null);assert.equal(unknown.inferredCommodity,null);
 assert.deepEqual(unknown.quotedOldMappingReferences,[{element:'金',labels:['珠寶玉石'],acceptedByNamedAuthor:false,notARecommendation:true}]);
 for(const name of['珠寶玉石','魚鹽','檀香','翠毛']){const out=inspect(values,ctx(name));assert(out.questionScopeComplete);assert.equal(out.explicitCommodityLabel,name);assert.equal(out.sourceQuestionCommodityPreserved,name);assert.equal(out.inferredCommodity,null);assert.equal(out.productClassification,null);assert.equal(out.commodityRecommendation,null);}
 assert.throws(()=>inspect(values,ctx('翡翠')),TypeError);
});
await check('TOC17 and body317–318 reveal omitted marriage82 and repeatedrisk81;workingmap expands136→137 without altering oldmap or source',async()=>{
 const map=await read(resolve(b,'B02_CURRENT_UNITS.json')),old=await read(resolve(r,'research/liuyao-exam-intent/B02_CURRENT_UNITS.json')),audit=await read(resolve(b,'NUMBERING_AUDIT.json')),manual=await read(resolve(b,'MANUAL_READINGS.json'));
 assert.equal(old.units.length,136);assert.equal(old.units.find(x=>x.id==='B02-ch082').normalizedHeading,'行險求財');assert(!old.units.some(x=>x.normalizedHeading==='婚姻'));
 assert.equal(map.units.length,137);assert.deepEqual(map.units.filter(x=>x.printedNumber===81).map(x=>x.normalizedHeading),['請會搖會','行險求財']);assert.equal(map.units.find(x=>x.id==='B02-ch082').normalizedHeading,'婚姻');
 assert.equal(map.units.find(x=>x.id==='B02-ch075').normalizedHeading,'往何方買賣');assert.equal(old.units.find(x=>x.id==='B02-ch075').normalizedHeading,'在何方買賣');
 assert.deepEqual(map.currentCounts,{registeredUnits:137,regularNumberedUnits:130,supplements:7,headingOnlyBodyUnits:47,partialFoundationUnits:7,otherPartialUnits:1,firstPassCompleteSpanUnits:82,wholeUnitsApplied:0});
 assert.equal(manual.chapterRanges.length,16);assert.equal(manual.chapter83.nextPDFPage,325);assert.equal(manual.chapter83.wholeFirstPassRead,false);
 assert(audit.historicalMapsRetained);assert(audit.corrections.every(x=>!x.sourceEmended));assert(map.units.every(x=>!x.entireUnitApplied));
});
await check('Strict context/figures reject missing fields,aliases,hidden premises;returned source data cannot mutate tables and money/action/date stay unknown',()=>{
 for(const bad of[null,{},[],{system:source.system},{system:source.system,commodityLabel:undefined},{...ctx('檀香'),profit:100},{...ctx('檀香'),[Symbol('x')]:true},{system:'modern-investment',commodityLabel:'檀香'}])assert.throws(()=>inspect(values,bad),TypeError);
 for(const bad of[[],Array(6),[8,8,7,7,8,'7']])assert.throws(()=>inspect(bad,ctx('檀香')),TypeError);
 const out=inspect(values,ctx('檀香'));out.quotedOldMappingReferences[0].labels.push('fake');out.wealthCoordinates[0].element='fake';const next=inspect(values,ctx('檀香'));
 assert.deepEqual(next.quotedOldMappingReferences[0].labels,['珠寶玉石']);assert.equal(next.wealthCoordinates[0].element,'金');
 for(const k of['inferredCommodity','commodityRecommendation','productClassification','actualPrice','profit','financialResult','saleOrPurchaseAction','geographicalRecommendation','chronologicalDateAdapter','effectiveStrength'])assert.equal(next[k],null);
 assert.equal(next.consumerApplied,false);assert.equal(next.sourceOutcomeValidated,false);
});
const result={date:'2026-10-28',status:'staged-corrected-b02-numbering-and-rejection-of-automatic-commodity-inference-verified',checks,
 summary:{newViewedSourcePositions:24,expandedPriorTOCPositions:1,sourceQARendersViewed:3,firstPassSpansAdded:16,workingRegisteredUnitsBefore:136,workingRegisteredUnitsAfter:137,currentFirstPassSpans:82,currentHeadingOnlyUnits:47,partialFoundationUnits:7,otherPartialUnits:1,
 actualHHCHexCalls:hhcCalls,printedCastFixtures:1,sourceKinBranchLabels:6,metalWealthCoordinates:2,selectedQuotedOldMappings:2,explicitSourceCommodityLabels:4,newHTTPRequests:0,newOriginalContainers:0},
 fixtureProjection:inspect(values,ctx(null)),sourceEmended:false,commodityInferenceRejectedByNamedAuthor:true,fullConditionalRulesEncoded:false,sourceOutcomesValidated:false,consumerChanged:false,wholeCatalogueCompleted:false};
await writeFile(resolve(q,'RESULTS.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({checks:checks.length,...result.summary}));
