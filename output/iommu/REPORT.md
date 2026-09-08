# Linux IOMMU 子系统 Patch 追踪报告

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
| 社区讨论中 | 53 | 98.1% |
| 已合入 | 0 | 0.0% |
| **总计** | **54** | **100%** |

### 按组织分类（TOP 15）

| 组织 | 数量 | 占比 |
|------|------|------|
| Individual Contributor | 19 | 35.2% |
| NVIDIA | 10 | 18.5% |
| Qualcomm | 8 | 14.8% |
| Google | 7 | 13.0% |
| AMD | 3 | 5.6% |
| Kernel.org | 2 | 3.7% |
| Linaro | 1 | 1.9% |
| Microsoft | 1 | 1.9% |
| Red Hat | 1 | 1.9% |
| Oracle | 1 | 1.9% |
| Intel | 1 | 1.9% |

### 按子系统分类

| 子系统 | 数量 | 占比 |
|--------|------|------|
| IOMMU Core | 15 | 27.8% |
| ARM SMMUv3 | 13 | 24.1% |
| AMD IOMMU | 7 | 13.0% |
| RISC-V IOMMU | 4 | 7.4% |
| IOMMUFD | 4 | 7.4% |
| ARM SMMU (v1/v2) | 4 | 7.4% |
| Intel VT-d | 3 | 5.6% |
| ARM SMMU Acceleration | 2 | 3.7% |
| IOMMU DMA-API | 1 | 1.9% |
| IOMMU Page Table | 1 | 1.9% |

## 重点 Patch Top20 清单

### 已合入

暂无。

### 社区讨论

| 厂商 | 简介 |
|------|------|
| NVIDIA | [PATCH v10 00/13] iommu/arm-smmu-v3: Adopt the crashed kernel's stream table for kdump ------围绕 iommu/arm-smmu-v3 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。 |
| Google | [PATCH v4 00/18] iommu: Add live update state preservation ------为 live update 场景保存和恢复设备、IOMMU 或 VFIO 状态，减少内核切换期间设备上下文丢失对虚拟化工作负载的影响。 |
| Google | [PATCH v7 00/24] KVM: arm64: SMMUv3 driver for pKVM (trap and emulate) ------重整 ARM SMMU 的失效处理和批量提交路径，降低无效化延迟并强化异常场景下的同步与错误处理。 |
| NVIDIA | [PATCH v2 00/11] iommu/tegra241-cmdqv: Fix error-interrupt races and VINTF lifecycle bugs ------集中修复 iommu/tegra241-cmdqv 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。 |
| Google | [PATCH v9 00/12] iommu/arm-smmu-v3: Implement Runtime/System Sleep ops ------围绕 iommu/arm-smmu-v3 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。 |
| Qualcomm | [PATCH v1 00/12] iommu: qcom_iommu: implement support for instances on MSM8974 ------补齐 Qualcomm 平台加密或 IOMMU 相关设备树绑定与驱动支持，使新 SoC 的硬件能力可被内核正确发现。 |
| Qualcomm | [PATCH v5 00/17] iommu/riscv: Enable MSI remapping, IOMMU_DMA and VFIO ------完善 RISC-V IOMMU 页表、失效或 DMA 集成能力，补齐架构驱动在虚拟化和设备隔离场景中的关键行为。 |
| NVIDIA | [PATCH v6 00/5] iommufd: Iterate the cache invalidation array in the core ------重整 ARM SMMU 的失效处理和批量提交路径，降低无效化延迟并强化异常场景下的同步与错误处理。 |
| NVIDIA | [PATCH v2 00/9] Use the generic iommu page table for SMMUv3 ------围绕 Use the generic iommu page table for SMMUv3 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。 |
| NVIDIA | [PATCH v2 00/3] iommufd: Fix vDEVICE allocation lifecycle bugs ------集中修复 iommufd 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。 |
| Oracle | [PATCH v2 00/5] amd_iommu: Do not create duplicate MSI capability ------围绕 amd_iommu 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。 |
| Individual Contributor | [PATCH v3 00/10] iommu/riscv: Add hardware dirty tracking for second-stage domains ------完善 RISC-V IOMMU 页表、失效或 DMA 集成能力，补齐架构驱动在虚拟化和设备隔离场景中的关键行为。 |
| Intel | [PATCH v5 00/6] intel_iommu: Enable PRQ support for passthrough device ------围绕 intel_iommu 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。 |
| AMD | [PATCH v4 00/7] Add support for AMD IOMMU GAPPI ------围绕 Add support for AMD IOMMU GAPPI 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。 |
| Qualcomm | [PATCH v2 00/6] iommu/qcom: Misc Fixes ------补齐 Qualcomm 平台加密或 IOMMU 相关设备树绑定与驱动支持，使新 SoC 的硬件能力可被内核正确发现。 |
| Red Hat | [PATCH v1 00/44] amd_iommu: Fix opcode reported in invalid command handling ------集中修复 amd_iommu 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。 |
| AMD | [PATCH v2 00/7] acpi_build: Refactor and cleanup AMD IVRS build ------围绕 acpi_build 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。 |
| Individual Contributor | [PATCH v1 00/7] riscv: iommu: Add QoS ID support for resctrl device assignment ------完善 RISC-V IOMMU 页表、失效或 DMA 集成能力，补齐架构驱动在虚拟化和设备隔离场景中的关键行为。 |
| Individual Contributor | [PATCH v1 00/3] iommu/iova: convert from rbtree to maple tree ------围绕 iommu/iova 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。 |
| NVIDIA | [PATCH v5 00/18] iommu/arm-smmu-v3: Quarantine device upon ATC invalidation timeout ------重整 ARM SMMU 的失效处理和批量提交路径，降低无效化延迟并强化异常场景下的同步与错误处理。 |

