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
| 社区讨论中 | 52 | 98.1% |
| 已合入 | 0 | 0.0% |
| **总计** | **53** | **100%** |

### 按组织分类（TOP 15）

| 组织 | 数量 | 占比 |
|------|------|------|
| Individual Contributor | 18 | 34.0% |
| NVIDIA | 10 | 18.9% |
| Qualcomm | 8 | 15.1% |
| Google | 7 | 13.2% |
| AMD | 3 | 5.7% |
| Kernel.org | 2 | 3.8% |
| Linaro | 1 | 1.9% |
| Microsoft | 1 | 1.9% |
| Red Hat | 1 | 1.9% |
| Oracle | 1 | 1.9% |
| Intel | 1 | 1.9% |

### 按子系统分类

| 子系统 | 数量 | 占比 |
|--------|------|------|
| ARM SMMUv3 | 13 | 24.5% |
| IOMMU Core | 13 | 24.5% |
| AMD IOMMU | 7 | 13.2% |
| RISC-V IOMMU | 5 | 9.4% |
| IOMMUFD | 4 | 7.5% |
| ARM SMMU (v1/v2) | 4 | 7.5% |
| Intel VT-d | 3 | 5.7% |
| ARM SMMU Acceleration | 2 | 3.8% |
| IOMMU DMA-API | 1 | 1.9% |
| IOMMU Page Table | 1 | 1.9% |

## 重点 Patch Top20 清单

### 已合入

暂无。

### 社区讨论

