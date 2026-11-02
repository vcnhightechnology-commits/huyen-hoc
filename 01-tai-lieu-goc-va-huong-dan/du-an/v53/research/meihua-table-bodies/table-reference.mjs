// Internal textual reference only. This module is never loaded by the site.
import {readFileSync}from'node:fs';
const data=JSON.parse(readFileSync(new URL('BODY_COLLATION.json',import.meta.url),'utf8'));
const copy=x=>JSON.parse(JSON.stringify(x));
export function field(number,name){
 if(!Number.isInteger(number)||number<1||number>8||typeof name!=='string')throw new TypeError('explicit trigram number and printed field required');
 const r=data.records.find(r=>r.trigramNumber===number&&r.field===name);if(!r)throw new TypeError('unknown printed field');return copy(r);
}
export function fields(number){
 if(!Number.isInteger(number)||number<1||number>8)throw new TypeError('trigram number');
 return data.records.filter(r=>r.trigramNumber===number).map(copy);
}
export function comparisonSummary(){return copy(data.counts)}
