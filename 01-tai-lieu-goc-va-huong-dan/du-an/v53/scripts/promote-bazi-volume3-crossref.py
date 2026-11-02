from pathlib import Path
from hashlib import sha256
import json, shutil
from PIL import Image

w=Path(__file__).resolve().parents[2]
b=w/'v53/research/bazi-jianlu-context'
s=w/'tmp/bazi-volume3-staging'
d=b/'volume3'
assert not d.exists(), 'One-shot promotion; never overwrite retained source packet'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda p,o:p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda p:sha256(p.read_bytes()).hexdigest()
d.mkdir()
for name in ['CADAL06066039.djvu','commons-description.html','IDENTITY.json','REQUESTS.json','RENDERS.json','p018-entity-crop.png','fetch.mjs','render.mjs']:
 shutil.copyfile(s/name,d/name)
shutil.copytree(s/'images',d/'images')
identity=read(d/'IDENTITY.json')
assert sha(d/'CADAL06066039.djvu')==identity['actualSHA256']=='2334006e3a46b16bdbf0bf6a79512d8d0c4b87a2ce2e8e1ff503121d8f2cffdc'
# Fetch/render logs describe their state at creation and remain byte-identical.
# Manual reading status is a separate, later record, not an alteration of logs.
renders=read(d/'RENDERS.json')
readings=[]
for x in sorted(renders['records'],key=lambda x:x['page']):
 page=x['page']
 if page==2:
  folio=None; classification='title-and-proofreader-paratext';scope='三命通會卷三 / 四庫全書 title; not proof of historical authorship'
 elif 3<=page<=18:
  folio=f"003-{(page-1)//2}{'a' if page%2 else 'b'}";classification='section-content';scope='論十干祿 first whole-range reading; not every character or condition compiled'
 elif page==19:
  folio='003-9a';classification='next-heading-boundary';scope='論金轝 begins; no claim its whole contents were applied'
 else:
  folio=f"003-{(page-1)//2}{'a' if page%2 else 'b'}";classification='section-content';scope='論羊刃 first whole-range reading; p119 includes next論空亡 heading, not its contents'
 readings.append({'page':page,'folio':folio,'file':x['file'],'sha256':x['sha256'],'directVisualRead':True,'classification':classification,'readScope':scope,'allCharactersCollated':False})
