import assert from 'node:assert/strict';
import {readFileSync,writeFileSync}from 'node:fs';
import {resolve}from 'node:path';
import {pathToFileURL}from 'node:url';
import {COURTYARD_SYSTEM,sourceCourtyardDiagram,sourceCourtyardCandidates}from '../research/home-yangzhai-courtyards/courtyard-reference.mjs';
const b=resolve(import.meta.dirname,'../research/home-yangzhai-courtyards'),w=resolve(b,'../../..'),system=COURTYARD_SYSTEM;
const {sourceLayerCoordinate}=await import(pathToFileURL(resolve(w,'v53/research/home-yangzhai-shishu/layer-coordinate-reference.mjs')).href);
const data=JSON.parse(readFileSync(resolve(b,'MANUAL_DIAGRAM_CELLS.json'),'utf8')),checks=[],comparisons=[],alternative=[];
const check=(name,fn)=>{fn();checks.push({name,ok:true});};
const project=(firstElement,layerIndex)=>sourceLayerCoordinate({system:'YZSS-Tianyige-selected-chuangong',countBasis:'ordered-source-jin',layerIndex,firstElement,declaredOrigin:'current-enclosure',boundary:{hasWall:true,hasDoor:true}});
check('Twelve direct diagrams contain69 numbered cells and preserve four unlabelled star cells',()=>{
 assert.equal(data.records.length,12);assert.equal(data.records.reduce((n,x)=>n+x.printedLayerCells.length,0),69);
 assert.deepEqual(data.records.filter(x=>x.printedLayerCells.length===5).map(x=>x.sourcePDFPage),[82,86,92]);
 assert.equal(data.records.flatMap(x=>x.printedLayerCells).filter(x=>x.sourceStar===null).length,4);
});
check('Same gate cannot select a unique first element across distinct source sitting and facing cases',()=>{
 for(const [gate,pages]of [['乾',[82,92]],['艮',[84,91]],['巽',[86,93]],['坤',[89,90]]]){
  const x=sourceCourtyardCandidates({system,sitting:null,facing:null,gate});
  assert.deepEqual(x.caseIDs,pages.map(p=>'YZSS-C'+p));assert.equal(x.modernPlanMatched,null);
  const first=x.caseIDs.map(caseID=>sourceCourtyardDiagram({system,caseID}).diagram.printedLayerCells[0].sourceElement);
  assert.equal(new Set(first).size,2);
 }
});
check('Existing layer component executes69 literal-first-seed contexts; C84 inconsistencies are retained',()=>{
 for(const diagram of data.records)for(const cell of diagram.printedLayerCells){
  const result=project(diagram.printedLayerCells[0].sourceElement,cell.ordinal);
  comparisons.push({caseID:diagram.id,ordinal:cell.ordinal,firstLiteralElement:diagram.printedLayerCells[0].sourceElement,
   literalElement:cell.sourceElement,existingComponentElement:result.element,match:cell.sourceElement===result.element});
 }
 assert.equal(comparisons.filter(x=>x.match).length,65);
 assert.deepEqual(comparisons.filter(x=>!x.match).map(x=>[x.caseID,x.ordinal]),[[ 'YZSS-C84',2],[ 'YZSS-C84',3],[ 'YZSS-C84',4],[ 'YZSS-C84',5]]);
 const c=data.records.find(x=>x.id==='YZSS-C84');
 for(const cell of c.printedLayerCells){const result=project('水',cell.ordinal);alternative.push({ordinal:cell.ordinal,declaredAlternativeFirstElement:'水',literalElement:cell.sourceElement,componentElement:result.element,match:cell.sourceElement===result.element});}
 assert.deepEqual(alternative.filter(x=>!x.match).map(x=>x.ordinal),[1,6]);
 assert.equal(c.printedLayerCells[0].sourceElement,'木');assert.equal(c.printedLayerCells[5].sourceElement,'木');
});
check('Height, size and unlabelled data are preserved without practical building advice',()=>{
 assert.equal(sourceCourtyardDiagram({system,caseID:'YZSS-C88'}).diagram.printedLayerCells[2].sourceSizeHeightWord,'高大');
 assert.equal(sourceCourtyardDiagram({system,caseID:'YZSS-C86'}).diagram.printedLayerCells[4].sourceSizeHeightWord,'小');
 for(const x of data.records){const r=sourceCourtyardDiagram({system,caseID:x.id});assert.equal(r.practicalHeightAdvice,null);assert.equal(r.modernVerticalFloorAdapter,null);assert.equal(r.fullProseConditionsApplied,false);}
});
check('Unknown inputs stay explicit; unmatched labels never receive an invented diagram or verdict',()=>{
 const x=sourceCourtyardCandidates({system,sitting:null,facing:null,gate:null});assert.equal(x.caseIDs.length,12);assert(x.missingInputs);
 const empty=sourceCourtyardCandidates({system,sitting:'東',facing:'東',gate:'坎'});assert.deepEqual(empty.caseIDs,[]);assert(empty.unmatchedIsNotUnlucky);assert.equal(empty.overallRecommendation,null);
 assert.throws(()=>sourceCourtyardCandidates({system,sitting:undefined,facing:'東',gate:'坎'}));
 assert.throws(()=>sourceCourtyardDiagram({system,caseID:84}));assert.throws(()=>sourceCourtyardDiagram({system:'modern',caseID:'YZSS-C84'}));
});
check('Returned arrays and cells cannot mutate the source table',()=>{
 const x=sourceCourtyardDiagram({system,caseID:'YZSS-C84'});x.diagram.printedLayerCells[0].sourceElement='水';x.literalUnresolvedCells.length=0;
 const fresh=sourceCourtyardDiagram({system,caseID:'YZSS-C84'});assert.equal(fresh.diagram.printedLayerCells[0].sourceElement,'木');assert.deepEqual(fresh.literalUnresolvedCells,[1,6]);
});
writeFileSync(resolve(w,'v53/qa/home-yangzhai-courtyards/REFERENCE_RESULTS.json'),JSON.stringify({date:'2026-10-28',checks,manualCells:69,
 actualExistingLayerComponentCalls:75,literalFirstSeedContexts:69,alternativeHypothesisContexts:6,
 selfSeedMatches:65,selfSeedDifferencesRetained:4,alternativeWaterSeedDifferencesRetained:2,
 alternativeHypothesisDoesNotEmendSource:true,newCalendarOrHHCEngineCalls:0,consumerChanged:false,
 allSourceConditionsApplied:false,comparisons,alternative},null,2)+'\n');
console.log(JSON.stringify({checks:checks.length,manualCells:69,existingLayerComponentCalls:75,retainedSelfSeedDifferences:4}));
