from pypdf import PdfReader
from pathlib import Path
from hashlib import sha256
import json
s=Path(__file__).resolve().parent;r=PdfReader(s/'Tianyige-330000-1705-0007405-yangzhai-shishu.pdf');m=json.loads((s/'NATIVE_IMAGES.json').read_text(encoding='utf-8'));bad=[]
for x in m['records']:
 im=list(r.pages[x['pdfPage']-1].images)[0];o=im.indirect_reference.get_object();raw=o._data;data=(s/x['file']).read_bytes()
 if raw!=data:bad.append({'page':x['pdfPage'],'filter':str(o.get('/Filter')),'rawBytes':len(raw),'dataBytes':len(data),'rawSHA':sha256(raw).hexdigest(),'dataSHA':sha256(data).hexdigest(),'rawEqualsImageData':raw==im.data,'imageEqualsSaved':im.data==data,'savedActuallyViewed':x['actuallyViewed']})
print(json.dumps(bad,ensure_ascii=False))
(s/'NATIVE_FAILURE_AUDIT.json').write_text(json.dumps({'date':'2026-10-28','failedClaim':'pypdfpage.imagesbytesidenticaltooriginalDCTstream','allFortySavedByteHashesStillMatch':True,'records':bad,'sourcePDFRewritten':False},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
