from pathlib import Path
from hashlib import sha256
import json,sys,zipfile

root=Path(__file__).resolve().parent.parent
qa=root/'qa/meihua-reading'
base=root/'research/meihua-reading'
sha=lambda b:sha256(b).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf8'))
engine=read(qa/'RESULTS.json')
assert len(engine['checks'])==8 and all(c['ok']for c in engine['checks'])
for key,file in[('indexSHA256','DIGITAL_UNIT_DISPOSITIONS.json'),('tableSHA256','TRIGRAM_TABLE_FIELDS.json'),('manualSHA256','MANUAL_READINGS.json')]:assert engine[key]==sha((base/file).read_bytes())
assert engine['summary']['newExternalResponses']==0 and not engine['summary']['consumerChanged']and not engine['summary']['wholeBookCompleted']
assert engine['htmlSHA256']==sha((root/'Huyen_Hoc_Cac.html').read_bytes())=='9e49791aa5b64c49d2ef5201e566ab5d83438918efce7f8ce0cc2ff887363759'
assert (root/'site/index.html').read_bytes()==(root.parent/'Huyen_Hoc_Cac.html').read_bytes()==(root/'Huyen_Hoc_Cac.html').read_bytes()
manual=read(base/'MANUAL_READINGS.json')
assert len(manual['records'])==15 and len(manual['variants'])==8
assert next(v for v in manual['variants']if v['id']=='li-earth')['printedPages']==[121]
assert next(v for v in manual['variants']if v['id']=='western-marsh')['printedPages']==[121]
for r in manual['records']:assert sha((base/r['sourceImage']).read_bytes())==r['imageSHA256']
assert len(read(root/'research/meihua/EXTRACTED_PAGES.json')['pages'])==99
assert read(root/'research/full-study/WORK_STATE.json')['latestResearchReport']=='MEIHUA_READING_REPORT.md'
assert read(root/'research/full-study/WORK_STATE.json')['overallStatus']=='active-not-complete'
assert read(root/'research/EXHAUSTIVE_WORK_STATE.json')['status']=='active-not-complete'
assert read(root/'research/meihua-reading/FUNCTIONAL_BACKLOG.json')['status']=='active-not-complete'
m=read(root/'PACKAGE_MANIFEST.json')
by={f['file']:f for f in m['files']}
for p in list(base.rglob('*'))+list(qa.rglob('*')):
 if p.is_file():assert sha(p.read_bytes())==by[p.relative_to(root).as_posix()]['sha256'],p
with zipfile.ZipFile(root.parent/'Huyen_Hoc_Cac_V53_source.zip')as z:
 for f in m['files']:
  if f['file'].startswith(('research/meihua-reading/','qa/meihua-reading/','research/meihua/')):assert sha(z.read('v53/'+f['file']))==f['sha256'],f['file']
r={'researchChecks':8,'indexedDigitalSections':123,'trigramTables':8,'tableFields':214,'targetedImageReadings':15,'newContentPages':14,'expandedPriorPage':1,'sourceIssues':8,'additionalNumberExamples':3,'furtherArithmeticExamples':5,'retainedPNGDerivatives':99,'newExternalResponses':0,'consumerHTMLBytes':694834,'consumerHTMLSHA256':engine['htmlSHA256'],'consumerChanged':False,'wholeBookCompleted':False,'wholeCatalogueCompleted':False,'sourcePackageFiles':len(m['files'])+1}
if '--no-write'in sys.argv:assert read(qa/'RELEASE_RESULTS.json')==r
else:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(r,ensure_ascii=False))
