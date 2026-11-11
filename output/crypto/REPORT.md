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
| 社区讨论中 | 70 | 54.7% |
| 已合入 | 48 | 37.5% |
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
| General Crypto | 72 | 56.2% |
| HWRNG | 22 | 17.2% |
| CAAM (NXP) | 7 | 5.5% |
| ECC | 5 | 3.9% |
| Skcipher | 5 | 3.9% |
| Talitos | 3 | 2.3% |
| CCP/SEV (AMD) | 2 | 1.6% |
| Public Key | 2 | 1.6% |
| Aead | 2 | 1.6% |
| JitterEntropy | 1 | 0.8% |
| Authenc | 1 | 0.8% |
| TCrypt | 1 | 0.8% |
| AF_ALG API | 1 | 0.8% |
| ICE (Qualcomm) | 1 | 0.8% |
| SPAcc | 1 | 0.8% |
| CESA (Marvell) | 1 | 0.8% |
| DRBG | 1 | 0.8% |

## 重点 Patch Top20 清单

### 已合入

| 厂商 | 简介 |
|------|------|
| Kernel.org | [PATCH v1 00/14] crypto: Remove the unnecessary crypto_rng API ------内核加密子系统原先通过一个过度通用的随机数算法接口来使用确定性随机位生成器和抖动熵源，造成多余抽象，且抖动熵源在启动时执行昂贵健康检查。该系列移除这个接口，改为库函数直接调用：确定性随机位生成器增加库接口和内置自检，抖动熵源健康检查推迟到首次使用；内核加密套接字接口的随机数算法改用库函数保留原有行为；标准随机数获取直接调用确定性随机位生成器。最终内核加密算法列表不再列出该算法，但相关功能仍可通过随机数用户接口和标准随机数接口使用。 |
| Intel | [PATCH v1 00/2] crypto: qat - fix config table locking ------Intel QAT 配置子系统中，配置段查找和调试读取原先未与删除路径同步，设备关闭、移除或更新键值并发时可能访问已释放内存。现在查找、插入和读取期间持有设备配置读写锁，并简化键值添加路径为直接复用首次找到的条目，移除冗余列表遍历与临时缓冲，纯流程整理无功能变化。 |
| Kernel.org | [PATCH v1 00/3] crypto: atmel-tdes - use separate DMA scatterlists ------Atmel TDES 加密驱动将 DMA 输入输出散列表由数组改为两个独立散列表，直接采用 4 字节从设备总线宽度，启动路径复用已有的快速模式判断，并在 DMA 初始化时合并错误清理路径，使数据结构和错误处理流程更简单。这是纯重构，不改变算法行为。 |
| Kernel.org | [PATCH v1 00/2] hwrng: virtio - use min() in copy_data() ------虚拟输入输出随机数生成器驱动在探测时改用带长度限制的格式化函数生成设备名，降低无界写入风险；复制数据时改用更简洁且类型兼容的取最小值写法，不改变既有行为。 |
| 归属待核实（free.fr） | [v2] crypto: caam/qi2 - lower the algorithm priority ------针对NXP CAAM队列接口加密加速器，将其算法优先级从2000降至100，避免默认算法选择时该硬件实现因过高优先级而过度抢占其他实现，与英特尔QAT加速器处理方式一致。按驱动名仍可访问该加速器，用户空间可通过算法配置接口提高其优先级。 |
| Individual Contributor | [v2] crypto: qat - zero the VF migration state buffer on save ------针对英特尔QAT设备虚拟功能迁移状态保存，修复状态缓冲区未清零导致的信息残留问题。原实现只写入序列化的各个区段，未使用的尾部仍保留分配时的堆旧数据或前次迁移数据，用户空间读取完整状态时可能获得这些残留。现在首次保存设置前清零整个缓冲区，之后每次保存状态前清零设置区后的剩余区域，防止陈旧数据泄露。 |
| Kernel.org | [PATCH] crypto: x86/aria - Take the address of each asm function in one file ------针对x86平台ARIA加密算法的AVX系列汇编实现，在使用Clang全链接时优化和控制流完整性检查构建时，多个目标文件分别获取同一汇编函数地址会导致符号被链接器误删，造成未定义符号链接失败。现在将每个汇编函数的地址获取集中到其所属层级的唯一文件中，再由各分发表统一填充，避免重复获取，使符号得以保留并正常链接；新版编译器已修复该问题，但该改动对旧版是必要绕开。 |
| Intel | [1/2] crypto: qat - initialise state_lock on every path in adf_devmgr_add_dev() ------Intel QAT 加速器设备管理中，当虚拟功能在之前已使用过的总线设备功能号上重建时，设备管理器会提前返回，导致状态互斥锁未初始化；随后设备启用或关闭时可能触发未初始化互斥体调试警告。现将初始化移到更新表之前，确保每条路径都完成初始化，修复虚拟功能重建场景下的锁状态问题。 |
| Kernel.org | [PATCH] crypto: sa2ul - Fix HMAC key preparation ------德州仪器 SA2UL 加密加速器在准备 HMAC 密钥时存在一字节越界写入，影响 SHA-256 情况，且从未支持超过 64 字节的密钥。现改为直接调用内核加密库中的 HMAC 密钥准备函数生成内外填充状态，不再手工构造，并移除间接调用，修复这些缺陷。 |
| Infradead Community | [v2] crypto: ccp: psp-sev.h: clean up kernel-doc warnings ------针对 AMD 安全处理器中 SEV 平台及客户机管理命令的接口文档，修正了错误的文档注释标记、补充多个保留字段说明，并将两组容易混淆的结构体名称和成员名更正。这些调整使内核文档生成不再产生大量警告，接口说明与结构体成员保持一致。 |
| Individual Contributor | [v4] crypto: talitos: init tasklets before requesting IRQs ------Talitos 加密引擎驱动原先在请求中断后才初始化软中断任务，若请求中断时已有由引导加载程序或 kexec 内核留下的挂起中断，会调度回调为空的任务。现将中断号查询和寄存器映射提前至资源分配前，先完成通道队列分配、引擎复位和软中断任务初始化，最后才请求中断；同时修正错误路径中对未请求中断的释放。从而避免启动阶段空回调调度与错误释放。 |
| Individual Contributor | [v4] crypto/amlogic: Use devm APIs for clock management ------Amlogic GXL 加密引擎驱动原先手动获取并启用总线时钟，需要在失败和移除时手动关闭；现改为使用设备管理的获取并启用时钟接口，由内核自动完成时钟使能与禁用，删除了手动清理调用，使探测流程更简洁，减少错误路径遗漏时钟释放的可能。 |
| AMD | [v3,1/1] crypto: ccp - Make usage of sev_cmd_mutex more granular ------AMD 安全处理器 SEV 固件输入输出控制接口原先在入口处持有互斥锁，包裹了可能耗时的用户态缓冲区拷贝等准备操作，该过程可能发生缺页并带来理论死锁风险，尤其与未来客户机内存页在共享与私有状态之间原地转换相关。现在将互斥锁下放到各命令内部，仅在平台状态迁移和固件命令执行时加锁，显著缩小持锁范围，消除这些用户态拷贝引发理论死锁的隐患。 |
| ANSSI | [v2] crypto: ecc - Handle exceptional points in Shamir multiplication ------椭圆曲线 Shamir 乘法原先不能正确处理相同点、相反点及无穷远点，导致有效 ECDSA 签名被内核错误拒绝，并可能在公钥等于基点或其相反点时接受无效签名，已错误拒绝 16 个 Wycheproof 有效向量。现在在预计算和累加过程中显式处理倍点、相消和无穷远点，并补充回归测试，使签名验证结果恢复正常。 |
| 归属待核实（gondor.apana.org.au） | [RESEND] hwrng: cctrng - Discard pm_runtime_put_autosuspend() return value ------某个硬件随机数发生器驱动原先会对运行时电源管理自动挂起释放接口的非零返回值打印错误信息，但该非零值只表示没有排队定时器或工作项去检查挂起，属于常见且合理的状态，例如向设备的运行时电源管理控制属性写入开启值之后。现在直接丢弃返回值不再告警，避免误导性错误日志，并为该接口将来改为无返回值做好准备。 |
| Kernel.org | [PATCH] hwrng: amd - use PMBASE_OFFSET consistently ------AMD 硬件随机数驱动在申请 I/O 区域时对电源管理基址偏移使用硬编码数值，现在统一改用现有宏表示；同时补上 I/O 映射失败错误消息中缺少的空格，提升代码一致性和错误信息可读性。 |
| Kernel.org | [PATCH] hwrng: intel - simplify intel_rng_mod_init() ------将 Intel 82802 硬件随机数驱动的初始化流程改为各错误分支直接返回错误码，移除用于统一跳转的变量和出口标签，使模块加载失败处理更直接，功能行为不变。 |
| Kernel.org | [PATCH] hwrng: cctrng - simplify cctrng_probe() ------调整 ARM cctrng 硬件随机数驱动的探针错误处理，注册失败时直接执行电源管理清理并返回错误，删除跳转标签，简化控制流，不改变功能。 |
| Individual Contributor | [PATCH] crypto: algif_skcipher: rewind rounded output bytes ------修复内核加密套接字接口在分段请求中的长度处理缺陷：接收迭代器按未对齐长度前进，而实际处理长度向下取整到块大小却没有回退，后续块可能从上一页面生命周期读取并暴露陈旧字节，使用无特权 XTS 模式 AES 可复现。现在在处理前回退被舍入的尾部，使返回长度与迭代器位置一致，封堵该泄露途径。 |
| Kernel.org | [PATCH] hwrng: amd - simplify control flow in amd_rng_mod_init() ------简化 AMD 768 硬件随机数驱动初始化中的设备查找流程，用循环内跳出并在循环后判空替代跳转标签，同时合并错误清理出口，使模块加载控制流更清晰，功能行为不变。 |

### 社区讨论

