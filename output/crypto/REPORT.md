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
| Kernel.org | [PATCH v2 00/20] Migrate x86 and RISC-V accelerated AES modes into library ------把 x86 与 RISC-V 上已有的 AES 各工作模式加速实现迁入内核加密库，并用 AES-NI 等指令为库补上 ECB、CBC、CTR、XTS 路径，再删除被取代的传统加密接口实现，使库调用和传统接口都经过同一套加速代码，消除过渡期因模板实例被低优先级库算法顶替而产生的性能回退。 |
| Red Hat | [PATCH v4 00/13] libcrypto: Provide more __cleanup functions for zeroizing data ------为内核加密库中的 AES 各模式密钥、消息摘要上下文和 HMAC 上下文等结构新增专用清零辅助函数，可配合自动清理机制在离开作用域时清除栈上敏感数据，替换原先分散的显式清零调用。同时补充统一文档说明密钥与上下文清零约定，并调整可信密钥和 SMB 客户端等调用点。 |
| Kernel.org | [PATCH v1 00/14] crypto: Remove the unnecessary crypto_rng API ------重构内核随机数生成路径：DRBG 和抖动熵源原先通过通用随机数算法接口访问，现改为库函数直接调用，并相应删除不再使用的通用随机数算法类型。DRBG 自检改为内置执行，抖动熵源健康检查推迟到首次使用时进行，避免未使用该功能时也产生启动开销；用户态算法接口改为直接调用这两个库。 |
| Kernel.org | [PATCH v1 00/3] lib/crypto: mldsa: Address some minor nits ------针对 ML-DSA 后量子签名验证库做若干健壮性修正：先校验公钥长度再计算后续数据地址，避免错误长度的公钥导致越界指针；显式拒绝非法算法参数并返回无效参数；同时标记验证结果必须被调用者检查。这些改动对现有合法调用者没有行为影响。 |
| Kernel.org | [PATCH v1 00/3] AES library fixups ------本次 AES 库修复包括三项：在 x86 的 CBC 加密中显式设置轮密钥寄存器别名，不再依赖上一函数碰巧留下的状态；提升 AES 库在 x86 和 RISC-V 平台上的优先级，避免优先级较低的其他驱动抢占 AES-NI 或 VAES 优化路径；并让 AES-NI 配置选入通用 AES、CBC 和 XTS 算法，保证启用该选项的系统仍具备 LUKS/dm-crypt 启动所需的算法。 |
| Intel | [PATCH v1 00/2] crypto: qat - fix config table locking ------英特尔的 QuickAssist 加速器在配置访问时存在锁保护不足，调试文件读取与配置增删之间不使用同一把锁，并发删除或更新可能导致释放后使用；现在将配置节的查找和插入纳入每设备锁，并用读锁保护调试读取。同时合并添加配置键时的重复链表遍历，一次定位旧条目后直接替换或释放，去掉临时缓冲和冗余搜索，实际行为不变。 |
| Kernel.org | [PATCH v1 00/2] hwrng: virtio - use min() in copy_data() ------虚拟随机数生成器驱动在复制数据时改用无符号类型通用的最小值宏替代带类型转换的旧宏，并依赖前面的边界检查保证差值为正；在设备命名时改用带长度限制的格式化函数，避免无界写入，同时使用已保存的索引。整体仅做代码清理和安全实践，不改变功能。 |
| Kernel.org | [PATCH] lib/crypto: powerpc/poly1305: Remove BROKEN implementation ------移除 PowerPC 平台的 Poly1305 加速实现。该实现此前因在软中断上下文无法工作而被标记为不可用且从未参与构建，实际汇编中还存在进位丢失等导致部分消息认证码计算错误的问题，并含有依赖秘密数据的分支。现在直接删除这些代码，后续可再考虑重新提交修复版本。 |
| 归属待核实（itx.no） | [v3] lib/crypto: sparc/aes-xts: Add optimization using the AES opcodes ------在 SPARC 平台利用 AES 指令实现内核库的 AES-XTS 加解密路径，覆盖 AES-128 和 AES-256 且每轮处理两个块，AES-192 及非 8 字节对齐数据回退到通用实现；同时恢复该库算法在 SPARC 上的注册并提高优先级，使磁盘加密等场景吞吐明显超过原先的传统实现。 |
| 归属待核实（free.fr） | [v2] crypto: caam/qi2 - lower the algorithm priority ------将 CAAM QI2 驱动的加密算法优先级从 2000 降到 100，避免它默认压过其他可用实现，与 QAT 驱动的处理保持一致。SEC 硬件引擎仍可通过驱动名称显式选择，用户态也能通过加密算法配置接口重新调高其优先级。 |
| Individual Contributor | [v2] crypto: qat - zero the VF migration state buffer on save ------修复 QAT 虚拟功能迁移状态缓冲区导出时的信息泄露：该缓冲区由堆分配，原先只写入已序列化段，未使用的尾部在首次导出时可能暴露堆中旧数据，后续导出也可能残留上次迁移数据。现在首次建立配置前清零整个缓冲区，之后每次保存状态前清零配置区域之后的部分。 |
| Kernel.org | [PATCH] crypto: x86/aria - Take the address of each asm function in one file ------解决 Clang 全链接时优化在多个目标文件对同一汇编弱符号取地址时会将其整体删除的链接错误。将 ARIA 各指令集版本的操作函数指针填充集中到各自所属的胶水文件中，通过新增的设置函数供各层调用，使每个汇编函数只在一个文件中被取地址，从而在启用 CFI 和全链接时优化时完成链接。 |
| Intel | [1/2] crypto: qat - initialise state_lock on every path in adf_devmgr_add_dev() ------英特尔的 QuickAssist 设备在虚拟功能重新创建且地址映射已存在时会提前返回，跳过状态互斥锁的初始化，导致后续启用或关闭设备时使用未初始化的互斥锁，可能触发锁调试警告。现在把互斥锁初始化移到设备状态建立前的公共路径上，确保所有创建流程都先完成初始化，避免重复创建虚拟功能时使用未初始化锁。 |
| Kernel.org | [PATCH] crypto: sa2ul - Fix HMAC key preparation ------德州仪器的 SA2UL 加密引擎驱动在准备 HMAC 密钥时，SHA-256 路径存在一字节缓冲区溢出，而且从未支持超过 64 字节的密钥。现在改为直接使用通用加密库的 HMAC 密钥准备接口，并去掉多余的间接调用，使长短密钥都能正确处理，也消除了该溢出。 |
| Infradead Community | [v2] crypto: ccp: psp-sev.h: clean up kernel-doc warnings ------AMD 安全处理器 SEV 的两个头文件中大量内核文档注释格式不规范，导致文档构建时出现成员描述缺失、结构体名称不匹配和误标记等警告。现在补上缺失的保留字段说明、修正结构体名称，并将不需要文档化的枚举注释改为普通注释，从而消除这些文档构建警告。 |
| Individual Contributor | [v4] crypto: talitos: init tasklets before requesting IRQs ------飞思卡尔 talitos 加密引擎驱动在申请中断后才初始化下半部任务，若引导加载程序或 kexec 内核在中断线上留下了挂起中断，注册时可能调度空回调。现在提前解析中断号和映射寄存器，先完成通道队列、设备复位和下半部初始化，再申请中断；同时修正错误路径中的中断号清理，避免释放从未申请的中断线。 |
| Individual Contributor | [v4] crypto/amlogic: Use devm APIs for clock management ------Amlogic 加密驱动原先手动获取并启用核心时钟，多个错误返回路径和卸载流程都要显式关闭，容易遗漏。改为使用设备资源管理的获取并启用接口后，时钟的禁用由内核自动完成，错误处理和卸载不再需要手动清理，探测流程得以简化。 |
| AMD | [v3,1/1] crypto: ccp - Make usage of sev_cmd_mutex more granular ------针对 AMD SEV 固件输入输出控制路径，原先进出时即持有命令互斥锁，覆盖了固件调用前的大量准备和用户内存拷贝；这些拷贝触发缺页异常时，在未来的客户机内存同页共享或私有原地转换场景下可能造成死锁。现将锁下移到各命令内部，仅围绕平台状态切换和固件命令执行持锁，缩短锁范围以避免潜在死锁。 |
| Individual Contributor | [v3] lib/crypto: chacha20poly1305: zeroize state in __chacha20poly1305_decrypt ------基于 ChaCha20-Poly1305 的解密辅助函数此前不在内部清除流密码状态，扩展随机数变体解密路径会把派生子密钥留在内核栈上；现将状态清零移入该辅助函数内部，使所有调用者都能自动清理，并把长度检查提前到调用方，避免无效输入时初始化临时状态。 |
| ANSSI | [v2] crypto: ecc - Handle exceptional points in Shamir multiplication ------椭圆曲线 Shamir 乘法对相同点、相反点和无穷远点处理有误，会拒绝部分合法 ECDSA 签名，并在公钥为基点或其负点时可能接受无效的消息摘要与签名组合；现补齐预计算和累加中的倍点、抵消与无穷远点处理，并加入相关回归测试，修正合法签名被拒和无效签名被接受的问题。 |

### 社区讨论

