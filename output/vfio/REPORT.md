# Linux VFIO 子系统 Patch 追踪报告

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
| 社区讨论中 | 27 | 100.0% |
| 已合入 | 0 | 0.0% |
| **总计** | **27** | **100%** |

### 按组织分类（TOP 15）

| 组织 | 数量 | 占比 |
|------|------|------|
| Google | 9 | 33.3% |
| IBM | 6 | 22.2% |
| Individual Contributor | 4 | 14.8% |
| NVIDIA | 4 | 14.8% |
| OzLabs Community | 2 | 7.4% |
| Huawei | 2 | 7.4% |

### 按子系统分类

| 子系统 | 数量 | 占比 |
|--------|------|------|
| VFIO PCI | 10 | 37.0% |
| VFIO Selftests | 4 | 14.8% |
| VFIO Core | 3 | 11.1% |
| VFIO IOMMUFD | 2 | 7.4% |
| VFIO CCW (s390) | 2 | 7.4% |
| VFIO Migration | 1 | 3.7% |
| VFIO Platform | 1 | 3.7% |
| VFIO CDX | 1 | 3.7% |
| VFIO FSL-MC | 1 | 3.7% |
| VFIO MLX5 Variant | 1 | 3.7% |
| VFIO Mediated Device | 1 | 3.7% |

## 重点 Patch Top20 清单

### 已合入

暂无。

### 社区讨论

