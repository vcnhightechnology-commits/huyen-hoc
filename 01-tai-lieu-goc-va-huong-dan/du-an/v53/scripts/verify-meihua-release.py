from pathlib import Path
from hashlib import sha256
import json,sys,zipfile

root=Path(__file__).resolve().parent.parent
workspace=root.parent
qa=root/'qa/meihua'
base=root/'research/meihua'
archive=workspace/'archives/v53-before-meihua'
sha=lambda b:sha256(b).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf8'))
m=read(root/'PACKAGE_MANIFEST.json')
old=read(archive/'PACKAGE_MANIFEST.json')
html=(root/'Huyen_Hoc_Cac.html').read_bytes()
assert html==(workspace/'Huyen_Hoc_Cac.html').read_bytes()==(root/'site/index.html').read_bytes()
assert len(html)==m['product']['bytes'] and sha(html)==m['product']['sha256']
assert sorted(p.name for p in (root/'site').iterdir())==['index.html']
assert b'<script src='not in html and b'<link rel="stylesheet"'not in html
assert (root/'meihua.js').read_bytes().strip()in html and(root/'meihua.css').read_bytes().strip()in html
assert not any(x in html for x in[b'NLC416',b'Wikisource',b'MANUAL_READINGS',b'af608094ab11ae2'])
assert {p.relative_to(root).as_posix()for p in root.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json'}=={f['file']for f in m['files']}
for f in m['files']:
 b=(root/f['file']).read_bytes()
 assert len(b)==f['bytes']and sha(b)==f['sha256'],f['file']
for f in old['files']:
 if '/'not in f['file']and f['file'].endswith(('.js','.css'))and f['file']!='app.js':
  assert sha((root/f['file']).read_bytes())==f['sha256'],f['file']
assert sha((archive/'Huyen_Hoc_Cac.html').read_bytes())==old['product']['sha256']=='57850abfad4a3c92069de448e3d654d427a4bd778d100b08925e5ba1c8330d8e'
assert (archive/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==799685060
with zipfile.ZipFile(archive/'Huyen_Hoc_Cac_V53_source.zip')as z:
 assert z.read('v53/PACKAGE_MANIFEST.json')==(archive/'PACKAGE_MANIFEST.json').read_bytes()
 assert z.read('v53/app.js')==(archive/'app.js').read_bytes()
with zipfile.ZipFile(archive/'Huyen_Hoc_Cac_V53_web.zip')as z:
 assert z.read('index.html')==(archive/'Huyen_Hoc_Cac.html').read_bytes()
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_web.zip')as z:
 assert sorted(z.namelist())==['HUONG_DAN.md','index.html']
 assert z.read('index.html')==html and z.read('HUONG_DAN.md')==(root/'README.md').read_bytes()
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_source.zip')as z:
 assert set(z.namelist())=={'v53/'+f['file']for f in m['files']}|{'v53/PACKAGE_MANIFEST.json'}
 assert z.read('v53/PACKAGE_MANIFEST.json')==(root/'PACKAGE_MANIFEST.json').read_bytes()
 for f in m['files']:assert sha(z.read('v53/'+f['file']))==f['sha256'],f['file']
for file,count in[(qa/'ENGINE_RESULTS.json',20),(qa/'BROWSER_RESULTS.json',38),(root/'qa/test-results.json',50)]:
 r=read(file)
 assert len(r['checks'])==count and all(x['ok']for x in r['checks'])
 assert not r.get('errors')and not r.get('http')and not r.get('requests')
engine=read(qa/'ENGINE_RESULTS.json')
assert engine['htmlSHA256']==sha(html)
assert engine['manualSHA256']==sha((base/'MANUAL_READINGS.json').read_bytes())
assert engine['rulesSHA256']==sha((base/'RULES.json').read_bytes())
assert engine['summary']['sourceWorkedExamples']==6 and not engine['summary']['fullBookCompleted']
assert engine['sourcePDFSHA256']==sha((base/'NLC416-12jh005426-44577.pdf').read_bytes())
pdf=read(qa/'PDF_RESULTS.json')
assert pdf['pages']==4 and pdf['visuallyReviewedPages']==[1,2,3,4]
assert pdf['pdfSHA256']==sha((qa/'plum-reading.pdf').read_bytes())
assert all(pdf[k]for k in['sourceComponentsVisible','bodyUseMutualAndChangedVisible','allSixPositionsVisible','inputAndResearchHidden','cardsTogether','readingHeadingWithIntro'])
for f in['plum-390.png','plum-1440.png',*[f'print-{n}.png'for n in range(1,5)],'plum-reading.txt','direction-reading.txt']:assert(qa/f).stat().st_size>500
state=read(root/'research/full-study/WORK_STATE.json')
assert state['overallStatus']=='active-not-complete'and state['latestConsumerReport']=='MEIHUA_REPORT.md'
assert next(x for x in state['items']if x['id']=='yi')['latestScope']=='../meihua/MANUAL_READINGS.json'
coverage=read(root/'research/library-current/COVERAGE.json')
assert next(x for x in coverage['catalogue']if x['id']=='B01')['currentStatus']=='partial_active'
assert coverage['counts']['wholeWorkApplied']==0
assert coverage['product']['sha256']==sha(html)
r={'htmlBytes':len(html),'htmlSHA256':sha(html),'automatedScopeChecks':108,'sourceRuntimeChecks':20,'browserChecks':38,'coreRegressionChecks':50,'sourceWorkedArithmeticExamples':6,'castingMethods':4,'structuralCases':384,'timeComponentTuples':51840,'directionCases':768,'soundCases':1728,'selectedSourceImages':25,'selectedContentImages':24,'endLeafImages':1,'frontMatterImages':11,'pdfPages':4,'siteClean':True,'previousReleasePreserved':True,'wholeBookCompleted':False,'wholeCatalogueCompleted':False,'manifestFilesVerified':len(m['files']),'sourceZIPFilesVerified':len(m['files'])+1}
if '--no-write'in sys.argv:assert read(qa/'RELEASE_RESULTS.json')==r
else:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(r,ensure_ascii=False))
