from pathlib import Path
from hashlib import sha256
import json
from PIL import Image

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/home-tomb-diagrams';q=r/'qa/home-tomb-diagrams'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
m=read(b/'SOURCE_MANIFEST.json');table=read(b/'DIAGRAM_TABLES.json')
assert sha(w/m['sourceContainer'])==m['sourceSHA256']
native=read(b/'CROPS.json')['records'];rotations=0
for x in native:
 assert sha(w/x['source'])==x['sourceSHA256']and sha(b/x['crop'])==x['cropSHA256']
 source=Image.open(w/x['source']).convert('RGB');crop=Image.open(b/x['crop']).convert('RGB');assert source.crop(x['box']).tobytes()==crop.tobytes()
 for a in x['rotations']:
  p=b/a['file'];mode={90:Image.Transpose.ROTATE_90,180:Image.Transpose.ROTATE_180,270:Image.Transpose.ROTATE_270}[a['angleCCW']]
  assert sha(p)==a['sha256']and Image.open(p).convert('RGB').tobytes()==crop.transpose(mode).tobytes();rotations+=1
metadata=['SECTOR_CROPS.json','DETAIL_CROP.json','DETAIL49_CROP.json','DETAIL_FIRE_CROP.json','DETAIL_WOOD_CROP.json','DETAIL_LEFT_CROPS.json']
crops=0
for name in metadata:
 d=read(b/name);records=d['records']if'records'in d else[d]
 for x in records:
  assert sha(b/x['parent'])==x['parentSHA256']and sha(b/x['file'])==x['sha256']
  assert Image.open(b/x['parent']).convert('RGB').crop(x['box']).tobytes()==Image.open(b/x['file']).convert('RGB').tobytes();crops+=1
for x in m['additionalProsePages']:assert sha(w/x['file'])==x['sha256']
assert len(table['rows'])==20 and sum(len(x['sourceYearPillars49'])for x in table['rows'])==50
assert len(table['transcriptionCorrections'])==4
for x in table['transcriptionCorrections']:assert(b/x['evidence']).exists()and x['notASourceEmendation']
assert sum(x['monthReadingResolved']for x in table['rows'])==19
unclear=[x for x in table['rows']if not x['monthReadingResolved']];assert len(unclear)==1 and unclear[0]['id']=='water-earth-丙辛'
assert unclear[0]['sourceMonthOrdinals49']is None and unclear[0]['monthReadingAlternatives']==[[12],[11,12]]
assert len(native)==2 and rotations==6 and crops==14
out={'date':'2026-10-28','retainedSourceContainerVerified':1,'nativeSourceImageHashesVerified':5,'exactNativeDiagramCrops':2,'losslessRotationsVerified':6,
 'nativeSectorCropsVerified':8,'nativeDetailCropsVerified':6,'totalQADerivativesVerified':22,'sourceMovementRows':20,'sourceYearEntries':50,'resolvedMonthSets':19,'unresolvedMonthSets':1,
 'targetedWorkingTranscriptionCorrections':4,'newHTTPRequests':0,'newOriginalContainers':0,'newSourcePages':0,'expandedPreviouslyReadPages':5,
 'allSourceImageCharactersDiplomaticallyTranscribed':False,'sourceEmended':False,'practicalOutcomesValidated':False,'wholeCatalogueCompleted':False}
(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,ensure_ascii=False))
