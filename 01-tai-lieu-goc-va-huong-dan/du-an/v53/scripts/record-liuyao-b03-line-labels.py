from pathlib import Path
from hashlib import sha256
import json,shutil
root=Path(__file__).resolve().parent.parent;w=root.parent;base=root/'research/liuyao-b03-line-labels';stage=w/'tmp/liuyao-b03-all-annotations-staging'
base.mkdir(exist_ok=True);(base/'images').mkdir(exist_ok=True)
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(n,d):(base/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda p:sha256(p.read_bytes()).hexdigest()
manual=read(stage/'manual-source-rows.json');assert len(manual['records'])==64
manual.update(all384PrimaryStemBranchKinRowsCollated=True,all128ShiYingPositionsCollated=True,
 all384AnnotationsCollated=False,allSourceClausesApplied=False,allDiagramPolarityMarksDiplomaticallyCollated=False,
 allGuaShenLabelsCollated=False,consumerApplied=False)
for r in manual['records']:r['sourceFieldsManuallyRead']=True;r['rawImageAvailable']=True
write('PRINTED_LINE_ROWS.json',manual)
old=read(root/'research/liuyao-b03-figures/MANUAL_READINGS.json');records=[]
for r in old['records']:
 if r['pdfPage']>59:continue
 source=(root/'research/liuyao-b03-figures'/r['image']).resolve();image=source.relative_to(root/'research').as_posix()
 records.append({'pdfPage':r['pdfPage'],'image':'../'+image,'sha256':sha(source),
 'scope':'expanded-line-label-collation-stem-branch-kin-roles-hidden','newSourcePage':False,
 'entirePageDiplomaticallyTranscribed':False})
qa=[]
for n in[46,49]:
 name=f'cross-page-{n}-qa.png';shutil.copyfile(stage/name,base/'images'/name)
 qa.append({'pdfPage':n,'image':'images/'+name,'sha256':sha(base/'images'/name),'dpi':360,'actuallyViewed':True,
 'scope':'Distinguish pure-palace kin-hidden label from gua-shen;cross-page chart column alignment','newSourcePage':False})
write('MANUAL_READINGS.json',{'date':'2026-10-27','sourceID':'B03-book1-volume2',
 'sourcePDF':'../liuyao-foundations/NLC892-GBZX0301013045-259368.pdf','sourceSHA256':manual['sourcePDFSHA256'],
 'sourcePDFBytes':50191031,'sourcePDFPages':60,'records':records,'qaImages':qa,'newHTTPBodies':0,'newOriginalPDFs':0,
 'expandedEarlierSourcePages':26,'QAOnlySourceRenders':2,'figures':64,'primaryStemBranchKinRows':384,'shiYingMarkers':128,
 'hiddenKinCoordinates':sum(len(r['hidden'])for r in manual['records']),
 'splitColumnFigures':[17,18,4,34,45,54],'allSourceClausesApplied':False,'entireBookApplied':False,
 'allDiagramPolarityMarksDiplomaticallyCollated':False,'allGuaShenLabelsCollated':False,'sourceInstructionsAreData':True})
write('SOURCE_AUDIT.json',{'date':'2026-10-27','sourceID':'B03-book1-volume2','sourcePDFSHA256':manual['sourcePDFSHA256'],
 'existingRawPDFBytes':50191031,'existingRawPDFPages':60,'newHTTPBodies':0,'newOriginalPDFs':0,
 'normalizedFromDirectManualImageReading':True,'generatedSourceRowsFromRuntime':False,
 'kinAbbreviations':{'父':'父母','兄':'兄弟','官':'官鬼','財':'妻財','子':'子孫'},
 'topDownSourceChartCorrespondsToLines':[6,5,4,3,2,1],'hiddenCoordinatesAreNotGuaShen':True,
 'existingDisputedHeadingNotResolved':'噬嗑normalized title does not replace earlier literal筮reading.',
 'wholeBookApplied':False,'wholeCatalogueCompleted':False,'consumerChanged':False})
qstage=w/'tmp/liuyao-b03-question3-staging';q3=read(qstage/'PRINTED_FIXTURES.json')
q3['qaImages']=[]
for n,side in[(9,'left'),(10,'right'),(10,'left'),(11,'right')]:
 name=f'q3-p{n}-{side}-qa.png';shutil.copyfile(qstage/name,base/'images'/name)
 q3['qaImages'].append({'pdfPage':n,'image':'images/'+name,'sha256':sha(base/'images'/name),'dpi':360,'actuallyViewed':True})
q3['manualImages']=[{'pdfPage':n,'image':f'../liuyao-b03-book6/images/bushi-book6-{n:02}.png',
 'sha256':sha(root/f'research/liuyao-b03-book6/images/bushi-book6-{n:02}.png'),'scope':'Expandedquestion3fourprintedcastfixtures'}for n in[9,10,11]]
q3['sourcePDF']='../liuyao-b03-book6/NLC892-GBZX0301013045-259424.pdf'
write('BOOK6_QUESTION3_FIXTURES.json',q3)
print('Recorded64manualfigures/384primaryrows/128roles/56hidden;26sourceimagesreused/2QAcrops,noall-clauseclaim.')
