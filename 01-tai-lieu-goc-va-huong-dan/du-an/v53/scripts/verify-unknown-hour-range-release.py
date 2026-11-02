from pathlib import Path
import hashlib,json,zipfile,sys
root=Path(__file__).resolve().parent.parent;workspace=root.parent
sha=lambda b:hashlib.sha256(b).hexdigest()
m=json.loads((root/'PACKAGE_MANIFEST.json').read_text(encoding='utf-8'));product=(root/'Huyen_Hoc_Cac.html').read_bytes()
assert sha(product)==m['product']['sha256'] and product==(root/'site/index.html').read_bytes()==(workspace/'Huyen_Hoc_Cac.html').read_bytes()
assert sorted(x.name for x in (root/'site').iterdir())==['index.html']
assert b'<script src=' not in product and b'<link rel="stylesheet"' not in product
for f in m['files']:
 b=(root/f['file']).read_bytes();assert sha(b)==f['sha256'] and len(b)==f['bytes'],f['file']
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_web.zip') as z:
 assert sorted(z.namelist())==['HUONG_DAN.md','index.html'];assert z.read('index.html')==product
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_source.zip') as z:
 assert z.read('v53/PACKAGE_MANIFEST.json')==(root/'PACKAGE_MANIFEST.json').read_bytes()
 for f in m['files']:assert sha(z.read('v53/'+f['file']))==f['sha256'],f['file']
archive=workspace/'archives/v53-before-unknown-hour-range'
assert sha((archive/'Huyen_Hoc_Cac.html').read_bytes())=='74d397db30d9b14c83dba0f5dfbb76aa9285d1a8c9e92540b9c8870a034dad2d'
old=json.loads((archive/'PACKAGE_MANIFEST.json').read_text(encoding='utf-8'))
for f in ['engine.js','app.js','bazi-relations.js','home-measured-plan.js','fortune.js','fortune-months.js']:
 assert sha((root/f).read_bytes())==next(x['sha256'] for x in old['files'] if x['file']==f)
for name,count in [('ENGINE_RESULTS.json',8),('BROWSER_RESULTS.json',16)]:
 r=json.loads((root/'qa/unknown-hour-range'/name).read_text(encoding='utf-8'));assert len(r['checks'])==count and all(x['ok'] for x in r['checks'])
for name,count in [('core-regression.log',50),('full-study-regression.log',34)]:assert f'{count}/{count} passed' in (root/'qa/unknown-hour-range'/name).read_text(encoding='utf-8')
p=json.loads((root/'qa/unknown-hour-range/PDF_RESULTS.json').read_text(encoding='utf-8'));assert p['bothOnsetBounds'] and p['tenTransitionRanges']
r={'htmlBytes':len(product),'htmlSHA256':sha(product),'manifestFiles':len(m['files']),'newChecks':24,'regressionChecks':84,'totalAutomatedChecks':108,'pdfPages':p['pages'],'publicPackageFiles':['HUONG_DAN.md','index.html'],'previousProductPreserved':True,'scope':'Unknown birth-hour bounds; other full-study research remains active.'}
if '--no-write' not in sys.argv:(root/'qa/unknown-hour-range/RELEASE_RESULTS.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(r,ensure_ascii=False))
