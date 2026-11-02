import{readFileSync}from'node:fs';
const source=JSON.parse(readFileSync(new URL('./SOURCE_GEOMETRY.json',import.meta.url),'utf8')),branches=source.branchOrder;
function branchValue(x){if(x!==null&&!branches.includes(x))throw new TypeError('Explicit canonical branch or null required');return x===null?null:branches.indexOf(x);}
export function inspectSourceFlanking({system,kind,anchorRole,anchorBranch,placements}={}){
 if(system!==source.system||anchorRole!=='命宮')throw new TypeError('Named source and explicit Ming anchor required');
 const pair=source.pairs.find(x=>x.kind===kind);if(!pair)throw new TypeError('Unknown source pair');
 if(!placements||typeof placements!=='object'||Array.isArray(placements)||Object.keys(placements).length!==2||!pair.stars.every(x=>Object.hasOwn(placements,x)))throw new TypeError('Exactly the two source stars with explicit nulls required');
 const a=branchValue(anchorBranch),positions=pair.stars.map(star=>({star,index:branchValue(placements[star])}));
 let geometryMatched=null;
 if(a!==null){const known=positions.filter(x=>x.index!==null),neighbours=[(a+11)%12,(a+1)%12];
  if(known.some(x=>!neighbours.includes(x.index)))geometryMatched=false;
  else if(known.length===2)geometryMatched=positions[0].index!==positions[1].index;
 }
 return{system,kind,anchorRole,anchorBranch,pair:structuredClone(pair),geometryMatched,
  placements:positions.map(x=>({star:x.star,branch:x.index===null?null:branches[x.index],offsetFromMing:a===null||x.index===null?null:(x.index-a+12)%12})),
  fullSourceConditionsMatched:null,sourceExclusionScopeResolved:false,starStrengthResolved:false,sourceOutcomeValidated:false,practicalOutcome:null,
  unimplementedSourceConditions:structuredClone(source.unimplementedSourceConditions),geometryIsNotWholePattern:true};
}
