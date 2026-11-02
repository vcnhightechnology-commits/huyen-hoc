from pathlib import Path
from hashlib import sha256
from pypdf import PdfReader
import json,subprocess

qa=Path(__file__).resolve().parent.parent/'qa/meihua-methods'
pdf=qa/'historical-tones.pdf'
old={n:sha256((qa/f'print-{n}.png').read_bytes()).hexdigest()for n in range(1,5)}
poppler=Path('C:/Users/Administrator.DESKTOP-98TGIBL/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe')
subprocess.run([str(poppler),'-scale-to','1400','-png',str(pdf),str(qa/'print')],check=True,capture_output=True)
pages=[p.extract_text()or''for p in PdfReader(pdf).pages]
compact=lambda s:''.join(s.split()).casefold()
text=compact('\n'.join(pages))
r={'pages':len(pages),'explicitToneOrder':compact('Bình, Nhập, Khứ, Khứ, Bình, Bình')in text,'noHourConventionVisible':compact('không cộng giờ')in text,'bodyUseMutualAndChanged':all(compact(s)in text for s in['Thể · Khôn','Dụng · Tốn','Lôi Trạch Quy Muội','Địa Thiên Thái']),'sixPositions':all(compact('Hào '+str(n))in text for n in range(1,7)),'inputControlsHidden':all(compact(s)not in text for s in['Số âm cổ từng chữ, theo thứ tự','Điền thời điểm hiện tại','Số trượng','Số cộng thêm']),'researchHidden':all(s not in text for s in['wikisource','nlc416','sha-256','manual_readings']),'pageCharacters':[len(p)for p in pages],'pdfSHA256':sha256(pdf.read_bytes()).hexdigest(),'renderedPages':[{'page':n,'sha256':sha256((qa/f'print-{n}.png').read_bytes()).hexdigest()}for n in range(1,len(pages)+1)],'visuallyReviewedPages':[1,2,3,4]}
assert r['pages']==4
assert all(r[k]for k in['explicitToneOrder','noHourConventionVisible','bodyUseMutualAndChanged','sixPositions','inputControlsHidden','researchHidden'])
assert all(p['sha256']==old[p['page']]for p in r['renderedPages'])
r['finalRenderMatchesVisuallyReviewedPNGs']=True
(qa/'PDF_RESULTS.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(r,ensure_ascii=False))
