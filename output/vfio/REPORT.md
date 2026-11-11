# Linux VFIO 子系统 Patch 追踪报告

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
| 社区讨论中 | 29 | 70.7% |
| 已合入 | 12 | 29.3% |
| 已关闭 | 0 | 0.0% |
| **总计** | **41** | **100%** |

### 按组织分类（TOP 15）

| 组织 | 数量 | 占比 |
|------|------|------|
| Individual Contributor | 8 | 19.5% |
| Google | 7 | 17.1% |
| NVIDIA | 7 | 17.1% |
| IBM | 4 | 9.8% |
| Kernel.org | 4 | 9.8% |
| Amazon | 2 | 4.9% |
| OzLabs Community | 2 | 4.9% |
| Red Hat | 2 | 4.9% |
| AMD | 1 | 2.4% |
| 归属待核实（baidu.com） | 1 | 2.4% |
| ARM | 1 | 2.4% |
| 归属待核实（openai.com） | 1 | 2.4% |
| Huawei | 1 | 2.4% |

### 按子系统分类

| 子系统 | 数量 | 占比 |
|--------|------|------|
| VFIO PCI | 16 | 39.0% |
| VFIO Core | 12 | 29.3% |
| VFIO Selftests | 3 | 7.3% |
| VFIO IOMMUFD | 2 | 4.9% |
| VFIO FSL-MC | 1 | 2.4% |
| VFIO Platform | 1 | 2.4% |
| VFIO AP (s390) | 1 | 2.4% |
| VFIO Migration | 1 | 2.4% |
| VFIO CCW (s390) | 1 | 2.4% |
| VFIO CDEV | 1 | 2.4% |
| VFIO CDX | 1 | 2.4% |
| VFIO MLX5 Variant | 1 | 2.4% |

## 重点 Patch Top20 清单

### 已合入

| 厂商 | 影响力 | 简介 |
|------|------|------|
| NVIDIA | 高（80） | [PATCH v7 00/10] mlx5 support for VFIO self test ------为 VFIO 自测试框架增加对 NVIDIA ConnectX 网卡的支持，新增用户态测试驱动能够通过设备命令接口完成硬件初始化、队列和内存区域创建，并建立 RDMA 写自回环数据通路执行 DMA 测试；同时把 MSI-X 向量接到完成事件队列，使自回环写完成时可触发中断，从而覆盖 DMA 与中断测试路径。 |
| Individual Contributor | 中（73） | [v2,1/2] vfio/nvgrace-gpu: Use a core-only open_device in fallback mode ------针对 NVIDIA Grace GPU 在 ACPI 内存属性缺失或 C2C 链接断开时进入的降级直通模式，原先打开设备会无条件注册毒页处理内存区间，零长度区间会覆盖整个地址空间并残留，导致二次打开失败、解绑后重新打开触发释放后使用。现为降级模式提供仅执行核心启用流程的打开操作，不再注册毒页区间，使打开关闭对称并消除残留与释放后使用问题。 |
| Huawei | 中（67） | [v6,2/2] hisi_acc_vfio_pci: reject live migration on 64KB page with QM_HW_V3 hardware ------在华为加速器第三代队列管理硬件采用虚拟功能控制模式且系统页大小为64KB时，功能寄存器和迁移寄存器共享第二个基地址寄存器区域同一物理页且无隔离，会把迁移寄存器暴露给客户机，导致客户机内核出现调用栈错误；此前直接在打开设备时拒绝导致直通完全不可用。现在把工作模式判断提前到探测阶段，检测到该组合时绑定通用虚拟功能 I/O 操作，保留设备直通并禁用实时迁移。 |
| Google | 中（62） | [v2] vfio: selftests: Add documentation ------为内核开发者新增 VFIO 自测试文档，说明如何准备真实 PCI 设备、绑定驱动、运行测试和清理环境，并介绍测试框架的库结构、设备与 IOMMU 抽象以及编写新测试的基本流程，便于开发者利用这些用户态程序为 VFIO、IOMMU 和中断路径编写功能或回归测试。 |
| Individual Contributor | 中（56） | [PATCH v2 00/7] vfio: mmap()/mprotect() hygiene for MMIO region mappings ------对平台、FSL-MC 和 CDX 总线上的 VFIO 内存映射做接口卫生修复：清除只读区域的允许写标志，防止用户通过内存保护调用把只读映射升级为可写；保持映射偏移使用逻辑文件偏移，避免设备撤销映射时找不到对应虚拟区域；同时拒绝 CDX 的写时复制私有映射。这些是防御性加固，堵住只读区域被改写和未来映射撤销被绕过的潜在途径。 |
| NVIDIA | 中（55） | [v3,1/1] vfio/pci: Remove the core dependency on driver data ------重构 VFIO PCI 核心与变体驱动之间的驱动数据传递，原先核心运行时代码把 PCI 驱动数据直接当作核心设备指针，要求所有变体驱动必须把核心设备放在私有数据起始处，限制私有布局并影响 Rust PCI 基础设施；现改为在各驱动侧生成包装回调，驱动可存放自己的私有结构再委托核心处理，解除核心对驱动数据布局的约束。 |
| 归属待核实（baidu.com） | 中（48） | [PATCH] vfio/pci: Restore 8-byte ioeventfd support ------修复 VFIO PCI 的 ioeventfd 注册，先前清理 64 位读写条件编译的提交错误地把仅在缺少 64 位写接口时才执行的 8 字节长度拒绝变成无条件拒绝，导致所有 8 字节 ioeventfd 注册失败；现在移除该无条件检查，恢复 8 字节 ioeventfd 支持。 |
| NVIDIA | 中（46） | [v2,1/4] vfio: Reject a second cdev open before mutating shared device state ------修复 VFIO 字符设备绑定路径的二次打开处理，原先单开检查位于绑定操作末尾，此时新绑定已可能改写设备令牌并记录 KVM 关联，失败回滚会清除当前打开者的关联或使引用失衡；现在在任何共享状态修改之前检查打开计数，检测到设备已占用时返回“设备忙”，使无法完成的绑定不触碰现有打开者状态。 |
| Individual Contributor | 低（43） | [v2] vfio/type1: avoid walking reserved-only mappings while unpinning ------设备直通解除大规模仅保留页的DMA映射时，原先仍逐页检查数千万个保留页做无效分类，可能长时间占用CPU并触发软锁；现在单独记录映射中是否含有非保留页，对仅保留页映射跳过逐页处理，缩短解除映射耗时。 |
| Individual Contributor | 低（38） | [v4] vfio/platform: prevent read-only region mappings from becoming writable ------平台设备经VFIO暴露只读MMIO区域时，原先只拒绝直接的可写映射，用户仍可先创建只读映射再提升内存保护权限改为可写；现在映射时清除区域的可写许可，堵住这种升级路径。当前没有树内平台驱动实际发布只读区域，属于防御性加固。 |
| Individual Contributor | 低（32） | [v3] vfio/fsl-mc: prevent read-only region mappings from becoming writable ------fsl-mc总线设备经VFIO暴露区域时，原先只拒绝直接的可写映射，用户仍可先创建只读映射再提升内存保护权限改为可写；现在映射时清除区域的可写许可，堵住这种升级路径。当前该总线所有区域都带写标志，暂无设备实际触发，属于防御性加固。 |
| Individual Contributor | 低（30） | [1/3] vfio/pci: Drain eventfd RCU callbacks on module exit ------vfio-pci核心模块卸载时，替换中断事件通知对象的释放回调可能仍挂在RCU队列中并指向即将卸载的模块代码；现在模块清理阶段先等待所有RCU回调执行完毕再退出，避免卸载后执行无效回调。 |

