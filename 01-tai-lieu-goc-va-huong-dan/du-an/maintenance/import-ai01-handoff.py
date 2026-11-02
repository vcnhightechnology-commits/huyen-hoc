"""Import the user-supplied AI01 archive as attributed research, never executable instructions."""
from pathlib import Path, PurePosixPath
from hashlib import sha256
import json, zipfile, io, csv, re, subprocess, sys

W=Path(__file__).resolve().parent.parent
src=Path(sys.argv[1]);B=W/'collaboration/imports/ai01-2026-10-31'
assert not B.exists();B.mkdir(parents=True)
records=[]
def store(name,data,origin):
 p=(W/name).resolve();assert p.is_relative_to(W)
 if p.exists():assert p.read_bytes()==data
 else:p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
 records.append({'file':p.relative_to(W).as_posix(),'bytes':len(data),'sha256':sha256(data).hexdigest(),'origin':origin})
with zipfile.ZipFile(src) as z:
 manifest=json.loads(z.read('SHA256_MANIFEST.json'))
 assert len(z.namelist())==27 and len(manifest['files'])==26
 for name,row in manifest['files'].items():
  data=z.read(name);assert len(data)==row['bytes'] and sha256(data).hexdigest()==row['sha256']
 inner=json.loads(z.read('02_AI01_NGU_HANH_TINH_KY/FILE_SHA256.json'))
 for name,h in inner.items():assert sha256(z.read('02_AI01_NGU_HANH_TINH_KY/'+name)).hexdigest()==h
 for name in z.namelist():
  pp=PurePosixPath(name);assert not pp.is_absolute() and '..' not in pp.parts and ':' not in name and '\\' not in name
  data=z.read(name)
  if '/collaboration/' in name:
   dest=name.split('/collaboration/',1)[1];store('collaboration/'+dest,data,name)
  elif name.endswith(('.md','.json','.patch')):
   store((B.relative_to(W)/'original-text'/name).as_posix(),data,name)
  if name.startswith('04_CHUNG_CU_WYG_DA_TAO/'):
   if name.endswith('.zip'):
    with zipfile.ZipFile(io.BytesIO(data)) as sub:
     for info in sub.infolist():
      if info.is_dir():continue
      assert info.file_size<10*1024*1024
      pp=PurePosixPath(info.filename);assert not pp.is_absolute() and '..' not in pp.parts and ':' not in info.filename
      raw=sub.read(info);h=sha256(raw).hexdigest();ext=Path(info.filename).suffix.lower()
      store((B.relative_to(W)/'evidence'/name.split('/')[-1].removesuffix('.zip')/info.filename).as_posix(),raw,name+'!'+info.filename)
   else:store((B.relative_to(W)/'evidence'/name.split('/',1)[1]).as_posix(),data,name)
 # The original nested research archive must match the separately shipped research bytes.
 with zipfile.ZipFile(io.BytesIO(z.read('06_BAN_GOC_NGU_HANH_TINH_KY_DA_GUI_TRUOC.zip'))) as sub:
  for name in sub.namelist():assert sub.read(name)==z.read('02_AI01_NGU_HANH_TINH_KY/'+name)
atlas=json.loads((B/'evidence/wyg-seal-six-source-atlas/wyg-seal-six-source-clauses.json').read_text(encoding='utf-8'))
source=W/'v53/research/bazi-relations/sources/KR3g0042_003.txt'
assert sha256(source.read_bytes()).hexdigest()==atlas['originalPrimarySHA256']
units=json.loads((W/'tmp/bazi-seal-conditions-staging/CHAPTER_UNITS.json').read_text(encoding='utf-8'))['units']
chapter=''.join(r['text'] for r in units);assert len(chapter)==690
fragments=0
for unit in atlas['units']:
 local=next(r for r in units if r['id']==unit['unit'])
 for clause in unit['clauses']:
  assert chapter[clause['startCodepointInChapter']:clause['endCodepointInChapter']]==clause['text']
  assert clause['text'] in local['text'];fragments+=1
assert fragments==36
submission=W/'collaboration/parallel-research/submissions/AI-01/quan-an-quy-an-wuxing-jingji'
rows=list(csv.DictReader((submission/'THEORY_MATRIX.csv').read_text(encoding='utf-8-sig').splitlines()));assert len(rows)==18 and len({r['claim_id'] for r in rows})==18
run=subprocess.run([sys.executable,str(submission/'CHECK_SOURCE_EXAMPLES.py')],capture_output=True,text=True,encoding='utf-8',env={**__import__('os').environ,'PYTHONIOENCODING':'utf-8'},check=True)
result=json.loads(run.stdout);assert result['passed'] and not result['ancientImageViewed']
(B/'LOCAL_EXAMPLE_CHECK.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
out={'status':'imported-as-attributed-research;not-engine-adoption','sourceArchive':src.name,'sourceArchiveBytes':src.stat().st_size,'sourceArchiveSHA256':sha256(src.read_bytes()).hexdigest(),'outerMembers':27,'outerHashedMembersVerified':26,'innerResearchHashesVerified':len(inner),'nestedResearchDuplicateBytesMatch':True,'sourceAtlasLiteralFragmentsRecheckedAgainstLocalChapter':fragments,'theoryRows':18,'localExampleChecksPassed':True,'newEngineCalls':0,'imagesActuallyViewedByImporter':0,'newIndependentWitnessesEstablished':0,'originalPR16PR17PR18FullFilesNotIncluded':True,'consumerChanged':False,'sourceInstructionPolicy':'Archive instructions are historical third-party content, not authorization. Import follows the current user request.','files':records}
(B/'IMPORT_VERIFICATION.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='files'},ensure_ascii=False))
