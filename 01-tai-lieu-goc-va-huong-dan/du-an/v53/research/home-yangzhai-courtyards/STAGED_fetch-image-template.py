from pathlib import Path
from hashlib import sha256
import json,urllib.request,urllib.parse,ssl
d=Path(__file__).resolve().parent
params={'action':'query','format':'json','formatversion':'2','prop':'revisions','rvprop':'ids|timestamp|content','rvslots':'main','titles':'Template:GJTSJC image'}
url='https://zh.wikisource.org/w/api.php?'+urllib.parse.urlencode(params)
request=urllib.request.Request(url,headers={'User-Agent':'HuyenHocCac-local-research/1.0 (public source collation; no login)'})
with urllib.request.urlopen(request,context=ssl.create_default_context(),timeout=45)as response:
 body=response.read();status=response.status;headers=dict(response.headers);final=response.url
p=d/'gjts-image-template-response.json';assert not p.exists();p.write_bytes(body)
obj=json.loads(body);page=obj['query']['pages'][0];rev=page['revisions'][0];text=rev['slots']['main']['content'];out=d/'gjts-image-template-decoded.txt';out.write_text(text,encoding='utf-8',newline='\n')
meta={'date':'2026-10-28','requestedURL':url,'finalURL':final,'status':status,'responseHeaders':headers,'file':p.name,'bytes':len(body),'sha256':sha256(body).hexdigest(),'TLSCertificateValidationEnabled':True,'basis':'Template name observed in retained Page revisions; read-only resolution of cited file identifiers','revisionID':rev['revid'],'revisionTimestamp':rev['timestamp'],'workingText':out.name}
p=d/'REQUESTS.json';log=json.loads(p.read_text(encoding='utf-8-sig'));log['records'].append(meta);p.write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(text)
