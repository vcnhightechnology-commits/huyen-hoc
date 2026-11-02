// Source-local explanation by希尹; pair rationale never establishes actual transformation.
import{readFileSync}from'node:fs';
const read=n=>JSON.parse(readFileSync(new URL(n,import.meta.url),'utf8'));
const source=read('MANUAL_PAIR_CYCLE.json'),run=read('ACTUAL_RUNTIME.json'),partners=read('REUSED_PARTNERS.json');
export const SOURCE_ID='TMTH005-FOOD-C16-Xiyin',FRAME_ID='reported-transformation-pair-rationale';
const freeze=x=>{if(x&&typeof x==='object'){Object.values(x).forEach(freeze);Object.freeze(x);}return x;};
freeze(source);freeze(run);freeze(partners);
const exact=(o,keys)=>{if(!o||Object.getPrototypeOf(o)!==Object.prototype||Reflect.ownKeys(o).length!==keys.length||keys.some(k=>!Object.hasOwn(o,k)))throw TypeError('Explicit named source, frame, pair and glyph policy required.');};
const stemPair=p=>[...p].length===2&&[...p].every(s=>'甲乙丙丁戊己庚辛壬癸'.includes(s));
export function inspectFoodTransformationRationale(o){
 exact(o,['sourceID','frameID','pairID','glyphPolicy']);
 if(o.sourceID!==SOURCE_ID||o.frameID!==FRAME_ID||!['digital-literal-only','retained-native-working-己'].includes(o.glyphPolicy))return null;
 const row=source.rows.find(r=>r.id===o.pairID);if(!row)return null;
 const native=o.glyphPolicy==='retained-native-working-己',a=native?row.nativeImageWorkingPair:row.digitalPairLiteral,t=native?row.nativeImageWorkingFoodTargetPair:row.digitalFoodTargetPairLiteral;
 const available=stemPair(a)&&stemPair(t),ordinary=[],partnerRows=[];
 if(available){for(const root of a)for(const target of t){const actual=[...run.newRows,...run.reusedRows].find(r=>r.root===root&&r.target===target);if(!actual)throw Error('Retained actual component coordinate missing.');ordinary.push({root,target,actualHHCTenGod:actual.actualHHC,actualLunarTenGod:actual.actualLunar,runtimeWasReused:!actual.newCall,editorialComponentExpansion:true});}
  for(const s of a+t){const r=partners.rows.find(r=>r.stem===s);if(!r)throw Error('Retained partner coordinate missing.');partnerRows.push({...r});}}
 return freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,pairID:row.id,sourceVoiceName:'希尹',
  sourceClauseLiteral:row.sourceClause,sourceDigitalPairLiteral:row.digitalPairLiteral,sourceDigitalFoodTargetPairLiteral:row.digitalFoodTargetPairLiteral,
  glyphPolicy:o.glyphPolicy,selectedPairReading:a,selectedFoodTargetPairReading:t,
  nativeWorkingJiGlyphApplied:native&&(a!==row.digitalPairLiteral||t!==row.digitalFoodTargetPairLiteral),
  allSourceGlyphsGloballyEmended:false,sourcePairOrderPreserved:true,
  reportedTransformedElement:row.sourceTransformedElement,reportedTargetTransformedElement:row.targetSourceTransformedElement,
  reportedDirectedElementControlClaim:[...row.directedTransformedElementClaim],
  reportedPairElementCycle:source.rows.map(r=>({pairID:r.id,digitalPairLiteral:r.digitalPairLiteral,reportedElement:r.sourceTransformedElement,reportedTargetElement:r.targetSourceTransformedElement})),
  ordinaryCoordinateComparisonAvailable:available,retainedOrdinaryComponentRelations:available?ordinary:null,
  ordinaryFoodGodRelations:available?ordinary.filter(r=>r.actualLunarTenGod==='食神').length:null,
  ordinaryNonFoodRelations:available?ordinary.filter(r=>r.actualLunarTenGod!=='食神').length:null,
  allComponentRelationsAreFoodGod:available?ordinary.every(r=>r.actualLunarTenGod==='食神'):null,
  retainedCombinationPartnerCoordinates:available?partnerRows:null,
  partnerIdentityValidatesSourceTransformedElement:false,
  pairRationaleReplacesOrdinaryTenGodRelations:false,
  actualNatalCombination:null,effectiveTransformation:null,calculatedSourceTransformationElement:null,
  effectiveFoodGeneration:null,sourceRationaleCompleteMeaning:null,
  overallPattern:null,wealthPrediction:null,healthPrediction:null,overallFortune:null,sourceOutcome:null,
  sourceAttributionVerifiedAuthorIdentity:null,sourceClaimIsHistorical:true,
  newEngineCalls:0,consumerApplied:false,wholeContextApplied:false});
}
