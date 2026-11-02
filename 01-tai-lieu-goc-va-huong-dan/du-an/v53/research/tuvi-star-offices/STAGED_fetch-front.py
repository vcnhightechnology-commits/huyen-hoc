from pathlib import Path
from hashlib import sha256
import urllib.request,urllib.error,ssl,json,concurrent.futures,threading
w=Path.cwd();b=Path(__file__).resolve().parent;b.mkdir(exist_ok=True)
manifest_file=w/'v53/research/fortune-followup/official-manifest.json'
manifest=json.loads(manifest_file.read_text(encoding='utf-8-sig'))
canvases=manifest['sequences'][0]['canvases'];assert len(canvases)==129
lock=threading.Lock();records=[]
def save():
 (b/'REQUESTS.json').write_text(json.dumps(dict(date='2026-10-28',records=sorted(records,key=lambda x:x['canvas'])),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def fetch(n):
 resource=canvases[n-1]['images'][0]['resource'];url=resource['@id'].replace('/full/max/','/full/2200,/')
 assert url.startswith('https://www.digital.archives.go.jp/api/content/')
 p=b/f'canvas-{n:03}.jpg';assert not p.exists()
 request=urllib.request.Request(url,headers={'User-Agent':'HuyenHocCac-local-research/1.0 (public historic-book study; no login)'})
 try:
  with urllib.request.urlopen(request,context=ssl.create_default_context(),timeout=50)as response:body=response.read();status=response.status;headers=dict(response.headers);final=response.url
 except urllib.error.HTTPError as e:body=e.read();status=e.code;headers=dict(e.headers);final=e.url
 except Exception as e:
  with lock:records.append(dict(canvas=n,requestedURL=url,errorType=type(e).__name__,error=str(e),TLSCertificateValidationEnabled=True,bodyRetained=False));save()
  return
 output=p if status==200 and body[:2]==b'\xff\xd8' else b/f'canvas-{n:03}-response.bin'
 output.write_bytes(body)
 rec=dict(canvas=n,requestedURL=url,finalURL=final,status=status,file=output.name,bytes=len(body),sha256=sha256(body).hexdigest(),responseHeaders=headers,
  TLSCertificateValidationEnabled=True,kind='Institution-served2200widthJPEGderivative;notoriginalJP2bytes',actuallyViewed=False)
 with lock:records.append(rec);save()
with concurrent.futures.ThreadPoolExecutor(max_workers=3)as pool:list(pool.map(fetch,range(1,13)))
assert len(records)==12
print(json.dumps(dict(retainedBodies=sum('file'in x for x in records),HTTP200JPEG=sum(x.get('status')==200 and x.get('file','').endswith('.jpg')for x in records),actuallyViewed=0)))