### 社区讨论

| 厂商 | 影响力 | 简介 |
|------|------|------|
| NVIDIA | 高（86） | [PATCH v6 00/31] vfio/pci: Add CXL Type-2 device passthrough support ------为直通框架增加计算快速链路第二类型设备支持，使虚拟机可访问这类设备及其主机管理数据内存。新增可按需加载的提供者模块，在设备绑定、复位、低功耗切换和热复位等节点协调状态保存与恢复；将设备内存区域作为共享内存缓冲区暴露给客户机，并阻止客户机直接访问主机管理数据内存解码器寄存器，同时虚拟化相关配置空间字段。这样既提供内存直通，也保证复位后解码器状态可恢复。 |
| Google | 中（73） | [PATCH v1 00/9] vfio: Add support for platform devices ------为轻量虚拟机工具补充平台设备直通能力，适用于把非 PCI 平台设备分配给客户机。此前平台设备的输入输出区域和中断缺少设备树描述，客户机无法绑定驱动。现在通过运行参数接收平台设备和可选设备树模板，预留客户机物理地址区域，将输入输出区域和中断写入生成的设备树节点，支持边沿触发中断，并修复同一组内后续设备的文件描述符泄漏，使客户机可依据模板中的兼容属性加载驱动。 |
| OzLabs Community | 中（73） | [PATCH v8 00/9] vfio/pci: Add mmap() for DMABUFs ------将 VFIO PCI 设备内存映射区的普通映射改为内部基于 DMA 缓冲区实现，允许显式导出的 DMA 缓冲区再被内存映射。此前委托部分设备内存需共享完整设备文件描述符，权限过大。现在普通映射创建单范围 DMA 缓冲区，缺页时从缓冲区查找物理页帧；导出缓冲区可映射给其他进程，只暴露被授权子范围。新增按描述符立即撤销缓冲区的用户请求，撤销会清空页表、解除导入并禁止后续映射，低功耗恢复路径也会恢复因低功耗而撤销的映射。 |
| Kernel.org | 中（70） | [PATCH v6 00/11] iommufd: Infrastructure for vIOMMU creation for confidential guests and guest TSM requests ------为使iommufd支持为保密客户机创建vIOMMU并转发客户TSM请求，先调整VFIO对KVM的引用：缓存VM文件引用而不是裸KVM结构指针，使虚拟机生命周期由文件引用管理，避免依赖KVM内部计数；字符设备绑定路径则在更新KVM文件前检查设备已打开，拒绝重复绑定，防止第二次绑定覆盖设备级KVM关联。随后引入外部vIOMMU提供者接口和vdevice TSM请求接口，删除旧的PCI客户请求入口。 |
| Google | 中（67） | [PATCH v6 00/18] iommu: Add live update state preservation ------为内核实时更新场景增加IOMMU状态保存与恢复：在保存阶段持久化IOMMU域、页表、设备和PASID状态，下一内核启动时恢复并重新附加；用户态可标记硬件页表参与保存，保存期间锁定映射并禁止分离设备，使经VFIO字符设备直通的设备能跨内核重启保持原有映射。 |
| IBM | 中（63） | [v6,1/5] s390/vfio-ap: Fix leak of pinned NIB and registered GISC in vfio_ap_irq_enable/disable() ------s390 AP队列直通中启用或禁用中断时，原先可能在中断仍使能时解除固定通知页，导致后续硬件中断DMA写入已释放页面，可能造成内存损坏或崩溃；现在禁用中断后先轮询确认中断位清除，超时则有意保留固定页和中断子类不释放以避免野写入，仅在队列不可用时立即释放。 |
| NVIDIA | 中（63） | [v2,12/12] vfio/nvidia-vgpu: add the Rust VFIO variant driver ------新增Rust编写的NVIDIA vGPU VFIO PCI驱动，用于将虚拟GPU实例直通给用户态；首次打开设备时通过SR-IOV物理功能接口创建实例，最后关闭时关闭实例，并强制使用分配的基地址寄存器窗口，协调固件复位与PCI复位。无可用的Nova vGPU接口时回退普通PCI直通。 |
| Google | 中（63） | [PATCH v1 00/7] iommu: Introduce Page Table Observability Framework ------在IOMMU域中增加页表分配计数，并把VFIO容器附加的各域页表内存用量通过文件描述符信息接口的新字段暴露给用户态，仅当所有域都由通用页表库实现时才报告完整数值，否则省略该字段；同时新增自测试验证稀疏映射后计数增加且解除映射后页面暂不回收，便于观察每个用户占用的IO页表内存。 |
| IBM | 中（62） | [v6,4/5] vfio/spapr_tce: Normalize EEH IOA error injection addresses ------在sPAPR VFIO EEH错误注入路径中，将用户态传入的Linux资源地址转换为平台错误注入接口期望的PCI总线地址，已是总线地址则原样保留；仅对内存或IO基地址寄存器访问类错误做转换，配置空间和DMA地址不转换，全零地址直接放行，避免因地址域不匹配而错误拒绝注入。 |
| Google | 中（62） | [PATCH v1 00/5] vfio/pci: Fix power state race with SR-IOV enablement ------修复VFIO PCI电源状态转换与SR-IOV启用间的竞争：关闭或注册设备时返回D0的转换未持内存锁，若用户同时启用虚拟功能且设备在D3hot，两个线程可能并发把设备切回D0，导致先恢复PF资源再启用虚拟功能或并发使用已保存电源状态，触发内核警告。现在所有电源转换都持锁，标记虚拟功能活动标志的无锁访问，并新增自测试覆盖关闭D3hot、启用SR-IOV及二者竞争，监控内核警告计数。 |
| ARM | 中（61） | [RFC,v2,12/15] vfio: Support VFIO devices that access the CPU MMU ------为没有输入输出内存管理单元、通过中央处理器内存管理单元执行直接内存访问的设备增加虚拟功能 I/O 支持。这类设备不使用容器，新增专门的设备组类型，允许设备注册和打开，同时跳过容器及输入输出内存管理单元相关的绑定和检查；虚拟机管理器需凭设备特定信息创建虚拟设备，因此不会分配容器。 |
| NVIDIA | 中（61） | [12/13] vfio/nvidia-vgpu: add the NVIDIA vGPU VFIO variant driver ------为英伟达虚拟图形处理器虚拟功能新增虚拟功能 I/O 变体驱动，仅通过驱动覆盖机制绑定英伟达设备并拒绝非虚拟功能。设备打开、复位和关闭生命周期交由物理功能侧的配套核心驱动协调；配置空间读取返回固件选定的设备和子系统标识，并按分配规格调整第一号基地址寄存器窗口大小，其余操作复用通用虚拟功能 I/O 设备核心。 |
| Google | 中（58） | [PATCH v3 00/4] Introduce vfio_dma_mapping_perf_test ------新增VFIO DMA映射性能自测试，不通过易波动的延迟阈值做通过失败判断，而是直接测量并报告内存映射、DMA映射、解映射和解除内存映射各阶段耗时，且预先填充内存页以隔离缺页处理；加入基于内存文件的映射路径来比较性能差异，并支持命令行指定DMA区域大小，便于可变规模的延迟测试。 |
| NVIDIA | 中（58） | [PATCH v1 00/19] vfio/pci: Handle PCI error recovery and report state to userspace ------为通用 VFIO PCI 驱动加入主机高级错误报告恢复支持并向用户态报告状态。此前恢复回调可能与配置访问、复位、中断、电源管理并发，导致访问重叠或已释放数据被读取。现在以恢复锁和访问阻塞标志统管各路径：普通访问持读锁，恢复持写锁等待在途访问并阻断新访问，复位与恢复互斥，中断被屏蔽。用户态启用后可从设备特性接口读取带序列号的状态，区分冻结、复位和失败并识别合并通知。仅通用驱动且用户显式启用后生效。 |
| IBM | 中（58） | [v11,5/5] vfio-pci/zdev: Add VFIO FMB device features ------为 IBM z 架构 PCI 设备新增函数测量块（FMB）直通用户态的 VFIO 设备特性。此前用户态无法直接获取该测量数据。现在提供两个特性：设置型特性可启用或禁用 FMB，启用时会先关闭再打开，重复启用等于重启测量；获取型特性仅在已启用时把最新 FMB 数据拷入用户提供的缓冲区，所需长度由设备信息能力上报，未启用时读取返回无消息。用户态可据此获取最新性能测量数据。 |
| Red Hat | 中（57） | [v2,3/7] vfio/pci: Add qcom-vfio-pci variant driver ------为高通 ath11k 和 ath12k WiFi 设备增加虚拟功能输入输出变体驱动。这些设备在虚拟机中因固件需要物理主机消息中断地址，而客户机只能看到虚拟地址，导致初始化失败。该驱动分配消息中断后缓存主机物理地址，写入扩展配置空间并附上特定签名，虚拟机内驱动自动发现并使用，无需修改虚拟机管理器。前提是虚拟机启用输入输出内存管理单元中断重映射和缓存模式，否则缓存地址写操作可能无法正确路由。 |
| NVIDIA | 中（55） | [PATCH v2 00/16] vfio/pci: Handle PCI error recovery and report state to userspace ------为让用户态感知并配合主机PCI错误恢复，VFIO PCI在所有设备访问路径中加入门控，恢复期间阻塞配置空间、内存映射空间、只读固件区、中断、复位和电源管理等操作，并先缓冲固件读取再复制给用户，防止用户态缺页阻塞恢复；新增恢复状态通知接口，向用户态报告冻结、重置或失败，恢复完成后自动恢复设备状态并允许用户重新配置中断。 |
| Individual Contributor | 中（52） | [PATCH] vfio/nvgrace-gpu: Skip PFN registration for empty memory regions ------NVIDIA Grace GPU在缺少ACPI内存属性或C2C链路断开而进入回退模式时，可用内存区长度为零，但设备打开仍会注册PFN地址空间，插入覆盖全部地址范围的节点；该节点不会被关闭路径移除，导致再次打开失败，设备解绑后后续注册或内存故障处理可能访问已释放内存，并错误记录无页结构的内存故障。现在长度为零时跳过注册和注销，避免上述问题。 |
| Kernel.org | 中（51） | [RFC,POC,31/50] vfio: install the migration data descriptor when the ioctl returns ------把VFIO迁移数据文件描述符的返回逻辑改为使用内核统一的描述符准备和安装机制，在迁移状态控制请求返回时安装数据描述符，并依赖文件退出路径完成清理，替代原来手动分配未用描述符、拷贝用户态后再安装并逐层回滚的做法，简化该路径的错误处理。 |
| Google | 低（43） | [v1] vfio/pci: pass FAULT_FLAG_WRITE to vmf_insert_pfn_pmd/pud() ------修复VFIO PCI映射设备内存时大页插入未传递写标志的问题。此前在共享可写虚拟内存区被降级为只读保护后，写缺页会进入大页写保护流程，但处理函数因写标志始终为假而不设置写权限，导致同一写缺页反复发生、陷入无限循环。现在从缺页标志中提取写意图并传给PMD/PUD级插入函数，使写缺页能正确标记大页表项为脏和可写，打破循环。 |

