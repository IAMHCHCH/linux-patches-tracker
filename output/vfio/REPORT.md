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
| VFIO PCI | 11 | 45.8% |
| VFIO Core | 3 | 12.5% |
| VFIO Selftests | 3 | 12.5% |
| VFIO CCW (s390) | 2 | 8.3% |
| VFIO IOMMUFD | 1 | 4.2% |
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
| NVIDIA | [PATCH v4 00/27] vfio/pci: Add CXL Type-2 device passthrough support ------此补丁系列为VFIO引入CXL Type-2设备直通支持，新增vfio-cxl模块并注册接口，通过虚拟化DVSEC与HDM解码器寄存器、接管BAR映射及模拟提交握手，实现CXL内存设备安全透传。 |
| Google | [PATCH v5 00/20] vfio/pci: Base Live Update support for VFIO ------为 VFIO PCI 设备引入基础实时更新（Live Update）支持，通过重构关闭路径、导出内部辅助函数、注册文件处理器并保留设备文件，配合新增的查找、恢复及强制回取机制，使设备在更新会话中可被安全迁移与还原。 |
| Huawei | [PATCH v19 00/18] vfio/pci: Add PCIe TPH support ------该系列围绕 vfio/pci: Add PCIe TPH support，具体包括隐藏 TPH capability（当设备不支持 TPH 时）、虚拟化 PCIe TPH capability registers、实现 TPH_ST feature for batch ST table programming、暴露 tph_policy via debugfs、新增 dmabuf TPH metadata storage and fd query helper。 |
| IBM | [PATCH v9 00/10] s390/vfio_ccw fixes ------该补丁系列针对s390的vfio_ccw驱动修复多项缺陷，涵盖通道程序段数限制、内存释放与越界检查、CRW锁和IDAW常量处理等，强化并发安全与范围校验以提升稳定性。 |
| Individual Contributor | [PATCH v5 00/9] vfio/pci: Add mmap() for DMABUFs ------该补丁集为vfio/pci设备BAR内存映射引入DMABUF机制，通过查找PFN、创建DMABUF并支持用户态mmap，替代原有直接映射，并增强映射撤销与生命周期管理，从而提升设备内存共享与安全隔离能力。 |
| NVIDIA | [PATCH v4 00/10] mlx5 support for VFIO self test ------为VFIO自测试框架新增mlx5驱动支持，允许指定region大小并补充调试日志，实现数据路径、memcpy操作及MSI发送功能，涵盖硬件初始化和命令接口，从而完成对mlx5设备在虚拟化场景下的自检测试。 |
| Google | [PATCH v2 00/4] Introduce vfio_dma_mapping_perf_test ------该补丁系列新增VFIO DMA映射性能自测工具，支持memfd场景、自定义映射大小，并验证iommu_unmap后区域确实解除映射。 |
| IBM | [PATCH v1 00/23] s390/vfio_ccw: Free all memory if cp_init() fails ------该补丁集针对 s390/vfio_ccw 驱动，修复内存泄漏、越界访问及并发安全问题，通过限制通道程序段数、精确计算 IDAL 长度、取消工作队列、完善清理与锁机制，确保异常路径下全部资源释放和操作安全性。 |
| Google | [PATCH v4 00/18] iommu: Add live update state preservation ------本补丁集为支持设备热迁移时的状态保持，新增iommufd对vfio字符设备绑定关系的保存与恢复接口，并修改vfio/pci以保留其iommufd状态，确保更新过程中设备与IOMMU映射不中断。 |
| Google | [PATCH v4 00/9] vfio: selftests: Add driver for Intel Ethernet Gigabit Controller (IGB) ------此补丁集为vfio自测框架新增Intel IGB网卡驱动，支持高级收发描述符与MSI-X中断路由，并调整超时及PCIe重试配置，以提升虚拟化环境下的硬件模拟测试效率。 |
| Huawei | [PATCH v3 00/3] hisi_acc_vfio_pci: fix three driver issues ------该补丁系列针对 hisi_acc_vfio_pci 驱动修复三个问题：修正 PF 透传场景下实时迁移的使能条件，在 QM_HW_V3 硬件上禁止 64KB 页面大小下的实时迁移以避免故障，并在重置完成后及时清除 set_reset_flag 标志，从而提升设备直通与迁移的稳定性和正确性。 |
| NVIDIA | [PATCH v1 00/5] PCI/vfio-pci: Guard resets against active SR-IOV VFs ------该补丁系列在 vfio-pci 中阻止对已启用虚拟功能的 SR-IOV 物理功能执行重置，改用 pci_reset_supported() 替代旧接口，避免破坏活跃虚拟功能。 |
| IBM | [v5,1/4] s390/vfio-ap: Fix leak of pinned NIB and registered NISC in vfio_ap_irq_enable/disable() ------该补丁修复s390 vfio-ap在启用/禁用队列中断时对已固定NIB页及已注册NISC的泄漏问题，通过轮询确认IR位状态并将失败路径改为保留资源以避免释放后使用。 |
| Individual Contributor | [v4,10/10] vfio/pci: Add mmap() attributes to DMABUF feature ------该补丁为VFIO PCI设备的DMABUF导出功能新增内存属性控制接口，允许用户通过新增的ioctl命令设置后续mmap映射使用不可缓存或写组合属性，默认保持不可缓存，且不影响已有映射。 |
| NVIDIA | [rdma-next,09/15] vfio/mlx5: Enable relaxed ordering on the live migration data mkey ------补丁为VFIO mlx5迁移数据内存键启用宽松排序，使分配内存键时依据设备能力设置该属性，以提升迁移时DMA性能，涉及命令分配路径。 |
| Google | [v8,2/6] vfio: selftests: igb: Use PHY internal loopback on 82576 ------该补丁将vfio的igb网卡selftest从依赖自协商和MAC环回改为配置82576的PHY内部环回，并保留RCTL.LBM_MAC作为QEMU模拟器专用兼容，从而让测试在真实硬件与QEMU下均可正常工作。 |
| IBM | [v7,01/23] vfio: Use file-based reference counting for KVM ------该补丁将KVM页面追踪和VFIO引用计数从基于kvm指针改为基于kvm文件（file），用get_file/fput替代kvm_get_kvm/kvm_put_kvm，使VFIO设备生命周期通过文件引用管理，增强安全性。 |
| IBM | [v4,01/27] VFIO: take reference to the KVM module ------该补丁为VFIO框架在关联KVM时增加模块引用计数保护，在获取KVM安全引用及设备文件或组设置KVM时同步持有并管理KVM模块引用，防止KVM模块卸载引发竞态释放问题。 |
| Individual Contributor | [PATCH] vfio/cdx: prevent read-only region mappings from becoming writable ------该补丁在VFIO CDX驱动中为只读内存区域清除VM_MAYWRITE标志，防止用户通过mprotect将映射升级为可写，确保只读访问限制不被绕过。 |
| Google | [RFC,v1,1/1] vfio/pci: Revoke BARs and DMABUFs during sysfs-triggered PCI reset ------该补丁让 vfio-pci 在 sysfs 触发 PCI 复位时，通过新增的 reset_prepare/reset_done 回调在释放内存锁后统一撤销 BAR 映射和 DMA-BUF，并简化了多设备热复位路径的锁处理与撤销逻辑。 |