| 厂商 | 简介 |
|------|------|
| Google | [PATCH v4 00/18] iommu: Add live update state preservation ------此补丁集为IOMMU子系统引入设备热更新状态保存机制，通过新增页表保留与恢复回调及域重连操作，使设备在固件热更新期间不中断地保留地址映射并恢复硬件状态。 |
| Google | [PATCH v7 00/24] KVM: arm64: SMMUv3 driver for pKVM (trap and emulate) ------该补丁集为pKVM在EL2异常级别新增SMMUv3驱动，采用trap-and-emulate方式截获并模拟设备MMIO访问，影子化流表与命令队列，实现直通设备DMA隔离和嵌套地址翻译。 |
| NVIDIA | [PATCH v10 00/13] iommu/arm-smmu-v3: Adopt the crashed kernel's stream table for kdump ------该补丁集使kdump内核直接接管崩溃内核保留的SMMU流表，避免设备重置导致IOMMU状态丢失，通过解析并复用原有CD表、流表及预留ASID/VMID，同时关闭事件队列，实现崩溃后IOMMU上下文无缝继承。 |
| Qualcomm | [PATCH v5 00/17] iommu/riscv: Enable MSI remapping, IOMMU_DMA and VFIO ------该补丁系列使RISC-V IOMMU支持MSI重映射、IOMMU_DMA及VFIO，通过将iommufd软件MSI映射改为可增长位图并预留IOVA窗口，同时准备MSI地址列表以管理中断映射。 |
| NVIDIA | [PATCH v2 00/11] iommu/tegra241-cmdqv: Fix error-interrupt races and VINTF lifecycle bugs ------该补丁系列修复 Tegra241 命令队列虚拟化驱动中错误中断与 VINTF 生命周期的竞态及泄漏，通过完善初始化顺序、同步中断处理、收紧 vSID 校验和错误映射边界，并修正资源释放与回退逻辑来增强稳定性。 |
| Oracle | [PATCH v2 00/5] amd_iommu: Do not create duplicate MSI capability ------该系列围绕 amd_iommu: Do not create duplicate MSI capability，具体包括Define MMIO register masks、避免 latch unsupported GA log status bits、避免 create duplicate MSI capability、调整 extended feature register read-only、改用 full BDF（当 reporting page faults 时）。 |
| Google | [PATCH v9 00/12] iommu/arm-smmu-v3: Implement Runtime/System Sleep ops ------本补丁集为arm-smmu-v3驱动引入运行时与系统睡眠电源管理能力，涉及中断配置重构、命令队列终止与恢复、MSI状态缓存及gerror处理等改动，最终通过pm_runtime及睡眠操作确保硬件访问前正确管理电源状态。 |
| Qualcomm | [PATCH v1 00/12] iommu: qcom_iommu: implement support for instances on MSM8974 ------此补丁系列为MSM8974平台的QCOM IOMMU驱动补齐实例支持，新增SMMU全局寄存器与短描述符页表格式处理，并实现对非TZ管理实例的编程、上下文保存恢复及故障终止等能力。 |
| Google | [PATCH v1 00/7] iommu/arm-smmu-v3: Fixes reported by Sashiko ------该补丁集修复arm-smmu-v3及iommufd路径中的多处缺陷：纠正缓存失效错误处理、确保L2页表先于L1指针可见、防止重复流损坏红黑树，并修正测试代码中的越界与UBSAN等问题。 |
| NVIDIA | [PATCH v6 00/5] iommufd: Iterate the cache invalidation array in the core ------该补丁集将缓存失效数组的遍历逻辑从各驱动和自测代码上移到 iommufd 核心统一执行，驱动仅处理单条失效命令，并新增对不支持位的拒绝检查，从而消除重复实现并增强命令校验一致性。 |
| NVIDIA | [PATCH v2 00/3] iommufd: Fix vDEVICE allocation lifecycle bugs ------此补丁集修复iommufd中vDEVICE分配生命周期缺陷，确保错误路径释放igroup锁、初始化成功后才发布设备，并要求ARM SMMUv3场景下vDEVICE严格对应单一Stream ID。 |
| Individual Contributor | [PATCH v3 00/10] iommu/riscv: Add hardware dirty tracking for second-stage domains ------该补丁集为RISC-V IOMMU二级阶段域引入硬件脏页跟踪功能，新增GSCID/GVMA命令、脏页PTE操作及GADE预启用支持，提升DMA设备内存回收效率。 |
| Intel | [PATCH v5 00/6] intel_iommu: Enable PRQ support for passthrough device ------本补丁系列为透传设备启用Intel IOMMU的PRQ支持，通过修改intel_iommu_accel模块，在底半部释放故障队列资源，并添加PRQ响应接收与注入机制，使直通设备能够利用页请求队列服务。 |
| AMD | [PATCH v4 00/7] Add support for AMD IOMMU GAPPI ------该补丁集为AMD IOMMU新增GAPPI支持，通过引入命令行开关、重命名IOMMU接口以明确APICID与唤醒中断语义、传递vCPU运行状态，并在IRTE未运行时编程guest模式表项，实现基于GAPPI的虚拟机中断唤醒。 |
| Qualcomm | [PATCH v2 00/6] iommu/qcom: Misc Fixes ------该补丁集修复高通IOMMU驱动的多个缺陷：反转故障检测、运行时电源管理错误处理、页表操作泄漏及时钟顺序，并优化pgtbl_ops发布时机，提升驱动稳定性。 |
| Red Hat | [PATCH v1 00/44] amd_iommu: Fix opcode reported in invalid command handling ------该补丁集修复AMD IOMMU在无效命令处理时错误上报操作码的问题，并修正中断寄存器解码、命令缓冲字节序、页遍历状态辅助函数返回值及中断重映射表解析中的位域和字节序错误。 |
| Individual Contributor | [PATCH v1 00/7] riscv: iommu: Add QoS ID support for resctrl device assignment ------该补丁系列为RISC-V IOMMU增加QoS ID支持，通过按ID查找和校验更新IOMMU组，为设备分配组并编程QoS ID，同时经sysfs暴露全局ID，服务于resctrl设备分配场景。 |
| NVIDIA | [PATCH v5 00/18] iommu/arm-smmu-v3: Quarantine device upon ATC invalidation timeout ------该补丁集在ATC无效化超时后对相关设备实施隔离，通过将blocked状态扩展为枚举、修正流节点管理及引入锁与批量命令机制，增强SMMU对超时错误的处理能力和设备故障隔离的可靠性。 |
| NVIDIA | [PATCH v2 00/9] Use the generic iommu page table for SMMUv3 ------本补丁系列旨在使SMMUv3采用通用iommu页表框架，移除对io-pgtable-arm的依赖，并新增ARMv8页表格式及DBM支持。 |
| Individual Contributor | [PATCH v2 00/11] KVM: selftests: sev_smoke_test: Only run VM types the host offers ------该系列围绕 KVM: selftests: sev_smoke_test: Only run VM types the host offers，具体包括iommufd 中Plumb dma-buf memory-type (RAM vs MMIO) through the phys map、iommufd 中Look up private-interconnect phys via exporter symbols。 |

---

## 已合入 Patches

暂无。

## 社区讨论中 Patches

### ◆ 子系统：ARM SMMUv3（13 patches）

**▸ 组织：NVIDIA**（6 patches）

**[SERIES] iommu/arm-smmu-v3: Adopt the crashed kernel's stream table for kdump** （cover letter，10/13 个 patch 达到代码量阈值）

