// Private B02chapters8..12reference. No automatic question parsing,use-line selection or prediction.
import{readFileSync}from'node:fs';import{compile}from'../liuyao-foundations/liuyao-reference.mjs';
import{candidates}from'../liuyao-hidden-spirits/hidden-reference.mjs';
const read=n=>JSON.parse(readFileSync(new URL(n,import.meta.url),'utf8'));
const source=read('CONDITIONS.json'),subjects=read('SUBJECTS_AND_ROLES.json'),elements=[...'木火土金水'],copy=x=>structuredClone(x);
const d=(a,b)=>(elements.indexOf(b)-elements.indexOf(a)+5)%5;
function line(n){if(!Number.isInteger(n)||n<1||n>6)throw TypeError('explicit line1..6');return n;}
function relativeRole(useElement,otherElement){return['same-element','other-element','仇神','忌神','元神'][d(useElement,otherElement)];}
export function roleTable(useElement){
 if(!elements.includes(useElement))throw TypeError('explicit five-element character');
 return elements.map(element=>({element,role:relativeRole(useElement,element)}));
}
export function subjectCandidates(values,subjectID){
 const s=subjects.subjects.find(s=>s.id===subjectID);if(!s)throw TypeError('exact supported subject ID;no free-text or disputed-subject inference');
 return{subject:copy(s),...candidates(values,s.desiredKin),useLineSelected:null,sourceMethod:'B02chapter8exactnamedcategory-only'};
}
export function roleGraph(values,useLine){
 line(useLine);const chart=compile(values),use=chart.lines[useLine-1];
 const nodes=chart.lines.map(l=>({...l,relativeRole:l.line===useLine?'用神':relativeRole(use.element,l.element)}));
 const edges=[];for(const a of nodes)for(const b of nodes){if(a.line===b.line)continue;const delta=d(a.element,b.element);if(delta===1||delta===2)edges.push({fromLine:a.line,toLine:b.line,relation:delta===1?'generates':'controls',activityPremisesNotResolved:true});}
 return{chart,useLine,useElement:use.element,nodes,edges,automaticUseGodSelection:false,useHasQi:null,predictedEvent:null,
  policy:'Edges are simultaneous structural relations,not prioritized causal effects. Coactivechains/strength/calendar/use-rootpremisesremainseparate.'};
}
function eval3(e,f){
 if(typeof e==='string')return Object.hasOwn(f,e)?f[e]:null;
 if(e.not){const r=eval3(e.not,f);return r===null?null:!r;}
 if(e.all){const v=e.all.map(x=>eval3(x,f));return v.includes(false)?false:v.includes(null)?null:true;}
 if(e.any){const v=e.any.map(x=>eval3(x,f));return v.includes(true)?true:v.includes(null)?null:false;}
 throw Error('invalid source expression');
}
export function actorConditions(values,useLine,actorLine,premises={}){
 line(actorLine);const graph=roleGraph(values,useLine),actor=graph.nodes[actorLine-1];
 if(!premises||typeof premises!=='object'||Array.isArray(premises)||Object.keys(premises).some(k=>!source.factualInputs.includes(k)||typeof premises[k]!=='boolean'))throw TypeError('only explicit boolean research premises;missing is unknown');
 if(!actor.moving&&Object.entries(premises).some(([k,v])=>k.startsWith('changed')&&v))throw TypeError('actual changed-line facts require a source moving line,not merely dark activity');
 const facts={...premises,active:actor.moving?true:premises.darkMovement??null,
  changedReturnGeneration:actor.changed?d(actor.changed.element,actor.element)===1:false,
  changedReturnControl:actor.changed?d(actor.changed.element,actor.element)===2:false};
 for(const [key,role]of[['originActive','元神'],['opposingActive','忌神'],['enemyActive','仇神']]){
  const explicitMotion=graph.nodes.some(n=>n.relativeRole===role&&n.moving);
  if(explicitMotion&&premises[key]===false)throw TypeError('asserted coactivity contradicts explicit moving figure');
  facts[key]=explicitMotion?true:premises[key]??null;
 }
 const clauses=source.clauses.filter(c=>c.role===actor.relativeRole).map(c=>({...copy(c),result:eval3(c.expression,facts)}));
 const effectiveMatches=clauses.filter(c=>c.result===true&&c.kind==='effective').map(c=>c.id),ineffectiveMatches=clauses.filter(c=>c.result===true&&c.kind==='ineffective').map(c=>c.id);
 return{graph,actorLine,actorRole:actor.relativeRole,clauses,effectiveMatches,ineffectiveMatches,
  unknownClauses:clauses.filter(c=>c.result===null).map(c=>c.id),concurrentEffectiveAndIneffective:effectiveMatches.length>0&&ineffectiveMatches.length>0,
  resolvedStructuralFacts:copy(facts),assertedResearchPremises:copy(premises),useHasQi:premises.useHasQi??null,
  rootQualification:'Source separately requires用神有氣/無根assessment. Matchingeffectivenessclausesalonecannotestablishaneventoutcome.',
  automaticUseGodSelection:false,priorityInvented:false,predictedEvent:null,consumerApplied:false};
}