| 厂商 | 简介 |
|------|------|
| Bootlin | [PATCH v8 00/20] crypto: talitos - Driver cleanup ------对 Talitos 安全引擎驱动做纯结构清理：将原先集中在单一实现中的哈希、对称加密、AEAD 和硬件随机数拆分为各自文件；哈希改用内核块级接口，去掉自行拼接部分块的缓冲逻辑；用宏统一定义各类算法模板，并用静态键助手区分 SEC1 与 SEC2 硬件版本，同时把两代描述符和指针布局分离为独立结构。还新增了维护者条目。 |
| Rambus | [PATCH v5 00/19] crypto: cmh - add Rambus CryptoManager Hub driver ------新增 Rambus CryptoManager Hub 硬件加密加速器驱动，通过邮箱虚拟命令队列提交异步请求，向内核加密接口注册 SHA-2/SHA-3/SHAKE、SM3、HMAC、AES/SM4 系列、ChaCha20-Poly1305、RSA、ECDSA/SM2、X25519 及多种后量子签名和密钥封装算法，并提供 DRBG 硬件随机数。 |
| Kernel.org | [PATCH v2 00/20] Migrate x86 and RISC-V accelerated AES modes into library ------将x86和RISC-V架构的多种AES模式算法（包括ECB、CBC、CTR、XTS等）迁移到通用加密库，并新增AES-NI优化与AVX迁移，移除原有架构特定实现。这使传统crypto API能直接使用库中的加速代码，避免模板优先级问题导致性能回退，同时保持32位和64位支持。 |
| Red Hat | [PATCH v4 00/13] libcrypto: Provide more __cleanup functions for zeroizing data ------为内核加密库中的 AES、AES-XTS、AES-GCM、AES-CCM、MD5、SM3、BLAKE2、SHA-1、SHA-2 等密钥和上下文结构提供显式清零辅助函数，可配合自动清理在作用域结束时擦除敏感数据，并替换库内原有手动清零调用；新增清零规范文档。可信密钥和 SMB 客户端改用这些辅助函数，x86 引导过渡代码编译时禁用加固字符串宏以解决头文件冲突。 |
| Texas Instruments | [PATCH v10 00/15] Fix several issues in DTHEv2 driver ------修复德州仪器 DTHEv2 加密引擎驱动的多个缺陷：空设备列表可能被误当有效条目，软中断锁竞争可能死锁，高内存页访问可致内存破坏，设备移除时在途请求可能访问已释放数据，AES 散射列表长度不匹配会使 DMA 超时崩溃，AEAD 标签操作存在缓存一致性时序问题；同时补齐错误路径的 DMA 清理，并仅在内存不足时才回退软件。 |
| Vayavya Labs | [PATCH v27 00/4] crypto: spacc - Add SPAcc Crypto Driver ------为 Synopsys SPAcc 硬件加密引擎新增驱动，支持 SHA、MD5 等多种哈希和带密钥哈希算法，并可自动检测硬件支持的算法，适用于集成该 IP 的平台，使内核能够调用其硬件加速哈希运算。 |
| Texas Instruments | [PATCH v1 00/30] Clean and improve SA2UL driver ------清理并修复德州仪器 SA2UL 驱动：删除大量未使用的代码、字段和宏，修正错误路径中的安全上下文、哈希资源及 DMA 映射泄漏；释放安全上下文前显式擦除密钥和状态，降低信息残留风险；修复导出哈希中间状态时栈缓冲区过小造成的越界，以及并发更新密钥可能破坏在途请求命令标签的问题，并按算法需求动态计算元数据长度。 |
| AMD | [PATCH v5 00/7] Implement SNP live firmware update support ------为 AMD 的 SEV-SNP 安全虚拟化功能增加固件实时更新：通过固件加载接口上传新固件，使用下载固件扩展命令；若传统安全加密虚拟化平台正在运行客户机则返回忙碌并拒绝更新，若仅处于初始化状态则先关闭平台并释放固件占用的缓冲，更新后再恢复，SNP 客户机不中断。固件先暂存，管理员可通过后续命令决定是否永久提交，也可重新上传旧镜像回滚。 |
| Texas Instruments | [PATCH v9 00/2] Add support for hashing algorithms in TI DTHE V2 ------为德州仪器 DTHE V2 硬件加密引擎的哈希引擎增加 SHA-224/256/384/512 和对应 HMAC 算法支持，使原本主要处理对称运算的硬件还能卸载摘要和带密钥的消息认证计算，适用于需要完整性校验或 HMAC 的 TI 平台场景。 |
| 归属待核实（mandelbit.com） | [PATCH v1 00/2] lib/crypto: x86/chacha: Add 16-block AVX-512 implementation ------为x86的ChaCha流密码新增16块AVX-512实现，一次处理1024字节，利用512位寄存器提高并行度，在支持AVX-512VL的CPU上用于超过8块的长输入（除非设置避免512位寄存器降频）。在AMD Zen 5上1024字节吞吐量从5168提升到10168 MB/s。同时增加KUnit测试和基准，覆盖长度、对齐、页边界及计数器回绕。 |
| 归属待核实（ptudor.net） | [PATCH v1 00/3] hwrng: add Microchip RNG90 support ------新增Microchip RNG90 I2C硬件随机数生成器驱动：上电唤醒并识别设备，构造信息读取和随机数命令，校验响应长度和CRC，处理设备自检失败而不暴露不合格输出。因数据表未量化每输出位熵，默认使用最小非零熵质量，可在系统验证后通过sysfs调整。同时提供32个KUnit测试用例覆盖命令帧、恢复、挂起等。 |
| Kernel.org | [PATCH v1 00/3] AES library fixups ------修复x86 AES库的两个问题并提高兼容性：显式设置CBC加密中的密钥寄存器别名，避免依赖前一函数遗留状态；将库版AES分组模式优先级从300提高到500，防止已被替代的ccp和padlock驱动错误覆盖AES-NI/VAES实现。同时让AES-NI配置项自动选择所需算法，确保启用LUKS/dm-crypt的系统仍能获得必要支持。 |
| Kernel.org | [PATCH] lib/crypto: powerpc/poly1305: Remove BROKEN implementation ------删除已标记为损坏超过一年的 PowerPC Poly1305 加速实现。该实现在软中断上下文不可用，且汇编逻辑存在进位丢失等问题导致部分输入计算结果错误，还含有依赖秘密数据的分支；删除后 PowerPC 回退到通用 Poly1305 实现，待修正版本再考虑。 |
| 浙江大学 | [v2] crypto: ccp - Fix use-after-free in backlog cmd advancement ------修复 CCP 加密协处理器驱动中积压命令提升的释放后使用问题：原实现先由队列线程取出积压命令，稍后由工作队列重新入队，期间命令不在任何列表，设备销毁时刷新无法触达，工作队列会在设备释放后继续使用，且预留空间可能被并发提交占用。现在在出队时同锁转移空闲槽位，由队列内核线程完成推进回调，并在拆除前标记停止，避免唤醒已停止线程。 |
| Kernel.org | [PATCH] crypto: arc4 - Remove obsolete crypto API support for ARC4 ------ARC4 的内核用户已直接使用库实现，旧加密 API 封装也被标记废弃多年，并已从默认套接字加密允许列表中移除。该补丁删除这套过时的 ARC4 加密接口和对应测试示例，避免继续暴露不安全的算法入口；内核中仍保留 ARC4 库实现，以支持某些遗留协议。 |
| 归属待核实（gondor.apana.org.au） | [PATCH] crypto: caam - Remove public key support ------移除 CAAM 驱动中多年未维护且存在严重问题的公钥加密支持。此前该部分仍在内核中提供 RSA 等公钥操作，但缺乏维护；删除后相关硬件公钥算法不再通过内核加密接口暴露，以避免继续使用这些存在缺陷的代码路径，驱动的其他加密功能不受影响。 |
| 归属待核实（itx.no） | [v3] lib/crypto: sparc/aes-xts: Add optimization using the AES opcodes ------为 SPARC 平台的 AES 磁盘加密模式增加硬件加速：利用处理器内置 AES 指令和 VIS3 向量指令扩展的 128 位移位操作处理 128 位和 256 位密钥的加密与解密，每次迭代处理两个数据块；192 位密钥和未按 8 字节对齐的数据继续由通用代码处理。优化后，内核加密套接字接口在 T7-1 上 256 位密钥吞吐从 390 提升到 936 MiB/s，T4-1 上从 238 提升到 544，内存盘上的顺序读写也明显提高。 |
| Intel | [PATCH] crypto: qat - add support for enhanced decompression mode on GEN6 devices ------为Intel QAT GEN6设备增加增强解压模式：允许固件利用压缩引擎内嵌的解压引擎处理普通解压请求，绕过压缩和转换阶段，从而提高解压吞吐量且不影响同时进行压缩。该模式通过新的sysfs属性控制，写入后立即生效并跨上下电和配置变更持久化；默认在仅配置解压服务时启用。 |
| 归属待核实（gondor.apana.org.au） | [PATCH] crypto: aes - Add import_core/export_core to cmac/xcbc/cbcmac ------修正AES的CMAC、XCBC和CBC-MAC实现的导出导入格式，使其与通用模板一致。原先这些库版消息认证码的状态导出与通用模板不匹配，且在CMAC和XCBC中未完整保留被暂存的块；现在导出时额外执行一次加密以保存该块信息，导入时正确恢复部分块状态，避免状态信息丢失。 |
| Individual Contributor | [PATCH] crypto: jitterentropy - add fast hardware jitter mixer extension ------为抖动熵子系统新增快速硬件抖动混合扩展：利用高精度周期计数器和内存指针属性扰动分支预测单元与硬件预取器，通过执行时间变化产生架构微熵，不依赖浮点运算，兼容内核空间。该扩展在x86上测试，用于生成熵序列，但代码中注明非加密用途。 |

---

## 已合入 Patches

### ◆ 子系统：General Crypto（21 patches）

**▸ 组织：Kernel.org**（7 patches）

**crypto: x86/aria - Take the address of each asm function in one file**

- 日期：2026-10-12
- 状态：已合入
- 作者邮箱：Kees Cook <kees@kernel.org>
- 概括：针对x86平台ARIA加密算法的AVX系列汇编实现，在使用Clang全链接时优化和控制流完整性检查构建时，多个目标文件分别获取同一汇编函数地址会导致符号被链接器误删，造成未定义符号链接失败。现在将每个汇编函数的地址获取集中到其所属层级的唯一文件中，再由各分发表统一填充，避免重复获取，使符号得以保留并正常链接；新版编译器已修复该问题，但该改动对旧版是必要绕开。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261012031920.i.329-kees@kernel.org/

**[SERIES] crypto: atmel-tdes - use separate DMA scatterlists** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-10-11
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：Atmel TDES 加密驱动的 DMA 路径原先用包含输入和输出两项的 scatterlist 数组配置传输，现改为两个独立的输入、输出 scatterlist 变量，地址宽度直接使用 4 字节常量。启动加密时复用已有的快速模式布尔变量，不再重复检查标志；DMA 初始化失败时合并重复的错误处理分支，并在获取接收通道失败时立即释放已取得的发送通道。这些是纯代码整理，运行行为不变，使流程更直观并减少重复判断。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: atmel-tdes - use separate DMA scatterlists
  - crypto: atmel-tdes - reuse fast in atmel_tdes_crypt_start()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261011131556.272382-4-blum@kernel.org/

**crypto: sa2ul - Fix HMAC key preparation**

- 日期：2026-09-23
- 状态：已合入
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：德州仪器 SA2UL 加密加速器在准备 HMAC 密钥时存在一字节越界写入，影响 SHA-256 情况，且从未支持超过 64 字节的密钥。现改为直接调用内核加密库中的 HMAC 密钥准备函数生成内外填充状态，不再手工构造，并移除间接调用，修复这些缺陷。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260923051116.92741-1-ebiggers@kernel.org/

**[SERIES] crypto: cast5 - use memcpy_and_pad() in cast5_setkey()** （cover letter，5/5 个 patch 达到代码量阈值）

- 日期：2026-09-21
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：将CAST5、CAST6、IXP4XX以及Marvell Octeontx/Octeontx2驱动中密钥或HMAC填充的“先复制再清零剩余空间”写法统一替换为复制加填充接口，减少成对调用，简化密钥设置和初始化流程，行为不变。
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
- 概括：Atmel TDES 驱动的外设数据控制器和 DMA 两种传输执行函数原先各自保存传输长度并在非快速路径同步缓冲区，还通过参数传递长度。本次把保存长度和缓冲区同步统一放到传输启动函数中，两个执行函数直接读取设备结构中的长度，去掉了重复代码和冗余参数，流程更集中，实际传输与同步操作不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260916171659.129009-3-blum@kernel.org/

**crypto: xilinx - clear AES key buffer before freeing it**

- 日期：2026-09-08
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：针对 Xilinx ZynqMP AES-GCM 加密卸载引擎的算法上下文释放过程，原先直接释放存放 AES 密钥的缓冲区，密钥内容可能残留在内存中。现在改用敏感数据释放函数，在释放前清除缓冲区内容，降低密钥材料残留和被后续读取的风险。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260908191607.405177-2-blum@kernel.org/

**crypto: atmel-tdes - simplify DMA buffer initialization**

- 日期：2026-09-03
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：Atmel TDES 加密驱动的 DMA 缓冲区初始化流程被简化：缓冲区长度按 DES 块大小对齐的计算合并为一条语句，输入、输出缓冲区的 DMA 映射错误处理合并到公共路径，并在输出映射失败时先取消已映射的输入缓冲区；同时将部分调试日志改为错误日志并调整长度打印格式。整体属于流程整理，映射与清理行为保持不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260903210845.162790-2-blum@kernel.org/

**▸ 组织：Individual Contributor**（6 patches）

**[SERIES] crypto: Use pm_runtime_resume_and_get()** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-09-22
- 状态：已合入
- 作者邮箱：Bui Duc Phuc <phucduc.bui@gmail.com>
- 概括：三款不同平台的硬件加密引擎（全志、CCREE、SL3516）在初始化加密上下文或随机数读取时，原先手动调用运行时电源管理获取并在失败后清理引用计数。这些补丁改为直接调用内核提供的合并接口，由该接口在失败路径内部完成引用计数回落，去掉重复的清理代码。属于纯代码整理，不改变运行行为，只是让电源管理错误处理更统一、不易遗漏。
- 达到阈值的 patches（3 个，显示前 5）：
  - crypto: sun8i-ss - Use pm_runtime_resume_and_get()
  - crypto: ccree - Use pm_runtime_resume_and_get()
  - crypto: sl3516 - Use pm_runtime_resume_and_get()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260922031954.320895-2-phucduc.bui@gmail.com/

**crypto: ccp: kill v3 IRQ tasklet during teardown**

