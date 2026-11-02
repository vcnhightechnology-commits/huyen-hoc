from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,sys,tarfile
r=Path(__file__).resolve().parents[1];w=r.parent;b=r/'research/tuvi-star-offices';q=r/'qa/tuvi-star-offices'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
ident=read(b/'PROMOTION_IDENTITIES.json');assert len(ident['records'])==69
for x in ident['records']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'],x['file']
text=(b/'STAGED_test-star-offices.mjs').read_text(encoding='utf-8-sig')
for old,new in [("from'./star-office-reference.mjs'","from'../research/tuvi-star-offices/star-office-reference.mjs'"),("const b=import.meta.dirname,w=resolve(b,'../..'),read=","const b=resolve(import.meta.dirname,'../research/tuvi-star-offices'),w=resolve(b,'../../..'),read="),("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/tuvi-star-offices/REFERENCE_RESULTS.json')")]:assert text.count(old)==1;text=text.replace(old,new)
assert text==(r/'scripts/test-tuvi-star-offices.mjs').read_text(encoding='utf-8')
source=read(b/'SOURCE_MANIFEST.json');assert sha(w/source['manifestFile'])==source['manifestSHA256']
manifest=read(w/source['manifestFile'])['sequences'][0]['canvases'];assert len(manifest)==129
assert len(source['images'])==30;headers=0
for x in source['images']:
 p=b/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'];assert Image.open(p).size==(2200,1659)
 assert x['status']==200 and x['TLSCertificateValidationEnabled']and x['actuallyViewed']
 assert x['requestedURL']==manifest[x['canvas']-1]['images'][0]['resource']['@id'].replace('/full/max/','/full/2200,/')
 headers+=bool(x['responseHeadersRetained'])
assert headers==29 and not source['editionYearEstablished']and source['originalJP2BodiesAcquired']==0
failed=read(b/'REQUESTS.json')['records'];assert len(failed)==12 and all(x['TLSCertificateValidationEnabled']and not x['bodyRetained']and 'CERTIFICATE_VERIFY_FAILED'in x['error']for x in failed)
count=0
for f in ['QA_IMAGES.json','QA_STAR_IMAGES.json']:
 for x in read(q/f)['records']:
  assert x['actuallyViewed']and not x['resampled']and sha(q/x['file'])==x['sha256']
  assert ImageChops.difference(Image.open(b/x['sourceFile']).convert('RGB').crop(x['cropBox']),Image.open(q/x['file']).convert('RGB')).getbbox()is None;count+=1
assert count==13
manual=read(b/'FIRST_PASS_READINGS.json');assert len(manual['records'])==30 and [x['canvas']for x in manual['records']]==list(range(1,31));assert all(x['actuallyViewed']and not x['wholeConditionalRulesApplied']for x in manual['records'])
inv=read(b/'CURRENT_CANVAS_INVENTORY.json');assert len(inv['records'])==129
assert sum(bool(x['retainedDerivatives'])for x in inv['records'])==46
for x in inv['records']:
 for y in x['retainedDerivatives']:assert sha(w/y['file'])==y['sha256']
assert inv['counts']['positionsWithoutRetainedDerivativeInThisInventory']==83
units=read(b/'SOURCE_DISPOSITIONS.json')['units'];assert len(units)==22 and all(not x['wholeUnitApplied']for x in units)
table=read(b/'SOURCE_TABLES.json');assert len(table['rows'])==14 and len([y for x in table['rows']for y in x['elementClaims']])==15
assert next(x for x in table['rows']if x['sourceName']=='廉貞')['elementClaims'][0]['elements']==['木']
assert not read(b/'READING_CORRECTIONS.json')['consumerEverAffected']
res=read(q/'REFERENCE_RESULTS.json');assert len(res['checks'])==7 and all(x['ok']for x in res['checks']);assert res['summary']['actualHHCTuviCalls']==12 and res['summary']['actualIztroNatalCalls']==12
assert len(res['runtime'])==168 and all(x['hhcBranch']==x['iztroBranch']and not x['profile']['officeIsPlacementConstraint']and not x['profile']['officeReplacesPhysicalPlacement']and x['profile']['practicalOutcome']is None for x in res['runtime'])
assert len({(x['solar'],x['input']['hour'])for x in res['runtime']})==12
assert sha(w/res['actualEngine']['file'])==res['actualEngine']['sha256']=='39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6'
# Recheck four pinned runtime files against actual retained package bytes, not merely a declared version.
runtime=read(w/res['runtimePackageProof']);tgz=w/runtime['runtimeTarball'];assert sha(tgz)==runtime['runtimeTarballSHA256']=='d44e96631c0506424c3aef25a7bba8e43e01729102d6a703720cbe224aec5403'
with tarfile.open(tgz,'r:gz')as t:
 for x in runtime['runtime']:
  p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'];assert p.read_bytes()==t.extractfile('package/'+x['file'].split('/iztro/',1)[1]).read()
assert len(runtime['runtime'])==4
state=read(b/'WORK_STATE.json');assert not state['wholeCatalogueCompleted']and not state['fullChaptersApplied']and not state['sourceStarPlacementAlgorithmValidated']
out=dict(date='2026-10-28',promotionIdentities=69,completeRuntimeChecks=7,institutionJPEGDerivativeHTTP200Bodies=30,responseHeaderSets=29,probeHeadersUnavailable=1,failedPythonCertificateRequestsRetained=12,certificateValidationNeverDisabled=True,originalJP2Bodies=0,firstPassReadNewPositions=30,nativeCropsViewedPixelMatched=13,mistargetCropExcludedAsLianzhenProof=True,manifestItemCanvases=129,distinctRetainedPositions=46,unretainedPositions=83,selectedStarProfiles=14,elementVoiceClaims=15,actualHHCTuviCalls=12,actualIztroNatalCalls=12,matchedMajorStarBranchPalaceCoordinates=168,retainedIztroRuntimeFilesMatchedToTarball=4,fullSourceChaptersApplied=False,sourcePlacementAlgorithmValidated=False,sourceOutcomesValidated=False,consumerChanged=False,wholeCatalogueCompleted=False)
p=q/'SOURCE_RESULTS.json'
if '--no-write'in sys.argv:assert read(p)==out
else:p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
