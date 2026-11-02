from pathlib import Path
from collections import Counter
from urllib.parse import unquote,urlsplit
import json,hashlib
root=Path(__file__).resolve().parent.parent
ws=root.parent
out=root/'research/library-current'
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
s=read(out/'COVERAGE.json');p=read(out/'RUNTIME_PROBE.json');old=read(root/'research/library-audit/COVERAGE.json');cat=read(root/'research/library-audit/LEGACY_CATALOGUE.json')
checks=[]
def check(name,condition):
 checks.append({'name':name,'ok':bool(condition)})
 assert condition,name
 print('PASS',name)
check('Every one of 40 catalogue entries retains its original ID and URL',len(s['catalogue'])==40 and [(r['id'],r['url']) for r in s['catalogue']]==[(r['id'],r['url']) for r in cat['books']])
check('All 16 overlapping module references remain separately identifiable',len(s['moduleSources'])==16 and [(r['id'],r['url']) for r in s['moduleSources']]==[(r['id'],r['url']) for r in cat['moduleSources']])
def canonical(url):
 u=urlsplit(unquote(url));return u.netloc+u.path.replace('/zh-hant/','/wiki/').rstrip('/')+('?' + u.query if u.query else '')
check('38 canonical catalogue URLs preserve duplicate CText and general-portal pairs',len({canonical(r['url']) for r in s['catalogue']})==38)
check('Two general portals are not promoted into possessed or fully applied books',all(r['resourceKind']=='general_portal' and r['currentStatus']=='not_established' for r in s['catalogue'] if r['id'] in ['F03','M05']))
check('No source record is mislabeled as an entire work fully applied',s['counts']['wholeWorkApplied']==0 and all(not r['wholeWorkApplied'] for r in s['catalogue']+s['moduleSources']))
check('Four partial-work records and four inherited URL claims are counted without double counting',Counter(r['currentStatus'] for r in s['catalogue'])==Counter({'partial_active':4,'inherited_rule_claim':4,'not_established':30,'research_only':2}) and {r['id'] for r in s['catalogue'] if r['currentStatus']=='partial_active'}=={'F01','M01','M04','T01'})
check('Alternate witnesses do not silently verify legacy original URLs',all(r['originalURLIndependentlyValidatedByAlternateWitness'] is False for r in s['catalogue']))
check('Current execution corresponds to the actual published standalone HTML',s['product']['sha256']==p['product']['sha256']==sha(ws/'Huyen_Hoc_Cac.html')==sha(root/'Huyen_Hoc_Cac.html')==sha(root/'site/index.html'))
check('All loaded module hashes and consumer rendering connections are current',all(sha(ws/f['file'])==f['sha256'] for f in p['files']) and all(p['consumerConnections'].values()))
check('Runtime confirms 384 individual ordinary line readings and only two all-moving supplements',p['yi']['individualOrdinaryReadings']==384 and p['yi']['allSpecific'] and p['yi']['supplements']==[1,2])
check('Runtime confirms ten relationship labels, twelve hidden-stem branches and unknown-hour handling',p['bazi']['uniqueRelationshipLabels']==10 and p['bazi']['hiddenStemBranches']==12 and p['bazi']['knownPillars']==4 and p['bazi']['unknownHourPillars']==3 and not p['bazi']['hasUsefulGodDiagnosis'])
check('Runtime confirms date-based period flow and split16 annual month intervals',p['tuvi']['palaces']==12 and p['tuvi']['majorRanges']==12 and p['tuvi']['annualTransformations']==4 and p['tuvi']['yearReadingIntervals']==14 and p['tuvi']['leapReadingIntervals']==2 and not p['tuvi']['fullCombinedStarPrediction'])
check('Runtime confirms seven room guides and ambiguity-preserving bearing lookup',p['home']['roomCount']==7 and p['home']['ageDirectionCount']==8 and len(p['home']['bearingBoundaryCandidates'])==2 and not p['home']['hasMeasuredFloorplanSolver'])
check('Every current evidence file exists and matches its recorded bytes and hash',all((ws/f['file']).stat().st_size==f['bytes'] and sha(ws/f['file'])==f['sha256'] for f in s['evidenceFiles']))
bazi=read(root/'research/four-items/BAZI_SOURCE_AUDIT.json');pdf=bazi['facsimile']['download'];image=root/'research/four-items'/bazi['facsimile']['pageImage']
check('The alternate Yuanhai scan and targeted page image retain the recorded bytes',sha(root/'research/four-items/sources'/pdf['file'])==pdf['sha256'] and sha(image)==bazi['facsimile']['pageImageSHA256'])
check('Historical audit is preserved rather than rewritten as a new result',sha(root/'research/library-audit/COVERAGE.json')==s['historicalAudit']['sha256'] and old['counts']['status']=={'inherited_rule_claim':6,'partial_active':2,'not_established':30,'research_only':2})
check('The all-applied condition is false and no bulk new download is claimed',s['conclusion']=='NOT_ALL_APPLIED' and s['counts']['newDownloadsThisScope']==0 and len(s['additionalWitnesses'])==4)
(out/'TEST_RESULTS.json').write_text(json.dumps({'date':'2026-10-26','checks':checks,'scope':'Current catalogue/source tracing and actual runtime capability inspection. No fresh whole-work philological review or independent predictive validation.'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'{len(checks)}/{len(checks)} checks passed')
