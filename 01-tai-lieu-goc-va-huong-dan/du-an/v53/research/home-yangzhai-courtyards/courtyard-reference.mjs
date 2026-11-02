import {readFileSync} from 'node:fs';
const data=JSON.parse(readFileSync(new URL('./MANUAL_DIAGRAM_CELLS.json',import.meta.url),'utf8'));
export const COURTYARD_SYSTEM='YZSS-Tianyige-12-printed-courtyards';
const dirs=[...'東西南北'],gates=[...'乾坎艮震巽離坤兌'];
function exact(v,values,name){if(!values.includes(v))throw new TypeError(`Explicit canonical ${name} required`);}
function system(v){exact(v,[COURTYARD_SYSTEM],'system');}
export function sourceCourtyardDiagram({system:named,caseID}){
 system(named);exact(caseID,data.records.map(x=>x.id),'caseID');
 return {system:named,diagram:structuredClone(data.records.find(x=>x.id===caseID)),
  numberingMeansPrintedOrderedLayers:true,modernVerticalFloorAdapter:null,sourceFirstRoomFacingOrCountOriginEstablished:false,
  fullProseConditionsApplied:false,practicalHeightAdvice:null,overallRecommendation:null,
  literalUnresolvedCells:caseID==='YZSS-C84'?[1,6]:[]};
}
export function sourceCourtyardCandidates({system:named,sitting,facing,gate}){
 system(named);exact(sitting,[...dirs,null],'sitting');exact(facing,[...dirs,null],'facing');exact(gate,[...gates,null],'gate');
 const records=data.records.filter(x=>(sitting===null||x.sourceSitting===sitting)&&(facing===null||x.sourceFacing===facing)&&(gate===null||x.sourceGate===gate));
 return {system:named,caseIDs:records.map(x=>x.id),selectorIsSourceLabelsOnly:true,unmatchedIsNotUnlucky:true,
  missingInputs:[sitting,facing,gate].some(x=>x===null),modernPlanMatched:null,overallRecommendation:null};
}
