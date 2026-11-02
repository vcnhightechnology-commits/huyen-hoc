import{readFile,writeFile,mkdir}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';
import assert from'node:assert/strict';import vm from'node:vm';
import{createRequire}from'node:module';
import{compile,catalogue}from'../research/liuyao-foundations/liuyao-reference.mjs';
import{figureAvailability}from'../research/liuyao-b03-figures/availability-reference.mjs';
import{supportChainCoordinates}from'../research/liuyao-b03-book6/support-chain-reference.mjs';
const root=resolve(import.meta.dirname,'..'),w=resolve(root,'..'),base=resolve(root,'research/liuyao-b03-line-labels'),
 qa=resolve(root,'qa/liuyao-b03-line-labels'),archive=resolve(w,'archives/v53-before-liuyao-b03-all-annotations'),
 read=async p=>JSON.parse(await readFile(p,'utf8')),sha=b=>createHash('sha256').update(b).digest('hex'),checks=[];
function test(name,fn){fn();checks.push({name,ok:true});console.log('PASS',name);}
const source=await read(resolve(base,'PRINTED_LINE_ROWS.json')),manual=await read(resolve(base,'MANUAL_READINGS.json')),
 locator=await read(resolve(root,'research/liuyao-b03-figures/FIGURE_LOCATOR.json')),
 audit=await read(resolve(base,'SOURCE_AUDIT.json')),pdf=await readFile(resolve(base,manual.sourcePDF));
for(const r of[...manual.records,...manual.qaImages])assert.equal(sha(await readFile(resolve(base,r.image))),r.sha256);
test('Existing50191031byte/60page source and26expanded earlier images/twoQA crops preserve SHA;zeroHTTP/PDF',()=>{
 assert.equal(pdf.length,50191031);assert.equal(sha(pdf),manual.sourceSHA256);
 assert.equal(sha(pdf),'5dcd7b5005b1e86f441a9350eefb7c0e9e628c47ab926b2a7d1bdd6691a4773d');
 assert.deepEqual(manual.records.map(r=>r.pdfPage),Array.from({length:26},(_,i)=>i+34));assert.equal(manual.qaImages.length,2);
 assert.equal(manual.newHTTPBodies,0);assert.equal(manual.newOriginalPDFs,0);assert.equal(audit.generatedSourceRowsFromRuntime,false);
});
test('64unique manually read figures/384primary rows/128shi-ying positions with explicit direction and six split-column figures',()=>{
 assert.equal(source.records.length,64);assert.deepEqual(source.records.map(r=>r.number).sort((a,b)=>a-b),Array.from({length:64},(_,i)=>i+1));
 for(const r of source.records){assert.equal(r.ganzhiTopDown.split(' ').length,6);assert.equal([...r.kinTopDown].length,6);
  assert(r.sourceFieldsManuallyRead);assert(r.shi>=1&&r.shi<=6&&r.ying>=1&&r.ying<=6);
  const pages=r.annotationPages??[r.page];assert(pages.every(p=>manual.records.some(m=>m.pdfPage===p)));
 }
 assert.deepEqual(source.records.filter(r=>r.annotationPages).map(r=>r.number),[17,18,4,34,45,54]);
 assert.equal(source.all384AnnotationsCollated,false);assert.equal(source.allGuaShenLabelsCollated,false);
 assert.equal(source.allDiagramPolarityMarksDiplomaticallyCollated,false);assert.equal(audit.hiddenCoordinatesAreNotGuaShen,true);
});
const ctx={};ctx.window=ctx;vm.createContext(ctx);const engine=await readFile(resolve(root,'engine.js'));vm.runInContext(engine.toString('utf8'),ctx);
const cat=catalogue(),kin=audit.kinAbbreviations,charts=[];let hhcCalls=0,primaryRows=0,roleMarkers=0,hiddenCoordinates=0,availabilityCalls=0;
test('64actual HHC figure identity calls anchor source fixtures to source-specific private charts',()=>{
 for(const r of source.records){const c=cat.find(c=>c.number===r.number),v=c.bits.map(b=>b?7:8);
  assert.equal(ctx.HHC_ENGINE.hexNumber(v),r.number);hhcCalls++;
  const chart=compile(v);assert.equal(chart.primary.number,r.number);
  const loc=locator.figures.find(f=>f.number===r.number);assert.equal(loc.palace,chart.primary.palace);
  charts.push({r,values:v,chart});
 }assert.equal(hhcCalls,64);
});
const compared=[];
test('All384primary stem-branch/kin rows and128shi-ying markers match source transcription, without fabricated gua-shen',()=>{
 for(const{r,chart}of charts){const sb=r.ganzhiTopDown.split(' ').reverse(),ks=[...r.kinTopDown].reverse();
  for(let i=0;i<6;i++){const a=chart.lines[i];assert.equal(a.stem+a.branch,sb[i],`figure${r.number}line${i+1}ganzhi`);
   assert.equal(a.kin,kin[ks[i]],`figure${r.number}line${i+1}kin`);primaryRows++;
   compared.push({number:r.number,line:i+1,sourceStemBranch:sb[i],sourceKin:kin[ks[i]],privateStemBranch:a.stem+a.branch,privateKin:a.kin});
  }
  assert.equal(chart.primary.shi,r.shi);assert.equal(chart.primary.ying,r.ying);roleMarkers+=2;
 }assert.equal(primaryRows,384);assert.equal(roleMarkers,128);
});
const hiddenResults=[];
test('56printed hidden-kin coordinates match actual B03 availability gate across320explicit kin queries;no gua-shen substitution',()=>{
 for(const{r,values}of charts){const observed=r.hidden.map(h=>({...h,kin:kin[h.kin]})).sort((a,b)=>a.line-b.line),actual=[];
  for(const k of Object.values(kin)){const a=figureAvailability(values,k);availabilityCalls++;
   assert.equal(a.effectiveUseGodSelection,null);assert.equal(a.卦身Method,null);assert.equal(a.consumerApplied,false);
   for(const h of a.hiddenSearchCandidates)actual.push({line:h.line,kin:h.kin,branch:h.branch,element:h.element});
  }
  actual.sort((a,b)=>a.line-b.line);assert.deepEqual(actual,observed,`figure${r.number}hidden`);hiddenCoordinates+=observed.length;
  hiddenResults.push({number:r.number,source:observed,private:actual});
 }
 assert.equal(hiddenCoordinates,56);assert.equal(availabilityCalls,320);
 assert(!source.records.find(r=>r.number===17).hidden.some(h=>h.branch==='申'));
 assert.equal(source.records.find(r=>r.number===18).hidden[0].branch,'巳');
});
const old=await read(resolve(archive,'PACKAGE_MANIFEST.json')),html=await readFile(resolve(root,'Huyen_Hoc_Cac.html')),
 refs=old.files.filter(f=>/research\/liuyao-[^/]+\/.*reference\.mjs$/.test(f.file));
