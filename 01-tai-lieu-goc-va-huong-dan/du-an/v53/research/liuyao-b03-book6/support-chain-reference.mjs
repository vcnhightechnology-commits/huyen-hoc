// Q3: a generating primary line is a candidate 原神, not a proved effective rescue.
import {compile} from '../liuyao-foundations/liuyao-reference.mjs';
import {branchRelations} from '../liuyao-day-month/day-month-reference.mjs';
export function supportChainCoordinates(values,context,...extra){
 if(extra.length||!context||typeof context!=='object'||Array.isArray(context)||Object.getOwnPropertySymbols(context).length||
  Object.keys(context).some(k=>!['sourceContext','useLine'].includes(k))||context.sourceContext!=='B03-question3-original-support'||
  !Number.isInteger(context.useLine)||context.useLine<1||context.useLine>6)
  throw TypeError('Explicit B03-question3-original-support and selected primary useLine1..6 only.');
 const chart=compile(values),use=chart.lines[context.useLine-1];
 const candidates=chart.lines.filter(l=>l.line!==use.line&&branchRelations(l.branch,use.branch).generates).map(l=>{
  const ownReturn=l.changed?branchRelations(l.changed.branch,l.branch):null;
  return{line:l.line,branch:l.branch,kin:l.kin,moving:l.moving,sourcePDFPages:[9,10,11],
   primaryToSelectedUse:branchRelations(l.branch,use.branch),
   actualOwnChange:l.changed?structuredClone(l.changed):null,ownReturnRelation:ownReturn,
   rawOwnChangeControlsOriginal:ownReturn?.controls??null,
   structuralCaution:ownReturn?.controls?'source-own-change-control-premise-present':
    ownReturn?'own-change-control-not-present-other-premises-unresolved':'no-own-change-static-activation-unresolved',
   activation:null,overallStrength:null,effectiveGeneration:null,rescueOutcome:null};
 });
 return{schema:'hhc.liuyao.B03.support-chain-coordinates.v1',sourceID:'B03-book6',sourceQuestion:3,
  sourceContext:context.sourceContext,chart,selectedUse:{line:use.line,branch:use.branch,kin:use.kin},
  candidateOrigins:candidates,emptyCandidateListProvesNoRescue:false,
  hiddenOriginalSupportSearched:false,changedBranchesSubstitutedForPrimarySupport:false,
  ownChangedBranchMayNotAddressOtherPositions:true,
  missingPremises:['subject/use selection justification','month/day/strength','hidden original support',
   'functional void/retreat/extinction/tomb/monthbreak','static activation/dark movement','source priorities and outcome validation'],
  automaticUseGodSelection:false,effectiveSupportSelection:null,allSourceExceptionsChecked:false,
  predictedEvent:null,consumerApplied:false};
}
