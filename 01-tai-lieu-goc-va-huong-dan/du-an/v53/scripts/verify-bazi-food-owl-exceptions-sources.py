from pathlib import Path
from hashlib import sha256
from PIL import Image, ImageChops
import json, sys

r = Path(__file__).resolve().parents[1]
w = r.parent
b = r / 'research/bazi-food-owl-exceptions'
q = r / 'qa/bazi-food-owl-exceptions'
read = lambda p: json.loads(p.read_text(encoding='utf-8-sig'))
sha = lambda p: sha256(p.read_bytes()).hexdigest()
ident = read(b / 'PROMOTION_IDENTITIES.json')
assert len(ident['records']) == 21
for x in ident['records']:
    p = w / x['file']
    assert p.stat().st_size == x['bytes'] and sha(p) == x['sha256'], x['file']
text = (b / 'STAGED_test-owl-exceptions.mjs').read_text(encoding='utf-8')
for old, new in [
    ("from'./owl-exception-reference.mjs'", "from'../research/bazi-food-owl-exceptions/owl-exception-reference.mjs'"),
    ("const b=import.meta.dirname,w=resolve(b,'../..'),ctx={};", "const b=resolve(import.meta.dirname,'../research/bazi-food-owl-exceptions'),w=resolve(b,'../../..'),ctx={};"),
    ("resolve(b,'REFERENCE_RESULTS.json')", "resolve(w,'v53/qa/bazi-food-owl-exceptions/REFERENCE_RESULTS.json')"),
]:
    assert text.count(old) == 1, old
    text = text.replace(old, new)
assert text == (r / 'scripts/test-bazi-food-owl-exceptions.mjs').read_text(encoding='utf-8')
ctx = read(b / 'RETAINED_CONTEXT.json')
assert sha(w / ctx['file']) == ctx['sha256'] == 'c9179c1421a4521ce9bd0f5d48ab05e28a6a9ed11daf462927ad777343be0f68'
partition = read(b / 'CLAUSE_PARTITION.json')
rows = partition['records']
assert len(rows) == 10 and len(ctx['context']['text']) == 213
assert ''.join(x['digitalText'] for x in rows) == ctx['context']['text']
position = 0
for x in rows:
    start, end = x['localCodepointOffsets']
    assert start == position and end - start == len(x['digitalText'])
    assert x['globalCleanCodepointOffsets'] == [987 + start, 987 + end]
    assert not x['consumerApplied'] and not x['wholeClauseApplied']
    assert not x['sourceAnchorRoleAutomaticallyEstablished']
    position = end
assert position == 213
selected = [x for x in rows if x['sourceRecipientStemModel']]
assert len(selected) == 8
assert sum(3 ** len(x['requiredResearchPremises']) for x in selected) == 162
assert sum(len(x['requiredResearchPremises']) == 3 for x in selected) == 5
assert len({(x['sourceRecipientStemModel'], x['sourceOwlStemModel']) for x in selected}) == 7
assert sum(x['namedPillarToken'] is not None for x in selected) == 4
assert not partition['jiXinVersusXinDingPriorityResolved']
raw = read(b / 'RAW_REVIEW.json')
assert [x['sourceContainerPage'] for x in raw['records']] == [175, 176]
for x in raw['records']:
    assert x['actuallyViewed'] and not x['newSourceReadPosition'] and sha(w / x['file']) == x['sha256']
qa = read(q / 'QA_IMAGES.json')
assert len(qa['records']) == 4
for x in qa['records']:
    p = q / x['file']
    assert x['actuallyViewed'] and not x['resampled'] and sha(p) == x['sha256']
    expected = Image.open(w / x['sourceFile']).convert('RGB').crop(x['cropBox'])
    assert ImageChops.difference(expected, Image.open(p).convert('RGB')).getbbox() is None
reading = read(b / 'SELECTED_READING_AUDIT.json')
assert reading['glyphAtLuClause']['digital'] == '壬' and reading['glyphAtLuClause']['facsimile'] == '土'
res = read(q / 'REFERENCE_RESULTS.json')
assert len(res['checks']) == 5 and all(x['ok'] for x in res['checks'])
assert res['actualHHCTenGodQueries'] == 8 and res['actualLunarHiddenStemTableQueries'] == 4
assert res['actualLunarCombinationTableQueries'] == 4 and res['ternaryContexts'] == 162
assert res['newCalendarChartCalls'] == 0
assert len(res['relationRecords']) == 8 and all(x['actualFixedHHCTenGod'] == 'Thiên Ấn' for x in res['relationRecords'])
assert len(res['mechanismRecords']) == 4
for x in res['mechanismRecords']:
    assert x['partnerInHiddenStemList'] and x['statedPartner'] == x['actualCombinationPartner']
    assert not x['sourceRoleOrEffectiveTransformationValidated']
failure = read(q / 'TEST_FAILURE_AUDIT.json')
assert failure['firstRunCompleteChecksBeforeFailure'] == 3 and failure['firstRunTernaryContextsEvaluated'] == 162
assert not failure['logicOrManualSourceTableChanged'] and not failure['consumerAffected']
dispositions = read(b / 'SOURCE_DISPOSITIONS.json')
assert dispositions['testExecutionAudit']['firstFailedRun'] == failure
audit = dispositions['testExecutionAudit']
assert (audit['allRunsHHCTenGodQueries'], audit['allRunsLunarHiddenTableQueries'], audit['allRunsLunarCombinationTableQueries']) == (16, 8, 8)
assert not dispositions['sourceFullClausesApplied'] and not dispositions['consumerApplied']
state = read(b / 'WORK_STATE.json')
assert not state['wholeCatalogueCompleted'] and not state['fullNatalExceptionClassifierImplemented']
out = dict(date='2026-10-28', promotionIdentities=21, completeFinalRuntimeChecks=5,
    sourceContextCodepoints=213, exactDigitalPartitionUnits=10, selectedExceptionRecords=8,
    nativeCropsViewedPixelMatched=4, expandedNativePositions=[175, 176], newSourcePositions=0,
    ternaryContexts=162, finalHHCTenGodQueries=8, uniqueRecipientOwlPairs=7,
    finalLunarHiddenTableQueries=4, finalLunarCombinationTableQueries=4,
    allRunsHHCTenGodQueries=16, allRunsLunarHiddenTableQueries=8, allRunsLunarCombinationTableQueries=8,
    correctedExpectedCountOnly=True, rerunsNotIndependentEvidence=True,
    newHTTPBodies=0, newContainers=0, newCalendarChartCalls=0, consumerChanged=False,
    sourceBirthChartAnchorsEstablished=False, effectiveTransformationEstablished=False,
    wholeCatalogueCompleted=False)
p = q / 'SOURCE_RESULTS.json'
if '--no-write' in sys.argv:
    assert read(p) == out
else:
    p.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(out))
