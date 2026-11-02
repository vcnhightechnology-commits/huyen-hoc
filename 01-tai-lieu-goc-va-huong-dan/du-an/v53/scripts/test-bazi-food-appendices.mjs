import assert from 'node:assert/strict';
import vm from 'node:vm';
import {readFileSync,writeFileSync} from 'node:fs';
import {resolve} from 'node:path';
import {createRequire} from 'node:module';
import {createHash} from 'node:crypto';
import {sourceAppendixCoordinates as inspect,derivedSameNestCoordinate as nest} from '../research/bazi-food-appendices/appendix-reference.mjs';
const b=resolve(import.meta.dirname,'../research/bazi-food-appendices'),w=resolve(b,'../../..'),ctx={};ctx.window=ctx;vm.createContext(ctx);
for(const name of ['engine.js','bazi-relations.js'])vm.runInContext(readFileSync(resolve(w,'v53',name),'utf8'),ctx);
const L=createRequire(import.meta.url)(resolve(w,'v46/node_modules/lunar-typescript'));
const stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'];
const cycle=Array.from({length:60},(_,i)=>stems[i%10]+branches[i%12]);
const data=JSON.parse(readFileSync(resolve(b,'EXPLICIT_COORDINATES.json'),'utf8'));
const checks=[],relations=[],mechanisms=[],derived=[];
const check=(name,fn)=>{fn();checks.push({name,ok:true});};
const base=(system,anchorPillar,pillars,anchorFrame='source-declared')=>({system:'TMTH005-appendix-'+system,anchorPillar,pillars,anchorFrame});
const find=(input,id)=>inspect(input).cases.find(x=>x.caseID===id);
check('Seventeen retained contexts and twenty-three literal coordinate records retain six headings and eleven non-heading dispositions',()=>{
 const c=JSON.parse(readFileSync(resolve(b,'SELECTED_CONTEXTS.json'),'utf8'));
 const d=JSON.parse(readFileSync(resolve(b,'CLAUSE_DISPOSITIONS.json'),'utf8'));
 assert.equal(c.records.length,17);assert.equal(d.records.length,17);assert.equal(data.records.length,23);
 assert.equal(d.headings,6);assert.equal(d.nonHeadingContexts,11);
 assert.deepEqual(data.records.filter(x=>x.system==='fuxing').map(x=>[x.anchor,x.targets]),[['甲',['丙寅','丙子']],['乙',['丁亥','丁丑']]]);
 assert.deepEqual(data.records.filter(x=>x.system==='hongluan-tianyin').map(x=>[x.anchor,x.targets[0]]),[['丙','戊戌'],['辛','癸丑'],['壬','甲辰'],['乙','丁未']]);
 assert.deepEqual(data.records.filter(x=>x.system==='mochi').map(x=>[x.anchor,x.targets]),[['辛巳',['癸巳','癸亥']],['丙寅',['戊寅']],['戊申',['庚申']],['己巳',['辛亥']],['庚午',['壬申']],['甲戌',['丙寅']],['壬辰',['甲申']]]);
});
check('Twenty-six actual HHC relation calls preserve twenty-four FoodGod and two IndirectSeal literal coordinates',()=>{
 for(const row of data.records){
  const foodTargets=row.targetKind==='stem-and-branch'||row.targetKind==='stems'?row.targets.slice(0,1):row.targets;
  for(const target of foodTargets){
   const actual=ctx.HHC_BAZI_RELATIONS.god(stems.indexOf(row.anchor[0]),stems.indexOf(target[0]));
   assert.equal(actual,row.system==='tongke-owl'?'Thiên Ấn':'Thực Thần');
   relations.push({caseID:row.id,anchor:row.anchor,target,actualTenGod:actual});
  }
 }
 assert.equal(relations.length,26);assert.equal(relations.filter(x=>x.actualTenGod==='Thực Thần').length,24);
});
check('One actual lunar Lu and six combination-table queries support coordinates without establishing effective combination',()=>{
 const lu=L.LunarUtil.LU['丙'];assert.equal(lu,'巳');mechanisms.push({kind:'lu',stem:'丙',actual:lu});
 for(const row of data.records.filter(x=>x.system==='daihe')){
  const actual=L.LunarUtil.HE_GAN_5[stems.indexOf(row.targets[0])];assert.equal(actual,row.targets[1]);
  mechanisms.push({kind:'combination',caseID:row.id,foodStem:row.targets[0],actualPartner:actual});
 }
});
check('Tianchu requires both visible symbols in stated year-month-hour scope without inventing ten-stem table or colocation sufficiency',()=>{
 let x=find(base('tianchu','甲子',['庚午','丙寅','甲子','己巳']),'kitchen-jia');
 assert.deepEqual(x.targets.map(x=>x.present),[true,true]);assert.equal(x.listedCoordinateConjunction,true);
 assert.equal(inspect(base('tianchu','甲子',['庚午','丙寅','甲子','己巳'])).wholePatternEstablished,null);
 x=find(base('tianchu','甲子',['庚午','壬寅','甲子','己巳']),'kitchen-jia');assert.equal(x.listedCoordinateConjunction,false);
 x=find(base('tianchu','甲子',[null,'壬寅','甲子','己巳']),'kitchen-jia');assert.equal(x.listedCoordinateConjunction,null);
 const y=inspect(base('tianchu','乙丑',['乙丑','丙寅','乙丑','己巳']));assert.equal(y.cases[0].anchorMatches,false);assert(y.unlistedCasesAreUnknownNotRefuted);
});
check('Fuxing requires actual consistent year anchor; day or source-only anchor never silently replaces year; two targets remain unjoined',()=>{
 const p=['甲子','丙寅','甲戌','丙子'];
 let x=find(base('fuxing','甲子',p,'year'),'fortune-jia');
 assert.equal(x.coordinateGate,true);assert.deepEqual(x.targets.map(x=>x.present),[true,true]);assert.equal(x.listedCoordinateConjunction,null);assert.equal(x.targetJoinResolved,false);
 x=find(base('fuxing','甲戌',p,'day'),'fortune-jia');assert.equal(x.frameMatches,false);
 x=find(base('fuxing','甲子',p,'unknown'),'fortune-jia');assert.equal(x.frameMatches,null);
 assert.throws(()=>inspect(base('fuxing','甲戌',p,'year')));
});
check('Hongluan Tianyin scans only stated day-hour targets; an identical pillar in year/month cannot count',()=>{
 let x=find(base('hongluan-tianyin','丙子',['戊戌','庚寅','甲子','壬申']),'red-seal-丙');
 assert.equal(x.targets[0].present,false);assert.equal(x.singleTargetCoordinateMatch,false);
 x=find(base('hongluan-tianyin','丙子',['甲子','庚寅','戊戌',null]),'red-seal-丙');assert.equal(x.singleTargetCoordinateMatch,true);
 x=find(base('hongluan-tianyin','丙子',['戊戌','庚寅','甲子',null]),'red-seal-丙');assert.equal(x.singleTargetCoordinateMatch,null);
 assert.equal(inspect(base('hongluan-tianyin','丙子',['甲子','庚寅','戊戌',null])).sourceOutcome,null);
});
check('Mochi keeps first two targets separate and the six listed expansions do not become same-branch or a universal star table',()=>{
 const a=find(base('mochi','辛巳',['辛巳','壬辰','癸巳','甲子']),'ink-xinsi');
 assert.deepEqual(a.targets.map(x=>x.present),[true,false]);assert.equal(a.listedCoordinateConjunction,null);
 const b=find(base('mochi','己巳',['己巳','壬辰','辛亥','甲子']),'ink-己巳');assert.equal(b.singleTargetCoordinateMatch,true);
 assert.notEqual('己巳'[1],'辛亥'[1]);
 const c=find(base('tongke-owl','甲子',['甲子','丙寅','戊辰','壬子'],'year'),'owl-nest-jiazi');assert.equal(c.singleTargetCoordinateMatch,true);
 const d=find(base('tongke-owl','甲子',['甲子','壬子','戊辰','庚申'],'year'),'owl-nest-jiazi');assert.equal(d.singleTargetCoordinateMatch,false);
});
check('Sixty explicitly derived inclusive-thirteen coordinates cover all 3600 valid anchor-target pairs with sixty actual HHC relation queries',()=>{
 let matches=0;
 for(const a of cycle){
  const x=nest({system:'TMTH005-appendix-tongke-inclusive13-derived',anchorPillar:a,targetPillar:null});
  const actual=ctx.HHC_BAZI_RELATIONS.god(stems.indexOf(a[0]),stems.indexOf(x.expectedDerivedPillar[0]));
  assert.equal(actual,'Thực Thần');assert.equal(a[1],x.expectedDerivedPillar[1]);
  assert.equal(x.coordinateMatches,null);assert.equal(x.isPrintedSixtyRowTable,false);derived.push({anchor:a,target:x.expectedDerivedPillar,actualTenGod:actual});
  for(const t of cycle){const y=nest({system:x.system,anchorPillar:a,targetPillar:t});if(y.coordinateMatches)matches++;assert.equal(y.coordinateMatches,t[1]===a[1]&&stems.indexOf(t[0])===(stems.indexOf(a[0])+2)%10);}
 }
 assert.equal(matches,60);assert.equal(derived[0].target,'丙子');assert.notEqual(derived[0].target,cycle[13]);
 assert.equal(nest({system:'TMTH005-appendix-tongke-inclusive13-derived',anchorPillar:null,targetPillar:'丙子'}).coordinateMatches,null);
});
check('Strict unknowns, invalid cycles, scope contradictions and mutable output copies cannot turn into an established pattern',()=>{
 const x=base('mochi','辛巳',['辛巳','壬辰','癸巳',null]);
 for(const bad of [null,{},[],{...x,pillars:Array(4)},{...x,pillars:['甲丑',...x.pillars.slice(1)]},{...x,anchorPillar:'甲丑'},{...x,strength:true},{...x,anchorFrame:'natal'},{...x,[Symbol('x')]:1},Object.create(x)])assert.throws(()=>inspect(bad));
 const y=inspect(x);y.pillars[0]='甲子';y.cases[0].targets[0].present=false;
 assert.equal(inspect(x).pillars[0],'辛巳');assert.equal(inspect(x).cases[0].targets[0].present,true);
 for(const system of [...new Set(data.records.map(x=>x.system))]){
  const out=inspect(base(system,null,[null,null,null,null],'unknown'));
  assert.equal(out.wholePatternEstablished,null);assert.equal(out.sourceOutcome,null);assert.equal(out.consumerApplied,false);
  for(const c of out.cases){assert.equal(c.coordinateGate,null);assert(c.targets.every(x=>x.present===null));}
 }
});
const hash=p=>createHash('sha256').update(readFileSync(p)).digest('hex');
const out={date:'2026-10-28',checks,relations,mechanisms,derived,
 summary:{sourceUnits:6,sourceParentContexts:17,literalCoordinateRecords:23,
 finalHHCTenGodQueries:86,literalHHCTenGodQueries:26,derivedHHCTenGodQueries:60,
 actualLunarLuTableQueries:1,actualLunarCombinationTableQueries:6,
 derivedValidPairCoordinatesChecked:3600,derivedMatches:60,
 newCalendarChartCalls:0,newHHCBaziCalls:0,newIztroCalls:0,newHistoricalExamplesValidated:0,
 sourceAnchorRolesAutomaticallyEstablished:false,fullAppendixMethodsApplied:false,consumerChanged:false,wholeCatalogueCompleted:false},
 actualModules:['engine.js','bazi-relations.js'].map(name=>({file:'v53/'+name,sha256:hash(resolve(w,'v53',name))}))};
writeFileSync(resolve(w,'v53/qa/bazi-food-appendices/REFERENCE_RESULTS.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out.summary));