for(const f of refs)assert.equal(sha(await readFile(resolve(root,f.file))),f.sha256);
test('707411byte consumer and15earlier LiuYao references unchanged;printed line corpus/QA absent from site',()=>{
 assert.equal(refs.length,15);assert.equal(html.length,707411);assert.equal(sha(html),old.product.sha256);
 for(const token of['PRINTED_LINE_ROWS.json','liuyao-b03-line-labels','cross-page-46-qa.png'])assert.equal(html.includes(Buffer.from(token)),false);
});
const q3=await read(resolve(base,'BOOK6_QUESTION3_FIXTURES.json')),q3pdf=await readFile(resolve(base,q3.sourcePDF)),printed=[];
for(const r of[...q3.manualImages,...q3.qaImages])assert.equal(sha(await readFile(resolve(base,r.image))),r.sha256);
let printedCalls=0,supportContexts=0,ownBranchCoordinates=0,lunarCalls=0;
test('Four question3 source casts pass8actual HHC calls/six selected own-change branches/five explicit-use contexts',()=>{
 assert.equal(q3pdf.length,55093879);assert.equal(sha(q3pdf),q3.sourcePDFSHA256);
 assert.equal(sha(q3pdf),'1d6c656828533ac52ae1fd4ff06cc3c025db98ae5458dc686eda2a6b1d11f07f');
 assert.equal(q3.fixtures.length,4);assert.equal(q3.TOCQuestion3StatedCount,4);assert.equal(q3.all131Book6ExamplesIndependentlyCounted,false);
 for(const f of q3.fixtures){const v=f.valuesBottomToTop,p=ctx.HHC_ENGINE.hexNumber(v),
  c=ctx.HHC_ENGINE.hexNumber(v.map(x=>x===6?7:x===9?8:x)),a=compile(v);hhcCalls+=2;printedCalls+=2;
  assert.equal(p,f.primary);assert.equal(c,f.changed);assert.deepEqual(a.movingLines,f.movingLines);
  for(const change of f.sourceSelectedChanges){const line=a.lines[change.line-1];assert.equal(line.branch,change.primaryBranch);
   assert.equal(line.changed.branch,change.changedBranch);ownBranchCoordinates++;}
  const supports=[];
  for(const useLine of f.explicitUseLinesForCoordinateTest){const s=supportChainCoordinates(v,{sourceContext:'B03-question3-original-support',useLine});supportContexts++;
   assert.equal(s.selectedUse.branch,f.sourceUseBranch);assert.equal(s.effectiveSupportSelection,null);
   if(f.sourceOwnReturnControlOriginLine){const o=s.candidateOrigins.find(o=>o.line===f.sourceOwnReturnControlOriginLine);assert(o);assert.equal(o.rawOwnChangeControlsOriginal,true);}
   supports.push({useLine,candidateOrigins:s.candidateOrigins.map(o=>({line:o.line,branch:o.branch,moving:o.moving,rawOwnChangeControlsOriginal:o.rawOwnChangeControlsOriginal})),effectiveSupportSelection:s.effectiveSupportSelection});
  }
  printed.push({id:f.id,page:f.page,sourceDay:f.dayGanZhi,sourceMonth:f.monthBranch,primary:p,changed:c,movingLines:a.movingLines,
   sourceSelectedChanges:f.sourceSelectedChanges,supportContexts:supports,historicalOutcomeValidated:false});
 }
 assert.equal(printedCalls,8);assert.equal(ownBranchCoordinates,6);assert.equal(supportContexts,5);assert.equal(hhcCalls,72);
});
const req=createRequire(import.meta.url),runtime=await read(resolve(root,'research/bazi-late-zi/VERIFICATION.json'));
for(const r of runtime.runtime)assert.equal(sha(await readFile(resolve(w,r.file))),r.sha256);
const L=req(resolve(w,'v46/node_modules/lunar-typescript'));assert.equal(req(resolve(w,'v46/node_modules/lunar-typescript/package.json')).version,'1.8.6');
const dayRows=(await read(resolve(root,'research/liuyao-b03-book1-tables/NAYIN_ROWS.json'))).rows,dayReferences=[];
test('Four actual lunar noon-enumeration calls check source day labels/xunvoid only, no historical Gregorian reconstruction',()=>{
 const expectedVoid=['戌亥','子丑','午未','戌亥'];
 for(let i=0;i<q3.fixtures.length;i++){const f=q3.fixtures[i],row=dayRows.find(r=>r.dayGanZhi===f.dayGanZhi);assert(row);
  const [y,m,d,h,min,sec]=row.referenceNoonDate.split(/[- :]/).map(Number),ec=L.Solar.fromYmdHms(y,m,d,h,min,sec).getLunar().getEightChar();ec.setSect(2);lunarCalls++;
  assert.equal(ec.getDay(),f.dayGanZhi);assert.equal(ec.getDayXunKong(),expectedVoid[i]);
  dayReferences.push({id:f.id,sourceDay:f.dayGanZhi,referenceNoonOnlyForCyclicLabelCheck:row.referenceNoonDate,
   rawVoidBranches:ec.getDayXunKong(),sourceGregorianDateReconstructed:false});
 }assert.equal(lunarCalls,4);assert.equal(q3.sourceDatesConvertedToGregorian,false);assert.equal(q3.sourceHistoricalOutcomesValidated,false);
});
await mkdir(qa,{recursive:true});const cases={date:'2026-10-27',primaryRows:compared,hiddenResults,
 question3PrintedCasts:printed,sourceDayCoordinateReferences:dayReferences,
 sixSplitColumnSourceFigures:[17,18,4,34,45,54],diagramPolarityMarksFullyCollated:false,guaShenLabelsFullyCollated:false,
 historicalOutcomesValidated:false};
