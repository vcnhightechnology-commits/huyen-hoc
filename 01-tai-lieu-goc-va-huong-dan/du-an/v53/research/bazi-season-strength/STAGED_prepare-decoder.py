from pathlib import Path
w=Path.cwd();text=(w/'tmp/home-yangzhai-courtyard-staging/decode-gjts-native.mjs').read_text(encoding='utf-8')
for old,new in [('tmp/home-yangzhai-courtyard-staging','tmp/bazi-season-strength-staging'),('Gujin-Tushu-Jicheng-Volume476.djvu','CADAL06066038.djvu'),('e819d6f430065e4f63c121390d74ad6d3bc36457cfb8e59fb7a2cea6483130de','7a53f35982f0b946281d0e393c5d6ddcce1fd091aea83c11af6a06bcdfe6a85e'),('135','232'),('of[86,87,88,89]','of[109,110,111,112,113,114,115,116]'),('gjts-p${page}.png','p${page}.png'),('GJTS_LOCAL_RENDERS.json','LOCAL_RENDERS.json'),('Decoded4targeted-comparisonpositions','Decoded8targeted-strengthpositions')]:text=text.replace(old,new)
(w/'tmp/bazi-season-strength-staging/decode-native.mjs').write_text(text,encoding='utf-8')
print('Preparednativecodecwrapper;sourcecodecunchanged')
