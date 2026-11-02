from pathlib import Path
from hashlib import sha256
import json,sys,zipfile
root=Path(__file__).resolve().parent.parent;w=root.parent;base=root/'research/liuyao-progress-conditions';qa=root/'qa/liuyao-progress-conditions'
archive=w/'archives/v53-before-liuyao-progress-conditions';read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda b:sha256(b).hexdigest()
old=read(archive/'PACKAGE_MANIFEST.json');manifest=read(root/'PACKAGE_MANIFEST.json');html=(root/'Huyen_Hoc_Cac.html').read_bytes()
assert len(html)==707411 and sha(html)==old['product']['sha256']==manifest['product']['sha256']=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html==(w/'Huyen_Hoc_Cac.html').read_bytes()==(root/'site/index.html').read_bytes()==(archive/'Huyen_Hoc_Cac.html').read_bytes()
assert sorted(p.name for p in(root/'site').iterdir())==['index.html']
mutable={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'}
unchanged=0
for f in old['files']:
 if f['file']not in mutable:assert sha((root/f['file']).read_bytes())==f['sha256'],f['file'];unchanged+=1
assert len(old['files'])==2770 and(archive/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==2002252441
web=w/'Huyen_Hoc_Cac_V53_web.zip';assert web.stat().st_size==344047 and web.read_bytes()==(archive/web.name).read_bytes()
with zipfile.ZipFile(web)as z:assert sorted(z.namelist())==['HUONG_DAN.md','index.html']and z.read('index.html')==html
assert{p.relative_to(root).as_posix()for p in root.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json'}=={f['file']for f in manifest['files']}
for f in manifest['files']:
 b=(root/f['file']).read_bytes();assert len(b)==f['bytes']and sha(b)==f['sha256'],f['file']
with zipfile.ZipFile(w/'Huyen_Hoc_Cac_V53_source.zip')as z:
 assert set(z.namelist())=={'v53/'+f['file']for f in manifest['files']}|{'v53/PACKAGE_MANIFEST.json'}
 assert z.read('v53/PACKAGE_MANIFEST.json')==(root/'PACKAGE_MANIFEST.json').read_bytes()
 for f in manifest['files']:
  b=z.read('v53/'+f['file']);assert len(b)==f['bytes']and sha(b)==f['sha256'],f['file']
e=read(qa/'ENGINE_RESULTS.json');s=e['summary'];assert len(e['checks'])==14 and all(c['ok']for c in e['checks'])and e['htmlSHA256']==sha(html)
assert s=={'actualHHCHexCalls':4,'printedCastFixtures':2,'actualLunarCalls':10,'explicitLuAgreements':6,'unfilledLuRows':4,
 'motionPatterns':64,'uniqueMovingPatterns':6,'uniqueStationaryPatterns':6,'manualRecords':24,'firstPassChapterSpans':5,
 'boundedClauses':19,'QAOnlySourceRenders':7,'QAImages':8,'B02RegisteredUnits':136,'B02HeadingOnlyBodyUnits':98,'B02FirstPassUnits':31}
manual=read(base/'MANUAL_READINGS.json');assert [r['pdfPage']for r in manual['records']]==list(range(116,140))
for r in manual['records']+manual['qaImages']+manual['additionalTOCAuditReadings']:assert sha((base/r['image']).read_bytes())==r['sha256']
assert sha((base/manual['sourcePDF']).read_bytes())==manual['sourceSHA256']=='caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa'
assert manual['directEnd']=={'pdfPage':138,'reading':'增刪卜易卷二終'}and not manual['wholeBookApplied']
units=read(base/'B02_CURRENT_UNITS.json');assert(units['currentCounts']['registeredUnits'],units['currentCounts']['headingOnlyBodyUnits'],units['currentCounts']['firstPassCompleteSpanUnits'],units['currentCounts']['wholeUnitsApplied'])==(136,98,31,0)
assert units['priorTOCSHA256']==sha((root/'research/liuyao-void-motion/B02_CURRENT_UNITS.json').read_bytes())
assert read(base/'CHAPTER_SPANS.json')['numberingConflict']['bodyPrintedNumberAsRead']==31
assert next(r for r in units['units']if r['id']=='B02-ch033')['tocVolume']==2
stars=read(base/'STAR_COORDINATES.json');assert stars['nobleman']['gengStatus']=='within-page-conflict-not-resolved'
assert len(stars['salary']['explicitRows'])==6 and not stars['salary']['missingFourRowsFilledFromRuntime']
assert len(read(base/'PRINTED_FIXTURES.json')['fixtures'])==2 and len(read(base/'OPERATIONAL_CLAUSES.json')['clauses'])==19
state=read(w/'EXHAUSTIVE_WORK_STATE.json');assert state==read(root/'research/EXHAUSTIVE_WORK_STATE.json')and state['status']=='active-not-complete'
assert state['currentWork']['latestResearchReport']=='v53/LIUYAO_PROGRESS_CONDITIONS_REPORT.md'
assert state['currentWork']['currentB02UnitMap']=='v53/research/liuyao-progress-conditions/B02_CURRENT_UNITS.json'
full=read(root/'research/full-study/WORK_STATE.json');assert full['overallStatus']=='active-not-complete'and full['latestResearchReport']=='LIUYAO_PROGRESS_CONDITIONS_REPORT.md'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
coverage=read(root/'research/library-current/COVERAGE.json');assert coverage['counts']['wholeWorkApplied']==0 and coverage['counts']['newDownloadsThisScope']==0
assert coverage['counts']['status']=={'inherited_rule_claim':4,'partial_active':5,'research_only':4,'not_established':27}
assert next(c for c in coverage['catalogue']if c['id']=='B02')['currentB02UnitMap']=='v53/research/liuyao-progress-conditions/B02_CURRENT_UNITS.json'
assert read(w/'PENDING_RESEARCH_STATE.json')['status']=='B02-progress-conditions-current-scope-active'
assert read(root/'qa/liuyao-b03-line-labels/RELEASE_RESULTS.json')['manifestFilesVerified']==2770
refs=[f for f in old['files']if f['file'].startswith('research/liuyao-')and f['file'].endswith('reference.mjs')];assert len(refs)==15
for token in[b'progression-reference.mjs',b'STAR_COORDINATES.json',b'liuyao-progress-conditions']:assert token not in html
out={'date':'2026-10-27','checks':14,**s,'newHTTPBodiesThisRun':0,'newOriginalPDFsToRelease':0,
 'noblemanGengWithinPageConflictPreserved':True,'missingFourLuRowsUnfilled':True,'bodyNumberingVariantPreserved':True,
 'chapter33LocalVolumeMapCorrected':True,'wholeBookApplied':False,'wholeCatalogueCompleted':False,'consumerChanged':False,
 'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'priorFifteenReferencesPreserved':True,
 'previousSourceZIPPreservedBytes':2002252441,'unchangedEarlierV53Files':unchanged,
 'manifestFilesVerified':len(manifest['files']),'sourceZIPFilesVerified':len(manifest['files'])+1}
if '--no-write'in sys.argv:assert read(qa/'RELEASE_RESULTS.json')==out
else:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
