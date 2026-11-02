from pathlib import Path
from hashlib import sha256,sha1
import json,re
from PIL import Image
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/bazi-jianlu-context';q=r/'qa/bazi-jianlu-context'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
d=read(b/'SOURCE_MANIFEST.json')
assert sha(w/d['sourceContainer'])==d['sourceSHA256']and sha(w/d['decoder'])==d['decoderSHA256']
for x in d['retainedDigital']+d['nativeImages']:assert sha(w/x['file'])==x['sha256']
ending=d['newEndTitlePage'];assert sha(b/ending['file'])==ending['sha256']and ending['directVisualQA']
im=Image.open(b/ending['file']);assert im.mode=='RGBA'and im.size==(ending['width'],ending['height'])
assert sha256(im.tobytes()).hexdigest()==ending['pixelRGBA_SHA256']
cross=read(b/'CROSSREF_READINGS.json');assert sha(w/cross['sourceFile'])==cross['sourceSHA256']
assert(w/cross['sourceFile']).read_bytes()==(w/cross['duplicateRetainedFile']).read_bytes()
for x in cross['sections']:assert len((b/x['file']).read_text(encoding='utf-8'))==x['chars']
raw=(b/'RETAINED_DIGITAL_SECTION.txt').read_text(encoding='utf-8');norm=re.sub(r'<pb:[^>]+>|¶|\s','',raw);body=norm[norm.index('建禄者'):]
contexts=read(b/'JIANLU_CONTEXTS.json');assert ''.join(x['retainedDigitalText']for x in contexts['units'])==body and len(body)==1223
v3=re.sub(r'<pb:[^>]+>|¶|\s','',(b/'DIGITAL_CROSSREF_BLADE.txt').read_text(encoding='utf-8'))
tables=read(b/'BLADE_TABLES.json')['tables'];assert len(tables[0]['rows'])==8 and len(tables[1]['rows'])==5
for x in tables[0]['rows']:assert f"{x['branch']}者{x['stem']}之正位"in v3
assert tables[0]['unstatedStems']==['戊','己']and tables[1]['explicitlyExcludedStems']==['乙','丁','己','辛','癸']
assert len(read(b/'TARGETED_NATIVE_PASSAGES.json')['readings'])==5
v=b/'volume3';ident=read(v/'IDENTITY.json');original=(v/'CADAL06066039.djvu').read_bytes()
assert len(original)==ident['catalogueBytes']==ident['actualBytes']==10619960
assert sha1(original).hexdigest()==ident['catalogueSHA1']==ident['actualSHA1']
assert sha(v/'CADAL06066039.djvu')==ident['actualSHA256']==d['volume3']['sourceSHA256']
requests=read(v/'REQUESTS.json')['records'];assert len(requests)==2
for x in requests:
 assert x['status']==200 and x['tls']['authorized'] is True
 assert (v/x['file']).stat().st_size==x['bytes'] and sha(v/x['file'])==x['sha256']
fac=read(b/'FACSIMILE_CROSSREF_READINGS.json');renders=read(v/'RENDERS.json')
assert renders['actualContainerPages']==230 and len(renders['records'])==26
assert sorted(x['page']for x in fac['readings'])==[2,*range(3,20),*range(112,120)]
assert all(x['directVisualRead'] and not x['allCharactersCollated']for x in fac['readings'])
assert sum(x['classification']=='section-content'for x in fac['readings'])==24
for x in renders['records']:
 assert sha(v/x['file'])==x['sha256'] and (v/x['file']).stat().st_size==x['bytes']
 image=Image.open(v/x['file']);assert image.mode=='RGBA'and image.size==(x['width'],x['height'])
 assert sha256(image.tobytes()).hexdigest()==x['pixelRGBA_SHA256']
 assert next(t for t in fac['readings']if t['page']==x['page'])['sha256']==x['sha256']
entity=fac['entityCollation'];assert entity['nativeReading']=='嗤'and entity['rawDigitalUnchanged']
assert '&KR0339;'in(b/'DIGITAL_CROSSREF_LU.txt').read_text(encoding='utf-8')
assert sha(b/entity['nativeCrop'])==entity['cropSHA256']
assert Image.open(v/'images/p018.png').convert('RGBA').crop(entity['cropBox']).tobytes()==Image.open(b/entity['nativeCrop']).convert('RGBA').tobytes()
assert tables[0]['sourceImages']==[113]and tables[0]['namedSchoolClarificationImages']==[118,119]
assert all(t['tier']=='native-facsimile-targeted-passages'for t in tables)
out={'date':'2026-10-27','nativeImageHashesVerified':37,'expandedNativePagesVerified':10,'newVolume3NativePositionsVerified':26,'newEndTitlePageVerified':1,'newConditionalContentPages':24,'retainedDigitalFilesVerified':2,
 'sourceContextUnits':44,'retainedDigitalBodyCharacters':1223,'directBladeRowsDigitalOnly':0,'directBladeRowsNativeTargeted':13,'nativeEntityCropVerified':1,
 'allSourceImageCharactersCollated':False,'newHTTPRequests':2,'httpStatuses':[200,200],'normalTLSVerified':True,'newOriginalContainers':1,'newSourcePages':27,'expandedPreviouslyReadPages':10,'wholeCatalogueCompleted':False}
(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,ensure_ascii=False))
