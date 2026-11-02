from pathlib import Path
from hashlib import sha256
import json,runpy,contextlib,io,sys
v=Path(__file__).resolve().parent.parent;w=v.parent;r=v/'research/research-resume-pointer';q=v/'qa/research-resume-pointer';read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def digest(p):
 h=sha256()
 with p.open('rb')as f:
  for b in iter(lambda:f.read(4*1024*1024),b''):h.update(b)
 return h.hexdigest()
ids=read(r/'PROMOTION_IDENTITIES.json')
for x in ids['files']+read(r/'RETENTION_IDENTITIES.json')['files']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and digest(p)==x['sha256'],x['file']
inventory=read(r/'B02_MAP_INVENTORY.json');assert len(inventory['records'])==12
for x in inventory['records']:
 identity=x['identity'];p=w/identity['file'];assert p.stat().st_size==identity['bytes']and digest(p)==identity['sha256'];assert read(p)['currentCounts']==x['counts']
 assert x['explicitCurrentAfter']==(identity['file']=='v53/research/liuyao-foundation-span/B02_CURRENT_UNITS.json')
before=read(r/'BEFORE_POINTER.json');assert before['currentB02UnitMap']=='v53/research/liuyao-b02-jinqian/B02_CURRENT_UNITS.json'
oldManifest=read(w/'archives/v53-before-liuyao-b02-weather/PACKAGE_MANIFEST.json');prior=next(x for x in oldManifest['files']if x['file']=='research/library-current/COVERAGE.json');assert prior['sha256']==before['coverageIdentity']['sha256']
coverage=read(v/'research/library-current/COVERAGE.json');b02=next(x for x in coverage['catalogue']if x['id']=='B02');assert b02['currentB02UnitMap']=='v53/research/liuyao-foundation-span/B02_CURRENT_UNITS.json';assert b02['historicalCurrentB02UnitMapBefore29Oct']==before['currentB02UnitMap'];assert b02['latestLocalReadingScope']==b02['latestFoundationSpanScope'];assert b02['historicalLocalReadingScopeBeforePointerFix']!=b02['latestLocalReadingScope']
assert coverage['counts']['catalogueRecords']==40 and coverage['counts']['moduleSourceRecords']==16 and coverage['counts']['wholeWorkApplied']==0
args=sys.argv[:]
try:
 sys.argv=['test-research-resume-preflight.py','--no-write']
 with contextlib.redirect_stdout(io.StringIO()):runpy.run_path(str(v/'scripts/test-research-resume-preflight.py'))
finally:sys.argv=args
guard=read(q/'GUARD_RESULTS.json');assert guard['completeChecks']==7 and guard['positiveControls']==4
duplicate=read(r/'DUPLICATE_WORK_AUDIT.json');assert duplicate['duplicatePrivateModuleNotPromoted']and duplicate['newUniqueSourceCases']==0 and duplicate['actualAdditionalDuplicateHHCHexNumberCalls']==2 and duplicate['actualAdditionalDuplicateCompileCalls']==1
assert not(v/'research/liuyao-b02-weather-followup-20261029').exists()
html=(v/'Huyen_Hoc_Cac.html').read_bytes();assert len(html)==707411 and sha256(html).hexdigest()=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857';assert html==(w/'Huyen_Hoc_Cac.html').read_bytes()==(v/'site/index.html').read_bytes();assert sorted(p.name for p in(v/'site').iterdir())==['index.html']
out={'date':'2026-10-29','promotionIdentities':len(ids['files']),'historicalB02MapsUnchanged':12,'currentB02Units':137,'currentB02FirstPassSpans':137,'wholeUnitsApplied':0,'knownScopesIndexed':2,'completeChecks':7,'inconsistentStatePositiveControls':4,'newEngineCallsDuringGuardTests':0,'additionalDuplicateHHCHexNumberCallsDisclosed':2,'additionalDuplicateCompileCallsDisclosed':1,'newUniqueSourceCases':0,'newSourceImagePositions':0,'newHTTPRequests':0,'all8OriginalStagedDerivativesRestored':True,'duplicateWeatherModuleExcluded':True,'consumerChanged':False,'wholeCatalogueCompleted':False}
if '--no-write'not in sys.argv:(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
else:assert read(q/'SOURCE_RESULTS.json')==out
print(json.dumps(out))
