import {readFileSync} from 'node:fs';
const manual=JSON.parse(readFileSync(new URL('./MANUAL_PREMISES_REVISED.json',import.meta.url),'utf8'));
export const SYSTEMS=Object.freeze({...manual.systems});
const tri=x=>x===true||x===false||x===null;
const and=(a,b)=>a===false||b===false?false:a===null||b===null?null:true;
function exact(x,keys){if(!x||Object.getPrototypeOf(x)!==Object.prototype||Reflect.ownKeys(x).length!==keys.length||keys.some(k=>!Object.hasOwn(x,k)))throw TypeError('Exact named source premises required.');}
function checked(x,name,keys,triKeys){exact(x,['system',...keys]);if(x.system!==SYSTEMS[name]||triKeys.some(k=>!tri(x[k])))throw TypeError('Named source system and boolean-or-null premises required.');}
const bounds=()=>({calendarAdapterImplemented:false,sourceBoundaryTimestamp:null,sourceLeapMonthPolicy:null,modernTimeZoneAssigned:false,overallRecommendation:null,sourceOutcome:null,wholeSourceMethodApplied:false,consumerApplied:false});
export function sourceWorkContinuity(x){
 checked(x,'continuity',['timeBasis','operation','afterPillarRaising','hasPaused','sourceBoundaryCrossed','currentDirectionHarmful','currentBenefic'],['afterPillarRaising','hasPaused','sourceBoundaryCrossed','currentDirectionHarmful','currentBenefic']);
 if(!['declared-source-month-term','solar-term-month','numeric-lunar-month','unknown'].includes(x.timeBasis)||!['repair-existing','new-build','other','unknown'].includes(x.operation))throw TypeError('Explicit source frame/operation required.');
 let value=null,status='premises-unresolved',reassess=null;
 if(x.timeBasis!=='declared-source-month-term')status='source-time-frame-unestablished';
 else if(x.operation!=='repair-existing')status='operation-not-addressed';
 else if(x.afterPillarRaising!==true)status=x.afterPillarRaising===false?'outside-selected-after-pillar-context':'premises-unresolved';
 else if(x.sourceBoundaryCrossed!==true)status=x.sourceBoundaryCrossed===false?'no-cross-boundary-claim-evaluated':'premises-unresolved';
 else if(x.hasPaused===false){value=true;status='continuous-after-pillar-local-statement';reassess=false;}
 else if(x.hasPaused===true){reassess=true;if(x.currentDirectionHarmful===true){value=false;status='paused-harmful-direction-veto';}else if(x.currentDirectionHarmful===false){value=true;status='paused-declared-no-harm-local-statement';}else status='paused-direction-occupation-unresolved';}
 return{system:SYSTEMS.continuity,input:{...x},sourceLocalContinuation:value,sourceReassessmentRequired:reassess,status,currentBeneficAloneDoesNotResolveVeto:x.currentBenefic===true&&x.currentDirectionHarmful===null,sourcePositions:[257,258],...bounds()};
}
export function sourceCentralRepairPremises(x){
 checked(x,'central',['centerOccupationHarmful','centerBenefic','hasPaused','sourceBoundaryCrossed'],['centerOccupationHarmful','centerBenefic','hasPaused','sourceBoundaryCrossed']);
 const noHarm=x.centerOccupationHarmful===null?null:!x.centerOccupationHarmful;
 return{system:SYSTEMS.central,input:{...x},sourceInitialConjunction:and(noHarm,x.centerBenefic),sourcePausedBoundaryWarning:and(x.hasPaused,x.sourceBoundaryCrossed),overallRepairPermission:null,combinedPriorityResolved:false,sourceZoneBoundary:'屋簷滴水內',sourceZonePolygon:null,sourcePositions:[258,259],...bounds()};
}
export function sourceFunctionalAnchor(x){
 checked(x,'anchor',['caseID','sourcePremisesConfirmed'],['sourcePremisesConfirmed']);
 const row=manual.records.find(r=>r.id==='anchor').cases.find(r=>r.id===x.caseID);
 if(!row)throw TypeError('Named source building configuration required.');
 const confirmed=x.sourcePremisesConfirmed===true;
 return{system:SYSTEMS.anchor,input:{...x},sourceAnchor:confirmed?row.sourceAnchor:null,symbolicAnchor:confirmed?row.symbolicAnchor:null,requiredSourcePremises:row.sourcePremises,sourcePositions:[259],sourcePremisesConfirmed:confirmed,automaticPlanCoordinates:null,rectangleCentroidEquivalenceEstablished:false,modernArchitecturalTermEquivalenceEstablished:false,hallTermGlyphQualification:manual.records.find(r=>r.id==='anchor').readingQualification,...bounds()};
}
export function sourceYearOfficerRepairWindow(x){
 checked(x,'window',['timeBasis','operation','afterDahanFiveDays','pastLichunTwoDays','currentDirectionHarmful'],['afterDahanFiveDays','pastLichunTwoDays','currentDirectionHarmful']);
 if(!['declared-source-relative-days','civil-inclusive','civil-exclusive','elapsed-hours','unknown'].includes(x.timeBasis)||!['directional-repair','new-build','other','unknown'].includes(x.operation))throw TypeError('Explicit source interval frame/operation required.');
 let inside=null,avoid=null,status='premises-unresolved';
 if(x.timeBasis!=='declared-source-relative-days')status='relative-day-counting-unestablished';
 else if(x.operation!=='directional-repair')status='operation-not-addressed';
 else if(x.afterDahanFiveDays===false&&x.pastLichunTwoDays===true)status='inconsistent-relative-premises';
 else if(x.pastLichunTwoDays===true){inside=false;avoid=x.currentDirectionHarmful;status=avoid===true?'after-window-direction-veto':avoid===false?'after-window-no-harm-local-exception':'after-window-occupation-unresolved';}
 else if(x.afterDahanFiveDays===false){inside=false;status='before-selected-window-not-addressed';}
 else if(x.afterDahanFiveDays===true&&x.pastLichunTwoDays===false){inside=true;avoid=false;status='declared-local-repair-window';}
 return{system:SYSTEMS.window,input:{...x},sourceWindowApplies:inside,sourceLocalAvoidance:avoid,status,exactFifthDayBoundaryResolved:false,exactSecondDayBoundaryResolved:false,sourcePositions:[265],...bounds()};
}
