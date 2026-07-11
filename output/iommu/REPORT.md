# Linux IOMMU 子系统 Patch 追踪报告

---

## 报告信息

| 项目 | 内容 |
|------|------|
| 数据来源 | patchwork.kernel.org |
| 生成日期 | 2026-07-11 |
| 报告区间 | 2026-05-01 至 2026-06-30 |
| 仓库 | [https://github.com/IAMHCHCH/linux-patches-tracker](https://github.com/IAMHCHCH/linux-patches-tracker) |

---

## 统计概览

### 按状态分类

| 状态 | 数量 | 占比 |
|------|------|------|
| 社区讨论中 | 55 | 87.3% |
| 已合入 | 3 | 4.8% |
| **总计** | **63** | **100%** |

### 按组织分类（TOP 15）

| 组织 | 数量 | 占比 |
|------|------|------|
| Individual Contributor | 18 | 28.6% |
| NVIDIA | 15 | 23.8% |
| Google | 6 | 9.5% |
| Qualcomm | 5 | 7.9% |
| Microsoft | 4 | 6.3% |
| Huawei | 3 | 4.8% |
| AMD | 3 | 4.8% |
| Oracle | 3 | 4.8% |
| Intel | 3 | 4.8% |
| Debian | 1 | 1.6% |
| SiFive | 1 | 1.6% |
| Kernel.org | 1 | 1.6% |

### 按子系统分类

| 子系统 | 数量 | 占比 |
|--------|------|------|
| ARM SMMUv3 | 17 | 27.0% |
| IOMMU Core | 11 | 17.5% |
| RISC-V IOMMU | 9 | 14.3% |
| AMD IOMMU | 8 | 12.7% |
| IOMMUFD | 6 | 9.5% |
| ARM SMMU (v1/v2) | 4 | 6.3% |
| Intel VT-d | 4 | 6.3% |
| IOMMU Page Table | 2 | 3.2% |
| IOMMU SVA/SVM | 1 | 1.6% |
| ARM SMMU Acceleration | 1 | 1.6% |
## 已合入 Patches

### ◆ 子系统：IOMMUFD（2 patches）

**▸ 组织：NVIDIA**（2 patches）

**[SERIES] iommufd: Cache invalidation hardening and SMMUv3 batching rework** （cover letter，3/4 个 patch 达到代码量阈值）

- 日期：2026-06-03
- 状态：已合入
- 概括：重写重新设计部分实现，优化数据流和处理逻辑，持续改进代码质量和功能完备性
- 达到阈值的 patches（3 个，显示前 5）：
  - iommufd: Set upper bounds on cache invalidation entry_num and entry_len
  - iommu/arm-smmu-v3: Process vIOMMU invalidations in batches
  - iommu: Avoid copying the user array twice in the full-array copy helper
- 来源：https://patchwork.kernel.org/project/linux-kselftest/patch/9ae78ed8e64afbb2f2df27d03466380061adf7d9.1780521606.git.nicolinc@nvidia.com/

**[SERIES] iommufd: Fix bugs in eventq fops_read paths** （cover letter，3/7 个 patch 达到代码量阈值）

- 日期：2026-06-01
- 状态：已合入
- 概括：修复相关功能缺陷或逻辑错误，确保操作行为符合预期规范，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（3 个，显示前 5）：
  - iommufd: Reject invalid read count in iommufd_veventq_fops_read()
  - iommufd: Avoid partial fault group delivery in iommufd_fault_fops_read()
  - iommufd: Reject invalid read count in iommufd_fault_fops_read()
- 来源：https://patchwork.kernel.org/project/linux-kselftest/patch/25d29feac909e36f78c145fa99ef2d4cb7a415da.1780343944.git.nicolinc@nvidia.com/

---

### ◆ 子系统：RISC-V IOMMU（1 patches）

**▸ 组织：NVIDIA**（1 patches）

**[SERIES] Support non-leaf and range invalidation features in RISC-V** （cover letter，4/8 个 patch 达到代码量阈值）

- 日期：2026-05-08
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（4 个，显示前 5）：
  - iommu/riscv: Compute best stride for single invalidation
  - iommu/riscv: Include the dword number in RISCV_IOMMU_CMD macros
  - iommu: Split the kdoc comment for struct iommu_iotlb_gather
  - iommu/riscv: Enable PT_FEAT_DETAILED_GATHER and pass gather to iotlb_inval
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/3-v2-b5156f657dc1+25f-iommu_riscv_inv_jgg@nvidia.com/

---

## 社区讨论中 Patches

### ◆ 子系统：ARM SMMUv3（16 patches）

**▸ 组织：NVIDIA**（8 patches）

**iommu/arm-smmu-v3: Declare eats_s1chk and eats_trans as host-endian u64**

- 日期：2026-06-15
- 状态：社区讨论中
- 概括：将 arm_smmu_get_ste_update_safe 中的局部变量 eats_s1chk 和 eats_trans 的类型从 `__le64` 改为宿主字节序的 `u64`。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260615194533.3290010-1-nicolinc@nvidia.com/

**[SERIES] iommu/arm-smmu-v3: Tegra264 invalidation workaround** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-06-09
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/arm-smmu-v3: Detect Tegra264 erratum
  - iommu/arm-smmu-v3: Issue CFGI/TLBI twice on Tegra264
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260609073204.1760077-3-amhetre@nvidia.com/

**[SERIES] iommu/arm-smmu-v3: Add PRI support** （cover letter，7/9 个 patch 达到代码量阈值）

- 日期：2026-05-28
- 状态：社区讨论中
- 概括：新增pri support，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（7 个，显示前 5）：
  - iommu/arm-smmu-v3: Factor out __queue_empty() and __queue_consumed()
  - iommu/arm-smmu-v3: Drain in-flight fault handlers
  - iommu/arm-smmu-v3: Submit CMDQ_OP_PRI_RESP for IOPF event
  - iommu/arm-smmu-v3: Allocate IOPF queue for ARM_SMMU_FEAT_PRI
  - iommu/arm-smmu-v3: Support PRI Page Request in arm_smmu_handle_ppr()
  - ... 及其他 2 个 patch
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/e4e48ebe432c397ad5bd3f3292ceee24a233fbdd.1779944354.git.nicolinc@nvidia.com/

**[v6,3/3] iommu/arm-smmu-v3: Allow ATS to be always on**

- 日期：2026-05-21
- 状态：社区讨论中
- 概括：为支持设备要求ATS始终开启的场景，在ATS强制开启时即使没有PASID也分配CD表并设置S1DSS为bypass，利用EATS实现ATS持续生效。
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/18bb6f421b3be891caa8f1fb50f3a4d56b52d5be.1779392420.git.nicolinc@nvidia.com/

**[SERIES] Organize the SMMUv3 invalidation flow so iommupt can use it** （cover letter，8/8 个 patch 达到代码量阈值）

- 日期：2026-05-18
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（8 个，显示前 5）：
  - iommu/arm-smmu-v3: Keep track in the arm_smmu_invs if RIL is used
  - iommu/arm-smmu-v3: Optimize range invalidation for latency
  - iommu/arm-smmu-v3: Pass the parameters for the invalidation in a struct
  - iommu/arm-smmu-v3: Change how the tlbi describes the invalidation
  - iommu/arm-smmu-v3: Support the DS expansion of RIL's SCALE
  - ... 及其他 3 个 patch
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/4-v1-5b1ac97a5403+6588f-smmu_tlbi_jgg@nvidia.com/

**[SERIES] Remove SMMUv3 struct arm_smmu_cmdq_ent** （cover letter，6/9 个 patch 达到代码量阈值）

- 日期：2026-05-13
- 状态：社区讨论中
- 概括：移除smmuv3 struct arm_smmu_cmdq_ent，清理冗余或过时的代码，精简代码库规模，降低后续维护的复杂度和引入回归问题的风险
- 达到阈值的 patches（6 个，显示前 5）：
  - iommu/arm-smmu-v3: Use the HW arm_smmu_cmd in cmdq selection functions
  - iommu/arm-smmu-v3: Use the HW arm_smmu_cmd in cmdq submission functions
  - iommu/arm-smmu-v3: Directly encode CMDQ_OP_ATC_INV
  - iommu/arm-smmu-v3: Directly encode simple commands
  - iommu/arm-smmu-v3: Directly encode TLBI commands
  - ... 及其他 1 个 patch
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/2-v2-47b2bf710ad5+716ac-smmu_no_cmdq_ent_jgg@nvidia.com/

**[SERIES] iommu/arm-smmu-v3: Fix device crash on kdump kernel** （cover letter，5/6 个 patch 达到代码量阈值）

- 日期：2026-05-10
- 状态：社区讨论中
- 概括：修复device crash，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（5 个，显示前 5）：
  - iommu/arm-smmu-v3: Add arm_smmu_kdump_adopt_strtab() for kdump
  - iommu/arm-smmu-v3: Retain CR0_SMMUEN during kdump device reset
  - iommu/arm-smmu-v3: Skip EVTQ/PRIQ setup in kdump kernel
  - iommu/arm-smmu-v3: Detect ARM_SMMU_OPT_KDUMP_ADOPT in probe()
  - iommu/arm-smmu-v3: Suppress EVTQ/PRIQ events in kdump kernel
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/43fd9986b085cf5bfba2c9bc06c0411693a361e5.1778416609.git.nicolinc@nvidia.com/

**iommu/arm-smmu-v3-sva: Enable Hardware Access and Hardware Dirty bits**

- 日期：2026-05-03
- 状态：社区讨论中
- 概括：在 ARM SMMUv3 SVA 上下文描述符中依据硬件特性启用硬件访问和脏位更新位。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260503135413.1108138-1-nicolinc@nvidia.com/

**▸ 组织：Huawei**（3 patches）

**[3/5] iommu/arm-smmu-v3: Add Stream Table Entry display to debugfs**

- 日期：2026-05-20
- 状态：社区讨论中
- 概括：在debugfs中添加stream_table目录，为每个Stream ID创建子目录和ste文件，用于显示STE的配置信息和原始数据。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260520063714.2440584-3-xiaqinxin@huawei.com/

**[1/5] iommu/arm-smmu-v3: Add basic debugfs framework**

- 日期：2026-05-20
- 状态：社区讨论中
- 概括：为ARM SMMUv3驱动添加基础的debugfs框架，支持在/sys/kernel/debug/iommu/arm_smmu_v3/下创建每个SMMU实例的目录及capabilities文件，用于展示SMMU功能特性与配置。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260520063714.2440584-1-xiaqinxin@huawei.com/

**[5/5] iommu/arm-smmu-v3: Add Context Descriptor display to debugfs**

- 日期：2026-05-20
- 状态：社区讨论中
- 概括：为每个设备的debugfs目录新增cd文件，遍历所有SSID并输出有效的Context Descriptor字段与原始数据。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260520063714.2440584-5-xiaqinxin@huawei.com/

**▸ 组织：Individual Contributor**（2 patches）

**[v2] iommu/arm-smmu-v3: Limit queue allocation retry boundary to PAGE_SIZE**

- 日期：2026-05-09
- 状态：社区讨论中
- 概括：将arm-smmu-v3队列分配重试的停止条件从队列大小严格小于PAGE_SIZE改为小于等于PAGE_SIZE，防止大小等于页时继续降级。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/tencent_F13723B53F68DC857410D3DBE4F6C895C106@qq.com/

**[SERIES] iommu: Add PCI vendor:device ID to IOMMU fault logs** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-05-06
- 状态：社区讨论中
- 概括：新增pci vendor:device id，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/arm-smmu-v3: Print PCI vendor:device ID in SMMU translation fault logs
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260506150541.60467-2-yigitogu@amazon.de/

**▸ 组织：Google**（2 patches）

**[SERIES] iommu/arm-smmu-v3: Implement Runtime/System Sleep ops** （cover letter，7/12 个 patch 达到代码量阈值）

- 日期：2026-06-01
- 状态：社区讨论中
- 概括：实现runtime/system sleep ops，完善缺失的功能接口，完善子系统的功能完备性，确保与硬件平台和上层框架的正确协同
- 达到阈值的 patches（7 个，显示前 5）：
  - iommu/arm-smmu-v3: Refactor arm_smmu_setup_irqs
  - iommu/arm-smmu-v3: Cache and restore MSI config
  - iommu/tegra241-cmdqv: Restore PROD and CONS after resume
  - iommu/arm-smmu-v3: Implement pm_runtime & system sleep ops
  - iommu/arm-smmu-v3: Invoke pm_runtime before hw access
  - ... 及其他 2 个 patch
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260601215909.3958732-2-praan@google.com/

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

**▸ 组织：Debian**（1 patches）

**iommu/arm-smmu-v3: Disable PRI when no priq IRQ is available**

- 日期：2026-06-22
- 状态：社区讨论中
- 概括：当缺少PRI队列中断时，增加清除ARM_SMMU_FEAT_PRI特性标志的操作以禁用PRI功能。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260622-smmu_pri-v1-1-14ad92b6043f@debian.org/

---

### ◆ 子系统：AMD IOMMU（8 patches）

**▸ 组织：Oracle**（3 patches）

**[SERIES] amd_iommu: Fix Coverity and endianness issues** （cover letter，3/4 个 patch 达到代码量阈值）

- 日期：2026-06-24
- 状态：社区讨论中
- 概括：修复coverity and endianness issues，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（3 个，显示前 5）：
  - amd_iommu: Return int from page walk status helpers
  - amd_iommu: Decode IRTEs without bitfields
  - amd_iommu: Decode XT interrupt control register without bitfields
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260624195925.1254462-2-alejandro.j.jimenez@oracle.com/

**[2/2] amd_iommu: Fully initialize XT interrupt message state**

- 日期：2026-06-23
- 状态：社区讨论中
- 概括：将 `X86IOMMUIrq irq` 变量改为 `X86IOMMUIrq irq = { 0 }`，确保该结构体完全零初始化，避免未初始化的字段被用于构建 XT 中断消息。
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260623005813.984238-3-alejandro.j.jimenez@oracle.com/

**[SERIES] amd_iommu: Do not create duplicate MSI capability** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-06-09
- 状态：社区讨论中
- 概括：限制create duplicate msi capability，增加条件判断和安全保护逻辑，持续改进代码质量和功能完备性
- 达到阈值的 patches（4 个，显示前 5）：
  - amd_iommu: Do not latch unsupported GA log status bits
  - amd_iommu: Use full BDF when reporting page faults
  - amd_iommu: Do not create duplicate MSI capability
  - amd_iommu: Use INTCAPXT for IOMMU event interrupts
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260609204403.323149-4-dongli.zhang@oracle.com/

**▸ 组织：Individual Contributor**（2 patches）

**[v2,1/2] iommu/amd-vi: allow disable_iommu() against non-initialized IOMMUs**

- 日期：2026-05-06
- 状态：社区讨论中
- 概括：`disable_iommu`增加`force`参数，允许在IOMMU未启用时强制执行部分关闭操作。
- 来源：https://patchwork.kernel.org/project/xen-devel/patch/20260506135514.47310-2-roger.pau@citrix.com/

**[v3] iommu/amd-vi: do not zero IOMMU MMIO region**

- 日期：2026-05-06
- 状态：社区讨论中
- 概括：移除对IOMMU MMIO区域的全零初始化，改为在驱动接管前检测并禁用固件已启用的IOMMU。
- 来源：https://patchwork.kernel.org/project/xen-devel/patch/20260506165157.68567-1-roger.pau@citrix.com/

**▸ 组织：AMD**（2 patches）

**[SERIES] Add support for AMD IOMMU GAPPI** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-06-26
- 状态：社区讨论中
- 概括：新增支持 amd iommu gappi，扩展框架的硬件兼容性和功能覆盖范围，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu/amd: kvm/svm: Improve API between SVM and AMD IOMMU
  - iommu/amd: Configure IRTE to use the GAPPI for posted interrupts
  - iommu/amd: Provide kernel command line option to enable GAPPI
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260626105906.14577-2-sarunkod@amd.com/

**[SERIES] acpi_build: Refactor and cleanup AMD IVRS build** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-05-11
- 状态：社区讨论中
- 概括：重构重新组织代码结构以提升可读性和可维护性，提升代码的可读性和可维护性，为后续功能迭代奠定更清晰的基础
- 达到阈值的 patches（1 个，显示前 5）：
  - amd_iommu: Return empty efr for stub call
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260511123937.32743-4-sarunkod@amd.com/

**▸ 组织：Google**（1 patches）

**[SERIES] iommu/amd: Refactors for ATS updates** （cover letter，1/4 个 patch 达到代码量阈值）

- 日期：2026-06-01
- 状态：社区讨论中
- 概括：重构重新组织代码结构以提升可读性和可维护性，提升代码的可读性和可维护性，为后续功能迭代奠定更清晰的基础
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/amd: Clear aliases before setting the rlookup_table to NULL
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/20260601134204.2150602-2-praan@google.com/

---

### ◆ 子系统：IOMMU Core（8 patches）

**▸ 组织：Individual Contributor**（5 patches）

**[v11,08/13] iommu/ipmmu-vmsa: Implement suspend/resume callbacks**

- 日期：2026-06-10
- 状态：社区讨论中
- 概括：为 IPMMU-VMSA IOMMU 驱动添加系统挂起/恢复回调，在挂起时保存根 IPMMU 的域上下文和缓存 IPMMU 的微 TLB，恢复时将其还原。
- 来源：https://patchwork.kernel.org/project/xen-devel/patch/a1c9e3defdd8fc772b78e93b7758294828246eea.1781084290.git.mykola_kvach@epam.com/

**[17/17] iommu/rockchip: disable fetch dte time limit**

- 日期：2026-06-05
- 状态：社区讨论中
- 概括：在Rockchip IOMMU启用时，通过设置AUTO_GATING寄存器的BIT(31)禁用DTE获取时间限制，以修复IOMMU阻塞问题。
- 来源：https://patchwork.kernel.org/project/linux-rockchip/patch/20260606-spu-rga3multicore-v1-17-3ec2b15675f7@pengutronix.de/

**[RFC,v3,6/9] iommu/rockchip: Clear AUTO_GATING bit 1 on the RK356x v1 IOMMU**

- 日期：2026-06-04
- 状态：社区讨论中
- 概括：在RK356x v1 IOMMU使能分页后，清除AUTO_GATING寄存器的位1以防止页表遍历因时钟门控而卡死。
- 来源：https://patchwork.kernel.org/project/linux-rockchip/patch/20260604135255.62682-7-midgy971@gmail.com/

**[SERIES] iommu: introduce iova_to_phys_length and remove iova_to_phys** （cover letter，3/29 个 patch 达到代码量阈值）

- 日期：2026-06-03
- 状态：社区讨论中
- 概括：引入iova_to_phys_length and remove iova_to_phys，扩展框架的功能范围
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu/io-pgtable: selftests switch to iova_to_phys_length
  - iommufd/selftest: switch to iommu_iova_to_phys_length
  - iommufd: use iova_to_phys_length for efficient unmap
- 来源：https://patchwork.kernel.org/project/dri-devel/patch/20260603151804.1963871-6-guanghuifeng@linux.alibaba.com/

**[SERIES] iommu: introduce iova_to_phys_length for efficient IOVA-to-physical translation** （cover letter，1/4 个 patch 达到代码量阈值）

- 日期：2026-05-31
- 状态：社区讨论中
- 概括：引入iova_to_phys_length for efficient iova-to-physical translation，扩展框架的功能范围
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu: direct page-table drivers implement iova_to_phys_length
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260531093637.3893199-7-guanghuifeng@linux.alibaba.com/

**▸ 组织：Microsoft**（1 patches）

**[V3,01/11] iommu/hyperv: Rename hyperv-iommu.c to hyperv-irq.c**

- 日期：2026-05-12
- 状态：社区讨论中
- 概括：我们需要分析这个patch的标题和diff内容，用一句话概括核心改动，不超过200字符。标题是：`[V3,01/11] iommu/hyperv: Rename hyperv-iommu.c to hyperv-irq.c`。diff显示：文件重命名了，编译选项从`CONFIG_HYPERV_IOMMU`改为`CONFIG_HYPERV`，同时也修改了Kconfig相关？但没有显示修改Kconfi
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/20260512020259.1678627-2-mrathor@linux.microsoft.com/

**▸ 组织：Qualcomm**（1 patches）

**[v2,08/19] iommu/fsl: use platform_device_set_of_node()**

- 日期：2026-06-29
- 状态：社区讨论中
- 概括：使用 platform_device_set_of_node() 替代直接赋值 of_node，并相应地调整了设备节点引用计数的释放逻辑。
- 来源：https://patchwork.kernel.org/project/alsa-devel/patch/20260629-pdev-fwnode-ref-v2-8-8abe2513f96e@oss.qualcomm.com/

**▸ 组织：Google**（1 patches）

**[SERIES] iommu: Add live update state preservation** （cover letter，16/16 个 patch 达到代码量阈值）

- 日期：2026-06-14
- 状态：社区讨论中
- 概括：新增live update state preservation，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（16 个，显示前 5）：
  - iommu: Implement IOMMU Live update FLB callbacks
  - iommu/pages: Add APIs to preserve/unpreserve/restore iommu pages
  - iommupt: Implement preserve/unpreserve/restore callbacks
  - iommu: Implement IOMMU domain preservation
  - iommu: Implement device and IOMMU HW preservation
  - ... 及其他 11 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260614233728.2212104-3-skhawaja@google.com/

---

### ◆ 子系统：RISC-V IOMMU（7 patches）

**▸ 组织：Individual Contributor**（5 patches）

**[1/1] iommu/riscv: RFC: mark endpoint ATS-broken on ATS invalidation timeout**

- 日期：2026-06-25
- 状态：社区讨论中
- 概括：我们需要分析这个 Linux 内核 patch 的标题和 diff 内容，用一句话（不超过200字符）概括核心改动。要求直接说明做了什么改动，保持技术准确性，不用修饰性词语。

标题是：“[1/1] iommu/riscv: RFC: mark endpoint ATS-broken on ATS invalidation timeout”

diff 内容显示对 drivers/iommu/ri
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20260625093416.4023451-2-shanbeeyoo@gmail.com/

**[v1] iommu/riscv: Support 32-bit register accesses**

- 日期：2026-06-15
- 状态：社区讨论中
- 概括：添加配置选项和对应实现，使 RISC-V IOMMU 在 64 位寄存器无法对齐访问时，可通过成对 32 位 MMIO 操作配合自旋锁进行模拟访问。
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20260615064855.90316-1-zhangzhanpeng.jasper@bytedance.com/

**iommu/riscv: prefer WSI on IGS=BOTH when wired IRQs are described**

- 日期：2026-05-19
- 状态：社区讨论中
- 概括：当 RISC-V IOMMU 的 IGS 字段为 BOTH 且固件描述有线中断资源时，优先选择 WSI 中断模式而非 MSI。
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20260519125716.81594-1-fangyu.yu@linux.alibaba.com/

**[SERIES] iommu/riscv: Support Svpbmt memory types in generic_pt** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-05-12
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（2 个，显示前 5）：
  - iommupt: Encode IOMMU_MMIO/IOMMU_CACHE via RISC-V Svpbmt bits
  - iommu/riscv: Advertise Svpbmt support to generic page table
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260512074142.16356-3-fangyu.yu@linux.alibaba.com/

**[SERIES] iommu/riscv: Add hardware dirty tracking for second-stage domains** （cover letter，3/7 个 patch 达到代码量阈值）

- 日期：2026-05-07
- 状态：社区讨论中
- 概括：新增hardware dirty tracking，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu/riscv: report iommu capabilities
  - iommu/riscv: support GSCID and GVMA invalidation command
  - iommu/riscv: Pre-enable GADE for second-stage domains
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260507113706.11400-3-fangyu.yu@linux.alibaba.com/

**▸ 组织：SiFive**（1 patches）

**[v3,2/2] iommu/riscv: create a auxiliary device for HPM**

- 日期：2026-06-30
- 状态：社区讨论中
- 概括：为支持硬件性能监控(HPM)能力的RISC-V IOMMU设备创建辅助PMU设备。
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20260630083833.1275837-3-zong.li@sifive.com/

**▸ 组织：Qualcomm**（1 patches）

**[SERIES] iommu/riscv: Enable IOMMU_DMA** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-05-08
- 状态：社区讨论中
- 概括：启用之前被禁用或条件编译的功能特性，持续改进代码质量和功能完备性
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/riscv: Map IMSIC addresses for paging domains
  - iommu/dma: enable IOMMU_DMA for RISC-V
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20260508212339.381933-2-andrew.jones@oss.qualcomm.com/

---

### ◆ 子系统：ARM SMMU (v1/v2)（4 patches）

**▸ 组织：Qualcomm**（2 patches）

**[v3] iommu/arm-smmu: Use pm_runtime in fault handlers**

- 日期：2026-06-30
- 状态：社区讨论中
- 概括：在arm-smmu的上下文和全局故障处理中增加pm_runtime_get_if_active引用检查与释放，同时在挂起回调中禁用故障报告，以防止未上电的寄存器访问。
- 来源：https://patchwork.kernel.org/project/linux-arm-msm/patch/20260630-smmu-rpm-v3-1-f69874a580fa@oss.qualcomm.com/

**[SERIES] iommu/qcom: Misc Fixes** （cover letter，3/6 个 patch 达到代码量阈值）

- 日期：2026-06-23
- 状态：社区讨论中
- 概括：修复相关功能缺陷或逻辑错误，确保操作行为符合预期规范，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu/qcom: Check pm_runtime_resume_and_get() return in probe
  - iommu/qcom: Publish pgtbl_ops before releasing init_mutex
  - iommu/qcom: Document why sec_ptbl allocated flag needs no locking
- 来源：https://patchwork.kernel.org/project/linux-arm-msm/patch/20260623122034.1166295-2-mukesh.ojha@oss.qualcomm.com/

**▸ 组织：Individual Contributor**（1 patches）

**[v3] iommu: arm-smmu-qcom: Ensure smmu is powered up in set_ttbr0_cfg**

- 日期：2026-05-07
- 状态：社区讨论中
- 概括：在写入SMMU上下文银行前后增加运行时PM resume/autosuspend调用，以确保操作期间SMMU处于上电状态。
- 来源：https://patchwork.kernel.org/project/linux-arm-msm/patch/20260507-qcom_smmu_pmfix-v3-1-af8cd05831a2@gmail.com/

**▸ 组织：Microsoft**（1 patches）

**iommu/arm-smmu: pass smmu->dev to report_iommu_fault**

- 日期：2026-05-17
- 状态：社区讨论中
- 概括：将 report_iommu_fault 的第二个参数从 NULL 改为 smmu->dev，以便在报告 IOMMU 故障时传递设备指针。
- 来源：https://patchwork.kernel.org/project/linux-arm-msm/patch/20260517005052.3783378-1-shyamsaini@linux.microsoft.com/

---

### ◆ 子系统：IOMMUFD（4 patches）

**▸ 组织：NVIDIA**（2 patches）

**[SERIES] iommufd: Iterate the cache invalidation array in the core** （cover letter，5/5 个 patch 达到代码量阈值）

- 日期：2026-06-29
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（5 个，显示前 5）：
  - iommufd: Iterate the cache invalidation array in the core
  - iommufd/selftest: Convert cache invalidation mocks to the core array loop
  - iommu/arm-smmu-v3-iommufd: Convert cache invalidation to the core array loop
  - iommu/arm-smmu-v3-iommufd: Reject unsupported bits in invalidation commands
  - iommu/vt-d: Convert nested cache invalidation to the core array loop
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/dc0c92e0688db085e12e0b6931c49384489da887.1782767398.git.nicolinc@nvidia.com/

**[SERIES] iommufd: Fix vDEVICE allocation lifecycle bugs** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-06-29
- 状态：社区讨论中
- 概括：修复vdevice allocati，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（2 个，显示前 5）：
  - iommufd/viommu: Publish a vDEVICE only after vdevice_init() succeeds
  - iommu/arm-smmu-v3-iommufd: Require exactly one Stream ID for a vDEVICE
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/8f29de140d86bf507f71c6c27aee8e23e1c3940d.1782767110.git.nicolinc@nvidia.com/

**▸ 组织：AMD**（1 patches）

**iommufd: take dma_resv lock before dma_buf_unpin() in release path**

- 日期：2026-05-26
- 状态：社区讨论中
- 概括：在 iommufd 释放路径中为 dma_buf_unpin 调用添加 dma_resv 锁，以避免并发访问问题。
- 来源：https://patchwork.kernel.org/project/dri-devel/patch/20260526111034.4079-1-Ankit.Soni@amd.com/

**▸ 组织：Kernel.org**（1 patches）

**[SERIES] Add iommufd ioctls to support TSM operations** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-05-25
- 状态：社区讨论中
- 概括：新增iommufd ioctls，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（4 个，显示前 5）：
  - iommufd/device: Associate KVM file pointer with iommufd_device
  - iommufd/viommu: Keep a reference to the KVM file
  - iommufd/tsm: add vdevice TSM bind/unbind ioctl
  - iommufd/vdevice: add TSM request ioctl
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260525154816.1029642-3-aneesh.kumar@kernel.org/

---

### ◆ 子系统：Intel VT-d（4 patches）

**▸ 组织：Intel**（3 patches）

**[SERIES] intel_iommu: Enable PRQ support for passthrough device** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-06-18
- 状态：社区讨论中
- 概括：启用之前被禁用或条件编译的功能特性，持续改进代码质量和功能完备性
- 达到阈值的 patches（3 个，显示前 5）：
  - intel_iommu_accel: teardown FAULTQ resources in bottom half
  - intel_iommu_accel: Accept PRQ response for passthrough device
  - intel_iommu_accel: Add PRQ injection for passthrough device
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260618034844.618011-6-zhenzhong.duan@intel.com/

**[SERIES] intel_iommu: Enable PASID support for passthrough device** （cover letter，11/15 个 patch 达到代码量阈值）

- 日期：2026-05-27
- 状态：社区讨论中
- 概括：启用之前被禁用或条件编译的功能特性，持续改进代码质量和功能完备性
- 达到阈值的 patches（11 个，显示前 5）：
  - intel_iommu: Rename pasid property to "pasid-bits" and define it as type uint8
  - intel_iommu: Expose flag VIOMMU_FLAG_PASID_SUPPORTED and VIOMMU_FLAG_WANT_PASID_ATTACH
  - intel_iommu_accel: Switch to VTDAccelPASIDCacheEntry for PASID bind/unbind and PIOTLB invalidation
  - intel_iommu: Create the nested hwpt with IOMMU_HWPT_ALLOC_PASID flag
  - intel_iommu: Export some functions
  - ... 及其他 6 个 patch
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260527054658.1021096-6-zhenzhong.duan@intel.com/

**[SERIES] Update properties naming for 'x-scalable-mode' and 'x-flts'** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-05-13
- 状态：社区讨论中
- 概括：更新相关的配置或实现以反映最新的内核标准，保持子系统与内核主线的兼容性，适应 API 和框架的演进方向
- 达到阈值的 patches（1 个，显示前 5）：
  - intel_iommu: Change 'flts' property naming to 'fsts'
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260513064227.2304854-3-zhenzhong.duan@intel.com/

**▸ 组织：Individual Contributor**（1 patches）

**[v3] intel_iommu: Correctly set pt bit in extended capability register**

- 日期：2026-06-24
- 状态：社区讨论中
- 概括：将 VT-d Pass Through 能力位从常规能力寄存器 (CAP) 移到扩展能力寄存器 (ECAP) 中设置，修复原有错误。
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260624103933.1793586-3-leo@managarm.org/

---

### ◆ 子系统：IOMMU Page Table（2 patches）

**▸ 组织：Qualcomm**（1 patches）

**iommu/io-pgtable-arm: Add support for contiguous hint bit**

- 日期：2026-06-18
- 状态：社区讨论中
- 概括：为ARM LPAE页表分配器添加连续提示位（CONT bit）支持，通过Kconfig控制，按块大小合并映射并设置CONT位以提升TLB利用率。
- 来源：https://patchwork.kernel.org/project/linux-arm-msm/patch/20260618-iommu_contig_hint-v1-1-4502a59e6388@oss.qualcomm.com/

**▸ 组织：Google**（1 patches）

**[SERIES] iommu/io-pgtable-arm: iommu-pages and cleanup** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-05-13
- 状态：社区讨论中
- 概括：清理代码中的风格问题和废弃的命名方式，精简代码库规模，降低后续维护的复杂度和引入回归问题的风险
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/io-pgtable-arm: Use consistent sizes for page allocation and freeing
  - iommu/io-pgtable-arm: Use address conversion consistently
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260513215203.3852661-2-smostafa@google.com/

---

### ◆ 子系统：IOMMU SVA/SVM（1 patches）

**▸ 组织：Google**（1 patches）

**[v2] iommu: Allow device driver to use its own PASID space for SVA**

- 日期：2026-05-20
- 状态：社区讨论中
- 概括：允许设备驱动在SVA绑定时传入私有PASID，支持使用设备自身的PASID空间而非全局分配。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260520150743.727106-1-joonwonkang@google.com/

---

### ◆ 子系统：ARM SMMU Acceleration（1 patches）

**▸ 组织：NVIDIA**（1 patches）

**[SERIES] iommu/arm-smmu-v3: Fix Tegra241 CMDQV CMD_SYNC use-after-free** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-06-29
- 状态：社区讨论中
- 概括：修复use-after-free 漏洞，防止在错误恢复路径中访问已释放的内存对象，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/arm-smmu-v3: Manage teardown with devm
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260629094106.251694-2-skolothumtho@nvidia.com/

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

*报告由 Linux Patches Tracker 自动生成 | 2026-07-11 11:41:16*
