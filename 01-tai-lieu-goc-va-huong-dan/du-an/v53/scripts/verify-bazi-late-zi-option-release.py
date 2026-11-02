from pathlib import Path
from hashlib import sha256
import json,zipfile,sys

root=Path(__file__).resolve().parent.parent;workspace=root.parent
sha=lambda b:sha256(b).hexdigest()
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
archive=workspace/'archives/v53-before-late-zi-witness';old=json.loads((archive/'PACKAGE_MANIFEST.json').read_text(encoding='utf8'))
assert sha((archive/'Huyen_Hoc_Cac.html').read_bytes())=='f9bd8a3b03f77f61885efb7f0bff5fbe477c54558e6766e636f8e63dd36b1579'
assert old['product']['sha256']==sha((archive/'Huyen_Hoc_Cac.html').read_bytes())
with zipfile.ZipFile(archive/'Huyen_Hoc_Cac_V53_source.zip') as z:
    assert z.read('v53/PACKAGE_MANIFEST.json')==(archive/'PACKAGE_MANIFEST.json').read_bytes()
    for f in ['engine.js','app.js','bazi-relations.js','bazi-cycles.js','index.html']:assert z.read('v53/'+f)==(archive/f).read_bytes(),f
with zipfile.ZipFile(archive/'Huyen_Hoc_Cac_V53_web.zip') as z:assert z.read('index.html')==(archive/'Huyen_Hoc_Cac.html').read_bytes()
for f in ['bazi-relations.js','bazi-cycles.js','bazi-locations.css','build.mjs','content.js','yi-complete-data.js','yi-context.js','fortune.js','fortune-context.js','fortune-months.js','home-measured-plan.js','index.html']:
    file='scripts/build.mjs' if f=='build.mjs' else f
    assert sha((root/file).read_bytes())==next(x['sha256'] for x in old['files'] if x['file']==file),file
new_engine=(root/'engine.js').read_text(encoding='utf8');old_engine=(archive/'engine.js').read_text(encoding='utf8')
assert new_engine[:new_engine.index('function baziCalcData')]==old_engine[:old_engine.index('function baziCalcData')]
assert new_engine[new_engine.index('function tvJDN'):new_engine.index('function bazi(input)')]==old_engine[old_engine.index('function tvJDN'):old_engine.index('function bazi(input)')]
assert new_engine[new_engine.index('function destiny'):] == old_engine[old_engine.index('function destiny'):]
qa=root/'qa/bazi-late-zi-option'
for file,count in [('SOURCE_RESULTS.json',9),('ENGINE_RESULTS.json',12),('BROWSER_RESULTS.json',26)]:
    j=json.loads((qa/file).read_text(encoding='utf8'));assert len(j['checks'])==count and all(x['ok'] for x in j['checks'])
core=json.loads((root/'qa/test-results.json').read_text(encoding='utf8'));assert len(core['checks'])==50 and all(c['ok'] for c in core['checks']) and not core['errors'] and not core['requests']
browser=json.loads((qa/'BROWSER_RESULTS.json').read_text(encoding='utf8'));assert not browser['errors'] and not browser['http']
engine=json.loads((qa/'ENGINE_RESULTS.json').read_text(encoding='utf8'));assert engine['summary']=={'legacyCharts':7936,'realReferenceCharts':7936,'affectedHourRelationChecks':3720,'imageExamples':2}
pdf=json.loads((qa/'PDF_RESULTS.json').read_text(encoding='utf8'));assert pdf['pages']==7 and all(v for k,v in pdf.items() if k not in ['pages','pageCharacters','pdfSHA256']);assert sha((qa/'late-zi-option.pdf').read_bytes())==pdf['pdfSHA256']
for n in range(1,8):assert (qa/f'print-page-{n}.png').stat().st_size>10000
base=root/'research/bazi-late-zi-witness';source=json.loads((qa/'SOURCE_RESULTS.json').read_text(encoding='utf8'))
assert source['manualSHA256']==sha((base/'MANUAL_READINGS.json').read_bytes())
assert source['summary']['pdfBytes']==58287949 and source['summary']['pdfPages']==486 and source['summary']['parentImageChecks']==13
assert sha((base/'NCL-000002203.pdf').read_bytes())==source['summary']['pdfSHA256']=='3dfee4ef4636d48c2d2e749f90408a825e0eacee99b8c73b9748a03deb73dcfd'
html=product.decode('utf8')
for f in ['engine.js','app.js']:assert (root/f).read_bytes().decode('utf8').strip() in html
assert 'lateZiHour' in html and 'MANUAL_READINGS.json' not in html and 'NCL-000002203' not in html
result={'htmlBytes':len(product),'htmlSHA256':sha(product),'manifestFiles':len(manifest['files']),'automatedChecks':97,'sourceChecks':9,'engineChecks':12,'browserChecks':26,'coreChecks':50,'legacyChartsPreserved':7936,'realLibraryCharts':7936,'affectedHourRelationChecks':3720,'imageReadExamples':2,'targetContentPages':8,'targetReadingUnits':3,'pdfPages':7,'allFinalPDFPagesManuallyReviewed':True,'priorReleasePreserved':True,'nonBaziCalculationBytesUnchanged':True,'sourceZIPFilesVerified':len(manifest['files'])+1,'siteClean':True,'fourResearchDirections':'active-not-complete'}
if '--no-write' not in sys.argv:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(result,ensure_ascii=False))
