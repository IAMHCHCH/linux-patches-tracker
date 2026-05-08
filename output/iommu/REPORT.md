# Linux IOMMU 子系统 Patch 追踪报告

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
| 社区讨论中 | 57 | 96.6% |
| 已合入 | 1 | 1.7% |
| **总计** | **59** | **100%** |

### 按组织分类（TOP 15）

| 组织 | 数量 | 占比 |
|------|------|------|
| Individual Contributor | 18 | 30.5% |
| NVIDIA | 15 | 25.4% |
| Intel | 9 | 15.3% |
| Kernel.org | 4 | 6.8% |
| Google | 3 | 5.1% |
| SiFive | 1 | 1.7% |
| ARM | 1 | 1.7% |
| Debian | 1 | 1.7% |
| Qualcomm | 1 | 1.7% |
| NXP | 1 | 1.7% |
| Microsoft | 1 | 1.7% |
| SpacemiT | 1 | 1.7% |
| AMD | 1 | 1.7% |
| Oracle | 1 | 1.7% |
| Huawei | 1 | 1.7% |

### 按子系统分类

| 子系统 | 数量 | 占比 |
|--------|------|------|
| ARM SMMUv3 | 19 | 32.2% |
| Intel VT-d | 11 | 18.6% |
| IOMMU Core | 11 | 18.6% |
| RISC-V IOMMU | 5 | 8.5% |
| IOMMUFD | 4 | 6.8% |
| AMD IOMMU | 4 | 6.8% |
| IOMMU Page Table | 1 | 1.7% |
| IOMMU DMA-API | 1 | 1.7% |
| ARM SMMU (v1/v2) | 1 | 1.7% |
| IOMMU SVA/SVM | 1 | 1.7% |
| ARM SMMU Acceleration | 1 | 1.7% |
## 已合入 Patches

### ◆ 子系统：RISC-V IOMMU（1 patches）

**▸ 组织：NVIDIA**（1 patches）

**[SERIES] Convert riscv to use the generic iommu page table** （cover letter，4/6 个 patch 达到代码量阈值）

- 日期：2026-02-27
- 状态：已合入
- 概括：迁移riscv to use the generic iommu page table，适配新的接口规范
- 达到阈值的 patches（4 个，显示前 5）：
  - iommu/riscv: Disable SADE
  - iommu/riscv: Enable SVNAPOT support for contiguous ptes
  - iommu/riscv: Use the generic iommu page table
  - iommupt: Add the RISC-V page table format
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/6-v4-5a9ca1a9b7a5+5f2-iommu_pt_riscv_jgg@nvidia.com/

---

## 社区讨论中 Patches

### ◆ 子系统：ARM SMMUv3（19 patches）

**▸ 组织：NVIDIA**（8 patches）

**iommu/arm-smmu-v3-sva: Enable Hardware Access and Hardware Dirty bits**

- 日期：2026-05-03
- 状态：社区讨论中
- 概括：启用之前被禁用或条件编译的功能特性，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260503135413.1108138-1-nicolinc@nvidia.com/

**[SERIES] Remove SMMUv3 struct arm_smmu_cmdq_ent** （cover letter，6/9 个 patch 达到代码量阈值）

- 日期：2026-05-01
- 状态：社区讨论中
- 概括：移除smmuv3 struct arm_smmu_cmdq_ent，清理冗余或过时的代码，精简代码库规模，降低后续维护的复杂度和引入回归问题的风险
- 达到阈值的 patches（6 个，显示前 5）：
  - iommu/arm-smmu-v3: Use the HW arm_smmu_cmd in cmdq selection functions
  - iommu/arm-smmu-v3: Use the HW arm_smmu_cmd in cmdq submission functions
  - iommu/arm-smmu-v3: Directly encode CMDQ_OP_ATC_INV
  - iommu/arm-smmu-v3: Directly encode simple commands
  - iommu/arm-smmu-v3: Directly encode TLBI commands
  - ... 及其他 1 个 patch
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/2-v1-b7dc0a0d4aa0+3723d-smmu_no_cmdq_ent_jgg@nvidia.com/