- 日期：2026-09-20
- 状态：已合入
- 作者邮箱：Jiale Yao <yaojiale02@163.com>
- 概括：AMD 加密协处理器 v3 在使用消息信号中断扩展时，中断处理会调度软中断任务完成后续工作。原来的初始化失败路径和设备销毁流程在释放中断后没有等待已排队的软中断任务结束，它可能在内核释放设备管理内存后继续访问设备结构。现在这两条路径在释放中断后都会终止软中断任务，消除释放后访问的风险。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260920173407.2126086-1-yaojiale02@163.com/

**crypto: ccp: kill v5 IRQ tasklet during teardown**

- 日期：2026-09-20
- 状态：已合入
- 作者邮箱：Jiale Yao <yaojiale02@163.com>
- 概括：针对使用 MSI-X 中断的 AMD CCP v5 加密协处理器，初始化失败或销毁释放中断时，已排队的中断下半部任务未等待结束，可能在设备内存被释放后继续访问，存在释放后访问风险。现改为释放中断后同步终止该任务，避免任务在设备释放后执行。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260920173417.2126346-1-yaojiale02@163.com/

**[v2] crypto: qat - zero the VF migration state buffer on save**

- 日期：2026-09-19
- 状态：已合入
- 作者邮箱：Karl Mehltretter <kmehltretter@gmail.com>
- 概括：针对英特尔QAT设备虚拟功能迁移状态保存，修复状态缓冲区未清零导致的信息残留问题。原实现只写入序列化的各个区段，未使用的尾部仍保留分配时的堆旧数据或前次迁移数据，用户空间读取完整状态时可能获得这些残留。现在首次保存设置前清零整个缓冲区，之后每次保存状态前清零设置区后的剩余区域，防止陈旧数据泄露。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260919054934.27322-1-kmehltretter@gmail.com/

**[v4] crypto/amlogic: Use devm APIs for clock management**

- 日期：2026-09-16
- 状态：已合入
- 作者邮箱：Mohamad Raizudeen <raizudeen.kerneldev@gmail.com>
- 概括：Amlogic GXL 加密引擎驱动原先手动获取并启用总线时钟，需要在失败和移除时手动关闭；现改为使用设备管理的获取并启用时钟接口，由内核自动完成时钟使能与禁用，删除了手动清理调用，使探测流程更简洁，减少错误路径遗漏时钟释放的可能。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260916174227.5581-1-raizudeen.kerneldev@gmail.com/

**crypto: amcc: trng: use int for ppc4xx_trng_probe()**

- 日期：2026-09-04
- 状态：已合入
- 作者邮箱：Rosen Penev <rosenp@gmail.com>
- 概括：将 AMCC PPC4xx 加密加速器中的真随机数生成器探测函数从无返回值改为返回错误码，使探测失败能够传回主设备探测流程；主流程在随机数生成器失败时新增跳转路径，先注销此前已注册的加密算法再执行通用错误清理。随机数生成器仍为可选功能，设备树中不存在或不可用时直接返回成功，不阻塞主加密设备加载。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260904230144.127071-1-rosenp@gmail.com/

**▸ 组织：Intel**（3 patches）

**[SERIES] crypto: qat - fix mutex lifetimes in the device manager** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-10-06
- 状态：已合入
- 作者邮箱：Ahsan Atta <ahsan.atta@intel.com>
- 概括：英特尔 QuickAssist 设备管理中，状态锁原先在函数末尾初始化，但 VF 在宿主机上重建且映射已存在时会提前返回，导致新分配的设备带着未初始化的互斥锁进入上下电流程，调试锁检测会告警；现已把初始化前移到表更新之前的所有路径。另外，VF 到 PF 通信锁原先在设备关闭时销毁，但关闭完成后还要发送重启完成消息，PF 重启会访问已销毁锁；现把该锁生命周期绑定到加速设备，在添加时初始化、移除时销毁，避免在设备上下电之外使用无效锁。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: qat - initialise state_lock on every path in adf_devmgr_add_dev()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261006150649.2517748-2-ahsan.atta@intel.com/

**crypto: qat - force an edge when re-enabling all VF2PF interrupts**

- 日期：2026-09-29
- 状态：已合入
- 作者邮箱：George Abraham P <george.abraham.p@intel.com>
- 概括：Intel QuickAssist 设备复位或高级错误恢复期间，物理功能被复位而虚拟功能仍存活，屏蔽寄存器会被硬件恢复为未屏蔽状态；之后重新使能虚拟功能到物理功能中断时，直接解除屏蔽不产生边沿，导致复位前虚拟功能锁存的消息无法投递。现在在解除屏蔽前先屏蔽所有源，强制产生由屏蔽到未屏蔽的跳变，使复位期间挂起的消息能被重新触发投递。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260929083837.2102260-1-george.abraham.p@intel.com/

**[SERIES] crypto: qat - fix config table locking** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-09-18
- 状态：已合入
- 作者邮箱：Ahsan Atta <ahsan.atta@intel.com>
- 概括：Intel QAT 配置子系统中，配置段查找和调试读取原先未与删除路径同步，设备关闭、移除或更新键值并发时可能访问已释放内存。现在查找、插入和读取期间持有设备配置读写锁，并简化键值添加路径为直接复用首次找到的条目，移除冗余列表遍历与临时缓冲，纯流程整理无功能变化。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: qat - hold cfg->lock when accessing config sections
  - crypto: qat - avoid redundant config list walks when adding a key
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260918124112.537571-2-ahsan.atta@intel.com/

**▸ 组织：Infradead Community**（2 patches）

**[v2] crypto: ccp: psp-sev.h: clean up kernel-doc warnings**

- 日期：2026-09-18
- 状态：已合入
- 作者邮箱：Randy Dunlap <rdunlap@infradead.org>
- 概括：针对 AMD 安全处理器中 SEV 平台及客户机管理命令的接口文档，修正了错误的文档注释标记、补充多个保留字段说明，并将两组容易混淆的结构体名称和成员名更正。这些调整使内核文档生成不再产生大量警告，接口说明与结构体成员保持一致。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260918232736.3095763-1-rdunlap@infradead.org/

**crypto: ccp.h - repair all kernel-doc comments**

- 日期：2026-09-01
- 状态：已合入
- 作者邮箱：Randy Dunlap <rdunlap@infradead.org>
- 概括：为 CCP 加密协处理器的公共头文件全面修复内核文档注释：增补缺失的返回值说明、枚举类型关键字、枚举值和结构体成员描述，并采用嵌套结构注释格式。修复后消除了内核文档检查产生的大量警告，使相关接口的 API 文档能够正常生成，代码逻辑未发生变化。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260901185438.31038-1-rdunlap@infradead.org/

**▸ 组织：东南大学**（1 patches）

**crypto: atmel-sha: reject initialization without a device**

- 日期：2026-09-13
- 状态：已合入
- 作者邮箱：Slavin Liu <bolin.liu@seu.edu.cn>
- 概括：Atmel SHA1/SHA256 驱动初始化哈希请求时，需要从驱动列表查找设备；如果最后一个设备已被移除，查找结果为空。原代码仍继续执行，并在调试输出中访问空设备指针。现在在查找不到设备时直接返回设备不存在错误，让初始化在访问设备前失败，避免空指针解引用。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260913125143.109897-1-bolin.liu@seu.edu.cn/

**▸ 组织：Google**（1 patches）

**crypto: hisilicon/qm - annotate cap_tables with __counted_by_ptr**

- 日期：2026-09-23
- 状态：已合入
- 作者邮箱：Bill Wendling <morbo@google.com>
- 概括：为海思硬件加速器能力表指针添加计数属性，使编译器和动态边界检查工具能够把指针与其容量字段关联，从而发现越界访问。初始化路径改为先设置容量字段再设置指针，避免出现指针已赋值但计数为零或未初始化的瞬时状态。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260923060114.2605310-1-morbo@google.com/

**▸ 组织：Huawei**（1 patches）

**[SERIES] crypto: hisilicon/hpre - misc fixes and cleanups** （cover letter，1/7 个 patch 达到代码量阈值）

- 日期：2026-09-18
- 状态：已合入
- 作者邮箱：Weili Qian <qianweili@huawei.com>
- 概括：华为HPRE加速器修复：ECDH输出缓冲区过小返回无效参数，改为返回溢出错误使调用方可扩容；一致性内存分配此前硬编码GFP，可能在原子上下文睡眠或内存压力下失败，改为依据请求是否允许睡眠动态选择；调整前导零去除先检查长度，避免零长度越界读；按硬件实际传输长度映射ECDH输出，删除对空指针的一致性释放死代码，并清理未用宏、字段及重复簇数量计算。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: hisilicon/hpre - extract clusters num into inline function
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260918122726.3014899-4-qianweili@huawei.com/

---

### ◆ 子系统：HWRNG（14 patches）

**▸ 组织：Kernel.org**（12 patches）

**hwrng: amd - use PMBASE_OFFSET consistently**

- 日期：2026-10-08
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：AMD 硬件随机数驱动在申请 I/O 区域时对电源管理基址偏移使用硬编码数值，现在统一改用现有宏表示；同时补上 I/O 映射失败错误消息中缺少的空格，提升代码一致性和错误信息可读性。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261008093737.180712-2-blum@kernel.org/

**hwrng: intel - simplify intel_rng_mod_init()**

- 日期：2026-10-06
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：将 Intel 82802 硬件随机数驱动的初始化流程改为各错误分支直接返回错误码，移除用于统一跳转的变量和出口标签，使模块加载失败处理更直接，功能行为不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261006172628.103594-2-blum@kernel.org/

**hwrng: cctrng - simplify cctrng_probe()**

- 日期：2026-10-06
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：调整 ARM cctrng 硬件随机数驱动的探针错误处理，注册失败时直接执行电源管理清理并返回错误，删除跳转标签，简化控制流，不改变功能。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261006202734.104415-2-blum@kernel.org/

**hwrng: amd - simplify control flow in amd_rng_mod_init()**

- 日期：2026-10-02
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：简化 AMD 768 硬件随机数驱动初始化中的设备查找流程，用循环内跳出并在循环后判空替代跳转标签，同时合并错误清理出口，使模块加载控制流更清晰，功能行为不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261002141952.169528-2-blum@kernel.org/

**hwrng: stm32 - use devm_platform_ioremap_resource() in stm32_rng_probe()**

- 日期：2026-10-02
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：STM32 随机数发生器在探测映射寄存器时，原先获取资源并映射的流程返回了未使用的资源指针，现改用直接映射平台资源的接口并删除多余局部变量，简化代码。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261002144839.51627-3-blum@kernel.org/

**hwrng: stm32 - use swap() in stm32_rng_probe()**

- 日期：2026-10-01
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：STM32 硬件随机数发生器驱动在探测多个时钟时，原先手动交换两个时钟条目的标识和指针，现改用内核交换操作完成相同处理，仅简化代码流程，不改变功能。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261001210450.37467-2-blum@kernel.org/

**hwrng: stm32 - reuse clock rate in stm32_rng_clock_freq_restrain()**

- 日期：2026-10-01
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：STM32 随机数发生器在限制时钟频率时，原先调试打印又会重新读取一次时钟频率，现改为复用已经取得的时钟速率，并调整调试输出的格式，避免重复获取时钟。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261001211612.38124-2-blum@kernel.org/

**hwrng: atmel - use HZ_PER_MHZ in atmel_trng_init()**

- 日期：2026-09-29
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：Atmel 硬件随机数发生器初始化时，原先用单独的局部变量保存时钟频率，并和硬编码的一亿赫兹比较，超过阈值就设置半速率标志。现在合并为直接的条件判断，并用每兆赫兹常数替代硬编码频率，简化了初始化流程，实际判断行为保持不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260929213751.103658-3-blum@kernel.org/

**[SERIES] hwrng: virtio - use min() in copy_data()** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-09-26
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：虚拟输入输出随机数生成器驱动在探测时改用带长度限制的格式化函数生成设备名，降低无界写入风险；复制数据时改用更简洁且类型兼容的取最小值写法，不改变既有行为。
- 达到阈值的 patches（2 个，显示前 5）：
  - hwrng: virtio - use min() in copy_data()
  - hwrng: virtio - use snprintf() in probe_common()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260926055853.4868-3-blum@kernel.org/

**hwrng: core - reject unknown RNG names**

- 日期：2026-09-24
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：用户通过 sysfs 接口为硬件随机数框架切换当前随机数源时，如果填写了不存在的名称，原来的接口会错误地返回成功，但实际并未切换随机数源。现在在查找前预设设备不存在的错误码，找不到对应名称时向用户返回错误，避免静默失败。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260924212114.120633-2-blum@kernel.org/

