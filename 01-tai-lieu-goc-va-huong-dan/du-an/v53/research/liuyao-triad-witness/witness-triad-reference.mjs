import {triadContexts} from '../liuyao-combination-context/triad-context-reference.mjs';
export const JAPAN_ID='B02-Japan-4756814-volume2';
export const NLC_ID='B02-NLC416-12jh005345-45344';
const plain=o=>o!==null&&typeof o==='object'&&!Array.isArray(o)&&Object.getPrototypeOf(o)===Object.prototype&&!Object.getOwnPropertySymbols(o).length;
export function witnessTriadContexts(values,context) {
 if(!plain(context))throw new TypeError('Explicit plain source context required.');
 if(!Object.hasOwn(context,'sourceID')||![JAPAN_ID,NLC_ID].includes(context.sourceID))return null;
 const {sourceID,...oldContext}=context;
 const legacy=triadContexts(values,oldContext);
 const dark=oldContext.darkMovementByLine??{};
 const groups=legacy.groups.map(g=>({...g,primaryWitnesses:g.primaryWitnesses.map(w=>{
  let candidate=null,reason='NLC-one-literal-unadjudicated';
  if(sourceID===JAPAN_ID) {
   const allActual=w.nodes.every(n=>n.actualMoving);
   if(!allActual) {
    candidate=w.unknownActiveCount>0||w.knownActiveCount===3?null:false;
    reason='three-actual-subset-not-established';
   }else{
    const selected=new Set(w.nodes.map(n=>n.line));
    const other=legacy.chart.lines.filter(l=>!selected.has(l.line));
    const extraKnownActive=other.some(l=>l.moving||dark[l.line]===true);
    const extraUnknown=other.some(l=>!l.moving&&dark[l.line]!==false&&dark[l.line]!==true);
    candidate=extraKnownActive||extraUnknown?null:true;
    reason=candidate===true?'Japan-three-actual-known-rest-inactive':'additional-or-unknown-activity-unadjudicated';
   }
  }
  return {...w,selectedWitnessSourceID:sourceID,firstModeThreeActualMovingCandidate:candidate,
   firstModeCandidateReason:reason,fullSourceFormation:null,sourceFillOrOpenDate:null,practicalOutcome:null};
 })}));
 return {selectedWitnessSourceID:sourceID,
  selectedFirstModeDiplomatic:sourceID===JAPAN_ID?'一卦之內有三交動而合局者一也':'一卦之內有一交動而合局者一也',
  explicitWorkingLineGlyphNormalization:'交→爻 in line-reference context only',
  selectedFirstModeActualMovingSubset:sourceID===JAPAN_ID?3:null,
  selectedCountIsFullSemanticAdjudication:false,
  conservativeSubset:'Exactly three actual moving primary members; every other primary line explicitly inactive. Other source modes stay separate.',
  chart:legacy.chart,groups,legacyNLCFirstModeLiteral:legacy.firstModeLiteral,
  legacyNLCCountInterpretation:legacy.firstModeCountInterpretation,
  legacyNLCNotEmended:legacy.firstModeNotSilentlyEmended,
  effectiveFormation:null,transformedElement:null,calendarEpoch:null,practicalOutcome:null,
  sourceOutcomesValidated:false,consumerApplied:false};
}