| 厂商 | 简介 |
|------|------|
| NVIDIA | [PATCH v4 00/27] vfio/pci: Add CXL Type-2 device passthrough support ------为 VFIO 增加 CXL Type-2 加速器直通支持：绑定后按需加载 vfio-cxl 模块，为设备建立 CXL 内存设备并暴露 HDM 内存区域，同时把 HDM 解码器寄存器从直接 BAR 映射中排除，改由内核捕获并模拟提交握手，使客户机无法直接改写决定主机内存解码的物理解码器。绑定阶段会拒绝多解码器、交织等无法用单一虚拟解码器表示的拓扑，以及主机无法响应 CXL 复位请求的设备。 |
| OzLabs Community | [PATCH v5 00/9] vfio/pci: Add mmap() for DMABUFs ------让 VFIO 的 PCI BAR 映射改用 DMABUF 承载，并支持对导出的 DMABUF 直接做 mmap，使进程可以只把某个 BAR 子范围委托给其他客户端，而不必交出整个设备文件。新增按请求永久吊销 DMABUF 的能力，吊销后该缓冲区无法再被导入、附加或映射，已建立的映射也会失效，便于收回借出的 BAR 资源；同时把 BAR 撤销与清理路径合并，避免调用方遗漏其中一步。 |
| Google | [PATCH v5 00/20] vfio/pci: Base Live Update support for VFIO ------为 VFIO 直通设备增加跨 kexec 实时更新的基础支持：在冻结时把设备文件状态序列化并保存，下一内核可通过实时更新会话找回并重新打开该设备文件，而不是重新初始化设备。冻结前要求用户态关闭设备中断并保持 D0，冻结时设备会被复位，冻结后原设备文件不可用；若冻结失败，用户态需关闭文件并重新初始化。该功能目前为实验性且默认关闭。 |
| Huawei | [PATCH v19 00/18] vfio/pci: Add PCIe TPH support ------为 VFIO 直通设备增加 PCIe TPH 支持：在设备不支持时对用户态隐藏该能力，按策略虚拟化 TPH 能力寄存器并屏蔽写入，提供从 DMABUF 或 CPU 解析 PH/ST 以及批量编程 ST 表的用户接口，并在设备启用和关闭时复位硬件 TPH 状态，避免跨会话残留。 |
| IBM | [PATCH v9 00/10] s390/vfio_ccw fixes ------针对 s390 通道程序直通设备，修复通道程序初始化失败时只释放当前段而泄漏其他段内存、段数量无上限导致递归过深、越界检查多看一个命令字、首个间接地址读取不一致、按格式二计算格式一间接地址表长度偏大、读写区域索引未做范围限制、工作队列未取消、设备失联时在持锁路径清理资源、以及异步事件列表缺少保护等问题，分别补上清理、限长、校验和加锁处理。 |
| Huawei | [PATCH v20 00/16] vfio/pci: Add PCIe TPH support ------为 VFIO 直通设备增加 PCIe TPH（TLP 处理提示）支持，让用户态可以为设备发布 TPH 元数据并批量编程 ST 表。新增按需查询设备 TPH 能力、区分标准与扩展 ST 命名空间、校验设备作为完成方能否消费请求等接口，并修正 ST 表位置解析和使能标志的并发写入问题；同时缓存协商结果以减少重复读取配置空间。 |
| NVIDIA | [PATCH v4 00/10] mlx5 support for VFIO self test ------为 VFIO 自测框架新增 mlx5 ConnectX 驱动，通过命令接口把 VF 和 PF 初始化到运行状态，并用 RDMA 写自环回实现 DMA 内存拷贝，还支持通过 MSI-X 触发中断。为便于在用户态复用，把 WQE、CQE 等硬件结构定义和寄存器读写宏从内核头文件拆分出来，并让自测驱动可以声明所需的 DMA 区域大小。 |
| Google | [PATCH v2 00/4] Introduce vfio_dma_mapping_perf_test ------新增 VFIO DMA 映射性能测试，直接报告映射与解映射各阶段耗时而非判定通过失败，避免延迟阈值导致的测试不稳定。测试用预填充映射隔离缺页影响，并增加基于 memfd 的映射用例以对比不同映射方式，还允许通过命令行指定 DMA 区域大小和透传给测试框架的参数。 |
| Google | [PATCH v4 00/18] iommu: Add live update state preservation ------为内核热更新保留设备的 IOMMU 页表、域标识和进程地址空间标识表，在新内核恢复地址转换并重新挂接设备；保留期间禁止修改映射或更换地址空间。已实现底层恢复，但面向用户的 IOMMU 文件接口恢复流程仍待补齐，并附带状态保留测试。 |
| Google | [PATCH v4 00/9] vfio: selftests: Add driver for Intel Ethernet Gigabit Controller (IGB) ------为 VFIO 自测新增 Intel IGB 千兆网卡驱动，使测试可在 QEMU 模拟设备上运行而无需真实硬件。驱动用 PHY 内部环回实现内存拷贝，改用高级收发描述符、完整配置 MSI-X 中断路由，并延长拷贝完成等待时间；同时关闭 PCIe 完成超时重发，避免故意使用无效地址的测试反复重试干扰复位恢复。 |
| Huawei | [PATCH v3 00/3] hisi_acc_vfio_pci: fix three driver issues ------修复海思加速器直通与热迁移的三处问题：物理功能直通时检查迁移状态，避免错误回调访问空指针；复位后清除本次持锁标记，防止后续超时复位误释放他人的锁；第三代队列管理硬件搭配 64KB 内存页时禁用热迁移，避免寄存器隔离不足及客户机访存异常，其他配置的直通不受影响。 |
| NVIDIA | [PATCH v1 00/5] PCI/vfio-pci: Guard resets against active SR-IOV VFs ------让 PCI 函数级复位在 SR-IOV 物理功能仍有启用虚拟功能时被拒绝，避免复位波及未纳入影响范围的虚拟功能；同时新增可在复位前对受影响设备做检查的槽位或总线复位接口，vfio-pci 热复位据此要求先拆除虚拟功能。此外不再缓存复位是否可用，改为每次查询设备当前是否具备复位方法，避免管理操作使缓存失效。 |
| IBM | [v5,1/4] s390/vfio-ap: Fix leak of pinned NIB and registered NISC in vfio_ap_irq_enable/disable() ------在 s390 的 AP 队列中断使能/禁用流程中，硬件返回异常状态码时，原代码会去禁用此前已生效的中断配置，并释放本次调用尚未保存的 NIB 和 NISC，导致资源泄漏或误拆正常配置。现在改为只清理本次调用涉及的资源，保留队列上已保存的配置；禁用时若等待中断真正关闭超时，则向客户机返回未完成状态，避免其提前释放硬件仍可能写入的缓冲区。 |
| Google | [v10,2/3] vfio: selftests: igb: Add driver for Intel 82576 device ------为 VFIO 自测框架新增 Intel 82576 网卡驱动，使测试无需专用硬件即可在 QEMU 中运行。由于该网卡不支持小于以太网最小载荷的 DMA，驱动要求传输不小于 60 字节；它没有原生内存拷贝能力，改用 PHY 内部环回实现，并支持 MSI-X 中断路由，同时关闭 PCIe 完成超时重试以便无效 DMA 测试后能干净恢复。 |
| OzLabs Community | [v4,10/10] vfio/pci: Add mmap() attributes to DMABUF feature ------为 vfio-pci 导出的 DMABUF 增加内存属性设置接口，允许用户选择后续映射该缓冲区时使用非缓存或写合并页表属性。默认仍为非缓存，选择写合并后 BAR 区域映射会采用写合并属性，且只影响之后新建的映射，不改变已存在的映射。 |
| Google | [PATCH] vfio: selftests: Add documentation ------为 VFIO 自测补充文档，说明如何挑选和绑定设备、运行与清理测试、编写测试用例，以及辅助库提供的核心对象和驱动抽象，并加入驱动 API 索引和维护者条目，方便内核开发者上手使用这套基于真实 PCI 设备的用户态测试框架。 |
| NVIDIA | [rdma-next,09/15] vfio/mlx5: Enable relaxed ordering on the live migration data mkey ------为 mlx5 的 VFIO 热迁移数据内存键启用宽松排序。由于固件保证设备发出的数据写入在完成事件上报前已完成，无需强排序，启用后可在限制严格排序内存注册的硬件上支持热迁移，并改善性能。 |
| Google | [v8,2/6] vfio: selftests: igb: Use PHY internal loopback on 82576 ------为 82576 网卡的 VFIO 自测驱动改用 PHY 内部环回：原代码等待自协商后启用 MAC 环回，但该芯片手册明确不支持 MAC 环回，真实硬件上描述符引擎不工作。现改为配置 PHY 环回并强制 MAC 链路为千兆全双工，同时保留 MAC 环回位以兼容 QEMU 模拟，使自测在真机和模拟环境都能收发环回帧。 |
| IBM | [v7,01/23] vfio: Use file-based reference counting for KVM ------把 VFIO 与 KVM 之间的引用计数从手动模块符号引用改为基于文件引用计数，接口改为传递虚拟机文件指针，并让分组和设备文件各自持有引用，避免文件被回收后残留指针指向无关对象。这样去掉了 VFIO 对外导出的 KVM 符号，为同时加载第二个 KVM 模块铺路。 |
| IBM | [v4,01/27] VFIO: take reference to the KVM module ------在 VFIO 获取 KVM 引用时显式保存并增加 KVM 模块引用，替代原先依赖符号获取隐式维持模块存活的做法，为后续移除符号获取机制做准备。获取失败时按顺序回退释放模块引用，避免模块被卸载后仍被使用。 |