---

## 已合入 Patches

暂无。

## 社区讨论中 Patches

### ◆ 子系统：VFIO PCI（11 patches）

**▸ 组织：Google**（4 patches）

**[SERIES] iommu: Add live update state preservation** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-08
- 状态：社区讨论中
- 概括：本补丁集为支持设备热迁移时的状态保持，新增iommufd对vfio字符设备绑定关系的保存与恢复接口，并修改vfio/pci以保留其iommufd状态，确保更新过程中设备与IOMMU映射不中断。
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio/pci: Preserve the iommufd state of the vfio cdev
  - iommufd: Add APIs to preserve/unpreserve a vfio cdev
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260808022723.3893618-18-skhawaja@google.com/

**[RFC,v1,1/1] vfio/pci: Revoke BARs and DMABUFs during sysfs-triggered PCI reset**

- 日期：2026-08-07
- 状态：社区讨论中
- 概括：该补丁让 vfio-pci 在 sysfs 触发 PCI 复位时，通过新增的 reset_prepare/reset_done 回调在释放内存锁后统一撤销 BAR 映射和 DMA-BUF，并简化了多设备热复位路径的锁处理与撤销逻辑。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260807201405.3717430-2-praan@google.com/

**[RFC,1/1] vfio/pci: Disable sriov on PF device close**

