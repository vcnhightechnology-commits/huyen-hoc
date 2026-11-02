"""Extract the one embedded scan raster per PDF page, preserving image bytes.

No OCR and no reconstructed text. Contact sheets are navigation derivatives.
"""
from pathlib import Path
from hashlib import sha256
import json
from pypdf import PdfReader
from PIL import Image, ImageOps, ImageDraw

root=Path('v53/research/full-study/yi')
evidence=root/'evidence'
records=[]
for book,stem in [(1,'NCPSSD-71014695_周易四卷_第一册.pdf'),(2,'NCPSSD-71014696_周易四卷_第二册.pdf')]:
    target=evidence/f'book{book}-pages'
    target.mkdir(exist_ok=True)
    reader=PdfReader(evidence/stem)
    for n,page in enumerate(reader.pages,1):
        images=list(page.images)
        if len(images)!=1:
            raise ValueError((book,n,len(images)))
        scan=images[0]
        dest=target/f'p{n:03}.jpg'
        dest.write_bytes(scan.data)
        records.append({'book':book,'pdf':f'evidence/{stem}','pdfPage':n,'image':dest.relative_to(root).as_posix(),'bytes':len(scan.data),'sha256':sha256(scan.data).hexdigest(),'sourceImageName':scan.name,'extractedTextLength':len(page.extract_text())})
    # 12 pages per sheet, labels intentionally in ASCII.
    for start in range(1,len(reader.pages)+1,12):
        sheet=Image.new('RGB',(4*640,3*500),'white')
        draw=ImageDraw.Draw(sheet)
        for k,n in enumerate(range(start,min(start+12,len(reader.pages)+1))):
            im=Image.open(target/f'p{n:03}.jpg').convert('RGB')
            thumb=ImageOps.contain(im,(630,465))
            x=(k%4)*640;y=(k//4)*500
            sheet.paste(thumb,(x,y+30))
            draw.text((x+10,y+5),f'Book {book}; PDF page {n}',fill='black')
        sheet.save(evidence/f'book{book}-sheet-{start:03}.jpg',quality=90)
(root/'extracted-pages.json').write_text(json.dumps({'method':'pypdf page.images[0].data; no re-encoding of page JPEGs; contact sheets are resized derivatives','pages':records},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'pages':len(records),'pdfBooks':2,'allPagesHaveOneImage':True,'pagesWithExtractableText':sum(r['extractedTextLength']>0 for r in records)}))
