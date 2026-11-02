// Literal B02 chapter33 coordinates only. A conflicting source reading remains ambiguous.
import{readFileSync}from'node:fs';
const data=JSON.parse(readFileSync(new URL('STAR_COORDINATES.json',import.meta.url),'utf8'));
export function sourceStarCoordinates(context,...extra){
 const keys=['dayStem','dayBranch','season'];
 if(extra.length||!context||typeof context!=='object'||Array.isArray(context)||!Object.keys(context).length||
  Object.getOwnPropertySymbols(context).length||Object.keys(context).some(k=>!keys.includes(k)))throw TypeError('Explicit source day-stem/day-branch/season coordinates only.');
 for(const[k,domain]of[['dayStem','甲乙丙丁戊己庚辛壬癸'],['dayBranch','子丑寅卯辰巳午未申酉戌亥'],['season','春夏秋冬']])
  if(context[k]!==undefined&&context[k]!==null&&(typeof context[k]!=='string'||[...context[k]].length!==1||!domain.includes(context[k])))throw TypeError('Invalid explicit source coordinate.');
 const s=context.dayStem,b=context.dayBranch,season=context.season;
 let nobleman=null,salary=null,horse=null,joy=null;
 if(s){const branches=data.nobleman.verseRows[s];
  nobleman=s==='庚'?{status:'within-page-conflict',branches:null,alternatives:[{layer:'verse',branches:branches.slice()},
   {layer:'worked-example',branches:data.nobleman.proseExampleGeng.slice()}],effectiveChoice:null}:
   {status:'single-reading-in-retained-source-fields',branches:branches.slice(),effectiveChoice:null};
  salary=Object.hasOwn(data.salary.explicitRows,s)?{status:'explicit-printed-stem',branch:data.salary.explicitRows[s]}:
   {status:'not-explicit-in-retained-six-stem-lines',branch:null};
 }
 if(b){const row=data.horse.groups.find(r=>r.dayBranches.includes(b));horse={branch:row.target,sourceGroup:row.dayBranches.slice()};}
 if(season)joy={branch:data.joy.explicitSeasonRows[season],season};
 return{sourceID:'B02-ch033',sourcePDFPages:[136,137],dayStem:s??null,dayBranch:b??null,season:season??null,
  nobleman,salary,horse,joy,calendarAdapter:false,missingSalaryStemsNotFilled:true,
  effectiveStrength:null,positiveScore:null,predictedEvent:null,consumerApplied:false};
}
