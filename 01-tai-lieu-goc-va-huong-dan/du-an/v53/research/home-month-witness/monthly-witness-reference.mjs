import {readFileSync,existsSync}from'node:fs';
import{resolve}from'node:path';
import{pathToFileURL}from'node:url';
const b=import.meta.dirname,workspace=[resolve(b,'../..'),resolve(b,'../../..')].find(p=>existsSync(resolve(p,'v53/research/home-month-gods/source-month-gods.mjs')));
if(!workspace)throw Error('Expected retained source project.');
const {sourceMonthGod}=await import(pathToFileURL(resolve(workspace,'v53/research/home-month-gods/source-month-gods.mjs')));
const manual=JSON.parse(readFileSync(new URL('./MANUAL_WITNESS_TABLE.json',import.meta.url),'utf8'));
export const MONTH_COMPARISON_SYSTEM='P08-vs-ITKC-GO1508A.literal-only.v1';
const stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'],gua=[...'乾坤艮巽坎離震兌'];
const type=x=>x===null?null:x==='中'?'centre':stems.includes(x)?'stem':branches.includes(x)?'branch':gua.includes(x)?'trigram':'direction';
// A literal concordance of two explicitly named witnesses; never a preferred-source selector.
export function compareMonthGodWitnesses(input){
 const keys=['system','god','monthOrdinal','monthBasis'];
 if(!input||Object.getPrototypeOf(input)!==Object.prototype||Reflect.ownKeys(input).length!==keys.length||keys.some(k=>!Object.hasOwn(input,k)))throw TypeError('Exact named source-comparison frame required.');
 if(input.system!==MONTH_COMPARISON_SYSTEM)throw TypeError('Explicit source-comparison system required.');
 const row=manual.records.find(x=>x.id===input.god);if(!row)throw TypeError('Named god row required.');
 if(input.monthOrdinal!==null&&(!Number.isInteger(input.monthOrdinal)||input.monthOrdinal<1||input.monthOrdinal>12))throw TypeError('Explicit source month1..12 or null required.');
 if(!['declared-source-ordinal','calendar-date','birth-year','door-direction','unknown'].includes(input.monthBasis))throw TypeError('Explicit month basis required.');
 const p08IDs={'tian-dao':'tian-dao','tian-de':'tian-de','yue-de':'month-de','tian-de-he':'tian-de-he','yue-de-he':'month-de-he','yue-kong':'month-void','yue-cai':'month-wealth'};
 const left=structuredClone(sourceMonthGod({system:'Tianyige-P08-juan3-month-direction-seven-gods',god:p08IDs[row.id],monthOrdinal:input.monthOrdinal,monthBasis:input.monthBasis}));
 const cell=input.monthBasis==='declared-source-ordinal'&&input.monthOrdinal!==null?row.cells[input.monthOrdinal-1]:null;
 const right={system:manual.system,god:row.id,sourceTitle:row.title,sourceImage:row.sourceImage,monthOrdinal:input.monthOrdinal,monthBasis:input.monthBasis,literal:cell?.literal??null,resolved:!!cell,coordinateType:type(cell?.literal??null),sourceMonthBoundaryEstablished:false};
 return{system:MONTH_COMPARISON_SYSTEM,left,right,status:!left.resolved||!right.resolved?'not-comparable':left.literal===right.literal?'same-literal':'different-literal',comparisonLevel:'literal-coordinates-only',preferredWitness:null,automaticEmendation:null,calendarMonthAdapter:null,trigramBranchReplacement:null,centreStemReplacement:null,exactBearingAssignment:null,overallRecommendation:null,wholeDateSelectionMethodImplemented:false,consumerApplied:false};
}
