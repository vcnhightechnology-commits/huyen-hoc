from pathlib import Path
from hashlib import sha256
from pypdf import PdfReader
from PIL import Image
import io,json
p=Path(__file__).resolve().parent;w=p.parent.parent
pdf=w/'v53/research/home-yangzhai-shishu/Tianyige-330000-1705-0007405-yangzhai-shishu.pdf'
r=PdfReader(pdf);digest=sha256(pdf.read_bytes()).hexdigest()
assert len(r.pages)==195 and digest=='b6394102a995bb66df173452b37614b29d58e34ff85e08c43077006572ac48a5'
records=[]
for pos in range(13,35):
 refs=r.pages[pos-1]['/Resources']['/XObject'];images=[v for v in refs.values() if v.get_object().get('/Subtype')=='/Image'];assert len(images)==1
 ref=images[0];o=ref.get_object();assert str(o.get('/Filter'))=='/DCTDecode';raw=o._data;f=p/f'raw-p{pos:03}.jpg';assert not f.exists();f.write_bytes(raw)
 records.append({'pdfPage':pos,'file':f.name,'bytes':len(raw),'sha256':sha256(raw).hexdigest(),'nativeSize':list(Image.open(io.BytesIO(raw)).size),'sourceImageID':ref.idnum,'filter':'/DCTDecode','sourceByteIdentityVerified':True,'actuallyViewed':False,'newSourceReadPosition':pos!=34,'alreadyReadBoundaryPosition':pos==34})
out={'date':'2026-10-28','sourcePDF':pdf.relative_to(w).as_posix(),'sourcePDFSHA256':digest,'containerPositions':195,'records':records,'newHTTPRequests':0,'newOriginalContainers':0,'newIndependentWitnesses':0,'allExtractedPositionsViewed':False}
(p/'RAW_IMAGES.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print('22 raw extracted;21 potential new source positions13–33;34 prior boundary')
