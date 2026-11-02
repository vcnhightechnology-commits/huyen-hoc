// Private historical-source reference. Never imported by the consumer site.
import {readFileSync} from 'node:fs';
import {analyze,relation} from '../meihua-conditions/conditions-reference.mjs';
const read=name=>JSON.parse(readFileSync(new URL(name,import.meta.url),'utf8'));
const material=read('MATERIAL_PREMISES.json'),context=read('CONTEXT_PREMISES.json');
const elements=['Mộc','Hỏa','Thổ','Kim','Thủy'];
const trigramElements=[null,'Kim','Kim','Hỏa','Mộc','Mộc','Thủy','Thổ','Thổ'];
const copy=x=>structuredClone(x);
function object(value,allowed,name){
 if(!value||typeof value!=='object'||Array.isArray(value))throw new TypeError(name);
 for(const key of Object.keys(value))if(!allowed.includes(key))throw new TypeError(`${name}:unknown ${key}`);
 return value;
}
function element(value){if(!elements.includes(value))throw new TypeError('explicit body element');return value;}
function selectCase(id){const c=material.cases.find(c=>c.id===id);if(!c)throw new TypeError('explicit known source case');return c;}
const limits=()=>({numericWeight:null,finalVerdict:null,predictedDate:null,empiricalEffectEstablished:false,automaticObjectRecognition:false});

export function listMaterialCases(){return copy(material.cases);}
export function sourceContexts(){return copy(context);}

export function materialEvidence(options){
 object(options,['bodyElement','caseId'],'material premise');
 const body=element(options.bodyElement);
 if(options.caseId===null||options.caseId===undefined)return {missing:true,applicable:false,caseId:null,historicalQualification:null,limits:limits()};
 const c=selectCase(options.caseId),applicable=c.bodyElement===body;
 return {missing:false,caseId:c.id,bodyElement:body,requiredBodyElement:c.bodyElement,otherElement:c.otherElement,
  relationToBody:relation(body,c.otherElement),applicable,
  historicalQualification:applicable?c.historicalQualification:null,
  printedBoundedPhrase:applicable?c.printedBoundedPhrase:null,
  observationClass:c.observationClass,evidencePDFPages:c.evidencePDFPages.slice(),
  reason:applicable?'explicit-historical-premises-match':'body-context-not-established-by-this-clause',limits:limits()};
}

export function motionEvidence(options={}){
 object(options,['externalState','observerState'],'motion premise');
 const external=options.externalState??'unknown',observer=options.observerState??'unknown';
 if(!Object.hasOwn(context.motion.external,external)||!Object.hasOwn(context.motion.observer,observer))throw new TypeError('explicit qualitative motion state');
 return {externalState:external,observerState:observer,
  externalQualifier:context.motion.external[external],observerQualifier:context.motion.observer[observer],
  observationsComplete:external!=='unknown'&&observer!=='unknown',
  evidencePDFPages:context.motion.evidencePDFPages.slice(),combinedPriorityResolved:false,
  combinedPace:null,numericalMultiplier:null,predictedDate:null,empiricalTimingValidated:false};
}

// The user/researcher explicitly selects a source case AND a trigram AND records
// what was observed. A material label cannot silently choose乾versus兌,etc.
// New material qualifications stay separate from the existing symbolic graph.
export function inspectExternal(cast,options){
 object(options,['subject','seasonContext','observations','observerState'],'external options');
 const observations=options.observations??[];
 if(!Array.isArray(observations))throw new TypeError('explicit observations');
 motionEvidence({observerState:options.observerState});
 const selected=observations.map(o=>{
  object(o,['id','trigram','observed','caseId','externalState'],'observation');
  if(!Number.isInteger(o.trigram)||o.trigram<1||o.trigram>8)throw new TypeError('explicit trigram');
  const sourceCase=o.caseId==null?null:selectCase(o.caseId);
  if(sourceCase&&sourceCase.otherElement!==trigramElements[o.trigram])throw new TypeError('case and selected trigram element conflict');
  const motion=motionEvidence({externalState:o.externalState,observerState:options.observerState});
  return {observation:o,sourceCase,motion};
 });
 const symbolic=analyze(cast,{subject:options.subject,seasonContext:options.seasonContext,
  observations:selected.map(({observation:o})=>({id:o.id,trigram:o.trigram,observed:o.observed}))});
 const body=symbolic.nodes.find(n=>n.id==='body');
 const evidence=selected.map(({observation:o,sourceCase,motion})=>({id:o.id,
  material:body?materialEvidence({bodyElement:body.element,caseId:sourceCase?.id??null}):
   {missing:!sourceCase,applicable:false,caseId:sourceCase?.id??null,historicalQualification:null,
    reason:'subject-does-not-divide-body-use',limits:limits()},motion}));
 return {symbolic,evidence,materialQualificationsAppliedToGraph:false,sourceRolePolicy:'general-static-body-moving-use',
  alternativeLocalPoliciesNotApplied:context.rolePolicies.filter(p=>!p.consumerPolicy).map(p=>p.id),
  noExternalObservationInvented:evidence.length===0,limits:limits()};
}
