from pathlib import Path
import json
r=Path(__file__).resolve().parent.parent
p=r/'research/bazi-jianlu-context/TARGETED_NATIVE_PASSAGES.json'
d=json.loads(p.read_text(encoding='utf-8'));x=d['readings'][-1]
x.pop('text',None)
x['coordinateExtracts']=['戊日刃在午','庚日刃在酉','壬日刃在子','甲日刃在卯','丙日刃在午']
x['excerptType']='discontinuous-coordinate-extracts-not-a-continuous-quotation'
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
edits=[
 ('bazi-cycles.js','${monthStems(a)}<div class="bazi-dayun-block">',"${monthStems(a)}${window.HHC_BAZI_MONTH_CONTEXT?window.HHC_BAZI_MONTH_CONTEXT.render(r):''}<div class=\"bazi-dayun-block\">"),
 ('index.html','<script src="bazi-cycles.js"></script>','<script src="bazi-month-context.js"></script>\n<script src="bazi-cycles.js"></script>'),
 ('scripts/build.mjs',"'bazi-relations.js','bazi-cycles.js'","'bazi-relations.js','bazi-month-context.js','bazi-cycles.js'")
]
for name,old,new in edits:
 p=r/name;s=p.read_text(encoding='utf-8');assert s.count(old)==1,name;p.write_text(s.replace(old,new),encoding='utf-8')
print('Integrated optional month context after hidden-stem reading; engine and existing cycle inspection untouched.')