---

## 已合入 Patches

暂无。

## 社区讨论中 Patches

### ◆ 子系统：IOMMU Core（14 patches）

**▸ 组织：Individual Contributor**（10 patches）

**[v12,08/13] iommu/ipmmu-vmsa: Implement suspend/resume callbacks**

- 日期：2026-08-27
- 状态：社区讨论中
- 概括：实现suspend/resume callbacks，完善缺失的功能接口，完善子系统的功能完备性，确保与硬件平台和上层框架的正确协同
- 来源：https://patchwork.kernel.org/project/xen-devel/patch/1f036e7ad5ad6efba635ca029b0fab133300603a.1787838455.git.mykola_kvach@epam.com/

**[SERIES] iommu/rockchip: turn rk_iommu_ops into data** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-25
- 状态：社区讨论中
- 概括：围绕 iommu/rockchip 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/rockchip: Reject unsupported physical addresses
  - iommu/rockchip: Reduce rk_iommu_ops to pure data
- 来源：https://patchwork.kernel.org/project/linux-rockchip/patch/20260825092132.154150-3-xxm@rock-chips.com/

**[SERIES] IOMMU driver improvements for modern Exynos SysMMUs** （cover letter，2/4 个 patch 达到代码量阈值）

- 日期：2026-08-20
- 状态：社区讨论中
- 概括：重整 ARM SMMU 的失效处理和批量提交路径，降低无效化延迟并强化异常场景下的同步与错误处理。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/exynos: detect SysMMUs without BLOCK mode
  - iommu/exynos: decode the v7 fault transaction info
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260820-exynos-iommu-fixes-v1-1-6bbcd673bb15@gmail.com/

**[SERIES] iommu/iova: convert from rbtree to maple tree** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-08-18
- 状态：社区讨论中
- 概括：围绕 iommu/iova 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu/iova: defer maple tree erase on GFP_ATOMIC failure
  - iommu/iova: convert from rbtree to maple tree
  - iommu/iova: add KUnit test suite
- 来源：https://patchwork.kernel.org/project/linux-mm/patch/20260818152505.1057922-3-riel@surriel.com/

**iommu/msm: limit the per-master Machine ID list**

- 日期：2026-07-22
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-arm-msm/patch/20260722041619.17735-1-pengpeng@iscas.ac.cn/

**[SERIES] accel/rocket: RK3576 NPU (RKNN) enablement** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-07-18
- 状态：社区讨论中
- 概括：归纳 accel/rocket 系列中的关联改动，重点调整核心接口、驱动流程和异常处理逻辑。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/rockchip: take all DT clocks
  - iommu/rockchip: clear stale page faults before enabling stall
