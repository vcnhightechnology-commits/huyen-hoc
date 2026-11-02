from pathlib import Path
from html.parser import HTMLParser
import json
B=Path(__file__).resolve().parent
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.urls=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='script'and'src'in a:self.urls.append(a['src'])
p=Parser();p.feed((B/'chapter-response.html').read_text(encoding='utf-8'))
url=next(x for x in p.urls if'/book/$.4e315211.js'in x)
if url.startswith('//'):url='https:'+url
(B/'TARGETED_REQUESTS.json').write_text(json.dumps([{'url':url,'file':'public-book-reader.js','kind':'observed-public-reader-client;not-source-edition'}],ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'observedPublicClientURL':url}))
