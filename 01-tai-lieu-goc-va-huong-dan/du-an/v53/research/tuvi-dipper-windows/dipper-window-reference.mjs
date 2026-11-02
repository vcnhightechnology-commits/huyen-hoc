// Source text cross-reference. This module computes no age, period start or event date.
import {readFileSync} from 'node:fs';
const read=n=>JSON.parse(readFileSync(new URL(n,import.meta.url),'utf8'));
const classes=read('SOURCE_CLASSIFICATIONS.json'),windows=read('SOURCE_WINDOWS.json');
export const CLASS_SYSTEM=classes.system,WINDOW_SYSTEM=windows.system;
const freeze=x=>{if(x&&typeof x==='object'){for(const v of Object.values(x))freeze(v);Object.freeze(x);}return x;};
const rows=freeze(classes.rows),textWindows=freeze(windows.windows);
const exact=(x,keys)=>{if(!x||Object.getPrototypeOf(x)!==Object.prototype||Reflect.ownKeys(x).length!==keys.length||keys.some(k=>!Object.hasOwn(x,k)))throw TypeError('Exact explicit source fields required.');};
const bounds=()=>({classificationFromElementInferred:false,activeLimitDerivedFromNatalPosition:false,
 sourcePeriodStartAge:null,sourcePeriodStartPalace:null,calendarStart:null,calendarEnd:null,
 civilHalfYearBoundary:null,computedEventTime:null,eventOutcome:null,overallFortune:null,
 mixedDipperPrecedenceResolved:false,sourceEfficacyValidated:false,consumerApplied:false,wholeSourceMethodApplied:false});
export function lookupSourceDipperClass(x){
 exact(x,['system','sourceStar']);if(x.system!==CLASS_SYSTEM)return null;
 if(x.sourceStar!==null&&(typeof x.sourceStar!=='string'||x.sourceStar.length===0))throw TypeError('Explicit source star name or null required.');
 const row=rows.find(r=>r.sourceStar===x.sourceStar);
 return freeze({system:CLASS_SYSTEM,sourceStar:x.sourceStar,classificationFound:!!row,
  literalDipperDescriptor:row?.literalDipperDescriptor??null,singleDipper:row?.singleDipper??null,
  disposition:row?.disposition??'outside-selected-source-table',sourceCanvas:row?.sourceCanvas??null,
  combinedLabelResolved:false,...bounds()});
}
export function lookupDeclaredDipperWindow(x){
 exact(x,['system','dipper','period']);if(x.system!==WINDOW_SYSTEM)return null;
 if(!['北斗','南斗',null].includes(x.dipper)||!['大限','小限',null].includes(x.period))return null;
 const row=textWindows.find(r=>r.dipper===x.dipper&&r.period===x.period);
 return freeze({system:WINDOW_SYSTEM,dipper:x.dipper,period:x.period,literalWindow:row?.literal??null,
  sourceCanvas:35,historicalTextualWindowOnly:true,...bounds()});
}
export function inspectSourceDipperOccurrences(x){
 exact(x,['system','classificationSystem','frameID','period','occurrences']);
 if(x.system!==WINDOW_SYSTEM||x.classificationSystem!==CLASS_SYSTEM||x.frameID!=='declared-source-period-occurrences'||!['大限','小限',null].includes(x.period))return null;
 if(!Array.isArray(x.occurrences)||x.occurrences.length>64||Reflect.ownKeys(x.occurrences).length!==x.occurrences.length+1)throw TypeError('Dense occurrence list of at most64 required; never truncated.');
 const ids=new Set(),records=[];
 for(const o of x.occurrences){
  exact(o,['occurrenceID','sourceStar','branch','locationRole']);
  if(typeof o.occurrenceID!=='string'||!/^[-a-zA-Z0-9_:\u3400-\u9fff]{1,100}$/.test(o.occurrenceID)||ids.has(o.occurrenceID))throw TypeError('Unique explicit occurrence identifiers required.');
  if(o.branch!==null&&![...'子丑寅卯辰巳午未申酉戌亥'].includes(o.branch))throw TypeError('Declared canonical branch or null required.');
  if(!['natal-location-only','declared-period-location','unknown'].includes(o.locationRole))throw TypeError('Explicit location role required.');
  const c=lookupSourceDipperClass({system:CLASS_SYSTEM,sourceStar:o.sourceStar});ids.add(o.occurrenceID);
  const t=lookupDeclaredDipperWindow({system:WINDOW_SYSTEM,dipper:c.singleDipper,period:x.period});
  records.push({occurrenceID:o.occurrenceID,sourceStar:o.sourceStar,branch:o.branch,locationRole:o.locationRole,
   classificationFound:c.classificationFound,literalDipperDescriptor:c.literalDipperDescriptor,singleDipper:c.singleDipper,
   classificationCanvas:c.sourceCanvas,sourceLiteralWindow:t.literalWindow,
   sourceWindowIsApplicableToObservedLocation:null,combinedDescriptorKeptUnresolved:c.disposition==='combined-unresolved'});
 }
 return freeze({system:WINDOW_SYSTEM,classificationSystem:CLASS_SYSTEM,frameID:x.frameID,period:x.period,
  occurrences:records,allDeclaredOccurrencesPreserved:true,emptySetDoesNotMeanNoInfluence:true,
  sourceWindowIsTextualCrossReference:true,selectedOverallWindow:null,concurrentOrMixedStarsNotRanked:true,
  observedLocationRolesKeptSeparate:true,apiOccurrenceBoundIsNotSourceStarCount:true,...bounds()});
}