**[v4,3/3] iommu/arm-smmu-v3: Allow ATS to be always on**

- 日期：2026-04-27
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/7403163ebf59380f88c7503b3adf0dae07428df8.1777269009.git.nicolinc@nvidia.com/

**[V1,3/3] iommu/arm-smmu-v3: Honor IORT Root Complex PASID descriptors**

- 日期：2026-04-23
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-acpi/patch/20260423191417.2031652-4-vidyas@nvidia.com/

**[SERIES] iommu/arm-smmu-v3: Fix bugs and typos in arm_smmu_invs series** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-03-21
- 状态：社区讨论中
- 概括：修复bugs and typos，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/arm-smmu-v3: Do not continue in __arm_smmu_domain_inv_range()
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260321225041.11090-3-nicolinc@nvidia.com/

**[SERIES] iommu/arm-smmu-v3: Share domain across SMMU/vSMMU instances** （cover letter，7/10 个 patch 达到代码量阈值）

- 日期：2026-03-19
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（7 个，显示前 5）：
  - iommu/arm-smmu-v3: Pass in arm_smmu_make_cd_fn to arm_smmu_set_pasid()
  - iommu/arm-smmu-v3: Store IOTLB cache tags in struct arm_smmu_attach_state
  - iommu/arm-smmu-v3: Allocate INV_TYPE_S2_VMID_VSMMU in arm_vsmmu_init
  - iommu/arm-smmu-v3: Allocate IOTLB cache tag if no id to reuse
  - iommu/arm-smmu-v3: Pass in IOTLB cache tag to arm_smmu_master_build_invs()
  - ... 及其他 2 个 patch
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/7889322d41b1d8fa83bb318df2bd705a6241f6b1.1773949042.git.nicolinc@nvidia.com/

**[SERIES] iommu/arm-smmu-v3: Introduce an RCU-protected invalidation array** （cover letter，6/8 个 patch 达到代码量阈值）

- 日期：2026-03-17
- 状态：社区讨论中
- 概括：引入an rcu-protected invalidation array，扩展框架的功能范围，提升框架的抽象能力和代码可扩展性
- 达到阈值的 patches（6 个，显示前 5）：
  - iommu/arm-smmu-v3: Explicitly set smmu_domain->stage for SVA
  - iommu/arm-smmu-v3: Add arm_smmu_invs based arm_smmu_domain_inv_range()
  - iommu/arm-smmu-v3: Introduce a per-domain arm_smmu_invs array
  - iommu/arm-smmu-v3: Pre-allocate a per-master invalidation array
  - iommu/arm-smmu-v3: Perform per-domain invalidations using arm_smmu_invs
  - ... 及其他 1 个 patch
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/8f4a7064b5f41a7caa9db0740a9003bee88cd7ec.1773733797.git.nicolinc@nvidia.com/

**[v1,2/2] iommu/arm-smmu-v3: Recover ATC invalidate timeouts**

- 日期：2026-03-05
- 状态：社区讨论中
- 概括：安全加固增加输入验证和边界检查，防止恶意或异常数据导致系统异常行为，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/ca7ab934bf0f433b62a5c15d42241632c4cb9366.1772686998.git.nicolinc@nvidia.com/

**▸ 组织：Individual Contributor**（7 patches）

**[SERIES] iommu: Add PCI vendor:device ID to IOMMU fault logs** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-05-06
- 状态：社区讨论中
- 概括：新增pci vendor:device id，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/arm-smmu-v3: Print PCI vendor:device ID in SMMU translation fault logs
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260506150541.60467-2-yigitogu@amazon.de/

**[SERIES] iommu/arm-smmu: Use FIELD_MODIFY() for bitfield operations** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-04-30
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/arm-smmu-v3: Use FIELD_MODIFY()
  - iommu/arm-smmu-qcom: Use FIELD_MODIFY()
