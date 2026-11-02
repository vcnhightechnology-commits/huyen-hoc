from pathlib import Path
import hashlib,json,zipfile,sys
root=Path(__file__).resolve().parent.parent
workspace=root.parent
sha=lambda b:hashlib.sha256(b).hexdigest()
m=json.loads((root/'PACKAGE_MANIFEST.json').read_text(encoding='utf-8'));product=(root/'Huyen_Hoc_Cac.html').read_bytes()
assert product==(root/'site/index.html').read_bytes()==(workspace/'Huyen_Hoc_Cac.html').read_bytes()
assert sha(product)==m['product']['sha256']
assert sorted(x.name for x in (root/'site').iterdir())==['index.html']
assert b'<script src=' not in product and b'<link rel="stylesheet"' not in product
for f in m['files']:
 b=(root/f['file']).read_bytes();assert sha(b)==f['sha256'] and len(b)==f['bytes'],f['file']
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_web.zip') as z:
 assert sorted(z.namelist())==['HUONG_DAN.md','index.html'];assert z.read('index.html')==product
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_source.zip') as z:
 assert z.read('v53/PACKAGE_MANIFEST.json')==(root/'PACKAGE_MANIFEST.json').read_bytes()
 for f in m['files']:assert sha(z.read('v53/'+f['file']))==f['sha256'],f['file']
old=workspace/'archives/v53-before-measured-plan';assert sha((old/'Huyen_Hoc_Cac.html').read_bytes())=='b286bb521a8dc6e77ca4314f65db7ca7cd4ee3293c515cefe9cf09a16513492d'
prior=json.loads((old/'PACKAGE_MANIFEST.json').read_text(encoding='utf-8'))
for f in ['engine.js','app.js','home-guide.js','home-content.js','bearing-guide.js','mountains.js']:
 assert sha((root/f).read_bytes())==next(x['sha256'] for x in prior['files'] if x['file']==f)
for name,count in [('GEOMETRY_RESULTS.json',18),('BROWSER_RESULTS.json',25)]:
 r=json.loads((root/'qa/measured-plan'/name).read_text(encoding='utf-8'));assert len(r['checks'])==count and all(x['ok'] for x in r['checks'])
for name,count in [('home-regression.log',40),('core-regression.log',50)]:assert f'{count}/{count} passed' in (root/'qa/measured-plan'/name).read_text(encoding='utf-8')
pdf=json.loads((root/'qa/measured-plan/PDF_RESULTS.json').read_text(encoding='utf-8'));assert pdf['editingAndNavigationHidden'] and pdf['allRoomsAndOpeningsPresent']
r={'htmlBytes':len(product),'htmlSHA256':sha(product),'manifestFiles':len(m['files']),'newChecks':43,'regressionChecks':90,'totalAutomatedChecks':133,'pdfPages':pdf['pages'],'publicPackageFiles':['HUONG_DAN.md','index.html'],'previousProductPreserved':True,'scope':'Rectangular measured floorplan; research of all four fields remains active.'}
if '--no-write' not in sys.argv:(root/'qa/measured-plan/RELEASE_RESULTS.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(r,ensure_ascii=False))