| 厂商 | 简介 |
|------|------|
| Bootlin | [PATCH v8 00/20] crypto: talitos - Driver cleanup ------对飞思卡尔Talitos安全引擎驱动进行结构调整：把原先单一文件按核心、摘要、对称加密、认证加密和硬件随机数拆分，按SEC1与SEC2硬件版本分别定义描述符和指针格式并以静态键判断版本，用宏替代重复的算法模板定义，同时删除版本判断所需的传递参数。这是纯代码组织梳理，算法行为不变。 |
| Rambus | [PATCH v5 00/19] crypto: cmh - add Rambus CryptoManager Hub driver ------为Rambus CryptoManager Hub硬件加密加速器添加完整驱动支持：先提供平台启动、邮箱命令队列、DMA和中断完成等基础设施，再注册摘要、认证、对称、公钥和后量子算法，例如SHA-2/SHA-3、SM3、SM4、RSA、椭圆曲线、ChaCha20-Poly1305、ML-KEM和SLH-DSA等；同时提供字符设备管理硬件驻留密钥的生成、导入和生命周期，使私钥不出硬件设备。 |
| Texas Instruments | [PATCH v10 00/15] Fix several issues in DTHEv2 driver ------针对德州仪器 DTHEv2 硬件加密引擎修复多类缺陷：修正空设备链表可能被当作有效项、自旋锁用法不一致可能在软中断下造成死锁、高内存页经虚拟地址转换可能破坏内存，以及设备数据在请求未完成时可能被提前释放；同时裁剪 AES 和 AEAD 散列表至实际长度以避免 DMA 等待多余数据超时，调整缓存同步使认证标签操作在解映射之后执行，防止缓存失效覆盖标签，并让 AEAD 仅在内存不足时回退以免生成错误结果。 |
| Vayavya Labs | [PATCH v27 00/4] crypto: spacc - Add SPAcc Crypto Driver ------为 Synopsys 安全协议加速器硬件加密引擎新增驱动，提供哈希与带密钥认证摘要支持，覆盖 MD5、SHA-1/2/3 系列及 SM4 消息认证码等算法，并支持硬件自动检测实际可用算法而非静态配置；同时补充设备树绑定和构建配置，使该引擎能够接入内核加密框架。 |
| Texas Instruments | [PATCH v1 00/30] Clean and improve SA2UL driver ------对德州仪器SA2UL安全引擎驱动做集中清理和修复：删除未使用的代码、宏和字段，释放安全上下文前清零以防密钥残留；修正初始化错误路径中的资源泄漏和DMA映射泄漏；修复哈希导出时缓冲区过小导致的栈越界以及并发修改命令标签的问题；动态计算元数据长度，加入真随机数发生器的AES-CM模式准备支持，并改用加密引擎框架处理请求。 |
| Qualcomm | [PATCH v12 00/3] crypto - qce: fix self-test issues in aead ------修复Qualcomm QCE加密引擎在AEAD自检中的多个问题。原实现把每请求软件回退决策存入共享上下文，导致并发请求竞争标志，并可能清除AES-192密钥设置的永久回退标志；CCM在非块对齐或分片载荷下也会使引擎停顿并报硬件错误。现改用局部变量决定每请求是否回退且不再清除永久标志，对非块对齐或跨多个散列表项的CCM请求强制走软件回退。结果并发AEAD请求不再误路由，CCM自检通过。 |
| Qualcomm | [PATCH v12 00/4] crypto: qce - fix self-test issues in skcipher ------修复Qualcomm QCE加密引擎对称加密自检失败和硬件停顿问题。XTS原本会把短于一个密码块的消息当作成功空操作或送入引擎导致停顿，现对这类请求返回参数错误；AES-CTR遇到部分最终块时引擎同样会停顿，现改走软件回退；分片载荷跨多个散列表项也会使引擎停顿，现检测后交给软件回退；XTS弱密钥此前被无条件拒绝导致自检失败，现仅在FIPS或禁止弱密钥时拒绝，非FIPS下改用软件回退完成加密。 |
| AMD | [PATCH v5 00/7] Implement SNP live firmware update support ------为AMD安全嵌套分页平台增加在线固件更新：注册固件上传接口并实现扩展下载命令。如果传统SEV平台正在运行则会拒绝更新，否则关闭传统SEV并释放其固件缓冲后加载新镜像，再恢复平台，期间SNP保持在线、SNP客户机不受影响；管理端可先临时加载再决定提交或回滚。还允许初始化后重新查询SNP平台状态和特性，并加锁避免与工厂重置等操作竞争。 |
| Texas Instruments | [PATCH v9 00/2] Add support for hashing algorithms in TI DTHE V2 ------为德州仪器DTHE V2硬件加密引擎的哈希单元补充SHA-224/256/384/512摘要算法以及基于它们的HMAC算法，使原本只支持AES相关模式的设备也能将这些摘要和带密钥摘要计算卸载到硬件完成，扩展该安全引擎可处理的算法范围，减少软件哈希开销。 |
| 归属待核实（mandelbit.com） | [PATCH v1 00/2] lib/crypto: x86/chacha: Add 16-block AVX-512 implementation ------为x86平台的ChaCha流密码增加一次处理16块数据、使用512位寄存器的AVX-512实现，对长度超过8块的输入替换原8块AVX-512路径，短尾仍沿用旧代码，不含因512位寄存器降频的CPU则继续使用原实现；同时新增KUnit测试，用参考实现校验不同长度、轮数、对齐、原地操作和跨块调用，覆盖各架构优化路径，并加入基准测试。 |
| 归属待核实（ptudor.net） | [PATCH v1 00/3] hwrng: add Microchip RNG90 support ------针对Microchip RNG90这一I2C接口加密随机数发生器新增驱动，负责唤醒和识别设备、构造信息与随机数读取命令，校验响应长度和循环冗余校验，遇到健康或自检失败时不向外暴露被拒绝的输出；熵质量采用最小非零估计，允许管理员后续调整。随驱动提供内核单元测试，通过脚本化I2C适配器覆盖命令帧、轮询恢复、挂起与移除等路径，使该器件可作为硬件随机数源接入内核。 |
| Amazon | [PATCH v6 00/6] crypto: skcipher - multi-data-unit request splitting ------为dm-crypt等调用者引入多数据单元请求机制。在同步加密请求中新增数据单元大小字段，允许一个请求携带多个数据单元；API层对不支持原生多单元的算法透明拆分为逐单元调用，每个单元使用按64位小端计数器步进的初始化向量。dm-crypt对符合条件的配置（如plain64和essiv）将一个连续块扇区批量提交，输出与逐扇区路径逐字节一致。这样减少了按扇区逐一请求的数量，异步算法需原生支持多单元才能批量。 |
| 浙江大学 | [v2] crypto: ccp - Fix use-after-free in backlog cmd advancement ------针对 CCP 密码协处理器允许积压的命令推进流程修复释放后使用：原先命令从积压列表取出到工作队列重新入队之间存在空档，销毁设备时冲刷不到该命令，后续工作可能访问已释放设备并唤醒已停止的内核线程，并发提交还可能占走预留槽位使计数超限；现改为在出队时原子转移空位，由队列内核线程执行推进回调后再入队，并在停止队列前标记暂停、禁止唤醒，消除该空档。 |
| Kernel.org | [PATCH] crypto: arc4 - Remove obsolete crypto API support for ARC4 ------移除 ARC4 在内核加密框架中的分组算法接口支持，因为内核内用户已直接使用底层库，无线守护进程也已改为用户态实现，且该算法接口早已被标为过时并在用户态算法接口默认禁止；底层 ARC4 库继续保留，用于内核内仍需支持的遗留协议。 |
| 归属待核实（gondor.apana.org.au） | [PATCH] crypto: caam - Remove public key support ------移除CAAM驱动中的公钥算法支持，因为这部分代码长期无人维护且存在严重缺陷。删除对应的硬件公钥实现后，内核不再向用户暴露这些有问题的加速接口，但也意味着使用CAAM的RSA等公钥操作会失去硬件卸载能力。 |
| Intel | [PATCH] crypto: qat - add support for enhanced decompression mode on GEN6 devices ------为Intel QAT第六代设备新增增强解压模式：固件可把原本仅用于压缩验证的内嵌解压引擎也用于处理解压请求，跳过压缩和转换阶段，提高解压吞吐量且不影响压缩请求。驱动添加管理命令在初始化时配置该模式，并通过sysfs属性读写控制；只有当服务配置包含压缩或解压时才能启用，未设置时默认值随服务配置决定。 |
| 归属待核实（gondor.apana.org.au） | [PATCH] crypto: aes - Add import_core/export_core to cmac/xcbc/cbcmac ------修复AES库实现的CMAC、XCBC和CBCMAC状态导出导入格式与通用模板不一致的问题。此前这些算法的导出格式不匹配，可能导致状态信息在迁移时丢失；现为三者添加自定义导出和导入函数，其中CMAC和XCBC导出前对保留块额外执行一次加密，确保未完成分块的状态不丢失。结果使这些基于AES的消息认证码在需要保存和恢复哈希状态时与通用模板行为一致。 |
| Individual Contributor | [PATCH] crypto: jitterentropy - add fast hardware jitter mixer extension ------为抖动熵子系统新增一种快速硬件抖动混合器。它利用高精度周期计数器，并结合内存指针属性动态干扰分支预测单元和硬件预取器，从CPU执行时序变化中提取架构级微熵；不依赖浮点运算，适用于内核空间。该混合器在x86架构上使用标准高精度宏完成测试，为抖动熵源提供额外的混合路径。 |
| Qualcomm | [v11,1/2] crypto: qce - Only register algos if the user really wants it ------Qualcomm QCE驱动的加密算法仍存在尚未触发自检失败的问题。为避免默认暴露有风险算法，新增模块参数控制算法注册，默认不向内核加密子系统注册任何算法；仅当用户显式设置参数为真时才注册。驱动电源管理部分保持运行，以便运行时电源管理继续调节互连和时钟门控。结果是默认禁用该引擎的加密算法，需要时由管理员手动启用。 |
| NXP | [RFC,4/4] crypto: remove async_tx framework ------删除不再使用的异步传输框架。该框架原为RAID5等提供内存拷贝、异或和校验等操作的异步卸载接口，最后一个使用者RAID5已改为同步操作，因此移除异步传输API及其相关文件。此改动只做代码删除和流程简化，不引入新的功能或行为变化。 |

---

## 已合入 Patches

### ◆ 子系统：General Crypto（33 patches）

**▸ 组织：Kernel.org**（15 patches）

**lib/crypto: powerpc/poly1305: Remove BROKEN implementation**

- 日期：2026-10-29
- 状态：已合入
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：移除 PowerPC 平台的 Poly1305 加速实现。该实现此前因在软中断上下文无法工作而被标记为不可用且从未参与构建，实际汇编中还存在进位丢失等导致部分消息认证码计算错误的问题，并含有依赖秘密数据的分支。现在直接删除这些代码，后续可再考虑重新提交修复版本。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261029063522.124421-1-ebiggers@kernel.org/

