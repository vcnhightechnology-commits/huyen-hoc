import assert from'node:assert/strict';import fs from'node:fs';import{createHash}from'node:crypto';
import{SOURCE_ID,FRAME_ID,sourceHarmPair as pair,sourceHarmDeclaredPremise as premise,sourceHarmLiteralExample as example}from'./harm-reference.mjs';
const b=import.meta.dirname,read=n=>JSON.parse(fs.readFileSync(`${b}/${n}`,'utf8')),sha=x=>createHash('sha256').update(x).digest('hex');
for(const x of read('PREIMPLEMENTATION_FREEZE.json').files){const bytes=fs.readFileSync(`${b}/${x.file}`);assert.equal(bytes.length,x.bytes);assert.equal(sha(bytes),x.sha256);}
const e=read('EXPECTED_BEFORE_IMPLEMENTATION.json'),branches=[...'子丑寅卯辰巳午未申酉戌亥'],withNull=[...branches,null],base={sourceID:SOURCE_ID,frameID:FRAME_ID};
const query=(a,b)=>pair({...base,anchorBranch:a,otherBranch:b});
const nullKeys=['calendarDate','natalOutcome','disaster','medicalRisk','personality','genderInference','strength','effectiveHarm','priority','wholePatternEstablished'];
let invariantCount=0;function safe(r){assert(r);for(const k of nullKeys){assert.equal(r[k],null);invariantCount++;}assert.equal(r.sourceEfficacyValidated,false);assert.equal(r.appliedToNatalChart,false);assert(Object.isFrozen(r));}
const named=new Set(e.nominalPairs.flatMap(x=>[x,[...x].reverse().join('')]));
function allCompletions(a,b,truth){const results=(a===null?branches:[a]).flatMap(x=>(b===null?branches:[b]).map(y=>truth.has(x+y)));return results.every(Boolean)?true:results.every(x=>!x)?false:null;}
let pairFrames=0,positivePairs=0,unknownPairs=0;
for(const a of withNull)for(const b of withNull){const r=query(a,b),want=allCompletions(a,b,named);assert.equal(r.nominalSixHarmPair,want);assert.equal(r.editorialUnionWithClashCoordinate,want);safe(r);pairFrames++;if(want===true)positivePairs++;if(want===null)unknownPairs++;}
assert.equal(pairFrames,169);assert.equal(positivePairs,12);assert.equal(unknownPairs,25);
assert.equal(query('酉','戌').directedSourceWording,e.directedException['酉戌']);assert.equal(query('戌','酉').directedSourceWording,e.directedException['戌酉']);assert.equal(query('戌','酉').nominalSixHarmPair,true);assert.equal(query('戌','酉').effectiveHarm,null);
assert.equal(query('未','子').directedSourceWording,null);assert.equal(query('卯','辰').directedSourceWording,null);assert.equal(query('辰','卯').directedSourceWording,'source-harm-wording');assert.equal(query('寅','巳').directedSourceWording,null);
for(const [a,c,b]of e.causalRows){const r=query(a,b);assert.equal(r.sourceCausalRowListed,true);assert.equal(r.sourceListedClash,c);assert.equal(r.editorialUnionWithClashCoordinate,true);assert.equal(r.directionOverriddenByMechanicalRule,false);assert.equal(r.causalExplanationIsEffectiveHarm,false);}
assert.equal(query(null,'戌').sourceCausalRowListed,null);
const conditionOracles={'chou-wu-true-ghost':new Set(['丑午']),'yin-si-travel-ghost':new Set(['寅巳','巳寅']),'chen-mao-true-ghost':new Set(['辰卯']),'shen-hai-nayin-overcoming':new Set(['申亥','亥申'])};
let premiseFrames=0,unknownPremises=0,positivePremises=0;
for(const [id,truth]of Object.entries(conditionOracles))for(const a of withNull)for(const b of withNull)for(const p of [true,false,null]){
 const r=premise({...base,clauseID:id,anchorBranch:a,otherBranch:b,sourcePremise:p}),coordinate=allCompletions(a,b,truth);
 const completions=(coordinate===null?[true,false]:[coordinate]).flatMap(x=>(p===null?[true,false]:[p]).map(y=>x&&y));
 const want=completions.every(Boolean)?true:completions.every(x=>!x)?false:null;
 assert.equal(r.pairCoordinateGate,coordinate);assert.equal(r.sourceCoordinateAndDeclaredPremise,want);assert.equal(r.declaredSourcePredicate,p);assert.equal(r.sourcePredicateCalculated,false);safe(r);premiseFrames++;if(want===null)unknownPremises++;if(want===true)positivePremises++;
}
assert.equal(premiseFrames,2028);assert.equal(positivePremises,6);
const stems=[...'甲乙丙丁戊己庚辛壬癸'],pillars=Array.from({length:60},(_,i)=>stems[i%10]+branches[i%12]);let literalFrames=0,literalPositive=0;
for(const a of [...pillars,null])for(const b of [...pillars,null]){const r=example({...base,anchorPillar:a,otherPillar:b});const want=a!==null&&a!=='乙酉'||b!==null&&b!=='戊戌'?false:a===null||b===null?null:true;assert.equal(r.matchesLiteralExample,want);assert.equal(r.trueElementSystemEstablished,false);assert.equal(r.naYinElementsInferred,false);assert.equal(r.ordinaryStemElementsInferred,false);if(want===true){literalPositive++;assert.deepEqual(r.sourceTrueElementLabels,['金','火']);assert(Object.isFrozen(r.sourceTrueElementLabels));}else assert.equal(r.sourceTrueElementLabels,null);safe(r);literalFrames++;}
assert.equal(literalFrames,3721);assert.equal(literalPositive,1);assert.equal(example({...base,anchorPillar:e.negativeReversedExample[0],otherPillar:e.negativeReversedExample[1]}).matchesLiteralExample,false);
let unsupported=0;const good={...base,anchorBranch:'子',otherBranch:'未'};
for(const input of [null,[],new Date(),{},Object.create({sourceID:SOURCE_ID,frameID:FRAME_ID,anchorBranch:'子',otherBranch:'未'}),{...good,sourceID:'generic'},{...good,frameID:'calendar'},{...good,birthYear:2026},{...good,sex:'female'},{...good,unknown:undefined},{...good,[Symbol('extra')]:1}]){assert.equal(pair(input),null);unsupported++;}
for(const fn of [premise,example]){assert.equal(fn(good),null);unsupported++;}
assert.equal(premise({...base,clauseID:'auto-true-ghost',anchorBranch:'子',otherBranch:'未',sourcePremise:true}),null);unsupported++;
let invalid=0;for(const bad of [undefined,'戍','Zi','',0,false,new String('子')]){assert.throws(()=>query(bad,'未'),RangeError);invalid++;}
for(const bad of [undefined,'yes',1,{},[]]){assert.throws(()=>premise({...base,clauseID:'chou-wu-true-ghost',anchorBranch:'丑',otherBranch:'午',sourcePremise:bad}),TypeError);invalid++;}
for(const bad of ['乙戌','乙酉日','乙戍','yi-you',0]){assert.throws(()=>example({...base,anchorPillar:bad,otherPillar:'戊戌'}),RangeError);invalid++;}
const actual=read('ACTUAL_RUNTIME.json');assert(actual.clashes.every(x=>x.expected===x.actual));assert(actual.pillars.every(x=>x.actualNaYin===x.naYin&&x.actualStemElement===x.stemElement));assert.equal(actual.actualNewClashQueries+actual.actualNewNaYinQueries+actual.actualNewStemElementQueries,16);assert.equal(actual.sourceTrueMetalFireMeaningAdjudicated,false);
const result={passed:true,groups:9,frozenFiles:5,pairFrames,positiveNominalOrderedPairs:positivePairs,unknownPairFrames:unknownPairs,directedExceptionPreserved:true,causalRows:6,premiseFrames,positiveDeclaredPremiseFrames:positivePremises,unknownDeclaredPremiseFrames:unknownPremises,literalFrames,literalPositiveCases:literalPositive,nullInvariants:invariantCount,unsupportedRequests:unsupported,invalidInputs:invalid,retainedActualNewTableQueries:16,reusedUnionQueries:12,newEngineCallsDuringTests:0,wholeChapterApplied:false,consumerChanged:false};
if(process.argv.includes('--write-results'))fs.writeFileSync(`${b}/REFERENCE_RESULTS.json`,JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result));
