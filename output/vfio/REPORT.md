# Linux VFIO 子系统 Patch 追踪报告

---

## 报告信息

| 项目 | 内容 |
|------|------|
| 数据来源 | patchwork.kernel.org |
| 生成日期 | 2026-05-08 |
| 报告区间 | 2026-02-01 至 2026-05-06 |
| 仓库 | [https://github.com/IAMHCHCH/linux-patches-tracker](https://github.com/IAMHCHCH/linux-patches-tracker) |

---

## 统计概览

### 按状态分类

| 状态 | 数量 | 占比 |
|------|------|------|
| 社区讨论中 | 36 | 100.0% |
| 已合入 | 0 | 0.0% |
| **总计** | **36** | **100%** |

### 按组织分类（TOP 15）

| 组织 | 数量 | 占比 |
|------|------|------|
| NVIDIA | 9 | 25.0% |
| Individual Contributor | 7 | 19.4% |
| IBM | 6 | 16.7% |
| Google | 6 | 16.7% |
| Meta | 5 | 13.9% |
| Intel | 2 | 5.6% |
| Linux Community | 1 | 2.8% |

### 按子系统分类

| 子系统 | 数量 | 占比 |
|--------|------|------|
| VFIO PCI | 18 | 50.0% |
| VFIO Core | 11 | 30.6% |
| VFIO IOMMUFD | 2 | 5.6% |
| VFIO Selftests | 2 | 5.6% |
| VFIO Mediated Device | 1 | 2.8% |
| VFIO CDX | 1 | 2.8% |
| VFIO MLX5 Variant | 1 | 2.8% |
## 已合入 Patches

暂无。

## 社区讨论中 Patches

### ◆ 子系统：VFIO PCI（18 patches）

**▸ 组织：IBM**（5 patches）

**[v1,2/3] vfio-pci/zdev: Add VFIO FMB device feature**

- 日期：2026-05-01
- 状态：社区讨论中
- 概括：新增vfio fmb device feature，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260501192530.9429-3-oelghoul@linux.ibm.com/

**[SERIES] vfio/pci: Introduce vfio_pci driver for ISM devices** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-03-25
- 状态：社区讨论中
- 概括：引入vfio_pci driver for ism devices，扩展框架的功能范围，提升框架的抽象能力和代码可扩展性
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio/ism: Implement vfio_pci driver for ISM devices
  - vfio/pci: Rename vfio_config_do_rw() to vfio_pci_config_rw_single() and export it
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260325-vfio_pci_ism-v8-2-ddc504cde914@linux.ibm.com/

**[1/3] vfio/pci: Set VFIO_PCI_OFFSET_SHIFT to 48**

- 日期：2026-02-12
- 状态：社区讨论中
- 概括：修改将 vfio_pci_offset_shift 配置为 48，调整运行参数，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260212-vfio_pci_ism-v1-1-333262ade074@linux.ibm.com/

**[GIT,PULL,v1,35/36] MAINTAINERS: Replace backup for s390 vfio-pci**

- 日期：2026-02-10
- 状态：社区讨论中
- 概括：更新相关配置项或代码引用，保持子系统与内核主线的兼容性，适应 API 和框架的演进方向
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260210153417.77403-36-imbrenda@linux.ibm.com/

**MAINTAINERS: Replace backup for s390 vfio-pci**

- 日期：2026-02-02
- 状态：社区讨论中
- 概括：更新相关配置项或代码引用，保持子系统与内核主线的兼容性，适应 API 和框架的演进方向
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260202144557.1771203-1-farman@linux.ibm.com/

**▸ 组织：Meta**（5 patches）

**[SERIES] vfio/pci: Request resources and map BARs at enable time** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-05-05
- 状态：社区讨论中
- 概括：启用之前被禁用或条件编译的功能特性，持续改进代码质量和功能完备性
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio/pci: Check BAR resources before exporting a DMABUF
  - vfio/pci: Set up BAR resources and maps in vfio_pci_core_enable()
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260505173835.2324179-3-mattev@meta.com/

**[v3,1/3] vfio/pci: Set up bar resources and maps in vfio_pci_core_enable()**

- 日期：2026-04-30
- 状态：社区讨论中
- 概括：启用之前被禁用或条件编译的功能特性，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260430100340.2787446-2-mattev@meta.com/

**[SERIES] vfio/pci: Add mmap() for DMABUFs** （cover letter，7/9 个 patch 达到代码量阈值）

- 日期：2026-04-16
- 状态：社区讨论中
- 概括：新增mmap()，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（7 个，显示前 5）：
  - vfio/pci: Permanently revoke a DMABUF on request
  - vfio/pci: Convert BAR mmap() to use a DMABUF
  - vfio/pci: Support mmap() of a VFIO DMABUF
  - vfio/pci: Add a helper to create a DMABUF for a BAR-map VMA
  - vfio/pci: Add a helper to look up PFNs for DMABUFs
  - ... 及其他 2 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260416131815.2729131-9-mattev@meta.com/

**vfio/pci: Don't export DMABUFs for unmappable BARs**

- 日期：2026-04-15
- 状态：社区讨论中
- 概括：限制export dmabufs，增加条件判断和安全保护逻辑，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260415181623.1021090-1-mattev@meta.com/

**[SERIES] vfio/pci: Set up VFIO barmap before creating a DMABUF** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-04-15
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio/pci: Set up VFIO barmap before creating a DMABUF
  - vfio/pci: Serialise vfio_pci_core_setup_barmap()
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260415181423.1008458-1-mattev@meta.com/

**▸ 组织：Individual Contributor**（4 patches）

**[v2] vfio/xe: avoid duplicate reset in xe_vfio_pci_reset_done**

- 日期：2026-04-27
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260427012128.117051-1-zhaoguohan@kylinos.cn/

**vfio/pci: Allow disabling idle D3 on a per-device basis**

- 日期：2026-04-22
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260422081307.2550-1-lirongqing@baidu.com/

**[SERIES] Fix CVE-2024-27022: fork/hugetlb race with vfio prerequisites** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-04-02
- 状态：社区讨论中
- 概括：修复竞态条件问题，通过增加锁保护或调整执行顺序消除并发访问冲突，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（3 个，显示前 5）：
  - [6.6.y,1/4] vfio: Create vfio_fs_type with inode per device
  - [6.6.y,2/4] vfio/pci: Use unmap_mapping_range()
  - [6.6.y,3/4] vfio/pci: Insert full vma on mmap'd MMIO fault
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260402161311.63484-2-tugrul.kukul@est.tech/

**[v2,1/2] drivers/vfio_pci_core: Change PXD_ORDER check from switch case to if/else block**

- 日期：2026-03-09
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/b155e19993ee1f5584c72050192eb468b31c5029.1773058761.git.ritesh.list@gmail.com/

**▸ 组织：Google**（3 patches）

**vfio/pci: Use a private flag to prevent power state change with VFs**

- 日期：2026-05-04
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260504224142.1041477-1-rananta@google.com/

**[SERIES] KVM: selftests: Link with VFIO selftests lib and test device interrupts** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-03-31
- 状态：社区讨论中
- 概括：添加测试用例，验证关键功能的正确性和稳定性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（1 个，显示前 5）：
  - KVM: selftests: Add vfio_pci_irq_test
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260331194033.3890309-4-jrhilke@google.com/

**[SERIES] vfio/pci: Base Live Update support for VFIO device files** （cover letter，4/16 个 patch 达到代码量阈值）

- 日期：2026-03-23
- 状态：社区讨论中
- 概括：更新相关的配置或实现以反映最新的内核标准，保持子系统与内核主线的兼容性，适应 API 和框架的演进方向
- 达到阈值的 patches（4 个，显示前 5）：
  - vfio/pci: Register a file handler with Live Update Orchestrator
  - vfio/pci: Preserve vfio-pci device files across Live Update
  - vfio/pci: Retrieve preserved device files after Live Update
  - vfio: selftests: Add continuous DMA to vfio_pci_liveupdate_kexec_test
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260323235817.1960573-7-dmatlack@google.com/

**▸ 组织：NVIDIA**（1 patches）

**vfio/pci: Require vfio_device_ops.name**

- 日期：2026-03-31
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260331202443.2598404-1-alex.williamson@nvidia.com/

---

### ◆ 子系统：VFIO Core（11 patches）

**▸ 组织：NVIDIA**（5 patches）

**[RFC,9/9] vfio/listener: Skip DMA mapping for VFIO-owned RAM-device regions**

- 日期：2026-04-27
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260427181235.3003865-10-mhonap@nvidia.com/

**[v6,1/1] vfio/nvgrace-gpu: Add Blackwell-Next GPU readiness check via CXL DVSEC**

- 日期：2026-04-22
- 状态：社区讨论中
- 概括：新增blackwell-next gpu readiness check via cxl dvsec，扩展功能特性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260422134926.653211-1-ankita@nvidia.com/

**[SERIES] vfio/virtio: Fix list_lock type and modernize locking** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-04-14
- 状态：社区讨论中
- 概括：修复list_lock type and modernize locking，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（4 个，显示前 5）：
  - vfio/virtio: Convert list_lock from spinlock to mutex
  - vfio/virtio: Use guard() for migf->lock where applicable
  - vfio/virtio: Use guard() for bar_mutex in legacy I/O
  - vfio/virtio: Use guard() for list_lock where applicable
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260414200625.3601509-2-alex.williamson@nvidia.com/

**[SERIES] vfio/pci: Add CXL Type-2 device passthrough support** （cover letter，12/14 个 patch 达到代码量阈值）

- 日期：2026-04-01
- 状态：社区讨论中
- 概括：新增cxl type-2 device passthrough support，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（12 个，显示前 5）：
  - vfio/pci: Export config access helpers
  - vfio/cxl: Introduce HDM decoder register emulation framework
  - vfio/cxl: Provide opt-out for CXL feature
  - docs: vfio-pci: Document CXL Type-2 device passthrough
  - vfio: UAPI for CXL-capable PCI device assignment
  - ... 及其他 7 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260401143917.108413-8-mhonap@nvidia.com/

**[SERIES] Add virtualization support for EGM** （cover letter，9/15 个 patch 达到代码量阈值）

- 日期：2026-02-23
- 状态：社区讨论中
- 概括：新增virtualizati，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（9 个，显示前 5）：
  - vfio/nvgrace-gpu: Expand module_pci_driver to allow custom module init
  - vfio/nvgrace-egm: Register auxiliary driver ops
  - vfio/nvgrace-gpu: track GPUs associated with the EGM regions
  - vfio/nvgrace-gpu: Create auxiliary device for EGM
  - vfio/nvgrace-egm: Clear Memory before handing out to VM
  - ... 及其他 4 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260223155514.152435-2-ankita@nvidia.com/

**▸ 组织：Individual Contributor**（3 patches）

**vfio: pci: use kzalloc_flex**

- 日期：2026-03-26
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260326023747.54485-1-rosenp@gmail.com/

**vfio/type1: Retry follow_pfnmap_start() when PFNMAP is zapped**

- 日期：2026-03-17
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260317-retry-pin-on-reclaimed-pud-v1-1-1f0d0a23f78d@akamai.com/

**[46/61] vfio: Prefer IS_ERR_OR_NULL over manual NULL check**

- 日期：2026-03-10
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260310-b4-is_err_or_null-v1-46-bd63b656022d@avm.de/

**▸ 组织：Intel**（2 patches）

**[v2,2/2] vfio/xe: Notify PF about VF FLR in reset_prepare**

- 日期：2026-03-09
- 状态：社区讨论中
- 概括：准备为后续重大修改做前置准备，进行接口调整或代码重组，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260309152449.910636-3-piotr.piorkowski@intel.com/

**vfio/qat: extend Kconfig dependencies for 420xx and 6xxx devices**

- 日期：2026-02-13
- 状态：社区讨论中
- 概括：扩展现有功能，增加新的操作参数或接口能力，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260213091403.72338-1-suman.kumar.chakraborty@intel.com/

**▸ 组织：IBM**（1 patches）

**[v2,01/28] VFIO: take reference to the KVM module**

- 日期：2026-04-28
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260428155622.1361364-2-seiden@linux.ibm.com/

---

### ◆ 子系统：VFIO IOMMUFD（2 patches）

**▸ 组织：Google**（2 patches）

**[SERIES] vfio: selftests: Add support of creating multiple iommus from iommufd** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-05-05
- 状态：社区讨论中
- 概括：新增support of creating multiple iommus from iommufd，扩展功能特性
- 达到阈值的 patches（1 个，显示前 5）：
  - vfio: selftests: Add iommufd multi iommu test
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260505221518.619123-2-skhawaja@google.com/

**[SERIES] iommu: Add live update state preservation** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-04-27
- 状态：社区讨论中
- 概括：新增live update state preservation，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（2 个，显示前 5）：
  - iommufd: Add APIs to preserve/unpreserve a vfio cdev
  - vfio/pci: Preserve the iommufd state of the vfio cdev
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260427175633.1978233-15-skhawaja@google.com/

---

### ◆ 子系统：VFIO Selftests（2 patches）

**▸ 组织：Google**（1 patches）

**[SERIES] vfio: selftest: Add SR-IOV UAPI test** （cover letter，2/8 个 patch 达到代码量阈值）

- 日期：2026-05-05
- 状态：社区讨论中
- 概括：新增sr-iov uapi test，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio: selftests: Introduce a sysfs lib
  - vfio: selftests: Add tests to validate SR-IOV UAPI
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260505212838.1698034-2-rananta@google.com/

**▸ 组织：NVIDIA**（1 patches）

**[SERIES] vfio: selftest: Add NVIDIA GPU Falcon DMA test driver** （cover letter，1/4 个 patch 达到代码量阈值）

- 日期：2026-04-08
- 状态：社区讨论中
- 概括：新增nvidia gpu falc，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（1 个，显示前 5）：
  - vfio: selftests: Add NVIDIA Falcon driver for DMA testing
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260408225459.3088623-2-alex.williamson@nvidia.com/

---

### ◆ 子系统：VFIO Mediated Device（1 patches）

**▸ 组织：Linux Community**（1 patches）

**vfio/mdev: make VFIO_MDEV user-visible in Kconfig**

- 日期：2026-03-05
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260305233526.32607-1-jp.kobryn@linux.dev/

---

### ◆ 子系统：VFIO CDX（1 patches）

**▸ 组织：NVIDIA**（1 patches）

**[SERIES] vfio/cdx: Fix interrupt trigger races and consolidate MSI state** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-04-17
- 状态：社区讨论中
- 概括：修复interrupt trigger races and consolidate msi state
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio/cdx: Consolidate MSI configured state onto cdx_irqs
  - vfio/cdx: Serialize VFIO_DEVICE_SET_IRQS with a per-device mutex
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260417202800.88287-2-alex.williamson@nvidia.com/

---

### ◆ 子系统：VFIO MLX5 Variant（1 patches）

**▸ 组织：NVIDIA**（1 patches）

**[SERIES] mlx5 support for VFIO self test** （cover letter，3/5 个 patch 达到代码量阈值）

- 日期：2026-05-01
- 状态：社区讨论中
- 概括：添加测试用例，验证关键功能的正确性和稳定性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（3 个，显示前 5）：
  - vfio: selftests: mlx5 driver - add send_msi support
  - vfio: selftests: Add mlx5 driver - data path and memcpy ops
  - vfio: selftests: Add mlx5 driver - HW init and command interface
- 来源：https://patchwork.kernel.org/project/kvm/patch/8-v1-dc5fa250ca1d+3213-mlx5st_jgg@nvidia.com/

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

*报告由 Linux Patches Tracker 自动生成 | 2026-05-08 15:37:07*
