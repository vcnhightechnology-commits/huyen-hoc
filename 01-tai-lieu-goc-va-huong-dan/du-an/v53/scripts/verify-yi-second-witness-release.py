from pathlib import Path
from hashlib import sha256
import json,zipfile,sys
from PIL import Image
root=Path(__file__).resolve().parent.parent;workspace=root.parent
sha=lambda b:sha256(b).hexdigest()
manifest=json.loads((root/'PACKAGE_MANIFEST.json').read_text(encoding='utf8'));product=(root/'Huyen_Hoc_Cac.html').read_bytes()
assert product==(workspace/'Huyen_Hoc_Cac.html').read_bytes()==(root/'site/index.html').read_bytes()
assert len(product)==manifest['product']['bytes'] and sha(product)==manifest['product']['sha256']
assert [p.name for p in (root/'site').iterdir()]==['index.html']
for f in manifest['files']:
 b=(root/f['file']).read_bytes();assert len(b)==f['bytes'] and sha(b)==f['sha256'],f['file']
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_web.zip') as z:
 assert sorted(z.namelist())==['HUONG_DAN.md','index.html'];assert z.read('index.html')==product
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_source.zip') as z:
 assert z.read('v53/PACKAGE_MANIFEST.json')==(root/'PACKAGE_MANIFEST.json').read_bytes()
 for f in manifest['files']:assert sha(z.read('v53/'+f['file']))==f['sha256'],f['file']
archive=workspace/'archives/v53-before-yi-second-witness';old=json.loads((archive/'PACKAGE_MANIFEST.json').read_text(encoding='utf8'))
assert sha((archive/'Huyen_Hoc_Cac.html').read_bytes())=='99451380b729a68e5a0cf3dacf7b16134ced191bebe3d9aca85988f8a65a4635'
assert old['product']['sha256']==sha((archive/'Huyen_Hoc_Cac.html').read_bytes())
with zipfile.ZipFile(archive/'Huyen_Hoc_Cac_V53_source.zip') as z:
 assert z.read('v53/PACKAGE_MANIFEST.json')==(archive/'PACKAGE_MANIFEST.json').read_bytes()
 assert z.read('v53/yi-complete-data.js')==(archive/'yi-complete-data.js').read_bytes()
for f in ['engine.js','app.js','content.js','yi-content.js','yi-lines.js','yi-context.js','fortune.js','bazi-cycles.js','home-measured-plan.js','research/full-study/yi/facsimile-384-audit.json','research/full-study/yi/yao-384-collation-queue.json']:
 assert sha((root/f).read_bytes())==next(x['sha256'] for x in old['files'] if x['file']==f)
base=root/'research/yi-second-witness'
for r in json.loads((base/'DERIVATIVES.json').read_text(encoding='utf8'))['records']:
 b=(base/r['file']).read_bytes();assert len(b)==r['bytes'] and sha(b)==r['sha256'];assert sha((base/r['parent']).read_bytes())==r['parentSha256']
 box=r['cropBox'];expected=Image.open(base/r['parent']).crop(box).resize(((box[2]-box[0])*r['resize'],(box[3]-box[1])*r['resize']));actual=Image.open(base/r['file']);assert actual.size==expected.size and actual.tobytes()==expected.tobytes()
for name,count in [('ENGINE_RESULTS.json',15),('BROWSER_RESULTS.json',15)]:
 j=json.loads((root/'qa/yi-second-witness'/name).read_text(encoding='utf8'));assert len(j['checks'])==count and all(x['ok'] for x in j['checks'])
assert json.loads((root/'qa/yi-second-witness/ENGINE_RESULTS.json').read_text(encoding='utf8'))['htmlSHA256']==sha(product)
result={'htmlBytes':len(product),'htmlSHA256':sha(product),'manifestFiles':len(manifest['files']),'automatedScopeChecks':30,'realEngineCastPatterns':4096,'sourceTargetPositions':16,'commentaryPassages':5,'consumerPositionsRefined':4,'derivativePixelChecks':8,'priorReleasePreserved':True,'calculationsUnchanged':True,'siteClean':True,'sourceZIPFilesVerified':len(manifest['files'])+1,'scope':'Second attributed scan with qualified edition date; four editorial refinements. Four-direction research remains active.'}
if '--no-write' not in sys.argv:(root/'qa/yi-second-witness/RELEASE_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(result,ensure_ascii=False))
