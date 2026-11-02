// Private audit of explicitly declared research premises. Matching local
// source predicates never chooses a whole pattern, strength method or outcome.
import {readFileSync}from'node:fs';
import {sourceBladeCoordinates}from'./coordinate-reference.mjs';
const matrix=JSON.parse(readFileSync(new URL('PREDICATE_MATRIX.json',import.meta.url),'utf8'));
const reserved=new Set(matrix.coordinateFactKeys),registered=new Set(Object.keys(matrix.factRegistry));
const plain=x=>x!==null&&typeof x==='object'&&Object.getPrototypeOf(x)===Object.prototype&&!Object.getOwnPropertySymbols(x).length;
const all=x=>x.includes(false)?false:x.every(v=>v===true)?true:null;
const any=x=>x.includes(true)?true:x.every(v=>v===false)?false:null;
function evaluate(expression,facts){
 if(typeof expression==='string')return facts[expression];
 if(Object.hasOwn(expression,'not')){const x=evaluate(expression.not,facts);return x===null?null:!x;}
 if(Object.hasOwn(expression,'all'))return all(expression.all.map(x=>evaluate(x,facts)));
 if(Object.hasOwn(expression,'any'))return any(expression.any.map(x=>evaluate(x,facts)));
 throw TypeError('Unrecognized retained predicate expression');
}
function terms(expression){
 if(typeof expression==='string')return[expression];
 return Object.values(expression).flatMap(x=>(Array.isArray(x)?x:[x]).flatMap(terms));
}

export function auditSelectedPredicates(context){
 const keys=['system','dayPillar','hourPillar','declaredFacts'];
 if(!plain(context)||Object.keys(context).length!==keys.length||keys.some(k=>!Object.hasOwn(context,k))||Object.keys(context).some(k=>!keys.includes(k)))
  throw TypeError('Explicit named system, canonical day/hour or null, and declaredFacts required');
 if(context.system!==matrix.system||!plain(context.declaredFacts))throw TypeError('Named extracted source and plain research declarations required');
 for(const [key,value]of Object.entries(context.declaredFacts))
  if(!registered.has(key)||reserved.has(key)||![true,false,null].includes(value))throw TypeError('Unrecognized or non-Boolean declaration, or attempt to override a coordinate');
 if(context.declaredFacts.sourceOfficerStrong===true&&context.declaredFacts.sourceOfficerPresent===false)
  throw TypeError('Same-frame 官旺 and explicit 無官 cannot both be declared true');
 const day=sourceBladeCoordinates({system:'TMTH005-ri-ren',candidateDay:context.dayPillar,candidateHour:null});
 const pair=sourceBladeCoordinates({system:'TMTH005-negative-day-hour',candidateDay:context.dayPillar,candidateHour:context.hourPillar});
 const equal=p=>context.dayPillar===null?null:context.dayPillar===p;
 const coordinateFacts={dayIsWuWu:equal('戊午'),dayIsRenZi:equal('壬子'),dayIsBingWu:equal('丙午'),
  dayStemIsWuJi:context.dayPillar===null?null:'戊己'.includes(context.dayPillar[0]),
  listedDayBlade:day.listedCoordinateMatches,listedNegativeDayHour:pair.listedCoordinateMatches};
 const facts=Object.fromEntries([...registered].map(k=>[k,null]));Object.assign(facts,coordinateFacts,context.declaredFacts);
 const rows=matrix.rules.map(rule=>{
  const alternativeMatches=rule.predicateAlternatives.map(e=>evaluate(e,facts));
  const match=alternativeMatches.every(x=>x===alternativeMatches[0])?alternativeMatches[0]:null;
  const referenced=[...new Set(rule.predicateAlternatives.flatMap(terms))];
  return{id:rule.id,sourceSubcontextIDs:[...rule.sourceSubcontextIDs],sourceLocalStance:rule.sourceLocalStance,
   sourceRouteLabel:rule.sourceRouteLabel??null,localPremisesMatch:match,alternativeMatches,
   sourceReadingResolved:rule.sourceReadingResolved??true,
   premises:referenced.map(key=>({key,value:facts[key],basis:reserved.has(key)?'canonical-coordinate':'declared-research-premise',realPersonValidityEstablished:false})),
   unknownPremises:referenced.filter(k=>facts[k]===null),mayQualifyRule:rule.mayQualifyRule??null,
   fullSourceConditionSetEstablished:false,practicalOutcome:null};
 });
 const opposedLocalClaims=[];
 for(const positive of rows.filter(x=>x.localPremisesMatch===true&&x.sourceLocalStance==='positive'))
  for(const negative of rows.filter(x=>x.localPremisesMatch===true&&x.sourceLocalStance==='negative')){
   const parents=x=>x.sourceSubcontextIDs.map(id=>id.split('-')[1]);
   if(!parents(positive).some(x=>parents(negative).includes(x)))continue;
   opposedLocalClaims.push({positiveRule:positive.id,negativeRule:negative.id,
    moreSpecificQualificationCandidate:positive.mayQualifyRule===negative.id,
    sourcePrecedenceEstablished:false,practicalOutcome:null});
  }
 return{system:matrix.system,scope:'explicit-declared-premises-audit-only',coordinateFacts,declaredFacts:structuredClone(context.declaredFacts),rows,opposedLocalClaims,
  sourceOtherPatternRoutePremiseMatched:rows.find(x=>x.id==='other-pattern-priority').localPremisesMatch,
  factsAutomaticallyValidatedForRealPerson:false,sourcePrecedenceEstablished:false,
  fullBladePatternEstablished:null,strength:null,effectiveControlOrCombination:null,usefulGodSelected:null,
  historicalOutcomeValidated:false,practicalOutcome:null,financialResult:null,healthResult:null,lifespan:null,marriageResult:null,
  consumerApplied:false};
}
