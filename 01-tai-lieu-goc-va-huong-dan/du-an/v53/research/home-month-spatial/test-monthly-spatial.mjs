import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,existsSync} from 'node:fs';
import {resolve,dirname} from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';
import {SOURCE_ID,inspectMonthlyDuhuo as fire,inspectMonthlyDailyDatou as daily,inspectOneBeneficArrival as arrival} from './monthly-spatial-reference.mjs';
const b=dirname(fileURLToPath(import.meta.url));let w=b;while(!existsSync(resolve(w,'v53/engine.js'))){const up=dirname(w);assert.notEqual(up,w);w=up;}
const read=n=>JSON.parse(readFileSync(resolve(b,n),'utf8')),hash=p=>createHash('sha256').update(readFileSync(p)).digest('hex');
let groups=0,nulls=0,invalid=0,unsupported=0,frames=0;const test=f=>{f();groups++;};
const expected=read('EXPECTED_BEFORE_IMPLEMENTATION.json'),frozen=read('PREIMPLEMENTATION_FREEZE.json'),reuse=read('REUSE_IDENTITIES.json');
const oldActivity=await import(pathToFileURL(resolve(w,'v53/research/home-activity-clauses/activity-clause-reference.mjs')).href);
const unknown=['sourceMonthBoundary','sourceLeapMonthPolicy','sourceCalendarDate','computedStarLocations','modernPlanCoordinates','overallSourceVerdict','practicalFireRisk','practicalOutcome'];
function bounds(r){assert.ok(Object.isFrozen(r));for(const k of unknown){assert.equal(r[k],null);nulls++;}assert.equal(r.consumerApplied,false);assert.equal(r.wholeSourceMethodApplied,false);}
test(()=>{for(const r of [...frozen.files,...reuse.files]){const p=resolve(w,r.file);assert.equal(readFileSync(p).length,r.bytes);assert.equal(hash(p),r.sha256);}});
test(()=>{for(const c of expected.fireFrames){const snapshot=JSON.stringify(c.input),r=fire(c.input);assert.equal(r.textualFireTriggerCondition,c.expectedActivationCondition);assert.equal(r.separateNoMaleficNonObstructionClaim,c.expectedSeparateNoMaleficClaim);assert.equal(r.sourceTriggerJoin,'explicit-source-or');assert.equal(JSON.stringify(c.input),snapshot);bounds(r);frames++;}});
test(()=>{for(const c of expected.dailyFrames){const r=daily({sourceID:SOURCE_ID,frameID:'declared-monthly-daily-location-context',monthlyLabel:c.label,counterpartLayer:'daily',dailyDatouCoLocation:c.coLocation});assert.equal(r.textualFireTriggerCondition,c.expectedActivationCondition);bounds(r);frames++;}});
test(()=>{for(const c of expected.arrivalCases){const before=JSON.stringify(c.input),r=arrival(c.input);assert.equal(r.localNonObstructionClaim,c.expectedLocalClaim);assert.equal(JSON.stringify(c.input),before);assert.ok(Object.isFrozen(r.observations));assert.ok(r.observations.every(Object.isFrozen));bounds(r);frames++;}});
const tri=[false,null,true],base=expected.arrivalCases[0].input;
test(()=>{for(const actor of ['飛宮','地軸','帝舍','帝車','帝輅'])for(const complete of tri)for(const affected of tri)for(const a of tri)for(const l of tri)for(const a2 of tri)for(const l2 of tri){
 const obs=[{id:'a',eligibleBeneficConfirmed:a,atAffectedPlaceConfirmed:l},{id:'b',eligibleBeneficConfirmed:a2,atAffectedPlaceConfirmed:l2}],x={...base,actor,candidateSetComplete:complete,affectedPlaceConfirmed:affected,observations:obs},r=arrival(x);
 assert.deepEqual(arrival({...x,observations:[...obs].reverse()}).witnessedArrivalIDs.slice().sort(),r.witnessedArrivalIDs.slice().sort());assert.equal(arrival({...x,observations:[...obs].reverse()}).localNonObstructionClaim,r.localNonObstructionClaim);
 const positive=obs.some(o=>o.eligibleBeneficConfirmed===true&&o.atAffectedPlaceConfirmed===true);
 if(positive){assert.equal(r.qualifyingArrivalExists,true);assert.equal(r.localNonObstructionClaim,affected);}
 if(complete!==true&&!positive)assert.equal(r.qualifyingArrivalExists,null);
 if(affected===false)assert.equal(r.localNonObstructionClaim,false);
 if(r.localNonObstructionClaim===true){assert.equal(affected,true);assert.ok(positive);}
 bounds(r);frames++;
}});
test(()=>{const allFalse=Array.from({length:64},(_,i)=>({id:`f${i}`,eligibleBeneficConfirmed:false,atAffectedPlaceConfirmed:true})),one={id:'true-one',eligibleBeneficConfirmed:true,atAffectedPlaceConfirmed:true};
 assert.equal(arrival({...base,candidateSetComplete:true,observations:allFalse}).qualifyingArrivalExists,false);
 assert.equal(arrival({...base,candidateSetComplete:false,observations:[...allFalse.slice(0,63),one]}).qualifyingArrivalExists,true);
 assert.equal(arrival({...base,candidateSetComplete:null,observations:[]}).qualifyingArrivalExists,null);
 const unknownMember={id:'unknown',eligibleBeneficConfirmed:null,atAffectedPlaceConfirmed:true};assert.equal(arrival({...base,candidateSetComplete:true,observations:[unknownMember]}).qualifyingArrivalExists,null);
});
test(()=>{const fireBase=expected.fireFrames[0].input,dailyBase={sourceID:SOURCE_ID,frameID:'declared-monthly-daily-location-context',monthlyLabel:'月遊火',counterpartLayer:'daily',dailyDatouCoLocation:true};
 const unsupportedCases=[[fire,{...fireBase,frameID:'declared-monthly-daily-location-context'}],[fire,{...fireBase,sourceID:'P08'}],[daily,{...dailyBase,counterpartLayer:'monthly'}],[daily,{...dailyBase,monthlyLabel:'月獨火'}],[daily,{...dailyBase,frameID:'declared-monthly-location-context'}],[arrival,{...base,actor:'打頭火'}],[arrival,{...base,activity:'new-build'}],[arrival,{...base,frameID:'numeric-lunar-month'}]];
 for(const [fn,x]of unsupportedCases){assert.equal(fn(x),null);unsupported++;}
 const bad=[[fire,null],[fire,{}],[fire,{...fireBase,monthlyDatouCoLocation:1}],[fire,{...fireBase,wholeAnnualBingDingArrival:'丙'}],[fire,{...fireBase,extra:true}],[daily,{...dailyBase,dailyDatouCoLocation:undefined}],[arrival,{...base,candidateSetComplete:'yes'}],[arrival,{...base,observations:[base.observations[0],base.observations[0]]}],[arrival,{...base,observations:Array(2)}],[arrival,{...base,observations:Array.from({length:65},(_,i)=>({...base.observations[0],id:`x${i}`}))}],[arrival,{...base,observations:[{...base.observations[0],genericBenefic:true}]}],[arrival,{...base,observations:[{...base.observations[0],id:' '}]}],[arrival,{...base,observations:[{...base.observations[0],eligibleBeneficConfirmed:1}]}]];
 const symbolic={...base,[Symbol('hidden')]:true};bad.push([arrival,symbolic]);
 for(const [fn,x]of bad){assert.throws(()=>fn(x),TypeError);invalid++;}
});
test(()=>{const modulePath=resolve(w,'v53/research/home-activity-clauses/activity-clause-reference.mjs'),before=hash(modulePath);const old=oldActivity.sourceActivityClause({sourceID:oldActivity.SOURCE_ID,frameID:oldActivity.FRAME_ID,clauseID:'wantong-fire',activity:'start-building',markerStatus:true,beneficPresent:true});
 assert.equal(old.localAvoidance,true);assert.equal(old.overallSuitability,null);
 const r=arrival(base);assert.equal(r.localNonObstructionClaim,true);assert.equal(r.overallSourceVerdict,null);assert.equal(hash(modulePath),before);
});
const result={passed:true,groups,frozenFiles:frozen.files.length,declaredPremiseFrames:frames,sourcePrintedExamples:0,nullInvariants:nulls,unsupportedRequests:unsupported,invalidInputs:invalid,sourceUnits:3,monthlyActorLabels:5,priorWantongFireNonInterference:true,newEngineCallsDuringTests:0,newCalendarObjects:0,newHTTPBodies:0,consumerChanged:false,wholeSourceMethodApplied:false};
if(process.argv.includes('--write-results'))writeFileSync(resolve(b,'REFERENCE_RESULTS.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result));
