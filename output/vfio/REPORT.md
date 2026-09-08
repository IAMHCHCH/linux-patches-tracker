# Linux VFIO 子系统 Patch 追踪报告

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
| 社区讨论中 | 24 | 100.0% |
| 已合入 | 0 | 0.0% |
| **总计** | **24** | **100%** |

### 按组织分类（TOP 15）

| 组织 | 数量 | 占比 |
|------|------|------|
| Google | 8 | 33.3% |
| IBM | 6 | 25.0% |
| Individual Contributor | 4 | 16.7% |
| NVIDIA | 4 | 16.7% |
| Huawei | 2 | 8.3% |

### 按子系统分类

| 子系统 | 数量 | 占比 |
|--------|------|------|
| VFIO PCI | 10 | 41.7% |
| VFIO Core | 3 | 12.5% |
| VFIO Selftests | 3 | 12.5% |
| VFIO IOMMUFD | 2 | 8.3% |
| VFIO CCW (s390) | 2 | 8.3% |
| VFIO Migration | 1 | 4.2% |
| VFIO CDX | 1 | 4.2% |
| VFIO AP (s390) | 1 | 4.2% |
| VFIO MLX5 Variant | 1 | 4.2% |

## 重点 Patch Top20 清单

### 已合入

暂无。

### 社区讨论

