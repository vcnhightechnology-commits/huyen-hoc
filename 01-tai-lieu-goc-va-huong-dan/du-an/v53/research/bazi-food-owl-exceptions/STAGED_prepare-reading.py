from pathlib import Path
from hashlib import sha256
import json
from PIL import Image
b=Path(__file__).resolve().parent;w=b.parents[1]
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
save=lambda name,o:(b/name).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
corpus=w/'v53/research/bazi-food-source/CONTEXTS.json';context=next(x for x in read(corpus)['records']if x['id']=='FOOD-00-C15')
save('RETAINED_CONTEXT.json',dict(date='2026-10-28',file=corpus.relative_to(w).as_posix(),sha256=sha256(corpus.read_bytes()).hexdigest(),context=context,notNewHTTPOrWitness=True))
rows=[]
for page in [175,176]:
 p=w/f'v53/research/bazi-food-source/p{page}.png';rows.append(dict(sourceContainerPage=page,file=p.relative_to(w).as_posix(),sha256=sha256(p.read_bytes()).hexdigest(),actuallyViewed=True,newSourceReadPosition=False,scope='Expanded context of C15owl exceptions and subsequent prose; not all glyphs collated.'))
save('RAW_REVIEW.json',dict(date='2026-10-28',records=rows,newSourcePositions=0))
specs=[(175,'p175-exceptions-native.png',[350,300,1610,2860]),(176,'p176-exceptions-close-native.png',[1050,270,2120,2600])]
qa=[]
for page,name,box in specs:
 src=w/f'v53/research/bazi-food-source/p{page}.png';out=b/name;Image.open(src).crop(box).save(out)
 qa.append(dict(sourceFile=src.relative_to(w).as_posix(),file=name,cropBox=box,sha256=sha256(out.read_bytes()).hexdigest(),resampled=False,actuallyViewed=False))
save('QA_IMAGES.json',dict(date='2026-10-28',records=qa))
save('WORK_STATE.json',dict(date='2026-10-28',status='C15expanded2retainedimages-read-crops-awaiting-QA-no-rules-promoted',catalogueID='M01',sourceDirectory='tmp/bazi-food-owl-exceptions-staging',
 sourceParentContext='FOOD-00-C15',sourceImagePositions=[175,176],newHTTPRequests=0,newSourcePositions=0,consumerChanged=False,wholeCatalogueCompleted=False,
 unresolved=['Role/anchor of 己亥,丙午,乙巳,癸巳 examples and their stated exceptions must be explicit; do not assume a whole natal chart.',
 'Compare exact 己/巳/壬andotherglyphs in relevant crops before asserting typed literal matching.',
 '合化claimedbyprose does not mean any visible pair has effective transformation; preserve named textual premise and unknown conditions.',
 'FixedFood/IndirectSealrelations are distinct from source不畏/不倒食 rhetoric; noefficacyoroutcomeinference.'],
 next=['View native crops and transcribe selected exception clauses with exact source offsets and correction audit.', 'Only after premise scope is clear, implement complete bounded clauses, execute actual relation/engine comparisons if used, and preserve unknowns.', 'Latest packaged scope is month-command; confirm final4596file verification in PENDING before promotion.']))
print('PreparedC15retainedcontext/2expandedimages/2cropsawaitingvisualQA;noimplementedexceptionclaims')
