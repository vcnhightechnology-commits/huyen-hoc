from pathlib import Path
from hashlib import sha256
from pypdf import PdfReader
from PIL import Image,ImageChops
import json
w=Path(__file__).resolve().parents[1];dest=w/'tmp/home-yangzhai-final-spans-staging';dest.mkdir(exist_ok=True)
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda p,o:p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
pdf=w/'v53/research/home-yangzhai-shishu/Tianyige-330000-1705-0007405-yangzhai-shishu.pdf'
assert sha256(pdf.read_bytes()).hexdigest()=='b6394102a995bb66df173452b37614b29d58e34ff85e08c43077006572ac48a5'
reader=PdfReader(pdf);assert len(reader.pages)==195
rawcount=0;unique=set();groups=0
for name,expected in [('exterior',22),('selection',45),('talismans',28)]:
 d=w/f'tmp/home-yangzhai-{name}-staging';meta=read(d/'RAW_IMAGES.json');assert len(meta['records'])==expected
 for record in meta['records']:
  page=record['pdfPage'];obj=reader.pages[page-1]['/Resources']['/XObject'];imgs=[ref for ref in obj.values()if ref.get_object().get('/Subtype')=='/Image'];assert len(imgs)==1
  ref=imgs[0];data=ref.get_object()._data;p=d/record['file']
  assert p.read_bytes()==data and len(data)==record['bytes']and sha256(data).hexdigest()==record['sha256']
  assert ref.idnum==record['sourceImageID']and list(Image.open(p).size)==record['nativeSize']
  assert record['actuallyViewed'];rawcount+=1;unique.add(page)
 notes=read(d/'CONTEXT_READINGS.json')['groups'];assert len(notes)==expected
 assert {x['sourcePDFPage']for x in notes}=={x['pdfPage']for x in meta['records']}
 groups+=len(notes)
s=w/'tmp/home-yangzhai-selection-staging';meta=read(s/'QA_IMAGES.json')
assert len(meta['crops'])==8
for record in meta['crops']:
 p=s/record['file'];im=Image.open(p).convert('RGB');src=Image.open(s/f"raw-p{record['sourcePDFPage']:03}.jpg").convert('RGB')
 assert list(im.size)==record['pixelSize']and sha256(p.read_bytes()).hexdigest()==record['sha256']
 assert ImageChops.difference(im,src.crop(record['cropBox'])).getbbox()is None
 record['actuallyViewed']=True
meta['allViewed']=True;write(s/'QA_IMAGES.json',meta)
prior=set(range(1,13))|set(range(34,95))|set(range(111,125))
assert len(prior)==87
# Last verified door/water scope added only95–110, with94/111 already included.
prior.update(range(95,111));assert len(prior)==103
new=unique-prior;assert len(new)==92 and prior|unique==set(range(1,196))
panel=read(w/'tmp/home-yangzhai-exterior-staging/PANEL_INVENTORY.json')
ref=read(s/'REFERENCE_RESULTS.json');assert len(ref['checks'])==8 and all(x['ok']for x in ref['checks'])
assert ref['actualLunarObjects']==144 and ref['literalSimingDifferencesRetained']==12
unit=read(w/'v53/research/home-yangzhai-door-water/UNIT_MAP.json')
for row in unit['records']:
 if row['id']=='P08-01':row.update(status='firstpass-span',actuallyViewedPositions=list(range(6,34)),rawDCTImagesViewed='13–33;6–12 previously read via retained native-sized derivatives')
 if row['id']=='P08-09':row.update(status='firstpass-span',actuallyViewedPositions=list(range(124,169)),rawDCTImagesViewed=True,closingSharedPosition=168)
 if row['id']=='P08-10':row.update(status='firstpass-span-historical-ritual-reserved',actuallyViewedPositions=list(range(168,196)),rawDCTImagesViewed=True,consumerImplementationDisposition='historical research; no ritual efficacy or medical/financial outcome validated')
unit.update(date='2026-10-28',fullFirstPassBodySpans=10,all195PositionsRead=True,wholeUnitsApplied=0,
 totalDistinctPositionsWithFirstPassRead=195,unreadContainerPositions=0,latestNewFirstPassPositions=92,
 priorMapPreserved='v53/research/home-yangzhai-door-water/UNIT_MAP.json',
 basis=unit['basis']+' New92distinctpositions13–33/125–195actuallyread;95rawartifactrecords/94uniqueimagepositionsbecause168shared. All10numberedbodyspansfirstpass;notallglyphs/conditionsapplied.',
 readingArtifactBoundary='Earlier40 first-pass positions used pypdf native-sized reencoded derivatives, explicitly preserved. Later155 new positions were first read from raw DCT streams; old boundary positions also revisited. This does not claim every original40 raw full image was viewed.')
write(dest/'UNIT_MAP.json',unit)
write(dest/'NATIVE_RESULTS.json',{'date':'2026-10-28','rawArtifactRecordsVerified':rawcount,'uniqueRawPositionsThisScope':len(unique),'manualContextRecords':groups,'newDistinctReadPositions':len(new),'earlierDistinctReadPositions':103,'totalDistinctReadPositions':195,'fullFirstPassBodySpans':10,'nativeCropsViewedPixelMatched':8,'runtimeCompleteChecks':8,'actualLunarObjects':144,'actualHourLabelQueries':132,'sourceHourLiteralDifferencesRetained':12,'newHTTPRequests':0,'newIndependentWitnesses':0,'allSourceRulesApplied':False,'consumerChanged':False})
print(json.dumps(read(dest/'NATIVE_RESULTS.json')))
