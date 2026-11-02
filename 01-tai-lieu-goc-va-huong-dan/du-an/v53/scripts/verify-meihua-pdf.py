from pathlib import Path
from pypdf import PdfReader
from hashlib import sha256
import json

qa=Path(__file__).resolve().parent.parent/'qa/meihua'
pdf=qa/'plum-reading.pdf'
pages=[p.extract_text() or '' for p in PdfReader(pdf).pages]
compact=lambda s: ''.join(s.split()).casefold()
text=compact('\n'.join(pages))
r={
 'pages':len(pages),
 'sourceComponentsVisible':all(compact(x) in text for x in ['Năm Thìn','tháng 12','ngày 17 âm lịch','giờ Thân']),
 'bodyUseMutualAndChangedVisible':all(compact(x) in text for x in ['Thể · Đoài','Dụng · Ly','Thiên Phong Cấu','Dụng khắc Thể','Dụng sinh Thể','Trạch Sơn Hàm']),
 'allSixPositionsVisible':all(compact('Hào '+str(i)) in text for i in range(1,7)),
 'inputAndResearchHidden':not any(compact(x) in text for x in ['Số lượng sự vật đã đếm','Điền thời điểm hiện tại','NLC416','Wikisource','SHA-256','MANUAL_READINGS']),
 'cardsTogether':any(all(compact(x) in compact(p) for x in ['Thể · Đoài','Dụng · Ly','Thiên Phong Cấu','Dụng khắc Thể'])for p in pages),
 'readingHeadingWithIntro':any(all(compact(x) in compact(p) for x in ['LỜI GỢI MỞ','Thay đổi · cải cách'])for p in pages),
 'pageCharacters':[len(p) for p in pages],
 'pdfSHA256':sha256(pdf.read_bytes()).hexdigest(),
 'visuallyReviewedPages':[1,2,3,4],
 'visualReview':'All four rendered pages viewed:legible,no clipping,trigram cards intact,reading heading remains with intro.390px source form/result screenshot also viewed.'
}
assert r['pages']==4
assert all(r[k]for k in ['sourceComponentsVisible','bodyUseMutualAndChangedVisible','allSixPositionsVisible','inputAndResearchHidden','cardsTogether','readingHeadingWithIntro'])
(qa/'PDF_RESULTS.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(r,ensure_ascii=False))
