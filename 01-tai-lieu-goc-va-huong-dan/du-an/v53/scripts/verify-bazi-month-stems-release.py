from pathlib import Path
from hashlib import sha256
import json,zipfile,sys
root=Path(__file__).resolve().parent.parent;workspace=root.parent;sha=lambda b:sha256(b).hexdigest()
manifest=json.loads((root/'PACKAGE_MANIFEST.json').read_text(encoding='utf8'));product=(root/'Huyen_Hoc_Cac.html').read_bytes()
assert product==(workspace/'Huyen_Hoc_Cac.html').read_bytes()==(root/'site/index.html').read_bytes()
assert len(product)==manifest['product']['bytes'] and sha(product)==manifest['product']['sha256']
assert [p.name for p in (root/'site').iterdir()]==['index.html']
for f in manifest['files']:
    b=(root/f['file']).read_bytes();assert len(b)==f['bytes'] and sha(b)==f['sha256'],f['file']
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_web.zip') as z:
    assert sorted(z.namelist())==['HUONG_DAN.md','index.html'];assert z.read('index.html')==product;assert z.read('HUONG_DAN.md')==(root/'README.md').read_bytes()
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_source.zip') as z:
    assert z.read('v53/PACKAGE_MANIFEST.json')==(root/'PACKAGE_MANIFEST.json').read_bytes()
    assert set(z.namelist())=={'v53/'+f['file'] for f in manifest['files']}|{'v53/PACKAGE_MANIFEST.json'}
    for f in manifest['files']:assert sha(z.read('v53/'+f['file']))==f['sha256'],f['file']
archive=workspace/'archives/v53-before-month-stems';old=json.loads((archive/'PACKAGE_MANIFEST.json').read_text(encoding='utf8'))
assert sha((archive/'Huyen_Hoc_Cac.html').read_bytes())=='202c8417ad1e6bf9ed2d9a1fd3cad5875ed17569b86be663138556857db2e56a'
assert old['product']['sha256']==sha((archive/'Huyen_Hoc_Cac.html').read_bytes())
with zipfile.ZipFile(archive/'Huyen_Hoc_Cac_V53_source.zip') as z:
    assert z.read('v53/PACKAGE_MANIFEST.json')==(archive/'PACKAGE_MANIFEST.json').read_bytes()
    for f in ['bazi-cycles.js','bazi-locations.css']:assert z.read('v53/'+f)==(archive/f).read_bytes()
with zipfile.ZipFile(archive/'Huyen_Hoc_Cac_V53_web.zip') as z:assert z.read('index.html')==(archive/'Huyen_Hoc_Cac.html').read_bytes()
for f in ['engine.js','app.js','content.js','bazi-relations.js','fortune.js','fortune-context.js','fortune-months.js','yi-complete-data.js','yi-context.js','home-measured-plan.js','index.html','scripts/build.mjs']:
    assert sha((root/f).read_bytes())==next(x['sha256'] for x in old['files'] if x['file']==f),f
previous=(archive/'bazi-cycles.js').read_text(encoding='utf8');current=(root/'bazi-cycles.js').read_text(encoding='utf8')
assert previous[:previous.index('function render')]==current[:current.index('function render')]
qa=root/'qa/bazi-month-stems'
for f,count in [('SOURCE_RESULTS.json',7),('ENGINE_RESULTS.json',13),('BROWSER_RESULTS.json',21)]:
    j=json.loads((qa/f).read_text(encoding='utf8'));assert len(j['checks'])==count and all(x['ok'] for x in j['checks'])
browser=json.loads((qa/'BROWSER_RESULTS.json').read_text(encoding='utf8'));assert not browser['errors'] and not browser['http']
core=json.loads((root/'qa/test-results.json').read_text(encoding='utf8'));assert len(core['checks'])==50 and all(x['ok'] for x in core['checks']) and not core['errors'] and not core['requests']
engine=json.loads((qa/'ENGINE_RESULTS.json').read_text(encoding='utf8'));assert engine['summary']=={'realCharts':2928,'hiddenStemOccurrences':6840,'sourcePairs':16,'secondaryOfficialCases':4,'realSourceFixtures':16,'unknownHourSweeps':1}
source=json.loads((qa/'SOURCE_RESULTS.json').read_text(encoding='utf8'));assert source['summary']['successfulResponses']==37 and source['summary']['failed429']==1 and source['summary']['renderedPages']==17 and source['summary']['targetedContextPages']==11
base=root/'research/bazi-pattern-witness';assert source['manualSHA256']==engine['manualSHA256']==sha((base/'MANUAL_READINGS.json').read_bytes())
assert sha((base/'CADAL06066041.djvu').read_bytes())==source['summary']['containerSHA256']=='013ce4861680a2bf08b811050c45a45bb2d3ce9d164f7e2341d7070bd5cb2c1a'
for r in source['pages']:assert sha((base/r['file']).read_bytes())==r['sha256']
pdf=json.loads((qa/'PDF_RESULTS.json').read_text(encoding='utf8'));assert pdf['pages']==8 and all(v for k,v in pdf.items() if k not in ['pages','pageCharacters','pdfSHA256']);assert sha((qa/'month-stems.pdf').read_bytes())==pdf['pdfSHA256']
for n in range(1,9):assert (qa/f'print-page-{n}.png').stat().st_size>10000
html=product.decode('utf8');assert (root/'bazi-cycles.js').read_bytes().decode('utf8').strip() in html;assert (root/'bazi-locations.css').read_bytes().decode('utf8').strip() in html
assert 'bazi-month-stems result-expand-export' in html and 'CADAL06066041' not in html and 'MANUAL_READINGS.json' not in html
result={'htmlBytes':len(product),'htmlSHA256':sha(product),'manifestFiles':len(manifest['files']),'automatedChecks':91,'sourceChecks':7,'engineChecks':13,'browserChecks':21,'coreChecks':50,'realLibraryMonthCharts':2928,'monthHiddenOccurrences':6840,'sourceDayMonthPairs':16,'secondaryOfficialCases':4,'imageReadClauses':10,'partialSections':3,'renderedSourcePages':17,'failedHTTP429Excluded':1,'pdfPages':8,'allFinalPDFPagesManuallyReviewed':True,'priorReleasePreserved':True,'engineAppBytesUnchanged':True,'monthOnsetCycleCalculationsUnchanged':True,'sourceZIPFilesVerified':len(manifest['files'])+1,'siteClean':True,'fourResearchDirections':'active-not-complete'}
if '--no-write' not in sys.argv:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(result,ensure_ascii=False))
