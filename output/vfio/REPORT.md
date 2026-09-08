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
| NVIDIA | [PATCH v4 00/27] vfio/pci: Add CXL Type-2 device passthrough support ------为 VFIO PCI 补充 CXL Type-2 设备直通所需的 UAPI、区域暴露和配置裁剪逻辑，使用户态能够管理 CXL 加速设备资源。 |
| Google | [PATCH v5 00/20] vfio/pci: Base Live Update support for VFIO ------为 live update 场景保存和恢复设备、IOMMU 或 VFIO 状态，减少内核切换期间设备上下文丢失对虚拟化工作负载的影响。 |
| Huawei | [PATCH v19 00/18] vfio/pci: Add PCIe TPH support ------围绕 PCIe TPH 能力在 VFIO/IOMMU 路径中的发现、配置、转发表编程和状态复位展开，使用户态能够安全控制设备 TPH 行为。 |
| IBM | [PATCH v9 00/10] s390/vfio_ccw fixes ------集中修复 s390/vfio_ccw fixes 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。 |
| Individual Contributor | [PATCH v5 00/9] vfio/pci: Add mmap() for DMABUFs ------完善 DMA-BUF 相关映射、导出和权限控制流程，增强用户态共享设备内存时的资源管理和安全边界。 |
| NVIDIA | [PATCH v4 00/10] mlx5 support for VFIO self test ------补充 MLX5 设备在 VFIO 自测试中的模拟和 DMA 覆盖，验证变体驱动与 IOMMU 映射路径的协同。 |
| Google | [PATCH v2 00/4] Introduce vfio_dma_mapping_perf_test ------围绕 Introduce vfio_dma_mapping_perf_test 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。 |
| IBM | [PATCH v1 00/23] s390/vfio_ccw: Free all memory if cp_init() fails ------集中修复 s390/vfio_ccw 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。 |
| Google | [PATCH v4 00/9] vfio: selftests: Add driver for Intel Ethernet Gigabit Controller (IGB) ------围绕 vfio 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。 |
| Google | [PATCH v4 00/18] iommu: Add live update state preservation ------为 live update 场景保存和恢复设备、IOMMU 或 VFIO 状态，减少内核切换期间设备上下文丢失对虚拟化工作负载的影响。 |
| Huawei | [PATCH v3 00/3] hisi_acc_vfio_pci: fix three driver issues ------改进 HiSilicon 加速器驱动的复位、隔离、队列或错误处理路径，提升设备管理和虚拟化场景稳定性。 |
| NVIDIA | [PATCH v1 00/5] PCI/vfio-pci: Guard resets against active SR-IOV VFs ------补充 SR-IOV 相关 VFIO 流程和自测试覆盖，验证 PF/VF 生命周期、资源暴露和用户态接口行为。 |
| IBM | [v5,1/4] s390/vfio-ap: Fix leak of pinned NIB and registered NISC in vfio_ap_irq_enable/disable() ------修复leak of pinned nib and registered nisc，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险 |
| Individual Contributor | [v4,10/10] vfio/pci: Add mmap() attributes to DMABUF feature ------新增mmap() attributes，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求 |
| NVIDIA | [rdma-next,09/15] vfio/mlx5: Enable relaxed ordering on the live migration data mkey ------启用之前被禁用或条件编译的功能特性，持续改进代码质量和功能完备性 |
| Google | [v8,2/6] vfio: selftests: igb: Use PHY internal loopback on 82576 ------添加测试用例，验证关键功能的正确性和稳定性，增强框架的功能完整性和适用范围，满足更多使用场景的需求 |
| IBM | [v7,01/23] vfio: Use file-based reference counting for KVM ------修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性 |
| IBM | [v4,01/27] VFIO: take reference to the KVM module ------修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性 |
| Individual Contributor | [PATCH] vfio/cdx: prevent read-only region mappings from becoming writable ------修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性 |
| Google | [RFC,v1,1/1] vfio/pci: Revoke BARs and DMABUFs during sysfs-triggered PCI reset ------修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性 |

---

## 已合入 Patches

暂无。

## 社区讨论中 Patches

### ◆ 子系统：VFIO PCI（10 patches）

**▸ 组织：Google**（3 patches）

**[RFC,v1,1/1] vfio/pci: Revoke BARs and DMABUFs during sysfs-triggered PCI reset**

- 日期：2026-08-07
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260807201405.3717430-2-praan@google.com/

**[RFC,1/1] vfio/pci: Disable sriov on PF device close**

- 日期：2026-08-05
- 状态：社区讨论中
- 概括：禁用存在稳定性或安全性问题的功能，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260805003355.728299-2-skhawaja@google.com/

**[SERIES] vfio/pci: Base Live Update support for VFIO** （cover letter，7/18 个 patch 达到代码量阈值）

- 日期：2026-07-14
- 状态：社区讨论中
- 概括：为 live update 场景保存和恢复设备、IOMMU 或 VFIO 状态，减少内核切换期间设备上下文丢失对虚拟化工作负载的影响。
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
- 概括：完善 DMA-BUF 相关映射、导出和权限控制流程，增强用户态共享设备内存时的资源管理和安全边界。
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
- 概括：新增mmap() attributes，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260701171245.90111-11-matt@ozlabs.org/

**▸ 组织：Huawei**（2 patches）

**[SERIES] hisi_acc_vfio_pci: fix three driver issues** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-08-31
- 状态：社区讨论中
- 概括：改进 HiSilicon 加速器驱动的复位、隔离、队列或错误处理路径，提升设备管理和虚拟化场景稳定性。
- 达到阈值的 patches（2 个，显示前 5）：
  - hisi_acc_vfio_pci: reject live migration on 64KB page with QM_HW_V3 hardware
  - hisi_acc_vfio_pci: clear set_reset_flag after reset completed
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260831090951.844569-2-liulongfang@huawei.com/

