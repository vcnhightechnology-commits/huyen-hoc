/** Private source-text coordinates and explicit predicates, without natal inference. */
import{readFileSync}from'node:fs';
const t=JSON.parse(readFileSync(new URL('./MANUAL_TABLES.json',import.meta.url),'utf8'));
export const SOURCE_ID=t.sourceID,FRAME_ID=t.frameID;
const branches=t.branches,stems=[...'甲乙丙丁戊己庚辛壬癸'];
const own=(o,k)=>Object.prototype.hasOwnProperty.call(o,k);
function frame(o,keys){return o!==null&&typeof o==='object'&&!Array.isArray(o)&&[Object.prototype,null].includes(Object.getPrototypeOf(o))&&keys.every(k=>own(o,k))&&Reflect.ownKeys(o).every(k=>keys.includes(k))&&o.sourceID===SOURCE_ID&&o.frameID===FRAME_ID;}
function branch(v){if(v!==null&&!branches.includes(v))throw new RangeError('Explicit canonical branch or null required; source glyph normalization is documented, not automatic.');}
const possibilities=v=>v===null?branches:[v];
function gate(a,b,test){branch(a);branch(b);const results=new Set(possibilities(a).flatMap(x=>possibilities(b).map(y=>test(x,y))));return results.size===1?[...results][0]:null;}
function withheld(){return{anchorPillar:null,calendarDate:null,natalOutcome:null,disaster:null,medicalRisk:null,personality:null,genderInference:null,strength:null,effectiveHarm:null,priority:null,wholePatternEstablished:null,sourceEfficacyValidated:false,appliedToNatalChart:false};}
export function sourceHarmPair(o){
 if(!frame(o,['sourceID','frameID','anchorBranch','otherBranch']))return null;
 const a=o.anchorBranch,b=o.otherBranch;
 const nominal=gate(a,b,(x,y)=>t.pairs.some(p=>x!==y&&p.branches.includes(x)&&p.branches.includes(y)));
 const exact=t.directedClauses.find(r=>r.anchor===a&&r.other===b),cause=t.causalRows.find(r=>r.anchor===a&&r.other===b);
 const mechanical=gate(a,b,(x,y)=>t.unionPartners[y]===t.clashPartners[x]);
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,nominalSixHarmPair:nominal,directedSourceWording:exact?.wording??null,
  sourceCausalRowListed:a===null||b===null?null:Boolean(cause),sourceListedClash:cause?.clash??null,editorialUnionWithClashCoordinate:mechanical,
  causalExplanationIsEffectiveHarm:false,directionOverriddenByMechanicalRule:false,...withheld()});
}
export function sourceHarmDeclaredPremise(o){
 if(!frame(o,['sourceID','frameID','clauseID','anchorBranch','otherBranch','sourcePremise']))return null;
 const clause=t.conditions.find(c=>c.id===o.clauseID);if(!clause)return null;
 if(![true,false,null].includes(o.sourcePremise))throw new TypeError('Source predicate must be explicitly true, false or null.');
 const pair=gate(o.anchorBranch,o.otherBranch,(a,b)=>clause.allowedOrderedPairs.some(([x,y])=>a===x&&b===y));
 const combined=pair===false||o.sourcePremise===false?false:pair===true&&o.sourcePremise===true?true:null;
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,clauseID:clause.id,pairCoordinateGate:pair,declaredSourcePredicate:o.sourcePremise,
  sourceCoordinateAndDeclaredPremise:combined,sourcePredicateCalculated:false,...withheld()});
}
function pillar(v){if(v===null)return;if(typeof v!=='string'||[...v].length!==2)throw new RangeError('Canonical sexagenary pillar or null required.');const [a,b]=[...v],i=stems.indexOf(a),j=branches.indexOf(b);if(i<0||j<0||i%2!==j%2)throw new RangeError('Canonical sexagenary pillar or null required.');}
export function sourceHarmLiteralExample(o){
 if(!frame(o,['sourceID','frameID','anchorPillar','otherPillar']))return null;
 pillar(o.anchorPillar);pillar(o.otherPillar);const e=t.literalExample;
 const a=o.anchorPillar===null?null:o.anchorPillar===e.anchorPillar,b=o.otherPillar===null?null:o.otherPillar===e.otherPillar;
 const match=a===false||b===false?false:a===true&&b===true?true:null;
 const held=withheld();delete held.anchorPillar;
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,matchesLiteralExample:match,sourceTrueElementLabels:match===true?Object.freeze([...e.trueElementLabels]):null,
  trueElementSystemEstablished:false,naYinElementsInferred:false,ordinaryStemElementsInferred:false,...held});
}
