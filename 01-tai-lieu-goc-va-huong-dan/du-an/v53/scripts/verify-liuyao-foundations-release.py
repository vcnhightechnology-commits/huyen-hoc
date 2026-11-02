from pathlib import Path
from hashlib import sha256
import json,sys,zipfile
root=Path(__file__).resolve().parent.parent;workspace=root.parent
base=root/'research/liuyao-foundations';qa=root/'qa/liuyao-foundations';archive=workspace/'archives/v53-before-liuyao-foundations'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda b:sha256(b).hexdigest()
html=(root/'Huyen_Hoc_Cac.html').read_bytes();manifest=read(root/'PACKAGE_MANIFEST.json');old=read(archive/'PACKAGE_MANIFEST.json')
assert len(html)==707411 and sha(html)==manifest['product']['sha256']==old['product']['sha256']=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html==(workspace/'Huyen_Hoc_Cac.html').read_bytes()==(root/'site/index.html').read_bytes()==(archive/'Huyen_Hoc_Cac.html').read_bytes()
assert sorted(p.name for p in(root/'site').iterdir())==['index.html']
allowed={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'}
immutable=0
for f in old['files']:
 if f['file']not in allowed:assert sha((root/f['file']).read_bytes())==f['sha256'],f['file'];immutable+=1
web=workspace/'Huyen_Hoc_Cac_V53_web.zip';assert web.read_bytes()==(archive/web.name).read_bytes()and web.stat().st_size==344047
assert(archive/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==846213328
with zipfile.ZipFile(web)as z:
 assert sorted(z.namelist())==['HUONG_DAN.md','index.html']and z.read('index.html')==html and z.read('HUONG_DAN.md')==(root/'README.md').read_bytes()
assert {p.relative_to(root).as_posix()for p in root.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json'}=={f['file']for f in manifest['files']}
for f in manifest['files']:
 b=(root/f['file']).read_bytes();assert len(b)==f['bytes']and sha(b)==f['sha256'],f['file']
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_source.zip')as z:
 assert set(z.namelist())=={'v53/'+f['file']for f in manifest['files']}|{'v53/PACKAGE_MANIFEST.json'}
 assert z.read('v53/PACKAGE_MANIFEST.json')==(root/'PACKAGE_MANIFEST.json').read_bytes()
 for f in manifest['files']:
  b=z.read('v53/'+f['file']);assert len(b)==f['bytes']and sha(b)==f['sha256'],f['file']
engine=read(qa/'ENGINE_RESULTS.json');assert len(engine['checks'])==16 and all(c['ok']for c in engine['checks'])and engine['htmlSHA256']==sha(html)
s=engine['summary'];assert s['actualHHCHexCalls']==8260 and s['exhaustiveStructures']==4096 and s['movingAnnotations']==12288
assert s['changedPalaceDiff']==3584 and s['changedKinAnchorDifferences']==9864
assert s['exhaustiveDigest']=='5c127081137371396489bee77ccb6b61c5b94946ef64a9c2a78ee2c706169060'
audit=read(base/'SOURCE_AUDIT.json');assert audit['httpAttempts']==8 and audit['retained200Bodies']==6 and audit['tlsFailuresWithoutResponseBody']==2
containers=read(qa/'PDF_CONTAINER_CHECKS.json');assert [x['pdfPages']for x in containers['sources']]==[394,60]and not containers['pdfAuthoring']
assert sum(len(x['inspectedPageContainers'])for x in containers['sources'])==10
for a in audit['sources']:assert sha((base/a['file']).read_bytes())==a['sha256']
manual=read(base/'MANUAL_READINGS.json');assert len(manual['records'])==28 and manual['counts']['lowResolutionNavigationPages']==84
for r in manual['records']:assert sha((base/r['image']).read_bytes())==r['imageSHA256']and not r['wholePageFullyTranscribed']
fixtures=read(base/'SOURCE_FIXTURES.json')['examples'];assert fixtures[0]['number']==63 and fixtures[1]['number']==64
assert all('changedNumber'not in f for f in fixtures[:2])and[ f['derivedChangedNumber']for f in fixtures[:2]]==[51,12]
rules=read(base/'RULES.json');assert not rules['consumerApplied']and not rules['fullLiuYaoImplemented']
state=read(workspace/'EXHAUSTIVE_WORK_STATE.json');assert state==read(root/'research/EXHAUSTIVE_WORK_STATE.json')and state['status']=='active-not-complete'and state['currentWork']['latestResearchReport']=='v53/LIUYAO_FOUNDATIONS_REPORT.md'
assert state['previousMaiHoaWork']['latestResearchReport']=='v53/MEIHUA_HOUR_TABLE_REPORT.md'
full=read(root/'research/full-study/WORK_STATE.json');assert full['overallStatus']=='active-not-complete'and full['latestResearchReport']=='LIUYAO_FOUNDATIONS_REPORT.md'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
coverage=read(root/'research/library-current/COVERAGE.json');assert coverage['counts']['wholeWorkApplied']==0 and coverage['counts']['status']=={'inherited_rule_claim':4,'partial_active':5,'research_only':4,'not_established':27}
for id in ['B02','B03']:
 b=next(x for x in coverage['catalogue']if x['id']==id);assert b['currentStatus']=='research_only'and not b['wholeWorkApplied']and not b['inheritedAccessLabelIsVerified']
work=read(base/'WORK_STATE.json');assert work['foundationComplete']and work['status']=='foundation-complete-deeper-study-active'and not work['consumerChanged']and not work['wholeBookApplied']
for t in [b'liuyao-reference',b'SOURCE_FIXTURES.json',b'kinBasisPalace']:assert t not in html
out={'date':'2026-10-27','sourceAndRuntimeChecks':16,'originalPDFs':2,'originalPDFPages':[394,60],'retainedHTTP200Bodies':6,'failedTLSAttemptsWithoutBody':2,'boundedImageRecords':28,'navigationOnlyPages':84,
 'sourceExamples':4,'palaceMembers':64,'najiaPositions':48,'kinCells':25,'shiYingStages':8,'explicitDayStemRows':10,'literalSpiritRotations':2,'derivedOtherSpiritRotations':4,
 'exhaustivePrimaryChangedPairs':4096,'actualHHCHexCalls':8260,'movingAnnotations':12288,'changedPalaceDifferencePairs':3584,'changedKinAnchorDifferenceAnnotations':9864,'exhaustiveDigest':s['exhaustiveDigest'],
 'consumerChanged':False,'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'previousSourceZIPPreservedBytes':846213328,
 'unchangedEarlierV53Files':immutable,'manifestFilesVerified':len(manifest['files']),'sourceZIPFilesVerified':len(manifest['files'])+1,'privateFoundationComplete':True,
 'fullLiuYaoImplemented':False,'allBookClausesCompleted':False,'predictiveAccuracyEstablished':False,'wholeBooksApplied':False,'wholeCatalogueCompleted':False}
if '--no-write'in sys.argv:assert read(qa/'RELEASE_RESULTS.json')==out
else:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
