// Private source-coordinate matcher. No inference of strength, success or useful god.
import{readFileSync}from'node:fs';
const rows=JSON.parse(readFileSync(new URL('SOURCE_ROWS.json',import.meta.url),'utf8')).rows;
const stems='甲乙丙丁戊己庚辛壬癸',branches='子丑寅卯辰巳午未申酉戌亥';
export function inspectJianluCoordinates(context){
 if(arguments.length!==1||!context||typeof context!=='object'||Array.isArray(context)||Object.getOwnPropertySymbols(context).length||
  Object.keys(context).some(k=>!['sourceContext','dayStem','monthBranch','hourPillar'].includes(k))||context.sourceContext!=='WYG-005-jianlu'||
  typeof context.dayStem!=='string'||[...context.dayStem].length!==1||!stems.includes(context.dayStem))throw TypeError('Explicit sourceContext andsingle daystem required');
 const month=context.monthBranch??null,hour=context.hourPillar??null;
 if(month!==null&&(typeof month!=='string'||[...month].length!==1||!branches.includes(month)))throw TypeError('Explicitmonthbranch ornull');
 if(hour!==null&&(typeof hour!=='string'||[...hour].length!==2||!stems.includes([...hour][0])||!branches.includes([...hour][1])))throw TypeError('Explicit two-character hourpillar ornull');
 const row=rows.find(r=>r.dayStem===context.dayStem),expectedHour=hour===null?null:stems[(2*(stems.indexOf(context.dayStem)%5)+branches.indexOf([...hour][1]))%10]+[...hour][1];
 const monthMatch=month===null?null:month===row.monthBranch,hourMatch=hour===null?null:hour===row.printedHourPillar;
 return{sourceContext:'WYG-005-jianlu',sourceCoordinate:structuredClone(row),assertedInput:{dayStem:context.dayStem,monthBranch:month,hourPillar:hour},
  monthCoordinateMatched:monthMatch,hourCoordinateMatched:hourMatch,expectedHourAtAssertedBranch:expectedHour,
  hourDayCompatible:hour===null?null:hour===expectedHour,
  completeTripleMatched:monthMatch===false||hourMatch===false?false:monthMatch===true&&hourMatch===true?true:null,
  patternEstablished:null,strengthEstablished:null,favorableOutcome:null,usefulGodSelected:null,
  sourceTerm:'建禄',source宜IsNotUnconditionalOutcome:true,consumerApplied:false,modernCalendarBoundarySelected:false};
}
