from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,sys,tarfile
r=Path(__file__).resolve().parents[1];w=r.parent;b=r/'research/tuvi-lower-printed-cases';q=r/'qa/tuvi-lower-printed-cases';rd=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
ident=rd(b/'PROMOTION_IDENTITIES.json');assert len(ident['records'])==61
for x in ident['records']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'],x['file']
for name in ['run-printed-cases.mjs','test-printed-cases.mjs']:
 s=(b/('STAGED_'+name)).read_text(encoding='utf-8')
 for old,new in [("from'./printed-case-reference.mjs'","from'../research/tuvi-lower-printed-cases/printed-case-reference.mjs'"),("const b=resolve(import.meta.dirname),w=resolve(b,'../..'),","const b=resolve(import.meta.dirname,'../research/tuvi-lower-printed-cases'),w=resolve(b,'../../..'),")]:assert s.count(old)==1;s=s.replace(old,new)
 if name.startswith('test'):
  old="resolve(b,'REFERENCE_RESULTS.json')";assert s.count(old)==1;s=s.replace(old,"resolve(w,'v53/qa/tuvi-lower-printed-cases/REFERENCE_RESULTS.json')")
 assert s==(r/'scripts'/name.replace('printed-cases','tuvi-lower-printed-cases')).read_text(encoding='utf-8')
