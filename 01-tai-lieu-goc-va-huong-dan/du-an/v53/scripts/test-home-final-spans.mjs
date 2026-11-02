import assert from 'node:assert/strict';
import {readFileSync,writeFileSync} from 'node:fs';
import {resolve} from 'node:path';
import {createRequire} from 'node:module';
import {createHash} from 'node:crypto';
import {SOURCE_HOUR_SYSTEM,sourceLabelHour,sourceHourEvidence,sourceJieluActivityScope} from '../research/home-yangzhai-final-spans/selection/source-hour-reference.mjs';
const b=resolve(import.meta.dirname,'../research/home-yangzhai-final-spans/selection'),w=resolve(b,'../../../..'),r=resolve(w,'v53');
const req=createRequire(resolve(w,'v46/node_modules/lunar-typescript/dist/index.cjs'));
const {Solar}=req('./index.cjs');
const table=JSON.parse(readFileSync(resolve(b,'MANUAL_HOUR_TABLE.json'),'utf8'));
const branches=[...'子丑寅卯辰巳午未申酉戌亥'],system=SOURCE_HOUR_SYSTEM,checks=[],fixtures=[];
let calls=0;
const check=(name,fn)=>{fn();checks.push({name,ok:true});};
check('Manual entry has 11 columns and 132 literal cells; unresolved last column stays open',()=>{
 assert.equal(table.columns.length,11);assert.equal(table.directEnteredCells,132);
 for(const col of table.columns){assert.equal(col.hoursByDayBranch.length,12);for(const h of col.hoursByDayBranch)assert(branches.includes(h));}
 assert.equal(sourceLabelHour({system,dayBranch:'子',sourceLabel:'勾陳'}).hourBranch,null);
});
check('Literal printed coordinates remain distinguishable from editorial aliases',()=>{
 assert.equal(sourceLabelHour({system,dayBranch:'子',sourceLabel:'土堂'}).sourceLabel,'土堂');
 assert.equal(sourceLabelHour({system,dayBranch:'子',sourceLabel:'司命'}).hourBranch,'未');
 assert.equal(sourceLabelHour({system,dayBranch:'丑',sourceLabel:'司命'}).hourBranch,'酉');
 assert.throws(()=>sourceLabelHour({system,dayBranch:'子',sourceLabel:'玉堂'}));
});
check('Actual lunar-typescript executions compare all 132 entered coordinates without rewriting source differences',()=>{
 const dates=new Map();
 for(let day=1;day<=12;day++){
  const solar=Solar.fromYmdHms(2026,10,day,12,0,0),lunar=solar.getLunar();calls++;
  dates.set(lunar.getDayZhi(),day);
 }
 assert.equal(dates.size,12);
 for(const col of table.columns)for(let i=0;i<12;i++){
  const dayBranch=branches[i],h=branches.indexOf(col.hoursByDayBranch[i]),day=dates.get(dayBranch);
  const lunar=Solar.fromYmdHms(2026,10,day,h*2,0,0).getLunar();calls++;
  assert.equal(lunar.getDayZhiExact(),dayBranch);assert.equal(lunar.getTimeZhi(),col.hoursByDayBranch[i]);
  const actual=lunar.getTimeTianShen(),alias=table.comparisonAliasesOnly[col.sourceLabel]??col.sourceLabel;
  const record={dayBranch,sourceLabel:col.sourceLabel,sourceHour:col.hoursByDayBranch[i],sourceType:col.sourceType,
   solar:{year:2026,month:10,day,hour:h*2,minute:0},actualEngineLabel:actual,comparisonAlias:alias,match:actual===alias};
  fixtures.push(record);
 }
 const matches=fixtures.filter(x=>x.match),different=fixtures.filter(x=>!x.match);
 assert.equal(matches.length,120);assert.equal(different.length,12);
 assert(different.every(x=>x.sourceLabel==='司命'&&x.actualEngineLabel==='勾陈'));
 assert.equal(matches.filter(x=>x.sourceLabel==='土堂'&&x.comparisonAlias==='玉堂').length,12);
});
check('Unknown and uncovered hour rows never become unlucky defaults',()=>{
 for(const dayBranch of branches)for(const hourBranch of branches){
  const result=sourceHourEvidence({system,dayBranch,hourBranch});
  assert.equal(result.coverageIncomplete,true);assert.equal(result.overallRecommendation,null);
  assert.equal(result.missingLabelIsNotAnUnluckyHour,true);
  for(const row of result.sourceLabels)assert.equal(sourceLabelHour({system,dayBranch,sourceLabel:row.sourceLabel}).hourBranch,hourBranch);
 }
});
check('Source restriction applies only to three named activities, with unknown kept unknown',()=>{
 for(const jieluStatus of [true,false,null])for(const activity of ['travel','marriage','relocation','other','unknown']){
  const result=sourceJieluActivityScope({system,jieluStatus,activity});
  const expected=jieluStatus===false?false:jieluStatus===null||activity==='unknown'?null:activity!=='other';
  assert.equal(result.sourceRestrictionApplies,expected);assert.equal(result.overallRecommendation,null);
 }
});
check('Strict input rejects implicit calendar, aliases and coercion',()=>{
 for(const dayBranch of ['Tý',' 子',0,null,undefined])assert.throws(()=>sourceLabelHour({system,dayBranch,sourceLabel:'青龍'}));
 for(const bad of [undefined,'modern',''])assert.throws(()=>sourceHourEvidence({system:bad,dayBranch:'子',hourBranch:'申'}));
 for(const jieluStatus of [undefined,'true',0,1])assert.throws(()=>sourceJieluActivityScope({system,jieluStatus,activity:'travel'}));
 assert.throws(()=>sourceJieluActivityScope({system,jieluStatus:true,activity:'construction'}));
});
check('Results cannot mutate the preserved manual table',()=>{
 const result=sourceHourEvidence({system,dayBranch:'子',hourBranch:'申'});result.sourceLabels[0].sourceLabel='changed';result.pendingSourceLabels.push('changed');
 assert.equal(sourceHourEvidence({system,dayBranch:'子',hourBranch:'申'}).sourceLabels[0].sourceLabel,'青龍');
 assert.deepEqual(sourceHourEvidence({system,dayBranch:'子',hourBranch:'申'}).pendingSourceLabels,['勾陳']);
});
check('Consumer HTML and engine preserve the verified release bytes',()=>{
 const sha=p=>createHash('sha256').update(readFileSync(p)).digest('hex');
 for(const p of [resolve(w,'Huyen_Hoc_Cac.html'),resolve(r,'Huyen_Hoc_Cac.html'),resolve(r,'site/index.html')])assert.equal(sha(p),'549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857');
 assert.equal(sha(resolve(r,'engine.js')),'39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6');
});
writeFileSync(resolve(r,'qa/home-yangzhai-final-spans/selection/REFERENCE_RESULTS.json'),JSON.stringify({date:'2026-10-28',checks,actualLunarObjects:calls,
 actualHourLabelQueries:132,dateBranchProbeObjects:12,manualCellsCompared:132,matchesAfterExplicitAliases:120,
 matchesUsingTuTangAlias:12,literalSimingDifferencesRetained:12,untranscribedGouChenCells:12,
 newHHCExecutions:0,noConsumerChange:true,overallRecommendationValidated:false,fixtures},null,2)+'\n');
console.log(JSON.stringify({checks:checks.length,actualLunarObjects:calls,actualHourLabelQueries:132,matches:120,retainedDifferences:12}));
