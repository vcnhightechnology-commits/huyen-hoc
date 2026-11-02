export const XUANKONG_SYSTEM='YZSS-Tianyige-XuanKong-declared-frames-94-98';
const yang=[...'乾坎艮震'],yin=[...'巽離坤兌'],labels=[...yang,...yin];
function exact(x,keys){if(!x||Object.getPrototypeOf(x)!==Object.prototype||Reflect.ownKeys(x).length!==keys.length||keys.some(k=>!Object.hasOwn(x,k)))throw TypeError('Exact explicit inputs required');if(x.system!==XUANKONG_SYSTEM)throw TypeError('Named source system required');}
export function sourceXuanKongPolarity(input){
 exact(input,['system','frame','trigramLabel']);const {system,frame,trigramLabel}=input;
 if(!['source-xuankong-trigram-label','birth-fuyuan-group','water-mountain','unknown'].includes(frame)||!(trigramLabel===null||labels.includes(trigramLabel)))throw TypeError('Explicit canonical frame and label/null required');
 return {system,frame,trigramLabel,sourcePolarity:frame==='source-xuankong-trigram-label'&&trigramLabel!==null?(yang.includes(trigramLabel)?'陽':'陰'):null,
  sourcePDFPage:94,sourceFamilyYang:[...yang],sourceFamilyYin:[...yin],
  modernPlanRoomClassification:null,birthGuaGroup:null,waterMountainPolarity:null,universalPolarity:null,
  wholeXuanKongExchangeApplied:false,practicalOutcome:null,consumerApplied:false};
}
export function sourceDeclaredRoomCountBalance(input){
 exact(input,['system','countBasis','classificationEstablished','inventoryComplete','yangRoomCount','yinRoomCount']);
 const {system,countBasis,classificationEstablished,inventoryComplete,yangRoomCount,yinRoomCount}=input;
 if(!['declared-source-room-counts','modern-vertical-storeys','area-weighted','unknown'].includes(countBasis)||![true,false,null].includes(classificationEstablished)||![true,false,null].includes(inventoryComplete)||[yangRoomCount,yinRoomCount].some(x=>!(x===null||Number.isSafeInteger(x)&&x>=0)))throw TypeError('Explicit count semantics, three-valued premises and nonnegative safe integer/null required');
 const ready=countBasis==='declared-source-room-counts'&&classificationEstablished===true&&inventoryComplete===true&&yangRoomCount!==null&&yinRoomCount!==null&&(yangRoomCount>0||yinRoomCount>0);
 const selectedCountRelation=ready?(yangRoomCount===yinRoomCount?'equal':yangRoomCount>yinRoomCount?'more-yang':'more-yin'):null;
 return {system,sourcePDFPage:98,selectedCountRelation,sourceClassificationIsDeclaredNotInferred:true,
  roomTrigramsNotConvertedToPhysicalCounts:true,modernPlanAdapter:null,fullSourceConditionsApplied:false,
  healthPrediction:null,financialPrediction:null,practicalOutcome:null,overallRecommendation:null,consumerApplied:false};
}