**hwrng: intel - declare warning string as const**

- 日期：2026-09-23
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：Intel 硬件随机数驱动在检测到固件空间只读锁定时输出的提示字符串在初始化后不再修改，现将其声明为只读并放入初始化专用只读段，同时调整缩进，不改变功能。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260923104237.82599-2-blum@kernel.org/

**hwrng: amd - report partial reads in non-blocking mode**

- 日期：2026-09-23
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：AMD 硬件随机数发生器在非阻塞读取模式下，如果已经向调用方缓冲区复制了部分随机数但后续没有更多数据，原来的读取函数会返回 0，导致已复制的字节无法被正确上报。现在改为返回实际已复制的字节数，使部分读取结果能够正常返回给调用者。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260923201259.90336-2-blum@kernel.org/

**▸ 组织：Individual Contributor**（1 patches）

**hwrng: omap3-rom: Use pm_runtime_resume_and_get()**

- 日期：2026-09-22
- 状态：已合入
- 作者邮箱：Bui Duc Phuc <phucduc.bui@gmail.com>
- 概括：TI OMAP3 ROM 硬件随机数生成器读取时，原先手动进行运行时电源管理获取并处理错误路径的引用释放。现改用内核提供的统一接口，在获取运行时电源管理失败时自动释放引用，简化错误处理流程，实际行为不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260922032054.320969-1-phucduc.bui@gmail.com/

**▸ 组织：归属待核实（gondor.apana.org.au）**（1 patches）

**[RESEND] hwrng: cctrng - Discard pm_runtime_put_autosuspend() return value**

- 日期：2026-10-15
- 状态：已合入
- 作者邮箱：Herbert Xu <herbert@gondor.apana.org.au>
- 概括：某个硬件随机数发生器驱动原先会对运行时电源管理自动挂起释放接口的非零返回值打印错误信息，但该非零值只表示没有排队定时器或工作项去检查挂起，属于常见且合理的状态，例如向设备的运行时电源管理控制属性写入开启值之后。现在直接丢弃返回值不再告警，避免误导性错误日志，并为该接口将来改为无返回值做好准备。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/atCau3kHbzUefyMA@gondor.apana.org.au/

---

### ◆ 子系统：CAAM (NXP)（3 patches）

**▸ 组织：归属待核实（free.fr）**（2 patches）

**[v2] crypto: caam/qi2 - lower the algorithm priority**

- 日期：2026-09-29
- 状态：已合入
- 作者邮箱：Vincent Jardin <vjardin@free.fr>
- 概括：针对NXP CAAM队列接口加密加速器，将其算法优先级从2000降至100，避免默认算法选择时该硬件实现因过高优先级而过度抢占其他实现，与英特尔QAT加速器处理方式一致。按驱动名仍可访问该加速器，用户空间可通过算法配置接口提高其优先级。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260929-for-upstream-caam-qi2-priority-v2-1-bf0559ebf574@free.fr/

**crypto: caam/qi2 - reset the DPSECI at probe only when enabled**

- 日期：2026-09-28
- 状态：已合入
- 作者邮箱：Vincent Jardin <vjardin@free.fr>
- 概括：在 CAAM 队列接口二代的探测阶段，对管理控制器固件刚从配置中创建、尚未使能的数据路径安全引擎实例也执行复位，导致固件在每次启动时为每个队列记录刷新未确认等可恢复错误，尽管并没有待处理请求。现在先查询实例是否已经使能，只有已使能时才复位，移除阶段的复位保持不变，从而消除这类无意义的启动错误日志。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260928-for-upstream-caam-qi2-dpseci-reset-v1-1-042be6c05472@free.fr/

**▸ 组织：Individual Contributor**（1 patches）

**crypto: caam: map job ring registers without claiming region**

- 日期：2026-09-01
- 状态：已合入
- 作者邮箱：Rosen Penev <rosenp@gmail.com>
- 概括：在 i.MX 系列平台上，CAAM 加密加速器的作业环寄存器位于父安全模块寄存器窗口内部，父设备探测时已独占保留整个窗口；子作业环原先按常规方式映射并声明资源，因区域重叠而返回忙错误，导致探测失败并使硬件随机数生成器离线。现改为只映射寄存器而不重复声明区域，使作业环在 i.MX6、i.MX7、i.MX8 等平台上能正常探测并恢复随机数功能。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260901203736.13248-1-rosenp@gmail.com/

---

### ◆ 子系统：ECC（2 patches）

**▸ 组织：Kernel.org**（1 patches）

**crypto: atmel-ecc - simplify atmel_ecdh_compute_shared_secret**

- 日期：2026-09-01
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：在 Atmel ECC 加密驱动计算共享密钥的过程中，原先命令初始化失败时会跳转到统一释放标签再返回。现改为失败时立即释放临时工作数据并直接返回错误码，去掉多余的跳转标签，使该错误处理路径更直观，实际加密行为保持不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260901081126.44790-2-blum@kernel.org/

**▸ 组织：ANSSI**（1 patches）

**[v2] crypto: ecc - Handle exceptional points in Shamir multiplication**

- 日期：2026-09-26
- 状态：已合入
- 作者邮箱：Jérémy Jean <Jeremy.Jean@oss.cyber.gouv.fr>
- 概括：椭圆曲线 Shamir 乘法原先不能正确处理相同点、相反点及无穷远点，导致有效 ECDSA 签名被内核错误拒绝，并可能在公钥等于基点或其相反点时接受无效签名，已错误拒绝 16 个 Wycheproof 有效向量。现在在预计算和累加过程中显式处理倍点、相消和无穷远点，并补充回归测试，使签名验证结果恢复正常。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260926204323.1913803-4-Jeremy.Jean@oss.cyber.gouv.fr/

---

### ◆ 子系统：Authenc（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: atmel: handle authenc requests without plaintext**

- 日期：2026-09-22
- 状态：已合入
- 作者邮箱：Karl Mehltretter <kmehltretter@gmail.com>
- 概括：Microchip Atmel 硬件认证加密驱动处理只有关联数据、没有明文的请求时，会让 AES 的 DMA 传输零字节，导致有效请求被 DMA 引擎拒绝；并且同步完成时认证失败码可能被丢弃，使不匹配的标签误报为解密成功。现文本长度为零时跳过 AES 传输直接完成摘要，并让同步路径直接返回认证失败码，使坏标签正确返回认证失败。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260922051705.15329-1-kmehltretter@gmail.com/

---

### ◆ 子系统：TCrypt（1 patches）

**▸ 组织：归属待核实（gondor.apana.org.au）**（1 patches）

**crypto: tcrypt - Avoid reading req->base after submission**

- 日期：2026-09-22
- 状态：已合入
- 作者邮箱：Herbert Xu <herbert@gondor.apana.org.au>
- 概括：内核加密自测模块在请求提交后仍读取请求基址数据，该字段可能在处理期间改变，导致等待对象使用错误。现把等待结构与加密请求封装成合成对象并在调用中传递，提交后不再经由请求基址取等待信息，避免提交后的非法读取。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/arJPHqt-vgu8md57@gondor.apana.org.au/

---

### ◆ 子系统：Skcipher（1 patches）

**▸ 组织：归属待核实（free.fr）**（1 patches）

**crypto: caam/qi,qi2 - set plain_keylen for skcipher descriptors**

- 日期：2026-09-28
- 状态：已合入
- 作者邮箱：Vincent Jardin <vjardin@free.fr>
- 概括：在 LX2160A 等使用 CAAM 队列接口和队列接口二代的设备上，设置对称加密密钥时由于只填入了内联密钥但未标明密钥长度，硬件会把内联密钥字节当成命令解析，导致除 XTS 外的自检都报无效加载命令并失败。现在为同步块加密描述符补上明文密钥长度并清除密钥命令选项，使硬件能正确识别密钥并完成加密操作。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260928-for-upstream-caam-qi-plain-keylen-v1-1-6edb56649cf9@free.fr/

---

### ◆ 子系统：AF_ALG API（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: algif_skcipher: rewind rounded output bytes**

- 日期：2026-10-04
- 状态：已合入
- 作者邮箱：Daehyeon Ko <4ncienth@gmail.com>
- 概括：修复内核加密套接字接口在分段请求中的长度处理缺陷：接收迭代器按未对齐长度前进，而实际处理长度向下取整到块大小却没有回退，后续块可能从上一页面生命周期读取并暴露陈旧字节，使用无特权 XTS 模式 AES 可复现。现在在处理前回退被舍入的尾部，使返回长度与迭代器位置一致，封堵该泄露途径。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261004050946.3131044-1-4ncienth@gmail.com/

---

### ◆ 子系统：Talitos（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[v4] crypto: talitos: init tasklets before requesting IRQs**

- 日期：2026-10-04
- 状态：已合入
- 作者邮箱：Rosen Penev <rosenp@gmail.com>
- 概括：Talitos 加密引擎驱动原先在请求中断后才初始化软中断任务，若请求中断时已有由引导加载程序或 kexec 内核留下的挂起中断，会调度回调为空的任务。现将中断号查询和寄存器映射提前至资源分配前，先完成通道队列分配、引擎复位和软中断任务初始化，最后才请求中断；同时修正错误路径中对未请求中断的释放。从而避免启动阶段空回调调度与错误释放。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261004215042.383358-1-rosenp@gmail.com/

---

### ◆ 子系统：CCP/SEV (AMD)（1 patches）

**▸ 组织：AMD**（1 patches）

**[v3,1/1] crypto: ccp - Make usage of sev_cmd_mutex more granular**

- 日期：2026-10-21
- 状态：已合入
- 作者邮箱：Michael Roth <michael.roth@amd.com>
- 概括：AMD 安全处理器 SEV 固件输入输出控制接口原先在入口处持有互斥锁，包裹了可能耗时的用户态缓冲区拷贝等准备操作，该过程可能发生缺页并带来理论死锁风险，尤其与未来客户机内存页在共享与私有状态之间原地转换相关。现在将互斥锁下放到各命令内部，仅在平台状态迁移和固件命令执行时加锁，显著缩小持锁范围，消除这些用户态拷贝引发理论死锁的隐患。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261021192434.1924950-2-michael.roth@amd.com/

---

### ◆ 子系统：ICE (Qualcomm)（1 patches）

**▸ 组织：The Good Penguin**（1 patches）

**[SERIES] crypto: use designated initializers for acpi_device_id** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-09-03
- 状态：已合入
- 作者邮箱：Pawel Zalewski <pzalewski@thegoodpenguin.co.uk>
- 概括：将涉及 AMD 和海思平台的 ACPI 加密设备 ID 表改为具名字段初始化，明确标识符与驱动数据两项，并统一空终止项格式、去掉冗余的零赋值；仅改善可读性和初始化一致性，不改变实际匹配或驱动行为。
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
- 概括：重构内核随机数生成接口：移除不再需要的通用随机数算法抽象，将确定性随机比特生成器和抖动熵源改为直接库调用；把抖动熵源的健康检查从启动时推迟到首次使用，避免内置未使用时也执行昂贵检查；为新的库接口增加自测，并保持内核加密套接字随机数接口和内核标准随机数获取功能原有的行为。同时修复抖动熵源失败时未初始化的栈数据被混入确定性随机比特生成器的问题，该数据混入不会直接影响安全性，但属于未定义行为。
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

### ◆ 子系统：General Crypto（47 patches）

**▸ 组织：Kernel.org**（14 patches）

**lib/crypto: poly1305: Hide the mask value from compilers**

- 日期：2026-10-31
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：Poly1305 输出阶段需要根据累加值是否小于素数在原始值与减去素数的值之间选择，选择掩码会被编译器推理为全 0 或全 1，理论上可能被优化为依赖分支而破坏常量时间。通过向编译器隐藏掩码取值来阻断这种推断，保持现有常量时间选择行为。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261031042637.68815-1-ebiggers@kernel.org/

**lib/crypto: aes-cmac: Hide selection mask value from compilers**

- 日期：2026-10-31
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：AES-CMAC 子密钥推导中根据上一块的符号位决定是否与固定常数异或，编译器可能看出选择掩码的用途并生成依赖秘密的分支。通过隐藏掩码来防止编译器识别该选择，同时调整掩码类型以避免在 32 位架构上产生多余寄存器占用。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261031052053.201779-1-ebiggers@kernel.org/

