from pathlib import Path
from hashlib import sha256
from pypdf import PdfReader
from PIL import Image,ImageOps,ImageDraw
from io import BytesIO
import json,sys,subprocess
base=Path(__file__).resolve().parent.parent/'research/meihua'
out=base/'images';out.mkdir(exist_ok=True)
pdf=base/'NLC416-12jh005426-44577.pdf'
reader=PdfReader(pdf)
assert len(reader.pages)==232
pages=list(map(int,sys.argv[1].split(',')))
records=json.loads((base/'EXTRACTED_PAGES.json').read_text(encoding='utf8'))['pages'] if (base/'EXTRACTED_PAGES.json').exists() else []
sheet=Image.new('RGB',(1800,((len(pages)+4)//5)*400),'white');draw=ImageDraw.Draw(sheet)
for i,n in enumerate(pages):
    page=reader.pages[n-1]
    prefix=out/f'p{n:03}';file=f'images/p{n:03}.png'
    poppler=Path('C:/Users/Administrator.DESKTOP-98TGIBL/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe')
    subprocess.run([str(poppler),'-f',str(n),'-l',str(n),'-singlefile','-scale-to','2000','-png',str(pdf),str(prefix)],check=True,capture_output=True)
    data=(base/file).read_bytes();im=Image.open(BytesIO(data))
    xobjects=page['/Resources']['/XObject'].get_object()
    dimensions=[{'width':v.get_object().get('/Width'),'height':v.get_object().get('/Height'),'filter':str(v.get_object().get('/Filter'))} for v in xobjects.values() if v.get_object().get('/Subtype')=='/Image']
    record={'pdfPage':n,'file':file,'bytes':len(data),'sha256':sha256(data).hexdigest(),'size':list(im.size),'format':im.format,'textLayerCharacters':len(page.extract_text()),'embeddedImageMetadata':dimensions,'method':'Poppler pdftoppm single-page PNG render, scale-to2000; derivative, not original embedded-image bytes. Original PDF retained. No OCR.'}
    records=[r for r in records if r['pdfPage']!=n]+[record]
    thumb=ImageOps.contain(im.convert('RGB'),(350,370));x=(i%5)*360;y=(i//5)*400;sheet.paste(thumb,(x,y+25));draw.text((x+6,y+6),f'PDF p{n}',fill='black')
sheet.save(out/f'contact-{pages[0]}-{pages[-1]}.jpg',quality=90)
(base/'EXTRACTED_PAGES.json').write_text(json.dumps({'pdfPages':len(reader.pages),'pdfBytes':pdf.stat().st_size,'pdfSHA256':sha256(pdf.read_bytes()).hexdigest(),'pages':sorted(records,key=lambda r:r['pdfPage']),'policy':'Extraction/navigation does not establish manual reading or full-work collation.'},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'extractedRequested':len(pages),'retainedPages':len(records),'first':records[0]},ensure_ascii=False))
