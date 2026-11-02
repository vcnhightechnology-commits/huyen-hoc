import {readFileSync}from 'node:fs';
const table=JSON.parse(readFileSync(new URL('./MANUAL_COMMAND_TABLES.json',import.meta.url),'utf8'));
export const MONTH_COMMAND_SYSTEM='TMTH002-month-command-two-lists';
const variants=['chapter-prose','cited-Yujing-table'],branches=[...'子丑寅卯辰巳午未申酉戌亥'];
export function sourceMonthCommandList(input){
 const keys=['system','variant','monthBranch','frame'];
 if(!input||Object.getPrototypeOf(input)!==Object.prototype||Reflect.ownKeys(input).length!==keys.length||keys.some(k=>!Object.hasOwn(input,k)||!Object.getOwnPropertyDescriptor(input,k).enumerable||!Object.hasOwn(Object.getOwnPropertyDescriptor(input,k),'value')))throw TypeError('Four exact declared plain data fields required');
 const {system,variant,monthBranch,frame}=input;
 if(system!==MONTH_COMMAND_SYSTEM||![...variants,null].includes(variant)||!(monthBranch===null||branches.includes(monthBranch))||!['source-allocation-list','fixed-hidden-stems','actual-calendar-day','unknown'].includes(frame))throw TypeError('Named system, explicit list, month label and frame required');
 const record=variant!==null&&monthBranch!==null&&frame==='source-allocation-list'?table.records.find(x=>x.variant===variant&&x.monthBranch===monthBranch):null;
 return {system,variant,monthBranch,frame,sourceRow:record?structuredClone(record):null,
  arithmeticDayTotal:record?.arithmeticDayTotal??null,
  equalsNominalThirty:record?record.arithmeticDayTotal===30:null,
  canonicalStemSet:record?record.entries.every(x=>x.canonicalStem!==null)?[...new Set(record.entries.map(x=>x.canonicalStem))]:null:null,
  unresolvedLabels:record?record.entries.filter(x=>x.canonicalStem===null).map(x=>x.sourceLabel):[],
  chronologicalOrderEstablished:false,actualDayOffsetAdapter:null,actualDominantStem:null,
  fixedHiddenStemSubstitution:null,normalizedWeights:null,fullNatalStrength:null,
  sourceVariantsAdjudicated:false,practicalOutcome:null,consumerApplied:false};
}