**[SERIES] lib/crypto: mldsa: Address some minor nits** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-10-29
- 状态：已合入
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：为内核 ML-DSA 后量子签名验证库补充边界和参数校验：原先在确认公钥长度前就根据公钥计算内部元素地址，若传入过短公钥可能越过数组边界；现在先验证长度再计算。同时显式拒绝无效算法标识，并给验证接口加上必须检查返回值的编译要求；当前调用者均传入合法参数并检查结果，属于健壮性修正。
- 达到阈值的 patches（2 个，显示前 5）：
  - lib/crypto: mldsa: Check pk_len before doing pointer arithmetic
  - lib/crypto: mldsa: Explicitly check that 'alg' is a valid value
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261029054534.68481-2-ebiggers@kernel.org/

**lib/crypto: mips: Disable Octeon SHA code on little-endian kernels**

- 日期：2026-10-22
- 状态：已合入
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：针对 MIPS64 的 Cavium Octeon 小端内核，禁用由协处理器加速的 SHA-1、SHA-256 和 SHA-512 实现。这些实现在小端构建中存在多处字节序转换缺失，向协处理器写入的消息字和状态字会发生字节反射，导致计算出的哈希值不正确；大端构建不受影响，因此仅在配置上限制为小端时不再启用这些加速代码，避免使用错误的硬件哈希路径。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261022054450.20746-1-ebiggers@kernel.org/

**[SERIES] lib/crypto: Use size_t lengths for Poly1305 and ChaCha** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-10-14
- 状态：已合入
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：将通用加密库中消息认证和流密码函数的长度参数从32位升级为与地址宽度一致的无符号长度类型，纠正64位平台上汇编实际按完整寄存器长度处理而声明仍为32位的不一致。原先在部分架构上参数高位可能未定义或被符号扩展，长度超过有符号32位上限时可能行为异常；消息认证更新中的长度加法也可能回绕。当前内核调用者未传超大长度，属于调用接口健壮性修正。
- 达到阈值的 patches（2 个，显示前 5）：
  - lib/crypto: poly1305: Use size_t length
  - lib/crypto: chacha: Use size_t length
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261014152604.323310-2-ebiggers@kernel.org/

**crypto: x86/aria - Take the address of each asm function in one file**

- 日期：2026-10-12
- 状态：已合入
- 作者邮箱：Kees Cook <kees@kernel.org>
- 概括：解决 Clang 全链接时优化在多个目标文件对同一汇编弱符号取地址时会将其整体删除的链接错误。将 ARIA 各指令集版本的操作函数指针填充集中到各自所属的胶水文件中，通过新增的设置函数供各层调用，使每个汇编函数只在一个文件中被取地址，从而在启用 CFI 和全链接时优化时完成链接。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261012031920.i.329-kees@kernel.org/

**[SERIES] crypto: atmel-tdes - use separate DMA scatterlists** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-10-11
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：Atmel TDES 驱动把原来用于 DMA 的输入、输出散列表从数组成员改为两个独立变量，并直接使用固定 4 字节总线宽度；在启动加密时复用已有的快速路径判断变量，不再重复读取标志；DMA 通道初始化出错时改为统一跳转到同一清理路径并释放已申请通道。属于内部流程整理，不改变加解密行为。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: atmel-tdes - use separate DMA scatterlists
  - crypto: atmel-tdes - reuse fast in atmel_tdes_crypt_start()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261011131556.272382-4-blum@kernel.org/

**[SERIES] lib/crypto: x86/sha: Follow the normal %rbp convention** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-10-11
- 状态：已合入
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：修正 x86 平台 SHA-1、SHA-256 和 SHA-512 汇编例程中帧指针建立晚于被调用者保存寄存器压栈的问题，使栈帧符合常规布局，帧指针寄存器按 C 代码约定指向返回地址。在使用帧指针展开器的内核中，这些函数内若发生调用栈转储，将不再退化为扫描整个栈，而是可靠输出调用者链条。
- 达到阈值的 patches（3 个，显示前 5）：
  - lib/crypto: x86/sha1: Follow the normal %rbp convention
  - lib/crypto: x86/sha256: Follow the normal %rbp convention
  - lib/crypto: x86/sha512: Follow the normal %rbp convention
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261011134843.166585-2-ebiggers@kernel.org/

**lib/crypto: poly1305: Use memzero_explicit() in poly1305_final()**

- 日期：2026-10-06
- 状态：已合入
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：针对 Poly1305 认证算法结束处理，原先用普通结构体赋值清空描述上下文，在链接时优化下该清零写操作可能被当作无用存储删除，导致状态和密钥材料残留；改用显式清零函数覆盖整个上下文，确保结束操作后敏感中间状态被清除。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261006083432.16328-1-ebiggers@kernel.org/

**[SERIES] AES library fixups** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-09-30
- 状态：已合入
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：修复 AES 汇编代码中一个密钥寄存器别名此前依赖前次调用残留、靠偶然才能正确工作的隐患，改为显式赋值；提高内核 AES 库中电子密码本、CBC、CTS、CTR 等模式的算法优先级，避免优先级较低的 CPP 和 Padlock 驱动反而覆盖 AES-NI 或 VAES 优化实现；并让启用 AES-NI 的配置自动选择 AES、CBC 和 XTS，保证 LUKS 或 dm-crypt 系统仍可正常启动解锁。
- 达到阈值的 patches（2 个，显示前 5）：
  - lib/crypto: x86/aes: Set RNDKEY in aes_cbc_encrypt_aesni()
  - crypto: aes - Boost priority of encryption modes further
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260930170542.140403-2-ebiggers@kernel.org/

**[SERIES] Migrate x86 and RISC-V accelerated AES modes into library** （cover letter，15/19 个 patch 达到代码量阈值）

- 日期：2026-09-27
- 状态：已合入
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：将 x86 和 RISC-V 架构上已有的 AES 电子密码本、密码块链接、计数器、XTS 等模式加速实现迁移到通用加密库，并为 x86 库函数新增 AES-NI 版本，使其性能与将被删除的传统专用算法一致；随后移除旧实现。迁移期间通过暂时禁用相关架构上的库算法接线，避免计数器加解密等模板实例误选慢速库实现；同时修正 XTS 加密调整值曾泄露到目标缓冲区的问题，改为只保存在寄存器或栈内。
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
- 概括：德州仪器的 SA2UL 加密引擎驱动在准备 HMAC 密钥时，SHA-256 路径存在一字节缓冲区溢出，而且从未支持超过 64 字节的密钥。现在改为直接使用通用加密库的 HMAC 密钥准备接口，并去掉多余的间接调用，使长短密钥都能正确处理，也消除了该溢出。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260923051116.92741-1-ebiggers@kernel.org/

**[SERIES] crypto: cast5 - use memcpy_and_pad() in cast5_setkey()** （cover letter，5/5 个 patch 达到代码量阈值）

- 日期：2026-09-21
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：将 cast5、cast6 算法以及 IXP4XX 和 Marvell 平台硬件驱动中多处密钥或 HMAC 缓冲区准备逻辑，从先复制再清零的两次操作改为一次复制并填充操作，简化这些路径的代码流程，不改变原有行为。
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
- 概括：Atmel TDES 加密驱动把两条传输路径中重复的传输长度保存和慢速路径缓冲同步操作上移到统一启动入口，两条路径改为直接读取已保存长度，减少重复代码和参数传递，属流程整理，不改变实际加密行为。
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
- 概括：基于 ChaCha20-Poly1305 的解密辅助函数此前不在内部清除流密码状态，扩展随机数变体解密路径会把派生子密钥留在内核栈上；现将状态清零移入该辅助函数内部，使所有调用者都能自动清理，并把长度检查提前到调用方，避免无效输入时初始化临时状态。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261005150324.5621-1-raizudeen.kerneldev@gmail.com/

**[SERIES] crypto: Use pm_runtime_resume_and_get()** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-09-22
- 状态：已合入
- 作者邮箱：Bui Duc Phuc <phucduc.bui@gmail.com>
- 概括：在 Sunxi、ARM CryptoCell 和 Gemini 三款密码加速器驱动中，把获取运行时电源引用并处理失败的手写逻辑统一替换为内核提供的“恢复并持有”辅助调用，失败时由该调用自动释放引用；原先多处手动在错误路径释放引用的代码被删除，行为保持不变，仅简化了错误处理流程。
- 达到阈值的 patches（3 个，显示前 5）：
  - crypto: sun8i-ss - Use pm_runtime_resume_and_get()
  - crypto: ccree - Use pm_runtime_resume_and_get()
  - crypto: sl3516 - Use pm_runtime_resume_and_get()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260922031954.320895-2-phucduc.bui@gmail.com/

**crypto: ccp: kill v3 IRQ tasklet during teardown**

- 日期：2026-09-20
- 状态：已合入
- 作者邮箱：Jiale Yao <yaojiale02@163.com>
- 概括：CCP v3 加密协处理器在支持 MSI-X 的 PCI 设备上，中断会调度延迟任务，而拆解路径释放中断后未等待已排队的任务结束，任务可能在设备内存释放后继续访问。现在在初始化失败和销毁两条路径中释放中断后终止该延迟任务，避免释放后访问。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260920173407.2126086-1-yaojiale02@163.com/

**crypto: ccp: kill v5 IRQ tasklet during teardown**

- 日期：2026-09-20
- 状态：已合入
- 作者邮箱：Jiale Yao <yaojiale02@163.com>
- 概括：CCP v5 加密协处理器在支持 MSI-X 的 PCI 设备上，中断会调度延迟任务，而拆解路径释放中断后未等待已排队的任务结束，任务可能在设备内存释放后继续访问。现在在初始化失败和销毁两条路径中释放中断后终止该延迟任务，避免释放后访问。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260920173417.2126346-1-yaojiale02@163.com/

**[v2] crypto: qat - zero the VF migration state buffer on save**

- 日期：2026-09-19
- 状态：已合入
- 作者邮箱：Karl Mehltretter <kmehltretter@gmail.com>
- 概括：修复 QAT 虚拟功能迁移状态缓冲区导出时的信息泄露：该缓冲区由堆分配，原先只写入已序列化段，未使用的尾部在首次导出时可能暴露堆中旧数据，后续导出也可能残留上次迁移数据。现在首次建立配置前清零整个缓冲区，之后每次保存状态前清零配置区域之后的部分。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260919054934.27322-1-kmehltretter@gmail.com/

