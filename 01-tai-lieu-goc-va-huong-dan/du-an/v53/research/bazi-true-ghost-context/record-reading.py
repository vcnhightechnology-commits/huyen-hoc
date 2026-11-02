from pathlib import Path
from hashlib import sha256
from PIL import Image
import json,re
S=Path(__file__).resolve().parent;W=S.parent.parent
def save(n,d):(S/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def ident(p):return {'file':p.relative_to(S if p.is_relative_to(S) else W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
records=[]
for i in range(19,24):
 p=S/f'p{i}.png'
 with Image.open(p) as im:records.append({'page':i,'printedLeaf':f'{(i-1)//2}{"a" if i%2 else "b"}',**ident(p),'width':im.width,'height':im.height,'pixelRGBA_SHA256':sha256(im.convert('RGBA').tobytes()).hexdigest(),'actuallyViewed':True,'scope':'First-pass whole native image; selected source clauses below, not full diplomatic glyph collation.'})
save('NATIVE_REVIEW.json',{'source':ident(W/'v53/research/bazi-pattern-witness/CADAL06066041.djvu'),'decoder':ident(W/'v53/research/bazi-pattern-extension/tooling/djvu.js'),'records':records,'positionsActuallyViewed':list(range(19,24)),'newHTTPBodies':0,'newIndependentWitnesses':0,'sameTextualFamilyAsDigital':True,'fullChapterRead':False})
p=W/'v53/research/bazi-relations/sources/KR3g0042_005.txt';raw=p.read_text(encoding='utf-8-sig');a=raw.index('又云㸔官星有天');z=raw.index('喜忌篇云',a);extract=raw[a:z];(S/'DIGITAL_CONTEXT.txt').write_text(extract,encoding='utf-8');clean=re.sub(r'[\s¶]','',re.sub(r'<pb:[^>]+>','',extract));(S/'CONTEXT_CLEAN.txt').write_text(clean,encoding='utf-8')
anchors=[('又云㸔官星有天','天官鄉:月干制歲干'),('有地官鄉','地官鄉:月建制歲干'),('有真官鄉','真官鄉:命前三辰/月干與命干合'),('又云術者以甲見辛','真五行克納音;notordinary甲辛alone'),('干頭自見官','source-preference-with-combination-and-諸神'),('如甲寅生納音','literal-example甲寅/己亥'),('若不見太嵗本干克','alternative日月時乙庚scope'),('若止見庚','source偏官partial-configuration'),('又不見乙庚','partial-alternatives乙巳乙丑乙酉/申'),('餘倣此','analogy-not-full-table'),('又如己酉己卯','two-pair-true-ghost-counterexamples'),('大小運流年','historical-prediction-kept-private')]
starts=[];pos=0
for literal,role in anchors:
 i=clean.index(literal,pos);starts.append((i,role));pos=i+len(literal)
units=[{'id':f'T{i:02d}','literalDigital':clean[a:starts[i+1][0] if i+1<len(starts) else len(clean)],'role':r,'implemented':False} for i,(a,r) in enumerate(starts)]
save('CONTEXT_DISPOSITIONS.json',{'digitalSource':ident(p),'editorialUnits':len(units),'cleanCodepoints':len(clean),'cleanSHA256':sha256(clean.encode()).hexdigest(),'records':units,'selectedNativeReadings':[{'page':21,'digital':'甲巳為真土','native':'甲己為真土','resolution':'Role-based native reading記己;digital bytes unchanged;no source correction or all-glyph collation claimed.'},{'page':21,'native':'己酉己卯見丁壬壬子壬午見乙庚','resolution':'Two source examples remain separately anchored; original stem also overcome is completed on22.'},{'page':22,'native':'同受克故不作真官而作真鬼斷之','resolution':'Source conclusion requires cross-page antecedent;no isolatedkeywordalias.'}],'wholeChapterApplied':False})
save('WORK_STATE.json',{'date':'2026-10-29','status':'native-context-first-pass-selected-clauses-recorded;implementation-not-started','catalogueID':'M01','sourceContainer':'v53/research/bazi-pattern-witness/CADAL06066041.djvu','positionsActuallyViewed':list(range(19,24)),'editorialUnits':12,'newHTTPBodies':0,'newContainers':0,'newIndependentWitnesses':0,'newEngineCalls':0,'wholeChapterRead':False,'wholeChapterApplied':False,'publicProductChanged':False,'integratedIntoRelease':False,'finding':'Page21–22 distinguishes真五行克納音and本干同受克withdifferenttrue-official/true-ghostconclusions. This is a separate source framework;cannotrenameordinaryten-godlabels.','sourceLimits':['Fulltrue-five-elementtableandwhichsingle/pair configuration counts ascomplete.','若不見太歲本干克branch,乙庚in日月時andpartial庚/乙支alternatives require nestedconditionmodels,notpresencethresholds.','Whetherandhowthisvolume5frameworkconnectstovolume2harmtrue-ghostphrases remainsunestablished.','No source fortune/health/mortality/rank predictions validated.'],'next':['Read/crop selected21–22columns and preserve RGB identities;write manual expected examples before implementation.','Use retained actual table calls when they already cover required pillars/stems;run a new pinned batch only for a new comparison.','Keep namedtrue官鄉separate fromtrue五行官/鬼;no automaticyear/day/calendar adapter.','Continue三刑from214independently if this framework lacks explicit premises.']})
(S/'README.md').write_text('''# 真官/真五行/真鬼: nguồn quyển5 đang đọc

Năm vị trí native19–23/tờ9a–11a đã xem từ container có sẵn;không tải mới hoặc engine mới. Đây là khoảng ngữ cảnh trong論正官,chưa đọc/áp trọn chương. Bản số giữ riêng,12đơn vị biên tập phân biệt天官鄉,地官鄉,真官鄉và lời真五行克納音. Ảnh21cho甲己為真土khácglyph甲巳củabảnsố;giữbytegốc,chỉghiđọcrõtheovaitrò.

Câu同受克故不作真官而作真鬼斷之ở22kếthừahai ví dụ己酉/己卯見丁壬và壬子/壬午見乙庚ở21. Cần giữ vai命干/太歲/日月時,nhánh thay thế/khuyết và hệ真五行riêng. Chưa đủ căn cứ gán một can thường thành真鬼,tự chấm lực三五分hoặc coi nhãn này đồng nghĩa Thất Sát hiện hành. Chưa nối tự động quy tắc này vào午帶丑干真鬼của六害.

Chưa freeze kỳ vọng,chưa triển khai hàm hoặc promote. Tiếp crop/đối21–22 và khép tiền đề theo từng giọng;đừng lặp tải/render19–23 hoặc cộng lượt nhìn ảnh thành chương hoàn tất. Toàn bộ phần này là công việc dở ngoài site.
''',encoding='utf-8')
print(json.dumps({'positionsActuallyViewed':5,'editorialUnits':12,'implementationStarted':False,'newEngineCalls':0}))
