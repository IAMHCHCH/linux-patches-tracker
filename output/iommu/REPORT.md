# Linux IOMMU 子系统 Patch 追踪报告

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
| 社区讨论中 | 69 | 87.3% |
| 已合入 | 5 | 6.3% |
| 已关闭 | 5 | 6.3% |
| **总计** | **79** | **100%** |

### 按组织分类（TOP 15）

| 组织 | 数量 | 占比 |
|------|------|------|
| Google | 11 | 13.9% |
| Individual Contributor | 9 | 11.4% |
| NVIDIA | 8 | 10.1% |
| Qualcomm | 7 | 8.9% |
| Alibaba | 7 | 8.9% |
| Kernel.org | 6 | 7.6% |
| Intel | 4 | 5.1% |
| NXP | 3 | 3.8% |
| AMD | 3 | 3.8% |
| 东南大学 | 2 | 2.5% |
| 归属待核实（sanechips.com.cn） | 2 | 2.5% |
| 归属待核实（jannau.net） | 1 | 1.3% |
| SiFive | 1 | 1.3% |
| 归属待核实（foxmail.com） | 1 | 1.3% |
| 归属待核实（utexas.edu） | 1 | 1.3% |

### 按子系统分类

| 子系统 | 数量 | 占比 |
|--------|------|------|
| ARM SMMUv3 | 18 | 22.8% |
| IOMMU Core | 16 | 20.3% |
| RISC-V IOMMU | 12 | 15.2% |
| IOMMUFD | 11 | 13.9% |
| Intel VT-d | 6 | 7.6% |
| AMD IOMMU | 5 | 6.3% |
| IOMMU DMA-API | 4 | 5.1% |
| ARM SMMU (v1/v2) | 3 | 3.8% |
| IOMMU SVA/SVM | 2 | 2.5% |
| IOMMU Page Table | 1 | 1.3% |
| IOMMUPT | 1 | 1.3% |

## 重点 Patch Top20 清单

### 已合入

| 厂商 | 影响力 | 简介 |
|------|------|------|
| Intel | 高（81） | [PATCH v9 00/6] intel_iommu: Enable PRQ support for passthrough device ------为英特尔 IOMMU 直通设备启用页请求队列支持：当虚拟机在虚拟 IOMMU 中开启页请求时，创建故障队列对象并注册事件处理，把宿主机上报的可恢复故障事件转交客户机，同时接收客户机的页请求响应写回宿主机。对失效的进程地址空间标识条目，将故障队列资源释放推迟到下半部执行，避免主循环轮询尚未退出导致释放返回忙错误，使直通设备产生的可恢复页故障能够由客户机处理。 |
| Intel | 高（79） | [v8,6/6] intel_iommu_accel: teardown FAULTQ resources in bottom half ------当进程地址空间标识条目失效时，需要释放对应的故障队列对象和文件描述符。原路径直接释放时存在竞态：主循环仍可能在轮询中持有该文件引用，导致故障队列释放因繁忙而失败。改为把清理工作调度到下半部执行，确保轮询已退出并放弃文件引用后再关闭描述符并释放故障队列对象，从而在少见的并发时序下也能正确回收资源。 |
| Red Hat | 高（76） | [PATCH v2 00/75] virtio: fix exit(1) on DMA mapping failure during migration restore ------这组补丁修正虚拟化 IOMMU 的若干行为：英特尔 IOMMU 支持 PRI 页故障并发处理，并在启用共享虚拟内存时向客户机暴露可扩展模式相干页表遍历能力；页表项标志更新改为一次写入全部传入标志，并仅在页表项同时允许写访问时设置脏位；AMD IOMMU 的桩调用返回空扩展特性寄存器，避免在缺失实现时误报能力。这些调整让客户机页请求处理、脏页跟踪和能力报告更符合硬件语义。 |
| Individual Contributor | 中（59） | [3/4] iommufd: Reject a zero-length dirty bitmap request ------在 IOMMUFD 的脏位图请求检查中，长度为 0 的请求会在减法后回绕成极大值，可能通过溢出和对齐检查，导致后续按几乎无界范围扫描 IOAS。现改为在减法前直接拒绝零长度脏位图请求并返回非法参数，避免用户传入零长度时触发非预期的全区间脏位图操作。 |
| AMD | 中（51） | [PATCH v1 00/8] amd_iommu: Allow IOMMU to attach on non system bus ------为 AMD IOMMU 增加挂载到非系统 PCIe 总线上的能力：此前中断重映射关闭时 IOAPIC 仍被分配 IOMMU 地址空间，导致中断被错误翻译，现仅在支持中断重映射时才分配；同时允许通过设备总线属性把 IOMMU 放到 PCIe 根端口或扩展总线下，向上查找根总线建立 IVRS 表，只服务该总线下的设备。这样可在同一平台中隔离部分 PCI 设备，让 IOMMU 只覆盖指定层次。 |
| NVIDIA | 中（48） | [PATCH] iommupt: Do not allow PTEs to be split when dirty logging ------脏页记录逻辑此前允许拆分单个页表项来适配位图，可能把原本脏的内存区域报告为干净，清扫范围也只覆盖部分页表项。现改为按每个页表项的完整输入输出地址范围更新位图和收集清扫范围，位图对放不下的范围直接报错；同时调整自测页大小以匹配不加拆分的语义，避免脏页漏报。 |

### 社区讨论

| 厂商 | 影响力 | 简介 |
|------|------|------|
| Google | 高（83） | [PATCH v6 00/18] iommu: Add live update state preservation ------为基于 kexec 的内核热更新保存 IOMMU 状态，让由 iommufd 管理的设备在跨内核迁移时保留 DMA 映射。新增域、设备及页表保存/恢复接口，iommufd 用令牌标记需保留的硬件页表并在保留期间冻结地址空间映射；VT-d 实现保存根表、上下文和 PASID 表，恢复后重新附加设备并回收域标识。对支持 ATS 的设备暂不保留，因为跨内核恢复 ATS 状态复杂。 |
| NVIDIA | 高（81） | [PATCH v11 00/11] iommu/arm-smmu-v3: Adopt the crashed kernel's stream table for kdump ------为 arm-smmu-v3 增加 kdump 内核接管崩溃内核流表的能力：保留 SMMU 使能和流表基址，继续使用崩溃内核的页表转换在途 DMA，避免重置导致在途访问被中止或绕过而破坏内存；同时禁用事件和页请求队列，防止损坏的页表产生洪泛事件。启动时校验并采用流表，若不可信则丢弃；扫描保留旧内核使用的地址空间标识和虚拟机标识，避免新域命中残留 TLB 缓存。 |
| NVIDIA | 高（79） | [PATCH v3 00/10] Make the 32-bit ARM DMA API work with normal IOMMU DMA default domains (+ Tegra PoC) ------为多数 32 位 ARM 平台启用 IOMMU 核心拥有的 DMA 默认域，替换原先强制身份域并自行管理映射的方式；部分尚未兼容的平台继续使用身份域。Tegra SMMU 可按软件组启用 DMA 默认域，显示控制器等客户端先在旁路模式工作，待显示驱动接管并复位硬件后再开启地址翻译，避免引导期间显示控制器取指产生翻译故障。这样 Tegra 显示和 Host1x 设备能获得真实 DMA 域，同时支持驱动逐步转换。 |
| Kernel.org | 高（78） | [PATCH v7 00/16] iommufd: vIOMMUs and TSM guest requests for confidential guests ------为机密计算扩展 IOMMUFD 和 vIOMMU：允许 TEE 安全管理器代替物理 IOMMU 驱动提供 vIOMMU 操作，并新增 vdevice 的 TSM 请求接口，使虚拟机监控器能把客户机发出的 TSM 命令转发给管理直通设备的 TSM 实现；同时把 KVM 文件关联到设备和 vIOMMU，允许创建没有父硬件页表的 vIOMMU。适用于 CCA、SEV、TDX 等机密客户机需要向 TSM 发起认证或配置请求的场景。 |
| NVIDIA | 中（73） | [PATCH v5 00/15] iommu/arm-smmu-v3: Add PRI support ------为 ARM SMMUv3 驱动新增 PCI PRI 支持，使支持页请求的 PCI 设备在缺页时能向内核发起请求并由驱动返回响应。在此之前仅停滞事件可走缺页处理，PRI 队列未启用。实现包括分配队列与中断、处理页请求、提交响应命令，并在分离域时排空硬件队列与待处理故障工作，避免域释放后使用已释放内存。另外修复仅有停滞能力而无 SVA 时故障队列未分配可能导致崩溃的问题。 |
| NVIDIA | 中（73） | [PATCH v8 00/9] Organize the SMMUv3 invalidation flow so iommupt can use it ------针对 ARM SMMUv3 共享虚拟地址场景，修复 ARM errata 导致连续页表项范围失效可能覆盖不完整的问题：检测受影响硬件后，SVA 失效改为每次回调发出单个覆盖整个连续项的范围失效，避免用户通过内存映射操作触发欠失效。同时重构失效流程，用结构体传参并预计算命令，将范围失效优化为最多两次，供后续页表框架复用。 |
| Individual Contributor | 中（73） | [PATCH v2 00/11] mm: Memory providers for guest_memfd and iommufd ------引入内存提供者抽象，使没有页描述符的外部驱动内存可以同时后备客户机私有内存文件和 IOMMU 映射。客户机内存文件通过操作表接入该后备，IOMMU 文件描述符子系统在映射提供者文件时不固定页，改为按页查询物理地址；当提供者撤销某段内存时，同步解除并更新所有相关域映射。设备在撤销更新窗口内访问该范围可能发生故障。 |
| 归属待核实（reactivated.net） | 中（72） | [PATCH v7 00/6] Add support for Broadcom BCM2712 IOMMU driver (Raspberry Pi 5) ------为 Raspberry Pi 5 上的 Broadcom BCM2712 新增 IOMMU 驱动，覆盖显示管线与多媒体设备的内存访问转换，使用两级页表并管理各实例共享的二级 TLB 缓存。同时修复 IOMMU 页表测试中硬编码 38 位物理地址导致该仅支持 37 位输出地址的格式测试失败的问题，改为裁掉高位以适应 32 位。设备树补充 IOMMU 及缓存节点并让显示硬件接入。 |
| Google | 中（67） | [PATCH v9 00/25] KVM: arm64: SMMUv3 driver for pKVM (trap and emulate) ------为启用 pKVM 保护的 arm64 系统提供由 hypervisor 所有的 SMMUv3 驱动：通过陷阱和模拟向主机呈现 SMMU，并维护与主机第二阶段页表同步的影子 IOMMU 页表，以阻止主机设备对受保护虚拟机的 DMA 访问；驱动初始化需要预先保留页表池内存。 |
| Kernel.org | 中（66） | [RFC,v6,08/11] iommufd: Add vIOMMU provider support ------为 iommufd 的虚拟 IOMMU 分配引入提供商机制：特定非默认类型的虚拟 IOMMU 可由外部子系统注册实现及其共享私有数据。原来创建时直接调用物理 IOMMU 驱动，现在先查找外部提供商，未找到匹配项才回退到物理 IOMMU 驱动作为后备。注册商每次查找都会同时持有提供商引用和模块引用，避免模块被卸载；取消注册立即从查找表移除，不等待现有虚拟 IOMMU。 |
| NVIDIA | 中（66） | [v2,07/11] iommu: Let 32-bit ARM drivers opt into a DMA API default domain ------允许 32 位 ARM 上的 IOMMU 驱动在具备 ARM DMA 使用 IOMMU 支持时显式选择 DMA API 默认域，而不是无条件强制身份域。原先覆盖逻辑使驱动无法请求真实 DMA 域；现在移除了强制身份域的代码，并在无通用 IOMMU DMA 时仅对显式请求 DMA 域放行。所有现有 32 位 ARM 驱动因未声明默认域类型或返回零，行为保持不变，避免意外变化。 |
| Microsoft | 中（66） | [v6,4/5] iommu/hyperv: Add para-virtualized IOMMU support for Hyper-V guest ------为 Hyper-V 来宾添加半虚拟化 IOMMU 驱动，在客户机内部实现第一阶段地址转换，适用于分配给来宾的 PCI 设备。经过 Hyper-V 超调用完成能力发现、域管理、设备连接和 IOTLB 失效，并在客户机内存中构造与 x86 兼容的页表，嵌套宿主第二阶段页表，使映射操作无需 VM 退出，但取消映射仍需退出以刷新 IOTLB。初始版本不支持客户机休眠/恢复，因为 Hyper-V 设备域对象和附件无法由镜像保留。 |
| Individual Contributor | 中（64） | [PATCH v1 00/6] iommufd: harden DMA-BUF PAL setup and release ------修复 iommufd 在 DMA 缓冲物理地址列表建立和释放时的并发缺口：保留固定失败错误，将成功的映射发布、列表清除和解固定放在预留锁内，并保持页互斥锁存活到分离完成，防止并发失效回调访问半初始化或已释放的指针；自测加入失败注入验证清理路径。 |
| EPAM | 中（64） | [v13,09/14] iommu/ipmmu-vmsa: Implement suspend/resume callbacks ------为 Xen 下 Renesas R-Car Gen3 的 IPMMU 驱动实现挂起/恢复，保存并恢复活动上下文和微 TLB 寄存器，使系统休眠唤醒后 DMA 地址转换配置仍然有效。恢复时先恢复 Root IPMMU 的上下文，再恢复 Cache IPMMU 的微 TLB 选择状态，因为 Cache 微 TLB 通过配置指向 Root 上下文，顺序颠倒可能暴露陈旧或未初始化的状态。目前仅在 H3ULCB 平台上测试。 |
| Individual Contributor | 中（63） | [PATCH v1 00/14] guest_memfd: Export guest_memfd files to iommufd ------为客户机内存文件增加导出接口，使 IOMMU 文件描述符子系统可以映射客户机共享内存且不固定对应页面。当文件内容被截断、页属性转换或变为只读时，通过更新回调通知映射方取消旧映射并按当前状态重建；只读帧映射为无写权限。目前映射按单页粒度进行，设备在更新窗口内访问可能发生故障，暂不支持脏页跟踪、无 IOMMU 模式等场景。 |
| Alibaba | 中（61） | [v6,2/3] iommufd: Add IOMMU_GET_RECOMMENDED_RESERVATIONS ioctl ------新增按设备查询的 iommufd 接口，向用户态报告内核建议预留的 IO 虚拟地址范围；对 PCI 设备即主机桥的 MMIO 窗口，因为落在其中的 DMA 可能被 PCIe 交换机当作点对点流量，绕过 IOMMU 翻译。接口仅提供建议，由用户决定预留或自行避开。 |
| Google | 中（61） | [PATCH v1 00/22] DMA_PMD: PMD_SIZE-backed IO buffer pools ------为设备直接内存访问缓冲建立以物理连续的两兆字节页为后备的池，使 IOMMU 能用大页映射，从而减少 IOTLB 压力并降低映射与解映射开销；池支持动态分配回收、按节点储备和全局上限，并在页返还前刷新 IOMMU 映射，保持严格模式下的安全保证。 |
| Kernel.org | 中（60） | [RFC,v2,03/13] iommufd: Support MMIO provider attachment to vDEVICEs ------为虚拟设备增加 MMIO 提供者连接接口：后端确认与虚拟机关联后，提供者可以挂到现有虚拟设备，并在分离前保持 IOMMUFD 上下文存活；使用每虚拟设备互斥锁串行化连接、分离和内存转换，并提供私有 MMIO 范围查询，避免销毁时仍有私有范围。 |
| Qualcomm | 中（55） | [PATCH v6 00/16] iommu/riscv: Enable MSI remapping, IOMMU_DMA and VFIO ------为 RISC-V IOMMU 增加 MSI 重映射、DMA 映射和用户态设备访问支持：将软件 MSI 映射改为可增长位图和地址列表，为 IMSIC 每个可能 CPU 预留连续 IOVA 窗口并映射地址列表；随后启用 RISC-V 的 DMA 映射、VFIO 和 KVM/VFIO 接口，使设备可分配给虚拟机。固定的软件 MSI 窗口只能避开已知客户机冲突，无法保证完全不相交。 |
| Amazon | 低（40） | [PATCH v1 00/3] iommu: Reduce iommu_probe_device_lock contention ------针对并行设备探测尤其是虚拟功能初始化时全局探测锁竞争，将默认域创建与附加、sysfs 成员链接发布移到组互斥锁下完成，并用组锁维持同组设备只初始化一次的约束；失败时只回滚当前设备，其余成员等待后续探测或新成员加入再收尾。 |

