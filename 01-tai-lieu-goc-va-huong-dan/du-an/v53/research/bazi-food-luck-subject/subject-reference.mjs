// Fixed source-coordinate inspection, never a full luck/strength or prediction model.
import {readFileSync}from'node:fs';
const read=n=>JSON.parse(readFileSync(new URL(n,import.meta.url),'utf8'));
const source=read('SOURCE_READINGS.json'),runtime=read('ACTUAL_RUNTIME.json');
export const SOURCE_ID='TMTH005-FOOD-C14',FRAME_ID='named-source-coordinate-only';
const frozen=x=>{if(x&&typeof x==='object'){for(const v of Object.values(x))frozen(v);Object.freeze(x);}return x;};
const rawRows=frozen([...runtime.rows,...runtime.reused]),manual=frozen(source.selectedReadings);
const normalize=raw=>({'长生':'長生','临官':'臨官','冠带':'冠帶','沐浴':'沐浴','死':'死'})[raw]??null;
const exact=(o,keys)=>{if(!o||Object.getPrototypeOf(o)!==Object.prototype||Reflect.ownKeys(o).length!==keys.length||keys.some(k=>!Object.hasOwn(o,k)))throw TypeError('Exact explicit source and lexical policy fields required.');};
export function inspectFoodLuckSubject(o){
 exact(o,['sourceID','frameID','clauseID','implicitSubject','lexicalPolicy']);
 if(o.sourceID!==SOURCE_ID||o.frameID!==FRAME_ID)return null;
 if(!['literal-only','reported-SanmingTiyao-敗-as-沐浴'].includes(o.lexicalPolicy))return null;
 const clause=manual.find(r=>r.id===o.clauseID);if(!clause)return null;
 const implicit=clause.id==='implicit-shen';
 if(implicit&&!['庚','壬',null].includes(o.implicitSubject))throw TypeError('Initial clause accepts explicit庚/壬 hypothesis or null only.');
 if(!implicit&&o.implicitSubject!==null)throw TypeError('Explicit source subject cannot be replaced with a day-master surrogate.');
 const observedIDs=implicit?['possible-ren-shen','alternative-geng-shen']:[clause.id];
 const candidates=observedIDs.map(id=>{const r=rawRows.find(r=>r.id===id);if(!r)throw Error('Retained coordinate missing.');return {stem:r.stem,branch:r.branch,referencePhaseLiteral:normalize(r.actual),referencePhaseRaw:r.actual,sourceStatus:r.sourceStatus,runtimeCallWasReused:!r.newCall};});
 const subject=implicit?o.implicitSubject:clause.subject;
 const chosen=candidates.find(r=>r.stem===subject)??null;
 const literal=implicit?'長生':clause.sourcePhaseLiteral;
 const comparisonTerm=literal==='敗'?(o.lexicalPolicy==='reported-SanmingTiyao-敗-as-沐浴'?'沐浴':null):literal;
 return frozen({sourceID:SOURCE_ID,frameID:FRAME_ID,clauseID:clause.id,sourceImage:clause.image,
  sourceLiteral:clause.literal,sourcePhaseLiteral:literal,
  explicitSourceSubject:implicit?null:clause.subject,declaredImplicitSubjectHypothesis:implicit?o.implicitSubject:null,
  grammarSubjectAdjudicated:!implicit,initialImplicitGrammarSubject:null,
  candidateReferenceCoordinates:candidates,selectedDeclaredReferenceCoordinate:chosen,
  lexicalPolicy:o.lexicalPolicy,comparisonTerm,lexicalEquivalenceApplied:literal==='敗'&&comparisonTerm==='沐浴',
  selectedCoordinatePhaseComparison:chosen&&comparisonTerm?chosen.referencePhaseLiteral===comparisonTerm:null,
  referenceAgreementEstablishesSourceGrammar:false,allClausesUseDayMaster:false,
  sourceStrength:null,effectiveFoodProduction:null,wholeLuckSequence:null,
  practicalWealth:null,healthPrediction:null,sourceOutcome:null,overallFortune:null,
  sourcePhaseIsNotActualDeath:true,sourceClaimsAreHistorical:true,
  newEngineCalls:0,consumerApplied:false,wholeContextApplied:false});
}
