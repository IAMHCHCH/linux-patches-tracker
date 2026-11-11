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
| 社区讨论中 | 41 | 100.0% |
| 已合入 | 0 | 0.0% |
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
| VFIO PCI | 17 | 41.5% |
| VFIO Core | 12 | 29.3% |
| VFIO Selftests | 3 | 7.3% |
| VFIO FSL-MC | 1 | 2.4% |
| VFIO Platform | 1 | 2.4% |
| VFIO AP (s390) | 1 | 2.4% |
| VFIO Migration | 1 | 2.4% |
| VFIO CCW (s390) | 1 | 2.4% |
| VFIO CDEV | 1 | 2.4% |
| VFIO CDX | 1 | 2.4% |
| VFIO MLX5 Variant | 1 | 2.4% |
| VFIO IOMMUFD | 1 | 2.4% |

## 重点 Patch Top20 清单

### 已合入

暂无。

### 社区讨论

| 厂商 | 简介 |
|------|------|
| NVIDIA | [PATCH v6 00/31] vfio/pci: Add CXL Type-2 device passthrough support ------为 CXL Type-2 设备直通提供支持：新增 vfio-cxl 模块，在按需加载后独占组件寄存器 BAR，向客户机只读呈现 HDM 解码寄存器并将 HDM 内存区域作为可映射缓冲区导出；vfio-pci 增加排除范围列表，防止客户机直接访问这些寄存器。同时让持有 HDM 资源的驱动执行 CXL 复位，并在热复位和低功耗返回时恢复解码器状态；当 CXL 端口屏蔽次级总线复位时拒绝相关总线或槽复位，避免误报成功。 |
| NVIDIA | [PATCH v1 00/19] vfio/pci: Handle PCI error recovery and report state to userspace ------为VFIO PCI增加主机PCI错误恢复协调机制：恢复期间通过内部状态与锁阻塞新的设备访问，并串行化配置空间、复位、中断、运行时电源管理、BAR访问等操作，避免与恢复流程竞争；恢复结果可通过设备特性向用户态报告状态和序号，仅通用vfio-pci驱动在用户态启用后生效。 |
| OzLabs Community | [PATCH v8 00/9] vfio/pci: Add mmap() for DMABUFs ------为VFIO PCI的DMABUF导出和映射提供完整支持：普通BAR的mmap改为基于DMABUF，使导出的DMABUF文件描述符可被mmap，从而把BAR子范围安全地交给没有VFIO设备文件描述符的其他进程；同时统一撤销和恢复逻辑，并允许用户空间请求立即撤销DMABUF，使其映射失效且不能再被映射或附加。 |
| Google | [PATCH v1 00/5] vfio/pci: Fix power state race with SR-IOV enablement ------修复 VFIO PCI 设备电源状态转换与 SR-IOV 启用并发时的竞态：关闭设备路径未持有内存锁就执行电源状态恢复，可能与用户态写入虚拟功能数量触发的同时恢复并发执行，导致已启用虚拟功能时的基地址寄存器更新冲突和内核警告。现在所有电源状态转换均在内存锁保护下进行，并对无锁读写的虚拟功能活动标志进行标注，新增自测试覆盖 D3hot 关闭、D3hot 下启用 SR-IOV 及两者竞态，通过内核警告计数判定失败。 |
| NVIDIA | [PATCH v2 00/16] vfio/pci: Handle PCI error recovery and report state to userspace ------为直通给用户态的 PCI 设备加入主机 PCI 错误恢复处理：错误恢复开始后，新的配置空间、基地址寄存器与只读存储器、中断配置、设备复位和电源管理访问会被阻塞，已进入的访问需先完成，避免用户态与恢复流程并发改动设备；恢复过程中根据打开时保存的状态在复位后重建设备，完成后重新放行访问并通知用户态，上报冻结、复位、失败等状态，失败时保持阻塞，用户态需显式启用该能力。 |
| Google | [PATCH v1 00/9] vfio: Add support for platform devices ------在 kvmtool 虚拟机管理工具中新增平台设备直通支持：原先只支持 PCI 设备，现在可通过命令行指定已绑定到 VFIO 平台驱动的平台设备，把设备的输入输出内存区域映射到客户机预留地址，并从设备树模板生成客户机节点；同时抽取共用中断配置代码，支持边沿触发中断和多个中断线描述。这使 ARM 等平台设备能透传给客户机，且客户机可按模板获得兼容属性以驱动设备。 |
| NVIDIA | [PATCH v7 00/10] mlx5 support for VFIO self test ------为VFIO自测试框架新增mlx5 ConnectX设备驱动，可在VFIO环境中初始化HCA、建立命令队列和RDMA自环回队列，执行DMA内存复制测试，并能通过完成事件触发MSI-X中断，从而扩展自测试对mlx5设备DMA和中断路径的验证能力。 |
| Google | [PATCH v3 00/4] Introduce vfio_dma_mapping_perf_test ------新增 VFIO 直接内存访问映射性能自测工具，以延迟报告替代不稳定的通过或失败判断，分别测量内存映射、DMA 区域映射或解映射和内存解映射耗时。增加基于内存文件的映射测试，用于展示按文件映射接口比传统映射方式更快；并扩展自测框架支持自定义命令行参数，允许指定 DMA 区域大小，便于覆盖不同测试场景。 |
| Google | [PATCH v6 00/18] iommu: Add live update state preservation ------为支持跨内核热更新，在内核 IOMMU 核心、英特尔 VT-d 及 iommufd/VFIO 中新增状态保存与恢复路径：保存根表、上下文表、PASID 表、域编号和页表，并在恢复时回收已保存域编号、重新附加设备；用户态可先标记要保留的硬件页表，保存期间对应 IO 地址空间被设为不可变，映射或解映射会返回忙，避免状态变化。支持地址转换服务的设备拒绝保存，直通设备可在内核切换后继续使用原有 DMA 映射。 |
| IBM | [v6,1/5] s390/vfio-ap: Fix leak of pinned NIB and registered GISC in vfio_ap_irq_enable/disable() ------针对s390 vfio-ap AP队列中断使能与禁用，原来在禁用中断时可能过早释放固定通知指示字节页并注销客户中断子类，若硬件仍使能中断，后续中断会直接内存访问已释放页造成内存破坏；现在禁用后先轮询确认中断位已清再释放资源，若超时无法确认则保留该页和中断子类不释放，避免野DMA写。 |
| IBM | [v11,5/5] vfio-pci/zdev: Add VFIO FMB device features ------为通过VFIO透传的s390 zPCI设备增加FMB（函数测量块）透传能力，原来用户态无法直接获取FMB数据，现在提供两个设备特性：一个用于启用或禁用FMB，另一个在FMB启用后读取最新测量数据，从而让用户态能够按需控制并读取zPCI设备的功能测量统计。 |
| Individual Contributor | [v2,1/2] vfio/nvgrace-gpu: Use a core-only open_device in fallback mode ------针对NVIDIA Grace GPU在缺少ACPI内存属性或C2C链路断开时的回退模式，原来打开设备仍无条件注册空的内存区间用于毒页处理，导致区间树残留并在重新绑定后触发释放后使用；现在回退模式改用只执行PCI核心使能的打开路径，不再注册该区间，使打开与关闭对称。 |
| Google | [v1] vfio/pci: pass FAULT_FLAG_WRITE to vmf_insert_pfn_pmd/pud() ------VFIO PCI在插入巨页映射时原来始终按只读处理，当共享可写映射因软脏页清零等机制降级为写保护后，后续写缺页无法升级，陷入无限写缺页循环；现在根据缺页携带的写标志插入可写且标记脏的巨页条目，让写缺页能正确建立可写映射。 |
| Individual Contributor | [PATCH] vfio/nvgrace-gpu: Skip PFN registration for empty memory regions ------针对NVIDIA Grace GPU回退模式，原使用内存区长度为零时仍无条件注册页帧号地址空间，残留区间导致二次打开失败、解绑后释放后使用，并错误归类内存失效报告；现在仅在该区域长度非零时才注册和注销，回退模式不再注册任何区域。 |
| IBM | [v6,4/5] vfio/spapr_tce: Normalize EEH IOA error injection addresses ------在 sPAPR VFIO 的增强型错误处理错误注入接口中，先将用户态传入的目标地址规范化为 PCI/IOA 总线地址，再交给平台固件注入。此前 QEMU 可能传入 Linux 资源地址，而固件期望 PCI 总线地址，会造成注入失败。转换只针对 32/64 位且功能为内存或 IO 读写的错误；配置空间偏移和 DMA 地址保持原样不翻译，零地址零掩码代表无地址注入直接通过。 |
| Huawei | [v6,2/2] hisi_acc_vfio_pci: reject live migration on 64KB page with QM_HW_V3 hardware ------华为加速器在64KB页和第三代队列管理硬件组合下，功能区域与迁移寄存器共享同一个第二基地址寄存器物理页且无隔离，可能向客户机泄漏迁移寄存器并触发其内核回溯。此前修复在打开设备时直接拒绝，使直通完全不可用。现在改为在探测阶段根据虚拟功能控制模式和功能区域小于页大小来选择通用虚拟功能输入输出操作，保留设备直通能力，同时禁用有风险的动态迁移，避免迁移寄存器暴露。 |
| NVIDIA | [v2,12/12] vfio/nvidia-vgpu: add the Rust VFIO variant driver ------新增用 Rust 编写的 NVIDIA vGPU VFIO PCI 变体驱动，通过 Nova 核心管理虚拟 GPU 实例：首次打开设备时创建实例，最后一个句柄关闭时释放，暴露被分配的设备和子系统标识，限制第一号基地址寄存器窗口，并协调固件复位与 PCI 复位。该驱动通过 VFIO 覆盖匹配设备；没有可用 Nova vGPU 接口的设备仍使用普通 PCI 直通。构建上与 Nova 核心共享导出符号和元数据。 |
| ARM | [RFC,v2,12/15] vfio: Support VFIO devices that access the CPU MMU ------为不使用 IOMMU 而通过 CPU 内存管理单元访问内存的物理设备增加 VFIO 支持：新增 CPU MMU 组类型和注册接口，设备仍需属于 IOMMU 组，但打开设备组时不要求绑定容器或 IOMMU，也不要求提供 iommufd 所需的附加回调。这适用于虚拟机管理器为其创建虚拟设备（如设备树或 ACPI 表）的场景，管理器具备设备特定知识，知道无需分配容器，使这类设备能通过 VFIO 暴露。 |
| Red Hat | [v2,3/7] vfio/pci: Add qcom-vfio-pci variant driver ------新增高通 VFIO PCI 变体驱动，用于 ath11k 和 ath12k 无线设备直通。这些设备内嵌中断控制器，固件初始化时需要物理主机 MSI 地址，但虚拟机内只能看到虚拟客户机地址，导致初始化失败。驱动在分配后缓存物理 MSI 值，写入扩展配置空间并放置特定签名，供客户机驱动自动发现使用，无需修改 QEMU。前提是虚拟机启用 IOMMU 中断重映射和缓存模式，保证使用缓存物理地址的中断写入能正确路由。 |
| Google | [v2] vfio: selftests: Add documentation ------为 VFIO 自测试新增专门文档，说明这类测试作为用户态程序直接操作真实 PCI 设备，通过 VFIO 和 IOMMUFD 接口覆盖功能、回归和性能场景；文档给出设备选择、绑定到 VFIO-PCI 驱动、运行与清理步骤，并介绍辅助库和编写测试的基本结构，帮助内核开发者快速搭建和编写测试。 |

