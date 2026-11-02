import {readFileSync} from 'node:fs';
const table=JSON.parse(readFileSync(new URL('./SOURCE_TABLES.json',import.meta.url),'utf8'));
const branches=[...'子丑寅卯辰巳午未申酉戌亥'];
const palaces=['命宮','兄弟','夫妻','子女','財帛','疾厄','遷移','交友','官祿','田宅','福德','父母'];
function rowFor({system,star}={}){
 if(system!==table.system||typeof star!=='string')throw new TypeError('Explicit named source and canonical Vietnamese star are required');
 const row=table.rows.find(x=>x.vietnameseStar===star);if(!row)throw new TypeError('Unknown source star');return row;
}
export function sourceStarProfile(input){
 const row=rowFor(input);return {...structuredClone(row),system:table.system,officeIsPlacementConstraint:false,physicalPalaceInferred:false,practicalOutcome:null,elementScore:null,fullChapterApplied:false};
}
export function attachDeclaredPlacement(input){
 const p=sourceStarProfile(input),{branch,palace}=input;
 if(branch===undefined||palace===undefined)throw new TypeError('Placement branch and palace must be explicit, including null');
 if(branch!==null&&!branches.includes(branch))throw new TypeError('Canonical branch or null required');
 if(palace!==null&&!palaces.includes(palace))throw new TypeError('Canonical palace or null required');
 if(branch===null&&palace!==null)throw new TypeError('A palace cannot be attached without a known branch');
 return {...p,declaredPlacement:{branch,palace,known:branch!==null,provenance:'caller-supplied, not inferred from symbolic office'},officeReplacesPhysicalPlacement:false};
}
