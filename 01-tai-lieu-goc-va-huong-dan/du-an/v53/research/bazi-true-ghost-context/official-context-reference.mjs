import{readFileSync}from'node:fs';
const t=JSON.parse(readFileSync(new URL('./MANUAL_SOURCE_TABLES.json',import.meta.url),'utf8'));
export const SOURCE_ID=t.sourceID,FRAME_ID=t.frameID;
const stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'],cycle=Array.from({length:60},(_,i)=>stems[i%10]+branches[i%12]);
const own=(o,k)=>Object.prototype.hasOwnProperty.call(o,k);
function frame(o,keys){return o!==null&&typeof o==='object'&&!Array.isArray(o)&&[Object.prototype,null].includes(Object.getPrototypeOf(o))&&keys.every(k=>own(o,k))&&Reflect.ownKeys(o).every(k=>keys.includes(k))&&o.sourceID===SOURCE_ID&&o.frameID===FRAME_ID;}
function token(x,allowed){if(x!==null&&!allowed.includes(x))throw new RangeError('Explicit canonical token or null required.');}
const choices=(x,allowed)=>x===null?allowed:[x];
function quantify(values){return values.every(Boolean)?true:values.every(x=>!x)?false:null;}
const withheld=()=>({calendarDate:null,calendarFeasible:null,realBirthYear:null,realBirthDay:null,effectiveTransformation:null,trueFiveElementCalculated:false,wholePatternEstablished:null,sourceOutcome:null,medicalRisk:null,wealthPrediction:null,rankPrediction:null,strength:null,sourceEfficacyValidated:false,appliedToNatalChart:false});
export function sourceOfficialRegion(o){
 if(!frame(o,['sourceID','frameID','region','anchorStem','sourceMonthBranch']))return null;
 if(!['heaven','earth'].includes(o.region))return null;token(o.anchorStem,stems);token(o.sourceMonthBranch,branches);
 const rows=o.region==='heaven'?t.heavenRows:t.earthRows;
 const result=quantify(choices(o.anchorStem,stems).flatMap(a=>choices(o.sourceMonthBranch,branches).map(b=>rows.some(r=>r.anchorStems.includes(a)&&r.sourceMonthBranches.includes(b)))));
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,region:o.region,listedMonthCoordinate:result,anchorRole:'declared-source-year-stem',monthRole:'declared-source-month-branch',...withheld()});
}
export function sourceTrueOfficialRegion(o){
 if(!frame(o,['sourceID','frameID','sourceMingPillar','sourceMonthPillar']))return null;token(o.sourceMingPillar,cycle);token(o.sourceMonthPillar,cycle);
 const evaluate=(a,b)=>t.stemPartners[a[0]]===b[0]&&branches.indexOf(b[1])===(branches.indexOf(a[1])+3)%12;
 const result=quantify(choices(o.sourceMingPillar,cycle).flatMap(a=>choices(o.sourceMonthPillar,cycle).map(b=>evaluate(a,b))));
 const candidate=o.sourceMingPillar===null?null:t.stemPartners[o.sourceMingPillar[0]]+branches[(branches.indexOf(o.sourceMingPillar[1])+3)%12];
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,sourceTrueRegionCoordinate:result,editorialCandidateMonthPillar:candidate,advanceSteps:3,advanceJustifiedByPrintedExample:true,derivedSixtyRowTableIsPrinted:false,...withheld()});
}
export function sourceTrueOfficialGhostDistinction(o){
 if(!frame(o,['sourceID','frameID','naYinOvercomeByDeclaredTrueElement','originalStemAlsoOvercome']))return null;
 for(const p of [o.naYinOvercomeByDeclaredTrueElement,o.originalStemAlsoOvercome])if(![true,false,null].includes(p))throw new TypeError('Both source predicates must be true, false or null.');
 const label=o.naYinOvercomeByDeclaredTrueElement===true?(o.originalStemAlsoOvercome===true?'真鬼':o.originalStemAlsoOvercome===false?'真官':null):null;
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,selectedTerminalSourceLabel:label,sourcePredicatesWereDeclared:true,terminalClauseOnly:true,completeOfficialMethodEvaluated:false,appliesAutomaticallyToSixHarm:false,...withheld()});
}
export function sourceTrueGhostLiteralPair(o){
 if(!frame(o,['sourceID','frameID','sourceAnchorPillar','seenStemPair']))return null;token(o.sourceAnchorPillar,cycle);
 if(!Array.isArray(o.seenStemPair)||o.seenStemPair.length!==2||[0,1].some(i=>!own(o.seenStemPair,i))||Reflect.ownKeys(o.seenStemPair).some(k=>!['0','1','length'].includes(k)))throw new TypeError('Two explicit source stem slots required.');
 for(const x of o.seenStemPair)token(x,stems);
 const evaluate=(p,a,b)=>t.literalCounterexamples.some(r=>r.anchorPillars.includes(p)&&a!==b&&r.seenStemPair.includes(a)&&r.seenStemPair.includes(b));
 const result=quantify(choices(o.sourceAnchorPillar,cycle).flatMap(p=>choices(o.seenStemPair[0],stems).flatMap(a=>choices(o.seenStemPair[1],stems).map(b=>evaluate(p,a,b)))));
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,literalCounterexampleCoordinate:result,sourceTargetPillarRolesEstablished:false,pairPresenceIsSufficientForTrueGhost:false,fullNarrativeConditionsEvaluated:false,...withheld()});
}