- 来源：https://patchwork.kernel.org/project/linux-rockchip/patch/20260718031146.3368811-5-gahing@gahingwoo.com/

**[RFC,4/9] iommu/rockchip: skip orphaned-fault banks in rk_iommu_is_stall_active**

- 日期：2026-07-17
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260717085220.3212274-5-gahing@gahingwoo.com/

**[RFC,5/9] iommu/rockchip: skip orphaned-fault banks in CMD_ENABLE_STALL dispatch**

- 日期：2026-07-17
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-rockchip/patch/20260717085220.3212274-6-gahing@gahingwoo.com/

**[SERIES] riscv: iommu: Add QoS ID support for resctrl device assignment** （cover letter，3/4 个 patch 达到代码量阈值）

- 日期：2026-07-14
- 状态：社区讨论中
- 概括：完善 RISC-V IOMMU 页表、失效或 DMA 集成能力，补齐架构驱动在虚拟化和设备隔离场景中的关键行为。
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu: Add group lookup by ID
  - iommu/riscv: Program QoS IDs for assigned groups
  - iommu/riscv: Expose global QoS IDs in sysfs
- 来源：https://patchwork.kernel.org/project/linux-kselftest/patch/20260714130657.46963-2-zhangzhanpeng.jasper@bytedance.com/

**[RFC,09/14] iommu: lazy-populate iommu_group reserved_regions/type attrs**

- 日期：2026-07-02
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kexec/patch/20260702175114.24659-5-sakacpav@amazon.de/

**▸ 组织：Qualcomm**（3 patches）

**[SERIES] Fix GPU and display on ARM32 platforms using the MSM IOMMU** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-07-30
- 状态：社区讨论中
- 概括：集中修复 Fix GPU and display on ARM32 platforms using the MSM IOMMU 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/msm: track a context master per device and IOMMU
  - iommu/msm: use the IOMMU device for page table allocation
- 来源：https://patchwork.kernel.org/project/linux-rockchip/patch/20260730-fix-qcom-smmu-v2-1-18e0daf2d836@oss.qualcomm.com/

**[3/8] iommu/fsl: use platform_device_set_fwnode()**

- 日期：2026-07-20
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/alsa-devel/patch/20260720-pdev-set-fwnode-instead-of-of-node-v1-3-2dee93f42c54@oss.qualcomm.com/

**[v3,09/20] iommu/fsl: use platform_device_set_of_node()**

- 日期：2026-07-06
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/dri-devel/patch/20260706-pdev-fwnode-ref-v3-9-1ff028e33779@oss.qualcomm.com/

**▸ 组织：Google**（1 patches）

**[SERIES] iommu: Add live update state preservation** （cover letter，16/16 个 patch 达到代码量阈值）

- 日期：2026-08-08
- 状态：社区讨论中
- 概括：为 live update 场景保存和恢复设备、IOMMU 或 VFIO 状态，减少内核切换期间设备上下文丢失对虚拟化工作负载的影响。
- 达到阈值的 patches（16 个，显示前 5）：
  - iommu: Implement IOMMU Live update FLB callbacks
  - iommu/pages: Add APIs to preserve/unpreserve/restore iommu pages
  - iommupt: Implement preserve/unpreserve/restore callbacks
  - iommu: Implement IOMMU domain preservation
  - iommu: Implement device and IOMMU HW preservation
  - ... 及其他 11 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260808022723.3893618-3-skhawaja@google.com/

---

### ◆ 子系统：ARM SMMUv3（13 patches）

**▸ 组织：NVIDIA**（6 patches）

**[SERIES] iommu/arm-smmu-v3: Adopt the crashed kernel's stream table for kdump** （cover letter，10/13 个 patch 达到代码量阈值）

