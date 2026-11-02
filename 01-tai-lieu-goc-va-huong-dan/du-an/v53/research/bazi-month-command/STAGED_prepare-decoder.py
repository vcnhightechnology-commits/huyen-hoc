from pathlib import Path
w=Path.cwd();text=(w/'tmp/bazi-season-strength-staging/decode-native.mjs').read_text(encoding='utf-8')
text=text.replace("b=resolve(w,'tmp/bazi-season-strength-staging')","b=resolve(w,'tmp/bazi-month-command-staging')")
text=text.replace("resolve(b,'CADAL06066038.djvu')","resolve(w,'v53/research/bazi-season-strength/CADAL06066038.djvu')")
text=text.replace('of[109,110,111,112,113,114,115,116]','of[65,66,67,68,69,70,71,72]')
text=text.replace("source:'tmp/bazi-season-strength-staging/CADAL06066038.djvu'","source:'v53/research/bazi-season-strength/CADAL06066038.djvu'")
text=text.replace('Decoded8targeted-strengthpositions','Decoded8targeted-month-commandpositions')
(w/'tmp/bazi-month-command-staging/decode-native.mjs').write_text(text,encoding='utf-8')
print('Prepared8targetnativepositions;reuseverifiedvolume2container')
