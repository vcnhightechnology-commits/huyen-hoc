import{readFileSync}from'node:fs';const t=JSON.parse(readFileSync(new URL('./MANUAL_SOURCE_TABLES.json',import.meta.url),'utf8'));
export const SOURCE_ID=t.sourceID,FRAME_ID=t.frameID;
const branches=[...'子丑寅卯辰巳午未申酉戌亥'],stems=[...'甲乙丙丁戊己庚辛壬癸'],cycle=Array.from({length:60},(_,i)=>stems[i%10]+branches[i%12]),own=(o,k)=>Object.prototype.hasOwnProperty.call(o,k);
function frame(o,keys){return o!==null&&typeof o==='object'&&!Array.isArray(o)&&[Object.prototype,null].includes(Object.getPrototypeOf(o))&&keys.every(k=>own(o,k))&&Reflect.ownKeys(o).every(k=>keys.includes(k))&&o.sourceID===SOURCE_ID&&o.frameID===FRAME_ID;}
function canonical(x,all){if(x!==null&&!all.includes(x))throw new RangeError('Explicit canonical token or null required.');}
function ternary(x){if(![true,false,null].includes(x))throw new TypeError('Explicit true/false/null required.');}
const choices=(x,all)=>x===null?all:[x],quantify=a=>a.every(Boolean)?true:a.every(x=>!x)?false:null;
const withheld=()=>({calendarDate:null,fullFormation:null,effectivePenalty:null,sourceEntryCalculated:false,wholePatternEstablished:null,healthRisk:null,rankPrediction:null,outcome:null,sourceEfficacyValidated:false,appliedToNatalChart:false});
export function sourcePenaltyCoordinate(o){
 if(!frame(o,['sourceID','frameID','classificationVoice','leftOccurrence','rightOccurrence','leftBranch','rightBranch']))return null;
 if(!own(t.classificationVoices,o.classificationVoice)||!['A','B','C','D'].includes(o.leftOccurrence)||!['A','B','C','D'].includes(o.rightOccurrence)||o.leftOccurrence===o.rightOccurrence)return null;
 canonical(o.leftBranch,branches);canonical(o.rightBranch,branches);
 const present=quantify(choices(o.leftBranch,branches).flatMap(a=>choices(o.rightBranch,branches).map(b=>t.directedEdges.some(r=>r.from===a&&r.to===b))));
 const row=t.directedEdges.find(r=>r.from===o.leftBranch&&r.to===o.rightBranch);
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,nominalDirectedCoordinate:present,sourceFamily:row?.family??null,classificationVoice:o.classificationVoice,sourceClassLabel:row?t.classificationVoices[o.classificationVoice][row.family]??null:null,sourceDistinctOccurrencesDeclared:true,wholeThreeBranchGroupRequired:null,alternativeIsCorrection:false,...withheld()});
}
export function sourcePenaltyOrdinal(o){
 if(!frame(o,['sourceID','frameID','rowID']))return null;const row=t.sourceOrdinalRows.find(r=>r.id===o.rowID);if(!row)return null;
 const start=branches.indexOf(row.from),end=branches.indexOf(row.to),count=(row.direction==='forward'?end-start+12:start-end+12)%12+1;
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,rowID:row.id,from:row.from,to:row.to,direction:row.direction,inclusiveCount:count,sourceInclusiveCount:row.sourceInclusiveCount,formulaAdoptedForUnlistedPairs:false,...withheld()});
}
export function sourcePenaltyEntryClause(o){
 if(!frame(o,['sourceID','frameID','sourceDirection','fullThreePenaltyDeclared','entryDeclared']))return null;
 if(!['host-to-guest','guest-to-host'].includes(o.sourceDirection))return null;ternary(o.fullThreePenaltyDeclared);ternary(o.entryDeclared);
 const label=o.fullThreePenaltyDeclared===true&&o.entryDeclared!==null?t.entryClause.baseLabels[o.sourceDirection][o.entryDeclared?'entered':'not-entered']:null;
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,selectedBaseHistoricalLabel:label,fullnessWasDeclared:true,entryWasDeclared:true,baseClauseOnly:true,fuJuContextEvaluated:false,taishuiInvolvementCalculated:false,...withheld()});
}
export function sourcePenaltyLiteralEntry(o){
 if(!frame(o,['sourceID','frameID','sourceAnchorPillar','sourceTargetPillar']))return null;canonical(o.sourceAnchorPillar,cycle);canonical(o.sourceTargetPillar,cycle);
 const match=quantify(choices(o.sourceAnchorPillar,cycle).flatMap(a=>choices(o.sourceTargetPillar,cycle).map(b=>t.literalEntryExamples.some(r=>r.anchor===a&&r.target===b))));
 const row=t.literalEntryExamples.find(r=>r.anchor===o.sourceAnchorPillar&&r.target===o.sourceTargetPillar);
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,literalExampleCoordinate:match,sourceRelation:row?.sourceRelation??null,sourceActionWording:row?.sourceAction??null,literalSourceEntry:row?.literalEntry??null,generalEntryRuleEstablished:false,...withheld()});
}
export function sourcePenaltyControlExample(o){
 if(!frame(o,['sourceID','frameID','sourceYearPillar','sourceDayPillar','sourceHourPillar']))return null;
 for(const p of [o.sourceYearPillar,o.sourceDayPillar,o.sourceHourPillar])canonical(p,cycle);
 const e=t.sourceControlExample,values=[[o.sourceYearPillar,e.yearPillar],[o.sourceDayPillar,e.dayPillar],[o.sourceHourPillar,e.hourPillar]].map(([a,b])=>a===null?null:a===b);
 const result=values.includes(false)?false:values.includes(null)?null:true;
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,literalThreeRoleExample:result,sourceRolesExplicit:true,actualHistoricalDateEstablished:false,sourceControlActuallyEffective:null,...withheld()});
}
export function sourceFourSelfBranches(o){
 if(!frame(o,['sourceID','frameID','sourceSlots','beneficSuppressorDeclared']))return null;ternary(o.beneficSuppressorDeclared);
 if(!Array.isArray(o.sourceSlots)||o.sourceSlots.length!==4||[0,1,2,3].some(i=>!own(o.sourceSlots,i))||Reflect.ownKeys(o.sourceSlots).some(k=>!['0','1','2','3','length'].includes(k)))throw new TypeError('Four explicit source occurrence slots required.');
 for(const b of o.sourceSlots)canonical(b,branches);
 const absent=t.fourSelfBranches.filter(b=>!o.sourceSlots.includes(b)).length,unknown=o.sourceSlots.filter(x=>x===null).length;
 const complete=absent===0?true:absent>unknown?false:null;
 const declaredGate=complete===false||o.beneficSuppressorDeclared===false?false:complete===true&&o.beneficSuppressorDeclared===true?true:null;
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,fourDistinctSourceBranchPremise:complete,sourceCompletenessAndDeclaredBenefic:declaredGate,beneficWasDeclared:true,equivalentToRepeatedSameBranch:false,...withheld()});
}
