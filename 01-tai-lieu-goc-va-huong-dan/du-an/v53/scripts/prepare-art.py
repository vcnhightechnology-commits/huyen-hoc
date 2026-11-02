"""Create web-sized encodings without cropping, recoloring or altering the artwork."""
from pathlib import Path
from PIL import Image
import hashlib, json

root = Path(__file__).resolve().parent.parent
records = []
for name, width in [('hero-landscape', 1024), ('celestial-illustration', 768), ('lotus-still-life', 768)]:
    original = root / 'assets' / 'originals' / (name + '.png')
    target = root / 'assets' / (name + '.webp')
    with Image.open(original) as image:
        size = image.size
        image.thumbnail((width, width), Image.Resampling.LANCZOS)
        image.save(target, 'WEBP', quality=84, method=6)
        records.append({'name': name, 'original': str(original.relative_to(root)), 'originalSize': size,
                        'originalSha256': hashlib.sha256(original.read_bytes()).hexdigest(),
                        'web': str(target.relative_to(root)), 'webSize': image.size, 'webBytes': target.stat().st_size,
                        'webSha256': hashlib.sha256(target.read_bytes()).hexdigest()})
(root / 'assets' / 'ASSET_MANIFEST.json').write_text(json.dumps({'operation': 'Proportional downscaling and WebP encoding only; original PNG artwork retained.', 'assets': records}, indent=2)+'\n', encoding='utf-8')
print(json.dumps(records))
