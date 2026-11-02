/** Source-grounded occurrence inspection; no use-god ranking or calendar model. */
import{readFileSync,existsSync}from'node:fs';import{dirname,resolve}from'node:path';import{pathToFileURL}from'node:url';
import{compareQuotedOldMethod,SOURCE_ID}from'./multiple-use-reference.mjs';
let root=import.meta.dirname;while(!existsSync(resolve(root,'v53/engine.js'))){const parent=dirname(root);if(parent===root)throw Error('Workspace source root not found');root=parent;}
const {compile}=await import(pathToFileURL(resolve(root,'v53/research/liuyao-foundations/liuyao-reference.mjs')).href);
const manual=JSON.parse(readFileSync(new URL('./OCCURRENCE_MANUAL.json',import.meta.url),'utf8'));
export {SOURCE_ID};export const FRAME_ID=manual.frameID;
const own=(o,k)=>Object.prototype.hasOwnProperty.call(o,k),kin=['父母','兄弟','子孫','妻財','官鬼'];
function exact(o,keys){return o!==null&&typeof o==='object'&&!Array.isArray(o)&&[Object.prototype,null].includes(Object.getPrototypeOf(o))&&keys.every(k=>own(o,k))&&Reflect.ownKeys(o).every(k=>keys.includes(k));}
function frame(o,extra){return exact(o,['sourceID','frameID','kinBasis','layerScope','values','desiredKin',...extra])&&o.sourceID===SOURCE_ID&&o.frameID===FRAME_ID&&o.kinBasis===manual.kinBasis&&o.layerScope===manual.layerScope;}
function readOccurrences(o){
 if(!kin.includes(o.desiredKin))throw new RangeError('Declare one exact source kin category.');
 if(!Array.isArray(o.values)||o.values.length!==6||[0,1,2,3,4,5].some(i=>!own(o.values,i))||Reflect.ownKeys(o.values).some(k=>!['0','1','2','3','4','5','length'].includes(k))||o.values.some(v=>![6,7,8,9].includes(v)))throw new TypeError('Six explicit source line values, bottom to top.');
 const chart=compile(o.values),records=[];
 for(const line of chart.lines)records.push(Object.freeze({occurrenceID:`primary:${line.line}`,line:line.line,layer:'primary',branch:line.branch,element:line.element,kin:line.kin,kinBasisPalace:chart.primary.palace,sourceMoving:line.moving,sourceRole:line.role,temporalActivityEstablished:false}));
 for(const line of chart.lines)if(line.moving&&line.changed)records.push(Object.freeze({occurrenceID:`own-change:${line.line}`,line:line.line,layer:'own-moving-change',branch:line.changed.branch,element:line.changed.element,kin:line.changed.kin,kinBasisPalace:chart.primary.palace,sourceMoving:true,sourceRole:null,temporalActivityEstablished:false}));
 return {chart,records,matches:records.filter(r=>r.kin===o.desiredKin)};
}
function held(){return {selectedUseOccurrence:null,automaticUseGodSelection:false,unifiedRankingEstablished:false,fullSourceMethodEstablished:false,calendarDate:null,sourceStrength:null,functionalVoid:null,effectiveMonthBreak:null,predictedEvent:null,healthOutcome:null,sourceHistoricalOutcomeValidated:false,consumerApplied:false};}
export function inspectSourceUseOccurrences(o){
 if(!frame(o,[]))return null;const {chart,records,matches}=readOccurrences(o);
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,kinBasis:manual.kinBasis,layerScope:manual.layerScope,desiredKin:o.desiredKin,primaryFigure:chart.primary.number,changedFigure:chart.changed.number,primaryPalace:chart.primary.palace,
  sourceMovingLines:Object.freeze([...chart.movingLines]),allStructuralOccurrences:Object.freeze(records),matchingOccurrences:Object.freeze(matches),matchingOccurrenceCount:matches.length,matchingDistinctBranchCount:new Set(matches.map(x=>x.branch)).size,hiddenSpiritsIncluded:false,allChangedFigureLinesIncluded:false,
  occurrencesAreNotProvenSimultaneousActors:true,questionParsed:false,sourcePredicatesCalculated:false,...held()});
}
export function compareSourceOccurrencePairs(o){
 if(!frame(o,['candidateFacts']))return null;const {chart,matches}=readOccurrences(o);
 const fields=['occurrenceID','declaredUse','sourceStrength','sourceMotion','sourceMonthBroken','sourceVoid','sourceInjured'];
 if(!Array.isArray(o.candidateFacts)||o.candidateFacts.length<2||o.candidateFacts.length>12||Array.from({length:o.candidateFacts.length},(_,i)=>i).some(i=>!own(o.candidateFacts,i))||Reflect.ownKeys(o.candidateFacts).some(k=>k!=='length'&&!/^(0|[1-9][0-9]*)$/.test(String(k))))return null;
 if(o.candidateFacts.some(c=>!exact(c,fields)))return null;
 const ids=o.candidateFacts.map(c=>c.occurrenceID),allIDs=matches.map(x=>x.occurrenceID);
 if(ids.length!==allIDs.length||new Set(ids).size!==ids.length||ids.some(id=>!allIDs.includes(id)))return null;
 const toCandidate=(c,id)=>({candidateID:id,declaredUse:c.declaredUse,sourceStrength:c.sourceStrength,sourceMotion:c.sourceMotion,sourceMonthBroken:c.sourceMonthBroken,sourceVoid:c.sourceVoid,sourceInjured:c.sourceInjured});
 const pairs=[];
 for(let i=0;i<o.candidateFacts.length;i++)for(let j=i+1;j<o.candidateFacts.length;j++){
  const a=o.candidateFacts[i],b=o.candidateFacts[j],result=compareQuotedOldMethod({sourceID:SOURCE_ID,frameID:'quoted-old-method-two-declared-use-candidates',candidates:[toCandidate(a,'A'),toCandidate(b,'B')]});
  if(result===null)throw Error('Unexpected comparison frame mismatch');
  pairs.push(Object.freeze({leftOccurrenceID:a.occurrenceID,rightOccurrenceID:b.occurrenceID,inspectionProjection:'editorial-all-unordered-pairs;source-total-ranking-not-established',sourceComparison:result}));
 }
 return Object.freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,primaryFigure:chart.primary.number,desiredKin:o.desiredKin,kinBasis:manual.kinBasis,sourceOccurrences:Object.freeze(matches),candidateOrder:Object.freeze(ids),pairwiseComparisons:Object.freeze(pairs),pairCount:pairs.length,
  candidateSetCompleteForDeclaredStructuralScope:true,truncatedToTwo:false,threeOrMorePairwiseProjectionIsEditorial:matches.length>2,sourceSelectionPriorityComputed:false,unknownFactPolicy:'Missing is forbidden; canonical null is explicit unknown.',...held()});
}
