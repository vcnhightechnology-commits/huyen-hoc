from pathlib import Path
from hashlib import sha256
from pypdf import PdfReader
import json
qa=Path(__file__).resolve().parent.parent/'qa/meihua-layers'
pdf=qa/'body-use-layers.pdf';pages=[p.extract_text()or''for p in PdfReader(pdf).pages]
compact=lambda s:''.join(s.split()).casefold()
text=compact('\n'.join(pages))
r={'pages':len(pages),
 'explicitInputSummary':all(compact(s)in text for s in ['Năm Dần','tháng12','ngày1âm lịch','giờ Ngọ','cộng thêm4']),
 'fourLayerLabels':all(compact(s)in text for s in ['Điểm đang xét','Lớp hỗ · cùng phía Thể','Lớp hỗ · cùng phía Dụng','Sau khi đổi hào']),
 'mixedRelationsSeparate':all(compact(s)in text for s in ['Thể sinh Dụng','Hỗ phía Thể khắc Thể','Hỗ phía Dụng đồng hành với Thể','Dụng sau đổi hào đồng hành với Thể']),
 'mutualRolesVisible':all(compact(s)in text for s in ['Phía Thể:Đoài · Kim','Phía Dụng:Tốn · Mộc']),
 'sixReflectionPositions':all(compact('Hào '+str(n))in text for n in range(1,7)),
 'inputAndToastHidden':all(compact(s)not in text for s in ['Cách lấy số','Điền thời điểm hiện tại','Số cộng thêm','Đã lưu trên thiết bị này','Hồ sơ của tôi']),
 'researchHidden':all(s not in text for s in ['wikisource','nlc416','sha-256','manual_readings','conditions-reference']),
 'cardContentsTogether':all(any(all(compact(s)in compact(page)for s in group)for page in pages)for group in [
  ['Điểm đang xét','Thể sinh Dụng','Cân mức đóng góp'],['Lớp hỗ · cùng phía Thể','Hỗ phía Thể khắc Thể','Khi gặp lực cản'],
  ['Lớp hỗ · cùng phía Dụng','Hỗ phía Dụng đồng hành với Thể','Tìm điểm chung'],['Sau khi đổi hào','Dụng sau đổi hào đồng hành với Thể','Tìm điểm chung']]),
 'pageCharacters':[len(p)for p in pages],'pdfSHA256':sha256(pdf.read_bytes()).hexdigest(),
 'renderedPages':[{'page':n,'sha256':sha256((qa/f'print-{n}.png').read_bytes()).hexdigest()}for n in range(1,len(pages)+1)],
 'visuallyReviewedPages':[1,2,3,4],
 'visualReview':'Viewedallfourcurrentprint-mediaPNGs:legible,no clippedtext,eachlayercard intact,all sixpositions present,forms/hero/toast hidden. Layercontainer spanspages1–2at rowboundary.390/1440px layer/context screenshotsalsoinspected.'}
assert r['pages']==4
assert all(r[k]for k in ['explicitInputSummary','fourLayerLabels','mixedRelationsSeparate','mutualRolesVisible','sixReflectionPositions','inputAndToastHidden','researchHidden','cardContentsTogether'])
(qa/'PDF_RESULTS.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(r,ensure_ascii=False))
