import fs from'node:fs';import path from'node:path';import assert from'node:assert/strict';import{createHash}from'node:crypto';import{createRequire}from'node:module';
const b=import.meta.dirname,w=path.resolve(b,'../..'),out=path.join(b,'ACTUAL_RUNTIME.json'),sha=x=>createHash('sha256').update(x).digest('hex');
assert(!fs.existsSync(out),'Retained batch exists; verify instead of rerunning.');
const read=n=>JSON.parse(fs.readFileSync(path.join(b,n),'utf8'));
for(const x of read('PREIMPLEMENTATION_FREEZE.json').files){const raw=fs.readFileSync(path.join(b,x.file));assert.equal(raw.length,x.bytes);assert.equal(sha(raw),x.sha256);}
const L=createRequire(import.meta.url)(path.join(w,'v46/node_modules/lunar-typescript'));
const cases=read('EXPECTED_BEFORE_IMPLEMENTATION.json').actualLibraryExpected.map(x=>{
 const actualNaYin=L.LunarUtil.NAYIN[x.pillar],actualStemElement=L.LunarUtil.WU_XING_GAN[x.pillar[0]];
 return{...x,actualNaYin,actualStemElement,matches:actualNaYin===x.expectedNaYin&&actualStemElement===x.expectedStemElement};
});
const libraryFile='v46/node_modules/lunar-typescript/dist/index.cjs';
const output={date:'2026-10-29',executedUTC:new Date().toISOString(),libraryVersion:'1.8.6',libraryFile,librarySHA256:sha(fs.readFileSync(path.join(w,libraryFile))),scriptSHA256:sha(fs.readFileSync(import.meta.filename)),freezeSHA256:sha(fs.readFileSync(path.join(b,'PREIMPLEMENTATION_FREEZE.json'))),method:'Execute retained lunar-typescript;2 exported NAYIN lookups and2 WU_XING_GAN lookups for the two source repeated-pillar phrases. No complete natal charts or historical birth dates.',cases,actualNaYinTableQueries:2,actualStemElementTableQueries:2,actualCalendarObjects:0,actualNatalCharts:0,sourceGoldMeaningAdjudicated:false,sourcePredictionValidated:false};
fs.writeFileSync(out,JSON.stringify(output,null,2)+'\n');assert(cases.every(c=>c.matches));console.log(JSON.stringify({actualNaYinTableQueries:2,actualStemElementTableQueries:2,matches:4,actualNatalCharts:0}));
