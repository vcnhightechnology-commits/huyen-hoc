import fs from 'node:fs';
const table=JSON.parse(fs.readFileSync(new URL('MANUAL_COORDINATES.json',import.meta.url),'utf8'));
export const SYSTEM=table.system;
const branches=[...'子丑寅卯辰巳午未申酉戌亥'];
export function sourceBirthDeathCoordinate(o){
 if(!o||Object.getPrototypeOf(o)!==Object.prototype||Reflect.ownKeys(o).length!==3||
  !['system','stem','branch'].every(k=>Object.hasOwn(o,k))||o.system!==SYSTEM)return null;
 const row=table.rows.find(r=>r.stem===o.stem);if(!row||!branches.includes(o.branch))return null;
 const marker=o.branch===row.sourceBirthBranch?'生':o.branch===row.sourceDeathBranch?'死':null;
 return {system:SYSTEM,stem:o.stem,branch:o.branch,sourceMarker:marker,
  evidenceStatus:marker?'explicitly-listed':'not-enumerated-in-selected-clauses',
  // 己's sentence crosses 19→20; retain the frozen table and disclose the
  // additional preceding-page evidence in EVIDENCE_SUPPLEMENT.json.
  sourcePages:row.stem==='己'?[19,20]:[...row.sourcePages],sourceVoice:row.voice,
  otherTenStagesInferred:false,alternativeEarthStartsMerged:false,
  actualNatalPhase:null,natalStrength:null,healthOutcome:null,lifespan:null,
  practicalOutcome:null,consumerApplied:false,wholeChapterApplied:false};
}
