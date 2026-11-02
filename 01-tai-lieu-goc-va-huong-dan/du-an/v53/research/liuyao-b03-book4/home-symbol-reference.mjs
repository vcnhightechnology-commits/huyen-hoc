// Source-specific divination symbols, never measured rooms, doors or floor plans.
import {compile} from '../liuyao-foundations/liuyao-reference.mjs';
import {branchRelations} from '../liuyao-day-month/day-month-reference.mjs';
export function homeSymbolCoordinates(values,context,...extra){
 if(extra.length||!context||typeof context!=='object'||Array.isArray(context)||
  Object.getOwnPropertySymbols(context).length||Object.keys(context).some(k=>k!=='sourceContext')||
  context.sourceContext!=='B03-volume9-home-divination')
  throw TypeError('Explicit B03-volume9-home-divination context only; no bearing or floor-plan adapter.');
 const chart=compile(values),house=chart.lines[1],occupants=chart.lines[4],third=chart.lines[2],fourth=chart.lines[3];
 const relation=branchRelations(fourth.branch,house.branch);
 const doorKin=fourth.kin==='兄弟',doorGate=doorKin&&relation.combination;
 const bedException=third.kin==='兄弟'&&third.branch==='卯';
 const node=(line,sourceSymbol,pdfPages)=>({line:line.line,sourceSymbol,pdfPages,branch:line.branch,
  element:line.element,kin:line.kin,moving:line.moving,shiYingRole:line.role,
  actualOwnChange:line.changed?structuredClone(line.changed):null,
  realWorldObjectVerified:false,effectiveness:null});
 return {schema:'hhc.liuyao.B03.home-symbol-coordinates.v1',sourceID:'B03-book4',
  sourceContext:context.sourceContext,chart,
  houseAnchor:node(house,'宅',[28]),occupantAnchor:node(occupants,'人口',[28]),
  innerOuter:{innerLines:[1,2,3],outerLines:[4,5,6],sourcePDFPage:28,
   sourceSymbolicOnly:true,measuredInteriorExterior:null},
  houseOccupantRelation:branchRelations(house.branch,occupants.branch),
  fourthLineDoor:{candidate:node(fourth,'戶候選',[41]),
   kinPremisePresent:doorKin,
   gate:doorKin?'source-kin-prerequisite-present':'source-kin-prerequisite-not-present',
   principalDoorCombinationToHouse:relation.combination,
   principalDoorGate:doorGate?'source-symbol-prerequisites-present':'source-symbol-prerequisites-not-present',
   structuralRelation:relation,actualDoorExistence:null,physicalDoorLocation:null,
   motionRequiredByThisBoundedGate:false},
  thirdLineBedException:{line:3,kin:third.kin,branch:third.branch,gate:bedException,
   sourceSymbol:bedException?'床榻':null,sourcePDFPage:40,
   genericThirdLineDoorAssigned:false,actualBedLocation:null},
  ordinalIsNotBuildingStorey:true,shiYingNotReassigned:true,changedLayerNotUsedToSubstitutePrimaryKin:true,
  compassBearings:null,roomRecommendations:null,physicalFloorPlan:null,
  sourceOutcomeAdjudication:null,predictedEvent:null,consumerApplied:false};
}
