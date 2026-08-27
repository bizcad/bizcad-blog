# PromptTracking Corpus Manifest

SHA-256 of every session log in the PromptTracking corpus. **No content is disclosed here** -- this manifest is hashes only and is safe to publish.

## Root hash

```
e15144f220d759863ad00c5b11edc3350b1ecf1fb62ab66d3bd1101ef617f106
```

The root is `sha256` over the sorted `name<TAB>sha256<TAB>bytes` lines, one per file, newline-terminated, UTF-8. It does **not** cover this document's prose or the generated-at line, so regenerating an unchanged corpus reproduces the same root.

| | |
|---|---|
| files | 173 |
| total bytes | 22,269,243 |
| generated at (UTC) | 2026-08-27T20:03:41Z |

> **Note:** dates come from **filenames**, never from filesystem mtime -- a backup sweep rewrote the mtimes of 35 of these files, so mtime answers a different question.

## Scope -- what this manifest does and does not cover

Covered: every top-level `.md` / `.txt` file in `PromptTracking/` -- the session-log record itself.

Not covered, listed here so the boundary is visible rather than silent:

| excluded | bytes | why |
|---|---|---|
| `anthropic-report/` | 163,585 | derived media / data, not conversation |
| `audit-reports/` | 87,304 | derived media / data, not conversation |
| `mutation-ledger/` | 1,442,560 | derived media / data, not conversation |
| `whisper/` | 44,872,059 | derived media / data, not conversation |
| `workflows/` | 0 | derived media / data, not conversation |
| `youmind_com-gpt-5-6-fable-agent-stack-images/` | 1,730,924 | derived media / data, not conversation |
| `*.ps1` | -- | code, already version-controlled in git |

## To verify a file

```
certutil -hashfile "PromptTracking\<name>" SHA256     # Windows
sha256sum "PromptTracking/<name>"                     # Linux / macOS
```

Compare the result against the row below. A match proves those exact bytes existed unchanged as of the date this manifest was published.

## Files

