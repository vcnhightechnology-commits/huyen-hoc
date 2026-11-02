from pathlib import Path
from hashlib import sha256,sha1
import json,sys,zipfile
root=Path(__file__).resolve().parent.parent;w=root.parent
base=root/'research/liuyao-b03-volume5';qa=root/'qa/liuyao-b03-volume5';archive=w/'archives/v53-before-liuyao-b03-volume5'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda b:sha256(b).hexdigest()
old=read(archive/'PACKAGE_MANIFEST.json');manifest=read(root/'PACKAGE_MANIFEST.json');html=(root/'Huyen_Hoc_Cac.html').read_bytes()
assert len(html)==707411 and sha(html)==old['product']['sha256']==manifest['product']['sha256']=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html==(w/'Huyen_Hoc_Cac.html').read_bytes()==(root/'site/index.html').read_bytes()==(archive/'Huyen_Hoc_Cac.html').read_bytes()
assert sorted(p.name for p in(root/'site').iterdir())==['index.html']
mutable={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'}
unchanged=0
for f in old['files']:
 if f['file']not in mutable:
  assert sha((root/f['file']).read_bytes())==f['sha256'],f['file'];unchanged+=1
assert len(old['files'])==2333 and (archive/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==1191709090
web=w/'Huyen_Hoc_Cac_V53_web.zip';assert web.stat().st_size==344047 and web.read_bytes()==(archive/web.name).read_bytes()
with zipfile.ZipFile(web)as z:
 assert sorted(z.namelist())==['HUONG_DAN.md','index.html']and z.read('index.html')==html and z.read('HUONG_DAN.md')==(root/'README.md').read_bytes()
assert {p.relative_to(root).as_posix()for p in root.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json'}=={f['file']for f in manifest['files']}
for f in manifest['files']:
 b=(root/f['file']).read_bytes();assert len(b)==f['bytes']and sha(b)==f['sha256'],f['file']
with zipfile.ZipFile(w/'Huyen_Hoc_Cac_V53_source.zip')as z:
 assert set(z.namelist())=={'v53/'+f['file']for f in manifest['files']}|{'v53/PACKAGE_MANIFEST.json'}
 assert z.read('v53/PACKAGE_MANIFEST.json')==(root/'PACKAGE_MANIFEST.json').read_bytes()
 for f in manifest['files']:
  b=z.read('v53/'+f['file']);assert len(b)==f['bytes']and sha(b)==f['sha256'],f['file']
e=read(qa/'ENGINE_RESULTS.json');s=e['summary']
assert len(e['checks'])==9 and all(c['ok']for c in e['checks'])and e['htmlSHA256']==sha(html)
assert s=={'actualHHCHexCalls':20,'syntheticSourceMethodCases':4,'privateCoordinateContexts':2880,'sexagenaryCoordinateCandidates':14400,
 'graphDigest':'48209d968b68ec30160f40a1fe81d0b8be98313a77f70b15d66803fd0e76fdee','sourceTimingMethods':4,
 'boundedOperationalClauses':14,'manualContentPages':24,'completeFirstPassSectionSpans':4,'partialSectionSpans':1}
a=read(base/'ACQUISITION.json');pdf=(base/a['file']).read_bytes();api=read(base/'b03-book3-commons-api.json');p=next(iter(api['query']['pages'].values()))
assert len(pdf)==a['bytes']==p['imageinfo'][0]['size']==56939817
assert sha(pdf)==a['sha256']=='01859340e519ffb68a1f40996af73aa7f40beb10a723a7a2a070985201874c61'
assert sha1(pdf).hexdigest()==a['sha1']==p['imageinfo'][0]['sha1']=='7535277adf0dd40b5269e43c5693fc74fad5f04e'
assert p['revisions'][0]['revid']==a['descriptionRevision']==1004714434
requests=read(base/'REQUESTS.json')['records'];assert len(requests)==2
for r in requests:
 b=(base/r['file']).read_bytes();assert r['status']==200 and r['tls']['authorized']and len(b)==r['bytes']and sha(b)==r['sha256']
assert read(base/'PDF_CONTAINER_CHECKS.json')=={'pages':67,'encrypted':False,'textLayerPages':0}
manual=read(base/'MANUAL_READINGS.json')
assert manual['counts']=={'manualRecords':24,'contentImagesNewToRelease':24,'inheritedPendingContentImages':7,'newContentRendersThisHeartbeat':17,'QAOnlyRenders':1,'newOriginalPDFsToRelease':1,'retainedHTTPBodiesNewToRelease':2,'newHTTPBodiesThisHeartbeat':0}
assert [r['pdfPage']for r in manual['records']]==list(range(2,26))
for r in manual['records']+manual['QAOnlyImages']:assert sha((base/r['image']).read_bytes())==r['sha256']
assert manual['unviewedPhysicalBookPages']==[1]+list(range(26,68))and not manual['allVolume5ClausesApplied']
units=read(base/'VOLUME5_UNITS.json');assert units['firstPassCompleteRelevantSpanUnits']==4 and units['partialSpanUnits']==1 and not units['fullTextualVolumeRead']
timing=read(base/'TIMING_CLAUSES.json');assert len(timing['methods'])==4 and not timing['allTimingPremisesCompiled']and not timing['meteorologicalPredictionAccuracyEstablished']
assert len(read(base/'OPERATIONAL_CLAUSES.json')['clauses'])==14
state=read(w/'EXHAUSTIVE_WORK_STATE.json');assert state==read(root/'research/EXHAUSTIVE_WORK_STATE.json')and state['status']=='active-not-complete'
assert state['currentWork']['latestResearchReport']=='v53/LIUYAO_B03_VOLUME5_REPORT.md'and state['currentWork']['nextSourceLead']['status']=='downloaded-byte-verified-partial-volume5-read'
full=read(root/'research/full-study/WORK_STATE.json');assert full['overallStatus']=='active-not-complete'and full['latestResearchReport']=='LIUYAO_B03_VOLUME5_REPORT.md'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
coverage=read(root/'research/library-current/COVERAGE.json');assert coverage['counts']['wholeWorkApplied']==0 and coverage['counts']['newDownloadsThisScope']==2
assert coverage['counts']['status']=={'inherited_rule_claim':4,'partial_active':5,'research_only':4,'not_established':27}
assert len(next(c for c in coverage['catalogue']if c['id']=='B03')['localPossession'])==3
assert read(w/'PENDING_RESEARCH_STATE.json')['status']=='promoted-into-current-research-scope'
work=read(base/'WORK_STATE.json');assert not work['wholeBookApplied']and not work['wholeCatalogueCompleted']and work['unviewedPages']==[1]+list(range(26,68))
toc=read(root/'research/liuyao-void-motion/B02_CURRENT_UNITS.json')['currentCounts'];assert(toc['registeredUnits'],toc['headingOnlyBodyUnits'],toc['firstPassCompleteSpanUnits'])==(136,103,26)
assert read(root/'qa/liuyao-b03-volume4/RELEASE_RESULTS.json')['manifestFilesVerified']==2333
for token in[b'timing-reference.mjs',b'TIMING_CLAUSES.json',b'B03-book3']:assert token not in html
out={'date':'2026-10-27','checks':9,**s,'newOriginalPDFsToRelease':1,'retainedHTTPBodiesNewToRelease':2,'newHTTPBodiesThisHeartbeat':0,
 'newPDFBytes':len(pdf),'newPDFSHA256':a['sha256'],'newPDFPages':67,'contentImagesNewToRelease':24,
 'inheritedPendingContentImages':7,'newContentRendersThisHeartbeat':17,'QAOnlyRenders':1,
 'wholeBookApplied':False,'wholeCatalogueCompleted':False,'fullTimingAdjudicator':False,'meteorologicalAccuracyValidated':False,
 'consumerChanged':False,'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'priorNineReferencesPreserved':True,
 'previousSourceZIPPreservedBytes':1191709090,'unchangedEarlierV53Files':unchanged,
 'manifestFilesVerified':len(manifest['files']),'sourceZIPFilesVerified':len(manifest['files'])+1}
if '--no-write'in sys.argv:assert read(qa/'RELEASE_RESULTS.json')==out
else:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
