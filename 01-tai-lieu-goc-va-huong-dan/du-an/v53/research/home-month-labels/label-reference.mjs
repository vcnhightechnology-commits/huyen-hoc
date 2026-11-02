import fs from 'node:fs';
const read=n=>JSON.parse(fs.readFileSync(new URL(n,import.meta.url),'utf8'));
const data=read('MANUAL_CELLS.json'),second=read('MANUAL_SECOND_BLOCK.json'),amendment=read('READING_AMENDMENT.json');
const remaining=read('MANUAL_REMAINING_BLOCKS.json');
export const SYSTEM=data.system;
const extra=remaining.blocks.flatMap(b=>b.records.map(r=>({...r,evidenceCrop:b.sourceImage})));
const cells=new Map([...data.records,...second.records,...extra].map(r=>[`${r.sourceMonth}|${r.dayGanzhi}`,r]));
const stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'];
const validDay=s=>typeof s==='string'&&[...s].length===2&&stems.includes(s[0])&&branches.includes(s[1])&&stems.indexOf(s[0])%2===branches.indexOf(s[1])%2;
export function lookupSourceMonthCell(o){
 if(!o||Object.getPrototypeOf(o)!==Object.prototype||Reflect.ownKeys(o).length!==4||!['system','sourceMonth','dayGanzhi','monthBasis'].every(k=>Object.hasOwn(o,k))||o.system!==SYSTEM||o.monthBasis!=='declared-source-month')return null;
 if(o.sourceMonth!==null&&(!Number.isInteger(o.sourceMonth)||o.sourceMonth<1||o.sourceMonth>12))throw TypeError('Explicit source month1..12 or null required.');
 if(o.dayGanzhi!==null&&!validDay(o.dayGanzhi))throw TypeError('Canonical sexagenary day or null required.');
 const cell=cells.get(`${o.sourceMonth}|${o.dayGanzhi}`);
 const amended=cell&&cell.sourceMonth===amendment.sourceMonth&&cell.dayGanzhi===amendment.dayGanzhi;
 const label=amended?amendment.acceptedWorkingLabel:cell?.workingLiteralLabel??null;
 return {system:SYSTEM,sourceMonth:o.sourceMonth,dayGanzhi:o.dayGanzhi,
  cellWasInspected:!!cell,labelReadingStatus:amended?amendment.acceptedStatus:cell?.readingStatus??'not-transcribed-in-this-scope',
  workingLiteralLabel:label,unresolvedMeansBlank:false,
  evidence:cell?{sourcePage:cell.sourcePage,panel:cell.panel,sourceColumnFromRight:cell.sourceColumnFromRight,
    crop:cell.evidenceCrop??(cell.sourcePage===131?'first-ten-full-margins.png':'v53/research/home-day-markers/132-second-ten.png'),readingAmendmentApplied:!!amended}:null,
  all720CellsInspected:true,all720CellsTranscribed:false,sourceMonthBoundaryEstablished:false,
  automaticModernDate:null,combinedDaySuitability:null,practicalOutcome:null,
  futureEventPrediction:null,consumerApplied:false};
}
