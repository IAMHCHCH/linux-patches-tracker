# Linux Crypto 子系统 Patch 追踪报告

---

## 报告信息

| 项目 | 内容 |
|------|------|
| 数据来源 | patchwork.kernel.org |
| 生成日期 | 2026-09-08 |
| 报告区间 | 2026-07-01 至 2026-08-31 |
| 仓库 | [https://github.com/IAMHCHCH/linux-patches-tracker](https://github.com/IAMHCHCH/linux-patches-tracker) |

---

## 统计概览

### 按状态分类

| 状态 | 数量 | 占比 |
|------|------|------|
| 社区讨论中 | 58 | 56.3% |
| 已合入 | 37 | 35.9% |
| **总计** | **103** | **100%** |

### 按组织分类（TOP 15）

| 组织 | 数量 | 占比 |
|------|------|------|
| Individual Contributor | 57 | 55.3% |
| Linux Community | 11 | 10.7% |
| Kernel.org | 11 | 10.7% |
| Red Hat | 8 | 7.8% |
| Canonical | 4 | 3.9% |
| Bootlin | 2 | 1.9% |
| Huawei | 2 | 1.9% |
| Intel | 2 | 1.9% |
| Qualcomm | 2 | 1.9% |
| Vayavya Labs | 1 | 1.0% |
| AMD | 1 | 1.0% |
| Oracle | 1 | 1.0% |
| SUSE | 1 | 1.0% |

### 按子系统分类

| 子系统 | 数量 | 占比 |
|--------|------|------|
| General Crypto | 63 | 61.2% |
| Public Key | 7 | 6.8% |
| AF_ALG API | 4 | 3.9% |
| HWRNG | 4 | 3.9% |
| Asymmetric Keys | 4 | 3.9% |
| Talitos | 3 | 2.9% |
| CAAM (NXP) | 3 | 2.9% |
| Aead | 3 | 2.9% |
| ECC | 2 | 1.9% |
| CESA (Marvell) | 2 | 1.9% |
| Kerberos | 2 | 1.9% |
| SPAcc | 1 | 1.0% |
| ICE (Qualcomm) | 1 | 1.0% |
| Ahash | 1 | 1.0% |
| Authenc | 1 | 1.0% |
| Skcipher | 1 | 1.0% |
| QCE (Qualcomm) | 1 | 1.0% |

## 重点 Patch Top20 清单

### 已合入

| 厂商 | 简介 |
|------|------|
| Red Hat | [PATCH v5 00/10] crypto: Provide a function for zeroizing crypto_aes_ctx ------该补丁集新增专用的零化函数，用于安全清除crypto_aes_ctx中的AES密钥，并替换aspeed、padlock、sa2ul及ARM/arm64 AES-NEON等驱动的清理逻辑，同时利用编译器清理属性简化qat、safexcel和eip93的密钥检查与释放，避免敏感数据残留。 |
| Intel | [PATCH v2 00/5] crypto: iaa - Fixes for multi entry SG lists ------该补丁系列修复了IAA驱动处理多entry散列表中解压失败、字节统计错误及DMA地址映射未释放的问题，通过改用软硬件回退和bounce buffer机制，确保多SG场景下压缩解压操作的正确性与稳定性。 |
| Canonical | [PATCH v2 00/2] crypto: asymmetric_keys - fix OOB read in pefile_parse_binary ------此补丁系列修复了内核非对称密钥解析器中 pefile_parse_binary 函数存在的越界读取漏洞，并新增了相应的 KUnit 测试用例以验证解析逻辑的正确性，从而提升安全性和测试覆盖率。 |
| Kernel.org | [PATCH v1 00/3] crypto: af_alg_restrict cleanups ------此补丁系列清理af_alg_restrict机制，将cbc(paes)算法改为仅特权可用，用标志位替代布尔变量，并在允许列表匹配后提前终止查找。 |
| Linux Community | [PATCH v1 00/4] crypto: atmel-tdes - simplify fast path in crypt_start ------该补丁集简化了Atmel TDES加密驱动中crypt_start的快速路径，并重构缓冲区分配、清理冗余返回变量和条件检查，提升代码清晰度与可维护性。 |
| Individual Contributor | [PATCH v1 00/2] crypto: keembay - use crypto_memneq() to compare GCM AEAD tags ------该补丁集将 keembay 加密驱动的 GCM 与 CCM AEAD 标签比较全部改为使用常数时间的 crypto_memneq()，取代易泄露的常规比较操作，以消除因标签校验时序差异引发的侧信道风险。 |
| Linux Community | [PATCH v1 00/2] crypto: qce - simplify devm_qce_register_algs ------该补丁系列简化了高通加密引擎（qce）中请求处理与算法注册流程，通过重构相关函数降低冗余逻辑，使设备管理代码更清晰，提升可维护性而无功能变化。 |
| Linux Community | [PATCH v1 00/2] crypto: atmel-ecc - simplify control flow in atmel_ecdh_set_secret ------此补丁系列精简了 Atmel ECC 密码驱动中 atmel_ecdh_set_secret 函数流程，通过去除冗余返回变量并简化条件分支，使密钥设置路径更清晰易读，同时保持原有行为与功能不变。 |
| Linux Community | [PATCH] crypto: octeontx - simplify get_{eng,ucode}_type_str helpers ------该补丁将octeontx加密驱动中两个类型转字符串的辅助函数改为switch直接返回，移除临时变量并显式添加default分支，简化代码逻辑且行为不变。 |
| Kernel.org | [PATCH] crypto: af_alg - Allow additional ciphers for cryptsetup ------此补丁在加密接口的允许列表中新增xts(camellia)、xts(serpent)和xts(twofish)三项，使cryptsetup能够使用这些额外的XTS模式密码算法，扩大了磁盘加密支持的密码范围。 |
| Bootlin | [v5] hwrng: core - Stop/start hwrng_fillfn() kthread before/after suspend-resume ------该补丁在硬件随机数核心中注册电源管理通知器，使系统挂起或休眠前停止hwrng_fillfn填充线程，并在恢复后重新启动，避免休眠期间该内核线程干扰电源状态转换。 |
| Bootlin | [v2,2/2] hwrng: omap: Enable on Renesas RZ/N1D ------该补丁在OMAP硬件随机数生成器驱动的Kconfig依赖中新增ARCH_RZN1，使其能够编译并支持瑞萨RZ/N1D平台。 |
| Linux Community | [PATCH] crypto: qce - simplify control flow in register functions ------本补丁将高通加密引擎驱动中AEAD、AHASH和SKCIPHER三个注册函数原有的goto错误标签流程，改为在循环内出错时直接调用对应注销函数并返回错误码，从而简化控制流并减少冗余代码。 |
| Individual Contributor | [PATCH] crypto: octeontx2 - use crypto_memneq() to check HMAC for cipher_null authenc ------该补丁针对Marvell OcteonTX2驱动中cipher_null authenc的HMAC完整性检查，以crypto_memneq()常量时间比较替换memcmp()，避免时序侧信道泄露，提升密码学安全性。 |
| Individual Contributor | [PATCH] crypto: octeontx - use crypto_memneq() to check HMAC ------该补丁将Marvell OcteonTX驱动中HMAC验证的普通memcmp比较替换为恒定时间的crypto_memneq，以避免时序侧信道泄露。 |
| Individual Contributor | [PATCH] crypto: ccree - use crypto_memneq() to compare AEAD tag ------该补丁将ccree驱动AEAD解密完成路径中的认证标签比对从memcmp改为crypto_memneq，避免时序侧信道泄露，提升MAC比较的安全性。 |
| Individual Contributor | [PATCH] crypto: amcc: pass core_dev to request_irq ------该补丁将中断请求与释放的上下文参数由设备指针改为core_dev结构体，使中断处理函数无需再通过dev_get_drvdata间接获取驱动数据，简化和修正了AMCC加密驱动的中断传参。 |
| Individual Contributor | [PATCH] crypto: s5p-sss: pass s5p_aes_dev to irq handler ------此补丁将中断处理函数的设备标识从platform_device改为s5p_aes_dev，直接传递驱动私有数据，避免在中断处理中重复获取设备驱动数据，简化了处理流程并降低间接访问开销。 |
| Individual Contributor | [PATCH] crypto: rockchip: pass crypto_info to irq handler ------此补丁让rockchip加密驱动在注册中断时将crypto_info作为设备标识传入，中断处理函数直接使用该指针，省去调用platform_get_drvdata转换，简化了回调节流并确保数据正确。 |
| Individual Contributor | [PATCH] crypto: sa2ul - use crypto_memneq() to compare AEAD tag ------sa2ul加密驱动将AEAD认证标签的比较由memcmp改为crypto_memneq，采用恒定时间比较防止时序侧信道攻击，提升安全性。 |

### 社区讨论

| 厂商 | 简介 |
|------|------|
| Individual Contributor | [PATCH v4 00/19] crypto: cmh - add Rambus CryptoManager Hub driver ------该补丁系列为Linux内核新增Rambus CryptoManager Hub平台驱动，将硬件纳入内核加密框架，涵盖对称/非对称、哈希、签名及密钥管理等多类算法支持。 |
| Qualcomm | [PATCH v24 00/14] crypto/dmaengine: qce: introduce BAM locking and use DMA for register I/O ------此补丁系列为高通 qce 加密引擎驱动引入 BAM DMA 支持，将寄存器读写操作改用 DMA 传输，并添加 BAM 锁机制以解决并发访问与设备分离问题。 |
| Kernel.org | [PATCH v2 00/13] Library APIs for AES encryption modes ------为内核提供通用的AES加密库API，新增ECB、CBC、CTS、CTR、XCTR、XTS、GCM、CCM等模式实现，并将现有加密算法层改为复用该库，减少重复代码并统一底层逻辑。 |
| Individual Contributor | [PATCH v2 00/7] Fix several issues in DTHEv2 driver ------该补丁集修复TI DTHEv2加密驱动中多个缺陷，涵盖AES散列表长度修正、设备移除时的use-after-free、高内存页潜在内存损坏、死锁及sg_nents_for_len返回值验证等问题，提升驱动稳定性与安全性。 |
| Qualcomm | [PATCH v6 00/8] crypto: qce - Fix crypto self-test failures ------该补丁系列修复高通加密引擎驱动在自测试中的失败，针对空消息、部分块、分片载荷及弱密钥等硬件不支持场景，引入或修正回退机制并调整校验逻辑，确保算法行为正确。 |
| Individual Contributor | [PATCH v1 00/3] crypto: caam: Fix DMA mapping leak in the cbc(paes) job path ------该补丁系列通过将受保护密钥的DMA映射改为每个tfm仅映射一次，并在setkey阶段校验密钥头，修复了cbc(paes)作业路径中因重复映射导致的DMA映射泄漏问题。 |
| Red Hat | [PATCH v1 00/11] libcrypto: Provide more __cleanup functions for zeroizing data ------本补丁系列为libcrypto中AES、MD5、SHA1和SHA2等算法新增密钥零化清理包装函数，以替代memzero_explicit直接调用，确保对称密钥等敏感数据安全清除并防编译器优化，提升内存安全性。 |
| Individual Contributor | [PATCH v3 00/5] crypto: talitos - fix rename first/last to first_desc/last_desc ------该系列围绕 crypto: talitos - fix rename first/last to first_desc/last_desc，具体包括crypto: talitos - stop using crypto_ahash:  中init、talitos - fix SEC1 32k ahash request limitation、talitos - rename first/last to first_desc/last_desc。 |
| Individual Contributor | [PATCH v1 00/4] crypto: introduce generic dynamic software fallback and EIP93 support ------此补丁系列为加密子系统引入一套通用的动态软件回退机制，并新增对EIP93加密引擎的支持；通过迁移tcrypt中的周期基准辅助函数、实现统一的动态回退逻辑以及优化回退代理关闭时的开销，使得硬件驱动在算法不可用时可灵活切换到软件实现，从而提升兼容性与扩展性。 |
| Individual Contributor | [PATCH v2 00/5] crypto: eip93: fix request lifetime and completion handling ------该补丁集修复了eip93加密驱动中请求生命周期与完成处理的缺陷，通过守卫DMA清理、校验HMAC密钥、使用请求本地SA记录、调整结果描述符读取及处理请求ID耗尽，确保同步完成逻辑正确。 |
| Individual Contributor | [PATCH v7 00/2] Add support for hashing algorithms in TI DTHE V2 ------本补丁系列为TI DTHE V2加密驱动新增SHA-224/256/384/512算法及HMAC支持，扩展其哈希运算能力，使驱动能够处理标准SHA与基于哈希的消息认证码操作。 |
| Red Hat | [PATCH v2 00/6] crypto: Add __cleanup functions for zeroizing aes_cmac_key & aes_cmac_ctx ------该补丁集通过新增封装函数并利用`__cleanup()`属性，使`aes_cmac_key`与`aes_cmac_ctx`在作用域结束时自动清零，替换原手动`memzero_explicit()`调用，降低密钥残留泄露风险，增强内核加密安全性。 |
| Individual Contributor | [PATCH v1 00/5] lib/crypto: add HKDF and convert fscrypt and NVMe ------本补丁系列在 lib/crypto 中新增 HKDF-SHA256/384/512 实现及 KUnit 测试，并将 fscrypt 和 NVMe 的密钥派生逻辑迁移至该通用接口，以统一和复用内核密钥派生功能。 |
| Individual Contributor | [PATCH v1 00/2] crypto: rsassa-pkcs1: fix undersized key handling ------该补丁系列修复RSA-PKCS1算法对过小密钥处理不当的问题，在签名和验签流程中增加显式拒绝逻辑，避免因密钥尺寸不足导致的安全或错误行为。 |
| Kernel.org | [PATCH v2 00/5] lib/crypto: KUnit tests for AES-CCM and AES-GCM ------为 lib/crypto 新增基于 KUnit 的 AES-CCM 与 AES-GCM 测试套件，通过创建通用 aead 测试模板及测试工具，并调整哈希测试缓冲区管理，以系统验证加解密正确性。 |
| Individual Contributor | [PATCH v1 00/3] Add X.509 CRL support ------为X.509新增证书吊销列表（CRL）解析及签名验证能力，并支持间接CRL，以完善证书有效性检查机制。 |
| Individual Contributor | [PATCH v1 00/2] crypto: amlogic: Fix IRQ handler return value and fallthrough logic ------该补丁集修复了amlogic加密驱动中断处理返回值和switch语句中错误穿透逻辑的问题，并改用devm API统一管理时钟与引擎资源，简化了错误处理与释放流程。 |
| Kernel.org | [PATCH v1 00/2] More padata cleanups ------该补丁集清理padata机制，释放不再需要的padata_works工作项，并将相关剩余代码和数据标记为__init及__initdata，以优化内存占用并完善初始化阶段管理。 |
| Kernel.org | [PATCH v1 00/3] lib/crypto: FIPS self-tests for AES encryption modes ------该补丁系列把fips.h拆分为AES与SHA专用头文件，并为AES未认证模式及GCM、CCM添加FIPS自检，以验证加密实现合规性。 |
| Individual Contributor | [PATCH v1 00/2] crypto: img-hash: clean up probe ------该补丁集清理img-hash驱动的probe流程：将资源获取移入局部变量，并修复中断拆除顺序及提前获取时钟，以提高初始化与卸载的稳定性。 |

---

## 已合入 Patches

### ◆ 子系统：General Crypto（20 patches）

**▸ 组织：Individual Contributor**（12 patches）

**crypto: octeontx - use crypto_memneq() to check HMAC**

- 日期：2026-08-15
- 状态：已合入
- 概括：该补丁将Marvell OcteonTX驱动中HMAC验证的普通memcmp比较替换为恒定时间的crypto_memneq，以避免时序侧信道泄露。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/aoCdOiyhQZZsFm5S@david.gall/

**crypto: amcc: pass core_dev to request_irq**

- 日期：2026-08-12
- 状态：已合入
- 概括：该补丁将中断请求与释放的上下文参数由设备指针改为core_dev结构体，使中断处理函数无需再通过dev_get_drvdata间接获取驱动数据，简化和修正了AMCC加密驱动的中断传参。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260812191555.93423-1-rosenp@gmail.com/

**crypto: s5p-sss: pass s5p_aes_dev to irq handler**

- 日期：2026-08-11
- 状态：已合入
- 概括：此补丁将中断处理函数的设备标识从platform_device改为s5p_aes_dev，直接传递驱动私有数据，避免在中断处理中重复获取设备驱动数据，简化了处理流程并降低间接访问开销。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260811043358.136042-1-rosenp@gmail.com/

**crypto: rockchip: pass crypto_info to irq handler**

- 日期：2026-08-11
- 状态：已合入
- 概括：此补丁让rockchip加密驱动在注册中断时将crypto_info作为设备标识传入，中断处理函数直接使用该指针，省去调用platform_get_drvdata转换，简化了回调节流并确保数据正确。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260811044916.160856-1-rosenp@gmail.com/

**crypto: eip93 - use struct_size() and flexible array for ring allocation**

- 日期：2026-08-03
- 状态：已合入
- 概括：该补丁将 eip93_device 的 ring 指针改为柔性数组，并改用 struct_size 一次分配设备与环形队列，移除独立的 kcalloc 调用，简化内存管理。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260803224028.87631-1-rosenp@gmail.com/

**crypto: ccp - don't abuse kernel-doc comment format**

- 日期：2026-07-30
- 状态：已合入
- 概括：该补丁将AMD SFS用户接口头文件中的文档注释格式从内核文档专用的`/**`改为普通注释`/*`，避免滥用内核文档标记，涉及crypto/ccp驱动，仅修正注释格式，不影响代码逻辑。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260730051710.1412969-1-rdunlap@infradead.org/

**crypto: ccm - Set rfc4309 maxauthsize from child**

- 日期：2026-07-20
- 状态：已合入
- 概括：将 rfc4309 实例的 maxauthsize 由固定值 16 改为继承子算法的最大认证大小，使 CCM 模板能适配不同子算法的认证需求。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/al17HaL8wNd_fuDc@gondor.apana.org.au/

**crypto: hisilicon/sec: use devm_platform_ioremap_resource in sec_map_io**

- 日期：2026-07-15
- 状态：已合入
- 概括：该补丁将希微SEC驱动中手动获取平台资源并映射的代码替换为devm_platform_ioremap_resource辅助函数，简化错误处理并自动进行资源管理。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260715011533.1278258-1-rosenp@gmail.com/

**crypto: omap-aes: use devm_platform_get_and_ioremap_resource**

- 日期：2026-07-15
- 状态：已合入
- 概括：该patch重构OMAP AES驱动，用devm_platform_get_and_ioremap_resource统一获取并映射I/O资源，删除自定义DT与非DT分支，改用device_get_match_data获取平台数据，简化probe并移除冗余头文件，减少重复代码与错误处理路径。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260715215848.410011-1-rosenp@gmail.com/

**crypto: omap-sham: use devm_platform_get_and_ioremap_resource**

- 日期：2026-07-15
- 状态：已合入
- 概括：该补丁重构OMAP SHA驱动，用devm_platform_get_and_ioremap_resource统一获取I/O内存与中断资源，删除设备树专用解析函数及多余头文件，通过device_get_match_data确定平台数据，简化了探测流程。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260715220013.416122-1-rosenp@gmail.com/

**crypto: keembay - Initialize completion before requesting IRQ**

- 日期：2026-07-14
- 状态：已合入
- 概括：该补丁将keembay OCS AES驱动的完成量初始化提前到注册中断之前，避免中断处理程序访问未初始化的完成量，防止驱动探测时因竞态条件引发崩溃。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260714033015.367735-1-lilinmao@kylinos.cn/

**crypto: keembay - publish OF module alias for OCS AES/SM4**

- 日期：2026-07-14
- 状态：已合入
- 概括：为英特尔 Keem Bay OCS AES/SM4 加密驱动补充设备树匹配表的模块别名声明，使内核能依据设备树节点信息自动加载该驱动模块。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260714131442.153699-1-pengcan@kylinos.cn/

**▸ 组织：Linux Community**（6 patches）

**crypto: qce - simplify control flow in register functions**

- 日期：2026-08-15
- 状态：已合入
- 概括：本补丁将高通加密引擎驱动中AEAD、AHASH和SKCIPHER三个注册函数原有的goto错误标签流程，改为在循环内出错时直接调用对应注销函数并返回错误码，从而简化控制流并减少冗余代码。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260815150946.12142-3-thorsten.blum@linux.dev/

**crypto: starfive - use scatterlist length before DMA mapping**

- 日期：2026-07-25
- 状态：已合入
- 概括：该补丁在starfive加密驱动的AEAD请求处理中，将清零缓冲区时使用的sg_dma_len改为scatterlist的length字段，确保在DMA映射前获取正确的原始长度，修复了依赖映射后长度可能导致的缓冲区处理错误。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260725090609.315812-2-thorsten.blum@linux.dev/

**crypto: octeontx - simplify get_{eng,ucode}_type_str helpers**

- 日期：2026-07-23
- 状态：已合入
- 概括：该补丁将octeontx加密驱动中两个类型转字符串的辅助函数改为switch直接返回，移除临时变量并显式添加default分支，简化代码逻辑且行为不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260723163326.163043-2-thorsten.blum@linux.dev/

**crypto: powerpc/aes - use bool for encryption/decryption flag**

- 日期：2026-07-11
- 状态：已合入
- 概括：该补丁将powerpc架构AES-CBC密码算法及公共头文件中的加密/解密标志参数由int改为bool类型，同时把调用处的1和0替换为true和false，以增强代码语义清晰性，不改变任何功能行为。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260711145216.747128-3-thorsten.blum@linux.dev/

**crypto: atmel-sha204a - clear RNG data from memory**

- 日期：2026-07-08
- 状态：已合入
- 概括：该补丁在 Atmel SHA204A 驱动中，通过 kfree_sensitive 释放工作数据与私钥缓存，并在随机数读取路径上使用 memzero_explicit 清零栈上命令缓冲区，避免 RNG 敏感数据残留内存。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260708150359.545852-2-thorsten.blum@linux.dev/

**[SERIES] crypto: atmel-tdes - simplify fast path in crypt_start** （cover letter，2/4 个 patch 达到代码量阈值）

- 日期：2026-07-06
- 状态：已合入
- 概括：该补丁集简化了Atmel TDES加密驱动中crypt_start的快速路径，并重构缓冲区分配、清理冗余返回变量和条件检查，提升代码清晰度与可维护性。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: atmel-tdes - simplify fast path in crypt_start
  - crypto: atmel-tdes - use __get_free_page in buff_init
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260706150404.382209-5-thorsten.blum@linux.dev/

**▸ 组织：Intel**（1 patches）

**[SERIES] crypto: iaa - Fixes for multi entry SG lists** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-08-05
- 状态：已合入
- 概括：该补丁系列修复了IAA驱动处理多entry散列表中解压失败、字节统计错误及DMA地址映射未释放的问题，通过改用软硬件回退和bounce buffer机制，确保多SG场景下压缩解压操作的正确性与稳定性。
- 达到阈值的 patches（4 个，显示前 5）：
  - crypto: iaa - avoid counting fallback decompression bytes
  - crypto: iaa - fall back to software for multi-entry scatterlists
  - crypto: iaa - use bounce buffer for multi-sg decompress input
  - crypto: iaa - unmap dst before software fallback on decompress
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260805-iaa-crypto-fixes-zswap-v2-3-55c02694f499@intel.com/

**▸ 组织：Red Hat**（1 patches）

**[SERIES] crypto: Provide a function for zeroizing crypto_aes_ctx** （cover letter，8/10 个 patch 达到代码量阈值）

- 日期：2026-08-10
- 状态：已合入
- 概括：该补丁集新增专用的零化函数，用于安全清除crypto_aes_ctx中的AES密钥，并替换aspeed、padlock、sa2ul及ARM/arm64 AES-NEON等驱动的清理逻辑，同时利用编译器清理属性简化qat、safexcel和eip93的密钥检查与释放，避免敏感数据残留。
- 达到阈值的 patches（8 个，显示前 5）：
  - crypto: aspeed - clear the crypto_aes_ctx when done
  - crypto: padlock-aes - clear the crypto_aes_ctx when done
  - crypto: sa2ul - clear the crypto_aes_ctx when done
  - crypto: arm/aes-neonbs - clear the crypto_aes_ctx when done
  - crypto: arm64/aes-neonbs - clear the crypto_aes_ctx when done
  - ... 及其他 3 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260810093009.608090-3-thuth@redhat.com/

---

### ◆ 子系统：AF_ALG API（3 patches）

**▸ 组织：Kernel.org**（2 patches）

**[SERIES] crypto: af_alg_restrict cleanups** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-08-02
- 状态：已合入
- 概括：此补丁系列清理af_alg_restrict机制，将cbc(paes)算法改为仅特权可用，用标志位替代布尔变量，并在允许列表匹配后提前终止查找。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: af_alg - Make cbc(paes) privileged-only
  - crypto: af_alg - Stop after finding name in allowlist
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260802230055.100746-2-ebiggers@kernel.org/

**crypto: af_alg - Allow additional ciphers for cryptsetup**

- 日期：2026-07-05
- 状态：已合入
- 概括：此补丁在加密接口的允许列表中新增xts(camellia)、xts(serpent)和xts(twofish)三项，使cryptsetup能够使用这些额外的XTS模式密码算法，扩大了磁盘加密支持的密码范围。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260705184419.40762-1-ebiggers@kernel.org/

**▸ 组织：Individual Contributor**（1 patches）

**crypto: af_alg: Allow cbc(paes)**

- 日期：2026-07-26
- 状态：已合入
- 概括：该补丁在AF_ALG算法绑定中为cbc(paes)特殊处理，将掩码清零以绕过原有内核加密API限制，从而允许该算法经AF_ALG套接字接口被正常分配与使用。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260726192716.2351505-1-richard@nod.at/

---

### ◆ 子系统：Aead（3 patches）

**▸ 组织：Individual Contributor**（3 patches）

**crypto: ccree - use crypto_memneq() to compare AEAD tag**

- 日期：2026-08-15
- 状态：已合入
- 概括：该补丁将ccree驱动AEAD解密完成路径中的认证标签比对从memcmp改为crypto_memneq，避免时序侧信道泄露，提升MAC比较的安全性。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/aoCdZiqJjb5XDHHz@david.gall/

**crypto: sa2ul - use crypto_memneq() to compare AEAD tag**

- 日期：2026-08-07
- 状态：已合入
- 概括：sa2ul加密驱动将AEAD认证标签的比较由memcmp改为crypto_memneq，采用恒定时间比较防止时序侧信道攻击，提升安全性。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/anX9UKJ66Aak4ICV@fudgebox/

**[SERIES] crypto: keembay - use crypto_memneq() to compare GCM AEAD tags** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-07
- 状态：已合入
- 概括：该补丁集将 keembay 加密驱动的 GCM 与 CCM AEAD 标签比较全部改为使用常数时间的 crypto_memneq()，取代易泄露的常规比较操作，以消除因标签校验时序差异引发的侧信道风险。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: keembay - use crypto_memneq() to compare GCM AEAD tags
  - crypto: keembay - use crypto_memneq() to compare CCM AEAD tags
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/anYEQOzunX0Lm3N1@david.gall/

---

### ◆ 子系统：HWRNG（2 patches）

**▸ 组织：Bootlin**（2 patches）

**[v5] hwrng: core - Stop/start hwrng_fillfn() kthread before/after suspend-resume**

- 日期：2026-08-04
- 状态：已合入
- 概括：该补丁在硬件随机数核心中注册电源管理通知器，使系统挂起或休眠前停止hwrng_fillfn填充线程，并在恢复后重新启动，避免休眠期间该内核线程干扰电源状态转换。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260804-hw-random-fix-hwrng-fillfn-crash-suspend-resume-v5-1-c4769b3c007b@bootlin.com/

**[v2,2/2] hwrng: omap: Enable on Renesas RZ/N1D**

- 日期：2026-07-10
- 状态：已合入
- 概括：该补丁在OMAP硬件随机数生成器驱动的Kconfig依赖中新增ARCH_RZN1，使其能够编译并支持瑞萨RZ/N1D平台。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260710-schneider-v7-2-rc1-eip76-upstream-v2-2-4eab557b0e70@bootlin.com/

---

### ◆ 子系统：ICE (Qualcomm)（1 patches）

**▸ 组织：Linux Community**（1 patches）

**crypto: qat - use strscpy_pad to simplify adf_service_string_to_mask**

- 日期：2026-07-05
- 状态：已合入
- 概括：该补丁在QAT驱动中用strscpy_pad替代手动长度检查与复制，简化服务字符串解析接口，移除冗余的len参数传递，并确保输入缓冲区正确填充。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260705133842.241401-3-thorsten.blum@linux.dev/

---

### ◆ 子系统：CESA (Marvell)（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: cesa: manage SRAM teardown with devm**

- 日期：2026-07-17
- 状态：已合入
- 概括：该补丁将 Marvell CESA 驱动的 SRAM 释放逻辑改用 devm 管理，移除手动清理路径，并在引擎中添加父设备回指以简化错误处理与移除流程。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260717231742.1174221-1-rosenp@gmail.com/

---

### ◆ 子系统：Ahash（1 patches）

**▸ 组织：Linux Community**（1 patches）

**crypto: bcm - use memcpy_and_pad in ahash_hmac_setkey**

- 日期：2026-07-20
- 状态：已合入
- 概括：该补丁在博通加密驱动的HMAC密钥设置函数中，以memcpy_and_pad替代原先的memcpy加memset组合，安全地将认证密钥复制并零填充至块大小，简化了填充逻辑并避免潜在的边界溢出风险。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260720232249.117992-3-thorsten.blum@linux.dev/

---

### ◆ 子系统：CAAM (NXP)（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: caam: simplify probe resource and IRQ handling**

- 日期：2026-07-30
- 状态：已合入
- 概括：本补丁简化了CAAM作业环的probe流程，改用devm_platform_ioremap_resource获取内存资源、platform_get_irq获取中断，由此移除手动map与dispose动作，代码更简洁且资源管理更规范。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260730204722.1101805-1-rosenp@gmail.com/

---

### ◆ 子系统：Kerberos（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto/krb5: use kfree_sensitive() for derived key buffers**

- 日期：2026-08-03
- 状态：已合入
- 概括：该补丁将Kerberos加密及校验准备函数中释放派生密钥缓冲区的kfree改为kfree_sensitive，确保密钥数据在释放前被清零，防止敏感信息残留在内核内存中。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260803192621.329577-1-linux@jaseg.de/

---

### ◆ 子系统：Authenc（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: octeontx2 - use crypto_memneq() to check HMAC for cipher_null authenc**

- 日期：2026-08-15
- 状态：已合入
- 概括：该补丁针对Marvell OcteonTX2驱动中cipher_null authenc的HMAC完整性检查，以crypto_memneq()常量时间比较替换memcmp()，避免时序侧信道泄露，提升密码学安全性。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/aoCdBZ-kLQ0rciFi@david.gall/

---

### ◆ 子系统：ECC（1 patches）

**▸ 组织：Linux Community**（1 patches）

**[SERIES] crypto: atmel-ecc - simplify control flow in atmel_ecdh_set_secret** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-07-28
- 状态：已合入
- 概括：此补丁系列精简了 Atmel ECC 密码驱动中 atmel_ecdh_set_secret 函数流程，通过去除冗余返回变量并简化条件分支，使密钥设置路径更清晰易读，同时保持原有行为与功能不变。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: atmel-ecc - simplify control flow in atmel_ecdh_set_secret
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260728205825.471233-3-thorsten.blum@linux.dev/

---

### ◆ 子系统：QCE (Qualcomm)（1 patches）

**▸ 组织：Linux Community**（1 patches）

**[SERIES] crypto: qce - simplify devm_qce_register_algs** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-07-31
- 状态：已合入
- 概括：该补丁系列简化了高通加密引擎（qce）中请求处理与算法注册流程，通过重构相关函数降低冗余逻辑，使设备管理代码更清晰，提升可维护性而无功能变化。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: qce - simplify qce_handle_request
  - crypto: qce - simplify devm_qce_register_algs
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260731102532.742739-4-thorsten.blum@linux.dev/

---

### ◆ 子系统：Asymmetric Keys（1 patches）

**▸ 组织：Canonical**（1 patches）

**[SERIES] crypto: asymmetric_keys - fix OOB read in pefile_parse_binary** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-08-15
- 状态：已合入
- 概括：此补丁系列修复了内核非对称密钥解析器中 pefile_parse_binary 函数存在的越界读取漏洞，并新增了相应的 KUnit 测试用例以验证解析逻辑的正确性，从而提升安全性和测试覆盖率。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: asymmetric_keys - add KUnit tests for the PE parser
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/fcbc6b4d5855ba42a0fccf335b2604ef0b36f092.1786802052.git.fabrice.derepas@canonical.com/

---

## 社区讨论中 Patches

### ◆ 子系统：General Crypto（40 patches）

**▸ 组织：Individual Contributor**（19 patches）

**[v2] crypto: ccp: Initialize DBC ioctl mutex before registering device**

- 日期：2026-08-30
- 状态：社区讨论中
- 概括：该补丁将DBC设备的ioctl互斥锁初始化提前到设备注册之前，避免注册后立即访问未初始化锁的竞态问题。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260830015104.2040153-1-runyu.xiao@seu.edu.cn/

**crypto: arm64/aes-neonbs: transition to kmalloc_obj()**

- 日期：2026-08-30
- 状态：社区讨论中
- 概括：该补丁将ARM64 AES-NEONBS加密驱动中的两次临时密钥上下文分配从kmalloc(sizeof(*rk), GFP_KERNEL)改为kmalloc_obj(*rk)，利用新接口自动推导对象类型与大小，提升代码安全性与可维护性。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260830101714.625728-3-manuelebnerli@mailbox.org/

**crypto: atmel-tdes - zero-initialize device state**

- 日期：2026-08-29
- 状态：社区讨论中
- 概括：该补丁将Atmel TDES驱动中设备状态的分配从devm_kmalloc改为devm_kzalloc，实现零初始化，避免使用未初始化的内存区域。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260829035821.67220-1-kmehltretter@gmail.com/

**[SERIES] Add support for hashing algorithms in TI DTHE V2** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-27
- 状态：社区讨论中
- 概括：本补丁系列为TI DTHE V2加密驱动新增SHA-224/256/384/512算法及HMAC支持，扩展其哈希运算能力，使驱动能够处理标准SHA与基于哈希的消息认证码操作。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: ti - Add support for SHA224/256/384/512 in DTHEv2 driver
  - crypto: ti - Add support for HMAC in DTHEv2 driver
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260827133542.619717-2-t-pratham@ti.com/

**[SERIES] Fix several issues in DTHEv2 driver** （cover letter，2/7 个 patch 达到代码量阈值）

- 日期：2026-08-27
- 状态：社区讨论中
- 概括：该补丁集修复TI DTHEv2加密驱动中多个缺陷，涵盖AES散列表长度修正、设备移除时的use-after-free、高内存页潜在内存损坏、死锁及sg_nents_for_len返回值验证等问题，提升驱动稳定性与安全性。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: ti - Trim scatterlists to correct length in AES
  - crypto: ti - Use list_first_entry_or_null() in dthe_get_dev()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260827132318.613876-5-t-pratham@ti.com/

**[SERIES] crypto: cmh - add Rambus CryptoManager Hub driver** （cover letter，14/15 个 patch 达到代码量阈值）

- 日期：2026-08-25
- 状态：社区讨论中
- 概括：该补丁系列为Linux内核新增Rambus CryptoManager Hub平台驱动，将硬件纳入内核加密框架，涵盖对称/非对称、哈希、签名及密钥管理等多类算法支持。
- 达到阈值的 patches（14 个，显示前 5）：
  - crypto: cmh - add HMAC ahash
  - crypto: cmh - add ML-KEM/ML-DSA (QSE)
  - crypto: cmh - add DRBG hwrng
  - crypto: cmh - add CSHAKE/KMAC ahash
  - crypto: cmh - add RSA akcipher
  - ... 及其他 9 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260825221539.255951-6-aousherovitch@rambus.com/

**[SERIES] Add X.509 CRL support** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-08-22
- 状态：社区讨论中
- 概括：为X.509新增证书吊销列表（CRL）解析及签名验证能力，并支持间接CRL，以完善证书有效性检查机制。
- 达到阈值的 patches（1 个，显示前 5）：
  - x509: add CRL parser with indirect CRL support
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260822082642.48936-3-tnovikov@astralinux.ru/

**[SERIES] crypto: amlogic: Fix IRQ handler return value and fallthrough logic** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-08-21
- 状态：社区讨论中
- 概括：该补丁集修复了amlogic加密驱动中断处理返回值和switch语句中错误穿透逻辑的问题，并改用devm API统一管理时钟与引擎资源，简化了错误处理与释放流程。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: amlogic: Use devm APIs for clock and engine management
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260821151243.8125-1-raizudeen.kerneldev@gmail.com/

**[RFC] crypto: qat - zero the VF migration state buffer on save**

- 日期：2026-08-17
- 状态：社区讨论中
- 概括：该补丁为Intel QAT驱动的VF迁移保存流程添加memset清零操作，在setup与状态保存阶段分别将状态缓冲区整体及未用区域清零，再初始化迁移状态管理器，避免残留数据写入
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260817042613.19855-1-kmehltretter@gmail.com/

**[v3,2/4] crypto: rockchip: Add RK356x/RK3588 cryptographic offloader driver**

- 日期：2026-08-16
- 状态：社区讨论中
- 概括：新增独立的 Rockchip RK356x/RK3588 加密卸载驱动，通过新 Kconfig 选项和 rk2_crypto 系列文件实现对称加密与哈希硬件加速，并支持运行时电源管理。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260816194112.552100-3-dawidro@gmail.com/

**crypto: amcc: trng: use devm_of_iomap()**

- 日期：2026-08-12
- 状态：社区讨论中
- 概括：该补丁将AMCC crypto4xx真随机数发生器的寄存器映射改为使用devm_of_iomap()，用设备资源管理替代手动of_iomap()和iounmap()，同时调整错误检查为IS_ERR并移除释放路径中的显式iounmap调用。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260812185747.79173-1-rosenp@gmail.com/

**[v2,12/13] crypto: api - wipe tfm contexts before kdump**

- 日期：2026-08-11
- 状态：社区讨论中
- 概括：本补丁为加密API引入tfm上下文跟踪列表，在kdump前通过崩溃通知器清零敏感密钥调度内存，并将释放路径改用kfree_sensitive以确保擦除。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260811-crash-zeroize-rework-v2-12-9561d13c2340@jaseg.de/

**[SERIES] crypto: img-hash: clean up probe** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-08-11
- 状态：社区讨论中
- 概括：该补丁集清理img-hash驱动的probe流程：将资源获取移入局部变量，并修复中断拆除顺序及提前获取时钟，以提高初始化与卸载的稳定性。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: img-hash: fetch resources into locals before probe body
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260811212030.20057-2-rosenp@gmail.com/

**crypto: amcc: get irq and ioremap resource first**

- 日期：2026-07-30
- 状态：社区讨论中
- 概括：该补丁将中断获取与IO内存映射提前到探测函数开头，避免后续初始化失败时资源遗漏，并复用映射结果修正错误路径。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260730204915.1102403-1-rosenp@gmail.com/

**[SERIES] crypto: introduce generic dynamic software fallback and EIP93 support** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-07-28
- 状态：社区讨论中
- 概括：此补丁系列为加密子系统引入一套通用的动态软件回退机制，并新增对EIP93加密引擎的支持；通过迁移tcrypt中的周期基准辅助函数、实现统一的动态回退逻辑以及优化回退代理关闭时的开销，使得硬件驱动在算法不可用时可灵活切换到软件实现，从而提升兼容性与扩展性。
- 达到阈值的 patches（4 个，显示前 5）：
  - crypto: move cycle benchmark helpers out of tcrypt
  - crypto: introduce dynamic software fallback
  - crypto: eip93 - add dynamic software fallback support
  - crypto: eliminate fallback proxy overhead while disabled
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/e0ce93088c1d9772e928fcbd113a446b7fb7442f.1785226804.git.hurryman2212@gmail.com/

**lib/crypto: x86/chacha: Add a 16-block AVX-512 variant**

- 日期：2026-07-22
- 状态：社区讨论中
- 概括：该补丁为内核ChaCha库新增x86 AVX-512 16块并行处理变体，利用512位zmm寄存器同时加密十六个数据块以提高吞吐量，并接入Makefile构建系统。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260722153247.630519-1-martin@strongswan.org/

**[SERIES] lib/crypto: add HKDF and convert fscrypt and NVMe** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-07-21
- 状态：社区讨论中
- 概括：本补丁系列在 lib/crypto 中新增 HKDF-SHA256/384/512 实现及 KUnit 测试，并将 fscrypt 和 NVMe 的密钥派生逻辑迁移至该通用接口，以统一和复用内核密钥派生功能。
- 达到阈值的 patches（2 个，显示前 5）：
  - lib/crypto: tests: add HKDF KUnit tests
  - lib/crypto: add HKDF-SHA{256,384,512}
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260721140644.780006-3-marco@mandelbit.com/

**crypto: verify_pefile - Use constant-time digest comparison**

- 日期：2026-07-20
- 状态：社区讨论中
- 概括：此补丁将PE文件签名验证中的摘要比较从memcmp改为恒定时间的crypto_memneq，以防止时序侧信道攻击，影响PE数字签名校验的安全性。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260720031815.204237-1-yijiangshan@kylinos.cn/

**[SERIES] crypto: eip93: fix request lifetime and completion handling** （cover letter，4/5 个 patch 达到代码量阈值）

- 日期：2026-07-07
- 状态：社区讨论中
- 概括：该补丁集修复了eip93加密驱动中请求生命周期与完成处理的缺陷，通过守卫DMA清理、校验HMAC密钥、使用请求本地SA记录、调整结果描述符读取及处理请求ID耗尽，确保同步完成逻辑正确。
- 达到阈值的 patches（4 个，显示前 5）：
  - crypto: eip93: reject HMAC requests before setkey
  - crypto: eip93: use request-local SA records for cipher requests
  - crypto: eip93: order result descriptor reads after PE_READY
  - crypto: eip93: handle request ID exhaustion
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260707171537.467608-2-hurryman2212@gmail.com/

**▸ 组织：Kernel.org**（7 patches）

**[SERIES] lib/crypto: KUnit tests for AES-CCM and AES-GCM** （cover letter，5/5 个 patch 达到代码量阈值）

- 日期：2026-08-02
- 状态：社区讨论中
- 概括：为 lib/crypto 新增基于 KUnit 的 AES-CCM 与 AES-GCM 测试套件，通过创建通用 aead 测试模板及测试工具，并调整哈希测试缓冲区管理，以系统验证加解密正确性。
- 达到阈值的 patches（5 个，显示前 5）：
  - lib/crypto: tests: Create test-utils.h
  - lib/crypto: tests: Use per-test-case buffers in hash tests
  - lib/crypto: tests: Add KUnit test suite for AES-CCM
  - lib/crypto: tests: Add KUnit test suite for AES-GCM
  - lib/crypto: tests: Add aead-test-template.h
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260802233005.161467-2-ebiggers@kernel.org/

**[SERIES] lib/crypto: FIPS self-tests for AES encryption modes** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-08-02
- 状态：社区讨论中
- 概括：该补丁系列把fips.h拆分为AES与SHA专用头文件，并为AES未认证模式及GCM、CCM添加FIPS自检，以验证加密实现合规性。
- 达到阈值的 patches（3 个，显示前 5）：
  - lib/crypto: fips: Split fips.h into fips-aes.h and fips-sha.h
  - lib/crypto: aes: Add FIPS self-tests for unauthenticated modes
  - lib/crypto: aes: Add FIPS self-tests for GCM and CCM
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260802222408.91757-2-ebiggers@kernel.org/

**crypto: qce - Replace with stub driver**

- 日期：2026-07-31
- 状态：社区讨论中
- 概括：该补丁将高通加密引擎驱动彻底简化为仅用于绑定设备树节点的存根驱动，删除所有加密算法及DMA实现，不再暴露任何密码学功能，目的是允许互联总线降频以节省功耗。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260731050838.158825-1-ebiggers@kernel.org/

**[SERIES] More padata cleanups** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-07-17
- 状态：社区讨论中
- 概括：该补丁集清理padata机制，释放不再需要的padata_works工作项，并将相关剩余代码和数据标记为__init及__initdata，以优化内存占用并完善初始化阶段管理。
- 达到阈值的 patches（2 个，显示前 5）：
  - padata: Free the padata_works when they're no longer needed
  - padata: Mark remaining code as __init and data as __initdata
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260717171831.27994-3-ebiggers@kernel.org/

**[SERIES] Library APIs for AES encryption modes** （cover letter，12/13 个 patch 达到代码量阈值）

- 日期：2026-07-15
- 状态：社区讨论中
- 概括：为内核提供通用的AES加密库API，新增ECB、CBC、CTS、CTR、XCTR、XTS、GCM、CCM等模式实现，并将现有加密算法层改为复用该库，减少重复代码并统一底层逻辑。
- 达到阈值的 patches（12 个，显示前 5）：
  - crypto: xts - Split out __xts_verify_key() helper
  - lib/crypto: aes: Add ECB support
  - lib/crypto: aes: Add CBC and CBC-CTS support
  - lib/crypto: aes: Add CTR and XCTR support
  - lib/crypto: aes: Add XTS support
  - ... 及其他 7 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260715221153.246410-2-ebiggers@kernel.org/

**[2/2] padata: Remove serialized job support**

- 日期：2026-07-13
- 状态：社区讨论中
- 概括：该补丁移除了padata机制中已无实际用户的串行化作业支持，仅保留多线程并行作业功能，同时大幅精简相关文档，使padata不再承担有序回调职责，内核并行任务处理流程更简化。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260713223234.24812-3-ebiggers@kernel.org/

**lib/crypto: docs: Improve introduction sentence**

- 日期：2026-07-09
- 状态：社区讨论中
- 概括：该补丁仅修订内核加密库文档的开篇介绍，明确其服务对象为内核内部用户，并强调相较传统加密API在访问速度与便捷性上的优势，无代码逻辑改动。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260709022747.44635-1-ebiggers@kernel.org/

**▸ 组织：Red Hat**（6 patches）

**[v3] crypto: inside-secure - Zeroize temporary arrays on stack with sensitive data**

- 日期：2026-08-19
- 状态：社区讨论中
- 概括：该补丁在inside-secure加密驱动的哈希密钥设置函数中，对含敏感中间密钥的栈上临时数组调用memzero_explicit主动清零，防止密钥材料残留内存，提升安全性。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260819151845.835768-1-thuth@redhat.com/

**lib/crypto: chacha20poly1305: Clear chacha_state in xchacha20poly1305_decrypt()**

- 日期：2026-08-13
- 状态：社区讨论中
- 概括：该补丁为解密函数中chacha_state添加自动清零清理机制，统一了普通与xchacha路径的状态擦除行为，以防止密钥材料泄漏残留。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260813130147.949545-1-thuth@redhat.com/

**[SERIES] libcrypto: Provide more __cleanup functions for zeroizing data** （cover letter，7/7 个 patch 达到代码量阈值）

- 日期：2026-08-13
- 状态：社区讨论中
- 概括：本补丁系列为libcrypto中AES、MD5、SHA1和SHA2等算法新增密钥零化清理包装函数，以替代memzero_explicit直接调用，确保对称密钥等敏感数据安全清除并防编译器优化，提升内存安全性。
- 达到阈值的 patches（7 个，显示前 5）：
  - lib/crypto: aes: Provide a wrapper function for zeroizing crypto_aes_ctx
  - lib/crypto: aes: Use aes_zeroize_*key() instead of memzero_explicit()
  - lib/crypto: aes: Provide functions for zeroizing aes_key and aes_enckey
  - lib/crypto: md5: Use hmac_md5_zeroize_ctx() instead of memzero_explicit()
  - lib/crypto: sha1: Provide a wrapper for zeroizing hmac_sha1_ctx
  - ... 及其他 2 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260813134953.979481-2-thuth@redhat.com/

**[SERIES] lib/crypto: Provide a function for zeroizing hmac_sha1_ctx** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-12
- 状态：社区讨论中
- 概括：为安全清除敏感密钥数据，新增hmac_sha1_ctx清零函数，并将其用于替换sha1中的memzero_explicit调用，统一了密钥上下文的零化处理方式。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: Provide a wrapper for zeroizing hmac_sha1_ctx
  - lib/crypto: sha1: Use hmac_sha1_zeroize_ctx() instead of memzero_explicit()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260812163336.3103835-2-thuth@redhat.com/

**[SERIES] crypto: Add __cleanup functions for zeroizing aes_cmac_key & aes_cmac_ctx** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-08-07
- 状态：社区讨论中
- 概括：该补丁集通过新增封装函数并利用`__cleanup()`属性，使`aes_cmac_key`与`aes_cmac_ctx`在作用域结束时自动清零，替换原手动`memzero_explicit()`调用，降低密钥残留泄露风险，增强内核加密安全性。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: Provide wrapper functions for zeroizing aes_cmac_key and aes_cmac_ctx
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260807125845.1477067-2-thuth@redhat.com/

**[RFC] crypto: pcrypt - Disallow nesting of the pcrypt wrapper**

- 日期：2026-07-01
- 状态：社区讨论中
- 概括：该补丁在 crypto/pcrypt 初始化时检查驱动名是否含“pcrypt”，若存在则返回 -ELOOP，从而禁止 pcrypt 包装器嵌套，避免递归包装导致的潜在问题。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260701143947.944593-1-thuth@redhat.com/

**▸ 组织：Huawei**（2 patches）

**crypto: hisilicon/zip - enable auto clock gating for DAE**

- 日期：2026-08-29
- 状态：社区讨论中
- 概括：该补丁为海思zip DAE硬件在QM硬件版本V5及以上新增自动时钟门控控制，在内存初始化前后关闭再开启，初始化失败时提前返回，以降低功耗并保证初始化过程正确。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260829094924.2191402-1-huangchenghai2@huawei.com/

**[v2] crypto: hisilicon/sec - remove SEC crypto block cipher accelerator**

- 日期：2026-08-19
- 状态：社区讨论中
- 概括：该补丁删除hisilicon SEC加密块密码加速器的设备树绑定及hip07.dtsi中对应中断控制器和加速器节点，移除该已不再维护的硬件加速支持。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260819075353.94500-1-huangchenghai2@huawei.com/

**▸ 组织：Qualcomm**（2 patches）

**[SERIES] crypto/dmaengine: qce: introduce BAM locking and use DMA for register I/O** （cover letter，7/8 个 patch 达到代码量阈值）

- 日期：2026-07-23
- 状态：社区讨论中
- 概括：此补丁系列为高通 qce 加密引擎驱动引入 BAM DMA 支持，将寄存器读写操作改用 DMA 传输，并添加 BAM 锁机制以解决并发访问与设备分离问题。
- 达到阈值的 patches（7 个，显示前 5）：
  - crypto: qce - Cancel work on device detach
  - crypto: qce - Include algapi.h in the core.h header
  - crypto: qce - Simplify arguments of devm_qce_dma_request()
  - crypto: qce - Use existing devres APIs in devm_qce_dma_request()
  - crypto: qce - Map crypto memory for DMA
  - ... 及其他 2 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260723-qcom-qce-cmd-descr-v24-7-4f87bb4d9938@oss.qualcomm.com/

**[SERIES] crypto: qce - Fix crypto self-test failures** （cover letter，5/8 个 patch 达到代码量阈值）

- 日期：2026-07-17
- 状态：社区讨论中
- 概括：该补丁系列修复高通加密引擎驱动在自测试中的失败，针对空消息、部分块、分片载荷及弱密钥等硬件不支持场景，引入或修正回退机制并调整校验逻辑，确保算法行为正确。
- 达到阈值的 patches（5 个，显示前 5）：
  - crypto: qce - Reject empty messages for AES-XTS
  - crypto: qce - Use a fallback for AES-CTR with a partial final block
  - crypto: qce - Use a fallback for CCM with a partial final block
  - crypto: qce - Use fallback for CCM with a fragmented payload
  - crypto: qce - Use fallback for fragmented skcipher payloads
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260717-qce-fix-self-tests-v6-1-455775fe5f6c@oss.qualcomm.com/

**▸ 组织：AMD**（1 patches）

**[3/3] crypto: xilinx: zynqmp-aes-gcm: Send firmware decoded code instead of EBADMSG**

- 日期：2026-07-06
- 状态：社区讨论中
- 概括：此补丁调整了 ZynqMP AES-GCM 驱动解密路径的错误处理，不再将固件返回的已解码错误码强制转换为 -EBADMSG，而是直接向上层传递固件错误码，以保留更精确的认证失败原因。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260706110254.2427551-4-h.jain@amd.com/

**▸ 组织：Oracle**（1 patches）

**padata: Replace bottom-half spinlock variants**

- 日期：2026-07-17
- 状态：社区讨论中
- 概括：padata 模块将静态池锁的 bottom-half 变体替换为普通自旋锁，移除了禁软中断语义，仅保留互斥保护，降低临界区开销并简化并发上下文。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260717205028.63847-1-daniel.m.jordan@oracle.com/

**▸ 组织：Intel**（1 patches）

**[1/2] crypto: qat - allow KPT disable when service is not asym**

- 日期：2026-08-31
- 状态：社区讨论中
- 概括：此改动使QAT设备在关闭KPT时不再强制要求已启用非对称加密服务，仅启用时才校验服务类型，从而允许在非asym配置下禁用KPT。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260831063355.668528-2-nitesh.venkatesh@intel.com/

**▸ 组织：Linux Community**（1 patches）

**[SERIES] crypto: zstd - avoid initializing the workspace twice** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-25
- 状态：社区讨论中
- 概括：该补丁系列针对zstd压缩/解压缩路径中工作区被重复初始化的问题，通过跳过已初始化cstream和dstream的重复设置，避免二次初始化开销，从而提升crypto zstd操作的效率。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: zstd - Avoid redundant cstream initialization
  - crypto: zstd - Avoid redundant dstream initialization
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260825220616.3842633-2-usama.arif@linux.dev/

---

### ◆ 子系统：Public Key（6 patches）

**▸ 组织：Individual Contributor**（6 patches）

**[SERIES] crypto: rsassa-pkcs1: fix undersized key handling** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-26
- 状态：社区讨论中
- 概括：该补丁系列修复RSA-PKCS1算法对过小密钥处理不当的问题，在签名和验签流程中增加显式拒绝逻辑，避免因密钥尺寸不足导致的安全或错误行为。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: rsassa-pkcs1: reject undersized keys when signing
  - crypto: rsassa-pkcs1: reject undersized keys when verifying
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260826103744.1554131-2-Jeremy.Jean@oss.cyber.gouv.fr/

**crypto: rsassa-pkcs1 - Use constant-time digest comparison**

- 日期：2026-07-20
- 状态：社区讨论中
- 概括：此 patch 将 RSA-PKCS1 签名验证中的摘要比较由 memcmp 改为 crypto_memneq，采用常数时间比较，避免因时序差异泄露信息，提升安全性。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260720021322.122784-1-yijiangshan@kylinos.cn/

**crypto: pkcs7 - Use constant-time message digest comparison**

- 日期：2026-07-20
- 状态：社区讨论中
- 概括：该补丁将PKCS7签名验证中的消息摘要比较从memcmp改为crypto_memneq，采用恒定时间比较，防止时序侧信道攻击，增强了签名验证过程的安全性。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260720032316.210113-1-yijiangshan@kylinos.cn/

**[6.1/6.6/6.12.y] crypto: rsa-pkcs1pad: Don't WARN on an empty digest**

- 日期：2026-07-20
- 状态：社区讨论中
- 概括：该补丁将RSA PKCS1Pad验证流程中对空摘要的内核警告移除，改为静默返回无效参数错误，避免合法输入触发不必要的告警日志。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260720191525.15450-1-doruk@0sec.ai/

**crypto: rsassa-pkcs1: use constant-time comparison for digest and signature verification**

- 日期：2026-07-10
- 状态：社区讨论中
- 概括：该补丁将RSA PKCS1签名验证中的摘要比对从memcmp改为常数时间比较函数crypto_memneq，以避免因时序侧信道泄露摘要信息，提升安全性。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/alEr_e-G0L2nxxv-@fudgebox/

**crypto: pkcs7_verify: use constant-time comparison for digest and signature verification**

- 日期：2026-07-10
- 状态：社区讨论中
- 概括：PKCS#7 签名验证将摘要比较从 memcmp 改为 crypto_memneq，以常量时间比对消息摘要和签名，消除时序侧信道泄露风险，提升内核密码学验证安全性。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/alEsSl8i1_FpoU0f@fudgebox/

---

### ◆ 子系统：CAAM (NXP)（2 patches）

**▸ 组织：Individual Contributor**（2 patches）

**crypto: caam - reject overlong RSA CRT parameters**

- 日期：2026-08-10
- 状态：社区讨论中
- 概括：该补丁为CAAM驱动RSA私钥解析增加CRT参数长度校验，拒绝超过对应素数长度的dP、dQ、qInv，并修复错误清理路径及返回错误码。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260810154024.3178145-1-Jeremy.Jean@oss.cyber.gouv.fr/

**[SERIES] crypto: caam: Fix DMA mapping leak in the cbc(paes) job path** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-07-26
- 状态：社区讨论中
- 概括：该补丁系列通过将受保护密钥的DMA映射改为每个tfm仅映射一次，并在setkey阶段校验密钥头，修复了cbc(paes)作业路径中因重复映射导致的DMA映射泄漏问题。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: caam: Map the paes protected key once per tfm
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260726081504.2182951-2-richard@nod.at/

---

### ◆ 子系统：Talitos（2 patches）

**▸ 组织：Individual Contributor**（2 patches）

**crypto: talitos: pass talitos_private to irq handlers**

- 日期：2026-08-11
- 状态：社区讨论中
- 概括：该补丁将泰利托斯加密驱动中断处理函数的参数从设备指针改为私有的 talitos_private 结构体，省去驱动数据查找，并相应调整中断注册时的数据传递。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260811043953.150589-1-rosenp@gmail.com/

**[SERIES] crypto: talitos - fix rename first/last to first_desc/last_desc** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-07-09
- 状态：社区讨论中
- 概括：该系列围绕 crypto: talitos - fix rename first/last to first_desc/last_desc，具体包括crypto: talitos - stop using crypto_ahash:  中init、talitos - fix SEC1 32k ahash request limitation、talitos - rename first/last to first_desc/last_desc。
- 达到阈值的 patches（3 个，显示前 5）：
  - crypto: talitos - stop using crypto_ahash::init
  - crypto: talitos - fix SEC1 32k ahash request limitation
  - crypto: talitos - rename first/last to first_desc/last_desc
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260709193956.15619-4-ggoerisch@gmail.com/

---

### ◆ 子系统：HWRNG（2 patches）

**▸ 组织：SUSE**（1 patches）

**[v2,07/13] hw_random/via-rng: Stop using 32-bit MSR interfaces**

- 日期：2026-08-19
- 状态：社区讨论中
- 概括：VIA 硬件随机数生成器驱动 via-rng 不再使用 32 位 MSR 读写接口，改为调用 64 位 rdmsrq/wrmsrq 并借助 struct msr 保存寄存器值，以正确适配新平台 MSR 访问方式。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260819102314.1499258-8-jgross@suse.com/

**▸ 组织：Individual Contributor**（1 patches）

**hwrng: imx-rngc: check clk_prepare_enable() return value**

- 日期：2026-08-28
- 状态：社区讨论中
- 概括：该补丁为i.MX随机数发生器（imx-rngc）驱动增加时钟使能失败检查，探测和恢复函数中若clk_prepare_enable失败则返回错误码并输出提示，避免静默忽略时钟故障。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260828025423.2149304-1-dayou5941@163.com/

---

### ◆ 子系统：AF_ALG API（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[5.10/5.15] crypto: af_alg - Set merge to zero early in af_alg_sendmsg**

- 日期：2026-07-01
- 状态：社区讨论中
- 概括：该补丁在af_alg_sendmsg循环内提前将ctx->merge置零，确保后续数据不因旧状态被错误合并，修复crypto接口发送时的内存或数据完整性风险。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260701160121.100720-1-mdmitrichenko@astralinux.ru/

---

### ◆ 子系统：ECC（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[RFC,RESEND,v6,1/1] crypto: atmel-ecc - fix multi-device use-after-free and registration races**

- 日期：2026-07-12
- 状态：社区讨论中
- 概括：该补丁通过引入全局互斥锁、引用计数和完成量同步机制，修复了Atmel ECC加密驱动在多设备并发探测与移除时的注册竞态及活跃TFM导致的释放后使用问题。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260712200203.47764-1-l.rubusch@gmail.com/

---

### ◆ 子系统：CESA (Marvell)（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: cesa: check for sram_dma NULL**

- 日期：2026-07-13
- 状态：社区讨论中
- 概括：该补丁在Marvell CESA加密引擎释放SRAM时增加sram_dma非空检查，防止dma_unmap_resource对空DMA地址调用，避免潜在空指针异常，提升驱动健壮性。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260713050740.3687230-1-rosenp@gmail.com/

---

### ◆ 子系统：Kerberos（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: krb5 - Use constant-time checksum comparison**

- 日期：2026-07-20
- 状态：社区讨论中
- 概括：将 Kerberos 5 校验和验证中的 memcmp 替换为 crypto_memneq 常数时间比较，避免因时序差异泄露校验和信息，提升加密认证流程的安全性。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260720031304.198172-1-yijiangshan@kylinos.cn/

---

### ◆ 子系统：Asymmetric Keys（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: asymmetric_keys: copy X.509 TBS for data signature algorithms**

- 日期：2026-08-21
- 状态：社区讨论中
- 概括：该补丁将X.509证书签名验证中直接引用TBS内存改为通过kmemdup拷贝，用于数据签名算法场景，避免后续操作引用失效内存，并在拷贝失败时返回ENOMEM。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260821192502.3942767-2-Jeremy.Jean@oss.cyber.gouv.fr/

---

### ◆ 子系统：Skcipher（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: mxs-dcp: handle zero-length skcipher requests**

- 日期：2026-08-28
- 状态：社区讨论中
- 概括：该补丁在mxs-dcp加密驱动中提前检测零长度skcipher请求并直接返回成功，避免处理空数据时触发后续错误路径。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260828093209.3179074-1-lilinmao@kylinos.cn/

---

---
## 子系统说明

- **AF_ALG API**：用户空间加密 API（algif_skcipher、algif_hash 等）
- **DRBG**：确定性随机比特生成器
- **HWRNG**：硬件随机数生成器驱动
- **ECC**：椭圆曲线密码学（ECDSA、ECRDSA）
- **QAT (Intel)**：Intel QuickAssist Technology 硬件加速器
- **CCP/SEV (AMD)**：AMD 安全协处理器 / 安全加密虚拟化
- **CAAM (NXP)**：NXP Cryptographic Acceleration and Assurance Module
- **Talitos**：NXP/Freescale Talitos 安全加速器
- **QCE (Qualcomm)**：Qualcomm Crypto Engine
- **ICE (Qualcomm)**：Qualcomm Inline Crypto Engine
- **SPAcc**：安全算法硬件加速器
- **CESA (Marvell)**：Marvell Cryptographic Engine and Security Accelerator
- **VirtIO Crypto**：VirtIO 虚拟化加密设备
- **Crypto Engine**：加密算法引擎框架
- **Kerberos**：Kerberos 5 加密支持
- **Asymmetric Keys**：非对称密钥管理
- **Public Key**：公钥加密（X.509、PKCS7）
- **Authenc**：认证加密
- **Shash**：同步哈希算法
- **Ahash**：异步哈希算法
- **Skcipher**：对称密钥加密
- **Aead**：关联数据认证加密
- **Test Manager**：加密算法测试管理器
- **TCrypt**：加密速度测试模块
- **JitterEntropy**：Jitter 熵源 RNG
- **General Crypto**：通用 crypto（不属于特定子模块）

---

## 项目说明

本项目用于追踪 Linux 内核 crypto（加密）子系统的 patch 提交情况。crypto 子系统涵盖硬件加密加速器驱动（QAT、CCP、CAAM、QCE 等）、加密算法实现（AES、SHA、ECC、SMx 等）、以及用户空间加密 API（AF_ALG）。

### 过滤规则

- **小修改自动过滤**：移除类 < 200 行、修复/新增类 < 100 行的 patch 不纳入报告
- **多版本去重**：同一 patch 的多个版本（v3、v4、v5 等）只保留最高版本
- **Cover Letter 合成**：多 patch 系列只要有任一 patch 达到代码量阈值，就用 cover letter 代表
- **组织归类**：按贡献者邮箱域名自动归类到对应企业，个人邮箱归为 Individual Contributor

### 报告生成命令

```bash
# 生成所有模块报告
python3 tracker.py --all

# 只生成特定模块
python3 tracker.py 子系统

# 指定日期范围
python3 tracker.py 子系统 --start 2026-03-01 --end 2026-04-30
```

---

*报告由 Linux Patches Tracker 自动生成 | 2026-09-08 16:14:11*