---

## 已合入 Patches

暂无。

## 社区讨论中 Patches

### ◆ 子系统：VFIO PCI（17 patches）

**▸ 组织：NVIDIA**（3 patches）

**[SERIES] vfio/pci: Add CXL Type-2 device passthrough support** （cover letter，23/25 个 patch 达到代码量阈值）

- 日期：2026-10-16
- 状态：社区讨论中
- 作者邮箱：Manish Honap <mhonap@nvidia.com>
- 概括：为 VFIO PCI 增加 CXL Type-2 设备透传支持。通过独立 vfio-cxl 模块按需注册回调，将 HDM 内存区域暴露给 guest 并作为 DMA-BUF 导出，使用排除范围列表屏蔽 HDM 解码器寄存器等敏感区域，在设备打开、关闭、重置和低功耗转换中协调状态。原问题：普通 vfio-pci 无法处理 CXL Type-2 的内存和寄存器生命周期，导致透传失败或主机资源冲突。
- 达到阈值的 patches（23 个，显示前 5）：
  - vfio/pci: Detect CXL devices and load the CXL provider on demand
  - vfio/pci: Add a generic excluded-range list
  - vfio/pci: Virtualize the CXL DVSEC in vfio_pci_config.c
  - vfio/pci: Call the CXL open and close hooks around device use
  - vfio/pci: Bracket PCI resets with the CXL reset hooks
  - ... 及其他 18 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261016161839.2765592-8-mhonap@nvidia.com/

