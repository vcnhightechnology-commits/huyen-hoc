/** Internal source-local reading. Caller-declared premises have no calendar adapter.
 * A local 不避 clause never supplies overall permission or an empirical outcome.
 */
import { readFileSync } from 'node:fs';
const manual=JSON.parse(readFileSync(new URL('./MANUAL_CONDITIONS.json',import.meta.url),'utf8'));
function freeze(o){if(o&&typeof o==='object'){for(const value of Object.values(o))freeze(value);Object.freeze(o);}return o;}
const records=freeze(manual.records);
export const SOURCE_ID=manual.sourceID;
export const FRAME_ID=manual.frameID;
const schemas=freeze({
 'forest-mountain-timber':{qualification:'beneficPresent',markers:['forest-ge','mountain-ge'],activity:'enter-mountain-to-cut-timber'},
 'sacrifice-shen-present':{qualification:'shenPresentDay',markers:['shen-ge'],activity:'sacrificial-rite'}
});
const own=(o,k)=>Object.prototype.hasOwnProperty.call(o,k);
export function lookupGeCondition(id){return typeof id==='string'?records.find(r=>r.id===id)??null:null;}
function tri(value,key){if(value!==true&&value!==false&&value!==null)throw new TypeError(key+' must be true, false or null');}
export function sourceGeException(o){
 if(o===null||typeof o!=='object'||Array.isArray(o)||![Object.prototype,null].includes(Object.getPrototypeOf(o)))return null;
 if(!own(o,'sourceID')||o.sourceID!==SOURCE_ID||!own(o,'frameID')||o.frameID!==FRAME_ID||!own(o,'clauseID')||!own(schemas,o.clauseID))return null;
 const schema=schemas[o.clauseID];
 const required=['sourceID','frameID','clauseID','marker','activity','markerStatus',schema.qualification];
 if(required.some(k=>!own(o,k))||Reflect.ownKeys(o).some(k=>!required.includes(k)))return null;
 if(!schema.markers.includes(o.marker))throw new RangeError('marker outside named clause');
 if(typeof o.activity!=='string'||o.activity.length===0)throw new TypeError('activity must be a nonempty source activity identifier');
 tri(o.markerStatus,'markerStatus');tri(o[schema.qualification],schema.qualification);
 let reason='source-marker-not-established';
 let localAvoidance=null;
 if(o.markerStatus===true){
  if(o.activity!==schema.activity)reason='activity-not-covered-by-selected-short-clause';
  else if(o[schema.qualification]!==true)reason='qualifying-premise-not-established-no-converse';
  else {localAvoidance=false;reason='explicit-source-local-exception-under-declared-premises';}
 }
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,clauseID:o.clauseID,marker:o.marker,
  activity:o.activity,localAvoidance,explicitLocalException:localAvoidance===false,reason,
  overallSuitability:null,permissionToAct:null,harmPrediction:null,calendarDate:null,
  interClausePriority:null,sourceEfficacyValidated:false});
}