- 日期：2026-08-05
- 状态：社区讨论中
- 概括：该补丁在VFIO PCI核心的PF设备关闭流程中，检测到存在活动VF时自动调用sriov_configure禁用SR-IOV，实现关闭PF即同步释放VF资源，避免虚拟功能残留。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260805003355.728299-2-skhawaja@google.com/

**[SERIES] vfio/pci: Base Live Update support for VFIO** （cover letter，7/18 个 patch 达到代码量阈值）

- 日期：2026-07-14
- 状态：社区讨论中
- 概括：为 VFIO PCI 设备引入基础实时更新（Live Update）支持，通过重构关闭路径、导出内部辅助函数、注册文件处理器并保留设备文件，配合新增的查找、恢复及强制回取机制，使设备在更新会话中可被安全迁移与还原。
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
- 概括：该补丁集为vfio/pci设备BAR内存映射引入DMABUF机制，通过查找PFN、创建DMABUF并支持用户态mmap，替代原有直接映射，并增强映射撤销与生命周期管理，从而提升设备内存共享与安全隔离能力。
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
- 概括：该补丁为VFIO PCI设备的DMABUF导出功能新增内存属性控制接口，允许用户通过新增的ioctl命令设置后续mmap映射使用不可缓存或写组合属性，默认保持不可缓存，且不影响已有映射。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260701171245.90111-11-matt@ozlabs.org/

**▸ 组织：Huawei**（2 patches）

**[SERIES] hisi_acc_vfio_pci: fix three driver issues** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-08-31
- 状态：社区讨论中
- 概括：该补丁系列针对 hisi_acc_vfio_pci 驱动修复三个问题：修正 PF 透传场景下实时迁移的使能条件，在 QM_HW_V3 硬件上禁止 64KB 页面大小下的实时迁移以避免故障，并在重置完成后及时清除 set_reset_flag 标志，从而提升设备直通与迁移的稳定性和正确性。
- 达到阈值的 patches（2 个，显示前 5）：
  - hisi_acc_vfio_pci: reject live migration on 64KB page with QM_HW_V3 hardware
  - hisi_acc_vfio_pci: clear set_reset_flag after reset completed
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260831090951.844569-2-liulongfang@huawei.com/

**[SERIES] vfio/pci: Add PCIe TPH support** （cover letter，4/10 个 patch 达到代码量阈值）

- 日期：2026-07-02
- 状态：社区讨论中
- 概括：该系列围绕 vfio/pci: Add PCIe TPH support，具体包括隐藏 TPH capability（当设备不支持 TPH 时）、虚拟化 PCIe TPH capability registers、实现 TPH_ST feature for batch ST table programming、暴露 tph_policy via debugfs、新增 dmabuf TPH metadata storage and fd query helper。
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
- 概括：此补丁系列为VFIO引入CXL Type-2设备直通支持，新增vfio-cxl模块并注册接口，通过虚拟化DVSEC与HDM解码器寄存器、接管BAR映射及模拟提交握手，实现CXL内存设备安全透传。
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
- 概括：该补丁系列在 vfio-pci 中阻止对已启用虚拟功能的 SR-IOV 物理功能执行重置，改用 pci_reset_supported() 替代旧接口，避免破坏活跃虚拟功能。
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio/pci: Refuse to reset an SR-IOV PF with enabled VFs
  - vfio/pci: Use pci_reset_supported() in place of reset_works
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260812045325.2733631-4-alex.williamson@nvidia.com/

