from pathlib import Path
import json,hashlib
import pypdfium2 as pdfium
from pypdf import PdfReader
from PIL import Image,ImageOps,ImageDraw
out=Path(__file__).resolve().parent.parent/'research/full-study/home/kua'
src=out/'nlc287543.pdf'
doc=pdfium.PdfDocument(str(src))
selected=list(range(11,32))
thumbs=[]
for ordinal in selected:
    page=doc[ordinal-1]
    full=out/f'nlc287543-page{ordinal:03d}-local.png'
    page.render(scale=3).to_pil().save(full)
    im=Image.open(full).convert('RGB')
    im.thumbnail((320,300))
    tile=Image.new('RGB',(330,330),'#ffffff')
    tile.paste(im,((330-im.width)//2,25))
    ImageDraw.Draw(tile).text((8,6),f'PDF page {ordinal}',fill='#000000')
    thumbs.append(tile)
cols=3;rows=(len(thumbs)+cols-1)//cols
sheet=Image.new('RGB',(cols*330,rows*330),'#dddddd')
for i,tile in enumerate(thumbs):sheet.paste(tile,((i%cols)*330,(i//cols)*330))
sheet.save(out/'nlc287543-contact11-31.png')
record={'schema':'hhc.home.kua.local-pdf-render.v1','sourceFile':src.name,'sourceSHA256':hashlib.sha256(src.read_bytes()).hexdigest(),'pdfPageCount':len(doc),'metadata':dict(PdfReader(src).metadata or {}),'renderedOrdinals':selected,'method':'pypdfium2 render scale3, savedPNG, contact sheetPIL solely to navigate scans; not image repair or textual verification','outputSHA256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in out.glob('*local.png')}}
(out/'LOCAL_RENDERS.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'pages':len(doc),'rendered':selected},ensure_ascii=False))
