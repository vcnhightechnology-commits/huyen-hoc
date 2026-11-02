import assert from 'node:assert/strict';
import {readFileSync,writeFileSync}from 'node:fs';
import {createHash}from 'node:crypto';
import {fileURLToPath}from 'node:url';
import {SOURCE_ID,FRAME_ID,sourceGeException,lookupGeCondition}from './ge-exception-reference.mjs';
const read=name=>JSON.parse(readFileSync(new URL(name,import.meta.url),'utf8'));
const frozen=read('./PREIMPLEMENTATION_FREEZE.json');
for(const f of frozen.files){const b=readFileSync(new URL(f.file,import.meta.url));assert.equal(b.length,f.bytes);assert.equal(createHash('sha256').update(b).digest('hex'),f.sha256);}
const expected=read('./EXPECTED_BEFORE_IMPLEMENTATION.json');
for(const c of expected.cases){const actual=sourceGeException(c.input);assert.equal(actual.localAvoidance,c.localAvoidance,c.id);assert.equal(actual.explicitLocalException,c.localAvoidance===false,c.id);}
const base={sourceID:SOURCE_ID,frameID:FRAME_ID};
let frames=0,invariants=0;
const shapes=[
 {clauseID:'forest-mountain-timber',marker:'forest-ge',activity:'enter-mountain-to-cut-timber',qualification:'beneficPresent'},
 {clauseID:'forest-mountain-timber',marker:'mountain-ge',activity:'enter-mountain-to-cut-timber',qualification:'beneficPresent'},
 {clauseID:'sacrifice-shen-present',marker:'shen-ge',activity:'sacrificial-rite',qualification:'shenPresentDay'}
];
for(const s of shapes)for(const markerStatus of [true,false,null])for(const qualified of [true,false,null]){
 const {qualification,...frame}=s;
 const r=sourceGeException({...base,...frame,markerStatus,[qualification]:qualified});
 assert.equal(r.localAvoidance,markerStatus===true&&qualified===true?false:null);
 for(const key of expected.neverInferred){assert.equal(r[key],null);invariants++;}
 assert.equal(r.sourceEfficacyValidated,false);assert.ok(Object.isFrozen(r));frames++;
}
let unsupported=0;
for(const o of expected.unsupportedRequests){assert.equal(sourceGeException(o),null);unsupported++;}
const good=expected.cases[0].input;
for(const key of Object.keys(good)){const o={...good};delete o[key];assert.equal(sourceGeException(o),null);unsupported++;}
for(const o of [null,[],new Date(),Object.create({sourceID:SOURCE_ID}),{...good,sourceID:'other-tradition'},
 {...good,frameID:'gregorian-calendar'},{...good,calendarDate:'2026-10-29'},
 {...good,allOtherConditionsQualified:true},{...good,[Symbol('hidden')]:true}]){assert.equal(sourceGeException(o),null);unsupported++;}
let invalid=0;
for(const [key,value]of [['markerStatus',1],['beneficPresent','true'],['activity',''],['activity',null],['marker','earth-ge']]){
 assert.throws(()=>sourceGeException({...good,[key]:value}));invalid++;
}
const manual=read('./MANUAL_CONDITIONS.json');
assert.equal(manual.records.length,10);assert.equal(new Set(manual.records.map(r=>r.imageHeading)).size,7);
for(const r of manual.records){assert.deepEqual(lookupGeCondition(r.id),r);assert.ok(Object.isFrozen(lookupGeCondition(r.id)));assert.ok(Object.isFrozen(lookupGeCondition(r.id).pages));}
assert.equal(lookupGeCondition('earth-planting').literalUnpunctuated,'種植合成收日亦不避之');
assert.equal(lookupGeCondition('xing-zhou-ge').imageHeading,'刑隔');
assert.equal(lookupGeCondition('xing-zhou-ge').literalUnpunctuated,'合六壬理訴日定日不避州隔');
assert.equal(lookupGeCondition('nonexistent'),null);assert.equal(lookupGeCondition(null),null);
assert.equal(manual.records.filter(r=>r.disposition==='local-exception-from-declared-premises').length,2);
// Cross-clause non-interference: run the retained clause implementation itself once.
const previous=new URL('../../v53/research/home-activity-clauses/activity-clause-reference.mjs',import.meta.url);
const promoted=new URL('../home-activity-clauses/activity-clause-reference.mjs',import.meta.url);
let modulePath;
try{readFileSync(promoted);modulePath=promoted;}catch{modulePath=previous;}
const old=await import(modulePath.href);
const before=readFileSync(modulePath);
const fire=old.sourceActivityClause({...base,clauseID:'wantong-fire',activity:'start-building',markerStatus:true,beneficPresent:true});
assert.equal(fire.localAvoidance,true);
assert.equal(sourceGeException(good).localAvoidance,false);
assert.equal(fire.localAvoidance,true);assert.equal(fire.overallSuitability,null);
assert.deepEqual(readFileSync(modulePath),before);
const output={date:'2026-10-29',passed:true,groups:7,frozenFiles:4,expectedCases:expected.cases.length,
 ternaryFrames:frames,nullInvariants:invariants,unsupportedRequests:unsupported,invalidInputs:invalid,
 selectedConditionUnits:10,headingGroups:7,localExceptionClauses:2,deferredConditionUnits:8,
 priorClauseNonInterference:true,newCalendarEngineCalls:0,newChartCalls:0};
if(process.argv.includes('--write-results'))writeFileSync(new URL('./REFERENCE_RESULTS.json',import.meta.url),JSON.stringify(output,null,2)+'\n');
console.log(JSON.stringify(output));
