import {readFileSync,writeFileSync,existsSync} from 'node:fs';
import {resolve} from 'node:path';
import {pathToFileURL} from 'node:url';
import {createRequire} from 'node:module';
import {createHash} from 'node:crypto';
import vm from 'node:vm';
import assert from 'node:assert/strict';
const b=import.meta.dirname,w=process.cwd(),out=resolve(b,'ACTUAL_RUNTIME.json');
if(existsSync(out))throw Error('One-time actual batch already exists; use test-evidence.mjs instead.');
const read=p=>JSON.parse(readFileSync(p,'utf8').replace(/^\uFEFF/,''));
const hash=p=>createHash('sha256').update(readFileSync(p)).digest('hex');
const freeze=read(resolve(b,'TRANSCRIPTION_FREEZE.json'));
for(const row of freeze.files){const p=resolve(w,row.file);assert.equal(hash(p),row.sha256);assert.equal(readFileSync(p).length,row.bytes);}
const fixture=read(resolve(b,'MANUAL_PRINTED_CASES.json'));
const {derivedSameNestCoordinate}=await import(pathToFileURL(resolve(w,'v53/research/bazi-food-appendices/appendix-reference.mjs')));
const ctx={};ctx.window=ctx;vm.createContext(ctx);
for(const f of ['engine.js','bazi-relations.js'])vm.runInContext(readFileSync(resolve(w,'v53',f),'utf8'),ctx);
const req=createRequire(import.meta.url),L=req(resolve(w,'v46/node_modules/lunar-typescript'));
assert.equal(req(resolve(w,'v46/node_modules/lunar-typescript/package.json')).version,'1.8.6');
const stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'],roles=fixture.roleOrder;
const godMap={'比肩':'Tỷ Kiên','劫财':'Kiếp Tài','食神':'Thực Thần','伤官':'Thương Quan','偏财':'Thiên Tài','正财':'Chính Tài','七杀':'Thất Sát','正官':'Chính Quan','偏印':'Thiên Ấn','正印':'Chính Ấn'};
const pairs=[],inspections=[],selected=[];
for(const row of fixture.records){
 const all=row.pillars.map(p=>({s:stems.indexOf(p[0]),b:branches.indexOf(p[1])}));
 const inspected=JSON.parse(JSON.stringify(ctx.HHC_BAZI_RELATIONS.inspect({all,dayP:all[2]})));
 inspections.push({caseID:row.id,inputIsExplicitPrintedPillars:true,calendarBirthChart:false,actualInspection:inspected});
 for(let i=0;i<4;i++)for(let j=0;j<4;j++)if(i!==j){
  const a=row.pillars[i],t=row.pillars[j];
  const hhc=ctx.HHC_BAZI_RELATIONS.god(stems.indexOf(a[0]),stems.indexOf(t[0]));
  const lunar=L.LunarUtil.SHI_SHEN[a[0]+t[0]];
  assert.equal(hhc,godMap[lunar]);
  const derived=derivedSameNestCoordinate({system:'TMTH005-appendix-tongke-inclusive13-derived',anchorPillar:a,targetPillar:t});
  const sameBranch=a[1]===t[1],foodAndSame=hhc==='Thực Thần'&&sameBranch;
  assert.equal(derived.coordinateMatches,foodAndSame);
  pairs.push({caseID:row.id,rootRole:roles[i],targetRole:roles[j],rootPillar:a,targetPillar:t,actualHHCTenGod:hhc,actualLunarTenGod:lunar,sameBranch,reusedDerivedCoordinate:derived,foodGodAndSameBranch:foodAndSame});
 }
 const e=row.selectedPair,d=row.dayRootCounterfactual;
 const hit=pairs.find(x=>x.caseID===row.id&&x.rootRole===e.rootRole&&x.targetRole===e.targetRole);
 assert.equal(hit.rootPillar,e.rootPillar);assert.equal(hit.targetPillar,e.targetPillar);assert.equal(hit.actualHHCTenGod,e.hhcTenGod);assert.equal(hit.actualLunarTenGod,e.lunarTenGod);assert.equal(hit.foodGodAndSameBranch,true);
 const day=pairs.find(x=>x.caseID===row.id&&x.rootRole==='day'&&x.targetRole===d.targetRole);
 assert.equal(day.rootPillar,d.rootPillar);assert.equal(day.targetPillar,d.targetPillar);assert.equal(day.actualHHCTenGod,d.hhcTenGod);assert.equal(day.actualLunarTenGod,d.lunarTenGod);assert.equal(day.sameBranch,d.sameBranch);
 assert.equal(inspected.pillars[roles.indexOf(d.targetRole)].visible.god,d.hhcTenGod);
 selected.push({caseID:row.id,selectedEditorialRolePair:hit,dayRootCounterfactual:day,wholePatternEstablished:null,sourceOutcome:null,printedRolesNotExplicitlyAnnotated:true});
}
assert.equal(pairs.length,36);assert.equal(pairs.filter(x=>x.foodGodAndSameBranch).length,3);
assert.equal(selected.filter(x=>!x.dayRootCounterfactual.foodGodAndSameBranch).length,2);
const result={date:'2026-10-29',batchExecutedAt:new Date().toISOString(),freezeSHA256:hash(resolve(b,'TRANSCRIPTION_FREEZE.json')),scriptSHA256:hash(resolve(b,'run-actual-once.mjs')),engineSHA256:hash(resolve(w,'v53/engine.js')),relationsSHA256:hash(resolve(w,'v53/bazi-relations.js')),lunarLibrarySHA256:hash(resolve(w,'v46/node_modules/lunar-typescript/dist/index.cjs')),pairs,inspections,selected,summary:{printedFourPillarCases:3,directedRolePairs:36,distinctStemPairs:new Set(pairs.map(x=>x.rootPillar[0]+x.targetPillar[0])).size,directHHCGodCalls:36,lunarTenGodTableQueries:36,hhcInspectCalls:3,inspectInternalGodCallsCounted:false,selectedCandidatePairs:3,yearRootCandidates:2,dayRootCandidates:1,blindDaySubstitutionsChangingCoordinate:2,actualHHCNatalCharts:0,actualLunarCalendarObjects:0,actualIztroCharts:0,newHistoricalBirthDatesEstablished:0,wholeSourceClauseApplied:false,consumerChanged:false,runtimeBatches:1}};
writeFileSync(out,JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result.summary));
