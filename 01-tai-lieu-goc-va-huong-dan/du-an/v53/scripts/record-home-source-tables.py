from pathlib import Path
from hashlib import sha256
import json,shutil
from PIL import Image,ImageDraw
r=Path(__file__).resolve().parent.parent;w=r.parent;s=w/'tmp/home-tables-staging';old=w/'tmp/home-zhaijing-staging';b=r/'research/home-source-tables'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
assert len(read(w/'archives/v53-before-home-source-tables/PACKAGE_MANIFEST.json')['files'])==3051
b.mkdir(exist_ok=False);(b/'figures').mkdir();(r/'qa/home-source-tables').mkdir()
def write(n,d):(b/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
d=read(old/'NEXT_TOMB_MOVEMENT_DRAFT.json');d['status']='bounded-source-rule-with-explicit-traditional-coordinates';d['modernCalendarAdapterEstablished']=False
d['afterSolsticeRows']=[{'sourceYearStems':st,'pillar':pi,'movementElement':el,'avoidElement':av,'page':45}for st,pi,el,av in [('甲己','丁丑','水','土'),('乙庚','己丑','火','水'),('丙辛','辛丑','土','木'),('丁壬','癸丑','木','金'),('戊癸','乙丑','金','火')]]
write('TOMB_MOVEMENT_ROWS.json',d)
for src,dest in [('NEXT_TOMB_NAYIN_PROBE.json','PRIOR_TOMB_PROBE.json'),('NEXT_EIGHT_PALACES_NAMES.json','FIGURE_NAMES.json'),('NEXT_EIGHT_PALACES_PROBE.json','PRIOR_NAME_PROBE.json')]:shutil.copy2(old/src,b/dest)
fig=read(s/'MANUAL_FIGURES.json');assert fig['manualGlyphs']==384 and all(x['directVisualQA']for x in fig['records'])
for rec in fig['records']:
 shutil.copy2(s/rec['file'],b/'figures'/rec['file']);rec['file']='figures/'+rec['file']
for page,palaces in [(107,['艮','坎','乾']),(108,['兌','坤','離','巽','震'])]:
 sheet=Image.new('RGB',(len(palaces)*200,2000),'#e7e0d2');draw=ImageDraw.Draw(sheet)
 for rec in[x for x in fig['records']if x['page']==page]:
  col=palaces.index(rec['palace']);row=rec['stage'];crop=Image.open(b/rec['file']);sheet.paste(crop,(col*200+15,row*250+27));draw.text((col*200+15,row*250+7),f'{page} C{col+1} R{row+1}',fill='black')
 sheet.save(b/f'figures-{page}-sheet.png')
write('MANUAL_FIGURES.json',fig)
for n in[49,50]:shutil.copy2(s/f'p{n}-upright.png',b/f'p{n}-upright.png')
pages=[41,42,43,44,45,46,47,49,50,51,52,107,108]
write('MANUAL_READINGS.json',{'date':'2026-10-27','source':'v53/research/full-study/home/CADAL06056503.djvu','sourceSHA256':'bfd3b76c55d62324919ab161c8c2ba2ecb129b3b2c59a3ab0428807e8f8278db',
 'newSourcePages':0,'expandedPreviouslyReadPages':13,'newHTTPRequests':0,'newOriginalContainers':0,
 'readings':[{'page':n,'file':f'v53/research/home-you-nian/images/p{n:03}.png','sha256':sha(r/f'research/home-you-nian/images/p{n:03}.png'),'scope':'Movement premise/printedrow/example or64figureglyph-and-name collation; wholebooknotapplied.'}for n in pages],
 'qaDerivatives':[{'file':f'p{n}-upright.png','sourceFile':f'v53/research/home-you-nian/images/p{n:03}.png','transform':'transposeROTATE_90(noresampling)','sha256':sha(b/f'p{n}-upright.png')}for n in[49,50]],
 'nativeCrops':64,'nativeScaleContactSheets':2,'orientationDerivatives':2,'sourceInstructionsAreData':True,'allApplicationClausesExtracted':False,
 'correctionToPreviousNotes':'The printed term is尅/克 (overcoming), not冠/crown. Previous Englishyearmonth冠/crown wording is a research-note misreading, superseded here, not a sourcevariant or consumerbug.'})
write('OVERCOMING_RULE.json',{'sourceImages':[50,51,52],'sourceHeading':'年月尅山家','correctedSourceTerm':'尅','supersedesPreviousResearchTerm':'冠/crown',
 'sourceConditions':[{'code':'new-dwelling','source':'新建宅舍','applicable':True},{'code':'new-grave','source':'新立墳塋','applicable':True},
 {'code':'repair-foundation-unchanged','source':'拆修豎造不動地基','applicable':False},{'code':'burial-existing-grave','source':'舊塋附葬','applicable':False}],
 'rule':'Explicit year/month/day/hourpillar NaYin element controls the selectedmountain movementelement. Elements andcalendarcoordinates mustbeexplicit; no dateadapter orpracticaloutcome.',
 'printedExamples':[{'yearPillar':'甲子','candidatePillars':['甲子'],'context':'year','expectedMountainGroup':'water-earth','pages':[50]},
 {'yearPillar':'甲子','candidatePillars':['丙寅','丁卯'],'context':'month','expectedMountainGroup':'metal','pages':[50]},
 {'yearPillar':'甲子','candidatePillars':['戊辰','己巳'],'context':'month','expectedMountainGroup':'wood','pages':[50,51]},
 {'yearPillar':'甲子','candidatePillars':['庚午','辛未'],'context':'month','expectedMountainGroup':None,'pages':[51]},
 {'yearPillar':'甲子','candidatePillars':['壬申','癸酉'],'context':'month','expectedMountainGroup':'water-earth','pages':[51]},
 {'yearPillar':'甲子','candidatePillars':['丙子','丁丑'],'context':'month','expectedMountainGroup':'fire','pages':[51]},
 {'yearPillar':'壬申','candidatePillars':['壬申'],'context':'year-before-solstice','expectedMountainGroup':None,'pages':[51]},
 {'yearPillar':'壬申','candidatePillars':['壬申'],'context':'year-after-solstice-source-chou','expectedMountainGroup':'metal','pages':[51,52]}],
 'dayHourExtension':'Page52 says日尅時尅山家俱倣此; only relation with explicitly supplied NaYin,not a newcalendaradapter.',
 'diagram49WholeCellCollation':False,'consumerChanged':False,'wholeCatalogueCompleted':False})
print('Recorded20base/5solstice rows,384manualglyphs,64names and8printedexamplegroups; 尅/crown note corrected separately.')
