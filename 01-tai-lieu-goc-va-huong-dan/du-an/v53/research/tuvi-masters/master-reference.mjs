// Private named-source label lookup. Caller supplies a source branch;
// no birth-year/day/palace anchor is silently chosen here.
import{readFileSync}from'node:fs';
const table=JSON.parse(readFileSync(new URL('SOURCE_TABLES.json',import.meta.url),'utf8')),branches=[...'子丑寅卯辰巳午未申酉戌亥'];
export function masterLabel({system,kind,sourceBranch}={}){
 if(system!==table.system)throw TypeError('Explicit named source table required');
 if(!['ming-master','body-master'].includes(kind))throw TypeError('Explicit source master kind required');
 if(sourceBranch!==null&&!branches.includes(sourceBranch))throw TypeError('Explicit source branch or null required');
 const row=table.rows.find(x=>x.kind===kind&&x.branch===sourceBranch);
 return{system,kind,sourceBranch,sourceCoordinateKnown:sourceBranch===null?null:true,
  sourceNameLiteral:row?.sourceNameLiteral??null,sourceSingleStarResolved:row?row.sourceSingleStarResolved:null,
  sourceStarName:row?.canonicalSimplifiedStar??null,vietnameseStar:row?.vietnameseStar??null,
  editorialParseCandidates:row?.editorialParseCandidates?[...row.editorialParseCandidates]:[],
  parseCaveat:row?.parseCaveat??null,sourceCanvas:row?.sourceCanvas??null,
  sourceBranchAdapterInferred:false,bodyBirthYearAnchorExplicitlyAttested:kind==='body-master'?false:null,
  practicalOutcome:null,starStrength:null};
}