**lib/crypto: gf128hash: Hide selection mask values from compilers**

- 日期：2026-10-31
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：在伽罗瓦域哈希的进位乘法与密钥转换过程中，编译器可能把用于二选一的掩码优化为依赖秘密的分支，带来侧信道风险；现对这些掩码值增加编译器屏蔽，使其不会被识别为选择操作，并在屏蔽后再与数据相与。该问题在此处尚非已知发生，属于预防性加固。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261031052149.201983-1-ebiggers@kernel.org/

**lib/crypto: gf128mul: Hide selection mask values from compilers**

- 日期：2026-10-31
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：在伽罗瓦域乘法的移位约减路径中，编译器可能把选择约减常量或 0 的掩码识别为二选一并生成依赖秘密的分支；现同样对掩码值进行编译器屏蔽，并把只选择约减常量与 0 的掩码类型改为无符号长整型，避免 32 位架构上被强制物化到寄存器对，属于预防性侧信道加固。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261031052154.202008-1-ebiggers@kernel.org/

**crypto: arc4 - Remove obsolete crypto API support for ARC4**

- 日期：2026-10-31
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：ARC4 的内核用户已直接使用库实现，旧加密 API 封装也被标记废弃多年，并已从默认套接字加密允许列表中移除。该补丁删除这套过时的 ARC4 加密接口和对应测试示例，避免继续暴露不安全的算法入口；内核中仍保留 ARC4 库实现，以支持某些遗留协议。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261031211535.8793-1-ebiggers@kernel.org/

**lib/crypto: powerpc/poly1305: Remove BROKEN implementation**

- 日期：2026-10-29
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：删除已标记为损坏超过一年的 PowerPC Poly1305 加速实现。该实现在软中断上下文不可用，且汇编逻辑存在进位丢失等问题导致部分输入计算结果错误，还含有依赖秘密数据的分支；删除后 PowerPC 回退到通用 Poly1305 实现，待修正版本再考虑。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261029063522.124421-1-ebiggers@kernel.org/

**[SERIES] lib/crypto: mldsa: Address some minor nits** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-10-29
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：修正 ML-DSA 数字签名验证库的若干小问题：原先在确认公钥长度足够前进行指针偏移，可能越过数组末尾，现在先验证长度；显式检查算法参数取值是否合法，并为无效值返回错误；给签名验证函数添加必须检查返回值的编译属性，防止调用者忽略验证状态。这些改动对当前合法调用者无实际影响，属于健壮性修补。
- 达到阈值的 patches（2 个，显示前 5）：
  - lib/crypto: mldsa: Check pk_len before doing pointer arithmetic
  - lib/crypto: mldsa: Explicitly check that 'alg' is a valid value
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261029054534.68481-2-ebiggers@kernel.org/

**lib/crypto: mips: Disable Octeon SHA code on little-endian kernels**

- 日期：2026-10-22
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：MIPS64 Cavium Octeon 的小端内核构建中，使用 Octeon 协处理器加速 SHA-1、SHA-256 和 SHA-512 的代码因为缺少端序转换，会向协处理器写入字节反转的消息和状态，导致哈希结果可能不正确；大端构建不受影响。现在仅在 Octeon 大端内核上默认启用这些加速，小端构建不再启用。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261022054450.20746-1-ebiggers@kernel.org/

**[SERIES] lib/crypto: Use size_t lengths for Poly1305 and ChaCha** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-10-14
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：将内核加密库中 Poly1305 消息认证和 ChaCha 流加密接口的长度参数统一升级为与系统字长一致，使 C 声明与实际汇编预期及其他加密库一致；消除在 64 位架构上 32 位参数因符号扩展或高位未定义而可能在超大长度下产生错误，以及 Poly1305 更新时长度加法溢出的隐患。当前调用者不会传入如此大的长度，因此属于接口健壮性改进。
- 达到阈值的 patches（2 个，显示前 5）：
  - lib/crypto: poly1305: Use size_t length
  - lib/crypto: chacha: Use size_t length
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261014152604.323310-2-ebiggers@kernel.org/

**[SERIES] lib/crypto: x86/sha: Follow the normal %rbp convention** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-10-11
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：x86 的 SHA-1、SHA-256、SHA-512 汇编实现在压入被调用者保存寄存器之后才建立帧指针，导致函数执行期间栈帧约定不满足，启用帧指针展开器时调用追踪不可靠，只能靠扫描整个栈回退。这些补丁调整 AVX/AVX2 实现的序言和结语顺序，先建立帧指针再保存寄存器，恢复时按正确偏移弹出，使其符合 C 代码通用的栈帧布局。之后在启用帧指针展开器的内核上，这些函数内部的调用追踪能够可靠生成。
- 达到阈值的 patches（3 个，显示前 5）：
  - lib/crypto: x86/sha1: Follow the normal %rbp convention
  - lib/crypto: x86/sha256: Follow the normal %rbp convention
  - lib/crypto: x86/sha512: Follow the normal %rbp convention
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261011134843.166585-2-ebiggers@kernel.org/

**lib/crypto: poly1305: Use memzero_explicit() in poly1305_final()**

- 日期：2026-10-06
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：Poly1305 终结函数原先通过结构体整体赋值清零描述上下文，理论上链接时优化可能消除该清零，现改用不会被编译器优化掉的显式清零操作，保证终结后内部状态确实被擦除。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261006083432.16328-1-ebiggers@kernel.org/

**[SERIES] AES library fixups** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-09-30
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：在 x86 平台上，AES 通用库的 CBC 加密汇编原先依赖前一个函数遗留的轮密钥寄存器别名，碰巧可用；这些补丁将其显式设置，消除隐式依赖。同时把通用库中 ECB、CBC、CTS、CTR 等 AES 模式优先级从 300 提高到 500，避免优先级为 300/400 的 CCP 和 PadLock 驱动覆盖 AES-NI/VAES 优化实现。
- 达到阈值的 patches（2 个，显示前 5）：
  - lib/crypto: x86/aes: Set RNDKEY in aes_cbc_encrypt_aesni()
  - crypto: aes - Boost priority of encryption modes further
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260930170542.140403-2-ebiggers@kernel.org/

**[SERIES] Migrate x86 and RISC-V accelerated AES modes into library** （cover letter，15/19 个 patch 达到代码量阈值）

- 日期：2026-09-27
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：将x86和RISC-V架构的AES分组模式优化代码迁移到内核加密库。先为库中ECB、CBC、CTR、XTS添加x86 AES-NI汇编实现，兼顾32位并保持四个块一轮的并行；同时修正XTS旧代码将加密调整值溢出到目标缓冲暴露秘密值的问题。随后删除被取代的传统skcipher实现，并为RISC-V复制宏、改动密钥参数、迁移各模式优化。过渡期跳过部分架构上的库算法注册，防止模板实例绕开优化代码造成性能回退。
- 达到阈值的 patches（15 个，显示前 5）：
  - lib/crypto: aes-xctr: Pass counter by value to aes_xctr_arch()
  - lib/crypto: x86/aes: Clean up aes-aesni.S in preparation for AES modes
  - lib/crypto: x86/aes-cbc: Add AES-NI optimization
  - lib/crypto: x86/aes-ctr: Add AES-NI optimization
  - lib/crypto: x86/aes-xts: Add AES-NI optimization
  - ... 及其他 10 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260927224418.109759-3-ebiggers@kernel.org/

**[SERIES] x86: Remove cpu_has_xfeatures() and add AVX-512 xor_gen()** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-09-01
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：为软件 RAID 的异或生成新增 AVX-512 实现，使用 512 位向量并在合适时执行三输入异或，适用于 Zen 4 及之后、Sapphire Rapids 等支持 AVX512F 且不偏好 256 位向量的 CPU，排除老款易降频型号；同时当 CPU 声明的 AVX 或 AVX-512 缺少对应扩展状态位时，x86 和 UML 会告警并清除相应标志，使加解密、CRC 与异或等 SIMD 路径无需重复检查扩展状态位。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: x86 - Stop using cpu_has_xfeatures()
  - lib/crypto: x86: Stop using cpu_has_xfeatures()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260901145740.42337-4-ebiggers@kernel.org/

**▸ 组织：Individual Contributor**（8 patches）

**crypto: atmel-i2c - find the bus speed behind an I2C mux**

- 日期：2026-10-29
- 状态：社区讨论中
- 作者邮箱：Josef Schlehofer <pepe.schlehofer@gmail.com>
- 概括：Atmel 加密芯片挂在 I2C 多路复用器后面时，驱动原先只从通道适配器读取时钟频率属性，而该通道往往没有此属性，导致探测以无效参数失败。现在若当前适配器缺失该属性则继续向上查询父适配器，仍未找到时采用 100 kHz 默认值，使位于多路复用器后的芯片能够正常初始化。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261029082616.53365-1-pepe.schlehofer@gmail.com/

**lib/crypto: aes: use memzero_explicit() instead of memset()**

- 日期：2026-10-28
- 状态：社区讨论中
- 作者邮箱：Mohamad Raizudeen <raizudeen.kerneldev@gmail.com>
- 概括：AES-GCM 和 AES-CCM 解密在认证失败时用普通内存清零操作擦除输出缓冲区，编译器可能把清零步骤优化掉，使未通过认证的明文残留在内存中。改用防优化清零操作，确保这些敏感数据确实被覆盖，与文件中其他敏感擦除一致。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261028142636.5888-1-raizudeen.kerneldev@gmail.com/

**[SERIES] Batched zswap_store() framework with compression batching** （cover letter，1/4 个 patch 达到代码量阈值）

- 日期：2026-10-28
- 状态：社区讨论中
- 作者邮箱：Kanchana P. Sridhar <kanchanapsridhar2026@gmail.com>
- 概括：为异步压缩接口引入请求级单元大小和分段标志，使一次压缩或解压请求可携带多个独立数据单元，并为不支持分段的算法提供只接受单个分段的包装，调用方无需区分底层能力。新增查询算法批量大小的接口，zswap 将单元大小设为页大小并利用该接口按压缩器能力批量处理大 folio，包括批量分配条目，软件压缩器不支持时仍逐页处理。目标是减少 zswap 换出路径中逐页提交和分配的固定开销，硬件压缩器可一次处理多页。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: acomp - Define a unit_size in struct acomp_req to enable batching. mm: zswap: Set the unit size for zswap to PAGE_SIZE.
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261028030503.17923-2-kanchanapsridhar2026@gmail.com/

**crypto: amlogic - Free channel IRQs before disabling the clock**

- 日期：2026-10-15
- 状态：社区讨论中
- 作者邮箱：Myeonghun Pak <mhun512@gmail.com>
- 概括：Amlogic GXL 加密加速器在探测时先请求通道中断再分配通道数组，自动清理会先释放数组再释放中断；加密超时后即使引擎空闲，晚到的中断处理也可能在读取完成状态后写已释放的通道数组。现在在加密引擎退出并排空正常请求后、禁用总线时钟前显式释放中断，避免晚到中断访问已释放数组。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/179203206852.2659709.13834828335447558448.G3@gmail.com/

**lib/crypto: md5: correct header inclusions**

- 日期：2026-10-15
- 状态：社区讨论中
- 作者邮箱：Mohamad Raizudeen <raizudeen.kerneldev@gmail.com>
- 概括：MD5 库代码使用的循环移位宏来自位操作头文件，但此前未显式包含，依赖间接包含；同时包含的非对齐访问头文件未被使用。现在补充位操作头文件并移除非对齐访问头文件，消除隐式依赖，算法行为不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261015033843.6056-1-raizudeen.kerneldev@gmail.com/

**[v3] lib/crypto: chacha20poly1305: zeroize state in __chacha20poly1305_decrypt**

- 日期：2026-10-05
- 状态：社区讨论中
- 作者邮箱：Mohamad Raizudeen <raizudeen.kerneldev@gmail.com>
- 概括：将 ChaCha20-Poly1305 解密辅助函数改为自行清零流密码状态，与加密辅助函数保持一致；此前扩展随机数变体解密路径直接返回，未清零派生子密钥，导致其残留在栈上。长度检查移到调用方，无效输入不再初始化状态。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261005150324.5621-1-raizudeen.kerneldev@gmail.com/

**crypto: essiv: avoid request access after subrequest**

