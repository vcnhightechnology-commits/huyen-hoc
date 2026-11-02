// B02PDF77–79. Candidate membership, not functional formation or an outcome.
import{compile}from'../../v53/research/liuyao-foundations/liuyao-reference.mjs';
const groups=[{id:'water',members:[...'申子辰'],element:'水'},{id:'metal',members:[...'巳酉丑'],element:'金'},{id:'fire',members:[...'寅午戌'],element:'火'},{id:'wood',members:[...'亥卯未'],element:'木'}];
const plain=x=>!!x&&typeof x==='object'&&!Array.isArray(x)&&Object.getPrototypeOf(x)===Object.prototype&&!Object.getOwnPropertySymbols(x).length;
function witnesses(pool,group){const positions=group.members.map(b=>pool.filter(x=>x.branch===b)),out=[];for(const a of positions[0])for(const b of positions[1])for(const c of positions[2])out.push([a,b,c]);return out;}
function predicateMap(x,allowed){if(!plain(x)||Object.entries(x).some(([k,v])=>!allowed.includes(k)||(v!==true&&v!==false&&v!==null)))throw TypeError('Explicit supported boolean/null source predicates only.');return x;}
const tri=x=>x.includes(true)?true:x.includes(null)?null:false;
export function triadContexts(values,context={}){
 if(!plain(context)||Object.keys(context).some(k=>!['darkMovementByLine','voidOrMonthBrokenByNode','tombByNode'].includes(k)))throw TypeError('Explicit motion/void-break/tomb research predicates only.');
 const chart=compile(values),dark=predicateMap(context.darkMovementByLine??{},['1','2','3','4','5','6']);
 for(const l of chart.lines)if(l.moving&&dark[l.line]===true)throw TypeError('Actual moving glyph is not a static dark-moving line.');
 const primary=chart.lines.map(l=>({node:'p'+l.line,line:l.line,layer:'primary',branch:l.branch,actualMoving:l.moving,active:l.moving?true:dark[l.line]??null}));
 const changed=chart.lines.filter(l=>l.changed).map(l=>({node:'c'+l.line,line:l.line,layer:'changed',branch:l.changed.branch,actualMoving:true,active:true}));
 const all=[...primary,...changed],ids=all.map(x=>x.node),vb=predicateMap(context.voidOrMonthBrokenByNode??{},ids),tomb=predicateMap(context.tombByNode??{},ids);
 function annotate(nodes){
  const nodeIDs=nodes.map(x=>x.node),voidOrBreakPresent=tri(nodeIDs.map(n=>vb[n]??null)),tombPresent=tri(nodeIDs.map(n=>tomb[n]??null));
  return{nodes:structuredClone(nodes),voidOrMonthBreakPresent:voidOrBreakPresent,tombPresent,
   sourceCompletionDeferred:tri([voidOrBreakPresent,tombPresent]),sourceFillOrOpenDate:null,effectiveFormation:null,transformedElement:null};
 }
 const result=groups.map(g=>{
  const p=witnesses(primary,g).map(nodes=>{
   const active=nodes.filter(n=>n.active===true).length,unknown=nodes.filter(n=>n.active===null).length;
   return{...annotate(nodes),sourceMode2TwoActiveOneInactive:active>2||active+unknown<2?false:unknown?null:active===2,
    sourceMode1LiteralOneMovingRecorded:true,sourceMode1Adjudication:null,sourceMode1NotEmendedToThree:true,
    knownActiveCount:active,unknownActiveCount:unknown};
  });
  const sides=[['inner',1,3,3],['outer',4,6,4]].map(([side,a,b,ordinal])=>{
   const ends=chart.lines[a-1].moving&&chart.lines[b-1].moving;
   const pool=all.filter(n=>n.line===a||n.line===b);
   const candidates=ends?witnesses(pool,g).filter(ns=>ns.some(n=>n.layer==='changed')).map(annotate):[];
   return{side,sourceModeOrdinal:ordinal,endpointLines:[a,b],actualMovingEndpointsPresent:ends,candidateWitnesses:candidates,coordinateCandidatePresent:candidates.length>0,fullFormation:null};
  });
  return{...structuredClone(g),primaryWitnesses:p,sides,effectiveFormation:null,transformedElement:null};
 });
 return{source:'B02PDF77–79',chart,groups:result,
  firstModeLiteral:'一卦之內有一爻動而合局者一也',firstModeCountInterpretation:null,firstModeNotSilentlyEmended:true,
  secondMode:'Two active plus one inactive;missing dark-activity status remains unknown.',
  changedPoolPolicy:'Only source-mode endpoint lines1/3or4/6,with actual moving glyphs and at leastonechangednode. A candidate may use different branches from the same original/changed line;fullformation remainsnull.',
  mixedAllSixLinePoolNotUsed:true,calendarBranchesNotUsedForCompletion:true,
  sameBranchCopiesDoNotSupplyMissingMember:true,sourceQualifiedFormation:null,sourceInnerOuterOutcome:null,automaticUseLine:null,practicalOutcome:null,consumerApplied:false};
}