| 厂商 | 简介 |
|------|------|
| NVIDIA | [PATCH v4 00/27] vfio/pci: Add CXL Type-2 device passthrough support ------为 vfio/pci 新增 CXL Type-2 设备直通支持，引入 cxl 函数级 reset 接口、CXL ops 注册与 vfio-cxl 模块装载；该模块接管组件寄存器 BAR，虚拟化 CXL DVSEC 和 HDM decoder 寄存器，模拟 decoder commit 握手，在 reset/电源切换时撤销 HDM 映射。 |
| Huawei | [PATCH v19 00/18] vfio/pci: Add PCIe TPH support ------该系列围绕 vfio/pci: Add PCIe TPH support，具体包括隐藏 TPH capability（当设备不支持 TPH 时）、虚拟化 PCIe TPH capability registers、实现 TPH_ST feature for batch ST table programming。 |
| Google | [PATCH v5 00/20] vfio/pci: Base Live Update support for VFIO ------为 VFIO 设备文件加入基础 Live Update 支持：vfio-pci 注册文件处理器到 Live Update Orchestrator，使设备文件在 kexec 后保留，借助新增 vfio_find_device()/cdev 打开 API 和 LIVEUPDATE_SESSION_RETRIEVE_FD 会话检索保留设备。 |
| IBM | [PATCH v9 00/10] s390/vfio_ccw fixes ------该系列围绕 s390/vfio_ccw fixes，具体包括限制 channel program segment 数量、free all memory if cp_init() fails、修复 out of bounds check on CCW array、确保 读写 region 索引在范围内、实现 a crw lock。 |
| Individual Contributor | [PATCH v5 00/9] vfio/pci: Add mmap() for DMABUFs ------在 vfio/pci 中把 BAR mmap 重构为基于 DMABUF：增加 PFN 查找和 DMABUF 创建辅助函数，为 BAR 映射提供用户可见名称，新增对 VFIO DMABUF 的 mmap 入口，并重新梳理 BAR zap/revocation，支持按请求永久撤销 DMABUF。 |
| Huawei | [PATCH v3 00/3] hisi_acc_vfio_pci: fix three driver issues ------在 hisi_acc_vfio_pci 驱动中修复三处错误：PF passthrough 时更正 live migration 启用判定，QM_HW_V3 硬件在 64KB 页大小下拒绝启用 live migration，并在设备 reset 完成后清除 set_reset_flag。 |
| IBM | [PATCH v1 00/23] s390/vfio_ccw: Free all memory if cp_init() fails ------在 s390/vfio_ccw 中集中修正通道程序处理问题，重点保证 cp_init() 失败时释放所有已分配内存，其余修改包括限制通道程序段数、按 IDAW 类型计算 IDAL 长度、取消遗留工作队列、把 cp 清理移出 not operational、校验读写 region 索引范围、选择性扩大 io_mutex、修复 CCW 数组越界。 |
| NVIDIA | [PATCH v4 00/10] mlx5 support for VFIO self test ------为VFIO自测框架添加mlx5驱动支持，包括允许驱动指定所需region大小、新增dev_dbg调试、实现数据路径与memcpy ops、send_msi支持以及硬件初始化和命令接口。 |
| Google | [PATCH v2 00/4] Introduce vfio_dma_mapping_perf_test ------该系列围绕 Introduce vfio_dma_mapping_perf_test，具体包括vfio: selftests 中引入 vfio_dma_mapping_perf_test、vfio: selftests 中新增 memfd test to vfio_dma_mapping_perf_test。 |
| Google | [PATCH v4 00/9] vfio: selftests: Add driver for Intel Ethernet Gigabit Controller (IGB) ------为 vfio 自测引入 Intel IGB QEMU 设备驱动，使用高级 TX/RX 描述符，编程 MSI-X 中断路由，延长 memcpy 完成超时并禁用 PCIe completion timeout retries 以适配线速硬件。 |
| Google | [PATCH v4 00/18] iommu: Add live update state preservation ------为iommufd新增preserve/unpreserve API，使vfio cdev在live update期间能保留并恢复iommufd状态，vfio/pci据此在设备状态迁移时保存对应iommufd上下文。 |
| NVIDIA | [PATCH v1 00/5] PCI/vfio-pci: Guard resets against active SR-IOV VFs ------在vfio/pci中拒绝重置仍启用了VFs的SR-IOV PF，并用pci_reset_supported()替换reset_works判断，防止在活动VF存在时触发不安全重置。 |
| IBM | [v5,1/4] s390/vfio-ap: Fix leak of pinned NIB and registered NISC in vfio_ap_irq_enable/disable() ------在 s390/vfio-ap 中修复 vfio_ap_irq_enable/disable() 中 pinned NIB 和 registered NISC 泄漏。 |
| Individual Contributor | [v4,10/10] vfio/pci: Add mmap() attributes to DMABUF feature ------在vfio/pci的DMABUF特性中添加mmap()属性支持，允许用户态对导出的DMABUF执行内存映射操作。 |
| NVIDIA | [rdma-next,09/15] vfio/mlx5: Enable relaxed ordering on the live migration data mkey ------在vfio/mlx5驱动的live migration数据mkey上启用relaxed ordering，以优化迁移期间内存访问顺序与性能。 |
| Google | [v8,2/6] vfio: selftests: igb: Use PHY internal loopback on 82576 ------在vfio selftests的igb用例中，对82576网卡改用PHY内部回环模式执行环回测试。 |
| IBM | [v7,01/23] vfio: Use file-based reference counting for KVM ------在 vfio 核心代码中，将原来对 KVM 对象采用直接持有 struct kvm 指针引用计数的方式，改为在 vfio_group 与 KVM 关联时通过获取 KVM 文件描述符的 struct file 引用（fdget/kvm_destroy）来管理生命周期，使用基于文件的引用计数确保 KVM 在 vfio 使用期间不被释放。 |
| IBM | [v4,01/27] VFIO: take reference to the KVM module ------在 VFIO 与 KVM 交互路径中，在 vfio 设备初始化和释放时调用 try_module_get/module_put 来获取并释放 KVM 内核模块的引用，防止 VFIO 持有 KVM 相关指针时 KVM 模块被卸载，从而避免调用已卸载模块代码导致崩溃。 |
| Individual Contributor | [PATCH] vfio/cdx: prevent read-only region mappings from becoming writable ------在 vfio/cdx 驱动的 region 映射处理中，当用户通过 mmap 建立 VMA 时检查 region 的只读属性，若 region 声明为只读，则清除 VMA 的 VMA_WRITE 标志并拒绝后续通过写映射改变只读区域，确保只读区域不会被映射成可写。 |
| Google | [RFC,v1,1/1] vfio/pci: Revoke BARs and DMABUFs during sysfs-triggered PCI reset ------在 vfio/pci 实现中，当用户通过 sysfs 触发设备 reset 时，在设备复位前遍历并 zapping 所有被映射的 PCI BAR 区间（vma_pages）和 DMA-BUF 映射，通过 invalidate 使已建立的映射失效，防止 reset 期间或之后 guest 访问到已失效的 BAR/DMABUF 数据。 |

---

## 已合入 Patches

