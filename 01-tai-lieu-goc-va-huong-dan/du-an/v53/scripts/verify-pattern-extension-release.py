from pathlib import Path
from hashlib import sha256
import json, sys, zipfile

root = Path(__file__).resolve().parent.parent
workspace = root.parent
archive = workspace / 'archives/v53-before-pattern-extension'
qa = root / 'qa/bazi-pattern-extension'
sha = lambda b: sha256(b).hexdigest()
read_json = lambda p: json.loads(p.read_text(encoding='utf8'))
manifest = read_json(root / 'PACKAGE_MANIFEST.json')
old = read_json(archive / 'PACKAGE_MANIFEST.json')
product = (root / 'Huyen_Hoc_Cac.html').read_bytes()
assert product == (workspace / 'Huyen_Hoc_Cac.html').read_bytes() == (root / 'site/index.html').read_bytes() == (archive / 'Huyen_Hoc_Cac.html').read_bytes()
assert sha(product) == manifest['product']['sha256'] == old['product']['sha256'] == 'bfc9e9975fd96fda944f5f952b58c33967d228956f1f065623e0008b152e3e37'
assert len(product) == manifest['product']['bytes'] == 667112
assert [p.name for p in (root / 'site').iterdir()] == ['index.html']
actual = {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.name != 'PACKAGE_MANIFEST.json'}
assert actual == {r['file'] for r in manifest['files']}
for r in manifest['files']:
    b = (root / r['file']).read_bytes()
    assert len(b) == r['bytes'] and sha(b) == r['sha256'], r['file']
for r in old['files']:
    if not r['file'].startswith(('research/', 'qa/', 'scripts/')) and not r['file'].endswith('.md'):
        assert sha((root / r['file']).read_bytes()) == r['sha256'], r['file']
webzip = workspace / 'Huyen_Hoc_Cac_V53_web.zip'
assert webzip.read_bytes() == (archive / webzip.name).read_bytes()
with zipfile.ZipFile(webzip) as z:
    assert sorted(z.namelist()) == ['HUONG_DAN.md', 'index.html']
    assert z.read('index.html') == product
    assert z.read('HUONG_DAN.md') == (root / 'README.md').read_bytes()
with zipfile.ZipFile(workspace / 'Huyen_Hoc_Cac_V53_source.zip') as z:
    assert set(z.namelist()) == {'v53/'+r['file'] for r in manifest['files']} | {'v53/PACKAGE_MANIFEST.json'}
    assert z.read('v53/PACKAGE_MANIFEST.json') == (root / 'PACKAGE_MANIFEST.json').read_bytes()
    for r in manifest['files']:
        assert sha(z.read('v53/'+r['file'])) == r['sha256'], r['file']
with zipfile.ZipFile(archive / 'Huyen_Hoc_Cac_V53_source.zip') as z:
    assert z.read('v53/PACKAGE_MANIFEST.json') == (archive / 'PACKAGE_MANIFEST.json').read_bytes()
    for f in ['bazi-cycles.js', 'bazi-relations.js', 'bazi-locations.css', 'content.js', 'index.html']:
        assert z.read('v53/'+f) == (archive / f).read_bytes()
assert (archive / 'Huyen_Hoc_Cac_V53_source.zip').stat().st_size == 783648876
r = read_json(qa / 'RESULTS.json')
assert len(r['checks']) == 20 and all(t['ok'] for t in r['checks'])
assert r['summary']['actualLibraryCharts'] == 367
assert r['summary']['newTargetedClauses'] == 28
assert r['summary']['totalTargetedClausesAcrossTwoScopes'] == 38
assert r['summary']['totalTargetedMatrixHeadingsWithImages'] == 10
assert len(r['pairFixtures']) == 8 and len(r['luFixtures']) == 2 and len(r['negativeFixtures']) == 3
assert r['bladeFixture']['sourcePartialPillars'] == r['bladeFixture']['pillars'][2:] == ['甲申', '丁卯']
assert r['manualSHA256'] == sha((root / 'research/bazi-pattern-extension/MANUAL_READINGS.json').read_bytes())
assert r['renderManifestSHA256'] == sha((root / 'research/bazi-pattern-extension/LOCAL_RENDERS.json').read_bytes())
renders = read_json(root / 'research/bazi-pattern-extension/LOCAL_RENDERS.json')
decoder = read_json(qa / 'DECODER_RESULTS.json')
assert not decoder['httpRequests'] and not decoder['errors'] and decoder['actualDecodedPageCount'] == 226
assert decoder['sourceSHA256'] == renders['sourceSHA256'] and decoder['decoderSHA256'] == renders['decoderSHA256']
assert [p['page'] for p in decoder['reproduced']] == [2, 138, 198, 218]
for p in decoder['reproduced']:
    saved = next(x for x in renders['pages'] if x['page'] == p['page'])
    assert all(saved[k] == p[k] for k in ['sha256', 'width', 'height'])
matrix = read_json(root / 'research/full-study/bazi/PATTERN_READING_MATRIX.json')
assert matrix['completion']['targetedImageSections'] == 10 and matrix['completion']['targetedImageClauses'] == 38
assert len(matrix['records']) == 10 and all(not x['imageCollation']['wholeSectionComplete'] for x in matrix['records'])
assert all(not matrix['completion'][k] for k in ['wholeVolumeExhausted', 'completePatternClassifier', 'completeStrengthAlgorithm', 'unifiedUsefulGodAlgorithm'])
state = read_json(root / 'research/full-study/WORK_STATE.json')
assert state['overallStatus'] == 'active-not-complete'
assert next(i for i in state['items'] if i['id'] == 'bazi')['latestScope'] == '../bazi-pattern-extension/MANUAL_READINGS.json'
assert b'CADAL06066041' not in product and b'DjVu.Document' not in product
result = {
    'automatedChecks': 20, 'actualLibraryCharts': 367, 'newTargetedClauses': 28,
    'totalTargetedClauses': 38, 'targetedHeadings': 10, 'wholeSectionsComplete': 0,
    'nativePNGDerivatives': 31, 'newContextPages': 29, 'reproducedPNGs': 4,
    'htmlBytes': len(product), 'htmlSHA256': sha(product),
    'productAndWebZIPUnchanged': True, 'siteClean': True, 'priorReleasePreserved': True,
    'allManifestEntriesVerified': len(manifest['files']),
    'sourceZIPFilesVerified': len(manifest['files']) + 1,
    'fullClassifierImplemented': False, 'researchStatus': state['overallStatus']
}
if '--no-write' not in sys.argv:
    (qa / 'RELEASE_RESULTS.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf8')
else:
    assert read_json(qa / 'RELEASE_RESULTS.json') == result
print(json.dumps(result, ensure_ascii=False))