---

## 已合入 Patches

暂无。

## 社区讨论中 Patches

### ◆ 子系统：VFIO PCI（10 patches）

**▸ 组织：Google**（3 patches）

**[RFC,v1,1/1] vfio/pci: Revoke BARs and DMABUFs during sysfs-triggered PCI reset**

- 日期：2026-08-07
- 状态：社区讨论中
- 作者邮箱：Pranjal Shrivastava <praan@google.com>
- 概括：在 vfio-pci 中实现 PCI 错误处理器的复位准备与复位完成回调，使通过 sysfs 触发的设备复位（FLR 或 SBR）能通知驱动。此前这类复位不经过驱动，已导出的 DMA 缓冲和 BAR 映射不会被撤销，导入方仍可继续使用；现在复位前在持有内存写锁的情况下撤销 BAR 与已导出 DMA 缓冲，复位后再恢复，并相应调整热复位流程的加锁与解锁顺序。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260807201405.3717430-2-praan@google.com/

**[RFC,1/1] vfio/pci: Disable sriov on PF device close**

- 日期：2026-08-05
- 状态：社区讨论中
- 作者邮箱：Samiullah Khawaja <skhawaja@google.com>
- 概括：关闭 SR-IOV 物理功能的 VFIO 设备文件时，原先直接复位硬件，会打断已绑定主机驱动或其它 VFIO 实例的虚拟功能，造成内核状态与硬件不一致。现改为在复位前先关闭该设备的 SR-IOV，让虚拟功能在软件层面完成拆除和移除。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260805003355.728299-2-skhawaja@google.com/

**[SERIES] vfio/pci: Base Live Update support for VFIO** （cover letter，7/18 个 patch 达到代码量阈值）

