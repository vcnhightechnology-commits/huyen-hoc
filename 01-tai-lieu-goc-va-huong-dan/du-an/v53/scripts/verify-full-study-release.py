from pathlib import Path
import hashlib,json,zipfile,sys
root=Path(__file__).resolve().parent.parent
workspace=root.parent
sha=lambda b:hashlib.sha256(b).hexdigest()
manifest=json.loads((root/'PACKAGE_MANIFEST.json').read_text(encoding='utf-8'))
product=(root/'Huyen_Hoc_Cac.html').read_bytes()
assert sha(product)==manifest['product']['sha256']
assert product==(workspace/'Huyen_Hoc_Cac.html').read_bytes()==(root/'site/index.html').read_bytes()
assert sorted(p.name for p in (root/'site').iterdir())==['index.html']
assert b'<script src=' not in product and b'<link rel="stylesheet"' not in product
for f in manifest['files']:
 b=(root/f['file']).read_bytes();assert len(b)==f['bytes'] and sha(b)==f['sha256'],f['file']
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_web.zip') as z:
 assert sorted(z.namelist())==['HUONG_DAN.md','index.html'];assert z.read('index.html')==product
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_source.zip') as z:
 assert z.read('v53/PACKAGE_MANIFEST.json')==(root/'PACKAGE_MANIFEST.json').read_bytes()
 for f in manifest['files']:assert sha(z.read('v53/'+f['file']))==f['sha256'],f['file']
archive=workspace/'archives/v53-before-full-study'
assert sha((archive/'Huyen_Hoc_Cac.html').read_bytes())=='aacb2489cb840836d72b8627c985e78717468d67cad16301599d8618da5dedf4'
old=json.loads((archive/'PACKAGE_MANIFEST.json').read_text(encoding='utf-8'))
for f in ['engine.js','content.js','yi-complete-data.js','fortune.js','fortune-months.js','home-content.js']:
 assert sha((root/f).read_bytes())==next(x['sha256'] for x in old['files'] if x['file']==f),f
engine=json.loads((root/'qa/full-study/ENGINE_RESULTS.json').read_text(encoding='utf-8'))
browser=json.loads((root/'qa/full-study/BROWSER_RESULTS.json').read_text(encoding='utf-8'))
assert all(c['ok'] for c in engine['checks']) and len(engine['checks'])==14
assert all(c['ok'] for c in browser['checks']) and len(browser['checks'])==34
assert not browser['errors'] and not browser['requests']
for name,count in [('core-regression.log',50),('four-regression.log',47)]:assert f'{count}/{count} passed' in (root/'qa/full-study'/name).read_text(encoding='utf-8')
state=json.loads((root/'research/full-study/WORK_STATE.json').read_text(encoding='utf-8'))
assert state['overallStatus']=='active-not-complete' and len(state['items'])==4
result={'htmlSHA256':sha(product),'htmlBytes':len(product),'manifestFiles':len(manifest['files']),'engineChecks':14,'browserChecks':34,'regressionChecks':97,'siteFiles':['index.html'],'publicZipFiles':['HUONG_DAN.md','index.html'],'historicalProductPreserved':True,'allFourResearchDirectionsComplete':False,'validation':'Product, sourceZIP, manifest and recorded files verified. Use --no-write for the final read-only validation after packaging this record.'}
if '--no-write' not in sys.argv:
 (root/'qa/full-study/RELEASE_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
