import assert from'node:assert/strict';import fs from'node:fs';import{createHash}from'node:crypto';
import{SOURCE_ID,FRAME_ID,sourceClashCoordinate as clash,sourceClashLiteralExample as literal,sourceClashCompleteGroup as group,sourceYuJingClashDirection as direction,sourceLuClashExample as lu}from'./clash-reference.mjs';
const b=import.meta.dirname,sha=x=>createHash('sha256').update(x).digest('hex'),read=n=>JSON.parse(fs.readFileSync(`${b}/${n}`,'utf8'));
for(const x of read('PREIMPLEMENTATION_FREEZE.json').files){const raw=fs.readFileSync(`${b}/${x.file}`);assert.equal(raw.length,x.bytes);assert.equal(sha(raw),x.sha256);}
const e=read('EXPECTED_BEFORE_IMPLEMENTATION.json'),base={sourceID:SOURCE_ID,frameID:FRAME_ID},branches=[...'子丑寅卯辰巳午未申酉戌亥'],stems=[...'甲乙丙丁戊己庚辛壬癸'],cycle=Array.from({length:60},(_,i)=>stems[i%10]+branches[i%12]),choices=(x,all)=>x===null?all:[x],quantify=a=>a.every(Boolean)?true:a.every(x=>!x)?false:null;
const nullKeys=['calendarDate','calendarFeasibility','effectiveClash','fullPattern','overallGoodBad','medicalRisk','morality','rankPrediction'];let nullInvariants=0;
function safe(r){assert(r);for(const k of nullKeys){assert.equal(r[k],null);nullInvariants++;}assert.equal(r.sourceEfficacyValidated,false);assert.equal(r.appliedToNatalChart,false);assert(Object.isFrozen(r));}
let clashFrames=0,positiveClashes=0;
for(const a of [...branches,null])for(const b of [...branches,null]){
 const wanted=quantify(choices(a,branches).flatMap(x=>choices(b,branches).map(y=>e.directedClashTokens.includes(x+y))));
 const r=clash({...base,leftOccurrence:'A',rightOccurrence:'B',leftBranch:a,rightBranch:b});assert.equal(r.nominalClash,wanted);assert.equal(r.sourceSevenPositionCoordinate,wanted);assert.equal(r.sourceGeneralAdverseVerdictPermitted,false);if(wanted===true){assert.equal(r.forwardInclusiveCount,7);positiveClashes++;}safe(r);clashFrames++;
}
assert.equal(clashFrames,169);assert.equal(positiveClashes,12);
let literalFrames=0,literalPositive=0;
for(const a of [...cycle,null])for(const b of [...cycle,null]){
 const wanted=quantify(choices(a,cycle).flatMap(x=>choices(b,cycle).map(y=>Object.hasOwn(e.printedExamples,x+y))));
 const r=literal({...base,sourceAnchorPillar:a,sourceOtherPillar:b});assert.equal(r.literalExampleCoordinate,wanted);assert.equal(r.sourceRelationLabel,a===null||b===null?null:e.printedExamples[a+b]??null);safe(r);literalFrames++;if(wanted===true)literalPositive++;
}
assert.equal(literalFrames,3721);assert.equal(literalPositive,4);
const permutations=a=>a.length===0?['']:a.flatMap((x,i)=>permutations([...a.slice(0,i),...a.slice(i+1)]).map(t=>x+t));
let knownGroupFrames=0,unknownGroupFrames=0,completeGroupPermutations=0;
for(const [groupID,token]of Object.entries(e.fourGroups)){
 const truth=permutations([...token]);assert.equal(truth.length,24);
 const inspect=slots=>{const possible=truth.filter(t=>slots.every((x,i)=>x===null||x===t[i]));const want=possible.length===0?false:slots.includes(null)?null:true;const r=group({...base,groupID,sourceSlots:slots});assert.equal(r.sourceCompletenessPremise,want);assert.equal(r.sourceLiteralSaysNotTreatAsOrdinaryClash,want);assert.equal(r.completeGreatPatternEstablished,null);safe(r);return want;};
 for(const a of branches)for(const b of branches)for(const c of branches)for(const d of branches){if(inspect([a,b,c,d])===true)completeGroupPermutations++;knownGroupFrames++;}
 for(const a of [...token,null])for(const b of [...token,null])for(const c of [...token,null])for(const d of [...token,null])if([a,b,c,d].includes(null)){inspect([a,b,c,d]);unknownGroupFrames++;}
}
assert.equal(knownGroupFrames,41472);assert.equal(completeGroupPermutations,48);assert.equal(unknownGroupFrames,738);
assert.equal(group({...base,groupID:'four-stores',sourceSlots:[...'辰戌丑未']}),null);
let directionFrames=0;
for(const image of ['吉象','凶象',null])for(const self of ['用神','閒神',null])for(const other of ['用神','閒神',null]){
 const want=quantify(choices(self,['用神','閒神']).flatMap(a=>choices(other,['用神','閒神']).map(b=>a==='用神'&&b==='閒神'))),r=direction({...base,declaredImage:image,selfRole:self,otherRole:other});assert.equal(r.sourceRolePremise,want);assert.equal(r.sourceDesiredDirection,want===true&&image!==null?e.declaredDirection[image]:null);assert.equal(r.qiAndSupportEvaluated,false);safe(r);directionFrames++;
}
let luFrames=0;
for(const a of [...stems,null])for(const b of [...branches,null])for(const c of [...branches,null]){
 const want=quantify(choices(a,stems).flatMap(x=>choices(b,branches).flatMap(y=>choices(c,branches).map(z=>x==='甲'&&y==='寅'&&z==='申'))));const r=lu({...base,sourceAnchorStem:a,sourceLuBranch:b,seenBranch:c});assert.equal(r.literalLuClashCoordinate,want);assert.equal(r.wholeLuBreakingEffect,null);assert.equal(r.yearDayAnchorAutomaticallyChosen,false);safe(r);luFrames++;
}
assert.equal(luFrames,1859);
let unsupported=0;for(const fn of [clash,literal,group,direction,lu])for(const input of [null,[],{},new Date(),{...base,sourceID:'ordinary-good-bad'},{...base,frameID:'day-master'}]){assert.equal(fn(input),null);unsupported++;}
const good={...base,leftOccurrence:'A',rightOccurrence:'B',leftBranch:'子',rightBranch:'午'};
for(const extra of ['gender','birthDate','morality','priority']){assert.equal(clash({...good,[extra]:true}),null);unsupported++;}assert.equal(clash({...good,leftOccurrence:'A',rightOccurrence:'A'}),null);unsupported++;assert.equal(clash({...good,[Symbol('x')]:true}),null);unsupported++;
let invalid=0;for(const bad of ['戍',undefined,2,false,'子午']){assert.throws(()=>clash({...good,leftBranch:bad}),RangeError);invalid++;}
for(const bad of ['甲丑',undefined,false,'甲子日']){assert.throws(()=>literal({...base,sourceAnchorPillar:bad,sourceOtherPillar:'甲午'}),RangeError);invalid++;}
for(const bad of [[],new Array(4),'寅申巳亥',[...'寅申巳']]){assert.throws(()=>group({...base,groupID:'four-birth',sourceSlots:bad}),TypeError);invalid++;}
assert.throws(()=>direction({...base,declaredImage:'good',selfRole:'用神',otherRole:'閒神'}),RangeError);invalid++;
const actual=read('ACTUAL_RUNTIME.json');assert.equal(actual.actualNewNaYinQueries,6);assert.equal(actual.reusedNaYinQueries,2);assert.equal(actual.reusedClashQueries,12);assert(actual.rows.every(x=>x.expected===x.actual));assert(actual.reusedClashes.every(x=>x.expected===x.actual));const values=Object.fromEntries([...actual.rows,...actual.reusedNaYin].map(x=>[x.pillar,x.actual]));assert.equal([...values['辛巳']].at(-1),'金');assert.equal([...values['癸亥']].at(-1),'水');assert.equal([...values['壬申']].at(-1),'金');assert.equal([...values['庚寅']].at(-1),'木');assert.equal([...values['甲子']].at(-1),[...values['甲午']].at(-1));assert.equal([...values['己卯']].at(-1),[...values['己酉']].at(-1));
const manual=read('MANUAL_SOURCE_TABLES.json');assert.equal(manual.unresolvedFourStores.literalDigital,e.unresolvedFourStores);assert.equal(manual.unresolvedFourStores.groupImplemented,false);assert.equal(manual.namedBreakings.find(x=>x.id==='horse').glyphRoleUnresolved,true);assert.equal(manual.namedBreakings.find(x=>x.id==='union').fullRuleImplemented,false);
const result={passed:true,groups:9,frozenFiles:6,clashFrames,positiveClashes,literalFrames,literalPositiveCases:literalPositive,knownGroupFrames,unknownGroupFrames,completeGroupPermutations,directionFrames,luFrames,nullInvariants,unsupportedRequests:unsupported,invalidInputs:invalid,retainedActualNewNaYinQueries:6,reusedNaYinQueries:2,reusedClashQueries:12,newEngineCallsDuringTests:0,wholeChapterApplied:false,consumerChanged:false};if(process.argv.includes('--write-results'))fs.writeFileSync(`${b}/REFERENCE_RESULTS.json`,JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result));
