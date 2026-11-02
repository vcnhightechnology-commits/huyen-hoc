import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {resolve} from 'node:path';import {createHash} from 'node:crypto';
import assert from 'node:assert/strict';import vm from 'node:vm';
import {sourceTimingCoordinates} from '../research/liuyao-b03-volume5/timing-reference.mjs';
import {catalogue,compile} from '../research/liuyao-foundations/liuyao-reference.mjs';
import {firePhaseAtBranch} from '../research/liuyao-b03-boundaries/named-jie-reference.mjs';
const root=resolve(import.meta.dirname,'..'),base=resolve(root,'research/liuyao-b03-volume5'),
 qa=resolve(root,'qa/liuyao-b03-volume5'),archive=resolve(root,'../archives/v53-before-liuyao-b03-volume5');
const read=async p=>JSON.parse(await readFile(p,'utf8')),sha=(b,a='sha256')=>createHash(a).update(b).digest('hex');
const checks=[];function test(name,fn){fn();checks.push({name,ok:true});console.log('PASS',name);}
const acquisition=await read(resolve(base,'ACQUISITION.json')),requests=await read(resolve(base,'REQUESTS.json')),
 api=await read(resolve(base,'b03-book3-commons-api.json')),manual=await read(resolve(base,'MANUAL_READINGS.json')),
 units=await read(resolve(base,'VOLUME5_UNITS.json')),source=await read(resolve(base,'TIMING_CLAUSES.json')),
 clauses=await read(resolve(base,'OPERATIONAL_CLAUSES.json')),container=await read(resolve(base,'PDF_CONTAINER_CHECKS.json'));
for(const r of requests.records){const b=await readFile(resolve(base,r.file));
 assert.equal(r.status,200);assert.equal(r.tls.authorized,true);assert.equal(b.length,r.bytes);assert.equal(sha(b),r.sha256);assert.equal(sha(b,'sha1'),r.sha1);}