**[v3,1/1] vfio/pci: Remove the core dependency on driver data**

- 日期：2026-10-05
- 状态：社区讨论中
- 作者邮箱：Simon Song <xinmengs@nvidia.com>
- 概括：vfio-pci 核心原本强制变体驱动必须把核心设备指针放在 PCI 驱动数据开头，限制私有数据布局并妨碍 Rust 基础设施的类型化驱动数据。现新增宏为各变体驱动生成包装回调，让它们把私有结构存入驱动数据并透传核心设备给辅助函数，同时调整显示解码回调选择，解除核心对驱动数据布局的依赖。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261005184236.1946167-2-xinmengs@nvidia.com/

**[SERIES] vfio/pci: Handle PCI error recovery and report state to userspace** （cover letter，15/19 个 patch 达到代码量阈值）

- 日期：2026-09-01
- 状态：社区讨论中
- 作者邮箱：Shameer Kolothum Thodi <skolothumtho@nvidia.com>
- 概括：为通用 vfio-pci 驱动增加主机 PCI 错误恢复支持。原先 PCI 错误回调与用户态设备访问、复位、关闭等并发时可能访问已释放状态或造成死锁。现引入恢复状态、锁和访问保护，在设备打开、复位、配置读写、中断、运行时电源管理、DMA 缓冲导出等路径上串行化与恢复流程的冲突，并可将恢复事件和序列号报告给用户态；用户态需显式启用，变体驱动行为保持不变。
- 达到阈值的 patches（15 个，显示前 5）：
  - vfio/pci: Serialize generic device lifetime with recovery
  - vfio/pci: Serialize function reset with recovery
  - vfio/pci: Serialize ioeventfd writes with recovery
  - vfio/pci: Retry BAR faults after temporary recovery
  - vfio/pci: Serialize BAR and ROM access with recovery
  - ... 及其他 10 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260901093217.8539-2-skolothumtho@nvidia.com/

**▸ 组织：Google**（3 patches）

**[SERIES] vfio/pci: Fix power state race with SR-IOV enablement** （cover letter，3/5 个 patch 达到代码量阈值）

- 日期：2026-10-29
- 状态：社区讨论中
- 作者邮箱：David Matlack <dmatlack@google.com>
- 概括：修复支持 SR-IOV 的 VFIO PCI 设备在关闭与启用虚拟功能并发时的电源状态竞争：若用户通过配置空间把设备置于 D3hot，两条路径可能同时恢复电源，对需要电源恢复的设备可能造成物理功能资源窗口在虚拟功能启用后被错误写回或保存状态被重复释放。现在所有电源状态转换都在同一把内存区域锁保护下进行，并显式标注虚拟功能启用标志的并发访问；同时新增自测覆盖上述场景，并以内核警告计数变化判定失败。
- 达到阈值的 patches（3 个，显示前 5）：
  - vfio/pci: Hold memory_lock for all calls to vfio_pci_set_power_state()
  - vfio/pci: Annotate lockless accesses to vdev->sriov_active
  - vfio: selftests: Add test for device power state transitions
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261029203324.1637772-2-dmatlack@google.com/

**[SERIES] iommu: Add live update state preservation** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-10-25
- 状态：社区讨论中
- 作者邮箱：Samiullah Khawaja <skhawaja@google.com>
- 概括：为支持跨内核热更新，在内核 IOMMU 核心、英特尔 VT-d 及 iommufd/VFIO 中新增状态保存与恢复路径：保存根表、上下文表、PASID 表、域编号和页表，并在恢复时回收已保存域编号、重新附加设备；用户态可先标记要保留的硬件页表，保存期间对应 IO 地址空间被设为不可变，映射或解映射会返回忙，避免状态变化。支持地址转换服务的设备拒绝保存，直通设备可在内核切换后继续使用原有 DMA 映射。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommufd: Add APIs to preserve/unpreserve a vfio cdev
  - vfio/pci: Preserve the iommufd state of the vfio cdev
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261025021930.674647-17-skhawaja@google.com/