---

## 已合入 Patches

### ◆ 子系统：Intel VT-d（3 patches）

**▸ 组织：Intel**（2 patches）

**[SERIES] intel_iommu: Enable PRQ support for passthrough device** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-10-20
- 状态：已合入
- 作者邮箱：Duan, Zhenzhong <zhenzhong.duan@intel.com>
- 概括：为英特尔 IOMMU 直通设备启用页请求队列支持：当虚拟机在虚拟 IOMMU 中开启页请求时，创建故障队列对象并注册事件处理，把宿主机上报的可恢复故障事件转交客户机，同时接收客户机的页请求响应写回宿主机。对失效的进程地址空间标识条目，将故障队列资源释放推迟到下半部执行，避免主循环轮询尚未退出导致释放返回忙错误，使直通设备产生的可恢复页故障能够由客户机处理。
- 达到阈值的 patches（4 个，显示前 5）：
  - intel_iommu_accel: Add PRQ injection for passthrough device
  - intel_iommu_accel: Guard VTDAccelPASIDCacheEntry definition
  - intel_iommu_accel: Accept PRQ response for passthrough device
  - intel_iommu_accel: Teardown FAULTQ resources in bottom half
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20261020091955.1607161-5-zhenzhong.duan@intel.com/

**[v8,6/6] intel_iommu_accel: teardown FAULTQ resources in bottom half**

- 日期：2026-10-09
- 状态：已合入
- 作者邮箱：Duan, Zhenzhong <zhenzhong.duan@intel.com>
- 概括：当进程地址空间标识条目失效时，需要释放对应的故障队列对象和文件描述符。原路径直接释放时存在竞态：主循环仍可能在轮询中持有该文件引用，导致故障队列释放因繁忙而失败。改为把清理工作调度到下半部执行，确保轮询已退出并放弃文件引用后再关闭描述符并释放故障队列对象，从而在少见的并发时序下也能正确回收资源。
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20261009090737.3930000-7-zhenzhong.duan@intel.com/

**▸ 组织：Red Hat**（1 patches）

**[SERIES] virtio: fix exit(1) on DMA mapping failure during migration restore** （cover letter，5/7 个 patch 达到代码量阈值）

- 日期：2026-09-11
- 状态：已合入
- 作者邮箱：Michael S. Tsirkin <mst@redhat.com>
- 概括：该 QEMU 合集修复 virtio 迁移恢复路径中损坏的 DMA 地址导致目的端进程直接退出的问题，改为清理已映射项并向上返回错误；同时修复迁移配置长度异常可造成长时间忙等、virtio-pci 重复写队列启用位可被客户机触发大量映射命令导致内存耗尽等缺陷；并增加 Intel IOMMU 并发页请求处理、移除 AMD IOMMU 未支持的 PPR 和 HE 特性。
- 达到阈值的 patches（5 个，显示前 5）：
  - intel_iommu: Support concurrent page fault handling with PRI
  - intel_iommu: Always write all the flags passed to vtd_set_flag_in_pte
  - intel_iommu: Only set dirty bit when PTE exposes write permission
  - intel_iommu: Expose SMPWC when SVM is enabled
  - amd_iommu: Return empty efr for stub call
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/f19df1b13d1a0b5601b4b58067b8c2e91ae76ef3.1789117222.git.mst@redhat.com/

---

### ◆ 子系统：IOMMUFD（1 patches）

**▸ 组织：NVIDIA**（1 patches）

**iommupt: Do not allow PTEs to be split when dirty logging**

- 日期：2026-10-15
- 状态：已合入
- 作者邮箱：Jason Gunthorpe <jgg@nvidia.com>
- 概括：脏页记录逻辑此前允许拆分单个页表项来适配位图，可能把原本脏的内存区域报告为干净，清扫范围也只覆盖部分页表项。现改为按每个页表项的完整输入输出地址范围更新位图和收集清扫范围，位图对放不下的范围直接报错；同时调整自测页大小以匹配不加拆分的语义，避免脏页漏报。
- 来源：https://patchwork.kernel.org/project/linux-kselftest/patch/0-v1-5bb926ff73ec+576-iommufd_dirty_jgg@nvidia.com/

---

### ◆ 子系统：AMD IOMMU（1 patches）

**▸ 组织：AMD**（1 patches）

**[SERIES] amd_iommu: Allow IOMMU to attach on non system bus** （cover letter，2/5 个 patch 达到代码量阈值）

- 日期：2026-10-14
- 状态：已合入
- 作者邮箱：Sairaj Kodilkar <sarunkod@amd.com>
- 概括：允许 QEMU 的 AMD IOMMU 挂接到非系统 PCIe 总线（如根端口），从而只管理该根总线下的设备子集，实现部分设备隔离。原来 AMD IOMMU 只能挂在系统总线并服务整棵 PCI 拓扑，KVM 中断重映射也固定使用默认 IOMMU。现在通过总线属性向上找到首个根总线，仅为其下设备建立 IVRS 表；KVM 改为按设备查找实际服务的 IOMMU。
- 达到阈值的 patches（2 个，显示前 5）：
  - amd_iommu: Assign ioapic_as only when interrupt remapping is supported.
  - amd_iommu: Allow IOMMU to attachment on non-system (pcie.0) bus
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20261014053433.24564-2-sarunkod@amd.com/

---

## 社区讨论中 Patches

### ◆ 子系统：ARM SMMUv3（18 patches）

**▸ 组织：Google**（6 patches）

**[SERIES] KVM: arm64: SMMUv3 driver for pKVM (trap and emulate)** （cover letter，19/19 个 patch 达到代码量阈值）

