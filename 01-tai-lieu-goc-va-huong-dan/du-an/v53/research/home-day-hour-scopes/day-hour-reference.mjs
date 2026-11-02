import{readFileSync}from'node:fs';
const manual=JSON.parse(readFileSync(new URL('./MANUAL_PATTERNS_AND_HOUR_SCOPES.json',import.meta.url),'utf8'));
export const DAY_SYSTEM=manual.daySystem,HOUR_SYSTEM=manual.hourSystem;
const branches=[...'子丑寅卯辰巳午未申酉戌亥'],officers=[...'建除滿平定執破危成收開閉'],tri=x=>x===true||x===false||x===null;
function exact(x,keys){if(!x||Object.getPrototypeOf(x)!==Object.prototype||Reflect.ownKeys(x).length!==keys.length||keys.some(k=>!Object.hasOwn(x,k)))throw TypeError('Exact explicit source fields required.');}
const bounds=()=>({calendarAdapterImplemented:false,sourceMonthOrHourBoundary:null,sourceLeapMonthPolicy:null,sourceTimezone:null,overallRecommendation:null,sourceOutcome:null,consumerApplied:false,wholeSourceMethodApplied:false});
export function sourceDeclaredDayPattern(x){
 exact(x,['system','rule','timeBasis','sourceMonth','sourceSeason','dayBranch','sourceMonthClass','dayOfficer']);
 if(x.system!==DAY_SYSTEM||!['tiandi-turn','tianzei'].includes(x.rule)||!['declared-source-frame','numeric-lunar-month','solar-term-month','unknown'].includes(x.timeBasis))throw TypeError('Named source rule/time frame required.');
 if(x.sourceMonth!==null&&(!Number.isInteger(x.sourceMonth)||x.sourceMonth<1||x.sourceMonth>12)||!['spring','summer','autumn','winter',null].includes(x.sourceSeason)||![...branches,null].includes(x.dayBranch)||!['meng','zhong','ji',null].includes(x.sourceMonthClass)||![...officers,null].includes(x.dayOfficer))throw TypeError('Canonical source coordinates or null required.');
 if(x.rule==='tiandi-turn'&&(x.sourceMonthClass!==null||x.dayOfficer!==null)||x.rule==='tianzei'&&(x.sourceMonth!==null||x.sourceSeason!==null||x.dayBranch!==null))throw TypeError('Irrelevant premises must remain null; no cross-rule inference.');
 let matched=null;
 if(x.timeBasis==='declared-source-frame'){
  if(x.rule==='tiandi-turn'&&x.sourceMonth!==null&&x.sourceSeason!==null&&x.dayBranch!==null)matched=manual.dayPatterns[0].pairs.some(p=>p.season===x.sourceSeason&&p.month===x.sourceMonth&&p.branch===x.dayBranch);
  if(x.rule==='tianzei'&&x.sourceMonthClass!==null&&x.dayOfficer!==null)matched=manual.dayPatterns[1].classToOfficer[x.sourceMonthClass]===x.dayOfficer;
 }
 return{system:DAY_SYSTEM,input:{...x},sourcePatternMatched:matched,sourcePositions:x.rule==='tiandi-turn'?[247]:[247,248],sourceSeasonNotInferredFromMonth:true,sourceOfficerNotInferredFromDate:true,sourcePatternAbsenceIsNotAuspicious:true,overallActivityRestriction:null,tianGouGuardExceptionDerived:false,...bounds()};
}
export function sourceHourParagraph(x){
 exact(x,['system','hazard','declaredHazardStatus','activity','generalHourPremisesConfirmed','readingMode']);
 if(x.system!==HOUR_SYSTEM||!['jielu','xunzhong'].includes(x.hazard)||![x.declaredHazardStatus,x.generalHourPremisesConfirmed].every(tri)||!['memorial','travel','build','burial','office','marriage','relocation','temple-consecration','directional-repair','other','unknown'].includes(x.activity)||!['printed-ri','editorial-xun','unresolved'].includes(x.readingMode))throw TypeError('Explicit named hour paragraph, tri-state premises and reading mode required.');
 const p=manual.hourParagraphs.find(p=>p.id===x.hazard);let local=null;
 if(x.declaredHazardStatus===false)local=false;
 else if(x.declaredHazardStatus===true){if(p.namedRestrictedActivities.includes(x.activity))local=true;else if(p.namedNotAvoidedActivities.includes(x.activity))local=false;}
 const labelMatch=x.hazard==='jielu'?true:x.readingMode==='editorial-xun'?true:null;
 let override=null;
 if(x.declaredHazardStatus===false||x.generalHourPremisesConfirmed===false)override=false;
 else if(x.declaredHazardStatus===true&&x.generalHourPremisesConfirmed===true&&labelMatch===true&&manual.generalHourContext.namedActivities.includes(x.activity))override=true;
 return{system:HOUR_SYSTEM,input:{...x},namedParagraphRestriction:local,namedParagraphPositions:p.positions??[p.position],unlistedActivityDefaultIsUnknown:true,generalHourLiteralDayGlyph:'日',institutionalEditorialDayGlyph:'旬',generalOverrideMentionsChosenHazard:labelMatch,conditionalGeneralOverrideClaim:override,conditionalOverrideIsHistoricalClaim:true,combinedFinalRestriction:null,sourcePrioritiesResolved:false,fullGeneralHourPremisesCalculated:false,sourceDateOrHourClassificationDerived:false,...bounds()};
}
