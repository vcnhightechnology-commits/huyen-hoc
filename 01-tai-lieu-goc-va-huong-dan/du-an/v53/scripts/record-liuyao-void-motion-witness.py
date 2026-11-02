from pathlib import Path
from hashlib import sha256
import json
root=Path(__file__).resolve().parent.parent;base=root/'research/liuyao-void-motion'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda p:sha256(p.read_bytes()).hexdigest()
r=read(base/'REQUESTS.json')['records'];ok=[x for x in r if x.get('status')==200];failed=[x for x in r if x.get('error')]
assert len(ok)==11 and len(failed)==1
for x in ok:assert sha(base/x['file'])==x['sha256']and(base/x['file']).stat().st_size==x['bytes']and x['tls']['authorized']
m=read(base/'japan-volume1-manifest.json');assert len(m['sequences'][0]['canvases'])==51
images=[]
notes={30:'Navigation/bounded text:fiveelement interactions/use-subjectroles,not complete page transcription.',32:'Navigation/bounded text:澤天夬→天風姤andunchangedvs changedannotations;not a new64structuretable.',
35:'Boundedchapter8用神opening/subjectlists;not wholechaptercollation.',37:'Bounded元神5effective/6ineffectiveclausesandendpreceding忌神opening;seeQA crop. No兌→解datedexampleinside thiscorrespondingclause span.',38:'Bounded忌神5effective/7ineffectiveclausesand大過→鼎example;notwholebookabsence claim.'}
for n in[30,32,35,37,38]:
 f=f'japan-spread-{n}-original.jpg';c=m['sequences'][0]['canvases'][n-1]
 images.append({'sequenceCanvasOrdinal1':n,'canvasID':c['@id'],'imageResourceURL':c['images'][0]['resource']['@id'],'file':f,'sha256':sha(base/f),
 'label':c['label'],'readingScope':notes[n],'serverResponsePixels':[3000,2073],'canvasMetadataPixels':[6150,4250],
 'pixelPolicy':'Unmodified returned JPEGbytes;metadata dimensions do not prove response has original masterresolution. No upscaling asserted.',
 'entireSpreadDiplomaticallyTranscribed':False})
out={'date':'2026-10-27','institution':'National Archives of JAPAN','itemURL':'https://www.digital.archives.go.jp/item/4756813',
 'viewerURL':'https://www.digital.archives.go.jp/img/4756813','manifestURL':m['@id'],'manifestFile':'japan-volume1-manifest.json','manifestSHA256':sha(base/'japan-volume1-manifest.json'),
 'itemLabel':m['label'],'referenceCode':'子０５９－０００８-0001','canvasesRegistered':51,'manifestIsWholeBookExtraction':False,
 'parentCatalogEvidence':{'file':'../liuyao-foundations/japan-zengshan-catalog.html','sha256':sha(root/'research/liuyao-foundations/japan-zengshan-catalog.html'),
 'scope':'Retained official parentcatalog identifies6冊/6巻,清乾隆/学耕堂 and former毛利高標collection;not direct imprintimage verification.'},
 'transport':{'ordinaryPublicHTTPSRequests':12,'retainedHTTP200Bodies':11,'retainedBodyBytes':sum(x['bytes']for x in ok),'timeoutsWithoutBody':1,
 'webToolItemRequest':'403reported on2026-10-27;ordinarypublicHTTPS200withauthorizedTLSretained. No authenticationorTLSbypass.',
 'failedFile':'japan-spread-33-original.jpg','failedRequestRetried':False,'newOriginalPDFs':0},
 'navigationOnlyImages':[{'file':f'japan-nav-{n}.jpg','sha256':sha(base/f'japan-nav-{n}.jpg'),'reading':'thumbnailnavigationonly;notclausetranscription'}for n in[20,30,40]],
 'manualBoundedSpreadReadings':images,'qaCrop':{'file':'qa-crops/japan-37-origin-clauses.jpg','sha256':sha(base/'qa-crops/japan-37-origin-clauses.jpg')},
 'comparisonFindings':[
 {'id':'origin-clause-parallel','B02PDFPages':[51,52,53],'japanCanvasOrdinal1':37,'status':'parallel-five-effective-six-ineffective-clause-lists-present',
 'limit':'No full diplomatic collation;visible wording includes動不為空/沖空實空. Shared clause lists do not prove independent textual pedigree.'},
 {'id':'opposing-clause-parallel','B02PDFPages':[53,54],'japanCanvasOrdinal1':38,'status':'parallel-five-effective-seven-ineffective-and大過鼎-example-present',
 'limit':'Historical anecdote not independently validated.'},
 {'id':'PDF52-date-void-conflict','dateAsReadInB02':'酉月辛卯日','standardVoid':'午未','B02proseVoid':'寅卯','status':'unresolved',
 'finding':'No corresponding兌58→解40datedanecdote found within the directly read parallel元神clause span37. This does not establishabsenceelsewhere or justifyrewriting辛卯as辛亥.',
 'next':'Collate exactedition additions/otherwitnesses ifneeded;keep B02literalreading and exceptionopen.'}],
 'sourceClassification':'Officially hosted photographed printed-volume witness;different retained object fromB02PDF. Editiongenealogy/independence and imprint date not established by these bounded readings.',
 'wholeBookRead':False,'consumerApplied':False}
(base/'INDEPENDENT_WITNESS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out['transport'],ensure_ascii=False))
