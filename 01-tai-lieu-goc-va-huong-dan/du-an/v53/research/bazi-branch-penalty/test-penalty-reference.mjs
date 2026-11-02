import assert from'node:assert/strict';import fs from'node:fs';import{createHash}from'node:crypto';
import{SOURCE_ID,FRAME_ID,sourcePenaltyCoordinate as coordinate,sourcePenaltyOrdinal as ordinal,sourcePenaltyEntryClause as entry,sourcePenaltyLiteralEntry as literal,sourcePenaltyControlExample as control,sourceFourSelfBranches as four}from'./penalty-reference.mjs';
const b=import.meta.dirname,sha=x=>createHash('sha256').update(x).digest('hex'),read=n=>JSON.parse(fs.readFileSync(`${b}/${n}`,'utf8'));
for(const x of read('PREIMPLEMENTATION_FREEZE.json').files){const bytes=fs.readFileSync(`${b}/${x.file}`);assert.equal(bytes.length,x.bytes);assert.equal(sha(bytes),x.sha256);}
const e=read('EXPECTED_BEFORE_IMPLEMENTATION.json'),base={sourceID:SOURCE_ID,frameID:FRAME_ID},branches=[...'子丑寅卯辰巳午未申酉戌亥'],stems=[...'甲乙丙丁戊己庚辛壬癸'],cycle=Array.from({length:60},(_,i)=>stems[i%10]+branches[i%12]),complete=(x,a)=>x===null?a:[x],quantify=a=>a.every(Boolean)?true:a.every(x=>!x)?false:null;
const nullKeys=['calendarDate','fullFormation','effectivePenalty','wholePatternEstablished','healthRisk','rankPrediction','outcome'];let nullInvariants=0;
function safe(r){assert(r);for(const k of nullKeys){assert.equal(r[k],null);nullInvariants++;}assert.equal(r.sourceEntryCalculated,false);assert.equal(r.sourceEfficacyValidated,false);assert.equal(r.appliedToNatalChart,false);assert(Object.isFrozen(r));}
let coordinateFrames=0,positiveEdges=0;
for(const voice of ['primary','san-che-yi-lan'])for(const a of [...branches,null])for(const b of [...branches,null]){
 const expected=quantify(complete(a,branches).flatMap(x=>complete(b,branches).map(y=>e.directedPositiveTokens.includes(x+y))));
 const r=coordinate({...base,classificationVoice:voice,leftOccurrence:'A',rightOccurrence:'B',leftBranch:a,rightBranch:b});assert.equal(r.nominalDirectedCoordinate,expected);assert.equal(r.wholeThreeBranchGroupRequired,null);assert.equal(r.alternativeIsCorrection,false);
 assert.equal(r.sourceClassLabel,a===null||b===null?null:(voice==='primary'?e.primaryLabels:e.alternativeLabels)[a+b]??null);safe(r);coordinateFrames++;if(voice==='primary'&&expected===true)positiveEdges++;
}
assert.equal(coordinateFrames,338);assert.equal(positiveEdges,12);
assert.equal(coordinate({...base,classificationVoice:'primary',leftOccurrence:'A',rightOccurrence:'A',leftBranch:'辰',rightBranch:'辰'}),null);
for(const voice of ['primary','san-che-yi-lan'])assert.equal(coordinate({...base,classificationVoice:voice,leftOccurrence:'A',rightOccurrence:'B',leftBranch:'巳',rightBranch:'寅'}).nominalDirectedCoordinate,false);
for(const [rowID,sequence]of Object.entries(e.sourceOrdinalSequences)){
 const r=ordinal({...base,rowID});assert.equal(r.inclusiveCount,10);assert.equal(r.sourceInclusiveCount,10);assert.equal(r.from,[...sequence][0]);assert.equal(r.to,[...sequence].at(-1));assert.equal([...sequence].length,10);assert.equal(r.formulaAdoptedForUnlistedPairs,false);safe(r);
}
let entryFrames=0;
for(const direction of ['host-to-guest','guest-to-host'])for(const full of [true,false,null])for(const entered of [true,false,null]){
 const wanted=full===true&&entered!==null?e.entryLabels.find(x=>x.direction===direction&&x.entry===entered).sourceLabel:null;
 const r=entry({...base,sourceDirection:direction,fullThreePenaltyDeclared:full,entryDeclared:entered});assert.equal(r.selectedBaseHistoricalLabel,wanted);assert.equal(r.fuJuContextEvaluated,false);assert.equal(r.taishuiInvolvementCalculated,false);safe(r);entryFrames++;
}
let literalFrames=0,literalPositive=0;
for(const a of [...cycle,null])for(const b of [...cycle,null]){
 const expected=quantify(complete(a,cycle).flatMap(x=>complete(b,cycle).map(y=>x==='乙丑'&&Object.hasOwn(e.literalEntryTargets,y))));
 const r=literal({...base,sourceAnchorPillar:a,sourceTargetPillar:b});assert.equal(r.literalExampleCoordinate,expected);assert.equal(r.literalSourceEntry,a==='乙丑'&&Object.hasOwn(e.literalEntryTargets,b)?e.literalEntryTargets[b]:null);assert.equal(r.generalEntryRuleEstablished,false);safe(r);literalFrames++;if(expected===true)literalPositive++;
}
assert.equal(literalFrames,3721);assert.equal(literalPositive,5);
const controlQuery=(a,b,c)=>control({...base,sourceYearPillar:a,sourceDayPillar:b,sourceHourPillar:c});const exact=e.sourceControlExample;let roleFrames=0;
for(let slot=0;slot<3;slot++)for(const p of [...cycle,null]){
 const values=[...exact];values[slot]=p;const r=controlQuery(...values);assert.equal(r.literalThreeRoleExample,p===null?null:p===exact[slot]);assert.equal(r.actualHistoricalDateEstablished,false);assert.equal(r.sourceControlActuallyEffective,null);safe(r);roleFrames++;
}
for(let mask=0;mask<8;mask++){
 const args=exact.map((p,i)=>mask&(1<<i)?null:p),r=controlQuery(...args);assert.equal(r.literalThreeRoleExample,mask===0?true:null);safe(r);roleFrames++;
}
for(const swap of [[exact[1],exact[0],exact[2]],[exact[0],exact[2],exact[1]],[exact[2],exact[1],exact[0]]]){assert.equal(controlQuery(...swap).literalThreeRoleExample,false);roleFrames++;}
const permute=a=>a.length===0?['']:a.flatMap((x,i)=>permute([...a.slice(0,i),...a.slice(i+1)]).map(t=>x+t)),validOrders=new Set(permute([...e.fourSelfPermutation]));assert.equal(validOrders.size,24);
function fourOracle(slots){const compatible=[...validOrders].filter(s=>slots.every((x,i)=>x===null||x===s[i]));return compatible.length===0?false:slots.includes(null)?null:true;}
let knownFourFrames=0,positiveComplete=0,unknownFourFrames=0;
function checkFour(slots){const wanted=fourOracle(slots);for(const suppress of [true,false,null]){const r=four({...base,sourceSlots:slots,beneficSuppressorDeclared:suppress});assert.equal(r.fourDistinctSourceBranchPremise,wanted);const combined=wanted===false||suppress===false?false:wanted===true&&suppress===true?true:null;assert.equal(r.sourceCompletenessAndDeclaredBenefic,combined);assert.equal(r.equivalentToRepeatedSameBranch,false);safe(r);}return wanted;}
for(const a of branches)for(const b of branches)for(const c of branches)for(const d of branches){if(checkFour([a,b,c,d])===true)positiveComplete++;knownFourFrames++;}
for(const a of [...e.fourSelfPermutation,null])for(const b of [...e.fourSelfPermutation,null])for(const c of [...e.fourSelfPermutation,null])for(const d of [...e.fourSelfPermutation,null])if([a,b,c,d].includes(null)){checkFour([a,b,c,d]);unknownFourFrames++;}
assert.equal(knownFourFrames,20736);assert.equal(positiveComplete,24);assert.equal(unknownFourFrames,369);
let unsupported=0;
for(const fn of [coordinate,ordinal,entry,literal,control,four])for(const input of [null,[],{},new Date(),{...base,sourceID:'current-folklore'},{...base,frameID:'all-natal-branches'}]){assert.equal(fn(input),null);unsupported++;}
assert.equal(ordinal({...base,rowID:'all-pairs-ten'}),null);unsupported++;
const good={...base,classificationVoice:'primary',leftOccurrence:'A',rightOccurrence:'B',leftBranch:'寅',rightBranch:'巳'};
for(const key of ['gender','health','birthYear','dayMaster']){assert.equal(coordinate({...good,[key]:true}),null);unsupported++;}
assert.equal(coordinate({...good,[Symbol('extra')]:1}),null);unsupported++;
let invalid=0;
for(const bad of ['戍',undefined,1,false,'寅巳']){assert.throws(()=>coordinate({...good,leftBranch:bad}),RangeError);invalid++;}
for(const bad of [undefined,'yes',1]){assert.throws(()=>entry({...base,sourceDirection:'host-to-guest',fullThreePenaltyDeclared:bad,entryDeclared:true}),TypeError);invalid++;}
for(const bad of ['乙子',undefined,'乙丑日']){assert.throws(()=>literal({...base,sourceAnchorPillar:bad,sourceTargetPillar:'庚戌'}),RangeError);invalid++;}
for(const bad of [[],new Array(4),['辰','午','酉'],'辰午酉亥']){assert.throws(()=>four({...base,sourceSlots:bad,beneficSuppressorDeclared:true}),TypeError);invalid++;}
const actual=read('ACTUAL_RUNTIME.json');assert(actual.rows.every(x=>x.actual===x.expected));assert.equal(actual.actualNewNaYinQueries,8);assert.equal(actual.reusedNaYinQueries,1);assert.equal(actual.entryRuleGeneralized,false);
const comparisons=Object.fromEntries(actual.comparisons.map(x=>[x.target,x]));assert.equal(comparisons['庚戌'].ordinarySameElement,true);assert.equal(comparisons['丙戌'].ordinaryGenerationEitherDirection,true);assert.equal(comparisons['壬戌'].ordinaryGenerationEitherDirection,true);assert.equal(comparisons['戊戌'].ordinaryAnchorOvercomesTarget,true);assert.equal(comparisons['甲戌'].ordinaryTargetOvercomesAnchor,true);
const result={passed:true,groups:9,frozenFiles:6,coordinateFrames,nominalDirectedEdges:positiveEdges,namedClassificationVoices:2,ordinalRows:6,entryFrames,literalFrames,literalPositiveCases:literalPositive,roleFrames,knownFourFrames,positiveCompleteFourPermutations:positiveComplete,unknownFourFrames,threeValuedFourFrames:(knownFourFrames+unknownFourFrames)*3,nullInvariants,unsupportedRequests:unsupported,invalidInputs:invalid,retainedActualNewNaYinQueries:8,reusedNaYinQueries:1,newEngineCallsDuringTests:0,wholeChapterApplied:false,consumerChanged:false};
if(process.argv.includes('--write-results'))fs.writeFileSync(`${b}/REFERENCE_RESULTS.json`,JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result));
