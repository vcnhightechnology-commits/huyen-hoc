from pathlib import Path
import json
d=Path(__file__).resolve().parent
write=lambda p,o:p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Literal cell entries, in printed ordinal order. Not generated from a cycle or engine.
cases=[
 (82,'南','北','乾',[('水','六煞','文曲','低'),('木','生氣','貪狼','高'),('火','五鬼','廉貞','小'),('土','天乙','巨門','高'),('金','延年','武曲','高')]),
 (83,'南','北','坎',[('金',None,None,'中'),('水','六煞','文曲','低'),('木','生氣','貪狼','高'),('火','五鬼','廉貞','低'),('土','天乙','巨門','高'),('金','延年','武曲','高')]),
 (84,'西','東','艮',[('木','六煞','文曲','低'),('木','生氣','貪狼','高'),('火','五鬼','廉貞','小'),('土','天乙','巨門','高'),('金','延年','武曲','高'),('木','六煞','文曲','低')]),
 (85,'西','東','震',[('金',None,None,'中'),('水','六煞','文曲','低'),('木','生氣','貪狼','高'),('火','五鬼','廉貞','低'),('土','天乙','巨門','高'),('金','延年','武曲','高')]),
 (86,'北','南','巽',[('土','天乙','巨門','高'),('金','延年','武曲','高'),('水','六煞','文曲','低'),('木','生氣','貪狼','高'),('火','五鬼','廉貞','小')]),
 (87,'北','南','離',[('金',None,None,'中'),('水','六煞','文曲','低'),('木','生氣','貪狼','高'),('火','五鬼','廉貞','低'),('土','天乙','巨門','高'),('金','延年','武曲','高')]),
 (88,'東','西','兌',[('金',None,None,'高'),('水','六煞','文曲','低'),('木','生氣','貪狼','高大'),('火','五鬼','廉貞','低'),('土','天乙','巨門','高'),('金','延年','武曲','高')]),
 (89,'東','西','坤',[('土','天乙','巨門','高'),('金','延年','武曲','高'),('水','六煞','文曲','低'),('木','生氣','貪狼','高'),('火','五鬼','廉貞','小'),('土','天乙','巨門','高')]),
 (90,'北','南','坤',[('水','六煞','文曲','低'),('木','生氣','貪狼','高'),('火','五鬼','廉貞','低'),('土','天乙','巨門','高'),('金','延年','武曲','高'),('水','六煞','文曲','低')]),
 (91,'南','北','艮',[('火','五鬼','廉貞','低'),('土','天乙','巨門','高'),('金','延年','武曲','高'),('水','六煞','文曲','低'),('木','生氣','貪狼','高'),('火','五鬼','廉貞','低')]),
 (92,'東','西','乾',[('木','生氣','貪狼','高'),('火','五鬼','廉貞','低'),('土','天乙','巨門','高'),('金','延年','武曲','高'),('水','六煞','文曲','低')]),
 (93,'西','東','巽',[('金','延年','武曲','高'),('水','六煞','文曲','低'),('木','生氣','貪狼','高'),('火','五鬼','廉貞','低'),('土','天乙','巨門','高'),('金','延年','武曲','高')])]
records=[{'id':f'YZSS-C{page}','sourcePDFPage':page,'sourceSitting':sit,'sourceFacing':face,'sourceGate':gate,
 'printedLayerCells':[{'ordinal':i,'sourceElement':el,'sourceLabel':label,'sourceStar':star,'sourceSizeHeightWord':height}for i,(el,label,star,height)in enumerate(cells,1)]}for page,sit,face,gate,cells in cases]
assert len(records)==12 and sum(len(x['printedLayerCells'])for x in records)==69
write(d/'MANUAL_DIAGRAM_CELLS.json',{'date':'2026-10-28','entryMethod':'Manual visual entry before formula/engine comparison; preserve blank star cells and distinct size/height words',
 'records':records,'directPrintedCells':69,'not72':'Pages82/86/92 show five numbered interior cells; others six. Six-times-twelve was an initial staging estimate, not a counted source table.',
 'sourcePageRotation180':[86,87,88,89,90,92],'allHeightOrGeometryClausesApplied':False,'sourceOutcomesValidated':False,'consumerChanged':False})
p=d/'WORK_STATE.json';obj=json.loads(p.read_text(encoding='utf-8-sig'));obj['status']='12diagrams69manualinteriorcells-awaiting-collation-and-context-tests';obj['directManualCells']=69
for x in obj['records']:
 if x['sourcePDFPage']==86:x['expandedReview']=x['expandedReview'].replace('Six numbered layers visible.','Five numbered interior cells; initial six-cell estimate corrected after rotated crop.')
write(p,obj)
print('Saved12cases/69directcells; 3five-layerdiagrams; no derived expected values yet.')