---

## 已合入 Patches

### ◆ 子系统：VFIO PCI（4 patches）

**▸ 组织：归属待核实（baidu.com）**（1 patches）

**vfio/pci: Restore 8-byte ioeventfd support**

- 日期：2026-09-22
- 状态：已合入
- 作者邮箱：Li,Rongqing <lirongqing@baidu.com>
- 概括：修复 VFIO PCI 的 ioeventfd 注册，先前清理 64 位读写条件编译的提交错误地把仅在缺少 64 位写接口时才执行的 8 字节长度拒绝变成无条件拒绝，导致所有 8 字节 ioeventfd 注册失败；现在移除该无条件检查，恢复 8 字节 ioeventfd 支持。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260922040013.2188-1-lirongqing@baidu.com/

**▸ 组织：Individual Contributor**（1 patches）

**[1/3] vfio/pci: Drain eventfd RCU callbacks on module exit**

- 日期：2026-09-26
- 状态：已合入
- 作者邮箱：Jiale Yao <yaojiale02@163.com>
- 概括：vfio-pci核心模块卸载时，替换中断事件通知对象的释放回调可能仍挂在RCU队列中并指向即将卸载的模块代码；现在模块清理阶段先等待所有RCU回调执行完毕再退出，避免卸载后执行无效回调。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260926162554.163197-2-yaojiale02@163.com/

**▸ 组织：NVIDIA**（1 patches）

**[v3,1/1] vfio/pci: Remove the core dependency on driver data**

- 日期：2026-10-05
- 状态：已合入
- 作者邮箱：Simon Song <xinmengs@nvidia.com>
- 概括：重构 VFIO PCI 核心与变体驱动之间的驱动数据传递，原先核心运行时代码把 PCI 驱动数据直接当作核心设备指针，要求所有变体驱动必须把核心设备放在私有数据起始处，限制私有布局并影响 Rust PCI 基础设施；现改为在各驱动侧生成包装回调，驱动可存放自己的私有结构再委托核心处理，解除核心对驱动数据布局的约束。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261005184236.1946167-2-xinmengs@nvidia.com/

**▸ 组织：Huawei**（1 patches）

