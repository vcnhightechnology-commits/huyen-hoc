"""Restore only the selected small research handoff files; refuse conflicts."""
from pathlib import Path
from hashlib import sha256
import json

w = Path(__file__).resolve().parent.parent
manifest = json.loads((w / 'collaboration/WORKING_SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
planned = []
for row in manifest['files']:
    src = (w / row['repositoryFile']).resolve()
    dst = (w / row['originalFile']).resolve()
    assert src.is_relative_to(w) and dst.is_relative_to(w / 'tmp')
    data = src.read_bytes()
    assert len(data) == row['bytes'] and sha256(data).hexdigest() == row['sha256']
    if dst.exists():
        assert dst.is_file() and dst.read_bytes() == data, f'Existing file differs: {row["originalFile"]}'
    else:
        planned.append((dst, data))
for dst, data in planned:
    dst.parent.mkdir(parents=True, exist_ok=True)
    with dst.open('xb') as out:
        out.write(data)
print(f'Context verified: {len(manifest["files"])} files; restored {len(planned)} missing files. Binary sources remain local.')
