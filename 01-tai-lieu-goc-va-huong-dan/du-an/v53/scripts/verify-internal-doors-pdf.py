from pathlib import Path
from pypdf import PdfReader
import json, hashlib

root = Path(__file__).resolve().parent.parent
qa = root / 'qa/internal-doors'
pdf = qa / 'internal-doors.pdf'
pages = [p.extract_text() or '' for p in PdfReader(pdf).pages]
compact = lambda s: ''.join(s.split())
text = compact('\n'.join(pages))
result = {
    'pages': len(pages),
    'roomPairs': all(compact(x) in text for x in ['Phòng khách ↔ Phòng ngủ 1', 'Phòng ngủ 1 ↔ Góc làm việc']),
    'bothDoorLabels': all(compact(x) in text for x in ['N1. Cửa phòng ngủ', 'N2. Cửa góc làm việc']),
    'exactDoorEndpoints': all(compact(x) in text for x in ['(5; 1) → (5; 2)', '(6; 4) → (7; 4)']),
    'areaAndExteriorDirection': all(compact(x) in text for x in ['Khung 80 m²', 'Cửa chính', '180° · Nam']),
    'doorGroupNotSplit': any(all(compact(x) in compact(p) for x in ['Cửa thông giữa các phòng', 'N1. Cửa phòng ngủ', 'N2. Cửa góc làm việc']) for p in pages),
    'editingControlsHidden': all(compact(x) not in text for x in ['Phòng thứ nhất', 'Phòng thứ hai', '+ Thêm cửa nội bộ', 'Bắt đầu trên đoạn chung (m)']),
    'researchHidden': all(x not in text for x in ['CADAL', 'SHA-256', 'SPECIFICATION.md', 'SOURCE_RESULTS']),
    'pageCharacters': [len(p) for p in pages],
    'pdfSHA256': hashlib.sha256(pdf.read_bytes()).hexdigest()
}
assert result['pages'] == 3
assert all(v for k, v in result.items() if k not in ['pages', 'pageCharacters', 'pdfSHA256'])
(qa / 'PDF_RESULTS.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf8')
print(json.dumps(result, ensure_ascii=False))