**[v1] vfio/pci: pass FAULT_FLAG_WRITE to vmf_insert_pfn_pmd/pud()**

- 日期：2026-10-24
- 状态：社区讨论中
- 作者邮箱：Mina Almasry <almasrymina@google.com>
- 概括：VFIO PCI在插入巨页映射时原来始终按只读处理，当共享可写映射因软脏页清零等机制降级为写保护后，后续写缺页无法升级，陷入无限写缺页循环；现在根据缺页携带的写标志插入可写且标记脏的巨页条目，让写缺页能正确建立可写映射。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261024015540.538758-1-almasrymina@google.com/

**▸ 组织：OzLabs Community**（2 patches）

**[SERIES] vfio/pci: Add mmap() for DMABUFs** （cover letter，7/8 个 patch 达到代码量阈值）

- 日期：2026-10-06
- 状态：社区讨论中
- 作者邮箱：Matt Evans <matt@ozlabs.org>
- 概括：将 VFIO PCI 设备 BAR 的 mmap 改为通过 DMABUF 实现，并支持对导出的 DMABUF 文件描述符进行 mmap，使进程能安全共享 BAR 子范围而不必交出整个 VFIO 设备文件描述符。同时引入独立锁避免潜在死锁，修复低功耗恢复后撤销状态未恢复问题，统一 BAR 撤销与映射清理。
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
- 概括：VFIO PCI新增永久撤销DMABUF的接口：驱动进程可通过新特性传入已导出的缓冲区文件描述符，请求永久撤销；成功后缓冲区无法再被导入、附加或映射，已有的动态映射会被清理。用于回收先前借给下级客户端进程的PCI BAR资源，客户端结束后确保资源不可访问，再安全重新导出给新客户端，复位期间的临时撤销保持不变。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260911214200.33793-10-matt@ozlabs.org/

**▸ 组织：Kernel.org**（2 patches）

**[SERIES] KVM/VFIO: guest_memfd support for device MMIO resources** （cover letter，6/6 个 patch 达到代码量阈值）

- 日期：2026-10-17
- 状态：社区讨论中
- 作者邮箱：Aneesh Kumar K.V <aneesh.kumar@kernel.org>
- 概括：扩展 KVM 客户机内存文件机制支持设备 MMIO 资源，允许 VFIO PCI BAR 作为 PFN 后端提供内存，替代仅 folio 分配方式。新增绑定、获取 PFN、分离等回调，协调 VFIO 设备锁与客户机内存文件转换，限制宿主 BAR 访问和映射，在分离和私有转换时使映射失效。结果：虚拟机可将设备 MMIO 纳入客户机内存文件管理，并支持私有/共享转换。
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
- 概括：让VFIO PCI导出的dma-buf能够向导入方提供点对点DMA提供者信息，使导入方可以判断其点对点流量是否直接到达被导出的PCI BAR；当缓冲区因复位等原因被撤销后不再返回提供者信息，避免导入方继续使用已失效的点对点路径。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260928-fix-p2p-acs-v4-0-v8-17-404453b9c435@nvidia.com/

**▸ 组织：Red Hat**（2 patches）

**[SERIES] vfio/pci: fall back to platform ROM when pci_map_rom() fails** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-10-21
- 状态：社区讨论中
- 作者邮箱：Michael S. Tsirkin <mst@redhat.com>
- 概括：修复 VFIO PCI 设备的 ROM 读取逻辑：当硬件 ROM 资源窗口存在但内容不可读时，原先无法继续尝试平台固件提供的 ROM，现在只要硬件映射失败就会回退读取平台 ROM；并针对部分笔记本 GPU 增加从 ACPI 的 ROM 方法获取视频 BIOS 的最终回退。ACPI 规范虽更偏好该方法，但此处仅作为最后手段，避免破坏既有部署。
- 达到阈值的 patches（1 个，显示前 5）：
  - vfio/pci: read ROM via ACPI _ROM when hardware ROM is unreadable
- 来源：https://patchwork.kernel.org/project/kvm/patch/8ab8fdfe47a8d9c9f10680ddb4a03bccad43f7c5.1792566536.git.mst@redhat.com/

**[SERIES] Enable Qualcomm WiFi PCIe passthrough to VMs** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-10-11
- 状态：社区讨论中
- 作者邮箱：Jose Ignacio Tornos Martinez <jtornosm@redhat.com>
- 概括：为高通 WiFi PCIe 设备透传虚拟机添加支持。高通固件需要物理主机 MSI 地址而非 guest IOVA，新增高通 VFIO PCI 变体驱动，在 PCI 扩展配置空间写入“QMSI”签名缓存主机 MSI 地址数据，虚拟机内驱动发现并使用；同时为 ath11k/ath12k 增加复位后链路恢复重试，解决虚拟化时序变化导致初始化失败。需要 IOMMU 中断重映射和缓存模式配合。
- 达到阈值的 patches（1 个，显示前 5）：
  - vfio/pci: Add qcom-vfio-pci variant driver
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261011074514.515894-3-jtornosm@redhat.com/

**▸ 组织：AMD**（1 patches）

**[RFC] vfio/pci: Block for the upstream bridge lock in vfio_pci_core_disable()**

- 日期：2026-09-08
- 状态：社区讨论中
- 作者邮箱：YuanShang <YuanShang.Mao@amd.com>
- 概括：在SR-IOV等同一上游桥下多个VF并发释放时，VFIO PCI释放路径原先用尝试锁获取桥锁，只有一个功能会执行复位，其余功能可能未复位就交给下一用户且无日志。改为阻塞获取上游桥锁，使桥下多个功能的释放复位按顺序执行，避免未复位设备流出，代价是每个功能拆除时需等待一次功能级复位稳定时间。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260908080946.2235849-1-YuanShang.Mao@amd.com/