暂无。

## 社区讨论中 Patches

### ◆ 子系统：VFIO PCI（10 patches）

**▸ 组织：Google**（3 patches）

**[RFC,v1,1/1] vfio/pci: Revoke BARs and DMABUFs during sysfs-triggered PCI reset**

- 日期：2026-08-07
- 状态：社区讨论中
- 概括：在 vfio/pci 实现中，当用户通过 sysfs 触发设备 reset 时，在设备复位前遍历并 zapping 所有被映射的 PCI BAR 区间（vma_pages）和 DMA-BUF 映射，通过 invalidate 使已建立的映射失效，防止 reset 期间或之后 guest 访问到已失效的 BAR/DMABUF 数据。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260807201405.3717430-2-praan@google.com/

**[RFC,1/1] vfio/pci: Disable sriov on PF device close**

- 日期：2026-08-05
- 状态：社区讨论中
- 概括：在 vfio/pci 中禁用 sriov on PF device close。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260805003355.728299-2-skhawaja@google.com/

**[SERIES] vfio/pci: Base Live Update support for VFIO** （cover letter，7/18 个 patch 达到代码量阈值）

- 日期：2026-07-14
- 状态：社区讨论中
- 概括：为 VFIO 设备文件加入基础 Live Update 支持：vfio-pci 注册文件处理器到 Live Update Orchestrator，使设备文件在 kexec 后保留，借助新增 vfio_find_device()/cdev 打开 API 和 LIVEUPDATE_SESSION_RETRIEVE_FD 会话检索保留设备。
- 达到阈值的 patches（7 个，显示前 5）：
  - vfio/pci: Factor out the reset logic in VFIO PCI device close path
  - vfio: Export various helpers from VFIO
  - vfio/pci: Export vfio_pci_dma_buf_move for vfio-pci module
  - vfio/pci: Register a file handler with Live Update Orchestrator
  - vfio/pci: Preserve vfio-pci device files across Live Update
  - ... 及其他 2 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260714151505.3466855-2-vipinsh@google.com/

**▸ 组织：Individual Contributor**（2 patches）

**[SERIES] vfio/pci: Add mmap() for DMABUFs** （cover letter，7/7 个 patch 达到代码量阈值）

- 日期：2026-07-15
- 状态：社区讨论中
- 概括：在 vfio/pci 中把 BAR mmap 重构为基于 DMABUF：增加 PFN 查找和 DMABUF 创建辅助函数，为 BAR 映射提供用户可见名称，新增对 VFIO DMABUF 的 mmap 入口，并重新梳理 BAR zap/revocation，支持按请求永久撤销 DMABUF。
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
- 概括：在vfio/pci的DMABUF特性中添加mmap()属性支持，允许用户态对导出的DMABUF执行内存映射操作。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260701171245.90111-11-matt@ozlabs.org/

**▸ 组织：Huawei**（2 patches）

**[SERIES] hisi_acc_vfio_pci: fix three driver issues** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-08-31
- 状态：社区讨论中
- 概括：在 hisi_acc_vfio_pci 驱动中修复三处错误：PF passthrough 时更正 live migration 启用判定，QM_HW_V3 硬件在 64KB 页大小下拒绝启用 live migration，并在设备 reset 完成后清除 set_reset_flag。
- 达到阈值的 patches（2 个，显示前 5）：
  - hisi_acc_vfio_pci: reject live migration on 64KB page with QM_HW_V3 hardware
  - hisi_acc_vfio_pci: clear set_reset_flag after reset completed
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260831090951.844569-2-liulongfang@huawei.com/

**[SERIES] vfio/pci: Add PCIe TPH support** （cover letter，4/10 个 patch 达到代码量阈值）

- 日期：2026-07-02
- 状态：社区讨论中
- 概括：该系列围绕 vfio/pci: Add PCIe TPH support，具体包括隐藏 TPH capability（当设备不支持 TPH 时）、虚拟化 PCIe TPH capability registers、实现 TPH_ST feature for batch ST table programming。
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
- 概括：为 vfio/pci 新增 CXL Type-2 设备直通支持，引入 cxl 函数级 reset 接口、CXL ops 注册与 vfio-cxl 模块装载；该模块接管组件寄存器 BAR，虚拟化 CXL DVSEC 和 HDM decoder 寄存器，模拟 decoder commit 握手，在 reset/电源切换时撤销 HDM 映射。
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
- 概括：在vfio/pci中拒绝重置仍启用了VFs的SR-IOV PF，并用pci_reset_supported()替换reset_works判断，防止在活动VF存在时触发不安全重置。
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio/pci: Refuse to reset an SR-IOV PF with enabled VFs
  - vfio/pci: Use pci_reset_supported() in place of reset_works
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260812045325.2733631-4-alex.williamson@nvidia.com/