- 日期：2026-08-30
- 状态：社区讨论中
- 概括：该补丁集使kdump内核直接接管崩溃内核保留的SMMU流表，避免设备重置导致IOMMU状态丢失，通过解析并复用原有CD表、流表及预留ASID/VMID，同时关闭事件队列，实现崩溃后IOMMU上下文无缝继承。
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
- 概括：本补丁系列旨在使SMMUv3采用通用iommu页表框架，移除对io-pgtable-arm的依赖，并新增ARMv8页表格式及DBM支持。
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
- 概括：该补丁为Arm SMMUv3驱动新增IDR5.DS特性支持，并将TLBI命令的SCALE字段从5位扩展到6位，使范围无效化能覆盖更大地址空间，同时保持旧硬件兼容性。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/1b35fa8c417a21ac80a4a3f19db34d81ef6ca490.1785258826.git.nicolinc@nvidia.com/

**[SERIES] iommu/arm-smmu-v3: Tegra264 invalidation workaround** （cover letter，2/4 个 patch 达到代码量阈值）

- 日期：2026-07-26
- 状态：社区讨论中
- 概括：该补丁系列针对 Tegra264 上 SMMU 的 CFGI/TLBI 失效操作需重复执行才能生效的硬件勘误，通过重构命令队列强制同步逻辑并新增重复失效机制，在保留现有流程的同时确保缓存一致性。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/arm-smmu-v3: Enable CFGI/TLBI-repeat workaround on Tegra264
  - iommu/arm-smmu-v3-iommufd: Report CFGI/TLBI-repeat erratum
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260726081904.1408859-2-amhetre@nvidia.com/

**[3/7] iommupt: Add the 64 bit ARMv8 page table format**

- 日期：2026-07-06
- 状态：社区讨论中
- 概括：该补丁为通用 IOMMU 页表框架新增 64 位 ARMv8 VMSAv8-64 及长描述符格式的支持模块，涵盖多级页表、LPA/LPA2 扩展与不同粒度，并扩展对应的 Kconfig 与构建配置，方便后续驱动自动选用。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/3-v1-807e2d1a5efb+e1-iommupt_armv8_jgg@nvidia.com/

**[SERIES] iommu/arm-smmu-v3: Quarantine device upon ATC invalidation timeout** （cover letter，4/12 个 patch 达到代码量阈值）

- 日期：2026-07-03
- 状态：社区讨论中
- 概括：该补丁集在ATC无效化超时后对相关设备实施隔离，通过将blocked状态扩展为枚举、修正流节点管理及引入锁与批量命令机制，增强SMMU对超时错误的处理能力和设备故障隔离的可靠性。
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
- 概括：该补丁集修复arm-smmu-v3及iommufd路径中的多处缺陷：纠正缓存失效错误处理、确保L2页表先于L1指针可见、防止重复流损坏红黑树，并修正测试代码中的越界与UBSAN等问题。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/arm-smmu-v3: Ensure L2 tables are visible before L1 ptrs
  - iommu/arm-smmu-v3: Prevent rbtree corruption from duplicate streams
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260828125409.1921538-4-smostafa@google.com/

**iommu/arm-smmu-v3: Convert to use atomic poll timeout**

- 日期：2026-07-28
- 状态：社区讨论中
- 概括：此补丁将ARM SMMU v3寄存器同步等待从普通轮询超时改为原子轮询超时，避免调用中可能出现的睡眠，适用于原子上下文，确保轮询期间不阻塞调度。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260728211123.1059708-1-praan@google.com/

**[SERIES] iommu/arm-smmu-v3: Implement Runtime/System Sleep ops** （cover letter，7/12 个 patch 达到代码量阈值）

- 日期：2026-07-28
- 状态：社区讨论中
- 概括：本补丁集为arm-smmu-v3驱动引入运行时与系统睡眠电源管理能力，涉及中断配置重构、命令队列终止与恢复、MSI状态缓存及gerror处理等改动，最终通过pm_runtime及睡眠操作确保硬件访问前正确管理电源状态。
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
- 概括：该补丁集为pKVM在EL2异常级别新增SMMUv3驱动，采用trap-and-emulate方式截获并模拟设备MMIO访问，影子化流表与命令队列，实现直通设备DMA隔离和嵌套地址翻译。
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
- 概括：该补丁在kdump内核中将ARM SMMUv3的命令、事件和PRI队列大小限制为单页，以避免为硬件宣称的大队列分配过多内存，适用于仅需少量设备保存转储文件的场景。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260706084708.8072-1-kas@kernel.org/

**▸ 组织：Linaro**（1 patches）

**[2/2] iommu/arm-smmu-v3: Override for Inst/Data attribute**