- 日期：2026-09-21
- 状态：社区讨论中
- 作者邮箱：Jiale Yao <yaojiale02@163.com>
- 概括：ESSIV 认证加密模板在提交子请求后仍读取关联数据缓冲区指针，若异步完成提前释放该缓冲区并结束外层请求，提交返回后的访问可能使用已释放内存并触发重复释放。现改为在提交子请求前保存缓冲区指针，同步清理使用本地保存值，避免释放后访问。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260921090458.3364976-1-yaojiale02@163.com/

**crypto: keembay-ocs: prevent underflow in sg_data_total - remainder**

- 日期：2026-09-08
- 状态：社区讨论中
- 作者邮箱：Dmitriy Okunev <dokunevdmitriy@gmail.com>
- 概括：Intel Keem Bay OCS HCU 哈希驱动的更新请求在准备 DMA 时，用“当前散列数据长度加缓冲计数”的总数对块大小取模得到剩余值。若缓冲计数较大且总数小于块大小，剩余值可能超过当前散列数据长度，随后两者相减产生无符号下溢，得到一个异常大的长度传给散列段计数函数，可能造成内存破坏。现在当当前散列数据长度小于剩余值时返回无效参数错误，确保减法安全。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260908143447.2155188-1-dokunevdmitriy@gmail.com/

**▸ 组织：Intel**（4 patches）

**[v2,1/2] crypto: qat - enable three-service mode for QAT GEN5 devices**

- 日期：2026-10-30
- 状态：社区讨论中
- 作者邮箱：Ahsan Atta <ahsan.atta@intel.com>
- 概括：为英特尔 QAT 420xx 第五代设备增加三类服务并发模式，允许对称加密、非对称加密和压缩同时启用；补充配套的固件对象布局、环到服务映射及线程到仲裁器映射，使设备能按三种服务运行。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261030143019.484280-2-ahsan.atta@intel.com/

**crypto: qat - make adf_ae_shutdown() a void function**

- 日期：2026-10-30
- 状态：社区讨论中
- 作者邮箱：Ahsan Atta <ahsan.atta@intel.com>
- 概括：Intel QAT 的加速引擎关闭操作没有失败路径却一直以整数返回，唯一调用处因此包含无法到达的错误分支，并可能在关闭后跳过清除初始化状态。将其改为无返回值并删除死错误处理，使关闭流程直接完成，避免无效判断。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261030111916.483870-1-ahsan.atta@intel.com/

**crypto: qat - add support for enhanced decompression mode on GEN6 devices**

- 日期：2026-10-26
- 状态：社区讨论中
- 作者邮箱：Suman Kumar Chakraborty <suman.kumar.chakraborty@intel.com>
- 概括：为Intel QAT GEN6设备增加增强解压模式：允许固件利用压缩引擎内嵌的解压引擎处理普通解压请求，绕过压缩和转换阶段，从而提高解压吞吐量且不影响同时进行压缩。该模式通过新的sysfs属性控制，写入后立即生效并跨上下电和配置变更持久化；默认在仅配置解压服务时启用。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261026035501.1627846-1-suman.kumar.chakraborty@intel.com/

**[SERIES] crypto: iaa - rework the WQ selection tables** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-10-19
- 状态：社区讨论中
- 作者邮箱：Vinicius Costa Gomes <vinicius.gomes@intel.com>
- 概括：重构 Intel IAA 压缩加速器的工作队列选择逻辑：原先按扁平索引分配，CPU 可能被配到其他封装的设备而本封装设备空闲，表原地重建时请求还可能读到空队列失败。现在按 CPU 所在封装维护工作队列表，压缩请求在本封装内轮转，解压请求由每个 CPU 首次使用时选定一个工作队列并固定以降低延迟；表通过 RCU 发布，请求在 RCU 保护下获取引用，避免探测或移除期间访问空队列。
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
- 概括：修复德州仪器 DTHEv2 加解密引擎的多项缺陷：修正设备列表为空时的无效指针返回、软中断与自旋锁不一致可能导致死锁，以及高端内存页映射方式避免内存破坏；请求散列表现按实际数据长度裁剪，防止 DMA 因等待多余数据而超时。驱动移除时对仍在途的请求增加引用计数保护，错误路径统一终止 DMA 以回收描述符；AEAD 标签读写移到解除映射后，软件回退仅限内存分配失败，长度改为 64 位避免溢出。
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
- 概括：德州仪器SA2UL加密驱动清理与修复：删除未用字段、宏和死代码；修复错误路径中安全上下文、DMA映射和哈希资源的泄漏；修复哈希状态导出缓冲区过小导致的栈越界，以及并发密钥设置可能破坏在途命令标签的问题；元数据长度改为根据算法动态生成，DMA池改为内存池，并按正确方向同步设备数据；新增AES-CM随机数发生器启动初始化、硬件修订上报，并将请求统一交给通用加密引擎调度。
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
- 概括：为德州仪器 DTHE V2 硬件加密引擎的哈希引擎增加 SHA-224/256/384/512 和对应 HMAC 算法支持，使原本主要处理对称运算的硬件还能卸载摘要和带密钥的消息认证计算，适用于需要完整性校验或 HMAC 的 TI 平台场景。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: ti - Add support for SHA224/256/384/512 in DTHEv2 driver
  - crypto: ti - Add support for HMAC in DTHEv2 driver
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260910180424.2131193-2-t-pratham@ti.com/

**▸ 组织：AMD**（2 patches）

**[SERIES] Implement SNP live firmware update support** （cover letter，3/4 个 patch 达到代码量阈值）

- 日期：2026-10-21
- 状态：社区讨论中
- 作者邮箱：Pratik R. Sampat <prsampat@amd.com>
- 概括：为AMD SEV-SNP实现在线固件更新：通过固件上传界面可暂存新镜像，是否永久生效由管理员后续提交决定。若旧式SEV平台正在运行传统客户机，更新会被拒绝为忙；否则关闭旧平台、释放其固件缓冲区后执行下载并恢复，SNP客户机不受影响。还调整固件加载器停止模块引用避免循环引用，并允许SNP初始化后查询平台状态，为更新后刷新缓存信息做准备。
- 达到阈值的 patches（3 个，显示前 5）：
  - crypto: ccp - Factor out the release of the SEV firmware buffers
  - crypto: ccp - Allow SNP platform data to be queried after SNP INIT
  - crypto: ccp - Implement SNP Download Firmware EX
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/be72e0b1015156f8613fc2c360fa73d59108dcc6.1792599491.git.prsampat@amd.com/

**[RFC,kernel,04/17] crypto/ccp/tsm: Use TSM API for DOE**

- 日期：2026-09-16
- 状态：社区讨论中
- 作者邮箱：Alexey Kardashevskiy <aik@amd.com>
- 概括：AMD CCP 的 TSM 模块在通过 PCI DOE 传输 SPDM 命令时，原先直接调用通用 PCI DOE 接口。现在改用 TSM 提供的 DOE 传输接口，利用其额外的健全性检查，减少无效或异常传输被直接发出的可能。使用场景是 AMD SEV TIO 的 SPDM 命令通信。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260916115159.1938195-5-aik@amd.com/

**▸ 组织：归属待核实（gondor.apana.org.au）**（2 patches）

**crypto: aes - Add import_core/export_core to cmac/xcbc/cbcmac**

- 日期：2026-10-09
- 状态：社区讨论中
- 作者邮箱：Herbert Xu <herbert@gondor.apana.org.au>
- 概括：修正AES的CMAC、XCBC和CBC-MAC实现的导出导入格式，使其与通用模板一致。原先这些库版消息认证码的状态导出与通用模板不匹配，且在CMAC和XCBC中未完整保留被暂存的块；现在导出时额外执行一次加密以保存该块信息，导入时正确恢复部分块状态，避免状态信息丢失。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/asjT87HAZ_UUbbvm@gondor.apana.org.au/

**[v2] crypto: hash - Preserve withheld block in export_core**

- 日期：2026-10-09
- 状态：社区讨论中
- 作者邮箱：Herbert Xu <herbert@gondor.apana.org.au>
- 概括：部分哈希算法（如 CMAC 和 XCBC）在最终化前会保留一个数据块，但此前导出哈希状态时会丢失这个保留块，导致导出的状态不完整。现在在导出前若存在完整的保留块，先把它作为一次更新计入状态再导出，使导出结果包含等待最终处理的块。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/asjfxnGfCtvD7QJL@gondor.apana.org.au/

**▸ 组织：归属待核实（genproof.com）**（2 patches）

**[SERIES] lib/crypto: chacha: Handle lengths of 2 GiB or more on 32-bit arm and MIPS** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-10-14
- 状态：社区讨论中
- 作者邮箱：Vladimir Kukharenko <vladimir@genproof.com>
- 概括：修复 32 位 ARM 和 MIPS 平台上 ChaCha 流加密对 2 GiB 及以上输入处理不完整的问题：ARM 标量路径（如 NEON 不可用时）原用有符号比较和易溢出的块数计算，大长度时几乎不处理数据；MIPS 汇编也用有符号判断导致过早进入尾部路径。现在 ARM 改为无符号条件和无溢出计算，MIPS 在 C 层每次最多处理 1 GiB，使大长度加密结果完整。当前树内调用者未传入如此大的数据。
- 达到阈值的 patches（2 个，显示前 5）：
  - lib/crypto: arm/chacha: Handle lengths of 2 GiB or more in scalar code
  - lib/crypto: mips/chacha: Handle lengths of 2 GiB or more
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261014-libcrypto-chacha-32bit-2gib-v1-1-e0719ca0be89@genproof.com/

**[SERIES] lib/crypto: Handle large lengths in poly1305 and chacha20poly1305** （cover letter，1/5 个 patch 达到代码量阈值）

- 日期：2026-10-12
- 状态：社区讨论中
- 作者邮箱：Vladimir Kukharenko <vladimir@genproof.com>
- 概括：修复内核加密库中 Poly1305 消息认证和 ChaCha20-Poly1305 认证加密对超大输入长度的处理：原先在 64 位 MIPS、RISC-V 等架构上，长度按 32 位传递，超过 2 GiB 时汇编可能因符号扩展算错结束指针而越界读取，更新逻辑还可能因加法溢出或长度截断导致认证或加密不完整。现将长度类型改为与系统字长一致并按块分次传递，使超大输入也能正确完成认证与加解密；当前树内调用者尚未传入如此大的数据。
- 达到阈值的 patches（1 个，显示前 5）：
  - lib/crypto: chacha: Take a size_t length in chacha_crypt()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261012-libcrypto-4gib-lengths-v1-2-ea566c129a2e@genproof.com/

**▸ 组织：浙江大学**（1 patches）

**[v2] crypto: ccp - Fix use-after-free in backlog cmd advancement**

- 日期：2026-09-29
- 状态：社区讨论中
- 作者邮箱：Fan Wu <fanwu01@zju.edu.cn>
- 概括：修复 CCP 加密协处理器驱动中积压命令提升的释放后使用问题：原实现先由队列线程取出积压命令，稍后由工作队列重新入队，期间命令不在任何列表，设备销毁时刷新无法触达，工作队列会在设备释放后继续使用，且预留空间可能被并发提交占用。现在在出队时同锁转移空闲槽位，由队列内核线程完成推进回调，并在拆除前标记停止，避免唤醒已停止线程。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260929143825.21349-1-fanwu01@zju.edu.cn/

**▸ 组织：Qualcomm**（1 patches）

**[v11,1/2] crypto: qce - Only register algos if the user really wants it**

- 日期：2026-10-22
- 状态：社区讨论中
- 作者邮箱：Bartosz Golaszewski <bartosz.golaszewski@oss.qualcomm.com>
- 概括：高通的 QCE 加密驱动中，硬件算法仍存在未触发自检失败的已知问题，但此前仍会默认注册给内核使用。现增加模块参数，默认不再注册这些加密算法，只有用户显式传入启用参数时才会注册；驱动的电源管理部分继续保留，以便仍能通过运行时电源管理缩放互连时钟。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261022-qce-fixes-broken-label-v11-1-0d33c34fd0c3@oss.qualcomm.com/

**▸ 组织：归属待核实（jaseg.de）**（1 patches）

**[v3,06/12] crypto: api - Allocate tfms from the secret pool**

- 日期：2026-09-28
- 状态：社区讨论中
- 作者邮箱：Jan Sebastian Götte <linux@jaseg.de>
- 概括：内核加密框架的转换对象上下文会保存扩展后的密钥表，若发生崩溃转储可能被原样捕获。现在改为从秘密池分配转换对象及其上下文，并让 kdump 阶段能够擦除这些已标记页面，从而降低扩展密钥出现在崩溃转储中的风险；分配路径新增一次内存区域的桶查找。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260928-crash-memaction-upstream-20260921-v3-6-e511e9ee2329@jaseg.de/

