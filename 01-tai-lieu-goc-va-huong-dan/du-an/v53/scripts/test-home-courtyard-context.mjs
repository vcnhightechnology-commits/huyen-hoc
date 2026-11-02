import assert from 'node:assert/strict';
import {writeFileSync} from 'node:fs';
import {sourceCourtyardCountContext as context} from '../research/home-yangzhai-courtyards/courtyard-context-reference.mjs';
const base={system:'YZSS-Tianyige-12-printed-courtyards',caseID:'YZSS-C82',countBasis:'ordered-source-jin',firstRoomFacing:'inward',declaredOrigin:'outer-main-gate',boundary:{hasWall:false,hasDoor:false}};
const checks=[],cases=[];const check=(name,fn)=>{fn();checks.push({name,ok:true});};
check('Facing changes actual source ordinal; outward first layer remains unspecified',()=>{
 for(const caseID of ['YZSS-C82','YZSS-C84']){
  const inside=context({...base,caseID}),outside=context({...base,caseID,firstRoomFacing:'all-outward'});
  assert.equal(inside.selectedLiteralCoordinates[0].ordinal,1);
  assert.deepEqual(outside.selectedLiteralCoordinates.map(x=>[x.ordinal,x.sourceElement]),[[2,'水'],[3,'木'],[4,'火'],[5,'土'],[6,'金']]);
  assert.equal(outside.outwardLayerOne,null);assert.equal(outside.extendAfterSixth,null);
  assert.deepEqual(outside.selectedLiteralCoordinates.map(x=>x.sourceSizeHeightWord),[null,null,null,null,null]);
  cases.push({caseID,inside,outside});
 }
 assert.equal(cases[1].inside.selectedLiteralCoordinates[0].sourceElement,'木');
 assert.deepEqual(cases[1].inside.unresolvedDiagramCells,[1,6]);
});
check('Wall and door together change origin; mixed and unknown boundaries cannot seed coordinates',()=>{
 for(const hasWall of [true,false,null])for(const hasDoor of [true,false,null])for(const declaredOrigin of ['current-enclosure','outer-main-gate','unknown']){
  const result=context({...base,boundary:{hasWall,hasDoor},declaredOrigin});
  const ready=hasWall===true&&hasDoor===true&&declaredOrigin==='current-enclosure'||hasWall===false&&hasDoor===false&&declaredOrigin==='outer-main-gate';
  assert.equal(result.selectedLiteralCoordinates!==null,ready);cases.push({hasWall,hasDoor,declaredOrigin,selected:result.selectedLiteralCoordinates!==null});
 }
});
check('Ten other diagrams, uncertain facing and modern storeys do not silently inherit the two clauses',()=>{
 for(let p=82;p<=93;p++)if(![82,84].includes(p))assert.equal(context({...base,caseID:'YZSS-C'+p}).selectedLiteralCoordinates,null);
 for(const firstRoomFacing of ['mixed','unknown'])assert.equal(context({...base,firstRoomFacing}).selectedLiteralCoordinates,null);
 for(const countBasis of ['modern-vertical-storeys','unknown'])assert.equal(context({...base,countBasis}).selectedLiteralCoordinates,null);
 for(const result of cases.filter(x=>x.inside).map(x=>x.inside)){assert.equal(result.practicalHeightAdvice,null);assert.equal(result.overallRecommendation,null);assert.equal(result.allProseAndGeometryConditionsApplied,false);}
});
check('Explicit facts and returned copies protect source data',()=>{
 assert.throws(()=>context({...base,extra:true}));assert.throws(()=>context({...base,boundary:{hasWall:true}}));assert.throws(()=>context({...base,firstRoomFacing:'outward'}));
 const x=context(base);x.selectedLiteralCoordinates[0].sourceElement='火';assert.equal(context(base).selectedLiteralCoordinates[0].sourceElement,'水');
});
const out={date:'2026-10-28',checks,cases,actualExistingLayerComponentCalls:0,actualHHCChartCalls:0,calendarEngineCalls:0,consumerChanged:false,fullMethodApplied:false};
writeFileSync(new URL('../qa/home-yangzhai-courtyards/CONTEXT_RESULTS.json',import.meta.url),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({checksPassed:checks.length,boundaryContexts:27,existingLayerComponentCalls:0,consumerChanged:false}));
