from pathlib import Path
import json
from pypdf import PdfReader

root = Path(__file__).resolve().parent.parent
out = root / 'qa/bazi-relation-locations'
pages = [(p.extract_text() or '') for p in PdfReader(out / 'bazi-relation-locations.pdf').pages]
text = '\n'.join(pages)
baseline = json.loads((out / 'BEFORE_EXPORT.json').read_text(encoding='utf8'))
result = {
    'pages': len(pages),
    'hasVisiblePositions': 'Can lộ' in text,
    'hasHiddenPositions': 'Trong tàng can' in text,
    'hasKnownInterpretation': ''.join(baseline['phrase'].split()) in ''.join(text.split()),
    'hasLocations': 'Can năm:' in text and 'Chi tháng ' in text,
    'sourceResearchHidden': all(s not in text for s in ['SOURCE_AUDIT', 'KR3g0042', 'MANUAL_READINGS']),
    'formAndHeroHidden': 'Xem Bát tự' not in text and 'Ngày sinh dương lịch' not in text,
    'cycleHeadingSharesPageWithBody': any('Nguyệt lệnh và đại vận' in s and 'bản khí' in s[s.index('Nguyệt lệnh và đại vận'):] for s in pages),
    'pageCharacters': [len(s) for s in pages],
}
assert result['pages'] == 7
assert all(v for k, v in result.items() if k not in ['pages', 'pageCharacters']), result
(out / 'PDF_RESULTS.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
print(json.dumps(result, ensure_ascii=False))
