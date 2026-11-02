from pathlib import Path
W=Path(__file__).resolve().parents[2];B=Path(__file__).resolve().parent
assert not (B/'decode-selected.mjs').exists(),'Existing decoder and evidence must not be overwritten by this one-time preparation.'
s=(W/'v53/research/home-yangzhai-courtyards/STAGED_decode-gjts-native.mjs').read_text(encoding='utf-8-sig')
s=s.replace('tmp/home-yangzhai-courtyard-staging','tmp/home-p08-gjts-grid-witness-staging')
s=s.replace("resolve(b,'Gujin-Tushu-Jicheng-Volume476.djvu')","resolve(w,'v53/research/home-yangzhai-courtyards/Gujin-Tushu-Jicheng-Volume476.djvu')")
s=s.replace('[86,87,88,89]','[99]')
s=s.replace('Decoded4targeted-comparisonpositions','Decoded1targeted-comparisonposition')
s=s.replace("source:'tmp/home-p08-gjts-grid-witness-staging/Gujin-Tushu-Jicheng-Volume476.djvu'","source:'v53/research/home-yangzhai-courtyards/Gujin-Tushu-Jicheng-Volume476.djvu'")
(B/'decode-selected.mjs').write_text(s,encoding='utf-8')
