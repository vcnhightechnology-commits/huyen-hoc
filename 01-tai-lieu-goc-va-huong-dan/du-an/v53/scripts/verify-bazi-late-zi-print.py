from pathlib import Path
from hashlib import sha256
import json
from pypdf import PdfReader
root=Path(__file__).resolve().parent.parent;qa=root/'qa/bazi-late-zi-option'
pdf=qa/'late-zi-option.pdf';pages=[p.extract_text() or '' for p in PdfReader(pdf).pages];text=''.join(''.join(pages).split())
result={'pages':len(pages),'policyVisible':'CangiờTýmuộn:theongàykếtiếp' in text,'dayAndHourVisible':'QuýDậu' in text and 'GiápTý' in text,'visibleLocationsRetained':'Cangiờ:Giáp' in text,'relationsExpanded':'Gợiquytắc,tráchnhiệm' in text,'noResearchLeak':all(s not in text for s in ['NCL-000002203','MANUAL_READINGS','袁樹珊']),'formHidden':'XemBáttự' not in text and 'Điềnmộtchútvềbạn' not in text,'pageCharacters':[len(p) for p in pages],'pdfSHA256':sha256(pdf.read_bytes()).hexdigest()}
assert all(v for k,v in result.items() if k not in ['pages','pageCharacters','pdfSHA256']),result
(qa/'PDF_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print(json.dumps(result,ensure_ascii=False))
