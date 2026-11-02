import{readFileSync}from'node:fs';
import{compile}from'../../v53/research/liuyao-foundations/liuyao-reference.mjs';
const source=JSON.parse(readFileSync(new URL('TRAVELER_CONTEXT.json',import.meta.url),'utf8'));
export function explicitTravelerContext(values,context){
 const keys=['system','subject','question'];
 if(!context||Object.getPrototypeOf(context)!==Object.prototype||Object.getOwnPropertySymbols(context).length||Object.keys(context).length!==3||keys.some(k=>!Object.hasOwn(context,k)))throw TypeError('Explicit named system,subject andquestion ornull required');
 if(context.system!==source.system||context.subject!==null&&!source.subjects.some(x=>x.id===context.subject)||context.question!==null&&!source.questionLabels.includes(context.question))throw TypeError('Only named source subjects/questions are extracted,no automatic person or intent inference');
 const chart=compile(values),subject=source.subjects.find(x=>x.id===context.subject),complete=context.subject!==null&&context.question!==null;
 const projection=!complete?null:subject.kin?{kin:subject.kin,originalLines:chart.lines.filter(x=>x.kin===subject.kin).map(x=>x.line),changedLines:chart.lines.filter(x=>x.changed?.kin===subject.kin).map(x=>x.line),hiddenRoleAutomaticallySelected:false}:
  {structuralRole:'應',line:chart.primary.ying,physicalResponseBranch:chart.lines.find(x=>x.line===chart.primary.ying).branch,notAnIdentifiedRealPerson:true};
 return{system:source.system,subject:context.subject,question:context.question,sourcePages:[...source.sourcePages],chart,
  questionScopeComplete:complete,candidateRoleProjection:projection,sourceStructuralVocabulary:structuredClone(source.structuralVocabulary),
  sourceQuestionWasNotSilentlyChanged:true,biologicalIdentityInferred:false,useLineSelected:null,effectiveActivity:null,strength:null,
  structuralAffliction:null,actualPersonIllness:null,healthResult:null,lifespan:null,actualTravelSafety:null,
  returnDate:null,currentLocation:null,chronologicalDateAdapter:null,practicalOutcome:null,consumerApplied:false};
}
