import {readFileSync} from 'node:fs';
const table=JSON.parse(readFileSync(new URL('./EXPLICIT_COORDINATES.json',import.meta.url),'utf8'));
const stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'];
const cycle=Array.from({length:60},(_,i)=>stems[i%10]+branches[i%12]);
const plain=x=>!!x&&Object.getPrototypeOf(x)===Object.prototype&&Reflect.ownKeys(x).every(k=>typeof k==='string');
const valid=x=>typeof x==='string'&&cycle.includes(x);
const eq=(a,b)=>a===null?null:a===b;
const and=x=>x.includes(false)?false:x.includes(null)?null:true;
const presence=(pillars,positions,test)=>positions.some(i=>pillars[i]!==null&&test(pillars[i]))?true:positions.some(i=>pillars[i]===null)?null:false;
function exact(x,keys){if(!plain(x)||Reflect.ownKeys(x).length!==keys.length||keys.some(k=>!Object.hasOwn(x,k)))throw TypeError('Exact explicit source-coordinate fields required.');}

// Individual literal coordinates, with unknowns retained. Never a fortune/pattern classifier.
export function sourceAppendixCoordinates(input){
 exact(input,['system','anchorFrame','anchorPillar','pillars']);
 const system=input.system?.replace?.('TMTH005-appendix-','');
 if(typeof input.system!=='string'||input.system!=='TMTH005-appendix-'+system||!table.records.some(x=>x.system===system))throw TypeError('Named appendix system required.');
 if(!['year','day','source-declared','unknown'].includes(input.anchorFrame)||!(input.anchorPillar===null||valid(input.anchorPillar))||!Array.isArray(input.pillars)||input.pillars.length!==4||!Array.from(input.pillars).every(x=>x===null||valid(x)))throw TypeError('Canonical explicit pillars or null required.');
 const {anchorPillar:a,pillars:p}=input;
 if(input.anchorFrame==='year'&&a!==null&&p[0]!==null&&a!==p[0])throw TypeError('Year anchor must agree with actual year pillar.');
 if(input.anchorFrame==='day'&&a!==null&&p[2]!==null&&a!==p[2])throw TypeError('Day anchor must agree with actual day pillar.');
 const cases=table.records.filter(x=>x.system===system).map(row=>{
  const anchorMatches=a===null?null:row.anchor.length===1?a[0]===row.anchor:a===row.anchor;
  const frameMatches=row.requiredAnchorFrame==='year'?(input.anchorFrame==='unknown'?null:input.anchorFrame==='year'):(input.anchorFrame==='source-declared'?true:null);
  let targets;
  if(row.targetKind==='stem-and-branch')targets=row.targets.map((symbol,i)=>({symbol,kind:i===0?'stem':'branch',present:presence(p,row.targetPositions,x=>x[i]===symbol)}));
  else targets=row.targets.map(symbol=>({symbol,kind:row.targetKind==='stems'?'stem':'pillar',present:presence(p,row.targetPositions,x=>row.targetKind==='stems'?x[0]===symbol:x===symbol)}));
  const coordinateGate=and([anchorMatches,frameMatches]);
  return {caseID:row.id,parentContext:row.parentContext,anchorMatches,frameMatches,
   targets,targetPositions:row.targetPositions.slice(),coordinateGate,
   singleTargetCoordinateMatch:targets.length===1?and([coordinateGate,targets[0].present]):null,
   allListedTokensPresent:and(targets.map(x=>x.present)),
   // The two-token lists in Fuxing and Mochi have no adjudicated selection/join operator.
   listedCoordinateConjunction:row.targetJoinUnresolved?null:and([coordinateGate,...targets.map(x=>x.present)]),
   targetJoinResolved:!row.targetJoinUnresolved,fullSourceClauseApplied:false};
 });
 return {system:input.system,anchorFrame:input.anchorFrame,anchorPillar:a,pillars:p.slice(),cases,
  roleFactsAreExplicitResearchInputs:true,unlistedCasesAreUnknownNotRefuted:true,
  effectiveCombination:null,wholePatternEstablished:null,sourceOutcome:null,consumerApplied:false};
}

// A mathematical interpretation of 十三位; not sixty source-transcribed examples.
export function derivedSameNestCoordinate(input){
 exact(input,['system','anchorPillar','targetPillar']);
 if(input.system!=='TMTH005-appendix-tongke-inclusive13-derived'||![input.anchorPillar,input.targetPillar].every(x=>x===null||valid(x)))throw TypeError('Explicit canonical source cycle coordinates required.');
 const target=input.anchorPillar===null?null:cycle[(cycle.indexOf(input.anchorPillar)+12)%60];
 return {system:input.system,anchorPillar:input.anchorPillar,expectedDerivedPillar:target,
  targetPillar:input.targetPillar,coordinateMatches:target===null||input.targetPillar===null?null:target===input.targetPillar,
  ordinalCounting:'inclusive13=advance12',isPrintedSixtyRowTable:false,sourceAnchorRoleEstablished:false,
  wholePatternEstablished:null,sourceOutcome:null,consumerApplied:false};
}
