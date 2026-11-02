// Private B02 chapter29 source-layer matches; no strength/calendar/forecast adjudication.
import{compile}from'../liuyao-foundations/liuyao-reference.mjs';
const advance=['亥子','寅卯','巳午','申酉','丑辰','辰未','未戌','戌丑'];
const retreat=['子亥','卯寅','午巳','酉申','辰丑','未辰','戌未','丑戌'];
const strengthKeys=['originalStrength','changedStrength'],boolKeys=['originalVoid','changedVoid','originalBroken','changedBroken','nearTerm','hasDayMonthOrMovingSupport','originalAtDayOrMonth'];
const all=(...x)=>x.includes(false)?false:x.includes(null)?null:true,any=(...x)=>x.includes(true)?true:x.includes(null)?null:false;
const strength=(value,wanted)=>value==null?null:value===wanted;
export function progressionClauses(values,context,...extra){
 if(extra.length||!context||typeof context!=='object'||Array.isArray(context)||Object.getOwnPropertySymbols(context).length||
  Object.keys(context).some(k=>!['sourceContext','line',...strengthKeys,...boolKeys].includes(k))||context.sourceContext!=='B02-ch029'||
  !Number.isInteger(context.line)||context.line<1||context.line>6)throw TypeError('Explicit B02-ch029 selected-line context only.');
 for(const k of strengthKeys)if(context[k]!==undefined&&context[k]!==null&&!['旺相','休囚'].includes(context[k]))throw TypeError('Explicit categorical strength, no inferred score.');
 for(const k of boolKeys)if(context[k]!==undefined&&context[k]!==null&&typeof context[k]!=='boolean')throw TypeError('Only asserted boolean or unknown premises.');
 const chart=compile(values),line=chart.lines[context.line-1],pair=line.moving?line.branch+line.changed.branch:null,
  kind=advance.includes(pair)?'advance':retreat.includes(pair)?'retreat':null;
 const fact=Object.fromEntries([...strengthKeys,...boolKeys].map(k=>[k,context[k]??null]));
 const strongA=strength(fact.originalStrength,'旺相'),strongB=strength(fact.changedStrength,'旺相'),
  weakA=strength(fact.originalStrength,'休囚'),weakB=strength(fact.changedStrength,'休囚'),
  oneVoidOrBroken=any(fact.originalVoid,fact.changedVoid,fact.originalBroken,fact.changedBroken);
 const rules=kind==='advance'?[
  ['advance1',all(strongA,strongB),'乘勢而進'],['advance2',all(weakA,weakB),'待時而進'],
  ['advance3',any(weakA,weakB),'待旺相之日而進'],['advance4',oneVoidOrBroken,'待填實之日而進']
 ]:kind==='retreat'?[
  ['retreat1',all(any(all(strongA,strongB),fact.hasDayMonthOrMovingSupport),fact.nearTerm),'占近事得時而不退'],
  ['retreat2',all(weakA,weakB),'及時而退'],['retreat3',any(strongA,strongB),'待休囚之時而退'],
  ['retreat4',oneVoidOrBroken,'待填實之日而退']
 ]:[];
 const clauses=rules.map(([id,result,sourceQualitativeTiming])=>({id,result,sourcePDFPage:123,
  sourceLayer:'printed-list-introduced-by-野鶴曰',sourceQualitativeTiming}));
 const laterCautions=kind?[{id:'do-not-veto-from-transformed-void-break-alone',sourcePDFPages:[123,124],
  sourceLayer:'later-commentary-introduced-by-李我平日',
  result:all(fact.originalAtDayOrMonth,any(fact.changedVoid,fact.changedBroken)),
  boundedMeaning:'A day/month-aligned original moving line must not be denied progression solely because its own change is void/broken.',
  effect:'retain-original-strength-and-later-context;no-automatic-override'}]:[];
 return{schema:'hhc.B02-ch029.clause-matches.v2',selectedLine:context.line,primaryBranch:line.branch,
  changedBranch:line.changed?.branch??null,structuralPair:pair,structuralKind:kind,clauses,
  matchedClauseIDs:clauses.filter(c=>c.result===true).map(c=>c.id),unknownClauseIDs:clauses.filter(c=>c.result===null).map(c=>c.id),
  assertedPremises:fact,exclusiveClassification:false,youYiReadInclusivelyForResearch:true,
  laterCommentaryCautions:laterCautions,laterCommentaryCautionMatched:laterCautions.some(c=>c.result===true),
  concurrentListAndLaterCaution:clauses.some(c=>c.result===true)&&laterCautions.some(c=>c.result===true),
  laterEditorialCritiqueApplied:'bounded-caution-matches-only',sourcePriorityInvented:false,
  fullChapterReconciliationComplete:false,effectiveProgression:null,
  predictedDate:null,predictedEvent:null,consumerApplied:false};
}
export function visibleMotionPattern(values,...extra){
 if(extra.length)throw TypeError('Only the six explicit cast values are supported.');
 const chart=compile(values),moving=chart.movingLines,stationary=chart.lines.filter(l=>!l.moving).map(l=>l.line);
 return{sourceID:'B02-ch031',sourcePDFPages:[130,131,132,133,134],movingLines:moving,stationaryLines:stationary,
  uniqueVisibleMovingLine:moving.length===1?moving[0]:null,uniqueVisibleStationaryLine:stationary.length===1?stationary[0]:null,
  darkMotionDerived:false,useGodMayBeDiscarded:false,effectiveUseSelection:null,predictedEvent:null,consumerApplied:false};
}
