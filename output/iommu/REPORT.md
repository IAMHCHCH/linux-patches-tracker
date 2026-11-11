# Linux IOMMU 子系统 Patch 追踪报告

---

## 报告信息

| 项目 | 内容 |
|------|------|
| 数据来源 | patchwork.kernel.org |
| 生成日期 | 2026-11-11 |
| 报告区间 | 2026-09-01 至 2026-10-31 |
| 仓库 | [https://github.com/IAMHCHCH/linux-patches-tracker](https://github.com/IAMHCHCH/linux-patches-tracker) |

---

## 统计概览

### 按状态分类

| 状态 | 数量 | 占比 |
|------|------|------|
| 社区讨论中 | 69 | 87.3% |
| 已合入 | 5 | 6.3% |
| 已关闭 | 5 | 6.3% |
| **总计** | **79** | **100%** |

### 按组织分类（TOP 15）

| 组织 | 数量 | 占比 |
|------|------|------|
| Google | 11 | 13.9% |
| Individual Contributor | 9 | 11.4% |
| NVIDIA | 8 | 10.1% |
| Qualcomm | 7 | 8.9% |
| Alibaba | 7 | 8.9% |
| Kernel.org | 6 | 7.6% |
| Intel | 4 | 5.1% |
| NXP | 3 | 3.8% |
| AMD | 3 | 3.8% |
| 东南大学 | 2 | 2.5% |
| 归属待核实（sanechips.com.cn） | 2 | 2.5% |
| 归属待核实（jannau.net） | 1 | 1.3% |
| SiFive | 1 | 1.3% |
| 归属待核实（foxmail.com） | 1 | 1.3% |
| 归属待核实（utexas.edu） | 1 | 1.3% |

### 按子系统分类

| 子系统 | 数量 | 占比 |
|--------|------|------|
| ARM SMMUv3 | 18 | 22.8% |
| IOMMU Core | 16 | 20.3% |
| RISC-V IOMMU | 12 | 15.2% |
| IOMMUFD | 11 | 13.9% |
| Intel VT-d | 6 | 7.6% |
| AMD IOMMU | 5 | 6.3% |
| IOMMU DMA-API | 4 | 5.1% |
| ARM SMMU (v1/v2) | 3 | 3.8% |
| IOMMU SVA/SVM | 2 | 2.5% |
| IOMMU Page Table | 1 | 1.3% |
| IOMMUPT | 1 | 1.3% |

## 重点 Patch Top20 清单

### 已合入

| 厂商 | 简介 |
|------|------|
| Red Hat | [PATCH v2 00/75] virtio: fix exit(1) on DMA mapping failure during migration restore ------这批补丁修复QEMU迁移恢复路径：virtio请求DMA映射失败不再退出而报错，校验配置长度避免恶意流造成CPU空转，拒绝重复使能已启用队列；并新增virtio-media设备及其共享内存区域。Intel IOMMU支持PRI并发故障处理、完整写页表标志、仅对可写项置脏位，SVM模式下暴露一致性遍历；AMD IOMMU占位调用返回空能力。 |
| Intel | [PATCH v9 00/6] intel_iommu: Enable PRQ support for passthrough device ------为Intel IOMMU直通设备启用页请求队列支持：客户机开启PRQ后，在主机侧分配故障队列对象，把主机产生的可恢复故障事件注入客户机，并将客户机响应写回主机；对PRQ溢出或满错误返回成功响应并丢弃请求，其他错误返回无效请求响应。失效PASID条目时，释放故障队列和文件描述符改为安排到下半部执行，避开轮询退出竞争，确保资源释放成功。 |
| AMD | [PATCH v1 00/8] amd_iommu: Allow IOMMU to attach on non system bus ------允许AMD IOMMU挂载在非系统PCI总线上，如pcie根端口或pxb-pci，只管理该总线下的设备子集；通过向上查找第一个根总线来注册IOMMU操作并构建IVRS表，使中断重映射仅作用于其管理设备。同时仅在支持中断重映射时为IOAPIC分配IOMMU地址空间，关闭时IOAPIC改回系统地址空间，避免中断被错误翻译。 |
| Intel | [v8,6/6] intel_iommu_accel: teardown FAULTQ resources in bottom half ------当PASID条目失效需要释放故障队列对象和文件描述符时，原先在拆除读处理函数后立即释放，可能与主循环轮询退出存在竞争，造成释放忙错误。现在把这些资源的释放推迟到下半部执行，先让轮询退出并释放文件引用，再关闭描述符并释放故障队列标识，避免偶发释放失败。 |
| Individual Contributor | [3/4] iommufd: Reject a zero-length dirty bitmap request ------IOMMUFD脏位图查询校验长度时，零长度会在减一后回绕成很大的长度，从而以无界长度分配位图并可能导致扫描整个输入输出地址空间。修复是直接在减一之前拒绝零长度请求，确保无效的脏位图查询立即返回参数错误。 |
| NVIDIA | [PATCH] iommupt: Do not allow PTEs to be split when dirty logging ------通用页表在脏位记录中原本允许把单个页表项拆分后部分写入位图，会把脏内存误报为干净；清理收集也只覆盖位图能容纳的部分。现在改为按每个页表项的完整输入输出地址范围更新位图并加入收集，位图代码拒绝放不下的范围，保证脏页不丢失。 |

### 社区讨论

| 厂商 | 简介 |
|------|------|
| Google | [PATCH v9 00/25] KVM: arm64: SMMUv3 driver for pKVM (trap and emulate) ------在pKVM保护虚拟化环境中，主机可访问SMMU寄存器，无法防止其发起非隔离DMA。为在EL2实现DMA隔离，新增SMMUv3陷阱与模拟驱动：将MMIO捐献给hypervisor使主机访问陷入，在EL2维护同步于主机阶段2页表的影子页表，并模拟命令队列、流表等硬件状态，向主机呈现虚拟SMMU；同时将队列、配置解析、范围失效等公共代码拆出供主机与EL2复用。 |
| Oracle | [PATCH v3 00/5] amd_iommu: Bugfix and Cleanup for IO Page Fault ------修复 QEMU AMD IOMMU 模拟器的页错误处理和 MMIO 行为：页错误报告改为使用包含总线号的完整设备号，避免桥后设备错误记到错误的请求者；去掉重复的 MSI 能力；扩展特性寄存器改为只读；状态寄存器不再接受未支持的全局地址日志位写入，防止客户机旧内核清除事件中断时意外锁存全局地址日志溢出并反复重启。 |
| NVIDIA | [PATCH v11 00/11] iommu/arm-smmu-v3: Adopt the crashed kernel's stream table for kdump ------为kdump内核引入崩溃内核流表接管：探测时保留SMMU使能状态并继续沿用崩溃内核的流表和页表翻译在途DMA，避免中止或绕过在途DMA引发致命PCIe错误或物理内存破坏；扫描流表并保留崩溃内核已用的ASID和VMID，防止重用导致陈旧缓存翻译错配。kdump内核禁用事件队列和页请求队列，跳过相关初始化和中断，并把ASID空间改为每个SMMU独立管理。 |
| NVIDIA | [PATCH v5 00/15] iommu/arm-smmu-v3: Add PRI support ------为 ARM SMMUv3 增加 PCI 设备 PRI 页请求支持，使设备因缺页发出的页请求能由 IOMMU 通过命令队列回复；同时放宽 IOPF 队列分配条件，让仅支持 STALL、不支持 SVA 的硬件也能使用，并修复设备分离时事件队列和 IOPF 工作可能引用已释放域的问题。 |
| Google | [PATCH v11 00/16] iommu/arm-smmu-v3: Implement Runtime/System Sleep ops ------为 ARM SMMUv3 实现运行时电源管理和系统睡眠支持，使 SMMU 空闲时可下电，恢复时重新初始化中断、MSI 配置和队列索引；挂起前通过门控命令提交并排空命令队列，避免未完成的命令导致超时或状态丢失，并增加 KUnit 测试覆盖运行时电源管理路径。 |
| Google | [PATCH v1 00/22] DMA_PMD: PMD_SIZE-backed IO buffer pools ------为减少 IOMMU 的 IOTLB 压力和映射开销，新增基于物理连续 2MB 大页的 IO 缓冲区池，供设备驱动分配流式或长期缓冲，IOMMU 页表使用大页叶子映射，减少缺页和刷新；池化分配与回收摊薄映射成本，并带后台清理、全局上限和收缩器控制空闲内存。 |
| NVIDIA | [PATCH v8 00/9] Organize the SMMUv3 invalidation flow so iommupt can use it ------针对ARM SMMUv3的失效流程，为未来iommupt做准备。已发现范围失效可能从CONT条目中间拆分，在MMU-700/S3等硬件上导致失效不完整，SVA场景可被恶意触发。现在把失效参数封装并预计算命令，SVA失效改为单条覆盖整个可能CONT的范围失效，普通路径采用损坏位图描述叶子和表级变化，将范围失效限制在最多两条命令，并支持DS扩展SCALE上限。 |
| NXP | [PATCH v7 00/7] iommu/arm-smmu-v3: Support shared Stream IDs ------在恩智浦i.MX95等流ID空间有限的SoC上，多个DMA设备被配置为同一流ID，原SMMUv3驱动不支持共享，第二个设备无法探测。现在允许单流ID的多个设备共享同一流对象并加入同一IOMMU组，使用域级CD表让它们指向相同配置；共享ID时禁用SVA、PASID、ATS和停等需要唯一设备映射的功能，并在释放或阻断时避免中止仍活跃的共享设备。 |
| Kernel.org | [PATCH v7 00/16] iommufd: vIOMMUs and TSM guest requests for confidential guests ------为保密虚拟机场景，在 iommufd 框架中引入虚拟 IOMMU 和可信安全模块（TSM）客户机请求通道。将 VFIO 设备与对应 KVM 文件关联，使虚拟设备能把客户机发出的 TSM 命令转发给管理该设备的安全模块并返回响应；同时允许 PCI 安全模块后端提供虚拟 IOMMU 操作，并在断开时等待依赖虚拟设备释放后完成。KVM 引用改为基于文件计数，简化生命周期管理。 |
| Qualcomm | [PATCH v1 00/3] iommu: qcom: Fix the MSM GPU and display with DMA-address based mappings ------高通 Adreno GPU 和 MDP5 显示控制器需要 DMA 映射返回物理地址并自行填入设备页表，但相关输入输出内存管理单元驱动未为它们指定直通默认域，导致缓冲区被映射到未使用的默认域虚拟地址，db410c 上 GPU 无法启动，db820c 上 GPU 启动时系统复位；同时全量 TLB 失效只同步不真正作废条目，复用虚拟地址后 GPU 因陈旧条目挂起。 |
| NVIDIA | [PATCH v3 00/10] Make the 32-bit ARM DMA API work with normal IOMMU DMA default domains (+ Tegra PoC) ------让 32 位 ARM 平台能够使用 IOMMU 核心管理的 DMA 默认域，不再因传统 ARM DMA 实现而被强制成身份域；在 Tegra SMMU 上先对显示和 Host1x 设备启用真实 DMA 域，并让显示控制器在驱动接管、硬件不再扫描启动画面后才开启翻译，避免启动期间产生翻译故障。 |
| Individual Contributor | [PATCH v1 00/6] iommufd: harden DMA-BUF PAL setup and release ------修复 iommufd 中 DMA-BUF 物理地址列表映射和释放的竞态问题：固定失败时保留原始错误码，映射成功后才发布物理列表和附件，释放时在持锁阶段清除指针并完成解固定，互斥锁延后到分离之后销毁，避免反向映射回调与释放过程重复释放或访问已销毁锁；自测增加故障注入覆盖失败清理路径。 |
| NVIDIA | [PATCH v9 00/2] Organize the SMMUv3 invalidation flow so iommupt can use it ------为让未来的iommupt页表管理能复用SMMUv3的失效流程，改变TLB失效描述方式：原使用地址范围和页大小等参数信息不足，无法正确计算单步失效和范围失效。现在改用叶子和表级损坏位图来表达失效请求，使驱动能计算合适的步长和范围失效提示；同时支持DS扩展将范围失效的SCALE上限提高到39，适配支持该特性的硬件。 |
| Linux Community | [PATCH v7 00/5] iommu/riscv: Enable MSI remapping and IOMMU_DMA ------为 64 位 RISC-V 平台启用输入输出内存管理单元（IOMMU）的直接内存访问（DMA）和消息信号中断（MSI）重映射。针对 IMSIC 中断亲和性变化需要覆盖所有可能目标的问题，先构建按逻辑处理器索引的物理地址列表，再由 IOMMU 后端将其映射为连续输入输出虚拟地址范围并缓存基址。 |
| Amazon | [PATCH v1 00/3] iommu: Reduce iommu_probe_device_lock contention ------并行设备探测（尤其是虚拟功能初始化）时，全局探测锁成为争用热点，因为sysfs成员链接发布和首设备默认域设置都在锁内完成。现在把sysfs链接发布拆分为独立步骤并移到全局锁外，默认域设置也借助组列表延迟到锁外，两项改由组互斥锁保护；失败路径保持回滚语义，从而缩短全局锁持有时间，降低探测路径上的串行等待。 |
| 归属待核实（shutemov.name） | [v7,2/2] iommu/arm-smmu-v3: Default queue depths to one page in a kdump kernel ------针对 kdump 捕获内核内存紧张，ARM SMMUv3 启动时仍按硬件最大深度分配命令、事件和 PRI 三个队列，单个可达 4MB，其中事件和 PRI 队列随后会被关闭，造成浪费；改为在捕获内核中将三个队列深度都限制为一页条目，节省最多约 12MB 内存，且队列只承载命令和故障记录，不影响转储吞吐量。 |
| 归属待核实（utexas.edu） | [PATCH] iommu/sva: Charge IOPF allocations to the faulting mm's memcg ------设备引发SVA缺页时，处理线程未设置活动内存控制组，导致文件页缓存分配落入根控制组，逃过任务的内存上限。现在处理故障前切换到故障进程的内存控制组，完成缺页后恢复之前的活动控制组，使设备引发的页缓存正确计入所属控制组。 |
| EPAM | [v13,09/14] iommu/ipmmu-vmsa: Implement suspend/resume callbacks ------为 Xen 中的 R-Car IPMMU-VMSA 驱动增加系统挂起/恢复支持，挂起时保存根 IPMMU 的活动上下文和缓存 IPMMU 的微 TLB 配置，恢复时先写回根上下文再恢复缓存微 TLB，避免微 TLB 指向尚未恢复的上下文而暴露过期状态；该功能仅在 H3ULCB（R-Car Gen3）上测试。 |
| NVIDIA | [v2,07/11] iommu: Let 32-bit ARM drivers opt into a DMA API default domain ------32位ARM的IOMMU驱动原先无法请求DMA域作为默认域，统一被强制设为直通域，因为ARM DMA API会自行安装非托管域。现在把ARM DMA API状态视为普通域标记，移除强制覆盖，允许驱动显式选择DMA域，但仅作为显式选择而不作为默认回退，现有32位ARM驱动行为均保持不变。 |
| Qualcomm | [PATCH] iommu: arm-smmu-qcom: Skip fault-info reads when suspended ------高通Adreno GPU的SMMU故障信息收集函数在无运行时电源引用下读取寄存器。故障产生后GPU可能在处理线程到达前放弃电源投票，使SMMU进入挂起，此时读寄存器可能引发片上网络错误和异步系统错误。现在先尝试获取运行时电源引用，若设备已不活跃则跳过寄存器读取并记录警告，避免挂起期间访问。 |

---

## 已合入 Patches

### ◆ 子系统：Intel VT-d（3 patches）

**▸ 组织：Intel**（2 patches）

**[SERIES] intel_iommu: Enable PRQ support for passthrough device** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-10-20
- 状态：已合入
- 作者邮箱：Duan, Zhenzhong <zhenzhong.duan@intel.com>
- 概括：为Intel IOMMU直通设备启用页请求队列支持：客户机开启PRQ后，在主机侧分配故障队列对象，把主机产生的可恢复故障事件注入客户机，并将客户机响应写回主机；对PRQ溢出或满错误返回成功响应并丢弃请求，其他错误返回无效请求响应。失效PASID条目时，释放故障队列和文件描述符改为安排到下半部执行，避开轮询退出竞争，确保资源释放成功。
- 达到阈值的 patches（4 个，显示前 5）：
  - intel_iommu_accel: Add PRQ injection for passthrough device
  - intel_iommu_accel: Guard VTDAccelPASIDCacheEntry definition
  - intel_iommu_accel: Accept PRQ response for passthrough device
  - intel_iommu_accel: Teardown FAULTQ resources in bottom half
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20261020091955.1607161-5-zhenzhong.duan@intel.com/

**[v8,6/6] intel_iommu_accel: teardown FAULTQ resources in bottom half**

- 日期：2026-10-09
- 状态：已合入
- 作者邮箱：Duan, Zhenzhong <zhenzhong.duan@intel.com>
- 概括：当PASID条目失效需要释放故障队列对象和文件描述符时，原先在拆除读处理函数后立即释放，可能与主循环轮询退出存在竞争，造成释放忙错误。现在把这些资源的释放推迟到下半部执行，先让轮询退出并释放文件引用，再关闭描述符并释放故障队列标识，避免偶发释放失败。
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20261009090737.3930000-7-zhenzhong.duan@intel.com/

**▸ 组织：Red Hat**（1 patches）

**[SERIES] virtio: fix exit(1) on DMA mapping failure during migration restore** （cover letter，5/7 个 patch 达到代码量阈值）

- 日期：2026-09-11
- 状态：已合入
- 作者邮箱：Michael S. Tsirkin <mst@redhat.com>
- 概括：修正 QEMU 中 x86 输入输出内存管理单元模拟代码的若干正确性问题：为页请求状态处理加锁以支持并发页请求，一次性写入页表项的所有标志位，并仅在页表项实际暴露写权限时设置脏位；从 AMD 模拟的默认扩展特性和 ACPI 表中移除未实现的页请求和硬件错误特性，更新地址大小宏，使特性暴露与模拟能力一致。改动避免客户机启用不支持的能力或触发竞态，减少客户机可导致的异常行为。
- 达到阈值的 patches（5 个，显示前 5）：
  - intel_iommu: Support concurrent page fault handling with PRI
  - intel_iommu: Always write all the flags passed to vtd_set_flag_in_pte
  - intel_iommu: Only set dirty bit when PTE exposes write permission
  - intel_iommu: Expose SMPWC when SVM is enabled
  - amd_iommu: Return empty efr for stub call
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/f19df1b13d1a0b5601b4b58067b8c2e91ae76ef3.1789117222.git.mst@redhat.com/

---

### ◆ 子系统：IOMMUFD（1 patches）

**▸ 组织：NVIDIA**（1 patches）

**iommupt: Do not allow PTEs to be split when dirty logging**

- 日期：2026-10-15
- 状态：已合入
- 作者邮箱：Jason Gunthorpe <jgg@nvidia.com>
- 概括：通用页表在脏位记录中原本允许把单个页表项拆分后部分写入位图，会把脏内存误报为干净；清理收集也只覆盖位图能容纳的部分。现在改为按每个页表项的完整输入输出地址范围更新位图并加入收集，位图代码拒绝放不下的范围，保证脏页不丢失。
- 来源：https://patchwork.kernel.org/project/linux-kselftest/patch/0-v1-5bb926ff73ec+576-iommufd_dirty_jgg@nvidia.com/

---

### ◆ 子系统：AMD IOMMU（1 patches）

**▸ 组织：AMD**（1 patches）

**[SERIES] amd_iommu: Allow IOMMU to attach on non system bus** （cover letter，2/5 个 patch 达到代码量阈值）

- 日期：2026-10-14
- 状态：已合入
- 作者邮箱：Sairaj Kodilkar <sarunkod@amd.com>
- 概括：允许 AMD IOMMU 在非系统总线上实例化，以隔离 PCI 扩展总线下的设备子集。新增按设备查找所属 IOMMU 的机制，AMD 和 Intel 虚拟 IOMMU 均能返回对应状态；KVM 中断重映射改为先按 PCI 设备定位实际服务的 IOMMU，非 PCI 设备仅在中断重映射启用时回退默认单元。
- 达到阈值的 patches（2 个，显示前 5）：
  - amd_iommu: Assign ioapic_as only when interrupt remapping is supported.
  - amd_iommu: Allow IOMMU to attachment on non-system (pcie.0) bus
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20261014053433.24564-2-sarunkod@amd.com/

---

## 社区讨论中 Patches

### ◆ 子系统：ARM SMMUv3（18 patches）

**▸ 组织：Google**（6 patches）

**[SERIES] KVM: arm64: SMMUv3 driver for pKVM (trap and emulate)** （cover letter，19/19 个 patch 达到代码量阈值）

- 日期：2026-10-15
- 状态：社区讨论中
- 作者邮箱：Mostafa Saleh <smostafa@google.com>
- 概括：在pKVM保护虚拟化环境中，主机可访问SMMU寄存器，无法防止其发起非隔离DMA。为在EL2实现DMA隔离，新增SMMUv3陷阱与模拟驱动：将MMIO捐献给hypervisor使主机访问陷入，在EL2维护同步于主机阶段2页表的影子页表，并模拟命令队列、流表等硬件状态，向主机呈现虚拟SMMU；同时将队列、配置解析、范围失效等公共代码拆出供主机与EL2复用。
- 达到阈值的 patches（19 个，显示前 5）：
  - iommu/arm-smmu-v3: Move Queue and STE functions to header
  - iommu/arm-smmu-v3: Move IDR parsing to common functions
  - iommu/arm-smmu-v3: Move hitless machinery to common code
  - iommu/arm-smmu-v3-kvm: Probe SMMU HW
  - iommu/arm-smmu-v3-kvm: Emulate GBPA
  - ... 及其他 14 个 patch
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20261015200903.2735565-3-smostafa@google.com/

**[SERIES] iommu/arm-smmu-v3: Implement Runtime/System Sleep ops** （cover letter，7/14 个 patch 达到代码量阈值）

- 日期：2026-09-29
- 状态：社区讨论中
- 作者邮箱：Pranjal Shrivastava <praan@google.com>
- 概括：为 ARM SMMUv3 及 Tegra241 CMDQV 实现运行时电源管理和系统休眠支持：在命令队列生产索引中嵌入停止标志，挂起开始后阻止新命令提交，再排空命令和虚拟队列；恢复时重建中断和 MSI 配置并恢复生产和消费索引。休眠前处理未决全局错误，避免硬件状态丢失后无法记录。这样 SMMU 不活跃时可进入低功耗状态，唤醒后继续正确执行地址转换。
- 达到阈值的 patches（7 个，显示前 5）：
  - iommu/arm-smmu-v3: Refactor arm_smmu_setup_irqs
  - iommu/tegra241-cmdqv: Restore PROD and CONS after resume
  - iommu/arm-smmu-v3: Enable pm_runtime and setup devlinks
  - iommu/arm-smmu-v3: Invoke pm_runtime before hw access
  - iommu/arm-smmu-v3: Implement pm_runtime & system sleep ops
  - ... 及其他 2 个 patch
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/20260929034510.2023173-3-praan@google.com/

**[SERIES] iommu/arm-smmu-v3: Implement Live Update support** （cover letter，8/9 个 patch 达到代码量阈值）

- 日期：2026-09-29
- 状态：社区讨论中
- 作者邮箱：Pranjal Shrivastava <praan@google.com>
- 概括：为 ARM SMMUv3 增加 kexec 切换期间的在线更新能力：保留流表、上下文描述符表和事件队列，并保持 SMMU 开启，让已保留设备的 DMA 在切换中继续；新内核接管后恢复这些表、继承原有 ASID/VMID，并为未保留设备安装中止描述符后刷新缓存，失败时退回整体停用，从而避免 DMA 流量中断。
- 达到阈值的 patches（8 个，显示前 5）：
  - iommu/kho: Extend IOMMU KHO ABI for ARM SMMUv3
  - iommu/arm-smmu-v3: Implement KHO preservation for STEs
  - iommu/arm-smmu-v3: Implement Live Update Stream Table restoration
  - iommu/arm-smmu-v3: Implement Live Update CD Table restoration
  - iommu/arm-smmu-v3: Implement CD Table preservation
  - ... 及其他 3 个 patch
- 来源：https://patchwork.kernel.org/project/kexec/patch/20260929071950.2710070-2-praan@google.com/

**[SERIES] iommu/arm-smmu-v3: Fixes reported by Sashiko** （cover letter，1/5 个 patch 达到代码量阈值）

- 日期：2026-09-24
- 状态：社区讨论中
- 作者邮箱：Mostafa Saleh <smostafa@google.com>
- 概括：为 ARM SMMUv3 的流表和上下文描述符表在发布 L1 指针前补充写屏障，确保清零后的 L2 表先被硬件观察到，避免 SMMU 读取未初始化内容；并修复配套单元测试中描述符解析硬编码、数组合并缺少错误检查、边界断言后继续越界读取以及计数长度缺失触发越界等问题，使测试结果准确且不会访问非法指针。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/arm-smmu-v3: Ensure L2 tables are visible before L1 ptrs
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260924085616.300650-2-smostafa@google.com/

**[v10,08/15] iommu/arm-smmu-v3: Cache and restore MSI config**

- 日期：2026-09-08
- 状态：社区讨论中
- 作者邮箱：Pranjal Shrivastava <praan@google.com>
- 概括：针对 ARM SMMUv3 设备在系统挂起恢复后消息信号中断（MSI）配置寄存器内容丢失的问题，首次写入 MSI 地址和数据时进行缓存，恢复时先清零相关寄存器，再通过平台设备 MSI 重写接口重新配置事件队列、全局错误和页请求中断。若 MSI 初始化失败回退到有线中断，则清除 MSI 能力标记，避免恢复阶段重复尝试。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260908171712.356645-9-praan@google.com/

**iommu/arm-smmu-v3-sva: Relax ASID requirements**

- 日期：2026-09-07
- 状态：社区讨论中
- 作者邮箱：Mostafa Saleh <smostafa@google.com>
- 概括：放宽 ARM SMMUv3 共享虚拟地址（SVA）支持的地址空间标识（ASID）位宽限制。早期实现依赖 CPU 共享 ASID 进行 TLB 失效，要求 SMMU 的 ASID 空间不小于 CPU；后来该依赖已移除，SMMU 不再需要与 CPU 的 ASID 位宽匹配。因此删除相关检查，只根据 SMMU 自身 ASID 能力判断是否支持共享虚拟地址，避免因 CPU ASID 较小而错误拒绝。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260907154928.4012151-1-smostafa@google.com/

**▸ 组织：NVIDIA**（5 patches）

**[SERIES] iommu/arm-smmu-v3: Adopt the crashed kernel's stream table for kdump** （cover letter，8/11 个 patch 达到代码量阈值）

- 日期：2026-10-05
- 状态：社区讨论中
- 作者邮箱：Nicolin Chen <nicolinc@nvidia.com>
- 概括：Arm SMMUv3 在崩溃转储内核中采用上一内核的流表，避免重置硬件导致在飞 DMA 被丢弃或错误绕过转换破坏内存。启动时保留 SMMU 使能和流表基址，映射并校验旧流表，不可信则丢弃；同时扫描并保留旧内核正在使用的地址空间和虚拟机标识，防止新域复用旧缓存项；禁用事件队列和页请求队列，以免崩溃留下的脏页表产生事件噪声。设备驱动探测前沿用原页表完成在飞 DMA，待设备静默后再恢复管理。
- 达到阈值的 patches（8 个，显示前 5）：
  - iommu/arm-smmu-v3: Make the ASID space per SMMU instance
  - iommu/arm-smmu-v3: Add ARM_SMMU_OPT_KDUMP_ADOPT for kdump kernel
  - iommu/arm-smmu-v3: Disable the EVTQ and the PRIQ in a kdump kernel
  - iommu/arm-smmu-v3: Retain CR0_SMMUEN during kdump device reset
  - iommu/arm-smmu-v3-kexec: Reserve crashed kernel's ASIDs and VMIDs
  - ... 及其他 3 个 patch
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/e027296ac9db58fb7d69b1b4b5e4a2ed192dd401.1791226953.git.nicolinc@nvidia.com/

**[SERIES] Organize the SMMUv3 invalidation flow so iommupt can use it** （cover letter，7/7 个 patch 达到代码量阈值）

- 日期：2026-10-03
- 状态：社区讨论中
- 作者邮箱：Jason Gunthorpe <jgg@nvidia.com>
- 概括：针对ARM SMMUv3的失效流程，为未来iommupt做准备。已发现范围失效可能从CONT条目中间拆分，在MMU-700/S3等硬件上导致失效不完整，SVA场景可被恶意触发。现在把失效参数封装并预计算命令，SVA失效改为单条覆盖整个可能CONT的范围失效，普通路径采用损坏位图描述叶子和表级变化，将范围失效限制在最多两条命令，并支持DS扩展SCALE上限。
- 达到阈值的 patches（7 个，显示前 5）：
  - iommu/arm-smmu-v3: Pass the parameters for the invalidation in a struct
  - iommu/arm-smmu-v3: Move pgsize out of arm_smmu_inv
  - iommu/arm-smmu-v3: Handle ARM erratum for CONT under invalidation with SVA
  - iommu/arm-smmu-v3: Populate the tlbi at the top of the call chain
  - iommu/arm-smmu-v3: Precompute the invalidation commands
  - ... 及其他 2 个 patch
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/2-v8-1eaaed5e0433+3d3d2d-smmu_tlbi_jgg@nvidia.com/

**[SERIES] iommu/arm-smmu-v3: Quarantine device upon ATC invalidation timeout** （cover letter，2/10 个 patch 达到代码量阈值）

- 日期：2026-09-23
- 状态：社区讨论中
- 作者邮箱：Nicolin Chen <nicolinc@nvidia.com>
- 概括：修复 PCI 和 CXL 复位探测时误暂停 IOMMU 或错误宣告不存在的总线复位，避免探测本身导致设备 DMA 超时和数据丢失；同时修复重复流标识导致红黑树被清空的问题，并在 SMMUv3 命令队列中按位图跟踪 ATC 失效超时，超时后隔离设备，复位失败也不会重新挂回正常域，防止陈旧 ATC 条目可能引起内存损坏。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/arm-smmu-v3: Thread arm_smmu_master_domain on a per-master list
  - iommu/arm-smmu-v3: Quarantine ATS after an ATC invalidation timeout
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/5ddbd81323f86d045072ebf410a6f87da4f2796f.1790188511.git.nicolinc@nvidia.com/

**[SERIES] iommu/arm-smmu-v3: Add PRI support** （cover letter，10/12 个 patch 达到代码量阈值）

- 日期：2026-09-15
- 状态：社区讨论中
- 作者邮箱：Nicolin Chen <nicolinc@nvidia.com>
- 概括：为 ARM SMMUv3 增加 PCI 页请求支持，使支持 PRI 的设备在缺页时能上报并接收响应。同时修复启用页请求时的生命周期问题：在设备脱离域时排空硬件事件队列并同步中断和页面请求工作，避免旧域被释放后仍被处理；在只有停顿特性而没有 SVA 时也分配 IOPF 队列，防止空指针；关闭 SMMU 前先停用底层实现，PRI 队列溢出时丢弃不完整故障。仍存在由 IOMMU 核心引起的残余竞态窗口，需后续排序修复。
- 达到阈值的 patches（10 个，显示前 5）：
  - iommu/arm-smmu-v3: Drain in-flight fault events on domain detach
  - iommu/arm-smmu-v3: Flush in-flight fault work on domain detach
  - iommu/arm-smmu-v3: Disable the queue IRQs before disabling the SMMU
  - iommu/arm-smmu-v3: Submit CMDQ_OP_PRI_RESP for IOPF event
  - iommu/arm-smmu-v3: Allocate IOPF queue without FEAT_SVA
  - ... 及其他 5 个 patch
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/f74817bb45a4bfcda966d9b5ca366c649b6dfe46.1789446520.git.nicolinc@nvidia.com/

**[SERIES] iommu/arm-smmu-v3: Support guest-level Realm VSMMU (Part-1)** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-09-10
- 状态：社区讨论中
- 作者邮箱：Nicolin Chen <nicolinc@nvidia.com>
- 概括：为 Arm CCA 机密虚拟机引入领域级虚拟 SMMU 支持：通过领域服务接口命令探测并验证 T=1 虚拟 SMMU，拒绝 T=0 实例，激活后将其队列和页表分配保持在私有内存；在 IOMMU 核心中标记机密实例，为受信任设备实现 TDISP T=0 与 T=1 两种流状态，T=0 设备停放在阻止域并跳过直接映射保留区域，拒绝安装翻译域。适用于需要保护设备 DMA 翻译表不被宿主篡改的机密虚拟化场景。
- 达到阈值的 patches（4 个，显示前 5）：
  - iommu: Let a driver mark an IOMMU as confidential
  - iommu: Park TDISP T=0 devices in the blocking domain
  - iommu: Introduce TDISP T=0 state for confidential IOMMUs
  - iommu/arm-smmu-v3: Probe a guest-level Realm VSMMU via RSI commands
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/a2b4ecab20635c1b0defa47407af23ff901c778d.1789010941.git.nicolinc@nvidia.com/

**▸ 组织：NXP**（3 patches）

**[SERIES] iommu/arm-smmu-v3: Support shared Stream IDs** （cover letter，6/7 个 patch 达到代码量阈值）

- 日期：2026-10-30
- 状态：社区讨论中
- 作者邮箱：Peng Fan <peng.fan@oss.nxp.com>
- 概括：针对 NXP i.MX95 等 SMMU 流 ID 数量有限的平台，允许多个设备共享同一流 ID。原实现会拒绝第二个使用已占用流 ID 的设备，或需复制流状态。现在流对象单独分配，多个主设备直接指向同一流对象并加入同一 IOMMU 组，共用域级上下文描述表；共享时禁用 SVA、PASID、ATS 等依赖唯一 SID 映射的功能，且一个设备释放或阻断时不会中止其他共享者的 DMA。
- 达到阈值的 patches（6 个，显示前 5）：
  - iommu/arm-smmu-v3: Group aliasing devices into the same IOMMU group
  - iommu/arm-smmu-v3: Wire up shared-SID STE ordering and feature gating
  - iommu/arm-smmu-v3: Allocate streams individually
  - iommu/arm-smmu-v3: Delay stream allocation to inside the mutex
  - iommu/arm-smmu-v3: Use a per-domain CD table for non-PASID streams
  - ... 及其他 1 个 patch
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20261030-smmu-shared-sid-ver7-2026-10-26-v7-6-961726ebd6ab@Example.Com/

**[RFC,v4,1/4] iommu/arm-smmu-v3: Skip duplicate SIDs when erasing streams from RB tree**

- 日期：2026-10-01
- 状态：社区讨论中
- 作者邮箱：Peng Fan <peng.fan@oss.nxp.com>
- 概括：针对桥接 PCI 设备可能产生重复流 ID 的情况，修正 ARM SMMUv3 移除与错误回滚时对红黑树的擦除：重复节点在插入时未真正链入，但仍被无条件擦除，可能破坏红黑树。由于流数组按 ID 排序后重复项相邻，现在擦除时遇到与前一项相同的 ID 就跳过，确保只删除实际插入过的节点。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20261001-smmu-shared-sid-ver3-v4-1-06b34fb2e691@nxp.com/

**[RFC,v2,1/4] iommu/arm-smmu-v3: Convert streams from RB tree to XArray**

- 日期：2026-09-21
- 状态：社区讨论中
- 作者邮箱：Peng Fan <peng.fan@oss.nxp.com>
- 概括：将 ARM SMMUv3 驱动中流标识到流的查找结构从红黑树改为可扩展数组，保持原有互斥锁保护，避免需要 RCU 宽限期的并发问题。该重构简化了重复流标识的处理逻辑，并移除相应红黑树节点和比较回调；当前行为不变，意在为后续共享流标识支持做准备。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260921-smmu-shared-sid-v2-1-4b656ce68178@nxp.com/

**▸ 组织：归属待核实（foxmail.com）**（1 patches）

**iommu/arm-smmu-v3: Skip unlinked duplicate stream nodes on removal**

- 日期：2026-09-21
- 状态：社区讨论中
- 作者邮箱：zhoumin <teczm@foxmail.com>
- 概括：针对固件流 ID 列表可能包含重复项的情况，修正 ARM SMMUv3 的移除与插入回滚路径：同一主设备的重复流节点插入时未被链入红黑树，但删除阶段仍会对每个节点执行擦除，未链接节点可能清空树根，使其他设备的流 ID 映射丢失。现在将跳过的重复节点标记为未链接，并在两个删除路径中跳过这些节点，同时保持流数组和数量不变以维持既有检查。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/tencent_4392079B5C29406B923C037A7E66DD338005@qq.com/

**▸ 组织：Kernel.org**（1 patches）

**[v2,2/5] iommu/arm-smmu-v3: Switch to use acpi_bus_get_primary_device()**

- 日期：2026-09-30
- 状态：社区讨论中
- 作者邮箱：Rafael J. Wysocki (Intel) <rafael@kernel.org>
- 概括：在 ARM SMMUv3 的 Tegra241 CMDQV 配套设备探测中，改用会为返回设备增加引用的 ACPI 主设备获取接口，替换即将移除且可能返回后设备被释放的旧接口，消除设备在引用释放窗口被移除所造成的潜在释放后使用风险。
- 来源：https://patchwork.kernel.org/project/alsa-devel/patch/3636226.QJadu78ljV@rafael.j.wysocki/

**▸ 组织：归属待核实（shutemov.name）**（1 patches）

**[SERIES] iommu/arm-smmu-v3: Make the queue depths tunable, and shrink them in a kdump kernel** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-09-25
- 状态：社区讨论中
- 作者邮箱：Kiryl Shutsemau <kirill@shutemov.name>
- 概括：为 ARM SMMUv3 命令队列深度提供可调上限，引入按条目数对数设置的模块参数，默认仍为硬件宣传的最大值，让内存紧张或仅驱动少量设备的系统可减少每个实例及 Tegra241 CMDQV 预分配的一致性内存。同时在 kdump 内核中将三类队列深度默认设为一页，捕获内核使用小预留内存时每个实例不再按最大深度分配数 MB，而这些队列只承载命令和故障记录，不影响转储吞吐量。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/arm-smmu-v3: Default queue depths to one page in a kdump kernel
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260925141532.1274962-3-kirill@shutemov.name/

**▸ 组织：Debian**（1 patches）

**[SERIES] iommu/arm-smmu-v3: SMMU hitting kdump mid-air** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-09-11
- 状态：社区讨论中
- 作者邮箱：Breno Leitao <leitao@debian.org>
- 概括：在 kdump 场景中，arm-smmu-v3 复位会安装空流表，但崩溃前由旧内核驱动的设备仍可能持续 DMA，例如 Amazon EC2 金属实例上无驱动的 ENA 网卡，导致流 ID 无效故障甚至固件复位实例、无法写出 vmcore。现在 kdump 时从旧流表基址继承 L1 描述符，继续指向旧二级表；并延后默认域连接，使继承条目在设备探测后仍存活到下一次 DMA。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/arm-smmu-v3: inherit the previous kernel's stream table in kdump
  - iommu/arm-smmu-v3: defer attach in kdump so inherited entries survive probe
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260911-smmu_fix_aws-v1-1-75870bf9655b@debian.org/

---

### ◆ 子系统：IOMMU Core（14 patches）

**▸ 组织：东南大学**（2 patches）

**iommu/exynos: quiesce SysMMU before requesting IRQ**

- 日期：2026-09-21
- 状态：社区讨论中
- 作者邮箱：Runyu Xiao <runyu.xiao@seu.edu.cn>
- 概括：调整 Exynos SysMMU 初始化顺序：先获取时钟、初始化软件状态并探测硬件版本，在时钟使能期间禁用并清除配置使模块保持静默，然后再注册中断处理函数。这样可避免注册后、时钟和版本尚未初始化时，挂起中断进入处理函数访问未初始化字段的理论竞争；处理函数在 SysMMU 非活动时也会忽略中断，防止虚假中断访问无效故障状态。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260921120848.96215-1-runyu.xiao@seu.edu.cn/

**iommu/exynos: Initialize lock before requesting IRQ**

- 日期：2026-09-01
- 状态：社区讨论中
- 作者邮箱：Runyu Xiao <runyu.xiao@seu.edu.cn>
- 概括：修复 Exynos 系统内存管理单元（SysMMU）驱动中的锁初始化顺序问题。中断处理程序在请求中断后即可运行，而自旋锁此前在较后的位置才初始化；如果注册后立即产生中断，可能使用未初始化的锁。现将锁初始化提前到中断注册之前，避免早期中断访问无效锁状态。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260901130527.3289245-1-runyu.xiao@seu.edu.cn/

**▸ 组织：Qualcomm**（2 patches）

**[SERIES] iommu: qcom: Fix the MSM GPU and display with DMA-address based mappings** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-10-30
- 状态：社区讨论中
- 作者邮箱：Dmitry Baryshkov <dmitry.baryshkov@oss.qualcomm.com>
- 概括：高通 MSM 平台 GPU 和显示使用基于 DMA 地址的映射时存在两个问题：旧高通输入输出内存管理单元的全域地址转换缓存失效只同步不真正失效，drm/msm 依赖它导致 GPU 因陈旧映射挂起；同时相关 GPU 和 MDP5 设备未使用直接映射默认域，被内核 DMA 映射到未使用地址，GPU 启动失败或 SoC 复位。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/arm-smmu-qcom: Use identity default domains for MDP5
  - iommu/qcom: Use identity default domains for the MSM GPU and display
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20261031-msm-smmu-identity-v1-1-a2a70580eebd@oss.qualcomm.com/

**[SERIES] iommu/qcom+msm: Use identity domain for display/GPU** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-10-29
- 状态：社区讨论中
- 作者邮箱：Rob Clark <robin.clark@oss.qualcomm.com>
- 概括：旧高通输入输出内存管理单元驱动原先为所有设备分配内核管理的默认域，导致 GPU 和显示设备被附加内核 DMA 映射；而 drm/msm 驱动自行管理页表，期望拿到物理地址。现在在这些驱动中按设备兼容标识匹配 GPU 和显示设备，将默认域设为直接映射，使 DRM 驱动得到的地址可直接使用，避免附加的 DMA 映射干扰。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/qcom: Use identity domain for GPU and display
  - iommu/msm: Use identity domain for GPU and display
- 来源：https://patchwork.kernel.org/project/linux-arm-msm/patch/20261029212344.346069-2-robin.clark@oss.qualcomm.com/

**▸ 组织：归属待核实（jannau.net）**（1 patches）

**[v3,2/2] iommu: apple-dart: Support specifying the DMA aperture in the DT**

- 日期：2026-09-02
- 状态：社区讨论中
- 作者邮箱：Janne Grunau <j@jannau.net>
- 概括：为 Apple DART 输入输出内存管理单元增加从设备树指定直接内存访问窗口的能力。部分直连设备只允许在地址空间的一部分进行 DMA，设备可通过其 IOMMU 引用参数给出 64 位窗口起止和长度；驱动据此限制地址域，并在窗口超出硬件输入地址大小时只映射低位。若窗口跨过或回绕输入地址边界则拒绝，从而为设备分配正确的 DMA 区间。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260902-iommu-apple-dart-aperture-v3-2-252ce55b7001@jannau.net/

**▸ 组织：Individual Contributor**（1 patches）

**[v1,1/2] iommu: export iommu_get_dma_domain()**

- 日期：2026-09-28
- 状态：社区讨论中
- 作者邮箱：Jianfeng Liu <liujianfeng1994@gmail.com>
- 概括：导出获取设备默认 DMA 域的接口，供模块化驱动使用。DRM 的 msm 驱动在调试选项开启时，导入的 dma-buf 附件散列表不携带页结构，需要借助该接口将 DMA 地址还原为物理地址，才能把缓冲区映射到自己的页表中。
- 来源：https://patchwork.kernel.org/project/dri-devel/patch/20260928053901.7270-2-liujianfeng1994@gmail.com/

**▸ 组织：Kernel.org**（1 patches）

**[slab/for-next,09/14] iommu: specify SLAB_MAY_ACCOUNT for slab-backed page table caches**

- 日期：2026-10-21
- 状态：社区讨论中
- 作者邮箱：Harry Yoo <harry@kernel.org>
- 概括：为 ARM v7s、s390 和 sun50i 平台的输入输出内存管理单元页表缓存补充允许内存控制组记账的标志，使 VFIO、IOMMUFD 和 vhost-vDPA 通过带记账标记的分配标志执行映射时，驱动分配的页表内存能够正确计入内存控制组。此前缺少该标志，带记账标记的分配将来可能被拒绝，现在可正常记账。
- 来源：https://patchwork.kernel.org/project/linux-mm/patch/20261021-memalloc-prof-dont-waste-slabobj-ext-metadata-v1-9-096800aa3330@kernel.org/

**▸ 组织：EPAM**（1 patches）

**[v13,09/14] iommu/ipmmu-vmsa: Implement suspend/resume callbacks**

- 日期：2026-10-27
- 状态：社区讨论中
- 作者邮箱：Mykola Kvach <mykola_kvach@epam.com>
- 概括：为 Xen 中的 R-Car IPMMU-VMSA 驱动增加系统挂起/恢复支持，挂起时保存根 IPMMU 的活动上下文和缓存 IPMMU 的微 TLB 配置，恢复时先写回根上下文再恢复缓存微 TLB，避免微 TLB 指向尚未恢复的上下文而暴露过期状态；该功能仅在 H3ULCB（R-Car Gen3）上测试。
- 来源：https://patchwork.kernel.org/project/xen-devel/patch/3f8f4ecf30d38d589c2d08f5b2676bda93f8d880.1793129971.git.mykola_kvach@epam.com/

**▸ 组织：归属待核实（chromium.org）**（1 patches）

**iommu/mediatek: Track first resume with a dedicated boolean flag**

- 日期：2026-10-28
- 状态：社区讨论中
- 作者邮箱：Chen-Yu Tsai <wenst@chromium.org>
- 概括：MediaTek IOMMU 原先用特定寄存器值是否为零判断首次运行时恢复，隐式依赖硬件复位默认状态，难以理解。现在增加专用布尔标志直接跟踪首次恢复是否完成：首次恢复只开启时钟并置位，后续恢复才回写之前保存的寄存器。这样状态判断更明确，不改变恢复行为。
- 来源：https://patchwork.kernel.org/project/linux-mediatek/patch/20261028041651.3201911-1-wenst@chromium.org/

**▸ 组织：归属待核实（reactivated.net）**（1 patches）

**[SERIES] Add support for Broadcom BCM2712 IOMMU driver (Raspberry Pi 5)** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-09-27
- 状态：社区讨论中
- 作者邮箱：Daniel Drake <dan@reactivated.net>
- 概括：新增 Broadcom BCM2712 输入输出内存管理单元驱动，用于 Raspberry Pi 5 上 VC6 显示流水线和多媒体设备，借助通用页表框架管理两级页表，并维护跨实例共享的二级转译后备缓存，在修改或取消映射时统一刷新。同时调整通用页表边界测试地址以适配 37 位输出地址格式。该驱动使显示和多媒体设备获得地址转换能力，便于内存管理和隔离。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/generic_pt: Add Broadcom BCM2712 page table format
  - iommu: Add Broadcom BCM2712 IOMMU driver
- 来源：https://patchwork.kernel.org/project/devicetree/patch/20260927-bcm2712-iommu-submit-v7-4-dfa2b975cbc9@reactivated.net/

**▸ 组织：Microsoft**（1 patches）

**[SERIES] Hyper-V: Add para-virtualized IOMMU support for Linux guests** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-09-30
- 状态：社区讨论中
- 作者邮箱：Yu Zhang <zhangyu1@linux.microsoft.com>
- 概括：为 Linux 客户机新增 Hyper-V 半虚拟化 IOMMU 驱动，通过 hypercall 完成能力发现、域管理和设备挂接，客户机在自身内存构建阶段 1 页表并交给 Hyper-V 与宿主阶段 2 嵌套，映射操作不再触发虚拟机退出。同时增加逻辑设备标识注册表把 PCI 直通设备映射到 hypercall 所需标识，提取 x86 架构 MSI 保留区域辅助函数，并支持页号粒度的细粒度 IOTLB 刷新，失败时回退全域刷新。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/hyperv: Add para-virtualized IOMMU support for Hyper-V guest
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/20260930141409.437904-4-zhangyu1@linux.microsoft.com/

**▸ 组织：Amazon**（1 patches）

**[SERIES] iommu: Reduce iommu_probe_device_lock contention** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-09-11
- 状态：社区讨论中
- 作者邮箱：Sakac, Pavol <sakacpav@amazon.de>
- 概括：并行设备探测（尤其是虚拟功能初始化）时，全局探测锁成为争用热点，因为sysfs成员链接发布和首设备默认域设置都在锁内完成。现在把sysfs链接发布拆分为独立步骤并移到全局锁外，默认域设置也借助组列表延迟到锁外，两项改由组互斥锁保护；失败路径保持回滚语义，从而缩短全局锁持有时间，降低探测路径上的串行等待。
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu: split sysfs link publication out of iommu_group_alloc_device()
  - iommu: create device sysfs links outside iommu_probe_device_lock
  - iommu: set up the default domain outside iommu_probe_device_lock
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/20260911125907.67105-1-sakacpav@amazon.de/

**▸ 组织：Alibaba**（1 patches）

**[SERIES] iommu: Reserve PCI host bridge MMIO windows for IOVA** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-09-21
- 状态：社区讨论中
- 作者邮箱：Guanghui Feng <guanghuifeng@linux.alibaba.com>
- 概括：此前 VFIO type1 和输入输出内存管理文件描述符框架的 IOVA 分配未将 PCI 主机桥 MMIO 窗口列为保留区域，用户态可能选择落入这些窗口的地址；当设备位于 PCIe 交换机后且访问控制服务上行转发未完全启用时，DMA 事务可能被误当作点对点流量路由到错误设备。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu: Reserve PCI host bridge MMIO windows in group reserved regions
  - iommufd: Reserve PCI host bridge MMIO windows in IOAS reserved regions
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260921103922.1113752-2-guanghuifeng@linux.alibaba.com/

**▸ 组织：Google**（1 patches）

**[SERIES] iommu: Introduce Page Table Observability Framework** （cover letter，2/5 个 patch 达到代码量阈值）

- 日期：2026-10-01
- 状态：社区讨论中
- 作者邮箱：Pranjal Shrivastava <praan@google.com>
- 概括：引入 IO 页表可观测性框架，在 IOMMU 域上按页统计页表内存，并让基于通用页表库的驱动自动获得归属统计；随后在 VFIO 和 iommufd 的文件描述符信息中新增 IO 页表页数字段，向用户空间报告每个容器或上下文所占的 IO 页表页数，若驱动未统计则省略字段，当前计数在取消映射后继续保留。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommupt: Enable per-domain IOPT attribution
  - iommufd: Expose IO page table usage via fdinfo
- 来源：https://patchwork.kernel.org/project/linux-kselftest/patch/20261001224531.765278-2-praan@google.com/

---

### ◆ 子系统：RISC-V IOMMU（10 patches）

**▸ 组织：归属待核实（sanechips.com.cn）**（2 patches）

**[SERIES] iommu/riscv: Add nested translation (vIOMMU) support** （cover letter，3/9 个 patch 达到代码量阈值）

- 日期：2026-10-29
- 状态：社区讨论中
- 作者邮箱：Gong Shuai <gong.shuai@sanechips.com.cn>
- 概括：为 RISC-V IOMMU 添加嵌套翻译和虚拟 IOMMU 支持，让虚拟机监控器通过用户态接口为设备配置两阶段地址转换。用户空间可分配 RISC-V 硬件页表和虚拟 IOMMU 对象，提交客户第一阶段设备上下文，由内核将其与宿主第二阶段父域组合写入设备目录；客户页表更新所需的缓存失效命令经虚拟 IOMMU 转交，内核校验后替换隔离标识，防止客户无效化其他虚拟机的缓存。同时修正设备上下文有效位取值并保留完整转换控制字段。
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu/riscv: Add nested domain allocation
  - iommu/riscv: Use DC.tc.V as the device context valid bit
  - iommu/riscv: Add vIOMMU cache invalidation
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20261029061131.584453-6-gong.shuai@sanechips.com.cn/

**[RFC,11/12] iommu/riscv: Accept unpublished interrupt files in IRQ forwarding**

- 日期：2026-10-15
- 状态：社区讨论中
- 作者邮箱：Gong Shuai <gong.shuai@sanechips.com.cn>
- 概括：在 RISC-V IOMMU 中断转发中放宽目标校验，因为首个设备 MSI 转发可能在所有 vCPU 中断文件发布前发起。遇到尚未发布的中断文件时跳过，不再拒绝整个虚拟机拓扑；解析到这些条目的 MSI 只会使对应 vCPU 报故障，而不会让整机中断旁路创建失败。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261015065232.604503-12-gong.shuai@sanechips.com.cn/

**▸ 组织：Alibaba**（2 patches）

**[SERIES] iommu/riscv: Add irqbypass support without MSI page table** （cover letter，3/4 个 patch 达到代码量阈值）

- 日期：2026-10-14
- 状态：社区讨论中
- 作者邮箱：yu fangyu <fangyu.yu@linux.alibaba.com>
- 概括：RISC-V IOMMU 在不具备 MSI 页表的实现上支持中断转发。通过第二阶段页表把客户中断控制器页面映射到主机中断控制器物理页，使设备 MSI 写入直接到达虚拟处理器的中断文件；当虚拟处理器迁移导致主机页移动时，新增的页表叶条目原子替换操作在验证旧地址后换入新地址，避免解除映射与再映射之间出现写入故障窗口。无 MSI 页表能力时，转发入口验证目标必须为客户中断控制器页，失败或禁用转发只丢弃每中断状态并回落主机投递。
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu/riscv: Support IRQ forwarding without MSI page tables
  - iommu/riscv: Extract IRQ forwarding payload validation
  - iommupt: Add replace_leaf to atomically swap a leaf OA
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20261014141124.48569-5-fangyu.yu@linux.alibaba.com/

**[SERIES] iommu/riscv: Fix command queue publishing races** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-09-01
- 状态：社区讨论中
- 作者邮箱：yu fangyu <fangyu.yu@linux.alibaba.com>
- 概括：修复 RISC-V IOMMU 命令队列发布竞态，引入原始自旋锁序列化发布，确保软件生产者索引在命令写入和硬件尾部更新后才推进；队列满时在锁外等待硬件消费，避免长时间阻塞其他 CPU；当命令未能进入队列时不再等待 IOFENCE 完成，防止误报执行超时。原来并发提交可能使状态不一致并导致误等，现在各 CPU 发布命令互不干扰，失败路径能立即返回。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/riscv: Serialize command queue publishing
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20260901133920.14550-2-fangyu.yu@linux.alibaba.com/

**▸ 组织：Qualcomm**（2 patches）

**[SERIES] iommu/riscv: Add irqbypass support** （cover letter，7/10 个 patch 达到代码量阈值）

- 日期：2026-09-28
- 状态：社区讨论中
- 作者邮箱：Andrew Jones <andrew.jones@oss.qualcomm.com>
- 概括：为 RISC-V IOMMU 引入中断旁路支持，使其在第二阶段域中分配 MSI 页表，把客户 IMSIC 或 MRIF 目标映射进来，从而将中断直接转发给虚拟机而不经过宿主中断路径；同时加入转发请求校验、按设备转发计数、RCU 保护当前域及 MSI 表发布与设备连接的锁序列化，阻止已转发中断时替换第二阶段域或并发更新产生悬空表。
- 达到阈值的 patches（7 个，显示前 5）：
  - iommu/riscv: Allocate MSI tables for second-stage domains
  - iommu/riscv: Prepare domain bonds for outer locking
  - iommu/riscv: Cache the programmed device context
  - iommu/riscv: Validate IRQ forwarding requests
  - iommu/riscv: Add IRQ domain for interrupt remapping
  - ... 及其他 2 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260928143113.49838-2-andrew.jones@oss.qualcomm.com/

**[SERIES] iommu/riscv: Enable MSI remapping, IOMMU_DMA and VFIO** （cover letter，7/7 个 patch 达到代码量阈值）

- 日期：2026-09-25
- 状态：社区讨论中
- 作者邮箱：Andrew Jones <andrew.jones@oss.qualcomm.com>
- 概括：为 RISC-V 输入输出内存管理单元补齐中断重映射、设备 DMA 地址映射和用户态设备直通。将用户态接口的软件 MSI 映射改为按需增长，支持有序地址列表映射到连续输入输出虚拟地址范围并原子发布；为每颗可能处理器的 IMSIC 页保留软件 MSI 窗口，亲和性变化时可直接选取目标，但该窗口仅避开已知冲突，不能保证与客户 MSI 地址始终分离。
- 达到阈值的 patches（7 个，显示前 5）：
  - iommufd: Split software MSI map lookup and allocation
  - iommufd: Prepare software MSI maps for address lists
  - iommufd: Install software MSI map ranges atomically
  - iommufd: Bound software MSI mappings to the reserved range
  - iommu/riscv: Reserve an MSI IOVA window for iommufd
  - ... 及其他 2 个 patch
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20260925151659.419512-4-andrew.jones@oss.qualcomm.com/

**▸ 组织：SiFive**（1 patches）

**[v16,2/2] iommu/riscv: create a auxiliary device for HPM**

- 日期：2026-10-06
- 状态：社区讨论中
- 作者邮箱：Zong Li <zong.li@sifive.com>
- 概括：当 RISC-V 输入输出内存管理单元支持硬件性能监视器时，驱动通过辅助总线创建一个性能监视辅助设备，供上层绑定性能监视驱动。创建失败仅警告并禁用该监视功能，不影响 IOMMU 的地址翻译等基本工作；移除设备时也会销毁该辅助设备，避免遗留资源。
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20261006090327.309550-3-zong.li@sifive.com/

**▸ 组织：The Good Penguin**（1 patches）

**iommu/riscv: Use named initializers for acpi_device_id**

- 日期：2026-10-14
- 状态：社区讨论中
- 作者邮箱：Pawel Zalewski <pzalewski@thegoodpenguin.co.uk>
- 概括：将 RISC-V IOMMU 的 ACPI 设备标识表改为命名初始化方式，去掉冗余的置零字段，并统一列表终止项的格式。该修改仅提升代码可读性并与内核其他初始化风格保持一致，不改变实际行为。
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20261014-acpi-iommu-v1-1-1744523fa658@thegoodpenguin.co.uk/

**▸ 组织：Linux Community**（1 patches）

**[SERIES] iommu/riscv: Enable MSI remapping and IOMMU_DMA** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-10-22
- 状态：社区讨论中
- 作者邮箱：Andrew Jones <andrew.jones@linux.dev>
- 概括：为 RISC-V 的 IMSIC 中断控制器建立按逻辑处理器编号排序的 MSI 物理地址列表，并把所有可能目标页面映射到一段连续的输入输出虚拟地址范围；中断亲和性变化时可在原子上下文中按处理器位置直接选定目标，无需逐一查询。同时在 64 位 RISC-V 上启用设备 DMA 地址映射支持，使输入输出内存管理单元能够处理 MSI 重映射。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/dma: Prepare MSI physical address lists
  - iommu/dma: Enable IOMMU_DMA for 64-bit RISC-V
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20261022154603.1374754-2-andrew.jones@linux.dev/

**▸ 组织：Individual Contributor**（1 patches）

**[SERIES] iommu/riscv: Keep page table pages when IOTLB invalidation fails** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-10-20
- 状态：社区讨论中
- 作者邮箱：Yuho Choi <oss.patchbox@gmail.com>
- 概括：RISC-V 输入输出内存管理单元原先在发送缓存失效命令后立即释放页表页，未检查命令是否入队或完成确认，设备可能仍缓存旧页表项，这些页被复用后内容会被当作页表遍历；同时命令队列停在错误项时被误报为执行完成。现在命令发送、等待和失效都返回错误，失效未确认时保留页表页并一次性警告，队列未到达目标项时返回 I/O 错误，避免继续释放仍被引用的页表页。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/riscv: Do not report a stalled command queue as completed
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20261020053435.1179054-5-oss.patchbox@gmail.com/

---

### ◆ 子系统：IOMMUFD（10 patches）

**▸ 组织：Individual Contributor**（5 patches）

**[SERIES] guest_memfd: Export guest_memfd files to iommufd** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-10-27
- 状态：社区讨论中
- 作者邮箱：Fred Griffoul <griffoul@gmail.com>
- 概括：为让 iommufd 能映射虚拟机客户机内存文件，先把原本仅用于 DMA-BUF 的域跟踪信息迁移到通用页结构，使可撤销页类型都能记录映射的设备和 I/O 地址空间；随后接受客户机内存文件，经导出接口不固定页，在页被撤销时按更新回调解除映射并重新映射当前共享内存，只读帧映射为不可写，只能整页对齐映射。这样设备映射可跟随客户机共享内存的授予和回收，无需固定客户机内存页。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommufd: Map guest_memfd files
  - iommufd: Track the domains of revocable pages in struct iopt_pages
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261027154649.91571-10-griffoul@gmail.com/

**[SERIES] iommufd: harden DMA-BUF PAL setup and release** （cover letter，4/6 个 patch 达到代码量阈值）

- 日期：2026-10-20
- 状态：社区讨论中
- 作者邮箱：Karl Mehltretter <kmehltretter@gmail.com>
- 概括：iommufd 在处理 DMA-BUF 物理地址列表映射的建立与释放时存在时序缺陷：固定失败会被误报成功，映射在解锁后发布，释放后指针未清，互斥锁销毁过早，解除固定也未持有保留锁，这些可能导致并发失效回调空引用或重复释放。现在保留固定错误，在保留锁内发布和清理映射并清空指针，推迟互斥锁销毁到附件移除之后，锁内解除固定，同时补充自测验证失败清理。
- 达到阈值的 patches（4 个，显示前 5）：
  - iommufd: Publish successful PAL mappings under resv
  - iommufd: Keep the pages mutex alive until DMA-buf detach
  - iommufd: Unpin the DMA-buf while holding resv
  - iommufd/selftest: Check DMA-buf pin and map failure cleanup
- 来源：https://patchwork.kernel.org/project/linux-kselftest/patch/9a3912ce01cfd1205daeb13b57de47aa8f27f076.1792477872.git.kmehltretter@gmail.com/

**[SERIES] mm: Memory providers for guest_memfd and iommufd** （cover letter，5/5 个 patch 达到代码量阈值）

- 日期：2026-10-14
- 状态：社区讨论中
- 作者邮箱：Fred Griffoul <griffoul@gmail.com>
- 概括：为客体内存文件和 IOMMU 用户态接口引入统一内存提供者机制，使驱动私有的、可能没有内核页结构的物理内存能被虚拟机或 IOMMU 映射。提供者通过文件向消费者提供页帧和属性，可撤销区域并强制消费者先移除映射；客体内存文件将原生实现抽象为操作表并支持只读页报告，增加资源描述符备份；IOMMU 侧接受提供者文件后不固定页，按需填充域，撤销时统一解除映射并换入新页，支持大页以减少页表开销。
- 达到阈值的 patches（5 个，显示前 5）：
  - iommufd: Track the domains of pages that are not pinned
  - iommufd: Map memory provider files
  - iommufd/selftest: Add mock-domain IOVA queries
  - iommufd/selftest: Add a mock memory provider
  - iommufd: Use large IOMMU pages for provider mappings
- 来源：https://patchwork.kernel.org/project/linux-kselftest/patch/20261014093733.90312-6-griffoul@gmail.com/

**[v2,2/2] iommufd/selftest: Check dmabuf MMIO mappings filled from another domain**

- 日期：2026-10-08
- 状态：社区讨论中
- 作者邮箱：Andrea Parri <parri.andrea@gmail.com>
- 概括：在输入输出内存管理文件描述符框架的自测中，增加对直接内存访问缓冲区输入输出内存映射属性的跨域保持检查。模拟页表不区分内存类型，因此包装映射与反映射操作记录带该属性建立的页，并新增范围检查操作。测试覆盖已映射的缓冲区之后在同一地址空间新增第二个域以及复制到另一地址空间的域，确保这些后加入域仍获得相同的输入输出内存映射属性；未修复前三个模拟域变体均失败，修复后全部通过。
- 来源：https://patchwork.kernel.org/project/linux-kselftest/patch/20261008125206.11990-3-parri.andrea@gmail.com/

**[SERIES] iommufd: Keep IOMMU_HWPT_GET_DIRTY_BITMAP within the user bitmap** （cover letter，2/4 个 patch 达到代码量阈值）

- 日期：2026-09-25
- 状态：社区讨论中
- 作者邮箱：Andrea Parri <parri.andrea@gmail.com>
- 概括：修复脏位图查询可能越过调用方提供的位图写入的问题：当查询范围结束在脏的大页条目内部时，内核会把整个条目写入钉住页末尾，现在先把记录范围裁剪到位图边界，防止破坏用户内存；同时拒绝长度为零的脏位图请求，避免长度减一溢出后扫描整个地址空间，并添加越界和零长度自测覆盖。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommufd/iova_bitmap: Clip recorded ranges to the bitmap
  - iommufd: Reject a zero-length dirty bitmap request
- 来源：https://patchwork.kernel.org/project/linux-kselftest/patch/20260925161142.189813-2-parri.andrea@gmail.com/

**▸ 组织：Kernel.org**（3 patches）

**[RFC,v2,03/13] iommufd: Support MMIO provider attachment to vDEVICEs**

- 日期：2026-10-17
- 状态：社区讨论中
- 作者邮箱：Aneesh Kumar K.V <aneesh.kumar@kernel.org>
- 概括：为虚拟设备新增 MMIO 提供方附加机制。后端先验证其与虚拟机的关联，验证通过后设备 MMIO 提供方可附加到现有虚拟设备；附加后保持虚拟设备和 IOMMUFD 上下文存活，直到提供方分离。每个虚拟设备增加互斥锁，串行化提供方附加、分离，并供提供方和后端在内存转换与设备状态变更时共用，适用于虚拟 IOMMU 中需要提供私有 MMIO 的场景。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261017073149.1303738-4-aneesh.kumar@kernel.org/

**[SERIES] iommufd: vIOMMUs and TSM guest requests for confidential guests** （cover letter，6/6 个 patch 达到代码量阈值）

- 日期：2026-10-08
- 状态：社区讨论中
- 作者邮箱：Aneesh Kumar K.V <aneesh.kumar@kernel.org>
- 概括：为保密虚拟机场景，在 iommufd 框架中引入虚拟 IOMMU 和可信安全模块（TSM）客户机请求通道。将 VFIO 设备与对应 KVM 文件关联，使虚拟设备能把客户机发出的 TSM 命令转发给管理该设备的安全模块并返回响应；同时允许 PCI 安全模块后端提供虚拟 IOMMU 操作，并在断开时等待依赖虚拟设备释放后完成。KVM 引用改为基于文件计数，简化生命周期管理。
- 达到阈值的 patches（6 个，显示前 5）：
  - iommufd/device: Associate KVM file pointer with iommufd_device
  - iommufd/viommu: Keep a reference to the KVM file
  - iommufd: Add the vdevice TSM request ioctl
  - iommufd/viommu: Select vIOMMU operations before allocation
  - iommufd/viommu: Allow PCI TSM backends to provide vIOMMU operations
  - ... 及其他 1 个 patch
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/20261008055955.4014342-8-aneesh.kumar@kernel.org/

**[SERIES] iommufd: Infrastructure for vIOMMU creation for confidential guests and guest TSM requests** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-09-17
- 状态：社区讨论中
- 作者邮箱：Aneesh Kumar K.V <aneesh.kumar@kernel.org>
- 概括：为机密访客在 iommufd 中创建虚拟 IOMMU 和转发客户 TSM 请求提供基础设施。将 VFIO 对 KVM 的裸指针改为文件引用，使 VM 生命周期不依赖 KVM 内部引用；让 iommufd 设备关联 KVM 文件，增加 vIOMMU 父设备校验和硬件参数查询接口，并引入外部 vIOMMU provider 注册机制。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommufd: Add vIOMMU provider support
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260917140159.1163281-6-aneesh.kumar@kernel.org/

**▸ 组织：Alibaba**（2 patches）

**[SERIES] iommufd: Recommended reservations query and opt-in IOAS reservation** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-10-28
- 状态：社区讨论中
- 作者邮箱：Guanghui Feng <guanghuifeng@linux.alibaba.com>
- 概括：为 iommufd 新增按设备查询推荐保留 I/O 虚拟地址范围的接口，对 PCI 设备返回其所在宿主桥的 MMIO 窗口，提示用户空间在这些范围内发起 DMA 可能被 PCIe 交换机当成点对点流量而绕过 IOMMU 翻译。用户空间可自行避开，或通过新增的 I/O 地址空间范围保留接口将这些范围设为保留，之后内核拒绝映射到保留范围。两个步骤均为可选，未使用的用户空间行为不变。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommufd: Add IOMMU_GET_RECOMMENDED_RESERVATIONS ioctl
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261028090453.2392991-2-guanghuifeng@linux.alibaba.com/

**[v4,2/2] iommufd: Add IOMMU_GET_PCI_MMIO_WINDOWS ioctl**

- 日期：2026-10-25
- 状态：社区讨论中
- 作者邮箱：Guanghui Feng <guanghuifeng@linux.alibaba.com>
- 概括：在 iommufd 中新增按设备查询的 ioctl，向用户态报告该设备所在 PCI 主机桥的 MMIO 窗口地址范围。用户态如虚拟机监视器可据此了解哪些地址可能被 PCIe 交换机误判为对端 DMA 流量，从而自愿将输入输出虚拟地址分配避开这些区间；内核只报告范围，不强制预留或保护。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261025133000.205508-3-guanghuifeng@linux.alibaba.com/

---

### ◆ 子系统：AMD IOMMU（4 patches）

**▸ 组织：AMD**（2 patches）

**[SERIES] Add support for AMD IOMMU GAPPI** （cover letter，4/5 个 patch 达到代码量阈值）

- 日期：2026-10-22
- 状态：社区讨论中
- 作者邮箱：Sairaj Kodilkar <sarunkod@amd.com>
- 概括：AMD IOMMU 新增来宾 APIC 物理处理器中断机制，用于虚拟中断重映射中非运行虚拟处理器的唤醒。当设备中断目标为未运行的虚拟处理器时，IOMMU 在照常更新来宾虚拟 APIC 后备页的同时，向重映射表项指定的主机 CPU 直接发送物理核间中断，并用表项中的标签字段作为向量。
- 达到阈值的 patches（4 个，显示前 5）：
  - iommu/amd: KVM: SVM: Rename cpu to apicid in IOMMU interface
  - iommu/amd: KVM: SVM: Rename ga_log_intr to wakeup_intr in IOMMU interface
  - iommu/amd: Program guest-mode IRTEs for GAPPI wakeup when IRTE[IsRun] = 0
  - iommu/amd: Provide kernel command line option to enable GAPPI
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261022140425.27465-2-sarunkod@amd.com/

**[SERIES] iommu/amd: Implement live update state preservation** （cover letter，5/6 个 patch 达到代码量阈值）

- 日期：2026-10-05
- 状态：社区讨论中
- 作者邮箱：Ankit Soni <Ankit.Soni@amd.com>
- 概括：为 AMD IOMMU 在 kexec 活更新场景保存并恢复设备状态，使幸存设备跨内核继续安全 DMA。修正仅在崩溃转储内核延迟设备附加，避免活更新启动时未保留设备的块表项不被正确替换而无法 DMA；提前解析交棒树，固定 PCI 段设备表并记录每设备的域标识、页表模式和客户页表树。关机时清除未保留设备表项并停止命令、事件和页请求等引擎，超时则主动停机；启动时采用原有设备表和域标识，重新附加保留设备并校验状态一致，其余附加请求被拒绝。
- 达到阈值的 patches（5 个，显示前 5）：
  - iommu/amd: defer device attach only on a kdump boot
  - iommu/amd: preserve IOMMU and device state for live update
  - iommu/amd: restore preserved state on a live-update boot
  - iommu/amd: clear unpreserved DTEs and quiesce logs at live-update shutdown
  - iommu/amd: reattach preserved devices to their restored domains
- 来源：https://patchwork.kernel.org/project/kexec/patch/20261005064018.1558-2-Ankit.Soni@amd.com/

**▸ 组织：Google**（1 patches）

**[SERIES] iommu/amd: Refactors for ATS robustness** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-09-10
- 状态：社区讨论中
- 作者邮箱：Pranjal Shrivastava <praan@google.com>
- 概括：AMD IOMMU 驱动原先在设备探测失败时会清除设备表条目和反向查找表项，这在 kdump 启动时可能打断仍在进行的 DMA、破坏中断重映射，并存在缓存不一致风险；同时 ATS 配置失败被静默容忍。现在重构设备探测和 PCI 能力初始化，移除失败时的清除逻辑，让 ATS 准备失败直接使探测失败，并要求调用者先确认设备支持 ATS。结果是 kdump 期间保留既有 DMA 翻译，ATS 配置错误能显式暴露。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/amd: Refactor device probe and capability initialization
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/20260910142655.3281464-2-praan@google.com/

**▸ 组织：Oracle**（1 patches）

**[SERIES] amd_iommu: Bugfix and Cleanup for IO Page Fault** （cover letter，5/5 个 patch 达到代码量阈值）

- 日期：2026-10-30
- 状态：社区讨论中
- 作者邮箱：Alejandro Jimenez <alejandro.j.jimenez@oracle.com>
- 概括：修复 QEMU AMD IOMMU 模拟器的页错误处理和 MMIO 行为：页错误报告改为使用包含总线号的完整设备号，避免桥后设备错误记到错误的请求者；去掉重复的 MSI 能力；扩展特性寄存器改为只读；状态寄存器不再接受未支持的全局地址日志位写入，防止客户机旧内核清除事件中断时意外锁存全局地址日志溢出并反复重启。
- 达到阈值的 patches（5 个，显示前 5）：
  - amd_iommu: Make extended feature register read-only
  - amd_iommu: Do not create duplicate MSI capability
  - amd_iommu: Do not latch unsupported GA log status bits
  - amd_iommu: Use full BDF when reporting page faults
  - amd_iommu: Define MMIO register masks
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20261030003817.3521476-5-alejandro.j.jimenez@oracle.com/

---

### ◆ 子系统：ARM SMMU (v1/v2)（3 patches）

**▸ 组织：Qualcomm**（1 patches）

**iommu: arm-smmu-qcom: Skip fault-info reads when suspended**

- 日期：2026-09-11
- 状态：社区讨论中
- 作者邮箱：Bibek Kumar Patro <bibek.patro@oss.qualcomm.com>
- 概括：高通Adreno GPU的SMMU故障信息收集函数在无运行时电源引用下读取寄存器。故障产生后GPU可能在处理线程到达前放弃电源投票，使SMMU进入挂起，此时读寄存器可能引发片上网络错误和异步系统错误。现在先尝试获取运行时电源引用，若设备已不活跃则跳过寄存器读取并记录警告，避免挂起期间访问。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260912-priv_call_runtime_handlers-v1-1-fc0c3a17523f@oss.qualcomm.com/

**▸ 组织：归属待核实（brar.si）**（1 patches）

**[v2,2/2] iommu/arm-smmu-qcom: Skip PRR setup on SM7250 GPU SMMU**

- 日期：2026-10-23
- 状态：社区讨论中
- 作者邮箱：Ishu Brar <patches@brar.si>
- 概括：SM7250 平台的 GPU SMMU 与 SM8250 一样，固件在写入 Adreno SMMU 的 PRR 寄存器时会复位设备，首个进程级 GPU 页表创建就会触发。因此不安装 PRR 回调，避免创建 GPU 进程页表时设备复位，已在 OnePlus Nord 上验证 Vulkan 场景。
- 来源：https://patchwork.kernel.org/project/linux-arm-msm/patch/20261023-smmu-sm7250-v2-2-8bb881ce19f5@brar.si/

**▸ 组织：Individual Contributor**（1 patches）

**[SERIES] Enable LPAC on a7xx series GPUs** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-10-29
- 状态：社区讨论中
- 作者邮箱：Anna Maniscalco <anna.maniscalco2000@gmail.com>
- 概括：高通 Adreno 7 系列 GPU 的低优先级异步计算原先与主 GPU 共用域，无法独立更新页表。现在 ARM SMMU 驱动为其分配独立的上下文库和分离地址空间，固定流标识与上下文库的对应；固件配置低优先级异步计算孔径以允许命令处理器更新 SMMU 寄存器；DRM 驱动从设备树识别独立节点，初始化专用命令环和提交队列并提供用户空间提交接口，设备树把第二个流标识移入该节点。通过模块参数控制，当前默认对 Adreno 750 启用。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu: arm-smmu-qcom: Configure lpac device with split address space
- 来源：https://patchwork.kernel.org/project/linux-arm-msm/patch/20261029-descriptive-name-lpac-upstream-v2-1-a21a5c850961@gmail.com/

---

### ◆ 子系统：IOMMU DMA-API（3 patches）

**▸ 组织：NVIDIA**（2 patches）

**[SERIES] Make the 32-bit ARM DMA API work with normal IOMMU DMA default domains (+ Tegra PoC)** （cover letter，3/5 个 patch 达到代码量阈值）

- 日期：2026-10-26
- 状态：社区讨论中
- 作者邮箱：Mikko Perttunen <mperttunen@nvidia.com>
- 概括：该系列使 32 位 ARM DMA API 能使用 IOMMU 核心默认 DMA 域：新增卸载操作、ARM DMA cookie 类型，拆分映射初始化，实现核心持有域时的设置与卸载路径，并在多数 32 位 ARM 平台启用默认 DMA 域，少数平台暂保持身份域。Tegra SMMU 同时把显示客户端转换延迟到驱动接管后开启，并为 Tegra DRM、Host1x 软件组启用默认 DMA 域，修复特定探测顺序下同组多设备导致的探测失败。
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu/tegra-smmu: Defer display client translation to driver handover
  - iommu/tegra-smmu: Use a DMA API default domain per swgroup
  - iommu: Enable DMA default domains on (most) 32-bit ARM platforms
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20261026-b4-arm32-iommu-dma-cookie-v3-1-3901d74b1ff2@nvidia.com/

**[v2,07/11] iommu: Let 32-bit ARM drivers opt into a DMA API default domain**

- 日期：2026-10-16
- 状态：社区讨论中
- 作者邮箱：Mikko Perttunen <mperttunen@nvidia.com>
- 概括：32位ARM的IOMMU驱动原先无法请求DMA域作为默认域，统一被强制设为直通域，因为ARM DMA API会自行安装非托管域。现在把ARM DMA API状态视为普通域标记，移除强制覆盖，允许驱动显式选择DMA域，但仅作为显式选择而不作为默认回退，现有32位ARM驱动行为均保持不变。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20261016-b4-arm32-iommu-dma-cookie-v2-7-b06842a01938@nvidia.com/

**▸ 组织：Google**（1 patches）

**[SERIES] DMA_PMD: PMD_SIZE-backed IO buffer pools** （cover letter，12/12 个 patch 达到代码量阈值）

- 日期：2026-10-03
- 状态：社区讨论中
- 作者邮箱：Luigi Rizzo <lrizzo@google.com>
- 概括：为减少 IOMMU 的 IOTLB 压力和映射开销，新增基于物理连续 2MB 大页的 IO 缓冲区池，供设备驱动分配流式或长期缓冲，IOMMU 页表使用大页叶子映射，减少缺页和刷新；池化分配与回收摊薄映射成本，并带后台清理、全局上限和收缩器控制空闲内存。
- 达到阈值的 patches（12 个，显示前 5）：
  - iommu/dma: introduce CONFIG_DMA_PMD and metadata table
  - iommu/dma: add DMA_PMD pool lifecycle and page recycle hook
  - iommu/dma: Global cap and shrinker for DMA_PMD pool memory
  - iommu/dma: add DMA_PMD pool block allocation
  - iommu/dma: reserve a per-domain IOVA window for DMA_PMD pages
  - ... 及其他 7 个 patch
- 来源：https://patchwork.kernel.org/project/linux-mm/patch/20261003212241.3432303-2-lrizzo@google.com/

---

### ◆ 子系统：Intel VT-d（3 patches）

**▸ 组织：Intel**（2 patches）

**[v2,3/4] iommu/vt-d: Add an API for tdx-host when enabling trusted DMA**

- 日期：2026-10-15
- 状态：社区讨论中
- 作者邮箱：Baolu Lu <baolu.lu@linux.intel.com>
- 概括：为 TDX host 增加接口，将支持 TDX Connect 可信 DMA 扩展的 Intel IOMMU 切换到安全 TDX 模式。切换前逐单元验证地址转换、排队失效和可扩展模式已启用，并限制主机只能使用域标识空间下半部分；随后调用 TDX 模块完成设置，失败恢复域标识范围。进入 TDX 模式的单元不可热移除。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261015010705.1973284-4-baolu.lu@linux.intel.com/

**[SERIES] iommu/vt-d: Introduce trusted DMA initialization support** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-09-15
- 状态：社区讨论中
- 作者邮箱：Baolu Lu <baolu.lu@linux.intel.com>
- 概括：为 Intel VT-d 增加 TDX Connect 可信 DMA 初始化支持：在支持 TDXCS 扩展且启用 DMA 翻译的 IOMMU 上，通过 SEAMCALL 切换到安全 TDX 模式，分配元数据页和失效队列，并由 TDX 模块返回 IOMMU 标识；成功后把域 ID 高位保留给 TDX 模块，主机只使用低位，退出时恢复完整域 ID 范围。
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu/vt-d: Add interfaces for trusted DMA initialization
  - iommu/vt-d: Add helpers to set up and tear down TDX extensions
  - iommu/vt-d: Reserve MSB of domain ID space for TDX module
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260915074235.1219183-4-baolu.lu@linux.intel.com/

**▸ 组织：Google**（1 patches）

**[SERIES] iommu: Add live update state preservation** （cover letter，17/17 个 patch 达到代码量阈值）

- 日期：2026-10-25
- 状态：社区讨论中
- 作者邮箱：Samiullah Khawaja <skhawaja@google.com>
- 概括：为 kexec 活更新保存并恢复 IOMMU 状态：通过 KHO 分配保存内存，保存页表、域、设备及 IOMMU 硬件状态，VT-d 保存根表、上下文表和 PASID 表，并在新内核启动时恢复域并重新连接到设备。iommufd 提供 ioctl 标记硬件页表为需保存，保存后对应 IOAS 不可变，禁止映射修改；VFIO PCI 同时保存 cdev 及其 iommufd 绑定。
- 达到阈值的 patches（17 个，显示前 5）：
  - iommu: Implement IOMMU Live update FLB callbacks
  - iommu/pages: Add APIs to preserve/unpreserve/restore iommu pages
  - iommupt: Implement preserve/unpreserve/restore callbacks
  - iommu/vt-d: Clear unpreserved context entries during shutdown
  - iommu: Add APIs to get iommu and device preserved state
  - ... 及其他 12 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261025021930.674647-2-skhawaja@google.com/

---

### ◆ 子系统：IOMMU SVA/SVM（2 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[RFC,1/2] iommu: Add iommu_map_sgtable_dma()**

- 日期：2026-10-09
- 状态：社区讨论中
- 作者邮箱：Karl Mehltretter <kmehltretter@gmail.com>
- 概括：为私有 IOMMU 域导入 DMA 缓冲区场景新增接口，处理 DMA 附件只提供总线地址而无 CPU 页的问题。该接口通过设备默认 DMA 域反向翻译得到物理页并映射到目标域，失败时回滚已建映射，仅支持非回弹的 IOMMU-DMA 映射，其他后端或总线地址返回不支持。这样 Rockchip 等私有域导入方可在严格调试下完成映射。
- 来源：https://patchwork.kernel.org/project/linux-rockchip/patch/20261009002114.67851-2-kmehltretter@gmail.com/

**▸ 组织：归属待核实（utexas.edu）**（1 patches）

**iommu/sva: Charge IOPF allocations to the faulting mm's memcg**

- 日期：2026-10-12
- 状态：社区讨论中
- 作者邮箱：Peizhe Liu <peizheliu@utexas.edu>
- 概括：设备引发SVA缺页时，处理线程未设置活动内存控制组，导致文件页缓存分配落入根控制组，逃过任务的内存上限。现在处理故障前切换到故障进程的内存控制组，完成缺页后恢复之前的活动控制组，使设备引发的页缓存正确计入所属控制组。
- 来源：https://patchwork.kernel.org/project/linux-mm/patch/20261012200823.699316-1-peizheliu@utexas.edu/

---

### ◆ 子系统：IOMMU Page Table（1 patches）

**▸ 组织：Qualcomm**（1 patches）

**[v5] iommu/io-pgtable-arm: Add support for contiguous hint bit**

- 日期：2026-09-21
- 状态：社区讨论中
- 作者邮箱：Vijayanand Jitta <vijayanand.jitta@oss.qualcomm.com>
- 概括：为 ARM LPAE 页表加入连续提示位支持：当连续页表项映射自然对齐的连续内存块时，在整组描述符上设置该位，使硬件可合并翻译、扩大 TLB 覆盖；同时向调用方通告支持的连续组大小。部分取消映射会在修改任何描述符前被拒绝，避免留下不完整组，并提供禁用开关供存在相关硬件缺陷的 SMMU 驱动关闭该特性。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260921-iommu_contig_hint-v5-1-e7fbd1c3774d@oss.qualcomm.com/

---

### ◆ 子系统：IOMMUPT（1 patches）

**▸ 组织：Google**（1 patches）

**[SERIES] iommupt: Introduce IO page table shrinker** （cover letter，2/5 个 patch 达到代码量阈值）

- 日期：2026-10-01
- 状态：社区讨论中
- 作者邮箱：Pranjal Shrivastava <praan@google.com>
- 概括：为 IOMMU 通用页表引入按需回收空闲中间目录的收缩机制。叶子条目采用引用计数，目录完全清空后进入每域回收列表；内存压力下收缩器无锁摘取空目录并从页表树中断开，经全局宽限期保护并发映射后释放，并刷新 IOMMU 缓存，避免设备仍引用已释放页表。映射路径若发现目录被回收则返回重试，非 DMA 域才允许入队，因为 DMA 取消映射可能在中断上下文运行。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommupt: Introduce lockless page table shrinker
  - iommupt: Return real page count to the shrinker core
- 来源：https://patchwork.kernel.org/project/linux-mm/patch/20261001230219.818128-2-praan@google.com/

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
- **组织归类**：按完整邮箱域名及其子域名识别企业、高校和社区；公共邮箱归为 Individual Contributor，未知域名单独标为归属待核实，不推断雇主

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

*报告由 Linux Patches Tracker 自动生成 | 2026-11-11 15:44:26*
