// Private B02chapter28 candidate/reference graph. No forecast or automatic useful-god selector.
import{readFileSync}from'node:fs';
import{compile,catalogue}from'../liuyao-foundations/liuyao-reference.mjs';
const source=JSON.parse(readFileSync(new URL('CONDITIONS.json',import.meta.url),'utf8'));
const kinds=['父母','兄弟','官鬼','妻財','子孫'],elements=[...'木火土金水'],branches=[...'子丑寅卯辰巳午未申酉戌亥'];
const branchElements=Object.fromEntries(branches.map((b,i)=>[b,[...'水土木木土火火土金金土水'][i]]));
const copy=x=>structuredClone(x),cycle=(a,b)=>(elements.indexOf(b)-elements.indexOf(a)+5)%5;
function relation(flying,hidden){return['same-element','flying-generates-hidden','flying-controls-hidden','hidden-controls-flying','hidden-generates-flying'][cycle(flying,hidden)];}
function kin(p,e){return['兄弟','子孫','妻財','官鬼','父母'][cycle(p,e)];}
export function candidates(values,desiredKin,context={}){
 if(!kinds.includes(desiredKin))throw TypeError('explicit desired kin;no automatic useful-god selection');
 if(!context||typeof context!=='object'||Array.isArray(context)||Object.keys(context).some(k=>!['dayBranch','monthBranch'].includes(k)))throw TypeError('only optional explicit day/month branch context');
 for(const k of Object.keys(context))if(!branches.includes(context[k]))throw TypeError('explicit branch only');
 const chart=compile(values),palace=catalogue().find(c=>c.palace===chart.primary.palace&&c.stageIndex===0);
 const pure=compile(palace.bits.map(b=>b?7:8));
 const rootMatches=pure.lines.filter(l=>l.kin===desiredKin).map(l=>{
  const flying=chart.lines[l.line-1],r=relation(flying.element,l.element);
  return{line:l.line,palace:chart.primary.palace,pureHexagram:palace.number,stem:l.stem,branch:l.branch,element:l.element,kin:l.kin,
   flying:{stem:flying.stem,branch:flying.branch,element:flying.element,kin:flying.kin},relation:r,
   coincidesWithVisibleBranch:flying.branch===l.branch,selection:null,
   structuralFacts:{flyingGeneratesHidden:r==='flying-generates-hidden',flyingControlsHidden:r==='flying-controls-hidden'}};
 });
 const calendarCandidates=Object.entries(context).map(([role,branch])=>({role,branch,element:branchElements[branch],kin:kin(chart.primary.palaceElement,branchElements[branch])})).filter(l=>l.kin===desiredKin);
 return{schema:'hhc.liuyao.hidden-candidates.v1',desiredKin,chart,rootMatches,
  visibleLines:chart.lines.filter(l=>l.kin===desiredKin).map(l=>l.line),
  changedKinLines:chart.lines.filter(l=>l.changed?.kin===desiredKin).map(l=>l.line),calendarCandidates,
  sourceSearchRule:'If the desired kin is not available,use original palace pure figure;availability/usefulness of visible,changed and calendar candidates remains separate.',
  usefulnessSelection:null,consumerApplied:false,predictedEvent:null};
}
// Kleene three-valued logic: missing premise stays unknown. A matched clause is not a verdict.
function evaluate(expression,facts){
 if(typeof expression==='string')return Object.hasOwn(facts,expression)?facts[expression]:null;
 if(expression.all){const v=expression.all.map(x=>evaluate(x,facts));return v.includes(false)?false:v.includes(null)?null:true;}
 if(expression.any){const v=expression.any.map(x=>evaluate(x,facts));return v.includes(true)?true:v.includes(null)?null:false;}
 throw Error('unsupported source expression');
}
export function conditionMatches(candidate,assertedFacts={}){
 if(!candidate||typeof candidate!=='object'||!candidate.structuralFacts||!elements.includes(candidate.element)||!candidate.flying||!elements.includes(candidate.flying.element)||!Number.isInteger(candidate.line)||candidate.line<1||candidate.line>6||branchElements[candidate.branch]!==candidate.element||branchElements[candidate.flying.branch]!==candidate.flying.element)throw TypeError('explicit structural candidate from candidates()');
 if(!assertedFacts||typeof assertedFacts!=='object'||Array.isArray(assertedFacts)||Object.keys(assertedFacts).some(k=>!source.factualInputs.includes(k)||typeof assertedFacts[k]!=='boolean'))throw TypeError('only explicit boolean research premises;missing is unknown');
 const r=relation(candidate.flying.element,candidate.element);
 const facts={...assertedFacts,flyingGeneratesHidden:r==='flying-generates-hidden',flyingControlsHidden:r==='flying-controls-hidden'};
 const clauses=source.clauses.map(c=>({...copy(c),result:evaluate(c.expression,facts)}));
 const usefulMatches=clauses.filter(c=>c.result===true&&c.sourceClass==='six-listed-useful').map(c=>c.id);
 const unusableMatches=clauses.filter(c=>c.result===true&&c.sourceClass==='five-listed-unusable').map(c=>c.id);
 return{clauses,usefulMatches,unusableMatches,concurrentPositiveAndNegative:usefulMatches.length>0&&unusableMatches.length>0,
  unknownClauses:clauses.filter(c=>c.result===null).map(c=>c.id),assertedResearchPremises:copy(assertedFacts),
  usefulnessSelection:null,predictedEvent:null,sourcePriorityInvented:false};
}