- 日期：2026-10-15
- 状态：社区讨论中
- 作者邮箱：Mostafa Saleh <smostafa@google.com>
- 概括：为启用 pKVM 保护的 arm64 系统提供由 hypervisor 所有的 SMMUv3 驱动：通过陷阱和模拟向主机呈现 SMMU，并维护与主机第二阶段页表同步的影子 IOMMU 页表，以阻止主机设备对受保护虚拟机的 DMA 访问；驱动初始化需要预先保留页表池内存。
- 达到阈值的 patches（19 个，显示前 5）：
  - iommu/arm-smmu-v3: Move Queue and STE functions to header
  - iommu/arm-smmu-v3: Move IDR parsing to common functions
  - iommu/arm-smmu-v3: Move hitless machinery to common code
  - iommu/arm-smmu-v3-kvm: Probe SMMU HW
  - iommu/arm-smmu-v3-kvm: Emulate GBPA
  - ... 及其他 14 个 patch
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20261015200903.2735565-3-smostafa@google.com/

**[SERIES] iommu/arm-smmu-v3: Implement Runtime/System Sleep ops** （cover letter，7/14 个 patch 达到代码量阈值）

- 日期：2026-09-29
- 状态：社区讨论中
- 作者邮箱：Pranjal Shrivastava <praan@google.com>
- 概括：为 ARM SMMU v3 及 Tegra241 命令队列虚拟化驱动增加运行时电源管理和系统睡眠支持，在挂起前用停止标志门控新命令提交并排空命令与虚拟命令队列，恢复时重写 MSI 配置寄存器和缓存消息，并恢复 Tegra241 生产者/消费者索引；同时将中断处理注册与硬件使能分离，便于恢复时重新初始化中断。
- 达到阈值的 patches（7 个，显示前 5）：
  - iommu/arm-smmu-v3: Refactor arm_smmu_setup_irqs
  - iommu/tegra241-cmdqv: Restore PROD and CONS after resume
  - iommu/arm-smmu-v3: Enable pm_runtime and setup devlinks
  - iommu/arm-smmu-v3: Invoke pm_runtime before hw access
  - iommu/arm-smmu-v3: Implement pm_runtime & system sleep ops
  - ... 及其他 2 个 patch
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/20260929034510.2023173-3-praan@google.com/

**[SERIES] iommu/arm-smmu-v3: Implement Live Update support** （cover letter，8/9 个 patch 达到代码量阈值）

- 日期：2026-09-29
- 状态：社区讨论中
- 作者邮箱：Pranjal Shrivastava <praan@google.com>
- 概括：为 ARM SMMUv3 实现基于 kexec 交接的 Live Update 支持，使内核切换时受保护设备的 DMA 不被中断。保存流表、上下文描述符表和事件队列，关闭路径只阻断未保留设备并停用队列，保持 SMMU 使能位；新内核恢复流表和上下文表时不清除使能位，并让恢复的域继承原有地址空间标识，避免设备仍按旧标识翻译而失败。事件队列也跨交接收养，处理切换期间产生的事件。
- 达到阈值的 patches（8 个，显示前 5）：
  - iommu/kho: Extend IOMMU KHO ABI for ARM SMMUv3
  - iommu/arm-smmu-v3: Implement KHO preservation for STEs
  - iommu/arm-smmu-v3: Implement Live Update Stream Table restoration
  - iommu/arm-smmu-v3: Implement Live Update CD Table restoration
  - iommu/arm-smmu-v3: Implement CD Table preservation
  - ... 及其他 3 个 patch
- 来源：https://patchwork.kernel.org/project/kexec/patch/20260929071950.2710070-2-praan@google.com/

**[SERIES] iommu/arm-smmu-v3: Fixes reported by Sashiko** （cover letter，1/5 个 patch 达到代码量阈值）

- 日期：2026-09-24
- 状态：社区讨论中
- 作者邮箱：Mostafa Saleh <smostafa@google.com>
- 概括：针对 ARM SMMUv3 的流表和上下文描述符表更新，在写入上级指针前增加内存屏障，确保下级表内容先被 SMMU 观察到，避免读到随机数据；同时修正 SMMUv3 单元测试中错误解析上下文描述符、缺少分配/合并返回值检查、边界检查不停止导致越界，以及弹性数组计数未初始化引发未定义行为的问题，让测试正确失败而非越界访问。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/arm-smmu-v3: Ensure L2 tables are visible before L1 ptrs
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260924085616.300650-2-smostafa@google.com/

**[v10,08/15] iommu/arm-smmu-v3: Cache and restore MSI config**

- 日期：2026-09-08
- 状态：社区讨论中
- 作者邮箱：Pranjal Shrivastava <praan@google.com>
- 概括：ARM SMMUv3 的事件、错误和 PRI 队列 MSI 配置寄存器在电源关闭后内容丢失，恢复后可能无法发送 MSI；现在首次写入时缓存消息，在恢复阶段清除地址寄存器并重写各队列中断配置，若此前 MSI 失败已回退线中断则不再尝试恢复。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260908171712.356645-9-praan@google.com/

**iommu/arm-smmu-v3-sva: Relax ASID requirements**

- 日期：2026-09-07
- 状态：社区讨论中
- 作者邮箱：Mostafa Saleh <smostafa@google.com>
- 概括：ARM SMMUv3 共享虚拟地址支持原先要求 SMMU 的 ASID 位宽不小于 CPU，因为早期借助 DVM 做 TLB 失效并共享进程 ASID；该机制已移除，现删除 CPU ASID 相关检查，使 ASID 空间较小的 SMMU 也能启用 SVA。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260907154928.4012151-1-smostafa@google.com/

**▸ 组织：NVIDIA**（5 patches）

**[SERIES] iommu/arm-smmu-v3: Adopt the crashed kernel's stream table for kdump** （cover letter，8/11 个 patch 达到代码量阈值）

- 日期：2026-10-05
- 状态：社区讨论中
- 作者邮箱：Nicolin Chen <nicolinc@nvidia.com>
- 概括：针对 ARM SMMUv3 在 kdump 场景下重置硬件会中止在途 DMA 或绕过 SMMU 改写内存的问题，使 kdump 内核在探测时保留 SMMU 使能和流表基址，直接沿用崩溃内核的流表及页表继续翻译在途 DMA；同时禁用事件队列和页请求队列，扫描并预留已用 ASID 和 VMID，避免旧缓存条目串扰。这样在设备驱动重新初始化前，未停止的主设备 DMA 能安全被吸收，而不是触发致命错误或破坏内存。
- 达到阈值的 patches（8 个，显示前 5）：
  - iommu/arm-smmu-v3: Make the ASID space per SMMU instance
  - iommu/arm-smmu-v3: Add ARM_SMMU_OPT_KDUMP_ADOPT for kdump kernel
  - iommu/arm-smmu-v3: Disable the EVTQ and the PRIQ in a kdump kernel
  - iommu/arm-smmu-v3: Retain CR0_SMMUEN during kdump device reset
  - iommu/arm-smmu-v3-kexec: Reserve crashed kernel's ASIDs and VMIDs
  - ... 及其他 3 个 patch
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/e027296ac9db58fb7d69b1b4b5e4a2ed192dd401.1791226953.git.nicolinc@nvidia.com/

**[SERIES] Organize the SMMUv3 invalidation flow so iommupt can use it** （cover letter，7/7 个 patch 达到代码量阈值）

- 日期：2026-10-03
- 状态：社区讨论中
- 作者邮箱：Jason Gunthorpe <jgg@nvidia.com>
- 概括：针对 ARM SMMUv3 共享虚拟地址场景，修复 ARM errata 导致连续页表项范围失效可能覆盖不完整的问题：检测受影响硬件后，SVA 失效改为每次回调发出单个覆盖整个连续项的范围失效，避免用户通过内存映射操作触发欠失效。同时重构失效流程，用结构体传参并预计算命令，将范围失效优化为最多两次，供后续页表框架复用。
- 达到阈值的 patches（7 个，显示前 5）：
  - iommu/arm-smmu-v3: Pass the parameters for the invalidation in a struct
  - iommu/arm-smmu-v3: Move pgsize out of arm_smmu_inv
  - iommu/arm-smmu-v3: Handle ARM erratum for CONT under invalidation with SVA
  - iommu/arm-smmu-v3: Populate the tlbi at the top of the call chain
  - iommu/arm-smmu-v3: Precompute the invalidation commands
  - ... 及其他 2 个 patch
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/2-v8-1eaaed5e0433+3d3d2d-smmu_tlbi_jgg@nvidia.com/

**[SERIES] iommu/arm-smmu-v3: Quarantine device upon ATC invalidation timeout** （cover letter，2/10 个 patch 达到代码量阈值）

- 日期：2026-09-23
- 状态：社区讨论中
- 作者邮箱：Nicolin Chen <nicolinc@nvidia.com>
- 概括：当 SMMUv3 的 ATC 失效命令超时时，设备缓存可能存在陈旧条目，继续使用会导致内存损坏。现在在 PCI 重置探测时不提前挂起 IOMMU，复位失败时保持设备阻塞而不自动恢复；命令队列通过位图记录超时并重新检查错误；超时后设备被隔离并禁用 ATS，直到一次成功复位才重新挂接正常域。同时修复误删未插入流树节点导致所有主设备 DMA 查找失效的问题。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/arm-smmu-v3: Thread arm_smmu_master_domain on a per-master list
  - iommu/arm-smmu-v3: Quarantine ATS after an ATC invalidation timeout
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/5ddbd81323f86d045072ebf410a6f87da4f2796f.1790188511.git.nicolinc@nvidia.com/

**[SERIES] iommu/arm-smmu-v3: Add PRI support** （cover letter，10/12 个 patch 达到代码量阈值）

- 日期：2026-09-15
- 状态：社区讨论中
- 作者邮箱：Nicolin Chen <nicolinc@nvidia.com>
- 概括：为 ARM SMMU v3 增加 PRI 页请求处理，使启用页请求的 PCI 设备可上报缺页并由驱动提交成功或失败响应；同时在设备从域分离时排空硬件事件队列与待处理缺页工作，若排空超时则跳过清理并泄漏旧域，避免 IOMMU 核心提前释放域导致使用已释放内存。还调整缺页队列分配，使只有停顿特性而无共享虚拟地址时也能分配，防止缺页队列添加设备时崩溃。
- 达到阈值的 patches（10 个，显示前 5）：
  - iommu/arm-smmu-v3: Drain in-flight fault events on domain detach
  - iommu/arm-smmu-v3: Flush in-flight fault work on domain detach
  - iommu/arm-smmu-v3: Disable the queue IRQs before disabling the SMMU
  - iommu/arm-smmu-v3: Submit CMDQ_OP_PRI_RESP for IOPF event
  - iommu/arm-smmu-v3: Allocate IOPF queue without FEAT_SVA
  - ... 及其他 5 个 patch
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/f74817bb45a4bfcda966d9b5ca366c649b6dfe46.1789446520.git.nicolinc@nvidia.com/

**[SERIES] iommu/arm-smmu-v3: Support guest-level Realm VSMMU (Part-1)** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-09-10
- 状态：社区讨论中
- 作者邮箱：Nicolin Chen <nicolinc@nvidia.com>
- 概括：为 Arm CCA 机密虚拟机内的 ARM SMMU v3 增加客户级受保护 VSMMU 支持，在探测时通过固件接口获取真实设备信息并校验 ACPI 数据，激活后要求所有队列和页表分配在私有内存；同时引入 TDISP 设备 T=0 状态，将这类设备的客户可见 DMA 流停放在阻塞域，避免其使用未配置翻译的 IOMMU 路径。
- 达到阈值的 patches（4 个，显示前 5）：
  - iommu: Let a driver mark an IOMMU as confidential
  - iommu: Park TDISP T=0 devices in the blocking domain
  - iommu: Introduce TDISP T=0 state for confidential IOMMUs
  - iommu/arm-smmu-v3: Probe a guest-level Realm VSMMU via RSI commands
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/a2b4ecab20635c1b0defa47407af23ff901c778d.1789010941.git.nicolinc@nvidia.com/

