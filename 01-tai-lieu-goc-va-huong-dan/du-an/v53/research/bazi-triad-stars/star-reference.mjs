/** Internal coordinate definitions and the explicit 咸池 preface qualification only. */
import{readFileSync}from'node:fs';
const manual=JSON.parse(readFileSync(new URL('./MANUAL_COORDINATES.json',import.meta.url),'utf8'));
const branches=[...'子丑寅卯辰巳午未申酉戌亥'],stars=['general','canopy','xianchi'];
const own=(o,k)=>Object.prototype.hasOwnProperty.call(o,k);
export const SOURCE_ID=manual.sourceID;
export const FRAME_ID=manual.frameID;
export function sourceStarCoordinate(o){
 if(o===null||typeof o!=='object'||Array.isArray(o)||![Object.prototype,null].includes(Object.getPrototypeOf(o)))return null;
 const base=['sourceID','frameID','groupID','star','sourceAnchorBranch','targetBranch','anchorBasis'];
 if(!base.every(k=>own(o,k))||o.sourceID!==SOURCE_ID||o.frameID!==FRAME_ID||o.anchorBasis!=='source-declared-anchor-branch'||!stars.includes(o.star))return null;
 const row=manual.rows.find(r=>r.groupID===o.groupID);if(!row)return null;
 const keys=o.star==='xianchi'?[...base,'naYinGroupMatch']:base;
 if(!keys.every(k=>own(o,k))||Reflect.ownKeys(o).some(k=>!keys.includes(k)))return null;
 for(const key of['sourceAnchorBranch','targetBranch'])if(o[key]!==null&&!branches.includes(o[key]))throw new RangeError(key);
 if(o.star==='xianchi'&&![true,false,null].includes(o.naYinGroupMatch))throw new TypeError('naYinGroupMatch');
 const coordinate=o.sourceAnchorBranch!==null&&!row.branches.includes(o.sourceAnchorBranch)||o.targetBranch!==null&&o.targetBranch!==row[o.star]?false:
  o.sourceAnchorBranch===null||o.targetBranch===null?null:true;
 const gate=o.star==='xianchi'?(coordinate===false||o.naYinGroupMatch===false?false:coordinate===true&&o.naYinGroupMatch===true?true:null):coordinate;
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,star:o.star,groupID:row.groupID,
  sourceAnchorBranch:o.sourceAnchorBranch,targetBranch:o.targetBranch,listedTargetBranch:row[o.star],
  groupElement:row.groupElement,rawCoordinateMatches:coordinate,sourceSelectedCoordinateGate:gate,
  qualificationScope:o.star==='xianchi'?'declared-nayin-same-kind-preface-only':'middle-or-store-definition-only',
  naYinSourcePillar:null,anchorPillar:null,requiresFullTriadFormed:null,fullTriadFormationEvaluated:false,remainingSourceConditionsOpen:true,
  effectiveStar:null,wholePatternEstablished:null,natalOutcome:null,calendarDate:null,strength:null,
  interSourcePriority:null,medicalRisk:null,sourceEfficacyValidated:false,appliedToNatalChart:false});
}
