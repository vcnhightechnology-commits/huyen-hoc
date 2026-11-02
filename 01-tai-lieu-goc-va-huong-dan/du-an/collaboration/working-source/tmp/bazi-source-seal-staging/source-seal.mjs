import{readFileSync}from'node:fs';
const manual=JSON.parse(readFileSync(new URL('MANUAL.json',import.meta.url),'utf8'));
export function lookupSourceSeal(o){
 const keys=['sourceID','frameID','sourceClass','target'];
 if(!o||Object.getPrototypeOf(o)!==Object.prototype||Reflect.ownKeys(o).length!==4||keys.some(k=>!Object.hasOwn(o,k)))throw TypeError('Explicit source-group frame required.');
 if(o.sourceID!==manual.sourceID||o.frameID!=='literal-source-group-only')return null;
 const row=manual.rows.find(r=>r.sourceClass===o.sourceClass);if(!row)return null;
 const stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'];
 if(o.target!==null&&(typeof o.target!=='string'||[...o.target].length!==2||!stems.includes(o.target[0])||!branches.includes(o.target[1])||stems.indexOf(o.target[0])%2!==branches.indexOf(o.target[1])%2))throw TypeError('Canonical pillar or explicit null.');
 return Object.freeze({sourceID:o.sourceID,sourceClass:row.sourceClass,target:o.target,
  literalSourceTargets:Object.freeze([...row.targets]),literalTargetMatch:o.target===null?null:row.targets.includes(o.target),
  digitalOnly:true,sourceAnchorMeaning:null,waterEarthSeparateAssignment:null,C19Meaning:null,
  ordinaryTenGod:null,effectiveSeal:null,sourceStrength:null,sourceOutcome:null,
  absenceFromSelectedListEstablishesAdverseOutcome:false,consumerApplied:false,wholeContextApplied:false,newEngineCalls:0});
}