**[SERIES] vfio/pci: Add PCIe TPH support** （cover letter，4/10 个 patch 达到代码量阈值）

- 日期：2026-07-02
- 状态：社区讨论中
- 概括：围绕 PCIe TPH 能力在 VFIO/IOMMU 路径中的发现、配置、转发表编程和状态复位展开，使用户态能够安全控制设备 TPH 行为。
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
- 概括：为 VFIO PCI 补充 CXL Type-2 设备直通所需的 UAPI、区域暴露和配置裁剪逻辑，使用户态能够管理 CXL 加速设备资源。
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
- 概括：补充 SR-IOV 相关 VFIO 流程和自测试覆盖，验证 PF/VF 生命周期、资源暴露和用户态接口行为。
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio/pci: Refuse to reset an SR-IOV PF with enabled VFs
  - vfio/pci: Use pci_reset_supported() in place of reset_works
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260812045325.2733631-4-alex.williamson@nvidia.com/

**▸ 组织：IBM**（1 patches）

**[v1] vfio/pci: Avoid mapping BARs for devices with non-mappable BARs**

- 日期：2026-07-29
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260729181116.1373-1-alifm@linux.ibm.com/

---

### ◆ 子系统：VFIO Core（3 patches）

**▸ 组织：IBM**（2 patches）

**[v7,01/23] vfio: Use file-based reference counting for KVM**

- 日期：2026-08-31
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260831144802.834315-2-seiden@linux.ibm.com/

**[v4,01/27] VFIO: take reference to the KVM module**

- 日期：2026-07-06
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260706085229.979525-2-seiden@linux.ibm.com/

**▸ 组织：Individual Contributor**（1 patches）

**vfio/type1: conditional rescheduling while unpinning**

- 日期：2026-07-23
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260723-vfio-v1-1-3b59579916c6@gmail.com/

---

### ◆ 子系统：VFIO Selftests（3 patches）

**▸ 组织：Google**（3 patches）

**[SERIES] Introduce vfio_dma_mapping_perf_test** （cover letter，3/4 个 patch 达到代码量阈值）

- 日期：2026-08-04
- 状态：社区讨论中
- 概括：围绕 Introduce vfio_dma_mapping_perf_test 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。
- 达到阈值的 patches（3 个，显示前 5）：
  - vfio: selftests: Introduce vfio_dma_mapping_perf_test
  - vfio: selftests: Add memfd test to vfio_dma_mapping_perf_test
  - vfio: selftests: Allow a size for vfio_dma_mapping_perf_test
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260804165748.1060476-3-aaronlewis@google.com/

**[v8,2/6] vfio: selftests: igb: Use PHY internal loopback on 82576**

- 日期：2026-07-29
- 状态：社区讨论中
- 概括：添加测试用例，验证关键功能的正确性和稳定性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260729-igb_v3_b4-v8-2-3ed236272b4e@google.com/

**[SERIES] vfio: selftests: Add driver for Intel Ethernet Gigabit Controller (IGB)** （cover letter，2/5 个 patch 达到代码量阈值）

- 日期：2026-07-10
- 状态：社区讨论中
- 概括：围绕 vfio 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。
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
- 概括：为 live update 场景保存和恢复设备、IOMMU 或 VFIO 状态，减少内核切换期间设备上下文丢失对虚拟化工作负载的影响。
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio/pci: Preserve the iommufd state of the vfio cdev
  - iommufd: Add APIs to preserve/unpreserve a vfio cdev
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260808022723.3893618-18-skhawaja@google.com/

**[1/2] vfio/type1: Periodically try rescheduling when unmapping**

- 日期：2026-07-14
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260714210303.3967981-2-aaronlewis@google.com/

---

### ◆ 子系统：VFIO CCW (s390)（2 patches）

**▸ 组织：IBM**（2 patches）

**[SERIES] s390/vfio_ccw: Free all memory if cp_init() fails** （cover letter，6/10 个 patch 达到代码量阈值）

- 日期：2026-08-03
- 状态：社区讨论中
- 概括：集中修复 s390/vfio_ccw 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。
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
- 概括：集中修复 s390/vfio_ccw fixes 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。
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
- 概括：启用之前被禁用或条件编译的功能特性，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260726092943.2880176-10-michaelgur@nvidia.com/

---

### ◆ 子系统：VFIO CDX（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**vfio/cdx: prevent read-only region mappings from becoming writable**

- 日期：2026-08-19
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260819083943.1391-1-suruurism@gmail.com/

---

### ◆ 子系统：VFIO AP (s390)（1 patches）

**▸ 组织：IBM**（1 patches）

**[v5,1/4] s390/vfio-ap: Fix leak of pinned NIB and registered NISC in vfio_ap_irq_enable/disable()**

- 日期：2026-08-31
- 状态：社区讨论中
- 概括：修复leak of pinned nib and registered nisc，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260831171443.222225-2-akrowiak@linux.ibm.com/

---

### ◆ 子系统：VFIO MLX5 Variant（1 patches）

**▸ 组织：NVIDIA**（1 patches）

**[SERIES] mlx5 support for VFIO self test** （cover letter，3/5 个 patch 达到代码量阈值）

- 日期：2026-08-12
- 状态：社区讨论中
- 概括：补充 MLX5 设备在 VFIO 自测试中的模拟和 DMA 覆盖，验证变体驱动与 IOMMU 映射路径的协同。
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

*报告由 Linux Patches Tracker 自动生成 | 2026-09-08 15:00:08*
