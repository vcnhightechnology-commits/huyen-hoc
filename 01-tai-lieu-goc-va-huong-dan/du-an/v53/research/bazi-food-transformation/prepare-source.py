"""New private C16 work after the C13/C14 package inventory; do not mutate release inputs."""
from pathlib import Path
from hashlib import sha256
from PIL import Image
import json
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
assert not(B/'PREIMPLEMENTATION_FREEZE.json').exists()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(n,d):(B/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def ident(p):return {'file':p.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
p=W/'v53/research/bazi-food-source/p176.png';box=[535,300,1370,2860]
Image.open(p).convert('RGB').crop(box).save(B/'C16-native.png')
write('CROP_CANDIDATE.json',{'source':ident(p),'crop':ident(B/'C16-native.png'),'boxXYXY':box,'actuallyViewed':False,'newSourcePosition':False})
context=next(x for x in read(W/'v53/research/bazi-food-source/CONTEXTS.json')['records']if x['id']=='FOOD-00-C16')
write('SOURCE_CONTEXT.json',{'sourceID':'TMTH005-FOOD-C16-Xiyin','parent':context,'sourceVoiceName':'希尹',
 'nameIsAttributionInQuotedTextNotVerifiedAuthorIdentity':True,'newHTTPBodies':0,'newSourcePositions':0,'independentWitnesses':0,
 'wholeContextApplied':False,'consumerApplied':False,'packageBoundary':'Created after C13/C14 package inventory. This private C16 work is not claimed in that package or V53 manifest.'})
raw=[('jia-ji','甲巳','甲己','土','丙辛'),('bing-xin','丙辛','丙辛','水','戊癸'),('wu-gui','戊癸','戊癸','火','庚乙'),('geng-yi','庚乙','庚乙','金','壬丁'),('ren-ding','壬丁','壬丁','木','甲巳')]
rows=[]
for i,(id,digital,image,element,target)in enumerate(raw):
 target_image=raw[(i+1)%5][2];target_element=raw[(i+1)%5][3]
 rows.append({'id':id,'digitalPairLiteral':digital,'nativeImageWorkingPair':image,'sourceTransformedElement':element,
 'digitalFoodTargetPairLiteral':target,'nativeImageWorkingFoodTargetPair':target_image,'targetSourceTransformedElement':target_element,
 'sourceClause':digital+'化'+element+'故食'+target,'directedTransformedElementClaim':[element,target_element],
 'allFourOrdinaryStemRelationsAreFoodGod':False,'actualTransformationEstablished':False})
assert all(r['sourceClause']in context['text']for r in rows)
write('MANUAL_PAIR_CYCLE.json',{'sourceID':'TMTH005-FOOD-C16-Xiyin','rows':rows,'closingLiteral':'化氣相尅而食',
 'clauseOrderIsSourceOrder':True,'digitalJiGlyphPolicy':'Digital巳 preserved; image working己 requires explicit native-working policy, not global emendation.',
 'modernPairLabelsAreEditorial':True,'transformedElementsAreReportedSourceDoctrineNotActualNatalTransformation':True,
 'sourceRationaleDoesNotReplaceOrdinaryTenGodRelations':True})
expected=[]
for r in rows:
 for i,a in enumerate(r['nativeImageWorkingPair']):
  for j,t in enumerate(r['nativeImageWorkingFoodTargetPair']):
   god='食神'if i==j else '正官'if i==0 else '正印'
   expected.append({'pairID':r['id'],'root':a,'target':t,'expectedLunar':god,'expectedHHC':{'食神':'Thực Thần','正官':'Chính Quan','正印':'Chính Ấn'}[god],
    'comparisonIsEditorialComponentExpansion':True})
write('EXPECTED_RELATIONS.json',{'rows':expected,'count':20,'foodGodRelations':10,'nonFoodGodRelations':10,'notTwentySourcePrintedSingleStemClaims':True})
# Prefer explicit retained actual results. Do not execute any engines in this planner.
retained=[]
sources=[('v53/qa/bazi-food-core/TEN_RELATION_RESULTS.json','records'),('v53/research/bazi-food-chain/ACTUAL_RUNTIME.json','pairs'),('v53/research/bazi-tongke-cases/ACTUAL_RUNTIME.json','pairs')]
for file,key in sources:
 for index,r in enumerate(read(W/file)[key]):
  if 'declaredCoordinatePair'in r:a,t=(p[0]for p in r['declaredCoordinatePair'])
  elif 'rootPillar'in r:a,t=r['rootPillar'][0],r['targetPillar'][0]
  else:a,t=r['root'],r['target']
  retained.append({'root':a,'target':t,'actualHHC':r['actualHHCTenGod'],'actualLunar':r['actualLunarTenGod'],'file':file,'array':key,'index':index})
reuse=[];missing=[]
for e in expected:
 found=next((r for r in retained if r['root']==e['root']and r['target']==e['target']),None)
 if found:
  assert found['actualHHC']==e['expectedHHC']and found['actualLunar']==e['expectedLunar'];reuse.append({**e,'retained':found})
 else:missing.append(e)
write('RUNTIME_PLAN.json',{'method':'Reuse explicit retained actual coordinate payloads; run only missing component comparisons after manual freeze.',
 'reuse':reuse,'missing':missing,'retainedPayloadIdentities':[ident(W/f)for f,k in sources],
 'noNewCalendarObjects':True,'newHHCRelationCallsPlanned':len(missing),'newLunarTenGodTableQueriesPlanned':len(missing)})
print(json.dumps({'privateAfterInventory':True,'rows':5,'componentComparisons':20,'reusedPairs':len(reuse),'missingPairs':len(missing),'newEngineCallsSoFar':0}))