**[v4] crypto/amlogic: Use devm APIs for clock management**

- 日期：2026-09-16
- 状态：已合入
- 作者邮箱：Mohamad Raizudeen <raizudeen.kerneldev@gmail.com>
- 概括：Amlogic 加密驱动原先手动获取并启用核心时钟，多个错误返回路径和卸载流程都要显式关闭，容易遗漏。改为使用设备资源管理的获取并启用接口后，时钟的禁用由内核自动完成，错误处理和卸载不再需要手动清理，探测流程得以简化。
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
- 概括：Intel QAT 设备管理器中两个互斥锁的生命周期管理有误：设备状态锁此前在部分提前返回路径上未初始化，导致同一物理位置重建虚拟功能时可能锁住未初始化的锁；虚拟功能到物理功能的通信锁原在设备停止时已销毁，但之后发送重启完成消息还会使用。把它们改为随加速设备注册和注销统一初始化与销毁，使锁在所需周期内始终有效，避免使用未初始化或已销毁的锁。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: qat - initialise state_lock on every path in adf_devmgr_add_dev()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261006150649.2517748-2-ahsan.atta@intel.com/

**crypto: qat - force an edge when re-enabling all VF2PF interrupts**

- 日期：2026-09-29
- 状态：已合入
- 作者邮箱：George Abraham P <george.abraham.p@intel.com>
- 概括：修复 Intel QAT 设备在 PF 复位或 AER 恢复后 VF 到 PF 中断可能丢失的问题。VF2PF 中断为边沿触发，原来重新启用时直接取消屏蔽，但设备复位会把屏蔽寄存器重置为未屏蔽，导致没有跳变，复位期间锁存的 VF 消息无法送达。现在在启用所有 VF 到 PF 中断前先全部屏蔽，再解除屏蔽，强制产生边沿，使这类消息能够重新投递。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260929083837.2102260-1-george.abraham.p@intel.com/

**[SERIES] crypto: qat - fix config table locking** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-09-18
- 状态：已合入
- 作者邮箱：Ahsan Atta <ahsan.atta@intel.com>
- 概括：英特尔的 QuickAssist 加速器在配置访问时存在锁保护不足，调试文件读取与配置增删之间不使用同一把锁，并发删除或更新可能导致释放后使用；现在将配置节的查找和插入纳入每设备锁，并用读锁保护调试读取。同时合并添加配置键时的重复链表遍历，一次定位旧条目后直接替换或释放，去掉临时缓冲和冗余搜索，实际行为不变。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: qat - hold cfg->lock when accessing config sections
  - crypto: qat - avoid redundant config list walks when adding a key
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260918124112.537571-2-ahsan.atta@intel.com/

**▸ 组织：Infradead Community**（2 patches）

**[v2] crypto: ccp: psp-sev.h: clean up kernel-doc warnings**

- 日期：2026-09-18
- 状态：已合入
- 作者邮箱：Randy Dunlap <rdunlap@infradead.org>
- 概括：AMD 安全处理器 SEV 的两个头文件中大量内核文档注释格式不规范，导致文档构建时出现成员描述缺失、结构体名称不匹配和误标记等警告。现在补上缺失的保留字段说明、修正结构体名称，并将不需要文档化的枚举注释改为普通注释，从而消除这些文档构建警告。
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
- 概括：Atmel SHA 硬件加密驱动在初始化转换请求时，如果驱动列表中已无可用设备，原先仍继续访问设备信息，可能在日志中读取空指针。现在在查找设备为空时直接返回设备不存在错误，避免无设备情况下的无效访问。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260913125143.109897-1-bolin.liu@seu.edu.cn/

**▸ 组织：Google**（1 patches）

**crypto: hisilicon/qm - annotate cap_tables with __counted_by_ptr**

- 日期：2026-09-23
- 状态：已合入
- 作者邮箱：Bill Wendling <morbo@google.com>
- 概括：为华为加速器驱动中的能力表指针添加计数关联属性，使编译器和消毒器能依据元素计数检查越界访问；同时调整初始化顺序，先填写计数再填入指针，避免插装检查看到有效指针但计数为零的瞬时状态而误报。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260923060114.2605310-1-morbo@google.com/

**▸ 组织：归属待核实（itx.no）**（1 patches）

**[v3] lib/crypto: sparc/aes-xts: Add optimization using the AES opcodes**

- 日期：2026-10-04
- 状态：已合入
- 作者邮箱：Stian Halseth <stian@itx.no>
- 概括：在 SPARC 平台利用 AES 指令实现内核库的 AES-XTS 加解密路径，覆盖 AES-128 和 AES-256 且每轮处理两个块，AES-192 及非 8 字节对齐数据回退到通用实现；同时恢复该库算法在 SPARC 上的注册并提高优先级，使磁盘加密等场景吞吐明显超过原先的传统实现。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261004192812.4145406-1-stian@itx.no/

**▸ 组织：Red Hat**（1 patches）

**[SERIES] libcrypto: Provide more __cleanup functions for zeroizing data** （cover letter，10/10 个 patch 达到代码量阈值）

- 日期：2026-09-16
- 状态：已合入
- 作者邮箱：Thomas Huth <thuth@redhat.com>
- 概括：为内核加密库中的 AES、XTS、GCM、CCM、MD5、SM3、BLAKE2、SHA-1 和 SHA-2 等密钥与上下文结构新增统一的自动清零辅助函数，供调用方在作用域结束时清除栈上敏感数据；同步替换已有显式清零，并让可信密钥与 SMB 客户端改用这些辅助函数，还补充零化文档。这是接口整理，不改变算法计算。
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
- 概括：为华为 HPRE 非对称加速器修复多项问题：修正 RSA 零长度输入时的越界读取；ECDH 输出缓冲区过小改为返回溢出错误，并按其硬件实际传输长度做 DMA 映射，消除对空指针的释放和合法请求被拒绝；DMA 一致性内存分配根据请求可否睡眠动态选择标志，避免原子上下文调度风险。同时删除未使用宏与字段，提取重复的簇数量计算。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: hisilicon/hpre - extract clusters num into inline function
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260918122726.3014899-4-qianweili@huawei.com/

**▸ 组织：归属待核实（genproof.com）**（1 patches）

**[SERIES] lib/crypto: chacha: Handle lengths of 2 GiB or more on 32-bit arm and MIPS** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-10-14
- 状态：已合入
- 作者邮箱：Vladimir Kukharenko <vladimir@genproof.com>
- 概括：修复 32 位 ARM 标量代码和 MIPS 汇编的 ChaCha 流密码在长度达到 2 GiB 以上时的错误：ARM 标量路径因有符号条件判断和块数计算溢出而只修改极少字节，MIPS 汇编因有符号分支提前进入部分块处理而少处理数据。现在 ARM 改用无符号条件，MIPS 在 C 层分块每次最多处理 1 GiB。当前内核调用者不会传如此大的长度，属于健壮性修正。
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
- 概括：针对 AMD 随机数驱动，原先请求 I/O 区域失败时错误信息中的偏移量硬编码，且端口映射失败消息缺少空格；现在统一使用已定义的偏移常量并修正错误消息格式，使输出更一致易读，实际行为不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261008093737.180712-2-blum@kernel.org/

**hwrng: intel - simplify intel_rng_mod_init()**

- 日期：2026-10-06
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：针对 Intel 硬件随机数驱动初始化，原先多处错误分支依赖统一出口和默认错误码返回；现在在设备不存在、内存分配失败、初始化失败等分支直接返回对应错误码，移除统一跳转出口，使初始化函数控制流更直接，不改变功能。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261006172628.103594-2-blum@kernel.org/

**hwrng: cctrng - simplify cctrng_probe()**

- 日期：2026-10-06
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：涉及 ARM CryptoCell 随机数发生器探测，注册失败时原先跳转到统一清理标签再返回；现在在错误分支直接执行电源管理清理并返回错误码，省去跳转标签，使探测函数更简洁，行为不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261006202734.104415-2-blum@kernel.org/

**hwrng: amd - simplify control flow in amd_rng_mod_init()**

- 日期：2026-10-02
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：在 AMD 硬件随机数驱动的模块初始化过程中，原先用跳转标签退出 PCI 设备遍历并分散处理多处错误清理，现在改为循环内匹配后直接跳出、随后检查设备是否存在，并把错误清理路径合并到一处，使初始化控制流更简洁，功能不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261002141952.169528-2-blum@kernel.org/

**hwrng: stm32 - use devm_platform_ioremap_resource() in stm32_rng_probe()**

- 日期：2026-10-02
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：针对 STM32 硬件随机数驱动探测，原先同时获取并映射 I/O 资源但资源指针并未使用，还留下多余的局部变量；现在改用只执行资源映射的接口并删除该未用变量，使探测函数更简洁，功能不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261002144839.51627-3-blum@kernel.org/

**hwrng: stm32 - use swap() in stm32_rng_probe()**

- 日期：2026-10-01
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：简化 STM32 硬件随机数发生器探测中时钟顺序的处理。当两个时钟中第一个不是所需的内核时钟时，原来通过临时变量手动交换两个时钟项，现在改用交换函数完成同样操作，确保内核时钟位于首位，行为不变，代码更紧凑。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261001210450.37467-2-blum@kernel.org/

**hwrng: stm32 - reuse clock rate in stm32_rng_clock_freq_restrain()**

- 日期：2026-10-01
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：简化 STM32 硬件随机数发生器时钟频率约束逻辑。原来在计算分频系数时已读取时钟速率，但调试输出前又重复获取一次时钟速率；现在复用之前读取的速率，同时清理调试信息中冒号前的多余空格，逻辑行为保持不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261001211612.38124-2-blum@kernel.org/

**hwrng: atmel - use HZ_PER_MHZ in atmel_trng_init()**

- 日期：2026-09-29
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：简化 Atmel 硬件随机数发生器的初始化流程。原来读取外设时钟速率并判断是否超过 100MHz 后设置半速率标志，现在合并判断条件，并使用每兆赫兹对应的赫兹常量替换硬编码频率值，逻辑行为保持不变，代码更简洁。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260929213751.103658-3-blum@kernel.org/

