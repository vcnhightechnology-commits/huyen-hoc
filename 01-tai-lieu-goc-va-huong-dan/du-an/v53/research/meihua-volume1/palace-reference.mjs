// Private source catalogue;not loaded by the consumer site.
import {readFileSync} from 'node:fs';
const read=f=>JSON.parse(readFileSync(new URL(f,import.meta.url),'utf8'));
const source=read('PALACE_ROWS.json'),fields=read('TABLE_FIELDS.json').records;
const bits=[null,[1,1,1],[1,1,0],[1,0,1],[1,0,0],[0,1,1],[0,1,0],[0,0,1],[0,0,0]];
const copy=x=>structuredClone(x),entries=source.rows.flatMap(row=>row.members.map(member=>({
 ...member,parentTrigram:row.parentTrigram,printedParent:row.printedParent,palaceElement:row.palaceElement,
 evidencePDFPages:row.evidencePDFPages.slice(),bits:[...bits[member.lower],...bits[member.upper]],
 scope:'membership-in-printed-eight-name-group',notAMovingLineEvent:true,
 bodyElementInferred:false,shiYing:null,naJia:null,liuQin:null,predictedEvent:null})));
if(entries.length!==64||new Set(entries.map(e=>e.number)).size!==64||new Set(entries.map(e=>e.bits.join(''))).size!==64)throw new Error('source catalogue is not a64memberbijection');
function integer(n,min,max,name){if(!Number.isInteger(n)||n<min||n>max)throw new TypeError(name);return n;}
export function printedRows(){return copy(source.rows);}
export function lookupHexagram(number){integer(number,1,64,'explicit KingWen number');return copy(entries.find(e=>e.number===number));}
export function lookupBits(sixBits){
 if(!Array.isArray(sixBits)||sixBits.length!==6||!Array.from(sixBits).every(b=>b===0||b===1))throw new TypeError('six explicitnumeric bits,bottom-to-top');
 return copy(entries.find(e=>e.bits.every((b,i)=>b===sixBits[i])));
}
// A computational inference matching the literal rows,not a source claim of
// these binary masks,not an event path,andnot a complete LụcHào rule system.
export function derivePalace(parentTrigram){
 integer(parentTrigram,1,8,'parent trigram');
 const pure=[...bits[parentTrigram],...bits[parentTrigram]];
 return source.derivationMasksBottomLSB.map((mask,i)=>{
  const b=pure.map((v,j)=>v^((mask>>j)&1)),entry=lookupBits(b);
  if(entry.parentTrigram!==parentTrigram||entry.ordinal!==i+1)throw new Error('derivedbits conflict with printed membership');
  return {ordinal:i+1,number:entry.number,bits:b,derivation:'developer-inference-checked-against-literal-rows',notAMovingLineEvent:true};
 });
}
export function tableFieldEvidence(query={}){
 if(!query||typeof query!=='object'||Array.isArray(query))throw new TypeError('explicit field query');
 for(const k of Object.keys(query))if(!['trigram','printedHeader'].includes(k))throw new TypeError('unknown query premise');
 if(query.trigram!==undefined&&!source.rows.some(r=>r.printedParent===query.trigram))throw new TypeError('printedtrigramrequired');
 if(query.printedHeader!==undefined&&!fields.some(f=>f.printedHeader===query.printedHeader))throw new TypeError('printedheaderrequired');
 return copy(fields.filter(f=>(query.trigram===undefined||f.trigram===query.trigram)&&(query.printedHeader===undefined||f.printedHeader===query.printedHeader)));
}