**▸ 组织：NXP**（3 patches）

**[SERIES] iommu/arm-smmu-v3: Support shared Stream IDs** （cover letter，6/7 个 patch 达到代码量阈值）

- 日期：2026-10-30
- 状态：社区讨论中
- 作者邮箱：Peng Fan <peng.fan@oss.nxp.com>
- 概括：针对 i.MX95 等 SMMU 流 ID 数量有限、多个 DMA 设备被分配同一流 ID 的场景，让 SMMUv3 支持共享流 ID。将流对象单独分配并允许多个主设备共享；共享同一 ID 的设备划入同一 IOMMU 组，共用同一域上下文表，避免一个设备释放或附着失败时中止其他设备的 DMA。
- 达到阈值的 patches（6 个，显示前 5）：
  - iommu/arm-smmu-v3: Group aliasing devices into the same IOMMU group
  - iommu/arm-smmu-v3: Wire up shared-SID STE ordering and feature gating
  - iommu/arm-smmu-v3: Allocate streams individually
  - iommu/arm-smmu-v3: Delay stream allocation to inside the mutex
  - iommu/arm-smmu-v3: Use a per-domain CD table for non-PASID streams
  - ... 及其他 1 个 patch
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20261030-smmu-shared-sid-ver7-2026-10-26-v7-6-961726ebd6ab@Example.Com/

**[RFC,v4,1/4] iommu/arm-smmu-v3: Skip duplicate SIDs when erasing streams from RB tree**

- 日期：2026-10-01
- 状态：社区讨论中
- 作者邮箱：Peng Fan <peng.fan@oss.nxp.com>
- 概括：ARM SMMUv3 的桥接 PCI 设备可能产生重复流标识。插入时同一主设备的重复流会被直接丢弃，但重复节点的红黑树节点未初始化；移除和插入错误回滚路径却对所有流数组元素执行红黑树删除，删除未初始化节点会破坏红黑树。由于流数组已按标识排序，重复项相邻，现在在这两条路径跳过相邻重复标识，使删除与插入行为一致。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20261001-smmu-shared-sid-ver3-v4-1-06b34fb2e691@nxp.com/

**[RFC,v2,1/4] iommu/arm-smmu-v3: Convert streams from RB tree to XArray**

- 日期：2026-09-21
- 状态：社区讨论中
- 作者邮箱：Peng Fan <peng.fan@oss.nxp.com>
- 概括：为 ARM SMMUv3 IOMMU 的流标识到流描述符查找，将原本的红黑树流映射替换为索引数组结构，所有插入、删除和读取仍由原互斥锁串行化；删除红黑树比较器和节点成员，桥接 PCI 设备重复流标识的跳过处理随之简化。预期行为不变，为后续共享流标识能力做前期重构。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260921-smmu-shared-sid-v2-1-4b656ce68178@nxp.com/

**▸ 组织：归属待核实（foxmail.com）**（1 patches）

**iommu/arm-smmu-v3: Skip unlinked duplicate stream nodes on removal**

- 日期：2026-09-21
- 状态：社区讨论中
- 作者邮箱：zhoumin <teczm@foxmail.com>
- 概括：ARM SMMUv3 的固件流标识列表可能含重复项，例如别名桥后的 PCI 设备。同一主设备的重复流在插入时被接受但不链入红黑树，移除和插入错误回滚却仍删除每个流节点；删除未链入的零初始化节点可能清掉树根，导致其他设备的流标识映射丢失。现在标记跳过的重复节点，并在移除和回滚路径跳过它们，同时保持流数组和计数不变以保留后续检查。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/tencent_4392079B5C29406B923C037A7E66DD338005@qq.com/

**▸ 组织：Kernel.org**（1 patches）

**[v2,2/5] iommu/arm-smmu-v3: Switch to use acpi_bus_get_primary_device()**

- 日期：2026-09-30
- 状态：社区讨论中
- 作者邮箱：Rafael J. Wysocki (Intel) <rafael@kernel.org>
- 概括：ARM SMMUv3 在 ACPI 探测中为 Tegra241 伴生设备关联时，原先使用即将移除的接口获取物理节点后再取得引用，该接口退出并释放锁后设备可能被移除，造成释放后使用。现在改用会自行持有引用的主设备获取接口，消除这一潜在风险。
- 来源：https://patchwork.kernel.org/project/alsa-devel/patch/3636226.QJadu78ljV@rafael.j.wysocki/

**▸ 组织：归属待核实（shutemov.name）**（1 patches）

**[SERIES] iommu/arm-smmu-v3: Make the queue depths tunable, and shrink them in a kdump kernel** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-09-25
- 状态：社区讨论中
- 作者邮箱：Kiryl Shutsemau <kirill@shutemov.name>
- 概括：为 ARM SMMU v3 新增命令队列深度模块参数，可按条目数对数设置上限，默认取硬件最大值且下限一页，供内存紧张或仅驱动少量设备的系统减少连贯内存占用。在 kdump 捕获内核中默认三个队列深度均设为一页，避免每个 SMMU 实例从 crashkernel 保留区分配最多 12MB 全尺寸队列，节省转储所需内存且不影响转储吞吐。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/arm-smmu-v3: Default queue depths to one page in a kdump kernel
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260925141532.1274962-3-kirill@shutemov.name/

**▸ 组织：Debian**（1 patches）

**[SERIES] iommu/arm-smmu-v3: SMMU hitting kdump mid-air** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-09-11
- 状态：社区讨论中
- 作者邮箱：Breno Leitao <leitao@debian.org>
- 概括：在 arm-smmu-v3 的 kdump 启动场景中，捕获内核启动时设备仍在运行，但 SMMU 重置会安装空流表，导致无驱动网卡继续 DMA 产生非法流号事件，固件优先模式可能复位整机而无法生成转储。现在从旧流表基址读取并继承 L1 描述符到新流表，并在捕获内核中延迟域附加，让继承的流表条目在设备被探测前继续生效。这样持续 DMA 可继续翻译到可记录内存，但转储可能包含崩溃后变化的数据。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/arm-smmu-v3: inherit the previous kernel's stream table in kdump
  - iommu/arm-smmu-v3: defer attach in kdump so inherited entries survive probe
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260911-smmu_fix_aws-v1-1-75870bf9655b@debian.org/

---

### ◆ 子系统：IOMMU Core（14 patches）

**▸ 组织：东南大学**（2 patches）

**iommu/exynos: quiesce SysMMU before requesting IRQ**

- 日期：2026-09-21
- 状态：社区讨论中
- 作者邮箱：Runyu Xiao <runyu.xiao@seu.edu.cn>
- 概括：Exynos SysMMU 探测原先先注册中断，再获取时钟和识别硬件版本，期间出现的待处理中断可能在时钟和版本尚未初始化时被处理函数访问，属于理论竞态且未实际观测到。现在先获取时钟并初始化软件状态，在时钟使能期间禁用 SysMMU 并清空配置使其静止，然后再注册中断；中断处理中若发现 SysMMU 未激活则直接忽略，避免访问未就绪状态。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260921120848.96215-1-runyu.xiao@seu.edu.cn/

**iommu/exynos: Initialize lock before requesting IRQ**

- 日期：2026-09-01
- 状态：社区讨论中
- 作者邮箱：Runyu Xiao <runyu.xiao@seu.edu.cn>
- 概括：三星 Exynos SysMMU 驱动原先在注册中断后才初始化自旋锁，而中断处理函数在注册后可能立即执行并访问未初始化的锁；将该锁的初始化移到请求中断之前，使早期到达的中断也能使用已初始化的锁。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260901130527.3289245-1-runyu.xiao@seu.edu.cn/

**▸ 组织：Qualcomm**（2 patches）

**[SERIES] iommu: qcom: Fix the MSM GPU and display with DMA-address based mappings** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-10-30
- 状态：社区讨论中
- 作者邮箱：Dmitry Baryshkov <dmitry.baryshkov@oss.qualcomm.com>
- 概括：修复高通MSM平台上GPU和显示设备在基于DMA地址映射下的启动故障。此前旧版IOMMU的刷新函数只同步而不失效页表缓存，导致db410c上GPU因陈旧条目挂起；同时Adreno和MDP5设备未被设为直通域，被IOMMU-DMA域接管后与图形驱动自建页表冲突，db820c上系统复位。现在刷新时先失效整个上下文，并为Adreno、MDP5及msm8996补充直通域配置，使这些平台GPU能正常启动。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/arm-smmu-qcom: Use identity default domains for MDP5
  - iommu/qcom: Use identity default domains for the MSM GPU and display
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20261031-msm-smmu-identity-v1-1-a2a70580eebd@oss.qualcomm.com/

**[SERIES] iommu/qcom+msm: Use identity domain for display/GPU** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-10-29
- 状态：社区讨论中
- 作者邮箱：Rob Clark <robin.clark@oss.qualcomm.com>
- 概括：为高通旧版IOMMU驱动中的GPU和显示设备配置直通域。图形显示驱动会自行挂载并管理IOMMU域，但此前这些设备仍可能被IOMMU默认域接管，造成冲突；现在按设备兼容标识匹配Adreno和MDP/MDSS设备，将其默认域类型设为直通，使图形驱动可直接使用物理地址并自行管理页表。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/qcom: Use identity domain for GPU and display
  - iommu/msm: Use identity domain for GPU and display
- 来源：https://patchwork.kernel.org/project/linux-arm-msm/patch/20261029212344.346069-2-robin.clark@oss.qualcomm.com/

**▸ 组织：归属待核实（jannau.net）**（1 patches）

**[v3,2/2] iommu: apple-dart: Support specifying the DMA aperture in the DT**

- 日期：2026-09-02
- 状态：社区讨论中
- 作者邮箱：Janne Grunau <j@jannau.net>
- 概括：Apple DART 直连设备往往只需部分地址空间用于 DMA，现允许通过设备树 iommus 参数指定 DMA 窗口的起始和长度，并按页大小对齐和校验不能跨过 IAS 边界；指定窗口可超出输入地址范围，此时假定硬件截断高位地址，只映射低位部分。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260902-iommu-apple-dart-aperture-v3-2-252ce55b7001@jannau.net/

**▸ 组织：Individual Contributor**（1 patches）

**[v1,1/2] iommu: export iommu_get_dma_domain()**

- 日期：2026-09-28
- 状态：社区讨论中
- 作者邮箱：Jianfeng Liu <liujianfeng1994@gmail.com>
- 概括：为模块化图形驱动导出获取设备 DMA 默认域的内核接口。启用调试配置时，导入的 DMA-buf 散列表缺少物理页信息，图形驱动需要通过附加设备的 DMA API 域把 DMA 地址还原为物理地址，以映射进自身页表；导出后模块化驱动可以使用该接口。
- 来源：https://patchwork.kernel.org/project/dri-devel/patch/20260928053901.7270-2-liujianfeng1994@gmail.com/