- 来源：https://patchwork.kernel.org/project/linux-arm-msm/patch/20260430164545.49637-3-18255117159@163.com/

**[v2] iommu/arm-smmu-v3: Limit queue allocation retry boundary to PAGE_SIZE**

- 日期：2026-04-22
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/tencent_361CADF43F93DCA4D5489881006382FF4006@qq.com/

**iommu/arm-smmu-v3: Allow disabling Stage 1 translation**

- 日期：2026-04-20
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260420123221.20801-1-epetron@amazon.de/

**iommu/arm-smmu-v3: Stop queue allocation retry at PAGE_SIZE**

- 日期：2026-04-18
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/tencent_F6E384A40D990A279B460A0CDE1927FDF509@qq.com/

**iommu/arm-smmu-v3: Allocate cmdq_batch on the heap**

- 日期：2026-03-11
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260311094444.3714302-1-yphbchou0911@gmail.com/

**[v2] iommu/arm-smmu-v3: Restrict MMU-700 errata 2268618 and 2812531 to affected**

- 日期：2026-02-06
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260206-smmuv3-v2-1-f381a2125392@phytium.com.cn/

**▸ 组织：NXP**（1 patches）

**[2/3] iommu/arm-smmu-v3: Populate PMU child devices from Devicetree**

- 日期：2026-04-08
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260408-smmu-perf-v1-2-d75dac96e828@nxp.com/

**▸ 组织：Huawei**（1 patches）

**[SERIES] Add debugfs support for ARM SMMUv3** （cover letter，2/5 个 patch 达到代码量阈值）

- 日期：2026-03-28
- 状态：社区讨论中
- 概括：修复fs support，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/arm-smmu-v3: Add Stream Table Entry display to debugfs
  - iommu/arm-smmu-v3: Add basic debugfs framework
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260328100953.3441915-3-xiaqinxin@huawei.com/

**▸ 组织：Kernel.org**（1 patches）

**[SERIES] coco/TSM: Implement host-side support for Arm CCA TDISP setup** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-04-27
- 状态：社区讨论中
- 概括：实现host-side support，完善缺失的功能接口，完善子系统的功能完备性，确保与硬件平台和上层框架的正确协同
- 达到阈值的 patches（4 个，显示前 5）：
  - iommu/arm-smmu-v3: Discover RME support and realm IRQ topology
  - iommu/arm-smmu-v3: Save the programmed MSI message in msi_desc
  - iommu/arm-smmu-v3: Add initial pSMMU realm viommu plumbing
  - iommu/arm-smmu-v3: Track realm pSMMU users with refcount_t
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260427085344.941627-2-aneesh.kumar@kernel.org/

**▸ 组织：Google**（1 patches）

**[SERIES] KVM: arm64: SMMUv3 driver for pKVM (trap and emulate)** （cover letter，17/18 个 patch 达到代码量阈值）

- 日期：2026-05-01
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（17 个，显示前 5）：
  - iommu/arm-smmu-v3: Split code with hyp
  - iommu/arm-smmu-v3: Move IDR parsing to common functions
  - iommu/arm-smmu-v3: Move TLB range invalidation into common code
  - iommu/arm-smmu-v3-kvm: Add SMMUv3 driver
  - iommu/arm-smmu-v3-kvm: Add the kernel driver
  - ... 及其他 12 个 patch
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260501111928.259252-4-smostafa@google.com/

---

### ◆ 子系统：Intel VT-d（11 patches）

**▸ 组织：Intel**（8 patches）

**[SERIES] intel_iommu: Enable PASID support for passthrough device** （cover letter，10/13 个 patch 达到代码量阈值）