**▸ 组织：IBM**（1 patches）

**[v1] vfio/pci: Avoid mapping BARs for devices with non-mappable BARs**

- 日期：2026-07-29
- 状态：社区讨论中
- 概括：在 vfio/pci 中避免 mapping BARs for devices（携带 non-mappable BARs）。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260729181116.1373-1-alifm@linux.ibm.com/

---

### ◆ 子系统：VFIO Core（3 patches）

**▸ 组织：IBM**（2 patches）

**[v7,01/23] vfio: Use file-based reference counting for KVM**

- 日期：2026-08-31
- 状态：社区讨论中
- 概括：在 vfio 核心代码中，将原来对 KVM 对象采用直接持有 struct kvm 指针引用计数的方式，改为在 vfio_group 与 KVM 关联时通过获取 KVM 文件描述符的 struct file 引用（fdget/kvm_destroy）来管理生命周期，使用基于文件的引用计数确保 KVM 在 vfio 使用期间不被释放。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260831144802.834315-2-seiden@linux.ibm.com/

**[v4,01/27] VFIO: take reference to the KVM module**

- 日期：2026-07-06
- 状态：社区讨论中
- 概括：在 VFIO 与 KVM 交互路径中，在 vfio 设备初始化和释放时调用 try_module_get/module_put 来获取并释放 KVM 内核模块的引用，防止 VFIO 持有 KVM 相关指针时 KVM 模块被卸载，从而避免调用已卸载模块代码导致崩溃。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260706085229.979525-2-seiden@linux.ibm.com/

**▸ 组织：Individual Contributor**（1 patches）

**vfio/type1: conditional rescheduling while unpinning**

- 日期：2026-07-23
- 状态：社区讨论中
- 概括：在 vfio/type1 中按条件执行 rescheduling while unpinning。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260723-vfio-v1-1-3b59579916c6@gmail.com/

---

### ◆ 子系统：VFIO Selftests（3 patches）

**▸ 组织：Google**（3 patches）

**[SERIES] Introduce vfio_dma_mapping_perf_test** （cover letter，3/4 个 patch 达到代码量阈值）

- 日期：2026-08-04
- 状态：社区讨论中
- 概括：该系列围绕 Introduce vfio_dma_mapping_perf_test，具体包括vfio: selftests 中引入 vfio_dma_mapping_perf_test、vfio: selftests 中新增 memfd test to vfio_dma_mapping_perf_test。
- 达到阈值的 patches（3 个，显示前 5）：
  - vfio: selftests: Introduce vfio_dma_mapping_perf_test
  - vfio: selftests: Add memfd test to vfio_dma_mapping_perf_test
  - vfio: selftests: Allow a size for vfio_dma_mapping_perf_test
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260804165748.1060476-3-aaronlewis@google.com/

**[v8,2/6] vfio: selftests: igb: Use PHY internal loopback on 82576**

- 日期：2026-07-29
- 状态：社区讨论中
- 概括：在vfio selftests的igb用例中，对82576网卡改用PHY内部回环模式执行环回测试。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260729-igb_v3_b4-v8-2-3ed236272b4e@google.com/

**[SERIES] vfio: selftests: Add driver for Intel Ethernet Gigabit Controller (IGB)** （cover letter，2/5 个 patch 达到代码量阈值）

- 日期：2026-07-10
- 状态：社区讨论中
- 概括：为 vfio 自测引入 Intel IGB QEMU 设备驱动，使用高级 TX/RX 描述符，编程 MSI-X 中断路由，延长 memcpy 完成超时并禁用 PCIe completion timeout retries 以适配线速硬件。
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio: selftests: igb: Add driver for IGB QEMU device
  - vfio: selftests: igb: Disable PCIe completion timeout retries
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260710-igb_v3_b4-v4-1-56e7e2576cc1@google.com/