**▸ 组织：Kernel.org**（1 patches）

**[slab/for-next,09/14] iommu: specify SLAB_MAY_ACCOUNT for slab-backed page table caches**

- 日期：2026-10-21
- 状态：社区讨论中
- 作者邮箱：Harry Yoo <harry@kernel.org>
- 概括：为多个输入输出内存管理单元的页表缓存补充允许按内存控制组计费的标记。此前虚拟化接口进行映射时会把带内存控制组计费的分配标志传给这些页表缓存，但缓存未声明支持计费，导致内存控制组统计无法生效，并且后续严格校验下这类分配会被拒绝。现在这些缓存允许计费，使映射分配能正常计入对应控制组。
- 来源：https://patchwork.kernel.org/project/linux-mm/patch/20261021-memalloc-prof-dont-waste-slabobj-ext-metadata-v1-9-096800aa3330@kernel.org/

**▸ 组织：EPAM**（1 patches）

**[v13,09/14] iommu/ipmmu-vmsa: Implement suspend/resume callbacks**

- 日期：2026-10-27
- 状态：社区讨论中
- 作者邮箱：Mykola Kvach <mykola_kvach@epam.com>
- 概括：为 Xen 下 Renesas R-Car Gen3 的 IPMMU 驱动实现挂起/恢复，保存并恢复活动上下文和微 TLB 寄存器，使系统休眠唤醒后 DMA 地址转换配置仍然有效。恢复时先恢复 Root IPMMU 的上下文，再恢复 Cache IPMMU 的微 TLB 选择状态，因为 Cache 微 TLB 通过配置指向 Root 上下文，顺序颠倒可能暴露陈旧或未初始化的状态。目前仅在 H3ULCB 平台上测试。
- 来源：https://patchwork.kernel.org/project/xen-devel/patch/3f8f4ecf30d38d589c2d08f5b2676bda93f8d880.1793129971.git.mykola_kvach@epam.com/

**▸ 组织：归属待核实（chromium.org）**（1 patches）

**iommu/mediatek: Track first resume with a dedicated boolean flag**

- 日期：2026-10-28
- 状态：社区讨论中
- 作者邮箱：Chen-Yu Tsai <wenst@chromium.org>
- 概括：联发科 IOMMU 驱动原先依靠写长度控制寄存器非零的硬件默认值判断首次运行时恢复，逻辑隐晦且易误读；现改为使用专门布尔标志直接记录首次恢复是否已完成，使状态判断不再依赖寄存器隐式默认值。
- 来源：https://patchwork.kernel.org/project/linux-mediatek/patch/20261028041651.3201911-1-wenst@chromium.org/

**▸ 组织：归属待核实（reactivated.net）**（1 patches）

**[SERIES] Add support for Broadcom BCM2712 IOMMU driver (Raspberry Pi 5)** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-09-27
- 状态：社区讨论中
- 作者邮箱：Daniel Drake <dan@reactivated.net>
- 概括：为 Raspberry Pi 5 上的 Broadcom BCM2712 新增 IOMMU 驱动，覆盖显示管线与多媒体设备的内存访问转换，使用两级页表并管理各实例共享的二级 TLB 缓存。同时修复 IOMMU 页表测试中硬编码 38 位物理地址导致该仅支持 37 位输出地址的格式测试失败的问题，改为裁掉高位以适应 32 位。设备树补充 IOMMU 及缓存节点并让显示硬件接入。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/generic_pt: Add Broadcom BCM2712 page table format
  - iommu: Add Broadcom BCM2712 IOMMU driver
- 来源：https://patchwork.kernel.org/project/devicetree/patch/20260927-bcm2712-iommu-submit-v7-4-dfa2b975cbc9@reactivated.net/

**▸ 组织：Microsoft**（1 patches）

**[SERIES] Hyper-V: Add para-virtualized IOMMU support for Linux guests** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-09-30
- 状态：社区讨论中
- 作者邮箱：Yu Zhang <zhangyu1@linux.microsoft.com>
- 概括：为 Hyper-V Linux 来宾新增半虚拟化 IOMMU 驱动，借助 hypercall 进行能力发现、域与设备管理及 IOTLB 刷新；来宾在自身内存中构建第一级地址翻译页表并交由 Hyper-V 嵌套到宿主第二级页表，从而避免来宾 IOMMU 映射操作触发的虚拟机退出，但解除映射仍需退出以刷新 IOTLB。另增加页选择性 IOTLB 刷新，失败时回退到整个域刷新，初始实现不支持休眠恢复。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/hyperv: Add para-virtualized IOMMU support for Hyper-V guest
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/20260930141409.437904-4-zhangyu1@linux.microsoft.com/

**▸ 组织：Amazon**（1 patches）

**[SERIES] iommu: Reduce iommu_probe_device_lock contention** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-09-11
- 状态：社区讨论中
- 作者邮箱：Sakac, Pavol <sakacpav@amazon.de>
- 概括：针对并行设备探测尤其是虚拟功能初始化时全局探测锁竞争，将默认域创建与附加、sysfs 成员链接发布移到组互斥锁下完成，并用组锁维持同组设备只初始化一次的约束；失败时只回滚当前设备，其余成员等待后续探测或新成员加入再收尾。
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu: split sysfs link publication out of iommu_group_alloc_device()
  - iommu: create device sysfs links outside iommu_probe_device_lock
  - iommu: set up the default domain outside iommu_probe_device_lock
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/20260911125907.67105-1-sakacpav@amazon.de/

**▸ 组织：Alibaba**（1 patches）

**[SERIES] iommu: Reserve PCI host bridge MMIO windows for IOVA** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-09-21
- 状态：社区讨论中
- 作者邮箱：Guanghui Feng <guanghuifeng@linux.alibaba.com>
- 概括：DMA IOVA 分配本会保留 PCI 主机桥 MMIO 窗口，避免地址落入桥窗口被误解为点对点 DMA；但 VFIO type1 和 iommufd 之前只从 IOMMU 驱动获取保留区域，未包含这些窗口，用户态可能选择重叠的 IOVA，在 ACS 未完全开启时 PCIe switch 可能把 DMA 路由到错误设备。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu: Reserve PCI host bridge MMIO windows in group reserved regions
  - iommufd: Reserve PCI host bridge MMIO windows in IOAS reserved regions
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260921103922.1113752-2-guanghuifeng@linux.alibaba.com/

**▸ 组织：Google**（1 patches）

**[SERIES] iommu: Introduce Page Table Observability Framework** （cover letter，2/5 个 patch 达到代码量阈值）

- 日期：2026-10-01
- 状态：社区讨论中
- 作者邮箱：Pranjal Shrivastava <praan@google.com>
- 概括：新增 IO 页表可观测性框架，按 IOMMU 域统计页表占用的物理页数，并通过 vfio 和 iommufd 的 fdinfo 接口向用户空间报告。原先只有全局计数，无法归因到具体容器或上下文；现在页表分配时绑定所属域并增减计数，通用页表库自动接入。vfio 容器和 iommufd 上下文分别聚合其管理的域页表页数，以 iommu-nr-pages 字段展示；若某域未接入统计，字段省略而非报告不完整数据。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommupt: Enable per-domain IOPT attribution
  - iommufd: Expose IO page table usage via fdinfo
- 来源：https://patchwork.kernel.org/project/linux-kselftest/patch/20261001224531.765278-2-praan@google.com/

---

### ◆ 子系统：RISC-V IOMMU（10 patches）

**▸ 组织：归属待核实（sanechips.com.cn）**（2 patches）

**[SERIES] iommu/riscv: Add nested translation (vIOMMU) support** （cover letter，3/9 个 patch 达到代码量阈值）

- 日期：2026-10-29
- 状态：社区讨论中
- 作者邮箱：Gong Shuai <gong.shuai@sanechips.com.cn>
- 概括：为 RISC-V IOMMU 增加嵌套翻译和 vIOMMU 支持，使 VMM 可向 guest 暴露 IOMMU，设备 DMA 经 guest 一级和 host 二级两级页表翻译。修正设备上下文有效位处理并复制完整字段，新增 RISC-V 硬件信息和 hwpt/vIOMMU 用户接口；分配嵌套域时校验 guest 一级配置，attach 时将其与宿主二级上下文合并。
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu/riscv: Add nested domain allocation
  - iommu/riscv: Use DC.tc.V as the device context valid bit
  - iommu/riscv: Add vIOMMU cache invalidation
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20261029061131.584453-6-gong.shuai@sanechips.com.cn/

**[RFC,11/12] iommu/riscv: Accept unpublished interrupt files in IRQ forwarding**

- 日期：2026-10-15
- 状态：社区讨论中
- 作者邮箱：Gong Shuai <gong.shuai@sanechips.com.cn>
- 概括：在 RISC-V 输入输出内存管理单元中断转发中，当客户机通过虚拟输入输出内存管理单元转发消息信号中断时，消息信号中断表可能在所有虚拟处理器的中断文件发布之前就需要安装。原有校验会因存在未发布项而拒绝整个请求，导致整台虚拟机失去中断旁路；现在跳过未发布项，只有解析到这些未发布项的消息中断会在对应虚拟处理器上故障并写入故障队列。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261015065232.604503-12-gong.shuai@sanechips.com.cn/

**▸ 组织：Alibaba**（2 patches）

**[SERIES] iommu/riscv: Add irqbypass support without MSI page table** （cover letter，3/4 个 patch 达到代码量阈值）

- 日期：2026-10-14
- 状态：社区讨论中
- 作者邮箱：yu fangyu <fangyu.yu@linux.alibaba.com>
- 概括：针对不具备 MSI 页表能力的 RISC-V IOMMU，设备 MSI 写需经第二阶段页表翻译，但原来无法在第二阶段为 guest IMSIC 页建立转发路径。现在在第二阶段映射 guest IMSIC 地址到宿主 IMSIC 物理页，并新增通用页表叶子原子替换操作，使 vCPU 迁移导致宿主页变化时无需先解除映射，避免出现设备 MSI 写故障窗口。
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu/riscv: Support IRQ forwarding without MSI page tables
  - iommu/riscv: Extract IRQ forwarding payload validation
  - iommupt: Add replace_leaf to atomically swap a leaf OA
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20261014141124.48569-5-fangyu.yu@linux.alibaba.com/

**[SERIES] iommu/riscv: Fix command queue publishing races** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-09-01
- 状态：社区讨论中
- 作者邮箱：yu fangyu <fangyu.yu@linux.alibaba.com>
- 概括：RISC-V IOMMU 命令队列发布存在并发竞态，可能使软件生产者索引在命令实际写入并发布前就被推进；现增加自旋锁串行化发布，并在队列满时于锁外等待硬件消费，避免长时间阻塞其他 CPU。同时当命令入队失败时不再等待完成信号，防止误报执行超时。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/riscv: Serialize command queue publishing
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20260901133920.14550-2-fangyu.yu@linux.alibaba.com/

**▸ 组织：Qualcomm**（2 patches）

**[SERIES] iommu/riscv: Add irqbypass support** （cover letter，7/10 个 patch 达到代码量阈值）

