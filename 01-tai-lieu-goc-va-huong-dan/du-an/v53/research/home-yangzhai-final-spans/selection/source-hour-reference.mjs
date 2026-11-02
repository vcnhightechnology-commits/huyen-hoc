import {readFileSync} from 'node:fs';
const table=JSON.parse(readFileSync(new URL('./MANUAL_HOUR_TABLE.json',import.meta.url),'utf8'));
export const SOURCE_HOUR_SYSTEM='YZSS-Tianyige-hour-table-134-135';
const branches=[...'子丑寅卯辰巳午未申酉戌亥'];
const exact=(value,values,name)=>{if(!values.includes(value))throw new TypeError(`Invalid ${name}`);};
const systemCheck=value=>exact(value,[SOURCE_HOUR_SYSTEM],'system');
// This is a bounded printed-table lookup. It does not repair the witness from a modern formula.
export function sourceLabelHour({system,dayBranch,sourceLabel}){
 systemCheck(system);exact(dayBranch,branches,'day branch');
 exact(sourceLabel,[...table.columns.map(x=>x.sourceLabel),'勾陳'],'source label');
 const row=table.columns.find(x=>x.sourceLabel===sourceLabel);
 if(!row)return {system,dayBranch,sourceLabel,hourBranch:null,sourceType:null,status:'unresolved-printed-column',overallRecommendation:null};
 return {system,dayBranch,sourceLabel,hourBranch:row.hoursByDayBranch[branches.indexOf(dayBranch)],
  sourceType:row.sourceType,sourcePDFPage:row.sourcePDFPage,status:sourceLabel==='司命'?'literal-source-engine-discrepancy':'literal-source-coordinate',
  overallRecommendation:null};
}
export function sourceHourEvidence({system,dayBranch,hourBranch}){
 systemCheck(system);exact(dayBranch,branches,'day branch');exact(hourBranch,branches,'hour branch');
 const sourceLabels=table.columns.filter(x=>x.hoursByDayBranch[branches.indexOf(dayBranch)]===hourBranch)
  .map(x=>({sourceLabel:x.sourceLabel,sourceType:x.sourceType,sourcePDFPage:x.sourcePDFPage}));
 return {system,dayBranch,hourBranch,sourceLabels,coverageIncomplete:true,
  pendingSourceLabels:['勾陳'],missingLabelIsNotAnUnluckyHour:true,overallRecommendation:null};
}
// Caller must declare this textual status; no day/stem, calendar or time-boundary adapter is implied.
export function sourceJieluActivityScope({system,jieluStatus,activity}){
 systemCheck(system);exact(jieluStatus,[true,false,null],'declared jielu status');
 exact(activity,['travel','marriage','relocation','other','unknown'],'activity');
 const sourceRestrictionApplies=jieluStatus===false?false:
  jieluStatus===null||activity==='unknown'?null:['travel','marriage','relocation'].includes(activity);
 return {system,jieluStatus,activity,sourceRestrictionApplies,
  sourcePDFPage:134,otherFactorsStillUnresolved:true,overallRecommendation:null};
}