**▸ 组织：IBM**（1 patches）

**[v11,5/5] vfio-pci/zdev: Add VFIO FMB device features**

- 日期：2026-10-28
- 状态：社区讨论中
- 作者邮箱：Omar Elghoul <oelghoul@linux.ibm.com>
- 概括：为通过VFIO透传的s390 zPCI设备增加FMB（函数测量块）透传能力，原来用户态无法直接获取FMB数据，现在提供两个设备特性：一个用于启用或禁用FMB，另一个在FMB启用后读取最新测量数据，从而让用户态能够按需控制并读取zPCI设备的功能测量统计。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261028154352.15108-6-oelghoul@linux.ibm.com/

**▸ 组织：归属待核实（baidu.com）**（1 patches）

**vfio/pci: Restore 8-byte ioeventfd support**

- 日期：2026-09-22
- 状态：社区讨论中
- 作者邮箱：Li,Rongqing <lirongqing@baidu.com>
- 概括：此前清理条件编译时误把仅在缺少八字节写入支持时才执行的八字节事件注册拒绝变成了无条件拒绝，导致VFIO PCI的所有八字节事件注册失败。现删除该无条件拒绝，恢复八字节事件通知注册支持，符合原始设计意图。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260922040013.2188-1-lirongqing@baidu.com/

**▸ 组织：Individual Contributor**（1 patches）

**[1/3] vfio/pci: Drain eventfd RCU callbacks on module exit**

- 日期：2026-09-26
- 状态：社区讨论中
- 作者邮箱：Jiale Yao <yaojiale02@163.com>
- 概括：在 vfio-pci 模块卸载场景中，替换事件文件描述符时释放会延迟到 RCU 回调执行，关闭设备后回调仍可能排队，依赖驱动移除后卸载核心模块时回调可能指向已释放的模块代码。现在核心模块退出前等待所有未完成的 RCU 回调，避免回调执行时引用已卸载的模块内存。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260926162554.163197-2-yaojiale02@163.com/

**▸ 组织：Huawei**（1 patches）

**[SERIES] fix two issues in hisi_acc_vfio_pci driver** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-10-13
- 状态：社区讨论中
- 作者邮箱：Longfang Liu <liulongfang@huawei.com>
- 概括：修复华为加速器直通驱动的两个问题：物理功能直通时复位准备路径曾因空指针导致内核崩溃，现在先判断是否支持动态迁移，非迁移设备直接跳过复位协调，并避免复位标志未清除而误释放无关锁；第三代队列管理硬件搭配64KB页时，功能区域与迁移寄存器共享物理页，可能向虚拟机泄漏迁移寄存器，改为探测阶段选择通用直通操作，保留直通但禁用动态迁移。
- 达到阈值的 patches（1 个，显示前 5）：
  - hisi_acc_vfio_pci: reject live migration on 64KB page with QM_HW_V3 hardware
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261013071929.3988687-2-liulongfang@huawei.com/

---

### ◆ 子系统：VFIO Core（12 patches）

**▸ 组织：Individual Contributor**（3 patches）

**[SERIES] vfio/nvgrace-gpu: Separate the fallback-mode open_device** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-10-15
- 状态：社区讨论中
- 作者邮箱：Andrea Parri <parri.andrea@gmail.com>
- 概括：针对英伟达 Grace Hopper GPU 直通设备在 ACPI 内存属性缺失或芯片间高速互连断开时的回退模式，原先打开与关闭路径不对称，会以零长度参数注册地址空间，形成覆盖全范围的区间且不清理，设备重绑后可能触发释放后使用。现在回退模式改用仅执行通用 PCI 核心使能的打开路径，与通用关闭对称，不再触碰 GPU 专用状态；常规路径也去掉零长度判断，无条件初始化模拟寄存器。
- 达到阈值的 patches（1 个，显示前 5）：
  - vfio/nvgrace-gpu: Use a core-only open_device in fallback mode
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261015081937.405320-2-parri.andrea@gmail.com/

**vfio/nvgrace-gpu: Skip PFN registration for empty memory regions**

- 日期：2026-09-25
- 状态：社区讨论中
- 作者邮箱：Andrea Parri <parri.andrea@gmail.com>
- 概括：针对NVIDIA Grace GPU回退模式，原使用内存区长度为零时仍无条件注册页帧号地址空间，残留区间导致二次打开失败、解绑后释放后使用，并错误归类内存失效报告；现在仅在该区域长度非零时才注册和注销，回退模式不再注册任何区域。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260925161024.189771-1-parri.andrea@gmail.com/

**[v2] vfio/type1: avoid walking reserved-only mappings while unpinning**

- 日期：2026-09-19
- 状态：社区讨论中
- 作者邮箱：Sam Crossley <samuelcrossley@gmail.com>
- 概括：GPU直通等场景拆除大型设备直通DMA映射时，如果一个映射只含保留页帧，原先仍会逐页执行无效释放检查，128 GiB保留映射会遍历约3360万个页帧，单次取消映射可让CPU长时间占用并触发软锁定看门狗。现增加非保留页帧标志，只有保留与非保留页帧混合的映射才逐页处理，纯保留映射跳过该遍历，避免无效空操作带来的长时间软锁定。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260919-vfio-v2-1-68e7ed355972@gmail.com/

**▸ 组织：IBM**（2 patches）

**[v6,4/5] vfio/spapr_tce: Normalize EEH IOA error injection addresses**