- 日期：2026-07-14
- 状态：社区讨论中
- 作者邮箱：Vipin Sharma <vipinsh@google.com>
- 概括：为 vfio-pci 增加基础 Live Update 支持，使绑定该驱动的设备在主机经 kexec 进行 Live Update 时可不中断运行。冻结阶段撤销 DMA 缓冲并复位设备，把设备的 PCI 段号与总线设备功能号序列化后经 Kexec-Handover 与 Live Update 编排器保留；新内核启动后用户态可通过检索接口取回被保留的设备文件，且必须经该接口获取而不能直接打开字符设备。该支持目前为实验性且默认关闭。
- 达到阈值的 patches（7 个，显示前 5）：
  - vfio/pci: Factor out the reset logic in VFIO PCI device close path
  - vfio: Export various helpers from VFIO
  - vfio/pci: Export vfio_pci_dma_buf_move for vfio-pci module
  - vfio/pci: Register a file handler with Live Update Orchestrator
  - vfio/pci: Preserve vfio-pci device files across Live Update
  - ... 及其他 2 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260714151505.3466855-2-vipinsh@google.com/

**▸ 组织：OzLabs Community**（2 patches）

**[SERIES] vfio/pci: Add mmap() for DMABUFs** （cover letter，7/7 个 patch 达到代码量阈值）

- 日期：2026-07-15
- 状态：社区讨论中
- 作者邮箱：Matt Evans <matt@ozlabs.org>
- 概括：让 VFIO 的 PCI BAR 映射改用 DMABUF 承载，并支持对导出的 DMABUF 直接做 mmap，使进程可以只把某个 BAR 子范围委托给其他客户端，而不必交出整个设备文件。新增按请求永久吊销 DMABUF 的能力，吊销后该缓冲区无法再被导入、附加或映射，已建立的映射也会失效，便于收回借出的 BAR 资源；同时把 BAR 撤销与清理路径合并，避免调用方遗漏其中一步。
- 达到阈值的 patches（7 个，显示前 5）：
  - vfio/pci: Add a helper to look up PFNs for DMABUFs
  - vfio/pci: Add a helper to create a DMABUF for a BAR-map VMA
  - vfio/pci: Convert BAR mmap() to use a DMABUF
  - vfio/pci: Provide a user-facing name for BAR mappings
  - vfio/pci: Clean up BAR zap and revocation
  - ... 及其他 2 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260715174737.15287-4-matt@ozlabs.org/

**[v4,10/10] vfio/pci: Add mmap() attributes to DMABUF feature**

- 日期：2026-07-01
- 状态：社区讨论中
- 作者邮箱：Matt Evans <matt@ozlabs.org>
- 概括：为 vfio-pci 导出的 DMABUF 增加内存属性设置接口，允许用户选择后续映射该缓冲区时使用非缓存或写合并页表属性。默认仍为非缓存，选择写合并后 BAR 区域映射会采用写合并属性，且只影响之后新建的映射，不改变已存在的映射。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260701171245.90111-11-matt@ozlabs.org/

**▸ 组织：Huawei**（2 patches）

**[SERIES] hisi_acc_vfio_pci: fix three driver issues** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-08-31
- 状态：社区讨论中
- 作者邮箱：Longfang Liu <liulongfang@huawei.com>
- 概括：修复海思加速器直通与热迁移的三处问题：物理功能直通时检查迁移状态，避免错误回调访问空指针；复位后清除本次持锁标记，防止后续超时复位误释放他人的锁；第三代队列管理硬件搭配 64KB 内存页时禁用热迁移，避免寄存器隔离不足及客户机访存异常，其他配置的直通不受影响。
- 达到阈值的 patches（2 个，显示前 5）：
  - hisi_acc_vfio_pci: reject live migration on 64KB page with QM_HW_V3 hardware
  - hisi_acc_vfio_pci: clear set_reset_flag after reset completed
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260831090951.844569-2-liulongfang@huawei.com/

**[SERIES] vfio/pci: Add PCIe TPH support** （cover letter，4/10 个 patch 达到代码量阈值）

