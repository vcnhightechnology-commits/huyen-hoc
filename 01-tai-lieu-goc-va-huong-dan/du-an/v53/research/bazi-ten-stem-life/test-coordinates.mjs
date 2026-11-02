import fs from'node:fs';import assert from'node:assert/strict';import{createHash}from'node:crypto';
import{SYSTEM,sourceBirthDeathCoordinate as lookup}from'./coordinate-reference.mjs';
const read=n=>JSON.parse(fs.readFileSync(new URL(n,import.meta.url),'utf8'));
const expected=read('EXPECTED_BEFORE_IMPLEMENTATION.json'),actual=read('ACTUAL_RUNTIME.json');
let listed=0,unlisted=0,frames=0;
for(const stem of'甲乙丙丁戊己庚辛壬癸')for(const branch of'子丑寅卯辰巳午未申酉戌亥'){
 const r=lookup({system:SYSTEM,stem,branch});assert(r);frames++;
 const e=expected.pairs.find(x=>x.stem===stem&&x.branch===branch);
 if(e){assert.equal(r.sourceMarker,e.expectedSourceMarker==='长生'?'生':'死');listed++;}
 else{assert.equal(r.sourceMarker,null);assert.equal(r.evidenceStatus,'not-enumerated-in-selected-clauses');unlisted++;}
 for(const k of['actualNatalPhase','natalStrength','healthOutcome','lifespan','practicalOutcome'])assert.equal(r[k],null);
 assert.equal(r.otherTenStagesInferred,false);assert.equal(r.alternativeEarthStartsMerged,false);
}
assert.equal(listed,20);assert.equal(unlisted,100);
assert.equal(lookup({system:SYSTEM,stem:'戊',branch:'申'}).sourceMarker,null);
assert.equal(lookup({system:SYSTEM,stem:'己',branch:'卯'}).sourceMarker,null);
assert.deepEqual(lookup({system:SYSTEM,stem:'己',branch:'酉'}).sourcePages,[19,20]);
const invalid=[null,[],{}, {system:'generic',stem:'甲',branch:'亥'},
 {system:SYSTEM,stem:'甲',branch:'亥',birthDate:'2000-01-01'},
 {system:SYSTEM,stem:'甲',branch:'己'},{system:SYSTEM,stem:'甲木',branch:'亥'},
 {system:SYSTEM,stem:'甲',branch:'亥',[Symbol('hidden')]:true}];
for(const x of invalid)assert.equal(lookup(x),null);
const r=lookup({system:SYSTEM,stem:'甲',branch:'亥'});r.sourcePages.length=0;
assert(lookup({system:SYSTEM,stem:'甲',branch:'亥'}).sourcePages.length>0);
assert.equal(actual.actualCoordinateMethodCalls,20);assert.equal(actual.actualNatalCharts,0);
assert.deepEqual(actual.pairs.map(x=>({stem:x.stem,branch:x.branch,expectedSourceMarker:x.expectedSourceMarker,expectedLunarLabel:x.expectedLunarLabel})),expected.pairs);
assert(actual.pairs.every(x=>x.matches&&x.actualLunarLabel===x.expectedLunarLabel));
for(const x of read('PREIMPLEMENTATION_FREEZE.json').files){const b=fs.readFileSync(new URL(x.file,import.meta.url));assert.equal(b.length,x.bytes);assert.equal(createHash('sha256').update(b).digest('hex'),x.sha256);}
console.log(JSON.stringify({date:'2026-10-29',passed:true,groups:6,declaredStemBranchFrames:frames,
 explicitlyListedSourceCoordinates:listed,unlistedNotFalse:unlisted,unsupportedFramesRejected:invalid.length,
 retainedActualMethodCallsVerified:20,newEngineCallsDuringTests:0,actualNatalCharts:0,
 fullTwelveStageMatrixInferred:false,sourceAlternateVoicesMerged:false,consumerChanged:false}));
