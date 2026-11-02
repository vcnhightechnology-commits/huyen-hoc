/** Internal literal activity scopes from ITKC選擇要略vol2.
 * Source markers/layout roles are caller-declared; no date/modern geometry adapter.
 * A local exception is never overall permission or a prediction.
 */
export const SOURCE_ID='itkc-1508A-vol2-daily-selected';
export const FRAME_ID='source-declared-day-and-symbolic-activity';
const baseKeys=['sourceID','frameID','clauseID','activity'];
const schema={
 'white-tiger':['kind','starPosition','locationRole'],
 'four-waste':['dayKind','beneficPresent'],
 'wantong-fire':['markerStatus','beneficPresent'],
 'tianhuo':['markerStatus','voice'],
 'received-death':['markerStatus','beneficPresent'],
 'tiange':['markerStatus','huangdaoQualified'],
 'renge':['markerStatus','marriageDayQualified'],
 'fire-ge':['markerStatus'],'water-ge':['markerStatus']
};
const own=(o,k)=>Object.prototype.hasOwnProperty.call(o,k);
function select(value,values,key) {if(!values.includes(value))throw new RangeError(key);}
function tri(value,key){select(value,[true,false,null],key);}
const result=(o,localAvoidance,reason)=>Object.freeze({
 sourceID:SOURCE_ID,clauseID:o.clauseID,activity:o.activity,localAvoidance,
 explicitLocalException:localAvoidance===false,reason,
 overallSuitability:null,permissionToBuild:null,harmPrediction:null,
 calendarDate:null,sourceEfficacyValidated:false
});
export function sourceActivityClause(o) {
 if(o===null||typeof o!=='object'||Array.isArray(o)||!own(o,'sourceID')||o.sourceID!==SOURCE_ID||
 !own(o,'frameID')||o.frameID!==FRAME_ID||!own(o,'clauseID')||!own(schema,o.clauseID))return null;
 const required=[...baseKeys,...schema[o.clauseID]];
 if(required.some(k=>!own(o,k))||Object.keys(o).some(k=>!required.includes(k)))return null;
 if(typeof o.activity!=='string'||o.activity.length===0)throw new TypeError('activity');
 const finish=(value,reason)=>result(o,value,reason);
 if(o.clauseID==='white-tiger') {
  select(o.kind,['dasha','leiting'],'kind');
  select(o.starPosition,['central-palace','other-palace','unknown'],'starPosition');
  select(o.locationRole,['hall-middle','hall-other','outside-hall','unknown'],'locationRole');
  if(o.starPosition!=='central-palace')return finish(null,'central-palace-premise-not-established');
  if(o.locationRole==='unknown')return finish(null,'symbolic-location-not-established');
  if(o.activity==='repair-hall') {
   const avoid=o.kind==='dasha'?o.locationRole==='hall-middle':o.locationRole!=='outside-hall';
   return finish(avoid,avoid?'named-repair-prohibition':'explicit-remaining-locations-exception');
  }
  if(o.activity==='music-or-noisy-guests'&&o.locationRole==='hall-middle')return finish(true,'separate-reported-noise-clause');
  return finish(null,'activity-or-noise-location-unadjudicated');
 }
 if(o.clauseID==='four-waste') {
  select(o.dayKind,['regular','lateral','unknown'],'dayKind');tri(o.beneficPresent,'beneficPresent');
  if(o.activity!=='start-building')return finish(null,'miscellaneous-activities-not-expanded');
  if(o.dayKind==='regular')return finish(true,'regular-four-waste-start-building');
  if(o.dayKind==='lateral'&&o.beneficPresent===true)return finish(false,'lateral-four-waste-with-benefic');
  return finish(null,'conditional-exception-not-established');
 }
 tri(o.markerStatus,'markerStatus');
 for(const k of ['beneficPresent','huangdaoQualified','marriageDayQualified'])if(own(o,k))tri(o[k],k);
 if(o.clauseID==='tianhuo')select(o.voice,['official-calendar','reported-other-almanacs'],'voice');
 if(o.markerStatus!==true)return finish(null,'source-day-marker-not-established');
 switch(o.clauseID) {
  case 'wantong-fire':
   return finish(['start-building','erect-pillars','make-fire-drying-kiln','build-thatch-hut'].includes(o.activity)?true:null,
    'four-named-activities-only-benefics-do-not-cancel');
  case 'tianhuo': {
   const acts=o.voice==='official-calendar'?['thatch-cover']:['cover-house','cover-hut','cover-boat'];
   return finish(acts.includes(o.activity)?true:null,'retain-reported-source-voice');
  }
  case 'received-death':
   if(['inherit-title','receive-investiture','take-office','submit-memorial'].includes(o.activity))return finish(true,'named-office-investiture-memorial-prohibition');
   if(o.activity==='burial')return finish(false,'explicit-burial-exception');
   return finish(null,'no-ritual-or-construction-override-implemented');
  case 'tiange':
   if(['travel','seek-office','submit-memorial','present-petition'].includes(o.activity)&&o.huangdaoQualified===true)return finish(false,'named-activity-with-huangdao-exception');
   return finish(null,'no-inferred-converse');
  case 'renge':
   if(['marry-wife','admit-household-member'].includes(o.activity)&&o.marriageDayQualified===true)return finish(false,'named-marriage-household-exception');
   return finish(null,'no-inferred-converse');
  default:return finish(null,'conjunction-and-inter-clause-priority-unresolved');
 }
}