- 日期：2026-07-02
- 状态：社区讨论中
- 作者邮箱：fengchengwen <fengchengwen@huawei.com>
- 概括：为 vfio-pci 增加 PCIe TPH（事务层处理提示）支持，让用户态可查询和控制设备的 TPH 能力。此前 TPH 能力对用户不可见且相关寄存器写入被丢弃；现在按策略分级开放，虚拟化 TPH 能力寄存器，支持从 DMA 缓冲或 CPU 来源解析处理提示与转向标签，并支持批量编程转向标签表，同时修正了内核 TPH 辅助函数中转向标签表位置提取和并发更新问题。
- 达到阈值的 patches（4 个，显示前 5）：
  - vfio/pci: Hide TPH capability when TPH is unsupported
  - vfio/pci: Virtualize PCIe TPH capability registers
  - vfio/pci: Implement TPH_ST feature for batch ST table programming
  - vfio/pci: Reset hardware TPH state on device enable/disable
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260702124224.57168-10-fengchengwen@huawei.com/

**▸ 组织：NVIDIA**（2 patches）

**[SERIES] vfio/pci: Add CXL Type-2 device passthrough support** （cover letter，18/22 个 patch 达到代码量阈值）

- 日期：2026-08-13
- 状态：社区讨论中
- 作者邮箱：Manish Honap <mhonap@nvidia.com>
- 概括：为 vfio-pci 增加 CXL Type-2 设备直通支持：新增按需加载的 vfio-cxl 模块，在绑定后创建 CXL 内存设备并接管整个组件寄存器 BAR，拒绝多解码器或交织拓扑，把 HDM 解码器寄存器从直接映射中排除并改为陷阱模拟，虚拟化 DVSEC、模拟提交握手、在复位和电源切换时撤销映射，并向用户态暴露 HDM 区域与解码器几何信息。
- 达到阈值的 patches（18 个，显示前 5）：
  - vfio/cxl: Create the CXL memory device at bind
  - vfio/pci: Detect CXL devices and load vfio-cxl on demand
  - vfio/cxl: Own the whole component register BAR
  - vfio/cxl: Reject unsupported decoder topologies at bind
  - vfio/pci: Let a provider exclude a BAR sub-range from mmap
  - ... 及其他 13 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260813093631.2288172-6-mhonap@nvidia.com/

**[SERIES] PCI/vfio-pci: Guard resets against active SR-IOV VFs** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-12
- 状态：社区讨论中
- 作者邮箱：Alex Williamson <alex.williamson@nvidia.com>
- 概括：让 PCI 函数级复位在 SR-IOV 物理功能仍有启用虚拟功能时被拒绝，避免复位波及未纳入影响范围的虚拟功能；同时新增可在复位前对受影响设备做检查的槽位或总线复位接口，vfio-pci 热复位据此要求先拆除虚拟功能。此外不再缓存复位是否可用，改为每次查询设备当前是否具备复位方法，避免管理操作使缓存失效。
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio/pci: Refuse to reset an SR-IOV PF with enabled VFs
  - vfio/pci: Use pci_reset_supported() in place of reset_works
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260812045325.2733631-4-alex.williamson@nvidia.com/

**▸ 组织：IBM**（1 patches）

**[v1] vfio/pci: Avoid mapping BARs for devices with non-mappable BARs**

- 日期：2026-07-29
- 状态：社区讨论中
- 作者邮箱：Farhan Ali <alifm@linux.ibm.com>
- 概括：为 s390 的 ISM 等 BAR 无法被 CPU 映射的设备跳过 BAR 映射，避免其 256 TiB 的 BAR 触发地址范围受限告警。该标志由 PCI 核心在枚举时设置，此前已在探测映射路径使用，现在映射 BAR 资源时同样遵循。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260729181116.1373-1-alifm@linux.ibm.com/

---

### ◆ 子系统：VFIO Selftests（4 patches）

**▸ 组织：Google**（4 patches）

**vfio: selftests: Add documentation**

- 日期：2026-08-18
- 状态：社区讨论中
- 作者邮箱：David Matlack <dmatlack@google.com>
- 概括：为 VFIO 自测补充文档，说明如何挑选和绑定设备、运行与清理测试、编写测试用例，以及辅助库提供的核心对象和驱动抽象，并加入驱动 API 索引和维护者条目，方便内核开发者上手使用这套基于真实 PCI 设备的用户态测试框架。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260818000550.2526247-1-dmatlack@google.com/

**[SERIES] Introduce vfio_dma_mapping_perf_test** （cover letter，3/4 个 patch 达到代码量阈值）

