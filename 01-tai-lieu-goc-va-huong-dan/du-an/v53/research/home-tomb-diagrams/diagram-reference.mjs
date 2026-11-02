// Private direct diagram-coordinate queries. Gregorian date, field compass and
// practical construction outcome adapters are deliberately not inferred.
import{readFileSync}from'node:fs';
const table=JSON.parse(readFileSync(new URL('DIAGRAM_TABLES.json',import.meta.url),'utf8')),stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'];
const pillars=Array.from({length:60},(_,i)=>stems[i%10]+branches[i%12]),periods=[null,'before-current-winter-solstice','after-current-winter-solstice-in-source-chou-period'];
function rowFor(system,mountain,sourceYearStem,period){
 if(system!=='xieji41-49-ordinary-diagram')throw TypeError('Explicit named diagram system required');
 if(mountain!==null&&!table.groups.some(g=>g.mountains.includes(mountain)))throw TypeError('Explicit source mountain label or null required');
 if(sourceYearStem!==null&&!stems.includes(sourceYearStem))throw TypeError('Explicit single source year stem or null required');
 if(!periods.includes(period))throw TypeError('Explicit source period or null required');
 const group=table.groups.find(g=>g.mountains.includes(mountain)),row=group&&sourceYearStem?table.rows.find(x=>x.mountainGroup===group.id&&x.sourceYearStems.includes(sourceYearStem)):null;
 const applicable=group?group.id==='metal'?period===null?null:period===periods[1]:true:null;
 return{group,row,applicable};
}
export function diagramYear({system,mountain,sourceYearPillar,sourcePeriod}={}){
 if(sourceYearPillar!==null&&!pillars.includes(sourceYearPillar))throw TypeError('Explicit valid sexagenary source year pillar or null required');
 const {group,row,applicable}=rowFor(system,mountain,sourceYearPillar?.[0]??null,sourcePeriod),listed=row?row.sourceYearPillars49.includes(sourceYearPillar):null;
 return{system,mountain,sourceYearPillar,sourcePeriod,mountainGroup:group?.id??null,diagramMovementElement:row?.sourceMovementElement41??null,
  listedInOrdinaryDiagram:listed,ordinaryDiagramPeriodApplicable:applicable,sourceConditionMatch:applicable===true?listed:null,
  fullSourceMethodEstablished:false,calendarAdapter:null,practicalOutcome:null};
}
export function diagramMonth({system,mountain,sourceYearStem,sourcePeriod,candidateMonthOrdinal}={}){
 if(candidateMonthOrdinal!==null&&(!Number.isInteger(candidateMonthOrdinal)||candidateMonthOrdinal<1||candidateMonthOrdinal>12))throw TypeError('Explicit source month ordinal1..12 or null required');
 const {group,row,applicable}=rowFor(system,mountain,sourceYearStem,sourcePeriod),alternatives=row?row.monthReadingResolved?[row.sourceMonthOrdinals49]:row.monthReadingAlternatives:[];
 const outcomes=candidateMonthOrdinal===null?[]:alternatives.map(x=>x.includes(candidateMonthOrdinal));
 const match=outcomes.length&&outcomes.every(x=>x===outcomes[0])?outcomes[0]:null;
 return{system,mountain,sourceYearStem,sourcePeriod,candidateMonthOrdinal,mountainGroup:group?.id??null,
  sourceMonthSetResolved:row?row.monthReadingResolved:null,sourceMonthAlternatives:structuredClone(alternatives),
  listedAcrossReadingAlternatives:match,ordinaryDiagramPeriodApplicable:applicable,sourceConditionMatch:applicable===true?match:null,
  sourceMonthReadingCaveat:row?.monthReadingCaveat??null,dateBound:false,calendarAdapter:null,practicalOutcome:null};
}
