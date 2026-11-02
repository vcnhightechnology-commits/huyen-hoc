// Source-specific coordinates only. Explicit research premises are not established event facts.
import {readFileSync} from 'node:fs';
import {compile} from '../liuyao-foundations/liuyao-reference.mjs';
import {dayCoordinates} from '../liuyao-void-motion/void-motion-reference.mjs';
const source=JSON.parse(readFileSync(new URL('TIMING_CLAUSES.json',import.meta.url),'utf8'));
const branches=[...'子丑寅卯辰巳午未申酉戌亥'];
const allowed=['sourceContext','method','useLine','noOtherCauseConfirmed','combinationConfirmed',
 'tombPremiseConfirmed','tombBranch','startDayGanZhi'];
const copy=x=>structuredClone(x);
function partner(rows,b){return rows.find(row=>row.includes(b))?.find(x=>x!==b)??null;}
export function sourceTimingCoordinates(values,context,...extra){
 if(extra.length||!context||typeof context!=='object'||Array.isArray(context)||
  Object.getOwnPropertySymbols(context).length||Object.keys(context).some(k=>!allowed.includes(k)))
  throw TypeError('Explicit supported source timing context required.');
 if(context.sourceContext!=='weather-timing-paragraph')throw TypeError('No implicit transfer to another question domain.');
 const method=source.methods.find(m=>m.id===context.method);
 if(!method)throw TypeError('One of the four compiled source methods required.');
 if(!Number.isInteger(context.useLine)||context.useLine<1||context.useLine>6)throw TypeError('Explicit selected useLine1..6 required.');
 for(const k of ['noOtherCauseConfirmed','combinationConfirmed','tombPremiseConfirmed'])
  if(context[k]!==undefined&&context[k]!==null&&typeof context[k]!=='boolean')throw TypeError('Research premises must be boolean or null.');
 if(context.tombBranch!==undefined&&context.tombBranch!==null&&!branches.includes(context.tombBranch))
  throw TypeError('Explicit single tomb branch required.');
 const day=context.startDayGanZhi===undefined||context.startDayGanZhi===null?null:dayCoordinates(context.startDayGanZhi);
 const chart=compile(values), use=chart.lines[context.useLine-1], requirements=[];
 if(method.motion)requirements.push({id:'actual-line-motion',known:true,
  satisfied:method.motion==='moving'?use.moving:!use.moving});
 requirements.push({id:method.requiresBoolean,known:context[method.requiresBoolean]===true||context[method.requiresBoolean]===false,
  satisfied:context[method.requiresBoolean]??null,callerAssertion:true});
 if(method.target==='clash-tomb'||method.requiresOwnChangedBranchEqualsExplicitTomb){
  requirements.push({id:'explicit-tomb-branch',known:!!context.tombBranch,satisfied:context.tombBranch?true:null});
 }
 if(method.requiresOwnChangedBranchEqualsExplicitTomb)
  requirements.push({id:'actual-own-change-is-explicit-tomb',known:!!context.tombBranch,
   satisfied:context.tombBranch?!!use.changed&&use.changed.branch===context.tombBranch:null});
 const status=requirements.some(r=>r.known&&r.satisfied===false)?'premises-not-satisfied'
  :requirements.every(r=>r.known&&r.satisfied===true)?'explicit-premises-present':'unresolved-premises';
 let targetBranch=null;
 if(status==='explicit-premises-present')targetBranch=method.target==='combine-subject'
  ?partner(source.sixCombinationPairs,use.branch):partner(source.sixClashPairs,method.target==='clash-tomb'?context.tombBranch:use.branch);
 const cycleCandidates=day&&targetBranch?Array.from({length:60},(_,offset)=>{
  const i=(day.cycleIndex0+offset)%60;
  return{offsetDays:offset,sexagenaryIndex0:i,ganZhi:[...'甲乙丙丁戊己庚辛壬癸'][i%10]+branches[i%12]};
 }).filter(d=>d.ganZhi.endsWith(targetBranch)):null;
 return{schema:'hhc.liuyao.B03.source-timing-coordinate.v1',sourceID:'B03-book3',sourcePDFPage:8,
  sourceContext:context.sourceContext,method:copy(method),explicitContext:copy(context),
  chart,useLine:context.useLine,subjectBranch:use.branch,actualOwnChangedBranch:use.changed?.branch??null,
  requirements,premiseStatus:status,unresolved:requirements.filter(r=>!r.known).map(r=>r.id),
  targetBranch,cycleCandidates,cycleOffset0IncludesSuppliedDay:true,
  cycleCandidatesAreCoordinatesNotPredictedDates:true,gregorianDates:null,
  callerPremisesIndependentlyVerified:false,fullTimingAdjudication:null,meteorologicalForecast:null,
  allOtherSourceCausesChecked:false,predictedEvent:null,consumerApplied:false};
}
