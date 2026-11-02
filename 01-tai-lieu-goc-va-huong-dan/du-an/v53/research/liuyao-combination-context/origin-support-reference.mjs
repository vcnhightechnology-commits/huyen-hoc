// Private B02source51exception boundary; no event or clinical inference.
import{actorConditions}from'../liuyao-use-god/use-god-reference.mjs';
import{branchRelations}from'../liuyao-day-month/day-month-reference.mjs';
const plain=x=>!!x&&typeof x==='object'&&!Array.isArray(x)&&Object.getPrototypeOf(x)===Object.prototype&&!Object.getOwnPropertySymbols(x).length;
export function inspectOriginSupport(values,useLine,originLine,context={}){
 if(!plain(context)||Object.keys(context).some(k=>!['premises','changedCombinationHold'].includes(k)))throw TypeError('Only explicit research premises and changedCombinationHold are supported.');
 const premises=context.premises??{};
 if(!plain(premises))throw TypeError('Explicit own boolean research premises only.');
 const held=context.changedCombinationHold??null;
 if(held!==null&&typeof held!=='boolean')throw TypeError('changedCombinationHold must be true,false or null.');
 const conditions=actorConditions(values,useLine,originLine,premises),actor=conditions.graph.nodes[originLine-1];
 if(actor.relativeRole!=='元神')throw TypeError('This source exception only addresses an explicit origin line.');
 const ownChangedCombination=actor.changed?branchRelations(actor.branch,actor.changed.branch).combination:false;
 if(held===true&&!ownChangedCombination)throw TypeError('A declared own-changed combination hold requires a real moving branch combination.');
 const source51Blocker=ownChangedCombination?(held===null?null:held):false;
 return{source:'B02PDF51own-changed-combination-caveat',conditions,originLine,useLine,
  ownChangedCombination,changedBranch:actor.changed?.branch??null,declaredChangedCombinationHold:held,
  source51Blocker,source51BlockerIsNotAutomaticFromCombinationPresence:true,
  matchedEffectiveClausesBeforeCaveat:conditions.effectiveMatches.slice(),
  unconditionalSupportClaimAllowed:source51Blocker===true?false:null,
  supportVerdict:null,releaseFromHold:null,useLineSelection:null,overallStrength:null,
  clinicalOutcome:null,practicalOutcome:null,consumerApplied:false,
  remainingPremises:['source-qualified hold/release determination','complete root/qi and effective-strength assessment','other concurrent source exceptions','calendar boundary if a date is later provided'],
  policy:'Source51explicitly blocks this declared held-origin case. A raw午未orotherbranchcombination alone doesnotprovea hold,and lack of thisblockerdoesnotproveeffectivegeneration.'};
}
