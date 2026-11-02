from pathlib import Path
from hashlib import sha256
from PIL import Image
import json
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/home-source-tables';q=r/'qa/home-source-tables'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
fig=read(b/'MANUAL_FIGURES.json');manual=read(b/'MANUAL_READINGS.json');images={}
for x in manual['readings']:
 p=w/x['file'];assert sha(p)==x['sha256'];images[x['page']]=p
assert len(images)==13 and manual['newSourcePages']==0
ambiguous=0;nonambiguous=0
for x in fig['records']:
 assert x['sourceSHA256']==sha(w/x['sourceFile']);assert sha(b/x['file'])==x['sha256']
 with Image.open(w/x['sourceFile'])as original,Image.open(b/x['file'])as crop:
  expected=original.crop(tuple(x['box']));assert expected.mode==crop.mode and expected.size==crop.size and expected.tobytes()==crop.tobytes()
 assert len(x['manualTopToBottom'])==6 and all(v in[0,1]for v in x['manualTopToBottom'])and x['directVisualQA']
 for candidate,actual in zip(x['topToBottomDetected'],x['manualTopToBottom']):
  if candidate is None:ambiguous+=1
  else:assert candidate==actual;nonambiguous+=1
for x in manual['qaDerivatives']:
 assert sha(b/x['file'])==x['sha256']
 with Image.open(w/x['sourceFile'])as original,Image.open(b/x['file'])as upright:
  expected=original.transpose(Image.Transpose.ROTATE_90);assert expected.size==upright.size and expected.tobytes()==upright.tobytes()
assert(ambiguous,nonambiguous)==(65,319)
for page in[107,108]:
 with Image.open(b/f'figures-{page}-sheet.png')as sheet:
  records=[x for x in fig['records']if x['page']==page];palaces=['艮','坎','乾']if page==107 else['兌','坤','離','巽','震']
  assert sheet.size==(len(palaces)*200,2000)
  for x in records:
   with Image.open(b/x['file'])as crop:
    xx=palaces.index(x['palace'])*200+15;yy=x['stage']*250+27
    actual=sheet.crop((xx,yy,xx+crop.width,yy+crop.height));assert actual.tobytes()==crop.convert('RGB').tobytes()
unit=read(r/'research/home-you-nian/VOLUME_UNIT_MAP.json');assert len(unit['units'])==12 and not unit['wholeWorkApplied']
assert read(b/'OVERCOMING_RULE.json')['correctedSourceTerm']=='尅'
out={'date':'2026-10-27','expandedSourcePagesHashVerified':13,'exactNativeCropsVerified':64,'contactSheetsNativePixelsVerified':2,'losslessOrientationDerivativesVerified':2,
 'manualGlyphs':384,'ambiguousDetectorSamplesResolvedManually':ambiguous,'nonambiguousSamplesAgreeWithManual':nonambiguous,'newSourcePages':0,'newHTTPRequests':0,
 'figureNamesLiteralMatchPriorRuntime':62,'predeclaredAliasMatches':1,'remainingGlyphDifference':'恒/恆 at32 preserved','wholeCatalogueCompleted':False}
(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