**[SERIES] fix two issues in hisi_acc_vfio_pci driver** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-10-13
- 状态：已合入
- 作者邮箱：Longfang Liu <liulongfang@huawei.com>
- 概括：修复华为加速器 VFIO 直通驱动的两个问题：物理功能直通时复位准备路径会解引用空队列管理指针导致内核崩溃，现将迁移操作检查提前到复位入口，非迁移设备直接跳过队列管理复位协调，并清除复位标志，避免超时后错误释放其他锁；第三代队列管理硬件在 64KB 页下功能区域与迁移寄存器共享同一物理页，会向客户机泄漏迁移寄存器，改为在探测阶段判断驱动模式，使这类设备仍可直通但禁用活迁移，而不是直接拒绝。
- 达到阈值的 patches（1 个，显示前 5）：
  - hisi_acc_vfio_pci: reject live migration on 64KB page with QM_HW_V3 hardware
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261013071929.3988687-2-liulongfang@huawei.com/

---

### ◆ 子系统：VFIO Core（2 patches）

**▸ 组织：Individual Contributor**（2 patches）

**[SERIES] vfio/nvgrace-gpu: Separate the fallback-mode open_device** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-10-15
- 状态：已合入
- 作者邮箱：Andrea Parri <parri.andrea@gmail.com>
- 概括：修复 NVIDIA Grace GPU 在缺少 ACPI 内存属性或芯片间互联链路断开时进入降级模式的问题。原来降级模式共用完整打开函数但关闭时用核心路径，导致打开时注册覆盖全地址范围的内存区域节点，第二次打开失败，解绑后节点悬空触发释放后使用。现在为降级模式单独实现只做核心启用的打开函数，不再触碰内存区域节点，并移除完整打开中针对降级模式的长度检查。结果消除重复打开失败和释放后使用问题。
- 达到阈值的 patches（1 个，显示前 5）：
  - vfio/nvgrace-gpu: Use a core-only open_device in fallback mode
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261015081937.405320-2-parri.andrea@gmail.com/

**[v2] vfio/type1: avoid walking reserved-only mappings while unpinning**

- 日期：2026-09-19
- 状态：已合入
- 作者邮箱：Sam Crossley <samuelcrossley@gmail.com>
- 概括：设备直通解除大规模仅保留页的DMA映射时，原先仍逐页检查数千万个保留页做无效分类，可能长时间占用CPU并触发软锁；现在单独记录映射中是否含有非保留页，对仅保留页映射跳过逐页处理，缩短解除映射耗时。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260919-vfio-v2-1-68e7ed355972@gmail.com/

---

### ◆ 子系统：VFIO FSL-MC（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[v3] vfio/fsl-mc: prevent read-only region mappings from becoming writable**

- 日期：2026-09-03
- 状态：已合入
- 作者邮箱：Abdifatah Suruur <suruurism@gmail.com>
- 概括：fsl-mc总线设备经VFIO暴露区域时，原先只拒绝直接的可写映射，用户仍可先创建只读映射再提升内存保护权限改为可写；现在映射时清除区域的可写许可，堵住这种升级路径。当前该总线所有区域都带写标志，暂无设备实际触发，属于防御性加固。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260903092912.444-1-suruurism@gmail.com/

---

### ◆ 子系统：VFIO Platform（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[v4] vfio/platform: prevent read-only region mappings from becoming writable**

- 日期：2026-09-06
- 状态：已合入
- 作者邮箱：Abdifatah Suruur <suruurism@gmail.com>
- 概括：平台设备经VFIO暴露只读MMIO区域时，原先只拒绝直接的可写映射，用户仍可先创建只读映射再提升内存保护权限改为可写；现在映射时清除区域的可写许可，堵住这种升级路径。当前没有树内平台驱动实际发布只读区域，属于防御性加固。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260906123239.10858-1-suruurism@gmail.com/

---

### ◆ 子系统：VFIO Selftests（1 patches）

**▸ 组织：Google**（1 patches）

**[v2] vfio: selftests: Add documentation**

- 日期：2026-09-03
- 状态：已合入
- 作者邮箱：David Matlack <dmatlack@google.com>
- 概括：为内核开发者新增 VFIO 自测试文档，说明如何准备真实 PCI 设备、绑定驱动、运行测试和清理环境，并介绍测试框架的库结构、设备与 IOMMU 抽象以及编写新测试的基本流程，便于开发者利用这些用户态程序为 VFIO、IOMMU 和中断路径编写功能或回归测试。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260903183814.2111748-1-dmatlack@google.com/

---

### ◆ 子系统：VFIO CDEV（1 patches）

**▸ 组织：NVIDIA**（1 patches）

**[SERIES] vfio: Fix cdev second-open and harden selftests** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-09-11
- 状态：已合入
- 作者邮箱：Alex Williamson <alex.williamson@nvidia.com>
- 概括：修复虚拟功能输入输出设备字符设备接口的二次打开问题：原先第二次绑定会在最终拒绝前先改写共享的虚拟功能令牌和内核虚拟机指针，导致当前打开者的关联被破坏。现在把单次打开检查提前到绑定流程修改状态之前，冲突时返回设备忙，保证失败操作不改变现有用户状态。并补充自测验证这一点；同时将自测中混合匹配超时扩至 90 秒、运行器总超时扩至 600 秒，以容纳固件优先错误处理下设备被卡死和系统管理中断造成的长时间延迟。
- 达到阈值的 patches（1 个，显示前 5）：
  - vfio: Reject a second cdev open before mutating shared device state
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260911170429.1642480-2-alex.williamson@nvidia.com/

---

### ◆ 子系统：VFIO CDX（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[SERIES] vfio: mmap()/mprotect() hygiene for MMIO region mappings** （cover letter，5/5 个 patch 达到代码量阈值）

- 日期：2026-09-29
- 状态：已合入
- 作者邮箱：Abdifatah Suruur <suruurism@gmail.com>
- 概括：对平台、FSL-MC 和 CDX 总线上的 VFIO 内存映射做接口卫生修复：清除只读区域的允许写标志，防止用户通过内存保护调用把只读映射升级为可写；保持映射偏移使用逻辑文件偏移，避免设备撤销映射时找不到对应虚拟区域；同时拒绝 CDX 的写时复制私有映射。这些是防御性加固，堵住只读区域被改写和未来映射撤销被绕过的潜在途径。
- 达到阈值的 patches（5 个，显示前 5）：
  - vfio/fsl-mc: keep logical vm_pgoff in MMIO region mmap
  - vfio/platform: keep logical vm_pgoff in MMIO region mmap
  - vfio/cdx: keep logical vm_pgoff in MMIO region mmap
  - vfio/cdx: reject non-shared MMIO mmaps
  - vfio/cdx: prevent read-only region mappings from becoming writable
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260929094848.7439-6-suruurism@gmail.com/

---

### ◆ 子系统：VFIO MLX5 Variant（1 patches）

**▸ 组织：NVIDIA**（1 patches）

**[SERIES] mlx5 support for VFIO self test** （cover letter，3/5 个 patch 达到代码量阈值）

- 日期：2026-09-21
- 状态：已合入
- 作者邮箱：Jason Gunthorpe <jgg@nvidia.com>
- 概括：为虚拟功能输入输出自测框架加入对 mlx5 ConnectX 设备的支持。新增该设备的硬件初始化与命令接口驱动，通过命令队列完成启用、页面管理和保护域及内存密钥创建，并实现基于强制回环远程直接内存访问写的数据搬运路径；同时用专用事件队列关联消息中断向量，使回环写完成后能产生消息中断。还提供相关硬件结构、字段访问宏和内存映射输入输出辅助函数，允许驱动声明约 18MB 的缓冲区需求。自测现在可以在这些设备上运行直接内存访问和消息中断测试。
- 达到阈值的 patches（3 个，显示前 5）：
  - vfio: selftests: mlx5 driver - add send_msi support
  - vfio: selftests: Add mlx5 driver - data path and memcpy ops
  - vfio: selftests: Add mlx5 driver - HW init and command interface