- 日期：2026-08-30
- 状态：社区讨论中
- 概括：围绕 iommu/arm-smmu-v3 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。
- 达到阈值的 patches（10 个，显示前 5）：
  - iommu/arm-smmu-v3: Retain CR0_SMMUEN during kdump device reset
  - iommu/arm-smmu-v3: Skip RMR bypass for kdump adoption
  - iommu/arm-smmu-v3-kdump: Reserve crashed kernel's ASIDs and VMIDs
  - iommu/arm-smmu-v3: Add ARM_SMMU_OPT_KDUMP_ADOPT for kdump kernel
  - iommu/arm-smmu-v3: Detect ARM_SMMU_OPT_KDUMP_ADOPT in probe()
  - ... 及其他 5 个 patch
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/8280230c0906b4c62635c5eb2760bd0e25bbd1d1.1788130528.git.nicolinc@nvidia.com/

**[SERIES] Use the generic iommu page table for SMMUv3** （cover letter，5/9 个 patch 达到代码量阈值）

- 日期：2026-08-12
- 状态：社区讨论中
- 概括：围绕 Use the generic iommu page table for SMMUv3 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。
- 达到阈值的 patches（5 个，显示前 5）：
  - iommu/arm-smmu-v3: Move the DMA API comment to flush_iotlb_all
  - iommu/arm-smmu-v3: Use the generic iommu page table
  - iommupt/armv8: Add DBM support
  - iommupt/armv8: Implement the iommu specific components
  - iommupt/armv8: Add the 64 bit ARMv8 page table format
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/1-v2-563ee63886f0+1209-iommupt_armv8_jgg@nvidia.com/

**[v5,1/6] iommu/arm-smmu-v3: Support IDR5.DS and widen the TLBI SCALE field**

- 日期：2026-07-28
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/1b35fa8c417a21ac80a4a3f19db34d81ef6ca490.1785258826.git.nicolinc@nvidia.com/

**[SERIES] iommu/arm-smmu-v3: Tegra264 invalidation workaround** （cover letter，2/4 个 patch 达到代码量阈值）

- 日期：2026-07-26
- 状态：社区讨论中
- 概括：重整 ARM SMMU 的失效处理和批量提交路径，降低无效化延迟并强化异常场景下的同步与错误处理。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/arm-smmu-v3: Enable CFGI/TLBI-repeat workaround on Tegra264
  - iommu/arm-smmu-v3-iommufd: Report CFGI/TLBI-repeat erratum
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260726081904.1408859-2-amhetre@nvidia.com/

**[3/7] iommupt: Add the 64 bit ARMv8 page table format**

- 日期：2026-07-06
- 状态：社区讨论中
- 概括：新增the 64 bit armv8 page table format，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/3-v1-807e2d1a5efb+e1-iommupt_armv8_jgg@nvidia.com/

**[SERIES] iommu/arm-smmu-v3: Quarantine device upon ATC invalidation timeout** （cover letter，4/12 个 patch 达到代码量阈值）

- 日期：2026-07-03
- 状态：社区讨论中
- 概括：重整 ARM SMMU 的失效处理和批量提交路径，降低无效化延迟并强化异常场景下的同步与错误处理。
- 达到阈值的 patches（4 个，显示前 5）：
  - iommu: Convert gdev->blocked from bool to enum gdev_blocked
  - iommu/arm-smmu-v3: Don't rb_erase() a never-inserted stream node
  - iommu: Pass in reset result to pci_dev_reset_iommu_done()
  - iommu/arm-smmu-v3: Thread arm_smmu_master_domain on a per-master list
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/05da17325cf02758fb0eb3bde34c8ef2a22decbe.1783044582.git.nicolinc@nvidia.com/

**▸ 组织：Google**（4 patches）

**[SERIES] iommu/arm-smmu-v3: Fixes reported by Sashiko** （cover letter，2/7 个 patch 达到代码量阈值）

- 日期：2026-08-28
- 状态：社区讨论中
- 概括：集中修复 iommu/arm-smmu-v3 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/arm-smmu-v3: Ensure L2 tables are visible before L1 ptrs
  - iommu/arm-smmu-v3: Prevent rbtree corruption from duplicate streams
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260828125409.1921538-4-smostafa@google.com/

**iommu/arm-smmu-v3: Convert to use atomic poll timeout**

- 日期：2026-07-28
- 状态：社区讨论中
- 概括：迁移to use atomic poll timeout，适配新的接口规范，保持子系统与内核主线的兼容性，适应 API 和框架的演进方向
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260728211123.1059708-1-praan@google.com/

