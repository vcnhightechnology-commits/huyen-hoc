from pathlib import Path
from html.parser import HTMLParser
from hashlib import sha256
import json,re
class Tables(HTMLParser):
 def __init__(self):super().__init__();self.tables=[];self.stack=[]
 def handle_starttag(self,t,a):
  if t=='table':self.stack.append({'rows':[],'row':None,'cell':None})
  if t=='tr'and self.stack:self.stack[-1]['row']=[]
  if t in ['td','th']and self.stack:self.stack[-1]['cell']=''
 def handle_data(self,d):
  if self.stack and self.stack[-1]['cell']is not None:self.stack[-1]['cell']+=d
 def handle_endtag(self,t):
  if not self.stack:return
  x=self.stack[-1]
  if t in ['td','th']and x['cell']is not None:
   if x['row']is not None:x['row'].append(' '.join(x['cell'].split()))
   x['cell']=None
  if t=='tr'and x['row']is not None:x['rows'].append(x['row']);x['row']=None
  if t=='table':self.tables.append(self.stack.pop())
b=Path.cwd()/'tmp/home-month-witness-staging';out=[];titles=['天道','天德','月德','天德合','月德合','月空','月財']
for name in ['itkc-month-directions-0110.html','xuanze-yaolue-upper.html']:
 p=Tables();p.feed((b/name).read_text(encoding='utf-8'));found=[t for t in p.tables if any(r and r[0].startswith('天道')for r in t['rows'])and any(r and r[0]=='月財'for r in t['rows'])];assert len(found)==1;rows=[]
 for row in found[0]['rows']:
  if not row:continue
  title=re.split('[【〈]',row[0])[0].strip()
  if title in titles:assert len(row)==13;rows.append({'title':title,'cells':row[1:]})
 assert len(rows)==7;out.append({'file':name,'sha256':sha256((b/name).read_bytes()).hexdigest(),'records':rows})
(b/'DIGITAL_TABLE_EXTRACTS.json').write_text(json.dumps({'date':'2026-10-29','method':'Standard-library HTMLParser, only the uniquely identified月方吉table; no OCR/no text normalization of cells','files':out,'independentWitnessCountForSameDigitalReadings':0},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'parsedBodies':len(out),'monthlyRowsEach':7,'monthlyCellsEach':84}))
