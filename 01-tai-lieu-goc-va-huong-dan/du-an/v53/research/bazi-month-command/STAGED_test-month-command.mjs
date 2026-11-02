import assert from 'node:assert/strict';import {readFileSync,writeFileSync}from 'node:fs';import {resolve}from 'node:path';import {createRequire}from 'node:module';
import {MONTH_COMMAND_SYSTEM as system,sourceMonthCommandList as list}from './month-command-reference.mjs';
const b=import.meta.dirname,w=resolve(b,'../..'),L=createRequire(import.meta.url)(resolve(w,'v46/node_modules/lunar-typescript'));
const table=JSON.parse(readFileSync(resolve(b,'MANUAL_COMMAND_TABLES.json'),'utf8')),checks=[],comparisons=[];
const base={system,variant:'chapter-prose',monthBranch:'子',frame:'source-allocation-list'},check=(name,fn)=>{fn();checks.push({name,ok:true});};
check('Two literal source lists retain24 rows69 allocations and non-normalized totals',()=>{
 assert.equal(table.records.length,24);assert.equal(table.records.reduce((n,x)=>n+x.entries.length,0),69);
 assert.equal(table.records.filter(x=>x.variant==='chapter-prose').reduce((n,x)=>n+x.arithmeticDayTotal,0),360);
 assert.equal(table.records.filter(x=>x.variant==='cited-Yujing-table').reduce((n,x)=>n+x.arithmeticDayTotal,0),358);
 assert.equal(list({...base,variant:'cited-Yujing-table',monthBranch:'酉'}).arithmeticDayTotal,32);
 assert.equal(list({...base,variant:'cited-Yujing-table'}).arithmeticDayTotal,26);
});
check('24 actual lunar hidden-stem table accesses compare named source lists as a different data type',()=>{
 for(const row of table.records){
  const actualFixedStems=[...L.LunarUtil.ZHI_HIDE_GAN[row.monthBranch]],out=list({...base,variant:row.variant,monthBranch:row.monthBranch});
  const canonicalSourceSet=out.canonicalStemSet;
  const exactSetMatch=canonicalSourceSet===null?null:canonicalSourceSet.length===actualFixedStems.length&&canonicalSourceSet.every(x=>actualFixedStems.includes(x));
  comparisons.push({variant:row.variant,monthBranch:row.monthBranch,actualLunarFixedStems:actualFixedStems,canonicalSourceSet,unresolvedSourceLabels:out.unresolvedLabels,exactSetMatch,
   allSourceLabelsRetained:row.entries.map(x=>x.sourceLabel),notAnEngineBug:true,notProofOfEffectiveCommand:true});
 }
 assert.equal(comparisons.length,24);assert.equal(comparisons.filter(x=>x.exactSetMatch===null).length,2);
 const child=comparisons.filter(x=>x.monthBranch==='子');assert(child.every(x=>x.exactSetMatch===false));
 assert.deepEqual(child.map(x=>x.actualLunarFixedStems),[['癸'],['癸']]);
});
check('Earth palace labels remain unconverted; prose and Yujing branch sets are not silently merged',()=>{
 assert.deepEqual(list({...base,monthBranch:'寅'}).unresolvedLabels,['艮土']);assert.equal(list({...base,monthBranch:'寅'}).canonicalStemSet,null);
 assert.deepEqual(list({...base,monthBranch:'申'}).unresolvedLabels,['坤土']);
 assert.deepEqual(list({...base,monthBranch:'辰'}).sourceRow.entries.map(x=>x.sourceLabel),['乙','壬','戊']);
 assert.deepEqual(list({...base,variant:'cited-Yujing-table',monthBranch:'辰'}).sourceRow.entries.map(x=>x.sourceLabel),['戊','乙','癸']);
});
check('Unknown variant/frame/month and modern calendar queries cannot obtain a dominant stem or weights',()=>{
 for(const input of [{...base,variant:null},{...base,monthBranch:null},...['fixed-hidden-stems','actual-calendar-day','unknown'].map(frame=>({...base,frame}))])assert.equal(list(input).sourceRow,null);
 for(const row of table.records){const out=list({...base,variant:row.variant,monthBranch:row.monthBranch});for(const key of ['actualDayOffsetAdapter','actualDominantStem','fixedHiddenStemSubstitution','normalizedWeights','fullNatalStrength','practicalOutcome'])assert.equal(out[key],null);assert.equal(out.chronologicalOrderEstablished,false);}
 assert.throws(()=>list({...base,daysSinceJie:10}));assert.throws(()=>list({...base,variant:'auto'}));assert.throws(()=>list({...base,monthBranch:'Tý'}));
});
check('Original number anomalies and source-copy safety survive lookup',()=>{
 const audit=JSON.parse(readFileSync(resolve(b,'ARITHMETIC_AUDIT.json'),'utf8'));assert.equal(audit.source69AnnualCountIntro.computedTotal,4*35+4*35+2*50);assert.equal(audit.source69AnnualCountIntro.printedClaimedTotal,360);assert(audit.notCorrectedToConventionalTotals);
 const x=list(base);x.sourceRow.entries[0].days=0;assert.equal(list(base).sourceRow.entries[0].days,7);
});
const summary={actualLunarHiddenStemTableQueries:24,newCalendarChartCalls:0,sourceRows:24,allocationEntries:69,
 exactCanonicalSetMatches:comparisons.filter(x=>x.exactSetMatch===true).length,differentCanonicalSets:comparisons.filter(x=>x.exactSetMatch===false).length,unresolvedCanonicalSets:2};
writeFileSync(resolve(b,'REFERENCE_RESULTS.json'),JSON.stringify({date:'2026-10-28',checks,summary,comparisons,consumerChanged:false,actualDateCommandOrStrengthValidated:false},null,2)+'\n');
console.log(JSON.stringify({checksPassed:checks.length,...summary}));