**▸ 组织：IBM**（1 patches）

**[v1] vfio/pci: Avoid mapping BARs for devices with non-mappable BARs**

- 日期：2026-07-29
- 状态：社区讨论中
- 概括：此补丁在VFIO PCI核心的BAR映射流程中，跳过对存在不可映射BAR设备的映射操作，避免无效或错误的内存映射尝试。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260729181116.1373-1-alifm@linux.ibm.com/

---

### ◆ 子系统：VFIO Core（3 patches）

**▸ 组织：IBM**（2 patches）

**[v7,01/23] vfio: Use file-based reference counting for KVM**

- 日期：2026-08-31
- 状态：社区讨论中
- 概括：该补丁将KVM页面追踪和VFIO引用计数从基于kvm指针改为基于kvm文件（file），用get_file/fput替代kvm_get_kvm/kvm_put_kvm，使VFIO设备生命周期通过文件引用管理，增强安全性。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260831144802.834315-2-seiden@linux.ibm.com/

**[v4,01/27] VFIO: take reference to the KVM module**

- 日期：2026-07-06
- 状态：社区讨论中
- 概括：该补丁为VFIO框架在关联KVM时增加模块引用计数保护，在获取KVM安全引用及设备文件或组设置KVM时同步持有并管理KVM模块引用，防止KVM模块卸载引发竞态释放问题。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260706085229.979525-2-seiden@linux.ibm.com/

**▸ 组织：Individual Contributor**（1 patches）

**vfio/type1: conditional rescheduling while unpinning**

- 日期：2026-07-23
- 状态：社区讨论中
- 概括：本补丁在 VFIO type1 的页取消固定流程中引入分批与条件调度，每次最多解除 64MB 映射后主动让出 CPU，防止大规模 DMA 映射拆除时触发软锁看门狗，改善了系统响应性。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260723-vfio-v1-1-3b59579916c6@gmail.com/

---

### ◆ 子系统：VFIO Selftests（3 patches）

**▸ 组织：Google**（3 patches）

**[SERIES] Introduce vfio_dma_mapping_perf_test** （cover letter，3/4 个 patch 达到代码量阈值）

- 日期：2026-08-04
- 状态：社区讨论中
- 概括：该补丁系列新增VFIO DMA映射性能自测工具，支持memfd场景、自定义映射大小，并验证iommu_unmap后区域确实解除映射。
- 达到阈值的 patches（3 个，显示前 5）：
  - vfio: selftests: Introduce vfio_dma_mapping_perf_test
  - vfio: selftests: Add memfd test to vfio_dma_mapping_perf_test
  - vfio: selftests: Allow a size for vfio_dma_mapping_perf_test
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260804165748.1060476-3-aaronlewis@google.com/

**[v8,2/6] vfio: selftests: igb: Use PHY internal loopback on 82576**

- 日期：2026-07-29
- 状态：社区讨论中
- 概括：该补丁将vfio的igb网卡selftest从依赖自协商和MAC环回改为配置82576的PHY内部环回，并保留RCTL.LBM_MAC作为QEMU模拟器专用兼容，从而让测试在真实硬件与QEMU下均可正常工作。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260729-igb_v3_b4-v8-2-3ed236272b4e@google.com/

**[SERIES] vfio: selftests: Add driver for Intel Ethernet Gigabit Controller (IGB)** （cover letter，1/5 个 patch 达到代码量阈值）

- 日期：2026-07-10
- 状态：社区讨论中
- 概括：此补丁集为vfio自测框架新增Intel IGB网卡驱动，支持高级收发描述符与MSI-X中断路由，并调整超时及PCIe重试配置，以提升虚拟化环境下的硬件模拟测试效率。
- 达到阈值的 patches（1 个，显示前 5）：
  - vfio: selftests: igb: Disable PCIe completion timeout retries
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260710-igb_v3_b4-v4-1-56e7e2576cc1@google.com/

---

### ◆ 子系统：VFIO CCW (s390)（2 patches）

**▸ 组织：IBM**（2 patches）

