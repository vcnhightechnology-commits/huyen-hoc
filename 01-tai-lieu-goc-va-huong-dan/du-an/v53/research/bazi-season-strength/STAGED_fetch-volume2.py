from pathlib import Path
from hashlib import sha256,sha1
import urllib.request,urllib.parse,urllib.error,ssl,json
b=Path(__file__).resolve().parent
title='File:CADAL06066038 三命通會·卷二.djvu'
params=dict(action='query',format='json',formatversion='2',titles=title,prop='imageinfo|revisions',iiprop='url|size|sha1|timestamp|extmetadata',rvprop='ids|timestamp|content',rvslots='main')
url='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(params)
records=[]
def fetch(url,file,kind):
 p=b/file;assert not p.exists()
 request=urllib.request.Request(url,headers={'User-Agent':'HuyenHocCac-local-research/1.0 (public book source collation; no login)'})
 try:
  with urllib.request.urlopen(request,context=ssl.create_default_context(),timeout=50)as response:body=response.read();status=response.status;headers=dict(response.headers);final=response.url
 except urllib.error.HTTPError as e:body=e.read();status=e.code;headers=dict(e.headers);final=e.url
 p.write_bytes(body)
 item=dict(date='2026-10-28',requestedURL=url,finalURL=final,file=file,status=status,bytes=len(body),sha256=sha256(body).hexdigest(),responseHeaders=headers,TLSCertificateValidationEnabled=True,kind=kind)
 records.append(item);(b/'REQUESTS.json').write_text(json.dumps(dict(date='2026-10-28',records=records),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 assert status==200,(file,status)
 return body,item
body,record=fetch(url,'commons-volume2-metadata-response.json','repository metadata,not institution original server')
obj=json.loads(body);page=obj['query']['pages'][0];assert not page.get('missing');info=page['imageinfo'][0];revision=page['revisions'][0]
assert info['size']==10858550 and info['sha1']=='7ee461bd944fbf23fcf0a0011aff5882214bca5c'
record.update(pageID=page['pageid'],revisionID=revision['revid'],revisionTimestamp=revision['timestamp'],expectedSourceBytes=info['size'],expectedSourceSHA1=info['sha1'])
pinned='https://commons.wikimedia.org/w/index.php?title='+urllib.parse.quote(title)+'&oldid='+str(revision['revid'])
fetch(pinned,'commons-volume2-description-pinned.html','pinned repository attribution,not independently authenticated CADAL institutional catalogue')
body,record=fetch(info['url'],'CADAL06066038.djvu','repository DjVu facsimile; upload derived from CADAL PDF per file history')
assert len(body)==info['size']and sha1(body).hexdigest()==info['sha1']and body[:8]==b'AT&TFORM'
record.update(apiSizeAndSHA1Matched=True,sha1=sha1(body).hexdigest(),magic='AT&TFORM')
(b/'REQUESTS.json').write_text(json.dumps(dict(date='2026-10-28',records=records),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(b/'ACQUISITION.json').write_text(json.dumps(dict(date='2026-10-28',sourceTitle=title,sourceFile='CADAL06066038.djvu',sourceSHA256=sha256(body).hexdigest(),sourceBytes=len(body),metadata=info,pinnedDescription=pinned,
 sourceInstitutionAttributedByRepository='CADAL 06066038 / Zhejiang University',institutionOriginalBytesDownloaded=False,independentInstitutionCatalogueVerified=False,actuallyViewedPages=[],sourceWholeWorkRead=False,consumerChanged=False),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(sourceBytes=len(body),sourceSHA256=sha256(body).hexdigest(),apiSizeAndSHA1Matched=True,HTTP200TLSBodies=len(records),actuallyReadPages=0)))
