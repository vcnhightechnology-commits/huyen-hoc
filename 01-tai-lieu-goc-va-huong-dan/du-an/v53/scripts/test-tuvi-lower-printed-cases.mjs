import assert from'node:assert/strict';import{readFileSync,writeFileSync}from'node:fs';import{resolve}from'node:path';import{createHash}from'node:crypto';
import{PRINTED_CASE_SOURCE as system,printedCase,comparePrintedCase as compare}from'../research/tuvi-lower-printed-cases/printed-case-reference.mjs';
const b=resolve(import.meta.dirname,'../research/tuvi-lower-printed-cases'),w=resolve(b,'../../..'),read=n=>JSON.parse(readFileSync(resolve(b,n),'utf8').replace(/^\uFEFF/,'')),sha=buffer=>createHash('sha256').update(buffer).digest('hex'),table=read('MANUAL_PRINTED_CASES.json'),runtime=read('INITIAL_ACTUAL_RUNTIME.json'),checks=[],records=[];
const check=(name,fn)=>{fn();checks.push({name,ok:true});};
check('Frozeninitialsourceanddirectimagecorrectionpreserve27clearmajorcoordinatesandoneunresolvedlabel',()=>{
 const freeze=read('TRANSCRIPTION_FREEZE.json'),initial=read('INITIAL_TRANSCRIPTION_FREEZE.json');assert.equal(sha(readFileSync(resolve(b,freeze.file))),freeze.sha256);assert.equal(initial.actualHHCTuviCallsAtFreeze,0);assert.equal(initial.actualIztroNatalCallsAtFreeze,0);assert.equal(sha(readFileSync(resolve(b,initial.file.replace('MANUAL_','INITIAL_MANUAL_')))),initial.sha256);
 assert.equal(table.records.reduce((n,x)=>n+Object.values(x.majorBranches).filter(Boolean).length,0),27);assert.equal(table.records[0].majorBranches['天梁'],null);
 assert.equal(table.records[1].majorBranches['廉貞'],'戌');assert.equal(read('INITIAL_MANUAL_PRINTED_CASES.json').records[1].majorBranches['廉貞'],'子');
});
check('TwoactualHHCandtwoactualiztrobyLunarchartsreassessedwithoutnewcalls match38sourcecoordinatesperengine',()=>{
 assert.equal(runtime.actualHHCTuviCalls,2);assert.equal(runtime.actualIztroNatalCalls,2);assert.equal(runtime.engineSHA256,sha(readFileSync(resolve(w,'v53/engine.js'))));
 for(const row of table.records){
  const old=runtime.records.find(x=>x.caseID===row.id),hhc=compare({system,caseID:row.id,projection:old.hhcProjection}),iztro=compare({system,caseID:row.id,projection:old.iztroProjection});
  assert.equal(hhc.mismatches.length,0);assert.equal(iztro.mismatches.length,0);assert.equal(hhc.matches,row.id==='ma-zhou-left'?18:20);assert.equal(iztro.matches,hhc.matches);
  const date=old.iztroSolar.split('-').map(Number);assert.deepEqual(date,[old.hhcSolar.y,old.hhcSolar.m,old.hhcSolar.d]);
  records.push({...old,initialHhcComparison:old.hhcComparison,initialIztroComparison:old.iztroComparison,hhcComparison:hhc,iztroComparison:iztro});
 }
 assert.equal(records.reduce((n,x)=>n+x.hhcComparison.matches,0),38);assert.equal(records.reduce((n,x)=>n+x.iztroComparison.matches,0),38);
});
check('Modernmechanicalyears/ordinarymontharedeclaredtests,notbiographicaldateoroutcomeverification',()=>{
 assert.deepEqual(table.records.map(x=>x.sourceYearPillar),['己卯','癸卯']);assert.deepEqual(table.records.map(x=>x.modernTestYear),[1939,1963]);assert.deepEqual(table.records.map(x=>x.sourceCucNumber),[6,4]);
 for(const row of table.records){const x=records.find(x=>x.caseID===row.id);assert.equal(x.fullHistoricalDateAttributed,false);assert.equal(x.input.leap,false);assert.equal(x.input.calendar,'lunar');assert.equal(x.input.tz,8);assert.equal(x.input.gender,'male');assert.equal(x.input.hour,row.hourCenter);assert.equal(x.hhcComparison.historicalBirthDateEstablished,false);assert.equal(x.hhcComparison.sourcePredictionValidated,false);}
});
check('Oneknownmismatchandunknownprojectionareexposedwithoutinventingtheunreadsourceglyph',()=>{
 const row=table.records[0],p=structuredClone(records[0].hhcProjection);p.majorBranches['紫微']='子';p.majorBranches['天機']=null;const x=compare({system,caseID:row.id,projection:p});assert.equal(x.mismatches.length,1);assert.equal(x.coordinates.find(x=>x.id==='major:天機').status,'projection-unknown');assert.equal(x.coordinates.find(x=>x.id==='major:天梁').status,'source-unresolved');assert.equal(x.practicalOutcome,null);
 const copy=printedCase({system,caseID:row.id});copy.majorBranches['紫微']='亥';assert.equal(printedCase({system,caseID:row.id}).majorBranches['紫微'],'辰');
});
check('Strictinputframeandunchangedconsumersitekeeptheresearchcomparisonprivate',()=>{
 const projection=records[0].hhcProjection,base={system,caseID:table.records[0].id,projection};for(const o of[{...base,system:'all'},{...base,caseID:'unknown'},{...base,extra:true},{...base,projection:{...projection,cucNumber:'6'}},{...base,projection:{...projection,majorBranches:{...projection.majorBranches,'天梁':'Giáp'}}}])assert.throws(()=>compare(o),TypeError);
 assert.throws(()=>printedCase({system,caseID:table.records[0].id,[Symbol('extra')]:true}),TypeError);
 const html=readFileSync(resolve(w,'v53/Huyen_Hoc_Cac.html'));assert.equal(html.length,707411);assert(html.equals(readFileSync(resolve(w,'Huyen_Hoc_Cac.html'))));assert(html.equals(readFileSync(resolve(w,'v53/site/index.html'))));assert(!html.includes(Buffer.from(system)));
});
writeFileSync(resolve(w,'v53/qa/tuvi-lower-printed-cases/REFERENCE_RESULTS.json'),JSON.stringify({date:'2026-10-28',checks,currentInvocationNewHHCTuviCalls:0,currentInvocationNewIztroCalls:0,reusesImmutableRuntime:true,actualScopeHHCTuviCalls:2,actualScopeIztroNatalCalls:2,matchedSourceCoordinateFieldsPerEngine:38,individualEngineSourceChecks:76,clearMajorCoordinates:27,unresolvedMajorCoordinates:1,sourceMingLabels:2,sourceCucLabels:2,sourceTransformationCoordinates:7,manualCoordinateCorrections:1,sourceBiographicalDateEstablished:false,sourceOutcomesValidated:false,records,consumerChanged:false,wholeCatalogueCompleted:false},null,2)+'\n');console.log(JSON.stringify({checksPassed:checks.length,actualScopeHHC:2,actualScopeIztro:2,newChartCallsThisInvocation:0,matchedPerEngine:38,individualChecks:76,manualCoordinateCorrections:1}));
