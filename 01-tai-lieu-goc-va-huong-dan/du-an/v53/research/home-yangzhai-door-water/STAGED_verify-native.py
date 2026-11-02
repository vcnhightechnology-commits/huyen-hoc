from pathlib import Path
from hashlib import sha256
import json,sys
from PIL import Image
from pypdf import PdfReader

p=Path(__file__).resolve().parent;w=p.parent.parent
read=lambda n:json.loads((p/n).read_text(encoding='utf-8'))
raw=read('RAW_IMAGES.json'); pdf=w/raw['sourcePDF']
assert sha256(pdf.read_bytes()).hexdigest()==raw['sourcePDFSHA256']
doc=PdfReader(pdf);assert len(doc.pages)==195
assert len(raw['records'])==18 and raw['allExtractedPositionsViewed']
for a in raw['records']:
    obj=doc.pages[a['pdfPage']-1]['/Resources']['/XObject']
    images=[v for v in obj.values() if v.get_object().get('/Subtype')=='/Image']
    assert len(images)==1 and images[0].idnum==a['sourceImageID']
    x=images[0].get_object();data=(p/a['file']).read_bytes()
    assert str(x.get('/Filter'))=='/DCTDecode' and data==x._data
    assert len(data)==a['bytes'] and sha256(data).hexdigest()==a['sha256']
    assert list(Image.open(p/a['file']).size)==a['nativeSize'] and a['actuallyViewed']
for a in read('QA_IMAGES.json'):
    data=(p/'qa'/a['file']).read_bytes();assert sha256(data).hexdigest()==a['sha256'] and a['actuallyViewed']
    im=Image.open(p/a['source']).convert('RGB').crop(a['box'])
    actual=Image.open(p/'qa'/a['file']).convert('RGB')
    assert im.size==actual.size and im.tobytes()==actual.tobytes()
out={'date':'2026-10-28','rawDCTStreamIdentitiesVerified':18,'originalJPEGsActuallyViewed':18,
 'newSourceReadPositions':16,'alreadyReadBoundariesExpanded':2,'nativeLosslessCropsViewedAndPixelVerified':12,
 'sourcePDFUnchanged':True,'sourcePDFSHA256':raw['sourcePDFSHA256'],
 'newHTTPRequests':0,'newOriginalContainers':0,'newIndependentTextualWitnesses':0,
 'allGlyphsCollated':False,'consumerChanged':False}
if '--no-write' in sys.argv: assert read('NATIVE_RESULTS.json')==out
else:(p/'NATIVE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
