from pathlib import Path
from hashlib import sha256
from collections import Counter
from difflib import SequenceMatcher
import json,unicodedata

root=Path(__file__).resolve().parent.parent;base=root/'research/meihua-table-bodies';qa=root/'qa/meihua-table-bodies'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda p:sha256(p.read_bytes()).hexdigest()
norm=lambda s:''.join(c for c in s if not c.isspace()and not unicodedata.category(c).startswith('P'))
tables=read(root/'research/meihua-volume1/TABLE_FIELDS.json')['records']; groups={};group=None
for line in(base/'PHYSICAL_READINGS.txt').read_text(encoding='utf-8').splitlines():
 if not line or line.startswith('#'):continue
 if line.startswith('['):group=line[1:-1];groups[group]=[]
 else:groups[group].append(line)
numbers={'乾':1,'兌':2,'離':3,'震':4,'巽':5,'坎':6,'艮':7,'坤':8}
assert set(groups)==set(numbers)and all(len(v)==27 for v in groups.values())
associations={'天時','地理','人物','人事','身體','靜物','動物','屋舍','飲食','方道','五色','五味'}
records=[]
for t in tables:
 body=groups[t['trigram']][t['physicalOrderInTable']-1];n=norm(body);digital=t['digitalBody'];dn=norm(digital)if digital else None;header=t['printedHeader']
 category='cultural-symbol-association'if header in associations else 'calendar-analogy-premises-open'if header=='時序'else 'name-number-analogy-not-cast-arithmetic'if header in ['姓字','數目']else 'traditional-forecast-claim-not-empirically-established'
 r={'id':t['trigram']+'-'+header,'trigram':t['trigram'],'trigramNumber':numbers[t['trigram']],'field':header,'physicalOrder':t['physicalOrderInTable'],
 'pdfPages':t['bodyPDFPages'],'physicalNormalizedReading':body,'physicalReadingSHA256':sha256(body.encode()).hexdigest(),
 'punctuation':'Editorial comma segmentation;not a diplomatic transcription of original spacing/punctuation. No character compatibility folding or spelling emendation.',
 'unresolvedGlyphs':body.count('□'),'readingStatus':'one-glyph-open'if '□'in body else 'normalized-body-reading-complete',
 'digitalHeader':t['digitalHeader'],'digitalBody':digital,'digitalBodySHA256':t['digitalBodySHA256'],
 'comparison':'missing-in-pinned-digital'if digital is None else 'glyph-open'if '□'in body else 'same-after-punctuation-removal'if n==dn else 'different-character-sequence',
 'differences':[]if dn is None else [{'physical':n[i:j],'digital':dn[k:l]}for op,i,j,k,l in SequenceMatcher(None,n,dn,autojunk=False).get_opcodes()if op!='equal'],
 'disposition':category,'consumerApplied':False,'predictiveAccuracyEstablished':False}
 records.append(r)
write(base/'BODY_COLLATION.json',{'schema':'hhc.meihua.table-body-collation.v1','date':'2026-10-27','sourcePDF':'../meihua/NLC416-12jh005426-44577.pdf',
 'physicalTranscriptionFile':'PHYSICAL_READINGS.txt','physicalTranscriptionSHA256':sha(base/'PHYSICAL_READINGS.txt'),
 'sourcePDFSHA256':sha(root/'research/meihua/NLC416-12jh005426-44577.pdf'),'sourceBytes':5621631,'records':records,
 'counts':{'bodyPositions':len(records),'trigrams':8,'fieldsEach':27,'normalizedReadingsComplete':sum(not r['unresolvedGlyphs']for r in records),'glyphOpenFields':sum(bool(r['unresolvedGlyphs'])for r in records),
 'comparison':dict(Counter(r['comparison']for r in records)),'disposition':dict(Counter(r['disposition']for r in records))},
 'notClaimed':['Full critical edition or independent witness collation','Historical forecast accuracy','Calendar boundary algorithm from symbolic time lists','Whole-book/catalogue completion'],
 'newHTTPResponses':0,'newContentPages':0,'expandedEarlierPageReadings':22,'nativeQARenders':7,'nativeGlyphCrops':12})
