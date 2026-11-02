// Private source-case lookup. Exact whole-pillar labels do not redefine Ten Gods.
import{readFileSync}from'node:fs';
const table=JSON.parse(readFileSync(new URL('MANUAL_PILLAR_EXAMPLES.json',import.meta.url),'utf8'));
const stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'];
export const FOOD_PILLAR_SOURCE=table.system;
const canonical=p=>typeof p==='string'&&[...p].length===2&&stems.includes(p[0])&&branches.includes(p[1])&&stems.indexOf(p[0])%2===branches.indexOf(p[1])%2;
export function sourceFoodPillarExample(input){
 const keys=['system','rootPillar','targetPillar','rootBasis'];
 if(input===null||typeof input!=='object'||Object.getPrototypeOf(input)!==Object.prototype||Reflect.ownKeys(input).length!==keys.length||keys.some(k=>!Object.hasOwn(input,k)))throw TypeError('Explicit source and canonical pillar frame required.');
 if(input.system!==FOOD_PILLAR_SOURCE)throw TypeError('Unknown named source.');
 if(!['declared-source-example','natal-day','natal-year','calendar-date','unknown'].includes(input.rootBasis))throw TypeError('Unknown root basis.');
 for(const k of['rootPillar','targetPillar'])if(input[k]!==null&&!canonical(input[k]))throw TypeError('Canonical stem-branch pillar or explicit null required.');
 const frameKnown=input.rootBasis==='declared-source-example'&&input.rootPillar!==null&&input.targetPillar!==null;
 const row=frameKnown&&input.rootPillar===table.sourceRootPillar?table.records.find(x=>x.targetPillar===input.targetPillar):null;
 return {system:FOOD_PILLAR_SOURCE,rootPillar:input.rootPillar,targetPillar:input.targetPillar,rootBasis:input.rootBasis,
 sourceExampleStatus:row?'directly-listed':'not-established',sourceLabels:row?row.sourceLabels.slice():null,
 sourceLabelRole:'historical-whole-pillar-description;not-modern-Ten-God',sourceRootNatalPosition:null,
 modernTenGod:null,modernBranchRelation:null,remainingStemGeneralizationImplemented:false,
 gatheringScore:null,halfMultiplier:null,wholeFoodPatternEstablished:null,strength:null,practicalOutcome:null,consumerApplied:false};
}
