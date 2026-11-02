from pathlib import Path
from hashlib import sha256
import json,re,sys
from PIL import Image

s=Path(__file__).resolve().parent
w=next(p for p in s.parents if (p/'v53/research/bazi-season-strength/CADAL06066038.djvu').is_file())
read=lambda n:json.loads((s/n).read_text(encoding='utf-8-sig'))
def check(p,x):
 b=p.read_bytes();assert len(b)==x['bytes']and sha256(b).hexdigest()==x['sha256'],p
for x in read('PREIMPLEMENTATION_FREEZE.json')['files']:check(s/x['file'],x)
review=read('NATIVE_REVIEW.json')
check(w/review['retainedContainer']['file'],review['retainedContainer']);check(w/review['decoder']['file'],review['decoder'])
assert review['retainedContainer']['sha256']=='7a53f35982f0b946281d0e393c5d6ddcce1fd091aea83c11af6a06bcdfe6a85e'
viewed=[];unread=[]
for x in review['records']:
 p=s/x['file'];check(p,x)
 with Image.open(p)as im:
  assert im.size==(x['width'],x['height'])
  assert sha256(im.convert('RGBA').tobytes()).hexdigest()==x['pixelRGBA_SHA256']
 (viewed if x['actuallyViewed']else unread).append(x['page'])
assert viewed==list(range(191,200))and unread==[200,201,202]
accepted=trial=0
for x in read('NATIVE_CROPS.json')['records']:
 raw=s/Path(x['raw']['file']).name;crop=s/Path(x['crop']['file']).name;check(raw,x['raw']);check(crop,x['crop']);assert x['viewed']
 with Image.open(raw)as im,Image.open(crop)as cr:
  box=x['boxXYXY'];assert 0<=box[0]<box[2]<=im.width and 0<=box[1]<box[3]<=im.height
  assert cr.size==(box[2]-box[0],box[3]-box[1])and cr.convert('RGB').tobytes()==im.crop(box).convert('RGB').tobytes()
 if x['accepted']:accepted+=1
 else:trial+=1
chapter=read('CHAPTER_DISPOSITIONS.json');check(w/chapter['sourceDigital']['file'],chapter['sourceDigital'])
source=(w/chapter['sourceDigital']['file']).read_text(encoding='utf-8-sig');start=source.index('　　論支元六合');end=source.index('　　論支元三合',start)
assert (s/'DIGITAL_CHAPTER_LOCATOR.txt').read_text(encoding='utf-8')==source[start:end]
clean=re.sub(r'[\s¶]','',re.sub(r'<pb:[^>]+>','',source[start:end]))
assert clean==(s/'CHAPTER_CLEAN.txt').read_text(encoding='utf-8')and sha256(clean.encode()).hexdigest()==chapter['cleanSHA256']
assert len(clean)==1087 and len(clean.encode('utf-16-le'))//2==1090
assert ''.join(x['literalDigital']for x in chapter['records'])==clean
assert chapter['firstPassChapterPositions']==list(range(192,200))and chapter['outsideBoundaryViewed']==[191]
manual=read('MANUAL_TABLES.json');assert len(manual['pairs'])==6 and len(manual['monthRows'])==len(manual['directedRows'])==12 and len(manual['hiddenRows'])==2
out={'date':'2026-10-29','passed':True,'retainedContainerBytes':review['retainedContainer']['bytes'],'sourcePositionsActuallyViewed':9,'firstPassChapterPositions':8,'outsideBoundaryPositions':1,'adjacentDecodedNotRead':3,'nativePNGRGBAHashesMatched':12,'acceptedCropsRGBMatched':accepted,'trialCropsRGBMatched':trial,'digitalCleanCodepoints':1087,'digitalUTF16Units':1090,'editorialDispositionUnits':14,'frozenFiles':5,'newHTTPBodies':0,'newContainers':0,'newIndependentWitnesses':0,'sourceMonthCalendarAdapter':False,'wholeChapterApplied':False}
if '--write-results'in sys.argv:(s/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
