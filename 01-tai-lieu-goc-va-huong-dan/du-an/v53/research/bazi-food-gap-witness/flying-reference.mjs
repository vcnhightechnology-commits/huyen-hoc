import {readFileSync} from 'node:fs';
const table=JSON.parse(readFileSync(new URL('./DAY_AND_COORDINATE_TABLES.json',import.meta.url),'utf8'));
const stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'];
const cycle=Array.from({length:60},(_,i)=>stems[i%10]+branches[i%12]);
const plain=x=>!!x&&Object.getPrototypeOf(x)===Object.prototype&&Reflect.ownKeys(x).every(k=>typeof k==='string');
const presence=(p,test)=>p.some(x=>x!==null&&test(x))?true:p.includes(null)?null:false;
const and=x=>x.includes(false)?false:x.includes(null)?null:true;
// Source-visible coordinates only. Virtual source 官 is never inserted as an actual pillar.
export function sourceFlyingCoordinates(input){
 if(!plain(input)||Reflect.ownKeys(input).length!==2||!Object.hasOwn(input,'system')||!Object.hasOwn(input,'pillars'))throw TypeError('Exact named system and four explicit pillars required.');
 const set=table.daySets.find(x=>input.system==='TMTH005-'+x.id);
 if(!set||!Array.isArray(input.pillars)||input.pillars.length!==4||!Array.from(input.pillars).every(x=>x===null||cycle.includes(x)))throw TypeError('Named source voice and canonical four pillars or null required.');
 const p=input.pillars,day=p[2],daySetMatches=day===null?null:set.days.includes(day);
 // Six-day quote has its own clause. Do not inherit two-day mechanism gates into it.
 const mechanism=set.id==='daochong-six-quoted'?null:table.mechanismCases.find(x=>x.day===day&&x.id.startsWith(set.id==='feitian-four-prose'?'fei-':'dao-'))??null;
 const occurrences=(symbols,index)=>p.flatMap((x,i)=>x!==null&&symbols.includes(x[index])?[{position:i,pillar:x,symbol:x[index]}]:[]);
 const raw=mechanism?{
   caseID:mechanism.id,
   knownRepeatedBranchCount:p.filter(x=>x!==null&&x[1]===mechanism.repeatedBranch).length,
   additionalRepeatedBranchPositions:[0,1,3].filter(i=>p[i]!==null&&p[i][1]===mechanism.repeatedBranch),
   repeatedBranchInventoryComplete:!p.includes(null),quantityThresholdAdjudicated:false,
   visibleSourceOfficerPresence:presence(p,x=>x[0]===mechanism.sourceOfficerStem),
   visibleVirtualTargetBranchPresence:presence(p,x=>x[1]===mechanism.virtualTargetBranch),
   sourceVirtualTarget:{branch:mechanism.virtualTargetBranch,officerStem:mechanism.sourceOfficerStem,isActualPillar:false},
   printedAttractionPool:mechanism.printedAttractionBranchPool.slice(),attractionScope:mechanism.attractionScope,
   rawAttractionOccurrences:occurrences(mechanism.printedAttractionBranchPool,1),
   rawRestraintOccurrences:occurrences(mechanism.printedRestraintBranchPool,1),
   rawStemMentionOccurrences:occurrences(mechanism.visibleStemMentions,0),
   sourceFocusedStem:mechanism.laterFocusedStem??null,
   sourceRawHitsAreNotFinalRejection:true,attractionOrRestraintEffective:null,
  }:null;
 const fireBranches=[...'寅午戌'].map(branch=>({branch,visible:presence(p,x=>x[1]===branch)}));
 return {system:input.system,pillars:p.slice(),sourceVoice:set.kind,daySetMatches,
   sourceDaySet:set.days.slice(),rawMechanism:raw,
   sixDayQuoteVisibleInventory:set.id==='daochong-six-quoted'?{
    fireBranches,allThreeFireBranchesVisible:and(fireBranches.map(x=>x.visible)),
    knownBingStemCount:p.filter(x=>x!==null&&x[0]==='丙').length,countComplete:!p.includes(null),
    countDoesNotEstablishEffectiveThreeHarmony:true}:null,
   finalEditorTwoDayPreference:set.id.startsWith('daochong-')?table.finalDaoComment.days.slice():null,sixDayQuoteNotErasedByPreference:true,
   additionalSourceConditionsNotEvaluated:set.additionalConditionsNotAutomaticallyEvaluated.slice(),
   sourceActualCalendarPolicy:null,effectiveVirtualClash:null,effectiveBinding:null,wholePatternEstablished:null,
   practicalOutcome:null,consumerApplied:false};
}
