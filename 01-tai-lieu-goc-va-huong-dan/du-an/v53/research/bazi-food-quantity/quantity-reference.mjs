// Literal C23 count exemplars only; missing slots share a constrained count domain.
import{readFileSync}from'node:fs';
const read=n=>JSON.parse(readFileSync(new URL(n,import.meta.url),'utf8'));
const relation=read('REUSE_IDENTITIES.json').actualRetainedPair;
export const SOURCE_ID='TMTH005-FOOD-C23-Huzhongzi',FRAME_ID='visible-literal-quantity-examples';
const stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'],roles=['year','month','day','hour'];
const freeze=x=>{if(x&&typeof x==='object'){Object.values(x).forEach(freeze);Object.freeze(x);}return x;};
const exact=(o,keys)=>{if(!o||Object.getPrototypeOf(o)!==Object.prototype||Reflect.ownKeys(o).length!==keys.length||keys.some(k=>!Object.hasOwn(o,k)))throw TypeError('Exact explicit source fields required.');};
export function inspectFoodQuantityExamples(o){
 exact(o,['sourceID','frameID','sourceAnchorStem','sourceAnchorRole','pillars']);
 if(o.sourceID!==SOURCE_ID||o.frameID!==FRAME_ID||o.sourceAnchorStem!=='甲'||o.sourceAnchorRole!=='unassigned-in-source')return null;
 if(!Array.isArray(o.pillars)||o.pillars.length!==4||Reflect.ownKeys(o.pillars).length!==5||[0,1,2,3].some(i=>!Object.hasOwn(o.pillars,i)))throw TypeError('Four explicit canonical pillars or null required.');
 const jia=[],bing=[],missing=[];
 for(let i=0;i<4;i++){const p=o.pillars[i];if(p===null){missing.push(roles[i]);continue;}
  const chars=typeof p==='string'?[...p]:[];
  if(chars.length!==2||!stems.includes(chars[0])||!branches.includes(chars[1])||stems.indexOf(chars[0])%2!==branches.indexOf(chars[1])%2)throw TypeError('Noncanonical pillar.');
  if(chars[0]==='甲')jia.push(roles[i]);if(chars[0]==='丙')bing.push(roles[i]);}
 const configurations=[];
 for(let j=0;j<=missing.length;j++)for(let b=0;b<=missing.length-j;b++)configurations.push({jia:jia.length+j,bing:bing.length+b,other:4-jia.length-bing.length-j-b});
 const tri=predicate=>{const values=configurations.map(predicate);return values.every(Boolean)?true:values.some(Boolean)?null:false;};
 return freeze({sourceID:SOURCE_ID,frameID:FRAME_ID,sourceVoiceName:'壺中子',sourceAnchorStem:'甲',sourceAnchorRole:null,
  pillars:[...o.pillars],visibleJiaPositions:jia,visibleBingPositions:bing,unknownPillarPositions:missing,
  visibleJiaCountLowerBound:jia.length,visibleBingCountLowerBound:bing.length,
  possibleVisibleJiaCountRange:[jia.length,jia.length+missing.length],possibleVisibleBingCountRange:[bing.length,bing.length+missing.length],
  jointlyPossibleStemCountConfigurations:configurations,
  sourceAnchorVisibleSomewhere:tri(c=>c.jia>=1),
  literalMatches:{exactlyTwoBing:tri(c=>c.bing===2),exactlyThreeBing:tri(c=>c.bing===3),
   sourceSurplusLiteralExample:tri(c=>c.jia>=1&&(c.bing===2||c.bing===3)),
   sourceShortageLiteralExample:tri(c=>c.jia===2&&c.bing===1)},
  retainedActualFoodRelation:{root:'甲',target:'丙',actualHHCTenGod:relation.actualHHCTenGod,actualLunarTenGod:relation.actualLunarTenGod},
  genericFoodCountThreshold:null,effectiveFoodSurplus:null,effectiveFoodShortage:null,
  oneUsableVersusThreeIdleStrengthComparison:null,C21NumericalMultiplier:null,C19BlessingMisfortuneScore:null,
  hiddenFoodCount:null,dayMasterAnchorChosen:null,overallPattern:null,wealthPrediction:null,
  healthPrediction:null,familyPrediction:null,sourceOutcome:null,overallFortune:null,
  literalExampleMatchEstablishesOutcome:false,quantityMatchDefinesAllManyFewUses:false,
  sourceClaimsAreHistorical:true,newEngineCalls:0,consumerApplied:false,wholeContextApplied:false});
}
