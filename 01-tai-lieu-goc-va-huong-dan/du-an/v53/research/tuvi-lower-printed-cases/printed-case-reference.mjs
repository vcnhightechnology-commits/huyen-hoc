// Private printed-coordinate comparison. Never a biographical or predictive verifier.
import{readFileSync}from'node:fs';
const table=JSON.parse(readFileSync(new URL('MANUAL_PRINTED_CASES.json',import.meta.url),'utf8'));
export const PRINTED_CASE_SOURCE=table.system;
const branches=[...'子丑寅卯辰巳午未申酉戌亥'],plain=x=>x!==null&&typeof x==='object'&&Object.getPrototypeOf(x)===Object.prototype;
export function printedCase(input){
 if(!plain(input)||Reflect.ownKeys(input).length!==2||!Object.hasOwn(input,'system')||!Object.hasOwn(input,'caseID')||input.system!==table.system)throw TypeError('Exact named source/case required.');
 const row=table.records.find(x=>x.id===input.caseID);if(!row)throw TypeError('Unknown printed case.');
 return structuredClone(row);
}
export function comparePrintedCase(input){
 const keys=['system','caseID','projection'];if(!plain(input)||Reflect.ownKeys(input).length!==3||keys.some(k=>!Object.hasOwn(input,k)))throw TypeError('Explicit case and projection required.');
 const row=printedCase({system:input.system,caseID:input.caseID}),p=input.projection;
 if(!plain(p)||Reflect.ownKeys(p).length!==4||['mingBranch','cucNumber','majorBranches','transformationBranches'].some(k=>!Object.hasOwn(p,k))||!plain(p.majorBranches)||!plain(p.transformationBranches))throw TypeError('Four declared coordinate fields required.');
 if(p.mingBranch!==null&&!branches.includes(p.mingBranch)||p.cucNumber!==null&&![2,3,4,5,6].includes(p.cucNumber))throw TypeError('Canonical Ming/cuc or null required.');
 const stars=Object.keys(row.majorBranches),kinds=['祿','權','科','忌'];
 for(const [obj,allowed]of[[p.majorBranches,stars],[p.transformationBranches,kinds]])for(const k of Reflect.ownKeys(obj))if(!allowed.includes(k)||obj[k]!==null&&!branches.includes(obj[k]))throw TypeError('Declared source star/kind and branch or null only.');
 const coordinates=[{id:'ming',source:row.mingBranch,actual:p.mingBranch},{id:'cuc',source:row.sourceCucNumber,actual:p.cucNumber},...stars.map(star=>({id:'major:'+star,source:row.majorBranches[star],actual:p.majorBranches[star]??null})),...row.transformationLabels.map(x=>({id:'transform:'+x.kind,source:x.branch,actual:p.transformationBranches[x.kind]??null,sourceStar:x.star}))].map(x=>({...x,status:x.source===null?'source-unresolved':x.actual===null?'projection-unknown':x.source===x.actual?'match':'mismatch'}));
 return{system:table.system,caseID:row.id,coordinates,comparedCoordinates:coordinates.filter(x=>['match','mismatch'].includes(x.status)).length,matches:coordinates.filter(x=>x.status==='match').length,mismatches:coordinates.filter(x=>x.status==='mismatch'),historicalBirthDateEstablished:false,sourcePredictionValidated:false,allMinorStarsCollated:false,wholeSourceApplied:false,practicalOutcome:null,consumerApplied:false};
}
