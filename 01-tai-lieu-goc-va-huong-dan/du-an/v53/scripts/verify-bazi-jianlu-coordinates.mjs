import{readFile,writeFile,mkdir}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';import{createRequire}from'node:module';import assert from'node:assert/strict';import vm from'node:vm';
import{inspectJianluCoordinates}from'../research/bazi-jianlu-coordinates/jianlu-reference.mjs';
const r=resolve(import.meta.dirname,'..'),w=resolve(r,'..'),b=resolve(r,'research/bazi-jianlu-coordinates'),q=resolve(r,'qa/bazi-jianlu-coordinates'),
 read=async p=>JSON.parse(await readFile(p,'utf8')),sha=data=>createHash('sha256').update(data).digest('hex'),checks=[];
function test(name,fn){fn();checks.push({name,ok:true});console.log('PASS',name);}
const m=await read(resolve(b,'MANUAL_READINGS.json')),rows=(await read(resolve(b,'SOURCE_ROWS.json'))).rows,probe=await read(resolve(b,'PROBE_RESULTS.json')),
 container=await readFile(resolve(b,m.source)),digital=await readFile(resolve(b,m.digitalComparator));
for(const p of m.readings)assert.equal(sha(await readFile(resolve(b,p.file))),p.sha256);
assert.equal(sha(await readFile(resolve(b,m.qaCrop.file))),m.qaCrop.sha256);
test('Retained container/comparator/two expandedimages/crop keepSHA;zero new pages orHTTP',()=>{
 assert.equal(sha(container),m.sourceSHA256);assert.equal(sha(digital),m.digitalSHA256);assert.equal(m.newSourcePages,0);assert.equal(m.newHTTPRequests,0);
 assert.equal(m.readings.length,2);assert(m.readings.every(x=>x.actuallyViewed));assert.equal(m.qaCrop.actuallyViewed,true);
});
const txt=digital.toString(),lo=txt.indexOf('<pb:KR3g0042_WYG_005-113a>'),hi=txt.indexOf('<pb:KR3g0042_WYG_005-114a>'),bounded=txt.slice(lo,hi).replace(/<pb:[^>]+>|¶|\s/g,'');
test('Ten direct source triplets match exact folio113a-b;three己/巳variants explicit;lastrow crossespages',()=>{
 assert.equal(rows.length,10);for(const row of rows)assert(bounded.includes(row.digitalTripletAsRetained),row.digitalTripletAsRetained);
 assert.equal(rows.filter(x=>x.digitalGlyphVariant).length,3);assert.deepEqual(rows.at(-1).sourceImages,[223,224]);
 assert.equal(rows[2].printedHourPillar,'己亥');assert.equal(rows[2].digitalTripletAsRetained,'丙日巳月宜巳亥時');
});
const audit=await read(resolve(r,'research/bazi-late-zi/VERIFICATION.json'));
for(const f of audit.runtime)assert.equal(sha(await readFile(resolve(w,f.file))),f.sha256);
const req=createRequire(import.meta.url),L=req(resolve(w,'v46/node_modules/lunar-typescript'));
test('Actual lunar-typescript1.8.6 runtime has retained audited bytes',()=>{assert.equal(req(resolve(w,'v46/node_modules/lunar-typescript/package.json')).version,'1.8.6');});
const c={};c.window=c;vm.createContext(c);for(const p of ['engine.js','bazi-relations.js'])vm.runInContext(await readFile(resolve(r,p),'utf8'),c);
const E=c.HHC_ENGINE,R=c.HHC_BAZI_RELATIONS,stems='甲乙丙丁戊己庚辛壬癸',branches='子丑寅卯辰巳午未申酉戌亥';
let hhcCalls=0,lunarCalls=0;const sourceFixtures=[],full=[];
test('Ten fixture dates execute120HHC/120Lunar calls over12hours;all fourpillars andday-hour arithmeticagree',()=>{
 for(const row of rows){const f=probe.fixtures.find(x=>x.source.dayStem===row.dayStem);assert(f);
  for(let bi=0;bi<12;bi++){const input={...f.input,hour:2*bi},chart=E.bazi(input);hhcCalls++;
   const native=L.Solar.fromYmdHms(input.y,input.m,input.d,input.hour,input.minute,0).getLunar().getEightChar();native.setSect(2);lunarCalls++;
   const pillars=[native.getYear(),native.getMonth(),native.getDay(),native.getTime()];assert.deepEqual(Array.from(chart.pillars,p=>p.han),pillars);
   assert(pillars[2].startsWith(row.dayStem));assert(pillars[1].endsWith(row.monthBranch));
   const got=inspectJianluCoordinates({sourceContext:'WYG-005-jianlu',dayStem:row.dayStem,monthBranch:row.monthBranch,hourPillar:pillars[3]});
   assert.equal(got.expectedHourAtAssertedBranch,pillars[3]);assert.equal(got.hourDayCompatible,true);assert.equal(got.completeTripleMatched,pillars[3]===row.printedHourPillar);
   full.push({input,pillars});
   if(pillars[3]===row.printedHourPillar){const relations=R.inspect(chart),kill=relations.gods.find(g=>g.name==='Thất Sát');assert(kill);
    const positions=[...kill.positions.visible,...kill.positions.hidden].filter(p=>p.pillarIndex===3);assert(positions.length);
    assert.equal(L.LunarUtil.SHI_SHEN[row.dayStem+stems[positions[0].stem]],'七杀');
    sourceFixtures.push({source:row,input,pillars,sourceCoordinateMatched:got.completeTripleMatched,hourKillPositions:JSON.parse(JSON.stringify(positions)),historicalBirthDate:false});
   }
  }
 }assert.equal(hhcCalls,120);assert.equal(lunarCalls,120);assert.equal(sourceFixtures.length,10);
});
test('Ten source hours all contain explicit stem orhiddenbranch Thất Sát in actualchart;not a favorableverdict',()=>{
 for(const f of sourceFixtures){assert(f.hourKillPositions.length);const x=inspectJianluCoordinates({sourceContext:'WYG-005-jianlu',dayStem:f.source.dayStem,monthBranch:f.source.monthBranch,hourPillar:f.source.printedHourPillar});
  for(const k of ['patternEstablished','strengthEstablished','favorableOutcome','usefulGodSelected'])assert.equal(x[k],null);
  assert.equal(x.modernCalendarBoundarySelected,false);assert.equal(x.consumerApplied,false);}
});
let monthContexts=0;
test('120day-month contexts:onlyten directsource monthcoordinatesmatch;hourabsence staysunknown',()=>{
 for(const row of rows)for(const branch of branches){const x=inspectJianluCoordinates({sourceContext:'WYG-005-jianlu',dayStem:row.dayStem,monthBranch:branch});
  assert.equal(x.monthCoordinateMatched,branch===row.monthBranch);assert.equal(x.hourCoordinateMatched,null);assert.equal(x.hourDayCompatible,null);
  assert.equal(x.completeTripleMatched,branch===row.monthBranch?null:false);monthContexts++;}
 assert.equal(monthContexts,120);
});
test('Unknown,false andinvalidday-hour aredistinct;source丙己亥confirmed andfalse乙亥controlrejected',()=>{
 const ctx={sourceContext:'WYG-005-jianlu',dayStem:'丙'},u=inspectJianluCoordinates(ctx),p=inspectJianluCoordinates({...ctx,monthBranch:'巳',hourPillar:'己亥'}),n=inspectJianluCoordinates({...ctx,monthBranch:'巳',hourPillar:'乙亥'});
 assert.equal(u.monthCoordinateMatched,null);assert.equal(u.completeTripleMatched,null);assert.equal(p.hourDayCompatible,true);assert.equal(p.completeTripleMatched,true);
 assert.equal(n.hourDayCompatible,false);assert.equal(n.completeTripleMatched,false);assert.equal(n.expectedHourAtAssertedBranch,'己亥');
 assert.equal(probe.compatible,10);assert.equal(probe.incompatible,0);assert.equal(probe.sourceEmended,false);
});
test('Strictcontext/sparseinputs andmutation guards preserve retainedsource',()=>{
 const ctx={sourceContext:'WYG-005-jianlu',dayStem:'甲'};
 for(const bad of[null,{},[],{...ctx,dayStem:''},{...ctx,dayStem:'甲乙'},{...ctx,monthBranch:0},{...ctx,hourPillar:'壬'},{...ctx,date:'today'},{...ctx,[Symbol('x')]:true}])assert.throws(()=>inspectJianluCoordinates(bad));
 assert.throws(()=>inspectJianluCoordinates(ctx,null));const x=inspectJianluCoordinates(ctx);x.sourceCoordinate.printedHourPillar='錯';assert.equal(inspectJianluCoordinates(ctx).sourceCoordinate.printedHourPillar,'壬申');
});
const html=await readFile(resolve(r,'Huyen_Hoc_Cac.html'));
test('HTMLunchanged;privatepatternmatcher absentfrom product',()=>{
 assert.equal(html.length,707411);assert.equal(sha(html),'549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857');assert(!html.includes(Buffer.from('jianlu-reference')));
});
await mkdir(q,{recursive:true});await writeFile(resolve(q,'RESULTS.json'),JSON.stringify({date:'2026-10-27',checks,summary:{actualHHCBaziCalls:hhcCalls,actualLunarCalls:lunarCalls,sourceTriplets:10,sourceHourKillContexts:10,privateMonthContexts:monthContexts,expandedPreviouslyReadPages:2,newSourcePages:0,newHTTPRequests:0},sourceFixtures,caseDigest:sha(JSON.stringify(full)),htmlSHA256:sha(html),fullPatternClassifier:false,wholeCatalogueCompleted:false},null,2)+'\n');