- 日期：2026-04-30
- 状态：社区讨论中
- 概括：启用之前被禁用或条件编译的功能特性，持续改进代码质量和功能完备性
- 达到阈值的 patches（10 个，显示前 5）：
  - intel_iommu: Create the nested hwpt with IOMMU_HWPT_ALLOC_PASID flag
  - intel_iommu: Export some functions
  - intel_iommu: Change pasid property from bool to uint8
  - iommufd: Extend attach/detach_hwpt callbacks to support pasid
  - intel_iommu_accel: Handle PASID entry removal for system reset
  - ... 及其他 5 个 patch
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260430071315.354333-5-zhenzhong.duan@intel.com/

**[v2,1/2] intel_iommu: widen impl.min_access_size to 8 to fix MMIO abort**

- 日期：2026-04-24
- 状态：社区讨论中
- 概括：修复mmio abort，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260424201842.176953-2-junjie.cao@intel.com/

**[1/2] intel_iommu: Replace assert(size == 4) with guest error in MMIO handlers**

- 日期：2026-04-20
- 状态：社区讨论中
- 概括：修复相关功能缺陷或逻辑错误，确保操作行为符合预期规范，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260420170523.17908-1-junjie.cao@intel.com/

**intel_iommu: Re-expose VTD_ECAP_PT**

- 日期：2026-04-15
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260415095832.9631-1-zhenzhong.duan@intel.com/

**[v3,14/14] intel_iommu: Expose flag VIOMMU_FLAG_PASID_SUPPORTED when configured**

- 日期：2026-04-03
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260403035541.18355-15-zhenzhong.duan@intel.com/

**[SERIES] intel_iommu: Enable PRQ support for passthrough device** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-03-27
- 状态：社区讨论中
- 概括：启用之前被禁用或条件编译的功能特性，持续改进代码质量和功能完备性
- 达到阈值的 patches（3 个，显示前 5）：
  - intel_iommu_accel: Accept PRQ response for passthrough device
  - intel_iommu_accel: Add PRQ injection for passthrough device
  - intel_iommu_accel: teardown FAULTQ resources in bottom half
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260327025228.474257-5-zhenzhong.duan@intel.com/

**[SERIES] PCI/TSM: PCIe Link Encryption Establishment via TDX platform services** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-03-27
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu/vt-d: Cache max domain ID to avoid redundant calculation
  - iommu/vt-d: Reserve the MSB domain ID bit for the TDX module
  - iommu/vt-d: Export a helper to do function for each dmar_drhd_unit
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/20260327160132.2946114-19-yilun.xu@linux.intel.com/

**[SERIES] Update properties naming for 'x-scalable-mode' and 'x-flts'** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-03-11
- 状态：社区讨论中
- 概括：更新相关的配置或实现以反映最新的内核标准，保持子系统与内核主线的兼容性，适应 API 和框架的演进方向
- 达到阈值的 patches（1 个，显示前 5）：
  - intel_iommu: Change 'flts' property naming to 'fsts'
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260311092320.212849-2-zhenzhong.duan@intel.com/

**▸ 组织：Individual Contributor**（2 patches）

**[SERIES] intel_iommu: Only set dirty bit when PTE exposes write permission** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-03-13
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（2 个，显示前 5）：
  - intel_iommu: Only set dirty bit when PTE exposes write permission
  - intel_iommu: Always write all the flags passed to vtd_set_flag_in_pte
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260313145244.1063405-1-clement.mathieu--drif@bull.com/

**intel_iommu: Do not report recoverable faults to host**

- 日期：2026-02-08
- 状态：社区讨论中
- 概括：限制report recoverable faults to host，增加条件判断和安全保护逻辑，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260208082252.288-1-clement.mathieu--drif@eviden.com/

**▸ 组织：Kernel.org**（1 patches）

**[09/38] iommu/vt-d: Use sched_clock() instead of get_cycles()**

- 日期：2026-04-10
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260410120318.187521447@kernel.org/

---

### ◆ 子系统：IOMMU Core（10 patches）

**▸ 组织：Individual Contributor**（6 patches）

**[v2] iommu/rockchip: disable fetch dte time limit**

