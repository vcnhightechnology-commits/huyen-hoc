import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import assert from 'node:assert/strict';
import {witnessTriadContexts,JAPAN_ID,NLC_ID} from './witness-triad-reference.mjs';
const root=path.dirname(fileURLToPath(import.meta.url));
const read=n=>JSON.parse(fs.readFileSync(path.join(root,n),'utf8').replace(/^\uFEFF/,''));
const e=read('EXPECTED_BEFORE_IMPLEMENTATION.json'),dark=Object.fromEntries([1,2,3,4,5,6].map(n=>[n,false]));
let cases=0,patterns=0,rejected=0,unknownSources=0,unknownDeferred=0;
const assertUnknownOutcome=x=>{for(const k of ['effectiveFormation','transformedElement','calendarEpoch','practicalOutcome'])assert.equal(x[k],null);assert(x.legacyNLCNotEmended);assert.equal(x.legacyNLCCountInterpretation,null);};
for(const c of e.manualCases) {
 const x=witnessTriadContexts(c.values,{sourceID:c.sourceID,darkMovementByLine:c.darkMovementByLine});assertUnknownOutcome(x);
 const wood=x.groups.find(g=>g.id==='wood').primaryWitnesses;assert.equal(wood.length,1);
 assert.equal(wood[0].firstModeThreeActualMovingCandidate,c.expectedWoodFirstModeCandidate,c.id);
 if(Object.hasOwn(c,'expectedLegacyMode2'))assert.equal(wood[0].sourceMode2TwoActiveOneInactive,c.expectedLegacyMode2,c.id);
 cases++;
}
for(let mask=0;mask<64;mask++){
 const values=Array.from({length:6},(_,i)=>mask>>i&1?6:8);
 const x=witnessTriadContexts(values,{sourceID:JAPAN_ID,darkMovementByLine:dark});assertUnknownOutcome(x);
 const w=x.groups.find(g=>g.id==='wood').primaryWitnesses[0];
 const selectedMoving=[0,2,4].every(i=>mask>>i&1);
 const expected=selectedMoving?(mask===21?true:null):false;
 assert.equal(w.firstModeThreeActualMovingCandidate,expected);
 patterns++;
}
for(const sourceID of [undefined,'B03','B02','all-editions']){
 assert.equal(witnessTriadContexts(e.syntheticEngineFixture.values,{sourceID}),null);unknownSources++;
}
for(const context of [
 {sourceID:JAPAN_ID,dayBranch:'未'},{sourceID:JAPAN_ID,calendarDate:'2026-10-29'},
 {sourceID:JAPAN_ID,firstModeCount:1},{sourceID:JAPAN_ID,darkMovementByLine:{1:true}},
 {sourceID:JAPAN_ID,tombByNode:{p8:true}},Object.create({sourceID:JAPAN_ID}),null]){
 assert.throws(()=>witnessTriadContexts(e.syntheticEngineFixture.values,context));rejected++;
}
for(const context of [{voidOrMonthBrokenByNode:{p1:true}},{tombByNode:{p3:true}},{}]){
 const x=witnessTriadContexts(e.syntheticEngineFixture.values,{sourceID:JAPAN_ID,darkMovementByLine:dark,...context});
 const w=x.groups.find(g=>g.id==='wood').primaryWitnesses[0];
 assert.equal(w.firstModeThreeActualMovingCandidate,true);
 assert.equal(w.fullSourceFormation,null);assert.equal(w.sourceFillOrOpenDate,null);assert.equal(x.practicalOutcome,null);
 if(Object.keys(context).length)assert.equal(w.sourceCompletionDeferred,true);else assert.equal(w.sourceCompletionDeferred,null);
 unknownDeferred++;
}
const source=read('MANUAL_WITNESS_COLLATION.json');assert.equal(source.selectedComparisons[0].JapanDiplomatic,'一卦之內有三交動而合局者一也');
assert.equal(source.selectedComparisons[0].NLCDiplomatic,'一卦之內有一交動而合局者一也');
const runtime=read('ACTUAL_RUNTIME.json');assert.equal(runtime.successfulCalls,2);assert.equal(runtime.primaryNumber,2);assert.equal(runtime.changedNumber,63);assert.equal(runtime.sourcePrintedCast,false);
const f=read('PREIMPLEMENTATION_FREEZE.json');assert.equal(f.implementationExists,false);
for(const x of f.files){const b=fs.readFileSync(path.join(root,x.file));assert.equal(b.length,x.bytes);assert.equal(createHash('sha256').update(b).digest('hex'),x.sha256);}
console.log(JSON.stringify({date:'2026-10-29',passed:true,groups:8,manualExpectedCases:cases,syntheticMotionPatterns:patterns,unknownSourceFrames:unknownSources,unsupportedInputsRejected:rejected,deferredQualificationContexts:unknownDeferred,preimplementationFilesUnchanged:f.files.length,retainedActualHHCCallsVerified:2,newHHCCallsDuringTests:0,printedSourceCastsNew:0,selectedSourceComparisons:3,NLCUnemended:true,fullFunctionalFormation:false,consumerChanged:false,wholeCatalogueCompleted:false}));
