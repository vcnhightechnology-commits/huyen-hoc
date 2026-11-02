import assert from 'node:assert/strict';
import vm from 'node:vm';
import{readFileSync,writeFileSync}from'node:fs';
import{resolve}from'node:path';
import{createRequire}from'node:module';
import{FOOD_PILLAR_SOURCE as system,sourceFoodPillarExample as lookup}from'./source-pillar-example.mjs';
const b=resolve(import.meta.dirname),w=resolve(b,'../..'),ctx={};ctx.window=ctx;vm.createContext(ctx);
for(const name of['engine.js','bazi-relations.js'])vm.runInContext(readFileSync(resolve(w,'v53',name),'utf8'),ctx);
const L=createRequire(import.meta.url)(resolve(w,'v46/node_modules/lunar-typescript'));
const table=JSON.parse(readFileSync(resolve(b,'MANUAL_PILLAR_EXAMPLES.json'),'utf8'));
const stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'];
const cycle=Array.from({length:60},(_,i)=>stems[i%10]+branches[i%12]);
const base={system,rootPillar:'甲子',targetPillar:'丙辰',rootBasis:'declared-source-example'},checks=[],cases=[];
const check=(name,fn)=>{fn();checks.push({name,ok:true});};
let uniqueRelation,branchProbe,abstractFrames=0,unsupportedBasisFrames=0;
check('Six printed full-pillar cases retain their distinct descriptions',()=>{
 assert.deepEqual(table.records.map(x=>x.targetPillar),['丙子','丙寅','丙辰','丙午','丙申','丙戌']);
 assert.equal(table.sourceRootPillar,'甲子');
 for(const row of table.records){const actual=lookup({...base,targetPillar:row.targetPillar});assert.deepEqual(actual.sourceLabels,row.sourceLabels);assert.equal(actual.sourceRootNatalPosition,null);cases.push(actual);}
 assert.deepEqual(lookup(base).sourceLabels,['正印']);
 assert.deepEqual(lookup({...base,targetPillar:'丙午'}).sourceLabels,['自刑破命']);
});
check('One actual HHC and one actual lunar query compare the sole distinct stem pair; not six independent pairs',()=>{
 const hhc=ctx.HHC_BAZI_RELATIONS.god(0,2),lunar=L.LunarUtil.SHI_SHEN['甲丙'];
 assert.equal(hhc,'Thực Thần');assert.equal(lunar,'食神');
 uniqueRelation={rootStem:'甲',targetStem:'丙',actualHHCTenGod:hhc,actualLunarTenGod:lunar,applicablePrintedExamples:6,actualHHCRelationCalls:1,actualLunarTenGodTableQueries:1};
 branchProbe={rootBranch:'子',actualLunarClashPartner:L.LunarUtil.CHONG[0],printedTarget:'丙午',sourceDescription:lookup({...base,targetPillar:'丙午'}).sourceLabels,sourceSelfPunishmentMechanismAssigned:false};
 assert.equal(branchProbe.actualLunarClashPartner,'午');
 for(const x of cases){assert.equal(x.modernTenGod,null);assert.equal(x.modernBranchRelation,null);}
});
check('3600 canonical root/target frames expose only six directly printed cases; unlisted does not mean source-negative',()=>{
 let found=0;
 for(const rootPillar of cycle)for(const targetPillar of cycle){
  const x=lookup({...base,rootPillar,targetPillar});abstractFrames++;
  if(x.sourceExampleStatus==='directly-listed'){found++;assert.equal(rootPillar,'甲子');assert(table.records.some(r=>r.targetPillar===targetPillar));}
  else assert.equal(x.sourceLabels,null);
  for(const key of['gatheringScore','halfMultiplier','wholeFoodPatternEstablished','strength','practicalOutcome','sourceRootNatalPosition'])assert.equal(x[key],null);
  assert.equal(x.remainingStemGeneralizationImplemented,false);
 }
 assert.equal(found,6);assert.equal(abstractFrames,3600);
});
check('Named natal/calendar bases cannot borrow an unassigned source-root role',()=>{
 for(const rootBasis of['natal-day','natal-year','calendar-date','unknown'])for(const rootPillar of cycle)for(const row of table.records){
  const x=lookup({...base,rootBasis,rootPillar,targetPillar:row.targetPillar});assert.equal(x.sourceLabels,null);unsupportedBasisFrames++;
 }
 assert.equal(unsupportedBasisFrames,1440);
 for(const input of[{...base,rootPillar:null},{...base,targetPillar:null}])assert.equal(lookup(input).sourceLabels,null);
});
check('Strict input domains, isolated results and unchanged consumer bytes prevent accidental semantic promotion',()=>{
 for(const input of[{...base,rootPillar:'甲丑'},{...base,targetPillar:'丙辰 '},{...base,rootPillar:undefined},{...base,rootBasis:'day'},{...base,system:'all-schools'},{...base,forceModernTenGod:true},Object.assign(Object.create({}),base)])assert.throws(()=>lookup(input),TypeError);
 const x=lookup(base);x.sourceLabels[0]='食神';assert.deepEqual(lookup(base).sourceLabels,['正印']);
 const html=readFileSync(resolve(w,'v53/Huyen_Hoc_Cac.html'));assert.equal(html.length,707411);
 assert(html.equals(readFileSync(resolve(w,'Huyen_Hoc_Cac.html'))));assert(html.equals(readFileSync(resolve(w,'v53/site/index.html'))));
 assert(!html.includes(Buffer.from(system)));assert(!html.includes(Buffer.from('sourceFoodPillarExample')));
});
writeFileSync(resolve(b,'REFERENCE_RESULTS.json'),JSON.stringify({date:'2026-10-28',checks,uniqueRelation,branchProbe,cases,
 summary:{directlyPrintedCases:6,distinctComparedStemPairs:1,actualHHCRelationCalls:1,actualLunarTenGodTableQueries:1,actualLunarClashTableQueries:1,canonicalFrameQueries:abstractFrames,unsupportedBasisNullQueries:unsupportedBasisFrames,actualHHCBaziCharts:0,actualIztroCharts:0,sourceWholePatternImplemented:false,sourceOutcomesValidated:false,consumerChanged:false}},null,2)+'\n');
console.log(JSON.stringify({checksPassed:checks.length,printedCases:6,distinctComparedStemPairs:1,actualHHCRelationCalls:1,actualLunarTenGodTableQueries:1,actualLunarClashTableQueries:1,canonicalFrames:abstractFrames,unsupportedBases:unsupportedBasisFrames}));
