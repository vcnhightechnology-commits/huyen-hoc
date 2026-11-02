from pathlib import Path
from hashlib import sha256
import json,re,sys
from PIL import Image
s=Path(__file__).resolve().parent
w=next(p for p in s.parents if(p/'v53/research/bazi-season-strength/CADAL06066038.djvu').is_file())
read=lambda n:json.loads((s/n).read_text(encoding='utf-8-sig'))
def check(p,x):
 b=p.read_bytes();assert len(b)==x['bytes']and sha256(b).hexdigest()==x['sha256'],p
for x in read('PREIMPLEMENTATION_FREEZE.json')['files']:check(s/x['file'],x)
review=read('NATIVE_REVIEW.json');check(w/review['retainedContainer']['file'],review['retainedContainer']);check(w/review['decoder']['file'],review['decoder'])
assert review['retainedContainer']['sha256']=='7a53f35982f0b946281d0e393c5d6ddcce1fd091aea83c11af6a06bcdfe6a85e'
for x in review['records']:
 check(s/x['file'],x);assert x['actuallyViewed']
 with Image.open(s/x['file'])as im:assert im.size==(x['width'],x['height'])and sha256(im.convert('RGBA').tobytes()).hexdigest()==x['pixelRGBA_SHA256']
assert [r['page']for r in review['records']]==list(range(199,206))and review['firstPassNewPositions']==list(range(200,206))
accepted=trial=0
for x in read('NATIVE_CROPS.json')['records']:
 raw=s/Path(x['raw']['file']).name;crop=s/Path(x['crop']['file']).name;check(raw,x['raw']);check(crop,x['crop']);assert x['viewed']
 with Image.open(raw)as im,Image.open(crop)as cr:
  box=x['boxXYXY'];assert 0<=box[0]<box[2]<=im.width and 0<=box[1]<box[3]<=im.height
  assert cr.size==(box[2]-box[0],box[3]-box[1])and cr.convert('RGB').tobytes()==im.crop(box).convert('RGB').tobytes()
 if x['accepted']:accepted+=1
 else:trial+=1
c=read('CHAPTER_DISPOSITIONS.json');check(w/c['sourceDigital']['file'],c['sourceDigital']);raw=(w/c['sourceDigital']['file']).read_text(encoding='utf-8-sig');start=raw.index('　　論支元三合');end=raw.index('　　論將星華葢',start)
assert raw[start:end]==(s/'DIGITAL_CHAPTER_LOCATOR.txt').read_text(encoding='utf-8')
clean=re.sub(r'[\s¶]','',re.sub(r'<pb:[^>]+>','',raw[start:end]));assert clean==(s/'CHAPTER_CLEAN.txt').read_text(encoding='utf-8')and sha256(clean.encode()).hexdigest()==c['cleanSHA256']
assert ''.join(r['literalDigital']for r in c['records'])==clean and len(clean)==807 and len(c['records'])==22
assert c['firstPassChapterPositions']==list(range(199,205))and c['newFirstPassPositions']==list(range(200,205))and c['outsideBoundaryViewed']==[205]
manual=read('MANUAL_TABLES.json');assert len(manual['groups'])==5 and sum(g['threeBranchGroup']for g in manual['groups'])==4
assert '故申子申為水局'in clean and manual['selectedLiteralAnomalies'][0]['image']=='故申子申為水局'
out={'date':'2026-10-29','passed':True,'retainedContainerBytes':review['retainedContainer']['bytes'],'sourcePositionsReviewed':7,'sourcePositionsNewlyViewed':6,'chapterPositions':6,'sharedPriorBoundary':1,'outsideBoundary':1,'nativePNGRGBAHashesMatched':7,'acceptedCropsRGBMatched':accepted,'trialCropsRGBMatched':trial,'digitalCleanCodepoints':807,'editorialDispositionUnits':22,'frozenFiles':5,'newHTTPBodies':0,'newContainers':0,'newIndependentWitnesses':0,'wholeChapterApplied':False}
if '--write-results'in sys.argv:(s/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
