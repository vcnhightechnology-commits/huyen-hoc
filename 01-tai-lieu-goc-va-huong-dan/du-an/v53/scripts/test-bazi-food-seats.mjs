import assert from 'node:assert/strict';import vm from 'node:vm';import {readFileSync,writeFileSync}from 'node:fs';import {resolve}from 'node:path';
import {FOOD_SEAT_SYSTEM as system,sourceFoodSeat as seat}from '../research/bazi-food-seats/food-seat-reference.mjs';
const b=resolve(import.meta.dirname,'../research/bazi-food-seats'),w=resolve(b,'../../..'),c={};c.window=c;vm.createContext(c);
for(const f of ['engine.js','bazi-relations.js'])vm.runInContext(readFileSync(resolve(w,'v53',f),'utf8'),c);
const stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'];
const table=JSON.parse(readFileSync(resolve(b,'MANUAL_SEAT_CLAUSE.json'),'utf8')),checks=[],relationChecks=[],coordinates=[],chartProjections=[];
const base={system,anchorBasis:'day-stem',dayStem:'甲',targetPillar:'丙寅'},check=(name,fn)=>{fn();checks.push({name,ok:true});};
check('Five manual family groups keep20 branch memberships; paired stems are not a cross product',()=>{
 assert.equal(table.records.length,5);assert.equal(table.records.reduce((n,x)=>n+x.branches.length,0),20);
 assert.equal(seat(base).selectedSeatMembership,true);assert.equal(seat({...base,targetPillar:'丁卯'}).fixedFoodRelation,false);
 assert.equal(seat({...base,dayStem:'乙',targetPillar:'丁卯'}).selectedSeatMembership,true);
 assert.throws(()=>seat({...base,targetPillar:'丙卯'}));assert.throws(()=>seat({...base,dayStem:'乙',targetPillar:'丁午'}));
});
check('100 actual HHC Ten-God calls validate fixed relation across all ten day and ten target stems',()=>{
 for(let i=0;i<10;i++)for(let j=0;j<10;j++){
  const dayStem=stems[i],targetPillar=stems[j]+(j%2?'丑':'子'),result=seat({...base,dayStem,targetPillar});
  const actual=c.HHC_BAZI_RELATIONS.god(i,j);assert.equal(result.fixedFoodRelation,actual==='Thực Thần');
  relationChecks.push({dayStem,targetStem:stems[j],actualHHCTenGod:actual,sourceFoodRelation:result.fixedFoodRelation});
 }
 assert.equal(relationChecks.length,100);assert.equal(relationChecks.filter(x=>x.sourceFoodRelation).length,10);
});
check('600 valid coordinate contexts retain20 selected memberships without asserting strength from a miss',()=>{
 for(const dayStem of stems)for(let s=0;s<10;s++)for(let j=0;j<12;j++)if(s%2===j%2){
  const targetPillar=stems[s]+branches[j],x=seat({...base,dayStem,targetPillar});coordinates.push({dayStem,targetPillar,food:x.fixedFoodRelation,member:x.selectedSeatMembership});
  assert.equal(x.fullStrength,null);assert.equal(x.foodPatternEstablished,null);assert.equal(x.practicalOutcome,null);assert.equal(x.fullSourceClauseConditionsApplied,false);
 }
 assert.equal(coordinates.length,600);assert.equal(coordinates.filter(x=>x.food).length,60);assert.equal(coordinates.filter(x=>x.member).length,20);
 assert.equal(seat({...base,targetPillar:'丙子'}).selectedSeatMembership,false);
});
check('Two actual source-example HHC charts project new seat criteria without inventing historical dates',()=>{
 const examples=JSON.parse(readFileSync(resolve(w,'v53/qa/bazi-food-source/SOURCE_EXAMPLES_PROBE.json'),'utf8'));
 for(const x of examples.records){
  const chart=c.HHC_ENGINE.bazi(x.modernFeasibilityInput),pillars=Array.from(chart.pillars,x=>x.han);assert.deepEqual(pillars,x.expectedSourcePillars);
  const results=pillars.map(targetPillar=>seat({...base,dayStem:pillars[2][0],targetPillar}));
  chartProjections.push({modernFeasibilityInput:x.modernFeasibilityInput,pillars,matchingPillarIndices:results.flatMap((r,i)=>r.selectedSeatMembership?[i]:[]),fullStrength:null,historicalBirthDateAttributed:false,sourceOutcomesValidated:false});
 }
 assert.deepEqual(chartProjections.map(x=>x.matchingPillarIndices),[[1,3],[]]);
});
check('Unknown or wrong anchor stays unknown, and strict input/copies protect source facts',()=>{
 for(const input of [{...base,dayStem:null},{...base,targetPillar:null},{...base,anchorBasis:'birth-year-stem'},{...base,anchorBasis:'unknown'}])assert.equal(seat(input).selectedSeatMembership,null);
 assert.throws(()=>seat({...base,dayStem:'Giáp'}));assert.throws(()=>seat({...base,targetPillar:'丙寅 '}));assert.throws(()=>seat({...base,extra:true}));
 const x=seat(base);x.selectedGroup.branches[0]='子';assert.equal(seat(base).selectedGroup.branches[0],'寅');
});
writeFileSync(resolve(w,'v53/qa/bazi-food-seats/REFERENCE_RESULTS.json'),JSON.stringify({date:'2026-10-28',checks,actualHHCTenGodCalls:100,actualHHCBaziChartCalls:2,newLunarOrIztroCalls:0,
 abstractValidCoordinates:600,selectedMemberships:20,relationChecks,coordinates,chartProjections,consumerChanged:false,fullStrengthEstablished:false,fullC20ClauseConditionsApplied:false},null,2)+'\n');
console.log(JSON.stringify({checksPassed:checks.length,actualHHCTenGodCalls:100,actualHHCBaziCalls:2,coordinateContexts:600,selectedMemberships:20}));
