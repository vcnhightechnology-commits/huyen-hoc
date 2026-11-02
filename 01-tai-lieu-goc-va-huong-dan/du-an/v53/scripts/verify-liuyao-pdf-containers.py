"""Read original PDF containers only; does not author or modify any PDF."""
from pathlib import Path
from hashlib import sha256
import json
from pypdf import PdfReader
from PIL import Image
root=Path(__file__).resolve().parent.parent;base=root/'research/liuyao-foundations';qa=root/'qa/liuyao-foundations'
audit=json.loads((base/'SOURCE_AUDIT.json').read_text(encoding='utf-8'))
out=[]
for s in audit['sources']:
 p=base/s['file'];assert sha256(p.read_bytes()).hexdigest()==s['sha256'];pdf=PdfReader(p)
 assert len(pdf.pages)==s['pdfPages'];pages=[]
 for n in ([3,21,44,46,47,394]if s['prefix']=='zengshan'else[2,20,21,22]):
  page=pdf.pages[n-1];image=base/f"images/{s['prefix']}-{n}.png";dpi=230 if s['prefix']=='zengshan' else 180
  with Image.open(image)as im:
   width,height=im.size
   assert abs(width-float(page.mediabox.width)*dpi/72)<2 and abs(height-float(page.mediabox.height)*dpi/72)<2
  pages.append({'pdfPage':n,'mediaBox':[float(x)for x in page.mediabox],
   'textLayerCharacters':len(page.extract_text()or''),'renderDPI':dpi,'renderPixels':[width,height],
   'renderSHA256':sha256(image.read_bytes()).hexdigest()})
 out.append({'file':s['file'],'sha256':s['sha256'],'pdfPages':len(pdf.pages),'inspectedPageContainers':pages})
(qa/'PDF_CONTAINER_CHECKS.json').write_text(json.dumps({'date':'2026-10-27','sources':out,'pdfAuthoring':False,'ocrUsed':False,'scope':'Page counts and selected render dimensions/container identity;not all pages read or rendered anew.'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'originalPDFs':len(out),'pdfPages':[x['pdfPages']for x in out],'pageContainersChecked':sum(len(x['inspectedPageContainers'])for x in out),'pdfAuthoring':False}))
