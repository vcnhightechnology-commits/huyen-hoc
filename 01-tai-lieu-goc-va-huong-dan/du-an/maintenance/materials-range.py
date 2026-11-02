"""Download selected source objects using authenticated byte ranges, verifying original SHA-256."""
from pathlib import Path, PurePosixPath
from hashlib import sha256
import argparse, json, subprocess, urllib.request, zlib, os, re

W = Path(__file__).resolve().parent.parent
p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--path', action='append', default=[])
p.add_argument('--prefix', action='append', default=[])
p.add_argument('--destination', type=Path, required=True)
p.add_argument('--gh', default='gh')
p.add_argument('--anonymous', action='store_true', help='Read public repository assets without a GitHub login')
a = p.parse_args()
if not (a.path or a.prefix): p.error('Select --path or --prefix explicitly.')
m = json.loads((W/'collaboration/materials/MANIFEST.json').read_text(encoding='utf-8'))
assert m['repository']=='dedaithien-sudo/huyen-hoc' and m['releaseTag']=='materials-v53'
rows = [r for r in m['files'] if r['file'] in a.path or any(r['file'].startswith(s) for s in a.prefix)]
assert rows and all(any(r['file']==s for r in rows) for s in a.path), 'Unknown source path'
dest = a.destination.resolve()
for r in rows:
    parts=PurePosixPath(r['file'])
    assert not parts.is_absolute() and not any(x in {'..','.git','.aws','.codex'} for x in parts.parts) and ':' not in r['file'] and '\\' not in r['file']
    target=(dest/r['file']).resolve(); assert target.is_relative_to(dest)
    if target.exists():
        assert target.is_file() and sha256(target.read_bytes()).hexdigest()==r['sha256'], 'Existing destination differs: '+str(target)

def gh(*cmd): return subprocess.check_output([a.gh,*cmd],text=True,timeout=45)
if a.anonymous:
    req=urllib.request.Request(f"https://api.github.com/repos/{m['repository']}/releases/tags/{m['releaseTag']}",headers={'User-Agent':'HHC-Materials'})
    with urllib.request.urlopen(req,timeout=45) as response: release=json.load(response)
else:
    release=next(r for r in json.loads(gh('api',f"repos/{m['repository']}/releases?per_page=100")) if r['tag_name']==m['releaseTag'])
assets={r['name']:r for r in release['assets']}
token=None if a.anonymous else gh('auth','token','--hostname','github.com').strip()
opener=urllib.request.build_opener()
bundles={r['file']:r for r in m['bundles']}
completed=0
for r in rows:
    target=(dest/r['file']).resolve()
    if target.exists(): completed+=1; continue
    o=m['objects'][r['sha256']]; b=bundles[o['bundle']]; remote=assets[o['bundle']]
    assert remote['size']==b['bytes'] and remote['digest']=='sha256:'+b['sha256']
    rr=o['httpRange']; start=rr['offset']; size=rr['compressedBytes']; end=start+size-1
    assert isinstance(start,int) and isinstance(size,int) and start>=0 and size>=0 and end<b['bytes']
    url=remote['url']; assert url.startswith('https://api.github.com/repos/dedaithien-sudo/huyen-hoc/releases/assets/')
    target.parent.mkdir(parents=True,exist_ok=True); pending=target.with_name(target.name+'.hhc-range-pending');assert not pending.exists()
    h=sha256(); count=0; received=0
    decoder=zlib.decompressobj(-15) if rr['compressionMethod']==8 else None
    assert rr['compressionMethod'] in (0,8)
    try:
        with pending.open('xb') as out:
            if size:
                request=urllib.request.Request(url,headers={'Accept':'application/octet-stream','Range':f'bytes={start}-{end}','User-Agent':'HHC-Materials'})
                # An unredirected header is NOT forwarded to the signed download host.
                if token: request.add_unredirected_header('Authorization','Bearer '+token)
                with opener.open(request,timeout=45) as response:
                    assert response.status==206 and response.headers.get('Content-Range')==f'bytes {start}-{end}/{b["bytes"]}', 'Server must honor the exact requested range'
                    while True:
                        block=response.read(64*1024)
                        if not block: break
                        received+=len(block); assert received<=size
                        data=decoder.decompress(block,r['bytes']-count+1) if decoder else block
                        count+=len(data); assert count<=r['bytes']; h.update(data); out.write(data)
                    if decoder:
                        data=decoder.flush();count+=len(data);assert count<=r['bytes'];h.update(data);out.write(data)
                        assert decoder.eof and not decoder.unused_data and not decoder.unconsumed_tail
        assert received==size and count==r['bytes'] and h.hexdigest()==r['sha256'], 'Original source SHA-256 mismatch'
        os.link(pending,target)
    finally:
        if pending.exists(): pending.unlink()
    completed+=1
    print(json.dumps({'source':r['file'],'originalBytes':count,'downloadedCompressedBytes':received,'sha256Verified':True,'completed':completed,'selected':len(rows)},ensure_ascii=False),flush=True)