const pdf=await readFile(resolve(base,acquisition.file)),page=Object.values(api.query.pages)[0];
test('Previously staged API/raw PDF retained exactly with two authorized HTTPS bodies, no redownload',()=>{
 assert.equal(requests.records.length,2);assert.equal(pdf.length,56939817);assert.equal(sha(pdf),acquisition.sha256);
 assert.equal(acquisition.sha256,'01859340e519ffb68a1f40996af73aa7f40beb10a723a7a2a070985201874c61');
 assert.equal(sha(pdf,'sha1'),page.imageinfo[0].sha1);assert.equal(page.imageinfo[0].size,pdf.length);
 assert.equal(page.revisions[0].revid,1004714434);assert.equal(container.pages,67);assert.equal(container.textLayerPages,0);
 assert.equal(container.encrypted,false);assert.equal(manual.counts.newHTTPBodiesThisHeartbeat,0);
});
for(const r of [...manual.records,...manual.QAOnlyImages])assert.equal(sha(await readFile(resolve(base,r.image))),r.sha256);
test('24 actual content readings, four complete section spans and one partial; crop not counted as another page',()=>{
 assert.deepEqual(manual.records.map(r=>r.pdfPage),Array.from({length:24},(_,i)=>i+2));
 assert.equal(manual.counts.inheritedPendingContentImages,7);assert.equal(manual.counts.newContentRendersThisHeartbeat,17);
 assert.equal(manual.QAOnlyImages.length,1);assert.equal(manual.QAOnlyImages[0].pdfPage,8);
 assert.equal(units.firstPassCompleteRelevantSpanUnits,4);assert.equal(units.partialSpanUnits,1);
 assert.deepEqual(units.units.map(u=>u.heading),['天時','年時','國朝','征戰','身命']);
 assert.equal(units.units.at(-1).firstPassRelevantSpanComplete,false);assert.equal(units.fullTextualVolumeRead,false);
});
test('Four timing methods keep context tomb and own changed tomb separate; source conditions and historical claims retained',()=>{
 assert.equal(source.methods.length,4);assert.equal(source.methods.find(m=>m.id==='enters-context-tomb').target,'clash-tomb');
 assert.equal(source.methods.find(m=>m.id==='self-change-tomb').target,'clash-subject');
 assert.equal(source.allTimingPremisesCompiled,false);assert.equal(source.meteorologicalPredictionAccuracyEstablished,false);
 assert.equal(clauses.clauses.length,14);assert(clauses.clauses.some(c=>c.id==='life-horizon-quotation'));
 assert(clauses.clauses.every(c=>!c.consumerApplied&&!c.historicalOutcomesValidated));
});
const ctx={};ctx.window=ctx;vm.createContext(ctx);vm.runInContext(await readFile(resolve(root,'engine.js'),'utf8'),ctx);
const E=ctx.HHC_ENGINE,cat=catalogue();let hhcCalls=0;
const syntheticResults=[];
const cast=[7,7,7,9,9,7], staticCast=[7,7,7,7,7,7], common={sourceContext:'weather-timing-paragraph',useLine:4,startDayGanZhi:'甲戌'};
test('Same synthetic fire line 午 to 戌 yields 辰 for contextual tomb but 子 for its own transformed tomb',()=>{
 const chart=compile(cast);assert.equal(chart.lines[3].branch,'午');assert.equal(chart.lines[3].changed.branch,'戌');
 const phase=firePhaseAtBranch('戌');
 assert.equal(phase.phase,'墓');
 assert.equal(phase.coordinateEvidence,'derived-from-printed-order-and-forward-rule');
 assert.equal(phase.functionalEffect,null); // inherited coordinate, not an efficacy or literal-cell claim
 const a=sourceTimingCoordinates(cast,{...common,method:'enters-context-tomb',tombBranch:'戌',tombPremiseConfirmed:true});
 const b=sourceTimingCoordinates(cast,{...common,method:'self-change-tomb',tombBranch:'戌',tombPremiseConfirmed:true});
 assert.equal(a.targetBranch,'辰');assert.equal(b.targetBranch,'子');
 assert.equal(a.cycleCandidates[0].offsetDays,6);assert.equal(b.cycleCandidates[0].offsetDays,2);
 const c=sourceTimingCoordinates(cast,{...common,method:'moving-no-other-cause',noOtherCauseConfirmed:true});
 const d=sourceTimingCoordinates(staticCast,{...common,method:'static-combined',combinationConfirmed:true});
 assert.equal(c.targetBranch,'未');assert.equal(d.targetBranch,'子');
 for(const r of [a,b,c,d]){
  assert.equal(E.hexNumber(r.chart.input),r.chart.primary.number);
  assert.equal(E.hexNumber(r.chart.changed.bits.map(b=>b?7:8)),r.chart.changed.number);hhcCalls+=2;
  assert.equal(r.predictedEvent,null);assert.equal(r.callerPremisesIndependentlyVerified,false);
  syntheticResults.push({syntheticNotPrintedCast:true,result:r});
 }
 assert.equal(hhcCalls,8);
});
test('Missing source premises do not generate dates; wrong actual motion or own changed branch refutes the selected method',()=>{
 const unresolved=sourceTimingCoordinates(cast,{...common,method:'self-change-tomb'});
 assert.equal(unresolved.premiseStatus,'unresolved-premises');assert.equal(unresolved.targetBranch,null);assert.equal(unresolved.cycleCandidates,null);
 const falseTomb=sourceTimingCoordinates(cast,{...common,method:'self-change-tomb',tombBranch:'丑',tombPremiseConfirmed:true});
 assert.equal(falseTomb.premiseStatus,'premises-not-satisfied');assert.equal(falseTomb.targetBranch,null);
 const wrong=sourceTimingCoordinates(staticCast,{...common,method:'moving-no-other-cause',noOtherCauseConfirmed:true});
 assert.equal(wrong.premiseStatus,'premises-not-satisfied');
 const no=sourceTimingCoordinates(cast,{...common,method:'moving-no-other-cause',noOtherCauseConfirmed:false});
 assert.equal(no.cycleCandidates,null);
 const noAnchor=sourceTimingCoordinates(cast,{sourceContext:common.sourceContext,useLine:4,method:'moving-no-other-cause',noOtherCauseConfirmed:true});
 assert.equal(noAnchor.targetBranch,'未');assert.equal(noAnchor.cycleCandidates,null);assert.equal(noAnchor.gregorianDates,null);
});
const branches=[...'子丑寅卯辰巳午未申酉戌亥'],stems=[...'甲乙丙丁戊己庚辛壬癸'];
// Independent arithmetic partner and periodic position oracle. Not the implementation's table lookup/filter.
const combineIndex=[1,0,11,10,9,8,7,6,5,4,3,2];
const representatives=branches.map(b=>{for(const c of cat){const v=c.bits.map(x=>x?7:8),r=compile(v),line=r.lines.find(l=>l.branch===b);
 if(line)return{branch:b,values:v,line:line.line,number:c.number};}throw Error('missing branch');});