- 日期：2026-08-04
- 状态：社区讨论中
- 作者邮箱：Aaron Lewis <aaronlewis@google.com>
- 概括：为 VFIO 自测新增 DMA 映射性能测试，直接报告映射与解映射各阶段的耗时而非判定通过失败，避免延迟阈值带来的不稳定。测试支持指定 DMA 区域大小，并新增基于内存文件描述符的映射用例，用于比较不同映射方式的延迟；同时把解映射完整性检查集中到公共库中，简化各测试的校验。
- 达到阈值的 patches（3 个，显示前 5）：
  - vfio: selftests: Introduce vfio_dma_mapping_perf_test
  - vfio: selftests: Add memfd test to vfio_dma_mapping_perf_test
  - vfio: selftests: Allow a size for vfio_dma_mapping_perf_test
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260804165748.1060476-3-aaronlewis@google.com/

**[v8,2/6] vfio: selftests: igb: Use PHY internal loopback on 82576**

- 日期：2026-07-29
- 状态：社区讨论中
- 作者邮箱：Josh Hilke <jrhilke@google.com>
- 概括：为 82576 网卡的 VFIO 自测驱动改用 PHY 内部环回：原代码等待自协商后启用 MAC 环回，但该芯片手册明确不支持 MAC 环回，真实硬件上描述符引擎不工作。现改为配置 PHY 环回并强制 MAC 链路为千兆全双工，同时保留 MAC 环回位以兼容 QEMU 模拟，使自测在真机和模拟环境都能收发环回帧。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260729-igb_v3_b4-v8-2-3ed236272b4e@google.com/

**[SERIES] vfio: selftests: Add driver for Intel Ethernet Gigabit Controller (IGB)** （cover letter，2/5 个 patch 达到代码量阈值）

- 日期：2026-07-10
- 状态：社区讨论中
- 作者邮箱：Josh Hilke <jrhilke@google.com>
- 概括：为 VFIO 自测新增 Intel 千兆以太网控制器（IGB）驱动，使自测可在 QEMU 模拟的 IGB 设备上运行而无需真实硬件。驱动用回环模式实现内存拷贝，并针对真实 82576 硬件改用 PHY 内部回环、高级收发描述符、完整的 MSI-X 中断路由，延长拷贝完成等待时间并关闭 PCIe 完成超时重试，以兼容物理设备。
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio: selftests: igb: Add driver for IGB QEMU device
  - vfio: selftests: igb: Disable PCIe completion timeout retries
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260710-igb_v3_b4-v4-1-56e7e2576cc1@google.com/

---

### ◆ 子系统：VFIO Core（3 patches）

**▸ 组织：IBM**（2 patches）

**[v7,01/23] vfio: Use file-based reference counting for KVM**

- 日期：2026-08-31
- 状态：社区讨论中
- 作者邮箱：Steffen Eiden <seiden@linux.ibm.com>
- 概括：把 VFIO 与 KVM 之间的引用计数从手动模块符号引用改为基于文件引用计数，接口改为传递虚拟机文件指针，并让分组和设备文件各自持有引用，避免文件被回收后残留指针指向无关对象。这样去掉了 VFIO 对外导出的 KVM 符号，为同时加载第二个 KVM 模块铺路。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260831144802.834315-2-seiden@linux.ibm.com/

**[v4,01/27] VFIO: take reference to the KVM module**

- 日期：2026-07-06
- 状态：社区讨论中
- 作者邮箱：Steffen Eiden <seiden@linux.ibm.com>
- 概括：在 VFIO 获取 KVM 引用时显式保存并增加 KVM 模块引用，替代原先依赖符号获取隐式维持模块存活的做法，为后续移除符号获取机制做准备。获取失败时按顺序回退释放模块引用，避免模块被卸载后仍被使用。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260706085229.979525-2-seiden@linux.ibm.com/

**▸ 组织：Individual Contributor**（1 patches）

**vfio/type1: conditional rescheduling while unpinning**

- 日期：2026-07-23
- 状态：社区讨论中
- 作者邮箱：Samuel Crossley <samuelcrossley@gmail.com>
- 概括：解除大块设备直通 DMA 映射时，保留内存映射的逐页释放循环没有重新调度点，曾导致 GPU 直通主机在释放上百 GiB 设备内存时软锁死。现把释放工作分批处理并在批间让出 CPU，使单次解除映射不会长时间卡住处理器。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260723-vfio-v1-1-3b59579916c6@gmail.com/

---

### ◆ 子系统：VFIO IOMMUFD（2 patches）

**▸ 组织：Google**（2 patches）

