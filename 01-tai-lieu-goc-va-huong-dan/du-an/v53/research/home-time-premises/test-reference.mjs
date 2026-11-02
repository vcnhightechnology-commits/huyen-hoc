import assert from'node:assert/strict';
import{readFileSync,writeFileSync}from'node:fs';
import{resolve,basename}from'node:path';
import{createHash}from'node:crypto';
import{REPAIR_SYSTEM,EXAMPLE_SYSTEM,sourceLocalRepairScope as local,sourcePrintedMonthlySite as site}from'./repair-scope-reference.mjs';
const b=import.meta.dirname,w=process.cwd(),read=p=>JSON.parse(readFileSync(p,'utf8').replace(/^\uFEFF/,'')),hash=p=>createHash('sha256').update(readFileSync(p)).digest('hex'),checks=[];
const check=(name,fn)=>{fn();checks.push({name,ok:true});};
const clauses=read(resolve(b,'MANUAL_CLAUSES.json')),freeze=read(resolve(b,'TRANSCRIPTION_FREEZE.json')),base={system:REPAIR_SYSTEM,clause:'qiu-angdao',monthBasis:'declared-source-month',operation:'repair-existing',occupiedSiteMatch:true,tugongBaiDayException:null,earthworkIncluded:null};
const records=[];
check('Four scoped predicates, four exact printed sites and eight native crops frozen before reference tests',()=>{
 for(const x of freeze.files){const p=resolve(b,basename(x.file));assert.equal(hash(p),x.sha256);assert.equal(readFileSync(p).length,x.bytes);}
 const contexts=read(resolve(b,'CONTEXT_DISPOSITIONS.json'));assert.equal(contexts.sections.length,19);assert.equal(clauses.records.length,4);assert.equal(read(resolve(b,'PRINTED_SITE_EXAMPLES.json')).records.length,4);assert(freeze.beforeFirstReferenceTests);
 const clean=x=>x.replace(/[\s.，。：“”【】○]/g,'').replaceAll('値','值');
 for(const c of clauses.records){const parent=contexts.sections.find(x=>x.id===c.parent);for(const literal of c.selectedLiterals)assert(clean(parent.digitalText).includes(clean(literal)),literal);}
});
check('Existing repair, new build and other operations retain source-local rather than global permission',()=>{
 for(const clause of ['qiu-angdao','monthly-hao']){const x=local({...base,clause});assert.equal(x.localAvoidance,true);records.push(x);assert.equal(local({...base,clause,occupiedSiteMatch:false}).localAvoidance,false);assert.equal(local({...base,clause,occupiedSiteMatch:null}).localAvoidance,null);}
 const qiu=local({...base,operation:'new-build'});assert.equal(qiu.localAvoidance,false);assert.equal(qiu.status,'explicit-new-build-exception');records.push(qiu);
 for(const clause of ['monthly-hao','tugong','youlong-fulong']){const x=local({...base,clause,operation:'new-build'});assert.equal(x.localAvoidance,null);assert.equal(x.status,'operation-not-addressed');records.push(x);}
 for(const operation of ['other','unknown'])assert.equal(local({...base,operation}).localAvoidance,null);
});
check('Tugong exception needs its own declared day, while Youlong additionally needs declared earthwork',()=>{
 const states=[true,false,null],tugongExpected=[false,true,null],youlongExpected=[[false,true,null],[true,true,true],[null,true,null]];
 for(let i=0;i<3;i++){
  const x=local({...base,clause:'tugong',tugongBaiDayException:states[i]});assert.equal(x.localAvoidance,tugongExpected[i]);records.push(x);
  for(let j=0;j<3;j++){const x=local({...base,clause:'youlong-fulong',tugongBaiDayException:states[i],earthworkIncluded:states[j]});assert.equal(x.localAvoidance,youlongExpected[i][j]);records.push(x);}
 }
 assert.equal(local({...base,clause:'tugong',tugongBaiDayException:true,occupiedSiteMatch:null}).localAvoidance,false);
 assert.equal(local({...base,clause:'youlong-fulong',tugongBaiDayException:true,earthworkIncluded:true,occupiedSiteMatch:null}).localAvoidance,false);
});
let referenceFrames=0,unknownFrames=0;
check('672accepted abstract frames expose missing premises and reject automatic lunar or jieqi month substitution',()=>{
 for(const clause of clauses.records)for(const monthBasis of ['declared-source-month','numeric-lunar-month','solar-term-month','unknown'])for(const operation of ['repair-existing','new-build','other','unknown'])for(const occupiedSiteMatch of [true,false,null])for(const day of clause.hasTugongBaiDayException?[true,false,null]:[null])for(const earth of clause.id==='youlong-fulong'?[true,false,null]:[null]){
  const x=local({...base,clause:clause.id,monthBasis,operation,occupiedSiteMatch,tugongBaiDayException:day,earthworkIncluded:earth});referenceFrames++;
  if(monthBasis!=='declared-source-month'){unknownFrames++;assert.equal(x.localAvoidance,null);assert.equal(x.sourceMonthFrameEstablished,false);}
  for(const k of ['calendarMonthTimestampBoundary','leapMonthPolicy','globalNoJieqiPolicy','overallDateRecommendation','sourceOutcome'])assert.equal(x[k],null);assert.equal(x.consumerApplied,false);
 }
 assert.equal(referenceFrames,672);assert.equal(unknownFrames,504);
});
check('Only four directly printed locations returned, without inventing an annual or twelve-month location table',()=>{
 const rows=read(resolve(b,'PRINTED_SITE_EXAMPLES.json')).records;
 for(const e of rows){const x=site({system:EXAMPLE_SYSTEM,clause:e.clause,yearGanzhi:e.yearGanzhi,monthOrdinal:e.monthOrdinal,monthBasis:'declared-source-month'});assert.equal(x.sourceExampleID,e.id);assert.equal(x.sourceListedSite,e.site);assert.equal(x.fullTwelveMonthTableImplemented,false);records.push(x);}
 for(const yearGanzhi of [null,'乙丑'])assert.equal(site({system:EXAMPLE_SYSTEM,clause:'qiu-angdao',yearGanzhi,monthOrdinal:2,monthBasis:'declared-source-month'}).sourceListedSite,null);
 for(const e of rows)for(const monthBasis of ['numeric-lunar-month','solar-term-month','unknown'])assert.equal(site({system:EXAMPLE_SYSTEM,clause:e.clause,yearGanzhi:e.yearGanzhi,monthOrdinal:e.monthOrdinal,monthBasis}).sourceListedSite,null);
 assert.equal(site({system:EXAMPLE_SYSTEM,clause:'monthly-hao',yearGanzhi:null,monthOrdinal:2,monthBasis:'declared-source-month'}).sourceListedSite,null);
 assert.equal(site({system:EXAMPLE_SYSTEM,clause:'youlong-fulong',yearGanzhi:null,monthOrdinal:1,monthBasis:'declared-source-month'}).sourceListedSite,null);
});
check('Four calendar illustrations reuse an already executed batch and do not establish any monthly source adapter',()=>{
 const cache=read(resolve(b,'CACHED_CALENDAR_COUNTEREXAMPLES.json'));assert.equal(cache.records.length,4);assert.equal(hash(resolve(w,cache.source.file)),cache.source.sha256);
 const original=read(resolve(w,cache.source.file));assert.deepEqual(cache.records,original.boundary.slice(0,4));for(const x of cache.records){assert.notEqual(x.lunarMonth,x.explicitMonthFrame);assert.notEqual(x.numericLunarMonthMarker,x.declaredEngineMonthBranchMarker);assert.equal(x.sourceMonthBasisValidated,false);}
 assert.equal(cache.newCalendarObjects,0);assert.equal(cache.newZhiXingCalls,0);
});
check('Malformed and cross-clause premises rejected, returned evidence isolated and consumer bytes retained',()=>{
 for(const x of [null,{},[],{...base,system:'global'},{...base,clause:'all'},{...base,operation:'renovate'},{...base,occupiedSiteMatch:1},{...base,monthBasis:'lunar'},{...base,tugongBaiDayException:false},{...base,extra:true},Object.create(base),{...base,clause:'tugong',earthworkIncluded:false}])assert.throws(()=>local(x),TypeError);
 const ex={system:EXAMPLE_SYSTEM,clause:'qiu-angdao',yearGanzhi:'甲子',monthOrdinal:2,monthBasis:'declared-source-month'};
 for(const x of [{...ex,yearGanzhi:'甲丑'},{...ex,monthOrdinal:'2'},{...ex,monthOrdinal:0},{...ex,system:'all'},{...ex,extra:true}])assert.throws(()=>site(x),TypeError);
 const x=local(base);x.input.operation='new-build';x.sourcePositions.push(0);assert.equal(local(base).input.operation,'repair-existing');assert(!local(base).sourcePositions.includes(0));
 for(const p of ['Huyen_Hoc_Cac.html','v53/Huyen_Hoc_Cac.html','v53/site/index.html'])assert.equal(hash(resolve(w,p)),'549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857');
});
const out={date:'2026-10-29',checks,records,summary:{completeChecks:checks.length,abstractAcceptedFrames:referenceFrames,unsupportedMonthFramesKeptUnknown:unknownFrames,sectionDispositions:19,selectedClausePredicates:4,printedSiteExamples:4,sourceCoordinateEfficacyEstablished:false,cachedActualCalendarIllustrations:4,newHHCCharts:0,newLunarObjects:0,newLunarZhiXingCalls:0,newIztroCharts:0,consumerChanged:false,wholeSourceMethodApplied:false}};
if(!process.argv.includes('--no-write'))writeFileSync(resolve(b,'REFERENCE_RESULTS.json'),JSON.stringify(out,null,2)+'\n');else assert.deepEqual(read(resolve(b,'REFERENCE_RESULTS.json')),out);console.log(JSON.stringify(out.summary));
