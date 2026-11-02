from pathlib import Path
from hashlib import sha256
import json,urllib.request,urllib.parse,urllib.error,ssl,datetime
d=Path(__file__).resolve().parent
title='欽定古今圖書集成/博物彙編/藝術典/第676卷'
params={'action':'query','format':'json','formatversion':'2','prop':'revisions','rvprop':'ids|timestamp|content','rvslots':'main','titles':title}
url='https://zh.wikisource.org/w/api.php?'+urllib.parse.urlencode(params)
req=urllib.request.Request(url,headers={'User-Agent':'HuyenHocCac-local-research/1.0 (public source collation; no login)'})
try:
 with urllib.request.urlopen(req,context=ssl.create_default_context(),timeout=45)as response:
  body=response.read();status=response.status;headers=dict(response.headers);final=response.url
except urllib.error.HTTPError as e:
 body=e.read();status=e.code;headers=dict(e.headers);final=e.url
except Exception as e:
 (d/'FETCH_ERROR.json').write_text(json.dumps({'date':'2026-10-28','url':url,'error':str(e),'responseBodyObtained':False,'tlsValidationDisabled':False},ensure_ascii=False,indent=2)+'\n',encoding='utf-8');raise
path=d/'gjts676-revision-response.json';assert not path.exists();path.write_bytes(body)
meta={'date':'2026-10-28','requestedURL':url,'finalURL':final,'status':status,'responseHeaders':headers,'file':path.name,'bytes':len(body),'sha256':sha256(body).hexdigest(),'TLSCertificateValidationEnabled':True,'notInstitutionOriginalFacsimile':True}
if status==200:
 obj=json.loads(body);page=obj['query']['pages'][0];rev=page['revisions'][0]
 meta.update(pageID=page['pageid'],title=page['title'],revisionID=rev['revid'],revisionTimestamp=rev['timestamp'],pinnedURL='https://zh.wikisource.org/w/index.php?title='+urllib.parse.quote(title)+'&oldid='+str(rev['revid']))
 text=rev['slots']['main']['content'];out=d/'gjts676-decoded-wikitext.txt';out.write_text(text,encoding='utf-8',newline='\n')
 meta['decodedWorkingText']={'file':out.name,'bytes':out.stat().st_size,'sha256':sha256(out.read_bytes()).hexdigest(),'notOriginalHTTPBytes':True}
(d/'REQUESTS.json').write_text(json.dumps({'date':'2026-10-28','records':[meta]},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in meta.items()if k not in ['responseHeaders','requestedURL','finalURL']},ensure_ascii=False))
