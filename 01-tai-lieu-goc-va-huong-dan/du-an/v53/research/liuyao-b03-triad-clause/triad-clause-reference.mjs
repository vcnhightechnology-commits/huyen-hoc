// Private B03 literal-clause provider; declared activity is not automatic calendar proof.
import{readFileSync}from'node:fs';
import{compile}from'../liuyao-foundations/liuyao-reference.mjs';
const table=JSON.parse(readFileSync(new URL('FULL_CLAUSE.json',import.meta.url),'utf8'));
export const TRIAD_CLAUSE_SOURCE=table.system;
const plain=x=>x!==null&&typeof x==='object'&&Object.getPrototypeOf(x)===Object.prototype;
export function declaredTriadClause(input){
 const keys=['system','groupID','members'];
 if(!plain(input)||Reflect.ownKeys(input).length!==3||keys.some(k=>!Object.hasOwn(input,k))||input.system!==table.system)throw TypeError('Explicit source,group and three member declarations required.');
 const group=table.groups.find(x=>x.id===input.groupID);if(!group)throw TypeError('Unknown source group.');
 if(!Array.isArray(input.members)||input.members.length!==3)throw TypeError('Three members required.');
 for(const x of input.members)if(!plain(x)||Reflect.ownKeys(x).length!==2||!Object.hasOwn(x,'branch')||!Object.hasOwn(x,'active')||![...'子丑寅卯辰巳午未申酉戌亥'].includes(x.branch)||![true,false,null].includes(x.active))throw TypeError('Canonical branch and boolean/null activity required.');
 const complete=group.members.every(b=>input.members.some(x=>x.branch===b)),active=input.members.filter(x=>x.active===true).length,unknown=input.members.filter(x=>x.active===null).length;
 const status=!complete?'incomplete-members':unknown?'activity-premise-unknown':active===2?'two-active-raises-one-coordinate':active===1?'one-active-does-not-raise-two':active===0?'all-inactive-local-clause-fails':'three-active-not-addressed-here';
 return{system:table.system,groupID:group.id,members:structuredClone(input.members),completeDistinctMembership:complete,knownActiveCount:active,unknownActiveCount:unknown,status,
 localPremisePass:!complete?false:unknown||active===3?null:active===2,
 sourceRaisedMemberCoordinate:complete&&!unknown&&active===2?input.members.find(x=>x.active===false).branch:null,
 activityBasis:'declared-research-fact;not-automaticcalendar',sourceFormation:null,strength:null,practicalOutcome:null,consumerApplied:false};
}
export function primaryTriadClause(values,context={}){
 if(!plain(context)||Reflect.ownKeys(context).some(k=>k!=='darkActivityByLine')||!plain(context.darkActivityByLine??{}))throw TypeError('Only declared dark activity by line supported.');
 const chart=compile(values),dark=context.darkActivityByLine??{};
 for(const k of Reflect.ownKeys(dark))if(!['1','2','3','4','5','6'].includes(k)||![true,false,null].includes(dark[k])||chart.lines[Number(k)-1].moving)throw TypeError('Only static-glyph line dark-activity declarations allowed.');
 const nodes=chart.lines.map(x=>({line:x.line,branch:x.branch,active:x.moving?true:dark[x.line]??null,visibleMoving:x.moving}));
 const groups=table.groups.map(g=>{
  const positions=g.members.map(b=>nodes.filter(n=>n.branch===b)),witnesses=[];
  for(const a of positions[0])for(const b of positions[1])for(const c of positions[2]){
   const ns=[a,b,c],result=declaredTriadClause({system:table.system,groupID:g.id,members:ns.map(({branch,active})=>({branch,active}))});
   witnesses.push({...result,lines:ns.map(x=>x.line),visibleMovingCount:ns.filter(x=>x.visibleMoving).length,raisedLine:result.sourceRaisedMemberCoordinate?ns.find(x=>x.branch===result.sourceRaisedMemberCoordinate).line:null});
  }
  return{groupID:g.id,members:g.members.slice(),missingMembers:g.members.filter((_,i)=>positions[i].length===0),witnesses};
 });
 return{source:table.system,chart,groups,primaryMembershipOnly:true,changedOrCalendarCompletionImplemented:false,darkActivityAutomaticallyComputed:false,sourceFormation:null,predictedEvent:null,consumerApplied:false};
}
