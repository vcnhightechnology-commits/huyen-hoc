from pathlib import Path
from hashlib import sha256
import json
import sys
import zipfile

v = Path(__file__).resolve().parent.parent
w = v.parent
q = v / 'qa/bazi-food-chain'
read = lambda p: json.loads(p.read_text(encoding='utf-8-sig'))
prepare = '--prepare' in sys.argv
assert prepare or '--no-write' in sys.argv


def digest(p):
    h = sha256()
    with p.open('rb') as stream:
        for block in iter(lambda: stream.read(4 * 1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


archive = w / 'archives/v53-before-bazi-food-chain'
snapshot = read(archive / 'SNAPSHOT.json')
assert snapshot['sourceManifestFiles'] == 5768
assert snapshot['sourceZIPBytes'] == 3045844885
for x in snapshot['files']:
    p = archive / x['file']
    assert p.stat().st_size == x['bytes'] and digest(p) == x['sha256'], x['file']
allowed = {'NEXT_STEPS.md', 'research/EXHAUSTIVE_WORK_STATE.json', 'research/full-study/WORK_STATE.json',
           'research/library-current/COVERAGE.json', 'research/library-current/COVERAGE.md'}
unchanged = 0
for x in read(archive / 'PACKAGE_MANIFEST.json')['files']:
    if x['file'] in allowed:
        continue
    p = v / x['file']
    assert p.stat().st_size == x['bytes'] and digest(p) == x['sha256'], x['file']
    unchanged += 1
assert unchanged == 5763
source = read(q / 'SOURCE_RESULTS.json')
assert source['passed'] and source['referenceTests'] == read(q / 'RESULTS.json')
assert source['newEngineCallsDuringContinuation'] == source['newHTTPRequests'] == 0
assert (w / 'EXHAUSTIVE_WORK_STATE.json').read_bytes() == (v / 'research/EXHAUSTIVE_WORK_STATE.json').read_bytes()
coverage = read(v / 'research/library-current/COVERAGE.json')
assert coverage['counts']['wholeWorkApplied'] == 0 and coverage['counts']['newDownloadsThisScope'] == 0
assert coverage['counts']['status'] == {'inherited_rule_claim': 4, 'partial_active': 5, 'not_established': 24, 'research_only': 7}
assert all(next(x for x in coverage['catalogue'] if x['id'] == cid)['currentStatus'] == 'research_only' for cid in ['L01', 'L02'])
assert not read(v / 'research/bazi-jianlu-context/CANDIDATE_STATUS.json')['browserTestsPassed']
selection = next(x for x in coverage['catalogue'] if x['id'] == 'M01')['foodParentContextSelection']
assert selection['parentsWithSelectedModuleOrDeclaredPremiseLinks'] == 44
assert selection['otherParentsWithoutSuchLinks'] == 46 and selection['wholeParentsApplied'] == 0
assert selection['currentMatrix'] == 'v53/research/bazi-food-chain/CURRENT_CONTEXT_COVERAGE.json'
assert read(v / 'research/EXHAUSTIVE_WORK_STATE.json')['status'] == 'active-not-complete'
html = (v / 'Huyen_Hoc_Cac.html').read_bytes()
html_sha = sha256(html).hexdigest()
assert len(html) == 707411 and html_sha == '549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html == (w / 'Huyen_Hoc_Cac.html').read_bytes() == (v / 'site/index.html').read_bytes()
assert sorted(p.name for p in (v / 'site').iterdir()) == ['index.html']
web = w / 'Huyen_Hoc_Cac_V53_web.zip'
assert digest(web) == digest(archive / web.name)
with zipfile.ZipFile(web) as z:
    assert sorted(z.namelist()) == ['HUONG_DAN.md', 'index.html'] and z.read('index.html') == html
payload = q / 'RELEASE_RESULTS.json'
files = [p for p in v.rglob('*') if p.is_file() and p.name != 'PACKAGE_MANIFEST.json']
if prepare:
    count = len(files) + (0 if payload.exists() else 1)
else:
    manifest = read(v / 'PACKAGE_MANIFEST.json')
    assert {p.relative_to(v).as_posix() for p in files} == {x['file'] for x in manifest['files']}
    assert manifest['product']['sha256'] == html_sha
    for x in manifest['files']:
        p = v / x['file']
        assert p.stat().st_size == x['bytes'] and digest(p) == x['sha256'], x['file']
    with zipfile.ZipFile(w / 'Huyen_Hoc_Cac_V53_source.zip') as z:
        assert set(z.namelist()) == {'v53/' + x['file'] for x in manifest['files']} | {'v53/PACKAGE_MANIFEST.json'}
        assert z.read('v53/PACKAGE_MANIFEST.json') == (v / 'PACKAGE_MANIFEST.json').read_bytes()
        for x in manifest['files']:
            h = sha256()
            size = 0
            with z.open('v53/' + x['file']) as stream:
                for block in iter(lambda: stream.read(4 * 1024 * 1024), b''):
                    h.update(block)
                    size += len(block)
            assert size == x['bytes'] and h.hexdigest() == x['sha256'], x['file']
    count = len(manifest['files'])
out = {'date': '2026-10-29', 'sourceVerification': source, 'consumerChanged': False, 'wholeCatalogueCompleted': False,
       'htmlBytes': len(html), 'htmlSHA256': html_sha, 'siteClean': True, 'webZIPUnchanged': True,
       'previousSourceZIPPreservedBytes': 3045844885, 'unchangedEarlierV53Files': unchanged,
       'manifestFilesVerified': count, 'sourceZIPFilesVerified': count + 1}
if prepare:
    payload.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'preparedExpectedPayload': True, 'manifestFilesAfterPackage': count, 'requiresFinalNoWriteVerification': True}))
else:
    assert read(payload) == out
    print(json.dumps({'finalReadOnlyVerificationPassed': True,
                      'sourceZIPBytes': (w / 'Huyen_Hoc_Cac_V53_source.zip').stat().st_size, **out}, ensure_ascii=False))
