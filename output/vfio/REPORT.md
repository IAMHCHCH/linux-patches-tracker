# Linux VFIO 子系统 Patch 追踪报告

---

## 报告信息

| 项目 | 内容 |
|------|------|
| 数据来源 | patchwork.kernel.org |
| 生成日期 | 2026-07-03 |
| 报告区间 | 2026-05-01 至 2026-06-30 |
| 仓库 | [https://github.com/IAMHCHCH/linux-patches-tracker](https://github.com/IAMHCHCH/linux-patches-tracker) |

---

## 统计概览

### 按状态分类

| 状态 | 数量 | 占比 |
|------|------|------|
| 社区讨论中 | 28 | 100.0% |
| 已合入 | 0 | 0.0% |
| **总计** | **28** | **100%** |

### 按组织分类（TOP 15）

| 组织 | 数量 | 占比 |
|------|------|------|
| Google | 7 | 25.0% |
| NVIDIA | 5 | 17.9% |
| Individual Contributor | 5 | 17.9% |
| Meta | 4 | 14.3% |
| IBM | 3 | 10.7% |
| Huawei | 2 | 7.1% |
| Kernel.org | 1 | 3.6% |
| Qualcomm | 1 | 3.6% |

### 按子系统分类

| 子系统 | 数量 | 占比 |
|--------|------|------|
| VFIO PCI | 16 | 57.1% |
| VFIO Core | 6 | 21.4% |
| VFIO Selftests | 3 | 10.7% |
| VFIO IOMMUFD | 2 | 7.1% |
| VFIO MLX5 Variant | 1 | 3.6% |
## 已合入 Patches

暂无。

## 社区讨论中 Patches

### ◆ 子系统：VFIO PCI（16 patches）

**▸ 组织：Google**（4 patches）

**[SERIES] iommu: Add live update state preservation** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-06-14
- 状态：社区讨论中
- 概括：新增live update state preservation，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio/pci: Preserve the iommufd state of the vfio cdev
  - iommufd: Add APIs to preserve/unpreserve a vfio cdev
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260614233728.2212104-18-skhawaja@google.com/

**[SERIES] vfio/pci: Support ZONE_DEVICE-backed P2P Registration** （cover letter，2/4 个 patch 达到代码量阈值）

- 日期：2026-06-10
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio/pci: Block mmap & dmabuf export for ZONE_DEVICE-registered BARs
  - vfio/pci: Block ZONE_DEVICE registration for BARs with active DMABUFs
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260610151853.3608948-2-praan@google.com/

**[v2] vfio/pci: Use a private flag to prevent power state change with VFs**

- 日期：2026-05-14
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260514173449.3282188-1-rananta@google.com/

**[SERIES] vfio/pci: Base Live Update support for VFIO** （cover letter，4/15 个 patch 达到代码量阈值）

- 日期：2026-05-11
- 状态：社区讨论中
- 概括：更新相关的配置或实现以反映最新的内核标准，保持子系统与内核主线的兼容性，适应 API 和框架的演进方向
- 达到阈值的 patches（4 个，显示前 5）：
  - vfio/pci: Register a file handler with Live Update Orchestrator
  - vfio/pci: Preserve vfio-pci device files across Live Update
  - vfio/pci: Retrieve preserved device files after Live Update
  - vfio: selftests: Add continuous DMA to vfio_pci_liveupdate_kexec_test
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260511234802.2280368-2-vipinsh@google.com/

**▸ 组织：Meta**（3 patches）

**[v7,4/5] vfio/pci: implement get_tph and DMA_BUF_TPH feature**

- 日期：2026-06-11
- 状态：社区讨论中
- 概括：实现get_tph and dma_buf_tph feature，完善缺失的功能接口，完善子系统的功能完备性，确保与硬件平台和上层框架的正确协同
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260611161546.4075580-5-zhipingz@meta.com/

**vfio/pci: Make VFIO_PCI_OFFSET_TO_INDEX() return unsigned**

- 日期：2026-05-11
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260511144642.2926799-1-mattev@meta.com/

**[SERIES] vfio/pci: Request resources and map BARs at enable time** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-05-11
- 状态：社区讨论中
- 概括：启用之前被禁用或条件编译的功能特性，持续改进代码质量和功能完备性
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio/pci: Set up BAR resources and maps in vfio_pci_core_enable()
  - vfio/pci: Check BAR resources before exporting a DMABUF
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260511145829.2993601-2-mattev@meta.com/

**▸ 组织：IBM**（2 patches）

**[v5,4/4] vfio-pci/zdev: Add VFIO FMB device features**

- 日期：2026-06-26
- 状态：社区讨论中
- 概括：新增vfio fmb device features，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260626175525.37370-5-oelghoul@linux.ibm.com/

**[v2,2/3] vfio-pci/zdev: Add VFIO FMB device feature**

- 日期：2026-05-19
- 状态：社区讨论中
- 概括：新增vfio fmb device feature，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260519224204.19154-3-oelghoul@linux.ibm.com/

**▸ 组织：Huawei**（2 patches）

**[v16,10/12] vfio/pci: Add TPH_CPU_ST to query CPU's TPH steering tag**

- 日期：2026-06-04
- 状态：社区讨论中
- 概括：新增tph_cpu_st，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260604132804.28678-11-fengchengwen@huawei.com/

**hisi_acc_vfio_pci: simplify the command for reading device information.**

- 日期：2026-05-14
- 状态：社区讨论中
- 概括：简化代码逻辑，减少不必要的复杂度，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260514092026.2018844-1-liulongfang@huawei.com/

**▸ 组织：Individual Contributor**（2 patches）

**vfio/pci: make nointxmask and disable_idle_d3 module params read-only**

- 日期：2026-06-10
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260610054734.3591169-1-kanie@linux.alibaba.com/

**[RFC,06/12] PCI: Convert vfio_pci_core.c to pci_is_sriov_* helpers**

- 日期：2026-06-04
- 状态：社区讨论中
- 概括：迁移vfio_pci_core.c to pci_is_sriov_* helpers，适配新的接口规范
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260604150153.3619662-7-dimitri.daskalakis1@gmail.com/

**▸ 组织：NVIDIA**（2 patches）

**[SERIES] vfio/pci: Add CXL Type-2 device passthrough support** （cover letter，5/5 个 patch 达到代码量阈值）

- 日期：2026-06-25
- 状态：社区讨论中
- 概括：新增cxl type-2 device passthrough support，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（5 个，显示前 5）：
  - vfio: UAPI for CXL Type-2 device passthrough
  - vfio/pci: Add CONFIG_VFIO_PCI_CXL with bind-time CXL Type-2 acquisition
  - vfio/pci/cxl: Add HDM + COMP_REGS regions and DVSEC clipping shim
  - docs: vfio-pci: Document CXL Type-2 device passthrough
  - vfio/pci: Provide opt-out for CXL Type-2 extensions
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260625165407.1769572-6-mhonap@nvidia.com/

**[SERIES] vfio/pci: Latch module params, fix bitfield use and VGA unwind** （cover letter，2/7 个 patch 达到代码量阈值）

- 日期：2026-06-15
- 状态：社区讨论中
- 概括：修复bitfield use and vga unwind，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio/pci: Latch disable_idle_d3 per device
  - vfio/pci: Latch all module parameters per device
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260615191241.688297-4-alex.williamson@nvidia.com/

**▸ 组织：Qualcomm**（1 patches）

**[SERIES] vfio/pci: Hide and optionally override the PCIe Device Serial Number** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-06-13
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio/pci: Virtualize and scrub Device Serial Number from guests
  - vfio/pci: Allow userspace to set a virtual Device Serial Number
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260613-pcie_vfio-v1-1-09168188f3f2@oss.qualcomm.com/

---

### ◆ 子系统：VFIO Core（6 patches）

**▸ 组织：Individual Contributor**（2 patches）

**[v3,23/32] vfio: use iova_to_phys_length for efficient unmap**

- 日期：2026-06-03
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260603151804.1963871-24-guanghuifeng@linux.alibaba.com/

**vfio: prevent infinite loop in vfio_mig_get_next_state() on blocked arc**

- 日期：2026-06-02
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/SYBPR01MB7881290BBDE79B61AE6A017FAF122@SYBPR01MB7881.ausprd01.prod.outlook.com/

**▸ 组织：Meta**（1 patches）

**[v4,1/3] vfio: add dma-buf get_tph callback and DMA_BUF_TPH feature**

- 日期：2026-05-19
- 状态：社区讨论中
- 概括：新增dma-buf get_tph callback and dma_buf_tph feature，扩展功能特性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260519201401.1558410-2-zhipingz@meta.com/

**▸ 组织：Kernel.org**（1 patches）

**[v5,1/5] vfio: cache KVM VM file references instead of raw struct kvm pointers**

- 日期：2026-05-25
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260525154816.1029642-2-aneesh.kumar@kernel.org/

**▸ 组织：NVIDIA**（1 patches）

**[v8,1/1] vfio/nvgrace-gpu: Add Blackwell-Next GPU readiness check via CXL DVSEC**

- 日期：2026-06-02
- 状态：社区讨论中
- 概括：新增blackwell-next gpu readiness check via cxl dvsec，扩展功能特性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260602063015.3915-1-ankita@nvidia.com/

**▸ 组织：IBM**（1 patches）

**[v3,01/27] VFIO: take reference to the KVM module**

- 日期：2026-05-29
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260529155050.2902245-2-seiden@linux.ibm.com/

---

### ◆ 子系统：VFIO Selftests（3 patches）

**▸ 组织：Google**（2 patches）

**vfio: selftests: Add driver for IGB QEMU device**

- 日期：2026-05-11
- 状态：社区讨论中
- 概括：新增driver，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260511211839.2781731-1-jrhilke@google.com/

**[SERIES] vfio: selftest: Add SR-IOV UAPI test** （cover letter，1/8 个 patch 达到代码量阈值）

- 日期：2026-05-05
- 状态：社区讨论中
- 概括：新增sr-iov uapi test，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（1 个，显示前 5）：
  - vfio: selftests: Add tests to validate SR-IOV UAPI
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260505212838.1698034-2-rananta@google.com/

**▸ 组织：NVIDIA**（1 patches）

**[SERIES] vfio: selftest: Add NVIDIA GPU Falcon DMA test driver** （cover letter，1/4 个 patch 达到代码量阈值）

- 日期：2026-06-09
- 状态：社区讨论中
- 概括：新增nvidia gpu falc，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（1 个，显示前 5）：
  - vfio: selftests: Add NVIDIA Falcon driver for DMA testing
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260609232855.3808971-2-rubind@nvidia.com/

---

### ◆ 子系统：VFIO IOMMUFD（2 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[v2,23/30] vfio/iommufd: use iova_to_phys_length for efficient unmap**

- 日期：2026-06-02
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260602104637.1219810-24-guanghuifeng@linux.alibaba.com/

**▸ 组织：Google**（1 patches）

**[SERIES] vfio: selftests: Add support of creating multiple iommus from iommufd** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-05-05
- 状态：社区讨论中
- 概括：新增support of creating multiple iommus from iommufd，扩展功能特性
- 达到阈值的 patches（1 个，显示前 5）：
  - vfio: selftests: Add iommufd multi iommu test
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260505221518.619123-2-skhawaja@google.com/

---

### ◆ 子系统：VFIO MLX5 Variant（1 patches）

**▸ 组织：NVIDIA**（1 patches）

**[SERIES] mlx5 support for VFIO self test** （cover letter，3/5 个 patch 达到代码量阈值）

- 日期：2026-05-15
- 状态：社区讨论中
- 概括：添加测试用例，验证关键功能的正确性和稳定性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（3 个，显示前 5）：
  - vfio: selftests: mlx5 driver - add send_msi support
  - vfio: selftests: Add mlx5 driver - data path and memcpy ops
  - vfio: selftests: Add mlx5 driver - HW init and command interface
- 来源：https://patchwork.kernel.org/project/kvm/patch/8-v2-72e9640932fd+2c64-mlx5st_jgg@nvidia.com/

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

*报告由 Linux Patches Tracker 自动生成 | 2026-07-03 15:41:19*
