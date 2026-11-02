from pathlib import Path
from hashlib import sha256
import json,re,tarfile
from PIL import Image

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/tuvi-masters';q=r/'qa/tuvi-masters'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
m=read(b/'SOURCE_MANIFEST.json');table=read(b/'SOURCE_TABLES.json');crops=read(b/'CROPS.json')['records']
assert sha(w/m['retainedManifest'])==m['retainedManifestSHA256']
manifest=read(w/m['retainedManifest']);viewer=(r/'research/fortune-followup/official-viewer.html').read_text(encoding='utf-8')
public=json.loads(re.search(r'var najContentList = (\[.*?\]);',viewer,re.S).group(1))
for x in m['images']:
 p=w/x['file'];assert sha(p)==x['sha256']==x['retainedRequest']['sha256']
 assert p.stat().st_size==x['retainedRequest']['bytes'] and x['retainedRequest']['status']==200 and x['retainedRequest']['tls']['authorized']
 assert Image.open(p).size==(2200,1659)
 canvas=manifest['sequences'][0]['canvases'][x['canvas']-1]
 assert x['retainedRequest']['url']==canvas['images'][0]['resource']['service']['@id']+'/full/2200,/0/native.jpg'
 assert not public[x['canvas']-1]['restricted']
for x in crops:
 assert sha(w/x['source'])==x['sourceSHA256']and sha(b/x['crop'])==x['cropSHA256']
 original=Image.open(w/x['source']).convert('RGB');crop=Image.open(b/x['crop']).convert('RGB')
 assert original.size==tuple(x['sourceSize'])and original.crop(x['box']).tobytes()==crop.tobytes()and x['nativePixelsUnscaled']
assert len(crops)==2 and read(b/'MANUAL_READINGS.json')['directNativeCropsViewed']==2
assert len(table['rows'])==24 and len({(x['kind'],x['branch'])for x in table['rows']})==24
assert sum(x['kind']=='body-master'and x['sourceSingleStarResolved']for x in table['rows'])==10
assert [x['branch']for x in table['rows']if x['kind']=='body-master'and not x['sourceSingleStarResolved']]==['子','午']
assert all(x['sourceNameLiteral']=='火鈴星'and x['canonicalSimplifiedStar']is None for x in table['rows']if x['kind']=='body-master'and not x['sourceSingleStarResolved'])
assert not table['bodyBirthYearAnchorExplicitlyAttested']and not table['wholeBookApplied']
tgz=w/m['runtimeTarball'];assert sha(tgz)==m['runtimeTarballSHA256']
with tarfile.open(tgz,'r:gz')as archive:
 for x in m['runtime']:
  p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256']
  name=x['file'].split('node_modules/iztro/')[1]
  assert p.read_bytes()==archive.extractfile('package/'+name).read()
out={'date':'2026-10-27','retainedPublicImageDerivativesVerified':2,'nativePixelCropsVerified':2,'sourceMingCoordinates':12,'sourceBodyCoordinates':12,
 'bodyDirectSingleStarCoordinates':10,'bodyUnresolvedCompoundCoordinates':2,'runtimeTarballIdentityVerified':True,'runtimeFilesByteIdenticalToTarball':4,
 'newHTTPRequests':0,'newOriginalContainers':0,'newSourcePages':0,'expandedPreviouslyReadPages':2,'originalJP2BytesAcquired':False,
 'bodyBirthYearAnchorExplicitlyAttested':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False}
(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,ensure_ascii=False))
