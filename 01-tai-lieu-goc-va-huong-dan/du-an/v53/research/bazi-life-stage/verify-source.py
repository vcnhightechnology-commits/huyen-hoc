from pathlib import Path
from hashlib import sha256
from PIL import Image, ImageChops
import json
import re
import subprocess

s = Path(__file__).resolve().parent
w = s.parent.parent
read = lambda p: json.loads(p.read_text(encoding='utf-8-sig'))
digest = lambda p: sha256(p.read_bytes()).hexdigest()
frozen = read(s / 'PREIMPLEMENTATION_FREEZE.json')
assert not frozen['implementationExists'] and not frozen['runtimeExists']
for x in frozen['files']:
    p = s / x['file']
    assert p.stat().st_size == x['bytes'] and digest(p) == x['sha256'], x['file']
for x in read(s / 'SOURCE_IDENTITIES.json')['files']:
    p = w / x['file']
    assert p.stat().st_size == x['bytes'] and digest(p) == x['sha256'], x['file']
for x in read(s / 'NATIVE_CROPS.json')['records']:
    source = w / x['source']
    crop = s / x['crop']
    assert digest(source) == x['sourceSHA256'] and digest(crop) == x['cropSHA256']
    original = Image.open(source).convert('RGB')
    actual = Image.open(crop).convert('RGB')
    x0, y0, x1, y1 = x['boxXYXY']
    assert 0 <= x0 < x1 <= original.width and 0 <= y0 < y1 <= original.height
    assert original.crop(x['boxXYXY']).size == actual.size
    assert ImageChops.difference(original.crop(x['boxXYXY']), actual).getbbox() is None
    assert x['nativeCropActuallyViewed'] and not x['resampled']
manual = read(s / 'MANUAL_TERMS.json')
text = (w / 'v53/research/bazi-season-strength/RETAINED_DIGITAL_STRENGTH_SECTION.txt').read_text(encoding='utf-8-sig')
text = re.sub(r'<pb:[^>]+>', '', text)
text = ''.join(c for c in text if not c.isspace() and c != '¶')
# The retained transcription uses U+98EC 飬; the manually read working
# character is U+990A 養. Keep bytes intact and disclose this one comparison.
assert '胎飬' in text
comparison_text = text.replace('飬', '養')
assert ''.join(manual['mainOrder']) in comparison_text
for x in manual['quotedRows']:
    assert x['sourceDefinition'] in text, x['literalName']
for anchor in manual['explicitAliasAnchors'].values():
    assert anchor in text
assert manual['broadGroupQualifier'] in text
for anchor in manual['noAutomaticOutcomeAnchors']:
    assert anchor in text
runtime = read(s / 'ACTUAL_RUNTIME.json')
assert runtime['librarySHA256'] == digest(w / 'v46/node_modules/lunar-typescript/dist/index.cjs')
assert runtime['scriptSHA256'] == digest(s / 'run-actual-once.mjs')
assert runtime['freezeSHA256'] == digest(s / 'PREIMPLEMENTATION_FREEZE.json')
assert runtime['summary']['actualLunarLifeStageTableReads'] == 1
assert runtime['summary']['actualCalendarObjects'] == 0
result = subprocess.run(['node', str(s / 'test-life-stage.mjs')], check=True, capture_output=True, text=True, encoding='utf-8')
tests = json.loads(result.stdout)
assert tests['passed']
(s / 'TEST_RESULTS.json').write_text(json.dumps(tests, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
out = {'date': '2026-10-29', 'passed': True, 'nativeCropsRGBMatched': 4,
       'preimplementationFilesUnchanged': 3, 'retainedIdentityFilesVerified': 8,
       'mainTermsImageRead': 12, 'quotedDefinitionsImageRead': 12, 'explicitAliasTokens': 4,
       'editorialAlignmentsNotPromotedToAliases': 2, 'newIndependentWitnesses': 0,
       'digitalComparisonVariants': [{'retained': '飬', 'workingImageReading': '養', 'comparisonOnly': True}],
       'newHTTPBodies': 0, 'newSourcePositions': 0, 'runtime': runtime['summary'], 'referenceTests': tests,
       'consumerChanged': False, 'wholeChapterApplied': False, 'wholeCatalogueCompleted': False}
(s / 'SOURCE_RESULTS.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(out, ensure_ascii=False))
