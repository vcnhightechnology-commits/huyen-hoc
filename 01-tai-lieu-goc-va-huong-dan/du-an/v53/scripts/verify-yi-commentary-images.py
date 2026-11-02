from pathlib import Path
from hashlib import sha256
from pypdf import PdfReader
from PIL import Image
from io import BytesIO
import json

root = Path(__file__).resolve().parent.parent
base = root / 'research/yi-commentary-context'
qa = root / 'qa/yi-commentary-context'
qa.mkdir(parents=True, exist_ok=True)
manual = json.loads((base/'MANUAL_READINGS.json').read_text(encoding='utf8'))
source = base / manual['sourcePDF']
assert source.stat().st_size == 95666503
assert sha256(source.read_bytes()).hexdigest() == manual['sourceSHA256']
reader = PdfReader(source)
assert len(reader.pages) == 325
old = json.loads((root/'research/yi-second-witness/EXTRACTED_PAGES.json').read_text(encoding='utf8'))
pages = sorted({n for r in manual['readings'] for n in r['pdfPages']})
records = []
for n in pages:
    page = reader.pages[n-1]
    images = list(page.images)
    assert len(images) == 1
    data = images[0].data
    rel = 'evidence/p248.jpg' if n == 248 else f'../yi-second-witness/evidence/p{n:03}.jpg'
    saved = (base/rel).read_bytes()
    assert saved == data
    im = Image.open(BytesIO(data))
    assert im.format == 'JPEG' and im.size == (1713, 1240)
    assert len(page.extract_text()) == 0
    if n != 248:
        prior = next(p for p in old['pages'] if p['pdfPage'] == n)
        assert prior['sha256'] == sha256(data).hexdigest() and prior['bytes'] == len(data)
    records.append({'pdfPage':n,'file':rel,'bytes':len(data),'sha256':sha256(data).hexdigest(),'size':list(im.size),'method':'Exact pypdf embedded JPEG extraction checked against saved bytes; no OCR','newExtraction':n==248})
result = {'sourcePDF':manual['sourcePDF'],'sourceBytes':source.stat().st_size,'sourceSHA256':manual['sourceSHA256'],'pdfPages':len(reader.pages),'actualRasterSize':[1713,1240],'httpRequests':0,'targetImages':8,'newExtraction':1,'manualReadingUnits':7,'pages':records}
(base/'IMAGE_AUDIT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
(qa/'IMAGE_RESULTS.json').write_text(json.dumps({'exactJPEGsVerified':8,'newExtraction':1,'sourcePDFSHA256':manual['sourceSHA256'],'imageAuditSHA256':sha256((base/'IMAGE_AUDIT.json').read_bytes()).hexdigest(),'textExtractionCharacters':0,'ocrUsed':False},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k!='pages'},ensure_ascii=False))
