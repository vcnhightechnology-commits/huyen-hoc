from pathlib import Path
import hashlib,json,zipfile,sys
root=Path(__file__).resolve().parent.parent;workspace=root.parent
sha=lambda b:hashlib.sha256(b).hexdigest()
m=json.loads((root/'PACKAGE_MANIFEST.json').read_text(encoding='utf-8'));product=(root/'Huyen_Hoc_Cac.html').read_bytes()
assert product==(root/'site/index.html').read_bytes()==(workspace/'Huyen_Hoc_Cac.html').read_bytes() and sha(product)==m['product']['sha256']
assert sorted(x.name for x in (root/'site').iterdir())==['index.html']
assert b'<script src=' not in product and b'<link rel="stylesheet"' not in product
for f in m['files']:
 b=(root/f['file']).read_bytes();assert len(b)==f['bytes'] and sha(b)==f['sha256'],f['file']
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_web.zip') as z:
 assert sorted(z.namelist())==['HUONG_DAN.md','index.html'];assert z.read('index.html')==product
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_source.zip') as z:
 assert z.read('v53/PACKAGE_MANIFEST.json')==(root/'PACKAGE_MANIFEST.json').read_bytes()
 for f in m['files']:assert sha(z.read('v53/'+f['file']))==f['sha256'],f['file']
archive=workspace/'archives/v53-before-fortune-context';assert sha((archive/'Huyen_Hoc_Cac.html').read_bytes())=='ec15e8bbda0445be2acfaa8c2c1a1b7fccc391bf22a91819ff25b5119948ee52'
old=json.loads((archive/'PACKAGE_MANIFEST.json').read_text(encoding='utf-8'))
for f in ['engine.js','app.js','content.js','tuvi-context.js','fortune-months.js','bazi-cycles.js','home-measured-plan.js']:
 assert sha((root/f).read_bytes())==next(x['sha256'] for x in old['files'] if x['file']==f)
with zipfile.ZipFile(archive/'Huyen_Hoc_Cac_V53_source.zip') as z:prior=z.read('v53/fortune.js').decode('utf-8')
current=(root/'fortune.js').read_bytes().decode('utf-8')
calculation=lambda s:s.split('function inspect(chart,value){',1)[1].split('function resultHTML(chart,r){',1)[0]
assert calculation(current)==calculation(prior)
for name,count in [('ENGINE_RESULTS.json',11),('BROWSER_RESULTS.json',19)]:
 r=json.loads((root/'qa/fortune-context'/name).read_text(encoding='utf-8'));assert len(r['checks'])==count and all(x['ok'] for x in r['checks'])
for name,count in [('core-regression.log',50),('four-regression.log',47),('months-regression.log',22)]:assert f'{count}/{count} passed' in (root/'qa/fortune-context'/name).read_text(encoding='utf-8')
p=json.loads((root/'qa/fortune-context/PDF_RESULTS.json').read_text(encoding='utf-8'));assert p['threeNatalContextsPresent'] and p['annualScopePresent'] and p['dateControlsHidden']
r={'htmlBytes':len(product),'htmlSHA256':sha(product),'manifestFiles':len(m['files']),'newChecks':30,'regressionChecks':119,'totalAutomatedChecks':149,'pdfPages':p['pages'],'publicPackageFiles':['HUONG_DAN.md','index.html'],'previousProductPreserved':True,'fortuneCalculationUnchanged':True,'scope':'Period reading with exact natal star membership and annual labels; source variants remain distinct.'}
if '--no-write' not in sys.argv:(root/'qa/fortune-context/RELEASE_RESULTS.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(r,ensure_ascii=False))