| file | sha256 | bytes |
|---|---|---|
| `Claude-output-logs-20260706-12-25am.txt` | `f844a22630773515ed6b98a54f7ba1bf32ff0598f7353c4587cdcff2a46e0e92` | 67,860 |
| `HANDOFF_20260805.md` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | 0 |
| `Memory Log 20260426.md` | `5d460385e3a5c3063f96eb0f3e8f0987526b6527fd50ac6e4060fd3f933d43a3` | 401,632 |
| `Memory Log 20260427.md` | `50722be120911672f03cf0917d7c0d3a4986bbfcd43d4ff31a4768b094e35c7a` | 457,354 |
| `Memory Log 20260429.md` | `1a9238b7eedb6af12093c73022817f9b76a3761ad2b60fb2d5b580573281b026` | 466,781 |
| `Next Session Copilot 20260504.md` | `d4855d871f037b03a98c9633e10de876dc0ef8810135116d3bfd15cdf5ea00f6` | 1,422 |
| `Next Session Prompt 20260430.md` | `16bdb45f7dcadf515b47c9e1403857940b69fb4fecda195e4130224bf1620adb` | 10,875 |
| `Next Session Prompt 20260501.md` | `252f30fff0ec3cac15b63ef1dd2874bcc68b38665779295a36e5a5cb982b15f0` | 7,774 |
| `Next Session Prompt 20260502.md` | `5a9d7accdaae63816b474d6207bfc3dfdbd0a0d398e0ec118eb02829f1361cd1` | 9,356 |
| `Next Session Prompt 20260503.md` | `84261c312d0d8c0688bba5701bc20a64e3503fb0818543df640b056b7a6242c6` | 5,775 |
| `Next Session Prompt 20260504.md` | `f537dbf2df429dbd4472625df0e17700d470c23286421bdec8e79695cabb2c82` | 6,219 |
| `Session Log 2026-06-15 Pacing WO-040.md` | `8d051a7b9ee4a384664ee603b632f181f3e6cb9ac8e84408aa938e9a7a2ed92a` | 3,373 |
| `Session Log 20260205.md` | `466bc904feabca7a1960e56f5b4adae5560f0256d09cf5599c013960491553b9` | 98,387 |
| `Session Log 20260206.md` | `c543cc276b1f7e597399ce7e6d71bad7b7c5ef0c22f8b1e332de78085c20005a` | 129,155 |
| `Session Log 20260207.md` | `bb1a17b049cd6e9369455bb1d44caa8849c9d591d7b3da7723a00226fe446707` | 38,038 |
| `Session Log 20260208.md` | `0a5dbf1190bf1ad9503616ec2ef8f638f05625886d8affe48ab9c0fe16629b5c` | 143,793 |
| `Session Log 20260209.md` | `0af566a7f40f622fbab9a3922e2e356d83d73054f2345502ee69ad7515a3f403` | 121,290 |
| `Session Log 20260210.md` | `edc2f9f526dbd069ee5bdb9ab9d9a890b5368aadd636702aec497bc950610c3a` | 164,418 |
| `Session Log 20260211.md` | `a8b52572a79c896a7ab91c2938c71f4b7e622b3af680c446d3e14566e724db00` | 146,092 |
| `Session Log 20260212.md` | `93bbef13a671f8cd1d91b287c53f5882cd7d7f00a20e41168895e2d67f5e1f2f` | 132,416 |
| `Session Log 20260213.md` | `c077cf1e3f05f9fd54e05ecb582fe7b4a998548d28c6d959c807ac7d0432fab6` | 169,162 |
| `Session Log 20260214.md` | `5df11883fdcecfee75817a4e8f415a8f05e5e65cac30b7269ae68743cde04a58` | 111,702 |
| `Session Log 20260215.md` | `fc544831d30c5b3027d2268ffa80a30e21695b6454eeec7a7ae9029cf225241c` | 127,124 |
| `Session Log 20260216.md` | `e4fd42e2c1e46dbbcf01004949f3fff0d05868dbb3dae44c90ccce44a777e565` | 199,581 |
| `Session Log 20260217.md` | `d0533a1fdbbb419ee53eed582a836097b94b68771addd1be44ccdd2e5bc8d2d8` | 134,000 |
| `Session Log 20260218.md` | `7148f62d65b2b2b91cf9366b20678ce8785f6fd116e95c97c6fbe79b143e30be` | 43,690 |
| `Session Log 20260219.md` | `86fac886efbd6a51bc8d2ad999f1883c61eefe7fe9a3301b5e54e26bba01a3e9` | 62,946 |
| `Session Log 20260220.md` | `de733a62a053418b5ffe92ddde3a371b5cc260546bb647b9b0bbf1d6ab6bf692` | 1,617 |
| `Session Log 20260225.md` | `e839e08cc5b539562721926dd5d38956140c681a8b63b8f0e9bb11678992cdd6` | 25,260 |
| `Session Log 20260226.md` | `99c91bfaf41a2fa4720f0d1e73a6a75823588d79ac2ba732d01fe7238301a7cd` | 17,762 |
| `Session Log 20260227.md` | `9b095c7884c27b3ce1743235e1edd30feb18bdc8a299755153d9d988384b10f2` | 228,868 |
| `Session Log 20260301.md` | `756a5fd2d1dec94a1957c7ca2770be788082728ce9e0e0b7ee58ed8973f21858` | 58,255 |
| `Session Log 20260302.md` | `4fc7cefdb73aeb09dfb11f63addaec4928d5051de1d63529712a499a50279475` | 117,347 |
| `Session Log 20260303.md` | `b0480e7b31cca2536a8dd050c56397b6a3e0e663663904608e6f6f13356b1734` | 31,412 |
| `Session Log 20260304.md` | `dfd994bf83e8fe0b6c0786ab6bb8e4fbe1440f31fc970f809952479977288d15` | 109,995 |
| `Session Log 20260306.md` | `7122895f39e8be43a08b0fd4d01ef31beef36f51340f96246a52b521d6e1c63d` | 143,606 |
| `Session Log 20260308.md` | `7f2deafbad9cceef5e0cdc89c12a6265ef6050989a915a190a743726c0b84324` | 36,442 |
| `Session Log 20260310.md` | `0ecb531d2ece90a0f551d2fa102bf12fa47bdd57870038e1f65ca7d6af3ccbec` | 90,566 |
| `Session Log 20260311.md` | `330efc138f3789f4d1daa62263f877ef669eb5e377be65aafacf58e089ab49cd` | 273,813 |
| `Session Log 20260312.md` | `4088033cb9b392d1c8dda6bd9a096e94c49290f3ac9253704768783611e857e0` | 70,590 |
| `Session Log 20260313.md` | `9c70eda803db9e8fb2e24eb0b9cc756166d1991772b1ae4d8e8c310da55cefe9` | 64,661 |
| `Session Log 20260315.md` | `44d5877e9f9f60d4665b11f145bba5373182ae066880e58d84b30233e12a54c4` | 45,920 |
| `Session Log 20260316.md` | `cbd2458b77ce060511383c855050deb80466cee58b1c46aecca3a2ecea8a8ee7` | 89,192 |
| `Session Log 20260317-part-1.md` | `9e3fc3616a309fb51ab07f13bc88a16768d7209873628409dc2b07c9781d4a9c` | 261,731 |
| `Session Log 20260317-part-2.md` | `22de5bed38fe19a28cd0ea686215b4f92ed72384299bf8fa3cf68b74eb1274d0` | 613,783 |
| `Session Log 20260317.md` | `17eb4fe534bba36d5a4d640cdfc58b111dac7bd24dd9064d9f39fc42ba2880ae` | 879,634 |
| `Session Log 20260318.md` | `afcc9fee0427754f19861b0756e74dfa1ce68da982e0864699a4a4d719a8eff2` | 91,740 |
| `Session Log 20260319.md` | `88df8e2aa74d66d6f484a0fd96bc3a45a9e1a1283e920f9d2d72e7a9611c893e` | 47,162 |
| `Session Log 20260320.md` | `9c81a43d263c38a55bc43933fbf01b2ee18531a69d41221710f7c17e49ed385a` | 163,494 |
| `Session Log 20260321.md` | `f5f454504d38d14e3d12fa452bbdbfa6445f1b5ef78f6340e126ca100b4e9cf2` | 118,424 |
| `Session Log 20260322.md` | `7691dace8a6c2733bc8104fe5d23d51ac6db955e9a9aa81ebe29c9b4212eb321` | 84,034 |
| `Session Log 20260323-1.md` | `5e10ecffbd02ece7fc01ac4ba0e20a60051f9cdd4e43dfbaa270a78601ab7b37` | 101,449 |
| `Session Log 20260323.md` | `01a786fea0dcd8c9fa0920d4ff19be424184ad9d65ac33f81d653cc6f257a79d` | 16,586 |
| `Session Log 20260324.md` | `743d01c210be73980bcdb4534565b02143274abd22ae1a5932f0f0aa1d124bc5` | 112,113 |
| `Session Log 20260325.md` | `33eb2f70961ed57e909510c5c566dd5ff8e5c51c442ccf60c8a7cfd320ad7c9f` | 83,521 |
| `Session Log 20260326.md` | `1da1e4623d403e36262acbfce26205cbd79b2826f79cbac72f98e2c6e839e1e8` | 101,140 |
| `Session Log 20260327.md` | `ba6a8a18e55c26d881e8886e273f8904381c900539b018b7b0c74fb6780ab46d` | 245,055 |
| `Session Log 20260328.md` | `3fd1ffdec74214967f59acee4235f7fc5bed364313839df664504c136cd81a5d` | 199,634 |
| `Session Log 20260330.md` | `6d5882c583e353cd2335b9aeb46b6432fd10c54300b02fdfe950d1a20838e9b4` | 168,589 |
| `Session Log 20260331.md` | `60fd0404e609c2612b2f09f42b8931a2bcd881d224f7d9e910aa9004e995350e` | 170,059 |
| `Session Log 20260401.md` | `5a1f0f7cfad8b45a73aeb4622769d5428afc9aba3127b03fb9effe00138f36d5` | 108,110 |
| `Session Log 20260402.md` | `78d0790acf5a4662a7572ac39d8288d96801a9f556e6f05b83d79b0f2955f478` | 92,903 |
| `Session Log 20260403.md` | `ec7956e3e88e4bc963793ee9e6e5326cada4c6ee9d149f568d0de7e5a456d52b` | 105,681 |
| `Session Log 20260404.md` | `d9a3035e88e6e4d5cb211d05d53bb8cae03438c5ad70e8dea4ff365224efee30` | 140,351 |
| `Session Log 20260405.md` | `3fcf4f9efce42cdf047cb7f3753dee0ac8652b9ea109976cbe2aefdacd3684dc` | 55,594 |
| `Session Log 20260406.md` | `7221e296276423e467e773c3c995bee5c124ecc7024c90170c9e65a08f89fc39` | 142,767 |
| `Session Log 20260407.md` | `a68ec82cdc30d628dae4c44f613059cc41f7b7672a6397b9063842e66fa17676` | 59,220 |
| `Session Log 20260408.md` | `f1522c5ecbe321e5e844a135776d499cc7fdf08e3d194a5c96f0071494980a07` | 135,993 |
| `Session Log 20260409.md` | `fb6a53ef1f06fabfbaa107a456a157e503ae78ead9ac702463e23de123556b63` | 258,063 |
| `Session Log 20260410.md` | `7428ea64ef057fdcdc981d1dde95a41f9cd7a0d5a861b942cc7d8c490ab52dd3` | 39,712 |
| `Session Log 20260412.md` | `4fb6b26cde69b06d17d294063623e5e59fc06b2514ebecbfd26555d2fe346d79` | 569,357 |
| `Session Log 20260413.md` | `f3991fb0504dfc7738334d6dd2d92c95b9c7aebb35df4a2bbaafdbe3bb779087` | 21,601 |
| `Session Log 20260414.md` | `c3574bd2a4e3b0a6939cb4fdcb8e6a59681307ad34cd4fc1025a50d097320662` | 67,719 |
| `Session Log 20260415.md` | `b00b8bf9753b2e424f9c121cc1b113fdda53d33bc65fa523be108c3cfe38e1a7` | 89,678 |
| `Session Log 20260416.md` | `850c2b63ae1009f7507e5f8175d4297f6175481353fb1a1e88a995f2dcc641c2` | 101,610 |
| `Session Log 20260417.md` | `79954d3d1b1af475c95fe03ba6d4a8a9901dd46c78eed1a9124c327ce01115e3` | 117,017 |
| `Session Log 20260418.md` | `900201a2a8d0c75dd9d293656f22c7e133a296e7a9606b3e26e416e820a9fc66` | 109,766 |
| `Session Log 20260419.md` | `8cce2566c31a530ce981cdcaccbb7777a5fa3e62c7cc0751c8ad68beb728bc86` | 118,835 |
| `Session Log 20260420.md` | `bc20fe36c76b22f41644fc11889cbb2c71f5f04c3b1be93ddf14de626083ed48` | 168,209 |
| `Session Log 20260421.md` | `552e367cfa312a64b9330d815fafdc3b37ba6f92e927e5830b49235f25551435` | 120,683 |
| `Session Log 20260422.md` | `a7359e7e7daefc14418a4128e282055feaeb618abcbfc442e0b04b82d69fd437` | 190,257 |
| `Session Log 20260423.md` | `1e692373de9b36b5a6d636c495653da2c13a592c0463ed71c2c57e96b296c9b4` | 151,077 |
| `Session Log 20260424.md` | `4bc178bfcf570ad465ff1d240f5f26242c2828c1363b880e45dd40bd5d72fffb` | 67,662 |
| `Session Log 20260425.md` | `20f2b6105c22a5fae79993a511f4d358c4159975e2af16f8b15a6e8451f01404` | 221,663 |
| `Session Log 20260426.md` | `577c9da7cda5e248a8b0e28e94bac94933e2609548286eecee268ccdfe305af9` | 98,385 |
| `Session Log 20260427.md` | `4cf2a2c100def16be73807c36f07cce016dc38fa6f4936608e3c22bd8d7a235c` | 195,005 |
| `Session Log 20260429.md` | `75e53600ee9cf0ee2864636ea859b447154bf3d809fef77cd21141fed074b939` | 98,944 |
| `Session Log 20260430.md` | `f5e293ac381e5589b27ac4385451e5d89a4ffffe861b47d11def4c66d707e0a8` | 71,547 |
| `Session Log 20260501.md` | `5573824cd829fe6087879f423cddf1eff6377d17ebb519e681dfbf98dfa746d9` | 109,356 |
| `Session Log 20260502.md` | `115d592d483cec4d2607f4f904d030e4fedd4f4246196dd6d6a8b58e49e78020` | 84,522 |
| `Session Log 20260503.md` | `7e0b24f22dad45818f679aba11eac88f25ecaa5e21d57b4eb318b17ec0fd9202` | 90,454 |
| `Session Log 20260504.md` | `1a53018ce13e2922a3c4e0d05468ab531d2902d642883dc5964eb5faebef0f90` | 152,832 |
| `Session Log 20260514.md` | `53fb43e78f06bfc1aca154320fb7b4647226cb6065f2b0fffc6f996c80721d9c` | 16,049 |
| `Session Log 20260515.md` | `38a40846166986d320c11c8760007f457f4fbcd7d6af7f983c92bb13184855ad` | 33,166 |
| `Session Log 20260516.md` | `9848abebd33a9c2051ba8f2d0d6afcb856dc95728e67c0dfd0a248d4c59c407b` | 60,419 |
| `Session Log 20260517.md` | `bd83df41092bae132d6775b155768116926eec1f317a2ae2a26269ca0a019282` | 295,707 |
| `Session Log 20260518.md` | `1729519db61f4e710fc2f888e5ed01b5ca3391f9e104d934308b4bbf4b5dd720` | 152,266 |
| `Session Log 20260519.md` | `fb4c311382e096f1e2a1d00fff8f375987b8a205a77048f32884f50c4a5a9dbc` | 46,516 |
| `Session Log 20260520.md` | `76b5a7f1002d35e5a40dece7cd92f1561d595d4259f1d02aa1a3287ea1c141a0` | 201,056 |
| `Session Log 20260521.md` | `ee2e77e15440a0b8dde54bc76dacefe592471682b021b48ed53669fcddaa1a5f` | 307,835 |
| `Session Log 20260522.md` | `d1f1ad7283670720dbc5fb6a28ac4f92996e0a0926af57279a66577f6dac0129` | 226,956 |
| `Session Log 20260524.md` | `c41ba55bf8222d9a997c25397d988121aa4ffe8a44f88e382e38de65540bae68` | 44,539 |
| `Session Log 20260530.md` | `79ad27fe5b83ed11ef6cee494b658e3c5177e0e5ce449d3442b295e69f69443c` | 22,845 |
| `Session Log 20260531.md` | `6eb545a6a459feda70de0373bb1ecf756b3ba9f43a76ed3479d0e977eb0df95d` | 188,586 |
| `Session Log 20260601.md` | `ffaa7bd8b8f2d8aada50f9ed09d00ba7b8405ee78c10f9d28799e595a29b4e63` | 169,299 |
| `Session Log 20260602.md` | `0e0aef4666116811dfa8c4d5b9279616635f99847f27c7739a26160bf816fa33` | 239,132 |
| `Session Log 20260603.md` | `170708e46149ad0d33dbdb8263eb731ff07c83c46f1e6538bee38c5ca78cc456` | 148,394 |
| `Session Log 20260604.md` | `c3b237722c5781ce0e1067af056c0e93c20aac315e4d17a522af458d40ac5370` | 345,433 |
| `Session Log 20260605.md` | `573b01f64694c969b5ca49a23b94784ccc10190528c09a2fdda28a4d0f80b7ba` | 137,729 |
| `Session Log 20260607.md` | `5251663849e887ce88103ed2a584707f5f747e767c14ab79ee1d43ab409a4eeb` | 608,132 |
| `Session Log 20260608.md` | `f8385996e0c9d81ca5776603cffd02ff974abb9e33052cd033ecea527d8bb4b6` | 18,104 |
| `Session Log 20260609.md` | `b224c537d3822b283e6d5e816bbb2734eca1feef7d88b9a1d16ae358f1cf9947` | 143,288 |
| `Session Log 20260610.md` | `54b251ba81e422e9effe518d471bf97890d599c6f8d0ca65fc08d7e66bfa6946` | 129,184 |
| `Session Log 20260611.md` | `0bd33260f5abbcab675364a9da0d8c82c43bd71fec3d453727ca3e2add83c3b2` | 296,831 |
| `Session Log 20260612.md` | `81bab876bb45c08819f0a594e7092a1b32fcbae3d69f76dd39b712d9984432a9` | 158,272 |
| `Session Log 20260613.md` | `32ea9e39815748b65cd1e901f98ea98c2d87d2b80eeb4c9f09c45c63be269843` | 64,215 |
| `Session Log 20260614.md` | `ef3091826092b0a98c71dc84c44b8aa32f6e2a4b39e6d588b74a14675f46516c` | 30,031 |
| `Session Log 20260615.md` | `51312854499f22f838aba94898a1ce0d4d4bd0f016ffc779f14f61b6af698eee` | 187,554 |
| `Session Log 20260616.md` | `c20e2cf85ab9360edd72e845b045b20d7bdf022fd9718d30fdc9a964ded3158c` | 121,593 |
| `Session Log 20260617.md` | `c2e2bafd2bcf03809798eb7e587f780512b17ae1c8db10c18c1647ff74eea71d` | 70,925 |
| `Session Log 20260618.md` | `87055ed4721116a341c03850669008799a24d16a918cd13f4d7de6b29c8dc996` | 243,273 |
| `Session Log 20260619.md` | `bab2de28030c4498fbcedba1fc1e401635958e06a16ef065618e7c856198360b` | 63,585 |
| `Session Log 20260621.md` | `4b78fbd894e2493bd57ec3ab47cf63fbca1187e9f904d955084ca19212c7bb1a` | 40,096 |
| `Session Log 20260622.md` | `18306185c3763b3774f2bb29bd77efa56c0c4edc6c4d6204c85c001ab9248204` | 57,893 |
| `Session Log 20260624.md` | `3d388370df9012eab27a14fb4e0977696a20e9bb71662196f99b90c94db40161` | 75,029 |
| `Session Log 20260625.md` | `98556d87428ed87fcbc01490bc1373945e77165dc1966e71419a775ba351560d` | 91,334 |
| `Session Log 20260626.md` | `42d18e34fcfda2000ca5a2c68deea80e3803f6ed6d03b61fee107f7a2b6b7fcb` | 75,254 |
| `Session Log 20260627.md` | `d60c99be11d9f2c6c1d8405235378520c15c25165221c1100a26a6d975296ad7` | 49,757 |
| `Session Log 20260629.md` | `19f4acddcba3f0855acf7a4cf3614acad970104d69304dc13b8a52970605965d` | 89,715 |
| `Session Log 20260630.md` | `b3844edb75243a75b3906d788d2505f6d59ad2dca371d9099d8a2c05accefce8` | 139,048 |
| `Session Log 20260701.md` | `54b1c570c55914197c22385d9fa775a51bed7cc6f1a693b93f479bb0427c2a22` | 106,808 |
| `Session Log 20260702.md` | `18f372c95b4700d99fd85931afa120cc9f55e54d84553ea64e5d486e31d83a61` | 32,331 |
| `Session Log 20260703.md` | `7e6a4b7417086b250857e6471b583d404ca91520d51717811c092da226a6ae1e` | 15,308 |
| `Session Log 20260704.md` | `f725f7e78bc8a5998c8a7c9d49ce084349452313b0385c3472e7a0609d3b31ea` | 65,752 |
| `Session Log 20260705.md` | `4cb8f03dc7559ec6acf4918a636a64edab0f7ef83787eb927bd400a4759b52bb` | 168,793 |
| `Session Log 20260706.md` | `fe7133ac227bf9df5344bc67a20dd25cdfffcd55a6a26a6f107492cc3fb1364d` | 34,392 |
| `Session Log 20260707.md` | `fda539ed589187497832a341f061844058baf6aedff06d4e19416f1a03aa0752` | 30,371 |
| `Session Log 20260709.md` | `cc8b0c1e798b696acbdbe1f404f5091a7b40d2a6798006b683f2d0d08bfae636` | 44,277 |
| `Session Log 20260713.md` | `580dec1c79a70e325eaa5be0dce29d8a4fa33a7c9f7ae3f5ef20cab0a903d83a` | 108,178 |
| `Session Log 20260715.md` | `72f9b6e349a64f172090254ceb06cc62b07865703bd957ffb59c153620f6a217` | 17,720 |
| `Session Log 20260716.md` | `2e8818d20dd2be01754f50be066530f4f34d1fa7ba785d7207de8934e43b17c4` | 65,224 |
| `Session Log 20260717.md` | `6485f67d6a59566a7b6a23db4264966a3992f87013fed995bc4d931b1ef21fdf` | 22,214 |
| `Session Log 20260719.md` | `a51d4d0368ecd6212ffab90a1f6d255f6aa767693e3876d41c5108a2fc6e018a` | 124,836 |
| `Session Log 20260720.md` | `ce15320d1fec3cbd44a0b214667b300c9b7b06201efa92a6d3864c3f654b69f2` | 46,315 |
| `Session Log 20260721.md` | `28bf6617949f1b4e8b431d04494095827eec7d4fb852029c2e6617a32d17604a` | 14,819 |
| `Session Log 20260724.md` | `5a8495d7e43b93359f9b6222f3c11c3d5a0a69ae20a861f8b1f90b522500623f` | 107,767 |
| `Session Log 20260725.md` | `46c63b84ee2bafe9475c1db16bd39eda89fc5ee8b13dd691ec7a47e1d2bb5bbb` | 83,754 |
| `Session Log 20260728.md` | `967374469bf0a9652d8022ab78b1f5ddae7aba7d30e2f1b3dc0ea90656eaf126` | 61,501 |
| `Session Log 20260729.md` | `94b0bee87903daaf834a8f494d16b5c3a07daf4156749db3d012932e89198fe1` | 14,750 |
| `Session Log 20260730.md` | `327e0e17118378cbfc208108026ce249c18286a29030cb4984a923feec9a24b2` | 651,604 |
| `Session Log 20260802.md` | `b649be827471b84c1ed4049f25e0dc32b188b13a688d5160299018f67924b356` | 354,780 |
| `Session Log 20260803.md` | `2b71ebd439c538ad6c9b69dfd5753ba33309e0666bdfbb48b5855def55072b36` | 253,493 |
| `Session Log 20260804.md` | `1064cf64f76bc9ee23542e7623e5f398c8e83f1523fc5abdc51217391cfc08e4` | 89,460 |
| `Session Log 20260805.md` | `55682891dae985f09ed275c615c2e7ec3985f35dd33e0e0d9e8048fb44140c8d` | 102,527 |
| `Session Log 20260806.md` | `aa8c9d46e0a837e9966491d57c822914012f7f81e8c66e81f685279b3651b891` | 940,891 |
| `Session Log 20260807.md` | `eee05e2e316fe7d51652b91b758c91cb584623c12979ab37a354088a950b4823` | 23,372 |
| `Session Log 20260808.md` | `8869fa7f7f8bb3fbfdc7cdff968f3b0963b1abc076a7955b33d232d07521ff33` | 274,349 |
| `Session Log 20260809.md` | `3306753b4a091ca019a18850a5469bcacff30daea087522e1b144a5268107e45` | 21,314 |
| `Session Log 20260810.md` | `5062a6575ccc4ad6f54bc8f688627d5179a50abb58b499d20e81397c6505ccce` | 123,338 |
| `Session Log 20260811.md` | `a95858a0e1e049eb3ec9605e55238b8c646fea79923f4f9fac56290888357ada` | 148,353 |
| `Session Log 20260812.md` | `2385c317fdc8262186232571e2b503c13db5320146547634fa2d5572e8f1e626` | 99,219 |
| `Session Log 20260813.md` | `8391c5b917064ccb15a764ebed9ed57c1c170d459185c6c8ab27e439a9272eae` | 100,537 |
| `Session Log 20260814.md` | `a46c376f5a85b2d013e22df8943057dd076193317e17657d56b5297c61a2ef9d` | 25,845 |
| `Session Log 20260815.md` | `738ecc46a4b890b65b33b83234094f723ba0e6d0873a24e62e0338383ebb3e6c` | 6,382 |
| `Session Log 20260817.md` | `a0c976715c09c930d157083f28b9e6e530dc142a0d5164a804747384d4a92df8` | 35,195 |
| `Session Log 20260818.md` | `059a8a1d6ac2eea1fade243796aada1281bf3bfc21ed9b2ba3b0ad2863bb602e` | 2,768 |
| `Session Log 20260819.md` | `01727f99ac37b07b117367ae0c9c90177923ae8d7e56b8ac1e7860dfbc894327` | 41,500 |
| `Session Log 20260821.md` | `fc36d8b05f35c12e94fc911fa68c6def009b8ee2fe90293e325c9f9b6033c3e6` | 39,416 |
| `Session Log 20260822.md` | `7e51f8d30373b59f3f762175794a0a42938cfa9da84797cbf92fdae77bdd21ee` | 6,107 |
| `Session Log 20260826.md` | `12904ab3d7b284f69a9159d27702292eb41e18cf9ce9f31b74e376024ee43340` | 16,083 |
| `Session Log 20260827.md` | `c9dbbd6f9a0cd454e988ebb461c5f225a031e5453966698302915275a0889a07` | 6,384 |
| `Verbatim Chat Session Claude Code Desktop 20260317.md` | `c9959fd4bb95991646f8f349daad9aaf5e36a1cb42c4619fa526a4223ad0aa71` | 72,351 |
| `dockercompselogs.txt` | `060e4d3479c755697c5c3194c6851c80ab1317e6790cdedd9322588417af2724` | 1,583 |

