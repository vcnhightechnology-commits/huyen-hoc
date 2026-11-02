// Explicit named source tables only. No modern date, direction or placement inference.
const groups=Object.freeze({
 'xieji-regular':Object.freeze({'水':'亥壬子癸','木':'寅甲卯乙巽','火':'巳丙午丁','金':'申庚酉辛乾','土':'辰未戌丑坤艮'}),
 'xieji-hongfan':Object.freeze({'水':'甲寅辰巽戌坎辛申','火':'離壬丙乙','木':'震艮巳','金':'乾亥兌丁','土':'丑癸坤庚未'})
});
export function mountainElement({system,mountain}={}){
 if(!Object.hasOwn(groups,system))throw new TypeError('Explicit named table required');
 if(mountain===null)return {system,mountain,element:null,practicalOutcome:null};
 if(typeof mountain!=='string'||[...mountain].length!==1)throw new TypeError('Single known mountain required');
 const row=Object.entries(groups[system]).find(([,v])=>v.includes(mountain));
 if(!row)throw new TypeError('Unknown coordinate for this table');
 return {system,mountain,element:row[0],sourcePage:system==='xieji-regular'?10:18,practicalOutcome:null};
}
const life=Object.freeze(['子癸','丑艮','寅甲','卯乙','辰巽','巳丙','午丁','未坤','申庚','酉辛','戌乾','亥壬']);
export function zhaijingMonthlyCoordinates({witness,sourceMonthNumber}={}){
 if(witness!=='WYG-retained-transcription')throw new TypeError('Only explicitly named retained WYG transcription supported');
 if(sourceMonthNumber===null)return {witness,sourceMonthNumber,lifeCoordinates:null,deathCoordinates:null,calendarBoundary:null,leapMonthRule:null,practicalOutcome:null};
 if(!Number.isInteger(sourceMonthNumber)||sourceMonthNumber<1||sourceMonthNumber>12)throw new TypeError('Explicit source month number1–12 required; no Gregorian adapter');
 return {witness,sourceMonthNumber,lifeCoordinates:[...life[sourceMonthNumber-1]],deathCoordinates:[...life[(sourceMonthNumber+5)%12]],
  sourceTerm:'月生氣/死氣',sourceTier:'digital-transcription-only, not facsimilecollated',calendarBoundary:null,leapMonthRule:null,practicalOutcome:null};
}
