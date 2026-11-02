// B03 identified named-jie coordinate bridge, no solar-date converter or finalvoidforecast.
import{readFileSync}from'node:fs';import{annotate}from'../liuyao-void-motion/void-motion-reference.mjs';
const data=JSON.parse(readFileSync(new URL('JIE_MONTH_ROWS.json',import.meta.url),'utf8'));
const fire=JSON.parse(readFileSync(new URL('FIRE_PHASE_EXAMPLE.json',import.meta.url),'utf8')),branches=[...'子丑寅卯辰巳午未申酉戌亥'];
export function firePhaseAtBranch(atBranch){
 if(!branches.includes(atBranch))throw TypeError('explicitsinglebranchrequired');
 const offset=(branches.indexOf(atBranch)-branches.indexOf(fire.explicitFireExample.birthBranch)+12)%12;
 return{element:'火',atBranch,phase:fire.printedPhaseOrder[offset],sourceID:'B03',sourcePDFPages:[22,23],framework:fire.framework,
  coordinateEvidence:offset<=2?'explicit-fire-example':'derived-from-printed-order-and-forward-rule',
  functionalEffect:null,overallStrength:null,consumerApplied:false};
}
export function monthForConfirmedJie(jieName){
 const r=data.rows.find(r=>r.jieAsPrinted===jieName||r.runtimeSimplifiedAlias===jieName);
 if(!r)throw TypeError('one explicit named12jie in the identifiedB03table required');
 return{...structuredClone(r),sourceID:'B03',sourcePDFPage:33,inputMeaning:'most-recent-confirmed-jie-not-next-term',
  calendarBoundaryInstant:null,gregorianTimezone:null,sourceMonthOrdinalIsLunarMonthNumber:false,computedUsability:null,consumerApplied:false};
}
export function annotateWithConfirmedJie(values,context){
 if(!context||typeof context!=='object'||Array.isArray(context)||Object.getOwnPropertySymbols(context).length||Object.keys(context).some(k=>!['jieName','dayGanZhi','strengthBeforeDayByLine'].includes(k)))throw TypeError('explicitconfirmedjieandoptionalday/strengthonly');
 const month=monthForConfirmedJie(context.jieName),inner={monthBranch:month.monthBranch};
 for(const k of['dayGanZhi','strengthBeforeDayByLine'])if(context[k]!==undefined)inner[k]=context[k];
 const a=annotate(values,inner);
 return{...a,schema:'hhc.liuyao.b03-named-jie-context.v1',explicitNamedJie:month,
  sourceFramework:'B03namedjiecoordinatebridge+B02identifiedstructuralreference;notclaimedallrulesidentical',
  sourceDateInputConvention:'callerconfirmsmostrecentnamedjie;thismoduledoesnotacceptordeduceaGregoriandate',
  rawMonthBreakLines:a.lines.filter(l=>l.rawMonthClash).map(l=>l.line)};
}