test('Twelve representative source branch coordinates executed in actual HHC engine once each',()=>{
 for(const r of representatives){assert.equal(E.hexNumber(r.values),r.number);hhcCalls++;}
 assert.equal(hhcCalls,20);
});
let contexts=0,candidates=0;const graph=createHash('sha256');
test('2880 source-coordinate contexts agree with independent branch arithmetic and five periodic sexagenary positions',()=>{
 for(let day=0;day<60;day++)for(let branch=0;branch<12;branch++)for(const method of source.methods){
  const r=representatives[branch],v=r.values.slice();
  if(method.motion==='moving')v[r.line-1]=v[r.line-1]===7?9:6;
  const changed=compile(v).lines[r.line-1].changed;
  const tomb=method.requiresOwnChangedBranchEqualsExplicitTomb?changed.branch:branches[day%12];
  const facts={sourceContext:common.sourceContext,method:method.id,useLine:r.line,
   [method.requiresBoolean]:true,startDayGanZhi:stems[day%10]+branches[day%12]};
  if(method.target==='clash-tomb'||method.requiresOwnChangedBranchEqualsExplicitTomb)facts.tombBranch=tomb;
  const result=sourceTimingCoordinates(v,facts);
  const index=method.target==='combine-subject'?combineIndex[branch]
   :((method.target==='clash-tomb'?branches.indexOf(tomb):branch)+6)%12;
  const first=(index-day%12+12)%12, offsets=Array.from({length:5},(_,i)=>first+12*i);
  assert.equal(result.targetBranch,branches[index]);assert.equal(result.premiseStatus,'explicit-premises-present');
  assert.deepEqual(result.cycleCandidates.map(c=>c.offsetDays),offsets);
  assert.deepEqual(result.cycleCandidates.map(c=>c.ganZhi),offsets.map(o=>stems[(day+o)%10]+branches[(day+o)%12]));
  assert.equal(result.fullTimingAdjudication,null);assert.equal(result.meteorologicalForecast,null);
  assert.equal(result.allOtherSourceCausesChecked,false);assert.equal(result.gregorianDates,null);
  graph.update(JSON.stringify([day,branch,method.id,index,offsets])+'\n');contexts++;candidates+=offsets.length;
 }
 assert.equal(contexts,2880);assert.equal(candidates,14400);
});
test('Explicit domain, selected line, known method and typed premises required; no cross-domain or coercion fallback',()=>{
 for(const context of [{...common,sourceContext:'personal-fate',method:'self-change-tomb'},
  {...common,useLine:0,method:'static-combined'},{...common,method:'all-causes'},
  {...common,method:'self-change-tomb',tombPremiseConfirmed:1},
  {...common,method:'self-change-tomb',tombBranch:'戌亥'},
  {...common,method:'self-change-tomb',startDayGanZhi:'甲丑'},
  {...common,method:'self-change-tomb',strength:'strong'}])assert.throws(()=>sourceTimingCoordinates(cast,context));
 assert.throws(()=>sourceTimingCoordinates([7,7,7,7,7],{...common,method:'static-combined'}));
 assert.throws(()=>sourceTimingCoordinates(cast,{...common,method:'self-change-tomb'},null));
 const before=JSON.stringify(cast);sourceTimingCoordinates(cast,{...common,method:'self-change-tomb'});assert.equal(JSON.stringify(cast),before);
});
const old=await read(resolve(archive,'PACKAGE_MANIFEST.json')),html=await readFile(resolve(root,'Huyen_Hoc_Cac.html'));
for(const f of old.files.filter(f=>!f.file.includes('/')&&/\.(js|css)$/.test(f.file)||/research\/liuyao-[^/]+\/.*reference\.mjs$/.test(f.file)))
 assert.equal(sha(await readFile(resolve(root,f.file))),f.sha256);
test('Consumer and nine earlier private references preserved; new source data is absent from site',()=>{
 assert.equal(html.length,707411);assert.equal(sha(html),old.product.sha256);
 for(const x of ['TIMING_CLAUSES.json','timing-reference.mjs','B03-book3'])assert.equal(html.includes(Buffer.from(x)),false);
});
await mkdir(qa,{recursive:true});const summary={actualHHCHexCalls:hhcCalls,syntheticSourceMethodCases:4,
 privateCoordinateContexts:contexts,sexagenaryCoordinateCandidates:candidates,graphDigest:graph.digest('hex'),
 sourceTimingMethods:4,boundedOperationalClauses:14,manualContentPages:24,completeFirstPassSectionSpans:4,partialSectionSpans:1};
await writeFile(resolve(qa,'SOURCE_CASE_RESULTS.json'),JSON.stringify({date:'2026-10-27',syntheticResults,
 historicalCastsReconstructed:false,historicalOutcomesValidated:false},null,2)+'\n');
await writeFile(resolve(qa,'ENGINE_RESULTS.json'),JSON.stringify({date:'2026-10-27',checks,summary,
 htmlSHA256:sha(html),consumerChanged:false,wholeBookApplied:false},null,2)+'\n');
console.log(JSON.stringify({checks:checks.length,...summary}));