- 日期：2026-04-28
- 状态：社区讨论中
- 概括：禁用存在稳定性或安全性问题的功能，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-rockchip/patch/20260428-spu-iommudtefix-v2-1-f592f579e508@pengutronix.de/

**[v2,4/8] iommu/msm: Look up masters per IOMMU instance**

- 日期：2026-04-27
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/devicetree/patch/20260427-mainline-send-v1-sending-v2-4-dcaa9178007b@alex-min.fr/

**[v14,3/5] iommu: Add verisilicon IOMMU driver**

- 日期：2026-04-15
- 状态：社区讨论中
- 概括：新增verisilic，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/linux-rockchip/patch/20260415072349.44237-4-benjamin.gaignard@collabora.com/

**[v8,08/13] iommu/ipmmu-vmsa: Implement suspend/resume callbacks**

- 日期：2026-04-02
- 状态：社区讨论中
- 概括：实现suspend/resume callbacks，完善缺失的功能接口，完善子系统的功能完备性，确保与硬件平台和上层框架的正确协同
- 来源：https://patchwork.kernel.org/project/xen-devel/patch/63b219c3cae5201c5db804f69c3b88ac41c9bdf6.1775125380.git.mykola_kvach@epam.com/

**[v3,3/4] iommu/generic_pt: disable GCOV for iommu_amdv1.o**

- 日期：2026-04-01
- 状态：社区讨论中
- 概括：禁用存在稳定性或安全性问题的功能，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/netdevbpf/patch/20260401142020.1434243-4-khorenko@virtuozzo.com/

**[50/61] iommu: Prefer IS_ERR_OR_NULL over manual NULL check**

- 日期：2026-03-10
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-rockchip/patch/20260310-b4-is_err_or_null-v1-50-bd63b656022d@avm.de/

**▸ 组织：NVIDIA**（2 patches）

**[SERIES] iommu/arm-smmu-v3: Quarantine device upon ATC invalidation timeout** （cover letter，5/9 个 patch 达到代码量阈值）

- 日期：2026-04-16
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（5 个，显示前 5）：
  - iommu: Add iommu_report_device_broken() to quarantine a broken device
  - iommu/arm-smmu-v3: Block ATS upon an ATC invalidation timeout
  - iommu: Pass in reset result to pci_dev_reset_iommu_done()
  - iommu: Change group->devices to RCU-protected list
  - iommu: Defer __iommu_group_free_device() to be outside group->mutex
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/c90693e75c0610da38103a683b558d5596bd843b.1776381841.git.nicolinc@nvidia.com/

**[v2] iommu: Always fill in gather when unmapping**

- 日期：2026-04-02
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-mediatek/patch/0-v2-b24668f107b2+11bbe-iommu_gather_always_jgg@nvidia.com/

**▸ 组织：Microsoft**（1 patches）

**[V2,01/11] iommu/hyperv: rename hyperv-iommu.c to hyperv-irq.c**

- 日期：2026-05-01
- 状态：社区讨论中
- 概括：重命名符号或函数以更清晰地表达其用途和语义，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/20260501004157.3108202-2-mrathor@linux.microsoft.com/

**▸ 组织：Google**（1 patches）

**[SERIES] iommu: Add live update state preservation** （cover letter，13/14 个 patch 达到代码量阈值）

- 日期：2026-04-27
- 状态：社区讨论中
- 概括：新增live update state preservation，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（13 个，显示前 5）：
  - iommu/pages: Add APIs to preserve/unpreserve/restore iommu pages
  - iommupt: Implement preserve/unpreserve/restore callbacks
  - iommu/vt-d: Implement device and iommu preserve/unpreserve ops
  - iommu/vt-d: Restore IOMMU state and reclaimed domain ids
  - iommu: Restore and reattach preserved domains to devices
  - ... 及其他 8 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260427175633.1978233-6-skhawaja@google.com/

---

### ◆ 子系统：RISC-V IOMMU（4 patches）

