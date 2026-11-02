import fs from'node:fs';import assert from'node:assert/strict';import{createHash}from'node:crypto';
import{SYSTEM,lookupSourceMonthCell as lookup}from'./label-reference.mjs';
const read=n=>JSON.parse(fs.readFileSync(new URL(n,import.meta.url),'utf8'));
const data=read('MANUAL_CELLS.json'),expected=read('EXPECTED_BEFORE_IMPLEMENTATION.json'),amendment=read('READING_AMENDMENT.json');
const second=read('MANUAL_SECOND_BLOCK.json');
const full=read('EXPECTED_FULL_GRID.json');
const query=(m,d)=>lookup({system:SYSTEM,sourceMonth:m,dayGanzhi:d,monthBasis:'declared-source-month'});
const stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'];
const days=Array.from({length:60},(_,i)=>stems[i%10]+branches[i%12]);
let inspected=0,readable=0,unresolved=0,untranscribed=0;
for(let m=1;m<=12;m++)for(const d of days){const r=query(m,d);
 if(r.cellWasInspected){inspected++;if(r.workingLiteralLabel===null)unresolved++;else readable++;}
 else{untranscribed++;assert.equal(r.workingLiteralLabel,null);assert.equal(r.evidence,null);}
 for(const k of['automaticModernDate','combinedDaySuitability','practicalOutcome','futureEventPrediction'])assert.equal(r[k],null);
 assert.equal(r.sourceMonthBoundaryEstablished,false);assert.equal(r.unresolvedMeansBlank,false);
}
assert.equal(inspected,full.inspectedCells);assert.equal(readable,full.readableLabels);assert.equal(unresolved,full.unknownLabels);assert.equal(untranscribed,0);
for(const x of expected.fixedCases)assert.equal(query(x.month,x.day).workingLiteralLabel,x.expected);
assert.equal(query(12,'癸酉').workingLiteralLabel,null);assert.equal(query(12,'癸酉').evidence.readingAmendmentApplied,true);
assert.equal(query(1,'甲戌').workingLiteralLabel,'受死');
for(const x of full.fixedCases)assert.equal(query(x.month,x.day).workingLiteralLabel,x.expected);
assert(query(1,'癸亥').evidence.crop.includes('sixth-ten-complete.png'));
for(const x of full.priorMarkersUnresolvedThisRead)assert.equal(query(x.sourceMonth,x.dayGanzhi).workingLiteralLabel,null);
const nulls=[[null,'甲子'],[1,null],[null,null]];for(const[m,d]of nulls){const r=query(m,d);assert.equal(r.cellWasInspected,false);assert.equal(r.workingLiteralLabel,null);}
const base={system:SYSTEM,sourceMonth:1,dayGanzhi:'甲子',monthBasis:'declared-source-month'};
for(const x of[null,{},[],{...base,monthBasis:'lunar-month'},{...base,monthBasis:'solar-month'}, {...base,birthDate:'2000-01-01'}, {...base,system:'generic'}, {...base,[Symbol('hidden')]:1}])assert.equal(lookup(x),null);
for(const x of[{...base,sourceMonth:0},{...base,sourceMonth:13},{...base,sourceMonth:1.5},{...base,dayGanzhi:'甲丑'},{...base,dayGanzhi:' 甲子'}])assert.throws(()=>lookup(x));
query(1,'甲子').evidence.sourceColumnFromRight=999;assert.equal(query(1,'甲子').evidence.sourceColumnFromRight,1);
for(const f of['PREIMPLEMENTATION_FREEZE.json','SUPPLEMENT_FREEZE.json','SECOND_BLOCK_FREEZE.json','FULL_GRID_FREEZE.json'])for(const x of read(f).files){const b=fs.readFileSync(new URL(x.file,import.meta.url));assert.equal(b.length,x.bytes);assert.equal(createHash('sha256').update(b).digest('hex'),x.sha256);}
assert.equal(data.records.filter(x=>x.workingLiteralLabel==='河魁').length,11);
assert.equal(amendment.revisedReadableCellCount,82);
console.log(JSON.stringify({date:'2026-10-29',passed:true,groups:7,sourceGridQueries:720,inspectedCells:inspected,
 readableCellLabels:readable,unresolvedCellLabels:unresolved,otherCellsUntranscribed:untranscribed,
 explicitReadingAmendments:1,unknownInputsPreserved:nulls.length,newEngineCalls:0,consumerChanged:false,
 wholeSourceApplied:false}));