**▸ 组织：归属待核实（itx.no）**（1 patches）

**[v3] lib/crypto: sparc/aes-xts: Add optimization using the AES opcodes**

- 日期：2026-10-04
- 状态：社区讨论中
- 作者邮箱：Stian Halseth <stian@itx.no>
- 概括：为 SPARC 平台的 AES 磁盘加密模式增加硬件加速：利用处理器内置 AES 指令和 VIS3 向量指令扩展的 128 位移位操作处理 128 位和 256 位密钥的加密与解密，每次迭代处理两个数据块；192 位密钥和未按 8 字节对齐的数据继续由通用代码处理。优化后，内核加密套接字接口在 T7-1 上 256 位密钥吞吐从 390 提升到 936 MiB/s，T4-1 上从 238 提升到 544，内存盘上的顺序读写也明显提高。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261004192812.4145406-1-stian@itx.no/

**▸ 组织：东南大学**（1 patches）

**[v2] crypto: inside-secure: initialize EIP93 state before requesting IRQ**

- 日期：2026-10-09
- 状态：社区讨论中
- 作者邮箱：Runyu Xiao <runyu.xiao@seu.edu.cn>
- 概括：针对 SafeXcel EIP-93 加密引擎驱动，将硬件与环初始化提前到中断注册之前，并在注册完成前保持设备中断关闭，避免注册过程中中断处理函数访问尚未就绪的状态；若注册失败则先关闭引擎并清理环寄存器，再让资源释放。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261009033149.1127441-1-runyu.xiao@seu.edu.cn/

**▸ 组织：归属待核实（sang-engineering.com）**（1 patches）

**crypto: ccp - unmap descriptor before completing cookie**

- 日期：2026-10-10
- 状态：社区讨论中
- 作者邮箱：Wolfram Sang <wsa+renesas@sang-engineering.com>
- 概括：AMD CCP 的 DMA 引擎在描述符完成后，原先先标记完成再解除映射；现在先解除描述符映射再发出完成通知，保证完成事件触发时相关缓冲区已完成刷新，避免消费方在数据落地前收到完成信号。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261010125001.19300-3-wsa+renesas@sang-engineering.com/

**▸ 组织：NXP**（1 patches）

**[RFC,4/4] crypto: remove async_tx framework**

- 日期：2026-10-15
- 状态：社区讨论中
- 作者邮箱：Frank Li <Frank.Li@oss.nxp.com>
- 概括：移除内核异步传输框架及其文档和关联文件。该框架曾用于 RAID5 等场景的内存复制、异或和 RAID6 校验卸载，并可跨通道编排依赖操作；最后一个使用者 RAID5 已改为同步操作后，框架不再被使用，删除以简化内核。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261015-asycn_tx_remove-v1-4-056a7085e0a1@nxp.com/

**▸ 组织：Red Hat**（1 patches）

**[SERIES] libcrypto: Provide more __cleanup functions for zeroizing data** （cover letter，10/10 个 patch 达到代码量阈值）

- 日期：2026-09-16
- 状态：社区讨论中
- 作者邮箱：Thomas Huth <thuth@redhat.com>
- 概括：为内核加密库中的 AES、AES-XTS、AES-GCM、AES-CCM、MD5、SM3、BLAKE2、SHA-1、SHA-2 等密钥和上下文结构提供显式清零辅助函数，可配合自动清理在作用域结束时擦除敏感数据，并替换库内原有手动清零调用；新增清零规范文档。可信密钥和 SMB 客户端改用这些辅助函数，x86 引导过渡代码编译时禁用加固字符串宏以解决头文件冲突。
- 达到阈值的 patches（10 个，显示前 5）：
  - lib/crypto: aes: Provide functions for zeroizing aes_key and aes_enckey
  - lib/crypto: aes-xts: Provide function for zeroizing aes_xts_key
  - lib/crypto: aes-gcm: Provide functions for zeroizing aes_gcm* structures
  - lib/crypto: aes-ccm: Provide functions for zeroizing aes_ccm* structures
  - lib/crypto: md5: Provide a function for zeroizing hmac_md5 structures
  - ... 及其他 5 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260916095022.604354-2-thuth@redhat.com/

**▸ 组织：Rambus**（1 patches）

**[SERIES] crypto: cmh - add Rambus CryptoManager Hub driver** （cover letter，13/13 个 patch 达到代码量阈值）

- 日期：2026-09-17
- 状态：社区讨论中
- 作者邮箱：Alex Ousherovitch <aousherovitch@rambus.com>
- 概括：新增 Rambus CryptoManager Hub 硬件加密加速器驱动，通过邮箱虚拟命令队列提交异步请求，向内核加密接口注册 SHA-2/SHA-3/SHAKE、SM3、HMAC、AES/SM4 系列、ChaCha20-Poly1305、RSA、ECDSA/SM2、X25519 及多种后量子签名和密钥封装算法，并提供 DRBG 硬件随机数。
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
- 概括：AMD PSP初始化修复并新增BC-250支持：固件版本属性可见性判断在板卡TEE驱动数据缺失时会解引用空指针导致模块加载崩溃，现在先检查指针；启动SEV或TEE子设备此前只看硬件能力，遇到缺少驱动数据会失败并连累平台访问等功能，改为要求两者同时满足；为BC-250安全处理器添加PCI标识和寄存器布局，但其TEE环无法完成初始化，所以仅启用平台访问和动态加速控制探测。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: ccp - do not start PSP sub-devices without their vdata
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/178984289057.12336.8102552838289034525@mtsistemi.it/

**▸ 组织：Huawei**（1 patches）

**[SERIES] crypto: hisilicon/qm - fix bugs and harden against abnormal hardware** （cover letter，2/4 个 patch 达到代码量阈值）

- 日期：2026-09-24
- 状态：社区讨论中
- 作者邮箱：Weili Qian <qianweili@huawei.com>
- 概括：华为硬件加速器管理模块在固件缺少 ACPI、设备异常或 SVA 不支持等情况下存在多类风险：无 ACPI 设备可能空指针；能力版本寄存器返回全 1 时继续使用无效版本；异常硬件读出的队列深度可能造成越界或除零；SVA 不支持时错误路径释放不到已创建的加速设备。补丁分别加入空指针判断并清除运行时电源标志、对异常版本提前返回错误、增加队列深度下限校验、改用局部变量直接释放，从而在异常硬件或固件环境下尽早失败或正确回收资源。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: hisilicon/qm - clear runtime PM flag for non-power-manageable device
  - crypto: hisilicon/qm - check queue depth read from hardware
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260924113812.1110302-2-qianweili@huawei.com/

**▸ 组织：归属待核实（mandelbit.com）**（1 patches）

**[SERIES] lib/crypto: x86/chacha: Add 16-block AVX-512 implementation** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-10-25
- 状态：社区讨论中
- 作者邮箱：Antonio Quartulli <antonio@mandelbit.com>
- 概括：为x86的ChaCha流密码新增16块AVX-512实现，一次处理1024字节，利用512位寄存器提高并行度，在支持AVX-512VL的CPU上用于超过8块的长输入（除非设置避免512位寄存器降频）。在AMD Zen 5上1024字节吞吐量从5168提升到10168 MB/s。同时增加KUnit测试和基准，覆盖长度、对齐、页边界及计数器回绕。
- 达到阈值的 patches（2 个，显示前 5）：
  - lib/crypto: x86/chacha: Add 16-block AVX-512 (zmm) implementation
  - lib/crypto: tests: Add KUnit tests and benchmark for ChaCha
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261025234758.3219829-3-antonio@mandelbit.com/

---

### ◆ 子系统：HWRNG（5 patches）

**▸ 组织：Individual Contributor**（2 patches）

**hwrng: mtk - wait long enough for the next word**

- 日期：2026-10-26
- 状态：社区讨论中
- 作者邮箱：Ryan Brue <ryanbrue.dev@gmail.com>
- 概括：联发科硬件随机数生成器在 MT8695 上产生下一个 32 位字所需时间超过原 60 微秒超时，中位数达 82 微秒，大多数读取因此失败或短读。将就绪等待超时提高到 1 毫秒，较快的生成器仍可立即返回，读取不再因超时中断。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261026-rbrue-sheldon-upstreaming-mtk-rng-timeout-v1-1-551b4b6b4f86@gmail.com/

**[v2] hwrng: imx-rngc - check return value of clk_prepare_enable()**

- 日期：2026-09-06
- 状态：社区讨论中
- 作者邮箱：Ma Yukun <0x4fe6@gmail.com>
- 概括：i.MX 随机数生成器驱动在探测时启用时钟的调用可能失败，但原先未检查返回值；一旦时钟启用失败，后续仍会在无时钟状态下读取硬件寄存器，可能导致总线挂起或外部中止。现改为检查时钟启用结果，失败即终止探测并返回错误，避免在硬件未获得时钟时继续访问寄存器。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/178869518976.1724.8613243679737914482@gmail.com/

**▸ 组织：SUSE**（1 patches）

**[v5,07/12] hw_random/via-rng: Stop using 32-bit MSR interfaces**

- 日期：2026-10-26
- 状态：社区讨论中
- 作者邮箱：Jürgen Groß <jgross@suse.com>
- 概括：VIA C3 处理器内置随机数发生器在初始化时需要读写特定 MSR 配置使能和噪声源。原驱动使用即将被移除的 32 位 MSR 读写接口。现在改用 64 位接口读写完整 MSR，低 32 位配置逻辑保持不变，确保接口移除后该随机数发生器仍可正常初始化。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261026130223.773129-8-jgross@suse.com/

**▸ 组织：归属待核实（gondor.apana.org.au）**（1 patches）

**hwrng: cctrng - Lock read and writer of circular buffer**

- 日期：2026-10-26
- 状态：社区讨论中
- 作者邮箱：Herbert Xu <herbert@gondor.apana.org.au>
- 概括：Arm CryptoCell 随机数生成器驱动中，环形缓冲区在读取与写入之间没有任何同步机制，读取路径原先尝试获取自旋锁失败就直接返回，写入路径也不加锁，并发访问可能破坏缓冲区数据。现在改用互斥锁同时保护读取和写入，读取可被信号中断并返回错误，写入完成处理也在持锁下更新环形缓冲区，消除读写竞争。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/at7rX1rkRAzHYwCB@gondor.apana.org.au/

**▸ 组织：归属待核实（ptudor.net）**（1 patches）

**[SERIES] hwrng: add Microchip RNG90 support** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-10-24
- 状态：社区讨论中
- 作者邮箱：Patrick Tudor <ptudor@ptudor.net>
- 概括：新增Microchip RNG90 I2C硬件随机数生成器驱动：上电唤醒并识别设备，构造信息读取和随机数命令，校验响应长度和CRC，处理设备自检失败而不暴露不合格输出。因数据表未量化每输出位熵，默认使用最小非零熵质量，可在系统验证后通过sysfs调整。同时提供32个KUnit测试用例覆盖命令帧、恢复、挂起等。
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
- 概括：生成椭圆曲线公钥时原先没有随机化初始坐标，使最终坐标及后续模逆输入成为私钥的确定性函数；模逆并非恒定时间，因此密钥生成运行时间可能泄露私钥信息，影响蓝牙 SMP 和 TPM2 HMAC 会话生成的临时 P-256 密钥。现在在点乘前生成随机初始坐标，盲化模逆输入，降低计时侧信道泄露私钥的风险，性能变化在噪声范围内。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261026034429.742489-1-pawliczekerwin@gmail.com/

**crypto: ecc - Use constant-time modular inversion in ecc_point_mult()**

- 日期：2026-09-28
- 状态：社区讨论中
- 作者邮箱：Erwin Pawliczek <pawliczekerwin@gmail.com>
- 概括：椭圆曲线迪菲-赫尔曼点乘中用于射影坐标取逆的模逆算法会因私钥相关的分支和迭代次数产生运行时间差异，可能泄漏私钥信息。现在将其替换为常数时间的伯恩斯坦-杨算法，原实现保留给输入公开的签名验证路径，并增加单元测试；ECDH 性能下降约百分之十几，但点乘中仍存在其他时序泄露风险。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260928042641.307683-1-pawliczekerwin@gmail.com/