- 来源：https://patchwork.kernel.org/project/kvm/patch/7-v7-c6d30e8ce1e4+3dfa6-mlx5st_jgg@nvidia.com/

---

## 社区讨论中 Patches

### ◆ 子系统：VFIO PCI（12 patches）

**▸ 组织：OzLabs Community**（2 patches）

**[SERIES] vfio/pci: Add mmap() for DMABUFs** （cover letter，7/8 个 patch 达到代码量阈值）

- 日期：2026-10-06
- 状态：社区讨论中
- 作者邮箱：Matt Evans <matt@ozlabs.org>
- 概括：针对 VFIO 直通 PCI 设备，将基地址寄存器空间的常规内存映射改为由直接内存访问缓冲区承载，并支持用户态对导出的缓冲区文件描述符执行内存映射，使进程可安全共享某段基地址寄存器子区域而无需交出完整设备句柄。新增用户请求撤销缓冲区机制，撤销时清除页表项、解除导入并禁止后续映射或附加；同时修复低功耗唤醒恢复路径未恢复撤销状态的问题，并调整导出锁避免潜在死锁。
- 达到阈值的 patches（7 个，显示前 5）：
  - vfio/pci: Un-revoke DMABUFs in LOW_POWER_ENTRY_WITH_WAKEUP resume
  - vfio/pci: Add a helper to look up PFNs for DMABUFs
  - vfio/pci: Add a helper to create a DMABUF for a BAR-map VMA
  - vfio/pci: Convert BAR mmap() to use a DMABUF
  - vfio/pci: Clean up BAR zap and revocation
  - ... 及其他 2 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261006193643.76330-3-matt@ozlabs.org/

**[v6,9/9] vfio/pci: Permanently revoke a DMABUF on request**

- 日期：2026-09-11
- 状态：社区讨论中
- 作者邮箱：Matt Evans <matt@ozlabs.org>
- 概括：VFIO PCI导出的DMABUF新增永久撤销状态，并可通过设备特性接口传入文件描述符请求永久撤销。成功后缓冲区不能再被导入、附加或映射，已有动态映射也会被清理解除。主要用途是驱动进程把PCI BAR范围借给子进程后，在客户端结束时收回访问权，使原DMABUF失效，再安全地把BAR资源重新导出给新客户端。临时撤销仍用于复位等既有场景。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260911214200.33793-10-matt@ozlabs.org/

**▸ 组织：Kernel.org**（2 patches）

**[SERIES] KVM/VFIO: guest_memfd support for device MMIO resources** （cover letter，6/6 个 patch 达到代码量阈值）

- 日期：2026-10-17
- 状态：社区讨论中
- 作者邮箱：Aneesh Kumar K.V <aneesh.kumar@kernel.org>
- 概括：为 KVM 受保护虚拟机中直通的 PCI 设备提供将设备 MMIO 资源作为客户机专用内存的支持。原先客户机专用内存只能分配普通物理页，无法处理直接提供物理帧号的设备 MMIO 资源；现在扩展提供者回调支持物理帧号后端，允许 VFIO PCI 附加设备 BAR，并限制主机访问、跟踪用户映射、在分离时清理。适用于希望将直通设备 MMIO 作为客户机私有内存管理的架构，要求架构支持受保护映射且默认禁用内存映射。
- 达到阈值的 patches（6 个，显示前 5）：
  - vfio/pci: Provide guest_memfd backing for PCI BARs
  - vfio/pci: Track userspace BAR mappings
  - vfio: Dispatch guest_memfd provider operations through the filesystem
  - vfio/pci: Restrict host BAR access for guest_memfd providers
  - vfio/pci: Detach guest_memfd access before teardown
  - ... 及其他 1 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261017073149.1303738-9-aneesh.kumar@kernel.org/

**[v8,17/23] vfio/pci: Hand out the P2PDMA provider behind a dma-buf**

- 日期：2026-09-28
- 状态：社区讨论中
- 作者邮箱：Leon Romanovsky <leon@kernel.org>
- 概括：为VFIO PCI导出的dma-buf增加P2PDMA提供者查询支持，使导入方能够通过通用接口得知对等流量是否可以直达导出的BAR。缓冲区被撤销后不再返回提供者，因为清理顺序是先撤销再释放设备注册，撤销后的缓冲区已没有可描述的对等资源。这样弥补了之前导入方无法获取提供者信息的缺口。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260928-fix-p2p-acs-v4-0-v8-17-404453b9c435@nvidia.com/

**▸ 组织：Google**（2 patches）

**[SERIES] vfio/pci: Fix power state race with SR-IOV enablement** （cover letter，3/5 个 patch 达到代码量阈值）

- 日期：2026-10-29
- 状态：社区讨论中
- 作者邮箱：David Matlack <dmatlack@google.com>
- 概括：修复 VFIO PCI 设备关闭与启用 SR-IOV 并发时的电源状态竞争。原先进程关闭设备时将设备从 D3hot 恢复到 D0 未持有内存锁，可能与用户写入启用 SR-IOV 参数的线程同时执行，导致 PF 的 BAR 恢复顺序错乱，触发内核警告，甚至并发释放保存的电源状态。现在所有电源状态转换都在写内存锁保护下进行，并对无锁访问的活动标志做显式标注，新增自测覆盖 D3hot 关闭、SR-IOV 与竞争场景。
- 达到阈值的 patches（3 个，显示前 5）：
  - vfio/pci: Hold memory_lock for all calls to vfio_pci_set_power_state()
  - vfio/pci: Annotate lockless accesses to vdev->sriov_active
  - vfio: selftests: Add test for device power state transitions
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261029203324.1637772-2-dmatlack@google.com/

**[v1] vfio/pci: pass FAULT_FLAG_WRITE to vmf_insert_pfn_pmd/pud()**

- 日期：2026-10-24
- 状态：社区讨论中
- 作者邮箱：Mina Almasry <almasrymina@google.com>
- 概括：修复VFIO PCI映射设备内存时大页插入未传递写标志的问题。此前在共享可写虚拟内存区被降级为只读保护后，写缺页会进入大页写保护流程，但处理函数因写标志始终为假而不设置写权限，导致同一写缺页反复发生、陷入无限循环。现在从缺页标志中提取写意图并传给PMD/PUD级插入函数，使写缺页能正确标记大页表项为脏和可写，打破循环。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261024015540.538758-1-almasrymina@google.com/

**▸ 组织：NVIDIA**（2 patches）

**[SERIES] vfio/pci: Add CXL Type-2 device passthrough support** （cover letter，23/25 个 patch 达到代码量阈值）

