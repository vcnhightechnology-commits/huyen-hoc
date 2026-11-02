"""Read-only extraction of selected scan pages. Contacts are navigation aids, not collation."""
from pathlib import Path
from hashlib import sha256
from io import BytesIO
import json,sys
from pypdf import PdfReader
from PIL import Image,ImageOps,ImageDraw

base=Path(__file__).resolve().parent.parent/'research/bazi-late-zi-witness'
reader=PdfReader(base/'NCL-000002203.pdf')
assert len(reader.pages)==486
pages=list(map(int,sys.argv[1].split(',')))
out=base/'evidence';out.mkdir(exist_ok=True)
records=json.loads((base/'EXTRACTED_PAGES.json').read_text(encoding='utf8'))['pages'] if (base/'EXTRACTED_PAGES.json').exists() else []
for start in range(0,len(pages),12):
    batch=pages[start:start+12]
    sheet=Image.new('RGB',(1400,3*530),'white');draw=ImageDraw.Draw(sheet)
    for i,n in enumerate(batch):
        page=reader.pages[n-1];all_images=list(page.images);scans=[s for s in all_images if sha256(s.data).hexdigest()!='6d7e3af02fd89fad74210c74fc9ebea3d55f13cc13eaf036162b23663a381ed2'];assert len(scans)==1,(n,len(scans))
        scan=scans[0];im=Image.open(BytesIO(scan.data))
        suffix={'JPEG':'.jpg','JPEG2000':'.jp2','PNG':'.png'}[im.format]
        name=f'evidence/p{n:03}{suffix}';(base/name).write_bytes(scan.data)
        row={'pdfPage':n,'file':name,'imageName':scan.name,'format':im.format,'bytes':len(scan.data),'sha256':sha256(scan.data).hexdigest(),'size':im.size,'pdfTextLength':len(page.extract_text()),'otherImages':[{'name':s.name,'sha256':sha256(s.data).hexdigest(),'size':Image.open(BytesIO(s.data)).size} for s in all_images if s is not scan]}
        if im.format=='JPEG2000':
            visual=f'evidence/p{n:03}-view.png';im.save(base/visual)
            row['visualPNG']=visual;row['visualSHA256']=sha256((base/visual).read_bytes()).hexdigest()
        records=[r for r in records if r['pdfPage']!=n]+[row]
        thumb=ImageOps.contain(im.convert('RGB'),(340,490));x=(i%4)*350;y=(i//4)*530
        sheet.paste(thumb,(x,y+25));draw.text((x+6,y+5),f'PDF {n}',fill='black')
    sheet.save(out/f'contact-{batch[0]:03}-{batch[-1]:03}.jpg',quality=92)
(base/'EXTRACTED_PAGES.json').write_text(json.dumps({'method':'pypdf extraction of embedded JPEG/JP2 page scan; repeated JP2 overlay identified by exact SHA256 and omitted from scan raster; no OCR; contacts resized for navigation only','pdfPages':len(reader.pages),'pages':sorted(records,key=lambda r:r['pdfPage'])},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'pdfPages':len(reader.pages),'selectedPages':pages,'storedPages':len(records)}))
