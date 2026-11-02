from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parent.parent
sha=lambda b:hashlib.sha256(b).hexdigest()
s=json.loads((root/'research/library-current/TEST_RESULTS.json').read_text(encoding='utf-8'))
assert len(s['checks'])==17 and all(x['ok'] for x in s['checks'])
print('PASS All 17 current source-coverage and runtime inspection checks')
snapshot=root.parent/'archives/v53-before-current-library-audit'
for f in json.loads((snapshot/'PRESERVED.json').read_text(encoding='utf-8')):
 p=root.parent/f['unchangedWorkspaceFile'] if 'unchangedWorkspaceFile' in f else snapshot/f['file']
 b=p.read_bytes();assert len(b)==f['bytes'] and sha(b)==f['sha256'],str(p)
print('PASS Prior source and manifest preserved; all HTML copies and consumer ZIP unchanged')
html=(root/'Huyen_Hoc_Cac.html').read_text(encoding='utf-8')
assert 'library-current' not in html and 'LIBRARY_APPLICATION_STATUS' not in html
print('PASS Current source audit and book inventory remain outside the consumer product')
