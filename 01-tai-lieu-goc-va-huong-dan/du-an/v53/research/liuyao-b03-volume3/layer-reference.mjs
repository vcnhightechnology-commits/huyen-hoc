// Private B03identifieddirectionaltrigram/NaJiabranchlayers. No efficacy or event verdict.
import{readFileSync}from'node:fs';import{compile}from'../liuyao-foundations/liuyao-reference.mjs';
const tables=JSON.parse(readFileSync(new URL('LAYER_TABLES.json',import.meta.url),'utf8'));
const trig=[{han:'乾',bits:'111'},{han:'兌',bits:'110'},{han:'離',bits:'101'},{han:'震',bits:'100'},{han:'巽',bits:'011'},{han:'坎',bits:'010'},{han:'艮',bits:'001'},{han:'坤',bits:'000'}];
function paired(pairs,a,b){return a!==b&&pairs.some(p=>p.includes(a)&&p.includes(b));}
export function movementCoordinate(fromBranch,toBranch){
 const b=[...'子丑寅卯辰巳午未申酉戌亥'];if(!b.includes(fromBranch)||!b.includes(toBranch))throw TypeError('twoexplicitsinglebranches');
 const pair=(rows)=>rows.some(r=>r[0]===fromBranch&&r[1]===toBranch);
 return{fromBranch,toBranch,coordinate:pair(tables.advanceRetreat.advancePairs)?'進神':pair(tables.advanceRetreat.retreatPairs)?'退神':null,
  strength:null,effectiveMovement:null,auspicious:null,sourcePDFPages:[12,13]};
}
export function classifyLayers(values,...extra){
 if(extra.length)throw TypeError('onlysixexplicitvalues;calendar/strength/contextnotimplementedhere');
 const main=compile(values),changedFullDiagnostic=compile(main.changed.bits.map(b=>b?7:8));
 const halves=['inner','outer'].map((kind,index)=>{
  const start=index*3,before=trig.find(t=>t.bits===main.primary.bits.slice(start,start+3).join('')),after=trig.find(t=>t.bits===main.changed.bits.slice(start,start+3).join('')),
   beforeBranches=main.lines.slice(start,start+3).map(l=>l.branch),afterBranches=changedFullDiagnostic.lines.slice(start,start+3).map(l=>l.branch),changed=before.han!==after.han,
   sameBranches=beforeBranches.every((b,i)=>b===afterBranches[i]);
  return{kind,before:before.han,after:after.han,trigramChanged:changed,directionalFanYin:changed&&paired(tables.trigramFanYin.pairs,before.han,after.han),
   fuYin:changed&&sameBranches,naJiaBranchesBefore:beforeBranches,naJiaBranchesAfterDiagnostic:afterBranches,
   diagnosticAfterBranchesAreNotStaticLineChangedAnnotations:true,effectiveness:null};
 });
 const moving=main.lines.filter(l=>l.moving).map(l=>({line:l.line,from:l.branch,to:l.changed.branch,
  branchFanYin:paired(tables.lineFanYin.pairs,l.branch,l.changed.branch),sameBranch:l.branch===l.changed.branch,
  stemAlsoSame:l.stem===l.changed.stem,movement:movementCoordinate(l.branch,l.changed.branch),effectiveness:null}));
 return{schema:'hhc.liuyao.B03.separate-transform-layers.v1',sourceID:'B03-book2',chart:main,halves,movingLines:moving,
  directionalFanYinHalves:halves.filter(h=>h.directionalFanYin).map(h=>h.kind),fuYinHalves:halves.filter(h=>h.fuYin).map(h=>h.kind),
  branchFanYinMovingLines:moving.filter(l=>l.branchFanYin).map(l=>l.line),
  staticLineChangedAnnotationsInvented:false,calendarAdapter:null,overallStrengthModel:null,priorityBetweenLayers:null,predictedEvent:null,consumerApplied:false};
}
