from pathlib import Path
from hashlib import sha256
import json, tarfile
from PIL import Image

r = Path(__file__).resolve().parent.parent
w = r.parent
b = r/'research/tuvi-void-child'
q = r/'qa/tuvi-void-child'
read = lambda p: json.loads(p.read_text(encoding='utf-8-sig'))
sha = lambda p: sha256(p.read_bytes()).hexdigest()

identities = read(b/'PROMOTION_IDENTITIES.json')['records']
for record in identities:
    p = w/record['file']
    assert p.stat().st_size == record['bytes'] and sha(p) == record['sha256'], p

master = read(r/'research/tuvi-masters/SOURCE_MANIFEST.json')
source = next(x for x in master['images'] if x['canvas'] == 80)
image = w/source['file']
assert image.stat().st_size == source['retainedRequest']['bytes'] == 509972
assert sha(image) == source['sha256'] == source['retainedRequest']['sha256']
assert source['retainedRequest']['status'] == 200 and source['retainedRequest']['tls']['authorized']
void_manifest = read(b/'VOID_SOURCE_MANIFEST.json')
manifest_file = w/void_manifest['retainedManifest']
assert sha(manifest_file) == void_manifest['retainedManifestSHA256']
canvas = read(manifest_file)['sequences'][0]['canvases'][79]
assert source['retainedRequest']['url'] == canvas['images'][0]['resource']['service']['@id']+'/full/2200,/0/native.jpg'
assert void_manifest['retainedImageSHA256'] == source['sha256']

for name in ['CHILD_CROP.json','VOID_CROP.json']:
    crop = read(b/name)
    assert crop['sourceSHA256'] == sha(w/crop['source'])
    assert crop['actuallyViewed'] and crop['pixelMatch']
    original = Image.open(w/crop['source']).convert('RGB')
    target = Image.open(b/'images'/crop['file']).convert('RGB')
    assert sha(b/'images'/crop['file']) == crop['sha256']
    assert original.size == tuple(crop['sourceSize']) == (2200,1659)
    assert original.crop(crop['box']).size == target.size
    assert original.crop(crop['box']).tobytes() == target.tobytes()

response = read(b/'RESPONSE.json')
child_manifest = read(b/'CHILD_SOURCE_MANIFEST.json')
assert response == child_manifest['newHigherResolutionRequest']
body = b/response['file']
assert body.stat().st_size == response['bytes'] == 608 and response['status'] == 403
assert sha(body) == response['sha256'] == '3583028b8177997257190b29910fd802ea895c68f197c795e5267d00cf76d6a0'
assert response['tls']['authorized'] and response['tls']['protocol'] == 'TLSv1.3'
assert not response['actuallyViewed'] and not child_manifest['nativeJP2Acquired']
assert b'<html' in body.read_bytes().lower()

child, void = read(q/'CHILD_RESULTS.json'), read(q/'VOID_RESULTS.json')
assert len(child['checks']) == 5 and len(void['checks']) == 7
assert all(x['ok'] for x in child['checks']+void['checks'])
assert child['summary']['actualHHCTuviCalls'] == child['summary']['actualIztroNatalCalls'] == 12
assert child['summary']['privateOrdinalPalaceBindings'] == 72
assert void['summary']['actualHHCTuviCalls'] == 60
assert void['summary']['actualIztroDefaultNatalCalls'] == void['summary']['actualIztroZhongzhouNatalCalls'] == 60
assert void['summary']['privateSourceYearBranchQueries'] == 1440
assert void['summary']['unresolvedSiQueries'] == 264 and void['summary']['unresolvedSiMemberships'] == 242
assert len(void['runtime']) == 60 and len(child['runtime']) == 12

runtime = {x['file']:x for x in master['runtime']+child['runtimeIdentity']+void['runtimeIdentity']}
tarball = w/master['runtimeTarball']
assert sha(tarball) == master['runtimeTarballSHA256'] == 'd44e96631c0506424c3aef25a7bba8e43e01729102d6a703720cbe224aec5403'
with tarfile.open(tarball,'r:gz') as archive:
    for record in runtime.values():
        p = w/record['file']
        assert p.stat().st_size == record['bytes'] and sha(p) == record['sha256']
        member = 'package/'+record['file'].split('node_modules/iztro/')[1]
        assert p.read_bytes() == archive.extractfile(member).read()
assert read(w/'v46/node_modules/iztro/package.json')['version'] == '2.6.2'

tables, ordinals = read(b/'SOURCE_TABLES.json'), read(b/'SOURCE_ORDINALS.json')
assert [len(x['rows']) for x in tables['systems']] == [5,6]
assert sum(len(x['canonicalWorkingBranches']) for s in tables['systems'] for x in s['rows']) == tables['canonicalWorkingBranchCoordinates'] == 22
assert sum(x['contextualSiNormalization'] for s in tables['systems'] for x in s['rows']) == tables['siNormalizationOccurrences'] == 2
assert tables['scopeLiteral'] == '論本生年' and tables['sourceScopeExplicitlyBirthYear']
assert not tables['singleSoftwareStarSelectorAttestedInSource'] and not tables['sourceYearBoundaryAdapterEstablished']
assert [(x['printedOrdinal'],x['sourcePalaceLiteral']) for x in ordinals['rows']] == [(1,'命'),(2,'財'),(3,'疾厄'),(4,'妻'),(5,'福'),(6,'官祿')]
assert not ordinals['sourceAgeCountingConventionResolved'] and not ordinals['wholePassageTranscribed']
assert not ordinals['unresolvedTail']['normalizationToDaXianOrAge15']
units = read(b/'CURRENT_UNITS.json')
assert len(units['units']) == 3 and not units['wholeBookApplied']
manual = read(b/'MANUAL_READINGS.json')
assert manual['uniquePriorSourcePositionsExpanded'] == 1 and manual['nativeCropsActuallyViewed'] == 2

out = {
    'date':'2026-10-28','retainedSourceImagesVerified':1,'retainedImageBytes':509972,
    'retainedPublicJPEGDerivativeNotOriginalJP2':True,'retainedImageOriginalTLSAuthorized':True,
    'nativeCropsPixelVerified':2,'promotionIdentityHashesVerified':len(identities),
    'additionalRuntimeFilesVerified':len(child['runtimeIdentity'])+len(void['runtimeIdentity']),
    'uniqueRuntimeFilesByteIdenticalToTarball':len(runtime),
    'sourceJieluStemGroups':5,'sourceXunzhongCycleGroups':6,'canonicalWorkingBranchCoordinates':22,
    'explicitSiNormalizationOccurrences':2,'sourcePrintedOrdinalCoordinates':6,
    'newHTTPRequestsThisHeartbeat':0,'inheritedFailedHTTPRequests':1,'inheritedFailedHTTPBodyBytes':608,
    'successfulNewImageDownloads':0,'newOriginalContainers':0,'newSourcePositions':0,
    'uniqueExpandedPriorSourcePositions':1,'originalJP2Acquired':False,
    'sourceYearBoundaryAdapterEstablished':False,'sourceSingleSoftwareStarSelectorAttested':False,
    'sourceAgeCountingConventionResolved':False,'wholeChildPassageTranscribed':False,
    'practicalOutcomesValidated':False,'consumerChanged':False,'wholeCatalogueCompleted':False
}
(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