- 日期：2026-10-16
- 状态：社区讨论中
- 作者邮箱：Manish Honap <mhonap@nvidia.com>
- 概括：为 VFIO 直通增加 CXL 第二类设备（同时具备缓存和内存协议）支持，通过独立提供者模块在绑定时按需加载，不使普通 VFIO PCI 路径依赖 CXL 内部接口。将 CXL 内存区域暴露给虚拟机，支持内存映射和导出为直接内存访问缓冲区；主机管理内存解码器寄存器只读呈现并排除直接访问，组件寄存器由宿主机独占处理；同时接入复位、低功耗转换和内存错误隔离流程。
- 达到阈值的 patches（23 个，显示前 5）：
  - vfio/pci: Detect CXL devices and load the CXL provider on demand
  - vfio/pci: Add a generic excluded-range list
  - vfio/pci: Virtualize the CXL DVSEC in vfio_pci_config.c
  - vfio/pci: Call the CXL open and close hooks around device use
  - vfio/pci: Bracket PCI resets with the CXL reset hooks
  - ... 及其他 18 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261016161839.2765592-8-mhonap@nvidia.com/

**[SERIES] vfio/pci: Handle PCI error recovery and report state to userspace** （cover letter，15/19 个 patch 达到代码量阈值）

- 日期：2026-09-01
- 状态：社区讨论中
- 作者邮箱：Shameer Kolothum Thodi <skolothumtho@nvidia.com>
- 概括：给通用虚拟功能输入输出 PCI 设备驱动增加主机 PCI 错误恢复支持。新增恢复状态记录（进行中、冻结、已复位、失败）和锁，使设备打开/关闭、配置空间访问、基地址寄存器与只读存储器访问、中断操作、热复位、运行时电源管理等路径与恢复过程互斥。恢复期间阻止新访问并等待既有操作退出，再撤销映射，完成后恢复访问并唤醒等待者。该能力仅通用驱动提供且需用户空间开启，变体驱动不变。
- 达到阈值的 patches（15 个，显示前 5）：
  - vfio/pci: Serialize generic device lifetime with recovery
  - vfio/pci: Serialize function reset with recovery
  - vfio/pci: Serialize ioeventfd writes with recovery
  - vfio/pci: Retry BAR faults after temporary recovery
  - vfio/pci: Serialize BAR and ROM access with recovery
  - ... 及其他 10 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260901093217.8539-2-skolothumtho@nvidia.com/

**▸ 组织：Red Hat**（2 patches）

**[SERIES] vfio/pci: fall back to platform ROM when pci_map_rom() fails** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-10-21
- 状态：社区讨论中
- 作者邮箱：Michael S. Tsirkin <mst@redhat.com>
- 概括：当 VFIO PCI 设备的 ROM BAR 存在但内容不可读（例如 GPU 未被系统固件初始化）时，原来在 BAR 映射失败后会直接停止，无法使用引导加载器保存的 ROM 或平台固件提供的 ACPI ROM 方法。现在在映射失败后先尝试引导加载器保存的 ROM，再尝试 ACPI ROM 方法，使这类设备的视频 BIOS 仍可通过 VFIO 读取。对某些原有行为保守处理，仅作为最后回退。
- 达到阈值的 patches（1 个，显示前 5）：
  - vfio/pci: read ROM via ACPI _ROM when hardware ROM is unreadable
- 来源：https://patchwork.kernel.org/project/kvm/patch/8ab8fdfe47a8d9c9f10680ddb4a03bccad43f7c5.1792566536.git.mst@redhat.com/

**[SERIES] Enable Qualcomm WiFi PCIe passthrough to VMs** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-10-11
- 状态：社区讨论中
- 作者邮箱：Jose Ignacio Tornos Martinez <jtornosm@redhat.com>
- 概括：针对高通 ath11k/ath12k WiFi 设备直通到虚拟机时固件只接受物理主机消息信号中断地址、而客户机只能得到虚拟地址导致中断无法送达的问题，主机侧新增高通专用虚拟功能输入输出驱动，在 PCIe 扩展配置空间用专用魔数签名缓存主机消息信号中断地址和数据；虚拟机内对应无线驱动检测到该签名后读取缓存值，否则回退标准配置，并为两种芯片增加全局复位后的链路恢复重试，使设备透传可用。
- 达到阈值的 patches（1 个，显示前 5）：
  - vfio/pci: Add qcom-vfio-pci variant driver
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261011074514.515894-3-jtornosm@redhat.com/

**▸ 组织：AMD**（1 patches）

**[RFC] vfio/pci: Block for the upstream bridge lock in vfio_pci_core_disable()**

- 日期：2026-09-08
- 状态：社区讨论中
- 作者邮箱：YuanShang <YuanShang.Mao@amd.com>
- 概括：VFIO PCI设备禁用时，原先用尝试锁获取上游桥锁，同一桥下的多个虚拟功能并发释放时，未获得锁的设备会跳过复位直接交还用户，且无日志。现在改为阻塞等待上游桥锁，使同一桥下的释放串行完成复位；多个功能依次拆除时，每个功能都要付出一次复位等待时间。修复场景常见于SR-IOV虚拟功能同时释放。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260908080946.2235849-1-YuanShang.Mao@amd.com/

**▸ 组织：IBM**（1 patches）

**[v11,5/5] vfio-pci/zdev: Add VFIO FMB device features**

- 日期：2026-10-28
- 状态：社区讨论中
- 作者邮箱：Omar Elghoul <oelghoul@linux.ibm.com>
- 概括：为 IBM z 架构 PCI 设备新增函数测量块（FMB）直通用户态的 VFIO 设备特性。此前用户态无法直接获取该测量数据。现在提供两个特性：设置型特性可启用或禁用 FMB，启用时会先关闭再打开，重复启用等于重启测量；获取型特性仅在已启用时把最新 FMB 数据拷入用户提供的缓冲区，所需长度由设备信息能力上报，未启用时读取返回无消息。用户态可据此获取最新性能测量数据。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261028154352.15108-6-oelghoul@linux.ibm.com/

---

### ◆ 子系统：VFIO Core（10 patches）

**▸ 组织：IBM**（2 patches）

**[v6,4/5] vfio/spapr_tce: Normalize EEH IOA error injection addresses**

- 日期：2026-10-23
- 状态：社区讨论中
- 作者邮箱：Narayana Murty N <nnmlinux@linux.ibm.com>
- 概括：在sPAPR VFIO EEH错误注入路径中，将用户态传入的Linux资源地址转换为平台错误注入接口期望的PCI总线地址，已是总线地址则原样保留；仅对内存或IO基地址寄存器访问类错误做转换，配置空间和DMA地址不转换，全零地址直接放行，避免因地址域不匹配而错误拒绝注入。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261023073642.59657-5-nnmlinux@linux.ibm.com/

**[v2] vfio: Use file-based reference counting for KVM**

- 日期：2026-09-03
- 状态：社区讨论中
- 作者邮箱：Steffen Eiden <seiden@linux.ibm.com>
- 概括：VFIO与KVM集成不再手动获取和释放KVM模块引用，改为在接口中传递虚拟机文件指针，由内核文件引用计数管理KVM生命周期，页面跟踪等回调也随之改为接收文件。这样可移除设备中保存的释放函数指针和手工符号引用，并删除KVM对外导出的相关符号，为将来第二套KVM模块并行存在创造条件。适用于s390加密设备等使用VFIO与KVM交互的场景。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260903-vfio-v2-1-ef4cd4190ae7@linux.ibm.com/