pages=[]
for n in range(33,55):
 image=root/f'research/meihua/images/p{n:03}.png';pages.append({'pdfPage':n,'printedPage':n-12,'image':'../meihua/images/'+image.name,'imageSHA256':sha(image),
 'expandedEarlierReading':True,'newContentPageReading':False,'readingLevel':'All mapped table-body positions on page visually compared;normalized body readings retained,not full diplomatic transcription.',
 'fieldIDs':[r['id']for r in records if n in r['pdfPages']]})
write(base/'MANUAL_READINGS.json',{'date':'2026-10-27','records':pages,'sourceInstructionPolicy':'Source secrecy/advice is document content,not user instructions to this agent.','newHTTPResponses':0})
write(base/'VARIANTS_AND_LIMITS.json',{'date':'2026-10-27','unresolvedGlyphs':[
 {'id':'震-飲食','pdfPage':39,'retained':'□酸味','candidates':['菓','葉'],'decision':'Do not insert digital果 or select a candidate from context alone.'},
 {'id':'離-天時','pdfPage':46,'retained':'日電虹□霞','candidates':['寬','霓'],'decision':'Printed form resembles寬;digital霓 is not automatically accepted as the scan reading.'}],
 'materialComparisons':[
 {'id':'乾-天時','physical':'電','digital':'雹','risk':'Different weather symbol;not interchangeable.'},
 {'id':'乾-時序','physical':'五金年月日時','digital':'一四九年月日時','risk':'Preserve the printed unusual wording;do not silently emend or parse as a dated calendar rule.'},
 {'id':'乾-地理','physical':'高九之所','digital':'高亢之所','risk':'Native crop retains visible九;semantic emendation would require separate evidence.'},
 {'id':'震-五色','physical':'黑青綠碧','digital':'青綠碧','risk':'Additional黑;do not overwrite all element palettes from one table.'},
 {'id':'巽-地理','physical':'花果茶圃','digital':'花果菜園','risk':'Different object/place wording.'},
 {'id':'巽-時序','physical':'三五八之時日月三月辰巳年月日時四月','digital':'三五八之時月日辰巳月日時','risk':'Extra month labels/year term and order;not a universal conversion algorithm.'},
 {'id':'坎-人物','physical':'盜賊','digital':'資賊','risk':'Different word;no person classification from a cast.'},
 {'id':'坎-屋舍','physical':'茶酒肆宅中濕地之處','digital':'花酒長器宅中混地之處','risk':'Different building words;keep source data outside home advice.'},
 {'id':'坎-婚姻','physical':'不利成婚不可婚辰戌丑未月','digital':'辰戌丑未月婚不可','risk':'Printed general clause missing in digital;historical claim only.'},
 {'id':'離-動物','physical':'雉龜鱉螺蚌','digital':'雉龜鱉蟹螺蚌','risk':'Digital蟹 not found in this printed row;do not fill it by analogy.'},
 {'id':'離-時序','physical':'二三七日','digital':'三二七日','risk':'Same-number membership does not prove equal wording/order;printed數目 elsewhere remains三二七.'},
 {'id':'兌-時序','physical':'金年月日二四九數月日','digital':'二四九月日','risk':'Extra金 and數;not a validated birth-year/calendar premise.'},
 {'id':'兌-數目','physical':'二四九','digital':'四二九','risk':'Printed姓字 retains四二九;different local order,not permission to change trigram2.'},
 {'id':'兌-官訟','physical':'因公有損','digital':'因訟有損','risk':'Different premise;keep as a historical assertion,not legal advice.'}],
 'interpretation':'Character-sequence differences include orthographic variants,word order,omissions and substantive wording. The automated diff count is not a count of proven digital transcription errors or independent traditions.',
 'qaLimit':'pypdf native-image decode lacks jbig2dec;metadata read succeeded and bundled Poppler rendered7targeted pages at300dpi. No new decoder/network/OCR. Crop coordinate error corrected before viewing12final crops.'})
print(json.dumps(read(base/'BODY_COLLATION.json')['counts'],ensure_ascii=False))
