from pathlib import Path
from hashlib import sha256,sha1
import json,urllib.request,ssl
d=Path(__file__).resolve().parent
metadata=json.loads((d/'gjts-commons-metadata-response.json').read_text(encoding='utf-8'))
record=next(x for x in metadata['query']['pages']if x['title']=='File:Gujin Tushu Jicheng, Volume 476 (1700-1725).djvu');info=record['imageinfo'][0]
url=info['url'];req=urllib.request.Request(url,headers={'User-Agent':'HuyenHocCac-local-research/1.0 (public source collation; no login)'})
with urllib.request.urlopen(req,context=ssl.create_default_context(),timeout=60)as response:
 body=response.read();status=response.status;headers=dict(response.headers);final=response.url
p=d/'Gujin-Tushu-Jicheng-Volume476.djvu';assert not p.exists();p.write_bytes(body)
assert len(body)==info['size']and sha1(body).hexdigest()==info['sha1']and body[:8]==b'AT&TFORM'
meta={'date':'2026-10-28','requestedURL':url,'finalURL':final,'status':status,'responseHeaders':headers,'file':p.name,'bytes':len(body),'sha256':sha256(body).hexdigest(),'sha1':sha1(body).hexdigest(),'apiSizeAndSHA1Match':True,'TLSCertificateValidationEnabled':True,'metadataFile':'gjts-commons-metadata-response.json','pagecountFromRepository':info['pagecount'],'metadataCredit':'Scan downloaded from pan.baidu.com; publisher/institution original server not independently established','metadataWorkDateNotVerifiedScanImprintDate':True,'vectorizedPNGorSVGNotUsedAsOriginalWitness':True}
p=d/'REQUESTS.json';log=json.loads(p.read_text(encoding='utf-8-sig'));log['records'].append(meta);p.write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in meta.items()if k not in ['responseHeaders','requestedURL','finalURL']},ensure_ascii=False))
