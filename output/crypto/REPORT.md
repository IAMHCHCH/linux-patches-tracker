# Linux Crypto 子系统 Patch 追踪报告

---

## 报告信息

| 项目 | 内容 |
|------|------|
| 数据来源 | patchwork.kernel.org |
| 生成日期 | 2026-09-11 |
| 报告区间 | 2026-07-01 至 2026-08-31 |
| 仓库 | [https://github.com/IAMHCHCH/linux-patches-tracker](https://github.com/IAMHCHCH/linux-patches-tracker) |

---

## 统计概览

### 按状态分类

| 状态 | 数量 | 占比 |
|------|------|------|
| 社区讨论中 | 61 | 57.0% |
| 已合入 | 37 | 34.6% |
| **总计** | **107** | **100%** |

### 按组织分类（TOP 15）

| 组织 | 数量 | 占比 |
|------|------|------|
| Individual Contributor | 32 | 29.9% |
| Kernel.org | 12 | 11.2% |
| Linux Community | 11 | 10.3% |
| Red Hat | 8 | 7.5% |
| Kylin | 7 | 6.5% |
| Canonical | 4 | 3.7% |
| Bootlin | 3 | 2.8% |
| ANSSI | 3 | 2.8% |
| Vayavya Labs | 2 | 1.9% |
| Astra Linux | 2 | 1.9% |
| 归属待核实（nod.at） | 2 | 1.9% |
| 归属待核实（jaseg.de） | 2 | 1.9% |
| Huawei | 2 | 1.9% |
| Intel | 2 | 1.9% |
| Qualcomm | 2 | 1.9% |

### 按子系统分类

| 子系统 | 数量 | 占比 |
|--------|------|------|
| General Crypto | 64 | 59.8% |
| Public Key | 7 | 6.5% |
| HWRNG | 5 | 4.7% |
| AF_ALG API | 4 | 3.7% |
| Talitos | 4 | 3.7% |
| Asymmetric Keys | 4 | 3.7% |
| CAAM (NXP) | 3 | 2.8% |
| Aead | 3 | 2.8% |
| SPAcc | 2 | 1.9% |
| ECC | 2 | 1.9% |
| CESA (Marvell) | 2 | 1.9% |
| Kerberos | 2 | 1.9% |
| ICE (Qualcomm) | 1 | 0.9% |
| Ahash | 1 | 0.9% |
| Authenc | 1 | 0.9% |
| Skcipher | 1 | 0.9% |
| QCE (Qualcomm) | 1 | 0.9% |

## 重点 Patch Top20 清单

### 已合入

| 厂商 | 简介 |
|------|------|
| Red Hat | [PATCH v5 00/10] crypto: Provide a function for zeroizing crypto_aes_ctx ------为多个加密驱动引入自动清除 AES 上下文的作用域清理机制，在函数返回时擦除栈上的密钥材料，修复部分驱动遗漏清除或第二条密钥扩展失败时残留密钥的问题，并把仅用于校验密钥长度的调用改为直接检查长度。 |
| Intel | [PATCH v2 00/5] crypto: iaa - Fixes for multi entry SG lists ------修复 IAA 压缩驱动对多条目散列表的处理：zswap 直接传入跨页对象后，解压会失败；现在小尺寸多条目源改用预分配缓冲页交给硬件，多条目目标仍回退软件，并在回退前解除目标映射以免数据被覆盖，同时修正解压字节统计。 |
| Kernel.org | [PATCH v1 00/3] crypto: af_alg_restrict cleanups ------内核加密套接字接口在限制模式下原本允许非特权进程使用受保护密钥的 CBC 加密，现改为仅限特权进程使用，并调整白名单匹配逻辑，找到同名算法后即停止查找，避免继续遍历。 |
| Individual Contributor | [PATCH v1 00/2] crypto: keembay - use crypto_memneq() to compare GCM AEAD tags ------Keembay 加密驱动的 GCM 与 CCM 解密路径原先用逐字节比较校验收到的认证标签，比较会在首个不同字节处提前结束，可能泄露有效前缀长度并导致标签伪造，破坏 AEAD 的完整性保证。现两处均改为恒定时间比较。 |
| Linux Community | [PATCH v1 00/2] crypto: qce - simplify devm_qce_register_algs ------高通 QCE 加密驱动中，算法注册失败时的回滚循环和请求分发循环写法被简化，去掉多余的初始返回值并直接返回处理结果，逻辑更直观，不改变实际行为。 |
| Canonical | [v2,2/2] crypto: asymmetric_keys - add KUnit tests for the PE parser ------为签名 PE 文件解析器补充 KUnit 测试，构造内存中的畸形 PE 镜像，验证缺少证书表目录项时被拒绝而非越界读取，以及证书项存在但为零时按未签名处理，测试仅能内建编译。 |
| Kernel.org | [PATCH] crypto: af_alg - Allow additional ciphers for cryptsetup ------为磁盘加密工具放行 Camellia、Serpent 和 Twofish 的 XTS 模式，使普通用户仍能通过内核加密套接字接口处理这些算法的密钥槽，避免启用算法限制后无法访问已有加密卷。 |
| Bootlin | [v5] hwrng: core - Stop/start hwrng_fillfn() kthread before/after suspend-resume ------硬件随机数内核线程在系统挂起期间仍会访问已挂起的随机数设备，在 J721S2 等平台上触发错误；现在通过电源管理通知在挂起前停止该线程、恢复后重启，避免挂起过程中访问设备。 |
| Bootlin | [v2,2/2] hwrng: omap: Enable on Renesas RZ/N1D ------把硬件随机数驱动的架构依赖列表加入瑞萨 RZ/N1D，使该芯片上集成的同类随机数模块能够被编译启用，该模块实际并非 OMAP 专有。 |
| Linux Community | [PATCH] crypto: qce - simplify control flow in register functions ------简化高通加密引擎各算法注册函数的控制流，去掉跳转标签，改为在注册失败时直接注销并返回，行为不变。 |
| Individual Contributor | [PATCH] crypto: octeontx2 - use crypto_memneq() to check HMAC for cipher_null authenc ------Marvell OCTEONTX2 加密驱动在校验空加密认证请求的 HMAC 时用逐字节比较，比较会在首个不同字节处提前结束，可能通过响应时间泄露匹配前缀长度；由于该场景下被校验数据未加密，攻击者可能据此伪造通过认证的消息。现改为恒定时间比较，避免时序差异。 |
| Individual Contributor | [PATCH] crypto: octeontx - use crypto_memneq() to check HMAC ------Marvell OCTEONTX 加密驱动在校验空加密认证请求的 HMAC 时用逐字节比较，比较会在首个不同字节处提前结束，可能通过响应时间泄露匹配前缀长度；由于该场景下被校验数据未加密，攻击者可能据此伪造通过认证的消息。现改为恒定时间比较，避免时序差异。 |
| Individual Contributor | [PATCH] crypto: ccree - use crypto_memneq() to compare AEAD tag ------CCREE 加密驱动在解密完成后比较计算出的消息认证码与收到的认证值，原先的逐字节比较会在首个不同字节处提前结束，可能通过响应时间泄露匹配前缀长度。现改为恒定时间比较，使认证失败路径不再暴露比较进度。 |
| Individual Contributor | [PATCH] crypto: amcc: pass core_dev to request_irq ------AMCC 加密驱动的中断处理原先从平台设备取回驱动数据结构，现改为在注册中断时直接传入该数据结构，中断处理与释放中断时不再需要额外查找，流程更直接，行为不变。 |
| Individual Contributor | [PATCH] crypto: s5p-sss: pass s5p_aes_dev to irq handler ------三星 S5P 加密驱动的线程化中断处理原先从平台设备取回驱动数据结构，现改为在注册中断时直接传入该数据结构，中断处理不再需要额外查找，流程更直接，行为不变。 |
| Individual Contributor | [PATCH] crypto: rockchip: pass crypto_info to irq handler ------瑞芯微加密驱动在注册中断时原先传入平台设备，中断处理再从中取回驱动数据结构，现改为直接传入该数据结构，中断处理不再需要额外查找，流程更直接，行为不变。 |
| Individual Contributor | [PATCH] crypto: sa2ul - use crypto_memneq() to compare AEAD tag ------SA2UL 加密驱动在解密回调中比较计算出的认证标签与收到的标签，原先的逐字节比较会在首个不同字节处提前结束，能提交解密请求并观察完成延迟的攻击者可能逐字节恢复期望标签，进而伪造有效标签、破坏 AEAD 的完整性保证。现改为恒定时间比较。 |
| 归属待核实（jaseg.de） | [PATCH] crypto/krb5: use kfree_sensitive() for derived key buffers ------在 Kerberos 加密与校验和密钥派生流程中，派生出的密钥缓冲区原先用普通释放方式回收，密钥内容会残留在已释放的内存对象里；现改为释放前先清除密钥内容，降低密钥材料被后续分配读取的风险。 |
| Individual Contributor | [PATCH] crypto: eip93 - use struct_size() and flexible array for ring allocation ------EIP93 加密引擎驱动原先在探测时单独分配环形缓冲区，现将其直接嵌入设备结构体并一次性分配，探测流程因此少一次分配和相应失败分支，功能行为不变。 |
| Infradead Community | [PATCH] crypto: ccp - don't abuse kernel-doc comment format ------AMD 安全处理器驱动中，部分普通注释误用了内核文档注释格式，导致文档检查工具产生告警；现改用普通注释写法，消除这些告警，不涉及功能变化。 |

### 社区讨论

| 厂商 | 简介 |
|------|------|
| Rambus | [PATCH v4 00/19] crypto: cmh - add Rambus CryptoManager Hub driver ------为 Rambus CryptoManager Hub 硬件加速器新增内核驱动，通过邮箱命令队列与硬件通信，注册 AES、SM4、SHA、SM3、SHAKE、KMAC、HMAC、RSA、ECDH、ECDSA、ML-KEM、ML-DSA、SLH-DSA 等算法，并提供字符设备管理硬件密钥的创建、导入、导出、派生与销毁。硬件内生成的私钥可始终留在设备中，不暴露给内核调用方。 |
| Bootlin | [PATCH v4 00/19] crypto: talitos - Driver cleanup ------对 Freescale Talitos 安全引擎驱动做整理：把哈希、对称加密、AEAD 和随机数实现拆到独立文件并迁入专门目录，改用新的算法注册接口和宏定义，按 SEC 版本区分描述符结构，并借助静态键简化版本判断。哈希部分还改用块级接口，去掉自行维护的部分块缓冲，剩余尾部数据交回核心层重新提交。 |
| Qualcomm | [PATCH v24 00/14] crypto/dmaengine: qce: introduce BAM locking and use DMA for register I/O ------高通 QCE 加密驱动改用 BAM DMA 完成寄存器读写，并新增 BAM 管道锁定支持，同时修复设备卸载时工作队列未取消、BAM 中断释放顺序等问题；寄存器访问不再直接写内存映射，需等待传输完成，涉及多设备与并发场景。 |
| Kernel.org | [PATCH v2 00/13] Library APIs for AES encryption modes ------为内核加密库补充 AES 各工作模式的库接口，包括 ECB、CBC、CBC-CTS、CTR、XCTR、XTS、GCM 和 CCM，并让对应的加密算法改用这些库函数实现。这样架构优化代码可迁入库中供直接调用，XTS 的密文窃取也由库统一处理，无需各架构自行实现；GCM 和 CCM 支持增量处理，便于处理大消息。 |
| Individual Contributor | [PATCH v3 00/5] crypto: talitos - fix rename first/last to first_desc/last_desc ------修复 talitos 驱动在 6.6 稳定分支上的编译错误：此前把描述符首尾字段改名时漏改一处，导致 mpc85xx 编译失败。系列先回退这两次错误回退，再按正确顺序应用上游改动，让驱动不再通过 ahash 接口的 init 指针调用自身代码，并让 SEC1 引擎把超过 32k 的哈希请求拆成多个描述符处理，避免出现超出硬件上限的失败，最后完成字段改名。 |
| Individual Contributor | [PATCH v1 00/4] crypto: introduce generic dynamic software fallback and EIP93 support ------为加密驱动引入可选的动态软件回退：按算法组在 16 到 16384 字节的固定块大小上比较硬件与软件实现，把每设备的回退阈值通过 sysfs 暴露，请求按阈值分派到硬件或软件。EIP93 驱动按请求大小趋势分组并注册回退代理，控制关闭时注销代理以避免额外开销；已分配的转换无法在提供者之间迁移，因此启用前创建的转换仍绑定硬件，禁用后已存在的代理转换在释放前强制走硬件。 |
| Texas Instruments | [PATCH v7 00/2] Add support for hashing algorithms in TI DTHE V2 ------TI DTHEv2 硬件加密引擎原先只支持 AES 类算法，现为其哈希引擎新增 SHA224/256/384/512 以及对应的 HMAC 算法，使该硬件可用于消息摘要和带密钥的消息认证场景。 |
| 归属待核实（mandelbit.com） | [PATCH v1 00/5] lib/crypto: add HKDF and convert fscrypt and NVMe ------把 fscrypt 和 NVMe 认证各自私有的 HKDF 密钥派生代码提取为公共的 HKDF-SHA256、SHA-384、SHA-512 库函数，并补充 KUnit 测试。fscrypt 和 NVMe 认证改用公共实现，派生密钥不变；NVMe 不再为拼接信息分配临时缓冲区，从而去掉该分配失败路径。ovpn 的本地实现也改为调用公共函数，并把伪随机密钥改为内嵌的已准备 HMAC 密钥，去掉分配和设置密钥的失败路径。 |
| Kernel.org | [PATCH v2 00/5] lib/crypto: KUnit tests for AES-CCM and AES-GCM ------为内核加密库的 AES-CCM 和 AES-GCM 新增 KUnit 测试套件，包含一致性测试、蒙特卡洛测试、基准测试以及来自外部来源的测试向量，并检查 CCM 的消息长度校验。同时抽出共享的 AEAD 测试模板和测试工具头文件，把哈希测试改为每个用例自行分配缓冲区，使测试更独立。 |
| Kernel.org | [PATCH v1 00/3] lib/crypto: FIPS self-tests for AES encryption modes ------为内核加密库中的 AES 补充 FIPS 自检：除已有的 CMAC 自检外，新增裸 AES 以及 ECB、CBC、CBC-CTS、CTR、XTS 等非认证模式的加解密自检，并新增 GCM 和 CCM 的自检，同时把测试向量按 AES 与 SHA 拆分成独立头文件。这样在后续接入架构优化实现时，这些模式各自具备独立自检，自检失败会触发内核 panic。 |
| Individual Contributor | [RFC,RESEND,v6,1/1] crypto: atmel-ecc - fix multi-device use-after-free and registration races ------多片 Atmel ECC 设备并行初始化或快速移除再探测时，变换请求可能拿到尚未注册完成或正在解绑的 I2C 客户端指针，存在释放后使用风险；补丁引入引用计数与等待机制协调注册解绑，但超时路径仍可能遗留活跃变换，方案尚在讨论。 |
| Kernel.org | [2/2] padata: Remove serialized job support ------pcrypt 移除后，padata 中仅为其服务的串行任务支持已无使用者，现删除相关代码和文档，保留并行多线程任务调度能力，接口范围相应缩小。 |
| Texas Instruments | [v5,3/3] crypto: ti - Add support for HMAC in DTHEv2 Hashing Engine driver ------为德州仪器 DTHEv2 硬件加密引擎的哈希模块新增 HMAC 支持，使该硬件可加速 HMAC-SHA512/384/256/224 与 HMAC-MD5 运算，此前该引擎只支持普通哈希。驱动相应扩大密钥缓冲区以容纳 HMAC-SHA512 的密钥，并新增外层摘要存储，供使用该芯片的平台在硬件上完成带密钥的消息认证。 |
| Individual Contributor | [v3,2/4] crypto: rockchip: Add RK356x/RK3588 cryptographic offloader driver ------为 RK3568 和 RK3588 芯片新增第二代 Rockchip 加密加速驱动，提供 AES 的 ECB、CBC、XTS 模式以及 SHA、MD5、SM3 哈希的硬件卸载。硬件填充引擎无法跨描述符保持状态，因此多段散列表和不对齐请求会退回软件实现；XTS 硬件仅支持单段请求。驱动基于加密引擎框架，并在空闲两秒后关闭时钟和复位以省电。 |
| Astra Linux | [2/3] x509: add CRL parser with indirect CRL support ------为 X.509 证书解析新增证书吊销列表解析，按 RFC 5280 提取签发者和被吊销证书，并以证书序列号与签发者名称的哈希加入黑名单。同时支持间接吊销列表，通过解析签发分发点扩展识别间接标志，并用条目上的证书签发者扩展确定每条记录的签发者。吊销列表通过黑名单密钥环以 crl 前缀加载。 |
| Individual Contributor | [RFC] crypto: qat - zero the VF migration state buffer on save ------修复 Intel QAT 虚拟功能实时迁移接口中迁移状态缓冲区未完全初始化的问题：保存配置和状态时缓冲区只写入部分内容，却按完整大小对外暴露，未写入部分可能残留堆上旧数据或上次迁移的数据。现在保存配置前清零整个缓冲区，保存状态前清零配置区之后的区域，避免向读取方泄露陈旧内容。 |
| Individual Contributor | [PATCH] crypto: talitos: pass talitos_private to irq handlers ------talitos 加密驱动的中断处理程序原先从传入的设备结构里再取回私有数据，现在改为直接把私有数据传给中断处理程序，并在需要设备指针时从私有数据中取得。这只简化了中断入口的数据获取流程，不改变中断处理行为。 |
| strongSwan | [PATCH] lib/crypto: x86/chacha: Add a 16-block AVX-512 variant ------为 x86 的 ChaCha20 增加一次处理十六个块的 AVX-512 实现，使用完整 512 位寄存器，在输入超过八个块时优先于原有的八块 AVX-512VL 路径，剩余部分仍由后者处理。该实现只在支持 AVX-512F 且具备完整 zmm 保存状态的 CPU 上启用，并在标记偏好 256 位寄存器的 CPU 上保持禁用，以避免降频。在 Zen 5 上 1024 字节块的测速约为每秒 7.5 GB，对比原路径的 4.2 GB。 |
| Huawei | [v2] crypto: hisilicon/sec - remove SEC crypto block cipher accelerator ------移除已被 SEC2 驱动取代的华为海思 SEC 分组密码加速器驱动。该驱动长期没有活跃用户，原维护者已离开华为且无人接手，因此连同其配置选项、设备树绑定以及 hip07 板级描述中的相关节点一并删除，相关用户已迁移到算法覆盖更广的 SEC2 路径。 |
| Kernel.org | [15/33] lib/crypto: aesgcm: Remove old AES-GCM library ------删除已无使用者的旧 AES-GCM 库实现，包括其公开接口、配置选项和源文件，相关头文件也不再引入 AES 与 GHASH 头。这是清理不再被引用的代码，不改变现有加密功能。 |

---

## 已合入 Patches

### ◆ 子系统：General Crypto（20 patches）

**▸ 组织：Individual Contributor**（8 patches）

**crypto: octeontx - use crypto_memneq() to check HMAC**

- 日期：2026-08-15
- 状态：已合入
- 作者邮箱：David C.C.M. Gall <david.ccm.gall@googlemail.com>
- 概括：Marvell OCTEONTX 加密驱动在校验空加密认证请求的 HMAC 时用逐字节比较，比较会在首个不同字节处提前结束，可能通过响应时间泄露匹配前缀长度；由于该场景下被校验数据未加密，攻击者可能据此伪造通过认证的消息。现改为恒定时间比较，避免时序差异。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/aoCdOiyhQZZsFm5S@david.gall/

**crypto: amcc: pass core_dev to request_irq**

- 日期：2026-08-12
- 状态：已合入
- 作者邮箱：Rosen Penev <rosenp@gmail.com>
- 概括：AMCC 加密驱动的中断处理原先从平台设备取回驱动数据结构，现改为在注册中断时直接传入该数据结构，中断处理与释放中断时不再需要额外查找，流程更直接，行为不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260812191555.93423-1-rosenp@gmail.com/

**crypto: s5p-sss: pass s5p_aes_dev to irq handler**

- 日期：2026-08-11
- 状态：已合入
- 作者邮箱：Rosen Penev <rosenp@gmail.com>
- 概括：三星 S5P 加密驱动的线程化中断处理原先从平台设备取回驱动数据结构，现改为在注册中断时直接传入该数据结构，中断处理不再需要额外查找，流程更直接，行为不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260811043358.136042-1-rosenp@gmail.com/

**crypto: rockchip: pass crypto_info to irq handler**

- 日期：2026-08-11
- 状态：已合入
- 作者邮箱：Rosen Penev <rosenp@gmail.com>
- 概括：瑞芯微加密驱动在注册中断时原先传入平台设备，中断处理再从中取回驱动数据结构，现改为直接传入该数据结构，中断处理不再需要额外查找，流程更直接，行为不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260811044916.160856-1-rosenp@gmail.com/

**crypto: eip93 - use struct_size() and flexible array for ring allocation**

- 日期：2026-08-03
- 状态：已合入
- 作者邮箱：Rosen Penev <rosenp@gmail.com>
- 概括：EIP93 加密引擎驱动原先在探测时单独分配环形缓冲区，现将其直接嵌入设备结构体并一次性分配，探测流程因此少一次分配和相应失败分支，功能行为不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260803224028.87631-1-rosenp@gmail.com/

**crypto: hisilicon/sec: use devm_platform_ioremap_resource in sec_map_io**

- 日期：2026-07-15
- 状态：已合入
- 作者邮箱：Rosen Penev <rosenp@gmail.com>
- 概括：海思 SEC 加密驱动映射寄存器时手工获取资源再映射，现改用托管接口一次完成获取、申请和映射，并简化错误判断，行为不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260715011533.1278258-1-rosenp@gmail.com/

**crypto: omap-aes: use devm_platform_get_and_ioremap_resource**

- 日期：2026-07-15
- 状态：已合入
- 作者邮箱：Rosen Penev <rosenp@gmail.com>
- 概括：OMAP AES 驱动探测时用条件编译分别处理设备树和非设备树资源获取，现改用托管接口统一获取并映射寄存器，保留旧平台回退数据，简化探测流程。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260715215848.410011-1-rosenp@gmail.com/

**crypto: omap-sham: use devm_platform_get_and_ioremap_resource**

- 日期：2026-07-15
- 状态：已合入
- 作者邮箱：Rosen Penev <rosenp@gmail.com>
- 概括：OMAP SHA 驱动探测时同样用条件编译分别处理设备树和非设备树资源与中断获取，现改用托管接口统一处理，保留旧平台回退数据，简化探测流程。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260715220013.416122-1-rosenp@gmail.com/

**▸ 组织：Linux Community**（6 patches）

**crypto: qce - simplify control flow in register functions**

- 日期：2026-08-15
- 状态：已合入
- 作者邮箱：Thorsten Blum <thorsten.blum@linux.dev>
- 概括：简化高通加密引擎各算法注册函数的控制流，去掉跳转标签，改为在注册失败时直接注销并返回，行为不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260815150946.12142-3-thorsten.blum@linux.dev/

**crypto: starfive - use scatterlist length before DMA mapping**

- 日期：2026-07-25
- 状态：已合入
- 作者邮箱：Thorsten Blum <thorsten.blum@linux.dev>
- 概括：修复 StarFive AES 驱动在 DMA 映射前就读取散射表 DMA 长度的问题：在需要单独 DMA 长度字段的内核配置下，该长度此时尚未填充，改用原始散射表长度，避免后续清零缓冲区时长度计算错误。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260725090609.315812-2-thorsten.blum@linux.dev/

**crypto: octeontx - simplify get_{eng,ucode}_type_str helpers**

- 日期：2026-07-23
- 状态：已合入
- 作者邮箱：Thorsten Blum <thorsten.blum@linux.dev>
- 概括：简化 Marvell OcteonTX 加密驱动中把引擎类型和微码类型转成字符串的两个辅助函数，去掉局部变量、补上默认分支并直接返回结果，行为不变，只是让代码更短更直观。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260723163326.163043-2-thorsten.blum@linux.dev/

**crypto: powerpc/aes - use bool for encryption/decryption flag**

- 日期：2026-07-11
- 状态：已合入
- 作者邮箱：Thorsten Blum <thorsten.blum@linux.dev>
- 概括：把 PowerPC 上 AES 的 CBC 加解密标志从整数改为布尔类型，加密和解密调用分别传入真和假，仅统一参数语义，不改变加解密行为。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260711145216.747128-3-thorsten.blum@linux.dev/

**crypto: atmel-sha204a - clear RNG data from memory**

- 日期：2026-07-08
- 状态：已合入
- 作者邮箱：Thorsten Blum <thorsten.blum@linux.dev>
- 概括：Atmel SHA204A 随机数驱动在读取随机数后，栈上命令缓冲区仍残留最近一次随机字节，缓存的工作数据在事务失败或设备移除时也未擦除。现在在函数返回前显式清零该缓冲区，并在失败和移除路径用敏感释放清除缓存数据。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260708150359.545852-2-thorsten.blum@linux.dev/

**[SERIES] crypto: atmel-tdes - simplify fast path in crypt_start** （cover letter，2/4 个 patch 达到代码量阈值）

- 日期：2026-07-06
- 状态：已合入
- 作者邮箱：Thorsten Blum <thorsten.blum@linux.dev>
- 概括：Atmel TDES 驱动做流程简化：把快速路径的多个条件合并为一个判断，用单页分配接口替换零阶多页分配，并去掉停止流程中多余的返回变量和重复标志检查，直接返回错误。行为不变，仅减少冗余代码。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: atmel-tdes - simplify fast path in crypt_start
  - crypto: atmel-tdes - use __get_free_page in buff_init
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260706150404.382209-5-thorsten.blum@linux.dev/

**▸ 组织：Kylin**（2 patches）

**crypto: keembay - Initialize completion before requesting IRQ**

- 日期：2026-07-14
- 状态：已合入
- 作者邮箱：Linmao Li <lilinmao@kylinos.cn>
- 概括：Keem Bay OCS AES/SM4 驱动在注册中断处理后才初始化完成量，中断若在此时到达会使用未初始化的完成量；现在提前初始化，消除这一窗口。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260714033015.367735-1-lilinmao@kylinos.cn/

**crypto: keembay - publish OF module alias for OCS AES/SM4**

- 日期：2026-07-14
- 状态：已合入
- 作者邮箱：Can Peng <pengcan@kylinos.cn>
- 概括：Keem Bay OCS AES/SM4 驱动已有设备树匹配表但未导出，导致基于设备树的模块自动加载无法识别该设备；现在补上导出，使模块能按设备树自动加载。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260714131442.153699-1-pengcan@kylinos.cn/

**▸ 组织：归属待核实（gondor.apana.org.au）**（1 patches）

**crypto: ccm - Set rfc4309 maxauthsize from child**

- 日期：2026-07-20
- 状态：已合入
- 作者邮箱：Herbert Xu <herbert@gondor.apana.org.au>
- 概括：RFC4309 模式的 CCM 封装在初始化时把最大认证长度硬编码为 16，没有跟随底层算法。现改为从子算法读取该值，使封装后的认证长度上限与底层实现保持一致，避免底层支持更短认证长度时上层仍按 16 处理。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/al17HaL8wNd_fuDc@gondor.apana.org.au/

**▸ 组织：Infradead Community**（1 patches）

**crypto: ccp - don't abuse kernel-doc comment format**

- 日期：2026-07-30
- 状态：已合入
- 作者邮箱：Randy Dunlap <rdunlap@infradead.org>
- 概括：AMD 安全处理器驱动中，部分普通注释误用了内核文档注释格式，导致文档检查工具产生告警；现改用普通注释写法，消除这些告警，不涉及功能变化。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260730051710.1412969-1-rdunlap@infradead.org/

**▸ 组织：Intel**（1 patches）

**[SERIES] crypto: iaa - Fixes for multi entry SG lists** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-08-05
- 状态：已合入
- 作者邮箱：Vinicius Costa Gomes <vinicius.gomes@intel.com>
- 概括：修复 IAA 压缩驱动对多条目散列表的处理：zswap 直接传入跨页对象后，解压会失败；现在小尺寸多条目源改用预分配缓冲页交给硬件，多条目目标仍回退软件，并在回退前解除目标映射以免数据被覆盖，同时修正解压字节统计。
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
- 作者邮箱：Thomas Huth <thuth@redhat.com>
- 概括：为多个加密驱动提供统一的清理辅助，让存放 AES 密钥的本地上下文在离开作用域时自动清零，避免因遗漏返回路径而把密钥残留在栈上；同时把 safexcel 和 eip93 中仅用于校验密钥长度的密钥扩展改为直接检查长度，并修复 safexcel 在第二次密钥扩展失败时未清除首次结果的问题。
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
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：在启用算法限制时，将受保护密钥的 CBC 加密改为仅限特权进程使用，因为已知使用场景均以管理员身份运行；同时调整权限标记，让未显式标注的算法默认仅限特权进程，并在白名单命中后停止查找。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: af_alg - Make cbc(paes) privileged-only
  - crypto: af_alg - Stop after finding name in allowlist
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260802230055.100746-2-ebiggers@kernel.org/

**crypto: af_alg - Allow additional ciphers for cryptsetup**

- 日期：2026-07-05
- 状态：已合入
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：为磁盘加密工具放行 Camellia、Serpent 和 Twofish 的 XTS 模式，使普通用户仍能通过内核加密套接字接口处理这些算法的密钥槽，避免启用算法限制后无法访问已有加密卷。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260705184419.40762-1-ebiggers@kernel.org/

**▸ 组织：归属待核实（nod.at）**（1 patches）

**crypto: af_alg: Allow cbc(paes)**

- 日期：2026-07-26
- 状态：已合入
- 作者邮箱：Richard Weinberger <richard@nod.at>
- 概括：为内核加密套接字接口恢复对受保护密钥 CBC 加密的支持：此前禁止卸载到 CPU 之外的加密操作，导致依赖 CAAM 密钥封装、用户态无法自行实现的该算法被拒；现在对该算法单独放行，使普通用户仍可借助内核完成已有加密卷的访问。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260726192716.2351505-1-richard@nod.at/

---

### ◆ 子系统：Aead（3 patches）

**▸ 组织：Individual Contributor**（3 patches）

**crypto: ccree - use crypto_memneq() to compare AEAD tag**

- 日期：2026-08-15
- 状态：已合入
- 作者邮箱：David C.C.M. Gall <david.ccm.gall@googlemail.com>
- 概括：CCREE 加密驱动在解密完成后比较计算出的消息认证码与收到的认证值，原先的逐字节比较会在首个不同字节处提前结束，可能通过响应时间泄露匹配前缀长度。现改为恒定时间比较，使认证失败路径不再暴露比较进度。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/aoCdZiqJjb5XDHHz@david.gall/

**crypto: sa2ul - use crypto_memneq() to compare AEAD tag**

- 日期：2026-08-07
- 状态：已合入
- 作者邮箱：David C.C.M. Gall <david.ccm.gall@googlemail.com>
- 概括：SA2UL 加密驱动在解密回调中比较计算出的认证标签与收到的标签，原先的逐字节比较会在首个不同字节处提前结束，能提交解密请求并观察完成延迟的攻击者可能逐字节恢复期望标签，进而伪造有效标签、破坏 AEAD 的完整性保证。现改为恒定时间比较。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/anX9UKJ66Aak4ICV@fudgebox/

**[SERIES] crypto: keembay - use crypto_memneq() to compare GCM AEAD tags** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-07
- 状态：已合入
- 作者邮箱：David C.C.M. Gall <david.ccm.gall@googlemail.com>
- 概括：Keembay 加密驱动的 GCM 与 CCM 解密路径原先用逐字节比较校验收到的认证标签，比较会在首个不同字节处提前结束，可能泄露有效前缀长度并导致标签伪造，破坏 AEAD 的完整性保证。现两处均改为恒定时间比较。
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
- 作者邮箱：Thomas Richard (TI) <thomas.richard@bootlin.com>
- 概括：硬件随机数内核线程在系统挂起期间仍会访问已挂起的随机数设备，在 J721S2 等平台上触发错误；现在通过电源管理通知在挂起前停止该线程、恢复后重启，避免挂起过程中访问设备。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260804-hw-random-fix-hwrng-fillfn-crash-suspend-resume-v5-1-c4769b3c007b@bootlin.com/

**[v2,2/2] hwrng: omap: Enable on Renesas RZ/N1D**

- 日期：2026-07-10
- 状态：已合入
- 作者邮箱：Miquel Raynal <miquel.raynal@bootlin.com>
- 概括：把硬件随机数驱动的架构依赖列表加入瑞萨 RZ/N1D，使该芯片上集成的同类随机数模块能够被编译启用，该模块实际并非 OMAP 专有。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260710-schneider-v7-2-rc1-eip76-upstream-v2-2-4eab557b0e70@bootlin.com/

---

### ◆ 子系统：ICE (Qualcomm)（1 patches）

**▸ 组织：Linux Community**（1 patches）

**crypto: qat - use strscpy_pad to simplify adf_service_string_to_mask**

- 日期：2026-07-05
- 状态：已合入
- 作者邮箱：Thorsten Blum <thorsten.blum@linux.dev>
- 概括：Intel QAT 驱动解析服务配置字符串时，原先先清零缓冲区再拷贝并单独检查长度，流程冗余。现改用带填充的字符串拷贝一步完成，并用其返回值判断是否截断，同时去掉不再需要的长度参数和多余的长度计算。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260705133842.241401-3-thorsten.blum@linux.dev/

---

### ◆ 子系统：CESA (Marvell)（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: cesa: manage SRAM teardown with devm**

- 日期：2026-07-17
- 状态：已合入
- 作者邮箱：Rosen Penev <rosenp@gmail.com>
- 概括：Marvell CESA 加密引擎在探测失败或设备移除时，原先手动遍历所有引擎释放 SRAM 映射，可能对从未初始化的引擎执行解映射。现改为在映射成功建立后注册自动清理回调，由设备资源框架在探测回滚和移除时统一触发，并删除了显式释放调用，同时消除了对未初始化引擎操作的问题。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260717231742.1174221-1-rosenp@gmail.com/

---

### ◆ 子系统：Ahash（1 patches）

**▸ 组织：Linux Community**（1 patches）

**crypto: bcm - use memcpy_and_pad in ahash_hmac_setkey**

- 日期：2026-07-20
- 状态：已合入
- 作者邮箱：Thorsten Blum <thorsten.blum@linux.dev>
- 概括：博通加密驱动的 HMAC 密钥设置中，原先先复制密钥再手动填充零，现改用一次带填充的复制完成，简化了该段流程，行为不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260720232249.117992-3-thorsten.blum@linux.dev/

---

### ◆ 子系统：CAAM (NXP)（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: caam: simplify probe resource and IRQ handling**

- 日期：2026-07-30
- 状态：已合入
- 作者邮箱：Rosen Penev <rosenp@gmail.com>
- 概括：简化 CAAM 作业环的探测流程：改用平台接口获取中断和映射寄存器区域，中断获取失败时按负错误码判断，并删除不再需要的中断映射释放回调，由受管资源自动清理，各作业环节点区域互不重叠，因此独占映射不会引入冲突。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260730204722.1101805-1-rosenp@gmail.com/

---

### ◆ 子系统：Kerberos（1 patches）

**▸ 组织：归属待核实（jaseg.de）**（1 patches）

**crypto/krb5: use kfree_sensitive() for derived key buffers**

- 日期：2026-08-03
- 状态：已合入
- 作者邮箱：Jan Sebastian Götte <linux@jaseg.de>
- 概括：在 Kerberos 加密与校验和密钥派生流程中，派生出的密钥缓冲区原先用普通释放方式回收，密钥内容会残留在已释放的内存对象里；现改为释放前先清除密钥内容，降低密钥材料被后续分配读取的风险。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260803192621.329577-1-linux@jaseg.de/

---

### ◆ 子系统：Authenc（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: octeontx2 - use crypto_memneq() to check HMAC for cipher_null authenc**

- 日期：2026-08-15
- 状态：已合入
- 作者邮箱：David C.C.M. Gall <david.ccm.gall@googlemail.com>
- 概括：Marvell OCTEONTX2 加密驱动在校验空加密认证请求的 HMAC 时用逐字节比较，比较会在首个不同字节处提前结束，可能通过响应时间泄露匹配前缀长度；由于该场景下被校验数据未加密，攻击者可能据此伪造通过认证的消息。现改为恒定时间比较，避免时序差异。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/aoCdBZ-kLQ0rciFi@david.gall/

---

### ◆ 子系统：ECC（1 patches）

**▸ 组织：Linux Community**（1 patches）

**[SERIES] crypto: atmel-ecc - simplify control flow in atmel_ecdh_set_secret** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-07-28
- 状态：已合入
- 作者邮箱：Thorsten Blum <thorsten.blum@linux.dev>
- 概括：简化 atmel-ecc 的 ECDH 密钥设置流程：I2C 事务失败时直接释放公钥并去掉跳转标签，生成公钥函数去掉多余的返回变量，直接返回错误或成功，行为不变。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: atmel-ecc - simplify control flow in atmel_ecdh_set_secret
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260728205825.471233-3-thorsten.blum@linux.dev/

---

### ◆ 子系统：QCE (Qualcomm)（1 patches）

**▸ 组织：Linux Community**（1 patches）

**[SERIES] crypto: qce - simplify devm_qce_register_algs** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-07-31
- 状态：已合入
- 作者邮箱：Thorsten Blum <thorsten.blum@linux.dev>
- 概括：高通 QCE 加密驱动中，算法注册失败时的回滚循环和请求分发循环写法被简化，去掉多余的初始返回值并直接返回处理结果，逻辑更直观，不改变实际行为。
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
- 作者邮箱：Fabrice Derepas <fabrice.derepas@canonical.com>
- 概括：修复 PE 文件签名解析中读取证书表目录项时的越界读取：当映像声明的数据目录项数量不足时，解析器仍会读取固定位置的证书表大小字段，可能读到映像之外；现在要求该目录项必须存在，否则直接拒绝。该路径由 kexec 加载受签名校验的 PE 映像时触发，需要相应权限，且仅涉及越界读取。同时补充内核单元测试，用构造的畸形映像验证拒绝行为。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: asymmetric_keys - add KUnit tests for the PE parser
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/fcbc6b4d5855ba42a0fccf335b2604ef0b36f092.1786802052.git.fabrice.derepas@canonical.com/

---

## 社区讨论中 Patches

### ◆ 子系统：General Crypto（41 patches）

**▸ 组织：Individual Contributor**（10 patches）

**crypto: arm64/aes-neonbs: transition to kmalloc_obj()**

- 日期：2026-08-30
- 状态：社区讨论中
- 作者邮箱：Manuel Ebner <manuelebnerli@mailbox.org>
- 概括：arm64 的 AES 位切片实现把密钥扩展数据从栈上移到堆分配，本次将两处分配改为类型感知的分配接口，分配大小由对象类型自动推导，避免手写大小出错，行为不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260830101714.625728-3-manuelebnerli@mailbox.org/

**crypto: atmel-tdes - zero-initialize device state**

- 日期：2026-08-29
- 状态：社区讨论中
- 作者邮箱：Karl Mehltretter <kmehltretter@gmail.com>
- 概括：Atmel TDES 驱动在改用托管内存分配时误用了不置零的分配方式，导致设备状态残留旧标志，探测时可能跳过硬件复位或让引擎被误判为永久忙，SAM9X75 上表现为启动后首个 TDES 请求永不完成。现改回置零分配，使状态从干净值开始，请求可正常派发。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260829035821.67220-1-kmehltretter@gmail.com/

**[SERIES] crypto: amlogic: Fix IRQ handler return value and fallthrough logic** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-08-21
- 状态：社区讨论中
- 作者邮箱：Mohamad Raizudeen <raizudeen.kerneldev@gmail.com>
- 概括：修正 Amlogic 加密加速器中断处理程序的返回值：当某条数据流有中断但状态寄存器为空时，原来会继续循环并误报未知中断，现在直接返回已处理；对真正未知的中断改为返回未处理，使内核能识别虚假中断。同时改用设备托管接口管理时钟和加密引擎，去掉手动清理，简化探测和移除流程。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: amlogic: Use devm APIs for clock and engine management
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260821151243.8125-1-raizudeen.kerneldev@gmail.com/

**[RFC] crypto: qat - zero the VF migration state buffer on save**

- 日期：2026-08-17
- 状态：社区讨论中
- 作者邮箱：Karl Mehltretter <kmehltretter@gmail.com>
- 概括：修复 Intel QAT 虚拟功能实时迁移接口中迁移状态缓冲区未完全初始化的问题：保存配置和状态时缓冲区只写入部分内容，却按完整大小对外暴露，未写入部分可能残留堆上旧数据或上次迁移的数据。现在保存配置前清零整个缓冲区，保存状态前清零配置区之后的区域，避免向读取方泄露陈旧内容。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260817042613.19855-1-kmehltretter@gmail.com/

**[v3,2/4] crypto: rockchip: Add RK356x/RK3588 cryptographic offloader driver**

- 日期：2026-08-16
- 状态：社区讨论中
- 作者邮箱：Dawid Olesinski <dawidro@gmail.com>
- 概括：为 RK3568 和 RK3588 芯片新增第二代 Rockchip 加密加速驱动，提供 AES 的 ECB、CBC、XTS 模式以及 SHA、MD5、SM3 哈希的硬件卸载。硬件填充引擎无法跨描述符保持状态，因此多段散列表和不对齐请求会退回软件实现；XTS 硬件仅支持单段请求。驱动基于加密引擎框架，并在空闲两秒后关闭时钟和复位以省电。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260816194112.552100-3-dawidro@gmail.com/

**crypto: amcc: trng: use devm_of_iomap()**

- 日期：2026-08-12
- 状态：社区讨论中
- 作者邮箱：Rosen Penev <rosenp@gmail.com>
- 概括：PPC4xx 平台的真随机数发生器驱动改用受管设备资源方式映射寄存器，使映射在驱动卸载时自动解除，去掉了出错和移除路径中手动解除映射的调用，简化了清理流程。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260812185747.79173-1-rosenp@gmail.com/

**[SERIES] crypto: img-hash: clean up probe** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-08-11
- 状态：社区讨论中
- 作者邮箱：Rosen Penev <rosenp@gmail.com>
- 概括：调整图像哈希加速器驱动的探测流程，把中断、寄存器和时钟的获取提前到分配设备结构之前，使资源获取失败时可直接返回并支持延迟探测；同时把中断申请改为显式申请和释放，确保在移除和探测出错时先释放中断再终止任务队列，避免拆除过程中中断处理程序再次调度任务。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: img-hash: fetch resources into locals before probe body
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260811212030.20057-2-rosenp@gmail.com/

**crypto: amcc: get irq and ioremap resource first**

- 日期：2026-07-30
- 状态：社区讨论中
- 作者邮箱：Rosen Penev <rosenp@gmail.com>
- 概括：调整 AMCC 加密驱动的探测顺序，把获取中断和映射寄存器资源提前到其他初始化之前，这两步可能返回延迟探测，提前执行可避免在不需要时做多余工作。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260730204915.1102403-1-rosenp@gmail.com/

**[SERIES] crypto: introduce generic dynamic software fallback and EIP93 support** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-07-28
- 状态：社区讨论中
- 作者邮箱：Jihong Min <hurryman2212@gmail.com>
- 概括：为加密驱动引入可选的动态软件回退：按算法组在 16 到 16384 字节的固定块大小上比较硬件与软件实现，把每设备的回退阈值通过 sysfs 暴露，请求按阈值分派到硬件或软件。EIP93 驱动按请求大小趋势分组并注册回退代理，控制关闭时注销代理以避免额外开销；已分配的转换无法在提供者之间迁移，因此启用前创建的转换仍绑定硬件，禁用后已存在的代理转换在释放前强制走硬件。
- 达到阈值的 patches（4 个，显示前 5）：
  - crypto: move cycle benchmark helpers out of tcrypt
  - crypto: introduce dynamic software fallback
  - crypto: eip93 - add dynamic software fallback support
  - crypto: eliminate fallback proxy overhead while disabled
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/e0ce93088c1d9772e928fcbd113a446b7fb7442f.1785226804.git.hurryman2212@gmail.com/

**[SERIES] crypto: eip93: fix request lifetime and completion handling** （cover letter，4/5 个 patch 达到代码量阈值）

- 日期：2026-07-07
- 状态：社区讨论中
- 作者邮箱：Jihong Min <hurryman2212@gmail.com>
- 概括：修复 EIP93 加密引擎驱动的请求生命周期问题：未初始化映射时不再错误解映射，HMAC 在设置密钥前被拒绝，加密请求改用请求本地记录避免并发请求互相污染，结果描述符读取在引擎就绪后排序，请求编号耗尽时等待并容忍过期编号，减少错误路径下的内存与映射问题。
- 达到阈值的 patches（4 个，显示前 5）：
  - crypto: eip93: reject HMAC requests before setkey
  - crypto: eip93: use request-local SA records for cipher requests
  - crypto: eip93: order result descriptor reads after PE_READY
  - crypto: eip93: handle request ID exhaustion
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260707171537.467608-2-hurryman2212@gmail.com/

**▸ 组织：Kernel.org**（8 patches）

**[SERIES] x86: Remove cpu_has_xfeatures() and add AVX-512 xor_gen()** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-15
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：移除 x86 上对扩展状态特性检查函数的调用，改由内核在启动时校验并清除缺失的 AVX 与 AVX-512 状态位，同时为异或运算新增 AVX-512 实现，在支持且不偏好窄向量的新处理器上提升吞吐。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: x86 - Stop using cpu_has_xfeatures()
  - lib/crypto: x86: Stop using cpu_has_xfeatures()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260815181024.28924-4-ebiggers@kernel.org/

**[SERIES] lib/crypto: KUnit tests for AES-CCM and AES-GCM** （cover letter，5/5 个 patch 达到代码量阈值）

- 日期：2026-08-02
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：为内核加密库的 AES-CCM 和 AES-GCM 新增 KUnit 测试套件，包含一致性测试、蒙特卡洛测试、基准测试以及来自外部来源的测试向量，并检查 CCM 的消息长度校验。同时抽出共享的 AEAD 测试模板和测试工具头文件，把哈希测试改为每个用例自行分配缓冲区，使测试更独立。
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
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：为内核加密库中的 AES 补充 FIPS 自检：除已有的 CMAC 自检外，新增裸 AES 以及 ECB、CBC、CBC-CTS、CTR、XTS 等非认证模式的加解密自检，并新增 GCM 和 CCM 的自检，同时把测试向量按 AES 与 SHA 拆分成独立头文件。这样在后续接入架构优化实现时，这些模式各自具备独立自检，自检失败会触发内核 panic。
- 达到阈值的 patches（3 个，显示前 5）：
  - lib/crypto: fips: Split fips.h into fips-aes.h and fips-sha.h
  - lib/crypto: aes: Add FIPS self-tests for unauthenticated modes
  - lib/crypto: aes: Add FIPS self-tests for GCM and CCM
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260802222408.91757-2-ebiggers@kernel.org/

**crypto: qce - Replace with stub driver**

- 日期：2026-07-31
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：把高通 QCE 加密驱动改为仅绑定设备树节点的桩驱动：其注册的算法性能远不如 CPU 实现且开销更大，也不支持磁盘加密和 IPsec 等常见场景，因此移除全部加密功能，只保留降低互连带宽投票以省电的作用。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260731050838.158825-1-ebiggers@kernel.org/

**[SERIES] More padata cleanups** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-07-17
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：padata 在串行任务接口移除后仅剩启动期使用，因此把剩余内部函数和数据标记为启动后释放，并在启动完成后释放此前一直未释放的工作项内存，消除这一内存泄漏。
- 达到阈值的 patches（2 个，显示前 5）：
  - padata: Free the padata_works when they're no longer needed
  - padata: Mark remaining code as __init and data as __initdata
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260717171831.27994-3-ebiggers@kernel.org/

**[SERIES] Library APIs for AES encryption modes** （cover letter，12/13 个 patch 达到代码量阈值）

- 日期：2026-07-15
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：为内核加密库补充 AES 各工作模式（ECB、CBC 及密文窃取、CTR 与 XCTR、XTS、GCM、CCM）的库接口，并让传统加密算法改用这些库实现，同时把架构优化代码迁入库中。这样文件系统、网络等直接调用者可用更简洁的接口，XTS 的密文窃取也由库统一处理，不再要求各架构自行实现。
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
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：pcrypt 移除后，padata 中仅为其服务的串行任务支持已无使用者，现删除相关代码和文档，保留并行多线程任务调度能力，接口范围相应缩小。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260713223234.24812-3-ebiggers@kernel.org/

**lib/crypto: docs: Improve introduction sentence**

- 日期：2026-07-09
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：内核加密库文档的开头没有说明这是仅供内核内部使用的库，在线浏览者容易误解其用途。现在改写介绍语句，明确该库面向内核内部调用者，提供比传统加密接口更快捷的算法访问方式。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260709022747.44635-1-ebiggers@kernel.org/

**▸ 组织：Red Hat**（6 patches）

**[v3] crypto: inside-secure - Zeroize temporary arrays on stack with sensitive data**

- 日期：2026-08-19
- 状态：社区讨论中
- 作者邮箱：Thomas Huth <thuth@redhat.com>
- 概括：Inside Secure 硬件加密驱动的 AES-XCBC 和 AES-CMAC 设置密钥函数在栈上暂存密钥材料，函数返回后这些数据可能残留；现在在返回前显式清零这些临时数组，减少栈上泄露密钥的可能。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260819151845.835768-1-thuth@redhat.com/

**lib/crypto: chacha20poly1305: Clear chacha_state in xchacha20poly1305_decrypt()**

- 日期：2026-08-13
- 状态：社区讨论中
- 作者邮箱：Thomas Huth <thuth@redhat.com>
- 概括：XChaCha20-Poly1305 解密函数此前未像 ChaCha20-Poly1305 那样在结束时清除栈上的 ChaCha 状态，可能把密钥相关数据留在栈上；现在两个解密函数都在返回时自动清零该状态。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260813130147.949545-1-thuth@redhat.com/

**[SERIES] libcrypto: Provide more __cleanup functions for zeroizing data** （cover letter，7/7 个 patch 达到代码量阈值）

- 日期：2026-08-13
- 状态：社区讨论中
- 作者邮箱：Thomas Huth <thuth@redhat.com>
- 概括：为 AES、HMAC-MD5、HMAC-SHA1 和 SHA2 系列 HMAC 的密钥与上下文提供统一的自动清零辅助，让使用这些结构的代码在离开作用域时自动清除密钥材料，减少遗漏返回路径导致栈上残留密钥的风险；同时把库内已有的显式清零调用改为使用这些辅助，并为 x86 引导环境调整编译选项以兼容新增头文件。
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
- 作者邮箱：Thomas Huth <thuth@redhat.com>
- 概括：为 HMAC-SHA1 上下文提供自动清零辅助，使可信密钥等使用该算法的代码在提前返回、未调用终结函数时也能清除栈上的上下文，避免敏感数据残留；同时把库内已有的显式清零调用改为使用该辅助。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: Provide a wrapper for zeroizing hmac_sha1_ctx
  - lib/crypto: sha1: Use hmac_sha1_zeroize_ctx() instead of memzero_explicit()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260812163336.3103835-2-thuth@redhat.com/

**[SERIES] crypto: Add __cleanup functions for zeroizing aes_cmac_key & aes_cmac_ctx** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-08-07
- 状态：社区讨论中
- 作者邮箱：Thomas Huth <thuth@redhat.com>
- 概括：为使用 AES-CMAC 的代码提供密钥和上下文的自动清零辅助，使 SMB 服务端、TCP 认证选项、蓝牙配对以及无线认证等场景在离开作用域时自动清除本地密钥材料，避免敏感数据残留在栈上；蓝牙部分还额外清除了保存原始密钥的临时数组。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: Provide wrapper functions for zeroizing aes_cmac_key and aes_cmac_ctx
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260807125845.1477067-2-thuth@redhat.com/

**[RFC] crypto: pcrypt - Disallow nesting of the pcrypt wrapper**

- 日期：2026-07-01
- 状态：社区讨论中
- 作者邮箱：Thomas Huth <thuth@redhat.com>
- 概括：pcrypt 并行加密包装器允许被嵌套使用，在并发自测场景下可能因递归分配失败而触发内核告警。现在在初始化实例时检测算法名中是否已含 pcrypt，若已嵌套则直接拒绝，避免递归包装导致的资源耗尽和调用栈异常。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260701143947.944593-1-thuth@redhat.com/

**▸ 组织：Huawei**（2 patches）

**crypto: hisilicon/zip - enable auto clock gating for DAE**

- 日期：2026-08-29
- 状态：社区讨论中
- 作者邮箱：Chenghai Huang <huangchenghai2@huawei.com>
- 概括：海思压缩加速器的 DAE 模块此前空闲时仍持续耗电。现在在 DAE 初始化完成后开启自动时钟门控，并在初始化内存前先关闭门控以保证流程正确，使设备空闲时能降低功耗。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260829094924.2191402-1-huangchenghai2@huawei.com/

**[v2] crypto: hisilicon/sec - remove SEC crypto block cipher accelerator**

- 日期：2026-08-19
- 状态：社区讨论中
- 作者邮箱：Chenghai Huang <huangchenghai2@huawei.com>
- 概括：移除已被 SEC2 驱动取代的华为海思 SEC 分组密码加速器驱动。该驱动长期没有活跃用户，原维护者已离开华为且无人接手，因此连同其配置选项、设备树绑定以及 hip07 板级描述中的相关节点一并删除，相关用户已迁移到算法覆盖更广的 SEC2 路径。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260819075353.94500-1-huangchenghai2@huawei.com/

**▸ 组织：Qualcomm**（2 patches）

**[SERIES] crypto/dmaengine: qce: introduce BAM locking and use DMA for register I/O** （cover letter，7/8 个 patch 达到代码量阈值）

- 日期：2026-07-23
- 状态：社区讨论中
- 作者邮箱：Bartosz Golaszewski <bartosz.golaszewski@oss.qualcomm.com>
- 概括：为高通 QCE 加密引擎引入 BAM 管道锁定并用 DMA 完成寄存器读写：先修复设备卸载时未取消工作队列、BAM 中断释放顺序等问题，再让加密寄存器操作通过 DMA 命令描述符下发，并在事务完成前不写配置寄存器，避免引擎忙时被写入。
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
- 作者邮箱：Bartosz Golaszewski <bartosz.golaszewski@oss.qualcomm.com>
- 概括：高通加密引擎驱动因 DMA 不支持零长度传输、硬件不递增部分块计数器、只接受连续缓冲区等原因，多项自检失败。该系列对空消息的 HMAC 改走软件回退，空消息的 AES-XTS 返回参数错误，修正 CTR 部分块的计数器，并对部分块、分片负载及弱密钥的 XTS 改用软件回退，使相关算法自检通过。
- 达到阈值的 patches（5 个，显示前 5）：
  - crypto: qce - Reject empty messages for AES-XTS
  - crypto: qce - Use a fallback for AES-CTR with a partial final block
  - crypto: qce - Use a fallback for CCM with a partial final block
  - crypto: qce - Use fallback for CCM with a fragmented payload
  - crypto: qce - Use fallback for fragmented skcipher payloads
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260717-qce-fix-self-tests-v6-1-455775fe5f6c@oss.qualcomm.com/

**▸ 组织：Texas Instruments**（2 patches）

**[SERIES] Add support for hashing algorithms in TI DTHE V2** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-27
- 状态：社区讨论中
- 作者邮箱：T Pratham <t-pratham@ti.com>
- 概括：TI DTHEv2 硬件加密引擎原先只支持 AES 类算法，现为其哈希引擎新增 SHA224/256/384/512 以及对应的 HMAC 算法，使该硬件可用于消息摘要和带密钥的消息认证场景。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: ti - Add support for SHA224/256/384/512 in DTHEv2 driver
  - crypto: ti - Add support for HMAC in DTHEv2 driver
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260827133542.619717-2-t-pratham@ti.com/

**[SERIES] Fix several issues in DTHEv2 driver** （cover letter，2/7 个 patch 达到代码量阈值）

- 日期：2026-08-27
- 状态：社区讨论中
- 作者邮箱：T Pratham <t-pratham@ti.com>
- 概括：德州仪器 DTHEv2 加密驱动存在多处缺陷：设备列表为空时取到伪指针、软中断与进程间可能死锁、高端内存页经虚拟地址访问可能损坏内存、IPSec 场景下散列表长度超出实际数据导致 DMA 超时崩溃、驱动移除时进行中的变换上下文可能访问已释放数据、散列表长度校验缺失。现分别改用可返回空的取首项、统一加锁方式、按页建立映射、把散列表裁剪到实际密文长度、为设备数据加引用计数并在移除时有限等待、校验长度查询返回值，降低上述崩溃和越界风险。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: ti - Trim scatterlists to correct length in AES
  - crypto: ti - Use list_first_entry_or_null() in dthe_get_dev()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260827132318.613876-5-t-pratham@ti.com/

**▸ 组织：AMD**（1 patches）

**[3/3] crypto: xilinx: zynqmp-aes-gcm: Send firmware decoded code instead of EBADMSG**

- 日期：2026-07-06
- 状态：社区讨论中
- 作者邮箱：Harsh Jain <h.jain@amd.com>
- 概括：AMD Versal 平台 AES-GCM 解密失败时，驱动把固件返回的具体错误码统一替换成通用消息错误，掩盖了真实原因。现在直接向上层传递固件解码后的错误码，使调用者能区分不同失败情形。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260706110254.2427551-4-h.jain@amd.com/

**▸ 组织：Oracle**（1 patches）

**padata: Replace bottom-half spinlock variants**

- 日期：2026-07-17
- 状态：社区讨论中
- 作者邮箱：Daniel Jordan <daniel.m.jordan@oracle.com>
- 概括：padata 已不再在软中断上下文运行，因此把其工作锁的关中断自旋锁版本替换为普通自旋锁，仅简化加锁方式，不改变并发语义。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260717205028.63847-1-daniel.m.jordan@oracle.com/

**▸ 组织：Kylin**（1 patches）

**crypto: verify_pefile - Use constant-time digest comparison**

- 日期：2026-07-20
- 状态：社区讨论中
- 作者邮箱：Jiangshan Yi <yijiangshan@kylinos.cn>
- 概括：PE 文件签名校验中比较摘要时使用普通内存比较，耗时随首个不同字节位置变化，可能被用来逐字节伪造 PE 文件签名。现改为恒定时间比较，与加密子系统其他部分保持一致，并补充了所需头文件引用。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260720031815.204237-1-yijiangshan@kylinos.cn/

**▸ 组织：strongSwan**（1 patches）

**lib/crypto: x86/chacha: Add a 16-block AVX-512 variant**

- 日期：2026-07-22
- 状态：社区讨论中
- 作者邮箱：Martin Willi <martin@strongswan.org>
- 概括：为 x86 的 ChaCha20 增加一次处理十六个块的 AVX-512 实现，使用完整 512 位寄存器，在输入超过八个块时优先于原有的八块 AVX-512VL 路径，剩余部分仍由后者处理。该实现只在支持 AVX-512F 且具备完整 zmm 保存状态的 CPU 上启用，并在标记偏好 256 位寄存器的 CPU 上保持禁用，以避免降频。在 Zen 5 上 1024 字节块的测速约为每秒 7.5 GB，对比原路径的 4.2 GB。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260722153247.630519-1-martin@strongswan.org/

**▸ 组织：归属待核实（jaseg.de）**（1 patches）

**[v2,12/13] crypto: api - wipe tfm contexts before kdump**

- 日期：2026-08-11
- 状态：社区讨论中
- 作者邮箱：Jan Sebastian Götte <linux@jaseg.de>
- 概括：在启用崩溃转储前清除密钥配置下，内核加密变换对象中保存的扩展密钥等密钥材料会在 kdump 前被统一擦除，避免转储内存时泄露；但栈上或硬件密钥寄存器中的副本不在覆盖范围内，且该配置未启用时不做处理。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260811-crash-zeroize-rework-v2-12-9561d13c2340@jaseg.de/

**▸ 组织：东南大学**（1 patches）

**[v2] crypto: ccp: Initialize DBC ioctl mutex before registering device**

- 日期：2026-08-30
- 状态：社区讨论中
- 作者邮箱：Runyu Xiao <runyu.xiao@seu.edu.cn>
- 概括：AMD 动态加速控制的字符设备在注册后才初始化 ioctl 互斥锁，设备一旦发布，用户空间即可打开并调用 ioctl，此时锁尚未初始化。现将锁的初始化提前到设备注册之前，使已发布的 ioctl 回调总能见到已初始化的锁。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260830015104.2040153-1-runyu.xiao@seu.edu.cn/

**▸ 组织：Intel**（1 patches）

**[1/2] crypto: qat - allow KPT disable when service is not asym**

- 日期：2026-08-31
- 状态：社区讨论中
- 作者邮箱：None <nitesh.venkatesh@intel.com>
- 概括：Intel QAT 的密钥保护开关在服务不是非对称模式时拒绝任何写入，包括关闭操作，导致服务切换后残留的启用标志无法清除。现在先解析写入值，仅在启用方向检查服务类型，关闭请求在设备处于停止状态时始终接受，使恢复流程可完成。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260831063355.668528-2-nitesh.venkatesh@intel.com/

**▸ 组织：Rambus**（1 patches）

**[SERIES] crypto: cmh - add Rambus CryptoManager Hub driver** （cover letter，15/15 个 patch 达到代码量阈值）

- 日期：2026-08-25
- 状态：社区讨论中
- 作者邮箱：Ousherovitch, Alex <aousherovitch@rambus.com>
- 概括：为 Rambus CryptoManager Hub 硬件加速器新增内核驱动，通过邮箱命令队列与硬件通信，注册 AES、SM4、SHA、SM3、SHAKE、KMAC、HMAC、RSA、ECDH、ECDSA、ML-KEM、ML-DSA、SLH-DSA 等算法，并提供字符设备管理硬件密钥的创建、导入、导出、派生与销毁。硬件内生成的私钥可始终留在设备中，不暴露给内核调用方。
- 达到阈值的 patches（15 个，显示前 5）：
  - crypto: cmh - add HMAC ahash
  - crypto: cmh - add ML-KEM/ML-DSA (QSE)
  - crypto: cmh - add DRBG hwrng
  - crypto: cmh - add CSHAKE/KMAC ahash
  - crypto: cmh - add SHA-2/SHA-3/SHAKE ahash
  - ... 及其他 10 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260825221539.255951-6-aousherovitch@rambus.com/

**▸ 组织：归属待核实（mandelbit.com）**（1 patches）

**[SERIES] lib/crypto: add HKDF and convert fscrypt and NVMe** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-07-21
- 状态：社区讨论中
- 作者邮箱：Marco Baffo <marco@mandelbit.com>
- 概括：把 fscrypt 和 NVMe 认证各自私有的 HKDF 密钥派生代码提取为公共的 HKDF-SHA256、SHA-384、SHA-512 库函数，并补充 KUnit 测试。fscrypt 和 NVMe 认证改用公共实现，派生密钥不变；NVMe 不再为拼接信息分配临时缓冲区，从而去掉该分配失败路径。ovpn 的本地实现也改为调用公共函数，并把伪随机密钥改为内嵌的已准备 HMAC 密钥，去掉分配和设置密钥的失败路径。
- 达到阈值的 patches（2 个，显示前 5）：
  - lib/crypto: tests: add HKDF KUnit tests
  - lib/crypto: add HKDF-SHA{256,384,512}
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260721140644.780006-3-marco@mandelbit.com/

**▸ 组织：Astra Linux**（1 patches）

**[SERIES] Add X.509 CRL support** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-08-22
- 状态：社区讨论中
- 作者邮箱：Timofei Novikov <tnovikov@astralinux.ru>
- 概括：为内核的 X.509 证书处理新增证书吊销列表解析与签名校验能力：解析吊销列表中的签发者和被吊销证书，按序列号与签发者哈希加入黑名单，并支持间接吊销列表的逐条签发者识别；处理前会先校验吊销列表的数字签名，未提供密钥环时跳过校验。同时修正 ASN.1 解析中可选字段的处理，使可选引用类型和可选序列能正确跳过。
- 达到阈值的 patches（1 个，显示前 5）：
  - x509: add CRL parser with indirect CRL support
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260822082642.48936-3-tnovikov@astralinux.ru/

**▸ 组织：Linux Community**（1 patches）

**[SERIES] crypto: zstd - avoid initializing the workspace twice** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-25
- 状态：社区讨论中
- 作者邮箱：Usama Arif <usama.arif@linux.dev>
- 概括：zswap 压缩和解压每个页面时，zstd 驱动会先把共享工作区初始化为流式上下文，随后又按一次性路径重新初始化，前一次初始化完全白做。现将流式初始化推迟到真正需要流式处理的首次循环，一次性路径不再重复初始化。压缩基准单轮平均耗时在物理机下降约百分之二、单核虚拟机下降约百分之十，解压下降约百分之十四和百分之三十六。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: zstd - Avoid redundant cstream initialization
  - crypto: zstd - Avoid redundant dstream initialization
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260825220616.3842633-2-usama.arif@linux.dev/

---

### ◆ 子系统：Public Key（6 patches）

**▸ 组织：Individual Contributor**（2 patches）

**crypto: rsassa-pkcs1: use constant-time comparison for digest and signature verification**

- 日期：2026-07-10
- 状态：社区讨论中
- 作者邮箱：David C.C.M. Gall <david.ccm.gall@googlemail.com>
- 概括：RSA PKCS#1 签名校验用普通内存比较来核对摘要，比较过程可能通过时间差异泄露有效前缀长度，用户提供的摘要可到达该比较。现在改用恒定时间比较，使比较耗时不再随匹配前缀长度变化。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/alEr_e-G0L2nxxv-@fudgebox/

**crypto: pkcs7_verify: use constant-time comparison for digest and signature verification**

- 日期：2026-07-10
- 状态：社区讨论中
- 作者邮箱：David C.C.M. Gall <david.ccm.gall@googlemail.com>
- 概括：PKCS#7 消息签名校验在核对摘要时使用普通内存比较，可能通过时间差异泄露附加签名的有效前缀长度。现在改用恒定时间比较，使校验耗时不再随匹配前缀长度变化。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/alEsSl8i1_FpoU0f@fudgebox/

**▸ 组织：Kylin**（2 patches）

**crypto: rsassa-pkcs1 - Use constant-time digest comparison**

- 日期：2026-07-20
- 状态：社区讨论中
- 作者邮箱：Jiangshan Yi <yijiangshan@kylinos.cn>
- 概括：RSA PKCS#1 v1.5 签名校验中比较摘要时使用普通内存比较，比较耗时取决于首个不同字节的位置，可能被用来逐字节伪造签名。现改为恒定时间比较，与同一函数中已有的哈希前缀比较方式保持一致，堵住这一时序侧信道途径。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260720021322.122784-1-yijiangshan@kylinos.cn/

**crypto: pkcs7 - Use constant-time message digest comparison**

- 日期：2026-07-20
- 状态：社区讨论中
- 作者邮箱：Jiangshan Yi <yijiangshan@kylinos.cn>
- 概括：PKCS#7 签名校验中比较消息摘要时使用普通内存比较，耗时随首个不同字节位置变化，可能被用来逐字节伪造签名。现改为恒定时间比较，与加密子系统其他部分保持一致，并补充了所需头文件引用。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260720032316.210113-1-yijiangshan@kylinos.cn/

**▸ 组织：0SEC**（1 patches）

**[6.1/6.6/6.12.y] crypto: rsa-pkcs1pad: Don't WARN on an empty digest**

- 日期：2026-07-20
- 状态：社区讨论中
- 作者邮箱：Doruk Tan Ozturk <doruk@0sec.ai>
- 概括：在 6.1、6.6、6.12 稳定分支上，非特权用户可通过密钥验证接口传入零长度摘要，触发内核警告；若内核配置为警告即崩溃，本地用户可借此使机器宕机。现保留对无效请求返回参数错误，但不再对用户可控的长度发出警告。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260720191525.15450-1-doruk@0sec.ai/

**▸ 组织：ANSSI**（1 patches）

**[SERIES] crypto: rsassa-pkcs1: fix undersized key handling** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-26
- 状态：社区讨论中
- 作者邮箱：Jérémy Jean <Jeremy.Jean@oss.cyber.gouv.fr>
- 概括：RSA PKCS#1 v1.5 签名和验签在密钥长度不足时，用无符号密钥长度减去 11 会回绕，导致填充写入或读取越界，KASAN 已报告一字节密钥下的越界访问。现改为在签名和验签入口拒绝小于最小编码消息长度的密钥，返回参数错误，避免越界读写。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: rsassa-pkcs1: reject undersized keys when signing
  - crypto: rsassa-pkcs1: reject undersized keys when verifying
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260826103744.1554131-2-Jeremy.Jean@oss.cyber.gouv.fr/

---

### ◆ 子系统：HWRNG（3 patches）

**▸ 组织：StarFive**（1 patches）

**[v7,2/2] hwrng: starfive: rework clk/reset teardown order for JHB100**

- 日期：2026-08-12
- 状态：社区讨论中
- 作者邮箱：lianfeng.ouyang <lianfeng.ouyang@starfivetech.com>
- 概括：为 StarFive 真随机数驱动适配 JHB100 芯片：该芯片要求先关时钟再复位，否则复位域交叉可能产生毛刺影响下游模块，而 JH7110 保持先复位顺序。同时修正运行时电源管理在初始化、读取、重播种和清理路径上的配对，改用受管资源自动回滚，把重播种从硬中断移到工作队列，并用互斥锁串行化命令序列。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260812023401.44149-3-lianfeng.ouyang@starfivetech.com/

**▸ 组织：SUSE**（1 patches）

**[v2,07/13] hw_random/via-rng: Stop using 32-bit MSR interfaces**

- 日期：2026-08-19
- 状态：社区讨论中
- 作者邮箱：Jürgen Groß <jgross@suse.com>
- 概括：VIA 平台硬件随机数驱动原先使用计划移除的 32 位 MSR 读写接口，现改用对应的 64 位接口完成同样的寄存器读取和配置写入，行为不变，只是适配接口变更。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260819102314.1499258-8-jgross@suse.com/

**▸ 组织：Individual Contributor**（1 patches）

**hwrng: imx-rngc: check clk_prepare_enable() return value**

- 日期：2026-08-28
- 状态：社区讨论中
- 作者邮箱：李佑鸿 <dayou5941@163.com>
- 概括：i.MX 随机数发生器驱动在探测和系统恢复时忽略时钟使能失败，仍继续访问寄存器或报告成功；现在检查该返回值，失败时探测直接报错返回，恢复时把错误向上传递。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260828025423.2149304-1-dayou5941@163.com/

---

### ◆ 子系统：Talitos（3 patches）

**▸ 组织：Individual Contributor**（2 patches）

**crypto: talitos: pass talitos_private to irq handlers**

- 日期：2026-08-11
- 状态：社区讨论中
- 作者邮箱：Rosen Penev <rosenp@gmail.com>
- 概括：talitos 加密驱动的中断处理程序原先从传入的设备结构里再取回私有数据，现在改为直接把私有数据传给中断处理程序，并在需要设备指针时从私有数据中取得。这只简化了中断入口的数据获取流程，不改变中断处理行为。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260811043953.150589-1-rosenp@gmail.com/

**[SERIES] crypto: talitos - fix rename first/last to first_desc/last_desc** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-07-09
- 状态：社区讨论中
- 作者邮箱：Goetz Goerisch <ggoerisch@gmail.com>
- 概括：修复 talitos 驱动在 6.6 稳定分支上的编译错误：此前把描述符首尾字段改名时漏改一处，导致 mpc85xx 编译失败。系列先回退这两次错误回退，再按正确顺序应用上游改动，让驱动不再通过 ahash 接口的 init 指针调用自身代码，并让 SEC1 引擎把超过 32k 的哈希请求拆成多个描述符处理，避免出现超出硬件上限的失败，最后完成字段改名。
- 达到阈值的 patches（3 个，显示前 5）：
  - crypto: talitos - stop using crypto_ahash::init
  - crypto: talitos - fix SEC1 32k ahash request limitation
  - crypto: talitos - rename first/last to first_desc/last_desc
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260709193956.15619-4-ggoerisch@gmail.com/

**▸ 组织：Bootlin**（1 patches）

**[SERIES] crypto: talitos - Driver cleanup** （cover letter，15/19 个 patch 达到代码量阈值）

- 日期：2026-07-22
- 状态：社区讨论中
- 作者邮箱：Paul Louvel <paul.louvel@bootlin.com>
- 概括：对 talitos 驱动做结构整理：哈希改用块级 API 去掉软件缓冲，按功能拆分为独立文件，算法定义改用宏，初始化回调换成新接口，并用静态键区分 SEC 版本、为两代硬件分别定义描述符结构，使代码更易读，不改变硬件行为。
- 达到阈值的 patches（15 个，显示前 5）：
  - crypto: talitos/hash - Use CRYPTO_AHASH_BLOCK_ONLY API
  - crypto: talitos - Move driver into dedicated directory
  - crypto: talitos/hwrng - Move into separate file
  - crypto: talitos - Prepare crypto implementation file splitting
  - crypto: talitos/hash - Move into separate file
  - ... 及其他 10 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260722-7-1-rc1_talitos_cleanup-v4-1-81d1ed2ad911@bootlin.com/

---

### ◆ 子系统：CAAM (NXP)（2 patches）

**▸ 组织：ANSSI**（1 patches）

**crypto: caam - reject overlong RSA CRT parameters**

- 日期：2026-08-10
- 状态：社区讨论中
- 作者邮箱：Jérémy Jean <Jeremy.Jean@oss.cyber.gouv.fr>
- 概括：修复 CAAM 驱动处理 RSA 私钥 CRT 参数时的越界写：畸形密钥可提供比素数更长的参数，导致长度相减下溢并在拷贝时写出分配范围。现在在去除前导零后拒绝空或过长的参数，并按素数长度处理 qInv，同时避免全零整数越界读取。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260810154024.3178145-1-Jeremy.Jean@oss.cyber.gouv.fr/

**▸ 组织：归属待核实（nod.at）**（1 patches）

**[SERIES] crypto: caam: Fix DMA mapping leak in the cbc(paes) job path** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-07-26
- 状态：社区讨论中
- 作者邮箱：Richard Weinberger <richard@nod.at>
- 概括：修复 CAAM 受保护密钥的 CBC 加密流程中的映射泄漏：请求描述符的映射在请求结束时释放，密钥缓冲区则在加密对象初始化时映射一次、销毁时释放；补充映射失败检查和密钥长度、类型校验，清除换钥时的旧选项，并暂时拒绝尚未正确处理长度的 CCM 密钥，避免耗尽映射资源或读取残留密钥数据。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: caam: Map the paes protected key once per tfm
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260726081504.2182951-2-richard@nod.at/

---

### ◆ 子系统：AF_ALG API（1 patches）

**▸ 组织：Astra Linux**（1 patches）

**[5.10/5.15] crypto: af_alg - Set merge to zero early in af_alg_sendmsg**

- 日期：2026-07-01
- 状态：社区讨论中
- 作者邮箱：Mikhail Dmitrichenko <mdmitrichenko@astralinux.ru>
- 概括：用户态加密套接字在发送消息出错中止后，合并标志可能残留上一轮循环的无效值，下次进入发送流程时可能因无法完成的合并操作而崩溃。现在在循环开头提前将该标志清零，使出错后的下一次调用不再沿用旧状态。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260701160121.100720-1-mdmitrichenko@astralinux.ru/

---

### ◆ 子系统：ECC（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[RFC,RESEND,v6,1/1] crypto: atmel-ecc - fix multi-device use-after-free and registration races**

- 日期：2026-07-12
- 状态：社区讨论中
- 作者邮箱：Lothar Rubusch <l.rubusch@gmail.com>
- 概括：多片 Atmel ECC 设备并行初始化或快速移除再探测时，变换请求可能拿到尚未注册完成或正在解绑的 I2C 客户端指针，存在释放后使用风险；补丁引入引用计数与等待机制协调注册解绑，但超时路径仍可能遗留活跃变换，方案尚在讨论。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260712200203.47764-1-l.rubusch@gmail.com/

---

### ◆ 子系统：CESA (Marvell)（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: cesa: check for sram_dma NULL**

- 日期：2026-07-13
- 状态：社区讨论中
- 作者邮箱：Rosen Penev <rosenp@gmail.com>
- 概括：Marvell CESA 加密驱动在释放 SRAM 时，若此前 DMA 资源映射失败，仍会调用解除映射，可能触发错误；现在仅在映射成功时才解除映射，避免对无效地址操作。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260713050740.3687230-1-rosenp@gmail.com/

---

### ◆ 子系统：Kerberos（1 patches）

**▸ 组织：Kylin**（1 patches）

**crypto: krb5 - Use constant-time checksum comparison**

- 日期：2026-07-20
- 状态：社区讨论中
- 作者邮箱：Jiangshan Yi <yijiangshan@kylinos.cn>
- 概括：Kerberos 的 MIC 校验和比较使用普通内存比较，耗时随首个不同字节位置变化，可能被用来逐字节伪造校验和。现改为恒定时间比较，与同一子系统其他校验和比较方式一致，并补充了所需头文件引用。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260720031304.198172-1-yijiangshan@kylinos.cn/

---

### ◆ 子系统：Asymmetric Keys（1 patches）

**▸ 组织：ANSSI**（1 patches）

**crypto: asymmetric_keys: copy X.509 TBS for data signature algorithms**

- 日期：2026-08-21
- 状态：社区讨论中
- 作者邮箱：Jérémy Jean <Jeremy.Jean@oss.cyber.gouv.fr>
- 概括：对直接处理消息而非摘要的签名算法，X.509 证书解析曾让签名对象直接指向系统调用返回后即被释放的证书数据，后续把密钥链接进受限密钥环时可能访问已释放内存并导致验签使用被复用的数据；现在签名对象改为持有该数据的独立副本，并在释放时一并回收。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260821192502.3942767-2-Jeremy.Jean@oss.cyber.gouv.fr/

---

### ◆ 子系统：Skcipher（1 patches）

**▸ 组织：Kylin**（1 patches）

**crypto: mxs-dcp: handle zero-length skcipher requests**

- 日期：2026-08-28
- 状态：社区讨论中
- 作者邮箱：Linmao Li <lilinmao@kylinos.cn>
- 概括：MXS-DCP 加密驱动对长度为零的对称加密请求本应是无操作，却仍将其排队，导致 CBC 完成路径在更新 IV 时发生无符号下溢，解密时源地址越界到输入缓冲区之前；现在在入队前直接返回成功，避免非法访问并保持 IV 不变。
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
- **组织归类**：按完整邮箱域名及其子域名识别企业、高校和社区；公共邮箱归为 Individual Contributor，未知域名单独标为归属待核实，不推断雇主

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

*报告由 Linux Patches Tracker 自动生成 | 2026-09-11 18:20:17*
