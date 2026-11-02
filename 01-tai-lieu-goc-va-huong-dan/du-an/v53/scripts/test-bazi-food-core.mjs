import{readFile,writeFile}from'node:fs/promises';import{createRequire}from'node:module';import{createHash}from'node:crypto';import{resolve}from'node:path';import vm from'node:vm';import assert from'node:assert/strict';import{inspectFoodCore as inspect}from'../research/bazi-food-core/core-reference.mjs';
const w=process.cwd(),s=new URL('../qa/bazi-food-core/',import.meta.url),read=async p=>JSON.parse(await readFile(resolve(w,p),'utf8')),sha=x=>createHash('sha256').update(x).digest('hex'),checks=[],records=[];
const check=async(name,fn)=>{await fn();checks.push({name,ok:true});};
const base={system:'TMTH005-food-core-selected',pillars:['甲戌','庚午','戊辰','庚申'],declaredFacts:{}},row=(out,id)=>out.rows.find(x=>x.id===id),vals=[true,false,null],and=x=>x.includes(false)?false:x.every(v=>v===true)?true:null;
let actualHHC=0,relationInspections=0,lunarRelationQueries=0,ternaryCases=0;
await check('TwoactualHHCsourceexamplechartsprojectrawvisibleFoodviarealrelationmoduleandrealLunarrelationtable;twofoodstemsneverautomaticallybecomemanyor傷官',async()=>{
 const previous=await read('archives/v53-before-bazi-food-core/PACKAGE_MANIFEST.json'),c={};c.window=c;vm.createContext(c);
 for(const file of['engine.js','bazi-relations.js']){const bytes=await readFile(resolve(w,'v53',file));assert.equal(sha(bytes),previous.files.find(x=>x.file===file).sha256);vm.runInContext(bytes.toString(),c);}
 const L=createRequire(import.meta.url)(resolve(w,'v46/node_modules/lunar-typescript')),p=await read('v53/qa/bazi-food-source/SOURCE_EXAMPLES_PROBE.json');
 for(const x of p.records){const chart=c.HHC_ENGINE.bazi(x.modernFeasibilityInput);actualHHC++;const pillars=Array.from(chart.pillars,x=>x.han);assert.deepEqual(pillars,x.expectedSourcePillars);const r=c.HHC_BAZI_RELATIONS.inspect(chart);relationInspections++;const food=r.gods.find(x=>x.name==='Thực Thần'),positions=food?Array.from(food.positions.visible,x=>x.pillarIndex):[];const out=inspect({...base,pillars}),nativePositions=[];
  for(let i=0;i<4;i++){const g=L.LunarUtil.SHI_SHEN[pillars[2][0]+pillars[i][0]];lunarRelationQueries++;if(g==='食神')nativePositions.push(i);}
  assert.deepEqual(out.visibleFoodPositions.map(x=>x.pillarIndex),positions);assert.deepEqual(positions,nativePositions);assert.deepEqual(out.sourceQuantity,{many:null,few:null,derivedFromRawCount:false});assert.equal(out.fixedRelationRemappedByRepeatedFood,false);assert.equal(row(out,'repeat-pattern-label').localDeclaredPremisesMatch,null);
  records.push({id:x.id,pillars,actualHHCFoodVisiblePositions:positions,actualLunarFoodVisiblePositions:nativePositions,sourceManyFewNotDetermined:true,historicalBirthDateAttributed:false,independentNewSourceExample:false});
 }
 assert.deepEqual(records.map(x=>x.actualHHCFoodVisiblePositions),[[1,3],[]]);
});
await check('BalancedsourcepremisesuseallthreeKleenevalues;falseisnotunknownandtruthneverestablisheswholepatternorstrength',()=>{
 for(const a of vals)for(const b of vals)for(const d of vals){const x=inspect({...base,declaredFacts:{dayStrong:a,foodStrong:b,effectiveClashOrDamageAbsent:d}});assert.equal(row(x,'balanced-core').localDeclaredPremisesMatch,and([a,b,d]));assert.equal(x.fullFoodPatternEstablished,null);assert.equal(x.strength,null);assert.equal(x.practicalOutcome,null);ternaryCases++;}
});
await check('Source多and少aredistinctnotcomplements;sealLuckisnotnatalpresence;samedeclaredsealLuckcanhaveopposedstancesonlywhenquantityframechanges',()=>{
 for(const many of vals)for(const few of vals)for(const seal of vals){if(many===true&&few===true){assert.throws(()=>inspect({...base,declaredFacts:{sourceFoodMany:many,sourceFoodFew:few,sealLuckEffective:seal}}));continue;}
  const out=inspect({...base,declaredFacts:{sourceFoodMany:many,sourceFoodFew:few,sealLuckEffective:seal}});assert.equal(row(out,'many-food-seal-luck').localDeclaredPremisesMatch,and([many,seal]));assert.equal(row(out,'few-food-seal-luck').localDeclaredPremisesMatch,and([few,seal]));ternaryCases++;
 }
 const out=inspect({...base,declaredFacts:{sourceFoodMany:false,sealLuckEffective:true}});assert.equal(out.sourceQuantity.few,null);assert.equal(row(out,'few-food-seal-luck').localDeclaredPremisesMatch,null);
});
await check('KnownyangandYindaygateonlytheirrespectivenamedhiddencombinationpremises;coordinatepolaritydoesnotestablisheffectivecombinationorfoodpurity',()=>{
 for(const day of['戊辰','癸酉',null])for(const hidden of vals)for(const pure of vals){const x=inspect({...base,pillars:[null,null,day,null],declaredFacts:{foodEffectiveHiddenOfficerCombination:hidden,foodEffectiveHiddenSealCombination:hidden,foodPure:pure,sourceOfficerSealNonmanifestCriterion:true}}),yang=day===null?null:day==='戊辰';
  assert.equal(row(x,'yang-hidden-officer').localDeclaredPremisesMatch,and([yang,hidden,true,pure]));assert.equal(row(x,'yin-hidden-seal').localDeclaredPremisesMatch,and([yang===null?null:!yang,hidden,true,pure]));assert.equal(x.virtualCombinationEffectiveness,null);ternaryCases++;
 }
});
await check('Repeatedfoodcontextuallabelrequiresseparatedeclarationandnevermutatesfixedrawrelations;sourceafflictionconditionsneverproducehealthorlongevityresult',()=>{
 const x=inspect({...base,declaredFacts:{repeatedFoodPatternCriterion:true,foodEffectivelyRestricted:true,foodEffectivelyVoid:true}});assert.equal(x.visibleFoodCount,2);assert.equal(row(x,'repeat-pattern-label').localDeclaredPremisesMatch,true);assert(x.visibleFoodPositions.every(x=>x.fixedRelation==='食神'));assert.equal(row(x,'food-restricted-and-void').localDeclaredPremisesMatch,true);assert.equal(x.healthResult,null);assert.equal(x.lifespan,null);assert.equal(x.consumerApplied,false);
});
await check('Unknownpillarsproduceonlyknownlowerbound;dayunknownpreventsallrelationclassification;missingdeclaredweaknessisnotcomplementofknownstrength',()=>{
 let x=inspect({...base,pillars:['甲戌',null,'戊辰','庚申']});assert.equal(x.visibleFoodCount,null);assert.equal(x.knownVisibleFoodCountLowerBound,1);assert.equal(x.visibleScanComplete,false);
 x=inspect({...base,pillars:['甲戌','庚午',null,'庚申']});assert.equal(x.knownVisibleFoodCountLowerBound,null);assert.equal(x.visibleFoodPositions.length,0);assert.equal(x.coordinateFacts.dayIsYang,null);
 x=inspect({...base,declaredFacts:{dayStrong:false,owlStrong:true}});assert.equal(row(x,'weak-day-strong-owl').localDeclaredPremisesMatch,null);
});
await check('Canonicalcoordinatesarenotdeclarable;strictunknowns,extraornonenumerablekeys,symbols,sparsepillars,invalidcyclepairsandmisnamedsystemrejectwithoutcoercion',()=>{
 const symbol={...base,[Symbol('extra')]:true},nonenum={...base};Object.defineProperty(nonenum,'extra',{value:true});
 for(const x of[null,{},[],symbol,nonenum,{...base,system:'universal-food'},{...base,pillars:Array(4)},{...base,pillars:['甲丑',...base.pillars.slice(1)]},{...base,declaredFacts:{dayIsYang:true}},{...base,declaredFacts:{sourceFoodMany:'true'}},{...base,declaredFacts:{sourceFoodMany:true,sourceFoodFew:true}},{...base,declaredFacts:{visibleFoodCount:2}}])assert.throws(()=>inspect(x));
 const x=inspect(base);x.pillars[0]='乙亥';x.rows[0].premises[0].value=true;assert.equal(inspect(base).pillars[0],'甲戌');assert.equal(row(inspect(base),'balanced-core').premises[0].value,null);
});
const out={date:'2026-10-28',checks,records,summary:{sourceParentContexts:8,selectedClauses:12,selectedCodepoints:135,localPredicateRules:11,declaredResearchFacts:21,derivedCoordinateFacts:2,ternaryCases,actualHHCBaziCalls:actualHHC,actualHHCFoodRelationInspections:relationInspections,actualLunarRelationTableQueries:lunarRelationQueries,actualNewCalendarSearchOrLunarForwardCharts:0,previousSourceExamplesReprojectedNotIndependentNewEvidence:true,fullFoodPatternClassifier:false,sourceStrengthValidated:false,sourceOutcomesValidated:false,consumerChanged:false,wholeCatalogueCompleted:false}};
await writeFile(new URL('RESULTS.json',s),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out));
