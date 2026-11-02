from pathlib import Path
import pypdf
r=pypdf.PdfReader('v53/research/four-items/sources/yuanhai-NTL-v1.pdf')
print('pages',len(r.pages))
for i,p in enumerate(r.pages):
 t=p.extract_text()
 if '子宮癸水' in t or '地支藏遁' in t: print('MATCH',i+1,t[:1500])
