from pathlib import Path
import json,runpy,copy,sys
v=Path(__file__).resolve().parent.parent;read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
guard=runpy.run_path(str(v/'scripts/research-resume-preflight.py'),run_name='resume_guard')['assess_resume'];tests=[]
def check(name,fn):fn();tests.append({'name':name,'passed':True})
def rejected(fn):
 try:fn()
 except ValueError:return
 raise AssertionError('Expected inconsistent state to be rejected')
def current():
 r=guard('B02');assert r['disposition']=='current-map-verified'and r['currentMapCounts']['registeredUnits']==137 and r['currentMapCounts']['firstPassCompleteSpanUnits']==137
check('Current137map agrees with active coverage count and all historical maps remain independent',current)
def known():
 r=guard('B02','weather-voices-and-heng-case');assert r['disposition']=='reuse-existing-complete-bounded-scope'and r['newSourceCase']is False and r['reuseModule']=='v53/research/liuyao-weather/weather-reference.mjs'
check('Known already released weather role/printed-case scope resolves to reuse',known)
def opened():
 r=guard('B02','complete-weather-strength-and-timing');assert r['disposition']=='open-source-premises'and r['wholeChapterApplied']is False and r['newSourceCase']is None
check('Open full weather-strength/timing scope remains open',opened)
def unknown():
 for catalogue,scope,expected in [('B02','not-indexed','unindexed-scope-review-coverage-first'),('T01','weather-voices-and-heng-case','catalogue-not-indexed-review-coverage-first')]:
  r=guard(catalogue,scope);assert r['disposition']==expected and r['newSourceCase']is None and r['wholeCatalogueCompleted']is False
check('Unindexed scopes/catalogues never become complete',unknown)
def stale():
 c=read(v/'research/library-current/COVERAGE.json');next(x for x in c['catalogue']if x['id']=='B02')['currentB02UnitMap']='v53/research/liuyao-b02-jinqian/B02_CURRENT_UNITS.json';rejected(lambda:guard('B02',coverage=c))
check('Positive control reproduces and rejects the previous stale pointer',stale)
def forged():
 c=read(v/'research/library-current/COVERAGE.json');next(x for x in c['catalogue']if x['id']=='B02')['currentSourceUnitCounts']['firstPassSpans']=32;rejected(lambda:guard('B02',coverage=c))
 i=read(v/'research/library-current/RESUME_INDEX.json');i['catalogues']['B02']['currentMapIdentity']['sha256']='0'*64;rejected(lambda:guard('B02',index=i))
 i=read(v/'research/library-current/RESUME_INDEX.json');i['catalogues']['B02']['expectedCounts']['wholeUnitsApplied']=137;rejected(lambda:guard('B02',index=i))
check('Contradictory counts, altered identity and false whole-application claim rejected',forged)
def preserved():
 a=read(v/'research/research-resume-pointer/DUPLICATE_WORK_AUDIT.json');assert a['actualAdditionalDuplicateHHCHexNumberCalls']==2 and a['actualAdditionalDuplicateCompileCalls']==1 and a['newUniqueSourceCases']==0 and a['duplicatePrivateModuleNotPromoted'];assert a['all8Original144DPIDerivativesSHAExactlyRestored']
 for args in [('B02',None),('B02','weather-voices-and-heng-case'),('B02','complete-weather-strength-and-timing'),('B02','unknown'),('unknown',None)]:
  r=guard(*args);assert r['newEngineCalls']==0 and r['wholeCatalogueCompleted']is False
check('Duplicate calls are disclosed and guard runs never execute engines or claim whole completion',preserved)
out={'date':'2026-10-29','completeChecks':len(tests),'positiveControls':4,'registeredUnits':137,'firstPassSpans':137,'wholeUnitsApplied':0,'knownScopesIndexed':2,'newSourcePositions':0,'newUniqueSourceCases':0,'newEngineCallsDuringGuardTests':0,'additionalDuplicateHHCHexNumberCallsBeforeFix':2,'additionalDuplicateCompileCallsBeforeFix':1,'consumerChanged':False,'wholeCatalogueCompleted':False,'checks':tests}
p=v/'qa/research-resume-pointer/GUARD_RESULTS.json'
if '--no-write'in sys.argv:assert read(p)==out
else:p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
