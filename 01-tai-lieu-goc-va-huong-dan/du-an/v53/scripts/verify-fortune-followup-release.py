from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parent.parent
for name,count in [('witness-tests.json',8),('conventions-browser-tests.json',12)]:
 s=json.loads((root/'qa/fortune-followup'/name).read_text(encoding='utf-8'))
 assert len(s['checks'])==count and all(x['ok'] for x in s['checks'])
print('PASS All 20 new source/runtime/convention checks remain successful')
snapshot=root.parent/'archives/v53-four-items-completed'
for f in json.loads((snapshot/'PRESERVED.json').read_text(encoding='utf-8')):
 body=(snapshot/f['file']).read_bytes()
 assert len(body)==f['bytes'] and hashlib.sha256(body).hexdigest()==f['sha256']
print('PASS The completed four-item HTML, manifest and both ZIP archives remain intact')
html=(root/'Huyen_Hoc_Cac.html').read_text(encoding='utf-8')
assert 'fortune-conventions' in html and 'WITNESS_AUDIT' not in html and '庚日武同相為首' not in html
print('PASS Public HTML contains the new result labels without private witness data')
