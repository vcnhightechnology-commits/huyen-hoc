import assert from 'node:assert/strict';
import {readFileSync,writeFileSync} from 'node:fs';
import {resolve,basename} from 'node:path';
import {createHash} from 'node:crypto';
import {pathToFileURL} from 'node:url';
const b=import.meta.dirname,w=process.cwd(),read=p=>JSON.parse(readFileSync(p,'utf8').replace(/^\uFEFF/,'')),hash=p=>createHash('sha256').update(readFileSync(p)).digest('hex');
const f=read(resolve(b,'MANUAL_PRINTED_CASES.json')),a=read(resolve(b,'ACTUAL_RUNTIME.json')),freeze=read(resolve(b,'TRANSCRIPTION_FREEZE.json')),checks=[];
const check=(name,fn)=>{fn();checks.push({name,ok:true});};
const {derivedSameNestCoordinate:lookup}=await import(pathToFileURL(resolve(w,'v53/research/bazi-food-appendices/appendix-reference.mjs')));
check('Manual three-case transcription and expected role probes frozen before one actual batch',()=>{
 for(const x of freeze.files){const p=resolve(b,basename(x.file));assert.equal(readFileSync(p).length,x.bytes);assert.equal(hash(p),x.sha256);}
 assert.equal(hash(resolve(b,'TRANSCRIPTION_FREEZE.json')),a.freezeSHA256);assert(Date.parse(freeze.frozenAt)<=Date.parse(a.batchExecutedAt));
 assert.equal(a.summary.runtimeBatches,1);assert.equal(a.summary.printedFourPillarCases,3);
 const c=read(resolve(b,'SELECTED_CONTEXTS.json'));const parent=c.records.find(x=>x.id==='FOOD-05-C03');assert.equal(parent.text.replace('禄','祿'),c.manualImageC03);
 for(const x of f.records)assert(c.manualImageC03.includes(x.sourceName+x.pillars.join('')));
});
check('Thirty-six cached directed frames reproduce the reused coordinate function without new engine calls',()=>{
 const keys=new Set();let hits=0;
 for(const p of a.pairs){
  const row=f.records.find(x=>x.id===p.caseID),i=f.roleOrder.indexOf(p.rootRole),j=f.roleOrder.indexOf(p.targetRole);assert.notEqual(i,j);
  const key=[p.caseID,i,j].join(':');assert(!keys.has(key));keys.add(key);assert.equal(p.rootPillar,row.pillars[i]);assert.equal(p.targetPillar,row.pillars[j]);
  const actual=lookup({system:'TMTH005-appendix-tongke-inclusive13-derived',anchorPillar:p.rootPillar,targetPillar:p.targetPillar});assert.deepEqual(actual,p.reusedDerivedCoordinate);
  assert.equal(actual.coordinateMatches,p.foodGodAndSameBranch);if(actual.coordinateMatches)hits++;
  assert.equal(actual.wholePatternEstablished,null);assert.equal(actual.sourceOutcome,null);assert.equal(actual.consumerApplied,false);
 }
 assert.equal(keys.size,36);assert.equal(hits,3);assert.equal(new Set(a.pairs.map(x=>x.rootPillar[0]+x.targetPillar[0])).size,23);
});
check('Three editorial compatible role pairs preserve two year roots and one day root',()=>{
 for(const row of f.records){const hit=a.pairs.filter(x=>x.caseID===row.id&&x.foodGodAndSameBranch);assert.equal(hit.length,1);const p=hit[0],e=row.selectedPair;
  for(const k of ['rootRole','targetRole','rootPillar','targetPillar'])assert.equal(p[k],e[k]);assert.equal(p.actualHHCTenGod,e.hhcTenGod);assert.equal(p.actualLunarTenGod,e.lunarTenGod);
 }
 assert.equal(a.selected.filter(x=>x.selectedEditorialRolePair.rootRole==='year').length,2);assert.equal(a.selected.filter(x=>x.selectedEditorialRolePair.rootRole==='day').length,1);
 assert.equal(f.selectedRolePairsAreEditorialAnalysesNotPrintedRoleAnnotations,true);
});
check('Blind day-root substitution changes two coordinates; reverse direction does not establish the same nest',()=>{
 let changed=0;
 for(const row of f.records){const x=a.selected.find(x=>x.caseID===row.id),e=row.dayRootCounterfactual,p=x.dayRootCounterfactual;
  assert.equal(p.actualHHCTenGod,e.hhcTenGod);assert.equal(p.actualLunarTenGod,e.lunarTenGod);assert.equal(p.sameBranch,e.sameBranch);
  if(!p.foodGodAndSameBranch)changed++;
  const i=f.roleOrder.indexOf(e.targetRole);assert.equal(a.inspections.find(x=>x.caseID===row.id).actualInspection.pillars[i].visible.god,e.hhcTenGod);
  const reverse=a.pairs.find(p=>p.caseID===row.id&&p.rootRole===row.selectedPair.targetRole&&p.targetRole===row.selectedPair.rootRole);
  assert.equal(reverse.reusedDerivedCoordinate.coordinateMatches,false);assert.equal(reverse.actualLunarTenGod,'偏印');
 }
 assert.equal(changed,2);
});
check('Actual-batch accounting distinguishes relation calls, cached replay and birth charts',()=>{
 assert.equal(a.summary.directHHCGodCalls,36);assert.equal(a.summary.lunarTenGodTableQueries,36);assert.equal(a.summary.hhcInspectCalls,3);
 assert.equal(a.summary.inspectInternalGodCallsCounted,false);assert.equal(a.summary.actualHHCNatalCharts,0);assert.equal(a.summary.actualLunarCalendarObjects,0);assert.equal(a.summary.actualIztroCharts,0);
 assert.equal(a.summary.newHistoricalBirthDatesEstablished,0);assert.equal(a.summary.wholeSourceClauseApplied,false);
 for(const row of a.selected){assert.equal(row.wholePatternEstablished,null);assert.equal(row.sourceOutcome,null);}
 for(const x of read(resolve(b,'SOURCE_IDENTITIES.json')).files){const p=resolve(w,x.file);assert.equal(hash(p),x.sha256);assert.equal(readFileSync(p).length,x.bytes);}
});
check('Consumer remains unchanged and private role evidence is absent from the site',()=>{
 const paths=['Huyen_Hoc_Cac.html','v53/Huyen_Hoc_Cac.html','v53/site/index.html'];for(const p of paths){assert.equal(readFileSync(resolve(w,p)).length,707411);assert.equal(hash(resolve(w,p)),'549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857');}
 const html=readFileSync(resolve(w,paths[0]),'utf8');for(const s of ['MANUAL_PRINTED_CASES','foodGodAndSameBranch','韓魏公','宋秦檜'])assert(!html.includes(s));
});
const result={date:'2026-10-29',checks,summary:{completeChecks:checks.length,printedCases:3,directedCachedFrames:36,distinctStemPairs:23,selectedEditorialPairs:3,dayRootSubstitutionChanges:2,reversedCoordinatesNotMatched:3,actualRuntimeBatchesRetained:1,newHHCRelationCallsThisTest:0,newLunarTableQueriesThisTest:0,newHHCInspectCallsThisTest:0,newNatalChartsThisTest:0,consumerChanged:false,wholeSourceClauseApplied:false}};
if(!process.argv.includes('--no-write'))writeFileSync(resolve(b,'TEST_RESULTS.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result.summary));
