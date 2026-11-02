// A source-qualified label bridge. C19 remains unresolved, even when C18 prints the same graph.
import{readFileSync,existsSync}from'node:fs';import path from'node:path';import{pathToFileURL}from'node:url';
let w=import.meta.dirname;while(!existsSync(path.join(w,'v53/engine.js'))){const p=path.dirname(w);if(p===w)throw Error('Workspace');w=p;}
const {sourceFoodPillarExample,FOOD_PILLAR_SOURCE}=await import(pathToFileURL(path.join(w,'v53/research/bazi-food-six-pillars/source-pillar-example.mjs')));
const retained=JSON.parse(readFileSync(new URL('REUSE.json',import.meta.url),'utf8')).actualRelation;
const freeze=x=>{if(x&&typeof x==='object'){Object.values(x).forEach(freeze);Object.freeze(x);}return x;};
export function inspectSourceZhengYin(o){
 const keys=['sourceID','contextID','root','target','basis'];
 if(!o||Object.getPrototypeOf(o)!==Object.prototype||Reflect.ownKeys(o).length!==keys.length||keys.some(k=>!Object.hasOwn(o,k)))throw TypeError('Exact source/context/coordinate/basis required.');
 if(o.sourceID!=='TMTH005-food-source-label-scope'||!['FOOD-00-C18','FOOD-00-C19'].includes(o.contextID))return null;
 let source=null,ordinary=null;
 if(o.contextID==='FOOD-00-C19'){
  if(o.root!==null||o.target!==null||o.basis!=='unresolved-source-clause')throw TypeError('C19 has no adjudicated root/target coordinate.');
 }else{
  source=sourceFoodPillarExample({system:FOOD_PILLAR_SOURCE,rootPillar:o.root,targetPillar:o.target,rootBasis:o.basis});
  if(source.sourceExampleStatus==='directly-listed')ordinary={...retained};
 }
 return freeze({sourceID:o.sourceID,contextID:o.contextID,root:o.root,target:o.target,basis:o.basis,
  literalLabel:source?.sourceLabels?.includes('正印')?'正印':null,
  labelNamespace:source?.sourceLabels?.includes('正印')?'C18-whole-pillar-description':null,
  sourceExample:source,retainedOrdinaryRelation:ordinary,ordinaryRelation:ordinary?.actualLunarTenGod??null,
  sameWrittenLabelEstablishesSameMeaning:false,C19Meaning:null,C19MapsToC18:null,C19MapsToOrdinaryTenGod:null,
  ordinaryZhengYinDetected:null,sourceStrength:null,gatheringScore:null,halfMultiplier:null,sourceOutcome:null,
  newEngineCalls:0,consumerApplied:false,wholeContextApplied:false});
}
