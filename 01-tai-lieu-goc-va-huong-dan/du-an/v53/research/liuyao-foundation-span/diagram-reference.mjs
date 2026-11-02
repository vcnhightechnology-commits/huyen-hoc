// Private source comparison; literal evidence and computed structural coordinates stay separate.
import{readFileSync}from'node:fs';
import{compile}from'../liuyao-foundations/liuyao-reference.mjs';
const source=JSON.parse(readFileSync(new URL('PRINTED_DIAGRAMS.json',import.meta.url),'utf8'));
const kin={父:'父母',兄:'兄弟',官:'官鬼',妻:'妻財',子:'子孫'};
export function inspectPrintedDiagram(number){
 if(!Number.isInteger(number)||number<1||number>64)throw TypeError('Explicit integer hexagram number1–64 required.');
 const literal=structuredClone(source.records.find(x=>x.number===number));
 if(!literal)throw Error('Source diagram not retained.');
 const chart=compile([...literal.sourceBits].reverse().map(x=>x==='1'?7:8)),differences=[],normalizations=[];
 const lines=[...literal.sourceBits].map((_,i)=>{
  const line=6-i,glyph=literal.literalBranchGlyphs[i],branch=glyph==='己'?'巳':glyph;
  if(glyph!==branch)normalizations.push({line,literal:glyph,working:branch,onlyWithinPrintedBranchColumn:true});
  const printed={literalBranch:glyph,workingBranch:branch,element:literal.literalElements[i],kin:kin[literal.kinAbbreviations[i]]},computed=chart.lines[line-1];
  for(const[field,a,b]of[['branch',branch,computed.branch],['element',printed.element,computed.element],['kin',printed.kin,computed.kin]])if(a!==b)differences.push({line,field,literal:a,computed:b});
  return{line,printed,computed:{branch:computed.branch,element:computed.element,kin:computed.kin}};
 });
 return{number,literal,lines,normalizations,differences,sourceEmended:false,chart,consumerApplied:false,practicalOutcome:null};
}
