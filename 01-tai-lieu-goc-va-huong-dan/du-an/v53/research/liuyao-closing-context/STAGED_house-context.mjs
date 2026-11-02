import{readFileSync}from'node:fs';
import{compile}from'../../v53/research/liuyao-foundations/liuyao-reference.mjs';
const data=JSON.parse(readFileSync(new URL('HOUSE_CONTEXTS.json',import.meta.url),'utf8'));
export function explicitHouseContext(values,context){
 const keys=['system','subject','question'];
 if(!context||Object.getPrototypeOf(context)!==Object.prototype||Object.getOwnPropertySymbols(context).length||Object.keys(context).length!==keys.length||keys.some(k=>!Object.hasOwn(context,k)))throw TypeError('Explicit named source system,subject andquestion ornull required');
 const method=data.methods.find(x=>x.id===context.system);if(!method)throw TypeError('Named extracted method required');
 for(const[k,options]of[['subject',method.subjects],['question',method.questions]])if(context[k]!==null&&!options.includes(context[k]))throw TypeError('Unrecognized explicit '+k);
 const chart=compile(values),complete=context.subject!==null&&context.question!==null;
 const roleDefs=method.roleBySubject?method.roleBySubject[context.subject]:method.roleByQuestion?method.roleByQuestion[context.question]:method.roles;
 const roleEstablished=complete&&Array.isArray(roleDefs)&&roleDefs.length>0;
 const roles=roleEstablished?roleDefs.map(x=>x.kin?{...structuredClone(x),originalLines:chart.lines.filter(y=>y.kin===x.kin).map(y=>y.line),changedLines:chart.lines.filter(y=>y.changed?.kin===x.kin).map(y=>y.line),hiddenRoleAutomaticallySelected:false}:
  {...structuredClone(x),line:x.structuralRole==='世'?chart.primary.shi:chart.primary.ying,notActualPersonOrMeasuredGeometry:true}):null;
 const landform=complete&&method.id==='b02-ch120-landform'?{sourceSiteLine:chart.primary.shi,sourceOppositeLine:chart.primary.ying,sourceMiddleTwoLines:Array.from({length:2},(_,i)=>Math.min(chart.primary.shi,chart.primary.ying)+i+1),actualMeasuredTerrain:null}:null;
 const band=complete&&method.sourceRelativeHeightBands?structuredClone(method.sourceRelativeHeightBands.find(x=>x.sourceLines.includes(chart.primary.shi))):null;
 return{system:method.id,subject:context.subject,question:context.question,sourcePages:[...method.pages],sourceVoice:method.sourceVoice,questionScopeComplete:complete,chart,
  sourceRolesExtracted:roleEstablished,candidateRoleProjections:roles,
  unknownReason:!complete?'explicit-question-scope-incomplete':!roleEstablished?method.sourceRejectsUndifferentiatedQuestion?'source-rejects-undifferentiated-household-query':'named-concern-not-yet-encoded':null,
  sourceRejectsUndifferentiatedQuestion:method.sourceRejectsUndifferentiatedQuestion??false,
  sourceSymbolicLandform:landform,sourceRelativeHeightBand:band,
  sourceHeightIsNotElevationOrDepth:band!==null,sourceRoleIsNotBiologicalIdentity:true,
  useLineSelected:null,strength:null,effectiveActivity:null,actualHouseOrRoomPlan:null,universalDoorLine:null,
  compassBearing:null,realLocation:null,actualElevation:null,diggingDepth:null,landOwnership:null,acquisitionDate:null,
  practitionerQuality:null,constructionSafety:null,healthResult:null,lifespan:null,familyOutcome:null,financialResult:null,
  chronologicalDateAdapter:null,practicalOutcome:null,consumerApplied:false};
}