- 日期：2026-07-24
- 状态：社区讨论中
- 概括：本补丁为Arm SMMUv3驱动新增Inst/Data属性覆盖配置，通过设备树选项和硬件IDR1能力检测，在STE中设置INSTCFG字段以强制指令属性为数据模式，并完善STE占用位掩码及不支持时的报错处理。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260724-arm-smmu-v3-instcfg-override-v1-2-e7acf4a8a525@linaro.org/

**▸ 组织：Individual Contributor**（1 patches）

**[RFC] iommu/arm-smmu-v3: Allow nested attach for PCI bridges without vDEVICE**

- 日期：2026-08-14
- 状态：社区讨论中
- 概括：该补丁针对arm-smmu-v3与iommufd的嵌套地址域附着流程，
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/PA1P190MB25578C482C8A3B06A4DCC6FDDBDA2@PA1P190MB2557.EURP190.PROD.OUTLOOK.COM/

---

### ◆ 子系统：IOMMU Core（12 patches）

**▸ 组织：Individual Contributor**（8 patches）

**[SERIES] iommu/rockchip: turn rk_iommu_ops into data** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-25
- 状态：社区讨论中
- 概括：该补丁集将rk_iommu_ops从含函数指针的结构精简为纯数据，并拒绝不支持的物理地址，以提升Rockchip IOMMU驱动的可维护性与安全性。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/rockchip: Reject unsupported physical addresses
  - iommu/rockchip: Reduce rk_iommu_ops to pure data
- 来源：https://patchwork.kernel.org/project/linux-rockchip/patch/20260825092132.154150-3-xxm@rock-chips.com/

**[SERIES] IOMMU driver improvements for modern Exynos SysMMUs** （cover letter，2/4 个 patch 达到代码量阈值）

- 日期：2026-08-20
- 状态：社区讨论中
- 概括：该补丁集改进了现代Exynos SysMMU的IOMMU驱动，针对无BLOCK模式的设备修正使能顺序与TLB失效逻辑，并新增v7故障事务信息解码能力。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/exynos: detect SysMMUs without BLOCK mode
  - iommu/exynos: decode the v7 fault transaction info
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260820-exynos-iommu-fixes-v1-1-6bbcd673bb15@gmail.com/

**[SERIES] iommu/iova: convert from rbtree to maple tree** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-08-18
- 状态：社区讨论中
- 概括：此补丁集将 IOMMU IOVA 管理从红黑树改为 maple tree，并处理 GFP_ATOMIC 分配失败时延迟擦除，同时新增 KUnit 测试来验证新实现。
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu/iova: defer maple tree erase on GFP_ATOMIC failure
  - iommu/iova: convert from rbtree to maple tree
  - iommu/iova: add KUnit test suite
- 来源：https://patchwork.kernel.org/project/linux-mm/patch/20260818152505.1057922-3-riel@surriel.com/

**iommu/msm: limit the per-master Machine ID list**

- 日期：2026-07-22
- 状态：社区讨论中
- 概括：该补丁在MSM IOMMU驱动中为每个主设备添加MID数量上限检查，超出MAX_NUM_MIDS即返回错误，防止越界并限制机器ID列表长度。
- 来源：https://patchwork.kernel.org/project/linux-arm-msm/patch/20260722041619.17735-1-pengpeng@iscas.ac.cn/

**[SERIES] accel/rocket: RK3576 NPU (RKNN) enablement** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-07-18
- 状态：社区讨论中
- 概括：为支持 RK3576 NPU 的 RKNN 功能，此补丁集修复了 Rockchip IOMMU 驱动：确保获取设备树中全部时钟，并在启用停顿时清除陈旧页错误，从而保障 NPU 正常稳定运行。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/rockchip: take all DT clocks
  - iommu/rockchip: clear stale page faults before enabling stall
- 来源：https://patchwork.kernel.org/project/linux-rockchip/patch/20260718031146.3368811-5-gahing@gahingwoo.com/

**[RFC,4/9] iommu/rockchip: skip orphaned-fault banks in rk_iommu_is_stall_active**

- 日期：2026-07-17
- 状态：社区讨论中
- 概括：该补丁在Rockchip IOMMU驱动的停滞状态检测中，忽略固件遗留的孤儿页错误银行，仅当页错误激活且无停滞但空闲时跳过，避免将其误判为未停滞，确保多银行协同判断更准确。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260717085220.3212274-5-gahing@gahingwoo.com/

**[RFC,5/9] iommu/rockchip: skip orphaned-fault banks in CMD_ENABLE_STALL dispatch**

