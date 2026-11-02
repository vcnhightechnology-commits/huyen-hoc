from pathlib import Path
from hashlib import sha256
from PIL import Image
import json
w=Path(__file__).resolve().parents[2];d=Path(__file__).resolve().parent
base=w/'v53/research/home-yangzhai-shishu'
old=json.loads((base/'RAW_STREAMS.json').read_text(encoding='utf-8-sig'))
notes={
82:'坐南朝北開乾門; 乾gate source marking屬土/四隅門 not generic乾palace金. Chart numbered1–5, not six at this page. Prose warns頭一層房朝內or朝外changes origin; read before any automated layer seed.',
83:'坐南朝北開坎門;門mark屬金/四正門. Six numbered layers;圖topnumber6. Prose貪狼不宜中宮 and進/height/side choices require separate coordinates. No modern vertical-floor adapter.',
84:'坐西朝東開艮門. Six numbered layers; gatecornerlabel土. Source房朝裏/朝外 affects count, treats沖字avoidance. Manually enter each printed height before comparing derivedcycle.',
85:'坐西朝東開震門. Six layer table visible; gate金. Prose木入中宮宜詳之; sourcefirstlayer金withoutnamedstar, not automatically伏位assigned.',
86:'坐北朝南開巽門. Drawing glyphs rotated180relativeprose. Needlosslessderivedrotationforcellcollation; rawfileandactualpapercoordinateskept. Six numbered layers visible.',
87:'坐北朝南開離門. Drawing rotated180relativeprose. Sourcefourfavorableheightgroupsand坐上differentfromgate; avoidtreatinggatep alacelabelasidenticaltocourtyardsequence.',
88:'坐東朝西開兌門. Drawing rotated180. Proseone/three/highplusfive/sixmaydifferif天乙巨門condition. Needkeepmainlabels,separatepalaceheightsandprosevariants.',
89:'坐東朝西開坤門. Drawing rotated180. Prose1/2/4/6higherand乾兌favorable; nogenericuniversalheightstarfromfirstpass.',
90:'坐北朝南開坤門. Drawing rotated180. Prose2/4/5higherplus乾兌; gate/sourceoriginmustremainexplicit.',
91:'坐南朝北開艮門. Six layer table; first火五鬼low, sourceprose2/3/5higherplus乾兌. Do not globallylabelthefirstlayeraswater.',
92:'坐東朝西開乾門. Drawing rotated180. Sourceprintedsixlayercoordinatepatternmustbemanuallyentered, not copiedfromsamegate82because坐/向different.',
93:'坐西朝東開巽門. Prose1/3/5/6higher; explicit ordered進waterwoodfireearthmetalexampleandten進extension. Firstlayerdependscase, rawpresence/gateonlynotenough.'
}
records=[]
for n,note in notes.items():
 x=next(x for x in old['records']if x['pdfPage']==n);p=base/x['file'];data=p.read_bytes();assert sha256(data).hexdigest()==x['sha256']
 records.append({'sourcePDFPage':n,'file':p.relative_to(w).as_posix(),'bytes':len(data),'sha256':x['sha256'],'nativeSize':list(Image.open(p).size),'fullRawImageActuallyViewed':True,'newSourceReadPosition':False,'expandedReview':note.replace('gatep alace','gatepalace')})
out={'date':'2026-10-28','catalogueID':'P08','status':'12retainedrawpositions-expanded-review-72cells-notyetfullytranscribed','newHTTPRequests':0,'newSourcePositions':0,'newOriginalContainers':0,'records':records,'sourceCaseDiagrams':12,'allCellTranscriptionOrConditionsComplete':False,'consumerChanged':False,'wholeCatalogueCompleted':False,'next':['Prepare lossless rotated diagram crops86–90/92; preserve pixel coordinate transform.','Enter each actual layer number, element, star and height independently before deriving cycle.','Keep gateelement label distinct frompalacetrigram;頭房towardinside/outsideandwall/doorboundariesarestillrequired.']}
(d/'WORK_STATE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Recorded 12 actual expanded raw views; 0 new source positions; courtyard scope active.')