**▸ 组织：SiFive**（1 patches）

**[v2,2/2] iommu/riscv: create a auxiliary device for HPM**

- 日期：2026-02-08
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20260208063848.3547817-3-zong.li@sifive.com/

**▸ 组织：SpacemiT**（1 patches）

**[SERIES] iommu/riscv: Enable IOMMU DMA mapping support** （cover letter，4/5 个 patch 达到代码量阈值）

- 日期：2026-02-28
- 状态：社区讨论中
- 概括：启用之前被禁用或条件编译的功能特性，持续改进代码质量和功能完备性
- 达到阈值的 patches（4 个，显示前 5）：
  - iommu/riscv: Enable IOMMU DMA mapping support
  - iommu/riscv: Add HPM support for performance monitoring
  - iommu/riscv: Add auxiliary bus framework and HPM device support
  - iommu/riscv: Add SpacemiT T100 IOATC HPM support
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/52E07C3A9B398459+126b1f464ae2a8bfcca6f504c64346541ae4db6f.1772289741.git.lv.zheng@linux.spacemit.com/

**▸ 组织：NVIDIA**（1 patches）

**[SERIES] Support non-leaf and range invalidation features in RISC-V** （cover letter，3/7 个 patch 达到代码量阈值）

- 日期：2026-04-10
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu/riscv: Enable PT_FEAT_DETAILED_GATHER and pass gather to iotlb_inval
  - iommu/riscv: Compute best stride for single invalidation
  - iommu: Split the kdoc comment for struct iommu_iotlb_gather
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/6-v1-54e7264d71b4+17cc3-iommu_riscv_inv_jgg@nvidia.com/

**▸ 组织：Individual Contributor**（1 patches）

**[SERIES] iommu/riscv: Support Svpbmt memory types in generic_pt** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-04-17
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（2 个，显示前 5）：
  - iommupt: Encode IOMMU_MMIO/IOMMU_CACHE via RISC-V Svpbmt bits
  - iommu/riscv: Advertise Svpbmt support to generic page table
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20260417140746.97817-3-fangyu.yu@linux.alibaba.com/

---

### ◆ 子系统：IOMMUFD（4 patches）

**▸ 组织：Kernel.org**（2 patches）

**[SERIES] Add iommufd ioctls to support TSM operations** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-04-27
- 状态：社区讨论中
- 概括：新增iommufd ioctls，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（4 个，显示前 5）：
  - iommufd/tsm: add vdevice TSM bind/unbind ioctl
  - iommufd/vdevice: add TSM guest request ioctl
  - iommufd/device: Associate a kvm pointer to iommufd_device
  - iommufd/viommu: Associate a kvm pointer to iommufd_viommu
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260427061005.901854-4-aneesh.kumar@kernel.org/

**[v2,1/3] iommufd/viommu: Allow associating a KVM VM fd with a vIOMMU**

- 日期：2026-03-09
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260309111704.2330479-2-aneesh.kumar@kernel.org/

**▸ 组织：Intel**（1 patches）

**iommufd: Rename all the idev and idevc variables to hiod and hiodc**

- 日期：2026-04-01
- 状态：社区讨论中
- 概括：重命名符号或函数以更清晰地表达其用途和语义，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260401080354.1347212-1-zhenzhong.duan@intel.com/

**▸ 组织：NVIDIA**（1 patches）

**[SERIES] Add DMA-buf mapping types and convert vfio/iommufd to use them** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-02-18
- 状态：社区讨论中
- 概括：新增dma-buf mapping types and convert vfio/iommufd，扩展功能特性
- 达到阈值的 patches（3 个，显示前 5）：
  - iommufd/selftest: Check multi-phys DMA-buf scenarios
  - iommufd: Use the PAL mapping type instead of a vfio function
  - iommufd: Support DMA-bufs with multiple physical ranges
