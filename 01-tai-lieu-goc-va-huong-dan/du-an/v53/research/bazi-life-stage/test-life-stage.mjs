import assert from 'node:assert/strict';
import fs from 'node:fs';
import {createHash} from 'node:crypto';
import {MAIN_SYSTEM,QUOTED_SYSTEM,sourceLifeStageOrder,lookupLifeStageTerm} from './life-stage-reference.mjs';
const read=n=>JSON.parse(fs.readFileSync(new URL(n,import.meta.url),'utf8'));
const fixture=read('EXPECTED_BEFORE_IMPLEMENTATION.json'),actual=read('ACTUAL_RUNTIME.json');
let termChecks=0,aliasChecks=0,unsupported=0,invariants=0;
const guard=o=>{for(const key of ['stemBranchCoordinate','yinYangDirection','actualPhaseForBirthChart','natalStrength',
  'sourceBroadGroupAutomaticallyApplied','practicalOutcome','healthOutcome','lifespan'])assert.equal(o[key],null);
  assert.equal(o.consumerApplied,false);assert.equal(o.wholeChapterApplied,false);invariants+=10;};
const main=sourceLifeStageOrder({system:MAIN_SYSTEM}),quoted=sourceLifeStageOrder({system:QUOTED_SYSTEM});
assert.deepEqual(main.records.map(x=>x.literalName),fixture.mainOrder);
assert.deepEqual(quoted.records.map(x=>x.literalName),fixture.quotedOrder);
assert.deepEqual(quoted.records.map(x=>x.sourceOrdinal),Array.from({length:12},(_,i)=>i+1));
assert.notDeepEqual(main.records.map(x=>x.literalName),quoted.records.map(x=>x.literalName));
guard(main);guard(quoted);
for(const [system,names]of [[MAIN_SYSTEM,fixture.mainOrder],[QUOTED_SYSTEM,fixture.quotedOrder]]){
 for(const [i,name]of names.entries()){
  const x=lookupLifeStageTerm({system,term:name});guard(x);assert.equal(x.sourceOrdinal,i+1);assert.equal(x.literalName,name);
  assert.equal(x.matchedAs,'literal-name');assert.equal(x.broadGroups.qualifier,'亦大槩言之');
  assert.equal(x.broadGroups.automaticallyAssigned,false);assert.equal(x.broadGroups.shorthandResolved,false);termChecks++;
 }
}
for(const expected of fixture.explicitAliasQueries){
 const x=lookupLifeStageTerm({system:QUOTED_SYSTEM,term:expected.term});guard(x);
 assert.equal(x.literalName,expected.canonicalSourceName);assert.equal(x.sourceOrdinal,expected.sourceOrdinal);
 assert.equal(x.matchedAs,'explicit-source-alias');aliasChecks++;
}
for(const term of fixture.notImplicitQuotedAliases){assert.equal(lookupLifeStageTerm({system:QUOTED_SYSTEM,term}),null);unsupported++;}
for(const [i,name]of fixture.mainOrder.entries()){
 const x=lookupLifeStageTerm({system:MAIN_SYSTEM,term:name});
 const matches=x.crossVoiceLexicalMatches;const expected=fixture.allMainNameQuotedOrdinal[i];
 assert.deepEqual(matches.map(x=>x.sourceOrdinal),expected===null?[]:[expected]);
 assert(matches.every(x=>!x.fullPhaseEquivalenceEstablished));
 if(name==='胎'||name==='養'){assert.equal(x.editorialAlignmentCandidates.length,1);assert.equal(x.editorialAlignmentCandidates[0].acceptedAsSourceAlias,false);}
}
const death=lookupLifeStageTerm({system:QUOTED_SYSTEM,term:'死'});
assert.equal(death.sourceDefinition,'萬物死');assert.equal(death.historicalMetaphorIsNotMedicalOrLifePrediction,true);
assert(death.sourceQualifiers.includes('見休囚死絶未必便作凶言'));
for(const input of [null,{},[],{system:'generic-twelve',term:'死'},{system:QUOTED_SYSTEM,term:' 死'},
 {system:QUOTED_SYSTEM,term:12},{system:QUOTED_SYSTEM,term:'長生',birthDate:'2000-01-01'},
 {system:QUOTED_SYSTEM,term:'長生',dayStem:'甲'},Object.assign(Object.create({foo:1}),{system:QUOTED_SYSTEM,term:'長生'}),
 {system:QUOTED_SYSTEM,term:'長生',[Symbol('hidden')]:true}]){
 assert.equal(lookupLifeStageTerm(input),null);unsupported++;
}
assert.equal(sourceLifeStageOrder({system:MAIN_SYSTEM,pillars:[]}),null);unsupported++;
const altered=lookupLifeStageTerm({system:QUOTED_SYSTEM,term:'墓'});altered.explicitSourceAliases[0]='fake';altered.broadGroups.literalTokens['四貴'].length=0;
assert.deepEqual(lookupLifeStageTerm({system:QUOTED_SYSTEM,term:'庫'}).explicitSourceAliases,['庫']);
assert.equal(lookupLifeStageTerm({system:QUOTED_SYSTEM,term:'庫'}).broadGroups.literalTokens['四貴'].length,4);
assert.equal(actual.summary.actualLunarLifeStageTableReads,1);assert.equal(actual.comparisons.length,12);
assert(actual.comparisons.every(x=>x.matchesSourceMainOrder));
assert.deepEqual(actual.actualLabels,fixture.expectedLunarSimplifiedSequence);
for(const x of read('PREIMPLEMENTATION_FREEZE.json').files){const b=fs.readFileSync(new URL(x.file,import.meta.url));assert.equal(b.length,x.bytes);assert.equal(createHash('sha256').update(b).digest('hex'),x.sha256);}
console.log(JSON.stringify({date:'2026-10-29',passed:true,groups:8,sourceOrders:2,definedQuotedStages:12,
 mainAndQuotedLiteralTermQueries:termChecks,explicitAliasQueries:aliasChecks,
 acceptedAliasTokens:4,editorialAlignmentsNotAcceptedAsAliases:2,unsupportedQueriesReturnedNull:unsupported,
 nonPredictionInvariants:invariants,sourceOrdinalAlignmentChecks:12,preimplementationFilesUnchanged:3,
 retainedActualLunarTableReads:1,newEngineCallsDuringTests:0,consumerChanged:false,wholeChapterApplied:false}));
