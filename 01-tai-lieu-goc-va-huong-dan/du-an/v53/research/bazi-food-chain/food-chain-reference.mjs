import fs from 'node:fs';
const source=JSON.parse(fs.readFileSync(new URL('MANUAL_CHAIN.json',import.meta.url),'utf8'));
export const SYSTEM='TMTH005-C07-source-chain';
const elements={甲:'木',丙:'火',壬:'水',戊:'土',庚:'金'},ring=Array.from('木火土金水');
const plain=o=>o!==null&&typeof o==='object'&&!Array.isArray(o)&&Object.getPrototypeOf(o)===Object.prototype&&!Object.getOwnPropertySymbols(o).length;
const all=xs=>xs.includes(false)?false:xs.every(v=>v===true)?true:null;
function relation(a,b) {
 const d=(ring.indexOf(elements[b])-ring.indexOf(elements[a])+5)%5;
 return d===1?'生':d===2?'剋':d===0?'同':d===3?'被剋':'被生';
}
export function inspectSourceFoodChain(context) {
 if(!plain(context)||!Object.hasOwn(context,'system')||context.system!==SYSTEM)return null;
 const keys=['system','subjectBinding','declaredFacts'];
 if(Reflect.ownKeys(context).some(k=>!keys.includes(k))||keys.some(k=>!Object.hasOwn(context,k)))return null;
 if(!['unresolved','parallel-bing-subject','adjacent-wu-subject'].includes(context.subjectBinding))throw new TypeError('Explicit supported subject-binding model required.');
 if(!plain(context.declaredFacts))throw new TypeError('Explicit research declarations required.');
 const names=['sameInteractionFrame','owlControlEffective','noCounteractingRescue'];
 for(const [key,value]of Object.entries(context.declaredFacts))
  if(!names.includes(key)||![true,false,null].includes(value))throw new TypeError('Registered boolean/null premises only.');
 const facts=Object.fromEntries(names.map(k=>[k,context.declaredFacts[k]??null]));
 const parallel=context.subjectBinding==='parallel-bing-subject';
 const scenario=parallel?all(Object.values(facts)):null;
 const edges=source.elementCoordinateEdges.map(e=>({...e,id:e.from+'>'+e.to,coordinateRelation:relation(e.from,e.to),
  effectiveInteraction:null,actualSuppression:null}));
 const mechanical={from:'戊',to:'庚',claimedAction:'剋',fixedCoordinateRelation:relation('戊','庚')};
 return {system:SYSTEM,sourceParent:'FOOD-00-C07',sourceNamedDayRoot:'甲',
  sourceNamedStems:[...source.sourceNamedStems],fiveStemsAreNotFiveBirthPillars:true,
  subjectBinding:context.subjectBinding,subjectBindingIsEditorialInference:parallel,
  sourceMeaningResolved:false,elementCoordinateEdges:edges,
  mechanicalAdjacencyAlternative:mechanical,
  selectedAdjacencyConflictsWithFixedControlRelation:context.subjectBinding==='adjacent-wu-subject'&&mechanical.fixedCoordinateRelation!==mechanical.claimedAction,
  declaredFacts:facts,selectedSourceScenarioPremisesMatch:scenario,
  sourceClaimedSuppressedOutgoingEdgeIDs:scenario===true?['丙>戊','丙>庚']:null,
  sourceClaimedSuppressionIsNotEngineValidated:true,
  fullEffectiveInhibition:null,rootStemAutomaticallyReplaced:false,
  autoRescueOrPriority:null,automaticBirthChart:null,
  realPersonStrength:null,practicalOutcome:null,wealthOutcome:null,healthOutcome:null,lifespan:null,
  consumerApplied:false};
}
