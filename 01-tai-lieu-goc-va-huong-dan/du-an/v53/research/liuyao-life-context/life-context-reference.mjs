// Private source-context projection. Presence, motion and element edges are
// separated from strength, efficacy, timing and historical outcome claims.
import{readFileSync}from'node:fs';import{compile}from'../liuyao-foundations/liuyao-reference.mjs';
const source=JSON.parse(readFileSync(new URL('SOURCE_CONTEXTS.json',import.meta.url),'utf8')),elements=[...'木火土金水'];
function relation(a,b){const d=(elements.indexOf(b)-elements.indexOf(a)+5)%5;return d===1?'generates':d===2?'controls':null;}
export function lifeSourceContext(values,context){
 if(!context||typeof context!=='object'||Array.isArray(context)||Object.getOwnPropertySymbols(context).length||Object.keys(context).some(k=>!['system','subject'].includes(k)))throw TypeError('Explicit source system and subject only');
 const method=source.methods.find(x=>x.id===context.system);if(!method)throw TypeError('Explicit named source context required');
 if(context.subject!=='self')throw TypeError('This bounded projection requires explicit self subject; no other-person or unasked focus inference');
 const chart=compile(values),self=chart.lines[chart.primary.shi-1];
 const groups=method.groups.map(g=>({...structuredClone(g),originalLines:chart.lines.filter(x=>x.kin===g.kin).map(x=>x.line),
  changedLines:chart.lines.filter(x=>x.changed?.kin===g.kin).map(x=>x.line)}));
 const lineIDs=[...new Set([self.line,...groups.flatMap(g=>g.originalLines)])];
 const nodes=lineIDs.map(id=>{const x=chart.lines[id-1];return{...structuredClone(x),visibleMoving:x.moving,darkActivity:null,active:x.moving?true:null,hasQi:null};});
 const edges=[];
 for(const a of nodes)for(const b of nodes){if(a.line===b.line)continue;const r=relation(a.element,b.element);if(r)edges.push({fromLine:a.line,toLine:b.line,relation:r,
  fromVisibleMoving:a.visibleMoving,toVisibleMoving:b.visibleMoving,effectiveRelation:null,priority:null});}
 const ownChanges=chart.lines.filter(x=>x.changed).map(x=>({line:x.line,originalElement:x.element,changedElement:x.changed.element,
  changedToOriginalRelation:relation(x.changed.element,x.element),originalToChangedRelation:relation(x.element,x.changed.element),effectiveReturnRelation:null}));
 return{system:method.id,subject:'self',sourcePages:[...method.sourcePages],chart,selfLine:self.line,self:structuredClone(self),groups,nodes,edges,ownChanges,
  scopeOfOneCast:'explicit-focus-only',separateQuestionCategories:[...source.separateQuestionSource.focusCategories],
  useLineSelected:null,selfHasQi:null,wealthHasQi:null,blessingHasQi:null,careerResult:null,financialResult:null,healthResult:null,lifespan:null,
  datePremisesApplied:false,sourceOutcomesValidated:false,consumerApplied:false};
}
