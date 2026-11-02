/** Source-specific coordinate/phrase reference, not effective natal combination. */
import {readFileSync}from 'node:fs';
const data=JSON.parse(readFileSync(new URL('./MANUAL_TABLES.json',import.meta.url),'utf8'));
const own=(o,k)=>Object.prototype.hasOwnProperty.call(o,k);
const branches=[...'子丑寅卯辰巳午未申酉戌亥'],stems=[...'甲乙丙丁戊己庚辛壬癸'];
const deepFreeze=o=>{if(o&&typeof o==='object'){for(const v of Object.values(o))deepFreeze(v);Object.freeze(o);}return o;};
deepFreeze(data);
export const SOURCE_ID=data.sourceID;
export const PAIR_FRAME=data.pairFrame;
export const MONTH_FRAME=data.monthFrame;
export const HIDDEN_FRAME=data.hiddenFrame;
function accept(o,frame,keys){
 if(o===null||typeof o!=='object'||Array.isArray(o)||![Object.prototype,null].includes(Object.getPrototypeOf(o)))return false;
 const all=['sourceID','frameID',...keys];
 return own(o,'sourceID')&&o.sourceID===SOURCE_ID&&own(o,'frameID')&&o.frameID===frame&&all.every(k=>own(o,k))&&Reflect.ownKeys(o).every(k=>all.includes(k));
}
const noVerdict={effectiveCombination:null,transformedElement:null,wholePatternEstablished:null,natalOutcome:null,calendarDate:null,strength:null,interSourcePriority:null,sourceEfficacyValidated:false};
function branch(x,name){if(!branches.includes(x))throw new RangeError(name);}
function tri(x,name){if(x!==true&&x!==false&&x!==null)throw new TypeError(name);}
export function sourceUnionPair(o){
 if(!accept(o,PAIR_FRAME,['from','to']))return null;
 branch(o.from,'from');branch(o.to,'to');
 const listed=data.pairs.some(([a,b])=>(a===o.from&&b===o.to)||(a===o.to&&b===o.from));
 const directed=data.directedRows.find(r=>r.from===o.from&&r.to===o.to);
 return Object.freeze({sourceID:SOURCE_ID,frameID:PAIR_FRAME,from:o.from,to:o.to,listedCoordinatePair:listed,
  directedSourceVoice:directed?data.directedVoice:null,directedSourcePhrase:directed?.sourcePhrase??null,
  ...noVerdict});
}
export function sourceUnionMonth(o){
 if(!accept(o,MONTH_FRAME,['sourceMonth']))return null;
 if(!Number.isInteger(o.sourceMonth)||o.sourceMonth<1||o.sourceMonth>12)throw new RangeError('sourceMonth');
 const row=data.monthRows.find(r=>r.month===o.sourceMonth);
 return Object.freeze({sourceID:SOURCE_ID,frameID:MONTH_FRAME,...row,...noVerdict});
}
export function sourceHiddenUnion(o){
 if(!accept(o,HIDDEN_FRAME,['caseID','anchorKind','anchor','anchorBasis','targetSeen','partnerSeen']))return null;
 const row=data.hiddenRows.find(r=>r.id===o.caseID);if(!row)return null;
 if(o.anchorBasis!=='source-declared-birth-anchor')return null;
 if(o.anchorKind!==row.anchorKind)throw new RangeError('anchorKind');
 if(!(o.anchorKind==='stem'?stems:branches).includes(o.anchor))throw new RangeError('anchor');
 tri(o.targetSeen,'targetSeen');tri(o.partnerSeen,'partnerSeen');
 const matches=o.anchor===row.anchor;
 const gate=!matches||o.targetSeen===true||o.partnerSeen===false?false:
  o.targetSeen===false&&o.partnerSeen===true?true:null;
 return Object.freeze({sourceID:SOURCE_ID,frameID:HIDDEN_FRAME,caseID:row.id,anchorKind:o.anchorKind,anchor:o.anchor,
  anchorCoordinateMatches:matches,absentTarget:row.absentTarget,seenPartner:row.seenPartner,
  sourceLabel:row.sourceLabel,declaredCoordinateGate:gate,appliedToNatalChart:false,anchorPillar:null,
  observationHorizon:null,sourceLocalPatternOnly:true,...noVerdict});
}
