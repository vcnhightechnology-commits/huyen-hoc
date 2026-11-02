from pathlib import Path
from hashlib import sha256
import json,re
b=Path(__file__).resolve().parent;w=b.parents[1];source=w/'v53/research/four-items/sources/KR3g0042_002.txt'
text=source.read_text(encoding='utf-8');start=text.index('論五行旺相休囚死並寄生十二宫');end=text.index('論遁月時',start)
section=text[start:end];out=b/'RETAINED_DIGITAL_STRENGTH_SECTION.txt';out.write_text(section,encoding='utf-8',newline='\n')
state=dict(date='2026-10-28',status='volume2repository-acquired-strength-facsimile-collation-active',catalogueID='M01',sourceDirectory='tmp/bazi-season-strength-staging',
 retainedDigital=dict(file=source.relative_to(w).as_posix(),sha256=sha256(source.read_bytes()).hexdigest(),decodedSliceFile=out.name,sliceNotOriginalHTTPBytes=True,digitalFolios=['002-54b','002-55a','002-55b','002-56a','002-56b','002-57a']),
 newRepositoryContainerBytes=10858550,newRepositoryContainerSHA256='7a53f35982f0b946281d0e393c5d6ddcce1fd091aea83c11af6a06bcdfe6a85e',newHTTP200TLSBodies=3,actuallyViewedPositions=[],
 pendingIssues=['Digital 夏水因 is not silently corrected to 囚 from common formula; inspect corresponding glyph first.',
 'Source 六月土旺 is not automatically 四季末18days or a Gregorian date rule.',
 'Source explicitly says生旺未必吉/休囚死絶未必凶; never equate a state label with overall fortune or full natal strength.'],
 newConsumerChange=False,wholeCatalogueCompleted=False,next=['Decode native target positions around54b–57a; verify actual folio labels, not arithmetic alone.', 'Manually enter25states before engine/formula comparison; retain unknown glyph if unresolved.', 'Keep seasonal labels separate from十二寄生, full strength, actual-calendar phase boundaries and source outcomes.'])
(b/'WORK_STATE.json').write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p=w/'PENDING_RESEARCH_STATE.json';d=json.loads(p.read_text(encoding='utf-8-sig'));d['inProgressStaging']=dict(file='tmp/bazi-season-strength-staging/WORK_STATE.json',status=state['status'],catalogueID='M01');d['next']=state['next'];p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Retaineddecodedsectionandcurrentworkstate;newcontainerstillunread')
