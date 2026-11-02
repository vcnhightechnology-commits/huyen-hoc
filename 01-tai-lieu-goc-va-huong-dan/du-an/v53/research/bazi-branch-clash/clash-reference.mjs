import{readFileSync}from'node:fs';const t=JSON.parse(readFileSync(new URL('./MANUAL_SOURCE_TABLES.json',import.meta.url),'utf8'));
export const SOURCE_ID=t.sourceID,FRAME_ID=t.frameID;
const branches=[...'子丑寅卯辰巳午未申酉戌亥'],stems=[...'甲乙丙丁戊己庚辛壬癸'],cycle=Array.from({length:60},(_,i)=>stems[i%10]+branches[i%12]),own=(o,k)=>Object.prototype.hasOwnProperty.call(o,k);
function frame(o,keys){return o!==null&&typeof o==='object'&&!Array.isArray(o)&&[Object.prototype,null].includes(Object.getPrototypeOf(o))&&keys.every(k=>own(o,k))&&Reflect.ownKeys(o).every(k=>keys.includes(k))&&o.sourceID===SOURCE_ID&&o.frameID===FRAME_ID;}
function token(v,all){if(v!==null&&!all.includes(v))throw new RangeError('Canonical token or null required.');}
const values=(v,all)=>v===null?all:[v],quantify=a=>a.every(Boolean)?true:a.every(x=>!x)?false:null;
const withheld=()=>({calendarDate:null,calendarFeasibility:null,effectiveClash:null,fullPattern:null,overallGoodBad:null,medicalRisk:null,morality:null,rankPrediction:null,sourceEfficacyValidated:false,appliedToNatalChart:false});
export function sourceClashCoordinate(o){
 if(!frame(o,['sourceID','frameID','leftOccurrence','rightOccurrence','leftBranch','rightBranch']))return null;
 if(!['A','B','C','D'].includes(o.leftOccurrence)||!['A','B','C','D'].includes(o.rightOccurrence)||o.leftOccurrence===o.rightOccurrence)return null;
 token(o.leftBranch,branches);token(o.rightBranch,branches);
 const gate=quantify(values(o.leftBranch,branches).flatMap(a=>values(o.rightBranch,branches).map(b=>t.clashPartners[a]===b)));
 const count=o.leftBranch===null||o.rightBranch===null?null:(branches.indexOf(o.rightBranch)-branches.indexOf(o.leftBranch)+12)%12+1;
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,nominalClash:gate,forwardInclusiveCount:count,sourceSevenPositionCoordinate:count===null?null:count===7,sourceGeneralAdverseVerdictPermitted:false,...withheld()});
}
export function sourceClashLiteralExample(o){
 if(!frame(o,['sourceID','frameID','sourceAnchorPillar','sourceOtherPillar']))return null;token(o.sourceAnchorPillar,cycle);token(o.sourceOtherPillar,cycle);
 const gate=quantify(values(o.sourceAnchorPillar,cycle).flatMap(a=>values(o.sourceOtherPillar,cycle).map(b=>t.literalPillarPairs.some(r=>r.anchor===a&&r.other===b))));
 const row=t.literalPillarPairs.find(r=>r.anchor===o.sourceAnchorPillar&&r.other===o.sourceOtherPillar);
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,literalExampleCoordinate:gate,sourceRelationLabel:row?.sourceLabel??null,sourceEfficacyConditionsComplete:false,...withheld()});
}
export function sourceClashCompleteGroup(o){
 if(!frame(o,['sourceID','frameID','groupID','sourceSlots']))return null;if(!own(t.completeGroups,o.groupID))return null;
 if(!Array.isArray(o.sourceSlots)||o.sourceSlots.length!==4||[0,1,2,3].some(i=>!own(o.sourceSlots,i))||Reflect.ownKeys(o.sourceSlots).some(k=>!['0','1','2','3','length'].includes(k)))throw new TypeError('Four explicit source slots required.');
 for(const b of o.sourceSlots)token(b,branches);
 const missing=t.completeGroups[o.groupID].filter(b=>!o.sourceSlots.includes(b)).length,unknown=o.sourceSlots.filter(x=>x===null).length,complete=missing===0?true:missing>unknown?false:null;
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,groupID:o.groupID,sourceCompletenessPremise:complete,sourceLiteralSaysNotTreatAsOrdinaryClash:complete===true?true:complete===false?false:null,completeGreatPatternEstablished:null,...withheld()});
}
export function sourceYuJingClashDirection(o){
 if(!frame(o,['sourceID','frameID','declaredImage','selfRole','otherRole']))return null;
 if(!['吉象','凶象',null].includes(o.declaredImage)||!['用神','閒神',null].includes(o.selfRole)||!['用神','閒神',null].includes(o.otherRole))throw new RangeError('Source image and role labels or null required.');
 const roles=o.selfRole!==null&&o.selfRole!=='用神'||o.otherRole!==null&&o.otherRole!=='閒神'?false:o.selfRole===null||o.otherRole===null?null:true;
 const direction=roles===true?t.yuJingDirection.find(r=>r.declaredImage===o.declaredImage)?.sourceDesiredDirection??null:null;
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,sourceRolePremise:roles,sourceDesiredDirection:direction,rolesWereDeclared:true,qiAndSupportEvaluated:false,...withheld()});
}
export function sourceLuClashExample(o){
 if(!frame(o,['sourceID','frameID','sourceAnchorStem','sourceLuBranch','seenBranch']))return null;
 token(o.sourceAnchorStem,stems);token(o.sourceLuBranch,branches);token(o.seenBranch,branches);
 const matched=[[o.sourceAnchorStem,'甲'],[o.sourceLuBranch,'寅'],[o.seenBranch,'申']].map(([a,b])=>a===null?null:a===b),gate=matched.includes(false)?false:matched.includes(null)?null:true;
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,literalLuClashCoordinate:gate,yearDayAnchorAutomaticallyChosen:false,luPositionCalculated:false,wholeLuBreakingEffect:null,...withheld()});
}
