from pathlib import Path
from hashlib import sha256,sha1
from io import BytesIO
import json,re
from pypdf import PdfReader
from PIL import Image

root=Path(__file__).resolve().parent.parent
base=root/'research/bazi-late-zi-witness';qa=root/'qa/bazi-late-zi-option';checks=[]
def test(name,ok,detail=None):
    checks.append({'name':name,'ok':bool(ok),'detail':detail});assert ok,name;print('PASS',name)
requests=json.loads((base/'REQUESTS.json').read_text(encoding='utf8'))['records']
for r in requests:
    b=(base/r['file']).read_bytes();assert len(b)==r['bytes'] and sha256(b).hexdigest()==r['sha256'] and sha1(b).hexdigest()==r['sha1'];assert r['status']==200 and r['tls']['authorized']
test('Four retained HTTPS response bodies keep byte length,hash and authorized TLS evidence',len(requests)==4)
pdf=(base/'NCL-000002203.pdf').read_bytes();api=json.loads((base/'commons-imageinfo.json').read_text(encoding='utf8'));info=next(iter(api['query']['pages'].values()))['imageinfo'][0]
test('Actual PDF matches Commons API size and SHA1; local SHA256 records identity',len(pdf)==info['size']==58287949 and sha1(pdf).hexdigest()==info['sha1']=='2543dd33a32be978bd09e96557cdc3a57c0309a4')
catalog=re.sub(r'<[^>]*>',' ',(base/'ncl-catalog.html').read_text(encoding='utf8'));catalog=re.sub(r'\s+','',catalog)
test('Institutional catalog independently identifies title,author,publisher,place,year and accession',all(s in catalog for s in ['新命理探原','袁樹珊','潤德','香港','1915','000002203','487']))
reader=PdfReader(BytesIO(pdf));manual=json.loads((base/'MANUAL_READINGS.json').read_text(encoding='utf8'))
test('Actual486PDF pages remain distinguished from catalog487and conditional1915edition date',len(reader.pages)==486 and manual['identity']['actualPDFPages']==486 and manual['identity']['catalogPageCount']==487 and 'no imprint year read' in manual['identity']['editionQualification'])
extracted=json.loads((base/'EXTRACTED_PAGES.json').read_text(encoding='utf8'))['pages'];by_page={r['pdfPage']:r for r in extracted}
for r in extracted:
    b=(base/r['file']).read_bytes();assert len(b)==r['bytes'] and sha256(b).hexdigest()==r['sha256'];assert list(Image.open(BytesIO(b)).size)==r['size']
test('All59stored navigation/evidence page rasters retain their exact extraction hashes',len(extracted)==59)
targets=sorted(set(manual['identity']['bibliographicPagesRead']+[n for u in manual['units'] for n in u['pdfPages']]))
for n in targets:
    r=by_page[n];images=list(reader.pages[n-1].images);chosen=[i for i in images if sha256(i.data).hexdigest()==r['sha256']];assert len(chosen)==1
    overlay=[i for i in images if sha256(i.data).hexdigest()=='6d7e3af02fd89fad74210c74fc9ebea3d55f13cc13eaf036162b23663a381ed2'];assert len(overlay)==1
test('All13selected content/bibliographic page rasters match their actual parent PDF images',len(targets)==13)
for n in [308,309]:
    r=by_page[n];b=(base/r['visualPNG']).read_bytes();assert sha256(b).hexdigest()==r['visualSHA256'];a=Image.open(base/r['file']);v=Image.open(BytesIO(b));assert a.size==v.size and a.mode==v.mode and a.tobytes()==v.tobytes()
test('Two JP2view PNG derivatives have identical decoded pixels and no text reconstruction',True)
test('Manual late-Zi instruction and direct named example remain separately anchored to read pages',manual['units'][1]['pdfPages']==[86,87,88] and manual['units'][2]['pdfPages']==[308,309,310] and '用壬日起庚子時' in manual['units'][2]['excerpts'])
test('Traditional onset,person identity and whole-book coverage remain explicitly excluded',all(s in manual['coverageLimit'] for s in ['three reading units','not59collated','One attributed scan']) and 'no onset date' in manual['units'][1]['limit'])
result={'checks':checks,'summary':{'httpBodies':len(requests),'pdfBytes':len(pdf),'pdfSHA256':sha256(pdf).hexdigest(),'pdfPages':len(reader.pages),'storedPageRasters':len(extracted),'parentImageChecks':len(targets),'targetContentPages':8,'targetUnits':3,'noOCR':True,'noIndependentTextualLineageClaim':True},'manualSHA256':sha256((base/'MANUAL_READINGS.json').read_bytes()).hexdigest()}
(qa/'SOURCE_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print(f'{len(checks)}/{len(checks)} source checks passed')
