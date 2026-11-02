import fs from 'node:fs';
import path from 'node:path';
import {createHash} from 'node:crypto';
import assert from 'node:assert/strict';
import {SYSTEM,inspectSourceFoodChain} from '../research/bazi-food-chain/food-chain-reference.mjs';
const base=path.resolve(import.meta.dirname,'../research/bazi-food-chain'),read=n=>JSON.parse(fs.readFileSync(path.join(base,n),'utf8'));
const fixture=read('EXPECTED_BEFORE_IMPLEMENTATION.json'),runtime=read('ACTUAL_RUNTIME.json');
let manual=0,contexts=0,invariants=0,frames=0,invalid=0;
function check(input) {
 const r=inspectSourceFoodChain({system:SYSTEM,...input});assert(r);
 for(const k of ['fullEffectiveInhibition','autoRescueOrPriority','automaticBirthChart','realPersonStrength','practicalOutcome','wealthOutcome','healthOutcome','lifespan'])assert.equal(r[k],null);
 assert.equal(r.sourceMeaningResolved,false);assert.equal(r.sourceClaimedSuppressionIsNotEngineValidated,true);assert.equal(r.consumerApplied,false);
 assert.equal(r.elementCoordinateEdges.length,6);
 for(const e of r.elementCoordinateEdges){assert.equal(e.relation,e.coordinateRelation);assert.equal(e.effectiveInteraction,null);assert.equal(e.actualSuppression,null);}
 assert.equal(r.sourceNamedDayRoot,'甲');assert.equal(r.fiveStemsAreNotFiveBirthPillars,true);invariants+=11;return r;
}
for(const c of fixture.manualCases){
 const r=check({subjectBinding:c.subjectBinding,declaredFacts:c.facts});
 assert.equal(r.selectedSourceScenarioPremisesMatch,c.expectedSourceScenarioPremises,c.id);
 assert.deepEqual(r.sourceClaimedSuppressedOutgoingEdgeIDs,c.expectedSuppressedEdgeIDs,c.id);
 assert.equal(r.selectedAdjacencyConflictsWithFixedControlRelation,c.expectedAdjacencyContradiction,c.id);manual++;
}
for(const subjectBinding of ['unresolved','parallel-bing-subject','adjacent-wu-subject'])
 for(const sameInteractionFrame of [true,false,null])for(const owlControlEffective of [true,false,null])for(const noCounteractingRescue of [true,false,null]){
 const r=check({subjectBinding,declaredFacts:{sameInteractionFrame,owlControlEffective,noCounteractingRescue}});contexts++;
 if(subjectBinding!=='parallel-bing-subject')assert.equal(r.selectedSourceScenarioPremisesMatch,null);
 if(r.selectedSourceScenarioPremisesMatch===true)assert.deepEqual(r.sourceClaimedSuppressedOutgoingEdgeIDs,['丙>戊','丙>庚']);
 if([sameInteractionFrame,owlControlEffective,noCounteractingRescue].includes(false)&&subjectBinding==='parallel-bing-subject')assert.equal(r.selectedSourceScenarioPremisesMatch,false);
}
for(const o of [null,[],{},'甲丙壬戊庚',{system:'generic-Bazi',subjectBinding:'parallel-bing-subject',declaredFacts:{}},
 {system:SYSTEM,declaredFacts:{}},{system:SYSTEM,subjectBinding:'parallel-bing-subject'},
 {system:SYSTEM,subjectBinding:'parallel-bing-subject',declaredFacts:{},birthDate:'2000-01-01'},
 {system:SYSTEM,subjectBinding:'parallel-bing-subject',declaredFacts:{},pillars:['甲子','丙寅','壬申','戊申']}]){
 assert.equal(inspectSourceFoodChain(o),null);frames++;
}
for(const o of [{subjectBinding:'auto',declaredFacts:{}},{subjectBinding:'parallel-bing-subject',declaredFacts:{wealthLoss:true}},
 {subjectBinding:'parallel-bing-subject',declaredFacts:{owlControlEffective:'true'}},{subjectBinding:'parallel-bing-subject',declaredFacts:[]},
 {subjectBinding:'parallel-bing-subject',declaredFacts:{sameInteractionFrame:1}}]){
 assert.throws(()=>inspectSourceFoodChain({system:SYSTEM,...o}));invalid++;
}
assert.equal(runtime.pairs.length,11);assert.equal(new Set(runtime.pairs.map(x=>x.root+x.target)).size,11);
for(const e of fixture.enginePairs){const x=runtime.pairs.find(x=>x.root===e.root&&x.target===e.target);assert.equal(x.actualHHCTenGod,e.hhcTenGod);assert.equal(x.actualLunarTenGod,e.lunarTenGod);}
assert.equal(runtime.pairs.find(x=>x.root==='甲'&&x.target==='壬').actualHHCTenGod,'Thiên Ấn');
assert.equal(runtime.pairs.find(x=>x.root==='丙'&&x.target==='壬').actualHHCTenGod,'Thất Sát');
assert.equal(runtime.pairs.find(x=>x.root==='戊'&&x.target==='庚').actualHHCTenGod,'Thực Thần');
assert.equal(runtime.pairs.find(x=>x.root==='丙'&&x.target==='庚').actualHHCTenGod,'Thiên Tài');
const frozen=read('PREIMPLEMENTATION_FREEZE.json');assert.equal(frozen.implementationExists,false);
for(const x of frozen.files){const b=fs.readFileSync(path.join(base,x.file));assert.equal(b.length,x.bytes);assert.equal(createHash('sha256').update(b).digest('hex'),x.sha256);}
console.log(JSON.stringify({date:'2026-10-29',passed:true,groups:7,manualExpectedCases:manual,declaredTernaryContexts:contexts,
 nonPredictionInvariants:invariants,unsupportedFramesReturnedNull:frames,invalidDeclarationsRejected:invalid,
 sourceCoordinateEdges:6,preimplementationFilesUnchanged:frozen.files.length,
 retainedActualHHCGodCallsVerified:runtime.summary.actualHHCGodCalls,retainedActualLunarTenGodQueriesVerified:11,
 retainedActualLunarStemElementQueriesVerified:5,newEngineCallsDuringTests:0,sourceEllipsisStillEditorial:true,
 sourceEffectivenessOrOutcomesValidated:false,consumerChanged:false,wholeParentApplied:false}));
