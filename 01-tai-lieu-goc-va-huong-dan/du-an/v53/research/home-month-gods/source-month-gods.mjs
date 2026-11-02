import{readFileSync}from'node:fs';
const name='Tianyige-P08-juan3-month-direction-seven-gods',data=JSON.parse(readFileSync(new URL('./MANUAL_MONTH_GOD_TABLES.json',import.meta.url),'utf8'));
const stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'],trigrams=[...'乾坤艮巽坎離震兌'];
export function sourceMonthGod({system,god,monthOrdinal,monthBasis}={}){
 if(system!==name)throw new TypeError('Explicit named source required');
 const row=data.records.find(x=>x.id===god);if(!row)throw new TypeError('Named god row required');
 if(monthOrdinal!==null&&(!Number.isInteger(monthOrdinal)||monthOrdinal<1||monthOrdinal>12))throw new TypeError('Source month1..12 or explicit null required');
 if(!['declared-source-ordinal','calendar-date','birth-year','door-direction','unknown'].includes(monthBasis))throw new TypeError('Declared month basis required');
 const applicable=monthBasis==='declared-source-ordinal'&&monthOrdinal!==null,cell=applicable?row.cells[monthOrdinal-1]:null,literal=cell?.literal??null;
 const coordinateType=literal===null?null:row.coordinateDomain==='cardinal-or-intercardinal-direction'?'direction':stems.includes(literal)?'stem':branches.includes(literal)?'branch':trigrams.includes(literal)?'trigram':null;
 return{system,god,sourceTitle:row.title,monthOrdinal,monthBasis,resolved:literal!==null,literal,coordinateType,sourcePDFPage:146,sourceSide:'left',resolutionBasis:!applicable?'source-month-not-established':literal===null?'source-glyph-unresolved':'direct-source-table-cell',unresolvedCandidates:cell?.unresolvedCandidates??[],calendarMonthAdapterImplemented:false,leapMonthPolicyEstablished:false,trigramToBranchAdapterImplemented:false,stemCombinationEfficacyEstablished:false,wholeDateSelectionMethodImplemented:false,practicalOutcome:null};
}