**▸ 组织：NVIDIA**（2 patches）

**[v2,12/12] vfio/nvidia-vgpu: add the Rust VFIO variant driver**

- 日期：2026-10-23
- 状态：社区讨论中
- 作者邮箱：Simon Song <xinmengs@nvidia.com>
- 概括：新增Rust编写的NVIDIA vGPU VFIO PCI驱动，用于将虚拟GPU实例直通给用户态；首次打开设备时通过SR-IOV物理功能接口创建实例，最后关闭时关闭实例，并强制使用分配的基地址寄存器窗口，协调固件复位与PCI复位。无可用的Nova vGPU接口时回退普通PCI直通。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261023154009.2246627-13-xinmengs@nvidia.com/

**[12/13] vfio/nvidia-vgpu: add the NVIDIA vGPU VFIO variant driver**

- 日期：2026-09-05
- 状态：社区讨论中
- 作者邮箱：Zhi Wang <zhiw@nvidia.com>
- 概括：为英伟达虚拟图形处理器虚拟功能新增虚拟功能 I/O 变体驱动，仅通过驱动覆盖机制绑定英伟达设备并拒绝非虚拟功能。设备打开、复位和关闭生命周期交由物理功能侧的配套核心驱动协调；配置空间读取返回固件选定的设备和子系统标识，并按分配规格调整第一号基地址寄存器窗口大小，其余操作复用通用虚拟功能 I/O 设备核心。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260905081116.106613-13-zhiw@nvidia.com/

**▸ 组织：Amazon**（2 patches）

**vfio: Create the group chardev outside vfio.group_lock**

- 日期：2026-09-11
- 状态：社区讨论中
- 作者邮箱：Sakac, Pavol <sakacpav@amazon.de>
- 概括：VFIO组字符设备创建原来全程持有全局组锁，包括分配、命名和字符设备注册，导致并行设备探测时无关的组创建也串行化并成为争用热点。现在只在锁内登记IOMMU组身份和检查重复，实际的分配、命名、字符设备添加及事件发送都在锁外执行；竞争者看到未发布保留后会等待并重试。这样全局组锁不再被字符设备注册和事件广播拖长，改善并行探测下的争用。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260911-vfopt-s4-v1-0-98ba1d2ef7ab@amazon.de/

**[RFC,8/8] vfio: Opt the group and vfio-dev class devices into staged sysfs**

- 日期：2026-09-11
- 状态：社区讨论中
- 作者邮箱：Sakac, Pavol <sakacpav@amazon.de>
- 概括：为VFIO组字符设备和vfio设备类设备启用分阶段sysfs注册：两者位于类目录下，类设备不会匹配驱动，也没有类接口消费者，因此可以安全地延迟到目录完全构建后再一次性发布。这样在大量虚拟功能并发注册时，sysfs目录构建不会在早期锁路径上排队，避免组字符设备移出全局锁后产生的并发注册争用转移到sysfs锁。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260911174414.97060-8-sakacpav@amazon.de/

**▸ 组织：Individual Contributor**（1 patches）

**vfio/nvgrace-gpu: Skip PFN registration for empty memory regions**

- 日期：2026-09-25
- 状态：社区讨论中
- 作者邮箱：Andrea Parri <parri.andrea@gmail.com>
- 概括：NVIDIA Grace GPU在缺少ACPI内存属性或C2C链路断开而进入回退模式时，可用内存区长度为零，但设备打开仍会注册PFN地址空间，插入覆盖全部地址范围的节点；该节点不会被关闭路径移除，导致再次打开失败，设备解绑后后续注册或内存故障处理可能访问已释放内存，并错误记录无页结构的内存故障。现在长度为零时跳过注册和注销，避免上述问题。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260925161024.189771-1-parri.andrea@gmail.com/

**▸ 组织：ARM**（1 patches）

**[RFC,v2,12/15] vfio: Support VFIO devices that access the CPU MMU**

- 日期：2026-10-15
- 状态：社区讨论中
- 作者邮箱：Ryan Roberts <ryan.roberts@arm.com>
- 概括：为没有输入输出内存管理单元、通过中央处理器内存管理单元执行直接内存访问的设备增加虚拟功能 I/O 支持。这类设备不使用容器，新增专门的设备组类型，允许设备注册和打开，同时跳过容器及输入输出内存管理单元相关的绑定和检查；虚拟机管理器需凭设备特定信息创建虚拟设备，因此不会分配容器。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261015142552.4128028-13-ryan.roberts@arm.com/

**▸ 组织：归属待核实（openai.com）**（1 patches）

**vfio: Publish the container after all fallible initialization**

- 日期：2026-10-30
- 状态：社区讨论中
- 作者邮箱：Kyle Zeng <kylebot@openai.com>
- 概括：调整VFIO模块初始化顺序，将容器发布和杂项设备注册挪到所有可能失败的步骤之后，并把无IOMMU后端注册提前到杂项设备之前。之前并发打开可能在初始化失败时拿到容器文件，模块释放后这些文件仍指向已释放的回调，导致越界访问；现在一旦用户态能打开VFIO设备，模块初始化已不会再失败，失败路径按逆序回收资源。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261030042337.74512-1-kylebot@openai.com/

**▸ 组织：Google**（1 patches）

**[SERIES] vfio: Add support for platform devices** （cover letter，6/7 个 patch 达到代码量阈值）

- 日期：2026-10-24
- 状态：社区讨论中
- 作者邮箱：Mostafa Saleh <smostafa@google.com>
- 概括：为 kvftool 虚拟机管理器新增 VFIO 平台设备直通能力，使用户可通过新命令行选项将系统平台总线下的设备（事先绑定到 VFIO 平台驱动）分配给虚拟机。原先只支持 PCI 设备直通；现在预留客户机地址空间，映射设备的 MMIO 区域并生成设备树节点，支持边沿触发中断，并允许用户提供设备树模板复制兼容属性等绑定信息，便于客户机驱动匹配。
- 达到阈值的 patches（6 个，显示前 5）：
  - vfio: Factor out wired IRQ setup and teardown
  - vfio: Support edge-triggered wired IRQs
  - vfio: Add basic support for vfio-platform
  - vfio: Reserve guest address space for VFIO platform
  - vfio: platform: Add interrupts support
  - ... 及其他 1 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261024161902.2093581-2-smostafa@google.com/

---

### ◆ 子系统：VFIO Selftests（2 patches）

**▸ 组织：Google**（2 patches）

**[SERIES] iommu: Introduce Page Table Observability Framework** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-10-01
- 状态：社区讨论中
- 作者邮箱：Pranjal Shrivastava <praan@google.com>
- 概括：在IOMMU域中增加页表分配计数，并把VFIO容器附加的各域页表内存用量通过文件描述符信息接口的新字段暴露给用户态，仅当所有域都由通用页表库实现时才报告完整数值，否则省略该字段；同时新增自测试验证稀疏映射后计数增加且解除映射后页面暂不回收，便于观察每个用户占用的IO页表内存。
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio/type1: Expose IO page table usage via fdinfo
  - vfio/selftests: Add observability test for IO page table usage
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261001224531.765278-5-praan@google.com/

