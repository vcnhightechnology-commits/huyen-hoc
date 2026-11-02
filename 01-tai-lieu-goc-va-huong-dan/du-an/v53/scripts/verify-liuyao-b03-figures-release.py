from pathlib import Path
from hashlib import sha256
import json,sys,zipfile
root=Path(__file__).resolve().parent.parent;workspace=root.parent;base=root/'research/liuyao-b03-figures';qa=root/'qa/liuyao-b03-figures';archive=workspace/'archives/v53-before-liuyao-b03-figures'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda b:sha256(b).hexdigest()
manifest=read(root/'PACKAGE_MANIFEST.json');old=read(archive/'PACKAGE_MANIFEST.json');html=(root/'Huyen_Hoc_Cac.html').read_bytes()
assert len(html)==707411 and sha(html)==manifest['product']['sha256']==old['product']['sha256']=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html==(workspace/'Huyen_Hoc_Cac.html').read_bytes()==(root/'site/index.html').read_bytes()==(archive/'Huyen_Hoc_Cac.html').read_bytes()
assert sorted(p.name for p in(root/'site').iterdir())==['index.html']
allowed={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'}
immutable=0
for f in old['files']:
 if f['file']not in allowed:assert sha((root/f['file']).read_bytes())==f['sha256'],f['file'];immutable+=1
assert(archive/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==984235159
web=workspace/'Huyen_Hoc_Cac_V53_web.zip';assert web.stat().st_size==344047 and web.read_bytes()==(archive/web.name).read_bytes()
with zipfile.ZipFile(web)as z:assert sorted(z.namelist())==['HUONG_DAN.md','index.html']and z.read('index.html')==html and z.read('HUONG_DAN.md')==(root/'README.md').read_bytes()
assert{p.relative_to(root).as_posix()for p in root.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json'}=={f['file']for f in manifest['files']}
for f in manifest['files']:
 b=(root/f['file']).read_bytes();assert len(b)==f['bytes']and sha(b)==f['sha256'],f['file']
with zipfile.ZipFile(workspace/'Huyen_Hoc_Cac_V53_source.zip')as z:
 assert set(z.namelist())=={'v53/'+f['file']for f in manifest['files']}|{'v53/PACKAGE_MANIFEST.json'}
 assert z.read('v53/PACKAGE_MANIFEST.json')==(root/'PACKAGE_MANIFEST.json').read_bytes()
 for f in manifest['files']:
  b=z.read('v53/'+f['file']);assert len(b)==f['bytes']and sha(b)==f['sha256'],f['file']
e=read(qa/'ENGINE_RESULTS.json');s=e['summary'];assert len(e['checks'])==9 and all(c['ok']for c in e['checks'])and e['htmlSHA256']==sha(html)
assert s=={'actualHHCHexCalls':79,'sourceFigureIdentities':64,'palaces':8,'additionalHiddenCases':13,'additionalHiddenPalaces':7,'printedChangedCase':1,'figureContentSpanPages':26,'all384LineAnnotationsCollated':False,'locatorDigest':'dad9db9b9d05ae47a91d0fadb0aa11fac06bfd09f7f79db945a654a3d951e193'}
manual=read(base/'MANUAL_READINGS.json');assert len(manual['records'])==27 and sum(r['newLocalRender']for r in manual['records'])==22
assert manual['counts']=={'manualImageRecords':27,'newLocalRenders':22,'expandedPriorRecords':5,'completeVolume2RelevantSpanPages':26,'newContentPages':21,'newEndleafPages':1}
assert manual['newOriginalPDFs']==manual['newHTTPResponses']==0 and not manual['wholePhysicalBookRead']
assert sha((base/manual['sourcePDF']).read_bytes())==manual['sourceSHA256']
for r in manual['records']:assert sha((base/r['image']).read_bytes())==r['sha256']
for r in[*manual['qaCrops'],manual['additionalGlyphQA']]:assert sha((base/r['file']).read_bytes())==r['sha256']
assert manual['additionalGlyphQA']['reading']=='火雷筮嗑'and manual['additionalGlyphQA']['renderDPI']==360
locator=read(base/'FIGURE_LOCATOR.json');assert len(locator['figures'])==64 and len({f['number']for f in locator['figures']})==64
assert locator['literalHeadingVariantNotes'][1]['reading']=='火雷筮嗑'
fixtures=read(base/'SOURCE_FIXTURES.json');assert len(fixtures['hiddenCases'])==13 and fixtures['changedAvailabilityCase']['values']==[6,8,7,7,7,7]
assert read(base/'AVAILABILITY_RULES.json')['calendarAvailabilityNotAdjudicated']
state=read(workspace/'EXHAUSTIVE_WORK_STATE.json');assert state==read(root/'research/EXHAUSTIVE_WORK_STATE.json')and state['status']=='active-not-complete'and state['currentWork']['latestResearchReport']=='v53/LIUYAO_B03_FIGURES_REPORT.md'
full=read(root/'research/full-study/WORK_STATE.json');assert full['overallStatus']=='active-not-complete'and full['latestResearchReport']=='LIUYAO_B03_FIGURES_REPORT.md'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
coverage=read(root/'research/library-current/COVERAGE.json');assert coverage['counts']['wholeWorkApplied']==0 and coverage['counts']['newDownloadsThisScope']==0 and coverage['counts']['status']=={'inherited_rule_claim':4,'partial_active':5,'research_only':4,'not_established':27}
work=read(base/'WORK_STATE.json');assert work['status']=='private-figure-locator-availability-complete-further-B03-active'and work['figureHeadings']==64 and work['qaCrops']==3 and not work['wholeBookApplied']and not work['all384LineAnnotationsCollated']
toc=read(root/'research/liuyao-void-motion/B02_CURRENT_UNITS.json');assert toc['currentCounts']['registeredUnits']==136 and toc['currentCounts']['headingOnlyBodyUnits']==103 and toc['currentCounts']['firstPassCompleteSpanUnits']==26
assert read(root/'qa/liuyao-b03-boundaries/RELEASE_RESULTS.json')['manifestFilesVerified']==2208
for token in[b'availability-reference',b'FIGURE_LOCATOR.json',b'AVAILABILITY_RULES.json']:assert token not in html
out={'date':'2026-10-27','checks':9,**s,'newOriginalPDFs':0,'newHTTPResponses':0,'newLocalRenders':22,'additionalQAPageRenders':1,'qaCrops':3,'expandedPriorRecords':5,'manualRecords':27,'newContentPages':21,'newEndleafPages':1,
 'heading21LiteralReading':'火雷筮嗑','heading21NormalizedFigure':21,'B02RegisteredUnitsUnchanged':136,'B02HeadingOnlyBodyUnitsUnchanged':103,'B02FirstPassSpanUnitsUnchanged':26,
 'calendarAvailabilityAdjudicated':False,'automaticUseGodSelection':False,'wholePhysicalBookRead':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False,
 'consumerChanged':False,'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'priorSixReferencesPreserved':True,
 'previousSourceZIPPreservedBytes':984235159,'unchangedEarlierV53Files':immutable,'manifestFilesVerified':len(manifest['files']),'sourceZIPFilesVerified':len(manifest['files'])+1}
if '--no-write'in sys.argv:assert read(qa/'RELEASE_RESULTS.json')==out
else:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
