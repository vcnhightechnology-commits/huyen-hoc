from pathlib import Path
from hashlib import sha256
import json
from PIL import Image,ImageChops
b=Path(__file__).resolve().parent;w=b.parents[1]
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def save(name,obj):(b/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
qa=read(b/'QA_IMAGES.json')
for x in qa['records']:x['actuallyViewed']=True
extra=b/'qa/p84-element-column-native.png'
qa['records'].append(dict(sourcePDFPage=84,sourceFile='v53/research/home-yangzhai-shishu/raw-p084.jpg',file='qa/'+extra.name,cropBox=[1680,400,1880,1720],transpose=None,resampled=False,sourceRawSHA256='2fba9f29407d00d8d47422a6cdf25c56adc11a555428372ee28dd172b81768a9',sha256=sha256(extra.read_bytes()).hexdigest(),pixelSize=list(Image.open(extra).size),actuallyViewed=True))
assert len(qa['records'])==13
save('QA_IMAGES.json',qa)
newqa=read(b/'GJTS_QA_IMAGES.json')
for x in newqa['records']:x['actuallyViewed']=True
save('GJTS_QA_IMAGES.json',newqa)
renders=read(b/'GJTS_LOCAL_RENDERS.json')
for x in renders['records']:
 x['actuallyViewed']=True;x['viewScope']='Full native image displayed to locate twelve diagrams and boundary prose; not every word transcribed or the whole page fully collated.'
save('GJTS_LOCAL_RENDERS.json',renders)
verified=[]
for x in qa['records']+newqa['records']:
 src=w/x['sourceFile'] if x in qa['records'] else b/x['sourceFile']
 out=b/x['file'];im=Image.open(src).convert('RGB').crop(x['cropBox'])
 if x['transpose']=='ROTATE_180':im=im.transpose(Image.Transpose.ROTATE_180)
 assert ImageChops.difference(im,Image.open(out).convert('RGB')).getbbox() is None
 assert sha256(out.read_bytes()).hexdigest()==x['sha256']
 verified.append(dict(file=x['file'],actuallyViewed=True,pixelsMatchNativeCrop=True))
save('NATIVE_RESULTS.json',dict(date='2026-10-28',crops=verified,cropsVerified=25,newDjvuNativePagesActuallyViewed=4,newDjvuWholePagesFullyCollated=0))
# Literal manual entry from native GJTS case84 crop. No cycle used to enter these six rows.
literal=[('木','六煞','文曲','低'),('木','生氣','貪狼','高'),('火','五鬼','廉貞','小'),('土','天乙','巨門','高'),('金','延年','武曲','高'),('木','六煞','文曲','低')]
original=next(x for x in read(b/'MANUAL_DIAGRAM_CELLS.json')['records'] if x['id']=='YZSS-C84')['printedLayerCells']
rows=[]
for i,(element,label,star,height) in enumerate(literal,1):
 manual=dict(ordinal=i,sourceElement=element,sourceLabel=label,sourceStar=star,sourceSizeHeightWord=height)
 rows.append(dict(caseID='YZSS-C84',sourceDjvuPage=87,crop='qa/gjts-case84-native.png',manualEntry=manual,matchesTianyigeLiteral=manual==original[i-1]))
assert all(x['matchesTianyigeLiteral'] for x in rows)
save('SELECTED_WITNESS_COLLATION.json',dict(date='2026-10-28',directManuallyEnteredSecondWitnessCells=6,records=rows,
 all69CellsCollatedAcrossWitnesses=False,otherElevenDiagrams='Located and native crops viewed; no complete cell-by-cell textual collation claimed.',
 editionIndependenceEstablished=False,reason='Compilation excerpt and possibly related exemplars; agreement does not establish authorial correctness or practical efficacy.',
 unresolvedAnomaly='Both literal diagrams have 木 at C84/1 and C84/6 beside 六煞/文曲. Neither water-seeded cycle nor literal-wood-seeded cycle reproduces all six printed elements. No automatic emendation.'))
audit=read(b/'READING_CORRECTION_AUDIT.json');audit['elementCorrection']['additionalEditionWitness']='GJTS scan DjVu87 selected native six-cell collation also prints 木 at1/6; same anomaly preserved.'
audit['elementCorrection']['independentWitnessOrEmendationEstablished']=False
audit['newWitnessGlyphLimit']='Other eleven witness diagrams not fully transcribed; faint or water/wood-like glyphs not silently equated from the cycle.'
save('READING_CORRECTION_AUDIT.json',audit)
state=read(b/'WORK_STATE.json');state.update(status='12literal-diagrams-context-preconditions-and-selected-second-witness-verified-not-yet-promoted',
 newHTTPRequests=5,newSourcePositions=0,newOriginalContainers=0,newRepositoryDjvuContainers=1,
 newComparisonWitnessPositionsViewed=4,wholeComparisonPagesFullyCollated=0,nativeCropsViewedPixelMatched=25,
 completeRuntimeChecks=10,actualExistingLayerComponentCalls=75,actualHHCChartCalls=0,calendarEngineCalls=0,
 directManualWitnessCells=6,all69CellsAcrossWitnessesCollated=False,
 next=['Cross-collate remaining63cells and all prose/side-palace/central-room clauses before any practical adapter.',
 'Preserve C84literal木/六煞 anomaly across two related editions; do not force an emendation from formula.',
 'Promote bounded research APIs and provenance; consumer stays unchanged until complete premises and UI QA.'])
state['records'][10]['expandedReview']='坐東朝西開乾門; five numbered interior cells, not six. Different first element from same gate C82; preserve sitting/facing and count origin.'
save('WORK_STATE.json',state)
save('SOURCE_DISPOSITIONS.json',dict(date='2026-10-28',records=[
 dict(kind='repository-facsimile',file='Gujin-Tushu-Jicheng-Volume476.djvu',bytes=33681249,sha256='e819d6f430065e4f63c121390d74ad6d3bc36457cfb8e59fb7a2cea6483130de',apiSHA1Matched=True,TLSValidated=True,institutionOriginalDownloaded=False,credit='Commons metadata: scan downloaded from pan.baidu.com',imprintIndependentlyValidated=False,dateInFilenameIsNotValidatedScanPrintDate=True),
 dict(kind='community-transcription',response='gjts676-page-revisions-response.json',pageNamespacesStored=11,wholePagesFullyRead=0,selectedProseReadPages=[86,87,88,89],facsimileNotReplacedByTranscription=True),
 dict(kind='recreated-diagram-assets',response='gjts-commons-metadata-response.json',imageMetadataRecords=24,imageBodiesDownloaded=0,notOriginalGlyphWitness=True),
 dict(kind='retained-original-HTTP-bytes',records=5,source='REQUESTS.json',allHTTP200TLS=True,initialDefaultNetworkFailure='FETCH_ERROR.json retained; no body acquired; authorized normal TLS acquisition later succeeded.'),
 dict(kind='local-native-DjVu-decoding',records=4,source='GJTS_LOCAL_RENDERS.json',notRawHTTPImages=True,noOCR=True,noBrowserBypass=True),
 dict(kind='editorial-reference',files=['courtyard-reference.mjs','courtyard-context-reference.mjs'],consumerApplied=False,allConditionsApplied=False,healthOrFinancialOutcomeValidation=False)]))
print('Recorded25pixel-verifiedcrops,6selectedliteralwitnesscells,10runtimechecks;noall-sourcecompletionclaim')
