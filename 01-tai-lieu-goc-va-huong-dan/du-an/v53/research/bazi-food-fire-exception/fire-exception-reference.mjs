import{readFileSync}from'node:fs';
const retained=JSON.parse(readFileSync(new URL('REUSE_IDENTITIES.json',import.meta.url),'utf8')).retainedActualPair;
export const SOURCE_ID='TMTH005-FOOD-C31-Mijue',FRAME_ID='source-explicit-day-hour-fire-premise';
const stems=[...'甲乙丙丁戊己庚辛壬癸'];
const exact=(o,keys)=>{if(!o||Object.getPrototypeOf(o)!==Object.prototype||Reflect.ownKeys(o).length!==keys.length||keys.some(k=>!Object.hasOwn(o,k)))throw TypeError('Exact named source, day/hour stems and declared fire premise required.');};
const eq=(s,t)=>s===null?null:s===t,and=(...v)=>v.includes(false)?false:v.includes(null)?null:true;
export function inspectFoodFireException(o){
 exact(o,['sourceID','frameID','dayStem','hourStem','effectiveFireStrong']);
 if(o.sourceID!==SOURCE_ID||o.frameID!==FRAME_ID)return null;
 for(const s of [o.dayStem,o.hourStem])if(s!==null&&!stems.includes(s))throw TypeError('Ten-stem literal or explicit null required.');
 if(o.effectiveFireStrong!==true&&o.effectiveFireStrong!==false&&o.effectiveFireStrong!==null)throw TypeError('Effective fire strength must be explicit boolean or null.');
 const role=and(eq(o.dayStem,'戊'),eq(o.hourStem,'庚'));
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,sourceVoice:'秘訣',sourceLiteral:'戊日庚時不宜火旺',
  dayStem:o.dayStem,hourStem:o.hourStem,declaredEffectiveFireStrong:o.effectiveFireStrong,
  sourceDayHourRolePremise:role,sourceFireContraindicationPremise:and(role,o.effectiveFireStrong),
  retainedActualFoodRelation:Object.freeze({root:'戊',target:'庚',actualHHCTenGod:retained.actualHHCTenGod,actualLunarTenGod:retained.actualLunarTenGod}),
  calculatedFireStrength:null,calendarConsistency:null,calendarBirthDate:null,
  singleFoodPlaceEstablished:null,C30OfficialDefinition:null,
  overallPattern:null,wealthPrediction:null,healthPrediction:null,overallFortune:null,sourceOutcome:null,
  absenceOfContraindicationEstablishesGoodFortune:false,
  sourceConditionTransferredToOtherFoodContexts:false,C13SummerConditionsOverwritten:false,
  newEngineCalls:0,consumerApplied:false,wholeContextApplied:false});
}
