import assert from'node:assert/strict';import vm from'node:vm';import{readFileSync,writeFileSync}from'node:fs';import{resolve}from'node:path';import{createRequire}from'node:module';
import{OWL_EXCEPTION_SYSTEM as system,sourceOwlExceptionPremises as inspect}from'./owl-exception-reference.mjs';
const b=import.meta.dirname,w=resolve(b,'../..'),ctx={};ctx.window=ctx;vm.createContext(ctx);
for(const f of['engine.js','bazi-relations.js'])vm.runInContext(readFileSync(resolve(w,'v53',f),'utf8'),ctx);
const L=createRequire(import.meta.url)(resolve(w,'v46/node_modules/lunar-typescript')),stems=[...'甲乙丙丁戊己庚辛壬癸'];
const table=JSON.parse(readFileSync(resolve(b,'CLAUSE_PARTITION.json'),'utf8')),rows=table.records.filter(x=>x.sourceRecipientStemModel!==null),checks=[],relationRecords=[],mechanismRecords=[];
const check=(name,fn)=>{fn();checks.push({name,ok:true});};
const base=row=>({system,caseID:row.id,roleFrame:'source-recipient-model',recipientStem:row.sourceRecipientStemModel,owlStem:row.sourceOwlStemModel,namedPillarToken:row.namedPillarToken,declaredPremises:{}});
check('Complete digital parent partitions213codepoints into ten units while eight exception records retain distinct scopes',()=>{
 const source=JSON.parse(readFileSync(resolve(b,'RETAINED_CONTEXT.json'),'utf8')).context;
 assert.equal([...source.text].length,213);assert.equal(table.records.length,10);assert.equal(rows.length,8);assert.equal(table.records.map(x=>x.digitalText).join(''),source.text);
 assert.deepEqual(rows.filter(x=>x.namedPillarToken).map(x=>x.namedPillarToken),['己亥','丙午','乙巳','癸巳']);
 assert.equal(table.jiXinVersusXinDingPriorityResolved,false);
});
check('Eight actual HHC relation queries keep IndirectSeal fixed despite source not-fear/not-daoshi rhetoric',()=>{
 for(const row of rows){const actual=ctx.HHC_BAZI_RELATIONS.god(stems.indexOf(row.sourceRecipientStemModel),stems.indexOf(row.sourceOwlStemModel));assert.equal(actual,'Thiên Ấn');relationRecords.push({caseID:row.id,editorialRecipientStem:row.sourceRecipientStemModel,owlActorStem:row.sourceOwlStemModel,actualFixedHHCTenGod:actual,sourceNoFearOrNoDaoshiDoesNotRemapRelation:true});}
 assert.deepEqual(relationRecords.filter(x=>['ji-xin','geng-ren'].includes(x.caseID)).map(x=>[x.editorialRecipientStem,x.owlActorStem]),[['辛','己'],['壬','庚']]);
});
check('Four actual hidden-stem and four combination-table queries establish coordinate support only',()=>{
 for(const row of rows.filter(x=>x.namedPillarToken)){
  const hidden=[...L.LunarUtil.ZHI_HIDE_GAN[row.namedPillarToken[1]]],pair=row.sourceStatedCombinationPair;
  const partner=pair.find(x=>x!==row.sourceOwlStemModel),actualPartner=L.LunarUtil.HE_GAN_5[stems.indexOf(row.sourceOwlStemModel)];
  assert.equal(actualPartner,partner);assert(hidden.includes(partner));
  const out=inspect(base(row));assert.equal(out.localDeclaredPremisesMatch,null);assert.equal(out.effectiveCombinationAutomaticallyEstablished,false);
  mechanismRecords.push({caseID:row.id,namedSourceToken:row.namedPillarToken,actualFixedHiddenStems:hidden,statedPartner:partner,actualCombinationPartner:actualPartner,partnerInHiddenStemList:true,sourceRoleOrEffectiveTransformationValidated:false});
 }
 assert.equal(mechanismRecords.length,4);
});
let ternaryContexts=0;
check('Allcase-specificthree-valuedpremises preserve unknowns, negative controls and no natal-chart admission',()=>{
 const vals=[true,false,null],and=x=>x.includes(false)?false:x.every(v=>v===true)?true:null;
 for(const row of rows){
  const rec=(i,values)=>{if(i===row.requiredResearchPremises.length){const facts=Object.fromEntries(row.requiredResearchPremises.map((k,j)=>[k,values[j]])),out=inspect({...base(row),declaredPremises:facts});assert.equal(out.localDeclaredPremisesMatch,and(values));assert.equal(out.fullFoodPatternEstablished,null);assert.equal(out.fixedTenGodRemapping,null);assert.equal(out.practicalOutcome,null);ternaryContexts++;return;}for(const v of vals)rec(i+1,[...values,v]);};rec(0,[]);
  const facts=Object.fromEntries(row.requiredResearchPremises.map(k=>[k,true]));
  assert.equal(inspect({...base(row),declaredPremises:facts,roleFrame:'natal-chart'}).localDeclaredPremisesMatch,false);
  assert.equal(inspect({...base(row),declaredPremises:facts,recipientStem:null}).localDeclaredPremisesMatch,null);
  assert.equal(inspect({...base(row),declaredPremises:facts,recipientStem:stems[(stems.indexOf(row.sourceRecipientStemModel)+1)%10]}).localDeclaredPremisesMatch,false);
 }
 assert.equal(ternaryContexts,162);
});
check('Sin-Dingcondition is not inherited by another clause and unknown natal pillars never become source anchor facts',()=>{
 const row=rows.find(x=>x.id==='xin-ding'),x=base(row);assert.equal(inspect(x).localDeclaredPremisesMatch,null);
 assert.equal(inspect({...x,declaredPremises:{sourceAnchorRoleAccepted:true,sourceDingPresent:true}}).localDeclaredPremisesMatch,null);
 assert.throws(()=>inspect({...x,declaredPremises:{effectiveStatedCombination:true}}));
 assert.throws(()=>inspect({...x,pillars:['甲子','甲子','辛酉','甲子']}));assert.throws(()=>inspect({...x,roleFrame:'day-stem'}));
 assert.equal(rows.find(x=>x.id==='jihai').readingIssue.includes('土'),true);
 const copy=inspect(x);copy.sourceRecord.requiredResearchPremises.length=0;assert.equal(inspect(x).facts.length,3);
});
writeFileSync(resolve(b,'REFERENCE_RESULTS.json'),JSON.stringify({date:'2026-10-28',checks,actualHHCTenGodQueries:8,actualLunarHiddenStemTableQueries:4,actualLunarCombinationTableQueries:4,newCalendarChartCalls:0,
 ternaryContexts,relationRecords,mechanismRecords,consumerChanged:false,allC15ClausesApplied:false,sourceBirthChartAnchorsEstablished:false,sourceOutcomesValidated:false},null,2)+'\n');
console.log(JSON.stringify({checksPassed:checks.length,actualHHCTenGodQueries:8,lunarHiddenTableQueries:4,lunarCombinationTableQueries:4,ternaryContexts}));