- 日期：2026-07-17
- 状态：社区讨论中
- 概括：在 iommu/rockchip 中skip orphaned-fault banks in CMD_ENABLE_STALL dispatch。
- 来源：https://patchwork.kernel.org/project/linux-rockchip/patch/20260717085220.3212274-6-gahing@gahingwoo.com/

**[RFC,09/14] iommu: lazy-populate iommu_group reserved_regions/type attrs**

- 日期：2026-07-02
- 状态：社区讨论中
- 概括：本补丁为每个 iommu_group 内嵌 sysfs_lazy_state，使 reserved_regions 与 type 属性不再在组创建时立即生成，而是通过新增的 lazy populate 回调在访问时按需创建，并辅以 kernfs_set_lazy 与锁保护，从而减少首屏组初始化开销并降低 sysfs 暴露时的无关副作用。
- 来源：https://patchwork.kernel.org/project/kexec/patch/20260702175114.24659-5-sakacpav@amazon.de/

**▸ 组织：Qualcomm**（3 patches）

**[SERIES] Fix GPU and display on ARM32 platforms using the MSM IOMMU** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-07-30
- 状态：社区讨论中
- 概括：该补丁集修复ARM32平台使用MSM IOMMU时GPU与显示异常，通过为每个设备和IOMMU跟踪上下文主控，并改用IOMMU设备分配页表，以正确管理地址空间。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/msm: track a context master per device and IOMMU
  - iommu/msm: use the IOMMU device for page table allocation
- 来源：https://patchwork.kernel.org/project/linux-rockchip/patch/20260730-fix-qcom-smmu-v2-1-18e0daf2d836@oss.qualcomm.com/

**[3/8] iommu/fsl: use platform_device_set_fwnode()**

- 日期：2026-07-20
- 状态：社区讨论中
- 概括：该改动将飞思卡尔PAMU驱动初始化中的platform_device_set_of_node替换为platform_device_set_fwnode，并调用of_fwnode_handle将设备节点转为通用fwnode，使平台设备固件节点设置统一走fwnode接口。
- 来源：https://patchwork.kernel.org/project/alsa-devel/patch/20260720-pdev-set-fwnode-instead-of-of-node-v1-3-2dee93f42c54@oss.qualcomm.com/

**[v3,09/20] iommu/fsl: use platform_device_set_of_node()**

- 日期：2026-07-06
- 状态：社区讨论中
- 概括：该补丁使Freescale PAMU IOMMU驱动在初始化时改用platform_device_set_of_node()设置设备树节点，并借助基于__free(device_node)的自动清理机制管理引用计数，从而简化了错误处理路径并减少手动释放带来的缺陷风险。
- 来源：https://patchwork.kernel.org/project/dri-devel/patch/20260706-pdev-fwnode-ref-v3-9-1ff028e33779@oss.qualcomm.com/

**▸ 组织：Google**（1 patches）

**[SERIES] iommu: Add live update state preservation** （cover letter，16/16 个 patch 达到代码量阈值）

- 日期：2026-08-08
- 状态：社区讨论中
- 概括：此补丁集为IOMMU子系统引入设备热更新状态保存机制，通过新增页表保留与恢复回调及域重连操作，使设备在固件热更新期间不中断地保留地址映射并恢复硬件状态。
- 达到阈值的 patches（16 个，显示前 5）：
  - iommu: Implement IOMMU Live update FLB callbacks
  - iommu/pages: Add APIs to preserve/unpreserve/restore iommu pages
  - iommupt: Implement preserve/unpreserve/restore callbacks
  - iommu: Implement IOMMU domain preservation
  - iommu: Implement device and IOMMU HW preservation
  - ... 及其他 11 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260808022723.3893618-3-skhawaja@google.com/

---

### ◆ 子系统：AMD IOMMU（7 patches）

**▸ 组织：AMD**（3 patches）

**[v2] iommu/amd: Force identity mode for selected GPUs only**

- 日期：2026-08-24
- 状态：社区讨论中
- 概括：此补丁将AMD IOMMU的identity映射强制应用条件从所有支持IOMMUv2的设备，收窄为仅针对未连接至AMD上游桥的独立ATI显卡，并新增APU内置GPU的quirk识别逻辑，同时保持加密与SNP场景下的安全防护。
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/20260824085821.5422-1-vasant.hegde@amd.com/

**[SERIES] Add support for AMD IOMMU GAPPI** （cover letter，4/5 个 patch 达到代码量阈值）

