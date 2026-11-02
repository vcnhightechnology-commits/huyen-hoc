// Private identified B02 framework. Explicit coordinates and premise matches only.
import{readFileSync}from'node:fs';
import{contextualize}from'../liuyao-day-month/day-month-reference.mjs';
import{spiritsForDayStem}from'../liuyao-foundations/liuyao-reference.mjs';
const read=n=>JSON.parse(readFileSync(new URL(n,import.meta.url),'utf8'));
const tables=read('CYCLE_TABLES.json'),clauses=read('OPERATIONAL_CLAUSES.json');
const stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'],elements=[...'木火土金水'];
const cycle=Array.from({length:60},(_,i)=>stems[i%10]+branches[i%12]),copy=x=>structuredClone(x);
function branch(b){if(!branches.includes(b))throw TypeError('explicit single branch required');return b;}
function record(o,keys){if(!o||typeof o!=='object'||Array.isArray(o)||Object.getOwnPropertySymbols(o).length||Object.keys(o).some(k=>!keys.includes(k)))throw TypeError('explicit supported context keys required');}
export function dayCoordinates(dayGanZhi){
 const i=cycle.indexOf(dayGanZhi);if(i<0)throw TypeError('one of60exact valid day GanZhi pairs required');
 const head=cycle[i-i%10],row=tables.sixXunVoidRows.find(r=>r.xunHead===head);
 return{dayGanZhi,dayStem:stems[i%10],dayBranch:branches[i%12],cycleIndex0:i,xunHead:head,voidBranches:copy(row.voidBranches),
  daysInXunIndex0:i%10,coordinateDerivation:'sexagenary-cycle-plus-six-literal-xun-rows',functionalVoid:null,gregorianInstant:null};
}
export function rawVoid(lineBranch,dayGanZhi){branch(lineBranch);return dayCoordinates(dayGanZhi).voidBranches.includes(lineBranch);}
export function phaseCoordinates(element,atBranch){
 if(!elements.includes(element))throw TypeError('explicit element required');branch(atBranch);
 const r=tables.fourPhaseRows.find(r=>r.element===element),keys=[...'生旺墓絕'];
 return{element,atBranch,framework:tables.fourPhaseConvention,listedMatches:keys.filter(k=>r[k]===atBranch),
  unknownSlots:keys.filter(k=>r[k]===null),tableRow:copy(r),functionalStage:null,overallStrength:null};
}
export function matchClauses(facts={}){
 record(facts,clauses.explicitBooleanPremises);
 if(Object.values(facts).some(v=>v!==true&&v!==false&&v!==null))throw TypeError('explicit boolean or null research premises only');
 for(const[a,b]of[['moving','static'],['strongBeforeDay','weakBeforeDay'],['receivesDayOrMovingSupport','noDayOrMovingSupport']])if(facts[a]===true&&facts[b]===true)throw TypeError('contradictory research premises');
 return clauses.clauses.map(c=>({...copy(c),premiseStatus:!c.requiresAll.length?'narrative-not-compiled':c.requiresAll.some(k=>facts[k]===false)?'not-satisfied':c.requiresAll.every(k=>facts[k]===true)?'premises-present':'unresolved',
  unresolvedPremises:c.requiresAll.filter(k=>facts[k]===undefined||facts[k]===null),effectApplied:false}));
}
function qualifiedMotion(line){
 const s=line.dayClashState;
 if(s.status==='movement-scattered')return{status:'scatter-possible-not-determined',darkMovement:false,scattered:null,
  sourceQualification:'B02chapter23PDF85..86:weakmovingclashhasrareexceptions;do not assert deterministic散fromstrengthalone'};
 return{...s,sourceQualification:'B02chapter22/23;strengthremainsanexplicitresearchpremise'};
}
export function annotate(values,context={}){
 record(context,['dayGanZhi','monthBranch','strengthBeforeDayByLine']);
 const day=context.dayGanZhi===undefined?null:dayCoordinates(context.dayGanZhi);
 if(context.monthBranch!==undefined)branch(context.monthBranch);
 const inner={};if(day)inner.dayBranch=day.dayBranch;if(context.monthBranch!==undefined)inner.monthBranch=context.monthBranch;
 if(context.strengthBeforeDayByLine!==undefined)inner.strengthBeforeDayByLine=context.strengthBeforeDayByLine;
 const prior=contextualize(values,inner);
 if(day){const spirits=spiritsForDayStem(day.dayStem);prior.chart.dayStem=day.dayStem;for(const l of prior.chart.lines)l.spirit=spirits[l.line-1];for(const l of prior.lines)l.spirit=spirits[l.line-1];}
 const enrich=(node,line)=>({...node,rawVoid:day?rawVoid(node.branch,day.dayGanZhi):null,functionalVoid:null,
  phaseAtDay:day?phaseCoordinates(node.element,day.dayBranch):null,
  phaseAtOwnChange:node===line&&line.changed?phaseCoordinates(node.element,line.changed.branch):null});
 const lines=prior.lines.map(l=>({...enrich(l,l),dayClashState:qualifiedMotion(l),
  changed:l.changed?enrich(l.changed,l):null,sourceQualifiedVoidVerdict:null}));
 const soul=prior.chart.primary.stageIndex===6?'遊魂':prior.chart.primary.stageIndex===7?'歸魂':null;
 return{schema:'hhc.liuyao.void-motion-coordinates.v1',explicitContext:copy(context),day,chart:prior.chart,lines,
  nodes:prior.nodes,edges:prior.edges,soulType:soul,soulStageEvidence:'B02PDF103:遊魂seventh/歸魂eighth;not event prediction',
  scope:'raw-coordinates-and-source-qualified-motion-only',calendarAdapter:null,overallStrengthModel:null,
  functionalVoidModel:null,fanFuModel:null,automaticUseGodSelection:false,predictedEvent:null,consumerApplied:false};
}
