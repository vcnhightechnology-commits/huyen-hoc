export const ROOM_LINE_SYSTEM='YZSS-Tianyige-room-last-five-declared-order';
const yang=[...'乾坎艮震'],yin=[...'巽離坤兌'],labels=[...yang,...yin];
const plain=x=>!!x&&Object.getPrototypeOf(x)===Object.prototype&&Reflect.ownKeys(x).every(k=>typeof k==='string');
function exact(x,keys){if(!plain(x)||Reflect.ownKeys(x).length!==keys.length||keys.some(k=>!Object.hasOwn(x,k)))throw TypeError('Exact explicit source inputs required.');}
const tri=x=>x===null?null:yang.includes(x)?1:0;
const room=x=>x==='unknown'?null:['east','north'].includes(x)?1:0;
export function sourceCarryPair(input){
 exact(input,['system','originLabel','destinationLabel']);
 if(input.system!==ROOM_LINE_SYSTEM||![input.originLabel,input.destinationLabel].every(x=>x===null||labels.includes(x)))throw TypeError('Canonical source trigram labels or null required.');
 return {system:input.system,carriedPair:[tri(input.originLabel),tri(input.destinationLabel)],
  sequence:'origin-then-destination',sourcePDFPage:94,positionsAfterGateInsertion:null,
  automaticGateComplement:null,completeHouseMethod:false,consumerApplied:false};
}
export function sourceLastFiveRoomLines(input){
 exact(input,['system','frame','tailComplete','sourceOrderEstablished','distinctSourceUnitsEstablished','gateLine','units']);
 if(input.system!==ROOM_LINE_SYSTEM||!['declared-source-counted-room-units','modern-vertical-storeys','area-weighted','unknown'].includes(input.frame)||
  ![input.tailComplete,input.sourceOrderEstablished,input.distinctSourceUnitsEstablished].every(x=>x===true||x===false||x===null)||
  ![0,1,null].includes(input.gateLine)||!Array.isArray(input.units))throw TypeError('Named frame, explicit premises, gate bit/null and source units required.');
 const ids=new Set();
 for(const x of Array.from(input.units)){
  exact(x,['id','sourceSide','workKind']);
  if(typeof x.id!=='string'||!x.id.trim()||ids.has(x.id)||!['east','north','west','south','unknown'].includes(x.sourceSide)||!['new','repair','unknown'].includes(x.workKind))throw TypeError('Unique declared source-unit IDs, explicit cardinal source side and work kind required.');
  ids.add(x.id);
 }
 const selected=input.units.slice(-5),enough=selected.length===5;
 const ready=enough&&input.frame==='declared-source-counted-room-units'&&input.tailComplete===true&&input.sourceOrderEstablished===true&&input.distinctSourceUnitsEstablished===true&&selected.every(x=>x.workKind!=='unknown');
 const upper=ready?selected.map(x=>room(x.sourceSide)):null;
 const lines=upper===null?null:[input.gateLine,...upper];
 return {system:input.system,sourcePDFPages:[94,95],selectedSourceUnitIDs:selected.map(x=>x.id),
  omittedEarlierUnitIDs:input.units.slice(0,Math.max(0,input.units.length-5)).map(x=>x.id),
  enoughDeclaredSourceUnits:enough,sourcePremisesReady:ready,upperFiveLines:upper,
  linesBottomToTop:lines,sixBitsKnown:lines!==null&&lines.every(x=>x!==null),
  orderedSourceUnitsMappedToUpperLinesIsExplicitEditorialModel:true,
  gateLineSuppliedNotInferred:input.gateLine,automaticGateComplement:null,
  initialPhaseWithFewerThanFiveRoomsImplemented:false,
  repeatedPhysicalRoomOrMultipleRepairCountingAutomaticallyEstablished:false,
  modernMeasuredPlanAdapter:null,sourceExchangeMethodCompleted:false,
  healthPrediction:null,wealthPrediction:null,practicalOutcome:null,consumerApplied:false};
}
