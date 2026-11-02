from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json
b=Path(__file__).resolve().parent;w=b.parents[1]
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
save=lambda name,o:(b/name).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
qa=read(b/'QA_IMAGES.json')
for name,box,note in [('p175-lu-glyph-native.png',[1330,300,1580,1500],'Initial target crop actually contains 如己亥 context, not the disputed祿clause; retained with correction note.'),('p175-lu-clause-native.png',[1120,300,1360,1500],'Correct target native crop shows 而土祿在亥; retain apparent literal土, no correction from standard祿table.')]:
 p=b/name;qa['records'].append(dict(sourceFile='v53/research/bazi-food-source/p175.png',file=name,cropBox=box,sha256=sha256(p.read_bytes()).hexdigest(),resampled=False,actuallyViewed=True,readingNote=note))
for x in qa['records']:
 src=w/x['sourceFile'];p=b/x['file'];assert sha256(p.read_bytes()).hexdigest()==x['sha256']
 assert ImageChops.difference(Image.open(src).convert('RGB').crop(x['cropBox']),Image.open(p).convert('RGB')).getbbox()is None;x['actuallyViewed']=True
save('QA_IMAGES.json',qa)
context=read(b/'RETAINED_CONTEXT.json')['context'];quote='如己亥不畏丁倒食丁與壬合化木而壬禄在亥';start=context['text'].index(quote)
save('SELECTED_READING_AUDIT.json',dict(date='2026-10-28',parentContext='FOOD-00-C15',localQuoteCodepointOffsets=[start,start+len(quote)],digitalQuote=quote,
 nativeSelectedReading='如己亥不畏丁倒食丁與壬合化木而土祿在亥',
 glyphAtLuClause=dict(digital='壬',facsimile='土',sourceContainerPage=175,crop='p175-lu-clause-native.png',notAutomaticallyCorrectedFromConventionalLuTable=True),
 nativeNote='土glyph presently read on native crop; not adjudicated authorial truth or emendation, compare another witness if required.',
 previousPrivateVisualGuess='Full-page initial impression could look己; correct crop actually shows土. Never promoted into a rule or consumer output.',
 sourceAnchorOfNamedExamplesUnresolved=True,effectiveTransformationPremisesUnresolved=True,allExceptionClausesTranscribed=False,consumerAffected=False))
state=read(b/'WORK_STATE.json');state.update(status='C15twoexpandedimages-fourcrops-viewed-lu-clause土-versus壬-recorded-rule-premises-open',nativeCropsViewedPixelMatched=4,
 currentTextualDifference='Native175而土祿在亥 versus digital而壬禄在亥; do not repair either automatically.',
 noExceptionEngineImplemented=True,passedRuntimeChecks=0,
 next=['Continue remaining C15exceptions, preserving exact clause offsets and explicit image/digital disagreement; current4cropsverified,do notcountnewsourcepositions.',
 'Named-pillarexampleanchorand effective合化premises remain unresolved; do not infer an exception from a bare visiblepair or force 土→壬 from conventional祿table.',
 'If this anchor remains blocked, switch to another complete independent clause/domain; retain latestverifiedmonthcommandrelease4596files.'])
save('WORK_STATE.json',state)
print('Recorded4nativecrops/土-versus壬atC15;noimplementedexceptionorconsumerchange')