await writeFile(resolve(qa,'SOURCE_CASE_RESULTS.json'),JSON.stringify(cases,null,2)+'\n');
const summary={actualHHCHexCalls:hhcCalls,privatePrimaryRows:primaryRows,sourceFigures:64,shiYingPositions:roleMarkers,
 hiddenKinCoordinates:hiddenCoordinates,privateAvailabilityQueries:availabilityCalls,expandedBook1SourcePages:26,expandedBook6SourcePages:3,
 QAOnlySourceRenders:5,QACrops:6,splitColumnFigures:6,newBook6PrintedCastFixtures:4,actualHHCPrintedCastCalls:printedCalls,
 printedOwnChangeBranchCoordinates:ownBranchCoordinates,privateSupportContextChecks:supportContexts,actualLunarCalls:lunarCalls,
 cumulativeBook6PrintedCastFixtures:6};
await writeFile(resolve(qa,'ENGINE_RESULTS.json'),JSON.stringify({date:'2026-10-27',checks,summary,engineSHA256:sha(engine),htmlSHA256:sha(html),
 caseDigest:sha(Buffer.from(JSON.stringify(cases))),consumerChanged:false,wholeBookApplied:false,wholeCatalogueCompleted:false},null,2)+'\n');
console.log(JSON.stringify({checks:checks.length,...summary}));
