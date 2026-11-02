from pathlib import Path
from hashlib import sha256
from pypdf import PdfReader
from PIL import Image
import json,io
s=Path(__file__).resolve().parent;pdf=s/'Tianyige-330000-1705-0007405-yangzhai-shishu.pdf';r=PdfReader(pdf)
m=json.loads((s/'NATIVE_IMAGES.json').read_text(encoding='utf-8'));known={x['pdfPage']:x for x in m['records']};selected=list(range(81,95))+list(range(111,125))
for pos in selected:
    page=r.pages[pos-1];images=list(page.images);assert len(images)==1
    image=images[0];native=image.data;im=Image.open(io.BytesIO(native));name=f'p{pos:03d}'+Path(image.name).suffix
    if pos in known:assert sha256((s/known[pos]['file']).read_bytes()).hexdigest()==known[pos]['sha256'];continue
    assert not(s/name).exists();(s/name).write_bytes(native)
    obj=image.indirect_reference.get_object()
    m['records'].append({'pdfPage':pos,'file':name,'bytes':len(native),'sha256':sha256(native).hexdigest(),'nativeSize':list(im.size),'nativeImageID':image.indirect_reference.idnum,'pdfFilter':str(obj.get('/Filter')),'method':'pypdf page.images native embedded image extraction,no resize,OCR,sharpen or reconstructed glyphs','actuallyViewed':False})
m['records'].sort(key=lambda x:x['pdfPage']);m['parserWarning']='startxref on same line as offset;parser continued,195pages/no repair or rewrite of PDF claimed'
(s/'NATIVE_IMAGES.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'nativeImagesTotal':len(m['records']),'newPositions':28,'actuallyViewedNotSetByExtractor':True}))
