"""Render new bounded pages of the retained B02PDF;no network or PDF authoring."""
from pathlib import Path
from hashlib import sha256
import subprocess,sys
root=Path(__file__).resolve().parent.parent
pdf=root/'research/liuyao-foundations/NLC416-12jh005345-45344.pdf'
assert sha256(pdf.read_bytes()).hexdigest()=='caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa'
out=root/'research/liuyao-day-month/images';out.mkdir(parents=True,exist_ok=True)
exe=Path('C:/Users/Administrator.DESKTOP-98TGIBL/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe')
pages=[int(n)for n in sys.argv[1:]]or[57,58,59,61,62,63,65,66,67,69,70,71]
for n in pages:
 assert 1<=n<=394
 dest=out/f'zengshan-{n}'
 if dest.with_suffix('.png').exists():continue
 subprocess.run([str(exe),'-f',str(n),'-l',str(n),'-r','230','-singlefile','-png',str(pdf),str(dest)],check=True,capture_output=True)
print('Newretainedrenderpages:',pages)