**[SERIES] s390/vfio_ccw: Free all memory if cp_init() fails** （cover letter，6/10 个 patch 达到代码量阈值）

- 日期：2026-08-03
- 状态：社区讨论中
- 概括：该补丁集针对 s390/vfio_ccw 驱动，修复内存泄漏、越界访问及并发安全问题，通过限制通道程序段数、精确计算 IDAL 长度、取消工作队列、完善清理与锁机制，确保异常路径下全部资源释放和操作安全性。
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
- 概括：该补丁系列针对s390的vfio_ccw驱动修复多项缺陷，涵盖通道程序段数限制、内存释放与越界检查、CRW锁和IDAW常量处理等，强化并发安全与范围校验以提升稳定性。
- 达到阈值的 patches（6 个，显示前 5）：
  - s390/vfio_ccw: limit the number of channel program segments
  - s390/vfio_ccw: ensure index for read/write regions are within range
  - s390/vfio_ccw: ensure first IDAW remains constant
  - s390/vfio_ccw: calculate idal length based on idaw type
  - s390/vfio_ccw: cancel existing workqueues
  - ... 及其他 1 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260728033022.2658232-3-farman@linux.ibm.com/

---

### ◆ 子系统：VFIO IOMMUFD（1 patches）

**▸ 组织：Google**（1 patches）

**[1/2] vfio/type1: Periodically try rescheduling when unmapping**

- 日期：2026-07-14
- 状态：社区讨论中
- 概括：该补丁在VFIO type1的取消映射与解绑循环中周期性调用cond_resched，每处理PUD_ORDER个页间隔主动让出CPU，以避免大量I/O地址映射解除时长时间占用处理器、提升系统整体调度响应性。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260714210303.3967981-2-aaronlewis@google.com/

---

### ◆ 子系统：VFIO Migration（1 patches）

**▸ 组织：NVIDIA**（1 patches）

**[rdma-next,09/15] vfio/mlx5: Enable relaxed ordering on the live migration data mkey**

- 日期：2026-07-26
- 状态：社区讨论中
- 概括：补丁为VFIO mlx5迁移数据内存键启用宽松排序，使分配内存键时依据设备能力设置该属性，以提升迁移时DMA性能，涉及命令分配路径。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260726092943.2880176-10-michaelgur@nvidia.com/

---

### ◆ 子系统：VFIO CDX（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**vfio/cdx: prevent read-only region mappings from becoming writable**

- 日期：2026-08-19
- 状态：社区讨论中
- 概括：该补丁在VFIO CDX驱动中为只读内存区域清除VM_MAYWRITE标志，防止用户通过mprotect将映射升级为可写，确保只读访问限制不被绕过。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260819083943.1391-1-suruurism@gmail.com/

---

### ◆ 子系统：VFIO AP (s390)（1 patches）

**▸ 组织：IBM**（1 patches）

**[v5,1/4] s390/vfio-ap: Fix leak of pinned NIB and registered NISC in vfio_ap_irq_enable/disable()**

- 日期：2026-08-31
- 状态：社区讨论中
- 概括：该补丁修复s390 vfio-ap在启用/禁用队列中断时对已固定NIB页及已注册NISC的泄漏问题，通过轮询确认IR位状态并将失败路径改为保留资源以避免释放后使用。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260831171443.222225-2-akrowiak@linux.ibm.com/

---

### ◆ 子系统：VFIO MLX5 Variant（1 patches）

**▸ 组织：NVIDIA**（1 patches）

**[SERIES] mlx5 support for VFIO self test** （cover letter，3/5 个 patch 达到代码量阈值）

- 日期：2026-08-12
- 状态：社区讨论中
- 概括：为VFIO自测试框架新增mlx5驱动支持，允许指定region大小并补充调试日志，实现数据路径、memcpy操作及MSI发送功能，涵盖硬件初始化和命令接口，从而完成对mlx5设备在虚拟化场景下的自检测试。
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

*报告由 Linux Patches Tracker 自动生成 | 2026-09-08 16:16:52*
