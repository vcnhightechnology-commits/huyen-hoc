import assert from 'node:assert/strict';import {readFileSync,writeFileSync}from 'node:fs';
import {SEASON_LABEL_SYSTEM as system,sourceSeasonState as state,sourceSeasonProfile as profile}from '../research/bazi-season-strength/season-label-reference.mjs';
const table=JSON.parse(readFileSync(new URL('../research/bazi-season-strength/MANUAL_SEASON_TABLE.json',import.meta.url),'utf8')),checks=[],coordinates=[];
const base={system,phase:'spring',phaseBasis:'declared-source-label',element:'木'},check=(name,fn)=>{fn();checks.push({name,ok:true});};
check('Five source phases preserve25slots with one literal因unclassified, not repaired by a common formula',()=>{
 assert.equal(table.records.length,25);assert.equal(table.records.filter(x=>x.recognizedState!==null).length,24);
 for(const row of table.records){const x=state({...base,phase:row.phase,element:row.element});assert.equal(x.literalState,row.literalState);assert.equal(x.recognizedState,row.recognizedState);coordinates.push({phase:row.phase,element:row.element,literal:x.literalState,recognized:x.recognizedState});}
 const x=state({...base,phase:'summer',element:'水'});assert.equal(x.literalState,'因');assert.equal(x.recognizedState,null);assert.equal(x.unresolvedPrintedGlyph,true);
 assert.equal(profile({system,phase:'summer',phaseBasis:'declared-source-label'}).wholeProfileStatesResolved,false);
});
check('Known direct coordinates retain distinctions among spring, autumn and separately named sixth month',()=>{
 assert.equal(state(base).recognizedState,'旺');assert.equal(state({...base,phase:'autumn'}).recognizedState,'死');
 assert.equal(state({...base,phase:'sixth-month-earth',element:'土'}).recognizedState,'旺');
 assert.equal(state({...base,phase:'winter',element:'土'}).recognizedState,'囚');
 assert.equal(state({...base,phase:'summer',element:'金'}).recognizedState,'死');
});
check('Calendar dates, solar-month labels and unknown inputs do not silently pick a source phase',()=>{
 for(const phaseBasis of ['calendar-date','solar-term-month','unknown']){assert.equal(state({...base,phaseBasis}).sourceRecord,null);assert.equal(profile({system,phase:'spring',phaseBasis}).rows,null);}
 assert.equal(state({...base,phase:null}).recognizedState,null);assert.equal(state({...base,element:null}).recognizedState,null);
 assert.throws(()=>state({...base,phase:'four-season-ends'}));assert.throws(()=>state({...base,month:6}));
});
check('Seasonal states never become numeric strength, twelve growth stages or fortune verdicts',()=>{
 for(const row of table.records){const x=state({...base,phase:row.phase,element:row.element});for(const key of ['genericNatalStrength','numericWeight','goodOrBad','healthPrediction','financialPrediction','twelveGrowthStage','practicalOutcome'])assert.equal(x[key],null);assert.equal(x.fullNatalMethodApplied,false);}
 for(const phase of ['spring','summer','sixth-month-earth','autumn','winter'])assert.equal(profile({system,phase,phaseBasis:'declared-source-label'}).overallRecommendation,null);
});
check('Wrong systems, aliases, extras and mutable returned source rows cannot corrupt the canonical table',()=>{
 assert.throws(()=>state({...base,system:'default'}));assert.throws(()=>state({...base,element:'Mộc'}));assert.throws(()=>state({...base,element:'甲'}));
 assert.throws(()=>state({...base,phaseBasis:undefined}));const x=state(base);x.sourceRecord.recognizedState='死';assert.equal(state(base).recognizedState,'旺');
});
writeFileSync(new URL('../qa/bazi-season-strength/REFERENCE_RESULTS.json',import.meta.url),JSON.stringify({date:'2026-10-28',checks,coordinates,sourceSlots:25,recognizedStateSlots:24,unclassifiedLiteralSlots:1,
 actualCalendarOrHHCEngineCalls:0,noEngineComparisonClaimed:true,datePhaseMappingValidated:false,fullStrengthEstablished:false,consumerChanged:false},null,2)+'\n');
console.log(JSON.stringify({checksPassed:checks.length,sourceSlots:25,recognized:24,unclassified:1,calendarEngineCalls:0}));
