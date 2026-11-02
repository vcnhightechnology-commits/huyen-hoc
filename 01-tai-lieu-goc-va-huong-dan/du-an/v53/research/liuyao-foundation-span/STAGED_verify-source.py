from pathlib import Path
from hashlib import sha256
from PIL import Image
import json,subprocess,shutil
w=Path(__file__).resolve().parents[2];s=Path(__file__).resolve().parent
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
def write(n,d):(s/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
m=read(s/'SOURCE_MANIFEST.json');pdf=w/m['sourcePDF'];assert sha(pdf)==m['sourceSHA256']and pdf.stat().st_size==m['sourceBytes']
for x in m['records']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256']and Image.open(p).size==tuple(x['size'])and x['actuallyViewed']
qa=read(s/'QA_RENDERS.json')
for x in qa['records']:
 a=s/x['qaFile'];b=s/x['cropFile'];assert sha(a)==x['qaSHA256']and sha(b)==x['cropSHA256']and x['cropActuallyViewed']
 im=Image.open(a).convert('RGB').crop(x['cropBox']);target=Image.open(b).convert('RGB');assert im.size==target.size and im.tobytes()==target.tobytes()
crop=read(s/'MOTION_CROP.json');p=w/crop['source'];a=Image.open(p).convert('RGB').crop(crop['cropBox']);b=Image.open(s/crop['cropFile']).convert('RGB');assert sha(p)==crop['sourceSHA256']and sha(s/crop['cropFile'])==crop['cropSHA256']and a.size==b.size and a.tobytes()==b.tobytes();crop['actuallyViewed']=True;crop['pixelMatch']=True;write('MOTION_CROP.json',crop)
reproductions=[]
for n,dpi,target in[(26,230,w/'v53/research/liuyao-foundations/images/zengshan-26.png'),(29,360,s/'qa360-29.png')]:
 out=s/f'redecode-{n}-{dpi}.png';subprocess.run([shutil.which('pdftoppm'),'-r',str(dpi),'-f',str(n),'-l',str(n),'-singlefile','-png',str(pdf),str(out.with_suffix(''))],check=True,capture_output=True)
 a=Image.open(out).convert('RGB');b=Image.open(target).convert('RGB');assert a.size==b.size and a.tobytes()==b.tobytes()
 reproductions.append({'pdfPage':n,'dpi':dpi,'file':out.name,'sha256':sha(out),'targetSHA256':sha(target),'pixelMatch':True,'newSourcePosition':False})
out={'date':'2026-10-28','retainedPDFBytesVerified':m['sourceBytes'],'retainedPDFSHA256':m['sourceSHA256'],'retainedImageHashesVerified':28,'retainedSourcePositionsReviewed':28,'newHTTPRequests':0,'newSourcePositions':0,'newOriginalContainers':0,'newIndependentWitnesses':0,'sourceAnomalyCropsViewedAndVerified':3,'motionNativeCropViewedAndVerified':1,'fullHigherResolutionPagesViewedNotClaimed':True,'pixelReproductions':reproductions,'firstPassSpansAdded':7,'firstPassUnitsCurrent':137,'wholeUnitsApplied':0,'allSourceCharactersCollated':False,'sourceMismatchesRetained':3,'consumerChanged':False,'wholeCatalogueCompleted':False}
write('SOURCE_RESULTS.json',out);print(json.dumps(out))
