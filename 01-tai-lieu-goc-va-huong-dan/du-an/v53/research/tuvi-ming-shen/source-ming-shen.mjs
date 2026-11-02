const systemName='NAJ-4468520-juan3-declared-month-hour-ming-shen',branches=[...'子丑寅卯辰巳午未申酉戌亥'];
export function sourceMingShen({system,monthOrdinal,hourBranch,leapMonth}={}){
 if(system!==systemName)throw new TypeError('Named source required');
 if(monthOrdinal!==null&&(!Number.isInteger(monthOrdinal)||monthOrdinal<1||monthOrdinal>12))throw new TypeError('Declared lunar month1..12 or explicit null required');
 if(hourBranch!==null&&!branches.includes(hourBranch))throw new TypeError('Declared canonical hour branch or explicit null required');
 if(![true,false,null].includes(leapMonth))throw new TypeError('Explicit leap flag or null required');
 const known=monthOrdinal!==null&&hourBranch!==null,printedLeapExample=leapMonth===true&&monthOrdinal===1&&hourBranch==='寅';
 const applicable=known&&(leapMonth===false||printedLeapExample),h=known?branches.indexOf(hourBranch):null,monthAnchor=monthOrdinal===null?null:(monthOrdinal+1)%12;
 const ming=applicable?(monthAnchor-h+12)%12:null,shen=applicable?(monthAnchor+h)%12:null;
 return{system,monthOrdinal,hourBranch,leapMonth,sourceMonthAnchor:monthAnchor===null?null:branches[monthAnchor],mingBranch:ming===null?null:branches[ming],shenBranch:shen===null?null:branches[shen],
  resolved:applicable,resolutionBasis:!known?'missing-month-or-hour':leapMonth===null?'leap-status-unknown':leapMonth===true?(printedLeapExample?'printed-leap-month1-hourYin-example':'general-leap-policy-unresolved'):'printed-regular-month-hour-rule',
  sourceGeneralLeapPolicyResolved:false,clockToHourBranchAdapterImplemented:false,calendarConversionImplemented:false,sourceOutcomesValidated:false,practicalOutcome:null};
}
