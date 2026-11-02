import {readFileSync}from'node:fs';
const manual=JSON.parse(readFileSync(new URL('./MANUAL_CLAUSES.json',import.meta.url),'utf8')),examples=JSON.parse(readFileSync(new URL('./PRINTED_SITE_EXAMPLES.json',import.meta.url),'utf8'));
export const REPAIR_SYSTEM=manual.system,EXAMPLE_SYSTEM=examples.system;
const exact=(x,keys)=>{if(!x||Object.getPrototypeOf(x)!==Object.prototype||Reflect.ownKeys(x).length!==keys.length||keys.some(k=>!Object.hasOwn(x,k)))throw TypeError('Exact explicit source-premise fields required.');};
const tri=x=>x===true||x===false||x===null,and=xs=>xs.includes(false)?false:xs.includes(null)?null:true;
const clause=id=>{const r=manual.records.find(x=>x.id===id);if(!r)throw TypeError('Named source clause required.');return r;};
const bases=['declared-source-month','numeric-lunar-month','solar-term-month','unknown'];
// Local textual operation scope; dates, source positions and efficacy are not inferred.
export function sourceLocalRepairScope(input){
 exact(input,['system','clause','monthBasis','operation','occupiedSiteMatch','tugongBaiDayException','earthworkIncluded']);
 if(input.system!==REPAIR_SYSTEM)throw TypeError('Named local repair system required.');
 const row=clause(input.clause);
 if(!bases.includes(input.monthBasis)||!['repair-existing','new-build','other','unknown'].includes(input.operation)||![input.occupiedSiteMatch,input.tugongBaiDayException,input.earthworkIncluded].every(tri))throw TypeError('Explicit source operation/month and boolean-or-null premises required.');
 if(!row.hasTugongBaiDayException&&(input.tugongBaiDayException!==null||input.earthworkIncluded!==null))throw TypeError('This clause has no such exception premise.');
 if(input.clause==='tugong'&&input.earthworkIncluded!==null)throw TypeError('Tugong paragraph does not add an earthwork condition to its exception.');
 let localAvoidance=null,status='premises-unresolved',exception=null;
 const frame=input.monthBasis==='declared-source-month';
 if(frame){
  if(input.operation==='new-build'&&row.newBuildExplicitException){localAvoidance=false;status='explicit-new-build-exception';}
  else if(input.operation!=='repair-existing'){status=input.operation==='unknown'?'premises-unresolved':'operation-not-addressed';}
  else if(input.occupiedSiteMatch===false){localAvoidance=false;status='outside-declared-affected-site';}
  else{
   exception=row.hasTugongBaiDayException?(input.clause==='youlong-fulong'?and([input.tugongBaiDayException,input.earthworkIncluded]):input.tugongBaiDayException):false;
   const restriction=and([input.occupiedSiteMatch,exception===null?null:!exception]);
   localAvoidance=restriction;
   status=restriction===true?'stated-local-repair-avoidance':restriction===false?'stated-local-exception':'premises-unresolved';
  }
 }
 return{system:REPAIR_SYSTEM,clause:row.id,parentContext:row.parent,sourceTitle:row.title,input:{...input},sourceMonthFrameEstablished:frame,sourceCalendarClaim:row.calendarClaim,localAvoidance,status,declaredExceptionApplies:exception,sourcePositions:row.sourcePositions.slice(),onlyThisLocalPredicateEvaluated:true,affectedLocationDerived:false,calendarDateAdapterImplemented:false,calendarMonthTimestampBoundary:null,leapMonthPolicy:null,globalNoJieqiPolicy:null,overallDateRecommendation:null,sourceOutcome:null,wholeSourceMethodApplied:false,consumerApplied:false};
}
export function sourcePrintedMonthlySite(input){
 exact(input,['system','clause','yearGanzhi','monthOrdinal','monthBasis']);
 if(input.system!==EXAMPLE_SYSTEM)throw TypeError('Explicit printed-example system required.');clause(input.clause);
 const stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'],cycle=Array.from({length:60},(_,i)=>stems[i%10]+branches[i%12]);
 if(input.yearGanzhi!==null&&!cycle.includes(input.yearGanzhi))throw TypeError('Canonical year or null required.');
 if(input.monthOrdinal!==null&&(!Number.isInteger(input.monthOrdinal)||input.monthOrdinal<1||input.monthOrdinal>12)||!bases.includes(input.monthBasis))throw TypeError('Canonical source month and explicit basis required.');
 const row=input.monthBasis==='declared-source-month'?examples.records.find(x=>x.clause===input.clause&&x.monthOrdinal===input.monthOrdinal&&(x.yearGanzhi===null||x.yearGanzhi===input.yearGanzhi)):null;
 return{system:EXAMPLE_SYSTEM,clause:input.clause,yearGanzhi:input.yearGanzhi,monthOrdinal:input.monthOrdinal,monthBasis:input.monthBasis,sourceExampleID:row?.id??null,sourceListedSite:row?.site??null,sourceSpecifiedYear:row?.yearGanzhi??null,yearNotStatedInSourceExample:row?row.yearGanzhi===null:null,printedExampleOnly:true,unlistedLocationsAreUnknownNotAbsent:true,allYearTableEstablished:false,fullTwelveMonthTableImplemented:false,modernRoomGeometryMapped:false,calendarAdapterImplemented:false,overallRecommendation:null,sourceOutcome:null,consumerApplied:false};
}
