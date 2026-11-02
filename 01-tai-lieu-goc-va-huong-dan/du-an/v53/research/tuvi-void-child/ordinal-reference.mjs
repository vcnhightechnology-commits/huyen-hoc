import{readFileSync}from'node:fs';
const source=JSON.parse(readFileSync(new URL('SOURCE_ORDINALS.json',import.meta.url),'utf8'));
export function childPrintedOrdinal(context){
 if(!context||Object.getPrototypeOf(context)!==Object.prototype||Object.getOwnPropertySymbols(context).length||Object.keys(context).length!==2||!Object.hasOwn(context,'system')||!Object.hasOwn(context,'printedOrdinal'))throw TypeError('Explicit source system and printedOrdinal or null required');
 if(context.system!==source.system)throw TypeError('Named extracted source required');
 if(context.printedOrdinal!==null&&(!Number.isInteger(context.printedOrdinal)||context.printedOrdinal<1||context.printedOrdinal>6))throw TypeError('Only the six extracted printed ordinals or null are supported');
 const row=source.rows.find(x=>x.printedOrdinal===context.printedOrdinal);
 return{system:source.system,printedOrdinal:context.printedOrdinal,sourceCoordinateKnown:row?true:null,sourcePalaceLiteral:row?.sourcePalaceLiteral??null,
  modernChartAliasProjection:row?{hhc:row.modernHHCAlias,iztro:row.modernIztroAlias}:null,
  aliasesAreVerbatimFullSourceLabels:false,sourceAgeCountingConventionResolved:false,GregorianAgeAdapter:null,
  firstMajorPeriodStartResolved:false,firstMajorPeriodAge:null,firstMajorPeriodPalace:null,
  wholePassageTranscribed:false,practicalOutcome:null,healthResult:null,lifespan:null,consumerApplied:false};
}
