from pathlib import Path
from html.parser import HTMLParser
import json
B=Path(__file__).resolve().parent
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.urls=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='script'and'src'in a:self.urls.append(a['src'])
p=Parser();p.feed((B/'chapter-response.html').read_text(encoding='utf-8'));rows=[]
for name in ['1746.0cd03317.js','7227.b637795c.js','5456.17c717b4.js','5796.f6337c0f.js']:
 url=next(x for x in p.urls if x.endswith('/'+name));url='https:'+url if url.startswith('//')else url
 rows.append({'url':url,'file':'client-'+name,'kind':'observed-public-reader-client;not-source-edition'})
(B/'IMAGE_CLIENT_REQUESTS.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
