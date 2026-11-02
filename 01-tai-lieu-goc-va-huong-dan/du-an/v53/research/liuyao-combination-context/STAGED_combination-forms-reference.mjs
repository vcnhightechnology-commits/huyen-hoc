// Private B02PDF73–74: six named combination forms, structural coordinates only.
import{compile}from'../../v53/research/liuyao-foundations/liuyao-reference.mjs';
import{branchRelations}from'../../v53/research/liuyao-day-month/day-month-reference.mjs';
const branches=[...'子丑寅卯辰巳午未申酉戌亥'];
function pairs(chart){return[1,2,3].map(n=>({lowerLine:n,upperLine:n+3,relation:branchRelations(chart.lines[n-1].branch,chart.lines[n+2].branch)}));}
export function combinationForms(values,context={}){
 if(!context||typeof context!=='object'||Array.isArray(context)||Object.getPrototypeOf(context)!==Object.prototype||Object.getOwnPropertySymbols(context).length||Object.keys(context).some(k=>!['monthBranch','dayBranch'].includes(k))||Object.values(context).some(v=>!branches.includes(v)))throw TypeError('Only explicitly named month/day branches;no automatic date or strength adapter.');
 const chart=compile(values),changed=compile(chart.changed.bits.map(b=>b?7:8));
 const primaryPairs=pairs(chart),changedPairs=pairs(changed),primarySixCombination=primaryPairs.every(x=>x.relation.combination),changedSixCombination=changedPairs.every(x=>x.relation.combination),primarySixClash=primaryPairs.every(x=>x.relation.clash);
 const calendarPairs=[];for(const[k,b]of Object.entries(context))for(const l of chart.lines)if(branchRelations(b,l.branch).combination)calendarPairs.push({calendarRole:k,calendarBranch:b,line:l.line,branch:l.branch,sourceLabel:l.moving?'合絆':'合起',sourceLabelIsNotAppliedEffect:true});
 const movingPairs=[],staticRaisedCoordinates=[];
 for(let i=0;i<6;i++)for(let j=i+1;j<6;j++){
  const a=chart.lines[i],b=chart.lines[j];if(!branchRelations(a.branch,b.branch).combination)continue;
  if(a.moving&&b.moving)movingPairs.push({lines:[a.line,b.line],branches:[a.branch,b.branch],sourceLabel:'合好',sourceLabelIsNotAppliedEffect:true});
  else if(a.moving!==b.moving)staticRaisedCoordinates.push({movingLine:a.moving?a.line:b.line,staticLine:a.moving?b.line:a.line,sourceLabel:'合起',sourceLabelIsNotAppliedEffect:true});
 }
 const ownChangedPairs=chart.lines.filter(l=>l.changed&&branchRelations(l.branch,l.changed.branch).combination).map(l=>({line:l.line,originalBranch:l.branch,changedBranch:l.changed.branch,sourceLabelPDF74:'化扶',source51HeldOriginCaveatMayBeSeparate:true,appliedSupport:null,appliedHold:null}));
 const moving=chart.movingLines.length>0;
 return{chart,changedChartNumber:changed.primary.number,primaryPairs,changedPairs,calendarPairs,movingPairs,staticRaisedCoordinates,ownChangedPairs,
  forms:[{sourceOrdinal:1,label:'日月合爻',coordinatePresent:calendarPairs.length>0},{sourceOrdinal:2,label:'爻與爻合',coordinatePresent:movingPairs.length>0},{sourceOrdinal:3,label:'爻動化合',coordinatePresent:ownChangedPairs.length>0},{sourceOrdinal:4,label:'卦逢六合',coordinatePresent:primarySixCombination},{sourceOrdinal:5,label:'六沖卦變六合',coordinatePresent:moving&&primarySixClash&&changedSixCombination},{sourceOrdinal:6,label:'六合卦變六合',coordinatePresent:moving&&primarySixCombination&&changedSixCombination}],
  primarySixCombination,changedSixCombination,primarySixClash,
  functionalCombination:null,transformationElement:null,automaticHold:null,releaseDate:null,useLine:null,sourceOutcomeValidated:false,practicalOutcome:null,consumerApplied:false,
  sourceLimits:['B02PDF74 calls own-changed pairing化扶,whilePDF51has a specificheld-origin case;no globalpriorityimposed.','Source76six-clash-to-combinationexceptiontoordinaryuse-strengthwording remains a historicalclaim,not an outcome rule.','Triad formation77–79is a different rule set and isnotinferredfromsix-paircoordinates.','Unknown darkactivity/strength/void/root/hold-releasepremisesremainunknown.']};
}
