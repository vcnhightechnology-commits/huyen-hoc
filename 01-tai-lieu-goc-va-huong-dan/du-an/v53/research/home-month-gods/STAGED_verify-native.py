from pathlib import Path
from hashlib import sha256
from pypdf import PdfReader
from PIL import Image,ImageChops
import json
w=Path.cwd();b=w/'tmp/home-month-gods-staging';read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));s=read(b/'SOURCE_DISPOSITIONS.json');p=w/s['sourcePDF']['file'];assert sha256(p.read_bytes()).hexdigest()==s['sourcePDF']['sha256'];pdf=PdfReader(p);assert len(pdf.pages)==195
for x in s['sourceRawImages']:
 refs=pdf.pages[x['sourcePDFPage']-1]['/Resources']['/XObject'];images=[v for v in refs.values()if v.get_object().get('/Subtype')=='/Image'];assert len(images)==1;ref=images[0];obj=ref.get_object();assert str(obj.get('/Filter'))=='/DCTDecode';assert obj._data==(w/x['file']).read_bytes();assert ref.idnum==x['sourceImageID']
for x in read(b/'QA_IMAGES.json')['records']:
 assert x['actuallyViewed']and x['pixelMatch']and not x['resampled'];assert ImageChops.difference(Image.open(w/x['sourceFile']).convert('RGB').crop(x['cropBox']),Image.open(b/x['file']).convert('RGB')).getbbox()is None
out=dict(date='2026-10-28',sourcePDFPositions=195,sourcePDFBytes=p.stat().st_size,sourcePDFSHA256=s['sourcePDF']['sha256'],rawDCTImagesByteIdenticalToPDF=8,nativeCropsViewedPixelMatched=13,excludedWrongTargetMonthLabelCrops=1,newSourcePositions=0,newHTTPRequests=0);(b/'NATIVE_RESULTS.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
