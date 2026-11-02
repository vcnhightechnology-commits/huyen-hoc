import{readFile,writeFile,mkdir}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';
import{createRequire}from'node:module';import assert from'node:assert/strict';import vm from'node:vm';
import{monthStemCoordinate,hourStemCoordinate}from'../research/liuyao-b03-book1-tables/stem-coordinate-reference.mjs';
const root=resolve(import.meta.dirname,'..'),w=resolve(root,'..'),base=resolve(root,'research/liuyao-b03-book1-tables'),
 qa=resolve(root,'qa/liuyao-b03-book1-tables'),archive=resolve(w,'archives/v53-before-liuyao-b03-book1-tables'),
 read=async p=>JSON.parse(await readFile(p,'utf8')),sha=b=>createHash('sha256').update(b).digest('hex'),checks=[];
function test(name,fn){fn();checks.push({name,ok:true});console.log('PASS',name);}
const manual=await read(resolve(base,'MANUAL_READINGS.json')),units=await read(resolve(base,'BOOK1_OPENING_UNITS.json')),
 anchors=await read(resolve(base,'STEM_ANCHORS.json')),nayin=await read(resolve(base,'NAYIN_ROWS.json')),
 toc=await read(resolve(base,'TOC_PRINTED_EXAMPLE_COUNTS.json')),voices=await read(resolve(base,'EDITION_VOICE_LEADS.json')),
 pdf=await readFile(resolve(base,manual.sourcePDF));
