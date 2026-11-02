from pathlib import Path
from hashlib import sha256
from pypdf import PdfReader
from PIL import Image
import json
s=Path(__file__).resolve().parent;read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda b:sha256(b).hexdigest()
m=read(s/'NATIVE_IMAGES.json');pdf=s/'Tianyige-330000-1705-0007405-yangzhai-shishu.pdf';assert sha(pdf.read_bytes())==m['pdfSHA256'];r=PdfReader(pdf);assert len(r.pages)==195
records=[]
for x in m['records']:
    image=list(r.pages[x['pdfPage']-1].images)[0];obj=image.indirect_reference.get_object();raw=obj._data;data=(s/x['file']).read_bytes()
    assert str(obj.get('/Filter'))=='/DCTDecode'and image.data==data and len(data)==x['bytes']and sha(data)==x['sha256']and x['actuallyViewed']
    im=Image.open(s/x['file']);assert list(im.size)==x['nativeSize']
    rawfile=s/f"raw-p{x['pdfPage']:03d}.jpg";assert rawfile.read_bytes()==raw
    records.append({'pdfPage':x['pdfPage'],'sourceImageID':x['nativeImageID'],'rawFile':rawfile.name,'rawBytes':len(raw),'rawSHA256':sha(raw),'rawSavedJPEGEqualsRawDCTStream':True,'rawStreamFullImageViewedNotClaimed':True,'derivativeJPEGReencodedByPypdf':raw!=data,'derivativeActuallyViewed':True})
crops=read(s/'CROPS.json')
for x in crops['records']:
    source=s/x['sourceFile'];p=s/x['file'];assert sha(source.read_bytes())==x['sourceSHA256']and sha(p.read_bytes())==x['sha256']
    a=Image.open(source).convert('RGB').crop(x['box']);b=Image.open(p).convert('RGB');assert a.size==b.size and a.tobytes()==b.tobytes();x.update(actuallyViewed=True,pixelIdentityVerified=True)
(s/'CROPS.json').write_text(json.dumps(crops,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
rawcrops=read(s/'RAW_CROPS.json')
for x in rawcrops['records']:
    source=s/x['sourceFile'];p=s/x['file'];assert sha(source.read_bytes())==x['sourceSHA256']and sha(p.read_bytes())==x['sha256']
    a=Image.open(source).convert('RGB').crop(x['box']);im=Image.open(p).convert('RGB');assert a.size==im.size and a.tobytes()==im.tobytes();x.update(actuallyViewed=True,pixelIdentityVerified=True)
(s/'RAW_CROPS.json').write_text(json.dumps(rawcrops,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
reqs=read(s/'REQUESTS.json')['records'];assert len(reqs)==4
for x in reqs:assert x['status']==200 and x['tlsAuthorized']and sha((s/x['file']).read_bytes())==x['sha256']and(s/x['file']).stat().st_size==x['bytes']
api=read(s/'commons-imageinfo.json');info=next(iter(api['query']['pages'].values()))['imageinfo'][0]
assert info['size']==pdf.stat().st_size and sha256(pdf.read_bytes()).hexdigest()==m['pdfSHA256']
from hashlib import sha1
assert sha1(pdf.read_bytes()).hexdigest()==info['sha1']
out={'date':'2026-10-28','retainedRequestsHTTP200TLSAndSHA256Verified':4,'repositoryPDFBytes':pdf.stat().st_size,'repositoryPDFSHA256':m['pdfSHA256'],'repositoryPDFSHA1AndSizeMatchAPI':True,'PDFPages':195,'PDFNotRewritten':True,'rawDCTStreamIdentitiesVerified':len(records),'nativeSizedReencodedDerivativesActuallyViewed':40,'rawSourceCropsViewedAndPixelVerified':4,'derivativeSourceCropsViewedAndPixelVerified':4,'fullRawSourceImagesActuallyViewedNotClaimed':True,'pypdfParserWarningRetained':'startxref on same line as offset;parser continued,no repairedPDF authored','records':records,'originalInstitutionPDFBytesClaimed':False,'institutionItemCatalogIndependentlyValidated':False,'allImageGlyphsCollated':False,'sourceOutcomesValidated':False,'consumerChanged':False,'wholeCatalogueCompleted':False}
(s/'NATIVE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
d=read(s/'UNIT_MAP.json');next(x for x in d['records']if x['id']=='P08-08')['actuallyViewedPositions']=list(range(111,125));write=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');write(s/'UNIT_MAP.json',d)
d=read(s/'WORK_STATE.json');d.pop('actualNativePositionsViewed',None);d.update(status='40native-sized-derivatives-firstpass-twochapterspans-fourrawsourcecrops-and-selectedlayercomponent6checks-verified',nativeSizedDerivativesViewed=40,derivativeJPEGsReencodedByPypdf=40,rawSourceCropsViewedAndPixelVerified=4,derivativeCropsViewedAndPixelVerified=4,rawDCTStreamIdentitiesVerified=40,manualContextGroups=46,passingChecks=6,privateLayerCoordinateContexts=50,boundaryContexts=27,sourceLayerModule='layer-coordinate-reference.mjs',newChartEngineExecutions=0);d['next']=['Promote40native-sizedreadingswithrawJPEGidentityand4rawcrops/46groups/2chapterspans/selectedlayercomponentafter3948snapshot.','Remaining155PDFpositionsand8mainunitsneedreading;chapters4/8allglyphs/subsidiaryclausesnotexhausted.','12printedlayerdiagrams82–93requireexactcoordinatecollation,height/door/houseorientationpremises;notselectrowsbyentrancetrigramalone.','FirstElementandcountedoriginrequiresseparateestablishment,bothwall/doorresetandneitherwall/doormaincaseonly;modernverticalfloorsnotassumedordered進.','Kitchen/stove火唵definition/criticizedinterpretationskeptwithsourcevoice;do notapplycategoricalhealth/wealth/lifespanorstructuralengineeringoutcomes.'];write(s/'WORK_STATE.json',d)
print(json.dumps({k:v for k,v in out.items()if k!='records'},ensure_ascii=False))
