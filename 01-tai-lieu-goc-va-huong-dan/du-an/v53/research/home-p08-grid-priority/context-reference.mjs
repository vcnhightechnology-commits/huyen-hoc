// Internal textual predicates; no date selection, direction calculation or remedy.
import {readFileSync} from 'node:fs';
const manual=JSON.parse(readFileSync(new URL('./MANUAL_CONTEXTS.json',import.meta.url),'utf8'));
const rows=new Map(manual.records.map(r=>[r.system,r]));
const tri=x=>x===true||x===false||x===null;
const exact=(x,keys)=>x&&Object.getPrototypeOf(x)===Object.prototype&&Reflect.ownKeys(x).length===keys.length&&keys.every(k=>Object.hasOwn(x,k));
const keys=['system','frame','activity','affectedContextConfirmed','genericBeneficPresent','listedStarClauseSatisfied'];
export function inspectDeclaredKuigangContext(x){
 if(!exact(x,keys))throw TypeError('Exact explicit source/context fields required.');
 const row=rows.get(x.system);
 if(!row||row.frame!==x.frame||x.activity!=='printed-dwelling-work')return null;
 if(![x.affectedContextConfirmed,x.genericBeneficPresent,x.listedStarClauseSatisfied].every(tri))throw TypeError('Every premise must be true, false or explicit null.');
 const day=x.system==='P08-DAY-INTRO-131';
 if(day&&x.listedStarClauseSatisfied!==null)throw TypeError('This selected day clause does not implement the separate imperial-star condition.');
 let localAvoidanceClaim=null,localFavourableClaim=null;
 if(day)localAvoidanceClaim=x.affectedContextConfirmed;
 else if(x.affectedContextConfirmed===false||x.listedStarClauseSatisfied===false)localFavourableClaim=false;
 else if(x.affectedContextConfirmed===true&&x.listedStarClauseSatisfied===true)localFavourableClaim=true;
 return Object.freeze({system:row.system,frame:row.frame,source:row.source,sourcePosition:row.position,
  localAvoidanceClaim,localFavourableClaim,
  genericBeneficSubstitutesForNamedCondition:false,
  absenceOfLocalClaimMeansFavourable:false,affectedContextDerived:false,listedStarClauseCalculated:false,
  namedStarListJoinResolved:false,dayAndDirectionRulesMerged:false,
  imperialStarSimultaneousPriority:null,overallSourceRestriction:null,overallDateRecommendation:null,
  calendarDate:null,monthBoundary:null,affectedDirection:null,practicalOutcome:null,
  sourceClaimsAreHistorical:true,wholeSourceMethodApplied:false,consumerApplied:false});
}