- 日期：2026-08-21
- 状态：社区讨论中
- 概括：该补丁集为AMD IOMMU新增GAPPI支持，通过引入命令行开关、重命名IOMMU接口以明确APICID与唤醒中断语义、传递vCPU运行状态，并在IRTE未运行时编程guest模式表项，实现基于GAPPI的虚拟机中断唤醒。
- 达到阈值的 patches（4 个，显示前 5）：
  - iommu/amd: Provide kernel command line option to enable GAPPI
  - iommu/amd: KVM: SVM: Rename cpu to apicid in IOMMU interface
  - iommu/amd: KVM: SVM: Rename ga_log_intr to wakeup_intr in IOMMU interface
  - iommu/amd: Program guest-mode IRTEs for GAPPI wakeup when IRTE[IsRun] = 0
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260821055611.27138-8-sarunkod@amd.com/

**[SERIES] acpi_build: Refactor and cleanup AMD IVRS build** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-08-07
- 状态：社区讨论中
- 概括：该补丁系列重构并清理QEMU中AMD IOMMU的IVRS ACPI表构建逻辑，通过让存根调用返回空EFR、更新地址与VA大小宏，并移除不支持的PPR和HE特性标记来简化代码。
- 达到阈值的 patches（1 个，显示前 5）：
  - amd_iommu: Return empty efr for stub call
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260807061250.27739-2-sarunkod@amd.com/

**▸ 组织：Individual Contributor**（1 patches）

**[1/2] amd_iommu: Honor DTE[IR] and DTE[IW] when DTE[Mode] is 0**

- 日期：2026-07-18
- 状态：社区讨论中
- 概括：在 amd_iommu 中Honor DTE[IR] and DTE[IW]（当 DTE[Mode] is 0 时）。
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260718175208.118721-2-danielpaziyski@gmail.com/

**▸ 组织：Red Hat**（1 patches）

**[SERIES] amd_iommu: Fix opcode reported in invalid command handling** （cover letter，4/6 个 patch 达到代码量阈值）

- 日期：2026-07-05
- 状态：社区讨论中
- 概括：该补丁集修复AMD IOMMU在无效命令处理时错误上报操作码的问题，并修正中断寄存器解码、命令缓冲字节序、页遍历状态辅助函数返回值及中断重映射表解析中的位域和字节序错误。
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
- 概括：该系列围绕 amd_iommu: Do not create duplicate MSI capability，具体包括Define MMIO register masks、避免 latch unsupported GA log status bits、避免 create duplicate MSI capability、调整 extended feature register read-only、改用 full BDF（当 reporting page faults 时）。
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
- 概括：该补丁集重构AMD IOMMU设备探测与能力初始化流程，修复DTE清除逻辑，并在ATS配置失败时终止探测，同时拆分错误路径以保留中断重映射功能，从而提升ATS机制的稳健性。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/amd: Refactor device probe and capability initialization
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/20260824122347.1588592-2-praan@google.com/

---

### ◆ 子系统：RISC-V IOMMU（5 patches）

**▸ 组织：Individual Contributor**（4 patches）

**[SERIES] iommu/riscv: Add hardware dirty tracking for second-stage domains** （cover letter，4/7 个 patch 达到代码量阈值）

- 日期：2026-08-21
- 状态：社区讨论中
- 概括：该补丁集为RISC-V IOMMU二级阶段域引入硬件脏页跟踪功能，新增GSCID/GVMA命令、脏页PTE操作及GADE预启用支持，提升DMA设备内存回收效率。
- 达到阈值的 patches（4 个，显示前 5）：
  - iommu/riscv: use data structure instead of individual values
  - iommupt: Add RISC-V Second-stage (iohgatp) page table support
  - iommu/riscv: support GSCID and GVMA invalidation command
  - iommu/riscv: Pre-enable GADE for second-stage domains
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20260821132749.82070-5-fangyu.yu@linux.alibaba.com/

**[SERIES] riscv: iommu: Add QoS ID support for resctrl device assignment** （cover letter，3/4 个 patch 达到代码量阈值）

- 日期：2026-07-14
- 状态：社区讨论中
- 概括：该补丁系列为RISC-V IOMMU增加QoS ID支持，通过按ID查找和校验更新IOMMU组，为设备分配组并编程QoS ID，同时经sysfs暴露全局ID，服务于resctrl设备分配场景。
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu: Add group lookup by ID
  - iommu/riscv: Program QoS IDs for assigned groups
  - iommu/riscv: Expose global QoS IDs in sysfs
- 来源：https://patchwork.kernel.org/project/linux-kselftest/patch/20260714130657.46963-2-zhangzhanpeng.jasper@bytedance.com/

