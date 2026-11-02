import{readFileSync}from'node:fs';
const data=JSON.parse(readFileSync(new URL('SOURCE_TABLES.json',import.meta.url),'utf8'));
const stems='甲乙丙丁戊己庚辛壬癸',branches='子丑寅卯辰巳午未申酉戌亥';
const sixty=Array.from({length:60},(_,i)=>stems[i%10]+branches[i%12]);
export function sourceYearVoid(context){
 const keys=['system','scope','sourceYearPillar','candidateBranch','orthographyPolicy'];
 if(!context||Object.getPrototypeOf(context)!==Object.prototype||Object.getOwnPropertySymbols(context).length||Object.keys(context).length!==5||keys.some(k=>!Object.hasOwn(context,k))||Object.keys(context).some(k=>!keys.includes(k)))throw TypeError('Declare source system, birth-year scope, source pillar/branch or null, and orthography policy');
 const method=data.systems.find(x=>x.system===context.system);if(!method||context.scope!=='birth-year')throw TypeError('Named birth-year method required;day/month substitutions are not supported');
 if(context.sourceYearPillar!==null&&!sixty.includes(context.sourceYearPillar))throw TypeError('Canonical sourceyear sixty-cycle pillar or null required');
 if(context.candidateBranch!==null&&!(typeof context.candidateBranch==='string'&&[...context.candidateBranch].length===1&&branches.includes(context.candidateBranch)))throw TypeError('Canonical branch or null required;no silent aliases');
 if(!['contextual-branch','leave-unresolved'].includes(context.orthographyPolicy))throw TypeError('Explicit Si orthography policy required');
 const year=context.sourceYearPillar,cycleHead=year===null?null:sixty[Math.floor(sixty.indexOf(year)/10)*10];
 const row=year===null?null:method.key==='birth-year-stem-group'?method.rows.find(x=>x.sourceStemGroup.includes(year[0])):method.rows.find(x=>x.sourceCycleHead===cycleHead);
 const selected=row?row.canonicalWorkingBranches.map(b=>row.contextualSiNormalization&&b==='巳'&&context.orthographyPolicy==='leave-unresolved'?null:b):null;
 const member=selected===null||context.candidateBranch===null?null:selected.includes(context.candidateBranch)?true:selected.includes(null)?null:false;
 return{system:method.system,scope:'birth-year',sourceYearPillar:year,sourceYearCoordinateKnown:row?true:null,
  sourceGroup:row?(row.sourceStemGroup??row.sourceCycleHead):null,sourcePhrase:row?.sourcePhrase??null,
  canonicalWorkingBranches:row?[...row.canonicalWorkingBranches]:null,selectedBranches:selected,candidateBranch:context.candidateBranch,branchMembership:member,
  orthographyPolicy:context.orthographyPolicy,contextualSiNormalization:row?.contextualSiNormalization??null,
  sourceYearBoundaryAdapter:null,singleSoftwareStarSelected:null,softwareRepresentationInferred:false,
  practicalOutcome:null,starStrength:null,healthResult:null,lifespan:null,consumerApplied:false};
}
