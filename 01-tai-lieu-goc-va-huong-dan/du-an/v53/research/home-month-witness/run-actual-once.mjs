import{readFileSync,writeFileSync,existsSync}from'node:fs';
import{resolve,basename}from'node:path';
import{createHash}from'node:crypto';
import vm from'node:vm';
import assert from'node:assert/strict';
import{MONTH_COMPARISON_SYSTEM as system,compareMonthGodWitnesses as compare}from'./monthly-witness-reference.mjs';
const b=import.meta.dirname,w=process.cwd(),out=resolve(b,'ACTUAL_RUNTIME.json'),hash=p=>createHash('sha256').update(readFileSync(p)).digest('hex'),read=p=>JSON.parse(readFileSync(p,'utf8').replace(/^\uFEFF/,''));
if(existsSync(out))throw Error('Actual batch retained; use test-witness.mjs.');
const freeze=read(resolve(b,'TRANSCRIPTION_FREEZE.json'));
for(const x of freeze.files){const p=resolve(b,basename(x.file));assert.equal(hash(p),x.sha256);assert.equal(readFileSync(p).length,x.bytes);}
const fixture=read(resolve(b,'MANUAL_WITNESS_TABLE.json')),expected=read(resolve(b,'MANUAL_EXPECTATIONS.json')),ctx={};ctx.window=ctx;vm.createContext(ctx);vm.runInContext(readFileSync(resolve(w,'v53/mountains.js'),'utf8'),ctx);
const mountainProbes=expected.actualEngineProbes.map(p=>{const actual=JSON.parse(JSON.stringify(ctx.HHC_MOUNTAINS.inspect(p.angle,0)));assert.equal(actual.selected.name,p.expectedMountain);assert.equal(actual.selected.center,p.expectedCenter);return{...p,actual};});
const comparisons=fixture.records.flatMap(row=>row.cells.map(c=>compare({system,god:row.id,monthOrdinal:c.monthOrdinal,monthBasis:'declared-source-ordinal'})));
const counts={'same-literal':0,'different-literal':0,'not-comparable':0};for(const x of comparisons)counts[x.status]++;
assert.deepEqual(counts,{'same-literal':77,'different-literal':5,'not-comparable':2});
const result={date:'2026-10-29',executedAt:new Date().toISOString(),freezeSHA256:hash(resolve(b,'TRANSCRIPTION_FREEZE.json')),scriptSHA256:hash(resolve(b,'run-actual-once.mjs')),mountainsSHA256:hash(resolve(w,'v53/mountains.js')),comparisons,mountainProbes,summary:{manuallyReadCells:84,sameLiterals:77,differentLiterals:5,originalP08Unresolved:2,actualHHCCompassCalls:2,distinctHypotheticalMountainCoordinates:2,modelBearingDifference:75,realSourceCellExactBearingsAssigned:0,calendarObjects:0,natalCharts:0,iztroCharts:0,runtimeBatchesAttempted:2,successfulRuntimeBatches:1,previousFailedRuntimeBatches:1,previousFailedCompassCalls:2,totalActualHHCCompassCallsIncludingFailure:4,newP08IndependentEditions:0,consumerChanged:false,wholeSourceApplied:false}};
writeFileSync(out,JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result.summary));