- 日期：2026-10-23
- 状态：社区讨论中
- 作者邮箱：Narayana Murty N <nnmlinux@linux.ibm.com>
- 概括：在 sPAPR VFIO 的增强型错误处理错误注入接口中，先将用户态传入的目标地址规范化为 PCI/IOA 总线地址，再交给平台固件注入。此前 QEMU 可能传入 Linux 资源地址，而固件期望 PCI 总线地址，会造成注入失败。转换只针对 32/64 位且功能为内存或 IO 读写的错误；配置空间偏移和 DMA 地址保持原样不翻译，零地址零掩码代表无地址注入直接通过。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261023073642.59657-5-nnmlinux@linux.ibm.com/

**[v2] vfio: Use file-based reference counting for KVM**

- 日期：2026-09-03
- 状态：社区讨论中
- 作者邮箱：Steffen Eiden <seiden@linux.ibm.com>
- 概括：将 VFIO 与 KVM 之间的引用计数从手动模块符号引用改为基于文件引用的机制：接口改为传递文件指针，利用内核已有的文件引用计数和释放机制管理生命周期，不再为每个设备保存释放回调，也不再手动维护模块引用。这样简化了 VFIO 与 KVM 集成代码，并移除 KVM 剩余的外部导出符号。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260903-vfio-v2-1-ef4cd4190ae7@linux.ibm.com/

**▸ 组织：NVIDIA**（2 patches）

**[v2,12/12] vfio/nvidia-vgpu: add the Rust VFIO variant driver**

- 日期：2026-10-23
- 状态：社区讨论中
- 作者邮箱：Simon Song <xinmengs@nvidia.com>
- 概括：新增用 Rust 编写的 NVIDIA vGPU VFIO PCI 变体驱动，通过 Nova 核心管理虚拟 GPU 实例：首次打开设备时创建实例，最后一个句柄关闭时释放，暴露被分配的设备和子系统标识，限制第一号基地址寄存器窗口，并协调固件复位与 PCI 复位。该驱动通过 VFIO 覆盖匹配设备；没有可用 Nova vGPU 接口的设备仍使用普通 PCI 直通。构建上与 Nova 核心共享导出符号和元数据。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261023154009.2246627-13-xinmengs@nvidia.com/

**[12/13] vfio/nvidia-vgpu: add the NVIDIA vGPU VFIO variant driver**

- 日期：2026-09-05
- 状态：社区讨论中
- 作者邮箱：Zhi Wang <zhiw@nvidia.com>
- 概括：为 NVIDIA vGPU 虚拟功能新增 VFIO 变体驱动：这类虚拟功能的打开、复位和关闭需要与物理功能侧的 nova-core 驱动协调，新驱动只在通过驱动覆盖方式绑定且确认为虚拟功能时接管设备，将实例生命周期操作委托给 nova-core，同时向用户态呈现固件选择的设备与子系统标识，并按分配配置调整基地址寄存器 1 区域孔径，其余 VFIO 操作复用核心框架。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260905081116.106613-13-zhiw@nvidia.com/

**▸ 组织：Amazon**（2 patches）

**vfio: Create the group chardev outside vfio.group_lock**

- 日期：2026-09-11
- 状态：社区讨论中
- 作者邮箱：Sakac, Pavol <sakacpav@amazon.de>
- 概括：并行设备探测时，VFIO组字符设备的分配、命名和注册原在全局组锁内完成，注册过程中还会发送热插拔事件，导致无关组创建串行化并拉长锁持有时间。现改为无锁分配、命名和构建字符设备，只在组列表上保留身份，热插拔事件延后到发布时发送；删除仍持锁保证名称释放。使字符设备注册不再占用全局锁，减轻并行探测时全局锁争用。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260911-vfopt-s4-v1-0-98ba1d2ef7ab@amazon.de/

**[RFC,8/8] vfio: Opt the group and vfio-dev class devices into staged sysfs**

- 日期：2026-09-11
- 状态：社区讨论中
- 作者邮箱：Sakac, Pavol <sakacpav@amazon.de>
- 概括：在海量VF同时注册的场景下，VFIO组字符设备和VFIO设备类对象在组锁外创建后，并发注册会集中到内核sysfs锁路径上。由于这两类设备不会被驱动匹配、也没有类接口消费者，热插拔事件又在发布后触发，现将其接入分阶段sysfs注册，使目录一次性发布，避免并发VF注册在sysfs锁上形成集中等待。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260911174414.97060-8-sakacpav@amazon.de/

**▸ 组织：ARM**（1 patches）

**[RFC,v2,12/15] vfio: Support VFIO devices that access the CPU MMU**

- 日期：2026-10-15
- 状态：社区讨论中
- 作者邮箱：Ryan Roberts <ryan.roberts@arm.com>
- 概括：为不使用 IOMMU 而通过 CPU 内存管理单元访问内存的物理设备增加 VFIO 支持：新增 CPU MMU 组类型和注册接口，设备仍需属于 IOMMU 组，但打开设备组时不要求绑定容器或 IOMMU，也不要求提供 iommufd 所需的附加回调。这适用于虚拟机管理器为其创建虚拟设备（如设备树或 ACPI 表）的场景，管理器具备设备特定知识，知道无需分配容器，使这类设备能通过 VFIO 暴露。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261015142552.4128028-13-ryan.roberts@arm.com/

**▸ 组织：归属待核实（openai.com）**（1 patches）

**vfio: Publish the container after all fallible initialization**

- 日期：2026-10-30
- 状态：社区讨论中
- 作者邮箱：Kyle Zeng <kylebot@openai.com>
- 概括：修复 VFIO 模块初始化竞态：原先设备节点在初始化完成前发布，并发打开可能在后续初始化失败时获得容器，失败清理不撤销已打开文件，导致文件操作回调指向已释放模块内存，可触发越界读取。现将容器初始化移出组初始化并作为最后一个可能失败的步骤，先注册无 IOMMU 后端再注册杂项设备，保证一旦可打开则初始化不再失败。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261030042337.74512-1-kylebot@openai.com/

