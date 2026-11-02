from pathlib import Path
from hashlib import sha256
from pypdf import PdfReader
from PIL import Image
import json,io
s=Path(__file__).resolve().parent;pdf=s/'Tianyige-330000-1705-0007405-yangzhai-shishu.pdf';r=PdfReader(pdf)
assert len(r.pages)==195 and sha256(pdf.read_bytes()).hexdigest()=='b6394102a995bb66df173452b37614b29d58e34ff85e08c43077006572ac48a5'
out=[]
for pos in range(1,13):
    page=r.pages[pos-1];images=list(page.images);assert len(images)==1,(pos,len(images))
    image=images[0];native=image.data;im=Image.open(io.BytesIO(native));name=f'p{pos:03d}'+Path(image.name).suffix
    assert not(s/name).exists();(s/name).write_bytes(native)
    obj=image.indirect_reference.get_object()
    out.append({'pdfPage':pos,'file':name,'bytes':len(native),'sha256':sha256(native).hexdigest(),'nativeSize':list(im.size),'nativeImageID':image.indirect_reference.idnum,'pdfFilter':str(obj.get('/Filter')),'method':'pypdf page.images native embedded image extraction,no resize,OCR,sharpen or reconstructed glyphs','actuallyViewed':False})
d={'date':'2026-10-28','pdfPages':len(r.pages),'pdfBytes':pdf.stat().st_size,'pdfSHA256':sha256(pdf.read_bytes()).hexdigest(),'pypdfVersion':'6.10.0','pdfMetadata':{str(k):str(v)for k,v in r.metadata.items()},'records':out,'allPagesRead':False,'consumerChanged':False}
(s/'NATIVE_IMAGES.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'pdfPages':len(r.pages),'extractedNativePositions':12,'allUnreadUntilViewed':True}))
