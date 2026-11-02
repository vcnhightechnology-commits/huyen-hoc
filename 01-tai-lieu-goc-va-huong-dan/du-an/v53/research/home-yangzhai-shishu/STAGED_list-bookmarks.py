from pypdf import PdfReader
from pathlib import Path
import json
s=Path(__file__).resolve().parent;r=PdfReader(s/'Tianyige-330000-1705-0007405-yangzhai-shishu.pdf');rows=[]
def walk(items):
 for x in items:
  if isinstance(x,list):walk(x);continue
  n=r.get_destination_page_number(x);rows.append({'title':str(x.get('/Title')),'pdfPage':None if n is None or n<0 else n+1,'kind':'repositoryPDFbookmark-notprintedtext-proof','actuallyViewed':False})
walk(r.outline)
(s/'REPOSITORY_BOOKMARKS.json').write_text(json.dumps({'date':'2026-10-28','records':rows,'notManuallyVerifiedTOC':True},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([x for x in rows if any(a in x['title']for a in['分房','穿宫','内形','第二','第一','第三','第四','第五','第六','第七','第八','第九','第十'])],ensure_ascii=False))
