from pathlib import Path
from hashlib import sha256
import json,urllib.request,urllib.parse,ssl,re
d=Path(__file__).resolve().parent
text=(d/'gjts676-decoded-wikitext.txt').read_text(encoding='utf-8')
m=re.search(r'<pages index="([^"]+)" from="(\d+)" to="(\d+)"',text);assert m
index,first,last=m.group(1),int(m.group(2)),int(m.group(3));assert last-first+1==11
titles=[f'Page:{index}/{p}'for p in range(first,last+1)]
params={'action':'query','format':'json','formatversion':'2','prop':'revisions','rvprop':'ids|timestamp|content','rvslots':'main','titles':'|'.join(titles)}
url='https://zh.wikisource.org/w/api.php?'+urllib.parse.urlencode(params)
req=urllib.request.Request(url,headers={'User-Agent':'HuyenHocCac-local-research/1.0 (public source collation; no login)'})
with urllib.request.urlopen(req,context=ssl.create_default_context(),timeout=45)as response:
 body=response.read();status=response.status;headers=dict(response.headers);final=response.url
p=d/'gjts676-page-revisions-response.json';assert not p.exists();p.write_bytes(body)
meta={'date':'2026-10-28','requestedURL':url,'finalURL':final,'status':status,'responseHeaders':headers,'file':p.name,'bytes':len(body),'sha256':sha256(body).hexdigest(),'TLSCertificateValidationEnabled':True,'basis':'Exact index/from/to from retained revision1942639; Page namespace titles derived explicitly','pages':[]}
obj=json.loads(body);out=d/'gjts676-pages';out.mkdir(exist_ok=True)
for page in obj['query']['pages']:
 assert not page.get('missing');rev=page['revisions'][0];pageText=rev['slots']['main']['content'];ordinal=int(page['title'].rsplit('/',1)[1]);p=out/f'p{ordinal}.txt';p.write_text(pageText,encoding='utf-8',newline='\n')
 meta['pages'].append({'pageID':page['pageid'],'title':page['title'],'revisionID':rev['revid'],'timestamp':rev['timestamp'],'file':p.relative_to(d).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest(),'isDecodedWorkingTextNotRawHTTP':True,'fullyRead':False})
assert len(meta['pages'])==11
p=d/'REQUESTS.json';log=json.loads(p.read_text(encoding='utf-8-sig'));log['records'].append(meta);p.write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':status,'responseBytes':len(body),'responseSHA256':meta['sha256'],'transcludedPageRevisions':len(meta['pages']),'allFullyRead':False}))