**[SERIES] iommu: Add live update state preservation** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-08
- 状态：社区讨论中
- 作者邮箱：Samiullah Khawaja <skhawaja@google.com>
- 概括：为内核热更新保留设备的 IOMMU 页表、域标识和进程地址空间标识表，在新内核恢复地址转换并重新挂接设备；保留期间禁止修改映射或更换地址空间。已实现底层恢复，但面向用户的 IOMMU 文件接口恢复流程仍待补齐，并附带状态保留测试。
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio/pci: Preserve the iommufd state of the vfio cdev
  - iommufd: Add APIs to preserve/unpreserve a vfio cdev
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260808022723.3893618-18-skhawaja@google.com/

**[1/2] vfio/type1: Periodically try rescheduling when unmapping**

- 日期：2026-07-14
- 状态：社区讨论中
- 作者邮箱：Aaron Lewis <aaronlewis@google.com>
- 概括：在 VFIO 类型一 IOMMU 解除大块 DMA 映射时，原先连续遍历物理页可能长时间不让出 CPU，触发调度延迟告警。现改为每处理一定数量的页就尝试重新调度，使单次解除映射不再长时间独占处理器。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260714210303.3967981-2-aaronlewis@google.com/

---

### ◆ 子系统：VFIO CCW (s390)（2 patches）

**▸ 组织：IBM**（2 patches）

**[SERIES] s390/vfio_ccw: Free all memory if cp_init() fails** （cover letter，6/10 个 patch 达到代码量阈值）

- 日期：2026-08-03
- 状态：社区讨论中
- 作者邮箱：Claudio Imbrenda <imbrenda@linux.ibm.com>
- 概括：为 s390 的 vfio-ccw 修复通道程序处理缺陷，包括初始化失败时释放全部已分配段、限制通道程序段数、修正 CCW 数组越界与读写区域索引范围、校验首个 IDAW 一致并按格式计算 IDAL 长度，同时在设备释放时取消工作队列、把清理移出不可操作路径、扩大互斥锁并新增 CRW 锁；该系列还包含若干 s390 KVM 的独立修复。
- 达到阈值的 patches（6 个，显示前 5）：
  - s390/vfio_ccw: Limit the number of channel program segments
  - s390/vfio_ccw: Calculate idal length based on idaw type
  - s390/vfio_ccw: Cancel existing workqueues
  - s390/vfio_ccw: Ensure index for read/write regions are within range
  - s390/vfio_ccw: Selectively expand io_mutex
  - ... 及其他 1 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260803160924.236807-3-imbrenda@linux.ibm.com/

**[SERIES] s390/vfio_ccw fixes** （cover letter，6/10 个 patch 达到代码量阈值）

- 日期：2026-07-28
- 状态：社区讨论中
- 作者邮箱：Eric Farman <farman@linux.ibm.com>
- 概括：为 s390 的 vfio-ccw 通道程序处理修复多处缺陷：初始化失败时不再只释放当前段而泄漏其他段，限制单个通道程序的段数以防递归过深，修正 CCW 数组越界检查、读写区域索引范围、首个 IDAW 一致性及 IDAL 长度按格式计算，并在设备释放时取消工作队列、把清理移出不可操作路径、扩大互斥锁范围并新增 CRW 锁，避免释放后仍派发工作或并发访问。
- 达到阈值的 patches（6 个，显示前 5）：
  - s390/vfio_ccw: limit the number of channel program segments
  - s390/vfio_ccw: ensure index for read/write regions are within range
  - s390/vfio_ccw: ensure first IDAW remains constant
  - s390/vfio_ccw: calculate idal length based on idaw type
  - s390/vfio_ccw: cancel existing workqueues
  - ... 及其他 1 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260728033022.2658232-3-farman@linux.ibm.com/

---

### ◆ 子系统：VFIO Migration（1 patches）

**▸ 组织：NVIDIA**（1 patches）

**[rdma-next,09/15] vfio/mlx5: Enable relaxed ordering on the live migration data mkey**

- 日期：2026-07-26
- 状态：社区讨论中
- 作者邮箱：Michael Gur <michaelgur@nvidia.com>
- 概括：为 mlx5 的 VFIO 热迁移数据内存键启用宽松排序。由于固件保证设备发出的数据写入在完成事件上报前已完成，无需强排序，启用后可在限制严格排序内存注册的硬件上支持热迁移，并改善性能。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260726092943.2880176-10-michaelgur@nvidia.com/