**[SERIES] hwrng: virtio - use min() in copy_data()** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-09-26
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：虚拟随机数生成器驱动在复制数据时改用无符号类型通用的最小值宏替代带类型转换的旧宏，并依赖前面的边界检查保证差值为正；在设备命名时改用带长度限制的格式化函数，避免无界写入，同时使用已保存的索引。整体仅做代码清理和安全实践，不改变功能。
- 达到阈值的 patches（2 个，显示前 5）：
  - hwrng: virtio - use min() in copy_data()
  - hwrng: virtio - use snprintf() in probe_common()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260926055853.4868-3-blum@kernel.org/

**hwrng: core - reject unknown RNG names**

- 日期：2026-09-24
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：配置当前硬件随机数设备时，若用户指定名称不在设备列表中，此前函数会返回成功但当前设备未改变。现在预先设置设备不存在错误，使未知名称被拒绝，避免误报成功。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260924212114.120633-2-blum@kernel.org/

**hwrng: intel - declare warning string as const**

- 日期：2026-09-23
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：Intel硬件随机数驱动在固件空间被锁定只读时会打印提示文字，该文字仅在初始化阶段使用且内容不变。现将其声明为只读初始化数据并调整格式，让提示字符串进入只读数据区。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260923104237.82599-2-blum@kernel.org/

**hwrng: amd - report partial reads in non-blocking mode**

- 日期：2026-09-23
- 状态：已合入
- 作者邮箱：Thorsten Blum <blum@kernel.org>
- 概括：AMD硬件随机数驱动在非阻塞读取时，若已经复制部分随机字节后暂无更多数据，会直接返回0，使本次部分读取被当作无数据。现在返回实际已复制的字节数，保留部分读取结果。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260923201259.90336-2-blum@kernel.org/

**▸ 组织：Individual Contributor**（1 patches）

**hwrng: omap3-rom: Use pm_runtime_resume_and_get()**

- 日期：2026-09-22
- 状态：已合入
- 作者邮箱：Bui Duc Phuc <phucduc.bui@gmail.com>
- 概括：OMAP3 ROM 硬件随机数发生器驱动在读取随机数时，原来用两步组合来恢复设备电源并处理错误，现在改用内核提供的合并接口直接完成恢复和错误处理，行为保持不变，仅简化了电源管理调用流程。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260922032054.320969-1-phucduc.bui@gmail.com/

**▸ 组织：归属待核实（gondor.apana.org.au）**（1 patches）

**[RESEND] hwrng: cctrng - Discard pm_runtime_put_autosuspend() return value**

- 日期：2026-10-15
- 状态：已合入
- 作者邮箱：Herbert Xu <herbert@gondor.apana.org.au>
- 概括：对于 Arm CryptoCell 真随机数发生器驱动，丢弃运行时 PM 自动挂起调用的返回值，不再记录错误。该返回值非零仅表示系统没有排队自动挂起检查，例如用户在 sysfs 中把设备运行时 PM 控制设为常开等正常情况也会出现；打印错误并无实际意义。这一修改也为将来将返回值类型改为空值做准备。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/atCau3kHbzUefyMA@gondor.apana.org.au/

---

### ◆ 子系统：CAAM (NXP)（3 patches）

**▸ 组织：归属待核实（free.fr）**（2 patches）

**[v2] crypto: caam/qi2 - lower the algorithm priority**

- 日期：2026-09-29
- 状态：已合入
- 作者邮箱：Vincent Jardin <vjardin@free.fr>
- 概括：将 CAAM QI2 驱动的加密算法优先级从 2000 降到 100，避免它默认压过其他可用实现，与 QAT 驱动的处理保持一致。SEC 硬件引擎仍可通过驱动名称显式选择，用户态也能通过加密算法配置接口重新调高其优先级。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260929-for-upstream-caam-qi2-priority-v2-1-bf0559ebf574@free.fr/

**crypto: caam/qi2 - reset the DPSECI at probe only when enabled**

- 日期：2026-09-28
- 状态：已合入
- 作者邮箱：Vincent Jardin <vjardin@free.fr>
- 概括：NXP CAAM队列接口驱动在探测时对所有数据路径对象无条件复位，未使能的对象会让管理控制器为每个队列打印可恢复事件，启动时产生大量错误日志。现在探测阶段先查询对象是否已使能，仅对已使能对象执行复位，移除路径不变。
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
- 概括：椭圆曲线 Shamir 乘法对相同点、相反点和无穷远点处理有误，会拒绝部分合法 ECDSA 签名，并在公钥为基点或其负点时可能接受无效的消息摘要与签名组合；现补齐预计算和累加中的倍点、抵消与无穷远点处理，并加入相关回归测试，修正合法签名被拒和无效签名被接受的问题。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260926204323.1913803-4-Jeremy.Jean@oss.cyber.gouv.fr/

---

### ◆ 子系统：Authenc（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: atmel: handle authenc requests without plaintext**

- 日期：2026-09-22
- 状态：已合入
- 作者邮箱：Karl Mehltretter <kmehltretter@gmail.com>
- 概括：Atmel加密驱动处理仅含关联数据、无明文的认证加密请求时，原本会无条件向AES DMA提交零字节传输，被DMA引擎拒绝，导致有效请求失败；同步完成路径还可能丢弃标签校验错误，把错误标签报告为解密成功。现在跳过零长度AES传输，并直接传递同步路径的认证结果，使此类请求正常完成，错误标签在新建和复用安全上下文时都返回认证失败。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260922051705.15329-1-kmehltretter@gmail.com/

---

### ◆ 子系统：TCrypt（1 patches）

**▸ 组织：归属待核实（gondor.apana.org.au）**（1 patches）

**crypto: tcrypt - Avoid reading req->base after submission**

- 日期：2026-09-22
- 状态：已合入
- 作者邮箱：Herbert Xu <herbert@gondor.apana.org.au>
- 概括：内核加密测试模块在速度测试中提交异步请求后仍读取请求对象内嵌的等待数据，该字段可能在处理期间被并发修改。现在将等待结构与请求对象合并成一个测试请求结构并整体传递，避免提交后再读取原请求字段。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/arJPHqt-vgu8md57@gondor.apana.org.au/

---

### ◆ 子系统：Skcipher（1 patches）

**▸ 组织：归属待核实（free.fr）**（1 patches）

**crypto: caam/qi,qi2 - set plain_keylen for skcipher descriptors**

- 日期：2026-09-28
- 状态：已合入
- 作者邮箱：Vincent Jardin <vjardin@free.fr>
- 概括：修复 CAAM 的 QI 和 QI2 队列接口在引入受保护密钥 AES 算法后出现的问题。该提交导致共享描述符加载零长度密钥，SEC 引擎把内联密钥字节当作命令解码，使 LX2160A 自检中除 XTS 外的对称加密全部失败。现在在设置普通对称加密密钥时记录实际明文密钥长度并禁用密钥命令选项，使描述符按正常密钥加载，恢复这些算法的加密操作。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260928-for-upstream-caam-qi-plain-keylen-v1-1-6edb56649cf9@free.fr/

---

### ◆ 子系统：AF_ALG API（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: algif_skcipher: rewind rounded output bytes**

- 日期：2026-10-04
- 状态：已合入
- 作者邮箱：Daehyeon Ko <4ncienth@gmail.com>
- 概括：在内核加密套接字处理连续对称加密请求时，原先接收迭代器按未取整的散列表长度推进，而实际加密只处理向下取整到块大小的长度，导致迭代器位置越过未写入数据；当读取端提供非零页面时，可能把上一页面生命周期中残留的旧字节当作结果返回给用户。现在先按取整余量回退迭代器，在长度为零时拒绝，并只用取整长度发起加密，消除这一错位暴露旧数据的问题。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261004050946.3131044-1-4ncienth@gmail.com/

---

### ◆ 子系统：Talitos（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[v4] crypto: talitos: init tasklets before requesting IRQs**

- 日期：2026-10-04
- 状态：已合入
- 作者邮箱：Rosen Penev <rosenp@gmail.com>
- 概括：飞思卡尔 talitos 加密引擎驱动在申请中断后才初始化下半部任务，若引导加载程序或 kexec 内核在中断线上留下了挂起中断，注册时可能调度空回调。现在提前解析中断号和映射寄存器，先完成通道队列、设备复位和下半部初始化，再申请中断；同时修正错误路径中的中断号清理，避免释放从未申请的中断线。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261004215042.383358-1-rosenp@gmail.com/

---

### ◆ 子系统：CCP/SEV (AMD)（1 patches）

**▸ 组织：AMD**（1 patches）

**[v3,1/1] crypto: ccp - Make usage of sev_cmd_mutex more granular**

- 日期：2026-10-21
- 状态：已合入
- 作者邮箱：Michael Roth <michael.roth@amd.com>
- 概括：针对 AMD SEV 固件输入输出控制路径，原先进出时即持有命令互斥锁，覆盖了固件调用前的大量准备和用户内存拷贝；这些拷贝触发缺页异常时，在未来的客户机内存同页共享或私有原地转换场景下可能造成死锁。现将锁下移到各命令内部，仅围绕平台状态切换和固件命令执行持锁，缩短锁范围以避免潜在死锁。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261021192434.1924950-2-michael.roth@amd.com/

---

### ◆ 子系统：ICE (Qualcomm)（1 patches）

**▸ 组织：The Good Penguin**（1 patches）

**[SERIES] crypto: use designated initializers for acpi_device_id** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-09-03
- 状态：已合入
- 作者邮箱：Pawel Zalewski <pzalewski@thegoodpenguin.co.uk>
- 概括：针对 AMD 安全处理器（CCP）与海思 SEC 驱动的 ACPI 设备匹配表，改用具名字段初始化并统一列表结尾格式，海思条目还删去冗余的零值私有数据；这是纯源码整理，让设备标识与私有数据的对应关系更直观，不改运行逻辑。
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
- 概括：移除内核随机数生成器的通用算法抽象层，DRBG 和抖动熵源改为直接库函数调用，标准随机数在 FIPS 模式下直接使用 DRBG，用户态随机数接口也改用库 API，删除通用随机数算法类型。同时修复 DRBG 混入未初始化栈数据，把抖动熵健康检查推迟到首次使用，保留自检，功能行为保持一致。
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

### ◆ 子系统：General Crypto（34 patches）

