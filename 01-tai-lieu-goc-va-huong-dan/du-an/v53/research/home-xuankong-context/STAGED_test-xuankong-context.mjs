import assert from 'node:assert/strict';import vm from 'node:vm';
import {readFileSync,writeFileSync} from 'node:fs';import {resolve} from 'node:path';import {pathToFileURL} from 'node:url';
import {XUANKONG_SYSTEM as system,sourceXuanKongPolarity as polarity,sourceDeclaredRoomCountBalance as balance} from './xuankong-context-reference.mjs';
const b=import.meta.dirname,w=resolve(b,'../..'),checks=[],fixtures=[];const check=(name,fn)=>{fn();checks.push({name,ok:true});};
const {sourceMountainPolarity}=await import(pathToFileURL(resolve(w,'v53/research/home-yangzhai-door-water/source-water-reference.mjs')).href);
const core=readFileSync(resolve(w,'v53/engine.js'),'utf8'),ctx={window:{}};vm.createContext(ctx);vm.runInContext(core,ctx);
const old=JSON.parse(readFileSync(resolve(w,'v53/research/full-study/home/DAYOUNIAN_ENGINE_CHECK.json'),'utf8')),access=new Map(old.results.map(x=>[x.sourceTrigram,x.engineAccessInput]));
check('Eight direct source labels use four yang and four yin without classifying a measured room',()=>{
 for(const trigramLabel of [...'乾坎艮震巽離坤兌']){
  const x=polarity({system,frame:'source-xuankong-trigram-label',trigramLabel});assert.equal(x.sourcePolarity,[...'乾坎艮震'].includes(trigramLabel)?'陽':'陰');
  assert.equal(x.modernPlanRoomClassification,null);assert.equal(x.practicalOutcome,null);
 }
});
check('Eight actual HHC group fields and eight actual water-reference calls preserve differing named classifications',()=>{
 const mountain={乾:'乾',坎:'子',艮:'艮',震:'卯',巽:'巽',離:'午',坤:'坤',兌:'酉'};
 for(const trigramLabel of [...'乾坎艮震巽離坤兌']){
  const literal=polarity({system,frame:'source-xuankong-trigram-label',trigramLabel}).sourcePolarity;
  const input=access.get(trigramLabel),actual=ctx.window.HHC_ENGINE.directions(input);
  const modernBirthGroup=actual.kua.group,unjustifiedEastYangAlias=modernBirthGroup==='Đông'?'陽':'陰';
  const water=sourceMountainPolarity({system:'YZSS-Tianyige-water-mountain-table',mountain:mountain[trigramLabel]});
  fixtures.push({trigramLabel,literal,engineAccessInput:input,actualHHCNumber:actual.number,modernBirthGroup,unjustifiedEastYangAlias,
   birthGroupWouldDiffer:literal!==unjustifiedEastYangAlias,explicitWaterMountain:mountain[trigramLabel],actualWaterPolarity:water.polarity,waterClassificationDiffers:literal!==water.polarity});
 }
 assert.equal(fixtures.length,8);assert.equal(fixtures.filter(x=>x.birthGroupWouldDiffer).length,4);assert.equal(fixtures.filter(x=>x.waterClassificationDiffers).length,4);
});
check('Alternative or unknown frames never silently return XuanKong polarity',()=>{
 for(const frame of ['birth-fuyuan-group','water-mountain','unknown'])for(const trigramLabel of [...'乾坎艮震巽離坤兌'])assert.equal(polarity({system,frame,trigramLabel}).sourcePolarity,null);
 assert.equal(polarity({system,frame:'source-xuankong-trigram-label',trigramLabel:null}).sourcePolarity,null);
});
const base={system,countBasis:'declared-source-room-counts',classificationEstablished:true,inventoryComplete:true,yangRoomCount:2,yinRoomCount:1};
check('Only established complete positive source counts permit an arithmetic comparison',()=>{
 assert.equal(balance(base).selectedCountRelation,'more-yang');assert.equal(balance({...base,yangRoomCount:1,yinRoomCount:2}).selectedCountRelation,'more-yin');assert.equal(balance({...base,yangRoomCount:1,yinRoomCount:1}).selectedCountRelation,'equal');
 for(const classificationEstablished of [false,null])for(const inventoryComplete of [true,false,null])assert.equal(balance({...base,classificationEstablished,inventoryComplete}).selectedCountRelation,null);
 for(const inventoryComplete of [false,null])assert.equal(balance({...base,inventoryComplete}).selectedCountRelation,null);
 for(const countBasis of ['modern-vertical-storeys','area-weighted','unknown'])assert.equal(balance({...base,countBasis}).selectedCountRelation,null);
 for(const counts of [{yangRoomCount:null,yinRoomCount:1},{yangRoomCount:1,yinRoomCount:null},{yangRoomCount:0,yinRoomCount:0}])assert.equal(balance({...base,...counts}).selectedCountRelation,null);
});
check('Health, wealth and full exchange are not inferred; explicit data and copies are protected',()=>{
 for(const counts of [[1,1],[2,1],[1,2]]){const x=balance({...base,yangRoomCount:counts[0],yinRoomCount:counts[1]});assert.equal(x.healthPrediction,null);assert.equal(x.financialPrediction,null);assert.equal(x.fullSourceConditionsApplied,false);}
 assert.throws(()=>polarity({system,frame:'source-xuankong-trigram-label',trigramLabel:'Càn'}));assert.throws(()=>polarity({system:'default',frame:'source-xuankong-trigram-label',trigramLabel:'乾'}));
 assert.throws(()=>balance({...base,yangRoomCount:-1}));assert.throws(()=>balance({...base,yangRoomCount:'2'}));assert.throws(()=>balance({...base,extra:true}));
 const x=polarity({system,frame:'source-xuankong-trigram-label',trigramLabel:'乾'});x.sourceFamilyYang[0]='坤';assert.equal(polarity({system,frame:'source-xuankong-trigram-label',trigramLabel:'乾'}).sourceFamilyYang[0],'乾');
});
writeFileSync(resolve(b,'REFERENCE_RESULTS.json'),JSON.stringify({date:'2026-10-28',checks,actualHHCDirectionsCalls:8,actualWaterReferenceCalls:8,newCalendarCalls:0,fixtures,
 differingBirthGroupProjections:4,differingWaterPolarityProjections:4,notEngineBugsOrPracticalOutcomes:true,consumerChanged:false,fullXuanKongExchangeApplied:false},null,2)+'\n');
console.log(JSON.stringify({checksPassed:checks.length,actualHHCDirectionsCalls:8,actualWaterReferenceCalls:8,birthGroupDifferences:4,waterDifferences:4}));
