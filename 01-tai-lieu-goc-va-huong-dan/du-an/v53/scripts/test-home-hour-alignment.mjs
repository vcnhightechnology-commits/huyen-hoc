import assert from 'node:assert/strict';
import {readFileSync,writeFileSync} from 'node:fs';
import {resolve} from 'node:path';
import {createRequire} from 'node:module';
import {createHash} from 'node:crypto';
import {SOURCE_HOUR_SYSTEM,sourceLabelHour,sourceHourEvidence,sourceJieluActivityScope} from '../research/home-hour-alignment/source-hour-reference.mjs';
const b=resolve(import.meta.dirname,'../research/home-hour-alignment'),w=resolve(b,'../../..'),system=SOURCE_HOUR_SYSTEM;
const req=createRequire(resolve(w,'v46/node_modules/lunar-typescript/dist/index.cjs')),{Solar}=req('./index.cjs');
const table=JSON.parse(readFileSync(resolve(b,'MANUAL_HOUR_TABLE.json'),'utf8'));
const previous=JSON.parse(readFileSync(resolve(w,'v53/qa/home-yangzhai-final-spans/selection/REFERENCE_RESULTS.json'),'utf8'));
const dates=new Map(previous.fixtures.filter(x=>x.sourceLabel==='青龍').map(x=>[x.dayBranch,x.solar.day]));
const branches=[...'子丑寅卯辰巳午未申酉戌亥'],checks=[],fixtures=[];
const check=(name,fn)=>{fn();checks.push({name,ok:true});};
check('Corrected table separates two real headers from neighbor day guide',()=>{
 assert.equal(table.columns.length,12);assert.equal(table.directEnteredCells,144);
 assert.deepEqual(table.columns.find(x=>x.sourceLabel==='司命').hoursByDayBranch,[...'午申戌子寅辰午申戌子寅辰']);
 assert.deepEqual(table.columns.find(x=>x.sourceLabel==='勾陳').hoursByDayBranch,[...'未酉亥丑卯巳未酉亥丑卯巳']);
 assert.equal(table.excludedNeighborDayGuide.literal,'申子辰巳酉丑寅午戌亥卯未');
 assert.equal(table.excludedNeighborDayGuide.semanticRoleUnresolved,true);
});
check('All144 source coordinates execute actual lunar label and type queries',()=>{
 assert.equal(dates.size,12);
 for(const col of table.columns)for(let i=0;i<12;i++){
  const dayBranch=branches[i],sourceHour=col.hoursByDayBranch[i],hour=branches.indexOf(sourceHour)*2,day=dates.get(dayBranch);
  const lunar=Solar.fromYmdHms(2026,10,day,hour,0,0).getLunar();
  assert.equal(lunar.getDayZhiExact(),dayBranch);assert.equal(lunar.getTimeZhi(),sourceHour);
  const actualEngineLabel=lunar.getTimeTianShen(),actualEngineType=lunar.getTimeTianShenType();
  const comparisonAlias=table.comparisonAliasesOnly[col.sourceLabel]??col.sourceLabel;
  const typeAlias=col.sourceType==='黃道'?'黄道':col.sourceType;
  const match=actualEngineLabel===comparisonAlias,typeMatch=actualEngineType===typeAlias;
  fixtures.push({dayBranch,sourceLabel:col.sourceLabel,sourceHour,solar:{year:2026,month:10,day,hour,minute:0},actualEngineLabel,comparisonAlias,actualEngineType,sourceType:col.sourceType,match,typeMatch});
 }
 assert.equal(fixtures.length,144);assert(fixtures.every(x=>x.match&&x.typeMatch));
 assert.equal(fixtures.filter(x=>x.sourceLabel==='司命'&&x.match).length,12);
 assert.equal(fixtures.filter(x=>x.sourceLabel==='勾陳'&&x.match).length,12);
});
check('Every source day-hour coordinate has exactly one literal label; complete coordinates do not imply full method',()=>{
 for(const dayBranch of branches)for(const hourBranch of branches){
  const result=sourceHourEvidence({system,dayBranch,hourBranch});assert.equal(result.sourceLabels.length,1);
  assert.equal(result.coverageIncomplete,false);assert.deepEqual(result.pendingSourceLabels,[]);assert.equal(result.overallRecommendation,null);
  const label=result.sourceLabels[0].sourceLabel;assert.equal(sourceLabelHour({system,dayBranch,sourceLabel:label}).hourBranch,hourBranch);
 }
});
check('Editorial alias remains distinct from literal glyph and no new calendar or activity adapter is assumed',()=>{
 assert.equal(sourceLabelHour({system,dayBranch:'子',sourceLabel:'土堂'}).sourceLabel,'土堂');
 assert.throws(()=>sourceLabelHour({system,dayBranch:'子',sourceLabel:'玉堂'}));
 for(const activity of ['travel','marriage','relocation'])assert.equal(sourceJieluActivityScope({system,jieluStatus:true,activity}).sourceRestrictionApplies,true);
 assert.equal(sourceJieluActivityScope({system,jieluStatus:true,activity:'other'}).sourceRestrictionApplies,false);
 assert.equal(sourceJieluActivityScope({system,jieluStatus:null,activity:'travel'}).sourceRestrictionApplies,null);
 assert.throws(()=>sourceJieluActivityScope({system,jieluStatus:true,activity:'construction'}));
});
check('Wrong or implicit input remains rejected and copies cannot mutate corrected source',()=>{
 assert.throws(()=>sourceLabelHour({system:'modern',dayBranch:'子',sourceLabel:'司命'}));
 assert.throws(()=>sourceLabelHour({system,dayBranch:undefined,sourceLabel:'司命'}));
 const x=sourceHourEvidence({system,dayBranch:'子',hourBranch:'午'});x.sourceLabels[0].sourceLabel='changed';
 assert.equal(sourceHourEvidence({system,dayBranch:'子',hourBranch:'午'}).sourceLabels[0].sourceLabel,'司命');
});
check('Consumer product and actual chart engine stay byte-identical',()=>{
 const sha=p=>createHash('sha256').update(readFileSync(p)).digest('hex');
 for(const p of ['Huyen_Hoc_Cac.html','v53/Huyen_Hoc_Cac.html','v53/site/index.html'])assert.equal(sha(resolve(w,p)),'549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857');
 assert.equal(sha(resolve(w,'v53/engine.js')),'39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6');
});
writeFileSync(resolve(w,'v53/qa/home-hour-alignment/REFERENCE_RESULTS.json'),JSON.stringify({date:'2026-10-28',checks,actualLunarObjects:144,actualHourLabelQueries:144,actualHourTypeQueries:144,datesReusedFromPreviousFixturesButAssertedOnEachNewLunarObject:true,
 sourceCells:144,matchesAfterExplicitAliases:144,typeMatches:144,retainedHourCoordinateDifferences:0,previous12DifferencesRetractedAsTranscriptionError:true,
 unresolvedNeighborDayGuideMeaning:true,overallRecommendationValidated:false,newHHCExecutions:0,consumerChanged:false,fixtures},null,2)+'\n');
console.log(JSON.stringify({checksPassed:checks.length,actualLunarObjects:144,hourLabelsMatched:144,hourTypesMatched:144,consumerChanged:false}));
