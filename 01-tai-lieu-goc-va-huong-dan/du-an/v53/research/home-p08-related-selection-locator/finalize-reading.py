from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json
W=Path(__file__).resolve().parents[2];B=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(n,d):(B/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def ident(p):return {'file':p.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
source=W/'v53/research/home-yangzhai-courtyards/Gujin-Tushu-Jicheng-Volume476.djvu'
assert sha256(source.read_bytes()).hexdigest()=='e819d6f430065e4f63c121390d74ad6d3bc36457cfb8e59fb7a2cea6483130de'
records=[]
for p in [B/'GJTS_LOCAL_RENDERS.json',*sorted(B.glob('GJTS_RENDERS_*.json'))]:
 d=read(p);assert d['sourceSHA256']==ident(source)['sha256']
 for r in d['records']:
  f=B/r['file'];assert f.stat().st_size==r['bytes']and sha256(f.read_bytes()).hexdigest()==r['sha256']
  im=Image.open(f).convert('RGBA');assert im.size==(r['width'],r['height']);assert sha256(im.tobytes()).hexdigest()==r['pixelRGBA_SHA256']
  records.append({**r,'actuallyViewed':True,'viewScope':'Layout/heading location only; not all characters collated or whole-page application.','metadataFile':p.name})
assert len(records)==9 and sorted(r['page']for r in records)==[95,96,97,98,99,100,101,102,105]
crop=B/'p96-selection-editorial-note.png';box=[620,3940,2050,5630]
a=Image.open(B/'gjts-p96.png').convert('RGB').crop(box);z=Image.open(crop).convert('RGB');assert a.size==z.size and ImageChops.difference(a,z).getbbox()is None
write('SOURCE_AND_VIEW_AUDIT.json',{'date':'2026-10-29','retainedContainer':ident(source),'decoder':ident(W/'v53/research/bazi-pattern-extension/tooling/djvu.js'),'records':records,'selectedNativeCrop':{**ident(crop),'boxXYXY':box,'RGBMatchesDecodedNative':True,'actuallyViewed':True},'initialTemplateDateCaveat':'First 99 metadata inherited 2026-10-28 from its template. All nine local renders and visual reviews in this scope occurred on 2026-10-29. Initial metadata is retained, not silently revised.','initialLaunchAudit':'PowerShell quoting failed before prepare.py existed; subsequent Node module-not-found made no decode/engine calls. Prepared via saved Python file, then decoded each selected page once.','newHTTPBodies':0,'newOriginalContainers':0,'newEngineCalls':0,'fullDiplomaticPageTranscription':False})
write('WORK_STATE.json',{'date':'2026-10-29','status':'bounded-related-compilation-locator-negative-for-720-grid;private-not-promoted','catalogueID':'P08','sourceDirectory':'v53/research/home-yangzhai-courtyards','containerAlreadyRetained':True,'locatorPositions':[95,96,97,98,99,100,101,102,105],'selectedSectionPositions':[96,97,98,99,100,101],'newP08SourcePositions':0,'newHTTPBodies':0,'newIndependentP08EditionsEstablished':0,'fullPagesDiplomaticallyCollated':0,'P08ReadableLabelsUnchanged':500,'P08UnresolvedLabelsUnchanged':220,'consumerChanged':False,'wholeCatalogueCompleted':False,'finding':'At bottom of96:論選擇第九. Selected layout96..101 continues selection/命前五神/九宮/年命/太陰過宮/節氣;102 opens論符鎮第十. No matching720cell day grid located in this bounded selection section. This is not proof of absence elsewhere in the135page container or other compilation volumes.','selectedEditorialNote':'另見選擇部故不錄','editorialNoteLimits':'Only this short fragment collated from native crop. Do not claim every nearby word, or identify exactly which P08 tables the note omitted.','disposition':'Do not fill P08 labels from this related abridged section. Search another legitimate source/context or a justified separate compilation 選擇部 route; do not re-render95..102/105 just to seek the same grid.','currentReleaseBoundary':'Created after the source-package file inventory was frozen; these nine locator renders are private working evidence and not asserted present in that ZIP.','next':['Retain the day/direction context inspector at tmp/home-p08-grid-priority-staging; promote with a useful subsequent combined scope.','For unresolved220labels, require actual matching table coordinates from a legitimate facsimile, not OCR, repetition or caption analogy.','Review already retained holdings before new acquisitions; no retry of prior blocked sources.']})
write('SOURCE_RESULTS.json',{'passed':True,'sourceContainerSHA256Matched':True,'nativePNGsByteAndRGBAMatched':9,'selectedCropRGBMatched':1,'sourceSelectionSectionLocated':[96,97,98,99,100,101],'matching720CellGridFound':False,'P08CellLabelsChanged':0,'newHTTPBodies':0,'newEngineCalls':0,'newOriginalContainers':0,'independentP08EditionEstablished':False,'consumerChanged':False})
print(json.dumps({'passed':True,'renderIdentitiesAndNativePixelsVerified':9,'cropRGBMatched':1,'P08CellLabelsChanged':0}))
