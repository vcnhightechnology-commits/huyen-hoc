// Private named-voice role candidates. This is not a weather forecast API.
import{readFileSync}from'node:fs';import{compile}from'../liuyao-foundations/liuyao-reference.mjs';
const methods=JSON.parse(readFileSync(new URL('QUESTION_ROLES.json',import.meta.url),'utf8')).methods;
export function weatherRoleCandidates(values,context){
 if(!context||typeof context!=='object'||Array.isArray(context)||Object.getOwnPropertySymbols(context).length||Object.keys(context).some(k=>!['system','question'].includes(k)))throw TypeError('Only explicit source system and question category supported');
 const method=methods.find(x=>x.id===context.system);if(!method)throw TypeError('Explicit named source voice required');
 if(context.question!==null&&!['rain','clear','cloud-thunder'].includes(context.question))throw TypeError('Explicit supported question category or null required');
 const selector=method.selectors.find(x=>x.question===context.question),chart=compile(values),roles=selector?.desiredKin??null;
 const originals=roles?chart.lines.filter(x=>roles.includes(x.kin)):null;
 const changed=roles?chart.lines.filter(x=>x.changed&&roles.includes(x.changed.kin)).map(x=>({line:x.line,...x.changed})):null;
 return{system:method.id,sourceVoice:method.sourceVoice,question:context.question,sourceRoleEstablished:context.question===null?null:!!selector,
  desiredKin:roles?[...roles]:null,chart,originalCandidates:originals,changedCandidates:changed,
  movingOriginalCandidateLines:originals?.filter(x=>x.moving).map(x=>x.line)??null,
  useLineSelected:null,availabilityEstablished:null,effectiveActivity:null,dayOrMonthPremisesApplied:false,
  geographicContext:null,predictedWeather:null,sourceOutcomesValidated:false,consumerApplied:false};
}
