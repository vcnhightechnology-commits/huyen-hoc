// Private B02reference:explicit branches,qualitative table,conditional day-clash labels and layer permissions.
import{readFileSync}from'node:fs';import{compile}from'../liuyao-foundations/liuyao-reference.mjs';
const read=n=>JSON.parse(readFileSync(new URL(n,import.meta.url),'utf8'));
const months=read('MONTH_PHASE_ROWS.json'),pairs=read('PAIR_TABLES.json'),branches=[...'子丑寅卯辰巳午未申酉戌亥'],elements=[...'木火土金水'];
const branchElement=Object.fromEntries(branches.map((b,i)=>[b,[...'水土木木土火火土金金土水'][i]])),copy=x=>structuredClone(x);
function branch(b){if(!branches.includes(b))throw TypeError('explicit single branch');return b;}
function element(e){if(!elements.includes(e))throw TypeError('explicit element character');return e;}
function paired(table,a,b){return table.some(p=>p.includes(a)&&p.includes(b)&&a!==b);}
function delta(a,b){return(elements.indexOf(b)-elements.indexOf(a)+5)%5;}
export function branchRelations(a,b){branch(a);branch(b);const ea=branchElement[a],eb=branchElement[b],d=delta(ea,eb);
 return{from:a,to:b,fromElement:ea,toElement:eb,sameBranch:a===b,sameElement:ea===eb,
  generates:d===1,controls:d===2,receivesGeneration:d===4,receivesControl:d===3,
  clash:paired(pairs.sixClashes.pairs,a,b),combination:paired(pairs.sixCombinations.pairs,a,b)};
}
export function monthRow(monthBranch){branch(monthBranch);return copy(months.rows.find(r=>r.monthBranch===monthBranch));}
export function monthElementLabel(monthBranch,lineElement){element(lineElement);const r=monthRow(monthBranch);return{...r.cells.find(c=>c.element===lineElement),monthBranch,pdfPage:r.pdfPage,numericStrength:null};}
export function threeCombinationIdentity(threeBranches){
 if(!Array.isArray(threeBranches)||threeBranches.length!==3||!Array.from(threeBranches).every(b=>branches.includes(b))||new Set(threeBranches).size!==3)throw TypeError('three explicit distinct branches');
 const r=pairs.threeCombinations.records.find(r=>r.branches.every(b=>threeBranches.includes(b)));
 return r?{...copy(r),presenceOnly:true,transformationApplied:false,useGodOrEventSelected:false}:null;
}
function options(context){
 if(!context||typeof context!=='object'||Array.isArray(context)||Object.getOwnPropertySymbols(context).length||Object.keys(context).some(k=>!['monthBranch','dayBranch','strengthBeforeDayByLine'].includes(k)))throw TypeError('explicit month/day branches and optional pre-day qualitative strength only');
 for(const k of['monthBranch','dayBranch'])if(context[k]!==undefined)branch(context[k]);
 const strength=context.strengthBeforeDayByLine??{};
 if(!strength||typeof strength!=='object'||Array.isArray(strength)||Object.keys(strength).some(k=>!['1','2','3','4','5','6'].includes(k)||!['旺相','休囚','unknown'].includes(strength[k])))throw TypeError('explicit line1..6pre-daystrength 旺相/休囚/unknown');
 return strength;
}
function clashLabel(moving,relation,strength){
 if(!relation)return{status:'unknown-day-context',darkMovement:null,scattered:null};
 if(!relation.clash)return{status:'no-day-clash',darkMovement:false,scattered:false};
 if(strength==='unknown')return{status:'day-clash-strength-unresolved',darkMovement:null,scattered:null};
 if(moving)return strength==='旺相'?{status:'movement-reinforced',darkMovement:false,scattered:false}:{status:'movement-scattered',darkMovement:false,scattered:true};
 return strength==='旺相'?{status:'dark-movement',darkMovement:true,scattered:false}:{status:'day-break',darkMovement:false,scattered:false};
}
export function contextualize(values,context={}){
 const strength=options(context),chart=compile(values),month=context.monthBranch?monthRow(context.monthBranch):null;
 const lines=chart.lines.map(l=>{
  const monthRelation=context.monthBranch?branchRelations(context.monthBranch,l.branch):null;
  const dayRelation=context.dayBranch?branchRelations(context.dayBranch,l.branch):null;
  const suppliedStrength=strength[l.line]??'unknown';
  return{...l,monthElementLabel:month?monthElementLabel(context.monthBranch,l.element):null,
   literalMonthBranchRank:month?month.primaryBranches.includes(l.branch)?'旺':month.secondaryBranchesAsRead.includes(l.branch)?'次':null:null,
   monthRelation,dayRelation,rawMonthClash:monthRelation?.clash??null,
   monthClashQualifiedByDayOccupancy:monthRelation&&dayRelation?monthRelation.clash&&dayRelation.sameBranch:null,
   strengthBeforeDay:suppliedStrength,strengthPremiseOrigin:'caller-asserted-research-premise-not-computed-overall-strength',
   dayClashState:clashLabel(l.moving,dayRelation,suppliedStrength),
   overallStrength:null,void:null,tomb:null,extinction:null,
   changedContext:l.changed?{monthRelation:context.monthBranch?branchRelations(context.monthBranch,l.changed.branch):null,
    dayRelation:context.dayBranch?branchRelations(context.dayBranch,l.changed.branch):null,ownPosition:l.line}:null};
 });
 const nodes=lines.map(l=>({id:'p'+l.line,kind:'primary',line:l.line,branch:l.branch,element:l.element,moving:l.moving}));
 for(const l of lines)if(l.changed)nodes.push({id:'c'+l.line,kind:'changed',line:l.line,branch:l.changed.branch,element:l.changed.element});
 for(const k of['monthBranch','dayBranch'])if(context[k])nodes.push({id:k==='monthBranch'?'month':'day',kind:'calendar',contextRole:k,branch:context[k],element:branchElement[context[k]]});
 const edges=[];
 for(const a of nodes)for(const b of nodes){
  if(a.id===b.id)continue;
  let scopeAllowed,policy;
  if(b.kind==='calendar'){scopeAllowed=false;policy='lines-do-not-injure-day-month';}
  else if(a.kind==='calendar'){scopeAllowed=true;policy='calendar-may-address-primary-and-changed';}
  else if(a.kind==='changed'){scopeAllowed=b.kind==='primary'&&a.line===b.line;policy=scopeAllowed?'changed-to-own-original-only':'changed-cross-position-blocked';}
  else if(b.kind==='changed'){scopeAllowed=false;policy='primary-to-changed-blocked';}
  else{scopeAllowed=true;policy='primary-layer-candidate-activity-strength-premises-required';}
  edges.push({...branchRelations(a.branch,b.branch),from:a.id,to:b.id,fromBranch:a.branch,toBranch:b.branch,scopeAllowed,policy,effectiveness:null,appliedToForecast:false});
 }
 return{schema:'hhc.liuyao.day-month-context.v1',chart,explicitContext:copy(context),monthTable:month,lines,nodes,edges,
  scope:'source-layer-and-qualitative-context-reference-only',calendarAdapter:null,overallStrengthModel:null,
  automaticUseGodSelection:false,predictedEvent:null,consumerApplied:false};
}
