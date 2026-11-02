// Internal literal table lookup. No date conversion,forecast or scoring API.
import{readFileSync}from'node:fs';
const data=JSON.parse(readFileSync(new URL('HOUR_TABLE.json',import.meta.url),'utf8')),copy=x=>JSON.parse(JSON.stringify(x));
export function row(rowKey){if(typeof rowKey!=='string')throw new TypeError('explicit printed row key required');const r=data.rows.find(r=>r.rowKey===rowKey);if(!r)throw new TypeError('unknown printed sexagenary row');return copy(r)}
export function cell(rowKey,hourBranch){const r=row(rowKey);if(typeof hourBranch!=='string'||!data.branchColumns.includes(hourBranch))throw new TypeError('explicit normalized branch column required');return{rowKey:r.rowKey,pdfPage:r.pdfPage,...r.cells.find(c=>c.hourBranch===hourBranch)}}
export function summary(){return copy(data.counts)}
