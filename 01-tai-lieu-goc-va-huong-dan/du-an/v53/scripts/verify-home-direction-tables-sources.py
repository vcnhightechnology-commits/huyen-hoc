from pathlib import Path
from hashlib import sha256
import json
from PIL import Image

r=Path(__file__).resolve().parent.parent
w=r.parent
b=r/'research/home-direction-tables'
d=json.loads((b/'SOURCE_TABLES.json').read_text(encoding='utf-8'))
assert sha256((w/d['sourceContainer']).read_bytes()).hexdigest()==d['sourceSHA256']
for x in d['readings']:assert sha256((w/x['file']).read_bytes()).hexdigest()==x['sha256']
crops=rotations=0
for x in d['qaDerivatives']:
 expected=Image.open(w/f"v53/research/home-you-nian/images/p{x['sourcePage']:03}.png").crop(tuple(x['cropBox']))
 if x['rotation']:
  expected=expected.transpose(getattr(Image.Transpose,f"ROTATE_{x['rotation']}"));rotations+=1
 else:crops+=1
 actual=Image.open(b/x['file'])
 assert actual.mode==expected.mode and actual.size==expected.size and actual.tobytes()==expected.tobytes(),x['file']
 assert sha256((b/x['file']).read_bytes()).hexdigest()==x['sha256']
assert crops==4 and rotations==6
assert len(d['source24TermRows'])==24 and len(d['geographicalNaJiaRows'])==8 and len(d['nextSourceClauses'])==8
out={'date':'2026-10-27','sourceContainerSHA256':d['sourceSHA256'],'nativeImageHashesVerified':5,
 'nativeCropsVerified':crops,'losslessRotationsVerified':rotations,'termLabels':24,'termCoordinateLabels':24,
 'najiaCoordinates':24,'manualGlyphs':24,'contextualProseSegments':8,'newHTTPRequests':0,'newSourcePages':0,
 'expandedPreviouslyReadPages':5,'historicalCitationIndependentlyVerified':False,'wholeCatalogueCompleted':False}
(r/'qa/home-direction-tables/SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
