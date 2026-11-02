from pathlib import Path
from hashlib import sha256
import json,urllib.request,urllib.parse,ssl,re
d=Path(__file__).resolve().parent;names=[]
for pos in [86,87,88,89]:
 text=(d/f'gjts676-pages/p{pos}.txt').read_text(encoding='utf-8')
 for name in re.findall(r'\{\{GJTSJC image\|([^|}]+)',text):
  if 'pic18'in name and any(f'pic{n}'in name for n in range(1805,1817)):names.append(name)
assert len(names)==12
container='Gujin Tushu Jicheng, Volume 476 (1700-1725).djvu'
titles=['File:'+container]+['File:'+name+ext for name in names for ext in ['.svg','.png']]
params={'action':'query','format':'json','formatversion':'2','prop':'imageinfo','iiprop':'url|sha1|size|mime|timestamp|extmetadata','titles':'|'.join(titles)}
url='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(params)
req=urllib.request.Request(url,headers={'User-Agent':'HuyenHocCac-local-research/1.0 (public source collation; no login)'})
with urllib.request.urlopen(req,context=ssl.create_default_context(),timeout=45)as res:body=res.read();status=res.status;headers=dict(res.headers);final=res.url
p=d/'gjts-commons-metadata-response.json';assert not p.exists();p.write_bytes(body)
obj=json.loads(body);existing=[x for x in obj['query']['pages']if x.get('imageinfo')];missing=[x['title']for x in obj['query']['pages']if not x.get('imageinfo')]
meta={'date':'2026-10-28','requestedURL':url,'finalURL':final,'status':status,'responseHeaders':headers,'file':p.name,'bytes':len(body),'sha256':sha256(body).hexdigest(),'TLSCertificateValidationEnabled':True,'existingTitles':[x['title']for x in existing],'missingTitles':missing}
p=d/'REQUESTS.json';log=json.loads(p.read_text(encoding='utf-8-sig'));log['records'].append(meta);p.write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':status,'existing':[{'title':x['title'],'imageinfo':x['imageinfo']}for x in existing],'missingCount':len(missing)},ensure_ascii=False))
