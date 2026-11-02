// Source-coordinate adapters only. The caller confirms year/day stem and branch.
const stems=[...'甲乙丙丁戊己庚辛壬癸'];
function input(context,keys){
 if(!context||typeof context!=='object'||Array.isArray(context)||Object.getOwnPropertySymbols(context).length||
  Object.keys(context).some(k=>!keys.includes(k))||keys.some(k=>typeof context[k]!=='string'||[...context[k]].length!==1))
  throw TypeError('Only explicit single-character anchor stem and branch are supported.');
}
export function monthStemCoordinate(context,...extra){
 if(extra.length)throw TypeError('No calendar/ordinal/strength arguments.');input(context,['yearStem','monthBranch']);
 const branches=[...'寅卯辰巳午未申酉戌亥子丑'],i=stems.indexOf(context.yearStem),offset=branches.indexOf(context.monthBranch);
 if(i<0||offset<0)throw TypeError('Explicit year stem and confirmed month branch.');
 const start=[2,4,6,8,0,2,4,6,8,0][i],stem=stems[(start+offset)%10];
 return{schema:'hhc.B03.year-month-stem-coordinate.v1',sourcePDFPage:24,yearStem:context.yearStem,
  monthBranch:context.monthBranch,monthStem:stem,ganZhi:stem+context.monthBranch,anchorBranch:'寅',anchorStem:stems[start],
  offsetFromSourceAnchor:offset,evidence:offset===0?'direct-source-anchor':'editorial-forward-cycle-expansion',
  lunarMonthOrdinalUsed:false,yearBoundaryConvention:null,solarTermInstant:null,calendarAdapter:false,consumerApplied:false};
}
export function hourStemCoordinate(context,...extra){
 if(extra.length)throw TypeError('No clock/timezone/strength arguments.');input(context,['dayStem','hourBranch']);
 const branches=[...'子丑寅卯辰巳午未申酉戌亥'],i=stems.indexOf(context.dayStem),offset=branches.indexOf(context.hourBranch);
 if(i<0||offset<0)throw TypeError('Explicit day stem and confirmed hour branch.');
 const start=[0,2,4,6,8,0,2,4,6,8][i],stem=stems[(start+offset)%10];
 return{schema:'hhc.B03.day-hour-stem-coordinate.v1',sourcePDFPage:25,dayStem:context.dayStem,
  hourBranch:context.hourBranch,hourStem:stem,ganZhi:stem+context.hourBranch,anchorBranch:'子',anchorStem:stems[start],
  offsetFromSourceAnchor:offset,evidence:offset===0?'direct-source-anchor':'editorial-forward-cycle-expansion',
  civilClockHour:null,dayBoundaryConvention:null,lateZiHourConvention:null,timezone:null,calendarAdapter:false,consumerApplied:false};
}
