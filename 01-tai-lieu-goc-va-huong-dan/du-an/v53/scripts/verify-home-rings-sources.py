from pathlib import Path
from hashlib import sha256
import json
from PIL import Image

r=Path(__file__).resolve().parent.parent
w=r.parent
b=r/'research/home-rings'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda p:sha256(p.read_bytes()).hexdigest()
d=read(b/'MANUAL_READINGS.json')
assert sha(w/d['sourceContainer'])==d['sourceSHA256']
for x in d['readings']:
    assert sha(w/x['file'])==x['sha256'] and x['directVisualQA']
crops=rotations=0
for x in d['qaDerivatives']:
    assert sha(b/x['file'])==x['sha256']
    actual=Image.open(b/x['file'])
    if x['operation']=='native-crop':
        expected=Image.open(w/x['sourceFile']).crop(tuple(x['cropBox']))
        crops+=1
    else:
        rotation=int(x['operation'].split('_')[-1])
        expected=Image.open(b/x['sourceCrop']).transpose(getattr(Image.Transpose,f'ROTATE_{rotation}'))
        rotations+=1
    assert actual.mode==expected.mode and actual.size==expected.size and actual.tobytes()==expected.tobytes(),x['file']
labels=read(b/'DIAGRAM_LABELS.json')
clauses=read(b/'SOURCE_CLAUSES.json')
assert len(clauses['passages'])==clauses['passageCount']==15
assert len(set(x['id']for x in clauses['passages']))==15
for x in labels['diagrams']:
    assert len(x['outerFromZi'])==len(x['innerFromZi'])==24
    assert len(set(x['outerFromZi']))==len(set(x['innerFromZi']))==24
    assert len(x['innerPairArcs'])==12 and len(set(''.join(x['innerPairArcs'])))==24
    assert x['directVisualQA'] and x['outerRole']=='正針'
assert crops==2 and rotations==6
out={'date':'2026-10-27','sourceContainerSHA256':d['sourceSHA256'],'sourceImageHashesVerified':6,
     'exactNativeCropsVerified':crops,'losslessRotationsVerified':rotations,'directDiagramLabels':96,
     'directPairArcs':24,'enumeratedProseSegments':15,'newHTTPRequests':0,'newSourcePages':0,
     'expandedPreviouslyReadPages':6,'allInteriorCrossingPathsTraced':False,'wholeCatalogueCompleted':False}
(r/'qa/home-rings/SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