**[SERIES] Introduce vfio_dma_mapping_perf_test** （cover letter，3/4 个 patch 达到代码量阈值）

- 日期：2026-09-10
- 状态：社区讨论中
- 作者邮箱：Aaron Lewis <aaronlewis@google.com>
- 概括：为 VFIO 设备直通场景新增 DMA 映射性能自测程序，不再采用易受环境波动影响的通过或失败判定，而是直接测量并输出内存映射、DMA 映射、DMA 解除映射和解除内存映射四个阶段的耗时；同时增加基于内存文件描述符的映射路径测试，用于展示该路径相对更快的延迟，并允许用户通过命令行指定 DMA 区域大小，便于在不同规模下测试。还在解除映射接口中集中校验区域是否完整解除映射，简化各测试的重复检查。
- 达到阈值的 patches（3 个，显示前 5）：
  - vfio: selftests: Introduce vfio_dma_mapping_perf_test
  - vfio: selftests: Add memfd test to vfio_dma_mapping_perf_test
  - vfio: selftests: Allow a size for vfio_dma_mapping_perf_test
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260910153326.3085937-2-aaronlewis@google.com/

---

### ◆ 子系统：VFIO IOMMUFD（2 patches）

**▸ 组织：Kernel.org**（1 patches）

**[SERIES] iommufd: Infrastructure for vIOMMU creation for confidential guests and guest TSM requests** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-09-17
- 状态：社区讨论中
- 作者邮箱：Aneesh Kumar K.V <aneesh.kumar@kernel.org>
- 概括：为使iommufd支持为保密客户机创建vIOMMU并转发客户TSM请求，先调整VFIO对KVM的引用：缓存VM文件引用而不是裸KVM结构指针，使虚拟机生命周期由文件引用管理，避免依赖KVM内部计数；字符设备绑定路径则在更新KVM文件前检查设备已打开，拒绝重复绑定，防止第二次绑定覆盖设备级KVM关联。随后引入外部vIOMMU提供者接口和vdevice TSM请求接口，删除旧的PCI客户请求入口。
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio: cache KVM VM file references instead of raw struct kvm pointers
  - vfio: cdev: Reject duplicate bind before updating KVM file
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260917140159.1163281-2-aneesh.kumar@kernel.org/

**▸ 组织：Google**（1 patches）

**[SERIES] iommu: Add live update state preservation** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-10-25
- 状态：社区讨论中
- 作者邮箱：Samiullah Khawaja <skhawaja@google.com>
- 概括：为内核实时更新场景增加IOMMU状态保存与恢复：在保存阶段持久化IOMMU域、页表、设备和PASID状态，下一内核启动时恢复并重新附加；用户态可标记硬件页表参与保存，保存期间锁定映射并禁止分离设备，使经VFIO字符设备直通的设备能跨内核重启保持原有映射。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommufd: Add APIs to preserve/unpreserve a vfio cdev
  - vfio/pci: Preserve the iommufd state of the vfio cdev
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261025021930.674647-17-skhawaja@google.com/

---

### ◆ 子系统：VFIO AP (s390)（1 patches）

**▸ 组织：IBM**（1 patches）

**[v6,1/5] s390/vfio-ap: Fix leak of pinned NIB and registered GISC in vfio_ap_irq_enable/disable()**

- 日期：2026-09-04
- 状态：社区讨论中
- 作者邮箱：Anthony Krowiak <akrowiak@linux.ibm.com>
- 概括：s390 AP队列直通中启用或禁用中断时，原先可能在中断仍使能时解除固定通知页，导致后续硬件中断DMA写入已释放页面，可能造成内存损坏或崩溃；现在禁用中断后先轮询确认中断位清除，超时则有意保留固定页和中断子类不释放以避免野写入，仅在队列不可用时立即释放。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260904093435.1161402-2-akrowiak@linux.ibm.com/

---

### ◆ 子系统：VFIO Migration（1 patches）

**▸ 组织：Kernel.org**（1 patches）

**[RFC,POC,31/50] vfio: install the migration data descriptor when the ioctl returns**

- 日期：2026-09-15
- 状态：社区讨论中
- 作者邮箱：Christian Brauner <brauner@kernel.org>
- 概括：把VFIO迁移数据文件描述符的返回逻辑改为使用内核统一的描述符准备和安装机制，在迁移状态控制请求返回时安装数据描述符，并依赖文件退出路径完成清理，替代原来手动分配未用描述符、拷贝用户态后再安装并逐层回滚的做法，简化该路径的错误处理。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260915-work-fd-reserve-unify-folded-v1-31-4d5217d6b246@kernel.org/

---

### ◆ 子系统：VFIO CCW (s390)（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[v1] vfio/ccw: Flush notoper_work before returning from reset**

- 日期：2026-09-22
- 状态：社区讨论中
- 作者邮箱：Yuho Choi <oss.patchbox@gmail.com>
- 概括：vfio-ccw在解除DMA映射回调中触发关闭事件，若子通道进入不可操作状态，通道程序页面释放被推迟到异步工作队列，导致回调返回时页面仍被固定，可能使VFIO解除映射重试耗尽并触发主机崩溃。现在在复位返回前等待该异步工作完成，确保页面已解除固定；正常关闭路径因工作未排队会立即返回，不受影响。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260922164928.477669-1-oss.patchbox@gmail.com/

---

---
## 子系统说明

- **VFIO PCI**：PCI 设备直通（vfio-pci 驱动，最常用的 VFIO 模块）
- **VFIO Platform**：平台设备直通（vfio-platform 驱动）
- **VFIO FSL-MC**：NXP Freescale Management Complex 总线设备直通
- **VFIO CDX**：Xilinx CDX 总线设备直通
- **VFIO Mediated Device**：中介设备框架（GPU/NIC 虚拟化切分）
- **VFIO IOMMUFD**：VFIO 与 IOMMUFD 框架的集成接口
- **VFIO CCW (s390)**：IBM s390 架构 Channel I/O 设备直通
- **VFIO AP (s390)**：IBM s390 架构 Adjunct Processor 设备直通
- **VFIO Migration**：虚拟机热迁移中的 VFIO 设备状态迁移
- **VFIO MLX5 Variant**：NVIDIA MLX5 变体驱动（基于 vfio-pci 扩展）
- **VFIO HiSilicon ACC**：华为海思加速器变体驱动
- **VFIO PDS Variant**：AMD Pensando 变体驱动
- **VFIO CDEV**：VFIO 字符设备接口（cdev ioctl 方式）
- **VFIO Selftests**：VFIO 内核自测试用例
- **VFIO Core**：VFIO 核心框架（设备发现、group/container 管理）

---

## 项目说明

本项目用于追踪 Linux 内核 VFIO (Virtual Function I/O) 子系统的 patch 提交情况。VFIO 允许用户空间程序直接访问硬件设备，主要应用于虚拟机设备直通（KVM/QEMU）和用户空间驱动（DPDK、SPDK）。

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

*报告由 Linux Patches Tracker 自动生成 | 2026-11-11 16:48:00*