**[SERIES] iommu/arm-smmu-v3: Implement Runtime/System Sleep ops** （cover letter，7/12 个 patch 达到代码量阈值）

- 日期：2026-07-28
- 状态：社区讨论中
- 概括：围绕 iommu/arm-smmu-v3 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。
- 达到阈值的 patches（7 个，显示前 5）：
  - iommu/arm-smmu-v3: Refactor arm_smmu_setup_irqs
  - iommu/tegra241-cmdqv: Restore PROD and CONS after resume
  - iommu/arm-smmu-v3: Cache and restore MSI config
  - iommu/arm-smmu-v3: Enable pm_runtime and setup devlinks
  - iommu/arm-smmu-v3: Implement pm_runtime & system sleep ops
  - ... 及其他 2 个 patch
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260728210928.1050849-2-praan@google.com/

**[SERIES] KVM: arm64: SMMUv3 driver for pKVM (trap and emulate)** （cover letter，17/17 个 patch 达到代码量阈值）

- 日期：2026-07-15
- 状态：社区讨论中
- 概括：重整 ARM SMMU 的失效处理和批量提交路径，降低无效化延迟并强化异常场景下的同步与错误处理。
- 达到阈值的 patches（17 个，显示前 5）：
  - iommu/arm-smmu-v3: Split code with hyp
  - iommu/arm-smmu-v3: Move TLB range invalidation into common code
  - iommu/arm-smmu-v3-kvm: Add SMMUv3 driver
  - iommu/arm-smmu-v3-kvm: Probe SMMU HW
  - iommu/arm-smmu-v3-kvm: Add MMIO emulation
  - ... 及其他 12 个 patch
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260715115906.2664882-4-smostafa@google.com/

**▸ 组织：Kernel.org**（1 patches）

**[v3] iommu/arm-smmu-v3: Shrink command/event/PRI queues in kdump kernel**

- 日期：2026-07-06
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260706084708.8072-1-kas@kernel.org/

**▸ 组织：Linaro**（1 patches）

**[2/2] iommu/arm-smmu-v3: Override for Inst/Data attribute**

- 日期：2026-07-24
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260724-arm-smmu-v3-instcfg-override-v1-2-e7acf4a8a525@linaro.org/

**▸ 组织：Individual Contributor**（1 patches）

**[RFC] iommu/arm-smmu-v3: Allow nested attach for PCI bridges without vDEVICE**

- 日期：2026-08-14
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/PA1P190MB25578C482C8A3B06A4DCC6FDDBDA2@PA1P190MB2557.EURP190.PROD.OUTLOOK.COM/

---

### ◆ 子系统：AMD IOMMU（7 patches）

**▸ 组织：AMD**（3 patches）

**[v2] iommu/amd: Force identity mode for selected GPUs only**

- 日期：2026-08-24
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/20260824085821.5422-1-vasant.hegde@amd.com/

**[SERIES] Add support for AMD IOMMU GAPPI** （cover letter，4/5 个 patch 达到代码量阈值）

- 日期：2026-08-21
- 状态：社区讨论中
- 概括：围绕 Add support for AMD IOMMU GAPPI 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。
- 达到阈值的 patches（4 个，显示前 5）：
  - iommu/amd: Provide kernel command line option to enable GAPPI
  - iommu/amd: KVM: SVM: Rename cpu to apicid in IOMMU interface
  - iommu/amd: KVM: SVM: Rename ga_log_intr to wakeup_intr in IOMMU interface
  - iommu/amd: Program guest-mode IRTEs for GAPPI wakeup when IRTE[IsRun] = 0
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260821055611.27138-8-sarunkod@amd.com/

**[SERIES] acpi_build: Refactor and cleanup AMD IVRS build** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-08-07
- 状态：社区讨论中
- 概括：围绕 acpi_build 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。
- 达到阈值的 patches（1 个，显示前 5）：
  - amd_iommu: Return empty efr for stub call
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260807061250.27739-2-sarunkod@amd.com/

**▸ 组织：Individual Contributor**（1 patches）

**[1/2] amd_iommu: Honor DTE[IR] and DTE[IW] when DTE[Mode] is 0**

