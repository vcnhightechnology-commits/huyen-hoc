from pathlib import Path
from hashlib import sha256
import subprocess,json,sys
root=Path(__file__).resolve().parent.parent;base=root/'research/liuyao-b03-volume3'
a=json.loads((base/'ACQUISITION.json').read_text(encoding='utf-8'));pdf=base/a['file'];assert sha256(pdf.read_bytes()).hexdigest()==a['sha256']
exe=Path('C:/Users/Administrator.DESKTOP-98TGIBL/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe')
out=base/'images';out.mkdir(exist_ok=True)
pages=[int(n)for n in sys.argv[1:]]or list(range(1,33))
for n in pages:
 assert 1<=n<=int(a['APIPages'])
 p=out/f'bushi-book2-{n}'
 if not p.with_suffix('.png').exists():subprocess.run([str(exe),'-f',str(n),'-l',str(n),'-r','200','-singlefile','-png',str(pdf),str(p)],check=True,capture_output=True)
print({'renderedOrRetainedPages':pages,'sourcePDFUnchanged':True})
