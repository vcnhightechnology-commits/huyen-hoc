from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json
b=Path(__file__).resolve().parent;w=b.parents[1]
# Independent visual entry from the twelve native GJTS crops already retained.
# Each compact cell: element/label/star/height; ? is unread/uncertain, - is a visibly unlabelled field.
manual={
82:'水/六煞/文曲/低 木/生氣/貪狼/高 火/五鬼/廉貞/小 土/天乙/巨門/高 金/延年/武曲/高',
83:'金/-/-/中 水/六煞/文曲/低 木/生氣/貪狼/高 火/五鬼/廉貞/低 土/天乙/巨門/高 金/延年/武曲/高',
84:'木/六煞/文曲/低 木/生氣/貪狼/高 火/五鬼/廉貞/小 土/天乙/巨門/高 金/延年/武曲/高 木/六煞/文曲/低',
85:'金/-/-/中 水/六煞/文曲/低 木/生氣/貪狼/高 火/五鬼/廉貞/低 土/天乙/巨門/高 金/延年/武曲/高',
86:'土/天乙/巨門/高 金/延年/武曲/高 ?/六煞/文曲/低 木/生氣/貪狼/高 火/五鬼/廉貞/小',
87:'金/-/-/中 ?/六煞/文曲/低 木/生氣/貪狼/高 火/五鬼/廉貞/低 土/天乙/巨門/高 金/延年/武曲/高',
88:'金/-/-/高 水/六煞/文曲/低 木/生氣/貪狼/高大 火/五鬼/廉貞/低 土/天乙/巨門/高 金/延年/武曲/高',
89:'土/天乙/巨門/高 金/延年/武曲/高 ?/六煞/文曲/低 木/生氣/貪狼/高 火/五鬼/廉貞/小 土/天乙/巨門/高',
90:'?/六煞/文曲/低 木/生氣/貪狼/高 火/五鬼/廉貞/低 土/天乙/巨門/高 金/延年/武曲/高 ?/六煞/文曲/低',
91:'火/五鬼/廉貞/低 土/天乙/巨門/高 金/延年/武曲/高 水/六煞/文曲/低 木/生氣/貪狼/高 火/五鬼/廉貞/低',
92:'木/生氣/貪狼/高 火/五鬼/廉貞/低 土/天乙/巨門/高 金/延年/武曲/高 水/六煞/文曲/低',
93:'金/延年/武曲/高 水/六煞/文曲/低 木/生氣/貪狼/高 火/五鬼/廉貞/低 土/天乙/巨門/高 金/延年/武曲/高'}
sourcePages={82:86,83:86,84:87,85:87,86:87,87:87,88:88,89:88,90:88,91:88,92:88,93:89}
rows=[]
for case,text in manual.items():
 for ordinal,cell in enumerate(text.split(),1):
  parts=cell.split('/');fields=['sourceElement','sourceLabel','sourceStar','sourceSizeHeightWord']
  row=dict(caseID=f'YZSS-C{case}',ordinal=ordinal,sourceDjvuPage=sourcePages[case],sourceCrop=f'v53/qa/home-yangzhai-courtyards/gjts-case{case}-native.png')
  row.update({key:None if value in ['?','-']else value for key,value in zip(fields,parts)})
  row['blankFields']=[key for key,value in zip(fields,parts)if value=='-'];row['uncertainFields']=[key for key,value in zip(fields,parts)if value=='?']
  if row['uncertainFields']:row['uncertaintyReason']='Faint or 木/水-like strokes in this repository scan; do not resolve from 文曲 or a cycle.'
  rows.append(row)
assert len(rows)==69
prior=json.loads((w/'v53/research/home-yangzhai-courtyards/MANUAL_DIAGRAM_CELLS.json').read_text(encoding='utf-8-sig'))
original={(d['id'],c['ordinal']):c for d in prior['records']for c in d['printedLayerCells']}
for row in rows:
 target=original[row['caseID'],row['ordinal']]
 row['resolvedFieldsMatchOtherLiteral']={field:row[field]==target[field]for field in fields if field not in row['uncertainFields']}
 row['allFourFieldsMatchEstablished']=not row['uncertainFields']and all(row['resolvedFieldsMatchOtherLiteral'].values())
assert sum(x['allFourFieldsMatchEstablished']for x in rows)==64
assert all(all(x['resolvedFieldsMatchOtherLiteral'].values())for x in rows)
assert [(x['caseID'],x['ordinal'])for x in rows if x['uncertainFields']]==[('YZSS-C86',3),('YZSS-C87',2),('YZSS-C89',3),('YZSS-C90',1),('YZSS-C90',6)]
out=dict(date='2026-10-28',entryMethod='Manual native-crop entry before comparison; no expected values generated from another witness or cycle.',records=rows,
 allNumberedCellsHaveAnExplicitReviewDisposition=True,numberedCells=69,fullyResolvedFourFieldMatches=64,partialCells=5,
 all69FullyTranscribedOrMatched=False,independentExemplarEstablished=False,consumerChanged=False,actualEngineCalls=0)
(b/'MANUAL_WITNESS_CELLS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
qa=json.loads((b/'QA_IMAGES.json').read_text(encoding='utf-8-sig'))
for x in qa['records']:
 src=w/x['sourceFile'];p=b/x['file'];assert sha256(p.read_bytes()).hexdigest()==x['sha256']
 assert ImageChops.difference(Image.open(src).convert('RGB').crop(x['cropBox']),Image.open(p).convert('RGB')).getbbox()is None
 x['actuallyViewed']=True
(b/'QA_IMAGES.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
state=dict(date='2026-10-28',status='all69witness-cells-reviewed64fullymatched5partial-awaiting-promotion',sourceDirectory='tmp/home-courtyard-collation-staging',
 sourceDjvuRetained='v53/research/home-yangzhai-courtyards/Gujin-Tushu-Jicheng-Volume476.djvu',
 sourceDjvuPositions=[86,87,88,89],newSourcePositions=0,newHTTPRequests=0,consumerChanged=False,wholeCatalogueCompleted=False,
 numberedCellsReviewed=69,fullyResolvedMatches=64,partialElementReadings=5,newIsolatedNativeCropsViewedPixelMatched=7,
 next=['Preserve5uncertainelementcells; no formula filling or automatic edit to Tianyige source.',
 'Promote explicit64match/5partial disposition without calling all69fullycollated; source efficacy/moderngeometry still unvalidated.',
 'Continue named context and full prose/side-palace rules, or independent domain if source premise remains open.'])
(b/'WORK_STATE.json').write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(numberedCellsReviewed=69,fullyResolvedMatches=64,partialElements=5,nativeCropsVerified=7,newEngineCalls=0)))
