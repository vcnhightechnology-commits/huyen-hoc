// C13 source-local premise inspection. No calendar conversion or strength scoring.
import {readFileSync,existsSync} from 'node:fs';
import path from 'node:path';
const read=p=>JSON.parse(readFileSync(p,'utf8'));
const frame=read(new URL('DECLARED_FRAME.json',import.meta.url));
let workspace=import.meta.dirname;
while(!existsSync(path.join(workspace,'v53/engine.js'))){const p=path.dirname(workspace);if(p===workspace)throw Error('Workspace not found.');workspace=p;}
const retained=read(path.join(workspace,'v53/research/bazi-food-chain/ACTUAL_RUNTIME.json'));
const pair=retained.pairs.find(r=>r.root==='甲'&&r.target==='丙');
if(!pair)throw Error('Retained actual fixed relation missing.');
export const SOURCE_ID='TMTH005-FOOD-C13',FRAME_ID='declared-source-strength-context';
const stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'];
const freeze=x=>{if(x&&typeof x==='object'){Object.values(x).forEach(freeze);Object.freeze(x);}return x;};
const exact=(o,keys)=>{if(!o||Object.getPrototypeOf(o)!==Object.prototype||Reflect.ownKeys(o).length!==keys.length||keys.some(k=>!Object.hasOwn(o,k)))throw TypeError('Exact explicit fields required.');};
const and=(...v)=>v.includes(false)?false:v.includes(null)?null:true;
const equals=(x,y)=>x===null?null:x===y;
export function inspectFoodStrengthContext(o){
 exact(o,['sourceID','frameID','pillars','sourceBirthSeason','sourceLuckRegion','declaredFacts']);
 if(o.sourceID!==SOURCE_ID||o.frameID!==FRAME_ID)return null;
 if(!Array.isArray(o.pillars)||o.pillars.length!==4||Reflect.ownKeys(o.pillars).length!==5||[0,1,2,3].some(i=>!Object.hasOwn(o.pillars,i)))throw TypeError('Four explicit canonical pillars or null required.');
 for(const p of o.pillars){if(p===null)continue;const chars=typeof p==='string'?[...p]:[];
  if(chars.length!==2||!stems.includes(chars[0])||!branches.includes(chars[1])||stems.indexOf(chars[0])%2!==branches.indexOf(chars[1])%2)throw TypeError('Noncanonical pillar.');}
 if(!frame.sourceBirthSeason.includes(o.sourceBirthSeason)||!frame.sourceLuckRegion.includes(o.sourceLuckRegion))throw TypeError('Explicit source season/region required.');
 exact(o.declaredFacts,frame.requiredFacts);
 if(Object.values(o.declaredFacts).some(v=>v!==true&&v!==false&&v!==null))throw TypeError('Declared facts must be boolean or explicit null.');
 const f=o.declaredFacts,markers=[];
 for(let i=0;i<4;i++){const p=o.pillars[i];if(p===null)continue;
  if('壬癸'.includes(p[0]))markers.push({pillar:frame.pillarOrder[i],slot:'stem',literal:p[0]});
  if('亥子'.includes(p[1]))markers.push({pillar:frame.pillarOrder[i],slot:'branch',literal:p[1]});}
 const literalAbsence=markers.length?false:o.pillars.includes(null)?null:true;
 const day=o.pillars[2]===null?null:o.pillars[2][0],jia=equals(day,'甲');
 const continuing=and(jia,f.bingWaterRestraintAbsent,f.continuingShengWangXiangLuSatisfied);
 const summer=equals(o.sourceBirthSeason,'summer'),spring=equals(o.sourceBirthSeason,'three-spring');
 return freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,parentContext:'FOOD-00-C13',
  visiblePillars:[...o.pillars],visibleLiteralWaterMarkers:markers,
  fourVisiblePillarsKnown:!o.pillars.includes(null),specifiedVisibleWaterMarkersAbsent:literalAbsence,
  declaredSourceBirthSeason:o.sourceBirthSeason,declaredSourceLuckRegion:o.sourceLuckRegion,
  declaredFacts:{...f},dayStem:day,selectedJiaExample: jia,
  retainedActualFoodPair:{...pair},foodRelationChecksReused:true,
  declaredPremiseMatches:{openingLiteralAbsence:and(jia,literalAbsence),
   waterRestraintBranch:and(jia,f.bingWaterRestraintAbsent===null?null:!f.bingWaterRestraintAbsent),
   continuingRequirements:continuing,
   summerRequirements:and(continuing,summer,equals(o.sourceLuckRegion,'東南'),f.fireStrong,f.earthStrong),
   springContrast:and(jia,spring,f.jiaStrong,f.bingReceivesGeneration,f.wuJiQiThin),
   springSouthernRequirements:and(continuing,spring,equals(o.sourceLuckRegion,'南方'),f.fireStrong,f.earthStrong)},
  sourcePhraseSubjectBinding:{shengWangXiangLu:null},
  sourceGlyphPolicy:'Digital戊巳/巳身 preserved; local native-image working readings戊己/己身 recorded separately.',
  effectiveWaterAbsenceInferredFromMarkers:null,hiddenWaterAbsence:null,calendarSeason:null,
  calculatedDayStrength:null,calculatedFoodStrength:null,calculatedEarthStrength:null,
  effectiveFoodGenerationOfWealth:null,wealthAmount:null,healthPrediction:null,
  overallPattern:null,overallFortune:null,sourceOutcome:null,
  sourceClaimsAreHistorical:true,premiseMatchesValidateOutcomes:false,
  newEngineCalls:0,consumerApplied:false,wholeContextApplied:false});
}