- 日期：2026-07-18
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260718175208.118721-2-danielpaziyski@gmail.com/

**▸ 组织：Red Hat**（1 patches）

**[SERIES] amd_iommu: Fix opcode reported in invalid command handling** （cover letter，4/6 个 patch 达到代码量阈值）

- 日期：2026-07-05
- 状态：社区讨论中
- 概括：集中修复 amd_iommu 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。
- 达到阈值的 patches（4 个，显示前 5）：
  - intel_iommu: Correctly set pt bit in extended capability register
  - amd_iommu: Decode XT interrupt control register without bitfields
  - amd_iommu: Return int from page walk status helpers
  - amd_iommu: Decode IRTEs without bitfields
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/0611d393031f9941fcfaf3f17c3ac2b7a0ea00d1.1783261895.git.mst@redhat.com/

**▸ 组织：Oracle**（1 patches）

**[SERIES] amd_iommu: Do not create duplicate MSI capability** （cover letter，5/5 个 patch 达到代码量阈值）

- 日期：2026-07-24
- 状态：社区讨论中
- 概括：围绕 amd_iommu 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。
- 达到阈值的 patches（5 个，显示前 5）：
  - amd_iommu: Define MMIO register masks
  - amd_iommu: Do not latch unsupported GA log status bits
  - amd_iommu: Do not create duplicate MSI capability
  - amd_iommu: Make extended feature register read-only
  - amd_iommu: Use full BDF when reporting page faults
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260724223216.108667-4-dongli.zhang@oracle.com/

**▸ 组织：Google**（1 patches）

**[SERIES] iommu/amd: Refactors for ATS robustness** （cover letter，1/4 个 patch 达到代码量阈值）

- 日期：2026-08-24
- 状态：社区讨论中
- 概括：集中修复 iommu/amd 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/amd: Refactor device probe and capability initialization
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/20260824122347.1588592-2-praan@google.com/

---

### ◆ 子系统：RISC-V IOMMU（4 patches）

**▸ 组织：Individual Contributor**（3 patches）

**[SERIES] iommu/riscv: Add hardware dirty tracking for second-stage domains** （cover letter，4/7 个 patch 达到代码量阈值）

- 日期：2026-08-21
- 状态：社区讨论中
- 概括：完善 RISC-V IOMMU 页表、失效或 DMA 集成能力，补齐架构驱动在虚拟化和设备隔离场景中的关键行为。
- 达到阈值的 patches（4 个，显示前 5）：
  - iommu/riscv: use data structure instead of individual values
  - iommupt: Add RISC-V Second-stage (iohgatp) page table support
  - iommu/riscv: support GSCID and GVMA invalidation command
  - iommu/riscv: Pre-enable GADE for second-stage domains
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20260821132749.82070-5-fangyu.yu@linux.alibaba.com/

**[v3] iommu/riscv: Use 32-bit MMIO accesses for 64-bit registers**

- 日期：2026-07-13
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20260713122903.9458-1-zhangzhanpeng.jasper@bytedance.com/

**[RFC,1/3] iommu/riscv: Complete MRIF MSI PTE setup**

- 日期：2026-07-01
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260701040017.42707-2-zhangzhanpeng.jasper@bytedance.com/

**▸ 组织：Qualcomm**（1 patches）

**[SERIES] iommu/riscv: Enable MSI remapping, IOMMU_DMA and VFIO** （cover letter，11/11 个 patch 达到代码量阈值）

- 日期：2026-08-31
- 状态：社区讨论中
- 概括：完善 RISC-V IOMMU 页表、失效或 DMA 集成能力，补齐架构驱动在虚拟化和设备隔离场景中的关键行为。
- 达到阈值的 patches（11 个，显示前 5）：
  - iommufd: Convert struct iommufd_sw_msi_maps to a growable bitmap
  - iommu/dma: Enable IOMMU_DMA for 64-bit RISC-V
  - iommu/riscv: Reserve an MSI IOVA window for iommufd
  - iommu/riscv: Report cache coherency capability
  - iommu/dma: Prepare MSI physical address lists
  - ... 及其他 6 个 patch
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20260831145943.313726-3-andrew.jones@oss.qualcomm.com/

---

