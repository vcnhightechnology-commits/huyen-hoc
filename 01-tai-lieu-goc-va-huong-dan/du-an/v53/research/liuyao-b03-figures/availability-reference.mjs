// Private B03 PDF59 visible/changed availability gate. Explicit desiredkin only.
import{candidates}from'../liuyao-hidden-spirits/hidden-reference.mjs';
export function figureAvailability(values,desiredKin,...extra){
 if(extra.length)throw TypeError('onlyexplicitvaluesanddesiredkin;calendar/卦身notimplementedhere');
 const a=candidates(values,desiredKin),visible=a.chart.lines.filter(l=>l.kin===desiredKin).map(l=>({line:l.line,kind:'primary',branch:l.branch,kin:l.kin})),
 changed=a.chart.lines.filter(l=>l.changed?.kin===desiredKin).map(l=>({line:l.line,kind:'changed',branch:l.changed.branch,kin:l.changed.kin})),shown=[...visible,...changed];
 return{schema:'hhc.liuyao.B03-figure-availability.v1',sourceID:'B03',sourcePDFPage:59,desiredKin,
  chart:a.chart,visibleCandidates:visible,changedCandidates:changed,
  structuralHiddenSearchNeeded:shown.length===0,sourceDefaultHiddenSearch:shown.length?'not-requested-kin-shown':'pure-palace-candidate-search',
  hiddenSearchCandidates:shown.length?[]:a.rootMatches,purePalaceDiagnostic:a.rootMatches,
  shownCandidateSelection:shown.length===1?{...shown[0],basis:'unique-shown-kin-coordinate-not-effectiveness'}:null,
  precedenceBetweenMultipleShownCandidates:null,calendarAvailability:null,overallSearchDecision:null,
  effectiveUseGodSelection:null,卦身Method:null,predictedEvent:null,consumerApplied:false};
}