test('Reused50191031byte/60page original source; no new HTTP or original PDF',()=>{
 assert.equal(pdf.length,50191031);assert.equal(sha(pdf),manual.sourceSHA256);
 assert.equal(sha(pdf),'5dcd7b5005b1e86f441a9350eefb7c0e9e628c47ab926b2a7d1bdd6691a4773d');
 assert.equal(manual.sourcePDFPages,60);assert.equal(manual.newHTTPBodies,0);assert.equal(manual.newOriginalPDFs,0);
});
for(const r of [...manual.records,...manual.qaImages])assert.equal(sha(await readFile(resolve(base,r.image))),r.sha256);
test('Opening1..33 bounded read/12QA crops/direct volume1 end, editorial groups not full application',()=>{
 assert.deepEqual(manual.records.map(r=>r.pdfPage),Array.from({length:33},(_,i)=>i+1));assert.equal(manual.qaImages.length,12);
 assert.equal(new Set(manual.qaImages.map(r=>r.pdfPage)).size,7);assert.equal(manual.directEnding.pdfPage,33);
 assert.equal(units.records.length,57);assert(units.records.every(r=>r.boundedSourceSpanFirstPassRead&&!r.entireUnitApplied));
 assert.equal(units.all384LineAnnotationsCollated,false);assert.equal(manual.entireBookApplied,false);
});
test('Separate preface/imprint/rule voices and131TOC-stated examples, not131verified body figures',()=>{
 assert.equal(voices.claims.length,4);assert.equal(voices.doNotMergePrefaceAndRuleVoicesAutomatically,true);
 assert(voices.claims[1].reading.includes('吳郡張景松'));assert.equal(voices.claims[1].GregorianDateReconstructed,false);
 assert.deepEqual(toc.rows.map(r=>r.sourceStatedPrintedExamples),[5,11,4,12,5,4,14,7,6,5,8,13,11,4,7,4,5,6]);
 assert.equal(toc.rows.reduce((a,r)=>a+r.sourceStatedPrintedExamples,0),131);assert.equal(toc.allExamplesVerified,false);
 assert.equal(anchors.yearMonthPairedAnchors.length,5);assert.equal(anchors.dayHourPairedAnchors.length,5);
 assert.equal(anchors.seasonalWatchVerseAt25ConvertedToModernClock,false);
});
const req=createRequire(import.meta.url),runtime=await read(resolve(root,'research/bazi-late-zi/VERIFICATION.json'));
for(const r of runtime.runtime)assert.equal(sha(await readFile(resolve(w,r.file))),r.sha256);
const L=req(resolve(w,'v46/node_modules/lunar-typescript'));assert.equal(req(resolve(w,'v46/node_modules/lunar-typescript/package.json')).version,'1.8.6');
const engine=await readFile(resolve(root,'engine.js')),ctx={};ctx.window=ctx;vm.createContext(ctx);vm.runInContext(engine.toString('utf8'),ctx);
const months=[],hours=[],nayinCases=[];let hhcCalls=0,lunarCalls=0;
test('120source month-stem coordinates agree with120actual HHC bazi and120actual lunar calls',()=>{
 for(let y=2000;y<2010;y++)for(let m=1;m<=12;m++){
  const ec=L.Solar.fromYmdHms(y,m,15,12,30,0).getLunar().getEightChar();ec.setSect(2);lunarCalls++;
  const source=monthStemCoordinate({yearStem:ec.getYear()[0],monthBranch:ec.getMonth()[1]});
  const hhc=ctx.HHC_ENGINE.bazi({y,m,d:15,hour:12,minute:30,tz:8,gender:'male',dayPolicy:'midnight',lateZiHour:'day'});hhcCalls++;
  assert.equal(source.ganZhi,ec.getMonth());assert.equal(hhc.pillars[1].han,source.ganZhi);
  assert.equal(source.calendarAdapter,false);assert.equal(source.yearBoundaryConvention,null);assert.equal(source.lunarMonthOrdinalUsed,false);
  months.push({date:[y,m,15,12,30],confirmedSourceCoordinates:{yearStem:source.yearStem,monthBranch:source.monthBranch},
   source:source.ganZhi,hhc:hhc.pillars[1].han,lunar:ec.getMonth(),evidence:source.evidence});
 }assert.equal(new Set(months.map(r=>r.confirmedSourceCoordinates.yearStem+r.confirmedSourceCoordinates.monthBranch)).size,120);
});
test('120source hour-stem coordinates agree with120actual HHC bazi and120actual lunar calls away from23h',()=>{
 for(let d=1;d<=10;d++)for(let hour=0;hour<24;hour+=2){
  const ec=L.Solar.fromYmdHms(2026,1,d,hour,30,0).getLunar().getEightChar();ec.setSect(2);lunarCalls++;
  const source=hourStemCoordinate({dayStem:ec.getDay()[0],hourBranch:ec.getTime()[1]});
  const hhc=ctx.HHC_ENGINE.bazi({y:2026,m:1,d,hour,minute:30,tz:8,gender:'male',dayPolicy:'midnight',lateZiHour:'day'});hhcCalls++;
  assert.equal(source.ganZhi,ec.getTime());assert.equal(hhc.pillars[3].han,source.ganZhi);
  assert.equal(source.civilClockHour,null);assert.equal(source.dayBoundaryConvention,null);assert.equal(source.timezone,null);
  hours.push({date:[2026,1,d,hour,30],confirmedSourceCoordinates:{dayStem:source.dayStem,hourBranch:source.hourBranch},
   source:source.ganZhi,hhc:hhc.pillars[3].han,lunar:ec.getTime(),evidence:source.evidence});
 }assert.equal(new Set(hours.map(r=>r.confirmedSourceCoordinates.dayStem+r.confirmedSourceCoordinates.hourBranch)).size,120);
 assert.equal([...months,...hours].filter(r=>r.evidence==='direct-source-anchor').length,20);
});
test('60nayin coordinates retain58script-normalized names and2explicit lexical variants; all60elements agree',()=>{
 const byDay=new Map();for(let i=0;i<60;i++){
  const ec=L.Solar.fromYmdHms(2026,1,1,12,0,0).next(i).getLunar().getEightChar();ec.setSect(2);lunarCalls++;
  byDay.set(ec.getDay(),ec.getDayNaYin());
 }
 assert.equal(nayin.rows.length,60);assert.equal(new Set(nayin.rows.map(r=>r.dayGanZhi)).size,60);
 for(const r of nayin.rows){const actual=byDay.get(r.dayGanZhi);assert.equal(actual,r.actualLunarNaYin);assert.equal(actual.at(-1),r.sourceLiteralName.at(-1));
  assert.equal(actual===r.editorialSimplifiedName,r.nameExactAfterScriptNormalization);nayinCases.push({day:r.dayGanZhi,source:r.sourceLiteralName,runtime:actual,nameExactAfterScriptNormalization:r.nameExactAfterScriptNormalization});
 }
 assert.deepEqual(nayin.rows.filter(r=>!r.nameExactAfterScriptNormalization).map(r=>[r.dayGanZhi,r.sourceLiteralName,r.actualLunarNaYin]),[['甲申','井泉水','泉中水'],['乙酉','井泉水','泉中水']]);
 assert.equal(nayin.rows[16].sourceLiteralName,'白蠟金');assert.equal(nayin.rows[40].sourceLiteralName,'覆燈火');
 assert.equal(lunarCalls,300);assert.equal(hhcCalls,240);
});
test('Explicit coordinate inputs required; reject clock/lunar ordinal/unknown keys and preserve input',()=>{
 for(const [fn,good]of[[monthStemCoordinate,{yearStem:'甲',monthBranch:'寅'}],[hourStemCoordinate,{dayStem:'甲',hourBranch:'子'}]]){
  for(const bad of[null,[],{},'甲',Object.fromEntries(Object.keys(good).map(k=>[k,'a'])),{...good,clock:12},{...good,lunarMonth:1},{...good,[Symbol('x')]:1}])assert.throws(()=>fn(bad));
  assert.throws(()=>fn(good,null));const before=JSON.stringify(good);fn(good);assert.equal(JSON.stringify(good),before);
 }
});
const old=await read(resolve(archive,'PACKAGE_MANIFEST.json')),html=await readFile(resolve(root,'Huyen_Hoc_Cac.html')),
 refs=old.files.filter(f=>/research\/liuyao-[^/]+\/.*reference\.mjs$/.test(f.file));