- 日期：2026-09-28
- 状态：社区讨论中
- 作者邮箱：Andrew Jones <andrew.jones@oss.qualcomm.com>
- 概括：为 RISC-V IOMMU 增加中断旁路支持，使虚拟机的中断可以经由第二阶段域的 MSI 表重映射到客户机中断文件，而不直接投递给宿主。新增按域延迟分配的 MSI 表、按设备保存已编程上下文，以及每 IOMMU 的中断重映射域；引入 RCU 保护并发域访问、请求验证和锁顺序，拒绝具有已转发中断的活跃第二阶段域替换，并确保域替换与设备上下文更新串行化，从而避免中断转发状态指向已脱离的表。
- 达到阈值的 patches（7 个，显示前 5）：
  - iommu/riscv: Allocate MSI tables for second-stage domains
  - iommu/riscv: Prepare domain bonds for outer locking
  - iommu/riscv: Cache the programmed device context
  - iommu/riscv: Validate IRQ forwarding requests
  - iommu/riscv: Add IRQ domain for interrupt remapping
  - ... 及其他 2 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260928143113.49838-2-andrew.jones@oss.qualcomm.com/

**[SERIES] iommu/riscv: Enable MSI remapping, IOMMU_DMA and VFIO** （cover letter，7/7 个 patch 达到代码量阈值）

- 日期：2026-09-25
- 状态：社区讨论中
- 作者邮箱：Andrew Jones <andrew.jones@oss.qualcomm.com>
- 概括：为 RISC-V IOMMU 增加 MSI 重映射、DMA 映射和用户态设备访问支持：将软件 MSI 映射改为可增长位图和地址列表，为 IMSIC 每个可能 CPU 预留连续 IOVA 窗口并映射地址列表；随后启用 RISC-V 的 DMA 映射、VFIO 和 KVM/VFIO 接口，使设备可分配给虚拟机。固定的软件 MSI 窗口只能避开已知客户机冲突，无法保证完全不相交。
- 达到阈值的 patches（7 个，显示前 5）：
  - iommufd: Split software MSI map lookup and allocation
  - iommufd: Prepare software MSI maps for address lists
  - iommufd: Install software MSI map ranges atomically
  - iommufd: Bound software MSI mappings to the reserved range
  - iommu/riscv: Reserve an MSI IOVA window for iommufd
  - ... 及其他 2 个 patch
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20260925151659.419512-4-andrew.jones@oss.qualcomm.com/

**▸ 组织：SiFive**（1 patches）

**[v16,2/2] iommu/riscv: create a auxiliary device for HPM**

- 日期：2026-10-06
- 状态：社区讨论中
- 作者邮箱：Zong Li <zong.li@sifive.com>
- 概括：RISC-V IOMMU 在检测到硬件性能监视器能力时创建一个辅助设备，供性能监视单元驱动绑定使用；辅助设备创建失败仅记录警告，IOMMU 仍可正常工作。卸载 IOMMU 时先销毁该辅助设备。
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20261006090327.309550-3-zong.li@sifive.com/

**▸ 组织：The Good Penguin**（1 patches）

**iommu/riscv: Use named initializers for acpi_device_id**

- 日期：2026-10-14
- 状态：社区讨论中
- 作者邮箱：Pawel Zalewski <pzalewski@thegoodpenguin.co.uk>
- 概括：将 RISC-V 输入输出内存管理单元的高级配置与电源接口设备识别表改为按字段名初始化，去掉冗余的显式零值，并统一列表结尾格式，使该表与内核其他同类初始化列表风格一致，阅读和后续维护更直观。
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20261014-acpi-iommu-v1-1-1744523fa658@thegoodpenguin.co.uk/

**▸ 组织：Linux Community**（1 patches）

**[SERIES] iommu/riscv: Enable MSI remapping and IOMMU_DMA** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-10-22
- 状态：社区讨论中
- 作者邮箱：Andrew Jones <andrew.jones@linux.dev>
- 概括：为 64 位 RISC-V 平台引入输入输出内存管理单元的消息中断重映射能力。新增接口在直接内存访问域中把全部可能的中断目标物理地址映射为一段连续设备虚拟地址，并在 RISC-V 消息中断控制器驱动中建立按逻辑处理器索引的目标地址列表；当中断亲和性变化时，直接以处理器索引在该连续区间内组成消息，避免在原子上下文进行映射。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/dma: Prepare MSI physical address lists
  - iommu/dma: Enable IOMMU_DMA for 64-bit RISC-V
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20261022154603.1374754-2-andrew.jones@linux.dev/

**▸ 组织：Individual Contributor**（1 patches）

**[SERIES] iommu/riscv: Keep page table pages when IOTLB invalidation fails** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-10-20
- 状态：社区讨论中
- 作者邮箱：Yuho Choi <oss.patchbox@gmail.com>
- 概括：修复 RISC-V IOMMU 在 IOTLB 失效未确认或命令队列停摆时仍释放页表页的问题：原实现不检查失效命令是否入队或完成，可能把 IOMMU 仍缓存的页表页归还分配器，后续被改写后可能被当作页表项遍历。现在命令发送、同步和失效路径返回错误，无法确认失效完成时保留待释放页表并打印一次性警告；同时命令队列因错误停止时不再误报为已完成，而是返回错误，避免继续释放页表。注意这只覆盖页表回收列表路径，不覆盖刷新队列等页释放。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/riscv: Do not report a stalled command queue as completed
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20261020053435.1179054-5-oss.patchbox@gmail.com/

---

### ◆ 子系统：IOMMUFD（10 patches）

**▸ 组织：Individual Contributor**（5 patches）

**[SERIES] guest_memfd: Export guest_memfd files to iommufd** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-10-27
- 状态：社区讨论中
- 作者邮箱：Fred Griffoul <griffoul@gmail.com>
- 概括：为客户机内存文件增加导出接口，使 IOMMU 文件描述符子系统可以映射客户机共享内存且不固定对应页面。当文件内容被截断、页属性转换或变为只读时，通过更新回调通知映射方取消旧映射并按当前状态重建；只读帧映射为无写权限。目前映射按单页粒度进行，设备在更新窗口内访问可能发生故障，暂不支持脏页跟踪、无 IOMMU 模式等场景。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommufd: Map guest_memfd files
  - iommufd: Track the domains of revocable pages in struct iopt_pages
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261027154649.91571-10-griffoul@gmail.com/

**[SERIES] iommufd: harden DMA-BUF PAL setup and release** （cover letter，4/6 个 patch 达到代码量阈值）

- 日期：2026-10-20
- 状态：社区讨论中
- 作者邮箱：Karl Mehltretter <kmehltretter@gmail.com>
- 概括：加固 iommufd 中 DMA-buf 物理地址列表的建立和释放：修复 pin 失败时错误被替换为成功、映射结果在解锁前过早发布、释放后仍留下悬挂指针、互斥锁先于分离销毁、unpin 未持有预留锁等问题。现在仅在 pin 和物理列表映射都成功后发布，释放时在预留锁内清除指针并执行 unpin，分离后再销毁锁，使并发失效回调不会再访问已释放对象。自测试加入 pin 和映射失败注入，验证失败路径不会映射缓冲区或重复释放。
- 达到阈值的 patches（4 个，显示前 5）：
  - iommufd: Publish successful PAL mappings under resv
  - iommufd: Keep the pages mutex alive until DMA-buf detach
  - iommufd: Unpin the DMA-buf while holding resv
  - iommufd/selftest: Check DMA-buf pin and map failure cleanup
- 来源：https://patchwork.kernel.org/project/linux-kselftest/patch/9a3912ce01cfd1205daeb13b57de47aa8f27f076.1792477872.git.kmehltretter@gmail.com/

**[SERIES] mm: Memory providers for guest_memfd and iommufd** （cover letter，5/5 个 patch 达到代码量阈值）

- 日期：2026-10-14
- 状态：社区讨论中
- 作者邮箱：Fred Griffoul <griffoul@gmail.com>
- 概括：引入内存提供者抽象，使没有页描述符的外部驱动内存可以同时后备客户机私有内存文件和 IOMMU 映射。客户机内存文件通过操作表接入该后备，IOMMU 文件描述符子系统在映射提供者文件时不固定页，改为按页查询物理地址；当提供者撤销某段内存时，同步解除并更新所有相关域映射。设备在撤销更新窗口内访问该范围可能发生故障。
- 达到阈值的 patches（5 个，显示前 5）：
  - iommufd: Track the domains of pages that are not pinned
  - iommufd: Map memory provider files
  - iommufd/selftest: Add mock-domain IOVA queries
  - iommufd/selftest: Add a mock memory provider
  - iommufd: Use large IOMMU pages for provider mappings
- 来源：https://patchwork.kernel.org/project/linux-kselftest/patch/20261014093733.90312-6-griffoul@gmail.com/

**[v2,2/2] iommufd/selftest: Check dmabuf MMIO mappings filled from another domain**

- 日期：2026-10-08
- 状态：社区讨论中
- 作者邮箱：Andrea Parri <parri.andrea@gmail.com>
- 概括：新增自测试，验证 DMA 缓冲区映射在从已映射区域派生的第二个域以及复制到另一地址空间的域中均保持内存映射输入输出属性。由于模拟页表没有内存类型位，测试通过包装映射与解除映射操作来记录带该属性的页面，并新增检查命令确认给定范围全部被标记。覆盖新增域和跨地址空间复制两种场景，没有此前修复时第二个域的检查会失败。
- 来源：https://patchwork.kernel.org/project/linux-kselftest/patch/20261008125206.11990-3-parri.andrea@gmail.com/

**[SERIES] iommufd: Keep IOMMU_HWPT_GET_DIRTY_BITMAP within the user bitmap** （cover letter，2/4 个 patch 达到代码量阈值）

- 日期：2026-09-25
- 状态：社区讨论中
- 作者邮箱：Andrea Parri <parri.andrea@gmail.com>
- 概括：修复 iommufd 获取脏页位图接口的越界写和零长度请求问题。当查询范围只覆盖大页的一部分时，脏页跟踪可能记录整个大页，旧逻辑会把位图写到用户缓冲区之后；现在先按实际位图边界裁剪记录范围，避免污染相邻内存。同时，长度为 0 的请求此前会因下溢被当作合法范围，可能扫描整个地址空间，现在直接拒绝。相应自测验证了边界外的保护字不被改写以及零长度请求返回无效参数。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommufd/iova_bitmap: Clip recorded ranges to the bitmap
  - iommufd: Reject a zero-length dirty bitmap request
- 来源：https://patchwork.kernel.org/project/linux-kselftest/patch/20260925161142.189813-2-parri.andrea@gmail.com/

**▸ 组织：Kernel.org**（3 patches）

**[RFC,v2,03/13] iommufd: Support MMIO provider attachment to vDEVICEs**

- 日期：2026-10-17
- 状态：社区讨论中
- 作者邮箱：Aneesh Kumar K.V <aneesh.kumar@kernel.org>
- 概括：为虚拟设备增加 MMIO 提供者连接接口：后端确认与虚拟机关联后，提供者可以挂到现有虚拟设备，并在分离前保持 IOMMUFD 上下文存活；使用每虚拟设备互斥锁串行化连接、分离和内存转换，并提供私有 MMIO 范围查询，避免销毁时仍有私有范围。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261017073149.1303738-4-aneesh.kumar@kernel.org/

**[SERIES] iommufd: vIOMMUs and TSM guest requests for confidential guests** （cover letter，6/6 个 patch 达到代码量阈值）