**▸ 组织：Kernel.org**（1 patches）

**[5.10.y,2/5] crypto: atmel-ecc - Struct headers need to start with keyword 'struct'**

- 日期：2026-09-02
- 状态：社区讨论中
- 作者邮箱：Sasha Levin <sashal@kernel.org>
- 概括：在 Atmel ECC 驱动中，将转换上下文结构体的内核文档注释改为以结构体关键字开头，使启用较严格编译警告时能够正确识别该结构体文档，消除因无法解析函数原型而产生的警告；仅修改注释格式，代码逻辑保持不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260902105322.2048136-2-sashal@kernel.org/

---

### ◆ 子系统：CAAM (NXP)（3 patches）

**▸ 组织：归属待核实（gondor.apana.org.au）**（1 patches）

**crypto: caam - Remove public key support**

- 日期：2026-09-04
- 状态：社区讨论中
- 作者邮箱：Herbert Xu <herbert@gondor.apana.org.au>
- 概括：移除 CAAM 驱动中多年未维护且存在严重问题的公钥加密支持。此前该部分仍在内核中提供 RSA 等公钥操作，但缺乏维护；删除后相关硬件公钥算法不再通过内核加密接口暴露，以避免继续使用这些存在缺陷的代码路径，驱动的其他加密功能不受影响。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/appZMZ7WS-KNaHbc@gondor.apana.org.au/

**▸ 组织：归属待核实（solid-run.com）**（1 patches）

**[RFC,net-next,2/3] crypto: caam/qi2 - skip isolated CPUs when setting up queue pairs**

- 日期：2026-09-30
- 状态：社区讨论中
- 作者邮箱：Josua Mayer <josua@solid-run.com>
- 概括：CAAM QI2 队列对初始化原针对每个在线 CPU 建立队列，但在 CPU 被隔离用于低延迟任务时，这些 CPU 没有对应的 DPIO 对象，导致驱动探测无限期挂起；现改为只使用受管中断掩码中的在线 CPU 建立队列并处理通知，跳过隔离 CPU，隔离 CPU 仍可提交请求，响应由未隔离 CPU 处理。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260930-dpaa2-isolcpus-v1-2-66c13f4fd75b@solid-run.com/

**▸ 组织：Individual Contributor**（1 patches）

**crypto: caam: jr: Use dedicated shutdown callback**

- 日期：2026-10-28
- 状态：社区讨论中
- 作者邮箱：Fabio Estevam <festevam@gmail.com>
- 概括：恩智浦 CAAM 加密任务环驱动在系统关机时复用设备移除流程，该流程会因仍有加密消费者持有引用而拒绝关闭，导致重启时出现设备忙警告。新增专用关机回调只关闭硬件任务环，不检查消费者引用也不注销算法，系统关机路径不再报告错误。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261028132825.657546-1-festevam@gmail.com/

---

### ◆ 子系统：Skcipher（3 patches）

**▸ 组织：Kylin**（1 patches）

**[v2] crypto: mxs-dcp: handle zero-length skcipher requests**

- 日期：2026-09-08
- 状态：社区讨论中
- 作者邮箱：Linmao Li <lilinmao@kylinos.cn>
- 概括：MXS-DCP 加密驱动处理零长度对称加密请求时，通用 ECB 和 CBC 实现会直接返回成功，但该驱动仍将请求排队。完成路径用零的剩余长度减去 AES 块大小来更新初始化向量，导致无符号值下溢，解密时源地址会落到输入缓冲区之前。现在在请求入队前检测零长度并直接返回成功，保持初始化向量不变，避免非法源地址访问。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260908094437.1548278-1-lilinmao@kylinos.cn/

**▸ 组织：Qualcomm**（1 patches）

**[SERIES] crypto: qce - fix self-test issues in skcipher** （cover letter，3/4 个 patch 达到代码量阈值）

- 日期：2026-10-19
- 状态：社区讨论中
- 作者邮箱：Bartosz Golaszewski <bartosz.golaszewski@oss.qualcomm.com>
- 概括：针对高通QCE加密引擎的自检测试失败：AES-XTS对不足一个分组长度的请求未加拒绝，引擎会等待完整分组而停滞；AES-CTR尾部分组及分散的散列表源或目的也会导致引擎停滞并报硬件错误；XTS弱密钥在非FIPS模式也被错误拒绝。现分别改为对过短XTS返回长度错误，将CTR尾块和分散请求交给软件回退，弱密钥通过通用校验后使用回退，引擎只处理连续的整块请求，自检得以通过。
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
- 概括：针对磁盘加密等对称加密场景，为请求新增数据单元大小字段，允许调用方一次提交多个数据单元，初始向量按低 8 字节的 64 位小端计数器逐单元推进。对于未声明原生多单元支持的算法，加密 API 层会透明拆分为逐单元调用；设备映射加密层对 plain64 和 essiv 配置把连续 bio 段合并为单个请求，替代原来的每扇区一次请求。plain64be 等非小端布局仍走原有路径，不改变算法输出。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: skcipher - split multi-unit requests in the API layer
  - crypto: testmgr - test multi-unit dispatch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260924075846.28203-2-lravich@amazon.com/

---

### ◆ 子系统：Talitos（2 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: talitos: request irq after tasklet_init()**

- 日期：2026-09-04
- 状态：社区讨论中
- 作者邮箱：Rosen Penev <rosenp@gmail.com>
- 概括：Talitos 加密加速器驱动在初始化时原先先注册中断，后初始化用于完成回调的任务队列；如果中断注册后、任务队列初始化前有共享中断或残留完成事件到来，中断处理会调度尚未初始化的任务队列，可能导致异常。现将中断注册移到任务队列初始化之后，使中断到来时任务队列已就绪，初始化顺序也与移除时的逆序一致。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260904211230.81963-1-rosenp@gmail.com/

**▸ 组织：Bootlin**（1 patches）

**[SERIES] crypto: talitos - Driver cleanup** （cover letter，16/19 个 patch 达到代码量阈值）

- 日期：2026-10-13
- 状态：社区讨论中
- 作者邮箱：Paul Louvel <paul.louvel@bootlin.com>
- 概括：针对飞思卡尔 Talitos 安全引擎的驱动进行结构性清理：把原本集中在单一文件中的哈希、同步加密、AEAD 与硬件随机数实现拆分为独立文件并归入专属目录；哈希处理改用内核的块对齐请求接口，去掉自维护的部分块缓冲和虚拟散列表项；算法声明用宏统一，SEC 版本判断改用静态密钥，SEC1 与 SEC2 的硬件描述符和指针格式按版本分开定义，并补充维护者条目。属于代码组织与接口迁移，不改变既有算法能力。
- 达到阈值的 patches（16 个，显示前 5）：
  - crypto: talitos - Move driver into dedicated directory
  - crypto: talitos/hash - Use CRYPTO_AHASH_BLOCK_ONLY API
  - crypto: talitos/hwrng - Move into separate file
  - crypto: talitos - Prepare crypto implementation file splitting
  - crypto: talitos/hash - Convert to {init,exit}_tfm type-specific API
  - ... 及其他 11 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261013-7-3-rc2_talitos_cleanup-v8-2-ca02be17696b@bootlin.com/

---

### ◆ 子系统：Public Key（2 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: pkcs7: Return no-digest for data-taking algorithms**

- 日期：2026-10-15
- 状态：社区讨论中
- 作者邮箱：Muhammad Mahdi Amirpour <ampr.mhd@gmail.com>
- 概括：PKCS#7 签名验证获取摘要时，对于直接消费原始数据而非预计算哈希的公钥算法（目前如 ML-DSA），此前无认证属性时会被拒绝，但有认证属性时会把修改过的认证属性缓冲区当作摘要返回。现在先识别这类数据消费型算法并返回不支持，使有无认证属性都一致地报告无中间摘要；完整性测量架构对这类模块签名保持无摘要状态，符合算法特性。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261015110826.126621-1-ampr.mhd@gmail.com/

**▸ 组织：归属待核实（cynove.com）**（1 patches）

**[SERIES] crypto: fix RSA results corrupted by non-coherent DMA** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-10-16
- 状态：社区讨论中
- 作者邮箱：Stephane Debusne <stephane.debusne@cynove.com>
- 概括：修复非相干 DMA 平台上 RSA 签名、验证及同步加解密结果被破坏的问题：原先输出缓冲与请求上下文放在同一分配中，可能共享缓存行，设备驱动在 DMA 映射后写请求上下文弄脏该行，DMA 解除映射时 CPU 陈旧数据会覆盖设备写入的结果。在 CAAM 的 i.MX8M Mini 上，签名结果前部常变成输入、验证常失败，进而影响无线监管数据库和证书加载。现将数据及输出缓冲单独分配，避免共享缓存行，使 RSA 结果正确。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: rsassa-pkcs1 - use a separate buffer for the RSA output
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261016090333.2247764-3-stephane.debusne@cynove.com/

---

### ◆ 子系统：Aead（2 patches）

**▸ 组织：Qualcomm**（1 patches）

**[SERIES] crypto - qce: fix self-test issues in aead** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-10-20
- 状态：社区讨论中
- 作者邮箱：Bartosz Golaszewski <bartosz.golaszewski@oss.qualcomm.com>
- 概括：修复 Qualcomm QCE 引擎 AEAD 自测试暴露的问题：需要软件回退的决定此前写入共享转换上下文，并发请求可能互相清掉标志；AES-192 密钥设置后的标志也会被首次回退清空，导致后续请求错误进入硬件。现改用局部变量继承转换级回退状态，不再清除共享标志。CCM 模式在消息长度为非块对齐或负载跨多个散列表片段时引擎会停等并报硬件错误，现检测这些情况并强制走软件回退，使自测试通过。
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
- 概括：修复高通 qce 加密驱动在 CCM 附加认证数据处理中的三处错误：带关联数据的请求每次分配临时缓冲区但从不释放，造成内存泄漏；错误路径解除 DMA 映射时使用了错误的散列表，使已映射表泄漏并可能错误解除未映射表；DMA 映射失败返回零被误判为成功，导致后续用空表操作并对未映射表调用解除映射。现在在完成和错误路径正确释放缓冲区，并对齐映射与解除映射及失败检查，避免请求失败后的资源泄漏和错误清理。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: qce - check dma_map_sg() result for the source scatterlist
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261016-fix-qce-ccm-adata-leak-v1-2-f54a82af2de0@uniontech.com/

---

### ◆ 子系统：JitterEntropy（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: jitterentropy - add fast hardware jitter mixer extension**

- 日期：2026-09-13
- 状态：社区讨论中
- 作者邮箱：حنان المطيري <ha2020anan@gmail.com>
- 概括：为抖动熵子系统新增快速硬件抖动混合扩展：利用高精度周期计数器和内存指针属性扰动分支预测单元与硬件预取器，通过执行时间变化产生架构微熵，不依赖浮点运算，兼容内核空间。该扩展在x86上测试，用于生成熵序列，但代码中注明非加密用途。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/CANai08PJ9bKRn3JkgUP7SFHn+qXLoE_JDerRv-UtMkELZXu-wg@mail.gmail.com/

---

### ◆ 子系统：SPAcc（1 patches）

**▸ 组织：Vayavya Labs**（1 patches）

**[SERIES] crypto: spacc - Add SPAcc Crypto Driver** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-10-30
- 状态：社区讨论中
- 作者邮箱：Pavitrakumar Managutte <pavitrakumarm@vayavyalabs.com>
- 概括：为新思 DWC SPAcc 安全协议加速引擎新增内核驱动，支持将多种摘要与消息认证算法卸载到该硬件，包括 MD5、SHA-1、SHA-2、SHA-3 以及基于 SM4 的 CMAC、XCBC 和 HMAC 组合。驱动还可在自动检测配置下探测硬件实际支持的算法集合并注册，并加入构建配置，适用于集成该加密 IP 的平台。
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
- 概括：Safexcel AEAD请求的DMA映射方向过宽：关联数据只读、解密时认证标签只输入，却按双向或从设备方向映射，非一致缓存系统上卸载小块输入可能将同缓存行陈旧数据复制到有效输出，造成明文或密文事后损坏。同时，部分映射失败时公共清理会再次解除已自动回滚的映射。现根据各散表条目与输出范围的实际重叠划分输入、输出或双向，并只解除成功映射，避免二次解除。
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

*报告由 Linux Patches Tracker 自动生成 | 2026-11-11 12:44:37*