**[v3] iommu/riscv: Use 32-bit MMIO accesses for 64-bit registers**

- 日期：2026-07-13
- 状态：社区讨论中
- 概括：该补丁将RISC-V IOMMU驱动的64位寄存器访问改为32位MMIO读写，引入hi_lo辅助宏组合高低32位，解决不支持64位MMIO访问硬件上的兼容性问题。
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20260713122903.9458-1-zhangzhanpeng.jasper@bytedance.com/

**[RFC,1/3] iommu/riscv: Complete MRIF MSI PTE setup**

- 日期：2026-07-01
- 状态：社区讨论中
- 概括：在 iommu/riscv 中Complete MRIF MSI PTE setup。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260701040017.42707-2-zhangzhanpeng.jasper@bytedance.com/

**▸ 组织：Qualcomm**（1 patches）

**[SERIES] iommu/riscv: Enable MSI remapping, IOMMU_DMA and VFIO** （cover letter，11/11 个 patch 达到代码量阈值）

- 日期：2026-08-31
- 状态：社区讨论中
- 概括：该补丁系列使RISC-V IOMMU支持MSI重映射、IOMMU_DMA及VFIO，通过将iommufd软件MSI映射改为可增长位图并预留IOVA窗口，同时准备MSI地址列表以管理中断映射。
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
- 概括：该补丁集将缓存失效数组的遍历逻辑从各驱动和自测代码上移到 iommufd 核心统一执行，驱动仅处理单条失效命令，并新增对不支持位的拒绝检查，从而消除重复实现并增强命令校验一致性。
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
- 概括：此补丁集修复iommufd中vDEVICE分配生命周期缺陷，确保错误路径释放igroup锁、初始化成功后才发布设备，并要求ARM SMMUv3场景下vDEVICE严格对应单一Stream ID。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommufd/viommu: Publish a vDEVICE only after vdevice_init() succeeds
  - iommu/arm-smmu-v3-iommufd: Require exactly one Stream ID for a vDEVICE
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/e903f775d491296a525097e2a90b3eb6a47cf2ef.1783311134.git.nicolinc@nvidia.com/

**▸ 组织：Google**（1 patches）

**[2/2] iommufd: Periodically reschedule when unmapping**

- 日期：2026-07-14
- 状态：社区讨论中
- 概括：该改动在iommufd取消映射时遍历页面的循环中，每处理完一个PUD阶页数即调用一次cond_resched，周期性让出处理器，避免长时间占用CPU导致调度延迟。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260714210303.3967981-3-aaronlewis@google.com/

**▸ 组织：Individual Contributor**（1 patches）

**[SERIES] KVM: selftests: sev_smoke_test: Only run VM types the host offers** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-07-20
- 状态：社区讨论中
- 概括：该系列围绕 KVM: selftests: sev_smoke_test: Only run VM types the host offers，具体包括iommufd 中Plumb dma-buf memory-type (RAM vs MMIO) through the phys map、iommufd 中Look up private-interconnect phys via exporter symbols。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommufd: Plumb dma-buf memory-type (RAM vs MMIO) through the phys map
  - iommufd: Look up private-interconnect phys via exporter symbols
- 来源：https://patchwork.kernel.org/project/linux-kselftest/patch/a7ca2d885903679dc63c85620bff72fea21f5c18.1784545391.git.dwmw@amazon.co.uk/

---

### ◆ 子系统：ARM SMMU (v1/v2)（4 patches）

**▸ 组织：Qualcomm**（3 patches）

**[SERIES] iommu: qcom_iommu: implement support for instances on MSM8974** （cover letter，8/10 个 patch 达到代码量阈值）

- 日期：2026-08-09
- 状态：社区讨论中
- 概括：此补丁系列为MSM8974平台的QCOM IOMMU驱动补齐实例支持，新增SMMU全局寄存器与短描述符页表格式处理，并实现对非TZ管理实例的编程、上下文保存恢复及故障终止等能力。
- 达到阈值的 patches（8 个，显示前 5）：
  - iommu: qcom_iommu: extract context bank programming into a helper
  - iommu: qcom_iommu: support the short-descriptor pagetable format
  - iommu: qcom_iommu: handle the SMMU global register space
  - iommu: qcom_iommu: support non-TZ-managed instances
  - iommu: qcom_iommu: restore context bank state after power collapse
  - ... 及其他 3 个 patch
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260809-msm8974-iommu-upstream-v1-2-87f5cd492560@oss.qualcomm.com/