- 日期：2026-10-08
- 状态：社区讨论中
- 作者邮箱：Aneesh Kumar K.V <aneesh.kumar@kernel.org>
- 概括：为机密计算扩展 IOMMUFD 和 vIOMMU：允许 TEE 安全管理器代替物理 IOMMU 驱动提供 vIOMMU 操作，并新增 vdevice 的 TSM 请求接口，使虚拟机监控器能把客户机发出的 TSM 命令转发给管理直通设备的 TSM 实现；同时把 KVM 文件关联到设备和 vIOMMU，允许创建没有父硬件页表的 vIOMMU。适用于 CCA、SEV、TDX 等机密客户机需要向 TSM 发起认证或配置请求的场景。
- 达到阈值的 patches（6 个，显示前 5）：
  - iommufd/device: Associate KVM file pointer with iommufd_device
  - iommufd/viommu: Keep a reference to the KVM file
  - iommufd: Add the vdevice TSM request ioctl
  - iommufd/viommu: Select vIOMMU operations before allocation
  - iommufd/viommu: Allow PCI TSM backends to provide vIOMMU operations
  - ... 及其他 1 个 patch
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/20261008055955.4014342-8-aneesh.kumar@kernel.org/

**[SERIES] iommufd: Infrastructure for vIOMMU creation for confidential guests and guest TSM requests** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-09-17
- 状态：社区讨论中
- 作者邮箱：Aneesh Kumar K.V <aneesh.kumar@kernel.org>
- 概括：为机密虚拟机的 vIOMMU 创建和客户机 TSM 请求提供支撑机制：VFIO 改为保存 KVM VM 文件引用，使生命周期不依赖内核内部指针；iommufd 增加 vIOMMU provider 机制，允许外部实现注册并管理私有数据，物理 IOMMU 驱动作为回退；新增 vdevice TSM 请求接口，让 VMM 转发客户机命令给对应 TSM 实现，并移除旧的 PCI 设备级请求入口。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommufd: Add vIOMMU provider support
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260917140159.1163281-6-aneesh.kumar@kernel.org/

**▸ 组织：Alibaba**（2 patches）

**[SERIES] iommufd: Recommended reservations query and opt-in IOAS reservation** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-10-28
- 状态：社区讨论中
- 作者邮箱：Guanghui Feng <guanghuifeng@linux.alibaba.com>
- 概括：新增两个 iommufd 接口：按设备查询内核推荐的保留 IOVA 范围，以及用户态在 IOAS 中主动保留这些范围。推荐范围来自设备所在 PCI 主机桥的 MMIO 窗口，若把 IOVA 落在这些窗口，DMA 可能被 PCIe 交换机当作对等流量绕开 IOMMU。用户态可查询后自行回避，或通过保留接口让内核从可用范围中排除并拒绝映射。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommufd: Add IOMMU_GET_RECOMMENDED_RESERVATIONS ioctl
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261028090453.2392991-2-guanghuifeng@linux.alibaba.com/

**[v4,2/2] iommufd: Add IOMMU_GET_PCI_MMIO_WINDOWS ioctl**

- 日期：2026-10-25
- 状态：社区讨论中
- 作者邮箱：Guanghui Feng <guanghuifeng@linux.alibaba.com>
- 概括：为 IOMMU 用户态接口新增按设备查询能力，返回指定 PCI 设备所在主机桥的内存映射窗口。用户态（如虚拟机管理器）可据此识别 PCIe 交换机可能误当作设备间点对点传输的地址范围，并自行决定是否将 IOVA 分配避开这些窗口；内核仅报告范围，不预留或强制隔离。该信息在设备绑定后、附加地址空间前即可查询。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261025133000.205508-3-guanghuifeng@linux.alibaba.com/

---

### ◆ 子系统：AMD IOMMU（4 patches）

**▸ 组织：AMD**（2 patches）

**[SERIES] Add support for AMD IOMMU GAPPI** （cover letter，4/5 个 patch 达到代码量阈值）

- 日期：2026-10-22
- 状态：社区讨论中
- 作者邮箱：Sairaj Kodilkar <sarunkod@amd.com>
- 概括：为 AMD AVIC 设备中断直通引入 GAPPI 通知机制：当目标 vCPU 不在运行状态时，IOMMU 除照常更新 guest vAPIC 页外，还按中断重映射表项中的目的地和向量向宿主 CPU 发送物理 APIC 中断来唤醒 vCPU，替代原有 GA log 路径。
- 达到阈值的 patches（4 个，显示前 5）：
  - iommu/amd: KVM: SVM: Rename cpu to apicid in IOMMU interface
  - iommu/amd: KVM: SVM: Rename ga_log_intr to wakeup_intr in IOMMU interface
  - iommu/amd: Program guest-mode IRTEs for GAPPI wakeup when IRTE[IsRun] = 0
  - iommu/amd: Provide kernel command line option to enable GAPPI
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261022140425.27465-2-sarunkod@amd.com/

**[SERIES] iommu/amd: Implement live update state preservation** （cover letter，5/6 个 patch 达到代码量阈值）

- 日期：2026-10-05
- 状态：社区讨论中
- 作者邮箱：Ankit Soni <Ankit.Soni@amd.com>
- 概括：为 AMD IOMMU 实现 live update 状态保存与恢复，使内核 kexec 切换时受保护设备继续按其原有页表翻译。保存 PCI 段的设备表和每个设备的域标识、页表模式及 GCR3 表；关闭时阻断未保留设备并停止命令、事件等引擎以避免写入新内核可复用内存，超时则触发内核恐慌。新内核采用保留的设备表、保留域标识并保持使能位，重新附接设备时验证与硬件一致，拒绝任何会改写活跃设备表项的其他附接。
- 达到阈值的 patches（5 个，显示前 5）：
  - iommu/amd: defer device attach only on a kdump boot
  - iommu/amd: preserve IOMMU and device state for live update
  - iommu/amd: restore preserved state on a live-update boot
  - iommu/amd: clear unpreserved DTEs and quiesce logs at live-update shutdown
  - iommu/amd: reattach preserved devices to their restored domains
- 来源：https://patchwork.kernel.org/project/kexec/patch/20261005064018.1558-2-Ankit.Soni@amd.com/

**▸ 组织：Google**（1 patches）

**[SERIES] iommu/amd: Refactors for ATS robustness** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-09-10
- 状态：社区讨论中
- 作者邮箱：Pranjal Shrivastava <praan@google.com>
- 概括：重构 AMD IOMMU 设备探测与能力初始化，移除失败时清除设备表项的逻辑，避免 kdump 启动时打断在途 DMA，也避免不刷缓存写设备表带来别名或撕裂写风险。原 ATS 配置失败后仍继续运行，现在直接使设备探测失败；同时 PCI ATS 层要求调用方先检查设备是否支持，再执行准备配置。整体使 AMD IOMMU 在 ATS 配置出错时不再静默继续，错误处理路径更清晰。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/amd: Refactor device probe and capability initialization
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/20260910142655.3281464-2-praan@google.com/

**▸ 组织：Oracle**（1 patches）

**[SERIES] amd_iommu: Bugfix and Cleanup for IO Page Fault** （cover letter，5/5 个 patch 达到代码量阈值）

- 日期：2026-10-30
- 状态：社区讨论中
- 作者邮箱：Alejandro Jimenez <alejandro.j.jimenez@oracle.com>
- 概括：修复QEMU中AMD IOMMU仿真的页错误报告与状态寄存器处理。此前重复添加消息信号中断能力，页错误记录缺失总线号导致错误报告设备，客户机清除事件中断时可能锁存仿真未产生的客户机地址翻译日志溢出位；现在使用完整设备号、移除重复能力、限制可写位并使扩展特性寄存器只读，避免客户机观察到虚假的GA日志溢出和重复重启。
- 达到阈值的 patches（5 个，显示前 5）：
  - amd_iommu: Make extended feature register read-only
  - amd_iommu: Do not create duplicate MSI capability
  - amd_iommu: Do not latch unsupported GA log status bits
  - amd_iommu: Use full BDF when reporting page faults
  - amd_iommu: Define MMIO register masks
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20261030003817.3521476-5-alejandro.j.jimenez@oracle.com/

---

### ◆ 子系统：ARM SMMU (v1/v2)（3 patches）

**▸ 组织：Qualcomm**（1 patches）

**iommu: arm-smmu-qcom: Skip fault-info reads when suspended**

- 日期：2026-09-11
- 状态：社区讨论中
- 作者邮箱：Bibek Kumar Patro <bibek.patro@oss.qualcomm.com>
- 概括：高通 Adreno SMMU 读取故障信息时未持有运行时电源引用，GPU 可能在回调前释放电源导致 SMMU 挂起，之后的寄存器访问可能引发 NoC 错误和异步 SError；改为读取前检查并保持设备活跃，若已开始挂起则跳过寄存器读取，避免触发冷恢复破坏故障现场。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260912-priv_call_runtime_handlers-v1-1-fc0c3a17523f@oss.qualcomm.com/

**▸ 组织：归属待核实（brar.si）**（1 patches）

**[v2,2/2] iommu/arm-smmu-qcom: Skip PRR setup on SM7250 GPU SMMU**

- 日期：2026-10-23
- 状态：社区讨论中
- 作者邮箱：Ishu Brar <patches@brar.si>
- 概括：SM7250 平台的图形处理器系统内存管理单元在写入进程级地址转换相关寄存器时会触发固件重置，导致首次为图形进程创建页表就失败。本改动针对该型号跳过这些寄存器的设置回调，避免触发固件重置，并在 OnePlus Nord 设备上通过 Vulkan 测试。
- 来源：https://patchwork.kernel.org/project/linux-arm-msm/patch/20261023-smmu-sm7250-v2-2-8bb881ce19f5@brar.si/

**▸ 组织：Individual Contributor**（1 patches）

**[SERIES] Enable LPAC on a7xx series GPUs** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-10-29
- 状态：社区讨论中
- 作者邮箱：Anna Maniscalco <anna.maniscalco2000@gmail.com>
- 概括：为高通a7xx系列GPU引入低优先级异步计算支持。此前低优先级计算与主图形共用IOMMU域，无法独立更新页表；现在为其配置独立的SID、上下文银行和分离地址空间，新增独立提交队列与初始化流程，并通过模块参数在Adreno 750上按需启用，使低优先级计算任务能独立调度运行。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu: arm-smmu-qcom: Configure lpac device with split address space
- 来源：https://patchwork.kernel.org/project/linux-arm-msm/patch/20261029-descriptive-name-lpac-upstream-v2-1-a21a5c850961@gmail.com/

---

### ◆ 子系统：IOMMU DMA-API（3 patches）

**▸ 组织：NVIDIA**（2 patches）

**[SERIES] Make the 32-bit ARM DMA API work with normal IOMMU DMA default domains (+ Tegra PoC)** （cover letter，3/5 个 patch 达到代码量阈值）