for(const f of refs)assert.equal(sha(await readFile(resolve(root,f.file))),f.sha256);
test('707411byte consumer and14prior LiuYao references preserved, private coordinate/source files absent from site',()=>{
 assert.equal(refs.length,14);assert.equal(html.length,707411);assert.equal(sha(html),old.product.sha256);
 for(const s of['stem-coordinate-reference.mjs','STEM_ANCHORS.json','EDITION_VOICE_LEADS.json'])assert.equal(html.includes(Buffer.from(s)),false);
});
await mkdir(qa,{recursive:true});const summary={actualHHCBaziCalls:hhcCalls,actualLunarCalls:lunarCalls,monthCoordinates:120,hourCoordinates:120,
 directSingleStemAnchors:20,editorialExpandedCoordinates:220,nayinCoordinates:60,nayinElementAgreements:60,nayinNamesAfterScriptNormalization:58,
 nayinLexicalVariants:2,manualRecords:33,QACrops:12,QAOnlySourceRenders:7,editorialUnitGroups:57,TOCStatedExamples:131};
const cases={date:'2026-10-27',months,hours,nayinCases,sourceClockBoundaryReconstructed:false,seasonalWatchConvertedToCivilClock:false,
 actualRealEngineVersions:{hhcEngineSHA256:sha(engine),lunar:'1.8.6',pinnedRuntimeFiles:runtime.runtime.length},
 testDatesAreEnumerationFixturesNotHistoricalReconstruction:true,sourceCoordinateInputsConfirmedByRealCalendarForComparisonOnly:true};
await writeFile(resolve(qa,'SOURCE_CASE_RESULTS.json'),JSON.stringify(cases,null,2)+'\n');
await writeFile(resolve(qa,'ENGINE_RESULTS.json'),JSON.stringify({date:'2026-10-27',checks,summary,
 htmlSHA256:sha(html),caseDigest:sha(Buffer.from(JSON.stringify(cases))),consumerChanged:false,wholeBookApplied:false,wholeCatalogueCompleted:false},null,2)+'\n');
console.log(JSON.stringify({checks:checks.length,...summary}));