### ◆ 子系统：IOMMUFD（4 patches）

**▸ 组织：NVIDIA**（2 patches）

**[SERIES] iommufd: Iterate the cache invalidation array in the core** （cover letter，5/5 个 patch 达到代码量阈值）

- 日期：2026-08-30
- 状态：社区讨论中
- 概括：重整 ARM SMMU 的失效处理和批量提交路径，降低无效化延迟并强化异常场景下的同步与错误处理。
- 达到阈值的 patches（5 个，显示前 5）：
  - iommufd/selftest: Convert cache invalidation mocks to the core array loop
  - iommufd: Iterate the cache invalidation array in the core
  - iommu/arm-smmu-v3-iommufd: Reject unsupported bits in invalidation commands
  - iommu/vt-d: Convert nested cache invalidation to the core array loop
  - iommu/arm-smmu-v3-iommufd: Convert cache invalidation to the core array loop
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/535f3b97e16c437f1df0c988a96229f623142ee9.1788127877.git.nicolinc@nvidia.com/

**[SERIES] iommufd: Fix vDEVICE allocation lifecycle bugs** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-07-06
- 状态：社区讨论中
- 概括：集中修复 iommufd 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommufd/viommu: Publish a vDEVICE only after vdevice_init() succeeds
  - iommu/arm-smmu-v3-iommufd: Require exactly one Stream ID for a vDEVICE
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/e903f775d491296a525097e2a90b3eb6a47cf2ef.1783311134.git.nicolinc@nvidia.com/

**▸ 组织：Google**（1 patches）

**[2/2] iommufd: Periodically reschedule when unmapping**

- 日期：2026-07-14
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260714210303.3967981-3-aaronlewis@google.com/

**▸ 组织：Individual Contributor**（1 patches）

**[SERIES] KVM: selftests: sev_smoke_test: Only run VM types the host offers** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-07-20
- 状态：社区讨论中
- 概括：完善 DMA-BUF 相关映射、导出和权限控制流程，增强用户态共享设备内存时的资源管理和安全边界。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommufd: Plumb dma-buf memory-type (RAM vs MMIO) through the phys map
  - iommufd: Look up private-interconnect phys via exporter symbols
- 来源：https://patchwork.kernel.org/project/linux-kselftest/patch/a7ca2d885903679dc63c85620bff72fea21f5c18.1784545391.git.dwmw@amazon.co.uk/

---

### ◆ 子系统：ARM SMMU (v1/v2)（4 patches）

**▸ 组织：Qualcomm**（3 patches）

**[SERIES] iommu: qcom_iommu: implement support for instances on MSM8974** （cover letter，9/10 个 patch 达到代码量阈值）

- 日期：2026-08-09
- 状态：社区讨论中
- 概括：补齐 Qualcomm 平台加密或 IOMMU 相关设备树绑定与驱动支持，使新 SoC 的硬件能力可被内核正确发现。
- 达到阈值的 patches（9 个，显示前 5）：
  - iommu: qcom_iommu: extract context bank programming into a helper
  - iommu: qcom_iommu: support the short-descriptor pagetable format
  - iommu: qcom_iommu: handle the SMMU global register space
  - iommu: qcom_iommu: support non-TZ-managed instances
  - iommu: qcom_iommu: restore context bank state after power collapse
  - ... 及其他 4 个 patch
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260809-msm8974-iommu-upstream-v1-2-87f5cd492560@oss.qualcomm.com/

**[v4] iommu/arm-smmu: Use pm_runtime in fault handlers**

- 日期：2026-08-06
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260806-smmu-rpm-v4-1-8183d007331c@oss.qualcomm.com/

**[SERIES] iommu/qcom: Misc Fixes** （cover letter，4/6 个 patch 达到代码量阈值）

- 日期：2026-07-17
- 状态：社区讨论中
- 概括：补齐 Qualcomm 平台加密或 IOMMU 相关设备树绑定与驱动支持，使新 SoC 的硬件能力可被内核正确发现。
- 达到阈值的 patches（4 个，显示前 5）：
  - iommu/qcom: Use devm_pm_runtime_enable() in qcom_iommu_device_probe()
  - iommu/qcom: Check pm_runtime_resume_and_get() return in probe
  - iommu/qcom: Publish pgtbl_ops before releasing init_mutex
  - iommu/qcom: Enable clocks before hardware access in qcom_iommu_ctx_probe()
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260717144608.3216274-2-mukesh.ojha@oss.qualcomm.com/

