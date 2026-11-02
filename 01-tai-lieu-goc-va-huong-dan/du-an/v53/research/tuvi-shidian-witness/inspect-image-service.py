from pathlib import Path
import re
B=Path(__file__).resolve().parent;s=(B/'client-7691.d2ca499c.js').read_text(encoding='utf-8')
for needle in ['getAllImages=function','getAllImages','AncientlibClient.','getBookPage','getAllImage']:
 hits=list(re.finditer(re.escape(needle),s));print(needle,len(hits))
 for m in hits[:3]:print(s[max(0,m.start()-1200):m.end()+450])
print('referenced client functions',sorted(set(re.findall(r'AncientlibClient\.([A-Za-z0-9_]+)',s))))