crop=d/'p018-entity-crop.png'
original=Image.open(d/'images/p018.png').convert('RGBA')
im=Image.open(crop).convert('RGBA')
box=[450,1300,850,2820]
assert original.crop(box).tobytes()==im.tobytes()
packet={
 'date':'2026-10-27','sourceInstructionsAreData':True,
 'container':'volume3/CADAL06066039.djvu','containerSHA256':identity['actualSHA256'],
 'sourceTier':'native-facsimile-with-identified-digital-crossreference',
 'downloadRecord':'volume3/REQUESTS.json','renderRecord':'volume3/RENDERS.json',
 'manualReadingFollowsRenderLogs':True,'directVisualPositions':26,'sectionContentPositions':24,'paratextOrBoundaryPositions':2,
 'readings':readings,
 'sectionRanges':[{'heading':'論十干祿','pages':list(range(3,19)),'firstFolio':'003-1a','lastFolio':'003-8b','wholeRangeFirstRead':True,'wholeSectionApplied':False},
                  {'heading':'論羊刃','pages':list(range(112,120)),'firstFolio':'003-55b','lastFolio':'003-59a','wholeRangeFirstRead':True,'wholeSectionApplied':False}],
 'targetedCollations':[
  {'id':'lu-ten-coordinates','pages':[3,4],'reading':'甲寅 乙卯 丙巳 丁午 戊巳 己午 庚申 辛酉 壬亥 癸子','normalization':'Role-aware canonical 巳 branch / 己 stem; preserve raw digital bytes and log variants separately.','disposition':'Ten coordinates corroborate existing source table; not another date/strength validation.'},
  {'id':'lu-element-referents','pages':[4],'reading':'如甲見丙寅甲土尅丙水為財','disposition':'Literal 甲土/丙水 preserved. Do not substitute modern 甲木/丙火 or equate 財 with the modern day-stem TenGod automatically.','transformedElementsExplanationEstablished':False},
  {'id':'lu-illustrated-combinations','pages':[13,14],'reading':'甲祿寅+亥明合;無寅得亥暗合;無寅見丑卯兩傍虛拱;寅又見丑卯兩傍實拱','disposition':'Private branch-membership projection for explicitly illustrated 甲 only; source phrase兩傍 positional sufficiency remains unverified; no extension to ten stems or outcome.'},
  {'id':'lu-not-automatic-outcome','pages':[14,18],'discontinuousExtracts':['凡人命帶祿或吉或凶或貴或賤未可全靠便為吉論','大抵命入格合造化亦不專在祿上'],'disposition':'Blocks unconditional good/bad outcome implementation.'},
  {'id':'eight-blade-coordinates','pages':[113],'reading':'甲卯 乙辰 丙午 丁未 庚酉 辛戌 壬子 癸丑','explicitRows':8,'unstatedStems':['戊','己'],'disposition':'Native confirmation of eight sentences quoted under希尹; not inferred ten-stem completion.'},
  {'id':'school-distinction','pages':[118,119],'reading':'子平以甲丙戊庚壬五陽干有刃乙丁己辛癸五陰干無刃','continuation':'其義見後論陽刃格中','disposition':'Named source voice explains two tables; not independent historical attribution or a merged coordinate system.'}
 ],
 'entityCollation':{'retainedDigitalFile':'DIGITAL_CROSSREF_LU.txt','retainedEntity':'&KR0339;','page':18,'folio':'003-8b','nativeReading':'嗤','context':'虛名虛譽足堪嗤是嫌亡也','nativeCrop':'volume3/p018-entity-crop.png','cropBox':box,'cropSHA256':sha(crop),'rawDigitalUnchanged':True,'otherWitnessesCollated':False},
 'remaining':['50 Lu-pillar labelled entries and their qualifiers have been seen in pages5–8 but not completely transcribed/compiled.','Other subsidiary clauses, strength, interacting source methods and actual positional semantics remain open.','Same WYG source family; independent edition/genealogy not established.'],
 'independentEditionEstablished':False,'all230PagesRead':False,'allSourceImageCharactersCollated':False,'wholeWorkApplied':False,
 'newHTTPResponses':2,'httpStatuses':[200,200],'newOriginalContainers':1,'normalTLSVerified':True
}
write(b/'FACSIMILE_CROSSREF_READINGS.json',packet)
manifest=read(b/'SOURCE_MANIFEST.json')
manifest.update({'volume3':{'directory':'volume3','identity':'volume3/IDENTITY.json','manualReadings':'FACSIMILE_CROSSREF_READINGS.json','sourceSHA256':identity['actualSHA256'],'bytes':identity['actualBytes'],'actualContainerPages':230,'newSourcePages':26,'sectionContentPositions':24},
 'newSourcePages':27,'newConditionalContentPages':24,'newHTTPRequests':2,'newOriginalContainers':1,
 'sourceTierLimits':'Volume5 native targeted reading and 44 digital contexts; volume3 first reading of24 content positions+2 paratext/boundary. Targeted native collation only. Not whole230 pages, full chapter application, independent edition or outcome validation.'})
write(b/'SOURCE_MANIFEST.json',manifest)
tables=read(b/'BLADE_TABLES.json')
t=tables['tables'][0]
t.update({'tier':'native-facsimile-targeted-passages','retainedDigitalFile':t['sourceFile'],'retainedDigitalSHA256':t['sourceSHA256'],'sourceFile':'v53/research/bazi-jianlu-context/volume3/CADAL06066039.djvu','sourceSHA256':identity['actualSHA256'],'sourceImages':[113],'namedSchoolClarificationImages':[118,119]})
write(b/'BLADE_TABLES.json',tables)
print(json.dumps({'promotedContainerBytes':identity['actualBytes'],'newNativeReadPositions':26,'targetedBladeRows':8,'entityReading':'嗤','wholeWorkApplied':False},ensure_ascii=False))
