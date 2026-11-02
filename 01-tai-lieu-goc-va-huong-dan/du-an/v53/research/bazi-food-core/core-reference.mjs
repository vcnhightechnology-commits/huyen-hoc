// Private, named-source premise audit. True local predicates never establish
// a whole pattern,real person's strength,fortune,medical or financial result.
import{readFileSync}from'node:fs';
const matrix=JSON.parse(readFileSync(new URL('SELECTED_PREDICATES.json',import.meta.url),'utf8'));
const stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'];
const foodOf={甲:'丙',乙:'丁',丙:'戊',丁:'己',戊:'庚',己:'辛',庚:'壬',辛:'癸',壬:'甲',癸:'乙'};
const canonical=p=>typeof p==='string'&&[...p].length===2&&stems.includes(p[0])&&branches.includes(p[1])&&stems.indexOf(p[0])%2===branches.indexOf(p[1])%2;
const plain=x=>x!==null&&typeof x==='object'&&Object.getPrototypeOf(x)===Object.prototype;
const all=x=>x.includes(false)?false:x.every(v=>v===true)?true:null;
export function inspectFoodCore(context){
 const keys=['system','pillars','declaredFacts'];
 if(!plain(context)||Reflect.ownKeys(context).length!==3||keys.some(k=>!Object.hasOwn(context,k))||context.system!==matrix.system||!plain(context.declaredFacts))throw TypeError('Explicit named system,fourpillars and research declarations required.');
 if(!Array.isArray(context.pillars)||context.pillars.length!==4||!Array.from(context.pillars).every(p=>p===null||canonical(p)))throw TypeError('Fourcanonicalvisiblepillars or explicitnull required.');
 const allowed=new Set(Object.keys(matrix.declaredResearchFactRegistry));
 for(const k of Reflect.ownKeys(context.declaredFacts))if(!allowed.has(k)||![true,false,null].includes(context.declaredFacts[k]))throw TypeError('Onlyregisteredboolean/null research declarations;coordinatescannotbeoverridden.');
 const declared=context.declaredFacts;
 if(declared.sourceFoodMany===true&&declared.sourceFoodFew===true)throw TypeError('Same-frame source多 and少 cannotbothbeassertedtrue.');
 const day=context.pillars[2],dayIsYang=day===null?null:stems.indexOf(day[0])%2===0;
 const coordinates={dayIsYang,dayIsYin:dayIsYang===null?null:!dayIsYang};
 const facts=Object.fromEntries([...allowed].map(k=>[k,null]));Object.assign(facts,coordinates,declared);
 const positions=[];if(day!==null)context.pillars.forEach((p,i)=>{if(p!==null&&p[0]===foodOf[day[0]])positions.push({pillarIndex:i,position:['year','month','day','hour'][i],stem:p[0],fixedRelation:'食神'});});
 const rawComplete=context.pillars.every(x=>x!==null),rawCount=day===null?null:positions.length;
 const rows=matrix.rules.map(rule=>({id:rule.id,sourceClauseIDs:[...rule.sourceClauseIDs],sourceLocalStance:rule.sourceLocalStance,
  localDeclaredPremisesMatch:all(rule.all.map(k=>facts[k])),premises:rule.all.map(k=>({key:k,value:facts[k],basis:matrix.coordinateFacts.includes(k)?'canonical-day-polarity':'declared-research-premise'})),
  unknownPremises:rule.all.filter(k=>facts[k]===null),fullSourceConditionSetEstablished:false,practicalOutcome:null}));
 return{system:context.system,pillars:context.pillars.slice(),coordinateFacts:coordinates,visibleFoodPositions:positions,
  visibleFoodCount:rawComplete?rawCount:null,knownVisibleFoodCountLowerBound:rawCount,visibleScanComplete:rawComplete,
  visibleCountInfersSourceManyFewPurityOrStrength:false,fixedRelationRemappedByRepeatedFood:false,
  sourceQuantity:{many:declared.sourceFoodMany??null,few:declared.sourceFoodFew??null,derivedFromRawCount:false},
  rows,declaredFacts:structuredClone(declared),factsAutomaticallyValidatedForRealPerson:false,
  fullFoodPatternEstablished:null,strength:null,virtualCombinationEffectiveness:null,sourcePrecedenceEstablished:false,
  usefulGodSelected:null,practicalOutcome:null,healthResult:null,financialResult:null,lifespan:null,consumerApplied:false};
}
