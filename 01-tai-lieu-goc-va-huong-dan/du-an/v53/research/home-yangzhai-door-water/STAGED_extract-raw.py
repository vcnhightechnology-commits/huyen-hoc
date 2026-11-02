from pathlib import Path
from hashlib import sha256
from pypdf import PdfReader
from PIL import Image
import io,json
s=Path(__file__).resolve().parent;w=s.parent.parent;pdf=w/'v53/research/home-yangzhai-shishu/Tianyige-330000-1705-0007405-yangzhai-shishu.pdf';r=PdfReader(pdf)
assert len(r.pages)==195 and sha256(pdf.read_bytes()).hexdigest()=='b6394102a995bb66df173452b37614b29d58e34ff85e08c43077006572ac48a5';records=[]
for pos in range(94,112):
    page=r.pages[pos-1];refs=page['/Resources']['/XObject'];images=[v for v in refs.values()if v.get_object().get('/Subtype')=='/Image'];assert len(images)==1
    ref=images[0];obj=ref.get_object();assert str(obj.get('/Filter'))=='/DCTDecode';raw=obj._data;f=s/f'raw-p{pos:03d}.jpg';assert not f.exists();f.write_bytes(raw);im=Image.open(io.BytesIO(raw));assert f.read_bytes()==raw
    records.append({'pdfPage':pos,'file':f.name,'bytes':len(raw),'sha256':sha256(raw).hexdigest(),'nativeSize':list(im.size),'sourceImageID':ref.idnum,'filter':'/DCTDecode','sourceByteIdentityVerified':True,'pypdfPageImagesEncoderNotUsed':True,'actuallyViewed':False,'newSourceReadPosition':pos not in [94,111],'alreadyReadBoundaryPosition':pos in [94,111]})
out={'date':'2026-10-28','sourcePDF':pdf.relative_to(w).as_posix(),'sourcePDFSHA256':sha256(pdf.read_bytes()).hexdigest(),'containerPositions':195,'records':records,'newHTTPRequests':0,'newOriginalContainers':0,'newIndependentWitnesses':0,'allExtractedPositionsViewed':False}
(s/'RAW_IMAGES.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'rawImagesExtracted':18,'awaitingVisualRead':18,'newPotentialReadPositions':16,'oldBoundaries':[94,111],'imageEncoderUsed':False}))
