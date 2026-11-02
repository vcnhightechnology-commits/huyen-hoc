from pathlib import Path
from hashlib import sha256
import json,re
from PIL import Image

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/bazi-lu-labels';q=r/'qa/bazi-lu-labels'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda p:sha256(p.read_bytes()).hexdigest()
m=read(b/'SOURCE_MANIFEST.json');t=read(b/'SOURCE_ROWS.json');ctx=read(b/'LU_SECTION_CONTEXTS.json');storage=read(b/'LU_STORAGE_TABLE.json')
assert sha(w/m['sourceContainer'])==m['sourceSHA256']
assert sha(w/m['retainedDigitalFile'])==m['retainedDigitalSHA256']
old=read(r/'research/bazi-jianlu-context/volume3/RENDERS.json')
for x in m['nativePages']+[m['additionalRetainedNativeContextPage']]:
 assert sha(w/x['file'])==x['sha256']
 render=next(y for y in old['records']if y['page']==x['page'])
 im=Image.open(w/x['file']);assert im.mode=='RGBA'and im.size==(render['width'],render['height'])
 assert sha256(im.tobytes()).hexdigest()==render['pixelRGBA_SHA256']
raw=(r/'research/bazi-jianlu-context/DIGITAL_CROSSREF_LU.txt').read_text(encoding='utf-8')
fragment=raw[raw.index('甲祿寅如'):raw.index('有生成祿')]
assert fragment==(b/'RETAINED_DIGITAL_TABLE.txt').read_text(encoding='utf-8')
normalized=re.sub(r'<pb:[^>]+>|¶|\s','',fragment)
assert len(t['rows'])==50 and len(t['sharedClaims'])==8
normalize=lambda s:s.replace('㓙','凶').replace('㐫','凶').replace('徳','德').replace('値','值')
normalized=normalize(normalized)
for x in t['rows']:
 assert x['candidatePillar']in normalized,x['id']
 for label in x['sourceLabels']:assert normalize(label)in normalized,(x['id'],label)
 if x['rowSpecificSourceClause']:assert normalize(x['rowSpecificSourceClause'])in normalized,(x['id'],x['rowSpecificSourceClause'])
 assert x['forecast']is None and x['outcomeValidated']is False
for x in t['sharedClaims']:
 assert normalize(x['clause'])in normalized and all(any(y['sourceStem']==x['stem']and y['candidatePillar']==p and x['id']in y['sharedClaimIDs']for y in t['rows'])for p in x['pillars'])
body=re.sub(r'<pb:[^>]+>|¶|\s','',raw);body=body[body.index('祿爵祿也'):]
assert len(body)==2217 and len(body.encode('utf-16-le'))//2==2218
assert ''.join(x['retainedDigitalText']for x in ctx['units'])==body and len(ctx['units'])==28
assert ctx['digitalOffsetUnit'].startswith('Unicode code points')
assert all(x['disposition']and x['nativePages']and not x['allImageCharactersCollated']for x in ctx['units'])
assert not ctx['wholeSectionApplied']and not ctx['allSourceImageCharactersCollated']
assert storage['sourceReading']in body and len([s for x in storage['sourceGroups']for s in x['stems']])==10
assert m['newHTTPRequests']==m['newSourcePages']==m['newOriginalContainers']==0
out={'date':'2026-10-27','retainedSourceContainerVerified':1,'nativePNGAndRGBAHashesVerified':6,'newSourcePages':0,'expandedPreviouslyReadPages':6,
 'newHTTPRequests':0,'newOriginalContainers':0,'nativeTableRows':50,'sharedSourceClaims':8,'retainedDigitalCrossrefOccurrencesVerified':True,
 'digitalContextUnits':28,'retainedDigitalCodePoints':2217,'retainedDigitalUTF16Units':2218,'directLuStorageCoordinates':10,
 'allSourceImageCharactersCollated':False,'wholeLuSectionApplied':False,'wholeCatalogueCompleted':False}
(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
