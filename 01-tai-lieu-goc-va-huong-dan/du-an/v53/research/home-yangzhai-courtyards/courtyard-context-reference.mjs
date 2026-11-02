import {COURTYARD_SYSTEM,sourceCourtyardDiagram} from './courtyard-reference.mjs';
const insideCases=['YZSS-C82','YZSS-C84'];
const outward=[['水','六煞','文曲'],['木','貪狼','貪狼'],['火','五鬼','廉貞'],['土','天乙','巨門'],['金','延年','武曲']];
// These are two literal prose lists, not a gate-to-element formula or a floor-plan adapter.
export function sourceCourtyardCountContext(input){
 const keys=['system','caseID','countBasis','firstRoomFacing','declaredOrigin','boundary'];
 if(!input||Object.getPrototypeOf(input)!==Object.prototype||Reflect.ownKeys(input).length!==keys.length||keys.some(k=>!Object.hasOwn(input,k)))throw TypeError('Six explicit inputs required');
 const {system,caseID,countBasis,firstRoomFacing,declaredOrigin,boundary}=input;
 const diagram=sourceCourtyardDiagram({system,caseID});
 if(!['ordered-source-jin','modern-vertical-storeys','unknown'].includes(countBasis)||!['inward','all-outward','mixed','unknown'].includes(firstRoomFacing)||!['current-enclosure','outer-main-gate','unknown'].includes(declaredOrigin)||!boundary||Object.getPrototypeOf(boundary)!==Object.prototype||Reflect.ownKeys(boundary).length!==2||!Object.hasOwn(boundary,'hasWall')||!Object.hasOwn(boundary,'hasDoor')||Object.values(boundary).some(x=>![true,false,null].includes(x)))throw TypeError('Explicit canonical count, first-room facing, origin and three-valued boundary facts required');
 const required=boundary.hasWall===true&&boundary.hasDoor===true?'current-enclosure':boundary.hasWall===false&&boundary.hasDoor===false?'outer-main-gate':null;
 const originMatches=required===null||declaredOrigin==='unknown'?null:required===declaredOrigin;
 const knownCase=insideCases.includes(caseID),knownFacing=['inward','all-outward'].includes(firstRoomFacing);
 const ready=originMatches===true&&countBasis==='ordered-source-jin'&&knownCase&&knownFacing;
 const cells=ready?(firstRoomFacing==='inward'?diagram.diagram.printedLayerCells.map(x=>({...x,evidenceKind:'literal-diagram'})):outward.map(([element,label,star],i)=>({ordinal:i+2,sourceElement:element,sourceLabel:label,sourceStar:star,sourceSizeHeightWord:null,evidenceKind:'literal-prose-second-through-sixth'}))):null;
 return {system:COURTYARD_SYSTEM,caseID,requiredOrigin:required,originMatches,firstRoomFacing,
  caseHasExplicitFacingClause:knownCase,selectedLiteralCoordinates:cells,
  outwardFirstLayerSpecified:false,outwardLayerOne:null,extendAfterSixth:null,
  unresolvedDiagramCells:firstRoomFacing==='inward'?diagram.literalUnresolvedCells:[],
  allProseAndGeometryConditionsApplied:false,roomCenterOrSidePalaceEstablished:false,
  modernVerticalFloorAdapter:null,practicalHeightAdvice:null,overallRecommendation:null,consumerApplied:false};
}
