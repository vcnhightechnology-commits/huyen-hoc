# Chỉ mục container PDF/DjVu

Nhận diện bằng chữ ký tệp, không chỉ phần mở rộng. Danh sách gồm cả bản nguồn, bản QA sinh ra và đối tượng lịch sử; số container không đồng nghĩa số tác phẩm hay truyền bản độc lập. Các đường dẫn cùng SHA-256 có cùng byte.

Đọc manifest để chọn đường dẫn cần phục hồi; `SOURCE_BOOKS.json` có đủ đường dẫn trùng. Nguồn chỉ còn tên mã băm trong kho lịch sử cần tra xuất xứ qua `recovery/consolidated-history/INDEX.sqlite` sau khi khôi phục.

| Loại | Tệp đại diện | MB | SHA-256 | Gói |
|---|---|---:|---|---|
| PDF | `recovery/consolidated-history/objects/7f/7fa1fdb5f6b5c05ab1ec3ffde92e6fb2d5df98bf1a87055075ae2c3c1240a627` | 0.2 | `7fa1fdb5f6b5c05ab1ec3ffde92e6fb2d5df98bf1a87055075ae2c3c1240a627` | `hhc-materials-006.zip` |
| PDF | `recovery/consolidated-history/objects/b1/b18eacead4c0924d8c62b5a6ac9b4e4f6c7dcfbd26f7eacb798fbb2ddf3cbaf4` | 0.1 | `b18eacead4c0924d8c62b5a6ac9b4e4f6c7dcfbd26f7eacb798fbb2ddf3cbaf4` | `hhc-materials-007.zip` |
| PDF | `recovery/consolidated-history/objects/c3/c3c6aa52e8136dd66bcfbb7516e2ce4a6bd3e89230ca1f65b10f681f373daf19` | 0.1 | `c3c6aa52e8136dd66bcfbb7516e2ce4a6bd3e89230ca1f65b10f681f373daf19` | `hhc-materials-008.zip` |
| PDF | `recovery/consolidated-history/objects/c7/c746c7794b498a041e871bebbc3ecfb13e8432a7c6c33ca6e13f891c216c9504` | 0.1 | `c746c7794b498a041e871bebbc3ecfb13e8432a7c6c33ca6e13f891c216c9504` | `hhc-materials-008.zip` |
| PDF | `recovery/consolidated-history/objects/e5/e5ca855d7f5de03a55a433e159019f4f34ceb29c4450ce8740820f566b07a24a` | 27.2 | `e5ca855d7f5de03a55a433e159019f4f34ceb29c4450ce8740820f566b07a24a` | `hhc-materials-009.zip` |
| DjVu | `v53/research/bazi-food-gap-witness/CADAL06056481.djvu` | 10.8 | `4f273322b3fd4339789e1408e0bbb4ea15a7956e5e508c6f99fced264e0b53ee` | `hhc-materials-003.zip` |
| DjVu | `v53/research/bazi-season-strength/CADAL06066038.djvu` | 10.9 | `7a53f35982f0b946281d0e393c5d6ddcce1fd091aea83c11af6a06bcdfe6a85e` | `hhc-materials-006.zip` |
| DjVu | `v53/research/bazi-jianlu-context/volume3/CADAL06066039.djvu` | 10.6 | `2334006e3a46b16bdbf0bf6a79512d8d0c4b87a2ce2e8e1ff503121d8f2cffdc` | `hhc-materials-002.zip` |
| PDF | `v53/research/home-fuduan/SSID-12152602-vol33-36.pdf` | 54.2 | `3f6f81e7332a779dc8c43e8b69808e3f03449b8c595daea649529bea2c8d84ca` | `hhc-materials-003.zip` |
| DjVu | `v53/research/home-yangzhai-courtyards/Gujin-Tushu-Jicheng-Volume476.djvu` | 33.7 | `e819d6f430065e4f63c121390d74ad6d3bc36457cfb8e59fb7a2cea6483130de` | `hhc-materials-010.zip` |
| PDF | `v53/research/home-yangzhai-shishu/Tianyige-330000-1705-0007405-yangzhai-shishu.pdf` | 151.3 | `b6394102a995bb66df173452b37614b29d58e34ff85e08c43077006572ac48a5` | `hhc-materials-008.zip` |
| PDF | `v53/research/liuyao-b03-volume5/NLC892-GBZX0301013045-259366.pdf` | 56.9 | `01859340e519ffb68a1f40996af73aa7f40beb10a723a7a2a070985201874c61` | `hhc-materials-001.zip` |
| PDF | `v53/research/liuyao-b03-book4/NLC892-GBZX0301013045-259367.pdf` | 57.0 | `5f8bb92f28120fa4c2c4d629ae8bad9f785dc02324f15f285085c99ab7ffadaf` | `hhc-materials-005.zip` |
| PDF | `v53/research/liuyao-b03-book5/NLC892-GBZX0301013045-259423.pdf` | 35.1 | `cca4c2ce376c54c6ead6463c72e6f25d6e6e544b3d6488d593415afabc6227a6` | `hhc-materials-009.zip` |
| PDF | `v53/research/liuyao-b03-book6/NLC892-GBZX0301013045-259424.pdf` | 55.1 | `1d6c656828533ac52ae1fd4ff06cc3c025db98ae5458dc686eda2a6b1d11f07f` | `hhc-materials-002.zip` |
| PDF | `v53/qa/bazi-late-zi-option/late-zi-option.pdf` | 0.1 | `2febcc1657b1489bf6fe7f906f3a4460149de7e3a0bd6856fd405f947d2a4d1b` | `hhc-materials-002.zip` |
| PDF | `v53/qa/bazi-month-stems/month-stems.pdf` | 0.1 | `35ac544e0ae24280cfa8052957379cbcffe1e8b29fc6268695ebe9efc855296b` | `hhc-materials-002.zip` |
| PDF | `v53/qa/bazi-relation-locations/bazi-relation-locations.pdf` | 0.1 | `ed520318d6ae36ecc72e56a2203bb9514e96e76c6b7888f2c816bcbfd54c527a` | `hhc-materials-010.zip` |
| PDF | `v53/qa/fortune-context/fortune-context.pdf` | 0.2 | `53d15fa44aa45e8b0952765b15a55332801098e8b0d2d4ebe5ca6f194e556165` | `hhc-materials-004.zip` |
| PDF | `v53/qa/fortune-months/year-reading-print.pdf` | 0.1 | `a8c883c8ec3a78360e399c12c7d890145691cde1172ecfef290874f897c3159d` | `hhc-materials-007.zip` |
| PDF | `v53/qa/full-study/yi-context.pdf` | 0.1 | `e93242391a049987259e401147692bb24095b458df9831cdc43bd5bc9ab9733e` | `hhc-materials-010.zip` |
| PDF | `v53/qa/internal-doors/internal-doors.pdf` | 0.1 | `2dc65ebcb28585a957b396e15698bf404b3999d48928f6d88eb230077a8569b5` | `hhc-materials-002.zip` |
| PDF | `v53/qa/measured-plan/mat-bang.pdf` | 0.1 | `6d5eaa1d01cb10c096ffc09f1d739fd0e7341dae0ed87de7218ae5d4cfbf1699` | `hhc-materials-005.zip` |
| PDF | `v53/qa/meihua-layers/body-use-layers-attempt2.pdf` | 0.1 | `25205b664c247c46c9f3652beb6bff71ce52be2ce0229403016ac8bfdb6f9098` | `hhc-materials-002.zip` |
| PDF | `v53/qa/meihua-layers/body-use-layers-attempt3.pdf` | 2.0 | `f27f9cfc96b80e30643540efa2fd064013e5460a9f43c31d2bde97129983f239` | `hhc-materials-010.zip` |
| PDF | `v53/qa/meihua-layers/body-use-layers.pdf` | 0.1 | `210768dad70380f68fa687eaf92f16169ce589db3af53a388857e3ea6135045b` | `hhc-materials-002.zip` |
| PDF | `v53/qa/meihua-methods/historical-tones.pdf` | 0.1 | `ea96e21e376c4dba4aad41199235c59480ea152202b1c2046cbe9cf92354bc49` | `hhc-materials-010.zip` |
| PDF | `v53/qa/meihua/plum-reading.pdf` | 0.1 | `58e0bb335ed1b023fdfe9040dc6dd310324e4bc197d4ba53a27f16a3d3758d6f` | `hhc-materials-004.zip` |
| PDF | `v53/qa/unknown-hour-range/unknown-hour.pdf` | 0.1 | `4820ac0e382eaa8fadab73e96a9d8c649fd2b6472b788efd48c523db3ee7776a` | `hhc-materials-003.zip` |
| PDF | `v53/research/bazi-late-zi-witness/NCL-000002203.pdf` | 58.3 | `3dfee4ef4636d48c2d2e749f90408a825e0eacee99b8c73b9748a03deb73dcfd` | `hhc-materials-003.zip` |
| DjVu | `v53/research/bazi-pattern-witness/CADAL06066041.djvu` | 10.7 | `013ce4861680a2bf08b811050c45a45bb2d3ce9d164f7e2341d7070bd5cb2c1a` | `hhc-materials-001.zip` |
| PDF | `v53/research/four-items/sources/yuanhai-NTL-v1.pdf` | 90.8 | `664bccd1ea4706c609df8ea6cd69a4565db97dc277e876fc22eb125ea41dcc9f` | `hhc-materials-005.zip` |
| DjVu | `v53/research/full-study/home/CADAL06056503.djvu` | 3.4 | `bfd3b76c55d62324919ab161c8c2ba2ecb129b3b2c59a3ab0428807e8f8278db` | `hhc-materials-008.zip` |
| PDF | `v53/research/full-study/home/kua/nlc287543.pdf` | 27.1 | `347281dba5998391b59138cbf45224e0df30f41d9eda2767f9d54f5ccb3f8315` | `hhc-materials-002.zip` |
| PDF | `v53/research/full-study/yi/evidence/NCPSSD-71014695_周易四卷_第一册.pdf` | 28.9 | `a35643bec19d116a0ce1323a4afcb6ac7d8cb247618adb0edc2531696ab64bb5` | `hhc-materials-007.zip` |
| PDF | `v53/research/full-study/yi/evidence/NCPSSD-71014696_周易四卷_第二册.pdf` | 35.7 | `9a810330902aa4230fd0e55db746e63f123aaeb7ae78899488cb62879ee26b2d` | `hhc-materials-007.zip` |
| PDF | `v53/research/liuyao-b03-volume3/NLC892-GBZX0301013045-259365.pdf` | 41.2 | `c1e1027331d43769733c6011b4fe99e90928e9fde013fce563c8e9bad81c04bf` | `hhc-materials-008.zip` |
| PDF | `v53/research/liuyao-foundations/NLC416-12jh005345-45344.pdf` | 11.1 | `caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa` | `hhc-materials-008.zip` |
| PDF | `v53/research/liuyao-foundations/NLC892-GBZX0301013045-259368.pdf` | 50.2 | `5dcd7b5005b1e86f441a9350eefb7c0e9e628c47ab926b2a7d1bdd6691a4773d` | `hhc-materials-004.zip` |
| PDF | `v53/research/meihua/NLC416-12jh005426-44577.pdf` | 5.6 | `af608094ab11ae209eae91a9365565e7c9cff604aac3da5e753e04d1cc4598c0` | `hhc-materials-007.zip` |
| PDF | `v53/research/yi-second-witness/NCL-00037.pdf` | 95.7 | `83472d8eb932ad44de18a552e54304947a01f994abbda5b534440db01026fa31` | `hhc-materials-006.zip` |
