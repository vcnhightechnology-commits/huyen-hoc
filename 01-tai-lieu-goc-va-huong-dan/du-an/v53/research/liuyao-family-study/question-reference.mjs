// Private source-question projection. Symbolic roles are candidates, never
// biological identities, automatically chosen use-lines or practical forecasts.
import {readFileSync} from 'node:fs';
import {compile} from '../liuyao-foundations/liuyao-reference.mjs';

const source=JSON.parse(readFileSync(new URL('SOURCE_CONTEXTS.json',import.meta.url),'utf8'));
const fields=['system','subject','question','classic','examStage'];

export function sourceQuestionProjection(values,context){
 if(!context||Object.getPrototypeOf(context)!==Object.prototype||Object.getOwnPropertySymbols(context).length||
    Object.keys(context).length!==fields.length||fields.some(k=>!Object.hasOwn(context,k))||Object.keys(context).some(k=>!fields.includes(k)))
  throw TypeError('Declare source system, subject, question, classic and examStage explicitly; use null for unknown');
 const method=source.methods.find(x=>x.id===context.system);
 if(!method)throw TypeError('Named extracted source context required');
 for(const [k,options]of[['subject',method.subjects],['question',method.questions]])
  if(context[k]!==null&&!options.includes(context[k]))throw TypeError('Unrecognized explicit '+k);
 const classicMethod=method.id==='b02-ch046-classic',examMethod=method.id==='b02-ch048-exam-stage';
 if(context.classic!==null&&(!classicMethod||!source.classics.some(x=>x.name===context.classic)))throw TypeError('Only an explicitly named source classic is supported');
 if(context.examStage!==null&&(!examMethod||!source.historicalExamStages.includes(context.examStage)))throw TypeError('Explicit historical stage required in its named context');
 const missing=[];
 if(context.subject===null)missing.push('subject');
 if(context.question===null)missing.push('question');
 if(classicMethod&&context.classic===null)missing.push('classic');
 if(examMethod&&context.examStage===null)missing.push('examStage');
 const chart=compile(values),scopeComplete=missing.length===0;
 const roleExtracted=method.roles.length>0&&!method.unextractedSubjects?.includes(context.subject);
 const groups=scopeComplete&&roleExtracted?method.roles.map(role=>({...structuredClone(role),
  originalLines:chart.lines.filter(x=>x.kin===role.kin).map(x=>x.line),
  changedLines:chart.lines.filter(x=>x.changed?.kin===role.kin).map(x=>x.line)})):null;
 return{system:method.id,subject:context.subject,question:context.question,sourcePages:[...method.pages],sourceVoice:method.sourceVoice,
  questionScope:{complete:scopeComplete,missing,oneSubjectOneQuestion:true},chart,
  candidateRoleGroups:groups,sourceRoleExtractionEstablished:roleExtracted,
  unknownReason:!scopeComplete?'explicit-question-scope-incomplete':!roleExtracted?'role-not-extracted-for-this-source-context':null,
  classicSourceCoordinate:scopeComplete&&classicMethod?structuredClone(source.classics.find(x=>x.name===context.classic)):null,
  historicalExamStage:scopeComplete&&examMethod?context.examStage:null,
  symbolicKinIsBiologicalIdentity:false,automaticQuestionInference:false,useLineSelected:null,strength:null,effectiveActivity:null,
  practicalOutcome:null,lifespan:null,healthResult:null,fertilityResult:null,marriageResult:null,examResult:null,
  chronologicalDateAdapter:null,sourceOutcomesValidated:false,consumerApplied:false};
}