source=rd(b/'SOURCE_MANIFEST.json');assert source['newHTTP200Bodies']==16 and len(source['sourceMetadata'])==3 and len(source['imageBodies'])==13
for x in source['sourceMetadata']+source['imageBodies']:
 p=b/x['file'];assert x['status']==200 and x['TLSCertificateValidationEnabled']and x['headers'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'];req=rd(b/x['requestRecord']);req=req if isinstance(req,list)else[req];assert any(y['file']==x['file']and y['sha256']==x['sha256']and y['url']==x['url']for y in req)
chain=source['chainFromRetainedCatalogue'];assert sha(w/chain['file'])==chain['sha256'];assert chain['linkedItem']in(w/chain['file']).read_text(encoding='utf-8')
assert 'https://www.digital.archives.go.jp/img/4469314'in(b/'official-item-4469314.html').read_text(encoding='utf-8');assert 'https://www.digital.archives.go.jp/api/iiif/4469314/manifest.json'in(b/'official-viewer-4469314.html').read_text(encoding='utf-8')
manifest=rd(b/'official-manifest.json');assert sha(b/'official-manifest.json')=='3f167e1280527e1c672a72d7ef060c299ce9dffad1f362ddba04575da3df1560';can=manifest['sequences'][0]['canvases'];assert len(can)==137
for x in source['imageBodies']:
 resource=can[x['canvas']-1]['images'][0]['resource']['@id'];size=3000 if x['file'].endswith('-3000.jpg')else 2200;assert x['url']==resource.replace('/full/max/',f'/full/{size},/');assert list(Image.open(b/x['file']).size)==x['actualDimensions']==([3000,2262]if size==3000 else[2200,1659]);assert x['actuallyViewed']
assert len({x['canvas']for x in source['imageBodies']})==12 and source['newOriginalJP2Bodies']==source['newIndependentEditionCount']==0
reading=rd(b/'FIRST_PASS_READINGS.json');assert len(reading['records'])==12 and len(reading['positionsNotYetViewed'])==125 and all(x['actuallyViewed']for x in reading['records']);assert not reading['wholeItemRulesApplied'];volume=rd(b/'VOLUME_NUMBERING_AUDIT.json');assert volume['newDirectReadings'][-1]==dict(canvas=136,literal='卷之七終')and not volume['allSevenBodiesVerified']
crops=[]
for name in ['CHART_CROPS.json','DETAIL_CROPS.json','CORRECTION_CROPS.json']:
 for x in rd(b/name)['records']:
  assert x['actuallyViewed']and x['pixelMatch']and x['RGBPixelMatch']and not x['resampled'];assert sha(b/x['file'])==x['sha256'];assert ImageChops.difference(Image.open(b/x['sourceFile']).convert('RGB').crop(x['cropBox']),Image.open(b/x['file']).convert('RGB')).getbbox()is None;crops.append(x)
assert len(crops)==8 and sum(bool(x.get('excludedFromBirthDateEvidence'))for x in crops)==1
pixel=rd(b/'CROP_VERIFICATION_AUDIT.json');assert len(pixel['earlierRelatedCropsRechecked'])==7
for x in pixel['earlierRelatedCropsRechecked']:
 assert x['RGBPixelMatch']and sha(w/x['cropFile'])==x['cropSHA256']
 # Find the preserved native box in the earlier scope's ledger, then check RGB directly.
 base=(w/x['cropFile']).parent;ledger=rd(base/'QA_IMAGES.json');row=next(y for y in ledger['records']if y['file']==Path(x['cropFile']).name)
 assert ImageChops.difference(Image.open(w/x['sourceFile']).convert('RGB').crop(row['cropBox']),Image.open(w/x['cropFile']).convert('RGB')).getbbox()is None
a=Image.new('RGBA',(2,2),(0,0,0,255));z=a.copy();z.putpixel((0,0),(255,0,0,255));difference=ImageChops.difference(a,z);assert difference.getbbox()is None and difference.convert('RGB').getbbox()is not None
proof=rd(b/'RUNTIME_PROOF.json')
for x in proof['localFiles']+[proof['tarball']]:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256']
assert proof['tarball']['sha256']=='d44e96631c0506424c3aef25a7bba8e43e01729102d6a703720cbe224aec5403'and rd(w/'v46/node_modules/iztro/package.json')['version']=='2.6.2'
with tarfile.open(w/proof['tarball']['file'],'r:gz')as archive:
 for x in proof['localFiles'][1:]:assert archive.extractfile('package/'+x['file'].split('iztro/',1)[1]).read()==(w/x['file']).read_bytes()
freeze=rd(b/'TRANSCRIPTION_FREEZE.json');assert sha(b/freeze['file'])==freeze['sha256'];initial=rd(b/'INITIAL_TRANSCRIPTION_FREEZE.json');assert initial['actualHHCTuviCallsAtFreeze']==initial['actualIztroNatalCallsAtFreeze']==0 and sha(b/'INITIAL_MANUAL_PRINTED_CASES.json')==initial['sha256'];assert freeze['currentFileContainsOneDirectImageCorrectionAfterRuntime']
manual=rd(b/'MANUAL_PRINTED_CASES.json');before=rd(b/'INITIAL_MANUAL_PRINTED_CASES.json');assert before['records'][1]['majorBranches']['廉貞']=='子';before['records'][1]['majorBranches']['廉貞']='戌';assert before==manual
assert sum(v is not None for x in manual['records']for v in x['majorBranches'].values())==27 and manual['records'][0]['majorBranches']['天梁']is None
assert [x['sourceYearPillar']for x in manual['records']]==['己卯','癸卯']and[ x['modernTestYear']for x in manual['records']]==[1939,1963];assert not manual['modernYearsAreHistoricalBirthYears']
correction=rd(b/'READING_CORRECTIONS.json');assert correction['newChartCallsAfterCorrection']==0 and correction['sourceUnresolvedTianliangLeftRemainsNull'];assert sha(b/correction['initialRuntimeFile'])==correction['initialRuntimeSHA256'];assert (b/'INITIAL_ACTUAL_RUNTIME.json').read_bytes()==(b/'ACTUAL_RUNTIME.json').read_bytes()
actual=rd(b/'INITIAL_ACTUAL_RUNTIME.json');assert actual['actualHHCTuviCalls']==actual['actualIztroNatalCalls']==2 and actual['actualRuntimeBatchInvocations']==1;assert sum(len(x['hhcComparison']['mismatches'])for x in actual['records'])==sum(len(x['iztroComparison']['mismatches'])for x in actual['records'])==1
res=rd(q/'REFERENCE_RESULTS.json');assert len(res['checks'])==5 and all(x['ok']for x in res['checks']);assert res['currentInvocationNewHHCTuviCalls']==res['currentInvocationNewIztroCalls']==0 and res['reusesImmutableRuntime'];assert len(res['records'])==2
for row in manual['records']:
 old=next(x for x in actual['records']if x['caseID']==row['id']);new=next(x for x in res['records']if x['caseID']==row['id'])
 for which in ['hhc','iztro']:
  p=new[which+'Projection'];assert p==old[which+'Projection'];comparison=new[which+'Comparison'];assert not comparison['mismatches']and comparison['matches']==(18 if row['id']=='ma-zhou-left'else 20)
  expected={'ming':row['mingBranch'],'cuc':row['sourceCucNumber'],**{'major:'+k:v for k,v in row['majorBranches'].items()},**{'transform:'+x['kind']:x['branch']for x in row['transformationLabels']}}
  for x in comparison['coordinates']:assert x['source']==expected[x['id']];assert x['status']==('source-unresolved'if x['source']is None else'match')
  assert comparison['historicalBirthDateEstablished']==comparison['sourcePredictionValidated']==False and comparison['practicalOutcome']is None
 assert [new['hhcSolar'][k]for k in['y','m','d']]==list(map(int,new['iztroSolar'].split('-')))
assert res['matchedSourceCoordinateFieldsPerEngine']==38 and res['individualEngineSourceChecks']==76
state=rd(b/'WORK_STATE.json');assert not state['wholeCatalogueCompleted']and not state['consumerChanged']and not state['wholeSourceApplied']
out=dict(date='2026-10-28',promotionIdentities=61,newHTTP200Bodies=16,institutionalJPEGDerivativeBodies=13,newDistinctPositionsRead=12,manifestPositions=137,remainingUnreadPositions=125,newOriginalJP2Bodies=0,newIndependentEditions=0,nativeCropsRGBPixelMatched=8,excludedBirthEvidenceCrops=1,earlierRelatedCropsRGBRechecked=7,RGBTamperPositiveControl=True,iztroCoreFilesMatchedRetainedTarball=4,completeRuntimeChecks=5,actualHHCTuviCalls=2,actualIztroByLunarCalls=2,postCorrectionChartCalls=0,sourceFieldsPerEngine=38,individualEngineSourceChecks=76,unresolvedMajorCoordinates=1,manualCoordinateCorrections=1,historicalBirthDatesEstablished=False,sourceOutcomesValidated=False,consumerChanged=False,wholeCatalogueCompleted=False)
p=q/'SOURCE_RESULTS.json'
if '--no-write'in sys.argv:assert rd(p)==out
else:p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
