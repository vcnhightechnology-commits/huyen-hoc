"""Preserve the tested calculation candidate; keep the completed consumer release live.
No browser launch, privilege escalation or substitute for the unavailable approval review.
"""
from pathlib import Path
from hashlib import sha256
import json,shutil

root=Path(__file__).resolve().parent.parent
archive=root.parent/'archives/v53-before-meihua-layers'
base=root/'research/meihua-layers'
candidate=base/'candidate'
candidate.mkdir(parents=True,exist_ok=True)
sha=lambda p:sha256(p.read_bytes()).hexdigest()
released='3800162854742c915d60f0051c65cadb0eb9a1c803f9f937bf1b6a593c96d268'
assert sha(archive/'Huyen_Hoc_Cac.html')==released
assert sha(root.parent/'Huyen_Hoc_Cac.html')==sha(root/'site/index.html')==released
for name in['meihua.js','meihua.css','Huyen_Hoc_Cac.html']:
    target=candidate/name
    assert not target.exists(), 'Candidate already exists; do not overwrite it automatically'
    shutil.copy2(root/name,target)
for name in['meihua.js','meihua.css','Huyen_Hoc_Cac.html']:
    shutil.copy2(archive/name,root/name)
assert sha(root/'Huyen_Hoc_Cac.html')==released
status={
 'schema':'hhc.meihua-layers.pending.v1','date':'2026-10-26',
 'status':'candidate-calculation-tested-browser-and-print-pending',
 'releasedHTMLSHA256':released,
 'candidateFiles':[{'file':p.name,'bytes':p.stat().st_size,'sha256':sha(p)}for p in sorted(candidate.iterdir())],
 'calculationChecks':14,'structures':384,'layerRelations':1536,
 'browserChecksExecuted':0,'pdfCreated':False,'released':False,
 'block':{'kind':'automatic-approval-review-unavailable-usage-limit','requestedAction':'node v53/scripts/verify-meihua-layers-browser.mjs --pdf','actionExecuted':False,'safetyVerdict':None,'reportedRetryTime':'Oct 27th, 2026 1:19 AM; tool message did not state timezone','policy':'Do not bypass approval review by switching launch mechanisms or permissions.'},
 'next':['When approval review is available, run the prepared browser runner with --candidate --pdf. A PDF operation-start marker already succeeded for this scope; do not repeat it for this first pending PDF.','Verify browser interaction,TXT/print expansion,profiles and mobile widths; render and visually inspect every PDF page.','Only after pending checks pass, integrate candidate modules,build,and synchronize HTML/site/source and web packages. Continue independent source research meanwhile.'],
 'wholeBookCompleted':False,'wholeCatalogueCompleted':False
}
(base/'PENDING.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(status,ensure_ascii=False))
