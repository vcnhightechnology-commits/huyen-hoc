from pathlib import Path
from hashlib import sha256,sha1
from PIL import Image
import json,sys
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/home-yangzhai-shishu';q=r/'qa/home-yangzhai-shishu'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
pdf=b/'Tianyige-330000-1705-0007405-yangzhai-shishu.pdf';assert pdf.stat().st_size==151275796 and sha(pdf)=='b6394102a995bb66df173452b37614b29d58e34ff85e08c43077006572ac48a5'
requests=read(b/'REQUESTS.json')['records'];assert len(requests)==4
for x in requests:
    p=b/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256']and x['status']==200 and x['tlsAuthorized']
info=next(iter(read(b/'commons-imageinfo.json')['query']['pages'].values()))['imageinfo'][0];assert info['size']==pdf.stat().st_size and sha1(pdf.read_bytes()).hexdigest()==info['sha1']=='8ea1b09c42f709746d990e2b7cb9242c3ba4e69d'
acq=read(b/'ACQUISITION.json');assert acq['commonsSizeAndSHA1Match']and not acq['allPagesRead']and not acq['independentTextualWitnessCompared']
native=read(b/'NATIVE_IMAGES.json');raw=read(b/'RAW_STREAMS.json');result=read(q/'NATIVE_RESULTS.json');failure=read(q/'NATIVE_FAILURE_AUDIT.json')
assert native['pdfPages']==195 and len(native['records'])==len(raw['records'])==len(result['records'])==40
expected=list(range(1,13))+list(range(81,95))+list(range(111,125));assert [x['pdfPage']for x in native['records']]==expected
assert raw['pypdfDerivativeByteDifferent']==raw['pypdfDerivativeRGBDifferent']==40 and failure['reencodedDerivativeCount']==40
for x,y,z in zip(native['records'],raw['records'],result['records']):
    a=b/x['file'];p=b/y['file'];assert a.stat().st_size==x['bytes']and sha(a)==x['sha256']and x['actuallyViewed']and x['sourceKind']=='native-sized-pypdf-image-derivative'and not x['savedDerivativeEqualsRawDCTStream']
    assert p.stat().st_size==y['bytes']and sha(p)==y['sha256']==z['rawSHA256']and y['rawStreamByteIdentityVerified']and not y['actuallyViewed']and not y['pypdfDerivativeByteIdentical']
    assert list(Image.open(a).size)==list(Image.open(p).size)==x['nativeSize']==y['nativeSize']
    assert z['rawSavedJPEGEqualsRawDCTStream']and z['derivativeJPEGReencodedByPypdf']and z['derivativeActuallyViewed']
assert not result['originalInstitutionPDFBytesClaimed']and not result['institutionItemCatalogIndependentlyValidated']and result['fullRawSourceImagesActuallyViewedNotClaimed']
cropcount=0
for name in ['CROPS.json','RAW_CROPS.json']:
    for x in read(q/name)['records']:
        src=b/x['sourceFile'];p=q/x['file'];assert sha(src)==x['sourceSHA256']and sha(p)==x['sha256']and x['actuallyViewed']and x['pixelIdentityVerified']
        a=Image.open(src).convert('RGB').crop(x['box']);im=Image.open(p).convert('RGB');assert a.size==im.size and a.tobytes()==im.tobytes();cropcount+=1
assert cropcount==8
units=read(b/'UNIT_MAP.json');assert units['numberedMainUnits']==10 and units['fullFirstPassBodySpans']==2 and units['wholeUnitsApplied']==0 and not units['all195PositionsRead']
assert {x['id']for x in units['records']if x['status']=='firstpass-span'}=={'P08-04','P08-08'}
assert next(x for x in units['records']if x['id']=='P08-08')['actuallyViewedPositions']==list(range(111,125))
contexts=read(b/'CONTEXT_READINGS.json');assert len(contexts['records'])==contexts['contextGroups']==46 and all(x['actuallyViewed']and not x['fullConditionSetEncoded']for x in contexts['records'])
assert next(x for x in contexts['records']if x['key']=='fire-an-definition')['workingAnchor']=='火唵即是廚房廚竈'
assert next(x for x in contexts['records']if x['key']=='five-element-cycle')['workingAnchor']=='頭層水二層木三層火四層土五層金'
layer=read(q/'LAYER_RESULTS.json');assert len(layer['checks'])==6 and all(x['ok']for x in layer['checks'])and layer['summary']['coordinateContexts']==50 and layer['summary']['boundaryContexts']==27 and layer['summary']['newEngineCalendarOrChartExecutions']==0
ids=read(b/'PROMOTION_IDENTITIES.json');assert len(ids['records'])==116
for x in ids['records']:
    p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256']
module=next(x for x in ids['records']if x['file']=='v53/research/home-yangzhai-shishu/layer-coordinate-reference.mjs');assert module['sha256']==sha(b/'layer-coordinate-reference.mjs')
staged=(b/'STAGED_test-layer-coordinate.mjs').read_text(encoding='utf-8');expectedTest=staged.replace("from'./layer-coordinate-reference.mjs'","from'../research/home-yangzhai-shishu/layer-coordinate-reference.mjs'").replace("new URL('LAYER_RESULTS.json',import.meta.url)","new URL('../qa/home-yangzhai-shishu/LAYER_RESULTS.json',import.meta.url)");assert expectedTest==(r/'scripts/test-home-yangzhai-layer-coordinate.mjs').read_text(encoding='utf-8')
out={'date':'2026-10-28','repositoryPDFBytes':151275796,'repositoryPDFSHA256':sha(pdf),'repositoryPDFSHA1AndSizeMatchAPI':True,'HTTP200TLSAndResponseHashesVerified':4,'sourceContainerPDFPositions':195,'nativeSizedPypdfDerivativePositionsActuallyViewed':40,'libraryReencodedJPEGsRetainedAndExplicitlyLabeled':40,'originalDCTStreamsRetainedAndIdentityChecked':40,'fullRaw40ImageViewsNotClaimed':True,'rawSourceCropsViewedAndPixelVerified':4,'derivativeCropsViewedAndPixelVerified':4,'recordedInitialRawIdentityCheckFailureAndCorrection':True,'originalPDFRewritten':False,'institutionItemCatalogIndependentlyValidated':False,'repositoryMetadataAttributionNotOriginalInstitutionBytes':True,'prefaceDateNotImprintDate':True,'printedTOCMainUnits':10,'fullFirstPassBodySpans':2,'manualContextGroups':46,'sourcePassingChecks':6,'privateCoordinateContexts':50,'privateBoundaryContexts':27,'newChartOrCalendarEngineExecutions':0,'engineComparisonNotApplicableForBoundedSourceCoordinateComponent':True,'promotionIdentityHashesVerified':116,'moduleByteIdenticalToStaging':True,'testBodyIdenticalExceptImportAndOutputPaths':True,'newHTTPRequests':4,'newRepositoryContainers':1,'newSourceReadPositions':40,'newIndependentWitnessTextComparisons':0,'all195PositionsRead':False,'allSourceConditionsApplied':False,'modernFloorOrRoomGeometryAdapter':False,'sourceOutcomesValidated':False,'consumerChanged':False,'wholeCatalogueCompleted':False}
if '--no-write'in sys.argv:assert read(q/'SOURCE_RESULTS.json')==out
else:(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
