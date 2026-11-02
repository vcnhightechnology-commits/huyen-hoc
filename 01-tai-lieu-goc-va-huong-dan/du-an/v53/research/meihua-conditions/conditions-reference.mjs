// Internal source-reference calculation. Not loaded by the consumer site.
import {readFileSync} from 'node:fs';
const load=name=>JSON.parse(readFileSync(new URL(name,import.meta.url),'utf8'));
const domainData=load('DOMAIN_RULES.json'),seasonData=load('SEASON_PREMISES.json');
const elements=['Mộc','Hỏa','Thổ','Kim','Thủy'];
const generate={Mộc:'Hỏa',Hỏa:'Thổ',Thổ:'Kim',Kim:'Thủy',Thủy:'Mộc'};
const control={Mộc:'Thổ',Thổ:'Thủy',Thủy:'Hỏa',Hỏa:'Kim',Kim:'Mộc'};
const trigramElements=[null,'Kim','Kim','Hỏa','Mộc','Mộc','Thủy','Thổ','Thổ'];
const trigramBits=[null,[1,1,1],[1,1,0],[1,0,1],[1,0,0],[0,1,1],[0,1,0],[0,0,1],[0,0,0]];
const sameBits=(a,b)=>Array.isArray(a)&&a.length===3&&a.every((v,i)=>v===b[i]);
function integer(v,name,min,max){if(!Number.isInteger(v)||v<min||v>max)throw new TypeError(name);return v;}
function trigram(n){integer(n,'trigram',1,8);return {n,element:trigramElements[n]};}
export function relation(body,other){
 if(!elements.includes(body)||!elements.includes(other))throw new TypeError('element');
 if(body===other)return 'same';
 if(generate[other]===body)return 'use-generates-body';
 if(generate[body]===other)return 'body-generates-use';
 if(control[body]===other)return 'body-controls-use';
 return 'use-controls-body';
}
export function listDomains(){return domainData.domains.map(d=>({id:d.id,ordinal:d.ordinal,heading:d.heading}));}
function selectDomain(id){const d=domainData.domains.find(d=>d.id===id);if(!d)throw new TypeError('explicit subject required');return d;}
export function seasonEvidence(element,context={}){
 if(!elements.includes(element)||!context||typeof context!=='object'||Array.isArray(context))throw new TypeError('season context');
 for(const k of Object.keys(context))if(!['season','monthBranch','dayBranch'].includes(k))throw new TypeError('unestablished calendar input');
 const result=[];
 for(const key of ['season','monthBranch','dayBranch']){
  if(!Object.hasOwn(context,key))continue;
  const value=context[key];let row;
  if(key==='season'&&typeof value==='string'&&Object.hasOwn(seasonData.seasons,value))row=seasonData.seasons[value];
  else if(typeof value==='string'&&Object.hasOwn(seasonData.branchStrong,value)){
   const strong=seasonData.branchStrong[value];row={strong,oppressed:control[strong]};
  }
  if(!row)throw new TypeError(key);
  result.push({basis:key,value,state:row.strong===element?'strong':row.oppressed===element?'oppressed':'unspecified',evidencePDFPages:key==='season'?[60,90]:[84,85]});
 }
 return {observations:result,missing:result.length===0,priorityResolved:false,overallState:null,calendarInferred:false};
}
function validateCast(cast){
 if(!cast||typeof cast!=='object')throw new TypeError('actual cast required');
 const upper=integer(cast.upper?.n,'upper',1,8),lower=integer(cast.lower?.n,'lower',1,8),moving=integer(cast.moving,'moving',1,6);
 for(const t of [cast.upper,cast.lower,cast.mutual?.upper,cast.mutual?.lower,cast.changedUse]){
  const n=integer(t?.n,'cast trigram',1,8);
  if(t.element!==trigramElements[n]||!sameBits(t.bits,trigramBits[n]))throw new TypeError('inconsistent cast trigram');
 }
 const expected=[...trigramBits[lower],...trigramBits[upper]].map((v,i)=>i===moving-1?(v?9:6):(v?7:8));
 if(!Array.isArray(cast.values)||cast.values.length!==6||!cast.values.every((v,i)=>v===expected[i]))throw new TypeError('inconsistent line values');
 const changed=expected.map(v=>v===6||v===7?1:0),pure=upper===lower&&[1,8].includes(upper);
 const nuclear=pure?changed:[...trigramBits[lower],...trigramBits[upper]];
 if(!sameBits(cast.mutual.lower.bits,nuclear.slice(1,4))||!sameBits(cast.mutual.upper.bits,nuclear.slice(2,5)))throw new TypeError('inconsistent mutual');
 if(!sameBits(cast.changedUse.bits,changed.slice(moving<=3?0:3,moving<=3?3:6)))throw new TypeError('inconsistent changed use');
 return {upper,lower,moving};
}
export function analyze(cast,options){
 const {upper,lower,moving}=validateCast(cast);
 if(!options||typeof options!=='object'||Array.isArray(options))throw new TypeError('explicit options');
 for(const k of Object.keys(options))if(!['subject','seasonContext','observations'].includes(k))throw new TypeError('unknown premise');
 const d=selectDomain(options.subject),observations=options.observations??[];
 if(!Array.isArray(observations)||observations.length>12)throw new TypeError('explicit observations');
 const ids=new Set(['body','use','mutual-body-side','mutual-use-side','changed-use']);
 const external=observations.map(o=>{
  if(!o||typeof o!=='object'||typeof o.id!=='string'||!/^external-[a-z0-9-]{1,32}$/.test(o.id)||ids.has(o.id))throw new TypeError('unique external id');
  ids.add(o.id);if(typeof o.observed!=='string'||!o.observed.trim()||o.observed.length>300)throw new TypeError('actual observation description');
  return {id:o.id,...trigram(o.trigram),origin:'explicit-observer-selection',observed:o.observed};
 });
 // Validate calendar premises even in a subject that does not divide body/use.
 seasonEvidence('Mộc',options.seasonContext??{});
 const limits={prognosticValidityEstablished:false,score:null,finalVerdict:null,predictedDate:null,monthDayPriorityResolved:false};
 if(!d.bodyUseApplicable)return {subject:d.id,bodyUseApplicable:false,roles:null,directClause:null,nodes:[],edges:[],qualifiers:[],
  externalObservations:external,missingPremises:d.missingPremises.slice(),limits,
  note:'Historicalweathersectionexplicitlydoesnotdividebody/use;no forecast supplied.'};
 const body=trigram(moving<=3?upper:lower),use=trigram(moving<=3?lower:upper);
 const mb=moving<=3?cast.mutual.upper:cast.mutual.lower,mu=moving<=3?cast.mutual.lower:cast.mutual.upper;
 const nodes=[{id:'body',...body},{id:'use',...use},{id:'mutual-body-side',...trigram(mb.n)},
              {id:'mutual-use-side',...trigram(mu.n)},{id:'changed-use',...trigram(cast.changedUse.n)},...external]
  .map(n=>({...n,relationToBody:relation(body.element,n.element),season:seasonEvidence(n.element,options.seasonContext??{})}));
 const edges=[];
 for(const from of nodes)for(const to of nodes){
  if(from.id===to.id)continue;
  if(generate[from.element]===to.element)edges.push({from:from.id,to:to.id,kind:'generates'});
  else if(control[from.element]===to.element)edges.push({from:from.id,to:to.id,kind:'controls'});
  else if(from.element===to.element)edges.push({from:from.id,to:to.id,kind:'same'});
 }
 const qualifiers=[];
 for(const target of nodes.filter(n=>n.id!=='body')){
  if(!['use-generates-body','use-controls-body'].includes(target.relationToBody))continue;
  for(const actor of nodes.filter(n=>!['body',target.id].includes(n.id))){
   let kind=null;
   if(control[actor.element]===target.element)kind=target.relationToBody==='use-generates-body'?'supporter-controlled':'controller-controlled';
   else if(generate[actor.element]===target.element&&target.relationToBody==='use-controls-body')kind='controller-supported';
   if(kind)qualifiers.push({actor:actor.id,target:target.id,kind,automaticCancellation:false,evidencePDFPages:[89]});
  }
 }
 const key=relation(body.element,use.element);
 return {subject:d.id,bodyUseApplicable:true,roles:{body:d.bodyRole,use:d.useRole},bodyReference:body.n,
         directRelation:key,directClause:{...d.directRelations[key],evidencePDFPages:d.evidencePDFPages.slice()},nodes,edges,qualifiers,
         externalObservations:external,qualifierScope:'Potential qualitative interactions across named layers;not a simultaneous event or automatic cancellation.',missingPremises:[...(options.seasonContext&&Object.keys(options.seasonContext).length?[]:['explicit-season-or-branch-context']),
          'conditional-strength-and-context-priority','domain-subsidiary-clauses'],limits};
}
