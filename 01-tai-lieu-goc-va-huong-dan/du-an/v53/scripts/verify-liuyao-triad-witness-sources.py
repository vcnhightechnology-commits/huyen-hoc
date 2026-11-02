from pathlib import Path
from hashlib import sha256
import json,sys,subprocess
from PIL import Image,ImageChops
v=Path(__file__).resolve().parent.parent;w=v.parent;r=v/'research/liuyao-triad-witness';q=v/'qa/liuyao-triad-witness'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def identity(p,x):
 b=p.read_bytes();assert len(b)==x['bytes']and sha256(b).hexdigest()==x['sha256'],str(p)
def mapped(p):return r/Path(p).name if p.startswith('tmp/liuyao-triad-witness-staging/')else w/p
promo=read(r/'PROMOTION_IDENTITIES.json')
for x in promo['files']:identity(r/x['file'],x)
assert (r/'witness-triad-reference.mjs').read_text(encoding='utf-8')==(r/'STAGED_witness-triad-reference.mjs').read_text(encoding='utf-8').replace('../../v53/research/liuyao-combination-context/','../liuyao-combination-context/')
for x in read(r/'UNCHANGED_DEPENDENCIES.json')['files']:identity(w/x['file'],x)
ws=read(r/'WORK_STATE.json')
for x in ws['inheritedMetadata']:identity(w/x['file'],x);identity(r/('INHERITED_'+Path(x['file']).name),x)
new=read(r/'REQUESTS.json')['records'];old=read(r/'INHERITED_REQUESTS.json')['records']
assert len(new)==4 and not ({x['url']for x in new}&{x['url']for x in old})
manifest=read(r/'INHERITED_japan-volume2-manifest.json');canvases=manifest['sequences'][0]['canvases'];assert len(canvases)==53
urls={x['images'][0]['resource']['@id']for x in canvases}
for x in new:
 assert x['status']==200 and x['tls']['authorized']is True and x['nodeHTTPSDefaultCertificateValidationEnforced']is True
 assert x['retrievedUTC'].startswith('2026-10-29T')and x['url']in urls;identity(r/x['file'],x)
 assert Image.open(r/x['file']).size==(3000,2073)
assert read(r/'REQUESTS.json')['date']=='2026-10-27'and read(r/'REQUEST_DATE_AUDIT.json')['sourceLedgerHeaderNotSilentlyChangedAfterFreeze']
dimensions=read(r/'DIMENSION_AUDIT.json')['records'];assert len(dimensions)==4
for x in dimensions:assert x['returnedDimensions']==[3000,2073]and x['manifestDimensions']==[6150,4250]and not x['jp2OriginalAcquired']
accepted=0;excluded=0
for x in read(r/'NATIVE_CROPS.json')['records']:
 identity(mapped(x['source']['file']),x['source']);identity(mapped(x['crop']['file']),x['crop']);assert x['viewed']
 if not x['accepted']:assert x['exclusionReason'];excluded+=1;continue
 a=Image.open(mapped(x['source']['file'])).convert('RGB').crop(x['boxXYXY']);b=Image.open(mapped(x['crop']['file'])).convert('RGB')
 assert ImageChops.difference(a,b).getbbox()is None;accepted+=1
assert accepted==3 and excluded==1
f=read(r/'PREIMPLEMENTATION_FREEZE.json');assert not f['implementationExists']
for x in f['files']:identity(r/x['file'],x)
m=read(r/'MANUAL_WITNESS_COLLATION.json');assert len(m['selectedComparisons'])==3
assert m['selectedComparisons'][0]['JapanDiplomatic']=='一卦之內有三交動而合局者一也'
assert m['selectedComparisons'][0]['NLCDiplomatic']=='一卦之內有一交動而合局者一也'
runtime=read(r/'ACTUAL_RUNTIME.json');identity(v/'engine.js',next(x for x in read(r/'UNCHANGED_DEPENDENCIES.json')['files']if x['file']=='v53/engine.js'))
assert runtime['successfulCalls']==2 and runtime['primaryNumber']==2 and runtime['changedNumber']==63
assert not runtime['sourcePrintedCast']and not runtime['sourceOutcomesValidated']
proc=subprocess.run(['node',str(r/'test-witness-triad.mjs')],capture_output=True,text=True,encoding='utf-8',check=True)
tests=json.loads(proc.stdout);assert tests==read(r/'REFERENCE_RESULTS.json')==read(q/'REFERENCE_RESULTS.json')
out={'date':'2026-10-29','passed':True,'promotionIdentitiesVerified':len(promo['files']),'HTTP200BodiesWithObservedAuthorizedTLS':4,'newArchiveImagePositions':4,'newNLCPositions':0,'navigationOnlyPositions':2,'targetPositions':2,'newOriginalJP2OrPDFContainers':0,'newIndependentTransmissionEstablished':False,'acceptedNativeCropsRGBMatched':accepted,'excludedTrialCrops':excluded,'preimplementationFrozenFilesUnchanged':5,'selectedSourceComparisons':3,'oldNLCModuleAndMapUnchanged':True,'deployedModuleOnlyImportPrefixChanged':True,'requestLedgerHeaderDateDisclosed':True,'actualSuccessfulHHCHexCalls':2,'newIndependentPrintedCasts':0,'engineNotReexecutedDuringSourceQA':True,'referenceTests':tests,'consumerChanged':False,'wholeCatalogueCompleted':False}
if '--no-write'in sys.argv:assert read(q/'SOURCE_RESULTS.json')==out
else:(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
