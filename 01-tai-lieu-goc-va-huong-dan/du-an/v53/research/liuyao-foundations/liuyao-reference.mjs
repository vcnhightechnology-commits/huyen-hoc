// Private structural reference. No consumer import, calendar adapter or forecast API.
import {readFileSync} from 'node:fs';
const rules=JSON.parse(readFileSync(new URL('RULES.json',import.meta.url),'utf8'));
const trigramBits=[null,[1,1,1],[1,1,0],[1,0,1],[1,0,0],[0,1,1],[0,1,0],[0,0,1],[0,0,0]];
const copy=x=>structuredClone(x);
const entries=rules.palaces.flatMap(p=>{
 const pure=[...trigramBits[p.trigram],...trigramBits[p.trigram]];
 return p.numbers.map((number,i)=>({number,normalizedName:p.normalizedNames[i],palace:p.han,
  palaceTrigram:p.trigram,palaceElement:p.element,stage:rules.stages[i],stageIndex:i,
  shi:rules.shiByStage[i],ying:rules.yingByStage[i],
  bits:pure.map((b,j)=>b^((rules.binaryMasksBottomLSB[i]>>j)&1))}));
});
if(entries.length!==64||new Set(entries.map(e=>e.number)).size!==64||new Set(entries.map(e=>e.bits.join(''))).size!==64)throw Error('64unique source identities required');
function explicitBits(bits){
 if(!Array.isArray(bits)||bits.length!==6||!Array.from(bits).every(b=>b===0||b===1))throw TypeError('six explicit numeric bits, bottom-to-top');
 return bits;
}
function member(bits){return entries.find(e=>e.bits.every((b,i)=>b===bits[i]));}
function assignments(bits){
 const lo=trigramBits.findIndex(t=>t?.every((b,i)=>b===bits[i]));
 const up=trigramBits.findIndex(t=>t?.every((b,i)=>b===bits[i+3]));
 if(lo<1||up<1)throw Error('invalid trigram');
 return [...rules.najia.find(r=>r.trigram===lo).lowerBottomToTop,
         ...rules.najia.find(r=>r.trigram===up).upperBottomToTop];
}
export function catalogue(){return copy(entries);}
export function palaceForBits(bits){return copy(member(explicitBits(bits)));}
export function spiritsForDayStem(dayStem){
 if(typeof dayStem!=='string'||!Object.hasOwn(rules.sixSpirits.starts,dayStem))throw TypeError('explicit single day stem');
 const start=rules.sixSpirits.order.indexOf(rules.sixSpirits.starts[dayStem]);
 return Array.from({length:6},(_,i)=>rules.sixSpirits.order[(start+i)%6]);
}
export function compile(values,options={}){
 if(!Array.isArray(values)||values.length!==6||!Array.from(values).every(v=>[6,7,8,9].includes(v)))throw TypeError('six explicit numeric6/7/8/9values,bottom-to-top');
 if(!options||typeof options!=='object'||Array.isArray(options)||Object.getOwnPropertySymbols(options).length||Object.keys(options).some(k=>k!=='dayStem'))throw TypeError('only optional explicit dayStem is supported');
 const dayStem=options.dayStem===undefined?null:options.dayStem;
 const spirits=dayStem===null?null:spiritsForDayStem(dayStem);
 const bits=values.map(v=>v%2),changedBits=values.map(v=>v===6?1:v===9?0:v%2);
 const main=member(bits),changed=member(changedBits),base=assignments(bits),changedBase=assignments(changedBits);
 const annotate=(stemBranch,index)=>{
  const [stem,branch]=[...stemBranch],element=rules.branchElements[branch];
  return {line:index+1,stem,branch,element,kin:rules.kinMatrix[main.palaceElement][element],kinBasisPalace:main.palace};
 };
 const lines=base.map((sb,i)=>({...annotate(sb,i),value:values[i],polarity:bits[i],moving:values[i]===6||values[i]===9,
  role:main.shi===i+1?'世':main.ying===i+1?'應':null,spirit:spirits?.[i]??null,
  changed:values[i]===6||values[i]===9?{...annotate(changedBase[i],i),polarity:changedBits[i]}:null}));
 return {schema:'hhc.liuyao.structural-chart.v1',orientation:'bottom-to-top',input:values.slice(),
  primary:copy(main),changed:{number:changed.number,normalizedName:changed.normalizedName,bits:changedBits,
   ownPalaceDiagnostic:changed.palace,ownPalaceElementDiagnostic:changed.palaceElement,
   annotationKinBasisPalace:main.palace,shiYingReassigned:false},
  dayStem,lines,movingLines:lines.filter(l=>l.moving).map(l=>l.line),
  scope:'structural-source-reference-only',consumerApplied:false,predictedEvent:null,
  missingPremises:['用神selection','飛伏rules','calendar month/day boundaries','旺衰/旬空conditionalrules','full source exceptions','outcome validation']};
}
