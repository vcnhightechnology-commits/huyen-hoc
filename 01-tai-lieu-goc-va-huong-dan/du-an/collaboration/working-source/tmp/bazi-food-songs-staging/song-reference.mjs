// A single ancient-song premise layer. Other verses retain their own source conditions.
import{readFileSync}from'node:fs';
const source=JSON.parse(readFileSync(new URL('SELECTED_V05_PREMISES.json',import.meta.url),'utf8'));
export const SOURCE_ID='TMTH005-FOOD-C35-ancient-song-V05',FRAME_ID='single-verse-declared-premises';
const exact=(o,keys)=>{if(!o||Object.getPrototypeOf(o)!==Object.prototype||Reflect.ownKeys(o).length!==keys.length||keys.some(k=>!Object.hasOwn(o,k)))throw TypeError('Explicit single-verse source fields required.');};
const and=(...v)=>v.includes(false)?false:v.includes(null)?null:true;
export function inspectFoodSongPremises(o){
 exact(o,['sourceID','frameID','verseID','declaredLuckElement','declaredFacts']);
 if(o.sourceID!==SOURCE_ID||o.frameID!==FRAME_ID||o.verseID!=='V05')return null;
 if(o.declaredLuckElement!==null&&!['水','木','土','金','火'].includes(o.declaredLuckElement))throw TypeError('Source luck element must be one of five element literals or explicit null.');
 exact(o.declaredFacts,['foodShengWang','wholeGuanShaMixtureAbsent']);
 if(Object.values(o.declaredFacts).some(v=>v!==true&&v!==false&&v!==null))throw TypeError('Source premises must be explicit boolean/null.');
 const preferred=o.declaredLuckElement===null?null:source.preferredLuckElements.includes(o.declaredLuckElement);
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,verseID:'V05',sourceText:source.sourceText,
  declaredLuckElement:o.declaredLuckElement,declaredFacts:Object.freeze({...o.declaredFacts}),
  literalPreferredLuckElement:preferred,selectedVersePremisesMatch:and(preferred,o.declaredFacts.foodShengWang,o.declaredFacts.wholeGuanShaMixtureAbsent),
  listedSourceLuckElements:Object.freeze([...source.preferredLuckElements]),
  sourceMixturePhrase:source.noMixtureLiteral,mixturePhraseSemanticBindingAdjudicated:false,
  V04OfficialPraiseLiteral:source.verse4OfficialClause,
  blanketOfficialPresenceProhibited:null,sourceVersePriority:null,
  calculatedFoodStrength:null,calculatedLuckElement:null,calendarLuckPeriod:null,
  fireAdverseOutcome:null,C31FireContraindicationInferred:null,
  overallPattern:null,wealthPrediction:null,healthPrediction:null,sourceOutcome:null,overallFortune:null,
  preferredListEstablishesOutcome:false,unlistedElementEstablishesAdverseOutcome:false,
  C13SummerConditionsOverwritten:false,otherVersesOverwritten:false,
  newEngineCalls:0,consumerApplied:false,wholeContextApplied:false});
}
