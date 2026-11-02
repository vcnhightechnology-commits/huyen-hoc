from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,sys
r=Path(__file__).resolve().parents[1];w=r.parent;b=r/'research/tuvi-ming-shen';q=r/'qa/tuvi-ming-shen';read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
ident=read(b/'PROMOTION_IDENTITIES.json');assert len(ident['records'])==46
for x in ident['records']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'],x['file']
text=(b/'STAGED_test-ming-shen.mjs').read_text(encoding='utf-8-sig')
for old,new in [("from'./source-ming-shen.mjs'","from'../research/tuvi-ming-shen/source-ming-shen.mjs'"),("const b=import.meta.dirname,w=resolve(b,'../..'),","const b=resolve(import.meta.dirname,'../research/tuvi-ming-shen'),w=resolve(b,'../../..'),"),("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/tuvi-ming-shen/REFERENCE_RESULTS.json')")]:assert text.count(old)==1;text=text.replace(old,new)
assert text==(r/'scripts/test-tuvi-ming-shen.mjs').read_text(encoding='utf-8')
source=read(b/'SOURCE_MANIFEST.json');assert sha(w/source['manifestFile'])==source['manifestSHA256'];manifest=read(w/source['manifestFile'])['sequences'][0]['canvases'];assert len(manifest)==129
assert len(source['images'])==25 and [x['canvas']for x in source['images']]==list(range(49,74))
for x in source['images']:
 p=b/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'];assert Image.open(p).size==(2200,1659);assert x['status']==200 and x['TLSCertificateValidationEnabled']and x['responseHeadersRetained']and x['actuallyViewed'];assert x['requestedURL']==manifest[x['canvas']-1]['images'][0]['resource']['@id'].replace('/full/max/','/full/2200,/')
assert source['originalJP2BodiesAcquired']==0 and not source['editionYearEstablished']
qa=read(q/'QA_IMAGES.json');assert len(qa['records'])==3
for x in qa['records']:
 assert x['actuallyViewed']and x['pixelIdenticalToSourceCrop']and not x['resampled']and sha(q/x['file'])==x['sha256'];assert ImageChops.difference(Image.open(b/x['sourceFile']).convert('RGB').crop(x['cropBox']),Image.open(q/x['file']).convert('RGB')).getbbox()is None
manual=read(b/'MING_SHEN_READINGS.json');assert len(manual['records'])==6 and manual['leapFirstMonthHourYinExampleAttested']and not manual['generalLeapMonthMappingForAllMonthsResolved'];assert next(x for x in manual['records']if x['id']=='leap-premise')['literal']=='又若閏正月生寅時逆轉子安命順至辰安身'
first=read(b/'FIRST_PASS_READINGS.json');assert len(first['records'])==25 and first['juan2LastTextCanvas']==73 and first['juan3TitleAndOpeningCanvas']==73;assert all(x['actuallyViewed']and not x['wholeConditionalRulesApplied']for x in first['records']);assert 'provisionalNoteCorrection'in first['records'][-1]
inv=read(b/'CURRENT_CANVAS_INVENTORY.json');assert len(inv['records'])==129 and sum(bool(x['retainedDerivatives'])for x in inv['records'])==89
for x in inv['records']:
 for y in x['retainedDerivatives']:assert sha(w/y['file'])==y['sha256']
assert inv['counts']['positionsWithoutRetainedDerivativeInThisInventory']==40
res=read(q/'REFERENCE_RESULTS.json');assert len(res['checks'])==7 and all(x['ok']for x in res['checks']);assert res['summary']['actualHHCTuviCalls']==144 and res['summary']['actualIztroNatalCalls']==144 and res['summary']['matchedSourceBranchCoordinates']==288
assert res['summary']['printedRegularExamples']==3 and res['summary']['printedLeapSpecificExamples']==1
assert len(res['runtime'])==144 and all(x['source']['mingBranch']==x['hhcMing']==x['iztroMing']and x['source']['shenBranch']==x['hhcShen']==x['iztroShen']and x['source']['practicalOutcome']is None and x['input']['y']==1985 and x['input']['d']==10 and not x['input']['leap']for x in res['runtime'])
assert {(x['input']['m'],x['source']['hourBranch'])for x in res['runtime']}=={(m,h)for m in range(1,13)for h in '子丑寅卯辰巳午未申酉戌亥'}
assert sha(w/res['actualEngine']['file'])==res['actualEngine']['sha256']=='39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6'
labels=read(b/'FLANKING_LABEL_DISPOSITIONS.json');assert len(labels['rows'])==9 and sum(x['sourceGroup']=='夾貴'for x in labels['rows'])==6 and sum(x['sourceGroup']=='夾敗'for x in labels['rows'])==3
assert not next(x for x in labels['rows']if x['id']=='ke-quan-lu')['sourceSimplePairResolved']and not next(x for x in labels['rows']if x['id']=='void-robbery')['sourceSimplePairResolved'];assert all(not x['fullPatternImplemented']for x in labels['rows'])
state=read(b/'WORK_STATE.json');assert not state['wholeChapterApplied']and not state['wholeCatalogueCompleted']and not state['sourceGeneralLeapPolicyResolved']
out=dict(date='2026-10-28',promotionIdentities=46,completeRuntimeChecks=7,newInstitutionJPEGDerivativeBodies=25,headerSetsRetained=25,firstPassNewPositions=25,nativeCropsViewedPixelMatched=3,juan2LastTextCanvas=73,juan3StartsCanvas=73,continuousFirstPassPositionsIncludingPrior=73,manifestItemPositions=129,distinctRetainedPositions=89,unretainedPositions=40,selectedSourceReadings=6,printedRegularMonth1Examples=3,printedLeap1YinSpecificExamples=1,regularSourceMonthHourCoordinates=144,actualHHCTuviCalls=144,actualIztroNatalCalls=144,matchedMingShenBranchCoordinates=288,generalLeapPolicyResolved=False,calendarAndClockAdaptersImplemented=False,flankingFavourableLabels=6,flankingAdverseLabels=3,threeTransformLabelNotCollapsedToPair=True,voidIdentityUnresolved=True,sourceOutcomesValidated=False,originalJP2Bodies=0,consumerChanged=False,wholeCatalogueCompleted=False)
p=q/'SOURCE_RESULTS.json'
if '--no-write'in sys.argv:assert read(p)==out
else:p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
