import {readFileSync} from 'node:fs';
const manual=JSON.parse(readFileSync(new URL('./MANUAL_SPATIAL_CLAUSES.json',import.meta.url),'utf8'));
export const SOURCE_ID=manual.sourceID;
const tri=x=>x===false||x===true||x===null;
const and=(a,b)=>a===false||b===false?false:a===true&&b===true?true:null;
const or=(a,b)=>a===true||b===true?true:a===false&&b===false?false:null;
const exact=(x,keys)=>{if(!x||Object.getPrototypeOf(x)!==Object.prototype||Reflect.ownKeys(x).length!==keys.length||keys.some(k=>!Object.hasOwn(x,k)))throw TypeError('Exact explicit source-premise fields required.');};
const checkTri=xs=>{if(!xs.every(tri))throw TypeError('Every premise requires true, false or explicit null.');};
const bounds=()=>({sourceClaimsAreHistorical:true,sourceMonthBoundary:null,sourceLeapMonthPolicy:null,
 sourceCalendarDate:null,computedStarLocations:null,modernPlanCoordinates:null,
 overallSourceVerdict:null,practicalFireRisk:null,practicalOutcome:null,
 wholeSourceMethodApplied:false,consumerApplied:false});
export function inspectMonthlyDuhuo(x){
 exact(x,['sourceID','frameID','monthlyDatouCoLocation','wholeAnnualBingDingArrival','noMaleficConfirmed']);
 if(x.sourceID!==SOURCE_ID||x.frameID!=='declared-monthly-location-context')return null;
 checkTri([x.monthlyDatouCoLocation,x.wholeAnnualBingDingArrival,x.noMaleficConfirmed]);
 const trigger=or(x.monthlyDatouCoLocation,x.wholeAnnualBingDingArrival);
 return Object.freeze({sourceID:SOURCE_ID,clauseID:'monthly-duhuo',sourcePosition:241,
  textualFireTriggerCondition:trigger,separateNoMaleficNonObstructionClaim:x.noMaleficConfirmed,
  simultaneousClauseClaimsNeedReview:trigger===true&&x.noMaleficConfirmed===true,
  annualBingDingClauseSplit:false,noMaleficInferredFromSelectedTriggers:false,
  sourceTriggerJoin:'explicit-source-or',...bounds()});
}
export function inspectMonthlyDailyDatou(x){
 exact(x,['sourceID','frameID','monthlyLabel','counterpartLayer','dailyDatouCoLocation']);
 if(x.sourceID!==SOURCE_ID||x.frameID!=='declared-monthly-daily-location-context'||x.counterpartLayer!=='daily'||!['月遊火','飛天獨火'].includes(x.monthlyLabel))return null;
 checkTri([x.dailyDatouCoLocation]);
 return Object.freeze({sourceID:SOURCE_ID,clauseID:'monthly-daily-datou',sourcePosition:245,
  monthlyLabel:x.monthlyLabel,counterpartLayer:'daily',textualFireTriggerCondition:x.dailyDatouCoLocation,
  dailyCounterpartSubstituted:false,...bounds()});
}
export function inspectOneBeneficArrival(x){
 exact(x,['sourceID','frameID','actor','activity','affectedPlaceConfirmed','candidateSetComplete','observations']);
 const actors=manual.records.find(r=>r.id==='one-benefic-arrival').actors;
 if(x.sourceID!==SOURCE_ID||x.frameID!=='declared-monthly-direction-repair-context'||!actors.includes(x.actor)||x.activity!=='repair-at-declared-place')return null;
 checkTri([x.affectedPlaceConfirmed,x.candidateSetComplete]);
 // 64 is an API input bound, never a claimed source star count.
 if(!Array.isArray(x.observations)||x.observations.length>64||Reflect.ownKeys(x.observations).length!==x.observations.length+1)throw TypeError('Dense bounded observation list required.');
 const seen=new Set(),records=[];
 for(const o of x.observations){
  exact(o,['id','eligibleBeneficConfirmed','atAffectedPlaceConfirmed']);
  if(typeof o.id!=='string'||!/^[-a-zA-Z0-9_]{1,64}$/.test(o.id)||seen.has(o.id))throw TypeError('Unique explicit observation IDs required.');
  checkTri([o.eligibleBeneficConfirmed,o.atAffectedPlaceConfirmed]);seen.add(o.id);
  records.push(Object.freeze({...o,qualifyingArrival:and(o.eligibleBeneficConfirmed,o.atAffectedPlaceConfirmed)}));
 }
 const witnessed=records.filter(r=>r.qualifyingArrival===true).map(r=>r.id);
 const uncertain=records.some(r=>r.qualifyingArrival===null);
 const any=witnessed.length?true:uncertain||x.candidateSetComplete!==true?null:false;
 return Object.freeze({sourceID:SOURCE_ID,clauseID:'one-benefic-arrival',sourcePosition:245,actor:x.actor,
  observations:Object.freeze(records),witnessedArrivalIDs:Object.freeze(witnessed),
  qualifyingArrivalExists:any,localNonObstructionClaim:and(x.affectedPlaceConfirmed,any),
  existenceAbsenceNeedsCompleteAssessment:true,assessmentCompletenessDerived:false,
  namedStarMembershipDerived:false,genericBeneficSubstitutes:false,
  sourceQuantifier:'其中但得一位',...bounds()});
}
