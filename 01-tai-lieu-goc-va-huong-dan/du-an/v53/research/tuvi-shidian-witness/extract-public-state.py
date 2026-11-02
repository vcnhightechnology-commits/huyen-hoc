"""Parse public server-rendered data as JSON, never execute page JavaScript."""
from pathlib import Path
from html.parser import HTMLParser
from hashlib import sha256
import json
B=Path(__file__).resolve().parent
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.inscript=False;self.scripts=[];self.current=''
 def handle_starttag(self,tag,attrs):
  if tag=='script':self.inscript=True;self.current=''
 def handle_data(self,data):
  if self.inscript:self.current+=data
 def handle_endtag(self,tag):
  if tag=='script'and self.inscript:self.scripts.append(self.current);self.inscript=False
p=Parser();p.feed((B/'chapter-response.html').read_text(encoding='utf-8'))
s=next(s for s in p.scripts if s.startswith('window._ROUTER_DATA = '));data=json.JSONDecoder().raw_decode(s.split('=',1)[1].lstrip())[0]
(B/'public-router-data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('loader keys',list(data['loaderData']))
targets={'7330176536911314959','7330176501968797733','7330176554300981298'};hits=[];meta=[]
def walk(x,path='root'):
 if isinstance(x,dict):
  if any(str(x.get(k))in targets for k in ['pageId','startPageId','endPageId','id']):hits.append({'path':path,'data':x})
  if x.get('bookId')=='SDZJ0170'or any(k in x for k in ['baseBook','versionName','editionName','bookInfo','bookSource']):
   meta.append({'path':path,'scalars':{k:v for k,v in x.items()if not isinstance(v,(dict,list))}})
  for k,v in x.items():walk(v,path+'.'+k)
 elif isinstance(x,list):
  for i,v in enumerate(x):walk(v,f'{path}[{i}]')
walk(data)
(B/'TARGET_PUBLIC_RECORDS.json').write_text(json.dumps({'metadata':meta,'targetRecords':hits},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for r in meta:print('META',json.dumps(r,ensure_ascii=False)[:2200])
for r in hits:
 x=r['data'];print('HIT',r['path'],json.dumps(x,ensure_ascii=False)[:1900])