**▸ 组织：Individual Contributor**（1 patches）

**[SERIES] Enable LPAC on a7xx series GPUs** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-07-05
- 状态：社区讨论中
- 概括：补齐 Qualcomm 平台加密或 IOMMU 相关设备树绑定与驱动支持，使新 SoC 的硬件能力可被内核正确发现。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu: arm-smmu-qcom: Configure lpac device with split address space
- 来源：https://patchwork.kernel.org/project/dri-devel/patch/20260705-descriptive-name-lpac-upstream-v1-1-01d50c3e0c99@gmail.com/

---

### ◆ 子系统：Intel VT-d（3 patches）

**▸ 组织：Individual Contributor**（2 patches）

**[v2] intel_iommu: Expose SMPWC when SVM is enabled**

- 日期：2026-08-08
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260808153626.873965-1-clement.mathieu--drif@bull.com/

**[v2] intel_iommu: Check address mask before using it in pasid-based iotlb invalidation**

- 日期：2026-07-24
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260724111424.376680-1-clement.mathieu--drif@bull.com/

**▸ 组织：Intel**（1 patches）

**[SERIES] intel_iommu: Enable PRQ support for passthrough device** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-08-31
- 状态：社区讨论中
- 概括：围绕 intel_iommu 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。
- 达到阈值的 patches（4 个，显示前 5）：
  - intel_iommu_accel: teardown FAULTQ resources in bottom half
  - intel_iommu_accel: Guard VTDAccelPASIDCacheEntry definition
  - intel_iommu_accel: Accept PRQ response for passthrough device
  - intel_iommu_accel: Add PRQ injection for passthrough device
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260831095200.1279366-7-zhenzhong.duan@intel.com/

---

### ◆ 子系统：ARM SMMU Acceleration（2 patches）

**▸ 组织：NVIDIA**（2 patches）

**[v3] iommu/tegra241-cmdqv: Reject a VCMDQ base above the 48-bit hardware limit**

- 日期：2026-07-29
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260729220329.805417-1-nicolinc@nvidia.com/

**[SERIES] iommu/tegra241-cmdqv: Fix error-interrupt races and VINTF lifecycle bugs** （cover letter，5/11 个 patch 达到代码量阈值）

- 日期：2026-07-14
- 状态：社区讨论中
- 概括：集中修复 iommu/tegra241-cmdqv 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。
- 达到阈值的 patches（5 个，显示前 5）：
  - iommu/tegra241-cmdqv: Publish an LVCMDQ only after it is fully initialized
  - iommu/tegra241-cmdqv: Reject a vSID wider than the SID_MATCH field
  - iommu/tegra241-cmdqv: Don't fall back to a freed smmu after devm_krealloc()
  - iommu/tegra241-cmdqv: Require exactly one Stream ID for a vSID
  - iommu/tegra241-cmdqv: Warn on a VCMDQ base above the 48-bit hardware limit
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/3e0d9156cd7ade5a5ee0b9a63a326dc324866ddf.1784059577.git.nicolinc@nvidia.com/

---

### ◆ 子系统：IOMMU DMA-API（1 patches）

**▸ 组织：Kernel.org**（1 patches）

**[v8,03/23] iommu/dma: Check atomic pool allocation result directly**

- 日期：2026-07-17
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260717180442.110954-4-aneesh.kumar@kernel.org/

---

### ◆ 子系统：IOMMU Page Table（1 patches）

**▸ 组织：Qualcomm**（1 patches）

**[v4] iommu/io-pgtable-arm: Add support for contiguous hint bit**

- 日期：2026-08-04
- 状态：社区讨论中
- 概括：新增支持 contiguous hint bit，扩展框架的硬件兼容性和功能覆盖范围，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260804-iommu_contig_hint-v4-1-d7a47ed5db98@oss.qualcomm.com/

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

*报告由 Linux Patches Tracker 自动生成 | 2026-09-08 15:02:33*