**[v4] iommu/arm-smmu: Use pm_runtime in fault handlers**

- 日期：2026-08-06
- 状态：社区讨论中
- 概括：此补丁让ARM SMMU的全局与上下文故障处理程序改用运行时PM管理，先通过pm_runtime_get_if_active确认设备活跃并加引用，处理完释放，同时将实现层回调迁入统一包装，并在挂起时禁用故障报告以防无时钟寄存器访问。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260806-smmu-rpm-v4-1-8183d007331c@oss.qualcomm.com/

**[SERIES] iommu/qcom: Misc Fixes** （cover letter，4/6 个 patch 达到代码量阈值）

- 日期：2026-07-17
- 状态：社区讨论中
- 概括：该补丁集修复高通IOMMU驱动的多个缺陷：反转故障检测、运行时电源管理错误处理、页表操作泄漏及时钟顺序，并优化pgtbl_ops发布时机，提升驱动稳定性。
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
- 概括：针对a7xx系列GPU启用LPAC功能，核心改动是在arm-smmu-qcom驱动中为LPAC设备分配独立的拆分地址空间，并修正GPU与LPAC在流标识符SID到上下文bank映射上的错误，确保两者隔离与正确寻址。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu: arm-smmu-qcom: Configure lpac device with split address space
- 来源：https://patchwork.kernel.org/project/dri-devel/patch/20260705-descriptive-name-lpac-upstream-v1-1-01d50c3e0c99@gmail.com/

---

### ◆ 子系统：Intel VT-d（3 patches）

**▸ 组织：Individual Contributor**（2 patches）

**[v2] intel_iommu: Expose SMPWC when SVM is enabled**

- 日期：2026-08-08
- 状态：社区讨论中
- 概括：Intel IOMMU 在启用 SVM 时新增暴露 SMPWC 能力位，并校验宿主 IOMMU 是否支持该可扩展模式一致性遍历，否则拒绝初始化以避免功能不匹配。
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260808153626.873965-1-clement.mathieu--drif@bull.com/

**[v2] intel_iommu: Check address mask before using it in pasid-based iotlb invalidation**

- 日期：2026-07-24
- 状态：社区讨论中
- 概括：该补丁为基于 PASID 的 IOTLB 失效增加地址掩码合法性校验，拒绝大于硬件最大值的掩码并添加断言，防止越界使用导致异常。
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260724111424.376680-1-clement.mathieu--drif@bull.com/

**▸ 组织：Intel**（1 patches）

**[SERIES] intel_iommu: Enable PRQ support for passthrough device** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-08-31
- 状态：社区讨论中
- 概括：本补丁系列为透传设备启用Intel IOMMU的PRQ支持，通过修改intel_iommu_accel模块，在底半部释放故障队列资源，并添加PRQ响应接收与注入机制，使直通设备能够利用页请求队列服务。
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
- 概括：此补丁在tegra241-cmdqv驱动中新增VCMDQ基地址的48位硬件上限检查，拒绝超限值并告警，避免地址被截断导致硬件从错误位置取命令。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260729220329.805417-1-nicolinc@nvidia.com/

**[SERIES] iommu/tegra241-cmdqv: Fix error-interrupt races and VINTF lifecycle bugs** （cover letter，5/11 个 patch 达到代码量阈值）

- 日期：2026-07-14
- 状态：社区讨论中
- 概括：该补丁系列修复 Tegra241 命令队列虚拟化驱动中错误中断与 VINTF 生命周期的竞态及泄漏，通过完善初始化顺序、同步中断处理、收紧 vSID 校验和错误映射边界，并修正资源释放与回退逻辑来增强稳定性。
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
- 概括：该补丁在iommu_dma_alloc中直接检查dma_alloc_from_pool返回的page是否为空，若分配失败立即返回NULL，避免后续使用无效页码；针对原子池分配与普通页面分配路径分别处理，提高错误路径的显式判断与安全性。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260717180442.110954-4-aneesh.kumar@kernel.org/

---

### ◆ 子系统：IOMMU Page Table（1 patches）

**▸ 组织：Qualcomm**（1 patches）

**[v4] iommu/io-pgtable-arm: Add support for contiguous hint bit**

- 日期：2026-08-04
- 状态：社区讨论中
- 概括：此补丁为ARM LPAE页表映射加入连续提示位支持，依据不同页粒度动态计算连续页组大小，并在对齐映射批量写入时设置PTE的contiguous位以减少页表开销，同时保留通过quirk禁用该功能的选项。
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

*报告由 Linux Patches Tracker 自动生成 | 2026-09-08 16:24:37*
