from pathlib import Path
from PIL import Image
import hashlib,json
root=Path(__file__).resolve().parent.parent
out=root/'research/library-audit'
checks=[]
def test(name,condition):
    checks.append({'name':name,'ok':bool(condition)});print('PASS' if condition else 'FAIL',name)
    assert condition,name
read=lambda path:json.loads(path.read_text(encoding='utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
a=read(out/'COVERAGE.json');p=read(out/'RUNTIME_PROBE.json');rows=a['catalogue']
test('Audit covers each of the 40 original catalogue IDs exactly once',len(rows)==40 and len({x['id'] for x in rows})==40)
test('All 16 inherited module source records keep their own IDs and historical claim labels',len(a['moduleSources'])==16 and len({x['id'] for x in a['moduleSources']})==16 and all(x['legacyVerifiedFieldIsHistoricalClaim'] for x in a['moduleSources']))
test('No whole book is falsely marked fully implemented',a['conclusion']=='NOT_ALL_APPLIED' and all(not x['wholeWorkApplied'] for x in rows+a['moduleSources']))
test('Resource types distinguish modern websites, institutions and portals from books',next(x for x in rows if x['id']=='M07')['resourceKind']=='modern_reference' and next(x for x in rows if x['id']=='V01')['resourceKind']=='institution' and next(x for x in rows if x['id']=='F03')['resourceKind']=='general_portal')
test('Duplicate catalogue entries are retained but not counted as unique titles or full books',a['counts']['canonicalCatalogueURLs']==38 and next(x for x in rows if x['id']=='F02')['url']==next(x for x in rows if x['id']=='X04')['url'])
test('The 384 stored lines are distinguished from the current 64 generic readings',a['counts']['embeddedLineTexts']==384 and p['yi']['hexagrams']==64 and not p['yi']['hasActualLineTexts'] and p['yi']['genericPositionHints']==6)
test('Runtime inspection records computed ten gods and existing age-start data honestly',len(p['bazi']['pillars'])==4 and all(x['god'] for x in p['bazi']['pillars']) and 'daHanStart' in p['tuvi']['palaceKeys'])
test('The actual engine files inspected still match recorded hashes',all(sha((root/f['file']).read_bytes())==f['sha256'] for f in p['files']))
m=read(out/'new-sources/MANIFEST.json');r=out/'new-sources'
test('Every newly saved response body matches byte length and SHA-256',all((r/f['file']).stat().st_size==f['bytes'] and sha((r/f['file']).read_bytes())==f['sha256'] for f in m['files'] if 'sha256' in f))
test('All accepted bodies were obtained over certificate-verified HTTPS with HTTP 200',all(f['status']==200 and f['tls']['authorized'] and f['requestedURL'].startswith('https:') for f in m['files'] if f['usable']))
test('Two failed image responses are excluded from valid facsimiles',len([f for f in m['files'] if not f['usable']])==2 and all(f['status']==400 for f in m['files'] if not f['usable']))
images=[f for f in m['files'] if f['file'].endswith('.jpg') and f['usable']]
test('The institutional manifest has 23 canvases, of which 21 actual images were saved',len(read(r/'ndl-760737-canvas-index.json'))==23 and len(images)==21)
test('Every accepted facsimile opens as the expected 3331 by 2882 JPEG',all(Image.open(r/f['file']).format=='JPEG' and Image.open(r/f['file']).size==(3331,2882) for f in images))
revs=read(r/'REVISIONS.json')['repositories']
test('Both Kanripo witnesses are pinned to immutable commits',len(revs)==2 and all(len(x['revision'])==40 for x in revs) and all(any(x['revision'] in f['requestedURL'] for x in revs) for f in m['files'] if f['file'].startswith('KR') and not f['file'].endswith('-commit.json')))
w=read(out/'TEXT_WITNESS_CHECK.json')
test('Three selected text differences are found without forcing a correction',len(w['pairs'])==3 and all(x['locatedInWYG'] and x['locatedInHFL'] for x in w['pairs']) and 'not' in w['scope'])
comparison=read(out/'NDL_ENGINE_COMPARISON.json')
test('Real engine comparison checks 32 explicitly transcribed direction labels',comparison['charts']==4 and comparison['fields']==comparison['matched']==32 and not comparison['differences'])
manual=read(out/'NDL_CHART_READINGS.json')
test('The source numbering difference is preserved rather than equating 五黄 with kua 2',next(x for x in manual['readings'] if x['kua']==2)['numericCaution'] and 'South at the top' in manual['method'])
test('Earlier source archives were actually rechecked rather than redownloaded',a['counts']['olderScanFilesHashChecked']==17 and a['counts']['olderYiFilesHashChecked']==64)
html=(root/'Huyen_Hoc_Cac.html').read_bytes();before=read(out/'PUBLIC_BASELINE.json')
test('Consumer HTML and release folder remain byte-identical during this research audit',sha(html)==before['htmlSha256'] and (root.parent/'Huyen_Hoc_Cac.html').read_bytes()==html==(root/'site/index.html').read_bytes())
test('Private books, new manifests and source names are absent from consumer HTML',all(x not in html.decode('utf-8') for x in ['NDL_CHART_READINGS','RUNTIME_PROBE','kanripo','ndl-760737','COVERAGE.json']))
(out/'VERIFICATION.json').write_text(json.dumps({'checks':checks,'passed':len(checks),'scope':'Coverage/provenance audit, not a full-book review or new UI regression suite.'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'{len(checks)}/{len(checks)} passed')
