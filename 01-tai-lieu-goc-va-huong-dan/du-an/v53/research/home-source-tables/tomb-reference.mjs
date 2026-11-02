// Private named-source reference: traditional coordinates must be supplied explicitly.
const stems='甲乙丙丁戊己庚辛壬癸',branches='子丑寅卯辰巳午未申酉戌亥';
const groups=[
 {id:'water-earth',mountains:'甲寅辰巽戌坎辛申丑癸坤庚未',tomb:'辰',elements:['木','金','水','火','土'],pages:[42,43]},
 {id:'fire',mountains:'離壬丙乙',tomb:'戌',elements:['火','土','木','金','水'],pages:[43,44]},
 {id:'wood',mountains:'震艮巳',tomb:'未',elements:['土','木','金','水','火'],pages:[44]},
 {id:'metal',mountains:'乾亥兌丁',tomb:'丑',elements:['金','水','火','土','木'],pages:[44,45]}
];
const periods=[null,'before-current-winter-solstice','after-current-winter-solstice-in-source-chou-period'];
const controller={'木':'金','金':'火','水':'土','火':'水','土':'木'};
const uses={'new-dwelling':true,'new-grave':true,'repair-foundation-unchanged':false,'burial-existing-grave':false};
function coordinate(x,kind,alphabet){if(x!==null&&(typeof x!=='string'||[...x].length!==1||!alphabet.includes(x)))throw new TypeError('Explicit '+kind+' or null required');}
function at(g,index){const branchIndex=branches.indexOf(g.tomb);return{pillar:stems[(2*index+branchIndex)%10]+g.tomb,movementElement:g.elements[index],sourceAvoidElement:controller[g.elements[index]]};}
export function tombMovement({system,mountain,sourceYearStem,sourcePeriod}={}){
 if(system!=='xieji-tomb-movement')throw new TypeError('Explicit named source system required');
 coordinate(mountain,'mountain',groups.map(x=>x.mountains).join(''));coordinate(sourceYearStem,'source year stem',stems);
 if(!periods.includes(sourcePeriod))throw new TypeError('Explicit source period or null required');
 const base={system,mountain,sourceYearStem,sourcePeriod,pillar:null,movementElement:null,sourceAvoidElement:null,calendarAdapter:null,practicalOutcome:null};
 if(mountain===null||sourceYearStem===null)return base;
 const g=groups.find(x=>x.mountains.includes(mountain)),index=stems.indexOf(sourceYearStem)%5;
 if(g.tomb==='丑'&&sourcePeriod===null)return{...base,sourceGroup:g.id,sourceAlternatives:[at(g,index),at(g,(index+1)%5)]};
 const i=(index+(g.tomb==='丑'&&sourcePeriod===periods[2]?1:0))%5;
 return{...base,...at(g,i),sourceGroup:g.id,sourcePages:g.pages};
}
export function sourceOvercoming({system,mountain,sourceYearStem,sourcePeriod,candidateNaYinElement,constructionContext,coordinateKind}={}){
 if(!['year','month','day','hour'].includes(coordinateKind))throw new TypeError('Explicit candidate coordinate kind required');
 coordinate(candidateNaYinElement,'candidate NaYin element','木火土金水');
 if(constructionContext!==null&&!Object.hasOwn(uses,constructionContext))throw new TypeError('Explicit source construction context or null required');
 const movement=tombMovement({system,mountain,sourceYearStem,sourcePeriod}),relation=candidateNaYinElement===null||movement.movementElement===null?null:movement.sourceAvoidElement===candidateNaYinElement,
 applicable=constructionContext===null?null:uses[constructionContext];
 return{movement,candidateNaYinElement,coordinateKind,constructionContext,sourceContextApplicable:applicable,elementOvercomesMovement:relation,
  sourceRuleApplies:applicable===false?false:applicable===null?null:relation,calendarAdapter:null,practicalOutcome:null};
}
