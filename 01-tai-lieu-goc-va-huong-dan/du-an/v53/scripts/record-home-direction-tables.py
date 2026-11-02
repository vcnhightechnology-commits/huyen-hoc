from pathlib import Path
from hashlib import sha256
import json, shutil

r=Path(__file__).resolve().parent.parent
w=r.parent
s=w/'tmp/home-direction-tables-staging'
b=r/'research/home-direction-tables'
q=r/'qa/home-direction-tables'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
assert len(read(w/'archives/v53-before-home-direction-tables/PACKAGE_MANIFEST.json')['files'])==3164
b.mkdir(exist_ok=False);q.mkdir(exist_ok=False)
d=read(s/'NEXT_DIRECTION_TABLES_DRAFT.json')
d['status']='direct-source-coordinate-tables-compiled-private'
d['sourceInstructionsAreData']=True
d['historicalCitationIndependentlyVerified']=False
for file,box,page in[('p054-right-column.png',[1750,300,2000,2860],54),('p056-quoted-conditions.png',[370,330,1460,2820],56)]:
 d['qaDerivatives'].append({'file':file,'sourcePage':page,'cropBox':box,'rotation':0,'sha256':sha256((s/file).read_bytes()).hexdigest()})
for x in d['qaDerivatives']:shutil.copy2(s/x['file'],b/x['file'])
(b/'SOURCE_TABLES.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
module=(s/'direction-reference.mjs').read_text(encoding='utf-8').replace('// Staged private prototype; not imported by the user website or current release.','// Private named geographical source tables; no date, room or forecast adapter.').replace('NEXT_DIRECTION_TABLES_DRAFT.json','SOURCE_TABLES.json')
(b/'direction-reference.mjs').write_text(module,encoding='utf-8')
shutil.copy2(s/'NEXT_RUNTIME_PROBE.json',b/'PRIOR_STAGED_PROBE.json')
print('Recorded24 term rows,24 geographical coordinates,24 glyphs,8 prose segments and10 native QA derivatives.')
