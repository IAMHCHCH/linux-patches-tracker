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
| NVIDIA | [PATCH v4 00/27] vfio/pci: Add CXL Type-2 device passthrough support ------在 vfio/pci 中加入 CXL Type-2 直通支持：通过 PCI_DVSEC_CXL_CAP 的 CACHE_CAPABLE/MEM_CAPABLE 识别 Type-2 设备并加载 vfio-cxl，vfio_cxl_init_device() 拒绝 decoder_count 非 1、interleave_ways 非 1 及无 cxl_reset_capable() 的拓扑。 |
| Google | [PATCH v5 00/20] vfio/pci: Base Live Update support for VFIO ------为 vfio-pci 接入 Live Update 基础机制：注册 live update 文件处理器，在设备冻结时阻止 MMIO/配置访问，保存并恢复 vfio cdev 与 iommufd 状态，让设备节点可跨更新保留。 |
| Individual Contributor | [PATCH v5 00/9] vfio/pci: Add mmap() for DMABUFs ------在 vfio/pci 中为 BAR-map VMA 引入 DMABUF 映射机制：新增 vfio_pci_dma_buf_find_pfn() 与 vfio_pci_dmabuf_export()，使 VFIO 设备 fd 的 mmap() 通过 DMABUF 持有 vfio_device 注册引用，并在 DMABUF 被 revoke 时撤销对应 BAR VMA。 |
| Huawei | [PATCH v19 00/18] vfio/pci: Add PCIe TPH support ------在 vfio/pci 中虚拟化 PCIe TPH capability 与 ST 表访问权限，新增 TPH_ST/DMA_BUF_TPH 设备特性和 IV-ST/NO-ST 策略控制，并在设备启停和 reset 路径同步硬件 TPH 状态。 |
| IBM | [PATCH v9 00/10] s390/vfio_ccw fixes ------在 s390/vfio_ccw 中限制单个通道程序的 ccwchain 数量为 CCWCHAIN_COUNT_MAX(16)；对 async/chp 读/写 region 索引增加 num_regions 边界检查并用 array_index_nospec 防错；在 get_guest_idal() 中校验首 IDAW 等于 cp->guest_iova，否则返回 -EINVAL。 |
| Huawei | [PATCH v20 00/16] vfio/pci: Add PCIe TPH support ------在 vfio/pci 中虚拟化 PCIe TPH capability 与 ST 表访问权限，新增 TPH_ST/DMA_BUF_TPH 设备特性和 IV-ST/NO-ST 策略控制，并在设备启停和 reset 路径同步硬件 TPH 状态。 |
| Huawei | [PATCH v3 00/3] hisi_acc_vfio_pci: fix three driver issues ------hisi_acc_vfio_pci 驱动修复：在 QM_HW_V3 且为 HW_ACC_MIG_VF_CTRL 模式时，若 BAR2 功能寄存器长度（pci_resource_len >> 1）小于 PAGE_SIZE（如 host 页 64KB），则在 hisi_acc_vf_qm_init() 中返回 -EINVAL 拒绝启用迁移。 |
| NVIDIA | [PATCH v4 00/10] mlx5 support for VFIO self test ------在 VFIO selftests 中新增 mlx5 用户态测试驱动，通过 BAR0 命令接口创建 PD/MR/QP/CQ/EQ 等对象，分配 DMA 缓冲区并用 RDMA WRITE 自环回验证设备 DMA 路径。 |
| Google | [PATCH v2 00/4] Introduce vfio_dma_mapping_perf_test ------在 VFIO selftests 中新增 vfio_dma_mapping_perf_test，用可配置映射大小和 memfd 场景测量 VFIO DMA map/unmap 性能，并断言 iommu_unmap() 后 region 已正确解除映射。 |
| Google | [PATCH v4 00/18] iommu: Add live update state preservation ------在 vfio_pci 的 VFIO_DEVICE_ATTACH_PT/DETACH_PT 及 iommufd 的 iommufd_hw_pagetable_attach() 中加入 iommufd_device_is_preserved() 检查，已进入 live update 保留状态的设备直接返回 -EBUSY。 |
| Google | [PATCH v4 00/9] vfio: selftests: Add driver for Intel Ethernet Gigabit Controller (IGB) ------在 tools/testing/selftests/vfio/lib/drivers/igb 下加入 IGB 的设备驱动，通过符号链接复用内核 e1000_82575.h/e1000_defines.h/e1000_regs.h，并在 igb_init() 中清除 E1000_GCR 的 E1000_GCR_CMPL_TMOUT_RESEND 位，关闭 PCIe completion timeout 重发。 |
| NVIDIA | [PATCH v1 00/5] PCI/vfio-pci: Guard resets against active SR-IOV VFs ------在 vfio_pci_core 中以 vdev->pdev 调用 pci_reset_supported() 取代原 vdev->reset_works 标志判断；对 vfio_pci_dev_set_hot_reset() 和 vfio_pci_dev_set_try_reset() 改用 pci_reset_bus_cond()，并新增 vfio_pci_dev_has_vfs() 回调。 |
| IBM | [v5,1/4] s390/vfio-ap: Fix leak of pinned NIB and registered NISC in vfio_ap_irq_enable/disable() ------在 s390 vfio_ap 的 vfio_ap_irq_disable() 中引入 vfio_ap_wait_for_irqstate()，将通过 TAPQ 轮询 IR bit 从仅等待清除扩展为可等待 enabled/disabled 两种状态；当 AQIC 返回 NORMAL 但 IR bit 超时未转为 disabled 时，清零 status 并伪造 OTHERWISE_CHANGED 返回给 guest。 |
| Google | [v10,2/3] vfio: selftests: igb: Add driver for Intel 82576 device ------在 tools/testing/selftests/vfio/lib/drivers/igb/ 下新增面向 Intel 82576 (0x10C9) 的 igb 测试驱动，通过符号链接复用 kernel igb 驱动的 e1000_82575.h/e1000_defines.h/e1000_regs.h。 |
| Individual Contributor | [v4,10/10] vfio/pci: Add mmap() attributes to DMABUF feature ------扩展 VFIO DMA_BUF feature 的 mmap 属性 UAPI，新增 VFIO_DEVICE_FEATURE_DMA_BUF_MEMATTR 结构用于设置 BAR 映射的内存属性，让用户态能显式控制 DMABUF mmap 行为。 |
| NVIDIA | [rdma-next,09/15] vfio/mlx5: Enable relaxed ordering on the live migration data mkey ------在 mlx5 vfio 驱动中为 alloc_mkey_in() 增加 mdev 参数，对 live migration data buffer 与 QP recv resources 创建的 mkey 调用 mlx5_core_mkey_set_relaxed_ordering()，使这些 mkey 启用 relaxed ordering。 |

