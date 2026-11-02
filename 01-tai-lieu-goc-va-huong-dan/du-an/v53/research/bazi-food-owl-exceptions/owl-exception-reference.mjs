import{readFileSync}from'node:fs';
const corpus=JSON.parse(readFileSync(new URL('./CLAUSE_PARTITION.json',import.meta.url),'utf8'));
export const OWL_EXCEPTION_SYSTEM=corpus.system;
const records=corpus.records.filter(x=>x.sourceRecipientStemModel!==null),stems=[...'甲乙丙丁戊己庚辛壬癸'];
const plain=x=>x!==null&&Object.getPrototypeOf(x)===Object.prototype;
function exact(x,keys){if(!plain(x)||Reflect.ownKeys(x).length!==keys.length||keys.some(k=>!Object.hasOwn(x,k)||!Object.getOwnPropertyDescriptor(x,k).enumerable||!Object.hasOwn(Object.getOwnPropertyDescriptor(x,k),'value')))throw TypeError('Exact plain declared fields required');}
const and=values=>values.includes(false)?false:values.every(x=>x===true)?true:null;
export function sourceOwlExceptionPremises(input){
 exact(input,['system','caseID','roleFrame','recipientStem','owlStem','namedPillarToken','declaredPremises']);
 const {system,caseID,roleFrame,recipientStem,owlStem,namedPillarToken,declaredPremises}=input;
 if(system!==OWL_EXCEPTION_SYSTEM||!records.some(x=>x.id===caseID)||!['source-recipient-model','natal-chart','unknown'].includes(roleFrame)||![...stems,null].includes(recipientStem)||![...stems,null].includes(owlStem))throw TypeError('Named source, case and explicit canonical roles/frame required');
 const row=records.find(x=>x.id===caseID);
 if(!(namedPillarToken===null||records.some(x=>x.namedPillarToken===namedPillarToken&&x.namedPillarToken!==null))||!plain(declaredPremises))throw TypeError('Named source pillar token/null and plain declared premises required');
 for(const k of Reflect.ownKeys(declaredPremises)){const desc=Object.getOwnPropertyDescriptor(declaredPremises,k);if(!row.requiredResearchPremises.includes(k)||!desc.enumerable||!Object.hasOwn(desc,'value')||![true,false,null].includes(desc.value))throw TypeError('Only case-specific three-valued research premises allowed');}
 const recipientMatches=recipientStem===null?null:recipientStem===row.sourceRecipientStemModel;
 const owlMatches=owlStem===null?null:owlStem===row.sourceOwlStemModel;
 const namedTokenMatches=row.namedPillarToken===null?true:namedPillarToken===null?null:namedPillarToken===row.namedPillarToken;
 const frameMatches=roleFrame==='unknown'?null:roleFrame==='source-recipient-model';
 const facts=row.requiredResearchPremises.map(key=>({key,value:declaredPremises[key]??null,basis:'declared-research-premise-not-derived-from-visible-presence'}));
 const localDeclaredPremisesMatch=and([recipientMatches,owlMatches,namedTokenMatches,frameMatches,...facts.map(x=>x.value)]);
 return{system,caseID,sourceRecord:structuredClone(row),frameMatches,recipientMatches,owlMatches,namedTokenMatches,facts,localDeclaredPremisesMatch,
  candidateTextualExceptionOnly:true,sourceRoleModelIsEditorial:true,sourceBirthChartAnchorValidated:false,
  effectiveCombinationAutomaticallyEstablished:false,sourcePriorityOverOtherClausesResolved:false,
  fixedTenGodRemapping:null,fullFoodPatternEstablished:null,overallStrength:null,practicalOutcome:null,consumerApplied:false};
}
