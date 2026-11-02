import assert from'node:assert/strict';import fs from'node:fs';import{createHash}from'node:crypto';
import{SOURCE_ID,FRAME_ID,sourceOfficialRegion as region,sourceTrueOfficialRegion as trueRegion,sourceTrueOfficialGhostDistinction as terminal,sourceTrueGhostLiteralPair as literal}from'./official-context-reference.mjs';
const b=import.meta.dirname,sha=x=>createHash('sha256').update(x).digest('hex'),read=n=>JSON.parse(fs.readFileSync(`${b}/${n}`,'utf8'));
for(const x of read('PREIMPLEMENTATION_FREEZE.json').files){const raw=fs.readFileSync(`${b}/${x.file}`);assert.equal(raw.length,x.bytes);assert.equal(sha(raw),x.sha256);}
const e=read('EXPECTED_BEFORE_IMPLEMENTATION.json'),base={sourceID:SOURCE_ID,frameID:FRAME_ID},stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'],cycle=Array.from({length:60},(_,i)=>stems[i%10]+branches[i%12]);
const nullKeys=['calendarDate','calendarFeasible','realBirthYear','realBirthDay','effectiveTransformation','wholePatternEstablished','sourceOutcome','medicalRisk','wealthPrediction','rankPrediction','strength'];let nullInvariants=0;
function safe(r){assert(r);for(const k of nullKeys){assert.equal(r[k],null);nullInvariants++;}assert.equal(r.appliedToNatalChart,false);assert.equal(r.sourceEfficacyValidated,false);assert.equal(r.trueFiveElementCalculated,false);assert(Object.isFrozen(r));}
const complete=(v,all)=>v===null?all:[v],quantify=arr=>arr.every(Boolean)?true:arr.every(x=>!x)?false:null;
let regionFrames=0,heavenTrue=0,earthTrue=0;
for(const kind of ['heaven','earth'])for(const stem of [...stems,null])for(const branch of [...branches,null]){
 const table=kind==='heaven'?e.heavenExpectedByStem:e.earthExpectedByStem;
 const expected=quantify(complete(stem,stems).flatMap(a=>complete(branch,branches).map(b=>table[a].includes(b))));
 const r=region({...base,region:kind,anchorStem:stem,sourceMonthBranch:branch});assert.equal(r.listedMonthCoordinate,expected);safe(r);regionFrames++;
 if(stem!==null&&branch!==null&&expected===true){if(kind==='heaven')heavenTrue++;else earthTrue++;}
}
assert.equal(regionFrames,286);assert.equal(heavenTrue,20);assert.equal(earthTrue,24);
const expectedMonth=a=>stems[(stems.indexOf(a[0])+5)%10]+branches[(branches.indexOf(a[1])+3)%12];let trueRegionFrames=0,trueRegionPositive=0;
for(const a of [...cycle,null])for(const b of [...cycle,null]){
 const expected=quantify(complete(a,cycle).flatMap(x=>complete(b,cycle).map(y=>expectedMonth(x)===y)));
 const r=trueRegion({...base,sourceMingPillar:a,sourceMonthPillar:b});assert.equal(r.sourceTrueRegionCoordinate,expected);assert.equal(r.editorialCandidateMonthPillar,a===null?null:expectedMonth(a));assert.equal(r.derivedSixtyRowTableIsPrinted,false);safe(r);trueRegionFrames++;if(expected===true)trueRegionPositive++;
}
assert.equal(trueRegionFrames,3721);assert.equal(trueRegionPositive,60);
assert.equal(trueRegion({...base,sourceMingPillar:e.printedTrueRegionExample[0],sourceMonthPillar:e.printedTrueRegionExample[1]}).sourceTrueRegionCoordinate,true);
let terminalFrames=0;
for(const a of [true,false,null])for(const b of [true,false,null]){
 const r=terminal({...base,naYinOvercomeByDeclaredTrueElement:a,originalStemAlsoOvercome:b});assert.equal(r.selectedTerminalSourceLabel,a===true&&b===true?'真鬼':a===true&&b===false?'真官':null);assert.equal(r.appliesAutomaticallyToSixHarm,false);assert.equal(r.completeOfficialMethodEvaluated,false);safe(r);terminalFrames++;
}
for(const row of e.declaredTerminalExamples)assert.equal(terminal({...base,naYinOvercomeByDeclaredTrueElement:row.naYinOvercome,originalStemAlsoOvercome:row.originalStemAlsoOvercome}).selectedTerminalSourceLabel,row.selectedLabel);
let literalFrames=0,literalPositive=0,literalUnknown=0;
const printed=new Set(e.counterexamples.flatMap(x=>[x.anchor+':'+x.seen.join(''),x.anchor+':'+[...x.seen].reverse().join('')]));
for(const p of [...cycle,null])for(const a of [...stems,null])for(const b of [...stems,null]){
 const expected=quantify(complete(p,cycle).flatMap(x=>complete(a,stems).flatMap(y=>complete(b,stems).map(z=>printed.has(x+':'+y+z)))));
 const r=literal({...base,sourceAnchorPillar:p,seenStemPair:[a,b]});assert.equal(r.literalCounterexampleCoordinate,expected);assert.equal(r.pairPresenceIsSufficientForTrueGhost,false);assert.equal(r.sourceTargetPillarRolesEstablished,false);safe(r);literalFrames++;if(expected===true)literalPositive++;if(expected===null)literalUnknown++;
}
assert.equal(literalFrames,7381);assert.equal(literalPositive,8);
let unsupported=0;
for(const fn of [region,trueRegion,terminal,literal])for(const o of [null,[],{},new Date(),{...base,sourceID:'generic-ten-gods'},{...base,frameID:'day-master'}]){assert.equal(fn(o),null);unsupported++;}
const good={...base,region:'heaven',anchorStem:'甲',sourceMonthBranch:'午'};
for(const k of ['birthDate','gender','dayMaster','autoTrueGhost']){assert.equal(region({...good,[k]:true}),null);unsupported++;}
assert.equal(region({...good,[Symbol('extra')]:true}),null);unsupported++;
let invalid=0;
for(const bad of ['巳',undefined,'甲子',false,3]){assert.throws(()=>region({...good,anchorStem:bad}),RangeError);invalid++;}
for(const bad of ['戍',undefined,'wu',false]){assert.throws(()=>region({...good,sourceMonthBranch:bad}),RangeError);invalid++;}
for(const bad of ['甲丑','丙子日','日',false]){assert.throws(()=>trueRegion({...base,sourceMingPillar:bad,sourceMonthPillar:'辛卯'}),RangeError);invalid++;}
for(const bad of ['yes',1,{},undefined]){assert.throws(()=>terminal({...base,naYinOvercomeByDeclaredTrueElement:bad,originalStemAlsoOvercome:true}),TypeError);invalid++;}
for(const bad of [[],['丁'],new Array(2),'丁壬',['丁','壬','甲']]){assert.throws(()=>literal({...base,sourceAnchorPillar:'己酉',seenStemPair:bad}),TypeError);invalid++;}
const actual=read('ACTUAL_RUNTIME.json'),reused=read('REUSED_ACTUAL_EVIDENCE.json');assert(actual.partners.every(x=>x.expected===x.actual)&&actual.naYin.every(x=>x.expected===x.actual));const actualPartners=new Map([...actual.partners.map(x=>[x.stem,x.actual]),...reused.mechanisms.map(x=>[x.foodStem,x.actualPartner])]);assert.equal(actualPartners.size,10);for(const stem of stems)assert.equal(actualPartners.get(stem),stems[(stems.indexOf(stem)+5)%10]);
assert.equal(actual.actualNewPartnerQueries+actual.actualNewNaYinQueries,10);assert.equal(actual.trueFiveElementMappingEstablished,false);
const result={passed:true,groups:9,frozenFiles:6,regionFrames,explicitHeavenCoordinates:heavenTrue,explicitEarthCoordinates:earthTrue,trueRegionFrames,derivedTrueRegionMatches:trueRegionPositive,literalFrames,literalPositiveCases:literalPositive,literalUnknownFrames:literalUnknown,terminalFrames,nullInvariants,unsupportedRequests:unsupported,invalidInputs:invalid,retainedNewTableQueries:10,reusedPartnerQueries:6,newEngineCallsDuringTests:0,wholeChapterApplied:false,consumerChanged:false};
if(process.argv.includes('--write-results'))fs.writeFileSync(`${b}/REFERENCE_RESULTS.json`,JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result));
