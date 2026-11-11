# Linux Crypto 子系统 Patch 追踪报告

---

## 报告信息

| 项目 | 内容 |
|------|------|
| 数据来源 | patchwork.kernel.org |
| 生成日期 | 2026-11-11 |
| 报告区间 | 2026-09-01 至 2026-10-31 |
| 仓库 | [https://github.com/IAMHCHCH/linux-patches-tracker](https://github.com/IAMHCHCH/linux-patches-tracker) |

---

## 统计概览

### 按状态分类

| 状态 | 数量 | 占比 |
|------|------|------|
| 社区讨论中 | 55 | 43.0% |
| 已合入 | 60 | 46.9% |
| 已关闭 | 13 | 10.2% |
| **总计** | **128** | **100%** |

### 按组织分类（TOP 15）

| 组织 | 数量 | 占比 |
|------|------|------|
| Kernel.org | 36 | 28.1% |
| Individual Contributor | 29 | 22.7% |
| Intel | 7 | 5.5% |
| 归属待核实（gondor.apana.org.au） | 6 | 4.7% |
| Qualcomm | 5 | 3.9% |
| AMD | 4 | 3.1% |
| 归属待核实（free.fr） | 4 | 3.1% |
| Texas Instruments | 3 | 2.3% |
| Infradead Community | 2 | 1.6% |
| StarFive | 2 | 1.6% |
| 东南大学 | 2 | 1.6% |
| 归属待核实（mandelbit.com） | 2 | 1.6% |
| Rambus | 2 | 1.6% |
| Huawei | 2 | 1.6% |
| 归属待核实（genproof.com） | 2 | 1.6% |

### 按子系统分类

| 子系统 | 数量 | 占比 |
|--------|------|------|
| General Crypto | 73 | 57.0% |
| HWRNG | 22 | 17.2% |
| CAAM (NXP) | 7 | 5.5% |
| ECC | 5 | 3.9% |
| Skcipher | 5 | 3.9% |
| Talitos | 3 | 2.3% |
| CCP/SEV (AMD) | 2 | 1.6% |
| Aead | 2 | 1.6% |
| JitterEntropy | 1 | 0.8% |
| Authenc | 1 | 0.8% |
| TCrypt | 1 | 0.8% |
| AF_ALG API | 1 | 0.8% |
| Public Key | 1 | 0.8% |
| ICE (Qualcomm) | 1 | 0.8% |
| SPAcc | 1 | 0.8% |
| CESA (Marvell) | 1 | 0.8% |
| DRBG | 1 | 0.8% |

## 重点 Patch Top20 清单

### 已合入

| 厂商 | 影响力 | 简介 |
|------|------|------|
| Red Hat | 高（75） | [PATCH v4 00/13] libcrypto: Provide more __cleanup functions for zeroizing data ------为内核加密库中的 AES、SHA2、BLAKE2、SM3 等算法的密钥和上下文结构新增类型化的自动清零辅助函数，调用方可借助作用域退出自动擦除敏感数据，替换原先手工清除调用；同时补充统一文档说明敏感参数清零约定，并将可信密钥等调用点改为使用新接口，减少因遗漏清除而将密钥或中间状态残留在栈上的可能。 |
| Kernel.org | 中（74） | [PATCH v2 00/20] Migrate x86 and RISC-V accelerated AES modes into library ------将 x86 和 RISC-V 上原有的 AES 工作模式架构加速代码迁入内核加密库，使库提供 CBC、CTR、XTS 等路径直接使用 AES-NI 或 RISC-V 优化实现；同时调整传统加密 API 中的优先级并移除已被取代的对称加密算法实现，避免库算法在模板组合中被慢速通用代码错误替换，保证原有加速性能不被回退，并清理迁移过程中的汇编实现。 |
| Kernel.org | 中（72） | [PATCH v1 00/14] crypto: Remove the unnecessary crypto_rng API ------移除内核随机数生成路径中泛化的随机数算法抽象，改为让 DRBG 和抖动熵源直接以库接口提供随机字节；标准随机数接口不再经过该抽象，网络随机数接口改用库函数，相关的自适应测试改为在首次使用时或模块初始化时执行。结果是删除一整套已无用户的随机数算法类型及支持，简化随机数生成调用链，并调整抖动熵源健康检查时机，避免未使用时开机即执行昂贵检查。 |
| 归属待核实（itx.no） | 中（63） | [v3] lib/crypto: sparc/aes-xts: Add optimization using the AES opcodes ------为 SPARC 平台利用 AES 操作码实现 XTS 加密解密的架构加速路径，支持 AES-128 和 AES-256、每轮处理两个块，AES-192 和非 8 字节对齐数据回退到通用实现；原先 SPARC 被禁止注册库 XTS 算法，现已允许注册并将优先级调整到与 x86、RISC-V 相同，使 dm-crypt 等场景顺序读写性能明显提高。 |
| Kernel.org | 中（61） | [PATCH] lib/crypto: powerpc/poly1305: Remove BROKEN implementation ------删除 PowerPC 上已标记为不可用的 Poly1305 加速实现。该实现原有不能在软中断上下文使用的问题，进一步检查发现汇编中进位归约丢失进位、最终更新错误假设以及输出时存在依赖秘密值的分支，部分输入会算出错误结果；因此直接移除，让相关平台使用通用 Poly1305，后续若要重新引入需先修正这些缺陷。 |
| Kernel.org | 中（61） | [PATCH] crypto: x86/aria - Take the address of each asm function in one file ------调整 x86 ARIA 各层汇编实现的地址取用方式，把 AVX 16 路和 AVX2 32 路操作表填充集中到拥有对应汇编函数的模块，避免在 Clang 全链接优化与控制流完整性保护下，多个目标文件取同一汇编符号地址时链接器错误丢弃符号，导致模块链接失败；属于为早期 Clang 构建问题的兼容性调整。 |
| Kernel.org | 中（59） | [PATCH v1 00/3] AES library fixups ------修复 AES 库实现中 CBC 加密函数未显式设置某寄存器别名而依赖前序调用残留的问题；提高 x86 上库提供的 AES 模式优先级，避免 CCP 和 PadLock 等驱动反而覆盖 AES-NI 或 VAES 优化代码；同时为旧 AES-NI 配置增加过渡性选择，保证启用该选项的系统仍能获得 LUKS 和 dm-crypt 启动所需算法。 |
| Intel | 中（58） | [PATCH v1 00/2] crypto: qat - fix config table locking ------修复 QAT 配置表并发访问缺陷：原先在未持有每设备锁时遍历配置段，或调试文件读取使用不匹配的全局锁，并发删除或更新键值可能释放正在访问的节点，造成释放后使用；现在在查找、插入及调试文件读取路径加每设备读写锁，并去掉旧全局锁。此外在添加键值时直接定位现有项，避免两次重复遍历和临时拷贝，流程不变。 |
| Kernel.org | 中（54） | [PATCH v1 00/2] lib/crypto: Use size_t lengths for Poly1305 and ChaCha ------将 Poly1305 和 ChaCha 的缓冲区长度参数从 32 位类型改为平台宽度类型，与密码库其他接口保持一致；同时修正部分 64 位架构汇编中高位未定义或符号扩展带来的潜在错误，并消除长度计算在极端输入下溢出的可能。由于当前调用者不会传入超过 32 位的长度，这属于接口健壮性改进，无实际功能变化。 |
| Kernel.org | 中（54） | [PATCH] crypto: sa2ul - Fix HMAC key preparation ------SA2UL 加密驱动在准备 HMAC 密钥时，SHA-256 路径因状态结构大小变化导致一字节越界写入，且超过 64 字节的 HMAC 密钥从未被正确处理。现改为复用内核密码库来生成内外哈希状态，移除间接调用，从而消除越界并让长密钥可用于相应摘要算法。 |
| Kernel.org | 中（52） | [PATCH v1 00/3] lib/crypto: x86/sha: Follow the normal %rbp convention ------x86 平台上 SHA-1、SHA-256 和 SHA-512 的汇编实现原先先保存被调用者寄存器再建立帧指针，违反常规调用约定，导致启用帧指针回溯时这些函数内的调用栈不可靠，回退为扫描整个栈并出现问号项。现调整入口和退出顺序，遵循常规帧指针约定，使调用栈能可靠生成。 |
| Individual Contributor | 中（51） | [v2] crypto: qat - zero the VF migration state buffer on save ------QAT 虚拟功能迁移状态缓冲区在内核堆中分配，保存状态时会向用户态暴露整个缓冲区，但只写入已序列化段，未使用的尾部保持原样，因此首次保存可能泄露堆旧内容，后续保存也可能泄露之前迁移残留数据。现在在写入设置数据前清零整个缓冲区，并在每次保存前保留设置数据、清零剩余状态区域，避免未初始化或旧数据暴露。 |
| Huawei | 中（50） | [6/7] crypto: hisilicon/hpre - extract clusters num into inline function ------华为 HPRE 加速器驱动中有多处重复从设备能力信息提取集群数量的逻辑。本次将这些重复片段统一到一个内联辅助函数中，后续设置集群、时钟门控、计数清零和调试信息初始化都调用该辅助函数，减少重复代码且不改变原有行为。 |
| Intel | 中（48） | [1/2] crypto: qat - initialise state_lock on every path in adf_devmgr_add_dev() ------QAT 驱动在设备加入时状态锁原先只在末尾初始化，而已存在标识映射的主机绑定虚拟功能会提前返回，导致每次在这些地址重建虚拟功能时锁保持零值，后续上下电使用未初始化互斥锁，在开启锁调试时会触发警告。现把状态锁初始化移到每设备状态设置处，使所有路径都完成初始化，避免使用未初始化的锁。 |
| Kernel.org | 中（47） | [PATCH v1 00/3] crypto: atmel-tdes - use separate DMA scatterlists ------对Atmel TDES驱动进行清理：将输入输出DMA散列表改为独立变量，直接使用4字节总线宽度，复用已有快速判断，并合并DMA初始化错误路径的释放，减少重复代码和出错可能。 |
| Infradead Community | 中（47） | [v2] crypto: ccp: psp-sev.h: clean up kernel-doc warnings ------清理 AMD 安全处理器接口头文件中的内核文档注释，修正两个头文件里结构体成员缺失或多余说明、结构体名称与实际定义不符以及枚举注释格式不当等问题，补全保留字段并更正字段描述，消除文档生成警告，使接口说明与结构定义一致。 |
| 归属待核实（free.fr） | 中（47） | [v2] crypto: caam/qi2 - lower the algorithm priority ------为CAAM/qi2加密驱动把默认算法优先级从2000降到100，避免它默认压制其他实现；用户仍可通过内核加密接口按需调高优先级，硬件也能继续按驱动名被调用。 |
| Individual Contributor | 低（45） | [v4] crypto: talitos: init tasklets before requesting IRQs ------修复talitos驱动支持第二个中断后先请求中断再初始化任务队列的顺序问题，避免引导加载器或kexec残留中断导致调度空回调；现在先完成队列初始化和设备复位再请求中断，并修正移除时对未请求中断号的释放。 |
| Individual Contributor | 低（45） | [v4] crypto/amlogic: Use devm APIs for clock management ------将Amlogic GXL加密驱动改为使用设备管理的时钟获取并启用接口，由内核自动处理时钟禁用，删除手动清理代码，简化探测流程并减少错误路径遗漏。 |
| Kernel.org | 低（37） | [PATCH v1 00/2] hwrng: virtio - use min() in copy_data() ------virtio 硬件随机数驱动中，设备名称原先用无目标长度限制的字符串格式化构造，虽然当前索引范围不会越界，但改为限定目标缓冲区长度，避免后续改动引入溢出；同时将可用数据长度计算中的带类型转换的较小值宏替换为更直接的较小值比较，行为保持不变。 |

### 社区讨论

| 厂商 | 影响力 | 简介 |
|------|------|------|
| Rambus | 高（78） | [PATCH v5 00/19] crypto: cmh - add Rambus CryptoManager Hub driver ------为Rambus CryptoManager Hub硬件加密加速器新增驱动，实现平台探测、邮箱队列和DMA管理，注册对称、哈希、认证、公钥及后量子等算法，并提供专用字符设备处理硬件密钥生命周期及内核加密API无法表达的密钥操作。 |
| Bootlin | 中（69） | [PATCH v8 00/20] crypto: talitos - Driver cleanup ------对talitos驱动进行结构重构，将原单文件按哈希、对称加密、认证加密和随机数等功能拆分，用宏简化算法注册，改用类型专用初始化接口，并区分不同SEC版本的描述符结构，使代码组织更清晰、减少重复。 |
| Kernel.org | 中（67） | [PATCH v5 00/8] x86: Remove cpu_has_xfeatures() and add AVX-512 xor_gen() ------在x86和用户模式Linux启动时检查AVX及AVX-512对应的扩展状态位，若缺失则清除相应特性标志；随后从x86加密与库代码中移除对扩展状态位的重复检查，并新增AVX-512异或生成实现，用于加速RAID等多磁盘异或运算，在部分服务器和客户端处理器上提升吞吐。 |
| Texas Instruments | 中（62） | [PATCH v10 00/15] Fix several issues in DTHEv2 driver ------修复德州仪器DTHEv2驱动的多处缺陷，包括空设备列表误判、锁不一致、高内存页地址错误、设备数据释放后仍被使用、散列表长度超出导致DMA等待超时，以及认证标签操作与缓存失效顺序问题，避免空指针、内存破坏和错误结果。 |
| Vayavya Labs | 中（61） | [PATCH v27 00/4] crypto: spacc - Add SPAcc Crypto Driver ------为Synopsys SPAcc硬件加密引擎添加驱动，增加MD5、SHA系列、SHA3、HMAC及SM4的CMAC/XCBC等哈希和认证算法支持，并提供自动检测功能，使内核能够根据硬件配置注册可用算法。 |
| AMD | 中（61） | [PATCH v5 00/7] Implement SNP live firmware update support ------为 AMD SEV-SNP 平台新增固件在线更新：通过系统固件上传接口接收镜像并调用专用下载命令更新，更新期间 SNP 客户机不受影响；传统 SEV 若正在运行则返回繁忙拒绝，若已初始化则先关闭并释放固件缓冲区，更新后再恢复。镜像先暂存，由管理员提交后才永久生效，也可回滚。配套调整固件加载器的模块引用和父设备固定，确保注销时所有上传操作已结束。 |
| Texas Instruments | 中（58） | [PATCH v9 00/2] Add support for hashing algorithms in TI DTHE V2 ------为德州仪器 DTHE V2 硬件加密引擎的哈希单元加入 SHA-224、SHA-256、SHA-384 和 SHA-512 算法支持，使这些摘要计算可卸载到该硬件；随后又加入对应的 HMAC-SHA512/384/256/224 认证算法，让基于 SHA-2 的消息认证也能由硬件完成，适合需要批量摘要和完整性校验的嵌入式场景。 |
| Qualcomm | 中（58） | [PATCH v12 00/4] crypto: qce - fix self-test issues in skcipher ------修复高通加密引擎对称加密自测试失败：AES-XTS短于一个块的消息直接返回参数错误，避免硬件停滞；AES-CTR最后一块不完整或负载分散在多个散列表项时改用软件回退；对XTS弱密钥，在非FIPS模式下改用软件回退而非直接拒绝，FIPS模式下则返回参数错误。 |
| Qualcomm | 中（57） | [PATCH v12 00/3] crypto - qce: fix self-test issues in aead ------修复高通加密引擎AEAD自测试失败：将每次请求的软件回退判断从共享变换上下文改为局部变量，避免并发请求互相覆盖标志；对CCM模式中长度非块对齐或负载分散在多个散列表项的情况强制走软件回退，防止硬件引擎因等待完整输入而停滞。 |
| 浙江大学 | 中（55） | [v2] crypto: ccp - Fix use-after-free in backlog cmd advancement ------修复 CCP 加密设备驱动中可延后命令从积压队列提升后短暂脱离链表引发的释放后使用：销毁设备时无法冲刷该命令，工作队列可能在设备释放后访问并唤醒已停止的内核线程；同时并发提交可能抢占预留位置，使命令计数超过上限。现在在出队时于同一锁内把空槽直接转移给积压命令原子预留，并在内核线程中执行回调后再入队，销毁前标记停用并抑制唤醒。 |
| Kernel.org | 中（54） | [PATCH] crypto: arc4 - Remove obsolete crypto API support for ARC4 ------删除内核中已过时的 ARC4 加密 API 包装器，仅保留供某些遗留协议直接调用的 ARC4 库实现。此前所有内核用户都已使用库接口，用户态无线守护进程也已改用用户空间 ARC4，该 API 已废弃警告六年，并默认不在用户态算法接口允许列表中，因此不再需要保留这一不安全算法的密码 API 入口。 |
| 归属待核实（ptudor.net） | 中（53） | [PATCH v1 00/3] hwrng: add Microchip RNG90 support ------为 I2C 接口的 Microchip RNG90 加密随机数发生器新增硬件随机数驱动，负责唤醒和识别设备、封装信息与随机数命令、在限定时间内轮询执行、校验响应长度和循环冗余校验，并在健康或自检失败时丢弃不合格输出。默认采用最小非零熵估计，管理员可在平台验证后调高。附带 KUnit 测试通过脚本化 I2C 适配器覆盖命令帧、恢复和健康失败等场景。 |
| Texas Instruments | 中（52） | [PATCH v1 00/30] Clean and improve SA2UL driver ------德州仪器 SA2UL 加密卸载引擎系列清理：移除未使用字段、死代码和冗余包装；修正初始化失败及请求执行路径中的安全上下文、哈希对象和 DMA 映射泄漏，释放安全上下文前擦除密钥材料；修复并发设置密钥可能破坏在途命令标签、哈希状态导出缓冲区过小导致内核栈越界；请求改由内核加密引擎统一调度，并为支持 AES-CM 的新硬件变体增加真随机数发生器启动准备。 |
| 归属待核实（mandelbit.com） | 中（51） | [PATCH v1 00/2] lib/crypto: x86/chacha: Add 16-block AVX-512 implementation ------为 x86 平台的 ChaCha 流密码库新增一次处理 16 个分组的 AVX-512 实现，输入超过 8 个分组时使用，尾部仍由现有实现完成；对会因 512 位寄存器而降频的处理器则自动避免该路径。AMD Zen 5 测试中，1KB 和 4KB 数据的加密吞吐从约 5.2GB/s 提升到约 10.2GB/s。附带架构无关的 KUnit 测试，覆盖标准向量、不同长度、对齐、页边界和多次调用。 |
| Intel | 中（50） | [PATCH] crypto: qat - add support for enhanced decompression mode on GEN6 devices ------为 Intel QAT 第六代设备新增增强解压模式：固件可让压缩引擎内嵌的解压单元直接处理解压请求，绕开压缩与翻译阶段，从而在并发压缩的同时提高解压吞吐。该模式通过设备属性接口开关控制，设置会持久化并在设备重新上下线或服务配置变化后重新应用；当只配置独立解压服务而未配置压缩服务时默认启用，并相应调整解压环对到压缩引擎的线程映射。 |
| 归属待核实（gondor.apana.org.au） | 中（48） | [PATCH] crypto: caam - Remove public key support ------CAAM驱动因长期无人维护且存在严重缺陷，现整体移除其公钥加密支持及相关源码文件，使该驱动不再提供公钥加密算法，防止这些未修复的缺陷被继续使用。 |
| Amazon | 中（46） | [PATCH v6 00/6] crypto: skcipher - multi-data-unit request splitting ------为对称加密请求增加多数据单元能力：调用方可一次提交多个单元，API层对不支持原生多单元的算法自动逐单元处理并按64位小端计数器推进初始向量，保证与逐单元调用结果逐字节一致；dm-crypt将连续bio段内的扇区合并为一个请求，减少逐扇区调用，但异步算法只有在原生支持时才批量。 |
| 归属待核实（gondor.apana.org.au） | 低（45） | [PATCH] crypto: aes - Add import_core/export_core to cmac/xcbc/cbcmac ------为内核AES库的CMAC、XCBC和CBCMAC实现补充状态导出与导入接口，使其导出格式与通用消息认证码模板对齐；其中CMAC和XCBC在导出前对暂存块再执行一次加密，避免状态丢失，保证状态序列化后能正确恢复。 |
| Individual Contributor | 低（45） | [PATCH] crypto: jitterentropy - add fast hardware jitter mixer extension ------为抖动熵子系统新增一个硬件抖动混合器扩展，利用高精度周期计数器和内存指针访问来扰动分支预测单元与硬件预取器，声称通过执行时间变化产生架构级微熵，且不依赖浮点运算；已在x86架构上测试。 |
| NXP | 低（44） | [RFC,4/4] crypto: remove async_tx framework ------在md/raid5已改用同步操作后，移除不再有使用者的异步传输框架及其接口文档，删除相关API和实现文件，移除对异步内存复制、异或校验等操作链的抽象。 |

---

## 已合入 Patches

### ◆ 子系统：General Crypto（33 patches）

**▸ 组织：Kernel.org**（15 patches）

**lib/crypto: powerpc/poly1305: Remove BROKEN implementation**

- 日期：2026-10-29
- 状态：已合入
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：删除 PowerPC 上已标记为不可用的 Poly1305 加速实现。该实现原有不能在软中断上下文使用的问题，进一步检查发现汇编中进位归约丢失进位、最终更新错误假设以及输出时存在依赖秘密值的分支，部分输入会算出错误结果；因此直接移除，让相关平台使用通用 Poly1305，后续若要重新引入需先修正这些缺陷。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261029063522.124421-1-ebiggers@kernel.org/

**[SERIES] lib/crypto: mldsa: Address some minor nits** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-10-29
- 状态：已合入
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：针对内核新增的 ML-DSA 后量子签名验证代码做三处小修正：当调用方传入长度不正确的公钥时，原来可能在确认长度前就计算公钥内部偏移，属于标准未定义行为，现改为先校验再取偏移；同时显式检查算法编号是否有效，无效时直接返回参数错误，避免依赖编译器对枚举范围的保证；并为签名验证函数加上返回值必须检查的声明。这些改动与现有调用方行为一致，只让边界输入处理更规范，不改变正常验证流程。
- 达到阈值的 patches（2 个，显示前 5）：
  - lib/crypto: mldsa: Check pk_len before doing pointer arithmetic
  - lib/crypto: mldsa: Explicitly check that 'alg' is a valid value
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261029054534.68481-2-ebiggers@kernel.org/

**lib/crypto: mips: Disable Octeon SHA code on little-endian kernels**

- 日期：2026-10-22
- 状态：已合入
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：针对 MIPS64 架构的 Cavium Octeon 处理器，小端构建内核原本启用基于协处理器的 SHA-1、SHA-256 和 SHA-512 加速代码，但该代码在小端字节序下存在字节序处理错误，无法正确计算哈希值，大端不受影响。现在仅在大端 Octeon 内核默认启用这些硬件哈希加速，小端内核改用其他实现，避免产生错误哈希结果。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261022054450.20746-1-ebiggers@kernel.org/

**[SERIES] lib/crypto: Use size_t lengths for Poly1305 and ChaCha** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-10-14
- 状态：已合入
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：将 Poly1305 和 ChaCha 的缓冲区长度参数从 32 位类型改为平台宽度类型，与密码库其他接口保持一致；同时修正部分 64 位架构汇编中高位未定义或符号扩展带来的潜在错误，并消除长度计算在极端输入下溢出的可能。由于当前调用者不会传入超过 32 位的长度，这属于接口健壮性改进，无实际功能变化。
- 达到阈值的 patches（2 个，显示前 5）：
  - lib/crypto: poly1305: Use size_t length
  - lib/crypto: chacha: Use size_t length
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261014152604.323310-2-ebiggers@kernel.org/

**crypto: x86/aria - Take the address of each asm function in one file**

- 日期：2026-10-12
- 状态：已合入
- 作者邮箱：Kees Cook <kees@kernel.org>
- 概括：调整 x86 ARIA 各层汇编实现的地址取用方式，把 AVX 16 路和 AVX2 32 路操作表填充集中到拥有对应汇编函数的模块，避免在 Clang 全链接优化与控制流完整性保护下，多个目标文件取同一汇编符号地址时链接器错误丢弃符号，导致模块链接失败；属于为早期 Clang 构建问题的兼容性调整。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261012031920.i.329-kees@kernel.org/

**[SERIES] crypto: atmel-tdes - use separate DMA scatterlists** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-10-11
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：Atmel TDES 加密驱动将 DMA 输入和输出散列表从数组合并形式拆成两个独立散列表，并直接指定四字节总线宽度；启动加密时复用已判断的快速标志，DMA 初始化出错时合并处理路径，申请到输入通道后再申请输出通道失败会直接释放输入通道。属于接口清理，不改变算法行为。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: atmel-tdes - use separate DMA scatterlists
  - crypto: atmel-tdes - reuse fast in atmel_tdes_crypt_start()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261011131556.272382-4-blum@kernel.org/

**[SERIES] lib/crypto: x86/sha: Follow the normal %rbp convention** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-10-11
- 状态：已合入
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：x86 平台上 SHA-1、SHA-256 和 SHA-512 的汇编实现原先先保存被调用者寄存器再建立帧指针，违反常规调用约定，导致启用帧指针回溯时这些函数内的调用栈不可靠，回退为扫描整个栈并出现问号项。现调整入口和退出顺序，遵循常规帧指针约定，使调用栈能可靠生成。
- 达到阈值的 patches（3 个，显示前 5）：
  - lib/crypto: x86/sha1: Follow the normal %rbp convention
  - lib/crypto: x86/sha256: Follow the normal %rbp convention
  - lib/crypto: x86/sha512: Follow the normal %rbp convention
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261011134843.166585-2-ebiggers@kernel.org/

**lib/crypto: poly1305: Use memzero_explicit() in poly1305_final()**

- 日期：2026-10-06
- 状态：已合入
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：在 Poly1305 消息认证码完成函数输出摘要后，原先用普通空结构体赋值清除描述上下文，该清零在链接时优化中理论上可能被消除；现改为显式清零，确保密钥和内部状态确实被清除，降低密钥材料残留风险。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261006083432.16328-1-ebiggers@kernel.org/

**[SERIES] AES library fixups** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-09-30
- 状态：已合入
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：修正 x86 AES-NI 库中 CBC 加密对临时寄存器别名的隐式依赖，避免偶然复用前一函数状态；并将库内 AES 模式优先级提升到高于 CCP 和 PadLock 驱动，防止较慢硬件加速覆盖 AES-NI/VAES 实现；同时让原有 AES-NI 选项自动选中必要的模式选项，确保仅启用该选项的系统仍能引导 LUKS/dm-crypt。
- 达到阈值的 patches（2 个，显示前 5）：
  - lib/crypto: x86/aes: Set RNDKEY in aes_cbc_encrypt_aesni()
  - crypto: aes - Boost priority of encryption modes further
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260930170542.140403-2-ebiggers@kernel.org/

**[SERIES] Migrate x86 and RISC-V accelerated AES modes into library** （cover letter，15/19 个 patch 达到代码量阈值）

- 日期：2026-09-27
- 状态：已合入
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：将 x86 的 AES-NI 和 RISC-V 上的 AES 模式加速实现迁移到通用加密库，使 ECB、CBC、CTR、XTS 等模式通过库接口直接获得优化代码，并删除被取代的架构专用实现；同时调整算法优先级，避免如 CCM 等复合模式因模板实例化而意外回退到较慢的通用 AES。
- 达到阈值的 patches（15 个，显示前 5）：
  - lib/crypto: aes-xctr: Pass counter by value to aes_xctr_arch()
  - lib/crypto: x86/aes: Clean up aes-aesni.S in preparation for AES modes
  - lib/crypto: x86/aes-cbc: Add AES-NI optimization
  - lib/crypto: x86/aes-ctr: Add AES-NI optimization
  - lib/crypto: x86/aes-xts: Add AES-NI optimization
  - ... 及其他 10 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260927224418.109759-3-ebiggers@kernel.org/

**crypto: sa2ul - Fix HMAC key preparation**

- 日期：2026-09-23
- 状态：已合入
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：SA2UL 加密驱动在准备 HMAC 密钥时，SHA-256 路径因状态结构大小变化导致一字节越界写入，且超过 64 字节的 HMAC 密钥从未被正确处理。现改为复用内核密码库来生成内外哈希状态，移除间接调用，从而消除越界并让长密钥可用于相应摘要算法。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260923051116.92741-1-ebiggers@kernel.org/

**[SERIES] crypto: cast5 - use memcpy_and_pad() in cast5_setkey()** （cover letter，5/5 个 patch 达到代码量阈值）

- 日期：2026-09-21
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：在 CAST5、CAST6 算法及 IXP4XX、OcteonTX/OcteonTX2 加速驱动中，把密钥或 HMAC 填充区原先先复制再清零的两步操作统一替换为内存复制并填充的单一调用，简化初始化流程，不改变功能。
- 达到阈值的 patches（5 个，显示前 5）：
  - crypto: cast5 - use memcpy_and_pad() in cast5_setkey()
  - crypto: cast6 - use memcpy_and_pad() in __cast6_setkey()
  - crypto: ixp4xx - use memcpy_and_pad() in register_chain_var()
  - crypto: octeontx - use memcpy_and_pad() in aead_hmac_init()
  - crypto: octeontx2 - use memcpy_and_pad() in aead_hmac_init()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260921061120.29694-6-blum@kernel.org/

**crypto: atmel-tdes - consolidate transfer setup**

- 日期：2026-09-16
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：Atmel TDES 加密驱动中两条传输路径原先各自保存传输长度并同步反弹缓冲区，存在重复设置；本次将这段共同逻辑上移到统一的传输启动流程，两条路径改为从设备结构读取长度，使传输准备代码集中、调用参数减少，属于流程重构。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260916171659.129009-3-blum@kernel.org/

**crypto: xilinx - clear AES key buffer before freeing it**

- 日期：2026-09-08
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：Xilinx ZynqMP AES-GCM 驱动在退出加密上下文时，原先直接释放 AES 密钥缓冲区，密钥内容可能残留在内存中。现在释放前先清零缓冲区，避免密钥材料在使用后继续留在内存里。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260908191607.405177-2-blum@kernel.org/

**crypto: atmel-tdes - simplify DMA buffer initialization**

- 日期：2026-09-03
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：Atmel TDES 驱动的 DMA 缓冲区初始化原先分散计算长度并多次跳转处理映射错误，输出缓冲区映射失败时也需要单独解除输入映射。现在一次计算缓冲区长度，合并公共错误路径，失败时先解除已映射的输入缓冲区并返回内存不足，同时用错误级别日志记录，流程更简洁。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260903210845.162790-2-blum@kernel.org/

**▸ 组织：Individual Contributor**（7 patches）

**[v3] lib/crypto: chacha20poly1305: zeroize state in __chacha20poly1305_decrypt**

- 日期：2026-10-05
- 状态：已合入
- 作者邮箱：Mohamad Raizudeen <raizudeen.kerneldev@gmail.com>
- 概括：在 ChaCha20-Poly1305 解密路径中，原先底层辅助函数不清理加密状态，扩展随机数变体直接返回结果，派生的 ChaCha20 密钥材料可能残留在栈上；现在把状态清零移入底层辅助函数，使所有解密入口都能在返回前清除自身状态，同时把输入长度检查提前到调用者，避免无效输入时初始化状态。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261005150324.5621-1-raizudeen.kerneldev@gmail.com/

**[SERIES] crypto: Use pm_runtime_resume_and_get()** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-09-22
- 状态：已合入
- 作者邮箱：Bui Duc Phuc <phucduc.bui@gmail.com>
- 概括：在 Sun8i SS、CCREE 和 SL3516 密码加速驱动中，把恢复设备运行时电源并获取引用的旧式手动错误处理改为使用内核提供的合并接口，失败时自动释放多余引用，简化流程且无功能变化。
- 达到阈值的 patches（3 个，显示前 5）：
  - crypto: sun8i-ss - Use pm_runtime_resume_and_get()
  - crypto: ccree - Use pm_runtime_resume_and_get()
  - crypto: sl3516 - Use pm_runtime_resume_and_get()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260922031954.320895-2-phucduc.bui@gmail.com/

**crypto: ccp: kill v3 IRQ tasklet during teardown**

- 日期：2026-09-20
- 状态：已合入
- 作者邮箱：Jiale Yao <yaojiale02@163.com>
- 概括：针对 AMD CCP v3 设备使用 MSI-X 时，中断处理会调度小任务；原先拆除路径只释放中断而不排空已排队的小任务，可能导致其在设备管理分配释放后继续访问 CCP 结构。现在在初始化错误路径和销毁过程中，释放中断后都终止该小任务，避免这种释放后访问。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260920173407.2126086-1-yaojiale02@163.com/

**crypto: ccp: kill v5 IRQ tasklet during teardown**

- 日期：2026-09-20
- 状态：已合入
- 作者邮箱：Jiale Yao <yaojiale02@163.com>
- 概括：针对 AMD CCP v5 设备使用 MSI-X 时，中断处理会调度小任务；原先拆除路径只释放中断而不排空已排队的小任务，可能导致其在设备管理分配释放后继续访问 CCP 结构。现在在初始化错误路径和销毁过程中，释放中断后都终止该小任务，避免这种释放后访问。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260920173417.2126346-1-yaojiale02@163.com/

**[v2] crypto: qat - zero the VF migration state buffer on save**

- 日期：2026-09-19
- 状态：已合入
- 作者邮箱：Karl Mehltretter <kmehltretter@gmail.com>
- 概括：QAT 虚拟功能迁移状态缓冲区在内核堆中分配，保存状态时会向用户态暴露整个缓冲区，但只写入已序列化段，未使用的尾部保持原样，因此首次保存可能泄露堆旧内容，后续保存也可能泄露之前迁移残留数据。现在在写入设置数据前清零整个缓冲区，并在每次保存前保留设置数据、清零剩余状态区域，避免未初始化或旧数据暴露。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260919054934.27322-1-kmehltretter@gmail.com/

**[v4] crypto/amlogic: Use devm APIs for clock management**

- 日期：2026-09-16
- 状态：已合入
- 作者邮箱：Mohamad Raizudeen <raizudeen.kerneldev@gmail.com>
- 概括：将Amlogic GXL加密驱动改为使用设备管理的时钟获取并启用接口，由内核自动处理时钟禁用，删除手动清理代码，简化探测流程并减少错误路径遗漏。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260916174227.5581-1-raizudeen.kerneldev@gmail.com/

**crypto: amcc: trng: use int for ppc4xx_trng_probe()**

- 日期：2026-09-04
- 状态：已合入
- 作者邮箱：Rosen Penev <rosenp@gmail.com>
- 概括：AMCC PPC4xx 加密驱动中的硬件随机数发生器探测原先不向主探测返回错误，无法在初始化失败时回滚；现在让其返回结果，主探测检查失败后会注销已注册的算法，使可选随机数功能初始化失败能被正确传导和清理。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260904230144.127071-1-rosenp@gmail.com/

**▸ 组织：Intel**（3 patches）

**[SERIES] crypto: qat - fix mutex lifetimes in the device manager** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-10-06
- 状态：已合入
- 作者邮箱：Ahsan Atta <ahsan.atta@intel.com>
- 概括：英特尔 QAT 设备管理器修正互斥锁生命周期：将状态锁初始化提前到所有返回路径之前，避免虚拟功能重建时复用已有映射却未初始化锁；把虚拟功能到物理功能的通知锁改为与加速设备同生命周期，在设备关闭后发送重启完成消息时仍可用，消除使用未初始化或已销毁锁的调试告警。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: qat - initialise state_lock on every path in adf_devmgr_add_dev()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261006150649.2517748-2-ahsan.atta@intel.com/

**crypto: qat - force an edge when re-enabling all VF2PF interrupts**

- 日期：2026-09-29
- 状态：已合入
- 作者邮箱：George Abraham P <george.abraham.p@intel.com>
- 概括：在 QAT 设备重置或高级错误恢复后，VF 到 PF 的中断源可能已锁存，而功能级复位把屏蔽寄存器置为默认未屏蔽，导致再次使能时没有屏蔽到未屏蔽的边沿，锁存消息无法投递。现在使能全部 VF 到 PF 中断前先整体屏蔽再立即解屏蔽，强制产生边沿，使设备重置后存活虚拟功能发出的通知能够送达。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260929083837.2102260-1-george.abraham.p@intel.com/

**[SERIES] crypto: qat - fix config table locking** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-09-18
- 状态：已合入
- 作者邮箱：Ahsan Atta <ahsan.atta@intel.com>
- 概括：修复 QAT 配置表并发访问缺陷：原先在未持有每设备锁时遍历配置段，或调试文件读取使用不匹配的全局锁，并发删除或更新键值可能释放正在访问的节点，造成释放后使用；现在在查找、插入及调试文件读取路径加每设备读写锁，并去掉旧全局锁。此外在添加键值时直接定位现有项，避免两次重复遍历和临时拷贝，流程不变。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: qat - hold cfg->lock when accessing config sections
  - crypto: qat - avoid redundant config list walks when adding a key
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260918124112.537571-2-ahsan.atta@intel.com/

**▸ 组织：Infradead Community**（2 patches）

**[v2] crypto: ccp: psp-sev.h: clean up kernel-doc warnings**

- 日期：2026-09-18
- 状态：已合入
- 作者邮箱：Randy Dunlap <rdunlap@infradead.org>
- 概括：清理 AMD 安全处理器接口头文件中的内核文档注释，修正两个头文件里结构体成员缺失或多余说明、结构体名称与实际定义不符以及枚举注释格式不当等问题，补全保留字段并更正字段描述，消除文档生成警告，使接口说明与结构定义一致。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260918232736.3095763-1-rdunlap@infradead.org/

**crypto: ccp.h - repair all kernel-doc comments**

- 日期：2026-09-01
- 状态：已合入
- 作者邮箱：Randy Dunlap <rdunlap@infradead.org>
- 概括：为 CCP 加密设备接口头文件统一修复内核文档注释，补上函数返回值、枚举类型、缺失枚举项和结构体成员描述，并改用正确的嵌套结构表示法，消除启用文档检查时产生的大量警告，实际代码功能不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260901185438.31038-1-rdunlap@infradead.org/

**▸ 组织：东南大学**（1 patches）

**crypto: atmel-sha: reject initialization without a device**

- 日期：2026-09-13
- 状态：已合入
- 作者邮箱：Slavin Liu <bolin.liu@seu.edu.cn>
- 概括：Atmel SHA 加速器初始化时，如果设备列表已为空，原先会在空设备指针下继续执行并访问设备字段，可能在设备移除后首次初始化变换时触发空指针访问；现在在查找设备为空时直接返回设备不存在错误，避免后续访问。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260913125143.109897-1-bolin.liu@seu.edu.cn/

**▸ 组织：Google**（1 patches）

**crypto: hisilicon/qm - annotate cap_tables with __counted_by_ptr**

- 日期：2026-09-23
- 状态：已合入
- 作者邮箱：Bill Wendling <morbo@google.com>
- 概括：针对 HiSilicon 加速器的能力表，把两个能力表指针按对应计数字段标注为受计数的指针，让编译器和内核地址消毒等检测机制能够识别指针与元素数量的关系，在开启相应边界检查时发现越界访问；同时在各初始化路径中先写入计数字段再赋值指针，避免出现指针有效而计数为零或未初始化的瞬时状态导致误报。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260923060114.2605310-1-morbo@google.com/

**▸ 组织：归属待核实（itx.no）**（1 patches）

**[v3] lib/crypto: sparc/aes-xts: Add optimization using the AES opcodes**

- 日期：2026-10-04
- 状态：已合入
- 作者邮箱：Stian Halseth <stian@itx.no>
- 概括：为 SPARC 平台利用 AES 操作码实现 XTS 加密解密的架构加速路径，支持 AES-128 和 AES-256、每轮处理两个块，AES-192 和非 8 字节对齐数据回退到通用实现；原先 SPARC 被禁止注册库 XTS 算法，现已允许注册并将优先级调整到与 x86、RISC-V 相同，使 dm-crypt 等场景顺序读写性能明显提高。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261004192812.4145406-1-stian@itx.no/

**▸ 组织：Red Hat**（1 patches）

**[SERIES] libcrypto: Provide more __cleanup functions for zeroizing data** （cover letter，10/10 个 patch 达到代码量阈值）

- 日期：2026-09-16
- 状态：已合入
- 作者邮箱：Thomas Huth <thuth@redhat.com>
- 概括：为内核加密库中多种对称加密和哈希算法的密钥与上下文结构增加清零辅助函数，可配合清理属性在作用域结束时自动清除栈上敏感数据，并替换原有显式清零调用、补充统一文档，可信密钥和 SMB 客户端也改用该机制。
- 达到阈值的 patches（10 个，显示前 5）：
  - lib/crypto: aes: Provide functions for zeroizing aes_key and aes_enckey
  - lib/crypto: aes-xts: Provide function for zeroizing aes_xts_key
  - lib/crypto: aes-gcm: Provide functions for zeroizing aes_gcm* structures
  - lib/crypto: aes-ccm: Provide functions for zeroizing aes_ccm* structures
  - lib/crypto: md5: Provide a function for zeroizing hmac_md5 structures
  - ... 及其他 5 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260916095022.604354-2-thuth@redhat.com/

**▸ 组织：Huawei**（1 patches）

**[SERIES] crypto: hisilicon/hpre - misc fixes and cleanups** （cover letter，1/7 个 patch 达到代码量阈值）

- 日期：2026-09-18
- 状态：已合入
- 作者邮箱：Weili Qian <qianweili@huawei.com>
- 概括：华为高性能 RSA、DH、ECDH 加速器驱动修复：循环先检查长度避免零长度越界读，移除 ECDH 中对空目标的死代码释放；输出缓冲区不足返回溢出错误并映射完整硬件输出；根据请求是否允许睡眠动态选择内存分配标志，提取重复的簇数量读取并删除未使用定义。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: hisilicon/hpre - extract clusters num into inline function
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260918122726.3014899-4-qianweili@huawei.com/

**▸ 组织：归属待核实（genproof.com）**（1 patches）

**[SERIES] lib/crypto: chacha: Handle lengths of 2 GiB or more on 32-bit arm and MIPS** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-10-14
- 状态：已合入
- 作者邮箱：Vladimir Kukharenko <vladimir@genproof.com>
- 概括：修复 32 位 ARM 标量和 MIPS 汇编的 ChaCha 实现在处理约 2 GiB 以上输入时，因剩余长度使用有符号比较而过早进入尾部处理、导致只处理少量数据的问题。ARM 标量路径改为无符号条件并避免块数计算回绕；MIPS 路径保留汇编，改由包装函数每次最多传入 1 GiB 分块处理。当前内核调用者不会传入这种长度，属于接口健壮性修复。
- 达到阈值的 patches（2 个，显示前 5）：
  - lib/crypto: arm/chacha: Handle lengths of 2 GiB or more in scalar code
  - lib/crypto: mips/chacha: Handle lengths of 2 GiB or more
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261014-libcrypto-chacha-32bit-2gib-v1-1-e0719ca0be89@genproof.com/

---

### ◆ 子系统：HWRNG（14 patches）

**▸ 组织：Kernel.org**（12 patches）

**hwrng: amd - use PMBASE_OFFSET consistently**

- 日期：2026-10-08
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：AMD 硬件随机数驱动在申请输入输出区域和映射端口时，将硬编码的偏移数值替换为已有地址偏移宏，使请求区域、错误消息和映射地址保持一致，并补全映射失败消息中缺失的空格。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261008093737.180712-2-blum@kernel.org/

**hwrng: intel - simplify intel_rng_mod_init()**

- 日期：2026-10-06
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：英特尔硬件随机数驱动模块初始化函数原先通过跳转标签集中处理错误返回，现改为在各失败点直接返回对应错误码，不再使用中间错误变量和跳转标签，使初始化失败路径更直接。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261006172628.103594-2-blum@kernel.org/

**hwrng: cctrng - simplify cctrng_probe()**

- 日期：2026-10-06
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：Arm cctrng 硬件随机数驱动在探测过程中注册随机数设备失败时，原先跳转到统一清理标签执行电源管理清理并返回错误，现改为直接调用电源管理清理后返回错误，删除多余跳转，简化失败路径。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261006202734.104415-2-blum@kernel.org/

**hwrng: amd - simplify control flow in amd_rng_mod_init()**

- 日期：2026-10-02
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：在 AMD 768 芯片组硬件随机数生成器驱动初始化时，原先通过跳转标签结束 PCI 设备匹配循环，并分散多个错误清理路径；现在改为循环内匹配后直接终止，循环后再判断是否找到设备，同时合并资源释放路径，使初始化流程更直接，设备行为保持不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261002141952.169528-2-blum@kernel.org/

**hwrng: stm32 - use devm_platform_ioremap_resource() in stm32_rng_probe()**

- 日期：2026-10-02
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：在 STM32 硬件随机数生成器驱动探测阶段，原先获取并映射平台输入输出资源时会返回一个未使用的资源指针；现在改用直接映射接口并删除该局部变量，资源映射过程更简洁。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261002144839.51627-3-blum@kernel.org/

**hwrng: stm32 - use swap() in stm32_rng_probe()**

- 日期：2026-10-01
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：在 STM32 硬件随机数生成器驱动初始化时，原代码用临时变量手动交换两个时钟描述结构，以保证首个时钟被识别为内核时钟；现在直接用交换操作互换这两项，初始化逻辑不变，代码路径得到简化。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261001210450.37467-2-blum@kernel.org/

**hwrng: stm32 - reuse clock rate in stm32_rng_clock_freq_restrain()**

- 日期：2026-10-01
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：在 STM32 硬件随机数生成器驱动限制时钟频率的调试日志中，原代码会再次向时钟框架查询当前速率；现在复用此前已读取的时钟速率值进行打印，避免重复查询，并顺带统一日志标点格式。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261001211612.38124-2-blum@kernel.org/

**hwrng: atmel - use HZ_PER_MHZ in atmel_trng_init()**

- 日期：2026-09-29
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：在 Atmel 硬件随机数发生器的初始化路径中，用内核提供的兆赫兹换算宏替代写死的频率数值，去掉临时速率变量并把频率判断与半速率设置合并，简化外设时钟超过 100 兆赫时使能半速模式的逻辑，不改变原有行为。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260929213751.103658-3-blum@kernel.org/

**[SERIES] hwrng: virtio - use min() in copy_data()** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-09-26
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：virtio 硬件随机数驱动中，设备名称原先用无目标长度限制的字符串格式化构造，虽然当前索引范围不会越界，但改为限定目标缓冲区长度，避免后续改动引入溢出；同时将可用数据长度计算中的带类型转换的较小值宏替换为更直接的较小值比较，行为保持不变。
- 达到阈值的 patches（2 个，显示前 5）：
  - hwrng: virtio - use min() in copy_data()
  - hwrng: virtio - use snprintf() in probe_common()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260926055853.4868-3-blum@kernel.org/

**hwrng: core - reject unknown RNG names**

- 日期：2026-09-24
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：硬件随机数核心的当前发生器名称写入接口，在用户请求的名称不存在时，原实现因错误码仍为零而报告写入成功，但实际没有切换当前发生器；现先设置“设备不存在”错误码再查找，未知名称会被拒绝，避免用户误以为切换已经生效。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260924212114.120633-2-blum@kernel.org/

**hwrng: intel - declare warning string as const**

- 日期：2026-09-23
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：Intel 硬件随机数发生器在固件空间被锁定只读时打印提示，该初始化期间使用的提示字符串此前未标记为常量且存储段属性为初始化数据；现改为只读常量并使用初始化专用只读存储段，并调整缩进，无功能变化。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260923104237.82599-2-blum@kernel.org/

**hwrng: amd - report partial reads in non-blocking mode**

- 日期：2026-09-23
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：AMD 硬件随机数发生器在非阻塞读取时，如果已经向输出缓冲复制了部分随机数据但后续没有更多数据，原实现返回零而没有报告已复制的字节数；现改为返回实际复制的字节数，使上层能正确获得部分读取结果。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260923201259.90336-2-blum@kernel.org/

**▸ 组织：Individual Contributor**（1 patches）

**hwrng: omap3-rom: Use pm_runtime_resume_and_get()**

- 日期：2026-09-22
- 状态：已合入
- 作者邮箱：Bui Duc Phuc <phucduc.bui@gmail.com>
- 概括：用于 OMAP3 ROM 硬件随机数发生器读取路径，将原先手动调用运行时电源管理获取接口、失败时再补充释放未增加引用的重复模式，改为内核现成的合并接口，由该接口在失败时内部完成释放；调用结果保持不变，仅减少错误处理分支。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260922032054.320969-1-phucduc.bui@gmail.com/

**▸ 组织：归属待核实（gondor.apana.org.au）**（1 patches）

**[RESEND] hwrng: cctrng - Discard pm_runtime_put_autosuspend() return value**

- 日期：2026-10-15
- 状态：已合入
- 作者邮箱：Herbert Xu <herbert@gondor.apana.org.au>
- 概括：cctrng 硬件随机数驱动在运行时电源管理自动挂起调用返回非零时不再打印错误。非零仅表示未排队挂起检查，例如用户通过 sysfs 写入“on”后属正常情况，原日志会产生误导；现在直接忽略返回值，也为后续将该接口返回类型改为无返回值做准备。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/atCau3kHbzUefyMA@gondor.apana.org.au/

---

### ◆ 子系统：CAAM (NXP)（3 patches）

**▸ 组织：归属待核实（free.fr）**（2 patches）

**[v2] crypto: caam/qi2 - lower the algorithm priority**

- 日期：2026-09-29
- 状态：已合入
- 作者邮箱：Vincent Jardin <vjardin@free.fr>
- 概括：为CAAM/qi2加密驱动把默认算法优先级从2000降到100，避免它默认压制其他实现；用户仍可通过内核加密接口按需调高优先级，硬件也能继续按驱动名被调用。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260929-for-upstream-caam-qi2-priority-v2-1-bf0559ebf574@free.fr/

**crypto: caam/qi2 - reset the DPSECI at probe only when enabled**

- 日期：2026-09-28
- 状态：已合入
- 作者邮箱：Vincent Jardin <vjardin@free.fr>
- 概括：在 CAAM 队列接口探测时不再对所有 DPSECI 对象盲目复位，而是先查询其启用状态，仅对已启用的对象执行复位，避免管理控制器刚创建且从未启用的对象被复位后对每条队列打印无实际请求却未确认刷新的错误日志；移除路径中的复位行为保持不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260928-for-upstream-caam-qi2-dpseci-reset-v1-1-042be6c05472@free.fr/

**▸ 组织：Individual Contributor**（1 patches）

**crypto: caam: map job ring registers without claiming region**

- 日期：2026-09-01
- 状态：已合入
- 作者邮箱：Rosen Penev <rosenp@gmail.com>
- 概括：在 i.MX 系列处理器上，CAAM 加密引擎的工作环属于父节点安全控制器寄存器窗口的子区域，父驱动已独占保留整块区域，原先工作环探测时再次请求资源会因冲突失败，导致工作环和硬件随机数发生器不可用。现在改为只映射寄存器地址而不重复请求资源，避免与父区域冲突，使工作环正常探测，恢复随机数功能。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260901203736.13248-1-rosenp@gmail.com/

---

### ◆ 子系统：ECC（2 patches）

**▸ 组织：Kernel.org**（1 patches）

**crypto: atmel-ecc - simplify atmel_ecdh_compute_shared_secret**

- 日期：2026-09-01
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：Atmel ECC 加密驱动在计算共享密钥时，原先初始化命令失败后需跳转到统一释放分支再返回，成功时则入队并返回进行中状态。补丁将失败分支改为就地释放工作数据后直接返回错误码，移除跳转标签，使控制流更直观，不改变原有逻辑。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260901081126.44790-2-blum@kernel.org/

**▸ 组织：ANSSI**（1 patches）

**[v2] crypto: ecc - Handle exceptional points in Shamir multiplication**

- 日期：2026-09-26
- 状态：已合入
- 作者邮箱：Jérémy Jean <Jeremy.Jean@oss.cyber.gouv.fr>
- 概括：椭圆曲线 Shamir 乘法原先对相同点、相反点和无穷远点的处理有误，可能拒绝有效 ECDSA 签名，并在公钥为基点或其相反点时可能接受无效摘要与签名组合。现在预计算和累加阶段显式处理倍点、相互抵消和无穷远点，并新增 P-256 ECDSA 与 256/512 位 EC-RDSA 的有效和无效回归向量，使这些边界点产生的签名验证结果符合预期。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260926204323.1913803-4-Jeremy.Jean@oss.cyber.gouv.fr/

---

### ◆ 子系统：Authenc（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: atmel: handle authenc requests without plaintext**

- 日期：2026-09-22
- 状态：已合入
- 作者邮箱：Karl Mehltretter <kmehltretter@gmail.com>
- 概括：用于 Atmel 认证加密硬件处理只有附加数据、无明文或密文的请求。此前即使附加数据已处理，仍无条件请求 AES 的 DMA 零字节传输，被 Atmel DMA 引擎拒绝，导致有效请求失败并常返回内存不足；同步摘要完成路径还会丢失标签不匹配错误，可能把解密失败误报成功。现在文本长度为零时跳过 AES 传输直接完成摘要，同步路径直接传递最终错误码，使坏标签对新旧变换都返回拒绝错误。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260922051705.15329-1-kmehltretter@gmail.com/

---

### ◆ 子系统：TCrypt（1 patches）

**▸ 组织：归属待核实（gondor.apana.org.au）**（1 patches）

**crypto: tcrypt - Avoid reading req->base after submission**

- 日期：2026-09-22
- 状态：已合入
- 作者邮箱：Herbert Xu <herbert@gondor.apana.org.au>
- 概括：在加密算法自测和性能测试中，异步请求提交给内核加密接口后，原先仍从请求对象内的等待数据字段读取完成状态，而该字段可能在处理期间被并发修改。现将等待结构与请求对象组合成测试专用请求结构，并传递组合结构，避免在提交后读取请求内部的等待字段，消除对可能变化数据的依赖。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/arJPHqt-vgu8md57@gondor.apana.org.au/

---

### ◆ 子系统：Skcipher（1 patches）

**▸ 组织：归属待核实（free.fr）**（1 patches）

**crypto: caam/qi,qi2 - set plain_keylen for skcipher descriptors**

- 日期：2026-09-28
- 状态：已合入
- 作者邮箱：Vincent Jardin <vjardin@free.fr>
- 概括：修复 CAAM 队列接口驱动为对称加密设置密钥时遗漏明文密钥长度和命令选项的问题。此前受保护 AES 支持引入后，共享描述符装入零长度密钥，安全引擎把内联密钥字节当作命令解析，导致 LX2160A 上除 XTS 外的自检向量均以无效加载命令失败；补齐字段后算法可正常完成设置和加解密。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260928-for-upstream-caam-qi-plain-keylen-v1-1-6edb56649cf9@free.fr/

---

### ◆ 子系统：AF_ALG API（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: algif_skcipher: rewind rounded output bytes**

- 日期：2026-10-04
- 状态：已合入
- 作者邮箱：Daehyeon Ko <4ncienth@gmail.com>
- 概括：内核套接字对称加密接收路径中，连续请求会按块大小向下取整长度，但未同步回退接收迭代器；这使后续块可能从提供者未写入的字节开始，在特定读取方式下把旧页中的陈旧字节作为输出返回，低权限用户可用 AES-XTS 构造请求观察到残留数据。现在在拒绝零处理长度前回退被舍去的尾部，使后续处理与已写长度对齐，堵住该泄露途径。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261004050946.3131044-1-4ncienth@gmail.com/

---

### ◆ 子系统：Talitos（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[v4] crypto: talitos: init tasklets before requesting IRQs**

- 日期：2026-10-04
- 状态：已合入
- 作者邮箱：Rosen Penev <rosenp@gmail.com>
- 概括：修复talitos驱动支持第二个中断后先请求中断再初始化任务队列的顺序问题，避免引导加载器或kexec残留中断导致调度空回调；现在先完成队列初始化和设备复位再请求中断，并修正移除时对未请求中断号的释放。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261004215042.383358-1-rosenp@gmail.com/

---

### ◆ 子系统：CCP/SEV (AMD)（1 patches）

**▸ 组织：AMD**（1 patches）

**[v3,1/1] crypto: ccp - Make usage of sev_cmd_mutex more granular**

- 日期：2026-10-21
- 状态：已合入
- 作者邮箱：Michael Roth <michael.roth@amd.com>
- 概括：AMD SEV 固件用户空间控制命令原先在顶层入口持有全局互斥锁，覆盖用户内存拷贝等可能缺页的准备工作；在未来的客户机私有内存文件支持中，恶意用户若利用共享与私有页转换触发特殊缺页处理，理论上可能造成死锁。现将该锁下移到各命令处理函数，仅保护平台状态转换和实际固件调用，缩短持锁范围，避免在可能缺页的用户内存拷贝期间持有锁。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261021192434.1924950-2-michael.roth@amd.com/

---

### ◆ 子系统：ICE (Qualcomm)（1 patches）

**▸ 组织：The Good Penguin**（1 patches）

**[SERIES] crypto: use designated initializers for acpi_device_id** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-09-03
- 状态：已合入
- 作者邮箱：Pawel Zalewski <pzalewski@thegoodpenguin.co.uk>
- 概括：AMD 安全协处理器和 HiSilicon SEC 加密引擎的 ACPI 设备 ID 表由位置式初始化改为命名字段初始化，并统一结束项格式、删除冗余零值，使列表读起来更清晰、与内核常规风格一致；实际设备匹配行为不变。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: ccp: use named initializers for acpi_device_id
  - crypto: hisilicon/sec: use named initializers for acpi_device_id
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260903-acpi-crypto-v1-1-253cc6fd9836@thegoodpenguin.co.uk/

---

### ◆ 子系统：DRBG（1 patches）

**▸ 组织：Kernel.org**（1 patches）

**[SERIES] crypto: Remove the unnecessary crypto_rng API** （cover letter，9/14 个 patch 达到代码量阈值）

- 日期：2026-10-18
- 状态：已合入
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：移除内核中已无实际算法用户的通用随机数算法抽象：抖动熵源和确定性随机比特生成器改为提供直接库接口，后者直接调用前者，标准随机数也直接调用生成器，加密算法套接字的随机数接口同步改为直接调用；同时为生成器库接口补充自检，并把抖动熵源健康检查从模块加载时推迟到首次使用，避免未使用时在启动阶段执行昂贵检查。生成器不再注册后，内核加密算法列表不再显示它，但现有随机数接口行为保持不变，仅简化调用链。
- 达到阈值的 patches（9 个，显示前 5）：
  - crypto: jitterentropy - Move health check to first use
  - crypto: drbg - Use jitterentropy library API
  - crypto: drbg - Add library API
  - crypto: drbg - Add self-test for library API
  - crypto: algif_rng - Use DRBG and jitterentropy library APIs
  - ... 及其他 4 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261018204618.104876-2-ebiggers@kernel.org/

---

## 社区讨论中 Patches

### ◆ 子系统：General Crypto（35 patches）

**▸ 组织：Individual Contributor**（6 patches）

**crypto: atmel-i2c - find the bus speed behind an I2C mux**

- 日期：2026-10-29
- 状态：社区讨论中
- 作者邮箱：Josef Schlehofer <pepe.schlehofer@gmail.com>
- 概括：Turris Omnia 路由器上，Atmel ATSHA204A 安全芯片位于 PCA9547 I2C 多路复用器之后，驱动此前只读取该复用器通道的时钟频率属性，因通道没有该属性导致探测直接失败。补丁改为先看客户端所在适配器，没有时逐级查找父适配器，仍无则默认 100 kHz，使设备能正常初始化，并按实际总线段速度计算唤醒令牌。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261029082616.53365-1-pepe.schlehofer@gmail.com/

**lib/crypto: aes: use memzero_explicit() instead of memset()**

- 日期：2026-10-28
- 状态：社区讨论中
- 作者邮箱：Mohamad Raizudeen <raizudeen.kerneldev@gmail.com>
- 概括：在 AES-GCM 和 AES-CCM 解密认证失败时，原用普通内存清零操作清除已解密但未通过认证的输出缓冲区，编译器可能优化掉该清零，导致数据残留。现改用强制清零函数，确保调用方即使未正确处理错误也不会接收到未经认证的解密数据，与该文件中其他敏感数据清除方式一致。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261028142636.5888-1-raizudeen.kerneldev@gmail.com/

**[SERIES] Batched zswap_store() framework with compression batching** （cover letter，1/4 个 patch 达到代码量阈值）

- 日期：2026-10-28
- 状态：社区讨论中
- 作者邮箱：Kanchana P. Sridhar <kanchanapsridhar2026@gmail.com>
- 概括：为内核异步压缩接口新增按单元大小拆分散列表的批量能力，并支持查询压缩器最大批次；不支持分段的算法通过包装器仍按单段调用。内存压缩交换在存储大页时，若底层压缩器支持批量则一次提交多个页，否则逐页压缩，同时改为批量分配交换条目并记录页所在节点，避免逐页重复检查内存控制组状态。该框架服务于硬件并行压缩器，现有软件压缩器仅增加少量指针开销，后续再优化小对象分配。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: acomp - Define a unit_size in struct acomp_req to enable batching. mm: zswap: Set the unit size for zswap to PAGE_SIZE.
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261028030503.17923-2-kanchanapsridhar2026@gmail.com/

**crypto: amlogic - Free channel IRQs before disabling the clock**

- 日期：2026-10-15
- 状态：社区讨论中
- 作者邮箱：Myeonghun Pak <mhun512@gmail.com>
- 概括：Amlogic GXL 加密加速器中，中断请求早于受管通道数组分配，自动清理会先释放数组再释放中断，在密码超时场景下晚到的中断处理可能写入已释放的通道完成状态；现改为在关闭总线时钟和释放通道数组前显式释放中断，并在加密引擎退出后执行。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/179203206852.2659709.13834828335447558448.G3@gmail.com/

**lib/crypto: md5: correct header inclusions**

- 日期：2026-10-15
- 状态：社区讨论中
- 作者邮箱：Mohamad Raizudeen <raizudeen.kerneldev@gmail.com>
- 概括：MD5 库代码中循环移位函数未显式包含所需头文件，依赖间接包含，同时包含了一个未使用的非对齐访问头文件；现补上对应头文件并移除多余包含，使头文件依赖明确。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261015033843.6056-1-raizudeen.kerneldev@gmail.com/

**crypto: essiv: avoid request access after subrequest**

- 日期：2026-09-21
- 状态：社区讨论中
- 作者邮箱：Jiale Yao <yaojiale02@163.com>
- 概括：使用 ESSIV 模板的带关联数据加密请求在提交子请求后，异步完成可能先释放关联缓冲区并完成外层请求，若随后再读取请求上下文中的关联缓冲区指针，可能访问已释放内存并再次释放。现在在提交子请求前先保存该指针，同步清理时使用本地快照，避免释放后访问和重复释放。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260921090458.3364976-1-yaojiale02@163.com/

**▸ 组织：Kernel.org**（6 patches）

**lib/crypto: poly1305: Hide the mask value from compilers**

- 日期：2026-10-31
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：Poly1305 消息认证码输出时需要在累加值和累加值减去模数之间做常量时间选择，原选择掩码对编译器可见，理论上可能被编译器识别并优化成依赖秘密的分支；目前未见 gcc 或 clang 实际触发，但补丁显式隐藏该掩码，防止未来编译优化破坏常量时间特性。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261031042637.68815-1-ebiggers@kernel.org/

**lib/crypto: aes-cmac: Hide selection mask value from compilers**

- 日期：2026-10-31
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：AES-CMAC 预处理在计算派生密钥时用掩码选择 0x87 或 0，该掩码原对编译器可见，理论上可被转化为依赖秘密的分支；补丁隐藏掩码，并将掩码类型改为无符号长整型以避免 32 位平台上被迫占用寄存器对，保持常量时间选择。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261031052053.201779-1-ebiggers@kernel.org/

**lib/crypto: gf128hash: Hide selection mask values from compilers**

- 日期：2026-10-31
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：GF(2^128) 哈希的常数时间乘法与密钥转换路径中有多个用于选择值的掩码，原掩码对编译器可见，理论上可能生成依赖秘密的分支；补丁统一隐藏这些选择掩码，使相关计算保持常量时间。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261031052149.201983-1-ebiggers@kernel.org/

**lib/crypto: gf128mul: Hide selection mask values from compilers**

- 日期：2026-10-31
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：GF(2^128) 乘法及 XTS 等模式中的倍乘运算使用选择掩码在 0x87 和 0 之间做常量时间选择，原掩码对编译器可见，可能被优化成秘密相关分支；补丁隐藏掩码，并在选择值仅两种情况时将掩码类型改为无符号长整型，避免 32 位架构上的额外寄存器开销。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261031052154.202008-1-ebiggers@kernel.org/

**crypto: arc4 - Remove obsolete crypto API support for ARC4**

- 日期：2026-10-31
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：删除内核中已过时的 ARC4 加密 API 包装器，仅保留供某些遗留协议直接调用的 ARC4 库实现。此前所有内核用户都已使用库接口，用户态无线守护进程也已改用用户空间 ARC4，该 API 已废弃警告六年，并默认不在用户态算法接口允许列表中，因此不再需要保留这一不安全算法的密码 API 入口。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261031211535.8793-1-ebiggers@kernel.org/

**[SERIES] x86: Remove cpu_has_xfeatures() and add AVX-512 xor_gen()** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-09-01
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：在x86和用户模式Linux启动时检查AVX及AVX-512对应的扩展状态位，若缺失则清除相应特性标志；随后从x86加密与库代码中移除对扩展状态位的重复检查，并新增AVX-512异或生成实现，用于加速RAID等多磁盘异或运算，在部分服务器和客户端处理器上提升吞吐。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: x86 - Stop using cpu_has_xfeatures()
  - lib/crypto: x86: Stop using cpu_has_xfeatures()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260901145740.42337-4-ebiggers@kernel.org/

**▸ 组织：Intel**（4 patches）

**[v2,1/2] crypto: qat - enable three-service mode for QAT GEN5 devices**

- 日期：2026-10-30
- 状态：社区讨论中
- 作者邮箱：Ahsan Atta <ahsan.atta@intel.com>
- 概括：在 Intel QAT 第五代 420xx 设备驱动中新增三服务并发配置，使同一设备可以同时启用对称加密、非对称加密和压缩三类加速服务；此前该模块不允许三者同时开启。补丁增加对应的固件对象布局、环到服务映射和线程到仲裁器映射，让设备引擎能够按配置分配给三类服务。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261030143019.484280-2-ahsan.atta@intel.com/

**crypto: qat - make adf_ae_shutdown() a void function**

- 日期：2026-10-30
- 状态：社区讨论中
- 作者邮箱：Ahsan Atta <ahsan.atta@intel.com>
- 概括：Intel QAT 加速器的加速引擎关闭操作始终成功，但原调用路径仍检查其返回值并保留不会触发的失败处理，还可能在失败分支跳过清除已初始化状态。补丁将该函数改为无返回值，删除死代码，在关闭后无条件清除状态标记，使关闭流程与实际语义一致并简化调用逻辑。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261030111916.483870-1-ahsan.atta@intel.com/

**crypto: qat - add support for enhanced decompression mode on GEN6 devices**

- 日期：2026-10-26
- 状态：社区讨论中
- 作者邮箱：Suman Kumar Chakraborty <suman.kumar.chakraborty@intel.com>
- 概括：为 Intel QAT 第六代设备新增增强解压模式：固件可让压缩引擎内嵌的解压单元直接处理解压请求，绕开压缩与翻译阶段，从而在并发压缩的同时提高解压吞吐。该模式通过设备属性接口开关控制，设置会持久化并在设备重新上下线或服务配置变化后重新应用；当只配置独立解压服务而未配置压缩服务时默认启用，并相应调整解压环对到压缩引擎的线程映射。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261026035501.1627846-1-suman.kumar.chakraborty@intel.com/

**[SERIES] crypto: iaa - rework the WQ selection tables** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-10-19
- 状态：社区讨论中
- 作者邮箱：Vinicius Costa Gomes <vinicius.gomes@intel.com>
- 概括：重构 Intel IAA 压缩加速器的工作队列选择：原先按 CPU 扁平索引可能把 CPU 配到其他处理器包上的设备，且重平衡时请求可能读到空队列而失败；现在改为每个处理器包维护 RCU 保护的队列表，压缩请求在所属包内轮询选择，重平衡整体发布新表，失败时保留旧表。解压请求则让每个 CPU 首次选择后固定在同一队列上，减少延迟波动。请求上下文记录持有引用的队列，提交和完成路径统一从请求获取，去除参数不一致。
- 达到阈值的 patches（4 个，显示前 5）：
  - crypto: iaa - carry the iaa_wq in the request
  - crypto: iaa - use RCU per-package WQ tables
  - crypto: iaa - keep each CPU on one WQ for decompression
  - crypto: iaa - take the WQ from the request in the submit helpers
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261019-iaa-crypto-wq-tables-v1-1-fab67b2a1538@intel.com/

**▸ 组织：Texas Instruments**（3 patches）

**[SERIES] Fix several issues in DTHEv2 driver** （cover letter，6/15 个 patch 达到代码量阈值）

- 日期：2026-10-16
- 状态：社区讨论中
- 作者邮箱：T Pratham <t-pratham@ti.com>
- 概括：针对德州仪器 DTHEv2 加密引擎驱动修复多处缺陷：修正空设备列表获取、自旋锁与移除时释放后使用风险，避免高端内存页散列表访问造成潜在内存破坏；按请求长度裁剪散列表并校验，对齐 DMA 缓冲区、分离源和目标填充，错误路径终止 DMA 描述符，仅内存不足才软件回退，长度改为 64 位防溢出，并调整认证标签操作与缓存失效顺序。
- 达到阈值的 patches（6 个，显示前 5）：
  - crypto: ti - Use list_first_entry_or_null() in dthe_get_dev()
  - crypto: ti - Trim scatterlists to correct length in AES
  - crypto: ti - Separate padding buffer for src and dst
  - crypto: ti - Fix use-after-free of dev_data on DTHEv2 driver removal
  - crypto: ti - Do AEAD software fallback on only ENOMEM
  - ... 及其他 1 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261016124456.1802080-2-t-pratham@ti.com/

**[SERIES] Clean and improve SA2UL driver** （cover letter，9/30 个 patch 达到代码量阈值）

- 日期：2026-09-15
- 状态：社区讨论中
- 作者邮箱：Chawdhry, Manorit <m-chawdhry@ti.com>
- 概括：对德州仪器 SA2UL 驱动做清理和修复：删除未使用字段、死代码与冗余封装，修正摘要和认证加密初始化错误路径的资源泄漏、DMA 映射泄漏、栈越界和命令标签并发破坏，释放前清零安全上下文，动态计算元数据长度；接入加密引擎队列，增加 AES-CM 随机数发生器启动并上报硬件修订。
- 达到阈值的 patches（9 个，显示前 5）：
  - crypto: sa2ul - consolidate encryption offset definitions
  - crypto: sa2ul - fix error handling in sa_prepare_iopad
  - crypto: sa2ul - generate dynamic metadata length
  - crypto: sa2ul - zero out security context on free
  - crypto: sa2ul - move export to appropriate location.
  - ... 及其他 4 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260915-b4-upstream-sa2ul-cleanup-v1-4-57ab34e97162@ti.com/

**[SERIES] Add support for hashing algorithms in TI DTHE V2** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-09-10
- 状态：社区讨论中
- 作者邮箱：T Pratham <t-pratham@ti.com>
- 概括：为德州仪器 DTHE V2 硬件加密引擎的哈希单元加入 SHA-224、SHA-256、SHA-384 和 SHA-512 算法支持，使这些摘要计算可卸载到该硬件；随后又加入对应的 HMAC-SHA512/384/256/224 认证算法，让基于 SHA-2 的消息认证也能由硬件完成，适合需要批量摘要和完整性校验的嵌入式场景。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: ti - Add support for SHA224/256/384/512 in DTHEv2 driver
  - crypto: ti - Add support for HMAC in DTHEv2 driver
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260910180424.2131193-2-t-pratham@ti.com/

**▸ 组织：AMD**（2 patches）

**[SERIES] Implement SNP live firmware update support** （cover letter，3/4 个 patch 达到代码量阈值）

- 日期：2026-10-21
- 状态：社区讨论中
- 作者邮箱：Pratik R. Sampat <prsampat@amd.com>
- 概括：为 AMD SEV-SNP 平台增加固件在线更新支持，用户通过固件上传接口写入新镜像，驱动执行下载固件扩展命令完成加载；若旧式 SEV 平台正在运行则返回忙，否则关闭并释放其缓冲区，SNP 虚拟机不受影响。同时清理固件加载器模块引用，并支持初始化后查询 SNP 平台数据。
- 达到阈值的 patches（3 个，显示前 5）：
  - crypto: ccp - Factor out the release of the SEV firmware buffers
  - crypto: ccp - Allow SNP platform data to be queried after SNP INIT
  - crypto: ccp - Implement SNP Download Firmware EX
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/be72e0b1015156f8613fc2c360fa73d59108dcc6.1792599491.git.prsampat@amd.com/

**[RFC,kernel,04/17] crypto/ccp/tsm: Use TSM API for DOE**

- 日期：2026-09-16
- 状态：社区讨论中
- 作者邮箱：Alexey Kardashevskiy <aik@amd.com>
- 概括：AMD CCP 的 TSM 模块在 SPDM 请求循环中，原来直接调用 PCI 数据对象交换传输，现改为使用带更多健全性检查的传输辅助函数，使支持 CMA 或安全会话等特性的 SPDM 消息收发在提交前增加一层合法性校验。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260916115159.1938195-5-aik@amd.com/

**▸ 组织：归属待核实（gondor.apana.org.au）**（2 patches）

**crypto: aes - Add import_core/export_core to cmac/xcbc/cbcmac**

- 日期：2026-10-09
- 状态：社区讨论中
- 作者邮箱：Herbert Xu <herbert@gondor.apana.org.au>
- 概括：为内核AES库的CMAC、XCBC和CBCMAC实现补充状态导出与导入接口，使其导出格式与通用消息认证码模板对齐；其中CMAC和XCBC在导出前对暂存块再执行一次加密，避免状态丢失，保证状态序列化后能正确恢复。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/asjT87HAZ_UUbbvm@gondor.apana.org.au/

**[v2] crypto: hash - Preserve withheld block in export_core**

- 日期：2026-10-09
- 状态：社区讨论中
- 作者邮箱：Herbert Xu <herbert@gondor.apana.org.au>
- 概括：在无部分块数据的核心导出场景中，CMAC 和 XCBC 等算法保留用于最终化的一个块未被包含，导致导出的哈希状态不完整；现改为在存在完整保留块时先执行一次哈希更新将其合并，再导出状态。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/asjfxnGfCtvD7QJL@gondor.apana.org.au/

**▸ 组织：浙江大学**（1 patches）

**[v2] crypto: ccp - Fix use-after-free in backlog cmd advancement**

- 日期：2026-09-29
- 状态：社区讨论中
- 作者邮箱：Fan Wu <fanwu01@zju.edu.cn>
- 概括：修复 CCP 加密设备驱动中可延后命令从积压队列提升后短暂脱离链表引发的释放后使用：销毁设备时无法冲刷该命令，工作队列可能在设备释放后访问并唤醒已停止的内核线程；同时并发提交可能抢占预留位置，使命令计数超过上限。现在在出队时于同一锁内把空槽直接转移给积压命令原子预留，并在内核线程中执行回调后再入队，销毁前标记停用并抑制唤醒。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260929143825.21349-1-fanwu01@zju.edu.cn/

**▸ 组织：Qualcomm**（1 patches）

**[v11,1/2] crypto: qce - Only register algos if the user really wants it**

- 日期：2026-10-22
- 状态：社区讨论中
- 作者邮箱：Bartosz Golaszewski <bartosz.golaszewski@oss.qualcomm.com>
- 概括：高通 QCE 加密引擎的算法仍存在一些暂未触发自检失败的问题，因此默认不向内核注册这些算法，只有用户显式通过模块参数启用时才注册；电源管理部分保持不变，以便继续通过运行时电源管理缩放互联和门控时钟。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261022-qce-fixes-broken-label-v11-1-0d33c34fd0c3@oss.qualcomm.com/

**▸ 组织：归属待核实（jaseg.de）**（1 patches）

**[v3,06/12] crypto: api - Allocate tfms from the secret pool**

- 日期：2026-09-28
- 状态：社区讨论中
- 作者邮箱：Jan Sebastian Götte <linux@jaseg.de>
- 概括：将加密变换对象的分配从普通内核内存改到机密内存池，因为其上下文包含展开后的密钥调度，普通分配可能被崩溃转储捕获。新分配所在页面由崩溃内存动作标记，供 kdump 内核在转储前擦除，降低密钥材料进入转储文件的风险；分配多一次桶查找，释放路径不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260928-crash-memaction-upstream-20260921-v3-6-e511e9ee2329@jaseg.de/

**▸ 组织：东南大学**（1 patches）

**[v2] crypto: inside-secure: initialize EIP93 state before requesting IRQ**

- 日期：2026-10-09
- 状态：社区讨论中
- 作者邮箱：Runyu Xiao <runyu.xiao@seu.edu.cn>
- 概括：调整 SafeXcel EIP-93 加密引擎的探测顺序，先完成描述符环和硬件状态初始化，再注册线程中断，避免请求中断后处理函数立即运行却访问尚未初始化的状态；当中断注册失败时，同步清理引擎并复位环寄存器，再交由设备资源管理机制释放 DMA 环。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261009033149.1127441-1-runyu.xiao@seu.edu.cn/

**▸ 组织：归属待核实（sang-engineering.com）**（1 patches）

**crypto: ccp - unmap descriptor before completing cookie**

- 日期：2026-10-10
- 状态：社区讨论中
- 作者邮箱：Wolfram Sang <wsa+renesas@sang-engineering.com>
- 概括：CCP 的 DMA 引擎在处理完成描述符时，原先先标记传输完成再取消映射，可能导致完成通知发出时缓冲区尚未刷写；现改为先取消描述符映射再标记完成，确保缓冲区刷写后才完成 cookie。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261010125001.19300-3-wsa+renesas@sang-engineering.com/

**▸ 组织：NXP**（1 patches）

**[RFC,4/4] crypto: remove async_tx framework**

- 日期：2026-10-15
- 状态：社区讨论中
- 作者邮箱：Frank Li <Frank.Li@oss.nxp.com>
- 概括：在md/raid5已改用同步操作后，移除不再有使用者的异步传输框架及其接口文档，删除相关API和实现文件，移除对异步内存复制、异或校验等操作链的抽象。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261015-asycn_tx_remove-v1-4-056a7085e0a1@nxp.com/

**▸ 组织：Rambus**（1 patches）

**[SERIES] crypto: cmh - add Rambus CryptoManager Hub driver** （cover letter，13/13 个 patch 达到代码量阈值）

- 日期：2026-09-17
- 状态：社区讨论中
- 作者邮箱：Alex Ousherovitch <aousherovitch@rambus.com>
- 概括：为Rambus CryptoManager Hub硬件加密加速器新增驱动，实现平台探测、邮箱队列和DMA管理，注册对称、哈希、认证、公钥及后量子等算法，并提供专用字符设备处理硬件密钥生命周期及内核加密API无法表达的密钥操作。
- 达到阈值的 patches（13 个，显示前 5）：
  - crypto: cmh - add DRBG hwrng
  - crypto: cmh - add SHA-2/SHA-3/SHAKE ahash
  - crypto: cmh - add SM3 ahash
  - crypto: cmh - add HMAC ahash
  - crypto: cmh - add ECDH/X25519 kpp
  - ... 及其他 8 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260917225929.2494111-12-aousherovitch@rambus.com/

**▸ 组织：归属待核实（mtsistemi.it）**（1 patches）

**[SERIES] crypto: ccp - two PSP init fixes, and the AMD BC-250** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-09-19
- 状态：社区讨论中
- 作者邮箱：Mattia Tadini <info@mtsistemi.it>
- 概括：针对 AMD BC-250 安全处理器未被驱动识别、内存窗口被禁用的问题，按实测寄存器布局补充设备支持并仅启用平台访问；同时修复 TEE 能力位存在但驱动配置缺失时空指针导致模块初始化崩溃，并改为同时检查硬件能力和驱动数据后再启动 SEV/TEE 子设备，避免缺少 TEE 配置时连累平台访问等无关功能无法使用。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: ccp - do not start PSP sub-devices without their vdata
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/178984289057.12336.8102552838289034525@mtsistemi.it/

**▸ 组织：Huawei**（1 patches）

**[SERIES] crypto: hisilicon/qm - fix bugs and harden against abnormal hardware** （cover letter，2/4 个 patch 达到代码量阈值）

- 日期：2026-09-24
- 状态：社区讨论中
- 作者邮箱：Weili Qian <qianweili@huawei.com>
- 概括：为华为加密加速器队列管理模块修复异常硬件处理：在设备不支持 ACPI 电源管理或缺少 ACPI 配套信息时清除运行时电源管理标志，避免空指针；在 SVA 不支持时释放已创建的用户加速接口以免泄漏；当能力版本或队列深度寄存器读回异常值时直接报错退出，防止使用无效配置导致越界或除零。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: hisilicon/qm - clear runtime PM flag for non-power-manageable device
  - crypto: hisilicon/qm - check queue depth read from hardware
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260924113812.1110302-2-qianweili@huawei.com/

**▸ 组织：归属待核实（genproof.com）**（1 patches）

**[SERIES] lib/crypto: Handle large lengths in poly1305 and chacha20poly1305** （cover letter，1/5 个 patch 达到代码量阈值）

- 日期：2026-10-12
- 状态：社区讨论中
- 作者邮箱：Vladimir Kukharenko <vladimir@genproof.com>
- 概括：修复内核 Poly1305 和 ChaCha20-Poly1305 库在大长度输入下的接口缺陷：多个 64 位架构的汇编实现原先按 32 位参数读取长度，单次处理约 2 GiB 以上时会计算出错误结束地址并可能越界读；更新函数也会因 32 位加法回绕或截断而少认证超过 4 GiB 的数据。现在这些接口按完整长度处理，并在底层按无符号整数上限分块调用。当前内核调用者不会传入如此大的输入，属于接口健壮性修复。
- 达到阈值的 patches（1 个，显示前 5）：
  - lib/crypto: chacha: Take a size_t length in chacha_crypt()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261012-libcrypto-4gib-lengths-v1-2-ea566c129a2e@genproof.com/

**▸ 组织：归属待核实（cynove.com）**（1 patches）

**[SERIES] crypto: fix RSA results corrupted by non-coherent DMA** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-10-16
- 状态：社区讨论中
- 作者邮箱：Stephane Debusne <stephane.debusne@cynove.com>
- 概括：修复非一致性 DMA 平台上 CAAM 等硬件 RSA 驱动结果被缓存行回写破坏的问题。同步辅助接口和验证路径原先把输出缓冲区紧挨请求上下文放在同一块分配中，缓冲区起始可能与驱动随后写入的上下文字段共享缓存行，设备写入结果会被旧缓存覆盖；在 i.MX8M Mini 上可导致签名字节替换输出开头，无线监管数据库和自签名证书验证失败。现在把数据缓冲区单独分配，避免与请求上下文共享缓存行。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: rsassa-pkcs1 - use a separate buffer for the RSA output
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261016090333.2247764-3-stephane.debusne@cynove.com/

**▸ 组织：归属待核实（mandelbit.com）**（1 patches）

**[SERIES] lib/crypto: x86/chacha: Add 16-block AVX-512 implementation** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-10-25
- 状态：社区讨论中
- 作者邮箱：Antonio Quartulli <antonio@mandelbit.com>
- 概括：为 x86 平台的 ChaCha 流密码库新增一次处理 16 个分组的 AVX-512 实现，输入超过 8 个分组时使用，尾部仍由现有实现完成；对会因 512 位寄存器而降频的处理器则自动避免该路径。AMD Zen 5 测试中，1KB 和 4KB 数据的加密吞吐从约 5.2GB/s 提升到约 10.2GB/s。附带架构无关的 KUnit 测试，覆盖标准向量、不同长度、对齐、页边界和多次调用。
- 达到阈值的 patches（2 个，显示前 5）：
  - lib/crypto: x86/chacha: Add 16-block AVX-512 (zmm) implementation
  - lib/crypto: tests: Add KUnit tests and benchmark for ChaCha
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261025234758.3219829-3-antonio@mandelbit.com/

---

### ◆ 子系统：HWRNG（4 patches）

**▸ 组织：SUSE**（1 patches）

**[v5,07/12] hw_random/via-rng: Stop using 32-bit MSR interfaces**

- 日期：2026-10-26
- 状态：社区讨论中
- 作者邮箱：Jürgen Groß <jgross@suse.com>
- 概括：针对 VIA 处理器随机数生成器初始化时使用的 32 位模型特定寄存器读写接口即将被移除，改为使用 64 位接口完成寄存器读取、状态修改与回写，使随机数源初始化和使能逻辑保持原有行为，避免后续接口删除影响该设备。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261026130223.773129-8-jgross@suse.com/

**▸ 组织：归属待核实（gondor.apana.org.au）**（1 patches）

**hwrng: cctrng - Lock read and writer of circular buffer**

- 日期：2026-10-26
- 状态：社区讨论中
- 作者邮箱：Herbert Xu <herbert@gondor.apana.org.au>
- 概括：为 cctrng 硬件随机数驱动的环形缓冲区增加互斥锁，同时覆盖读取和写入路径。原先读写之间没有任何同步机制，存在竞争风险；现在改用互斥锁统一保护缓冲区读写，消除并发访问可能导致的缓冲区状态不一致，并顺带支持等待标志。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/at7rX1rkRAzHYwCB@gondor.apana.org.au/

**▸ 组织：Individual Contributor**（1 patches）

**hwrng: mtk - wait long enough for the next word**

- 日期：2026-10-26
- 状态：社区讨论中
- 作者邮箱：Ryan Brue <ryanbrue.dev@gmail.com>
- 概括：联发科 mtk 硬件随机数驱动原本只等待 60 微秒产生下一个 32 位字，但 MT8695 平台上实际耗时中位数为 82 微秒，最长 225 微秒，导致多数等待超时，读取失败或返回短数据。现将超时提高到 1 毫秒，快速设备仍可即时返回；在 MT8695 上空闲后读取成功，长读取也完整返回且吞吐率不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261026-rbrue-sheldon-upstreaming-mtk-rng-timeout-v1-1-551b4b6b4f86@gmail.com/

**▸ 组织：归属待核实（ptudor.net）**（1 patches）

**[SERIES] hwrng: add Microchip RNG90 support** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-10-24
- 状态：社区讨论中
- 作者邮箱：Patrick Tudor <ptudor@ptudor.net>
- 概括：为 I2C 接口的 Microchip RNG90 加密随机数发生器新增硬件随机数驱动，负责唤醒和识别设备、封装信息与随机数命令、在限定时间内轮询执行、校验响应长度和循环冗余校验，并在健康或自检失败时丢弃不合格输出。默认采用最小非零熵估计，管理员可在平台验证后调高。附带 KUnit 测试通过脚本化 I2C 适配器覆盖命令帧、恢复和健康失败等场景。
- 达到阈值的 patches（2 个，显示前 5）：
  - hwrng: add Microchip RNG90 driver
  - hwrng: rng90: add KUnit tests
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261024-rng90-submit-v1-v1-2-e265cfabc9af@ptudor.net/

---

### ◆ 子系统：ECC（3 patches）

**▸ 组织：Individual Contributor**（2 patches）

**crypto: ecc - Randomize the initial Z in ecc_make_pub_key()**

- 日期：2026-10-26
- 状态：社区讨论中
- 作者邮箱：Erwin Pawliczek <pawliczekerwin@gmail.com>
- 概括：椭圆曲线公钥生成过程中原来没有随机化初始投影坐标，导致后续模逆的输入由私钥确定，而模逆执行时间不恒定，可能通过运行时间泄漏私钥。现在生成公钥时引入随机初始坐标并在结束后清零，以盲化模逆输入；蓝牙 SMP 和 TPM2 HMAC 会话等生成临时密钥的场景受益，性能变化在噪声范围内。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261026034429.742489-1-pawliczekerwin@gmail.com/

**crypto: ecc - Use constant-time modular inversion in ecc_point_mult()**

- 日期：2026-09-28
- 状态：社区讨论中
- 作者邮箱：Erwin Pawliczek <pawliczekerwin@gmail.com>
- 概括：将椭圆曲线点乘中的模逆从依赖输入分支的传统扩展欧几里得算法替换为常数时间实现，避免 ECDH 私钥参与求逆时通过运行时间泄露；签名验证等公开输入路径继续使用可变时间版本，并增加跨多条 NIST 和俄罗斯标准曲线的自测试。代价是 P-256 和 P-384 共享密钥计算分别变慢约 14% 和 12%，且同函数中的坐标蒙哥马利阶梯仍可能受时序侧信道影响。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260928042641.307683-1-pawliczekerwin@gmail.com/

**▸ 组织：Kernel.org**（1 patches）

**[5.10.y,2/5] crypto: atmel-ecc - Struct headers need to start with keyword 'struct'**

- 日期：2026-09-02
- 状态：社区讨论中
- 作者邮箱：Sasha Levin <sashal@kernel.org>
- 概括：该补丁修正 Atmel ECC 加密驱动中结构体的内核文档标题格式，把缺少结构体关键字前缀的注释改为标准形式，消除开启额外编译警告时出现的“无法理解函数原型”提示，属于文档格式修复。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260902105322.2048136-2-sashal@kernel.org/

---

### ◆ 子系统：CAAM (NXP)（3 patches）

**▸ 组织：归属待核实（gondor.apana.org.au）**（1 patches）

**crypto: caam - Remove public key support**

- 日期：2026-09-04
- 状态：社区讨论中
- 作者邮箱：Herbert Xu <herbert@gondor.apana.org.au>
- 概括：CAAM驱动因长期无人维护且存在严重缺陷，现整体移除其公钥加密支持及相关源码文件，使该驱动不再提供公钥加密算法，防止这些未修复的缺陷被继续使用。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/appZMZ7WS-KNaHbc@gondor.apana.org.au/

**▸ 组织：归属待核实（solid-run.com）**（1 patches）

**[RFC,net-next,2/3] crypto: caam/qi2 - skip isolated CPUs when setting up queue pairs**

- 日期：2026-09-30
- 状态：社区讨论中
- 作者邮箱：Josua Mayer <josua@solid-run.com>
- 概括：当按受管中断类型隔离 CPU 时，CAAM 队列接口驱动不再遍历所有在线 CPU 建立队列对，只使用受管中断域内的在线 CPU 承担响应通知和 NAPI 轮询，避免在隔离 CPU 上缺失亲和 DPIO 而无限期推迟探测；隔离 CPU 仍可提交请求，响应由这些受管中断域内的 CPU 处理，并根据实际清理掩码启停 NAPI。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260930-dpaa2-isolcpus-v1-2-66c13f4fd75b@solid-run.com/

**▸ 组织：Individual Contributor**（1 patches）

**crypto: caam: jr: Use dedicated shutdown callback**

- 日期：2026-10-28
- 状态：社区讨论中
- 作者邮箱：Fabio Estevam <festevam@gmail.com>
- 概括：为 CAAM 作业环平台驱动增加独立的系统关闭回调。原关闭路径复用驱动移除函数，会检查是否仍有加密消费者持有引用，若有则拒绝关闭并打印设备忙警告，导致重启时出现告警。现在系统关闭时直接关闭硬件作业环，不再检查消费者引用和注销算法，而正常移除仍保留原检查，以区分系统关闭与驱动解绑。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261028132825.657546-1-festevam@gmail.com/

---

### ◆ 子系统：Talitos（2 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: talitos: request irq after tasklet_init()**

- 日期：2026-09-04
- 状态：社区讨论中
- 作者邮箱：Rosen Penev <rosenp@gmail.com>
- 概括：Talitos 加密驱动原先先注册中断处理程序，再初始化任务调度对象；如果在这段窗口内收到共享中断或前次传输完成中断，中断处理会调度尚未初始化的任务，可能引发异常。现在将中断注册移到任务初始化之后，避免未初始化任务被调度。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260904211230.81963-1-rosenp@gmail.com/

**▸ 组织：Bootlin**（1 patches）

**[SERIES] crypto: talitos - Driver cleanup** （cover letter，16/19 个 patch 达到代码量阈值）

- 日期：2026-10-13
- 状态：社区讨论中
- 作者邮箱：Paul Louvel <paul.louvel@bootlin.com>
- 概括：对 Talitos 安全引擎驱动进行结构性清理，将原来混杂在单文件中的哈希、对称加密、AEAD、随机数等实现拆分到独立文件，哈希改用内核块对齐接口去掉软件累积缓冲，统一迁移到新的算法回调接口并用宏减少重复声明，分离 SEC1 与 SEC2 硬件描述符定义以便阅读，同时补充维护者条目；属于纯重构，不改变对外功能和设备支持。
- 达到阈值的 patches（16 个，显示前 5）：
  - crypto: talitos - Move driver into dedicated directory
  - crypto: talitos/hash - Use CRYPTO_AHASH_BLOCK_ONLY API
  - crypto: talitos/hwrng - Move into separate file
  - crypto: talitos - Prepare crypto implementation file splitting
  - crypto: talitos/hash - Convert to {init,exit}_tfm type-specific API
  - ... 及其他 11 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261013-7-3-rc2_talitos_cleanup-v8-2-ca02be17696b@bootlin.com/

---

### ◆ 子系统：Aead（2 patches）

**▸ 组织：Qualcomm**（1 patches）

**[SERIES] crypto - qce: fix self-test issues in aead** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-10-20
- 状态：社区讨论中
- 作者邮箱：Bartosz Golaszewski <bartosz.golaszewski@oss.qualcomm.com>
- 概括：修复高通加密引擎AEAD自测试失败：将每次请求的软件回退判断从共享变换上下文改为局部变量，避免并发请求互相覆盖标志；对CCM模式中长度非块对齐或负载分散在多个散列表项的情况强制走软件回退，防止硬件引擎因等待完整输入而停滞。
- 达到阈值的 patches（3 个，显示前 5）：
  - crypto: qce - Use fallback for CCM with a fragmented payload
  - crypto: qce - Use a fallback for CCM with a partial final block
  - crypto: qce - Don't modify the TFM context for per-request fallback
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261020-qce-fixes-aead-v12-3-77a2e09abd0c@oss.qualcomm.com/

**▸ 组织：UnionTech**（1 patches）

**[SERIES] crypto: qce - fix CCM AAD buffer leak and the AEAD error paths** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-10-16
- 状态：社区讨论中
- 作者邮箱：赵金明 <zhaojinming@uniontech.com>
- 概括：修复高通 QCE 加密驱动在 CCM 模式带关联数据时的资源处理错误：错误路径原先释放了错误的源散列表映射，导致实际映射泄漏并可能用错误数量释放其他散列表；每个带关联数据的请求还会泄漏关联数据缓冲区；源散列表映射失败未被检测，可能继续对未映射的散列表执行释放。现在统一释放正确的映射并补上缓冲区释放，失败时直接返回输入输出错误，避免内存泄漏和错误释放操作。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: qce - check dma_map_sg() result for the source scatterlist
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261016-fix-qce-ccm-adata-leak-v1-2-f54a82af2de0@uniontech.com/

---

### ◆ 子系统：Skcipher（2 patches）

**▸ 组织：Qualcomm**（1 patches）

**[SERIES] crypto: qce - fix self-test issues in skcipher** （cover letter，3/4 个 patch 达到代码量阈值）

- 日期：2026-10-19
- 状态：社区讨论中
- 作者邮箱：Bartosz Golaszewski <bartosz.golaszewski@oss.qualcomm.com>
- 概括：高通 QCE 驱动修复自测试暴露的问题：AES-XTS 拒绝短于一个块的消息；AES-CTR 最后不完整块和跨多个散列表项的请求改由软件后备处理；弱密钥按 FIPS 模式返回无效错误或交由软件后备加密，不再无条件拒绝。
- 达到阈值的 patches（3 个，显示前 5）：
  - crypto: qce - Use a fallback for AES-CTR with a partial final block
  - crypto: qce - Use fallback for fragmented skcipher payloads
  - crypto: qce - Reject messages shorter than a block for AES-XTS
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261019-qce-fixes-skcipher-v12-2-046e6be9bd83@oss.qualcomm.com/

**▸ 组织：Amazon**（1 patches）

**[SERIES] crypto: skcipher - multi-data-unit request splitting** （cover letter，2/5 个 patch 达到代码量阈值）

- 日期：2026-09-24
- 状态：社区讨论中
- 作者邮箱：Leonid Ravich <lravich@amazon.com>
- 概括：为同步加密请求新增多数据单元支持，调用方可按固定单元大小一次提交多个数据单元，使用低 64 位小端计数器派生每单元初始向量；对不支持原生多单元的算法，API 层会透明拆成逐单元调用，设备映射加密在 plain64/essiv 等小端计数器场景下可将一段连续扇区合并为一个请求，输出与逐扇区处理完全一致。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: skcipher - split multi-unit requests in the API layer
  - crypto: testmgr - test multi-unit dispatch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260924075846.28203-2-lravich@amazon.com/

---

### ◆ 子系统：JitterEntropy（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: jitterentropy - add fast hardware jitter mixer extension**

- 日期：2026-09-13
- 状态：社区讨论中
- 作者邮箱：حنان المطيري <ha2020anan@gmail.com>
- 概括：为抖动熵子系统新增一个硬件抖动混合器扩展，利用高精度周期计数器和内存指针访问来扰动分支预测单元与硬件预取器，声称通过执行时间变化产生架构级微熵，且不依赖浮点运算；已在x86架构上测试。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/CANai08PJ9bKRn3JkgUP7SFHn+qXLoE_JDerRv-UtMkELZXu-wg@mail.gmail.com/

---

### ◆ 子系统：Public Key（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: pkcs7: Return no-digest for data-taking algorithms**

- 日期：2026-10-15
- 状态：社区讨论中
- 作者邮箱：Muhammad Mahdi Amirpour <ampr.mhd@gmail.com>
- 概括：在 PKCS7 签名验证获取摘要时，对直接消费原始数据的签名算法（目前为 ML-DSA）提前判定并返回无摘要错误。原来这类算法带认证属性时可能把属性缓冲区误当摘要返回给完整性校验调用方；现在统一不再生成中间摘要，使调用方按无摘要情况处理，避免错误使用。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261015110826.126621-1-ampr.mhd@gmail.com/

---

### ◆ 子系统：SPAcc（1 patches）

**▸ 组织：Vayavya Labs**（1 patches）

**[SERIES] crypto: spacc - Add SPAcc Crypto Driver** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-10-30
- 状态：社区讨论中
- 作者邮箱：Pavitrakumar Managutte <pavitrakumarm@vayavyalabs.com>
- 概括：为 Synopsys 安全协议加速器硬件加密引擎新增驱动程序，支持 SM4 的 CMAC/XCBC、MD5/SHA 系列、SHA3 等哈希算法，并能根据硬件配置自动检测可用算法，同时加入内核构建选项。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: spacc - Add SPAcc ahash support
  - crypto: spacc - add spacc autodetect support
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261030172456.274744-3-pavitrakumarm@vayavyalabs.com/

---

### ◆ 子系统：CESA (Marvell)（1 patches）

**▸ 组织：归属待核实（mandelbit.com）**（1 patches）

**[SERIES] crypto: safexcel: fix AEAD DMA mapping and cleanup** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-09-15
- 状态：社区讨论中
- 作者邮箱：Ralf Lici <ralf@mandelbit.com>
- 概括：修正 SafeXcel 驱动认证加密请求的 DMA 映射：跟踪已成功映射的散列表，错误清理时仅撤销成功映射，避免重复撤销；并按条目与输出范围的重叠设置准确 DMA 方向，防止非一致性系统上缓存回写可能覆盖相邻有效输出导致明文或密文损坏。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: safexcel - Map AEAD buffers with accurate DMA directions
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/7bd0c89dd32e9712d7d08393842498698148064b.1789469436.git.ralf@mandelbit.com/

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

*报告由 Linux Patches Tracker 自动生成 | 2026-11-11 16:29:30*
