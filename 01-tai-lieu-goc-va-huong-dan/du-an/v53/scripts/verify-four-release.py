from pathlib import Path
import hashlib,json,zipfile

root=Path(__file__).resolve().parent.parent
workspace=root.parent
digest=lambda b:hashlib.sha256(b).hexdigest()
product=(root/'Huyen_Hoc_Cac.html').read_bytes()
manifest=json.loads((root/'PACKAGE_MANIFEST.json').read_text(encoding='utf-8'))
assert manifest['product']['sha256']==digest(product)
assert manifest['product']['bytes']==len(product)
assert all((p.read_bytes()==product) for p in [workspace/'Huyen_Hoc_Cac.html',root/'site/index.html'])
assert sorted(p.name for p in (root/'site').iterdir())==['index.html']
for f in manifest['files']:
 body=(root/f['file']).read_bytes()
 assert len(body)==f['bytes'] and digest(body)==f['sha256'],f['file']
print('PASS Three identical HTML copies, clean site and every manifest byte/hash')
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_web.zip') as z:
 assert sorted(z.namelist())==['HUONG_DAN.md','index.html']
 assert z.read('index.html')==product
 assert z.read('HUONG_DAN.md')==(root/'README.md').read_bytes()
print('PASS Web ZIP contains only current HTML and current consumer guide')
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_source.zip') as z:
 expected=['v53/'+p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()]
 assert sorted(expected)==sorted(z.namelist())
 assert z.read('v53/PACKAGE_MANIFEST.json')==(root/'PACKAGE_MANIFEST.json').read_bytes()
 for f in manifest['files']:
  assert digest(z.read('v53/'+f['file']))==f['sha256'],f['file']
print('PASS Source ZIP contains all current sources, report, evidence and QA with matching hashes')
snapshot=workspace/'archives/v53-before-four-items'
for f in json.loads((snapshot/'PRESERVED.json').read_text(encoding='utf-8')):
 body=(snapshot/f['file']).read_bytes()
 assert len(body)==f['bytes'] and digest(body)==f['sha256']
print('PASS All four preserved pre-change artifacts keep their original bytes')
checks=[]
for file,count in [('qa/four-items/engine-tests.json',14),('qa/four-items/fortune-policy-tests.json',7),('qa/four-items/browser-tests.json',47),('qa/test-results.json',50),('qa/home-guide/test-results.json',40),('qa/experience/test-results.json',36)]:
 data=json.loads((root/file).read_text(encoding='utf-8'))
 assert len(data['checks'])==count and all(x['ok'] for x in data['checks']),file
 checks+=data['checks']
assert len(checks)==194
print('PASS All six final test reports account for 194 successful checks')
for token in ['YI_REVIEW','SOURCE_AUDIT','ndl-760737','yuanhai-NTL','kanripo','sourceLineLabel']:
 assert token not in product.decode('utf-8'),token
print('PASS Standalone product contains no private source/corpus payload identifiers')
print(json.dumps({'htmlBytes':len(product),'htmlSHA256':digest(product),'passedChecks':len(checks),'releaseChecks':6,'publication':'local only'},ensure_ascii=False))
