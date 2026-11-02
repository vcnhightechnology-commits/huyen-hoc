// Private B02 chapter34 coordinate tool. Symbolic roles require an explicit question.
import {compile} from '../liuyao-foundations/liuyao-reference.mjs';
const roles=Object.freeze({marriage:'媒妁',litigation:'中證',trade:'牙行',loan:'中保',boat_travel:'附載',childbirth:'收生保母',social_exchange:'幫間'});
const known=[...Object.keys(roles),'weather','self','other'];
export function interposedContext(values,context){
 if(arguments.length!==2||!context||typeof context!=='object'||Array.isArray(context)||Object.getOwnPropertySymbols(context).length||
  Object.keys(context).some(k=>!['sourceContext','question','bilateralContext'].includes(k))||context.sourceContext!=='B02-ch034'||!known.includes(context.question)||
  ![undefined,null,true,false].includes(context.bilateralContext))
  throw TypeError('Explicit B02-ch034 sourceContext and supported question required');
 const chart=compile(values),lo=Math.min(chart.primary.shi,chart.primary.ying),hi=Math.max(chart.primary.shi,chart.primary.ying);
 const lines=chart.lines.filter(l=>lo<l.line&&l.line<hi).map(l=>({line:l.line,branch:l.branch,kin:l.kin,moving:l.moving}));
 if(lines.length!==2)throw Error('Expected two interposed coordinates');
 const candidateRole=Object.hasOwn(roles,context.question)?roles[context.question]:null;
 const bilateral=context.bilateralContext??null;
 const applicable=candidateRole===null?false:bilateral;
 const role=applicable===true?candidateRole:null;
 return {sourceContext:'B02-ch034',question:context.question,shi:chart.primary.shi,ying:chart.primary.ying,
  interposedLines:lines,candidateSymbolicRole:candidateRole,symbolicRole:role,roleApplicable:applicable,bilateralContext:bilateral,
  visibleMovingInterposedLines:lines.filter(l=>l.moving).map(l=>l.line),
  roleScope:'source-symbolism-not-real-person-identification',
  automaticQuestionInference:false,darkMotionDerived:false,obstructionEstablished:null,
  predictedOutcome:null,consumerApplied:false,completeStrengthAndUseGodRules:false};
}
