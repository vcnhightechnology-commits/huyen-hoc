import fs from 'node:fs';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {createRequire} from 'node:module';
import assert from 'node:assert/strict';
const base=import.meta.dirname,workspace=path.resolve(base,'../..'),out=path.join(base,'ACTUAL_RUNTIME.json');
if(fs.existsSync(out))throw Error('Retained actual table read exists; do not repeat it for counts.');
const hash=b=>createHash('sha256').update(b).digest('hex');
const read=n=>JSON.parse(fs.readFileSync(path.join(base,n),'utf8'));
const frozen=read('PREIMPLEMENTATION_FREEZE.json');assert.equal(frozen.runtimeExists,false);
for(const x of frozen.files){const b=fs.readFileSync(path.join(base,x.file));assert.equal(b.length,x.bytes);assert.equal(hash(b),x.sha256);}
const req=createRequire(import.meta.url),L=req(path.join(workspace,'v46/node_modules/lunar-typescript'));
const actual=[...L.LunarUtil.CHANG_SHENG];
const expected=read('EXPECTED_BEFORE_IMPLEMENTATION.json');
const comparisons=actual.map((literal,index)=>({index,lunarLabel:literal,
  comparisonLabel:expected.explicitComparisonNormalizationOnly[literal]??literal,
  normalization:expected.explicitComparisonNormalizationOnly[literal]?'explicit-comparison-only-Simplified-to-retained-Traditional':'none',
  sourceMainName:expected.mainOrder[index],
  matchesSourceMainOrder:(expected.explicitComparisonNormalizationOnly[literal]??literal)===expected.mainOrder[index]}));
const library=path.join(workspace,'v46/node_modules/lunar-typescript/dist/index.cjs');
const report={date:'2026-10-29',executedUTC:new Date().toISOString(),libraryVersion:req(path.join(workspace,'v46/node_modules/lunar-typescript/package.json')).version,
  librarySHA256:hash(fs.readFileSync(library)),scriptSHA256:hash(fs.readFileSync(import.meta.filename)),
  freezeSHA256:hash(fs.readFileSync(path.join(base,'PREIMPLEMENTATION_FREEZE.json'))),
  actualLabels:actual,comparisons,summary:{actualLunarLifeStageTableReads:1,labelsInTable:actual.length,
    actualCalendarObjects:0,actualEightCharObjects:0,actualHHCCharts:0,actualIztroCharts:0,
    sourceQuotedOrderComparedAsSameOrdinal:false,sourceAliasesOrStrengthValidated:false,consumerChanged:false}};
fs.writeFileSync(out,JSON.stringify(report,null,2)+'\n');
assert.deepEqual(actual,expected.expectedLunarSimplifiedSequence);
assert(comparisons.every(x=>x.matchesSourceMainOrder));
console.log(JSON.stringify({actualLunarTableReads:1,labelsCompared:actual.length,mainOrderMatched:true,actualCharts:0}));
