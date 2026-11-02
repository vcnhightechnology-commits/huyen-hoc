from pathlib import Path
import hashlib,json,re
root=Path(__file__).resolve().parent.parent
out=root/'research/library-audit'
r=out/'new-sources'
def clean(path):
    s=path.read_text(encoding='utf-8')
    s='\n'.join(x for x in s.splitlines() if not x.startswith('#'))
    return re.sub(r'[^\u3400-\u9fff\U00020000-\U0002fa1f]','',re.sub(r'<pb:[^>]+>','',s))
a=clean(r/'KR3g0019-KR3g0019_001.txt')
b=clean(r/'KR5a0294-KR5a0294_001.txt')
pairs=[
 {'id':'opening','wyg':'夫宅者乃是隂陽之樞紐人倫之軌模','hfl':'夫宅者乃是陰陽之樞紐人倫之軌模','observation':'隂/陰 differs in this opening. Kept literally, no blanket character conversion.'},
 {'id':'ability-wording','wyg':'非夫博物明賢而能悟斯道也','hfl':'非夫博物明賢無能悟斯道也','observation':'而/無 changes the recorded wording. Without matching facsimile pages, do not declare which is an OCR error or repair either text.'},
 {'id':'analogy','wyg':'猶藥病之效也','hfl':'猶樂病之效也','observation':'藥/樂 differs in the recorded transcription. Requires image checking before editorial correction.'}
]
for p in pairs:
    p['locatedInWYG']=p['wyg'] in a;p['locatedInHFL']=p['hfl'] in b
    assert p['locatedInWYG'] and p['locatedInHFL'],p['id']
record={'schema':'hhc.zhaijing.selected-transcription-collation.v1','date':'2026-10-25','sourceRevisions':json.loads((r/'REVISIONS.json').read_text(encoding='utf-8')),'pairs':pairs,'metadataCaution':'KR5a0294 labels BASEEDITION/WITNESS HFL and its Readme maps HFL to 涵芬樓版, but its SOURCE header mentions 三家本 1988. This edition attribution has not been independently reconciled against images. KR3g0019 WYG attribution is also maintainer metadata, not an authenticated original manuscript.','scope':'Three selected comparisons in volume 1, not a full-book collation or assessment of feng shui effects. These transcriptions are supplemental research evidence and are not introduced as user-facing room rules.','byteFiles':[{'file':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(r.glob('KR*.txt'))]}
(out/'TEXT_WITNESS_CHECK.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Located three selected comparisons in both immutable text witnesses.')
