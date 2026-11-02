/** Selected quoted old-method comparisons, not a unique use-god selector. */
import{readFileSync}from'node:fs';const t=JSON.parse(readFileSync(new URL('./MANUAL_SOURCE_CLAUSES.json',import.meta.url),'utf8'));
export const SOURCE_ID=t.sourceID,FRAME_ID=t.frameID;
const fields=['candidateID','declaredUse','sourceStrength','sourceMotion','sourceMonthBroken','sourceVoid','sourceInjured'];
const own=(o,k)=>Object.prototype.hasOwnProperty.call(o,k);
function exact(o,keys){return o!==null&&typeof o==='object'&&!Array.isArray(o)&&[Object.prototype,null].includes(Object.getPrototypeOf(o))&&keys.every(k=>own(o,k))&&Reflect.ownKeys(o).every(k=>keys.includes(k));}
const choices=(x,all)=>x===null?all:[x],quantify=v=>v.every(Boolean)?true:v.every(x=>!x)?false:null,and3=(a,b)=>a===false||b===false?false:a===null||b===null?null:true;
export function compareQuotedOldMethod(o){
 if(!exact(o,['sourceID','frameID','candidates'])||o.sourceID!==SOURCE_ID||o.frameID!==FRAME_ID)return null;
 if(!Array.isArray(o.candidates)||o.candidates.length!==2||[0,1].some(i=>!own(o.candidates,i))||Reflect.ownKeys(o.candidates).some(k=>!['0','1','length'].includes(k)))return null;
 if(o.candidates.some(c=>!exact(c,fields))||o.candidates.some(c=>!['A','B'].includes(c.candidateID))||o.candidates[0].candidateID===o.candidates[1].candidateID)return null;
 const [a,b]=o.candidates;
 for(const c of o.candidates){
  if(!['旺相','休囚',null].includes(c.sourceStrength)||!['動','靜',null].includes(c.sourceMotion))throw new RangeError('Explicit source strength/motion category or null required.');
  for(const key of ['declaredUse','sourceMonthBroken','sourceVoid','sourceInjured'])if(![true,false,null].includes(c[key]))throw new TypeError('Explicit source boolean premise or null required.');
 }
 const declared=and3(a.declaredUse,b.declaredUse);
 const rows=t.rules.map(r=>{
  const domain=[r.discard,r.prefer],possible=choices(a[r.field],domain).flatMap(x=>choices(b[r.field],domain).map(y=>({a:x===r.prefer&&y===r.discard,b:y===r.prefer&&x===r.discard})));
  const rawA=quantify(possible.map(x=>x.a)),rawB=quantify(possible.map(x=>x.b));
  return Object.freeze({clauseID:r.id,sourcePDFPage:r.page,sourceLayer:t.sourceLayer,literal:r.literal,leftCandidate:a.candidateID,rightCandidate:b.candidateID,
   rawCriterionPrefersLeft:rawA,rawCriterionPrefersRight:rawB,declaredTwoUsesAndPrefersLeft:and3(declared,rawA),declaredTwoUsesAndPrefersRight:and3(declared,rawB)});
 });
 const left=rows.filter(r=>r.declaredTwoUsesAndPrefersLeft===true).map(r=>r.clauseID),right=rows.filter(r=>r.declaredTwoUsesAndPrefersRight===true).map(r=>r.clauseID);
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,declaredTwoUsesPremise:declared,comparisons:Object.freeze(rows),knownLeftCriteria:Object.freeze(left),knownRightCriteria:Object.freeze(right),knownPreferenceDirectionsConflict:left.length>0&&right.length>0,
  unresolvedCriterionIDs:Object.freeze(rows.filter(r=>r.declaredTwoUsesAndPrefersLeft===null||r.declaredTwoUsesAndPrefersRight===null).map(r=>r.clauseID)),
  sourceCounterexamples:Object.freeze(t.counterexamples.map(r=>Object.freeze({...r}))),sourcePredicatesWereDeclared:true,predicateStrengthOrCalendarCalculated:false,
  unifiedRankingEstablished:false,authorAdoptsOldMethodUnconditionally:false,counterexampleOverridesCalculated:false,threeUsesReducedToTwo:false,selectedUseCandidate:null,
  calendarDate:null,effectiveVoid:null,effectiveMonthBreak:null,predictedEvent:null,healthOutcome:null,sourceHistoricalOutcomesValidated:false,consumerApplied:false});
}
