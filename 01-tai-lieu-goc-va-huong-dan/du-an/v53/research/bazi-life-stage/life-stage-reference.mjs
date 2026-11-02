import fs from 'node:fs';
const source=JSON.parse(fs.readFileSync(new URL('MANUAL_TERMS.json',import.meta.url),'utf8'));
export const MAIN_SYSTEM=source.mainSystem;
export const QUOTED_SYSTEM=source.quotedSystem;
const plain=o=>o!==null&&typeof o==='object'&&!Array.isArray(o)&&Object.getPrototypeOf(o)===Object.prototype;
const exact=(o,keys)=>plain(o)&&Reflect.ownKeys(o).length===keys.length&&keys.every(k=>Object.hasOwn(o,k));
const rows=system=>system===MAIN_SYSTEM?source.mainOrder.map((literalName,i)=>({sourceOrdinal:i+1,literalName,explicitSourceAliases:[],sourceDefinition:null,containerPages:source.mainListImages})):
  system===QUOTED_SYSTEM?source.quotedRows:null;
function limits(){return {sourceOnly:true,calendarAdapterEstablished:false,stemBranchCoordinate:null,
  yinYangDirection:null,actualPhaseForBirthChart:null,natalStrength:null,
  sourceBroadGroupAutomaticallyApplied:null,practicalOutcome:null,healthOutcome:null,lifespan:null,
  consumerApplied:false,wholeChapterApplied:false};}
export function sourceLifeStageOrder(context){
  if(!exact(context,['system']))return null;
  const selected=rows(context.system);if(!selected)return null;
  return {system:context.system,records:structuredClone(selected),sourceOrderIsNotTenStemStartRule:true,
    reportedVoice:context.system===QUOTED_SYSTEM?source.quotedVoice:null,...limits()};
}
export function lookupLifeStageTerm(context){
  if(!exact(context,['system','term'])||typeof context.term!=='string')return null;
  const selected=rows(context.system);if(!selected)return null;
  const row=selected.find(r=>r.literalName===context.term||r.explicitSourceAliases.includes(context.term));
  if(!row)return null;
  const otherSystem=context.system===MAIN_SYSTEM?QUOTED_SYSTEM:MAIN_SYSTEM;
  const tokens=[row.literalName,...row.explicitSourceAliases];
  const crossVoiceLexicalMatches=rows(otherSystem).filter(r=>[r.literalName,...r.explicitSourceAliases].some(t=>tokens.includes(t)))
    .map(r=>({system:otherSystem,sourceOrdinal:r.sourceOrdinal,literalName:r.literalName,
      sharedExplicitTokens:[r.literalName,...r.explicitSourceAliases].filter(t=>tokens.includes(t)),fullPhaseEquivalenceEstablished:false}));
  const editorialAlignmentCandidates=source.editorialAlignmentCandidatesNotAcceptedAliases
    .filter(x=>tokens.includes(context.system===MAIN_SYSTEM?x.mainTerm:x.quotedTerm))
    .map(x=>({...x,acceptedAsSourceAlias:false}));
  return {system:context.system,queryTerm:context.term,matchedAs:context.term===row.literalName?'literal-name':'explicit-source-alias',
    ...structuredClone(row),crossVoiceLexicalMatches,editorialAlignmentCandidates,
    historicalMetaphorIsNotMedicalOrLifePrediction:true,
    sourceQualifiers:[...source.noAutomaticOutcomeAnchors],
    broadGroups:{literalTokens:structuredClone(source.reportedBroadGroups),qualifier:source.broadGroupQualifier,
      shorthandResolved:false,automaticallyAssigned:false},...limits()};
}
