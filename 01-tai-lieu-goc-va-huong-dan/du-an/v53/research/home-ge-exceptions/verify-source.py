from pathlib import Path
from hashlib import sha256
import json,sys
from PIL import Image

s=Path(__file__).resolve().parent
w=next(p for p in s.parents if (p/'v53/research/home-day-hour-scopes').is_dir())
read=lambda name:json.loads((s/name).read_text(encoding='utf-8-sig'))
def check(p,identity):
    b=p.read_bytes()
    assert len(b)==identity['bytes'] and sha256(b).hexdigest()==identity['sha256'],p
frozen=read('PREIMPLEMENTATION_FREEZE.json')
for x in frozen['files']:check(s/x['file'],x)
reuse=read('SOURCE_REUSE.json')
for x in [*reuse['sourceImages'],reuse['digitalText'],reuse['digitalHTML']]:check(w/x['file'],x)
accepted=excluded=0
for x in read('NATIVE_CROPS.json')['records']:
    raw=w/x['source']['file'];crop=s/Path(x['crop']['file']).name
    check(raw,x['source']);check(crop,x['crop']);assert x['viewed']
    with Image.open(raw)as im,Image.open(crop)as cr:
        box=x['boxXYXY'];assert 0<=box[0]<box[2]<=im.width and 0<=box[1]<box[3]<=im.height
        assert cr.size==(box[2]-box[0],box[3]-box[1])
        assert cr.convert('RGB').tobytes()==im.crop(box).convert('RGB').tobytes()
    if x['accepted']:accepted+=1
    else:excluded+=1
manual=read('MANUAL_CONDITIONS.json')
assert len(manual['records'])==10 and len({r['imageHeading']for r in manual['records']})==7
assert [r['id']for r in manual['records']if r['disposition']=='local-exception-from-declared-premises']==['forest-mountain-timber','sacrifice-shen-present']
assert reuse['newSourcePositions']==reuse['newHTTPBodies']==reuse['newEngineCalls']==0
out={'date':'2026-10-29','passed':True,'sourceImagesReused':3,'nativeCropsRGBMatched':accepted,
 'excludedTrialsRGBMatched':excluded,'frozenFiles':4,'selectedConditionUnits':10,'headingGroups':7,
 'newHTTPBodies':0,'newSourcePositions':0,'newCalendarEngineCalls':0,'newIndependentWitnesses':0,
 'digitalSourceIndependentOfImages':False,'wholeWorkApplied':False}
if '--write-results'in sys.argv:(s/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