**▸ 组织：Google**（1 patches）

**[SERIES] vfio: Add support for platform devices** （cover letter，6/7 个 patch 达到代码量阈值）

- 日期：2026-10-24
- 状态：社区讨论中
- 作者邮箱：Mostafa Saleh <smostafa@google.com>
- 概括：为 kvmtool 虚拟机监视器新增 VFIO 平台设备直通路径，通过新的命令行参数将已绑定 VFIO 平台驱动的设备分配给虚拟机，映射其 MMIO 区域并生成客户机设备树节点；中断处理覆盖边沿触发类型，还可借助用户提供的设备树模板补全兼容字符串等属性，使客户机驱动能够绑定。同时修复同一 IOMMU 组内非首设备打开时的文件描述符泄漏。
- 达到阈值的 patches（6 个，显示前 5）：
  - vfio: Factor out wired IRQ setup and teardown
  - vfio: Support edge-triggered wired IRQs
  - vfio: Add basic support for vfio-platform
  - vfio: Reserve guest address space for VFIO platform
  - vfio: platform: Add interrupts support
  - ... 及其他 1 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261024161902.2093581-2-smostafa@google.com/

---

### ◆ 子系统：VFIO Selftests（3 patches）

**▸ 组织：Google**（3 patches）

**[SERIES] iommu: Introduce Page Table Observability Framework** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-10-01
- 状态：社区讨论中
- 作者邮箱：Pranjal Shrivastava <praan@google.com>
- 概括：引入输入输出内存管理单元页表观测框架，解决全局页表页数无法归因到具体用户的问题。框架按域统计页表页数，使用通用页表库的驱动自动计入；通过文件描述符信息文件新增页数指标，传统虚拟功能输入输出容器和输入输出内存管理文件描述符接口均可向用户空间报告自身页表占用，仅统计支持计数的域，不支持时省略该指标，避免部分计数。自测验证稀疏映射后页表计数增加且解除映射后计数保持，为后续回收提供观测依据。
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio/type1: Expose IO page table usage via fdinfo
  - vfio/selftests: Add observability test for IO page table usage
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261001224531.765278-5-praan@google.com/

**[SERIES] Introduce vfio_dma_mapping_perf_test** （cover letter，3/4 个 patch 达到代码量阈值）

- 日期：2026-09-10
- 状态：社区讨论中
- 作者邮箱：Aaron Lewis <aaronlewis@google.com>
- 概括：为 VFIO 新增 DMA 映射性能测试工具，测量 mmap、DMA 映射、解除映射和 munmap 各阶段延迟，支持 memfd 映射与自定义区域大小。传统通过/失败测试在延迟约束下容易抖动，该工具直接报告各阶段耗时，便于评估不同映射方式（如 IOMMU 文件映射接口）的性能差异。
- 达到阈值的 patches（3 个，显示前 5）：
  - vfio: selftests: Introduce vfio_dma_mapping_perf_test
  - vfio: selftests: Add memfd test to vfio_dma_mapping_perf_test
  - vfio: selftests: Allow a size for vfio_dma_mapping_perf_test
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260910153326.3085937-2-aaronlewis@google.com/

**[v2] vfio: selftests: Add documentation**

- 日期：2026-09-03
- 状态：社区讨论中
- 作者邮箱：David Matlack <dmatlack@google.com>
- 概括：为 VFIO 自测试新增专门文档，说明这类测试作为用户态程序直接操作真实 PCI 设备，通过 VFIO 和 IOMMUFD 接口覆盖功能、回归和性能场景；文档给出设备选择、绑定到 VFIO-PCI 驱动、运行与清理步骤，并介绍辅助库和编写测试的基本结构，帮助内核开发者快速搭建和编写测试。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260903183814.2111748-1-dmatlack@google.com/

---

### ◆ 子系统：VFIO FSL-MC（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[v3] vfio/fsl-mc: prevent read-only region mappings from becoming writable**

- 日期：2026-09-03
- 状态：社区讨论中
- 作者邮箱：Abdifatah Suruur <suruurism@gmail.com>
- 概括：修复 FSL-MC 总线设备经 VFIO 映射时只读区域可被提升为可写的问题：原实现虽然拒绝不带写标志区域的可写映射，但未清除映射的可写潜力位，用户态可先建立只读映射再通过内存保护接口改为可写。现在对这类区域清除可写潜力位，防止升级；由于 FSL-MC 总线当前发布的区域均带写标志，这条路径暂时不会触发，属于防御性加固。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260903092912.444-1-suruurism@gmail.com/

---

### ◆ 子系统：VFIO Platform（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[v4] vfio/platform: prevent read-only region mappings from becoming writable**

- 日期：2026-09-06
- 状态：社区讨论中
- 作者邮箱：Abdifatah Suruur <suruurism@gmail.com>
- 概括：修复 VFIO 平台设备内存映射中只读区域可被提升为可写的问题：原实现对无写标志区域仅拒绝直接可写映射，但保留映射的可写潜力位，用户态可先只读映射再利用内存保护接口升级为可写。现在对这类区域清除可写潜力位，阻止权限提升；当前内置平台驱动都未发布无写标志的区域，因此属于防御性加固。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260906123239.10858-1-suruurism@gmail.com/

---

### ◆ 子系统：VFIO AP (s390)（1 patches）

**▸ 组织：IBM**（1 patches）

**[v6,1/5] s390/vfio-ap: Fix leak of pinned NIB and registered GISC in vfio_ap_irq_enable/disable()**

