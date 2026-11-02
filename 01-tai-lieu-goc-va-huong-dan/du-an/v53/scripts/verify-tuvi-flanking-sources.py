from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,sys
r=Path(__file__).resolve().parents[1];w=r.parent;b=r/'research/tuvi-flanking';q=r/'qa/tuvi-flanking';read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
ident=read(b/'PROMOTION_IDENTITIES.json');assert len(ident['records'])==41
for x in ident['records']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'],x['file']
for oldname,result,newname in [('STAGED_test-flanking.mjs','REFERENCE_RESULTS.json','test-tuvi-flanking.mjs'),('STAGED_test-targeted-positives.mjs','TARGETED_POSITIVE_RESULTS.json','test-tuvi-flanking-positives.mjs')]:
 text=(b/oldname).read_text(encoding='utf-8-sig')
 for old,new in [("from'./source-flanking.mjs'","from'../research/tuvi-flanking/source-flanking.mjs'"),("const b=import.meta.dirname,w=resolve(b,'../..'),","const b=resolve(import.meta.dirname,'../research/tuvi-flanking'),w=resolve(b,'../../..'),"),("resolve(b,'"+result+"')","resolve(w,'v53/qa/tuvi-flanking/"+result+"')")]:assert text.count(old)==1;text=text.replace(old,new)
 assert text==(r/'scripts'/newname).read_text(encoding='utf-8')
source=read(b/'SOURCE_MANIFEST.json');assert sha(w/source['manifestFile'])==source['manifestSHA256'];manifest=read(w/source['manifestFile'])['sequences'][0]['canvases'];assert len(manifest)==129
assert len(source['images'])==18 and [x['canvas']for x in source['images']]==list(range(31,49))
for x in source['images']:
 p=b/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'];assert Image.open(p).size==(2200,1659);assert x['status']==200 and x['TLSCertificateValidationEnabled']and x['responseHeadersRetained']and x['actuallyViewed'];assert x['requestedURL']==manifest[x['canvas']-1]['images'][0]['resource']['@id'].replace('/full/max/','/full/2200,/')
assert source['originalJP2BodiesAcquired']==0 and not source['editionYearEstablished']
qa=read(q/'QA_IMAGES.json');assert len(qa['records'])==3
for x in qa['records']:
 assert x['actuallyViewed']and x['pixelIdenticalToSourceCrop']and not x['resampled']and sha(q/x['file'])==x['sha256'];assert ImageChops.difference(Image.open(b/x['sourceFile']).convert('RGB').crop(x['cropBox']),Image.open(q/x['file']).convert('RGB')).getbbox()is None
manual=read(b/'MANUAL_READINGS.json');assert len(manual['records'])==4 and not manual['sourceExclusionScopeResolved']and not manual['sourceOutcomeValidated']and not manual['wholeUnitApplied']
first=read(b/'FIRST_PASS_READINGS.json');assert len(first['records'])==18 and first['juan1EndCanvas']==38 and first['juan2StartsCanvas']==39;assert all(x['actuallyViewed']and not x['wholeConditionalRulesApplied']for x in first['records'])
inv=read(b/'CURRENT_CANVAS_INVENTORY.json');assert len(inv['records'])==129 and sum(bool(x['retainedDerivatives'])for x in inv['records'])==64
for x in inv['records']:
 for y in x['retainedDerivatives']:assert sha(w/y['file'])==y['sha256']
assert inv['counts']['positionsWithoutRetainedDerivativeInThisInventory']==65
res=read(q/'REFERENCE_RESULTS.json');assert len(res['checks'])==7 and all(x['ok']for x in res['checks']);assert res['summary']['actualHHCTuviCalls']==144 and res['summary']['actualIztroNatalCalls']==144 and res['summary']['matchedStarBranchCoordinates']==576
assert res['summary']['exhaustiveKnownGeometries']==3456 and res['summary']['exhaustiveGeometryMatches']==48 and res['summary']['positiveByKind']=={'sun-moon':0,'chang-qu':4}
assert len(res['runtime'])==288 and all(x['hhcStarBranches']==x['iztroStarBranches']and x['hhcMingBranch']==x['iztroMingBranch']and x['result']['fullSourceConditionsMatched']is None and x['result']['practicalOutcome']is None for x in res['runtime'])
assert sha(w/res['actualEngine']['file'])==res['actualEngine']['sha256']=='39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6'
target=read(q/'TARGETED_POSITIVE_RESULTS.json');assert target['actualHHCTuviSearchCalls']==165 and target['actualIztroPositiveCalls']==2 and target['additionalMatchedStarBranchCoordinates']==4 and len(target['positiveCases'])==2
for x in target['positiveCases']:
 assert x['input']['y']==1984 and x['input']['d']==2 and x['ming']==x['iztroMingBranch']=='未'and x['placements']=={'Thái Dương':'申','Thái Âm':'午'}and x['result']['geometryMatched']and x['result']['fullSourceConditionsMatched']is None
assert target['base144ChartsNotRerun']and not target['boundedSearch']['completedDomain']and target['searchCasesAreConstructedModernInputsNotHistoricalExamples']
state=read(b/'WORK_STATE.json');assert state['actualHHCTuviCalls']==309 and state['actualIztroNatalCalls']==146 and state['matchedStarBranchCoordinates']==580 and not state['sourceFullPatternsApplied']and not state['wholeCatalogueCompleted']
out=dict(date='2026-10-28',promotionIdentities=41,baseRuntimeChecks=7,newInstitutionJPEGDerivativeBodies=18,headerSetsRetained=18,firstPassNewPositions=18,nativeCropsViewedPixelMatched=3,juan1EndCanvas=38,juan2StartsCanvas=39,continuousFirstPassPositionsIncludingPrior=48,manifestItemPositions=129,distinctRetainedPositions=64,unretainedPositions=65,selectedSourceReadings=4,namedFlankingPairs=2,knownGeometryContexts=3456,knownGeometryMatches=48,baseRealChartsPerEngine=144,baseFlankingContexts=288,baseMatchedStarBranchCoordinates=576,baseGeometryPositiveSunMoon=0,baseGeometryPositiveChangQu=4,targetedHHCSearchedContexts=165,targetedIztroPositiveCalls=2,targetedPositiveCases=2,targetedDistinctGeometryShapes=1,actualHHCTuviCalls=309,actualIztroNatalCalls=146,totalMatchedStarBranchCoordinates=580,base144CasesNotRerun=True,sourceExclusionScopeResolved=False,fullSourceConditionsValidated=False,sourceOutcomesValidated=False,originalJP2Bodies=0,consumerChanged=False,wholeCatalogueCompleted=False)
p=q/'SOURCE_RESULTS.json'
if '--no-write'in sys.argv:assert read(p)==out
else:p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
