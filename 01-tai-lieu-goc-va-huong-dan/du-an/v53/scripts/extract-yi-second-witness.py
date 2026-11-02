"""Read-only source PDF extraction. Selected rasters retain embedded JPEG bytes.
Survey/contact sheets are navigation derivatives, not evidence of collation.
"""
from pathlib import Path
from hashlib import sha256
import json,sys
from pypdf import PdfReader
from PIL import Image,ImageOps,ImageDraw
from io import BytesIO
root=Path(__file__).resolve().parent.parent/'research/yi-second-witness'
reader=PdfReader(root/'NCL-00037.pdf')
assert len(reader.pages)==325
survey='--survey' in sys.argv
pages=list(range(1,326,10)) if survey else list(map(int,sys.argv[1].split(',')))
out=root/'evidence';out.mkdir(exist_ok=True)
records=[]
if (root/'EXTRACTED_PAGES.json').exists():records=json.loads((root/'EXTRACTED_PAGES.json').read_text(encoding='utf8'))['pages']
for batch in range(0,len(pages),15):
    selected=pages[batch:batch+15]
    sheet=Image.new('RGB',(2100,3*370),'white');draw=ImageDraw.Draw(sheet)
    for i,n in enumerate(selected):
        page=reader.pages[n-1];images=list(page.images);assert len(images)==1,(n,len(images))
        scan=images[0];im=Image.open(BytesIO(scan.data));assert im.format=='JPEG'
        thumb=ImageOps.contain(im.convert('RGB'),(410,335));x=(i%5)*420;y=(i//5)*370
        sheet.paste(thumb,(x,y+25));draw.text((x+8,y+5),f'NCL-00037; PDF p{n}',fill='black')
        if not survey:
            name=f'evidence/p{n:03}.jpg';(root/name).write_bytes(scan.data)
            rec={'pdfPage':n,'image':name,'sourceImageName':scan.name,'bytes':len(scan.data),'sha256':sha256(scan.data).hexdigest(),'size':im.size,'extractedTextLength':len(page.extract_text())}
            records=[r for r in records if r['pdfPage']!=n]+[rec]
    label=f'survey-{batch+1:03}' if survey else 'selected-'+str(selected[0])+'-'+str(selected[-1])
    sheet.save(out/(label+'.jpg'),quality=90)
if not survey:(root/'EXTRACTED_PAGES.json').write_text(json.dumps({'method':'Selected embedded JPEG bytes through pypdf page.images[0].data; no OCR; resized contacts for navigation only','pdfPages':325,'pages':sorted(records,key=lambda r:r['pdfPage'])},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'pdfPages':len(reader.pages),'selectedPages':pages,'surveyOnly':survey,'evidencePages':len(records)}))
