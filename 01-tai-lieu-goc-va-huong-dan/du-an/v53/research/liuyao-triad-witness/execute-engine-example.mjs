import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {witnessTriadContexts,JAPAN_ID} from './witness-triad-reference.mjs';
const root=path.dirname(fileURLToPath(import.meta.url));
if(fs.existsSync(path.join(root,'ACTUAL_RUNTIME.json')))throw new Error('Retained real-engine execution exists; use read-only tests rather than replaying.');
let workspace=root;while(!fs.existsSync(path.join(workspace,'v53/engine.js'))){const p=path.dirname(workspace);if(p===workspace)throw Error('workspace');workspace=p;}
const bytes=fs.readFileSync(path.join(workspace,'v53/engine.js')),hash=createHash('sha256').update(bytes).digest('hex');
assert.equal(hash,'39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6');
const e=JSON.parse(fs.readFileSync(path.join(root,'EXPECTED_BEFORE_IMPLEMENTATION.json'),'utf8')).syntheticEngineFixture;
const c={};c.window=c;vm.createContext(c);vm.runInContext(bytes.toString(),c);
const main=c.HHC_ENGINE.hexNumber(e.values),changed=c.HHC_ENGINE.hexNumber(e.changedValues);
assert.equal(main,e.primaryNumber);assert.equal(changed,e.changedNumber);
const projected=witnessTriadContexts(e.values,{sourceID:JAPAN_ID,darkMovementByLine:Object.fromEntries([1,2,3,4,5,6].map(n=>[n,false]))});
assert.equal(projected.chart.primary.number,main);assert.equal(projected.chart.changed.number,changed);
assert.deepEqual(projected.chart.lines.map(l=>l.branch),e.primaryBranchesBottomToTop);
const wood=projected.groups.find(g=>g.id==='wood').primaryWitnesses;
assert.equal(wood.length,1);assert.equal(wood[0].firstModeThreeActualMovingCandidate,true);
const out={date:'2026-10-29',executedEngine:'HHC_ENGINE.hexNumber',engineSHA256:hash,successfulCalls:2,
 syntheticValues:e.values,changedValues:e.changedValues,primaryNumber:main,changedNumber:changed,
 projectedPrimaryBranchesBottomToTop:projected.chart.lines.map(l=>l.branch),movingLines:projected.chart.movingLines,
 sourcePrintedCast:false,newIndependentSourceCast:false,sourceFormulaValidatedByEngine:false,sourceOutcomesValidated:false,
 comparisonScope:'Actual HHC figure IDs versus source-derived structural projection for one synthetic subset; not source calendar or predictive validation.'};
fs.writeFileSync(path.join(root,'ACTUAL_RUNTIME.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out));
