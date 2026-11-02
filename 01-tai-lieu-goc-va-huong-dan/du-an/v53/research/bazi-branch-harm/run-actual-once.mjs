import fs from'node:fs';import path from'node:path';import assert from'node:assert/strict';import{createHash}from'node:crypto';import{createRequire}from'node:module';
const b=import.meta.dirname;let w=b;while(!fs.existsSync(path.join(w,'v53/engine.js'))){const p=path.dirname(w);assert.notEqual(p,w);w=p;}
const out=path.join(b,'ACTUAL_RUNTIME.json'),sha=x=>createHash('sha256').update(x).digest('hex'),read=n=>JSON.parse(fs.readFileSync(path.join(b,n),'utf8'));
assert(!fs.existsSync(out),'Verified runtime batch already retained; do not repeat it.');
for(const x of read('PREIMPLEMENTATION_FREEZE.json').files){const raw=fs.readFileSync(path.join(b,x.file));assert.equal(raw.length,x.bytes);assert.equal(sha(raw),x.sha256);}
const file='v46/node_modules/lunar-typescript/dist/index.cjs',library=path.join(w,file),L=createRequire(import.meta.url)(library);
assert.equal(sha(fs.readFileSync(library)),'76e490b74e9913ed94b49689b90abc688ed1e2b11456312b3eb081ec63cf2fbe');
const e=read('EXPECTED_BEFORE_IMPLEMENTATION.json').actualLibraryExpected;
const clashes=[...'子丑寅卯辰巳午未申酉戌亥'].map((branch,index)=>({branch,index,expected:e.clashPartners[branch],actual:L.LunarUtil.CHONG[index]}));
const pillars=e.newPillarLookups.map(x=>({...x,actualNaYin:L.LunarUtil.NAYIN[x.pillar],actualStemElement:L.LunarUtil.WU_XING_GAN[x.pillar[0]]}));
const reusedPath='v53/research/bazi-branch-union/ACTUAL_RUNTIME.json',priorBytes=fs.readFileSync(path.join(w,reusedPath)),prior=JSON.parse(priorBytes);
assert(prior.partners.length===12&&prior.partners.every(x=>x.matches));
const output={executedUTC:new Date().toISOString(),libraryFile:file,libraryVersion:'1.8.6',librarySHA256:sha(fs.readFileSync(library)),scriptSHA256:sha(fs.readFileSync(import.meta.filename)),freezeSHA256:sha(fs.readFileSync(path.join(b,'PREIMPLEMENTATION_FREEZE.json'))),method:'Execute retained official lunar-typescript CHONG table12 times, plus2 NAYIN and2 WU_XING_GAN queries for the exact source pillars. Reuse retained12 HE_ZHI_6 results rather than querying them again.',clashes,pillars,reusedUnionEvidence:{file:reusedPath,sha256:sha(priorBytes),queriesRerun:0},actualNewClashQueries:12,actualNewNaYinQueries:2,actualNewStemElementQueries:2,actualCalendarObjects:0,actualNatalCharts:0,sourceTrueMetalFireMeaningAdjudicated:false,sourceEfficacyValidated:false};
fs.writeFileSync(out,JSON.stringify(output,null,2)+'\n');assert(clashes.every(x=>x.actual===x.expected));assert(pillars.every(x=>x.actualNaYin===x.naYin&&x.actualStemElement===x.stemElement));console.log(JSON.stringify({actualNewTableQueries:16,matches:16,reusedUnionQueries:12,repeatedEngineQueries:0,actualNatalCharts:0}));
