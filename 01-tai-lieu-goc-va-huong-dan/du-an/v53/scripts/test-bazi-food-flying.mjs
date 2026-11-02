import assert from 'node:assert/strict';
import vm from 'node:vm';
import {readFileSync,writeFileSync} from 'node:fs';
import {resolve} from 'node:path';
import {createRequire} from 'node:module';
import {createHash} from 'node:crypto';
import {sourceFlyingCoordinates as inspect} from '../research/bazi-food-gap-witness/flying-reference.mjs';
const b=resolve(import.meta.dirname,'../research/bazi-food-gap-witness'),w=resolve(b,'../../..'),ctx={};ctx.window=ctx;vm.createContext(ctx);
for(const name of ['engine.js','bazi-relations.js'])vm.runInContext(readFileSync(resolve(w,'v53',name),'utf8'),ctx);
const L=createRequire(import.meta.url)(resolve(w,'v46/node_modules/lunar-typescript'));
const table=JSON.parse(readFileSync(resolve(b,'DAY_AND_COORDINATE_TABLES.json'),'utf8'));
const stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'];
const cycle=Array.from({length:60},(_,i)=>stems[i%10]+branches[i%12]),checks=[],officers=[],labels=[],mechanisms=[];
const base=(s,p)=>({system:'TMTH005-'+s,pillars:p});
const check=(name,fn)=>{fn();checks.push({name,ok:true});};
check('Three named voices preserve literal four/two/six day sets without treating the Shangguan comment as a different eligibility list',()=>{
 assert.deepEqual(table.daySets.map(x=>x.days),[['庚子','壬子','辛亥','癸亥'],['丙午','丁巳'],['丙午','丙寅','丙戌','丁巳','丁未','丁卯']]);
 assert.deepEqual(table.finalFeiComment.positive,['庚子','辛亥']);assert.deepEqual(table.finalFeiComment.negative,['壬子','癸亥']);
 let n=0;
 for(const set of table.daySets){let hits=0;for(const day of cycle){const out=inspect(base(set.id,[null,null,day,null]));assert.equal(out.daySetMatches,set.days.includes(day));if(out.daySetMatches)hits++;n++;}assert.equal(hits,set.days.length);}
 assert.equal(n,180);
});
check('Six real HHC Officer relations and eighteen real lunar hidden/conflict/combine table queries support source coordinates without virtual pillar insertion',()=>{
 for(const row of table.mechanismCases){
  const actual=ctx.HHC_BAZI_RELATIONS.god(stems.indexOf(row.day[0]),stems.indexOf(row.sourceOfficerStem));assert.equal(actual,'Chính Quan');
  officers.push({caseID:row.id,day:row.day,sourceOfficer:row.sourceOfficerStem,actualTenGod:actual});
  const hidden=[...L.LunarUtil.ZHI_HIDE_GAN[row.virtualTargetBranch]],clash=L.LunarUtil.CHONG[branches.indexOf(row.repeatedBranch)],combine=L.LunarUtil.HE_ZHI_6[branches.indexOf(row.repeatedBranch)];
  assert.equal(clash,row.virtualTargetBranch);assert(hidden.includes(row.sourceOfficerStem));assert(row.printedRestraintBranchPool.includes(combine));
  mechanisms.push({caseID:row.id,actualHiddenStems:hidden,actualClashTarget:clash,actualSixCombinePartner:combine,
    additionalPrintedRestraintTokens:row.printedRestraintBranchPool.filter(x=>x!==combine),noSourceEfficacyProven:true});
 }
 assert.equal(officers.length,6);assert.deepEqual(mechanisms.find(x=>x.caseID==='dao-dingsi').additionalPrintedRestraintTokens,['辰']);
});
check('Four actual HHC relations to fixed principal month-hidden stems reproduce two Shangguan and two KiepTai coordinate labels only',()=>{
 for(const day of table.daySets[0].days){
  const principal=L.LunarUtil.ZHI_HIDE_GAN[day[1]][0],actual=ctx.HHC_BAZI_RELATIONS.god(stems.indexOf(day[0]),stems.indexOf(principal));
  assert.equal(actual,table.finalFeiComment.positive.includes(day)?'Thương Quan':'Kiếp Tài');
  labels.push({day,declaredSourceMonthBranch:day[1],actualFixedPrincipalHiddenStem:principal,actualTenGod:actual,actualBirthCalendarEstablished:false});
 }
 assert.deepEqual(labels.map(x=>x.actualTenGod),['Thương Quan','Kiếp Tài','Thương Quan','Kiếp Tài']);
});
check('Raw printed attraction and restraint can coexist; shared Dao pool is not automatically partitioned and no raw hit rejects a full pattern',()=>{
 const p=['甲子','丙辰','丁巳','戊申'],x=inspect(base('daochong-two-prose',p));
 assert.equal(x.daySetMatches,true);assert.deepEqual(x.rawMechanism.rawRestraintOccurrences.map(x=>x.symbol),['辰','申']);
 assert.deepEqual(x.rawMechanism.rawAttractionOccurrences.map(x=>x.symbol),['辰','申']);
 assert.equal(x.rawMechanism.attractionScope,'unassigned-collective-pool;notpartitionedintocase-specificbindingrules');
 assert.equal(x.wholePatternEstablished,null);assert.equal(x.rawMechanism.sourceRawHitsAreNotFinalRejection,true);
 assert.deepEqual(x.pillars,p);assert.equal(x.rawMechanism.sourceVirtualTarget.isActualPillar,false);assert.equal(x.pillars.length,4);
});
check('Source-first-party visible count is not silently converted into 多/有力 or hidden/filled-pillar verdict',()=>{
 const p=['庚子','壬子','庚子','丙寅'],x=inspect(base('feitian-four-prose',p));
 assert.equal(x.rawMechanism.knownRepeatedBranchCount,3);assert.deepEqual(x.rawMechanism.additionalRepeatedBranchPositions,[0,1]);
 assert.equal(x.rawMechanism.quantityThresholdAdjudicated,false);assert.equal(x.rawMechanism.visibleSourceOfficerPresence,false);assert.equal(x.rawMechanism.visibleVirtualTargetBranchPresence,false);
 assert.equal(x.effectiveVirtualClash,null);assert.equal(x.effectiveBinding,null);assert.equal(x.finalEditorTwoDayPreference,null);
 const a=inspect(base('feitian-four-prose',[...p.slice(0,3),null]));assert.equal(a.rawMechanism.visibleSourceOfficerPresence,null);assert.equal(a.rawMechanism.repeatedBranchInventoryComplete,false);
});
check('Two-day and six-day voices remain separate; literal extra days do not inherit earlier day mechanisms or become an automatic six-case rule',()=>{
 const p=['丙寅','丙午','丙戌','甲子'],a=inspect(base('daochong-six-quoted',p)),b=inspect(base('daochong-two-prose',p));
 assert.equal(a.daySetMatches,true);assert.equal(b.daySetMatches,false);assert.equal(a.rawMechanism,null);assert.equal(b.rawMechanism,null);
 assert.equal(a.sixDayQuoteVisibleInventory.allThreeFireBranchesVisible,true);assert.equal(a.sixDayQuoteVisibleInventory.knownBingStemCount,3);
 assert.equal(a.sixDayQuoteVisibleInventory.countDoesNotEstablishEffectiveThreeHarmony,true);assert.equal(a.wholePatternEstablished,null);
 assert.deepEqual(a.finalEditorTwoDayPreference,['丙午','丁巳']);assert.equal(a.sixDayQuoteNotErasedByPreference,true);
 assert.equal(inspect(base('feitian-four-prose',['甲子','丙寅','丙午','戊辰'])).rawMechanism,null);
 const c=inspect(base('daochong-six-quoted',[null,'丙午','丙戌','甲子']));assert.equal(c.sixDayQuoteVisibleInventory.allThreeFireBranchesVisible,null);
});
check('Joint 辛癸 mentions retain later focused 丙/戊 conditions without inventing severity or deleting the other source token',()=>{
 for(const [day,focus]of [['辛亥','丙'],['癸亥','戊']]){
  const out=inspect(base('feitian-four-prose',['丙寅','戊辰',day,'甲子']));
  assert.deepEqual(out.rawMechanism.rawStemMentionOccurrences.map(x=>x.symbol),['丙','戊']);assert.equal(out.rawMechanism.sourceFocusedStem,focus);assert.equal(out.practicalOutcome,null);
 }
});
check('Unknown pillars, impossible cycle pairs, extra calendar/strength keys and output mutation never establish a birth-chart rule',()=>{
 const x=base('feitian-four-prose',['甲子','丙寅','庚子',null]);
 for(const bad of [null,{},[],{...x,pillars:Array(4)},{...x,pillars:['甲丑','丙寅','庚子',null]},{...x,system:'daochong'},{...x,strong:true},{...x,date:'2026-10-28'},{...x,[Symbol('x')]:true},Object.create(x)])assert.throws(()=>inspect(bad));
 for(const set of table.daySets){const out=inspect(base(set.id,[null,null,null,null]));assert.equal(out.daySetMatches,null);assert.equal(out.wholePatternEstablished,null);assert.equal(out.consumerApplied,false);}
 const a=inspect(x);a.pillars[0]='乙丑';a.sourceDaySet.length=0;a.rawMechanism.printedAttractionPool.length=0;
 assert.equal(inspect(x).pillars[0],'甲子');assert.equal(inspect(x).sourceDaySet.length,4);assert.equal(inspect(x).rawMechanism.printedAttractionPool.length,3);
});
const hash=p=>createHash('sha256').update(readFileSync(p)).digest('hex');
const out={date:'2026-10-28',checks,officers,labels,mechanisms,
 summary:{completeChecks:8,namedDaySets:3,validDayMembershipCoordinates:180,literalMechanismCases:6,
  actualHHCTenGodQueries:10,officerHHCTenGodQueries:6,principalMonthHHCTenGodQueries:4,
  actualLunarHiddenStemTableQueries:10,actualLunarClashTableQueries:6,actualLunarSixCombineTableQueries:6,
  additionalLiteralRestraintNotStandardSixCombine:['丁巳:辰'],
  newCalendarChartCalls:0,newHHCBaziCalls:0,newIztroCalls:0,fullPatternMethodsApplied:false,
  virtualTargetAddedToActualPillars:false,consumerChanged:false,wholeCatalogueCompleted:false},
 actualModules:['engine.js','bazi-relations.js'].map(name=>({file:'v53/'+name,sha256:hash(resolve(w,'v53',name))}))};
writeFileSync(resolve(w,'v53/qa/bazi-food-gap-witness/REFERENCE_RESULTS.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out.summary));
