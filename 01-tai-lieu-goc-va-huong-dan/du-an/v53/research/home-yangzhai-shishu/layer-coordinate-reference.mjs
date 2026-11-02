// Source-local ordered進/layer coordinates,with explicit declared origin.
// This is not an adapter for storeys,modern rooms,metric plans or star verdicts.
const elements=['水','木','火','土','金'];
const plain=x=>x!==null&&typeof x==='object'&&Object.getPrototypeOf(x)===Object.prototype;
function exact(x,keys){return plain(x)&&Reflect.ownKeys(x).length===keys.length&&keys.every(k=>Object.hasOwn(x,k));}
export function sourceLayerCoordinate(input){
 const keys=['system','countBasis','layerIndex','firstElement','declaredOrigin','boundary'];
 if(!exact(input,keys)||input.system!=='YZSS-Tianyige-selected-chuangong')throw TypeError('Explicit namedsource and six exact inputs required.');
 if(!['ordered-source-jin','modern-vertical-storeys','unknown'].includes(input.countBasis)||!(input.layerIndex===null||Number.isInteger(input.layerIndex)&&input.layerIndex>=1&&input.layerIndex<=10)||!(input.firstElement===null||elements.includes(input.firstElement))||!['current-enclosure','outer-main-gate','unknown'].includes(input.declaredOrigin)||!exact(input.boundary,['hasWall','hasDoor'])||Object.values(input.boundary).some(x=>![true,false,null].includes(x)))throw TypeError('Explicit canonicalcount/origin/elements/null and two three-valuedboundaryfacts required.');
 const {hasWall,hasDoor}=input.boundary;
 const requiredOrigin=hasWall===true&&hasDoor===true?'current-enclosure':hasWall===false&&hasDoor===false?'outer-main-gate':null;
 const originMatch=requiredOrigin===null||input.declaredOrigin==='unknown'?null:input.declaredOrigin===requiredOrigin;
 const countMatch=input.countBasis==='unknown'?null:input.countBasis==='ordered-source-jin';
 const match=[originMatch,countMatch].includes(false)?false:[originMatch,countMatch].includes(null)?null:true;
 const element=match===true&&input.firstElement!==null&&input.layerIndex!==null?elements[(elements.indexOf(input.firstElement)+input.layerIndex-1)%5]:null;
 return{system:input.system,countBasis:input.countBasis,boundary:structuredClone(input.boundary),sourceBoundaryFrameRequired:requiredOrigin,
  declaredOrigin:input.declaredOrigin,originPremiseMatches:originMatch,countMeaningMatches:countMatch,selectedPremisesMatch:match,
  sourceLayerIndex:input.layerIndex,firstElement:input.firstElement,sourceFirstElementIsDeclaredNotInferred:true,element,
  coordinateOnly:element!==null,sourceAnchorPages:[81,93],firstFiveWaterStartExplicitlyPrinted:['水','木','火','土','金'],
  cycleFromDeclaredOtherStartIsEditorialApplicationOfSourceCycle:input.firstElement!==null&&input.firstElement!=='水',
  mixedWallDoorCaseAdjudicated:hasWall===hasDoor&&hasWall!==null,
  localStarName:null,nominalGoodOrBad:null,houseHeightAdvice:null,modernBuildingGeometryAdapterEstablished:false,
  sourceFirstElementDerivationEstablished:false,fullChuangongMethodEstablished:false,practicalOutcome:null,
  healthResult:null,financialResult:null,consumerApplied:false};
}
