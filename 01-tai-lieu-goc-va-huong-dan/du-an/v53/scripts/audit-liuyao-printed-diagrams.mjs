import{readFile,writeFile}from'node:fs/promises';import{createHash}from'node:crypto';import vm from'node:vm';import assert from'node:assert/strict';
import{compile}from'../research/liuyao-foundations/liuyao-reference.mjs';
const sha=b=>createHash('sha256').update(b).digest('hex'),s=new URL('../research/liuyao-foundation-span/',import.meta.url),raw=await readFile(new URL('PRINTED_DIAGRAMS.json',s)),source=JSON.parse(raw),code=await readFile(new URL('../../engine.js',s));
assert.equal(sha(code),'39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6');
const c={};c.window=c;vm.createContext(c);vm.runInContext(code.toString(),c);
const kin={父:'父母',兄:'兄弟',官:'官鬼',妻:'妻財',子:'子孫'},rows=[],differences=[],normalizations=[];
for(const r of source.records){
 const values=[...r.sourceBits].reverse().map(x=>x==='1'?7:8),chart=compile(values),hhc=c.HHC_ENGINE.hexNumber(values);
 const identity={sourceNumber:r.number,actualHHCNumber:hhc,privateNumber:chart.primary.number,sourcePalace:r.palace,privatePalace:chart.primary.palace,sourceShi:r.sourceShi,privateShi:chart.primary.shi,sourceYing:r.sourceYing,privateYing:chart.primary.ying};
 for(const[field,a,b]of[['identity',r.number,hhc],['privateIdentity',r.number,chart.primary.number],['palace',r.palace,chart.primary.palace],['shi',r.sourceShi,chart.primary.shi],['ying',r.sourceYing,chart.primary.ying]])if(a!==b)differences.push({number:r.number,pages:r.pdfPages,field,source:a,reference:b});
 const lineResults=[];
 for(let i=0;i<6;i++){
  const line=6-i,l=chart.lines[line-1],glyph=r.literalBranchGlyphs[i],working=glyph==='己'?'巳':glyph;
  if(glyph!==working)normalizations.push({number:r.number,line,literal:glyph,working,policy:'Explicit contextual branch glyph only; original scan and literal field unchanged.'});
  const out={line,sourceLiteralBranch:glyph,workingBranch:working,sourceElement:r.literalElements[i],sourceKin:kin[r.kinAbbreviations[i]],referenceBranch:l.branch,referenceElement:l.element,referenceKin:l.kin};
  for(const[field,a,b]of[['branch',working,l.branch],['element',out.sourceElement,l.element],['kin',out.sourceKin,l.kin]])if(a!==b)differences.push({number:r.number,pages:r.pdfPages,line,field,source:a,reference:b});
  lineResults.push(out);
 }
 rows.push({identity,lineResults});
}
const out={date:'2026-10-28',sourceRowsSHA256:sha(raw),engineSHA256:sha(code),actualHHCHexCalls:64,privateStaticCharts:64,printedDiagrams:64,printedLineRows:384,workingBranchNormalizations:normalizations.length,normalizations,differences,records:rows,notIndependentPredictiveValidation:true,sourceEmended:false,consumerChanged:false};
await writeFile(new URL('../../qa/liuyao-foundation-span/DIAGRAM_COMPARISON.json',s),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({actualHHCHexCalls:64,printedDiagrams:64,printedLineRows:384,workingBranchNormalizations:normalizations.length,differences},null,2));
