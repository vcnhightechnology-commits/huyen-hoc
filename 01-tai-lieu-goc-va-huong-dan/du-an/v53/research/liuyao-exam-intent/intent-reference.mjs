// Private projection of explicit source questions. This does not select a use-line,
// infer intent/occupation, measure strength, or predict practical outcomes.
import{readFileSync}from'node:fs';
import{compile}from'../liuyao-foundations/liuyao-reference.mjs';
const data=JSON.parse(readFileSync(new URL('SOURCE_CONTEXTS.json',import.meta.url),'utf8'));
const fields=['system','subject','question','intent','rank'];
export function sourceIntentProjection(values,context){
 if(!context||Object.getPrototypeOf(context)!==Object.prototype||Object.getOwnPropertySymbols(context).length||Object.keys(context).length!==fields.length||fields.some(k=>!Object.hasOwn(context,k))||Object.keys(context).some(k=>!fields.includes(k)))throw TypeError('Declare named source system, subject, question, intent and rank;use null for unknown');
 const method=data.methods.find(x=>x.id===context.system);if(!method)throw TypeError('Named extracted source context required');
 for(const k of['subject','question','intent'])if(context[k]!==null&&!method[k==='subject'?'subjects':k==='question'?'questions':'intents'].includes(context[k]))throw TypeError('Unrecognized explicit '+k);
 if(context.rank!==null&&(!method.requiresNamedRank||!data.namedRankQueries.includes(context.rank)))throw TypeError('Only an explicit source rank question is supported in its named context');
 if(context.subject!==null&&context.intent!==null&&method.allowedSubjectIntentPairs&&!method.allowedSubjectIntentPairs.some(([s,i])=>s===context.subject&&i===context.intent))throw TypeError('Source subject and intent combination is not extracted');
 const missing=['subject','question','intent'].filter(k=>context[k]===null);if(method.requiresNamedRank&&context.rank===null)missing.push('rank');
 const complete=missing.length===0,chart=compile(values),roles=method.rolesByIntent?method.rolesByIntent[context.intent]:method.roles;
 const established=complete&&Array.isArray(roles)&&roles.length>0;
 const candidates=established?roles.map(x=>({...structuredClone(x),originalLines:chart.lines.filter(y=>y.kin===x.kin).map(y=>y.line),changedLines:chart.lines.filter(y=>y.changed?.kin===x.kin).map(y=>y.line)})):null;
 return{system:method.id,subject:context.subject,question:context.question,intent:context.intent,rank:context.rank,
  sourcePages:[...method.pages],sourceVoice:method.sourceVoice,questionScope:{complete,missing},chart,
  candidateRoleGroups:candidates,sourceSubcontextRolesExtracted:established,
  unknownReason:!complete?'explicit-scope-incomplete':!established?'listed-source-intent-not-yet-encoded':null,
  sourceNamedRankQuestion:complete&&method.requiresNamedRank?context.rank:null,
  sourceGeographyAdapter:null,sourceBodySymbolEqualsSelf:null,sourceStrength:null,effectiveActivity:null,
  useLineSelected:null,practicalOutcome:null,examResult:null,officeResult:null,actualRank:null,
  financialResult:null,healthResult:null,lifespan:null,legalResult:null,engineeringSafety:null,chronologicalDateAdapter:null,
  symbolicKinIsBiologicalIdentity:false,automaticIntentInference:false,occupationInferred:false,consumerApplied:false};
}
