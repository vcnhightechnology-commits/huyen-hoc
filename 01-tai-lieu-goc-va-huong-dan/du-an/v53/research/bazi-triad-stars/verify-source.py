from pathlib import Path
from hashlib import sha256
import json,re,sys
from PIL import Image
s=Path(__file__).resolve().parent;w=next(p for p in s.parents if(p/'v53/research/bazi-season-strength/CADAL06066038.djvu').is_file())
read=lambda n:json.loads((s/n).read_text(encoding='utf-8-sig'))
def check(p,x):
 b=p.read_bytes();assert len(b)==x['bytes']and sha256(b).hexdigest()==x['sha256'],p
for x in read('PREIMPLEMENTATION_FREEZE.json')['files']:check(s/x['file'],x)
n=read('NATIVE_REVIEW.json');check(w/n['retainedContainer']['file'],n['retainedContainer']);check(w/n['decoder']['file'],n['decoder'])
assert n['retainedContainer']['sha256']=='7a53f35982f0b946281d0e393c5d6ddcce1fd091aea83c11af6a06bcdfe6a85e'
for x in n['records']:
 p=s/x['file'];check(p,x);assert x['actuallyViewed']
 with Image.open(p)as im:assert im.size==(x['width'],x['height'])and sha256(im.convert('RGBA').tobytes()).hexdigest()==x['pixelRGBA_SHA256']
assert [x['page']for x in n['records']]==list(range(204,210))and n['newPositionsActuallyViewed']==[206,207,208,209]
for x in read('NATIVE_CROPS.json')['records']:
 raw=s/Path(x['raw']['file']).name;crop=s/Path(x['crop']['file']).name;check(raw,x['raw']);check(crop,x['crop']);assert x['viewed']and x['accepted']
 with Image.open(raw)as im,Image.open(crop)as cr:
  box=x['boxXYXY'];assert 0<=box[0]<box[2]<=im.width and 0<=box[1]<box[3]<=im.height
  assert cr.size==(box[2]-box[0],box[3]-box[1])and cr.convert('RGB').tobytes()==im.crop(box).convert('RGB').tobytes()
c=read('CHAPTER_DISPOSITIONS.json');check(w/c['sourceDigital']['file'],c['sourceDigital']);raw=(w/c['sourceDigital']['file']).read_text(encoding='utf-8-sig');start=raw.index('　　論將星華葢');end=raw.index('　　論六害',start)
assert raw[start:end]==(s/'DIGITAL_CHAPTER_LOCATOR.txt').read_text(encoding='utf-8')
clean=re.sub(r'[\s¶]','',re.sub(r'<pb:[^>]+>','',raw[start:end]));assert clean==(s/'CHAPTERS_CLEAN.txt').read_text(encoding='utf-8')and sha256(clean.encode()).hexdigest()==c['cleanSHA256']
assert ''.join(x['literalDigital']for x in c['records'])==clean and len(clean)==899 and len(clean.encode('utf-16-le'))//2==902 and len(c['records'])==38
m=read('MANUAL_COORDINATES.json');a=read('READING_AMENDMENT.json');assert m['generalCanopyBasis']['requiresFullTriadFormed']is False and a['adoptedValue']is None and a['frozenManualPreserved']
assert m['xianchiPreface']['literal']=='按此煞須天干納音於地同類方是若只論寅午戌在卯天干納音或不屬火非是'
out={'date':'2026-10-29','passed':True,'sourcePositionsReviewed':6,'newPositionsActuallyViewed':4,'priorPositionsReused':2,'nativePNGRGBAHashesMatched':6,'nativeCropsRGBMatched':3,'editorialUnits':38,'digitalCodepoints':899,'digitalUTF16Units':902,'frozenFiles':5,'readingAmendments':1,'newHTTPBodies':0,'newContainers':0,'newIndependentWitnesses':0,'wholeChaptersApplied':False,'consumerChanged':False}
if '--write-results'in sys.argv:(s/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
