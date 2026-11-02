import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,existsSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {resolve,dirname} from 'node:path';
import {fileURLToPath} from 'node:url';
import {inspectDeclaredKuigangContext as inspect} from './context-reference.mjs';
const b=dirname(fileURLToPath(import.meta.url));let w=b;while(!existsSync(resolve(w,'v53/engine.js'))){const parent=dirname(w);assert.notEqual(parent,w);w=parent;}
const read=n=>JSON.parse(readFileSync(resolve(b,n),'utf8'));
const freeze=read('PREIMPLEMENTATION_FREEZE.json');
for(const r of freeze.files){const raw=readFileSync(resolve(w,r.file));assert.equal(raw.length,r.bytes);assert.equal(createHash('sha256').update(raw).digest('hex'),r.sha256);}
const expected=read('EXPECTED_CONTEXTS.json');let nulls=0;
const unknowns=['imperialStarSimultaneousPriority','overallSourceRestriction','overallDateRecommendation','calendarDate','monthBoundary','affectedDirection','practicalOutcome'];
for(const f of expected.frames){const before=JSON.stringify(f.input),r=inspect(f.input);assert.equal(r.localAvoidanceClaim,f.expectedLocalAvoidanceClaim);assert.equal(r.localFavourableClaim,f.expectedLocalFavourableClaim);assert.equal(JSON.stringify(f.input),before);assert.ok(Object.isFrozen(r));for(const k of unknowns){assert.equal(r[k],null);nulls++;}assert.equal(r.consumerApplied,false);assert.equal(r.wholeSourceMethodApplied,false);}
const day={...expected.frames[0].input,affectedContextConfirmed:true},direction={...expected.frames.find(x=>x.input.system.startsWith('ITKC')).input,affectedContextConfirmed:true,listedStarClauseSatisfied:null};
for(const generic of [true,false,null]){assert.equal(inspect({...day,genericBeneficPresent:generic}).localAvoidanceClaim,true);assert.equal(inspect({...direction,genericBeneficPresent:generic}).localFavourableClaim,null);}
// The two source frames cannot be exchanged even though their four names coincide.
assert.equal(inspect({...day,frame:direction.frame}),null);assert.equal(inspect({...direction,frame:day.frame}),null);
assert.equal(inspect({...day,system:'merged-kuigang'}),null);assert.equal(inspect({...day,activity:'all-activities'}),null);
for(const input of [null,{}, {...day,extra:true},{...day,affectedContextConfirmed:1},{...day,genericBeneficPresent:undefined},{...direction,listedStarClauseSatisfied:'三奇'},{...day,listedStarClauseSatisfied:true}])assert.throws(()=>inspect(input),TypeError);
// A favourable local assertion may coexist with a day avoidance; no global verdict.
const a=inspect(day),c=inspect({...direction,listedStarClauseSatisfied:true});assert.equal(a.localAvoidanceClaim,true);assert.equal(c.localFavourableClaim,true);assert.equal(a.overallDateRecommendation,null);assert.equal(c.overallDateRecommendation,null);
const result={passed:true,groups:6,frozenFiles:freeze.files.length,sourceContextFrames:expected.frames.length,nullInvariants:nulls,unsupportedContexts:4,invalidInputs:7,newEngineCalls:0,newEngineCallsDuringTests:0,newCalendarObjects:0,newHTTPBodies:0,consumerChanged:false,wholeSourceMethodApplied:false};
if(process.argv.includes('--write-results'))writeFileSync(resolve(b,'TEST_RESULTS.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result));
