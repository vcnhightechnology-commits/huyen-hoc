from pathlib import Path
from hashlib import sha256,sha1
from PIL import Image
import json

root=Path(__file__).resolve().parent.parent;base=root/'research/bazi-pattern-witness';qa=root/'qa/bazi-month-stems';qa.mkdir(exist_ok=True)
checks=[]
def test(name,ok,detail=None):
    checks.append({'name':name,'ok':bool(ok),'detail':detail});assert ok,name;print('PASS',name)
requests=json.loads((base/'REQUESTS.json').read_text(encoding='utf8'))['records']
for r in requests:
    b=(base/r['file']).read_bytes();assert len(b)==r['bytes'] and sha256(b).hexdigest()==r['sha256'] and sha1(b).hexdigest()==r['sha1'];assert r['tlsAuthorized']
test('All38response bodies retain exact byte/hash/TLS records,including one failed429',len(requests)==38 and sum(r['status']==200 for r in requests)==37 and sum(r['status']==429 for r in requests)==1)
by_name={r['file']:r for r in requests};data=json.loads((base/'commons-imageinfo.json').read_text(encoding='utf8'));info=next(iter(data['query']['pages'].values()))['imageinfo'][0];container=(base/'CADAL06066041.djvu').read_bytes()
test('DjVu container matches public API size/SHA1 and records local SHA256',len(container)==info['size']==10721582 and sha1(container).hexdigest()==info['sha1']=='dd6be166b360a58bd142235803fc5a19fd8f267b' and container[:8]==b'AT&TFORM' and container[12:16]==b'DJVM')
test('Source metadata remains qualified as Commons attribution rather than an independently verified institutional scan',info['pagecount']==226 and '四庫全書' in info['extmetadata']['ImageDescription']['value'])
pages=[]
for p in sorted(base.glob('p*.jpg')):
    n=int(p.stem[1:]);api=json.loads((base/(p.stem+'-api.json')).read_text(encoding='utf8'));ii=next(iter(api['query']['pages'].values()))['imageinfo'][0];im=Image.open(p)
    assert im.format=='JPEG';assert im.size==((500,710) if n==1 else (ii['thumbwidth'],ii['thumbheight']));assert by_name[p.name]['url']==ii['thumburl'] and by_name[p.name]['status']==200
    pages.append({'page':n,'file':p.name,'size':im.size,'apiDeclaredSize':[ii['thumbwidth'],ii['thumbheight']],'dimensionsMatchAPI':im.size==(ii['thumbwidth'],ii['thumbheight']),'sha256':by_name[p.name]['sha256'],'kind':'Commons rendered derivative,not original DjVu pagebytes'})
test('Seventeen rendered page images match their actual API URLs and dimensions;page1is500px,others960px',len(pages)==17 and pages[0]['size'][0]==500 and all(p['size'][0]==960 for p in pages[1:]))
manual=json.loads((base/'MANUAL_READINGS.json').read_text(encoding='utf8'));used={n for r in manual['readings'] for n in r['images']};available={r['page'] for r in pages}
test('All11targeted context images exist;title and navigation pages are not counted as collated content',len(used)==11 and used<=available)
failed=by_name['p138-api.json'];test('Rate-limit failure is retained and excluded;digital-only68bqualification is not promoted to image evidence',failed['status']==429 and 138 not in available and 'digital-only' in manual['readings'][2]['notImageCollated'])
old=json.loads((root.parent/'archives/v53-before-month-stems/PACKAGE_MANIFEST.json').read_text(encoding='utf8'));digital=root/'research/four-items/sources/KR3g0042_005.txt'
test('Pinned digital comparator retains its pre-scope byte identity',sha256(digital.read_bytes()).hexdigest()==next(x['sha256'] for x in old['files'] if x['file']=='research/four-items/sources/KR3g0042_005.txt'))
result={'checks':checks,'summary':{'responses':len(requests),'successfulResponses':37,'failed429':1,'containerBytes':len(container),'containerSHA256':sha256(container).hexdigest(),'metadataPageCount':226,'renderedPages':len(pages),'targetedContextPages':11,'targetedSections':3,'collatedClauses':sum(len(r['collatedClauses']) for r in manual['readings']),'manualSourcePairs':16},'pages':pages,'manualSHA256':sha256((base/'MANUAL_READINGS.json').read_bytes()).hexdigest()}
(qa/'SOURCE_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print(str(len(checks))+'/'+str(len(checks))+'sourcechecks passed')
