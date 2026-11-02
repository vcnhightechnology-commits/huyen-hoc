from pathlib import Path
from hashlib import sha256
import json,sys,zipfile

root=Path(__file__).resolve().parent.parent; workspace=root.parent
base=root/'research/meihua-layers';qa=root/'qa/meihua-layers';archive=workspace/'archives/v53-before-meihua-layers-release'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda b:sha256(b).hexdigest()
html=(root/'Huyen_Hoc_Cac.html').read_bytes();manifest=read(root/'PACKAGE_MANIFEST.json');old=read(archive/'PACKAGE_MANIFEST.json')
assert len(html)==707411 and sha(html)==manifest['product']['sha256']=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html==(workspace/'Huyen_Hoc_Cac.html').read_bytes()==(root/'site/index.html').read_bytes()==(base/'candidate/Huyen_Hoc_Cac.html').read_bytes()
assert sorted(p.name for p in (root/'site').iterdir())==['index.html']
for name in ['meihua.js','meihua.css']:assert(root/name).read_bytes()==(base/'candidate'/name).read_bytes() and(root/name).read_bytes()in html
assert b'<details class="mh-layers result-expand-export"'in html
for s in [b'Wikisource',b'NLC416',b'MANUAL_READINGS',b'SOURCE_APPLICATION',b'palace-reference',b'conditions-reference']:assert s not in html,s
allowed={'Huyen_Hoc_Cac.html','site/index.html','meihua.js','meihua.css','NEXT_STEPS.md','README.md','qa/test-results.json',
 'research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md',
 'research/meihua-layers/PENDING.json','research/meihua-layers/README.md','research/meihua-reading/FUNCTIONAL_BACKLOG.json','scripts/verify-meihua-layers-browser.mjs'}
immutable=0;old_modules=0
for f in old['files']:
 n=f['file'];b=(root/n).read_bytes()
 if n not in allowed and not(n.startswith('qa/') and n.endswith('.png') and '/'not in n[3:]):assert sha(b)==f['sha256'],n;immutable+=1
 if '/'not in n and n.endswith(('.js','.css'))and n not in ['meihua.js','meihua.css']:assert sha(b)==f['sha256'],n;old_modules+=1
assert (archive/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==837507250 and (archive/'Huyen_Hoc_Cac_V53_web.zip').stat().st_size==342884
assert sha((archive/'Huyen_Hoc_Cac.html').read_bytes())==old['product']['sha256']=='3800162854742c915d60f0051c65cadb0eb9a1c803f9f937bf1b6a593c96d268'
with zipfile.ZipFile(archive/'Huyen_Hoc_Cac_V53_web.zip')as z:assert z.read('index.html')==(archive/'Huyen_Hoc_Cac.html').read_bytes()
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_web.zip')as z:
 assert sorted(z.namelist())==['HUONG_DAN.md','index.html'] and z.read('index.html')==html and z.read('HUONG_DAN.md')==(root/'README.md').read_bytes()
assert {p.relative_to(root).as_posix()for p in root.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json'}=={f['file']for f in manifest['files']}
for f in manifest['files']:
 b=(root/f['file']).read_bytes();assert len(b)==f['bytes']and sha(b)==f['sha256'],f['file']
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_source.zip')as z:
 assert set(z.namelist())=={'v53/'+f['file']for f in manifest['files']}|{'v53/PACKAGE_MANIFEST.json'}
 assert z.read('v53/PACKAGE_MANIFEST.json')==(root/'PACKAGE_MANIFEST.json').read_bytes()
 for f in manifest['files']:
  b=z.read('v53/'+f['file']);assert len(b)==f['bytes']and sha(b)==f['sha256'],f['file']
engine=read(qa/'ENGINE_RESULTS.json');browser=read(qa/'BROWSER_RESULTS.json');core=read(qa/'core-test-results.json');pdf=read(qa/'PDF_RESULTS.json');pending=read(base/'PENDING.json')
for d,n in [(engine,14),(browser,34),(core,50)]:assert len(d['checks'])==n and all(c['ok']for c in d['checks'])
assert not browser['errors']and not browser['http']and browser['pdfCreated']and not core['errors']and not core['requests']
assert engine['htmlSHA256']==sha(html)and engine['summary']['inputAndCastingFunctionsUnchanged']
assert pdf['pages']==4 and pdf['visuallyReviewedPages']==[1,2,3,4]and sha((qa/'body-use-layers.pdf').read_bytes())==pdf['pdfSHA256']=='210768dad70380f68fa687eaf92f16169ce589db3af53a388857e3ea6135045b'
for r in pdf['renderedPages']:assert sha((qa/f"print-{r['page']}.png").read_bytes())==r['sha256']
for k in ['explicitInputSummary','fourLayerLabels','mixedRelationsSeparate','mutualRolesVisible','sixReflectionPositions','inputAndToastHidden','researchHidden','cardContentsTogether']:assert pdf[k]
assert pending['released']and pending['browserChecksExecuted']==34 and pending['pdfCreated']and pending['block']is None
for f in pending['candidateFiles']:assert sha((base/'candidate'/f['file']).read_bytes())==f['sha256']
source=read(base/'SOURCE_APPLICATION.json');assert source['newHTTPResponses']==source['newPageReadings']==0
for r in source['reusedImages']:assert sha((root/'research/meihua-reading'/r['sourceImage']).read_bytes())==r['imageSHA256']
state=read(workspace/'EXHAUSTIVE_WORK_STATE.json');assert state==read(root/'research/EXHAUSTIVE_WORK_STATE.json')and state['status']=='active-not-complete'and state['currentWork']['latestReport']=='v53/MEIHUA_LAYERS_REPORT.md'
full=read(root/'research/full-study/WORK_STATE.json');assert full['overallStatus']=='active-not-complete'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'and full['latestResearchReport']=='MEIHUA_VOLUME1_REPORT.md'
coverage=read(root/'research/library-current/COVERAGE.json');assert coverage['counts']['wholeWorkApplied']==0 and coverage['product']['sha256']==sha(html)
out={'primaryChecks':98,'calculationChecks':14,'candidateBrowserChecks':34,'integratedCoreChecks':50,'structures':384,'layerRelations':1536,'pureCases':12,
 'sourceSurnameExamples':3,'priorMethodFixtures':12,'newHTTPResponses':0,'newPageReadings':0,'pdfPages':4,'pdfVisualReviewComplete':True,'pdfContentAssertions':8,
 'htmlBytes':len(html),'htmlSHA256':sha(html),'candidateMatchesIntegratedHTML':True,'siteClean':True,'webPackageVerified':True,'manifestFilesVerified':len(manifest['files']),
 'sourceZIPFilesVerified':len(manifest['files'])+1,'unchangedEarlierV53Files':immutable,'otherRootJSCSSModulesUnchanged':old_modules,'previousSourceZIPPreservedBytes':837507250,
 'previousWebZIPPreservedBytes':342884,'historicalApprovalBlockResolved':True,'candidateReleased':True,'wholeBookApplied':False,'wholeCatalogueCompleted':False,'predictiveAccuracyEstablished':False}
if '--no-write'in sys.argv:assert read(qa/'RELEASE_RESULTS.json')==out
else:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
