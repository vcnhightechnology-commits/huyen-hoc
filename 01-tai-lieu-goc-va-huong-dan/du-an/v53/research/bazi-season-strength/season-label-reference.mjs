import {readFileSync}from 'node:fs';
const table=JSON.parse(readFileSync(new URL('./MANUAL_SEASON_TABLE.json',import.meta.url),'utf8'));
export const SEASON_LABEL_SYSTEM='TMTH002-selected-five-season-labels';
const phases=['spring','summer','sixth-month-earth','autumn','winter'],elements=[...'木火土金水'];
function validate(input,keys){
 if(!input||Object.getPrototypeOf(input)!==Object.prototype||Reflect.ownKeys(input).length!==keys.length||keys.some(k=>!Object.hasOwn(input,k)||!Object.getOwnPropertyDescriptor(input,k).enumerable||!Object.hasOwn(Object.getOwnPropertyDescriptor(input,k),'value')))throw TypeError('Exact explicit plain inputs required');
 if(input.system!==SEASON_LABEL_SYSTEM||![...phases,null].includes(input.phase)||!['declared-source-label','calendar-date','solar-term-month','unknown'].includes(input.phaseBasis))throw TypeError('Named source and explicit source phase/basis required');
}
export function sourceSeasonState(input){
 validate(input,['system','phase','phaseBasis','element']);const {system,phase,phaseBasis,element}=input;
 if(![...elements,null].includes(element))throw TypeError('Canonical element/null required');
 const record=phaseBasis==='declared-source-label'&&phase!==null&&element!==null?table.records.find(x=>x.phase===phase&&x.element===element):null;
 return {system,phase,phaseBasis,element,sourceRecord:record?structuredClone(record):null,
  literalState:record?.literalState??null,recognizedState:record?.recognizedState??null,
  unresolvedPrintedGlyph:record!==null&&record.recognizedState===null,
  dateToPhaseAdapterEstablished:false,allFourSeasonEndsAdapterEstablished:false,
  genericNatalStrength:null,numericWeight:null,goodOrBad:null,healthPrediction:null,financialPrediction:null,
  twelveGrowthStage:null,fullNatalMethodApplied:false,practicalOutcome:null,consumerApplied:false};
}
export function sourceSeasonProfile(input){
 validate(input,['system','phase','phaseBasis']);
 const {system,phase,phaseBasis}=input,rows=phase!==null&&phaseBasis==='declared-source-label'?elements.map(element=>sourceSeasonState({system,phase,phaseBasis,element})):null;
 return {system,phase,phaseBasis,rows,wholeProfileStatesResolved:rows===null?null:rows.every(x=>x.recognizedState!==null),
  genericNatalStrength:null,overallRecommendation:null,sourceStatesAreNotFortuneVerdicts:true,consumerApplied:false};
}