- 日期：2026-09-04
- 状态：社区讨论中
- 作者邮箱：Anthony Krowiak <akrowiak@linux.ibm.com>
- 概括：针对s390 vfio-ap AP队列中断使能与禁用，原来在禁用中断时可能过早释放固定通知指示字节页并注销客户中断子类，若硬件仍使能中断，后续中断会直接内存访问已释放页造成内存破坏；现在禁用后先轮询确认中断位已清再释放资源，若超时无法确认则保留该页和中断子类不释放，避免野DMA写。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260904093435.1161402-2-akrowiak@linux.ibm.com/

---

### ◆ 子系统：VFIO Migration（1 patches）

**▸ 组织：Kernel.org**（1 patches）

**[RFC,POC,31/50] vfio: install the migration data descriptor when the ioctl returns**

- 日期：2026-09-15
- 状态：社区讨论中
- 作者邮箱：Christian Brauner <brauner@kernel.org>
- 概括：调整VFIO设备迁移状态数据描述符的返回方式：在迁移状态查询接口把文件描述符返回用户态时才安装，后续释放依赖文件描述符退出路径处理；替代原先先预留未用描述符、复制完成后再手动安装的做法，简化复制失败时的清理流程。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260915-work-fd-reserve-unify-folded-v1-31-4d5217d6b246@kernel.org/

---

### ◆ 子系统：VFIO CCW (s390)（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[v1] vfio/ccw: Flush notoper_work before returning from reset**

- 日期：2026-09-22
- 状态：社区讨论中
- 作者邮箱：Yuho Choi <oss.patchbox@gmail.com>
- 概括：针对 s390 上的 VFIO ccw 设备，原先在 DMA 解映射回调中进行复位时，如果子通道无法禁用或静止，关闭流程只排队异步工作来释放通道程序页，回调可能在页面仍被钉住时返回，使 DMA 解映射重试耗尽并可能触发主机崩溃。现在复位发送关闭事件后等待该异步工作完成，确保页面在返回前解钉，正常路径不受影响。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260922164928.477669-1-oss.patchbox@gmail.com/

---

### ◆ 子系统：VFIO CDEV（1 patches）

**▸ 组织：NVIDIA**（1 patches）

**[SERIES] vfio: Fix cdev second-open and harden selftests** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-09-11
- 状态：社区讨论中
- 作者邮箱：Alex Williamson <alex.williamson@nvidia.com>
- 概括：修复 VFIO 字符设备第二次绑定在修改共享状态前才检查单打开限制的问题：原先第二次绑定先更新设备令牌和 KVM 关联，随后才被拒绝，错误路径可能破坏当前打开者的令牌和 KVM 引用。现将单打开检查提前到绑定操作开始处并返回忙碌，使无法完成的绑定不触碰现有状态；同时增加自测试验证失败第二次打开不破坏令牌，并延长相关测试超时。
- 达到阈值的 patches（1 个，显示前 5）：
  - vfio: Reject a second cdev open before mutating shared device state
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260911170429.1642480-2-alex.williamson@nvidia.com/

---

### ◆ 子系统：VFIO CDX（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[SERIES] vfio: mmap()/mprotect() hygiene for MMIO region mappings** （cover letter，5/5 个 patch 达到代码量阈值）

- 日期：2026-09-29
- 状态：社区讨论中
- 作者邮箱：Abdifatah Suruur <suruurism@gmail.com>
- 概括：修复 VFIO 平台、fsl-mc 和 cdx 的 MMIO 区域映射卫生问题：原先只读区域映射仍保留可写许可，用户态可通过内存保护升级为可写；映射偏移可能被物理帧号覆盖，破坏区间树键，未来撤销映射可能失效；cdx 还接受私有映射，写时复制路径会重新引入偏移覆盖。现清除只读区域的可写许可，保留逻辑偏移并要求共享映射，作为防御性修复。
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
- 状态：社区讨论中
- 作者邮箱：Jason Gunthorpe <jgg@nvidia.com>
- 概括：为 VFIO 自测试框架新增 mlx5 网络设备驱动支持，覆盖 ConnectX 设备的硬件初始化、命令接口、DMA 数据路径和 MSI 中断触发，可执行数据搬运等 DMA 测试；同时调整框架允许各驱动声明所需区域大小，补充调试输出，并整理 mlx5 IFC 定义和字段访问宏供自测试驱动使用。
- 达到阈值的 patches（3 个，显示前 5）：
  - vfio: selftests: mlx5 driver - add send_msi support
  - vfio: selftests: Add mlx5 driver - data path and memcpy ops
  - vfio: selftests: Add mlx5 driver - HW init and command interface
- 来源：https://patchwork.kernel.org/project/kvm/patch/7-v7-c6d30e8ce1e4+3dfa6-mlx5st_jgg@nvidia.com/

---

### ◆ 子系统：VFIO IOMMUFD（1 patches）

**▸ 组织：Kernel.org**（1 patches）

**[SERIES] iommufd: Infrastructure for vIOMMU creation for confidential guests and guest TSM requests** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-09-17
- 状态：社区讨论中
- 作者邮箱：Aneesh Kumar K.V <aneesh.kumar@kernel.org>
- 概括：为机密 guest 环境构建 vIOMMU 创建和 guest TSM 请求基础设施。VFIO 改为缓存 KVM VM 文件引用，iommufd 关联 KVM 文件，增加 vIOMMU provider 注册与外部实现查找，新增 vdevice 的 TSM 请求命令转发 guest 请求，移除旧的 PCI/TSM 接口并引入引用计数上下文。结果：外部 TSM 实现可以统一处理 guest 请求，VM 和设备生命周期更清晰。
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio: cache KVM VM file references instead of raw struct kvm pointers
  - vfio: cdev: Reject duplicate bind before updating KVM file
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260917140159.1163281-2-aneesh.kumar@kernel.org/

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

*报告由 Linux Patches Tracker 自动生成 | 2026-11-11 12:57:07*
