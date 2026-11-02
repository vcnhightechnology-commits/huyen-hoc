from pathlib import Path
import json,re
from pypdf import PdfReader
root=Path(__file__).resolve().parent.parent
out=root/'qa/fortune-months'
pdf=PdfReader(out/'year-reading-print.pdf')
texts=[page.extract_text() or '' for page in pdf.pages]
text=re.sub(r'\s+',' ',' '.join(texts))
checks=[{'name':'Real browser PDF contains all twelve month labels and both leap-six reading intervals','ok':all(f'Tháng {m}' in text for m in range(1,13)) and 'Tháng 6 nhuận · ngày 1–15' in text and 'Tháng 6 nhuận · ngày 16–29' in text},{'name':'Real browser PDF retains selected date and chosen leap-month convention','ok':'9/8/2025' in text and 'Từ ngày 16 dùng tháng kế tiếp' in text}]
result={'pages':len(pdf.pages),'checks':checks,'monthOverviewPageNumbers':[i+1 for i,t in enumerate(texts) if 'Các tháng trong năm' in t or 'Tháng 6 nhuận' in t]}
(out/'print-tests.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for c in checks:print('PASS' if c['ok'] else 'FAIL',c['name'])
print(json.dumps({'pages':result['pages'],'overviewPages':result['monthOverviewPageNumbers']}))
assert all(x['ok'] for x in checks)
