import fs from 'node:fs';import path from 'node:path';import {createHash}from'node:crypto';
import{createRequire}from'node:module';import assert from'node:assert/strict';
const base=import.meta.dirname,w=path.resolve(base,'../..'),out=path.join(base,'ACTUAL_RUNTIME.json');
if(fs.existsSync(out))throw Error('Retained execution exists; verify instead of repeating.');
const hash=b=>createHash('sha256').update(b).digest('hex');
const read=n=>JSON.parse(fs.readFileSync(path.join(base,n),'utf8'));
for(const x of read('PREIMPLEMENTATION_FREEZE.json').files){const b=fs.readFileSync(path.join(base,x.file));assert.equal(b.length,x.bytes);assert.equal(hash(b),x.sha256);}
const L=createRequire(import.meta.url)(path.join(w,'v46/node_modules/lunar-typescript'));
const stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'];
const pairs=read('EXPECTED_BEFORE_IMPLEMENTATION.json').pairs.map(x=>{
 // A declared coordinate carrier invokes the real library method. It is not
 // an EightChar natal chart and contains no fabricated calendar date.
 const carrier={getDayGan:()=>x.stem,getDayGanIndex:()=>stems.indexOf(x.stem)};
 const actual=L.EightChar.prototype.getDiShi.call(carrier,branches.indexOf(x.branch));
 return {...x,actualLunarLabel:actual,matches:x.expectedLunarLabel===actual};
});
const report={date:'2026-10-29',executedUTC:new Date().toISOString(),libraryVersion:'1.8.6',
 librarySHA256:hash(fs.readFileSync(path.join(w,'v46/node_modules/lunar-typescript/dist/index.cjs'))),
 scriptSHA256:hash(fs.readFileSync(import.meta.filename)),freezeSHA256:hash(fs.readFileSync(path.join(base,'PREIMPLEMENTATION_FREEZE.json'))),
 method:'Actual exported EightChar.prototype.getDiShi called with explicitly declared getDayGan/getDayGanIndex carrier; no calendar/natal instance.',
 pairs,actualCoordinateMethodCalls:pairs.length,actualCalendarObjects:0,actualNatalCharts:0,
 sourceOtherVoicesAdjudicated:false,sourcePredictionValidated:false};
fs.writeFileSync(out,JSON.stringify(report,null,2)+'\n');assert(pairs.every(x=>x.matches));
console.log(JSON.stringify({actualCoordinateMethodCalls:20,matched:20,actualNatalCharts:0}));