**▸ 组织：Individual Contributor**（6 patches）

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
- 概括：为压缩接口增加请求内单元大小和分段能力标志，并允许算法声明批量大小；zswap 在存储大页时按页组织批量请求，对支持批处理的压缩器一次提交多页，不支持的算法仍逐页处理并受每 CPU 缓存限制，同时先批量分配条目减少重复调用；后续会把压缩接口统一到相同调用约定，并使硬件并行压缩器能够真正并行处理多页。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: acomp - Define a unit_size in struct acomp_req to enable batching. mm: zswap: Set the unit size for zswap to PAGE_SIZE.
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261028030503.17923-2-kanchanapsridhar2026@gmail.com/

**crypto: amlogic - Free channel IRQs before disabling the clock**

- 日期：2026-10-15
- 状态：社区讨论中
- 作者邮箱：Myeonghun Pak <mhun512@gmail.com>
- 概括：在 Amlogic GXL 加密加速器中，通道中断请求先于通道数组分配，设备资源自动释放时会先释放数组再释放中断。若密码运算超时，中断处理程序可能已读取通道完成状态，在数组释放后仍写入状态并完成通道完成，造成释放后访问。现在在关闭总线时钟和设备资源释放通道数组之前显式释放所有通道中断，并放在加密引擎退出之后，既避免晚到中断访问已释放内存，又保持正常请求的中断驱动完成直到引擎排空。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/179203206852.2659709.13834828335447558448.G3@gmail.com/

**lib/crypto: md5: correct header inclusions**

- 日期：2026-10-15
- 状态：社区讨论中
- 作者邮箱：Mohamad Raizudeen <raizudeen.kerneldev@gmail.com>
- 概括：修正 MD5 库源文件的头文件包含。该文件使用了循环移位内联函数但未显式包含位操作头文件，过去依赖其他头文件间接引入；同时包含的非对齐访问头文件并未实际使用。现在补充位操作头文件并移除非对齐访问头文件，使头文件依赖与实际使用一致，减少间接包含变化带来的编译风险。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261015033843.6056-1-raizudeen.kerneldev@gmail.com/

**crypto: essiv: avoid request access after subrequest**

- 日期：2026-09-21
- 状态：社区讨论中
- 作者邮箱：Jiale Yao <yaojiale02@163.com>
- 概括：ESSIV 加密模板在提交子加密请求后仍读取请求上下文中的关联数据缓冲区指针；若异步完成提前运行，该缓冲区可能已被释放并完成外层请求，之后父请求继续访问该指针就会使用已释放内存或重复释放。现在在提交前保存该指针到局部变量，后续同步清理仅使用快照，避免释放后访问和二次释放。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260921090458.3364976-1-yaojiale02@163.com/

**▸ 组织：Kernel.org**（6 patches）

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
- 概括：在 GHASH 域乘常数的低位选择和密钥转换中，为选择掩码添加编译器隐藏，使编译器无法看到掩码用于二选一，从而避免生成依赖秘密数据的分支；当前并未观察到这类分支，属预防性处理。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261031052149.201983-1-ebiggers@kernel.org/

**lib/crypto: gf128mul: Hide selection mask values from compilers**

- 日期：2026-10-31
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：为 GF(2^128) 乘法中的倍乘路径隐藏选择掩码，避免编译器识别掩码后在处理秘密数据时生成条件分支；同时将部分只选固定多项式常数或零的掩码类型改为无符号长整型，避免 32 位架构被迫用寄存器对存放。当前未发现相关分支，属预防性加固。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261031052154.202008-1-ebiggers@kernel.org/

**crypto: arc4 - Remove obsolete crypto API support for ARC4**

- 日期：2026-10-31
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：移除 ARC4 在内核加密框架中的分组算法接口支持，因为内核内用户已直接使用底层库，无线守护进程也已改为用户态实现，且该算法接口早已被标为过时并在用户态算法接口默认禁止；底层 ARC4 库继续保留，用于内核内仍需支持的遗留协议。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261031211535.8793-1-ebiggers@kernel.org/

**[SERIES] x86: Remove cpu_has_xfeatures() and add AVX-512 xor_gen()** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-09-01
- 状态：社区讨论中
- 作者邮箱：Eric Biggers <ebiggers@kernel.org>
- 概括：x86 与 UML 在启动时核对 CPU 声明的 AVX/AVX-512 能力与对应扩展状态位，缺失时告警并清除特性标志，使加密、CRC 和异或等加速代码无需再单独检查扩展状态。随后为异或生成增加 AVX-512 路径，在 AMD Zen 4、Intel Sapphire Rapids、Rocket Lake、Nova Lake 等平台启用，4 千字节四盘基准吞吐由约 256 GB/s 升至约 492 GB/s。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: x86 - Stop using cpu_has_xfeatures()
  - lib/crypto: x86: Stop using cpu_has_xfeatures()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260901145740.42337-4-ebiggers@kernel.org/

**▸ 组织：Intel**（4 patches）

**[v2,1/2] crypto: qat - enable three-service mode for QAT GEN5 devices**

- 日期：2026-10-30
- 状态：社区讨论中
- 作者邮箱：Ahsan Atta <ahsan.atta@intel.com>
- 概括：针对英特尔 QAT 第五代加速设备，此前该驱动只允许同时启用两种服务，无法让对称加密、非对称加密和压缩三类卸载并发运行；现在新增三服务模式，补充对应固件对象布局、环到服务映射和线程到仲裁映射，使这些设备可同时提供三种加速服务。
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
- 概括：为Intel QAT第六代设备新增增强解压模式：固件可把原本仅用于压缩验证的内嵌解压引擎也用于处理解压请求，跳过压缩和转换阶段，提高解压吞吐量且不影响压缩请求。驱动添加管理命令在初始化时配置该模式，并通过sysfs属性读写控制；只有当服务配置包含压缩或解压时才能启用，未设置时默认值随服务配置决定。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261026035501.1627846-1-suman.kumar.chakraborty@intel.com/

**[SERIES] crypto: iaa - rework the WQ selection tables** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-10-19
- 状态：社区讨论中
- 作者邮箱：Vinicius Costa Gomes <vinicius.gomes@intel.com>
- 概括：为 Intel IAA 压缩/解压加速器重构工作队列选择表：原先按 CPU 全局索引分配队列会跨越物理包，且重建时并发请求可能读到空指针并失败；现在每物理包维护一张队列表，压缩在包内轮询，解压为各 CPU 固定一个队列，更新通过 RCU 发布并等待宽限期，避免跨包分配和并发访问失效。
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
- 概括：针对德州仪器 DTHEv2 加密驱动的 AES 和认证加密路径，修复链表空值、自旋锁不一致、高端内存引用、卸载时设备对象释放、散列表长度校验、DMA 描述符泄漏、填充缓冲对齐/分离等问题；认证加密仅在内存分配失败时回退软算法，标签操作改到散列表同步完成后进行，避免 IPSec 等场景下可能出现的 DMA 超时、内存破坏或标签被缓存失效覆盖。
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
- 概括：对德州仪器 SA2UL 加密驱动做系统性清理与修复：移除未使用字段和死代码，修正初始化及运行时错误路径中的安全上下文、哈希对象和 DMA 映射泄漏；修复导出哈希状态时栈缓冲区过小导致的越界，以及并发设置密钥可能破坏在途命令标签的问题，并在释放安全上下文前清零敏感数据。同时改用加密引擎统一排队请求，新增 AES-CM 随机数预热和硬件修订上报。
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
- 概括：为德州仪器DTHE V2硬件加密引擎的哈希单元补充SHA-224/256/384/512摘要算法以及基于它们的HMAC算法，使原本只支持AES相关模式的设备也能将这些摘要和带密钥摘要计算卸载到硬件完成，扩展该安全引擎可处理的算法范围，减少软件哈希开销。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: ti - Add support for SHA224/256/384/512 in DTHEv2 driver
  - crypto: ti - Add support for HMAC in DTHEv2 driver
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260910180424.2131193-2-t-pratham@ti.com/

**▸ 组织：AMD**（2 patches）

**[SERIES] Implement SNP live firmware update support** （cover letter，3/4 个 patch 达到代码量阈值）

- 日期：2026-10-21
- 状态：社区讨论中
- 作者邮箱：Pratik R. Sampat <prsampat@amd.com>
- 概括：为 AMD SEV-SNP 平台新增固件实时更新支持：管理员通过系统固件上传接口提交新镜像，驱动利用下载固件扩展命令执行更新；若传统 SEV 正在运行客户机则返回忙，已初始化则先关闭平台并释放固件缓冲区，更新后再恢复，SNP 部分在过程中保持运行，因此现有 SNP 虚拟机不受影响。配套调整固件加载器的引用计数，确保注销时所有上传操作已停止，避免模块或父设备被意外固定。
- 达到阈值的 patches（3 个，显示前 5）：
  - crypto: ccp - Factor out the release of the SEV firmware buffers
  - crypto: ccp - Allow SNP platform data to be queried after SNP INIT
  - crypto: ccp - Implement SNP Download Firmware EX
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/be72e0b1015156f8613fc2c360fa73d59108dcc6.1792599491.git.prsampat@amd.com/

**[RFC,kernel,04/17] crypto/ccp/tsm: Use TSM API for DOE**

- 日期：2026-09-16
- 状态：社区讨论中
- 作者邮箱：Alexey Kardashevskiy <aik@amd.com>
- 概括：AMD SEV 的 TSM 驱动在通过 PCI 数据对象交换接口发送 SPDM 消息时，从通用传输函数改用 TSM 专用传输接口，后者会执行更多健全性检查；这样在相关平台上发送和接收的请求会经过额外校验后继续处理。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260916115159.1938195-5-aik@amd.com/

**▸ 组织：归属待核实（gondor.apana.org.au）**（2 patches）

**crypto: aes - Add import_core/export_core to cmac/xcbc/cbcmac**

- 日期：2026-10-09
- 状态：社区讨论中
- 作者邮箱：Herbert Xu <herbert@gondor.apana.org.au>
- 概括：修复AES库实现的CMAC、XCBC和CBCMAC状态导出导入格式与通用模板不一致的问题。此前这些算法的导出格式不匹配，可能导致状态信息在迁移时丢失；现为三者添加自定义导出和导入函数，其中CMAC和XCBC导出前对保留块额外执行一次加密，确保未完成分块的状态不丢失。结果使这些基于AES的消息认证码在需要保存和恢复哈希状态时与通用模板行为一致。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/asjT87HAZ_UUbbvm@gondor.apana.org.au/

