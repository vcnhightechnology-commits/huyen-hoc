from pathlib import Path
from hashlib import sha256
import json, zipfile, sys

root = Path(__file__).resolve().parent.parent
workspace = root.parent
sha = lambda b: sha256(b).hexdigest()
manifest = json.loads((root / 'PACKAGE_MANIFEST.json').read_text(encoding='utf8'))
product = (root / 'Huyen_Hoc_Cac.html').read_bytes()
assert product == (workspace / 'Huyen_Hoc_Cac.html').read_bytes() == (root / 'site/index.html').read_bytes()
assert len(product) == manifest['product']['bytes'] and sha(product) == manifest['product']['sha256']
assert [p.name for p in (root / 'site').iterdir()] == ['index.html']
for f in manifest['files']:
    b = (root / f['file']).read_bytes()
    assert len(b) == f['bytes'] and sha(b) == f['sha256'], f['file']
with zipfile.ZipFile(workspace / 'Huyen_Hoc_Cac_V53_web.zip') as z:
    assert sorted(z.namelist()) == ['HUONG_DAN.md', 'index.html']
    assert z.read('index.html') == product
with zipfile.ZipFile(workspace / 'Huyen_Hoc_Cac_V53_source.zip') as z:
    assert z.read('v53/PACKAGE_MANIFEST.json') == (root / 'PACKAGE_MANIFEST.json').read_bytes()
    assert set(z.namelist()) == {'v53/' + f['file'] for f in manifest['files']} | {'v53/PACKAGE_MANIFEST.json'}
    for f in manifest['files']:
        assert sha(z.read('v53/' + f['file'])) == f['sha256'], f['file']
archive = workspace / 'archives/v53-before-bazi-relation-locations'
old = json.loads((archive / 'PACKAGE_MANIFEST.json').read_text(encoding='utf8'))
assert sha((archive / 'Huyen_Hoc_Cac.html').read_bytes()) == '676f0d26584810df0509b43065c5031a5ea26afa930679745f4bf8407e54a9d3'
assert old['product']['sha256'] == sha((archive / 'Huyen_Hoc_Cac.html').read_bytes())
with zipfile.ZipFile(archive / 'Huyen_Hoc_Cac_V53_source.zip') as z:
    assert z.read('v53/PACKAGE_MANIFEST.json') == (archive / 'PACKAGE_MANIFEST.json').read_bytes()
    assert z.read('v53/bazi-relations.js') == (archive / 'bazi-relations.js').read_bytes()
    assert z.read('v53/four-items.css') == (archive / 'four-items.css').read_bytes()
with zipfile.ZipFile(archive / 'Huyen_Hoc_Cac_V53_web.zip') as z:
    assert z.read('index.html') == (archive / 'Huyen_Hoc_Cac.html').read_bytes()
unchanged = ['engine.js', 'app.js', 'content.js', 'yi-content.js', 'yi-complete-data.js', 'yi-lines.js', 'yi-context.js', 'fortune.js', 'fortune-context.js', 'fortune-months.js', 'bazi-cycles.js', 'home-measured-plan.js', 'four-items.css']
for name in unchanged:
    assert sha((root / name).read_bytes()) == next(x['sha256'] for x in old['files'] if x['file'] == name), name
base = root / 'research/bazi-relation-locations'
audit = json.loads((base / 'SOURCE_AUDIT.json').read_text(encoding='utf8'))
for row in audit['sourceRecords']:
    b = (root / row['file']).read_bytes()
    assert len(b) == row['bytes'] and sha(b) == row['sha256']
assert sha((base / 'MANUAL_READINGS.json').read_bytes()) == audit['manualSHA256']
for row in audit['runtimeRecords']:
    b = (workspace / row['file']).read_bytes()
    assert len(b) == row['bytes'] and sha(b) == row['sha256']
qa = root / 'qa/bazi-relation-locations'
for name, count in [('ENGINE_RESULTS.json', 16), ('BROWSER_RESULTS.json', 21)]:
    j = json.loads((qa / name).read_text(encoding='utf8'))
    assert len(j['checks']) == count and all(c['ok'] for c in j['checks'])
browser = json.loads((qa / 'BROWSER_RESULTS.json').read_text(encoding='utf8'))
assert not browser['errors'] and not browser['http']
summary = json.loads((qa / 'ENGINE_RESULTS.json').read_text(encoding='utf8'))['summary']
assert summary['realCharts'] == 240 and summary['occurrenceFields'] == 3020 and summary['relationLayerCoverage'] == 20
pdf = json.loads((qa / 'PDF_RESULTS.json').read_text(encoding='utf8'))
assert pdf['pages'] == 7 and all(v for k, v in pdf.items() if k not in ['pages', 'pageCharacters'])
for n in range(1, 8):
    assert (qa / f'final-print-page-{n}.png').stat().st_size > 10000
before = json.loads((qa / 'BEFORE_EXPORT.json').read_text(encoding='utf8'))
assert not before['downloadContainsInterpretation']
assert before['phrase'] in (qa / 'after-default-closed.txt').read_text(encoding='utf8')
comparison = json.loads((base / 'RUNTIME_COMPARISON.json').read_text(encoding='utf8'))
assert comparison['cases'] == 240 and len(comparison['rows']) == 240
assert comparison['lateZiDifference']['hhc'][-1] == '壬子' and comparison['lateZiDifference']['lunarTypescriptSect2'][-1] == '甲子'
late_zi = json.loads((root / 'research/bazi-late-zi/VERIFICATION.json').read_text(encoding='utf8'))
assert len(late_zi['checks']) == 9 and all(c['ok'] for c in late_zi['checks'])
assert late_zi['scope']['realChartComparisons'] == 7936 and len(late_zi['rows']) == 7936
assert late_zi['variants'] == {'midnight': {'matches': 248, 'differences': 3720}, 'zi': {'matches': 3968, 'differences': 0}}
assert late_zi['engineSHA256'] == sha((root / 'engine.js').read_bytes())
for row in late_zi['sources']:
    b = (root / row['file']).read_bytes()
    assert len(b) == row['bytes'] and sha(b) == row['sha256']
for row in late_zi['runtime']:
    b = (workspace / row['file']).read_bytes()
    assert len(b) == row['bytes'] and sha(b) == row['sha256']
html = product.decode('utf8')
assert (root / 'bazi-relations.js').read_text(encoding='utf8').strip() in html
assert (root / 'bazi-locations.css').read_text(encoding='utf8').strip() in html
assert 'relation-guide result-expand-export' in html
result = {
    'htmlBytes': len(product), 'htmlSHA256': sha(product), 'manifestFiles': len(manifest['files']),
    'automatedScopeChecks': 37, 'realReferenceCharts': 240, 'occurrenceFields': 3020,
    'manualPairs': 11, 'pdfPages': 7, 'pdfManualReview': 'All seven final pages inspected; no clipping, hidden form/hero, cycle heading with body.',
    'separateLateZiResearchChecks': 9, 'lateZiChartComparisons': 7936, 'lateZiDifferencesRetained': 3720,
    'priorReleasePreserved': True, 'calculationsUnchanged': True, 'siteClean': True,
    'sourceZIPFilesVerified': len(manifest['files']) + 1,
    'scope': 'Relation locations and complete compact exports. Late-Zi policy kept separate; four research directions remain active.'
}
if '--no-write' not in sys.argv:
    (qa / 'RELEASE_RESULTS.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
print(json.dumps(result, ensure_ascii=False))
