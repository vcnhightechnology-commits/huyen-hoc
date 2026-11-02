import {readFileSync}from 'node:fs';
const table=JSON.parse(readFileSync(new URL('./MANUAL_SEAT_CLAUSE.json',import.meta.url),'utf8'));
export const FOOD_SEAT_SYSTEM='TMTH005-C20-food-seat-coordinates';
const stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'];
export function sourceFoodSeat(input){
 const keys=['system','anchorBasis','dayStem','targetPillar'];
 if(!input||Object.getPrototypeOf(input)!==Object.prototype||Reflect.ownKeys(input).length!==keys.length||keys.some(k=>!Object.hasOwn(input,k)||!Object.getOwnPropertyDescriptor(input,k).enumerable||!Object.hasOwn(Object.getOwnPropertyDescriptor(input,k),'value')))throw TypeError('Four exact plain explicit fields required');
 const {system,anchorBasis,dayStem,targetPillar}=input;
 if(system!==FOOD_SEAT_SYSTEM||!['day-stem','birth-year-stem','unknown'].includes(anchorBasis)||!(dayStem===null||stems.includes(dayStem)))throw TypeError('Named source, declared anchor and canonical day stem/null required');
 if(targetPillar!==null&&(typeof targetPillar!=='string'||[...targetPillar].length!==2||!stems.includes(targetPillar[0])||!branches.includes(targetPillar[1])||stems.indexOf(targetPillar[0])%2!==branches.indexOf(targetPillar[1])%2))throw TypeError('Canonical possible stem-branch pillar/null required');
 const row=dayStem===null?null:table.records.find(x=>x.dayStems.includes(dayStem));
 const known=anchorBasis==='day-stem'&&row!==null&&targetPillar!==null;
 const expectedFoodStem=row?row.foodStems[row.dayStems.indexOf(dayStem)]:null;
 const fixedFoodRelation=known?targetPillar[0]===expectedFoodStem:null;
 const selectedSeatMembership=known?fixedFoodRelation&&row.branches.includes(targetPillar[1]):null;
 return {system,anchorBasis,dayStem,targetPillar,fixedFoodRelation,selectedSeatMembership,
  sourcePhrase:'食神見生旺',sourceContextID:'FOOD-00-C20',sourceContainerPages:[177,178],
  selectedGroup:anchorBasis==='day-stem'&&row?structuredClone(row):null,
  falseDoesNotMeanWeakOrUnlucky:true,hiddenStemsIncluded:false,fullStrength:null,foodPatternEstablished:null,
  fullSourceClauseConditionsApplied:false,calendarBirthChartValidated:false,practicalOutcome:null,consumerApplied:false};
}