---

### ◆ 子系统：VFIO IOMMUFD（2 patches）

**▸ 组织：Google**（2 patches）

**[SERIES] iommu: Add live update state preservation** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-08
- 状态：社区讨论中
- 概括：为iommufd新增preserve/unpreserve API，使vfio cdev在live update期间能保留并恢复iommufd状态，vfio/pci据此在设备状态迁移时保存对应iommufd上下文。
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio/pci: Preserve the iommufd state of the vfio cdev
  - iommufd: Add APIs to preserve/unpreserve a vfio cdev
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260808022723.3893618-18-skhawaja@google.com/

**[1/2] vfio/type1: Periodically try rescheduling when unmapping**

- 日期：2026-07-14
- 状态：社区讨论中
- 概括：在 vfio/type1 中周期性尝试 rescheduling（当 unmapping 时）。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260714210303.3967981-2-aaronlewis@google.com/

---

### ◆ 子系统：VFIO CCW (s390)（2 patches）

**▸ 组织：IBM**（2 patches）

**[SERIES] s390/vfio_ccw: Free all memory if cp_init() fails** （cover letter，6/10 个 patch 达到代码量阈值）

- 日期：2026-08-03
- 状态：社区讨论中
- 概括：在 s390/vfio_ccw 中集中修正通道程序处理问题，重点保证 cp_init() 失败时释放所有已分配内存，其余修改包括限制通道程序段数、按 IDAW 类型计算 IDAL 长度、取消遗留工作队列、把 cp 清理移出 not operational、校验读写 region 索引范围、选择性扩大 io_mutex、修复 CCW 数组越界。
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
- 概括：该系列围绕 s390/vfio_ccw fixes，具体包括限制 channel program segment 数量、free all memory if cp_init() fails、修复 out of bounds check on CCW array、确保 读写 region 索引在范围内、实现 a crw lock。
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
- 概括：在vfio/mlx5驱动的live migration数据mkey上启用relaxed ordering，以优化迁移期间内存访问顺序与性能。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260726092943.2880176-10-michaelgur@nvidia.com/

---

### ◆ 子系统：VFIO CDX（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**vfio/cdx: prevent read-only region mappings from becoming writable**

- 日期：2026-08-19
- 状态：社区讨论中
- 概括：在 vfio/cdx 驱动的 region 映射处理中，当用户通过 mmap 建立 VMA 时检查 region 的只读属性，若 region 声明为只读，则清除 VMA 的 VMA_WRITE 标志并拒绝后续通过写映射改变只读区域，确保只读区域不会被映射成可写。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260819083943.1391-1-suruurism@gmail.com/

---

### ◆ 子系统：VFIO AP (s390)（1 patches）

**▸ 组织：IBM**（1 patches）

**[v5,1/4] s390/vfio-ap: Fix leak of pinned NIB and registered NISC in vfio_ap_irq_enable/disable()**

- 日期：2026-08-31
- 状态：社区讨论中
- 概括：在 s390/vfio-ap 中修复 vfio_ap_irq_enable/disable() 中 pinned NIB 和 registered NISC 泄漏。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260831171443.222225-2-akrowiak@linux.ibm.com/

---

### ◆ 子系统：VFIO MLX5 Variant（1 patches）

**▸ 组织：NVIDIA**（1 patches）

**[SERIES] mlx5 support for VFIO self test** （cover letter，3/5 个 patch 达到代码量阈值）

- 日期：2026-08-12
- 状态：社区讨论中
- 概括：为VFIO自测框架添加mlx5驱动支持，包括允许驱动指定所需region大小、新增dev_dbg调试、实现数据路径与memcpy ops、send_msi支持以及硬件初始化和命令接口。
- 达到阈值的 patches（3 个，显示前 5）：
  - vfio: selftests: Add mlx5 driver - data path and memcpy ops
  - vfio: selftests: mlx5 driver - add send_msi support
  - vfio: selftests: Add mlx5 driver - HW init and command interface
- 来源：https://patchwork.kernel.org/project/kvm/patch/6-v4-021df3fb5a3f+98e-mlx5st_jgg@nvidia.com/

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

*报告由 Linux Patches Tracker 自动生成 | 2026-09-08 19:16:32*