---

## 已合入 Patches

暂无。

## 社区讨论中 Patches

### ◆ 子系统：VFIO PCI（10 patches）

**▸ 组织：Google**（3 patches）

**[RFC,v1,1/1] vfio/pci: Revoke BARs and DMABUFs during sysfs-triggered PCI reset**

- 日期：2026-08-07
- 状态：社区讨论中
- 概括：在 vfio/pci 中撤销 BARs and DMABUFs（在 sysfs-triggered PCI reset 期间）。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260807201405.3717430-2-praan@google.com/

**[RFC,1/1] vfio/pci: Disable sriov on PF device close**

- 日期：2026-08-05
- 状态：社区讨论中
- 概括：在 vfio/pci 中禁用 sriov on PF device close。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260805003355.728299-2-skhawaja@google.com/

**[SERIES] vfio/pci: Base Live Update support for VFIO** （cover letter，7/18 个 patch 达到代码量阈值）

- 日期：2026-07-14
- 状态：社区讨论中
- 概括：为 vfio-pci 接入 Live Update 基础机制：注册 live update 文件处理器，在设备冻结时阻止 MMIO/配置访问，保存并恢复 vfio cdev 与 iommufd 状态，让设备节点可跨更新保留。
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
- 概括：新增用于查找 DMABUF 的 PFN 的 helper、新增用于创建 DMABUF for a BAR-map VMA 的 helper、将 BAR mmap() 改为使用 DMABUF、提供 BAR 映射的用户可见名称，并清理 BAR zap and revocation。
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
- 概括：扩展 VFIO DMA_BUF feature 的 mmap 属性 UAPI，新增 VFIO_DEVICE_FEATURE_DMA_BUF_MEMATTR 结构用于设置 BAR 映射的内存属性，让用户态能显式控制 DMABUF mmap 行为。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260701171245.90111-11-matt@ozlabs.org/

**▸ 组织：Huawei**（2 patches）

