from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,urllib.request,urllib.error,ssl
B=Path(__file__).resolve().parent
url='https://www.shidianguji.com/zh/book/SDZJ0170/chapter/1jvzooy7dkbhh'
assert not(B/'chapter-response.html').exists()and not(B/'REQUEST.json').exists()
req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (source-research; one bounded public chapter request)'})
try:
 with urllib.request.urlopen(req,timeout=40,context=ssl.create_default_context())as r:
  body=r.read(8*1024*1024+1);assert len(body)<=8*1024*1024
  (B/'chapter-response.html').write_bytes(body)
  out={'url':url,'finalURL':r.url,'status':r.status,'headers':dict(r.headers),'bytes':len(body),'sha256':sha256(body).hexdigest(),'TLSVerified':True,'acquiredUTC':datetime.now(timezone.utc).isoformat(),'bodyFile':'chapter-response.html','originalFacsimileAcquired':False,'independentEditionEstablished':False}
except Exception as e:
 out={'url':url,'status':'request-failed','errorType':type(e).__name__,'error':str(e),'TLSVerificationDisabled':False,'retryAttempted':False,'acquiredUTC':datetime.now(timezone.utc).isoformat()}
(B/'REQUEST.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items()if k!='headers'},ensure_ascii=False))
