from pathlib import Path
from hashlib import sha256
from PIL import Image
import json
d=Path(__file__).resolve().parent
write=lambda p,o:p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Direct entry of the printed columns, before any engine call or formula expansion.
cols=[('青龍','黃道','申戌子寅辰午申戌子寅辰午',134),
 ('明堂','黃道','酉亥丑卯巳未酉亥丑卯巳未',134),
 ('天刑','黑道','戌子寅辰午申戌子寅辰午申',134),
 ('朱雀','黑道','亥丑卯巳未酉亥丑卯巳未酉',134),
 ('金匱','黃道','子寅辰午申戌子寅辰午申戌',135),
 ('天德','黃道','丑卯巳未酉亥丑卯巳未酉亥',135),
 ('白虎','黑道','寅辰午申戌子寅辰午申戌子',135),
 ('土堂','黃道','卯巳未酉亥丑卯巳未酉亥丑',135),
 ('天牢','黑道','辰午申戌子寅辰午申戌子寅',135),
 ('玄武','黑道','巳未酉亥丑卯巳未酉亥丑卯',135),
 ('司命','黃道','未酉亥丑卯巳未酉亥丑卯巳',135)]
write(d/'MANUAL_HOUR_TABLE.json',{'date':'2026-10-28','sourcePDFSHA256':'b6394102a995bb66df173452b37614b29d58e34ff85e08c43077006572ac48a5',
 'sourcePDFPages':[134,135],'sourceDayBranches':list('子丑寅卯辰巳午未申酉戌亥'),
 'entryMethod':'Direct manual entry of 11 printed columns; no engine-generated expected values',
 'columns':[{'sourceLabel':label,'sourceType':typ,'hoursByDayBranch':list(hours),'sourcePDFPage':page}for label,typ,hours,page in cols],
 'pendingColumn':{'sourceLabel':'勾陳','sourcePDFPage':135,'reason':'Printed hour column visibly irregular; full diplomatic transcription and independent witness pending. Do not fill from a common formula.'},
 'comparisonAliasesOnly':{'青龍':'青龙','金匱':'金匮','土堂':'玉堂','天牢':'天牢','司命':'司命'},
 'tuTangAliasIsEditorialAndDoesNotRewritePrintedGlyph':True,
 'all144PrintedCellsCollated':False,'directEnteredCells':132,'overallAuspiciousnessValidated':False})
write(d/'READING_CORRECTION_AUDIT.json',{'date':'2026-10-28','sourcePDFPage':134,
 'initialFirstPassInterpretation':'An initial note read 截路空亡 as a blanket exception even to a yellow-path hour.',
 'nativeCropReading':'The passage separates 值黑道空亡為不吉 from 截路空亡止忌出行嫁娶移徙餘皆不忌.',
 'correction':'截路空亡 restriction here explicitly names travel, marriage and relocation; it does not authorize a blanket restriction on all other activities.',
 'sourceFragments':['凡遇黃道貴人祿馬值時百事利宜','值黑道空亡為不吉','截路空亡止忌出行嫁娶移徙餘皆不忌'],
 'initialNoteWasPrivate':True,'publishedEngineOrConsumerChanged':False,'rulePriorityBetweenAllFactorsEstablished':False})
p=d/'CONTEXT_READINGS.json';obj=json.loads(p.read_text(encoding='utf-8-sig'))
for row in obj['groups']:
 if row['sourcePDFPage']==134:row['editorialSummary']='定時吉凶: 黃/黑道 nhãn theo chi ngày/giờ. Đọc crop sửa ý ban đầu: 截路空亡 chỉ kiêng 出行嫁娶移徙, 餘皆不忌; không phải cấm mọi việc dù Hoàng đạo. Xem READING_CORRECTION_AUDIT.'
 if row['sourcePDFPage']==135:row['editorialSummary']+=' Native: nhãn 土堂 giữ nguyên, 玉堂 chỉ alias đối chiếu; cột 司命 ghi 未酉亥丑卯巳 lặp, chưa tự sửa. 勾陳 chưa chép đủ.'
write(p,obj)
p=d/'qa/p134-exception-complete-native.png';box=(580,200,1220,1955)
Image.open(d/'raw-p134.jpg').crop(box).save(p)
meta=json.loads((d/'QA_IMAGES.json').read_text(encoding='utf-8-sig'))
# These four additional crops have already been viewed. The complete exception crop is next.
extra=[('p135-bottom-hour-native.png',135,(1200,1170,2410,1950),True),('p135-last-two-native.png',135,(1220,1000,1515,1940),True),('p135-siming-native.png',135,(1360,850,1575,1950),True),('p134-exception-complete-native.png',134,box,False)]
for x in meta['crops']:x['actuallyViewed']=True
for name,page,b,seen in extra:
 p=d/'qa'/name
 meta['crops'].append({'file':p.relative_to(d).as_posix(),'sourcePDFPage':page,'cropBox':list(b),'sourceSize':[2460,1955],'pixelSize':list(Image.open(p).size),'sha256':sha256(p.read_bytes()).hexdigest(),'resampled':False,'actuallyViewed':seen})
write(d/'QA_IMAGES.json',meta)
print('11 direct columns / 132 cells saved; no engine executed yet; exception-scope correction preserved.')
