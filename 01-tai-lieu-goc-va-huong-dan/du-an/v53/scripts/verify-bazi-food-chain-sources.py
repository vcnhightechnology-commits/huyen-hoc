from pathlib import Path
from hashlib import sha256
import json
import subprocess
from PIL import Image, ImageChops

v = Path(__file__).resolve().parent.parent
w = v.parent
r = v / 'research/bazi-food-chain'
q = v / 'qa/bazi-food-chain'
read = lambda p: json.loads(p.read_text(encoding='utf-8-sig'))
hashfile = lambda p: sha256(p.read_bytes()).hexdigest()

promotion = read(r / 'PROMOTION_MANIFEST.json')
for x in promotion['byteExactCopies']:
    for p in [w / x['source'], w / x['target']]:
        assert p.stat().st_size == x['bytes'] and hashfile(p) == x['sha256'], str(p)
freeze = read(r / 'PREIMPLEMENTATION_FREEZE.json')
assert freeze['implementationExists'] is False
for x in freeze['files']:
    assert (r / x['file']).stat().st_size == x['bytes']
    assert hashfile(r / x['file']) == x['sha256']
identities = read(r / 'SOURCE_IDENTITIES.json')
for x in identities['files']:
    p = w / x['file']
    assert p.stat().st_size == x['bytes'] and hashfile(p) == x['sha256'], x['file']
source = next(x for x in read(v / 'research/bazi-food-source/CONTEXTS.json')['records'] if x['id'] == 'FOOD-00-C07')
manual = read(r / 'MANUAL_CHAIN.json')
assert manual['chainLiteral'] in source['text']
assert source['digitalFolios'] == ['005-85a']
assert manual['literalHasExplicitSecondSubject'] is False
accepted = excluded = 0
for x in read(r / 'NATIVE_CROPS.json')['records']:
    original = Image.open(w / x['source']['file']).convert('RGB')
    crop = Image.open(r / Path(x['crop']['file']).name).convert('RGB')
    assert hashfile(r / Path(x['crop']['file']).name) == x['crop']['sha256']
    if not x['accepted']:
        assert not x['viewed'] and x['boxXYXY'][3] > original.height
        excluded += 1
        continue
    x0, y0, x1, y1 = x['boxXYXY']
    assert 0 <= x0 < x1 <= original.width and 0 <= y0 < y1 <= original.height
    assert x['viewed'] and x['RGBMatchesSourceCrop']
    assert original.crop(x['boxXYXY']).size == crop.size
    assert ImageChops.difference(original.crop(x['boxXYXY']), crop).getbbox() is None
    accepted += 1
assert accepted == excluded == 2
runtime = read(r / 'ACTUAL_RUNTIME.json')
assert runtime['engineSHA256'] == hashfile(v / 'engine.js')
assert runtime['relationsSHA256'] == hashfile(v / 'bazi-relations.js')
assert runtime['lunarLibrarySHA256'] == hashfile(w / 'v46/node_modules/lunar-typescript/dist/index.cjs')
assert runtime['scriptSHA256'] == hashfile(r / 'run-actual-once.mjs')
assert runtime['freezeSHA256'] == hashfile(r / 'PREIMPLEMENTATION_FREEZE.json')
expected = read(r / 'EXPECTED_BEFORE_IMPLEMENTATION.json')
assert runtime['stemElements'] == expected['stemElements']
assert runtime['summary']['actualHHCNatalCharts'] == 0
assert runtime['summary']['actualIztroCharts'] == 0
previous = read(v / 'research/bazi-tongke-cases/CURRENT_CONTEXT_COVERAGE.json')
current = read(r / 'CURRENT_CONTEXT_COVERAGE.json')
assert current['previousMatrixSHA256'] == hashfile(v / 'research/bazi-tongke-cases/CURRENT_CONTEXT_COVERAGE.json')
changes = []
for old, new in zip(previous['records'], current['records'], strict=True):
    if old != new:
        assert old['id'] == new['id'] == 'FOOD-00-C07'
        assert old['selectedModuleLinks'] == [] and len(new['selectedModuleLinks']) == 1
        assert {k: x for k, x in old.items() if k != 'selectedModuleLinks'} == {k: x for k, x in new.items() if k != 'selectedModuleLinks'}
        assert new['selectedModuleLinks'][0]['sha256'] == hashfile(r / 'food-chain-reference.mjs')
        changes.append(new['id'])
assert changes == ['FOOD-00-C07']
assert sum(bool(x['selectedModuleLinks']) for x in current['records']) == 44
assert sum(not x['selectedModuleLinks'] for x in current['records']) == 46
assert not any(x['wholeContextApplied'] for x in current['records'])
coverage = read(v / 'research/library-current/COVERAGE.json')
m01 = next(x for x in coverage['catalogue'] if x['id'] == 'M01')
selection = m01['foodParentContextSelection']
assert selection['parentsWithSelectedModuleOrDeclaredPremiseLinks'] == 44
assert selection['otherParentsWithoutSuchLinks'] == 46
assert selection['currentMatrix'] == 'v53/research/bazi-food-chain/CURRENT_CONTEXT_COVERAGE.json'
assert selection['wholeParentsApplied'] == 0 and coverage['counts']['wholeWorkApplied'] == 0
original_test = (w / 'tmp/bazi-food-chain-staging/test-food-chain.mjs').read_bytes()
expected_test = original_test.replace(b"from './food-chain-reference.mjs'", b"from '../research/bazi-food-chain/food-chain-reference.mjs'")
expected_test = expected_test.replace(b'const base=import.meta.dirname,read=', b"const base=path.resolve(import.meta.dirname,'../research/bazi-food-chain'),read=")
assert expected_test == (v / 'scripts/test-bazi-food-chain.mjs').read_bytes()
result = subprocess.run(['node', str(v / 'scripts/test-bazi-food-chain.mjs')], cwd=w, check=True, capture_output=True, text=True, encoding='utf-8')
tests = json.loads(result.stdout)
assert tests == read(w / 'tmp/bazi-food-chain-staging/TEST_RESULTS.json')
out = {'date': '2026-10-29', 'passed': True, 'byteExactPromotedFiles': len(promotion['byteExactCopies']),
       'retainedIdentityFilesVerified': len(identities['files']), 'preimplementationFilesUnchanged': len(freeze['files']),
       'acceptedNativeCropsRGBMatched': accepted, 'excludedOutOfBoundsTrials': excluded,
       'parentMatrixRecordsPreserved': 89, 'newPartialParentLinks': 1, 'partialParents': 44, 'unlinkedParents': 46,
       'wholeParentsApplied': 0, 'retainedActualHHCGodCalls': 11, 'retainedActualLunarTenGodQueries': 11,
       'retainedActualLunarElementQueries': 5, 'newEngineCallsDuringContinuation': 0, 'newHTTPRequests': 0,
       'sourceMeaningResolved': False, 'consumerChanged': False, 'referenceTests': tests}
import sys
if '--no-write' in sys.argv:
    assert read(q / 'RESULTS.json') == tests
    assert read(q / 'SOURCE_RESULTS.json') == out
else:
    (q / 'RESULTS.json').write_text(json.dumps(tests, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (q / 'SOURCE_RESULTS.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(out, ensure_ascii=False))
