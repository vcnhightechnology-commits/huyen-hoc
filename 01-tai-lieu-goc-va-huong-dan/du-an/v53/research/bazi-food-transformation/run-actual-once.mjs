import fs from'node:fs';import path from'node:path';import vm from'node:vm';import{createHash}from'node:crypto';import{createRequire}from'node:module';import assert from'node:assert/strict';
const b=import.meta.dirname,out=path.join(b,'ACTUAL_RUNTIME.json');
if(fs.existsSync(out))throw Error('Retained actual runtime exists; do not reexecute.');
let w=b;while(!fs.existsSync(path.join(w,'v53/engine.js'))){const p=path.dirname(w);if(p===w)throw Error('Workspace');w=p;}
const read=p=>JSON.parse(fs.readFileSync(p,'utf8').replace(/^\uFEFF/,'')),hash=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const freeze=read(path.join(b,'PREIMPLEMENTATION_FREEZE.json'));assert(freeze.referenceAndActualRuntimeAbsentAtFreeze);
const plan=read(path.join(b,'RUNTIME_PLAN.json'));
for(const r of [...freeze.files,...read(path.join(b,'ENGINE_IDENTITIES.json')).files,...plan.retainedPayloadIdentities]){const p=path.join(w,r.file);assert.equal(fs.statSync(p).size,r.bytes);assert.equal(hash(p),r.sha256);}
const c={};c.window=c;vm.createContext(c);for(const n of ['engine.js','bazi-relations.js'])vm.runInContext(fs.readFileSync(path.join(w,'v53',n),'utf8'),c);
const req=createRequire(import.meta.url),L=req(path.join(w,'v46/node_modules/lunar-typescript'));assert.equal(req(path.join(w,'v46/node_modules/lunar-typescript/package.json')).version,'1.8.6');
const stems=[...'甲乙丙丁戊己庚辛壬癸'],newRows=[];
for(const e of plan.missing){const actualHHC=c.HHC_BAZI_RELATIONS.god(stems.indexOf(e.root),stems.indexOf(e.target)),actualLunar=L.LunarUtil.SHI_SHEN[e.root+e.target];
 assert.equal(actualHHC,e.expectedHHC);assert.equal(actualLunar,e.expectedLunar);newRows.push({...e,actualHHC,actualLunar,newCall:true});}
const reusedRows=plan.reuse.map(e=>({...e,actualHHC:e.retained.actualHHC,actualLunar:e.retained.actualLunar,newCall:false}));
assert.equal(newRows.length,6);assert.equal(reusedRows.length,14);
const result={executedUTC:new Date().toISOString(),scriptSHA256:hash(path.join(b,'run-actual-once.mjs')),freezeSHA256:hash(path.join(b,'PREIMPLEMENTATION_FREEZE.json')),
 engineSHA256:hash(path.join(w,'v53/engine.js')),relationsSHA256:hash(path.join(w,'v53/bazi-relations.js')),lunarLibrarySHA256:hash(path.join(w,'v46/node_modules/lunar-typescript/dist/index.cjs')),
 newRows,reusedRows,actualNewHHCGodCalls:6,actualNewLunarTenGodTableQueries:6,retainedRelationPairsReused:14,
 newPartnerTableQueries:0,retainedPartnerCoordinatesReused:10,actualCalendarObjects:0,actualNatalCharts:0,
 transformationValidated:false,sourceOutcomeValidated:false,consumerChanged:false,wholeContextApplied:false};
fs.writeFileSync(out,JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({newHHCGodCalls:6,newLunarTableQueries:6,reusedRelationPairs:14,reusedPartnerCoordinates:10,charts:0}));