**[v2] crypto: hash - Preserve withheld block in export_core**

- 日期：2026-10-09
- 状态：社区讨论中
- 作者邮箱：Herbert Xu <herbert@gondor.apana.org.au>
- 概括：针对 CMAC 和 XCBC 等需要保留最后一个数据块才能完成计算的哈希算法，导出哈希状态时没有包含这个被保留的块，导致导出的状态不完整。修复方法是在导出前，如果存在保留块，先将其作为一次哈希更新处理，再导出状态，这样导出的状态就包含该块，后续可以正确恢复并继续计算。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/asjfxnGfCtvD7QJL@gondor.apana.org.au/

**▸ 组织：浙江大学**（1 patches）

**[v2] crypto: ccp - Fix use-after-free in backlog cmd advancement**

- 日期：2026-09-29
- 状态：社区讨论中
- 作者邮箱：Fan Wu <fanwu01@zju.edu.cn>
- 概括：针对 CCP 密码协处理器允许积压的命令推进流程修复释放后使用：原先命令从积压列表取出到工作队列重新入队之间存在空档，销毁设备时冲刷不到该命令，后续工作可能访问已释放设备并唤醒已停止的内核线程，并发提交还可能占走预留槽位使计数超限；现改为在出队时原子转移空位，由队列内核线程执行推进回调后再入队，并在停止队列前标记暂停、禁止唤醒，消除该空档。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260929143825.21349-1-fanwu01@zju.edu.cn/

**▸ 组织：Qualcomm**（1 patches）

**[v11,1/2] crypto: qce - Only register algos if the user really wants it**

- 日期：2026-10-22
- 状态：社区讨论中
- 作者邮箱：Bartosz Golaszewski <bartosz.golaszewski@oss.qualcomm.com>
- 概括：Qualcomm QCE驱动的加密算法仍存在尚未触发自检失败的问题。为避免默认暴露有风险算法，新增模块参数控制算法注册，默认不向内核加密子系统注册任何算法；仅当用户显式设置参数为真时才注册。驱动电源管理部分保持运行，以便运行时电源管理继续调节互连和时钟门控。结果是默认禁用该引擎的加密算法，需要时由管理员手动启用。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261022-qce-fixes-broken-label-v11-1-0d33c34fd0c3@oss.qualcomm.com/

**▸ 组织：归属待核实（jaseg.de）**（1 patches）

**[v3,06/12] crypto: api - Allocate tfms from the secret pool**

- 日期：2026-09-28
- 状态：社区讨论中
- 作者邮箱：Jan Sebastian Götte <linux@jaseg.de>
- 概括：内核加密 API 分配转换对象时，原来使用普通内存，其上下文中的扩展密钥调度表可能在崩溃转储中被捕获。现在改为从秘密内存池分配整个对象，使对应页面被崩溃内存动作标记，kdump 内核能够擦除这些页面，降低崩溃转储泄露密钥的风险；分配过程多一次桶查找，释放路径不变。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260928-crash-memaction-upstream-20260921-v3-6-e511e9ee2329@jaseg.de/

**▸ 组织：东南大学**（1 patches）

**[v2] crypto: inside-secure: initialize EIP93 state before requesting IRQ**

- 日期：2026-10-09
- 状态：社区讨论中
- 作者邮箱：Runyu Xiao <runyu.xiao@seu.edu.cn>
- 概括：调整 Inside Secure EIP93 加密引擎驱动的初始化顺序。原来先请求线程化中断，再初始化描述符环和引擎，而中断处理可能在注册后立即运行，此时硬件状态尚未就绪。现在先完成硬件与环初始化，再请求中断；若中断注册失败，则清理引擎和环寄存器，避免中断处理访问未初始化状态或释放时残留资源。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261009033149.1127441-1-runyu.xiao@seu.edu.cn/

**▸ 组织：归属待核实（sang-engineering.com）**（1 patches）

**crypto: ccp - unmap descriptor before completing cookie**

- 日期：2026-10-10
- 状态：社区讨论中
- 作者邮箱：Wolfram Sang <wsa+renesas@sang-engineering.com>
- 概括：调整 AMD CCP DMA 引擎中描述符完成的通知顺序。此前先标记 DMA 请求完成再解除描述符映射，可能导致缓冲区未被刷新；现在改为先解除映射、再完成请求通知，确保描述符解除映射完成后再通知上层，保障缓冲区刷新顺序。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261010125001.19300-3-wsa+renesas@sang-engineering.com/

**▸ 组织：NXP**（1 patches）

**[RFC,4/4] crypto: remove async_tx framework**

- 日期：2026-10-15
- 状态：社区讨论中
- 作者邮箱：Frank Li <Frank.Li@oss.nxp.com>
- 概括：删除不再使用的异步传输框架。该框架原为RAID5等提供内存拷贝、异或和校验等操作的异步卸载接口，最后一个使用者RAID5已改为同步操作，因此移除异步传输API及其相关文件。此改动只做代码删除和流程简化，不引入新的功能或行为变化。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261015-asycn_tx_remove-v1-4-056a7085e0a1@nxp.com/

**▸ 组织：Rambus**（1 patches）

**[SERIES] crypto: cmh - add Rambus CryptoManager Hub driver** （cover letter，13/13 个 patch 达到代码量阈值）

- 日期：2026-09-17
- 状态：社区讨论中
- 作者邮箱：Alex Ousherovitch <aousherovitch@rambus.com>
- 概括：为Rambus CryptoManager Hub硬件加密加速器添加完整驱动支持：先提供平台启动、邮箱命令队列、DMA和中断完成等基础设施，再注册摘要、认证、对称、公钥和后量子算法，例如SHA-2/SHA-3、SM3、SM4、RSA、椭圆曲线、ChaCha20-Poly1305、ML-KEM和SLH-DSA等；同时提供字符设备管理硬件驻留密钥的生成、导入和生命周期，使私钥不出硬件设备。
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
- 概括：为 AMD BC-250 的 PSP 新增支持并修正两个初始化问题：显示固件版本时若硬件能力报告 TEE 但驱动数据缺失，原会空指针崩溃，现在先检查驱动数据；启动 SEV 和 TEE 子设备时同时要求硬件能力与驱动数据，避免缺少某子设备数据使平台访问等功能一并丢失。新增该设备的标识和仅平台访问的驱动数据，使 PSP 能正常初始化并提供平台访问，TEE 因超时被禁用。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: ccp - do not start PSP sub-devices without their vdata
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/178984289057.12336.8102552838289034525@mtsistemi.it/

**▸ 组织：Huawei**（1 patches）

**[SERIES] crypto: hisilicon/qm - fix bugs and harden against abnormal hardware** （cover letter，2/4 个 patch 达到代码量阈值）

- 日期：2026-09-24
- 状态：社区讨论中
- 作者邮箱：Weili Qian <qianweili@huawei.com>
- 概括：华为硬件队列管理驱动针对异常硬件和固件差异做修复：缺少 ACPI 支持时不再把空指针传给电源管理判断，并清除运行时电源管理标志以跳过挂起恢复；设备能力版本读到无效值或寄存器读出的队列深度低于最小值时直接返回错误，避免后续数组越界或除零；不支持共享虚拟地址时修正错误路径，改为释放本地分配的用户加速接口设备，堵住内存泄漏。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: hisilicon/qm - clear runtime PM flag for non-power-manageable device
  - crypto: hisilicon/qm - check queue depth read from hardware
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260924113812.1110302-2-qianweili@huawei.com/

**▸ 组织：归属待核实（genproof.com）**（1 patches）

**[SERIES] lib/crypto: Handle large lengths in poly1305 and chacha20poly1305** （cover letter，1/5 个 patch 达到代码量阈值）

- 日期：2026-10-12
- 状态：社区讨论中
- 作者邮箱：Vladimir Kukharenko <vladimir@genproof.com>
- 概括：将通用加密库中的消息认证和流密码长度参数从32位改为与地址宽度一致的无符号长度类型，并同步修正64位RISC-V、MIPS和ARM64汇编对该参数的解释。原先在单次处理数吉字节级数据时，这些平台可能因高位未定义或被符号扩展而误读长度，造成越界读取；消息认证更新中的长度加法也会回绕，流密码只处理零头，原地加密可能残留明文。当前没有内核调用者传入如此大的数据，属于调用接口健壮性修正。
- 达到阈值的 patches（1 个，显示前 5）：
  - lib/crypto: chacha: Take a size_t length in chacha_crypt()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261012-libcrypto-4gib-lengths-v1-2-ea566c129a2e@genproof.com/

**▸ 组织：归属待核实（mandelbit.com）**（1 patches）

**[SERIES] lib/crypto: x86/chacha: Add 16-block AVX-512 implementation** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-10-25
- 状态：社区讨论中
- 作者邮箱：Antonio Quartulli <antonio@mandelbit.com>
- 概括：为x86平台的ChaCha流密码增加一次处理16块数据、使用512位寄存器的AVX-512实现，对长度超过8块的输入替换原8块AVX-512路径，短尾仍沿用旧代码，不含因512位寄存器降频的CPU则继续使用原实现；同时新增KUnit测试，用参考实现校验不同长度、轮数、对齐、原地操作和跨块调用，覆盖各架构优化路径，并加入基准测试。
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
- 概括：VIA 随机数发生器驱动为配合内核移除32位机器特定寄存器访问接口的计划，改为使用64位访问方式读写随机数配置寄存器，把原本分开的高低位操作合并成一个64位值，保持初始化逻辑不变，避免后续接口删除导致该驱动无法使用。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261026130223.773129-8-jgross@suse.com/

**▸ 组织：归属待核实（gondor.apana.org.au）**（1 patches）

**hwrng: cctrng - Lock read and writer of circular buffer**

