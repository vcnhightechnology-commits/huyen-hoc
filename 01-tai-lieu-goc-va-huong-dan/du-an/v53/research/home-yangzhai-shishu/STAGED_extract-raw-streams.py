from pathlib import Path
from hashlib import sha256
from pypdf import PdfReader
from PIL import Image,ImageChops,ImageStat
import json,io
s=Path(__file__).resolve().parent;read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));write=lambda p,d:p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
m=read(s/'NATIVE_IMAGES.json');r=PdfReader(s/'Tianyige-330000-1705-0007405-yangzhai-shishu.pdf');records=[]
for x in m['records']:
    image=list(r.pages[x['pdfPage']-1].images)[0];obj=image.indirect_reference.get_object();raw=obj._data;file=f"raw-p{x['pdfPage']:03d}.jpg";assert str(obj.get('/Filter'))=='/DCTDecode'
    p=s/file;assert not p.exists();p.write_bytes(raw);assert p.read_bytes()==obj._data
    a=Image.open(io.BytesIO(raw)).convert('RGB');b=Image.open(s/x['file']).convert('RGB');assert a.size==b.size
    equal=raw==(s/x['file']).read_bytes();diff=ImageChops.difference(a,b);stats=ImageStat.Stat(diff)
    records.append({'pdfPage':x['pdfPage'],'file':file,'bytes':len(raw),'sha256':sha256(raw).hexdigest(),'nativeSize':list(a.size),'nativeImageID':image.indirect_reference.idnum,'pdfFilter':'/DCTDecode','rawStreamByteIdentityVerified':True,'actuallyViewed':False,'pypdfDerivativeByteIdentical':equal,'pypdfDerivativeRGBPixelIdentical':diff.getbbox()is None,'pixelDifferenceMeanByRGBChannel':stats.mean,'derivativeFile':x['file']})
    x['method']='pypdf6.10page.images derivative at native dimensions;38/40 JPEGs reencoded by library,NOTrawDCTstream. OriginalPDFandseparaterawstreamsretained;nointentionalresizeorOCR.'
    x['sourceKind']='native-sized-pypdf-image-derivative';x['savedDerivativeEqualsRawDCTStream']=equal
write(s/'NATIVE_IMAGES.json',m);write(s/'RAW_STREAMS.json',{'date':'2026-10-28','sourcePDFSHA256':m['pdfSHA256'],'method':'OriginalPDFindirectImageXObject._data/DCTDecode saved byte-for-byte. No image encoder used.','records':records,'totalRawStreams':len(records),'pypdfDerivativeByteDifferent':sum(not x['pypdfDerivativeByteIdentical']for x in records),'pypdfDerivativeRGBDifferent':sum(not x['pypdfDerivativeRGBPixelIdentical']for x in records)})
old=read(s/'CROPS.json');rawcrops=[]
for x in old['records']:
    src=s/f"raw-p{x['pdfPage']:03d}.jpg";f=s/('raw-'+x['file']);Image.open(src).crop(x['box']).save(f)
    rawcrops.append({'pdfPage':x['pdfPage'],'sourceFile':src.name,'sourceSHA256':sha256(src.read_bytes()).hexdigest(),'file':f.name,'sha256':sha256(f.read_bytes()).hexdigest(),'box':x['box'],'nativeNoResize':True,'actuallyViewed':False,'pixelIdentityVerified':False})
write(s/'RAW_CROPS.json',{'date':'2026-10-28','records':rawcrops,'oldDerivativeCropsRetained':True})
print(json.dumps({'rawStreams':len(records),'pypdfReencoded':sum(not x['pypdfDerivativeByteIdentical']for x in records),'RGBDifferent':sum(not x['pypdfDerivativeRGBPixelIdentical']for x in records),'rawCropsAwaitingView':4}))
