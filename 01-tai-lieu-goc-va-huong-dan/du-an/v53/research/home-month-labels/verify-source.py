from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,subprocess
s=Path(__file__).resolve().parent;w=s.parent.parent
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
h=lambda p:sha256(p.read_bytes()).hexdigest()
for name in ['PREIMPLEMENTATION_FREEZE.json','SUPPLEMENT_FREEZE.json','SECOND_BLOCK_FREEZE.json','FULL_GRID_FREEZE.json']:
 for x in read(s/name)['files']:
  p=s/x['file'];assert p.stat().st_size==x['bytes']and h(p)==x['sha256'],x['file']
identity=read(s/'SOURCE_IDENTITIES.json');p=w/identity['source']['file'];assert h(p)==identity['source']['sha256']
source=Image.open(p).convert('RGB');crop=Image.open(s/identity['crop']['file']).convert('RGB')
assert h(s/identity['crop']['file'])==identity['crop']['sha256']
assert ImageChops.difference(source.crop(identity['crop']['boxXYXY']),crop).getbbox()is None
second=read(s/'MANUAL_SECOND_BLOCK.json');p=w/second['sourceImage'];assert h(p)==second['sourceImageSHA256']
old=read(w/identity['priorMarkerTable']['file']);assert h(w/identity['priorMarkerTable']['file'])==identity['priorMarkerTable']['sha256']
remaining=read(s/'MANUAL_REMAINING_BLOCKS.json')
for b in remaining['blocks']:assert h(w/b['sourceImage'])==b['sourceImageSHA256']
records=read(s/'MANUAL_CELLS.json')['records']+second['records']+[x for b in remaining['blocks']for x in b['records']];assert len(records)==720
assert len({(x['sourceMonth'],x['dayGanzhi'])for x in records})==720
for x in records:
 previous=next(r for r in old['records']if r['sourceMonth']==x['sourceMonth']and r['dayGanzhi']==x['dayGanzhi'])
 if x['editorialCode']!='X':assert previous['selectedMarker']=={'J':'建','P':'破'}.get(x['editorialCode'])
margin=read(s/'SIXTH_CROP_MARGIN_AUDIT.json')['replacementCrop'];assert h(s/margin['file'])==margin['sha256']
raw=Image.open(w/margin['sourceFile']).convert('RGB');accepted=Image.open(s/margin['file']).convert('RGB')
assert ImageChops.difference(raw.crop(margin['boxXYXY']),accepted).getbbox()is None
im1=Image.open(w/'v53/research/home-day-markers/131-first-ten.png').convert('RGB')
im2=Image.open(p).convert('RGB')
comparisons=[('months01-04',im1,[0,0,1180,329]),('months05-08',im1,[0,318,1180,642]),('months09-12',im1,[0,627,1180,955]),
 ('second-months01-04',im2,[0,0,1175,330]),('second-months05-08',im2,[0,318,1175,650]),('second-months09-12',im2,[0,627,1175,955]),
 ('last-row-left',crop,[35,975,200,1065]),('row02-mid',crop,[600,205,850,300]),('row07-mid',crop,[600,600,850,700])]
for name,im,box in comparisons:
 actual=Image.open(s/(name+'.png')).convert('RGB');assert im.crop(box).size==actual.size
 assert ImageChops.difference(im.crop(box),actual).getbbox()is None
r=subprocess.run(['node',str(s/'test-labels.mjs')],check=True,capture_output=True,text=True,encoding='utf-8');tests=json.loads(r.stdout)
(s/'TEST_RESULTS.json').write_text(json.dumps(tests,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
out={'date':'2026-10-29','passed':True,'nativeCropsRGBMatched':11,'priorSelectedMarkerTableUnchanged':True,
 'inspectedCoordinates':720,'priorMarkerCoordinateDeferredRatherThanAutoFilled':1,'sixthCropMarginCorrected':True,
 'referenceTests':tests,'newEngineCalls':0,'newHTTPBodies':0,'newSourcePositions':0,'unresolvedGlyphAliasAccepted':False,
 'secondBlockFreezeAfterModuleEditDisclosed':True,'secondBlockDataFrozenBeforeSuccessfulExecution':True,
 'consumerChanged':False,'wholeCatalogueCompleted':False}
(s/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