- 日期：2026-10-26
- 状态：社区讨论中
- 作者邮箱：Herbert Xu <herbert@gondor.apana.org.au>
- 概括：Arm CryptoCell 随机数生成器驱动中，环形缓冲区在读取与写入之间没有任何同步机制，读取路径原先尝试获取自旋锁失败就直接返回，写入路径也不加锁，并发访问可能破坏缓冲区数据。现在改用互斥锁同时保护读取和写入，读取可被信号中断并返回错误，写入完成处理也在持锁下更新环形缓冲区，消除读写竞争。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/at7rX1rkRAzHYwCB@gondor.apana.org.au/

**▸ 组织：Individual Contributor**（1 patches）

**hwrng: mtk - wait long enough for the next word**

- 日期：2026-10-26
- 状态：社区讨论中
- 作者邮箱：Ryan Brue <ryanbrue.dev@gmail.com>
- 概括：联发科硬件随机数生成器在 MT8695 上产生下一个 32 位字所需时间超过原 60 微秒超时，中位数达 82 微秒，大多数读取因此失败或短读。将就绪等待超时提高到 1 毫秒，较快的生成器仍可立即返回，读取不再因超时中断。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261026-rbrue-sheldon-upstreaming-mtk-rng-timeout-v1-1-551b4b6b4f86@gmail.com/

**▸ 组织：归属待核实（ptudor.net）**（1 patches）

**[SERIES] hwrng: add Microchip RNG90 support** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-10-24
- 状态：社区讨论中
- 作者邮箱：Patrick Tudor <ptudor@ptudor.net>
- 概括：针对Microchip RNG90这一I2C接口加密随机数发生器新增驱动，负责唤醒和识别设备、构造信息与随机数读取命令，校验响应长度和循环冗余校验，遇到健康或自检失败时不向外暴露被拒绝的输出；熵质量采用最小非零估计，允许管理员后续调整。随驱动提供内核单元测试，通过脚本化I2C适配器覆盖命令帧、轮询恢复、挂起与移除等路径，使该器件可作为硬件随机数源接入内核。
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
- 概括：在椭圆曲线公钥生成过程中引入随机初始 Z 坐标。此前点乘的初始 Z 缺失，使得后续模逆运算的输入完全由私钥决定，而模逆并非恒定时间，运行时长可能泄露私钥信息。现在公钥生成时使用随机 Z 遮蔽模逆输入，与共享密钥派生路径一致；该改动覆盖蓝牙 SMP 和 TPM2 HMAC 会话等生成短暂 P-256 密钥的场景，性能影响在噪声范围内。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261026034429.742489-1-pawliczekerwin@gmail.com/

**crypto: ecc - Use constant-time modular inversion in ecc_point_mult()**

- 日期：2026-09-28
- 状态：社区讨论中
- 作者邮箱：Erwin Pawliczek <pawliczekerwin@gmail.com>
- 概括：椭圆曲线点乘中的模逆原先采用分支和迭代次数依赖输入的非恒定时间算法，ECDH私钥可能通过运行时间泄露；现改为恒定时间算法用于私钥参与的求逆，公开输入的签名验证继续使用原非恒定时间实现，并增加自测。性能上ECDH下降约12%到14%，且点乘坐标梯仍可能存在时间侧信道。
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
- 概括：移除CAAM驱动中的公钥算法支持，因为这部分代码长期无人维护且存在严重缺陷。删除对应的硬件公钥实现后，内核不再向用户暴露这些有问题的加速接口，但也意味着使用CAAM的RSA等公钥操作会失去硬件卸载能力。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/appZMZ7WS-KNaHbc@gondor.apana.org.au/

**▸ 组织：归属待核实（solid-run.com）**（1 patches）

**[RFC,net-next,2/3] crypto: caam/qi2 - skip isolated CPUs when setting up queue pairs**

- 日期：2026-09-30
- 状态：社区讨论中
- 作者邮箱：Josua Mayer <josua@solid-run.com>
- 概括：修复加密加速器队列接口驱动在隔离CPU场景下初始化被无限期推迟的问题。原先为每个在线CPU建立收发队列对并绑定轮询通知，但启用受管中断隔离的CPU没有分配亲和的数据处理接口对象，初始化遇到这类CPU就会卡住。现在只在线且属于内务受管中断集合的CPU上建立队列对和轮询通知，跳过隔离CPU，使探测继续；隔离CPU仍可提交加密请求，响应由内务CPU处理。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260930-dpaa2-isolcpus-v1-2-66c13f4fd75b@solid-run.com/

**▸ 组织：Individual Contributor**（1 patches）

**crypto: caam: jr: Use dedicated shutdown callback**

- 日期：2026-10-28
- 状态：社区讨论中
- 作者邮箱：Fabio Estevam <festevam@gmail.com>
- 概括：恩智浦 CAAM 加密任务环驱动在系统关机时复用设备移除流程，该流程会因仍有加密消费者持有引用而拒绝关闭，导致重启时出现设备忙警告。新增专用关机回调只关闭硬件任务环，不检查消费者引用也不注销算法，系统关机路径不再报告错误。
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
- 概括：对飞思卡尔 Talitos 安全引擎驱动做全面整理：将随机数、哈希、对称加密和认证加密实现拆分为独立文件，哈希改为按块处理并把尾部数据交回加密核心，迁移到类型专用初始化接口并用宏生成算法表；同时以静态分支区分 SEC1 与 SEC2 版本，拆分不同版本的硬件描述符结构，并补充维护者条目。整体为结构重构和流程简化。
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
- 概括：在 PKCS#7 签名验证中，对于 ML-DSA 这类直接消耗原始数据、不产生中间摘要的签名算法，获取摘要接口原来可能把认证属性的修改副本当作摘要返回给调用方。现在先检查算法是否直接处理数据，若是则直接返回不支持错误，明确表示没有可用摘要，避免 IMA 等调用方把非摘要数据当作摘要使用；调用方可以据此检测并跳过摘要处理。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20261015110826.126621-1-ampr.mhd@gmail.com/

**▸ 组织：归属待核实（cynove.com）**（1 patches）

**[SERIES] crypto: fix RSA results corrupted by non-coherent DMA** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-10-16
- 状态：社区讨论中
- 作者邮箱：Stephane Debusne <stephane.debusne@cynove.com>
- 概括：修复 RSA 签名与验证在非一致性 DMA 平台上的结果损坏问题：原先同步辅助函数和 PKCS#1 验证把数据或输出缓冲区紧邻请求上下文放在同一分配中，两者共享缓存行，设备写入结果后 CPU 缓存中的旧数据可能覆写输出，导致 i.MX8M Mini 上 RSA 签名或证书验证失败。现在将输出缓冲区单独分配，避免与请求上下文共享缓存行，使 DMA 结果正确。
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
- 概括：修复Qualcomm QCE加密引擎在AEAD自检中的多个问题。原实现把每请求软件回退决策存入共享上下文，导致并发请求竞争标志，并可能清除AES-192密钥设置的永久回退标志；CCM在非块对齐或分片载荷下也会使引擎停顿并报硬件错误。现改用局部变量决定每请求是否回退且不再清除永久标志，对非块对齐或跨多个散列表项的CCM请求强制走软件回退。结果并发AEAD请求不再误路由，CCM自检通过。
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
- 概括：针对高通 QCE 加密驱动的 CCM 模式，修复带关联数据请求中临时分配的关联数据缓冲区从不释放造成的内存泄漏，并纠正错误路径：源散列表 DMA 映射失败时原先未检测，且解除映射使用了错误的散列表。现在在完成和失败路径释放缓冲区，解除实际映射的散列表，映射失败返回输入输出错误，避免请求泄漏和错误清理。
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
- 概括：针对高通 QCE 加密引擎在 AES-XTS 短于一个块、AES-CTR 末尾不完整块、散列列表碎片化负载以及 XTS 两半密钥相等时会停转或错误拒绝的问题，改为：对不合法的 XTS 短请求返回参数错误，对硬件无法处理的 CTR 不完整块和碎片化负载转交软件后备；XTS 弱密钥在强制禁止时返回参数错误，非强制场景下也改用软件后备完成加密，使内核自检不再失败。
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
- 概括：对称加密请求新增每单元大小字段，调用方可一次提交多个数据单元；当底层算法不原生支持多单元处理时，加密或解密入口会按单元拆分并在单元间按 64 位小端计数器递增初始向量，输出与逐单元处理完全一致。配套用于 dm-crypt 批量提交连续扇区，默认 512 字节扇区时 4 KiB 段可合并为一次 8 单元请求，减少逐扇区开销；异步算法目前只有原生支持多单元的才可批量处理。
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
- 概括：为抖动熵子系统新增一种快速硬件抖动混合器。它利用高精度周期计数器，并结合内存指针属性动态干扰分支预测单元和硬件预取器，从CPU执行时序变化中提取架构级微熵；不依赖浮点运算，适用于内核空间。该混合器在x86架构上使用标准高精度宏完成测试，为抖动熵源提供额外的混合路径。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/CANai08PJ9bKRn3JkgUP7SFHn+qXLoE_JDerRv-UtMkELZXu-wg@mail.gmail.com/

---

### ◆ 子系统：SPAcc（1 patches）

**▸ 组织：Vayavya Labs**（1 patches）

**[SERIES] crypto: spacc - Add SPAcc Crypto Driver** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-10-30
- 状态：社区讨论中
- 作者邮箱：Pavitrakumar Managutte <pavitrakumarm@vayavyalabs.com>
- 概括：为 Synopsys 安全协议加速器 SPAcc 补充摘要算法支持与自动检测机制：新增 MD5、SHA-1、SHA-2、SHA-3 及基于 SM4 的 CMAC/XCBC 和对应 HMAC 卸载，自动检测模式可按硬件实际能力注册算法；同时加入设备树绑定和构建配置，适用于该硬件做摘要与消息认证码卸载。
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
- 概括：针对 Safexcel 加速器 AEAD 处理的 DMA 映射问题：原来在映射失败后仍会对已被自动撤销的映射执行取消映射，现在改为仅清理实际映射成功的列表；同时按每个缓冲区是否与输出范围重叠，为关联数据、认证标签和加解密输出选择正确的传输方向，避免非一致性系统上因过宽的输出方向把陈旧数据写回有效结果而导致的静默数据损坏。
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

*报告由 Linux Patches Tracker 自动生成 | 2026-11-11 15:34:16*