---

### ◆ 子系统：VFIO Platform（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**vfio/platform: prevent read-only region mappings from becoming writable**

- 日期：2026-08-19
- 状态：社区讨论中
- 作者邮箱：Abdifatah Suruur <suruurism@gmail.com>
- 概括：修复 vfio 平台设备只读区域映射可被改写的问题。此前只读区域虽拒绝可写映射，但映射仍保留可写标志，用户可先只读映射再用内存保护调用升级为可写，从而写入平台标记为只读的 MMIO 区域；现在对无写权限的区域清除该标志，使这类升级不再可行。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260819083940.1374-1-suruurism@gmail.com/

---

### ◆ 子系统：VFIO CDX（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**vfio/cdx: prevent read-only region mappings from becoming writable**

- 日期：2026-08-19
- 状态：社区讨论中
- 作者邮箱：Abdifatah Suruur <suruurism@gmail.com>
- 概括：修复 vfio 的 CDX 总线设备只读区域映射可被改写的问题。此前只读区域拒绝可写映射后仍保留可写标志，用户可先只读映射再升级为可写，写入设备标记为只读的 MMIO 区域；现在对无写权限的区域清除该标志，阻止这种升级。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260819083943.1391-1-suruurism@gmail.com/

---

### ◆ 子系统：VFIO FSL-MC（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**vfio/fsl-mc: prevent read-only region mappings from becoming writable**

- 日期：2026-08-19
- 状态：社区讨论中
- 作者邮箱：Abdifatah Suruur <suruurism@gmail.com>
- 概括：修复 vfio 的 fsl-mc 设备只读区域映射可被改写的问题。此前只读区域拒绝可写映射后仍保留可写标志，用户可先只读映射再升级为可写，写入设备标记为只读的 MMIO 区域（如响应门户）；现在对无写权限的区域清除该标志，阻止这种升级。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260819083949.1408-1-suruurism@gmail.com/

---

### ◆ 子系统：VFIO MLX5 Variant（1 patches）

**▸ 组织：NVIDIA**（1 patches）

**[SERIES] mlx5 support for VFIO self test** （cover letter，3/5 个 patch 达到代码量阈值）

- 日期：2026-08-12
- 状态：社区讨论中
- 作者邮箱：Jason Gunthorpe <jgg@nvidia.com>
- 概括：为 VFIO 自测框架新增 mlx5 ConnectX 驱动支持：把 mlx5 的 WQE/CQE 布局、硬件常量和寄存器访问宏整理成可被自测引用的头文件，补充大端 MMIO 与内存屏障等工具函数，允许驱动声明所需 DMA 区域大小，并实现命令接口、HCA 初始化、队列创建、RDMA 回环拷贝及通过 MSI-X 触发中断，使自测能覆盖该网卡的 DMA 与中断路径。
- 达到阈值的 patches（3 个，显示前 5）：
  - vfio: selftests: Add mlx5 driver - data path and memcpy ops
  - vfio: selftests: mlx5 driver - add send_msi support
  - vfio: selftests: Add mlx5 driver - HW init and command interface
- 来源：https://patchwork.kernel.org/project/kvm/patch/6-v4-021df3fb5a3f+98e-mlx5st_jgg@nvidia.com/

---

### ◆ 子系统：VFIO Mediated Device（1 patches）

**▸ 组织：IBM**（1 patches）

**[SERIES] s390/vfio-ap: Fix pre-existing bugs in vfio_ap device driver** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-08-31
- 状态：社区讨论中
- 作者邮箱：Anthony Krowiak <akrowiak@linux.ibm.com>
- 概括：修复 s390 vfio-ap 驱动的既有缺陷：启用中断失败时不再错误地关闭原有可用配置，而是只清理本次调用的通知资源；设备关闭时释放用户态注册的中断通知 eventfd 引用，避免内核长期泄漏；队列复位轮询增加两秒上限，防止硬件持续返回忙时无限循环并阻塞全局锁导致其他客户机挂起；域位图改用域数量常量以保持一致。
- 达到阈值的 patches（1 个，显示前 5）：
  - s390/vfio-ap: Fix leak of pinned NIB and registered NISC in vfio_ap_irq_enable/disable()
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260831171443.222225-5-akrowiak@linux.ibm.com/

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

*报告由 Linux Patches Tracker 自动生成 | 2026-09-11 18:20:42*
