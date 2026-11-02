from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parent.parent
sha=lambda b:hashlib.sha256(b).hexdigest()
folder=root/'research/month-boundaries'
s=json.loads((folder/'VERIFICATION.json').read_text(encoding='utf-8'))
assert len(s['checks'])==7 and all(x['ok'] for x in s['checks'])
for f in s['sources']:
 b=(root.parent/f['file']).read_bytes();assert len(b)==f['bytes'] and sha(b)==f['sha256']
print('PASS Seven new audit checks and all 200 original source body hashes')
a=json.loads((folder/'before.json').read_text(encoding='utf-8'))
assert a['summary']=={'years':200,'intervals':2472,'matching':2464,'differences':8,'unguarded':0,'missing':0}
assert all(not x['available'] and 'xác nhận lịch' in x['reason'] for x in a['differences'])
print('PASS All eight HKO month-boundary differences remain unavailable for navigation')
snapshot=root.parent/'archives/v53-before-month-boundary-audit'
for f in json.loads((snapshot/'PRESERVED.json').read_text(encoding='utf-8')):
 p=root.parent/f['unchangedWorkspaceFile'] if 'unchangedWorkspaceFile' in f else snapshot/f['file']
 b=p.read_bytes();assert len(b)==f['bytes'] and sha(b)==f['sha256'],str(p)
print('PASS Previous source/manifest preserved; all three HTML copies and consumer ZIP byte-identical')