**[SERIES] hisi_acc_vfio_pci: fix three driver issues** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-08-31
- 状态：社区讨论中
- 概括：修复 live migration enable conditions for PF passthrough、拒绝 QM_HW_V3 硬件在 64KB 页配置下执行 live migration，并清除 set_reset_flag（在 reset completed 后）。
- 达到阈值的 patches（2 个，显示前 5）：
  - hisi_acc_vfio_pci: reject live migration on 64KB page with QM_HW_V3 hardware
  - hisi_acc_vfio_pci: clear set_reset_flag after reset completed
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260831090951.844569-2-liulongfang@huawei.com/

**[SERIES] vfio/pci: Add PCIe TPH support** （cover letter，4/10 个 patch 达到代码量阈值）

- 日期：2026-07-02
- 状态：社区讨论中
- 概括：在 vfio/pci 中虚拟化 PCIe TPH capability 与 ST 表访问权限，新增 TPH_ST/DMA_BUF_TPH 设备特性和 IV-ST/NO-ST 策略控制，并在设备启停和 reset 路径同步硬件 TPH 状态。
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
- 概括：新增 a function-scoped reset entry for vfio-pci、新增 CXL ops registration interface、vfio/cxl 中新增 the vfio-cxl module skeleton、vfio/cxl 中绑定时创建 CXL memory device，并检测 CXL devices 并按需加载 vfio-cxl。
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
- 概括：vfio/pci 中拒绝重置仍启用 VF 的 SR-IOV PF，并vfio/pci 中用 pci_reset_supported() 替代 reset_works。
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
- 概括：在 vfio 中为 KVM 改用基于文件的引用计数。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260831144802.834315-2-seiden@linux.ibm.com/

**[v4,01/27] VFIO: take reference to the KVM module**

- 日期：2026-07-06
- 状态：社区讨论中
- 概括：在 VFIO 中获取 KVM 模块引用。
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
- 概括：在 VFIO selftests 中新增 vfio_dma_mapping_perf_test，用可配置映射大小和 memfd 场景测量 VFIO DMA map/unmap 性能，并断言 iommu_unmap() 后 region 已正确解除映射。
- 达到阈值的 patches（3 个，显示前 5）：
  - vfio: selftests: Introduce vfio_dma_mapping_perf_test
  - vfio: selftests: Add memfd test to vfio_dma_mapping_perf_test
  - vfio: selftests: Allow a size for vfio_dma_mapping_perf_test
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260804165748.1060476-3-aaronlewis@google.com/

**[v8,2/6] vfio: selftests: igb: Use PHY internal loopback on 82576**

- 日期：2026-07-29
- 状态：社区讨论中
- 概括：在 vfio: selftests: igb 中在 82576 上改用 PHY internal loopback。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260729-igb_v3_b4-v8-2-3ed236272b4e@google.com/

**[SERIES] vfio: selftests: Add driver for Intel Ethernet Gigabit Controller (IGB)** （cover letter，2/5 个 patch 达到代码量阈值）

- 日期：2026-07-10
- 状态：社区讨论中
- 概括：vfio: selftests: igb 中新增 driver for IGB QEMU device、vfio: selftests: igb 中改用 advanced TX and RX descriptors、vfio: selftests: igb 中Program MSI-X interrupt routing。
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
- 概括：vfio/pci 中保留 vfio cdev 的 iommufd 状态，并iommufd 中新增 保存/取消保存 vfio cdev 的 API。
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
- 概括：限制 channel program segment 数量、根据 IDAW 类型计算 IDAL 长度、取消已存在的 workqueue、Move cp cleanup out of not operational，并Free all memory if cp_init() fails。
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
- 概括：限制 channel program segment 数量、free all memory if cp_init() fails、修复 out of bounds check on CCW array、确保 读写 region 索引在范围内，并实现 a crw lock。
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
- 概括：在 vfio/mlx5 中启用 live migration data mkey 的 relaxed ordering。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260726092943.2880176-10-michaelgur@nvidia.com/

---

### ◆ 子系统：VFIO CDX（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**vfio/cdx: prevent read-only region mappings from becoming writable**

- 日期：2026-08-19
- 状态：社区讨论中
- 概括：在 vfio/cdx 中阻止 只读 region 映射 变为可写。
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
- 概括：在 VFIO selftests 中新增 mlx5 用户态测试驱动，通过 BAR0 命令接口创建 PD/MR/QP/CQ/EQ 等对象，分配 DMA 缓冲区并用 RDMA WRITE 自环回验证设备 DMA 路径。
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

*报告由 Linux Patches Tracker 自动生成 | 2026-09-08 21:29:08*
