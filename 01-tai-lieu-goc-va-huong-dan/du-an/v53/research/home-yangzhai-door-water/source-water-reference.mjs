// Private literal-table lookup for one retained witness. No building advice.
import {readFileSync} from 'node:fs';
const table=JSON.parse(readFileSync(new URL('MANUAL_WATER_TABLE.json',import.meta.url),'utf8'));
const polarity=JSON.parse(readFileSync(new URL('MANUAL_SOURCE_POLARITY.json',import.meta.url),'utf8'));
const SYSTEM='YZSS-Tianyige-water-mountain-table';
const mountains=Object.freeze([...'壬子癸丑艮寅甲卯乙辰巽巳丙午丁未坤申庚酉辛戌乾亥']);
const literalTargets=Object.freeze([...'甲乙丙丁庚辛壬癸乾']);
function strict(x,keys){
 if(x===null||typeof x!=='object'||Object.getPrototypeOf(x)!==Object.prototype||Reflect.ownKeys(x).length!==keys.length||
 keys.some(k=>!Object.hasOwn(x,k))||Reflect.ownKeys(x).some(k=>!keys.includes(k)))throw new TypeError('Exact declared source fields required');
 for(const k of keys){const d=Object.getOwnPropertyDescriptor(x,k);if(!d.enumerable||!Object.hasOwn(d,'value'))throw new TypeError('Plain enumerable data required');}
 if(x.system!==SYSTEM)throw new TypeError('Explicit named source system required');
 if(x.mountain!==null&&!mountains.includes(x.mountain))throw new TypeError('Canonical24-mountain mark or null required');
}
const copy=x=>x===null?null:JSON.parse(JSON.stringify(x));
export function sourceMountainPolarity(input){
 strict(input,['system','mountain']);const {system,mountain}=input;
 const sourceMark=mountain===null?null:Object.entries(polarity.mappingToMountainMarks).find(([,v])=>v===mountain)?.[0]??mountain;
 const category=sourceMark===null?null:polarity.yangMarks.includes(sourceMark)?'陽':polarity.yinMarks.includes(sourceMark)?'陰':null;
 return {system,mountain,sourceMark,polarity:category,sourcePDFPage:107,universalPolarity:null,practicalOutcome:null};
}
export function sourceWaterTable(input){
 strict(input,['system','mountain','anchorBasis','flow','targetMark']);
 const {system,mountain,anchorBasis,flow,targetMark}=input;
 if(!['mountain-dragon','birth-fuyuan','gate-facing','unknown'].includes(anchorBasis))throw new TypeError('Explicit source anchor basis required');
 if(!['outflow','inflow','unknown'].includes(flow))throw new TypeError('Explicit water role required');
 if(targetMark!==null&&!literalTargets.includes(targetMark))throw new TypeError('Literal table target mark or null required');
 const out={system,mountain,anchorBasis,flow,targetMark,sourcePDFPage:null,mainText:null,marginalText:null,
  mainTextContainsTarget:null,marginalTextContainsTarget:null,courtyardWorkingText:null,
  sourceFrameEstablished:false,sourceClassification:null,practicalOutcome:null,engineeringAdvice:null,
  measuredDirectionAdapter:null,reason:null};
 if(mountain===null)return {...out,reason:'missing-source-mountain'};
 if(anchorBasis!=='mountain-dragon')return {...out,reason:'source-frame-not-established-for-this-table'};
 if(flow!=='outflow')return {...out,reason:'this-table-lists-outflow-not-this-water-role'};
 const row=table.rows.find(x=>x.mountain===mountain);
 return {...out,sourcePDFPage:row.sourcePDFPage,mainText:copy(row.mainText),marginalText:copy(row.marginalText),
  mainTextContainsTarget:targetMark===null?null:row.mainText.targets.includes(targetMark),
  marginalTextContainsTarget:targetMark===null||row.marginalText===null?null:row.marginalText.targets.includes(targetMark),
  courtyardWorkingText:row.courtyardWorkingText,sourceFrameEstablished:true};
}
