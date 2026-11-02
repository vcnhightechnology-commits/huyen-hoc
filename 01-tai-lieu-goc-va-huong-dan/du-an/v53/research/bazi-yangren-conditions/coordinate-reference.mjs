import {readFileSync}from'node:fs';
const source=JSON.parse(readFileSync(new URL('SOURCE_COORDINATES.json',import.meta.url),'utf8'));
const stems='甲乙丙丁戊己庚辛壬癸',branches='子丑寅卯辰巳午未申酉戌亥';
const valid=x=>typeof x==='string'&&[...x].length===2&&stems.includes(x[0])&&branches.includes(x[1])&&stems.indexOf(x[0])%2===branches.indexOf(x[1])%2;
export function sourceBladeCoordinates(c){
 const keys=['system','candidateDay','candidateHour'];
 if(!c||Object.getPrototypeOf(c)!==Object.prototype||Object.keys(c).length!==3||Object.getOwnPropertySymbols(c).length||keys.some(k=>!Object.hasOwn(c,k))||Object.keys(c).some(k=>!keys.includes(k)))throw TypeError('Explicit named system/day/hour required;null means unknown');
 for(const k of['candidateDay','candidateHour'])if(c[k]!==null&&!valid(c[k]))throw TypeError('Source coordinate must be a valid canonical sixty-cycle pillar or null');
 const table=source.tables.find(x=>x.system===c.system),negative=c.system===source.negativeDayHourSystem;
 if(!table&&!negative)throw TypeError('Named extracted source-coordinate system required');
 if(table&&c.candidateHour!==null)throw TypeError('Day-set context has no hour coordinate');
 const known=c.candidateDay!==null&&(!negative||c.candidateHour!==null);
 const matches=!known?null:negative?source.negativeDayHourPairs.some(x=>x.day===c.candidateDay&&x.hour===c.candidateHour):table.days.includes(c.candidateDay);
 return{system:c.system,candidateDay:c.candidateDay,candidateHour:c.candidateHour,coordinatesKnown:known,listedCoordinateMatches:matches,
  matchedSourceRows:!known?null:negative?structuredClone(source.negativeDayHourPairs.filter(x=>x.day===c.candidateDay&&x.hour===c.candidateHour)):matches?[{sourceLabel:table.sourceLabel,day:c.candidateDay,sourcePages:[...table.sourcePages]}]:[],
  sourceLocalNegativeExampleMatches:negative?matches:null,fullSourceConditionsEvaluated:false,
  fullBladePatternEstablished:null,effectiveControlOrCombination:null,strength:null,practicalOutcome:null,sourceOutcomesValidated:false,consumerApplied:false};
}
