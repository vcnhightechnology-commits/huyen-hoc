import{readFile,writeFile}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';import vm from'node:vm';import assert from'node:assert/strict';
import{weatherRoleCandidates as inspect}from'../research/liuyao-weather/weather-reference.mjs';import{catalogue,compile}from'../research/liuyao-foundations/liuyao-reference.mjs';
const r=resolve(import.meta.dirname,'..'),w=resolve(r,'..'),b=resolve(r,'research/liuyao-weather'),q=resolve(r,'qa/liuyao-weather'),read=async p=>JSON.parse(await readFile(p,'utf8')),sha=x=>createHash('sha256').update(x).digest('hex'),checks=[];
async function check(name,fn){await fn();checks.push({name,ok:true});}
const methods=(await read(resolve(b,'QUESTION_ROLES.json'))).methods,fixture=(await read(resolve(b,'PRINTED_FIXTURES.json'))).fixtures[0],manual=await read(resolve(b,'MANUAL_READINGS.json')),src=await read(resolve(b,'SOURCE_MANIFEST.json'));
await check('Retained source PDF and all source-image/QA bytes match source records, including seven explicitly unread renders',async()=>{
 assert.equal(sha(await readFile(resolve(w,src.sourcePDF))),src.sourceSHA256);
 for(const x of manual.records)assert.equal(sha(await readFile(resolve(b,x.file))),x.sha256);
 for(const x of src.expandedPriorPages)assert.equal(sha(await readFile(resolve(w,x.file))),x.sha256);
 assert.equal(sha(await readFile(resolve(b,manual.highResolutionQA.file))),manual.highResolutionQA.sha256);
 assert.equal(manual.records.filter(x=>x.actuallyViewed).length,23);assert.equal(manual.records.filter(x=>!x.actuallyViewed).length,7);
});
let hhcCalls=0;const c={};c.window=c;vm.createContext(c);vm.runInContext(await readFile(resolve(r,'engine.js'),'utf8'),c);
await check('Printed恒→大過 case executes two real HHC calls and matches all six independently read kin/branch labels',()=>{
 assert.equal(c.HHC_ENGINE.hexNumber(fixture.valuesBottomToTop),32);hhcCalls++;
 assert.equal(c.HHC_ENGINE.hexNumber(fixture.valuesBottomToTop.map(v=>v===6?7:v===9?8:v)),28);hhcCalls++;
 const chart=compile(fixture.valuesBottomToTop);assert.deepEqual(chart.lines.map(x=>({branch:x.branch,kin:x.kin})),fixture.sourceBaseLabelsBottomToTop);
 assert.deepEqual(chart.movingLines,[5]);assert.equal(chart.lines[4].changed.branch,'酉');assert.equal(chart.lines[4].kin,'官鬼');assert.equal(chart.lines.find(x=>x.role==='世').branch,'酉');
});
await check('Named voices preserve rain parent, JueZi clear child, quoted clear child-or-wealth and quoted cloud/thunder ghost',()=>{
 const v=fixture.valuesBottomToTop,j=methods[0].id,o=methods[1].id,lines=(system,question)=>inspect(v,{system,question}).originalCandidates.map(x=>x.line);
 assert.deepEqual(lines(j,'rain'),[2]);assert.deepEqual(lines(j,'clear'),[4]);assert.deepEqual(lines(o,'clear'),[1,4,6]);assert.deepEqual(lines(o,'cloud-thunder'),[3,5]);
 const unknown=inspect(v,{system:j,question:'cloud-thunder'});assert.equal(unknown.sourceRoleEstablished,false);assert.equal(unknown.desiredKin,null);assert.equal(unknown.predictedWeather,null);
});
let contexts=0,contrasts=0;
await check('All64 figures×64 motion masks keep original/changed role candidates separate over20480 named question contexts',()=>{
 for(const h of catalogue())for(let mask=0;mask<64;mask++){
  const values=h.bits.map((bit,i)=>(mask>>i)&1?(bit?9:6):(bit?7:8)),chart=compile(values);
  for(const method of methods)for(const rule of method.selectors){
   const out=inspect(values,{system:method.id,question:rule.question});
   assert.deepEqual(out.originalCandidates.map(x=>x.line),chart.lines.filter(x=>rule.desiredKin.includes(x.kin)).map(x=>x.line));
   assert.deepEqual(out.changedCandidates.map(x=>x.line),chart.lines.filter(x=>x.changed&&rule.desiredKin.includes(x.changed.kin)).map(x=>x.line));
   assert.deepEqual(out.movingOriginalCandidateLines,chart.lines.filter(x=>x.moving&&rule.desiredKin.includes(x.kin)).map(x=>x.line));
   assert.equal(out.predictedWeather,null);assert.equal(out.useLineSelected,null);assert.equal(out.availabilityEstablished,null);assert.equal(out.dayOrMonthPremisesApplied,false);contexts++;
  }
  const a=inspect(values,{system:methods[0].id,question:'clear'}),b=inspect(values,{system:methods[1].id,question:'clear'});
  if(a.originalCandidates.length!==b.originalCandidates.length)contrasts++;
 }
 assert.equal(contexts,20480);assert(contrasts>0);
});
await check('Unknown question stays unknown; invalid source/input fields are rejected without defaults or mutation',()=>{
 const v=fixture.valuesBottomToTop.slice(),before=v.slice(),base={system:methods[0].id,question:'rain'};
 const unknown=inspect(v,{...base,question:null});assert.equal(unknown.sourceRoleEstablished,null);assert.equal(unknown.originalCandidates,null);
 for(const bad of[undefined,null,[],{}, {...base,date:'today'},{...base,question:undefined},{...base,question:'free-text'},{...base,[Symbol('x')]:true}])assert.throws(()=>inspect(v,bad),TypeError);
 for(const bad of[[],Array(6),[7,7,7,7,7,'9']])assert.throws(()=>inspect(bad,base),TypeError);
 const copy=inspect(v,base);copy.desiredKin[0]='invented';copy.originalCandidates[0].branch='invented';assert.equal(inspect(v,base).desiredKin[0],'父母');assert.deepEqual(v,before);
});
await check('Source boundary confirms weatherchapter inbodyvolume3, ending212 andvolume4/chapter36opening213 without TOC emendation',async()=>{
 const units=await read(resolve(b,'B02_CURRENT_UNITS.json')),bounds=await read(resolve(b,'SOURCE_BOUNDARIES.json'));
 assert.deepEqual(units.currentCounts,{registeredUnits:136,regularNumberedUnits:130,supplements:6,headingOnlyBodyUnits:95,partialFoundationUnits:7,otherPartialUnits:1,firstPassCompleteSpanUnits:33,wholeUnitsApplied:0});
 const a=units.units.find(x=>x.id==='B02-ch035'),n=units.units.find(x=>x.id==='B02-ch036');assert.equal(a.tocVolume,4);assert.equal(a.bodyTextualVolumeAsPrinted,3);assert.equal(a.bodyPDFPages.length,24);assert.deepEqual(n.bodyPDFPages,[213]);
 assert.equal(bounds.volume3EndingPage,212);assert.equal(bounds.volume4OpeningPage,213);assert.equal(bounds.TOCEmended,false);
 assert.equal((await read(resolve(b,'BOUNDED_CLAUSES.json'))).clauses.length,16);
});
await check('Current public HTML and all calendar/fortune/engine source bytes remain unchanged',async()=>{
 const old=await read(resolve(w,'archives/v53-before-liuyao-weather/PACKAGE_MANIFEST.json'));
 for(const file of['Huyen_Hoc_Cac.html','site/index.html','engine.js','app.js','content.js','fortune.js'])assert.equal(sha(await readFile(resolve(r,file))),old.files.find(x=>x.file===file).sha256);
});
const out={date:'2026-10-27',checks,summary:{actualHHCHexCalls:hhcCalls,printedCastFixtures:1,sourceBranchKinLabels:6,namedSourceMethods:2,namedQuestionSelectors:5,privateMotionQuestionContexts:contexts,clearCandidateContrastContexts:contrasts,
 boundedClauses:16,fullChapter35BodyPositions:24,newWeatherContentPositionsRead:21,newParatextPositionsRead:1,newNextChapterOpeningPositionsRead:1,renderedNotReadPositions:7,highResolutionQARenders:1,newHTTPRequests:0,newOriginalContainers:0},
 consumerChanged:false,wholeChapterApplied:false,meteorologicalModelValidated:false,wholeCatalogueCompleted:false};
await writeFile(resolve(q,'RESULTS.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({checks:checks.length,...out.summary}));
