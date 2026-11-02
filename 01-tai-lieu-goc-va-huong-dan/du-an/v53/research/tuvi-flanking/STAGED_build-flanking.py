from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json
b=Path('tmp/tuvi-minor-stars-staging');read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));write=lambda n,x:(b/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
qa=read(b/'QA_IMAGES.json')
for x in qa['records']:
 assert ImageChops.difference(Image.open(b/x['sourceFile']).convert('RGB').crop(x['cropBox']),Image.open(b/x['file']).convert('RGB')).getbbox()is None;x['actuallyViewed']=True;x['pixelIdenticalToSourceCrop']=True
write('QA_IMAGES.json',qa)
write('MANUAL_READINGS.json',dict(date='2026-10-28',system='NAJ-4468520-juan2-QA-flanking-two-neighbours',records=[
 dict(id='general-limit',canvas=39,literal='推吉凶不可一例而斷',role='Methodological constraint, not one-star or one-condition forecasting'),
 dict(id='solar-lunar-flank',canvas=40,literal='假如太陽太陰在身命前後二宮夾命不逢空劫羊殺其貴可矣',role='Selected printed annotation; evaluate only two distinct neighbouring palaces around explicitly declared Ming. Do not assign scope of unqualified 不逢 or validate outcome.'),
 dict(id='chang-qu-flank',canvas=40,literal='如昌曲夾命亦如之',role='Second explicitly named pair. Conditions inherited textually from same clause; no fortune assertion.'),
 dict(id='void-malefic-contrast',canvas=40,literal='夾空夾劫主貧賤夾羊夾陀為乞丐',role='Source heading outcome claims retained historically. Not an equivalence to either favourable geometry or medical/social predictions.')],fullClausesCharacterByCharacterCollated=False,selectedClauseReadingsActuallyViewed=True,sourceExclusionScopeResolved=False,sourceStrengthFullyResolved=False,sourceOutcomeValidated=False,wholeUnitApplied=False))
write('SOURCE_GEOMETRY.json',dict(date='2026-10-28',system='NAJ-4468520-juan2-QA-flanking-two-neighbours',branchOrder=list('子丑寅卯辰巳午未申酉戌亥'),geometryModel='Editorial cyclic12-neighbour encoding of printed 前後二宮; unordered two distinct neighbours. Not source-defined enumeration of0..11.',anchorRole='命宮',pairs=[dict(kind='sun-moon',stars=['Thái Dương','Thái Âm'],iztroNames=['太阳','太阴'],sourceNames=['太陽','太陰']),dict(kind='chang-qu',stars=['Văn Xương','Văn Khúc'],iztroNames=['文昌','文曲'],sourceNames=['文昌','文曲'])],unimplementedSourceConditions=['不逢空劫羊殺 scope and effective obstruction','星格/旺陷/吉化/三合 source preconditions beyond selected clause','身宮 relation not inferred from the phrase 身命','period-frame adapters and source outcomes'],consumerChanged=False,wholeUnitApplied=False))
module="""import{readFileSync}from'node:fs';
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
"""
(b/'source-flanking.mjs').write_text(module,encoding='utf-8')
print('Three native crops verified; two source pairs and unknown-safe flanking API prepared. No runtime verification yet.')