## Machine-readable

```json
{
  "schema": "prompttracking-corpus-manifest/1",
  "root_sha256": "e15144f220d759863ad00c5b11edc3350b1ecf1fb62ab66d3bd1101ef617f106",
  "file_count": 173,
  "total_bytes": 22269243,
  "generated_at_utc": "2026-08-27T20:03:41Z",
  "files": [
    {
      "name": "Claude-output-logs-20260706-12-25am.txt",
      "sha256": "f844a22630773515ed6b98a54f7ba1bf32ff0598f7353c4587cdcff2a46e0e92",
      "bytes": 67860
    },
    {
      "name": "HANDOFF_20260805.md",
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "bytes": 0
    },
    {
      "name": "Memory Log 20260426.md",
      "sha256": "5d460385e3a5c3063f96eb0f3e8f0987526b6527fd50ac6e4060fd3f933d43a3",
      "bytes": 401632
    },
    {
      "name": "Memory Log 20260427.md",
      "sha256": "50722be120911672f03cf0917d7c0d3a4986bbfcd43d4ff31a4768b094e35c7a",
      "bytes": 457354
    },
    {
      "name": "Memory Log 20260429.md",
      "sha256": "1a9238b7eedb6af12093c73022817f9b76a3761ad2b60fb2d5b580573281b026",
      "bytes": 466781
    },
    {
      "name": "Next Session Copilot 20260504.md",
      "sha256": "d4855d871f037b03a98c9633e10de876dc0ef8810135116d3bfd15cdf5ea00f6",
      "bytes": 1422
    },
    {
      "name": "Next Session Prompt 20260430.md",
      "sha256": "16bdb45f7dcadf515b47c9e1403857940b69fb4fecda195e4130224bf1620adb",
      "bytes": 10875
    },
    {
      "name": "Next Session Prompt 20260501.md",
      "sha256": "252f30fff0ec3cac15b63ef1dd2874bcc68b38665779295a36e5a5cb982b15f0",
      "bytes": 7774
    },
    {
      "name": "Next Session Prompt 20260502.md",
      "sha256": "5a9d7accdaae63816b474d6207bfc3dfdbd0a0d398e0ec118eb02829f1361cd1",
      "bytes": 9356
    },
    {
      "name": "Next Session Prompt 20260503.md",
      "sha256": "84261c312d0d8c0688bba5701bc20a64e3503fb0818543df640b056b7a6242c6",
      "bytes": 5775
    },
    {
      "name": "Next Session Prompt 20260504.md",
      "sha256": "f537dbf2df429dbd4472625df0e17700d470c23286421bdec8e79695cabb2c82",
      "bytes": 6219
    },
    {
      "name": "Session Log 2026-06-15 Pacing WO-040.md",
      "sha256": "8d051a7b9ee4a384664ee603b632f181f3e6cb9ac8e84408aa938e9a7a2ed92a",
      "bytes": 3373
    },
    {
      "name": "Session Log 20260205.md",
      "sha256": "466bc904feabca7a1960e56f5b4adae5560f0256d09cf5599c013960491553b9",
      "bytes": 98387
    },
    {
      "name": "Session Log 20260206.md",
      "sha256": "c543cc276b1f7e597399ce7e6d71bad7b7c5ef0c22f8b1e332de78085c20005a",
      "bytes": 129155
    },
    {
      "name": "Session Log 20260207.md",
      "sha256": "bb1a17b049cd6e9369455bb1d44caa8849c9d591d7b3da7723a00226fe446707",
      "bytes": 38038
    },
    {
      "name": "Session Log 20260208.md",
      "sha256": "0a5dbf1190bf1ad9503616ec2ef8f638f05625886d8affe48ab9c0fe16629b5c",
      "bytes": 143793
    },
    {
      "name": "Session Log 20260209.md",
      "sha256": "0af566a7f40f622fbab9a3922e2e356d83d73054f2345502ee69ad7515a3f403",
      "bytes": 121290
    },
    {
      "name": "Session Log 20260210.md",
      "sha256": "edc2f9f526dbd069ee5bdb9ab9d9a890b5368aadd636702aec497bc950610c3a",
      "bytes": 164418
    },
    {
      "name": "Session Log 20260211.md",
      "sha256": "a8b52572a79c896a7ab91c2938c71f4b7e622b3af680c446d3e14566e724db00",
      "bytes": 146092
    },
    {
      "name": "Session Log 20260212.md",
      "sha256": "93bbef13a671f8cd1d91b287c53f5882cd7d7f00a20e41168895e2d67f5e1f2f",
      "bytes": 132416
    },
    {
      "name": "Session Log 20260213.md",
      "sha256": "c077cf1e3f05f9fd54e05ecb582fe7b4a998548d28c6d959c807ac7d0432fab6",
      "bytes": 169162
    },
    {
      "name": "Session Log 20260214.md",
      "sha256": "5df11883fdcecfee75817a4e8f415a8f05e5e65cac30b7269ae68743cde04a58",
      "bytes": 111702
    },
    {
      "name": "Session Log 20260215.md",
      "sha256": "fc544831d30c5b3027d2268ffa80a30e21695b6454eeec7a7ae9029cf225241c",
      "bytes": 127124
    },
    {
      "name": "Session Log 20260216.md",
      "sha256": "e4fd42e2c1e46dbbcf01004949f3fff0d05868dbb3dae44c90ccce44a777e565",
      "bytes": 199581
    },
    {
      "name": "Session Log 20260217.md",
      "sha256": "d0533a1fdbbb419ee53eed582a836097b94b68771addd1be44ccdd2e5bc8d2d8",
      "bytes": 134000
    },
    {
      "name": "Session Log 20260218.md",
      "sha256": "7148f62d65b2b2b91cf9366b20678ce8785f6fd116e95c97c6fbe79b143e30be",
      "bytes": 43690
    },
    {
      "name": "Session Log 20260219.md",
      "sha256": "86fac886efbd6a51bc8d2ad999f1883c61eefe7fe9a3301b5e54e26bba01a3e9",
      "bytes": 62946
    },
    {
      "name": "Session Log 20260220.md",
      "sha256": "de733a62a053418b5ffe92ddde3a371b5cc260546bb647b9b0bbf1d6ab6bf692",
      "bytes": 1617
    },
    {
      "name": "Session Log 20260225.md",
      "sha256": "e839e08cc5b539562721926dd5d38956140c681a8b63b8f0e9bb11678992cdd6",
      "bytes": 25260
    },
    {
      "name": "Session Log 20260226.md",
      "sha256": "99c91bfaf41a2fa4720f0d1e73a6a75823588d79ac2ba732d01fe7238301a7cd",
      "bytes": 17762
    },
    {
      "name": "Session Log 20260227.md",
      "sha256": "9b095c7884c27b3ce1743235e1edd30feb18bdc8a299755153d9d988384b10f2",
      "bytes": 228868
    },
    {
      "name": "Session Log 20260301.md",
      "sha256": "756a5fd2d1dec94a1957c7ca2770be788082728ce9e0e0b7ee58ed8973f21858",
      "bytes": 58255
    },
    {
      "name": "Session Log 20260302.md",
      "sha256": "4fc7cefdb73aeb09dfb11f63addaec4928d5051de1d63529712a499a50279475",
      "bytes": 117347
    },
    {
      "name": "Session Log 20260303.md",
      "sha256": "b0480e7b31cca2536a8dd050c56397b6a3e0e663663904608e6f6f13356b1734",
      "bytes": 31412
    },
    {
      "name": "Session Log 20260304.md",
      "sha256": "dfd994bf83e8fe0b6c0786ab6bb8e4fbe1440f31fc970f809952479977288d15",
      "bytes": 109995
    },
    {
      "name": "Session Log 20260306.md",
      "sha256": "7122895f39e8be43a08b0fd4d01ef31beef36f51340f96246a52b521d6e1c63d",
      "bytes": 143606
    },
    {
      "name": "Session Log 20260308.md",
      "sha256": "7f2deafbad9cceef5e0cdc89c12a6265ef6050989a915a190a743726c0b84324",
      "bytes": 36442
    },
    {
      "name": "Session Log 20260310.md",
      "sha256": "0ecb531d2ece90a0f551d2fa102bf12fa47bdd57870038e1f65ca7d6af3ccbec",
      "bytes": 90566
    },
    {
      "name": "Session Log 20260311.md",
      "sha256": "330efc138f3789f4d1daa62263f877ef669eb5e377be65aafacf58e089ab49cd",
      "bytes": 273813
    },
    {
      "name": "Session Log 20260312.md",
      "sha256": "4088033cb9b392d1c8dda6bd9a096e94c49290f3ac9253704768783611e857e0",
      "bytes": 70590
    },
    {
      "name": "Session Log 20260313.md",
      "sha256": "9c70eda803db9e8fb2e24eb0b9cc756166d1991772b1ae4d8e8c310da55cefe9",
      "bytes": 64661
    },
    {
      "name": "Session Log 20260315.md",
      "sha256": "44d5877e9f9f60d4665b11f145bba5373182ae066880e58d84b30233e12a54c4",
      "bytes": 45920
    },
    {
      "name": "Session Log 20260316.md",
      "sha256": "cbd2458b77ce060511383c855050deb80466cee58b1c46aecca3a2ecea8a8ee7",
      "bytes": 89192
    },
    {
      "name": "Session Log 20260317-part-1.md",
      "sha256": "9e3fc3616a309fb51ab07f13bc88a16768d7209873628409dc2b07c9781d4a9c",
      "bytes": 261731
    },
    {
      "name": "Session Log 20260317-part-2.md",
      "sha256": "22de5bed38fe19a28cd0ea686215b4f92ed72384299bf8fa3cf68b74eb1274d0",
      "bytes": 613783
    },
    {
      "name": "Session Log 20260317.md",
      "sha256": "17eb4fe534bba36d5a4d640cdfc58b111dac7bd24dd9064d9f39fc42ba2880ae",
      "bytes": 879634
    },
    {
      "name": "Session Log 20260318.md",
      "sha256": "afcc9fee0427754f19861b0756e74dfa1ce68da982e0864699a4a4d719a8eff2",
      "bytes": 91740
    },
    {
      "name": "Session Log 20260319.md",
      "sha256": "88df8e2aa74d66d6f484a0fd96bc3a45a9e1a1283e920f9d2d72e7a9611c893e",
      "bytes": 47162
    },
    {
      "name": "Session Log 20260320.md",
      "sha256": "9c81a43d263c38a55bc43933fbf01b2ee18531a69d41221710f7c17e49ed385a",
      "bytes": 163494
    },
    {
      "name": "Session Log 20260321.md",
      "sha256": "f5f454504d38d14e3d12fa452bbdbfa6445f1b5ef78f6340e126ca100b4e9cf2",
      "bytes": 118424
    },
    {
      "name": "Session Log 20260322.md",
      "sha256": "7691dace8a6c2733bc8104fe5d23d51ac6db955e9a9aa81ebe29c9b4212eb321",
      "bytes": 84034
    },
    {
      "name": "Session Log 20260323-1.md",
      "sha256": "5e10ecffbd02ece7fc01ac4ba0e20a60051f9cdd4e43dfbaa270a78601ab7b37",
      "bytes": 101449
    },
    {
      "name": "Session Log 20260323.md",
      "sha256": "01a786fea0dcd8c9fa0920d4ff19be424184ad9d65ac33f81d653cc6f257a79d",
      "bytes": 16586
    },
    {
      "name": "Session Log 20260324.md",
      "sha256": "743d01c210be73980bcdb4534565b02143274abd22ae1a5932f0f0aa1d124bc5",
      "bytes": 112113
    },
    {
      "name": "Session Log 20260325.md",
      "sha256": "33eb2f70961ed57e909510c5c566dd5ff8e5c51c442ccf60c8a7cfd320ad7c9f",
      "bytes": 83521
    },
    {
      "name": "Session Log 20260326.md",
      "sha256": "1da1e4623d403e36262acbfce26205cbd79b2826f79cbac72f98e2c6e839e1e8",
      "bytes": 101140
    },
    {
      "name": "Session Log 20260327.md",
      "sha256": "ba6a8a18e55c26d881e8886e273f8904381c900539b018b7b0c74fb6780ab46d",
      "bytes": 245055
    },
    {
      "name": "Session Log 20260328.md",
      "sha256": "3fd1ffdec74214967f59acee4235f7fc5bed364313839df664504c136cd81a5d",
      "bytes": 199634
    },
    {
      "name": "Session Log 20260330.md",
      "sha256": "6d5882c583e353cd2335b9aeb46b6432fd10c54300b02fdfe950d1a20838e9b4",
      "bytes": 168589
    },
    {
      "name": "Session Log 20260331.md",
      "sha256": "60fd0404e609c2612b2f09f42b8931a2bcd881d224f7d9e910aa9004e995350e",
      "bytes": 170059
    },
    {
      "name": "Session Log 20260401.md",
      "sha256": "5a1f0f7cfad8b45a73aeb4622769d5428afc9aba3127b03fb9effe00138f36d5",
      "bytes": 108110
    },
    {
      "name": "Session Log 20260402.md",
      "sha256": "78d0790acf5a4662a7572ac39d8288d96801a9f556e6f05b83d79b0f2955f478",
      "bytes": 92903
    },
    {
      "name": "Session Log 20260403.md",
      "sha256": "ec7956e3e88e4bc963793ee9e6e5326cada4c6ee9d149f568d0de7e5a456d52b",
      "bytes": 105681
    },
    {
      "name": "Session Log 20260404.md",
      "sha256": "d9a3035e88e6e4d5cb211d05d53bb8cae03438c5ad70e8dea4ff365224efee30",
      "bytes": 140351
    },
    {
      "name": "Session Log 20260405.md",
      "sha256": "3fcf4f9efce42cdf047cb7f3753dee0ac8652b9ea109976cbe2aefdacd3684dc",
      "bytes": 55594
    },
    {
      "name": "Session Log 20260406.md",
      "sha256": "7221e296276423e467e773c3c995bee5c124ecc7024c90170c9e65a08f89fc39",
      "bytes": 142767
    },
    {
      "name": "Session Log 20260407.md",
      "sha256": "a68ec82cdc30d628dae4c44f613059cc41f7b7672a6397b9063842e66fa17676",
      "bytes": 59220
    },
    {
      "name": "Session Log 20260408.md",
      "sha256": "f1522c5ecbe321e5e844a135776d499cc7fdf08e3d194a5c96f0071494980a07",
      "bytes": 135993
    },
    {
      "name": "Session Log 20260409.md",
      "sha256": "fb6a53ef1f06fabfbaa107a456a157e503ae78ead9ac702463e23de123556b63",
      "bytes": 258063
    },
    {
      "name": "Session Log 20260410.md",
      "sha256": "7428ea64ef057fdcdc981d1dde95a41f9cd7a0d5a861b942cc7d8c490ab52dd3",
      "bytes": 39712
    },
    {
      "name": "Session Log 20260412.md",
      "sha256": "4fb6b26cde69b06d17d294063623e5e59fc06b2514ebecbfd26555d2fe346d79",
      "bytes": 569357
    },
    {
      "name": "Session Log 20260413.md",
      "sha256": "f3991fb0504dfc7738334d6dd2d92c95b9c7aebb35df4a2bbaafdbe3bb779087",
      "bytes": 21601
    },
    {
      "name": "Session Log 20260414.md",
      "sha256": "c3574bd2a4e3b0a6939cb4fdcb8e6a59681307ad34cd4fc1025a50d097320662",
      "bytes": 67719
    },
    {
      "name": "Session Log 20260415.md",
      "sha256": "b00b8bf9753b2e424f9c121cc1b113fdda53d33bc65fa523be108c3cfe38e1a7",
      "bytes": 89678
    },
    {
      "name": "Session Log 20260416.md",
      "sha256": "850c2b63ae1009f7507e5f8175d4297f6175481353fb1a1e88a995f2dcc641c2",
      "bytes": 101610
    },
    {
      "name": "Session Log 20260417.md",
      "sha256": "79954d3d1b1af475c95fe03ba6d4a8a9901dd46c78eed1a9124c327ce01115e3",
      "bytes": 117017
    },
    {
      "name": "Session Log 20260418.md",
      "sha256": "900201a2a8d0c75dd9d293656f22c7e133a296e7a9606b3e26e416e820a9fc66",
      "bytes": 109766
    },
    {
      "name": "Session Log 20260419.md",
      "sha256": "8cce2566c31a530ce981cdcaccbb7777a5fa3e62c7cc0751c8ad68beb728bc86",
      "bytes": 118835
    },
    {
      "name": "Session Log 20260420.md",
      "sha256": "bc20fe36c76b22f41644fc11889cbb2c71f5f04c3b1be93ddf14de626083ed48",
      "bytes": 168209
    },
    {
      "name": "Session Log 20260421.md",
      "sha256": "552e367cfa312a64b9330d815fafdc3b37ba6f92e927e5830b49235f25551435",
      "bytes": 120683
    },
    {
      "name": "Session Log 20260422.md",
      "sha256": "a7359e7e7daefc14418a4128e282055feaeb618abcbfc442e0b04b82d69fd437",
      "bytes": 190257
    },
    {
      "name": "Session Log 20260423.md",
      "sha256": "1e692373de9b36b5a6d636c495653da2c13a592c0463ed71c2c57e96b296c9b4",
      "bytes": 151077
    },
    {
      "name": "Session Log 20260424.md",
      "sha256": "4bc178bfcf570ad465ff1d240f5f26242c2828c1363b880e45dd40bd5d72fffb",
      "bytes": 67662
    },
    {
      "name": "Session Log 20260425.md",
      "sha256": "20f2b6105c22a5fae79993a511f4d358c4159975e2af16f8b15a6e8451f01404",
      "bytes": 221663
    },
    {
      "name": "Session Log 20260426.md",
      "sha256": "577c9da7cda5e248a8b0e28e94bac94933e2609548286eecee268ccdfe305af9",
      "bytes": 98385
    },
    {
      "name": "Session Log 20260427.md",
      "sha256": "4cf2a2c100def16be73807c36f07cce016dc38fa6f4936608e3c22bd8d7a235c",
      "bytes": 195005
    },
    {
      "name": "Session Log 20260429.md",
      "sha256": "75e53600ee9cf0ee2864636ea859b447154bf3d809fef77cd21141fed074b939",
      "bytes": 98944
    },
    {
      "name": "Session Log 20260430.md",
      "sha256": "f5e293ac381e5589b27ac4385451e5d89a4ffffe861b47d11def4c66d707e0a8",
      "bytes": 71547
    },
    {
      "name": "Session Log 20260501.md",
      "sha256": "5573824cd829fe6087879f423cddf1eff6377d17ebb519e681dfbf98dfa746d9",
      "bytes": 109356
    },
    {
      "name": "Session Log 20260502.md",
      "sha256": "115d592d483cec4d2607f4f904d030e4fedd4f4246196dd6d6a8b58e49e78020",
      "bytes": 84522
    },
    {
      "name": "Session Log 20260503.md",
      "sha256": "7e0b24f22dad45818f679aba11eac88f25ecaa5e21d57b4eb318b17ec0fd9202",
      "bytes": 90454
    },
    {
      "name": "Session Log 20260504.md",
      "sha256": "1a53018ce13e2922a3c4e0d05468ab531d2902d642883dc5964eb5faebef0f90",
      "bytes": 152832
    },
    {
      "name": "Session Log 20260514.md",
      "sha256": "53fb43e78f06bfc1aca154320fb7b4647226cb6065f2b0fffc6f996c80721d9c",
      "bytes": 16049
    },
    {
      "name": "Session Log 20260515.md",
      "sha256": "38a40846166986d320c11c8760007f457f4fbcd7d6af7f983c92bb13184855ad",
      "bytes": 33166
    },
    {
      "name": "Session Log 20260516.md",
      "sha256": "9848abebd33a9c2051ba8f2d0d6afcb856dc95728e67c0dfd0a248d4c59c407b",
      "bytes": 60419
    },
    {
      "name": "Session Log 20260517.md",
      "sha256": "bd83df41092bae132d6775b155768116926eec1f317a2ae2a26269ca0a019282",
      "bytes": 295707
    },
    {
      "name": "Session Log 20260518.md",
      "sha256": "1729519db61f4e710fc2f888e5ed01b5ca3391f9e104d934308b4bbf4b5dd720",
      "bytes": 152266
    },
    {
      "name": "Session Log 20260519.md",
      "sha256": "fb4c311382e096f1e2a1d00fff8f375987b8a205a77048f32884f50c4a5a9dbc",
      "bytes": 46516
    },
    {
      "name": "Session Log 20260520.md",
      "sha256": "76b5a7f1002d35e5a40dece7cd92f1561d595d4259f1d02aa1a3287ea1c141a0",
      "bytes": 201056
    },
    {
      "name": "Session Log 20260521.md",
      "sha256": "ee2e77e15440a0b8dde54bc76dacefe592471682b021b48ed53669fcddaa1a5f",
      "bytes": 307835
    },
    {
      "name": "Session Log 20260522.md",
      "sha256": "d1f1ad7283670720dbc5fb6a28ac4f92996e0a0926af57279a66577f6dac0129",
      "bytes": 226956
    },
    {
      "name": "Session Log 20260524.md",
      "sha256": "c41ba55bf8222d9a997c25397d988121aa4ffe8a44f88e382e38de65540bae68",
      "bytes": 44539
    },
    {
      "name": "Session Log 20260530.md",
      "sha256": "79ad27fe5b83ed11ef6cee494b658e3c5177e0e5ce449d3442b295e69f69443c",
      "bytes": 22845
    },
    {
      "name": "Session Log 20260531.md",
      "sha256": "6eb545a6a459feda70de0373bb1ecf756b3ba9f43a76ed3479d0e977eb0df95d",
      "bytes": 188586
    },
    {
      "name": "Session Log 20260601.md",
      "sha256": "ffaa7bd8b8f2d8aada50f9ed09d00ba7b8405ee78c10f9d28799e595a29b4e63",
      "bytes": 169299
    },
    {
      "name": "Session Log 20260602.md",
      "sha256": "0e0aef4666116811dfa8c4d5b9279616635f99847f27c7739a26160bf816fa33",
      "bytes": 239132
    },
    {
      "name": "Session Log 20260603.md",
      "sha256": "170708e46149ad0d33dbdb8263eb731ff07c83c46f1e6538bee38c5ca78cc456",
      "bytes": 148394
    },
    {
      "name": "Session Log 20260604.md",
      "sha256": "c3b237722c5781ce0e1067af056c0e93c20aac315e4d17a522af458d40ac5370",
      "bytes": 345433
    },
    {
      "name": "Session Log 20260605.md",
      "sha256": "573b01f64694c969b5ca49a23b94784ccc10190528c09a2fdda28a4d0f80b7ba",
      "bytes": 137729
    },
    {
      "name": "Session Log 20260607.md",
      "sha256": "5251663849e887ce88103ed2a584707f5f747e767c14ab79ee1d43ab409a4eeb",
      "bytes": 608132
    },
    {
      "name": "Session Log 20260608.md",
      "sha256": "f8385996e0c9d81ca5776603cffd02ff974abb9e33052cd033ecea527d8bb4b6",
      "bytes": 18104
    },
    {
      "name": "Session Log 20260609.md",
      "sha256": "b224c537d3822b283e6d5e816bbb2734eca1feef7d88b9a1d16ae358f1cf9947",
      "bytes": 143288
    },
    {
      "name": "Session Log 20260610.md",
      "sha256": "54b251ba81e422e9effe518d471bf97890d599c6f8d0ca65fc08d7e66bfa6946",
      "bytes": 129184
    },
    {
      "name": "Session Log 20260611.md",
      "sha256": "0bd33260f5abbcab675364a9da0d8c82c43bd71fec3d453727ca3e2add83c3b2",
      "bytes": 296831
    },
    {
      "name": "Session Log 20260612.md",
      "sha256": "81bab876bb45c08819f0a594e7092a1b32fcbae3d69f76dd39b712d9984432a9",
      "bytes": 158272
    },
    {
      "name": "Session Log 20260613.md",
      "sha256": "32ea9e39815748b65cd1e901f98ea98c2d87d2b80eeb4c9f09c45c63be269843",
      "bytes": 64215
    },
    {
      "name": "Session Log 20260614.md",
      "sha256": "ef3091826092b0a98c71dc84c44b8aa32f6e2a4b39e6d588b74a14675f46516c",
      "bytes": 30031
    },
    {
      "name": "Session Log 20260615.md",
      "sha256": "51312854499f22f838aba94898a1ce0d4d4bd0f016ffc779f14f61b6af698eee",
      "bytes": 187554
    },
    {
      "name": "Session Log 20260616.md",
      "sha256": "c20e2cf85ab9360edd72e845b045b20d7bdf022fd9718d30fdc9a964ded3158c",
      "bytes": 121593
    },
    {
      "name": "Session Log 20260617.md",
      "sha256": "c2e2bafd2bcf03809798eb7e587f780512b17ae1c8db10c18c1647ff74eea71d",
      "bytes": 70925
    },
    {
      "name": "Session Log 20260618.md",
      "sha256": "87055ed4721116a341c03850669008799a24d16a918cd13f4d7de6b29c8dc996",
      "bytes": 243273
    },
    {
      "name": "Session Log 20260619.md",
      "sha256": "bab2de28030c4498fbcedba1fc1e401635958e06a16ef065618e7c856198360b",
      "bytes": 63585
    },
    {
      "name": "Session Log 20260621.md",
      "sha256": "4b78fbd894e2493bd57ec3ab47cf63fbca1187e9f904d955084ca19212c7bb1a",
      "bytes": 40096
    },
    {
      "name": "Session Log 20260622.md",
      "sha256": "18306185c3763b3774f2bb29bd77efa56c0c4edc6c4d6204c85c001ab9248204",
      "bytes": 57893
    },
    {
      "name": "Session Log 20260624.md",
      "sha256": "3d388370df9012eab27a14fb4e0977696a20e9bb71662196f99b90c94db40161",
      "bytes": 75029
    },
    {
      "name": "Session Log 20260625.md",
      "sha256": "98556d87428ed87fcbc01490bc1373945e77165dc1966e71419a775ba351560d",
      "bytes": 91334
    },
    {
      "name": "Session Log 20260626.md",
      "sha256": "42d18e34fcfda2000ca5a2c68deea80e3803f6ed6d03b61fee107f7a2b6b7fcb",
      "bytes": 75254
    },
    {
      "name": "Session Log 20260627.md",
      "sha256": "d60c99be11d9f2c6c1d8405235378520c15c25165221c1100a26a6d975296ad7",
      "bytes": 49757
    },
    {
      "name": "Session Log 20260629.md",
      "sha256": "19f4acddcba3f0855acf7a4cf3614acad970104d69304dc13b8a52970605965d",
      "bytes": 89715
    },
    {
      "name": "Session Log 20260630.md",
      "sha256": "b3844edb75243a75b3906d788d2505f6d59ad2dca371d9099d8a2c05accefce8",
      "bytes": 139048
    },
    {
      "name": "Session Log 20260701.md",
      "sha256": "54b1c570c55914197c22385d9fa775a51bed7cc6f1a693b93f479bb0427c2a22",
      "bytes": 106808
    },
    {
      "name": "Session Log 20260702.md",
      "sha256": "18f372c95b4700d99fd85931afa120cc9f55e54d84553ea64e5d486e31d83a61",
      "bytes": 32331
    },
    {
      "name": "Session Log 20260703.md",
      "sha256": "7e6a4b7417086b250857e6471b583d404ca91520d51717811c092da226a6ae1e",
      "bytes": 15308
    },
    {
      "name": "Session Log 20260704.md",
      "sha256": "f725f7e78bc8a5998c8a7c9d49ce084349452313b0385c3472e7a0609d3b31ea",
      "bytes": 65752
    },
    {
      "name": "Session Log 20260705.md",
      "sha256": "4cb8f03dc7559ec6acf4918a636a64edab0f7ef83787eb927bd400a4759b52bb",
      "bytes": 168793
    },
    {
      "name": "Session Log 20260706.md",
      "sha256": "fe7133ac227bf9df5344bc67a20dd25cdfffcd55a6a26a6f107492cc3fb1364d",
      "bytes": 34392
    },
    {
      "name": "Session Log 20260707.md",
      "sha256": "fda539ed589187497832a341f061844058baf6aedff06d4e19416f1a03aa0752",
      "bytes": 30371
    },
    {
      "name": "Session Log 20260709.md",
      "sha256": "cc8b0c1e798b696acbdbe1f404f5091a7b40d2a6798006b683f2d0d08bfae636",
      "bytes": 44277
    },
    {
      "name": "Session Log 20260713.md",
      "sha256": "580dec1c79a70e325eaa5be0dce29d8a4fa33a7c9f7ae3f5ef20cab0a903d83a",
      "bytes": 108178
    },
    {
      "name": "Session Log 20260715.md",
      "sha256": "72f9b6e349a64f172090254ceb06cc62b07865703bd957ffb59c153620f6a217",
      "bytes": 17720
    },
    {
      "name": "Session Log 20260716.md",
      "sha256": "2e8818d20dd2be01754f50be066530f4f34d1fa7ba785d7207de8934e43b17c4",
      "bytes": 65224
    },
    {
      "name": "Session Log 20260717.md",
      "sha256": "6485f67d6a59566a7b6a23db4264966a3992f87013fed995bc4d931b1ef21fdf",
      "bytes": 22214
    },
    {
      "name": "Session Log 20260719.md",
      "sha256": "a51d4d0368ecd6212ffab90a1f6d255f6aa767693e3876d41c5108a2fc6e018a",
      "bytes": 124836
    },
    {
      "name": "Session Log 20260720.md",
      "sha256": "ce15320d1fec3cbd44a0b214667b300c9b7b06201efa92a6d3864c3f654b69f2",
      "bytes": 46315
    },
    {
      "name": "Session Log 20260721.md",
      "sha256": "28bf6617949f1b4e8b431d04494095827eec7d4fb852029c2e6617a32d17604a",
      "bytes": 14819
    },
    {
      "name": "Session Log 20260724.md",
      "sha256": "5a8495d7e43b93359f9b6222f3c11c3d5a0a69ae20a861f8b1f90b522500623f",
      "bytes": 107767
    },
    {
      "name": "Session Log 20260725.md",
      "sha256": "46c63b84ee2bafe9475c1db16bd39eda89fc5ee8b13dd691ec7a47e1d2bb5bbb",
      "bytes": 83754
    },
    {
      "name": "Session Log 20260728.md",
      "sha256": "967374469bf0a9652d8022ab78b1f5ddae7aba7d30e2f1b3dc0ea90656eaf126",
      "bytes": 61501
    },
    {
      "name": "Session Log 20260729.md",
      "sha256": "94b0bee87903daaf834a8f494d16b5c3a07daf4156749db3d012932e89198fe1",
      "bytes": 14750
    },
    {
      "name": "Session Log 20260730.md",
      "sha256": "327e0e17118378cbfc208108026ce249c18286a29030cb4984a923feec9a24b2",
      "bytes": 651604
    },
    {
      "name": "Session Log 20260802.md",
      "sha256": "b649be827471b84c1ed4049f25e0dc32b188b13a688d5160299018f67924b356",
      "bytes": 354780
    },
    {
      "name": "Session Log 20260803.md",
      "sha256": "2b71ebd439c538ad6c9b69dfd5753ba33309e0666bdfbb48b5855def55072b36",
      "bytes": 253493
    },
    {
      "name": "Session Log 20260804.md",
      "sha256": "1064cf64f76bc9ee23542e7623e5f398c8e83f1523fc5abdc51217391cfc08e4",
      "bytes": 89460
    },
    {
      "name": "Session Log 20260805.md",
      "sha256": "55682891dae985f09ed275c615c2e7ec3985f35dd33e0e0d9e8048fb44140c8d",
      "bytes": 102527
    },
    {
      "name": "Session Log 20260806.md",
      "sha256": "aa8c9d46e0a837e9966491d57c822914012f7f81e8c66e81f685279b3651b891",
      "bytes": 940891
    },
    {
      "name": "Session Log 20260807.md",
      "sha256": "eee05e2e316fe7d51652b91b758c91cb584623c12979ab37a354088a950b4823",
      "bytes": 23372
    },
    {
      "name": "Session Log 20260808.md",
      "sha256": "8869fa7f7f8bb3fbfdc7cdff968f3b0963b1abc076a7955b33d232d07521ff33",
      "bytes": 274349
    },
    {
      "name": "Session Log 20260809.md",
      "sha256": "3306753b4a091ca019a18850a5469bcacff30daea087522e1b144a5268107e45",
      "bytes": 21314
    },
    {
      "name": "Session Log 20260810.md",
      "sha256": "5062a6575ccc4ad6f54bc8f688627d5179a50abb58b499d20e81397c6505ccce",
      "bytes": 123338
    },
    {
      "name": "Session Log 20260811.md",
      "sha256": "a95858a0e1e049eb3ec9605e55238b8c646fea79923f4f9fac56290888357ada",
      "bytes": 148353
    },
    {
      "name": "Session Log 20260812.md",
      "sha256": "2385c317fdc8262186232571e2b503c13db5320146547634fa2d5572e8f1e626",
      "bytes": 99219
    },
    {
      "name": "Session Log 20260813.md",
      "sha256": "8391c5b917064ccb15a764ebed9ed57c1c170d459185c6c8ab27e439a9272eae",
      "bytes": 100537
    },
    {
      "name": "Session Log 20260814.md",
      "sha256": "a46c376f5a85b2d013e22df8943057dd076193317e17657d56b5297c61a2ef9d",
      "bytes": 25845
    },
    {
      "name": "Session Log 20260815.md",
      "sha256": "738ecc46a4b890b65b33b83234094f723ba0e6d0873a24e62e0338383ebb3e6c",
      "bytes": 6382
    },
    {
      "name": "Session Log 20260817.md",
      "sha256": "a0c976715c09c930d157083f28b9e6e530dc142a0d5164a804747384d4a92df8",
      "bytes": 35195
    },
    {
      "name": "Session Log 20260818.md",
      "sha256": "059a8a1d6ac2eea1fade243796aada1281bf3bfc21ed9b2ba3b0ad2863bb602e",
      "bytes": 2768
    },
    {
      "name": "Session Log 20260819.md",
      "sha256": "01727f99ac37b07b117367ae0c9c90177923ae8d7e56b8ac1e7860dfbc894327",
      "bytes": 41500
    },
    {
      "name": "Session Log 20260821.md",
      "sha256": "fc36d8b05f35c12e94fc911fa68c6def009b8ee2fe90293e325c9f9b6033c3e6",
      "bytes": 39416
    },
    {
      "name": "Session Log 20260822.md",
      "sha256": "7e51f8d30373b59f3f762175794a0a42938cfa9da84797cbf92fdae77bdd21ee",
      "bytes": 6107
    },
    {
      "name": "Session Log 20260826.md",
      "sha256": "12904ab3d7b284f69a9159d27702292eb41e18cf9ce9f31b74e376024ee43340",
      "bytes": 16083
    },
    {
      "name": "Session Log 20260827.md",
      "sha256": "c9dbbd6f9a0cd454e988ebb461c5f225a031e5453966698302915275a0889a07",
      "bytes": 6384
    },
    {
      "name": "Verbatim Chat Session Claude Code Desktop 20260317.md",
      "sha256": "c9959fd4bb95991646f8f349daad9aaf5e36a1cb42c4619fa526a4223ad0aa71",
      "bytes": 72351
    },
    {
      "name": "dockercompselogs.txt",
      "sha256": "060e4d3479c755697c5c3194c6851c80ab1317e6790cdedd9322588417af2724",
      "bytes": 1583
    }
  ]
}
```
