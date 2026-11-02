// Private named-source coordinates. The caller supplies the stem explicitly;
// no birthday anchor, pattern establishment, strength or outcome is inferred.
import{readFileSync}from'node:fs';
const tables=JSON.parse(readFileSync(new URL('BLADE_TABLES.json',import.meta.url),'utf8')).tables;
const stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'];
export function bladeCoordinate({system,stem,candidateBranch}={}){
 const table=tables.find(x=>x.system===system);
 if(!table)throw TypeError('Explicit named-source table required');
 if(!stems.includes(stem))throw TypeError('Explicit single source stem required');
 if(candidateBranch!==null&&!branches.includes(candidateBranch))throw TypeError('Explicit single candidate branch or null required');
 const row=table.rows.find(x=>x.stem===stem),excluded=table.explicitlyExcludedStems.includes(stem);
 return{system,stem,candidateBranch,sourceBranch:row?.branch??null,
  coordinateStatus:row?'directly-stated':excluded?'explicitly-excluded':'not-stated-in-this-table',
  sourceScopeAllowsCoordinate:row?true:excluded?false:null,
  coordinateMatched:candidateBranch===null?null:row?row.branch===candidateBranch:excluded?false:null,
  evidenceTier:table.tier,patternEstablished:null,strengthEstablished:null,practicalOutcome:null,calendarAnchor:null};
}