- 日期：2026-10-26
- 状态：社区讨论中
- 作者邮箱：Mikko Perttunen <mperttunen@nvidia.com>
- 概括：让 32 位 ARM 的 DMA API 支持由 IOMMU 核心拥有的 DMA 默认域，替代传统自定义未管理域。在 Tegra SMMU 上，显示控制器扫描启动画面时保持旁路，等驱动接管并完成复位后再开启翻译，避免启动早期翻译故障；按软件组为 TegraDRM 和 Host1x 设备启用 DMA 默认域，修复多设备同组时探测顺序导致的失败。部分尚未适配的平台继续使用身份域，使整体路径与 arm64 的 DMA 域管理方式接近。
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu/tegra-smmu: Defer display client translation to driver handover
  - iommu/tegra-smmu: Use a DMA API default domain per swgroup
  - iommu: Enable DMA default domains on (most) 32-bit ARM platforms
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20261026-b4-arm32-iommu-dma-cookie-v3-1-3901d74b1ff2@nvidia.com/

**[v2,07/11] iommu: Let 32-bit ARM drivers opt into a DMA API default domain**

- 日期：2026-10-16
- 状态：社区讨论中
- 作者邮箱：Mikko Perttunen <mperttunen@nvidia.com>
- 概括：允许 32 位 ARM 上的 IOMMU 驱动在具备 ARM DMA 使用 IOMMU 支持时显式选择 DMA API 默认域，而不是无条件强制身份域。原先覆盖逻辑使驱动无法请求真实 DMA 域；现在移除了强制身份域的代码，并在无通用 IOMMU DMA 时仅对显式请求 DMA 域放行。所有现有 32 位 ARM 驱动因未声明默认域类型或返回零，行为保持不变，避免意外变化。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20261016-b4-arm32-iommu-dma-cookie-v2-7-b06842a01938@nvidia.com/

**▸ 组织：Google**（1 patches）

**[SERIES] DMA_PMD: PMD_SIZE-backed IO buffer pools** （cover letter，12/12 个 patch 达到代码量阈值）

- 日期：2026-10-03
- 状态：社区讨论中
- 作者邮箱：Luigi Rizzo <lrizzo@google.com>
- 概括：为设备直接内存访问缓冲建立以物理连续的两兆字节页为后备的池，使 IOMMU 能用大页映射，从而减少 IOTLB 压力并降低映射与解映射开销；池支持动态分配回收、按节点储备和全局上限，并在页返还前刷新 IOMMU 映射，保持严格模式下的安全保证。
- 达到阈值的 patches（12 个，显示前 5）：
  - iommu/dma: introduce CONFIG_DMA_PMD and metadata table
  - iommu/dma: add DMA_PMD pool lifecycle and page recycle hook
  - iommu/dma: Global cap and shrinker for DMA_PMD pool memory
  - iommu/dma: add DMA_PMD pool block allocation
  - iommu/dma: reserve a per-domain IOVA window for DMA_PMD pages
  - ... 及其他 7 个 patch
- 来源：https://patchwork.kernel.org/project/linux-mm/patch/20261003212241.3432303-2-lrizzo@google.com/

---

### ◆ 子系统：Intel VT-d（3 patches）

**▸ 组织：Intel**（2 patches）

**[v2,3/4] iommu/vt-d: Add an API for tdx-host when enabling trusted DMA**

- 日期：2026-10-15
- 状态：社区讨论中
- 作者邮箱：Baolu Lu <baolu.lu@linux.intel.com>
- 概括：为支持受信任直接内存访问扩展的 Intel 输入输出内存管理单元新增初始化与释放接口，供 TDX 主机驱动在把硬件切换到安全 TDX 模式前后调用。初始化遍历活动单元，校验地址转换、排队失效和可扩展模式等前提，并把域标识符空间的高半段留给 TDX 模块、主机只使用低半段，随后回调完成切换；失败会恢复域标识符范围并返回错误。处于该模式的单元不接受热移除。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261015010705.1973284-4-baolu.lu@linux.intel.com/

**[SERIES] iommu/vt-d: Introduce trusted DMA initialization support** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-09-15
- 状态：社区讨论中
- 作者邮箱：Baolu Lu <baolu.lu@linux.intel.com>
- 概括：为 Intel TDX Connect 引入可信 DMA 初始化：通过 SEAMCALL 把支持 TDXCS 且启用 DMA 翻译的 VT-d IOMMU 切换到安全 TDX 模式，并为每个 IOMMU 分配元数据页和失效队列缓冲；成功后把域 ID 空间高半部分保留给 TDX 模块，主机只使用低半部分，避免可信与非可信翻译相互干扰。不支持的 IOMMU 会被跳过，初始化失败会回滚已切换单元。
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu/vt-d: Add interfaces for trusted DMA initialization
  - iommu/vt-d: Add helpers to set up and tear down TDX extensions
  - iommu/vt-d: Reserve MSB of domain ID space for TDX module
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260915074235.1219183-4-baolu.lu@linux.intel.com/

**▸ 组织：Google**（1 patches）

**[SERIES] iommu: Add live update state preservation** （cover letter，17/17 个 patch 达到代码量阈值）

- 日期：2026-10-25
- 状态：社区讨论中
- 作者邮箱：Samiullah Khawaja <skhawaja@google.com>
- 概括：为基于 kexec 的内核热更新保存 IOMMU 状态，让由 iommufd 管理的设备在跨内核迁移时保留 DMA 映射。新增域、设备及页表保存/恢复接口，iommufd 用令牌标记需保留的硬件页表并在保留期间冻结地址空间映射；VT-d 实现保存根表、上下文和 PASID 表，恢复后重新附加设备并回收域标识。对支持 ATS 的设备暂不保留，因为跨内核恢复 ATS 状态复杂。
- 达到阈值的 patches（17 个，显示前 5）：
  - iommu: Implement IOMMU Live update FLB callbacks
  - iommu/pages: Add APIs to preserve/unpreserve/restore iommu pages
  - iommupt: Implement preserve/unpreserve/restore callbacks
  - iommu/vt-d: Clear unpreserved context entries during shutdown
  - iommu: Add APIs to get iommu and device preserved state
  - ... 及其他 12 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261025021930.674647-2-skhawaja@google.com/

---

### ◆ 子系统：IOMMU SVA/SVM（2 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[RFC,1/2] iommu: Add iommu_map_sgtable_dma()**

- 日期：2026-10-09
- 状态：社区讨论中
- 作者邮箱：Karl Mehltretter <kmehltretter@gmail.com>
- 概括：新增设备 DMA 地址映射辅助函数，允许将设备已有的 DMA 地址表直接映射到另一个 IOMMU 域。它通过设备默认 DMA 域反查每个地址背后的物理内存，再建立目标域映射，错误时回滚已映射部分。解决了某些私有域导入器无法使用需要物理页的现有接口的问题；仅支持非反弹、非总线地址且对齐的设备 DMA 映射，零地址反向查询因无法区分空洞而不支持。
- 来源：https://patchwork.kernel.org/project/linux-rockchip/patch/20261009002114.67851-2-kmehltretter@gmail.com/

**▸ 组织：归属待核实（utexas.edu）**（1 patches）

**iommu/sva: Charge IOPF allocations to the faulting mm's memcg**

- 日期：2026-10-12
- 状态：社区讨论中
- 作者邮箱：Peizhe Liu <peizheliu@utexas.edu>
- 概括：在输入输出内存管理单元的共享虚拟地址页故障处理路径中，工作队列未设置活动内存控制组，设备访问触发的文件页缓存会被计入根控制组，而不是故障任务所属控制组，导致任务的内存上限被绕过。补丁在处理故障期间临时切换到故障进程的内存控制组，完成后再恢复原值，使这些页缓存计入对应任务的配额。
- 来源：https://patchwork.kernel.org/project/linux-mm/patch/20261012200823.699316-1-peizheliu@utexas.edu/

---

### ◆ 子系统：IOMMU Page Table（1 patches）

**▸ 组织：Qualcomm**（1 patches）

**[v5] iommu/io-pgtable-arm: Add support for contiguous hint bit**

- 日期：2026-09-21
- 状态：社区讨论中
- 作者邮箱：Vijayanand Jitta <vijayanand.jitta@oss.qualcomm.com>
- 概括：为 ARM LPAE 页表增加连续提示位：当一组连续页表项映射自然对齐的连续物理块时，在这组描述符上设置该位，使硬件能合并翻译并扩大 TLB 覆盖范围；在页大小位图中通告支持的连续组大小，调用方按正常页大小选择后直接安装带标记描述符。带标记组的局部取消映射会在改动前拒绝，避免留下半拆组；同时提供硬件缺陷时禁用该功能的开关。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260921-iommu_contig_hint-v5-1-e7fbd1c3774d@oss.qualcomm.com/

---

### ◆ 子系统：IOMMUPT（1 patches）

**▸ 组织：Google**（1 patches）

**[SERIES] iommupt: Introduce IO page table shrinker** （cover letter，2/5 个 patch 达到代码量阈值）

- 日期：2026-10-01
- 状态：社区讨论中
- 作者邮箱：Pranjal Shrivastava <praan@google.com>
- 概括：为通用 IO 页表实现内存收缩器，在系统内存压力下回收因稀疏映射或取消映射后遗留的空中间页表目录。叶子条目通过引用计数判断目录是否完全变空并记录到域回收列表；映射路径用原子增加引用防止与收缩并发冲突，收缩器无锁地切断空分支，等待宽限期确保无并发访问后释放，并刷新 IOMMU 的转换缓存以避免后续访问已释放表。仅非 DMA 域参与回收，避免中断上下文使用列表锁。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommupt: Introduce lockless page table shrinker
  - iommupt: Return real page count to the shrinker core
- 来源：https://patchwork.kernel.org/project/linux-mm/patch/20261001230219.818128-2-praan@google.com/

---

---
## 子系统说明

- **Intel VT-d**：Intel 虚拟化技术定向 I/O（DMA remapping、IRQ remapping）
- **AMD IOMMU**：AMD I/O 虚拟化技术（AMD-Vi）
- **ARM SMMUv3**：ARM 系统 MMU 第三代（PCIe ATS/PRI 支持）
- **ARM SMMU (v1/v2)**：ARM 系统 MMU 第一/二代（含 Qualcomm 实现）
- **ARM SMMU Acceleration**：SMMUv3 硬件加速命令队列（NVIDIA Tegra241 CMDQV）
- **RISC-V IOMMU**：RISC-V 架构 IOMMU 驱动
- **IOMMUFD**：基于文件描述符的 IOMMU 用户空间接口
- **IOMMU DMA-API**：IOMMU 与 DMA 映射 API 的集成层
- **IOMMU Page Table**：IOMMU 页表管理（io-pgtable 库）
- **IOMMU Pages**：物理内存页分配与 IOMMU 映射管理
- **IOMMUPT**：IOMMU 页表遍历与操作框架
- **Intel IOMMU Accel**：Intel IOMMU 硬件加速器支持
- **IOMMU SVA/SVM**：共享虚拟地址 / 共享虚拟内存（PASID、PRI）
- **IOMMU Core**：通用 IOMMU 框架（不属于特定驱动）

---

## 项目说明

本项目用于追踪 Linux 内核 IOMMU (Input-Output Memory Management Unit) 子系统的 patch 提交情况。IOMMU 提供设备-内存地址转换、内存保护和设备隔离功能，是设备直通/虚拟化的基础。由于 patchwork 无独立 IOMMU 项目，数据通过全局搜索获取并经过 subject prefix 白名单/黑名单精确过滤。

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

*报告由 Linux Patches Tracker 自动生成 | 2026-11-11 17:06:18*
