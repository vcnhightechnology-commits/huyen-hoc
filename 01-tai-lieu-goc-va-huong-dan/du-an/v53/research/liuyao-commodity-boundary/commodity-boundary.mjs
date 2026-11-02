import{readFileSync}from'node:fs';
import{compile}from'../liuyao-foundations/liuyao-reference.mjs';
const source=JSON.parse(readFileSync(new URL('COMMODITY_BOUNDARY.json',import.meta.url),'utf8'));
export function explicitCommodityBoundary(values,context){
 if(!context||Object.getPrototypeOf(context)!==Object.prototype||Object.getOwnPropertySymbols(context).length||Object.keys(context).length!==2||!Object.hasOwn(context,'system')||!Object.hasOwn(context,'commodityLabel'))throw TypeError('Explicit source system and commodityLabel or null required');
 if(context.system!==source.system||context.commodityLabel!==null&&!source.explicitSourceCommodityLabels.includes(context.commodityLabel))throw TypeError('Named source and literal extracted commodity label required;no silent aliases or inferred goods');
 const chart=compile(values),wealth=chart.lines.filter(x=>x.kin==='妻財'),elements=[...new Set(wealth.map(x=>x.element))];
 return{system:source.system,sourcePages:[...source.sourcePages],chart,explicitCommodityLabel:context.commodityLabel,questionScopeComplete:context.commodityLabel!==null,
  wealthCoordinates:wealth.map(x=>({line:x.line,branch:x.branch,element:x.element})),
  quotedOldMappingReferences:elements.flatMap(e=>source.quotedOldMappings.filter(x=>x.element===e).map(x=>({...structuredClone(x),acceptedByNamedAuthor:false,notARecommendation:true}))),
  automaticCommodityInferenceRejected:true,inferredCommodity:null,commodityRecommendation:null,productClassification:null,
  sourceQuestionCommodityPreserved:context.commodityLabel,actualPrice:null,profit:null,financialResult:null,saleOrPurchaseAction:null,
  geographicalRecommendation:null,chronologicalDateAdapter:null,effectiveStrength:null,sourceOutcomeValidated:false,consumerApplied:false};
}
