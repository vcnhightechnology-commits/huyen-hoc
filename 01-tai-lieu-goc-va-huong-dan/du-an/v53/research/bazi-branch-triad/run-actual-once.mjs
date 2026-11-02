import fs from'node:fs';import path from'node:path';import vm from'node:vm';import assert from'node:assert/strict';
import{createHash}from'node:crypto';import{createRequire}from'node:module';
const b=import.meta.dirname,w=path.resolve(b,'../..'),out=path.join(b,'ACTUAL_RUNTIME.json'),sha=b=>createHash('sha256').update(b).digest('hex');
assert(!fs.existsSync(out),'Retained actual batch exists; verify it instead of rerunning.');
const read=n=>JSON.parse(fs.readFileSync(path.join(b,n),'utf8'));
for(const x of read('PREIMPLEMENTATION_FREEZE.json').files){const raw=fs.readFileSync(path.join(b,x.file));assert.equal(raw.length,x.bytes);assert.equal(sha(raw),x.sha256);}
const expected=read('EXPECTED_BEFORE_IMPLEMENTATION.json'),ctx={};ctx.window=ctx;vm.createContext(ctx);
const engineFiles=[];
for(const file of['v53/engine.js','v53/bazi-relations.js']){const raw=fs.readFileSync(path.join(w,file));engineFiles.push({file,bytes:raw.length,sha256:sha(raw)});vm.runInContext(raw.toString('utf8'),ctx);}
const stems=[...'甲乙丙丁戊己庚辛壬癸'];
const tenGod=expected.actualTenGodQueries.map(x=>{const actual=ctx.HHC_BAZI_RELATIONS.god(stems.indexOf(x.anchorStem),stems.indexOf(x.targetStem));return{...x,actual,matches:actual===x.expectedTenGod};});
const L=createRequire(import.meta.url)(path.join(w,'v46/node_modules/lunar-typescript'));
const lu=expected.actualLuQueries.map(x=>{const actual=L.LunarUtil.LU[x.stem];return{...x,actual,matches:actual===x.expected};});
const libraryFile='v46/node_modules/lunar-typescript/dist/index.cjs';
const report={date:'2026-10-29',executedUTC:new Date().toISOString(),engineFiles,libraryVersion:'1.8.6',libraryFile,
 librarySHA256:sha(fs.readFileSync(path.join(w,libraryFile))),scriptSHA256:sha(fs.readFileSync(import.meta.filename)),
 freezeSHA256:sha(fs.readFileSync(path.join(b,'PREIMPLEMENTATION_FREEZE.json'))),
 method:'Execute retained HHC engine and HHC_BAZI_RELATIONS.god for20 declared stem pairs; execute lunar-typescript and query its LU table for丙/丁. No fabricated date or natal chart.',
 tenGod,lu,actualHHCTenGodCalls:20,actualLuTableQueries:2,actualCalendarObjects:0,actualNatalCharts:0,
 sourceBroadRoleIsNotPolaritySpecificTenGod:true,
 limits:'Coordinates only. Source 傷局 has both 食神 and 傷官 engine coordinates; not an engine defect or a change of fixed TenGod. No full effective formation, strength or outcome validated.',sourceEfficacyValidated:false};
fs.writeFileSync(out,JSON.stringify(report,null,2)+'\n');assert(tenGod.every(x=>x.matches)&&lu.every(x=>x.matches));
console.log(JSON.stringify({actualHHCTenGodCalls:20,actualLuTableQueries:2,matches:22,actualCalendarObjects:0,actualNatalCharts:0}));