- 来源：https://patchwork.kernel.org/project/dri-devel/patch/25-v1-b5cab63049c0+191af-dmabuf_map_type_jgg@nvidia.com/

---

### ◆ 子系统：AMD IOMMU（4 patches）

**▸ 组织：Individual Contributor**（2 patches）

**[v2,1/2] iommu/amd-vi: allow disable_iommu() against non-initialized IOMMUs**

- 日期：2026-05-06
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/xen-devel/patch/20260506135514.47310-2-roger.pau@citrix.com/

**[v3] iommu/amd-vi: do not zero IOMMU MMIO region**

- 日期：2026-05-06
- 状态：社区讨论中
- 概括：限制zero iommu mmio region，增加条件判断和安全保护逻辑，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/xen-devel/patch/20260506165157.68567-1-roger.pau@citrix.com/

**▸ 组织：AMD**（1 patches）

**[SERIES] amd_iommu: Support Generation of IOMMU XT interrupts** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-03-02
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（3 个，显示前 5）：
  - amd_iommu: Use switch case to determine mmio register name
  - amd_iommu: Turn on XT support only when guest has enabled it
  - amd_iommu: Generate XT interrupts when xt support is enabled
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260302115130.5903-2-sarunkod@amd.com/

**▸ 组织：Oracle**（1 patches）

**[SERIES] amd_iommu: Fix page size reporting on hugepage mappings** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-03-11
- 状态：社区讨论中
- 概括：修复page size reporting，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（2 个，显示前 5）：
  - amd_iommu: Follow root pointer before page walk and use 1-based levels
  - amd_iommu: Reject non-decreasing NextLevel in fetch_pte()
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260311203943.2309841-2-alejandro.j.jimenez@oracle.com/

---

### ◆ 子系统：IOMMU Page Table（1 patches）

**▸ 组织：ARM**（1 patches）

**[RFC] iommu/io-pgtable: Add support for Arm Mali v10+ GPUs page table format**

- 日期：2026-02-09
- 状态：社区讨论中
- 概括：新增支持 arm mali v10+ gpus page table format，扩展框架的硬件兼容性和功能覆盖范围
- 来源：https://patchwork.kernel.org/project/dri-devel/patch/20260209112542.194140-1-liviu.dudau@arm.com/

---

### ◆ 子系统：IOMMU DMA-API（1 patches）

**▸ 组织：Debian**（1 patches）

**iommu/dma: Rate-limit WARN in iommu_dma_unmap_phys()**

- 日期：2026-02-11
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/netdevbpf/patch/20260211-dma_io_mmu-v1-1-cf89e24437af@debian.org/

---

### ◆ 子系统：ARM SMMU (v1/v2)（1 patches）

**▸ 组织：Qualcomm**（1 patches）

**[v2] iommu/arm-smmu: Use pm_runtime in fault handlers**

- 日期：2026-03-13
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-arm-msm/patch/20260313-smmu-rpm-v2-1-8c2236b402b0@oss.qualcomm.com/

---

### ◆ 子系统：IOMMU SVA/SVM（1 patches）

**▸ 组织：Google**（1 patches）

**[RFC] iommu: Enable per-device SSID space for SVA**

- 日期：2026-04-24
- 状态：社区讨论中
- 概括：启用之前被禁用或条件编译的功能特性，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260424085011.3502295-1-joonwonkang@google.com/

---

### ◆ 子系统：ARM SMMU Acceleration（1 patches）

**▸ 组织：NVIDIA**（1 patches）

**[SERIES] iommu/tegra241-cmdqv: Fix initialization and uAPI related to HYP_OWN** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-03-13
- 状态：社区讨论中
- 概括：修复initializati，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/tegra241-cmdqv: Set supports_cmd op in tegra241_vcmdq_hw_init()
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/7988aa837f02e44c0f436bb236cba0573bd8974f.1773361875.git.nicolinc@nvidia.com/

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

*报告由 Linux Patches Tracker 自动生成 | 2026-05-08 15:38:01*
