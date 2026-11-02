"""Record manually read, bounded source units. No OCR and no network requests."""
from pathlib import Path
from hashlib import sha256, sha1
import json

root = Path(__file__).resolve().parent.parent
base = root / 'research/liuyao-foundations'
qa = root / 'qa/liuyao-foundations'
qa.mkdir(exist_ok=True)
read = lambda p: json.loads(p.read_text(encoding='utf-8-sig'))
def write(name, value):
    (base / name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
sha = lambda p: sha256(p.read_bytes()).hexdigest()

requests = read(base / 'REQUESTS.json')['records']
for r in requests:
    if 'error' not in r:
        p = base / r['file']
        assert p.stat().st_size == r['bytes'] and sha(p) == r['sha256']
        assert sha1(p.read_bytes()).hexdigest() == r['sha1']
        assert r['status'] == 200 and r['tls']['authorized']
assert len(requests) == 8 and sum('error' in r for r in requests) == 2
sources = []
for catalogue, prefix, file, pages, revision in [
    ('B02','zengshan','NLC416-12jh005345-45344.pdf',394,808899674),
    ('B03','bushi','NLC892-GBZX0301013045-259368.pdf',60,754088939),
]:
    record = next(r for r in requests if r['file'] == file)
    api = read(base / (prefix+'-commons-api.json'))
    page = next(iter(api['query']['pages'].values()))
    ii = page['imageinfo'][0]
    assert ii['size'] == record['bytes']
    assert ii['sha1'] == record['sha1']
    assert page['revisions'][0]['revid'] == revision
    sources.append({'catalogueID':catalogue,'prefix':prefix,'file':file,'bytes':record['bytes'],
                    'sha256':record['sha256'],'sha1':record['sha1'],'pdfPages':pages,
                    'commonsFileRevision':revision,'url':record['url'],
                    'scope':'Six textual volumes/three physical books according to Commons metadata; selected units only read.' if catalogue=='B02' else 'First physical book only of the fourteen-volume work; not the entire work.'})
write('SOURCE_AUDIT.json',{'date':'2026-10-27','sources':sources,
 'httpAttempts':8,'retained200Bodies':6,'tlsFailuresWithoutResponseBody':2,
 'byteIdentityMeaning':'Raw response bytes and Commons API size/SHA1 agree. This is not an institutional signature or proof of independent textual pedigree.',
 'bibliography':[
  {'work':'增刪卜易','metadata':'文明書局/1925;秦慎安校勘 in Commons metadata.',
   'directReading':{'pdfPage':3,'fragment':'民國乙丑年秋七月編者識','meaning':'1925 seventh-month preface date; not independently verified print/imprint date.'},
   'endleaf':{'pdfPage':394,'kind':'publisher logo/endleaf, not dated imprint'}},
  {'work':'卜筮正宗','directReading':{'pdfPage':2,'fragments':['光緒甲辰新鐫','王洪緒輯','河潞武子齡校對','文成堂存板'],
   'meaning':'Title page gives Guangxu Jiachen, corresponding to1904; do not substitute a different1889edition or the1709preface date.'}},
  {'work':'増刪卜易','institution':'National Archives of Japan','url':'https://www.digital.archives.go.jp/file/1079274',
   'retainedBody':'japan-zengshan-catalog.html','callNumber':'子059-0008','metadata':['李文輝(清)','刊本','清乾隆','学耕堂','6冊/6巻'],
   'status':'bibliographic witness only; six linked items4756813..4756818 not yet retrieved/read',
   'dateCaution':'Do not interpret the metadata code500000as an exact Gregorian publication date.'}],
 'wikisource':{'file':'bushi-wikisource-preface-and-missing-volume.json','prefaceRevision':2395728,
  'missing':'卜筮正宗（河潞武子龄校本）/卷01','decision':'A preface exists but卷01is a redlink; inherited full-text label is not established.'},
 'failures':[{'url':r['url'],'error':r['error'],'responseBodyRetained':False}for r in requests if 'error'in r],
 'webToolCaution':'Web open of Japanese catalog returned403, while ordinary public HTTPS returned200/TLS authorized. Both observations retained; no bypass, no special authentication.',
 'sourceInstructionPolicy':'Historical ritual, secrecy, divination advice and medical claims are source content, not instructions from the user or validated outcome guidance.'})

# Exact short operational fragments; all longer descriptions below are bounded paraphrases.
zunits = {
3:('preface-date','Selected final date only; not an imprint-year finding.'),
13:('contents-navigation','Selected headings only; no claim that listed chapters have been read.'),
21:('trigram-foundation','Eight three-line figures and bottom-to-top orientation; source title/authorship labels remain attributed.'),
22:('coins-and-moving-lines','One背陽static, two背陰static, three背陽moving, three字陰moving; bottom-to-top casting.'),
23:('worked-coins-recognition','Six outcomes1,2,3,0,3,2backs yield7,8,9,6,9,8; primary63. Replacing circle/cross with dots recognizes original polarity, not the changed hexagram.'),
24:('second-coins-recognition-and-palaces','Six outcomes2,3,2,1,0,1backs yield8,9,8,7,6,7; primary64.乾eight-name list; recognition figure is not a change demonstration.'),
25:('palace-names','坎/艮/震/巽/離eight-name groups and their palace elements; selected list text only.'),
26:('palace-names-and-chart-anchors','坤/兌groups; named乾/姤/遯/否diagram positions, not a384-row collation.'),
27:('chart-role-anchors','Named觀/剝/晉/大有role positions completing eight乾stages; remaining diagrams not fully transcribed.'),
28:('chart-navigation','Bounded diagrams and their palace headings; not all line labels transcribed.'),
34:('diagram-context-and-author-transition','Bounded end of64chart section and prose transition; not outcome verification.'),
35:('method-context','Selected beginner/method discussion; historical assertions not promoted to product advice.'),
36:('method-context','Selected questioning/repeated-cast context only; no predictive rule compiled.'),
37:('method-context','Selected example context only; no health or death prediction compiled.'),
38:('qian-structure','Selected乾diagram and line-label context; not medical efficacy evidence.'),
43:('chart-construction-context','Selected setup preceding the43→44worked example.'),
44:('moving-lines-example','澤天夬→天風姤with lines1and6moving; six primary branch/kin labels and two changed labels.'),
45:('original-palace-kin-and-najia','Changed丑土/戌土stay兄弟relative to original坤土; write only moving-line annotations. Eight NaJia prose assignments.'),
46:('five-element-kin-matrix','All25palace-element/line-element relations in六親歌; full乾static chart as fixture.'),
47:('shi-ying-and-change','Eight乾世positions and應two intervening lines apart; source marks circle陽moving/cross陰moving. Selected chapter7examples only.'),
394:('endleaf','Logo/endleaf only; not a dated imprint.'),
}
bunits = {
2:('edition-title','Selected title-page date, compiler, corrector and文成堂imprint.'),
16:('preface-context','Selected preface/authorial critique; not modern medical guidance.'),
17:('preface-context','Selected preface continuation only.'),
19:('introductory-navigation','Selected introductory headings only.'),
20:('coins-and-palace-lists','Coin/moving-line rule and first palace-name lists; no ritual instructions adopted.'),
21:('najia-and-palace-lists','Eight NaJia chants, all48stem/branch positions; remaining palace names;世應chant begins.'),
22:('roles-and-six-spirits','歸魂世3; six-spirit starts and two explicit day-stem rows. Other rotations are derived.'),
}
records=[]
for prefix, units in [('zengshan',zunits),('bushi',bunits)]:
    for page,(kind,note) in units.items():
        p=base/f'images/{prefix}-{page}.png'
        records.append({'source':prefix,'pdfPage':page,'image':p.relative_to(base).as_posix(),
         'imageSHA256':sha(p),'readingLevel':'bounded-manual-image-reading','unit':kind,'note':note,
         'wholePageFullyTranscribed':False,'ocrUsed':False})
write('MANUAL_READINGS.json',{'date':'2026-10-27','records':records,
 'counts':{'boundedImageRecords':len(records),'zengshan':len(zunits),'bushi':len(bunits),
           'lowResolutionNavigationPages':84,'navigationContactSheetsViewed':11},
 'navigationIsNotReading':'60+24low-resolution pages/contact sheets establish only navigation. Unlisted high-resolution renders have no reading claim.',
 'remaining':'The rest of394-page B02and60-page first-book B03, complete clauses, all later books ofB03 and independent witness collation remain open.'})

palace_raw=[
 ('乾',1,'金',[1,44,33,12,20,23,35,14],['乾為天','天風姤','天山遯','天地否','風地觀','山地剝','火地晉','火天大有']),
 ('坎',6,'水',[29,60,3,63,49,55,36,7],['坎為水','水澤節','水雷屯','水火既濟','澤火革','雷火豐','地火明夷','地水師']),
 ('艮',7,'土',[52,22,26,41,38,10,61,53],['艮為山','山火賁','山天大畜','山澤損','火澤睽','天澤履','風澤中孚','風山漸']),
 ('震',4,'木',[51,16,40,32,46,48,28,17],['震為雷','雷地豫','雷水解','雷風恒','地風升','水風井','澤風大過','澤雷隨']),
 ('巽',5,'木',[57,9,37,42,25,21,27,18],['巽為風','風天小畜','風火家人','風雷益','天雷無妄','火雷噬嗑','山雷頤','山風蠱']),
 ('離',3,'火',[30,56,50,64,4,59,6,13],['離為火','火山旅','火風鼎','火水未濟','山水蒙','風水渙','天水訟','天火同人']),
 ('坤',8,'土',[2,24,19,11,34,43,5,8],['坤為地','地雷復','地澤臨','地天泰','雷天大壯','澤天夬','水天需','水地比']),
 ('兌',2,'金',[58,47,45,31,39,15,62,54],['兌為澤','澤水困','澤地萃','澤山咸','水山蹇','地山謙','雷山小過','雷澤歸妹']),
]
palaces=[{'han':h,'trigram':t,'element':e,'numbers':ns,'normalizedNames':names,
          'evidence':[{'source':'bushi','pdfPages':[20,21]},{'source':'zengshan','pdfPages':[24,25,26]}]}
         for h,t,e,ns,names in palace_raw]
write('RULES.json',{'schema':'hhc.liuyao.structural-rules.v1','date':'2026-10-27',
 'tradition':'Selected operational foundations read in the two retained editions; not a universal predictive system.',
 'palaces':palaces,'namePolicy':'Semantic hexagram identity normalized; KingWen numbers/trigram indices are editorial identifiers, not printed numerals or diplomatic allograph transcription.',
 'binaryMasksBottomLSB':[0,1,3,7,15,31,23,16],
 'binaryMaskPolicy':'Computational inference checked against64printed memberships and the actual HHC engine; not moving-line history.',
 'najia':[{'trigram':t,'han':h,'lowerBottomToTop':lo.split(),'upperBottomToTop':up.split()}
  for t,h,lo,up in [
   (1,'乾','甲子 甲寅 甲辰','壬午 壬申 壬戌'),(2,'兌','丁巳 丁卯 丁丑','丁亥 丁酉 丁未'),
   (3,'離','己卯 己丑 己亥','己酉 己未 己巳'),(4,'震','庚子 庚寅 庚辰','庚午 庚申 庚戌'),
   (5,'巽','辛丑 辛亥 辛酉','辛未 辛巳 辛卯'),(6,'坎','戊寅 戊辰 戊午','戊申 戊戌 戊子'),
   (7,'艮','丙辰 丙午 丙申','丙戌 丙子 丙寅'),(8,'坤','乙未 乙巳 乙卯','癸丑 癸亥 癸酉')]],
 'najiaEvidence':{'source':'bushi','pdfPage':21,'fragment':'納甲裝卦歌（從下裝起）','corroboration':{'source':'zengshan','pdfPages':[45,46]}},
 'branchElements':dict(zip('子丑寅卯辰巳午未申酉戌亥','水土木木土火火土金金土水')),
 'kinMatrix':{
  '金':{'金':'兄弟','土':'父母','木':'妻財','火':'官鬼','水':'子孫'},
  '水':{'水':'兄弟','火':'妻財','土':'官鬼','金':'父母','木':'子孫'},
  '土':{'土':'兄弟','火':'父母','木':'官鬼','水':'妻財','金':'子孫'},
  '火':{'火':'兄弟','水':'官鬼','土':'子孫','木':'父母','金':'妻財'},
  '木':{'木':'兄弟','水':'父母','金':'官鬼','火':'子孫','土':'妻財'}},
 'kinEvidence':{'source':'zengshan','pdfPages':[46,47],'heading':'六親歌第五','basis':'Primary hexagram palace element, including changed-line annotations; never day-master or changed hexagram palace.'},
 'stages':['本宮','一世','二世','三世','四世','五世','遊魂','歸魂'],
 'shiByStage':[6,1,2,3,4,5,4,3],'yingByStage':[3,4,5,6,1,2,1,6],
 'roleEvidence':{'source':'zengshan','pdfPage':47,'fragment':'隔世爻兩位即是應爻','explicitQianStages':True,'corroboration':{'source':'bushi','pdfPages':[21,22]}},
 'changedPolicy':{'source':'zengshan','pdfPages':[44,45],
  'fragments':['六親須照前卦而論也','餘爻不動不變不必寫出'],
  'onlyMovingLineAnnotations':True,'kinBasis':'original-palace','changedOwnPalaceIsKinBasis':False,'changedShiYingReassigned':False},
 'sixSpirits':{'order':['青龍','朱雀','勾陳','螣蛇','白虎','玄武'],
  'starts':dict(zip('甲乙丙丁戊己庚辛壬癸',['青龍','青龍','朱雀','朱雀','勾陳','螣蛇','白虎','白虎','玄武','玄武'])),
  'evidence':{'source':'bushi','pdfPage':22,'literalRowsDayStems':['甲乙','丙丁'],'otherRotations':'derived, not separately printed rows'},
  'input':'Explicit day stem only; absent input gives no spirit labels. No date-boundary/calendar adapter inferred.'},
 'consumerApplied':False,'predictionModel':None,'fullLiuYaoImplemented':False})

write('SOURCE_FIXTURES.json',{'date':'2026-10-27','orientation':'Bottom-to-top; numeric6/7/8/9 are implementation encoding of printed cross/line/circle.',
 'examples':[
  {'id':'zengshan-63-recognition','pdfPages':[23],'values':[7,8,9,6,9,8],'backsPerCast':[1,2,3,0,3,2],
   'number':63,'movingLines':[3,4,5],'derivedChangedNumber':51,'scope':'Printed coin outcomes and primary-polarity recognition only; changed51is an implementation result, not a printed changed-hexagram fixture.'},
  {'id':'zengshan-64-recognition','pdfPages':[24],'values':[8,9,8,7,6,7],'backsPerCast':[2,3,2,1,0,1],
   'number':64,'movingLines':[2,5],'derivedChangedNumber':12,'scope':'Second primary-polarity recognition example; changed12is derived, not a printed changed figure.'},
  {'id':'zengshan-43-to44','pdfPages':[44,45],'values':[9,7,7,7,7,6],'number':43,'changedNumber':44,'movingLines':[1,6],
   'palace':'坤','element':'土','shi':5,'ying':2,
   'primaryBranches':['子','寅','辰','亥','酉','未'],
   'primaryKin':['妻財','官鬼','兄弟','妻財','子孫','兄弟'],
   'changedAnnotations':[{'line':1,'branch':'丑','element':'土','kin':'兄弟'},{'line':6,'branch':'戌','element':'土','kin':'兄弟'}],
   'counterexample':'Changed hexagram44belongs to乾金; using that as kin anchor would give父母for both changed土lines, contrary to the explicit explanation.'},
  {'id':'zengshan-qian-static','pdfPages':[46],'values':[7,7,7,7,7,7],'number':1,'changedNumber':1,'movingLines':[],
   'palace':'乾','element':'金','shi':6,'ying':3,'primaryBranches':['子','寅','辰','午','申','戌'],
   'primaryKin':['子孫','妻財','父母','官鬼','兄弟','父母'],'changedAnnotations':[]}],
 'qianRoleAnchors':[{'number':n,'shi':s,'ying':y,'pdfPages':[26]if i<4 else[27]}
                   for i,(n,s,y)in enumerate(zip([1,44,33,12,20,23,35,14],[6,1,2,3,4,5,4,3],[3,4,5,6,1,2,1,6]))],
 'literalSpiritRows':[
  {'dayStems':['甲','乙'],'bottomToTop':['青龍','朱雀','勾陳','螣蛇','白虎','玄武'],'pdfPage':22},
  {'dayStems':['丙','丁'],'bottomToTop':['朱雀','勾陳','螣蛇','白虎','玄武','青龍'],'pdfPage':22}],
 'notEvidenceOf':['empirical predictive accuracy','complete384printed chart-row collation','independent textual pedigree']})
write('FUNCTIONAL_BACKLOG.json',{'date':'2026-10-27','overallStatus':'active-not-complete',
 'completedPrivateFoundation':['64palace memberships','48NaJia assignments','25kin relations based on primary palace','8世應stages','moving-line polarity and sparse changed annotations','six-spirit starts with explicit day stem'],
 'nextUnits':[
  {'id':'source-unit-map','priority':1,'work':'Enumerate every actual chapter and locate remaining first-bookB03pages; acquire later physical books only against identified gaps.'},
  {'id':'hidden-spirits','priority':2,'work':'Read complete飛伏/伏神rules and printed cases, including missing kin and primary palace source; do not implement from a heading.'},
  {'id':'calendar-strength','priority':3,'work':'Read月建/日辰/旬空/旺衰rules and boundary premises before a calendar/strength classifier.'},
  {'id':'conditional-reading','priority':4,'work':'Extract用神/原神/忌神and動變conditional clauses, exceptions and counterexamples separately for each edition.'},
  {'id':'consumer-feature','priority':5,'work':'Only integrate complete, tested result/interpretation flows with UI/save/TXT/print QA; no source/corpus exposure.'},
  {'id':'independent-witness','priority':6,'work':'Japanese six-volume catalog is a lead, not read text. Inspect a specific independent image witness for unresolved clauses/variants.'}],
 'notEstablished':['EntireB02orB03applied','Allfouruserdirectionscomplete','Predictive accuracy','NLCdirectcatalogaccess','WikisourceB03fulltext'],
 'sourceInstructionsAreData':True})
print(json.dumps({'boundedImageRecords':len(records),'retainedHTTPBodies':6,'failedTLS':2,'palaceMembers':64,'najiaPositions':48,'kinCells':25,'sourceExamples':4},ensure_ascii=False))
