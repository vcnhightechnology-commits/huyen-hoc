from pathlib import Path
from hashlib import sha256
import json,re,shutil

r=Path(__file__).resolve().parent.parent;w=r.parent;s=w/'tmp/bazi-jianlu-conditions-staging';b=r/'research/bazi-jianlu-context';q=r/'qa/bazi-jianlu-context'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda p:sha256(p.read_bytes()).hexdigest()
assert len(read(w/'archives/v53-before-bazi-jianlu-context/PACKAGE_MANIFEST.json')['files'])==3188
b.mkdir(exist_ok=False);q.mkdir(exist_ok=False)
def write(name,data):(b/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for name in['RETAINED_DIGITAL_SECTION.txt','DIGITAL_CROSSREF_LU.txt','DIGITAL_CROSSREF_BLADE.txt','CROSSREF_READINGS.json','p226-ending.png','ENDING_RENDER.json','SOURCE_EXAMPLE_PROBE.json']:
 shutil.copy2(s/name,b/name)
contexts=read(s/'CONDITIONAL_CONTEXTS.json')
raw=(s/'RETAINED_DIGITAL_SECTION.txt').read_text(encoding='utf-8');chars=[];folios=[];current='005-110b'
for part in re.split(r'(<pb:[^>]+>)',raw):
 if part.startswith('<pb:'):current=part.split('WYG_')[1].rstrip('>')
 else:
  part=re.sub(r'¶|\s','',part);chars.extend(part);folios.extend([current]*len(part))
prefix=''.join(chars).index('建禄者');folios=folios[prefix:];body=''.join(chars)[prefix:]
assert len(body)==1223 and body==''.join(x['retainedDigitalText']for x in contexts['units'])
sourceImages={'005-110b':218,'005-111a':219,'005-111b':220,'005-112a':221,'005-112b':222,'005-113a':223,'005-113b':224,'005-114a':225}
structural={'definition','visible-year-hour','ten-hour-alternatives'}
historical={'generic-source-outcomes','luck-peer-claim','jia-yin-case','ding-wu-baseline','wu-si-baseline','xin-you-baseline','printed-example','comparative-school-comment','same-family-comment','recent-pattern-comment'}
quoted={'root-flower-quote','dubu-quote','another-verse','baizhang-quote','gui-winter-verse','yuanming-quote'}
for x in contexts['units']:
 fs=list(dict.fromkeys(folios[x['digitalStart']:x['digitalEndExclusive']]));x['retainedDigitalFolios']=fs;x['sourceImages']=[sourceImages[f]for f in fs]
 if x['id']in structural:
  x['dispositionStatus']='bounded-structural-projection-in-functional-candidate'
  x['functionalConditionsFullyCompiled']=False
  x['implementation']='Definition/year-hour projection is a functionally tested candidate, not deployed. Prior ten-hour matcher remains private. No full pattern or outcome classifier.'
 elif x['id']in historical:x['dispositionStatus']='source-history-and-unvalidated-outcome-retained-private'
 elif x['id']in quoted:x['dispositionStatus']='quoted-source-voice-retained-private-not-universal-rule'
 else:x['dispositionStatus']='explicit-conditional-branch-retained-unquantified-premises-open'
contexts.update(status='44-contiguous-digital-contexts-with-native-span-anchors-and-explicit-dispositions',allSourceImageCharactersCollated=False,wholeSectionApplied=False,
 structuralProjectionUnits=3,wholeCatalogueCompleted=False)
write('JIANLU_CONTEXTS.json',contexts)
write('TARGETED_NATIVE_PASSAGES.json',{'date':'2026-10-27','readings':[
 {'image':221,'folio':'005-112a','text':'歳月若是火多及或印綬雖無財官主吉','contextID':'wu-fire-seal-exception','consequence':'Do not apply a blanket 财官-required verdict to this entire source section.'},
 {'image':224,'folio':'005-113b','text':'是見煞取貴然亦不可太多','contextID':'too-many-kills','consequence':'宜 does not establish unconditional success; 太多 threshold unspecified.'},
 {'image':224,'folio':'005-113b','text':'提綱建禄將何取須看年時多透露局中六格自分明莫泥提綱反為悮','contextID':'baizhang-quote','consequence':'Look beyond month to year/hour visibility; no count-based selection.'},
 {'image':198,'folio':'005-100b','text':'惟甲丙戊庚壬五陽干有刃乙丁己辛癸五陰干無刃故曰陽刃','consequence':'Named five-yang school; not a universal ten-stem table.'},
 {'image':202,'folio':'005-102b','coordinateExtracts':['戊日刃在午','庚日刃在酉','壬日刃在子','甲日刃在卯','丙日刃在午'],'excerptType':'discontinuous-coordinate-extracts-not-a-continuous-quotation','consequence':'Five directly stated coordinates; prediction and adjacent exceptions remain separate.'}],
 'directVisualQA':True,'sourceInstructionsAreData':True,'outcomesValidated':False})
write('BLADE_TABLES.json',{'sourceInstructionsAreData':True,'tables':[
 {'system':'WYG003-quoted-eight-blade-coordinates','tier':'retained-digital-only','sourceFile':'v53/research/four-items/sources/KR3g0042_003.txt','sourceSHA256':sha(r/'research/four-items/sources/KR3g0042_003.txt'),
  'folio':'003-56a','sourceVoice':'希尹曰 as quoted in 論羊刃; not independently verified attribution',
  'rows':[{'stem':st,'branch':br}for st,br in[('甲','卯'),('乙','辰'),('丙','午'),('丁','未'),('庚','酉'),('辛','戌'),('壬','子'),('癸','丑')]],
  'unstatedStems':['戊','己'],'explicitlyExcludedStems':[],
  'sourceCaveat':'The section later distinguishes 子平五陽干有刃/五陰干無刃 and points to the later 陽刃 chapter. Preserve named voices.'},
 {'system':'WYG005-five-yang-blade-coordinates','tier':'native-facsimile-targeted-passages','sourceImages':[198,202],
  'rows':[{'stem':st,'branch':br}for st,br in[('甲','卯'),('丙','午'),('戊','午'),('庚','酉'),('壬','子')]],
  'unstatedStems':[],'explicitlyExcludedStems':['乙','丁','己','辛','癸'],
  'sourceCaveat':'Coordinates are not complete blade-pattern qualification; chapter204 has an apparent-pair exception.'}],
 'dateOrStemAnchorInferred':False,'practicalOutcome':None,'wholeSectionApplied':False})
manifest={'date':'2026-10-27','sourceContainer':'v53/research/bazi-pattern-witness/CADAL06066041.djvu','sourceSHA256':'013ce4861680a2bf08b811050c45a45bb2d3ce9d164f7e2341d7070bd5cb2c1a',
 'decoder':'v53/research/bazi-pattern-extension/tooling/djvu.js','decoderSHA256':'10a831d62cc7ced39c30c7350a11410402d082a0f0a5b073a88d3d7ca662add3',
 'retainedDigital':[{'file':f'v53/research/four-items/sources/KR3g0042_{v:03}.txt','sha256':sha(r/f'research/four-items/sources/KR3g0042_{v:03}.txt')}for v in[3,5]],
 'nativeImages':[{'image':n,'file':f'v53/research/bazi-pattern-extension/images/p{n:03}.png','sha256':sha(r/f'research/bazi-pattern-extension/images/p{n:03}.png'),'directVisualQA':True}for n in[198,202]+list(range(218,226))],
 'newEndTitlePage':read(b/'ENDING_RENDER.json'),'expandedPreviouslyReadPages':10,'newSourcePages':1,'newConditionalContentPages':0,'newHTTPRequests':0,'newOriginalContainers':0,
 'sourceTierLimits':'Volume5 native readings; volume3 digital only. End page226 confirms boundary, not an extra conditional-content page. No attribution/outcome verification.'}
assert sha(w/manifest['sourceContainer'])==manifest['sourceSHA256'];write('SOURCE_MANIFEST.json',manifest)
print('Recorded44 bounded contexts, two named blade tables,10 expanded native pages and one end-title page; no new HTTP or container.')
