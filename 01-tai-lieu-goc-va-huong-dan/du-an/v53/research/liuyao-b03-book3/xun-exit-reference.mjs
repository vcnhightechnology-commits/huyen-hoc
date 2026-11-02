// Raw sexagenary coordinates for the identified source paragraph; no functional void or event verdict.
import {compile} from '../liuyao-foundations/liuyao-reference.mjs';
import {dayCoordinates} from '../liuyao-void-motion/void-motion-reference.mjs';
const stems=[...'甲乙丙丁戊己庚辛壬癸'], branches=[...'子丑寅卯辰巳午未申酉戌亥'];
const allowed=['sourceContext','useLine','dayGanZhi'];
const ganZhi=i=>stems[((i%60)+60)%60%10]+branches[((i%60)+60)%60%12];
export function xunExitCoordinates(values,context,...extra){
 if(extra.length||!context||typeof context!=='object'||Array.isArray(context)||
  Object.getOwnPropertySymbols(context).length||Object.keys(context).some(k=>!allowed.includes(k)))
  throw TypeError('Only explicit sourceContext/useLine/dayGanZhi supported.');
 if(context.sourceContext!=='weather-timing-paragraph')throw TypeError('The source paragraph domain must be explicit.');
 if(!Number.isInteger(context.useLine)||context.useLine<1||context.useLine>6)throw TypeError('Explicit selected useLine1..6 required.');
 const chart=compile(values),use=chart.lines[context.useLine-1];
 const day=context.dayGanZhi===undefined||context.dayGanZhi===null?null:dayCoordinates(context.dayGanZhi);
 const rawVoid=day?day.voidBranches.includes(use.branch):null;
 const offset=rawVoid?10-day.daysInXunIndex0:null;
 const next=offset===null?null:dayCoordinates(ganZhi(day.cycleIndex0+offset));
 return {schema:'hhc.liuyao.B03.raw-xun-exit.v1',sourceID:'B03-book3',sourcePDFPage:8,
  sourceClause:'如旬空候出旬之日應事',sourceContext:context.sourceContext,
  explicitContext:structuredClone(context),chart,useLine:context.useLine,subjectBranch:use.branch,
  subjectMotion:use.moving?'moving':'static',subjectLayer:'primary-selected-line',
  day,rawVoid,premiseStatus:rawVoid===null?'unknown-day-coordinate':rawVoid?'raw-xun-coordinate-present':'not-in-raw-void',
  currentXunWindow:offset===null?null:{startOffset0:0,endOffset0:offset-1,includesSuppliedDay:true},
  firstOutsideCurrentXun:next?{offsetDays:offset,dayGanZhi:next.dayGanZhi,xunHead:next.xunHead,
   voidBranches:next.voidBranches,subjectStillRawVoid:next.voidBranches.includes(use.branch)}:null,
  exitIsNextXunBoundaryNotFunctionalVerdict:true,motionDoesNotOverrideThisRawCoordinate:true,
  changedBranchSubstituted:false,calendarInstantAdapter:null,gregorianDate:null,
  functionalVoid:null,allSourceExceptionsChecked:false,predictedEvent:null,
  meteorologicalForecast:null,consumerApplied:false};
}
