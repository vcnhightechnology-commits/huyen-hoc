from pathlib import Path
from hashlib import sha256
import json,sys,zipfile

root=Path(__file__).resolve().parent.parent
workspace=root.parent
archive=workspace/'archives/v53-before-meihua-methods'
qa=root/'qa/meihua-methods'
base=root/'research/meihua-methods'
sha=lambda b:sha256(b).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf8'))
m=read(root/'PACKAGE_MANIFEST.json');old=read(archive/'PACKAGE_MANIFEST.json')
html=(root/'Huyen_Hoc_Cac.html').read_bytes()
assert html==(root/'site/index.html').read_bytes()==(workspace/'Huyen_Hoc_Cac.html').read_bytes()
assert len(html)==m['product']['bytes']and sha(html)==m['product']['sha256']
assert sorted(p.name for p in(root/'site').iterdir())==['index.html']
assert b'<script src='not in html and b'<link rel="stylesheet"'not in html
assert(root/'meihua.js').read_bytes().strip()in html
assert not any(x in html for x in[b'Wikisource',b'NLC416',b'MANUAL_READINGS',b'SOURCE_APPLICATION'])
assert {p.relative_to(root).as_posix()for p in root.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json'}=={f['file']for f in m['files']}
for f in m['files']:
 b=(root/f['file']).read_bytes();assert len(b)==f['bytes']and sha(b)==f['sha256'],f['file']
for f in old['files']:
 if '/'not in f['file']and f['file'].endswith(('.js','.css'))and f['file']!='meihua.js':assert sha((root/f['file']).read_bytes())==f['sha256'],f['file']
assert sha((archive/'Huyen_Hoc_Cac.html').read_bytes())==old['product']['sha256']=='9e49791aa5b64c49d2ef5201e566ab5d83438918efce7f8ce0cc2ff887363759'
assert(archive/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==818758618
with zipfile.ZipFile(archive/'Huyen_Hoc_Cac_V53_source.zip')as z:
 assert z.read('v53/PACKAGE_MANIFEST.json')==(archive/'PACKAGE_MANIFEST.json').read_bytes()
 assert z.read('v53/meihua.js')==(archive/'meihua.js').read_bytes()
with zipfile.ZipFile(archive/'Huyen_Hoc_Cac_V53_web.zip')as z:assert z.read('index.html')==(archive/'Huyen_Hoc_Cac.html').read_bytes()
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_web.zip')as z:
 assert sorted(z.namelist())==['HUONG_DAN.md','index.html']
 assert z.read('index.html')==html and z.read('HUONG_DAN.md')==(root/'README.md').read_bytes()
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_source.zip')as z:
 assert set(z.namelist())=={'v53/'+f['file']for f in m['files']}|{'v53/PACKAGE_MANIFEST.json'}
 assert z.read('v53/PACKAGE_MANIFEST.json')==(root/'PACKAGE_MANIFEST.json').read_bytes()
 for f in m['files']:assert sha(z.read('v53/'+f['file']))==f['sha256'],f['file']
for file,count in[('ENGINE_RESULTS.json',12),('BROWSER_RESULTS.json',50)]:
 r=read(qa/file);assert len(r['checks'])==count and all(c['ok']for c in r['checks']);assert not r.get('errors')and not r.get('http')
engine=read(qa/'ENGINE_RESULTS.json')
assert engine['htmlSHA256']==sha(html)and engine['moduleSHA256']==sha((root/'meihua.js').read_bytes())
assert engine['summary']['legacyParityCases']==467 and engine['summary']['sourceWorkedExamples']==6 and engine['summary']['existingComposeUnchanged']
pdf=read(qa/'PDF_RESULTS.json')
assert pdf['pages']==4 and pdf['visuallyReviewedPages']==[1,2,3,4]and pdf['finalRenderMatchesVisuallyReviewedPNGs']
assert pdf['pdfSHA256']==sha((qa/'historical-tones.pdf').read_bytes())
for r in pdf['renderedPages']:assert r['sha256']==sha((qa/f"print-{r['page']}.png").read_bytes())
for f in['tones-390.png','tones-1440.png','historical-tones.txt']:assert(qa/f).stat().st_size>500
application=read(base/'SOURCE_APPLICATION.json');assert application['newExternalResponses']==application['newImageReadings']==0 and not application['wholeBookCompleted']
assert len(application['rules'])==7 and len(application['reusedImageEvidence'])==9
assert application['sourcePDFSHA256']==sha((base/application['sourcePDF']).read_bytes())
for r in application['reusedImageEvidence']:assert sha((base/r['image']).read_bytes())==r['imageSHA256']
state=read(root/'research/full-study/WORK_STATE.json')
assert state['overallStatus']=='active-not-complete'and state['latestConsumerReport']=='MEIHUA_METHODS_REPORT.md'
assert next(r for r in state['items']if r['id']=='yi')['latestScope']=='../meihua-methods/SOURCE_APPLICATION.json'
coverage=read(root/'research/library-current/COVERAGE.json');assert coverage['counts']['wholeWorkApplied']==0 and coverage['product']['sha256']==sha(html)
r={'htmlBytes':len(html),'htmlSHA256':sha(html),'scopeChecks':62,'sourceRuntimeChecks':12,'browserChecks':50,'topLevelMethodChoices':8,'wordSubmodes':4,'newInputVariants':7,'sourceWorkedExamples':6,'syntheticRuleFixtures':6,'legacyParityCases':467,'longCharacterLengths':90,'sourceImagesReused':9,'newSourceResponses':0,'newImageReadings':0,'pdfPages':4,'otherJSAndCSSUnchanged':True,'composeUnchanged':True,'siteClean':True,'previousReleasePreserved':True,'wholeBookCompleted':False,'wholeCatalogueCompleted':False,'manifestFilesVerified':len(m['files']),'sourceZIPFilesVerified':len(m['files'])+1}
if '--no-write'in sys.argv:assert read(qa/'RELEASE_RESULTS.json')==r
else:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(r,ensure_ascii=False))
