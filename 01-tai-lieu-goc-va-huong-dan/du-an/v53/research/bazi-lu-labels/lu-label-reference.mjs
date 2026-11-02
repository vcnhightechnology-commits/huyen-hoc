// Private lookup of explicitly printed labels, not a natal anchor or forecast.
import{readFileSync}from'node:fs';
const table=JSON.parse(readFileSync(new URL('SOURCE_ROWS.json',import.meta.url),'utf8'));
const storage=JSON.parse(readFileSync(new URL('LU_STORAGE_TABLE.json',import.meta.url),'utf8'));
const stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'];
const pillars=Array.from({length:60},(_,i)=>stems[i%10]+branches[i%12]);
function assertStem(stem){if(!stems.includes(stem))throw TypeError('Explicit single source stem required');}
export function luLabel({system,sourceStem,candidatePillar}={}){
 if(system!==table.system)throw TypeError('Explicit named source label table required');assertStem(sourceStem);
 if(candidatePillar!==null&&!pillars.includes(candidatePillar))throw TypeError('Explicit valid sexagenary pillar or null required');
 const row=table.rows.find(x=>x.sourceStem===sourceStem&&x.candidatePillar===candidatePillar);
 const lu=table.rows.find(x=>x.sourceStem===sourceStem).sourceLuBranch;
 return{system,sourceStem,candidatePillar,sourceLuBranch:lu,
  exactPairDocumented:candidatePillar===null?null:!!row,
  sourceLabels:row?[...row.sourceLabels]:null,rowSpecificSourceClause:row?row.rowSpecificSourceClause:null,
  sharedSourceClaims:row?row.sharedClaimIDs.map(id=>{const x=table.sharedClaims.find(t=>t.id===id);return structuredClone(x);}):null,
  sourcePages:row?[...row.sourcePages]:null,sourceStemAnchorField:null,
  modernTenGod:null,patternEstablished:null,strengthEstablished:null,practicalOutcome:null,isHistoricalSourceClaim:true};
}
export function luStorage({system,sourceStem,candidateBranch}={}){
 if(system!==storage.system)throw TypeError('Explicit named Lu storage system required');assertStem(sourceStem);
 if(candidateBranch!==null&&!branches.includes(candidateBranch))throw TypeError('Explicit single branch or null required');
 const sourceBranch=storage.sourceGroups.find(x=>x.stems.includes(sourceStem)).branch;
 return{system,sourceStem,candidateBranch,sourceBranch,coordinateMatched:candidateBranch===null?null:sourceBranch===candidateBranch,
  sourceConditionalExampleSatisfied:null,manyThresholdEstablished:false,ordinaryElementTombAlgorithm:false,
  sourceStemAnchorField:null,patternEstablished:null,practicalOutcome:null};
}
