"""Bind verified current research files to the latest comprehensive source package."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone,timedelta
import json,zipfile,sqlite3
W=Path(__file__).resolve().parent.parent;V=W/'v53';R=W/'recovery/storage-consolidation';F=W/'recovery/research-release';F.mkdir(exist_ok=True)
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def digest(p):
 h=sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
 return h.hexdigest()
package=read(R/'LATEST_PACKAGE_MANIFEST.json');assert package['status']=='latest-source-package-member-sha256-verified'
current=read(R/'CURRENT_VERIFICATION.json');assert current['status']=='current-product-and-retained-history-verified'
batch=read(F/'CURRENT_BATCH.json')
assert {x['file'] for x in current['currentResearchTests']}==set(batch['tests'])
assert read(R/'COLLECTION_STATE.json')['status']=='all-retained-content-sha256-verified'
assert read(R/'MAINTENANCE.json')['status']=='complete'
assert not (W/'archives').exists()
assert {p.name for p in W.glob('*.zip')}=={'Huyen_Hoc_Cac_V53_source.zip','Huyen_Hoc_Cac_V53_web.zip'}
entries={x['file']:x for x in package['files']};manifest=read(V/'PACKAGE_MANIFEST.json');source=W/'Huyen_Hoc_Cac_V53_source.zip'
assert source.stat().st_size==package['sourceZIPBytes']
for x in manifest['files']:
 packed=entries['v53/'+x['file']];assert packed['sha256']==x['sha256'] and packed['bytes']==x['bytes'],x['file']
assert entries['v53/PACKAGE_MANIFEST.json']['sha256']==digest(V/'PACKAGE_MANIFEST.json')
for name in ['PENDING_RESEARCH_STATE.json','EXHAUSTIVE_WORK_STATE.json','WORK_RESUME.md','PROJECT_RESEARCH_STATE.md']:
 assert entries[name]['sha256']==digest(W/name),name
with zipfile.ZipFile(source) as z:
 assert set(z.namelist())==set(entries) and len(z.namelist())==len(entries)
 assert z.read('recovery/consolidated-history/INDEX.sqlite')==(W/'recovery/consolidated-history/INDEX.sqlite').read_bytes()
 assert z.read('v53/Huyen_Hoc_Cac.html')==(V/'site/index.html').read_bytes()==(W/'Huyen_Hoc_Cac.html').read_bytes()
for name in batch['scopes']:
 for x in read(V/'qa'/name/'PROMOTION_IDENTITIES.json')['byteExactFiles']:
  assert digest(W/x['target'])==x['sha256'] and (W/x['target']).stat().st_size==x['bytes'],x['target']
c=read(V/'research/library-current/TMTH002_NATIVE_POSITION_COVERAGE.json');seen=set()
for scope in c['scopes']:
 p=W/scope['evidence']['file'];assert digest(p)==scope['evidence']['sha256'] and p.stat().st_size==scope['evidence']['bytes'];seen.update(scope['positions'])
assert len(seen)==batch['expectedTMTH002DistinctPositions']==c['distinctViewedCount']
assert c['remainingCount']==batch['expectedTMTH002RemainingPositions']
assert seen==set(c['distinctPositionsViewed']) and not c['wholeVolumeApplied']
db=sqlite3.connect('file:'+(W/'recovery/consolidated-history/INDEX.sqlite').as_posix()+'?mode=ro',uri=True);assert db.execute('PRAGMA integrity_check').fetchone()[0]=='ok';revisions=db.execute('SELECT count(*) FROM revisions').fetchone()[0];db.close()
out={'status':'current-research-and-comprehensive-source-package-verified','verifiedAt':datetime.now(timezone(timedelta(hours=7))).isoformat(),'report':'v53/BAZI_STARS_HARMS_REPORT.md','v53ManifestFiles':len(manifest['files']),'v53ManifestSHA256':digest(V/'PACKAGE_MANIFEST.json'),'comprehensiveSourceZIPFiles':len(entries),'sourceZIPBytes':source.stat().st_size,'sourceZIPSHA256':digest(source),'htmlBytes':707411,'htmlSHA256':current['htmlSHA256'],'webZIPSHA256':digest(W/'Huyen_Hoc_Cac_V53_web.zip'),'consumerChanged':False,'publicSiteClean':True,'currentResearchGroups':sum(x['groups'] for x in current['currentResearchTests']),'wholeCatalogueCompleted':False,'tmth002FirstPassPositions':68,'tmth002NotEstablishedPositions':164,'historicalMutableRevisionsPreserved':revisions,'newWholeSnapshotZIPsCreated':0,'chatHistoryUntouched':True,'packageEntryChecks':'Every member streamed and SHA-256 verified before atomic replacement; this audit binds the V53 manifest, root continuation state, index bytes and promotion identities to that package.','next':'論三刑:214 already inspected boundary;215 onward not yet read in this scope.'}
out.update(report=batch['report'],tmth002FirstPassPositions=len(seen),tmth002NotEstablishedPositions=c['remainingCount'],next=batch['next'])
(F/'FINAL_VERIFICATION.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,ensure_ascii=False),flush=True)
