"""Create readable container and bundle locators from the verified handoff inventory."""
from pathlib import Path
from collections import defaultdict
import json, zipfile, re

W = Path(__file__).resolve().parent.parent
B = W/'collaboration/materials'
m = json.loads((B/'MANIFEST.json').read_text(encoding='utf-8'))
paths = defaultdict(list)
for r in m['files']: paths[r['sha256']].append(r['file'])
books = []
for digest, names in paths.items():
    p = W/names[0]
    if p.exists():
        with p.open('rb') as f: header = f.read(16)
    else:
        o = m['objects'][digest]
        with zipfile.ZipFile(W/'tmp/materials-handoff'/o['bundle']) as z:
            with z.open(o['member']) as f: header = f.read(16)
    kind = 'PDF' if header.startswith(b'%PDF-') else 'DjVu' if header.startswith(b'AT&TFORM') and header[12:16] in (b'DJVU', b'DJVM') else None
    if kind:
        o = m['objects'][digest]
        books.append({'format': kind, 'bytes': o['bytes'], 'sha256': digest, 'bundle': o['bundle'], 'paths': sorted(names)})
books.sort(key=lambda r: r['paths'][0])
(B/'SOURCE_BOOKS.json').write_text(json.dumps({'scope': 'PDF/DjVu containers recognized by file signature, including originals, derived QA documents and historical objects; not a count of independently witnessed books', 'containers': books}, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
lines = ['# Chỉ mục container PDF/DjVu', '', 'Nhận diện bằng chữ ký tệp, không chỉ phần mở rộng. Danh sách gồm cả bản nguồn, bản QA sinh ra và đối tượng lịch sử; số container không đồng nghĩa số tác phẩm hay truyền bản độc lập. Các đường dẫn cùng SHA-256 có cùng byte.', '', 'Đọc manifest để chọn đường dẫn cần phục hồi; `SOURCE_BOOKS.json` có đủ đường dẫn trùng. Nguồn chỉ còn tên mã băm trong kho lịch sử cần tra xuất xứ qua `recovery/consolidated-history/INDEX.sqlite` sau khi khôi phục.', '', '| Loại | Tệp đại diện | MB | SHA-256 | Gói |', '|---|---|---:|---|---|']
for r in books:
    preferred = sorted(r['paths'], key=lambda p: (not p.startswith('v53/'), p.startswith('recovery/'), p))[0]
    lines.append(f"| {r['format']} | `{preferred}` | {r['bytes']/1000000:.1f} | `{r['sha256']}` | `{r['bundle']}` |")
(B/'SOURCE_BOOKS.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')
stats = {'files': len(m['files']), 'uniqueByteObjects': len(m['objects']), 'originalPathBytes': sum(r['bytes'] for r in m['files']), 'uploadBytes': sum(r['bytes'] for r in m['bundles']), 'bundles': len(m['bundles']), 'pdfDjvuContainersBySignature': len(books), 'allBundleMembersVerified': m['allObjectMembersSHA256Verified'], 'notAClaimOfWholeCatalogueCompletion': True}
(B/'SUMMARY.json').write_text(json.dumps(stats, indent=2)+'\n', encoding='utf-8')
groups = defaultdict(list)
for r in m['files']:
    parts=r['file'].split('/')
    key='/'.join(parts[:2]) if parts[0]=='tmp' else '/'.join(parts[:3]) if len(parts)>3 else parts[0]
    if key=='recovery/consolidated-history/objects': key+='/'+parts[3]
    groups[key].append(r)
folder=B/'file-index';folder.mkdir(exist_ok=True);index=[]
for scope, rows in sorted(groups.items()):
    name=re.sub('[^A-Za-z0-9._-]','--',scope)+'.json'
    records=[{**r,**{k:v for k,v in m['objects'][r['sha256']].items() if k!='bytes'}} for r in rows]
    p=folder/name;p.write_text(json.dumps({'scope':scope,'files':records},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    assert p.stat().st_size<1000000, name
    index.append({'scope':scope,'index':p.relative_to(W).as_posix(),'files':len(rows)})
assert sum(r['files'] for r in index)==len(m['files'])
(B/'FILE_INDEX.json').write_text(json.dumps({'purpose':'Small per-scope source locators with hashes and HTTP byte ranges.','scopes':index},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(stats), flush=True)
