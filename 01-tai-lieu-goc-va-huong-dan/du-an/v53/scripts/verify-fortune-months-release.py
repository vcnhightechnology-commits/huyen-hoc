from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parent.parent
files=[('qa/fortune-months/engine-tests.json',13),('qa/fortune-months/browser-tests.json',22),('qa/fortune-months/print-tests.json',2),('qa/four-items/browser-tests.json',47),('qa/test-results.json',50),('qa/home-guide/test-results.json',40)]
total=0
for name,count in files:
 s=json.loads((root/name).read_text(encoding='utf-8'));assert len(s['checks'])==count and all(x['ok'] for x in s['checks']),name;total+=count
assert total==174
print('PASS Six current month-view and regression reports account for 174 passing checks')
snapshot=root.parent/'archives/v53-before-fortune-months'
for f in json.loads((snapshot/'PRESERVED.json').read_text(encoding='utf-8')):
 b=(snapshot/f['file']).read_bytes();assert len(b)==f['bytes'] and hashlib.sha256(b).hexdigest()==f['sha256']
print('PASS Four prior release artifacts remain byte-identical in the preserved snapshot')
source=root/'research/fortune-table'
s=json.loads((source/'REQUESTS.json').read_text(encoding='utf-8'))
assert len(s['records'])==6
for f in s['records']:
 b=(source/f['file']).read_bytes();assert len(b)==f['bytes'] and hashlib.sha256(b).hexdigest()==f['sha256'] and f['status']==200 and f['tls']['authorized']
print('PASS Six new official image responses retain their recorded bytes and hashes')
html=(root/'Huyen_Hoc_Cac.html').read_text(encoding='utf-8')
assert 'HHC_FORTUNE_MONTHS' in html and 'DIAGRAM_AUDIT' not in html and 'official-088' not in html
print('PASS Consumer HTML contains the month function and excludes the private diagram evidence')
