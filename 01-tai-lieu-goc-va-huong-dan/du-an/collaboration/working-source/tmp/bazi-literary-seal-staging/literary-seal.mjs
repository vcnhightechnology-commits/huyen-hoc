import{readFileSync}from'node:fs';
const read=n=>JSON.parse(readFileSync(new URL(n,import.meta.url),'utf8')),manual=read('MANUAL.json'),runtime=read('ACTUAL_RUNTIME.json');
export const SOURCE_ID=manual.sourceID;
const freeze=x=>{if(x&&typeof x==='object'){Object.values(x).forEach(freeze);Object.freeze(x);}return x;};freeze(manual);freeze(runtime);
const stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'];
const canonical=p=>typeof p==='string'&&[...p].length===2&&stems.includes(p[0])&&branches.includes(p[1])&&stems.indexOf(p[0])%2===branches.indexOf(p[1])%2;
const controls=(a,b)=>({木:'土',土:'水',水:'火',火:'金',金:'木'})[a]===b;
const ny=p=>[...runtime.newNaYin,...runtime.reusedNaYin].find(r=>r.pillar===p);
const el=s=>[...runtime.newStemElements,...runtime.reusedStemElements].find(r=>r.stem===s);
export function inspectLiterarySealPair(o){
 const keys=['sourceID','root','target','rootBasis'];
 if(!o||Object.getPrototypeOf(o)!==Object.prototype||Reflect.ownKeys(o).length!==4||keys.some(k=>!Object.hasOwn(o,k)))throw TypeError('Exact named source coordinate frame required.');
 if(o.sourceID!==SOURCE_ID||o.rootBasis!=='unassigned-source-example')return null;
 for(const p of [o.root,o.target])if(p!==null&&!canonical(p))throw TypeError('Canonical pillar or explicit null required.');
 const row=manual.rows.find(r=>r.root===o.root&&r.target===o.target)??null;
 let comparison=null;
 if(row){const a=ny(row.root),t=ny(row.target),ae=el(row.root[0]),te=el(row.target[0]),partner=runtime.reusedBranchPartners.find(r=>r.branch===row.root[1]);
  if(!a||!t||!ae||!te||!partner)throw Error('Retained actual coordinate missing.');
  comparison={rootNaYin:a.actual,targetNaYin:t.actual,rootStemElement:ae.actual,targetStemElement:te.actual,
   targetNaYinControlsRoot:controls(t.actual.at(-1),a.actual.at(-1)),rootStemControlsTarget:controls(ae.actual,te.actual),
   targetStemControlsRoot:controls(te.actual,ae.actual),branchSixUnion:partner.actual===row.target[1],
   NaYinPayloadReuse:[!a.newCall,!t.newCall],stemPayloadReuse:[!ae.newCall,!te.newCall],
   comparisonIsEditorialOrdinaryElementReading:true};}
 return freeze({sourceID:SOURCE_ID,root:o.root,target:o.target,rootBasis:o.rootBasis,
  sourceExampleStatus:row?'directly-listed':'not-established',sourceGroup:row?.group??null,
  sourceMechanismPhrase:row?.sourceMechanismPhrase??null,retainedCoordinateComparison:comparison,
  sourceStemControlDirectionAdjudicated:null,sourceMechanismMeaning:null,
  sourceRootNatalRole:null,unlistedPairRefuted:null,sourceGlyphCorrection:null,
  effectiveSeal:null,sourceStrength:null,wholeWenzhangYinClassification:null,
  practicalLearningOutcome:null,wealthPrediction:null,sourceOutcome:null,
  coordinateDisagreementRefutesSource:false,consumerApplied:false,wholeContextApplied:false,newEngineCalls:0});
}
