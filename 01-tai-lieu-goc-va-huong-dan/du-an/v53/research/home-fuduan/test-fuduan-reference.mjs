import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {SOURCE_ID,FRAME_ID,sourceMansionAt,sourceBlockBoundary} from './fuduan-reference.mjs';
const root=path.dirname(fileURLToPath(import.meta.url));
const read=n=>JSON.parse(fs.readFileSync(path.join(root,n),'utf8').replace(/^\uFEFF/,''));
const e=read('EXPECTED_BEFORE_IMPLEMENTATION.json');
const base={sourceID:SOURCE_ID,frameID:FRAME_ID};
let prose=0,table=0,boundaries=0,frames=0,periodPairs=0,step28Pairs=0,unsupported=0,invalid=0;
const days={'甲子':0,'乙丑':1,'癸亥':59},hours=Array.from('子丑寅卯辰巳午未申酉戌亥');
for(const x of e.proseExamples) {
 assert.equal(sourceMansionAt({...base,yuan:x.yuan,dayOffset:days[x.day],hourIndex:hours.indexOf(x.hour)}).mansion,x.mansion);prose++;
}
for(const c of e.manualPrintedTable.columnsRightToLeft) {
 assert.equal(c.values.length,12);
 c.values.forEach((m,h)=>{assert.equal(sourceMansionAt({...base,yuan:c.yuan,dayOffset:0,hourIndex:h}).mansion,m);table++;});
}
for(const x of e.boundaries) {
 const b=sourceBlockBoundary({...base,yuan:x.yuan});
 for(const key of ['last','continuousNext','declaredNext','forwardGap'])assert.equal(b[key],x[key]);
 assert.equal(b.seamless,false);boundaries++;
}
for(let y=1;y<=7;y++)for(let d=0;d<60;d++)for(let h=0;h<12;h++) {
 const r=sourceMansionAt({...base,yuan:y,dayOffset:d,hourIndex:h});
 assert.equal(r.useForRecommendations,false);assert.equal(r.calendarDate,null);assert.equal(r.auspiciousness,null);frames++;
 if(d*12+h+28<720){const k=d*12+h+28;assert.equal(r.mansion,sourceMansionAt({...base,yuan:y,dayOffset:Math.floor(k/12),hourIndex:k%12}).mansion);step28Pairs++;}
 if(d+7<60){assert.equal(r.mansion,sourceMansionAt({...base,yuan:y,dayOffset:d+7,hourIndex:h}).mansion);periodPairs++;}
}
assert.equal(step28Pairs,4844);assert.equal(frames,5040);assert.equal(periodPairs,4452);
assert.equal(7*60*12,5040);assert.equal(5040/28,e.periodExpectations.continuousCompleteMansionLoops);
const unknownInputs=[null,[],{},'2026-10-29',
 ...e.unknownFrames.map(f=>({...base,frameID:f,yuan:1,dayOffset:0,hourIndex:0})),
 {...base,sourceID:'ITKC',yuan:1,dayOffset:0,hourIndex:0},
 {...base,yuan:1,dayOffset:0,hourIndex:0,date:'2026-10-29'},
 {...base,yuan:1,dayOffset:0,hourIndex:0,timeZone:'Asia/Ho_Chi_Minh'},
 {...base,yuan:1,dayOffset:0,hourIndex:0,fourKillSubmerged:true},
 {...base,yuan:1,dayOffset:0,hourIndex:0,rowMeans:'civil-day'}];
for(const x of unknownInputs){assert.equal(sourceMansionAt(x),null);unsupported++;}
for(const f of e.unknownFrames){assert.equal(sourceBlockBoundary({...base,frameID:f,yuan:1}),null);unsupported++;}
for(const [key,value] of [['yuan',0],['yuan',8],['yuan',1.2],['dayOffset',-1],['dayOffset',60],['dayOffset','0'],['hourIndex',-1],['hourIndex',12],['hourIndex',NaN],['hourIndex',null]]){
 assert.throws(()=>sourceMansionAt({...base,yuan:1,dayOffset:0,hourIndex:0,[key]:value}),RangeError);invalid++;
}
for(const value of [0,8,'1',undefined]){assert.throws(()=>sourceBlockBoundary({...base,yuan:value}),RangeError);invalid++;}
const frozen=read('PREIMPLEMENTATION_FREEZE.json');
for(const x of frozen.files){const b=fs.readFileSync(path.join(root,x.file));assert.equal(b.length,x.bytes);assert.equal(createHash('sha256').update(b).digest('hex'),x.sha256);}
console.log(JSON.stringify({passed:true,groups:8,manualTableMansionCells:table,sourceProseExamples:prose,boundaryExpectations:boundaries,finiteFrames:frames,sevenDayPeriodPairs:periodPairs,twentyEightStepPeriodPairs:step28Pairs,unsupportedFramesReturnedNull:unsupported,invalidInputsRejected:invalid,preimplementationFilesUnchanged:frozen.files.length,calendarEngineCalls:0,chartEngineCalls:0,printedRowsAreLiteralCoordinatesOnly:true,compilerCritiqueNotAdoptedAsRecommendation:true}));
