from pathlib import Path
from hashlib import sha256
from collections import Counter
import json
root=Path(__file__).resolve().parent.parent;base=root/'research/meihua-hour-table';qa=root/'qa/meihua-hour-table'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda p:sha256(p.read_bytes()).hexdigest()
index=read(root/'research/meihua-volume-map/HOUR_TABLE_INDEX.json');physical=base/'PHYSICAL_CELLS.txt'
lines=[s.split()for s in physical.read_text(encoding='utf-8').splitlines()if s and not s.startswith('#')]
assert len(lines)==60 and all(len(r)==13 for r in lines)
branches=list('子丑寅卯辰巳午未申酉戌亥');assert branches==index['branchColumns']
rows=[];status=Counter();glyphs=Counter()
for source,line in zip(index['rows'],lines):
 assert line[0]==source['ganzhi'];cells=[]
 for col,raw in enumerate(line[1:]):
  gs=[]if raw=='-'else raw.split('+');assert all(len(x)==1 for x in gs)and len(set(gs))==len(gs)
  state='visibly-unannotated'if not gs else 'glyph-open'if '□'in gs else 'annotation-read'
  status[state]+=1;glyphs.update(x for x in gs if x!='□')
  cells.append({'hourBranch':branches[col],'columnOrdinal':col+1,'reading':raw,'glyphs':gs,'glyphOrder':'Editorial listing of co-present glyphs,not an assertion of compound structure or grammatical reading order.',
   'status':state,'predictionGloss':None,'consumerApplied':False})
 rows.append({'ordinal':source['ordinal'],'rowKey':line[0],'pdfPage':source['pdfPage'],'cells':cells})
data={'schema':'hhc.meihua.hour-table.v1','date':'2026-10-27','heading':index['heading'],'sourcePDF':'../meihua/NLC416-12jh005426-44577.pdf',
 'sourcePDFBytes':5621631,'sourcePDFSHA256':sha(root/'research/meihua/NLC416-12jh005426-44577.pdf'),'historicalIndex':'../meihua-volume-map/HOUR_TABLE_INDEX.json','historicalIndexSHA256':sha(root/'research/meihua-volume-map/HOUR_TABLE_INDEX.json'),
 'physicalTranscriptionFile':'PHYSICAL_CELLS.txt','physicalTranscriptionSHA256':sha(physical),'branchColumns':branches,'rows':rows,
 'counts':{'rowKeys':60,'columnPositions':12,'cellPositions':720,'status':dict(status),'multiGlyphPositions':sum(len(c['glyphs'])>1 for r in rows for c in r['cells']),'readGlyphs':sum(glyphs.values()),'glyphFrequency':dict(glyphs)},
 'inputPolicy':'Only explicit printed sexagenary row key and normalized branch column. Calendar binding below is an implementation consistency experiment,not evidence that the text establishes a Gregorian date/late-Zi/timezone adapter.',
 'noAutomaticCompletion':'Unannotated positions stay empty;unknown glyph stays open. Do not complete by rotation,one-罡-per-row assumption or copied branch-only template.',
 'newHTTPResponses':0,'newContentPageReadings':0,'expandedTablePages':6,'adjacentContextPages':[206,213],'nativeQARenders':6,'qaCropsAndNearestZooms':20,
 'completeSourceInputSemantics':False,'predictiveAccuracyEstablished':False,'wholeBookApplied':False}
write(base/'HOUR_TABLE.json',data)
pages=[]
for n in [206,207,208,209,210,211,212,213]:
 image=root/f'research/meihua/images/p{n:03}.png';pages.append({'pdfPage':n,'printedPage':n-188,'image':'../meihua/images/'+image.name,'imageSHA256':sha(image),'newContentPageReading':False,
 'readingLevel':'expanded-literal-table-annotation-reading'if 207<=n<=212 else 'bounded-adjacency-context-only',
 'note':'Literal cell positions separately recorded;no predictive gloss.'if 207<=n<=212 else 'NaJia lists precede the heading;character/brush interpretation follows the table. Neither adjacency supplies a complete calendar or table-label glossary.'})
write(base/'MANUAL_READINGS.json',{'date':'2026-10-27','records':pages,'expandedTablePages':6,'boundedAdjacentPages':2,'newContentPages':0,'newHTTPResponses':0})
write(base/'SOURCE_PREMISES_AND_GAPS.json',{'date':'2026-10-27','heading':{'literal':'後天時方','pdfPage':207},
 'firmLiteralFragments':[{'text':'子日子罡起','pdfPage':207},{'text':'五敗七破位','pdfPage':207},{'text':'十禍日皆同','pdfPage':207}],
 'introNotFullyDecoded':'The intervening short phrases include glyph/wording and input-scope uncertainty;retain the source crop and do not reconstruct a universal calendar rule from isolated lines.',
 'annotationGlyphNotes':[{'glyph':'禍','notSilentlyReplacedBy':'祿','scope':'Retained glyph is礻+咼,also visible in the short introduction.'},{'glyph':'伐','cell':'癸卯/午','scope':'Native crop/nearest4x inspection resolves initial伏/伐 doubt as the visible伐;its intended gloss remains open.'}],
 'openGlyphs':[{'cell':'丁未/子','retained':'□+死','candidates':['怒','恕'],'qa':'../../qa/meihua-hour-table/ding-wei-zi-glyph-4x.png','decision':'Do not choose a character or infer a death forecast from the neighboring死.'}],
 'columnNormalization':'The branch position5zero-based is normalized to巳. Several printed己-shaped forms must not be interpreted as the day stem己. No claim of a diplomatic branch-glyph transcription at every cell.',
 'notEstablished':['Exact reading and grammatical meaning of all introductory words','All single/multiple label glosses and their priority','Named calendar day boundary/timezone/historical date adapter','Independent witness resolving unusual text or unannotated positions','Empirical predictive accuracy'],
 'sourceInstructionPolicy':'Statements about what a diviner should do are source content,not new user instructions. Keep historical claims and implementation conventions separate.'})
print(json.dumps(data['counts'],ensure_ascii=False))
