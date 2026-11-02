from pathlib import Path
import hashlib, json, shutil, zipfile, sys

root = Path(__file__).resolve().parent.parent
workspace = root.parent
product = root / 'Huyen_Hoc_Cac.html'
research_only = '--research-only' in sys.argv
site = root / 'site'
site.mkdir(exist_ok=True)
if not research_only:
    shutil.copyfile(product, site / 'index.html')
    shutil.copyfile(product, workspace / 'Huyen_Hoc_Cac.html')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

files = [p for p in root.rglob('*') if p.is_file() and p.name != 'PACKAGE_MANIFEST.json']
manifest = {'schema':'hhc.consumer.v53.package.v1', 'product':{'file':'Huyen_Hoc_Cac.html','bytes':product.stat().st_size,'sha256':sha(product)},'policy':'Local file identity hashes, not publisher signatures. Public package excludes development and research files.','files':[{'file':p.relative_to(root).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(files)]}
(root / 'PACKAGE_MANIFEST.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
webzip = workspace / 'Huyen_Hoc_Cac_V53_web.zip'
if not research_only:
    with zipfile.ZipFile(webzip, 'w', zipfile.ZIP_DEFLATED) as z:
        z.write(site / 'index.html', 'index.html')
        z.write(root / 'README.md', 'HUONG_DAN.md')
sourcezip = workspace / 'Huyen_Hoc_Cac_V53_source.zip'
with zipfile.ZipFile(sourcezip, 'w', zipfile.ZIP_DEFLATED) as z:
    for p in sorted(root.rglob('*')):
        if p.is_file(): z.write(p, 'v53/'+p.relative_to(root).as_posix())
with zipfile.ZipFile(webzip) as z:
    assert sorted(z.namelist()) == ['HUONG_DAN.md','index.html']
    assert hashlib.sha256(z.read('index.html')).hexdigest() == sha(product)
assert sha(workspace / 'Huyen_Hoc_Cac.html') == sha(product)
print(json.dumps({'htmlBytes':product.stat().st_size,'htmlSha256':sha(product),'webZipBytes':webzip.stat().st_size,'sourceZipBytes':sourcezip.stat().st_size,'manifestFiles':len(files)}, ensure_ascii=False))
