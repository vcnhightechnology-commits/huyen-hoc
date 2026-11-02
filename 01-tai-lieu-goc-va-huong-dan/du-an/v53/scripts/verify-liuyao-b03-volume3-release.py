from pathlib import Path
from hashlib import sha256
import json,sys,zipfile
root=Path(__file__).resolve().parent.parent;workspace=root.parent;base=root/'research/liuyao-b03-volume3';qa=root/'qa/liuyao-b03-volume3';archive=workspace/'archives/v53-before-liuyao-b03-volume3'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda b:sha256(b).hexdigest()
manifest=read(root/'PACKAGE_MANIFEST.json');old=read(archive/'PACKAGE_MANIFEST.json');html=(root/'Huyen_Hoc_Cac.html').read_bytes()
assert len(html)==707411 and sha(html)==manifest['product']['sha256']==old['product']['sha256']=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html==(workspace/'Huyen_Hoc_Cac.html').read_bytes()==(root/'site/index.html').read_bytes()==(archive/'Huyen_Hoc_Cac.html').read_bytes()
assert sorted(p.name for p in(root/'site').iterdir())==['index.html']
allowed={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'}
immutable=0
for f in old['files']:
 if f['file']not in allowed:assert sha((root/f['file']).read_bytes())==f['sha256'],f['file'];immutable+=1
assert(archive/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==1030931341
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
e=read(qa/'ENGINE_RESULTS.json');s=e['summary'];assert len(e['checks'])==11 and all(c['ok']for c in e['checks'])and e['htmlSHA256']==sha(html)
assert s=={'actualHHCHexCalls':24,'printedNamedFigurePairs':12,'privateChartPairs':4096,'privateMovingAnnotations':12288,'directionalFanYinPairs':960,'branchFanYinPairs':252,'fuYinPairs':252,'directionalVsBranchPresenceDisagreements':1148,'advanceAnnotations':512,'retreatAnnotations':512,'movementCoordinateComparisons':144,'operationalClauses':27,'firstPassDiscussionUnits':18,'graphDigest':'dcc0482f674726bb230d6f4f88735da3310054122154e322475a75516b470a9f'}
manual=read(base/'MANUAL_READINGS.json');assert len(manual['records'])==32 and all(r['newLocalRender']for r in manual['records'])
assert manual['counts']=={'manualRecords':32,'newLocalRenders':32,'newEighteenDiscussionContentPages':12,'volume3PolemicPages':16,'coverPages':1,'boundedNextVolumePages':3,'completeVolume3RelevantSpanPages':28}
for r in manual['records']:assert sha((base/r['image']).read_bytes())==r['sha256']
a=read(base/'ACQUISITION.json');pdf=(base/a['file']).read_bytes();assert len(pdf)==a['bytes']==41224832 and sha(pdf)==a['sha256']==manual['sourceSHA256']=='c1e1027331d43769733c6011b4fe99e90928e9fde013fce563c8e9bad81c04bf'
assert sha256((base/'b03-book2-commons-api.json').read_bytes()).hexdigest()=='60b05916181d083a5704fb17bbc6e51d43e791153f0a8d6879faf7a29f22b1b1'
api=read(base/'b03-book2-commons-api.json');page=next(iter(api['query']['pages'].values()));assert page['revisions'][0]['revid']==a['descriptionRevision']==754088942 and page['imageinfo'][0]['size']==len(pdf)
assert page['imageinfo'][0]['sha1']==a['sha1']=='fb4f1aca26238121204b48bd0bff55f480f526cb'
requests=read(base/'REQUESTS.json')['records'];assert len(requests)==2
for r in requests:
 b=(base/r['file']).read_bytes();assert len(b)==r['bytes']and sha(b)==r['sha256']and r['status']==200 and r['tls']['authorized']
container=read(base/'PDF_CONTAINER_CHECKS.json');assert container['pages']==49 and container['textLayerPages']==0 and not container['encrypted']
units=read(base/'VOLUME3_UNITS.json');assert len(units['units'])==18 and len(units['polemicUnits'])==14 and units['volume3RelevantSpanFirstPassRead']and not units['allVolume3ClausesApplied']and not units['entirePhysicalBookRead']
audit=read(base/'SOURCE_AUDIT.json');assert audit['unreadPages']==list(range(33,50))and not audit['wholeBookApplied']
assert len(read(base/'OPERATIONAL_CLAUSES.json')['clauses'])==27
state=read(workspace/'EXHAUSTIVE_WORK_STATE.json');assert state==read(root/'research/EXHAUSTIVE_WORK_STATE.json')and state['status']=='active-not-complete'and state['currentWork']['latestResearchReport']=='v53/LIUYAO_B03_VOLUME3_REPORT.md'
assert state['currentWork']['nextSourceLead']['status']=='downloaded-byte-verified-opening-read'
full=read(root/'research/full-study/WORK_STATE.json');assert full['overallStatus']=='active-not-complete'and full['latestResearchReport']=='LIUYAO_B03_VOLUME3_REPORT.md'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
coverage=read(root/'research/library-current/COVERAGE.json');assert coverage['counts']['wholeWorkApplied']==0 and coverage['counts']['newDownloadsThisScope']==2 and coverage['counts']['status']=={'inherited_rule_claim':4,'partial_active':5,'research_only':4,'not_established':27}
assert len(next(c for c in coverage['catalogue']if c['id']=='B03')['localPossession'])==2
work=read(base/'WORK_STATE.json');assert work['status']=='private-three-layer-reference-complete-volume4-and-adjudication-active'and not work['wholeBookApplied']and work['firstPassPolemicUnits']==14
toc=read(root/'research/liuyao-void-motion/B02_CURRENT_UNITS.json');assert toc['currentCounts']['registeredUnits']==136 and toc['currentCounts']['headingOnlyBodyUnits']==103 and toc['currentCounts']['firstPassCompleteSpanUnits']==26
assert read(root/'qa/liuyao-b03-figures/RELEASE_RESULTS.json')['manifestFilesVerified']==2247
for token in[b'layer-reference.mjs',b'LAYER_TABLES.json',b'VOLUME3_UNITS.json']:assert token not in html
out={'date':'2026-10-27','checks':11,**s,'newOriginalPDFs':1,'newRetainedHTTP200Bodies':2,'newPDFBytes':41224832,'newPDFSHA256':a['sha256'],'newPDFPages':49,
 'newLocalRenders':32,'manualRecords':32,'volume3FirstPassPolemicUnits':14,'completeVolume3ContentSpanPages':28,'boundedVolume4Pages':3,'coverPages':1,
 'B02RegisteredUnitsUnchanged':136,'B02HeadingOnlyBodyUnitsUnchanged':103,'B02FirstPassSpanUnitsUnchanged':26,
 'calendarAdapter':False,'overallStrengthModel':False,'automaticUseGodSelection':False,'sourcePolemicIsValidatedConsensus':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False,
 'consumerChanged':False,'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'priorSevenReferencesPreserved':True,
 'previousSourceZIPPreservedBytes':1030931341,'unchangedEarlierV53Files':immutable,'manifestFilesVerified':len(manifest['files']),'sourceZIPFilesVerified':len(manifest['files'])+1}
if '--no-write'in sys.argv:assert read(qa/'RELEASE_RESULTS.json')==out
else:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
