from pathlib import Path
from hashlib import sha256
import json, zipfile, sys

root = Path(__file__).resolve().parent.parent
workspace = root.parent
archive = workspace / 'archives/v53-before-internal-doors'
qa = root / 'qa/internal-doors'
sha = lambda b: sha256(b).hexdigest()
read_json = lambda p: json.loads(p.read_text(encoding='utf8'))
m = read_json(root / 'PACKAGE_MANIFEST.json')
old = read_json(archive / 'PACKAGE_MANIFEST.json')
html = (root / 'Huyen_Hoc_Cac.html').read_bytes()
assert html == (workspace / 'Huyen_Hoc_Cac.html').read_bytes() == (root / 'site/index.html').read_bytes()
assert len(html) == m['product']['bytes'] == 677537
assert sha(html) == m['product']['sha256'] == 'eb1425292f680ac60dd1af57ac805f6312d209ad92d72c4f6499de0502d9ff22'
assert [p.name for p in (root / 'site').iterdir()] == ['index.html']
assert b'<script src=' not in html and b'<link rel="stylesheet"' not in html
for f in ['home-internal-doors.js', 'home-measured-plan.js', 'home-measured-plan.css']:
    assert (root / f).read_bytes().strip() in html, f
assert html.index(b'window.HHC_HOME_DOORS=') < html.index(b'D=window.HHC_HOME_DOORS')
assert not any(x in html for x in [b'CADAL06056503', b'GEOMETRY_RESULTS.json', b'SPECIFICATION.md'])
assert {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.name != 'PACKAGE_MANIFEST.json'} == {f['file'] for f in m['files']}
for f in m['files']:
    b = (root / f['file']).read_bytes()
    assert len(b) == f['bytes'] and sha(b) == f['sha256'], f['file']
for f in old['files']:
    if ('/' not in f['file'] and f['file'].endswith(('.js', '.css')) and f['file'] not in ['home-measured-plan.js', 'home-measured-plan.css']) or f['file'].startswith('assets/'):
        assert sha((root / f['file']).read_bytes()) == f['sha256'], f['file']
assert sha((archive / 'Huyen_Hoc_Cac.html').read_bytes()) == old['product']['sha256'] == 'bfc9e9975fd96fda944f5f952b58c33967d228956f1f065623e0008b152e3e37'
assert (archive / 'Huyen_Hoc_Cac_V53_source.zip').stat().st_size == 796974820
with zipfile.ZipFile(archive / 'Huyen_Hoc_Cac_V53_source.zip') as z:
    assert z.read('v53/PACKAGE_MANIFEST.json') == (archive / 'PACKAGE_MANIFEST.json').read_bytes()
    for f in ['home-measured-plan.js', 'home-measured-plan.css', 'README.md']:
        assert z.read('v53/'+f) == (archive / f).read_bytes()
with zipfile.ZipFile(archive / 'Huyen_Hoc_Cac_V53_web.zip') as z:
    assert z.read('index.html') == (archive / 'Huyen_Hoc_Cac.html').read_bytes()
with zipfile.ZipFile(workspace / 'Huyen_Hoc_Cac_V53_web.zip') as z:
    assert sorted(z.namelist()) == ['HUONG_DAN.md', 'index.html']
    assert z.read('index.html') == html and z.read('HUONG_DAN.md') == (root / 'README.md').read_bytes()
with zipfile.ZipFile(workspace / 'Huyen_Hoc_Cac_V53_source.zip') as z:
    assert set(z.namelist()) == {'v53/'+f['file'] for f in m['files']} | {'v53/PACKAGE_MANIFEST.json'}
    assert z.read('v53/PACKAGE_MANIFEST.json') == (root / 'PACKAGE_MANIFEST.json').read_bytes()
    for f in m['files']:
        assert sha(z.read('v53/'+f['file'])) == f['sha256'], f['file']
for p, count in [(qa/'GEOMETRY_RESULTS.json',20), (qa/'BROWSER_RESULTS.json',27), (qa/'home-regression/test-results.json',40), (root/'qa/test-results.json',50)]:
    r = read_json(p)
    assert len(r['checks']) == count and all(x['ok'] for x in r['checks']), p.name
    assert not r.get('errors') and not r.get('requests'), p.name
geometry = read_json(qa/'GEOMETRY_RESULTS.json')
assert geometry['summary']['legacyGeometryModels'] == 50
assert geometry['summary']['newExternalResponses'] == 0
for f in read_json(root/'research/internal-doors/REUSED_SOURCES.json')['files']:
    b = (root/f['file']).read_bytes()
    assert len(b) == f['bytes'] and sha(b) == f['sha256']
pdf = read_json(qa/'PDF_RESULTS.json')
assert pdf['pages'] == 3 and all(v for k,v in pdf.items() if k not in ['pages','pageCharacters','pdfSHA256'])
assert sha((qa/'internal-doors.pdf').read_bytes()) == pdf['pdfSHA256']
for i in range(1,4):
    assert (qa/f'print-page-{i}.png').stat().st_size > 10000
for width in [390,1440]:
    for name in ['result','controls']:
        assert (qa/f'{name}-{width}.png').stat().st_size > 10000
state = read_json(root/'research/full-study/WORK_STATE.json')
assert state['overallStatus'] == 'active-not-complete'
assert next(x for x in state['items'] if x['id']=='home')['latestScope'] == '../internal-doors/SPECIFICATION.md'
assert '**Cửa thông giữa các phòng**' in (root/'README.md').read_text(encoding='utf8')
result = {
    'htmlBytes':len(html), 'htmlSHA256':sha(html), 'automatedChecks':137,
    'geometryChecks':20, 'browserChecks':27, 'homeRegressionChecks':40, 'coreChecks':50,
    'legacyGeometryModels':50, 'pdfPages':3, 'allPDFPagesVisuallyReviewed':True,
    'engineAppAndUnrelatedModulesUnchanged':True, 'newExternalSourceBodies':0,
    'siteClean':True, 'priorReleasePreserved':True,
    'manifestFilesVerified':len(m['files']), 'sourceZIPFilesVerified':len(m['files'])+1,
    'fourResearchDirections':state['overallStatus']
}
if '--no-write' not in sys.argv:
    (qa/'RELEASE_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
else:
    assert read_json(qa/'RELEASE_RESULTS.json') == result
print(json.dumps(result,ensure_ascii=False))
