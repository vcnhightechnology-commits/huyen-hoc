from pathlib import Path
from hashlib import sha256
import json
from pypdf import PdfReader
qa=Path(__file__).resolve().parent.parent/'qa/bazi-month-stems';pdf=qa/'month-stems.pdf';pages=[p.extract_text() or '' for p in PdfReader(pdf).pages];text=''.join(''.join(pages).split())
result={'pages':len(pages),'monthDetailVisible':'XemđủcáccantrongthángTỵ' in text,'mainAndSecondaryVisible':'Bính·bảnkhí' in text and 'Canh·cantàngkhác' in text and 'Mậu·cantàngkhác' in text,'officialRelationVisible':'ChínhQuan' in text,'positionLabelsVisible':'Vịtrícantộ' in text or 'Vịtrícanlộ' in text,'noResearchLeak':all(s not in text for s in ['CADAL06066041','KR3g0042','MANUAL_READINGS']),'formHidden':'XemBáttự' not in text and 'Điềnmộtchútvềbạn' not in text,'pageCharacters':[len(p) for p in pages],'pdfSHA256':sha256(pdf.read_bytes()).hexdigest()}
assert all(v for k,v in result.items() if k not in ['pages','pageCharacters','pdfSHA256']),result
(qa/'PDF_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print(json.dumps(result,ensure_ascii=False))
