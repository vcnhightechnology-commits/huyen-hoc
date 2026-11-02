import{readFileSync}from'node:fs';
const systemName='NAJ-4468520-juan3-printed-five-cuc-day-ziwei';
const data=JSON.parse(readFileSync(new URL('./ZIWEI_DAY_DIAGRAMS.json',import.meta.url),'utf8'));
export function sourceZiweiAnchor({system,cucNumber,lunarDay}={}){
 if(system!==systemName)throw new TypeError('Explicit named source required');
 if(cucNumber!==null&&![2,3,4,5,6].includes(cucNumber))throw new TypeError('Declared cục2..6 or explicit null required');
 if(lunarDay!==null&&(!Number.isInteger(lunarDay)||lunarDay<1||lunarDay>30))throw new TypeError('Declared lunar day1..30 or explicit null required');
 const row=cucNumber===null?null:data.records.find(x=>x.cucNumber===cucNumber),cell=row&&lunarDay!==null?row.cells.find(x=>x.dayNumeralsNormalized.includes(lunarDay)):null;
 return{system,cucNumber,lunarDay,resolved:!!cell,star:'紫微',branch:cell?.branch??null,sourceCanvas:row?.canvas??null,sourceSide:row?.side??null,resolutionBasis:cell?'printed-day-diagram':'missing-declared-cuc-or-day',cucAssignmentImplemented:false,calendarConversionImplemented:false,otherStarsImplemented:false,strengthOrOutcomeInferred:false,practicalOutcome:null};
}
