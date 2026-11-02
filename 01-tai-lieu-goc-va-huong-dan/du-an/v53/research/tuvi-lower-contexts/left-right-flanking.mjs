import{readFileSync}from'node:fs';
const source=JSON.parse(readFileSync(new URL('./SOURCE_FLANKING_CLAUSE.json',import.meta.url),'utf8')),branches=source.branchOrder;
export const LEFT_RIGHT_SOURCE=source.system;
function index(x){if(x===null)return null;if(!branches.includes(x))throw new TypeError('Canonical branch or explicit null required');return branches.indexOf(x);}
export function inspectLeftRightFlanking({system,anchorRole,anchorBranch,placements}={}){
 if(system!==source.system||anchorRole!=='命宮')throw new TypeError('Named source and Ming anchor required');
 if(!placements||Array.isArray(placements)||typeof placements!=='object'||Object.keys(placements).length!==2||!source.namedStars.every(s=>Object.hasOwn(placements,s)))throw new TypeError('Exactly two named placements required');
 const a=index(anchorBranch),values=source.namedStars.map(s=>index(placements[s]));let geometryMatched=null;
 if(a!==null){const neighbours=[(a+11)%12,(a+1)%12];if(values.some(v=>v!==null&&!neighbours.includes(v)))geometryMatched=false;else if(values.every(v=>v!==null))geometryMatched=values[0]!==values[1];}
 return{system,anchorRole,anchorBranch,placements:structuredClone(placements),geometryMatched,fullPatternMatched:null,sourceOutcomeValidated:false,practicalOutcome:null,notYetResolved:structuredClone(source.notYetResolved)};
}
