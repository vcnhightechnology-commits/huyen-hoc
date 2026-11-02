// Source-specific declared premises; no natal/strength/ordinary TenGod adapter.
export const SOURCE_ID='TMTH003-FujuYin-selected',FRAME_ID='five-source-positions-and-same-seal-declarations';
const positions=['year','month','day','hour','fetal'];
const exact=(o,keys)=>{if(!o||Object.getPrototypeOf(o)!==Object.prototype||Reflect.ownKeys(o).length!==keys.length||keys.some(k=>!Object.hasOwn(o,k)))throw TypeError('Exact explicit source premise fields required.');};
const tri=x=>{if(x!==true&&x!==false&&x!==null)throw TypeError('Boolean or explicit null required.');};
const and=(...v)=>v.includes(false)?false:v.includes(null)?null:true;
const or=(...v)=>v.includes(true)?true:v.includes(null)?null:false;
export function inspectFujuSeal(o){
 exact(o,['sourceID','frameID','sourcePositionWeakness','sameSealFacts']);
 if(o.sourceID!==SOURCE_ID||o.frameID!==FRAME_ID)return null;
 exact(o.sourcePositionWeakness,positions);
 exact(o.sameSealFacts,['zhengAtSeal','pianAtSeal','storage','strong','shaArrives','shaControlled']);
 [...Object.values(o.sourcePositionWeakness),...Object.values(o.sameSealFacts)].forEach(tri);
 const f=o.sameSealFacts,weak=and(...positions.map(k=>o.sourcePositionWeakness[k])),location=and(f.zhengAtSeal,f.pianAtSeal),storageOrStrong=or(f.storage,f.strong);
 const shaClause=or(f.shaArrives===null?null:!f.shaArrives,f.shaControlled);
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,
  sourcePositionWeakness:Object.freeze({...o.sourcePositionWeakness}),sameSealFacts:Object.freeze({...f}),
  allFiveSourcePositionsDeclaredWeak:weak,sameSealLocationPremise:location,storageOrStrongPremise:storageOrStrong,
  shaConditionalRestraintPremise:shaClause,selectedSourcePremisesMatch:and(weak,location,storageOrStrong,shaClause),
  fetalPositionInvented:false,sourceSealLabelsMappedToOrdinaryTenGod:false,
  actualFetalPillar:null,calculatedStrength:null,actualSealLocation:null,effectiveTransformation:null,
  C19Meaning:null,fullFujuYinClassification:null,blessingScore:null,wealthPrediction:null,
  healthPrediction:null,familyPrediction:null,sourceOutcome:null,overallFortune:null,
  premiseMatchValidatesOutcome:false,consumerApplied:false,wholeContextApplied:false,newEngineCalls:0});
}
