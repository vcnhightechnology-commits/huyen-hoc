/** Internal source coordinate premises; never sufficient effective transformation. */
import{readFileSync}from'node:fs';
const data=JSON.parse(readFileSync(new URL('./MANUAL_TABLES.json',import.meta.url),'utf8'));
const own=(o,k)=>Object.prototype.hasOwnProperty.call(o,k),branches=[...'子丑寅卯辰巳午未申酉戌亥'],stems=[...'甲乙丙丁戊己庚辛壬癸'];
export const SOURCE_ID=data.sourceID;
export const FRAME_ID=data.frameID;
export function sourceTriadPremises(o){
 const required=['sourceID','frameID','groupID','slots','anchorStem','anchorBasis'];
 if(o===null||typeof o!=='object'||Array.isArray(o)||![Object.prototype,null].includes(Object.getPrototypeOf(o))||
 !required.every(k=>own(o,k))||Reflect.ownKeys(o).some(k=>!required.includes(k))||o.sourceID!==SOURCE_ID||o.frameID!==FRAME_ID||o.anchorBasis!==data.stemRoleAnchorBasis)return null;
 const group=data.groups.find(g=>g.id===o.groupID);if(!group)return null;
 if(!Array.isArray(o.slots)||o.slots.length!==4||o.slots.some((v,i)=>!own(o.slots,i)||v!==null&&!branches.includes(v))||[0,1,2,3].some(i=>!own(o.slots,i)))throw new TypeError('Four explicit source branch slots, each a branch or null, required');
 if(!stems.includes(o.anchorStem))throw new RangeError('anchorStem');
 const unseen=group.branches.filter(branch=>!o.slots.includes(branch)),unknown=o.slots.filter(v=>v===null).length;
 const complete=unseen.length===0?true:unseen.length>unknown?false:null;
 const lu=data.threeLuClauses.find(r=>r.anchorStem===o.anchorStem&&r.groupID===group.id);
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,groupID:group.id,sourceElementLabel:group.element,
  requiredBranches:Object.freeze([...group.branches]),sourceCompletenessPremise:complete,
  missingThreeBranchExclusion:group.threeBranchGroup?(complete===null?null:!complete):null,
  sourceRoleLabel:data.stemRoleScope.includes(o.anchorStem)&&complete===true?group.sourceRoleForBingDing:null,
  sourceThreeLuCoordinateGate:lu?complete:null,sourceLuBranch:lu?.luBranch??null,
  anchorPillar:null,appliedToNatalChart:false,effectiveFormation:null,transformedElement:null,
  wholePatternEstablished:null,natalOutcome:null,calendarDate:null,strength:null,interSourcePriority:null,
  sourceEfficacyValidated:false});
}
