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
| 社区讨论中 | 74 | 93.7% |
| 已合入 | 0 | 0.0% |
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
| IOMMU Core | 14 | 17.7% |
| IOMMUFD | 13 | 16.5% |
| RISC-V IOMMU | 12 | 15.2% |
| Intel VT-d | 6 | 7.6% |
| AMD IOMMU | 5 | 6.3% |
| IOMMU DMA-API | 4 | 5.1% |
| ARM SMMU (v1/v2) | 3 | 3.8% |
| IOMMU SVA/SVM | 2 | 2.5% |
| IOMMU Page Table | 1 | 1.3% |
| IOMMUPT | 1 | 1.3% |

## 重点 Patch Top20 清单

### 已合入

暂无。

### 社区讨论

| 厂商 | 简介 |
|------|------|
| Google | [PATCH v9 00/25] KVM: arm64: SMMUv3 driver for pKVM (trap and emulate) ------在受保护 KVM 下新增 EL2 端 ARM SMMUv3 驱动和主机端配套驱动：把 SMMU MMIO 捐赠给 hypervisor，对主机访问进行陷阱并模拟寄存器读写，使 hypervisor 拥有硬件并建立影子页表，从而提供 DMA 隔离。同时将队列、流表项、IDR 解析、无命中更新和范围失效等逻辑移入主机与 hypervisor 共享代码，并实现命令队列和流表影子、TLB 失效以及主机阶段二页表的同步更新。 |
| Oracle | [PATCH v3 00/5] amd_iommu: Bugfix and Cleanup for IO Page Fault ------修复 QEMU 中 AMD IOMMU 仿真的 IO 页故障报告和寄存器语义：地址空间改用完整总线/设备/功能号，使根端口之后设备产生的页故障能归到正确请求者，不再误报为 00:00.0；初始化时避免重复创建 MSI 能力；将扩展特性寄存器设为只读，让功能位完全由 QEMU 控制；拒绝客户机对未产生的 GA 日志状态位进行写清除时锁存虚假溢出，从而避免客户机反复重启 GA 日志。 |
| NVIDIA | [PATCH v11 00/11] iommu/arm-smmu-v3: Adopt the crashed kernel's stream table for kdump ------为 kdump 场景改造 ARM SMMUv3 驱动：提前初始化标识分配器，将地址空间标识改为每实例独立，并在 kdump 内核中禁用事件队列和页请求队列；新增采用选项保留崩溃内核的流表，扫描并预留其正在使用的地址空间标识，防止新域复用旧标识导致直接内存访问命中陈旧缓存。 |
| NVIDIA | [PATCH v5 00/15] iommu/arm-smmu-v3: Add PRI support ------为 ARM SMMUv3 增加 PCI PRI 页请求处理能力：支持 PRI 的 PCI 设备缺页时通过页请求队列进入 IOPF 层，驱动再向 SMMU 提交页响应命令；同时把 IOPF 队列分配与 SVA 解耦，硬件具备暂停特性即可启用。补充设备脱离域时的清理顺序，先排空事件队列、同步中断并冲刷在途故障工作，再释放旧域，避免在途事件引用已释放内存；还修复关闭时未先禁用实现层回调，可能对已启用命令队列发起同步的问题。 |
| Google | [PATCH v11 00/16] iommu/arm-smmu-v3: Implement Runtime/System Sleep ops ------为 ARM SMMUv3 实现运行时电源管理和系统休眠操作：挂起前用停止标志禁止新命令提交，排空命令队列及 Tegra241 虚拟命令队列，并处理残留的全局错误；恢复时恢复虚拟命令队列的生产/消费索引、缓存 MSI 消息和中断配置，再重新启用硬件中断。这样 SMMU 在系统休眠或运行时挂起后可以安全断电并恢复工作，避免索引清零导致命令不消费或 MSI 配置丢失引起中断失效。 |
| Google | [PATCH v1 00/22] DMA_PMD: PMD_SIZE-backed IO buffer pools ------为直接内存访问缓冲新增基于 2MB 物理连续大页的分配池，使输入输出内存管理单元能使用大页映射，降低输入输出旁路转换缓冲压力及映射、解映射和刷新开销。池会动态分配回收大页，并用全局上限和收缩器限制空闲内存；域销毁时清理存活映射，确保内存仅在输入输出内存管理单元映射移除并刷新后才归还伙伴分配器。 |
| NVIDIA | [PATCH v8 00/9] Organize the SMMUv3 invalidation flow so iommupt can use it ------在 ARM SMMUv3 使用共享进程地址空间时，连续页表项可能因硬件缺陷在范围失效被从中间拆分时漏失效，恶意用户可借助内存映射操作触发；原有范围失效也可能发出多达 512 条单条命令或多次范围命令，延迟较高。补丁将 SVA 失效改为一次覆盖整个连续项的范围命令，并预计算失效命令、整理参数，将普通范围失效控制在最多两次且可重叠覆盖，以降低延迟，同时为后续页表接管的失效流程做准备。 |
| Red Hat | [PATCH v2 00/75] virtio: fix exit(1) on DMA mapping failure during migration restore ------对 Intel IOMMU 的缺页请求处理增加并发锁保护，将页表项标志更新改为一次性写入所有传入标志，并仅在页表项具备写权限时设置脏位；启用共享虚拟内存时暴露可扩展模式一致性能力，若主机 IOMMU 不支持则阻止加速；AMD IOMMU 桩调用返回空能力字段，避免读取无效能力。 |
| Intel | [PATCH v9 00/6] intel_iommu: Enable PRQ support for passthrough device ------为 Intel 输入输出内存管理单元的直通设备新增页请求队列支持：客户机启用后，主机侧可恢复故障事件被接收并注入客户机，客户机的响应也能写回主机；客户机侧溢出或满错误时，低优先级页请求按丢弃后返回成功响应，其他错误返回无效请求。故障队列资源释放被推迟到底半部执行，避免因轮询尚未退出、文件仍持有引用而导致释放返回忙错误。 |
| Qualcomm | [PATCH v1 00/3] iommu: qcom: Fix the MSM GPU and display with DMA-address based mappings ------在高通骁龙平台上，显示和 GPU 设备因 IOMMU 缓冲失效和默认域选择错误无法工作：清空全部 TLB 的操作实际只等待同步，导致图形驱动解除映射后 GPU 可能挂起；同时图形驱动需要物理地址，但设备被分配到 IOMMU DMA 域，缓冲区映射到错误的 IOVA，GPU 无法启动。 |
| NVIDIA | [PATCH v3 00/10] Make the 32-bit ARM DMA API work with normal IOMMU DMA default domains (+ Tegra PoC) ------让 32 位 ARM 的 DMA API 能与内核管理的 DMA 默认域协作，并在 Tegra SMMU 上验证：拆分离散 ARM DMA 映射的初始化和分配，新增不拥有域的 cookie 及安装/拆除操作，使核心可拥有 DMA 域；大部分 32 位 ARM 平台解除强制身份域，少数平台仍显式保持身份域。 |
| Individual Contributor | [PATCH v1 00/6] iommufd: harden DMA-BUF PAL setup and release ------修复 iommufd 导入 DMA-buf 并建立物理地址列表映射时的生命周期竞态和错误处理：若固定操作失败，保留该失败的真实错误码，避免被当成成功；成功映射的物理列表和附着须在 reservation 锁内一起发布，失败则保持为空；释放时先清空物理列表指针再解锁，并仍在锁内完成解固定，最后拆除附着并销毁互斥锁，防止并发失效回调访问已释放列表或已销毁锁。自检新增覆盖固定和映射失败清理。 |
| NVIDIA | [PATCH v9 00/2] Organize the SMMUv3 invalidation flow so iommupt can use it ------重新组织 ARM SMMUv3 的 TLB 失效描述，改为用叶级和表级位图累积失效损伤，并据此计算单步长及范围失效提示，替换原先无法充分描述范围的旧流程；这样既能修复当前失效信息不足的问题，也为将来接入 iommupt 的聚合式失效做准备。当硬件支持双步幅时，范围失效的比例上限可提升到 39，不再受 31 限制。 |
| Amazon | [PATCH v1 00/3] iommu: Reduce iommu_probe_device_lock contention ------并行初始化虚拟功能时，IOMMU 设备探测的全局锁成为主要争用点，其中向 sysfs 发布成员链接和首次设置默认域占用了大量持锁时间。补丁将这两项工作移出全局锁：先在全局锁内完成组成员分配并持有组引用，释放全局锁后在组锁下发布链接、设置默认域；发布或设置失败时按现有失败语义回退。这样缩短全局锁持有时间，缓解大量设备并行探测时的锁竞争。 |
| 归属待核实（utexas.edu） | [PATCH] iommu/sva: Charge IOPF allocations to the faulting mm's memcg ------修复设备缺页处理在工作队列中未设置活动内存控制组的问题：此前文件后端缺页产生的页缓存被计入根控制组，逃逸任务的内存上限。现在处理缺页前切换到故障进程所属的内存控制组，完成后恢复原值，使设备触发的页缓存分配正确归属并受内存限制约束。 |
| Intel | [v8,6/6] intel_iommu_accel: teardown FAULTQ resources in bottom half ------在 Intel 输入输出内存管理单元直通设备中，当地址空间标识条目失效时，原先释放故障队列会立即关闭处理函数并释放队列编号，但存在一个窗口：轮询尚未退出时文件仍持有队列引用，可能使释放返回忙错误。现改为把故障队列及关联文件、队列编号的释放推迟到下半部回调执行，确保轮询退出并放下引用后再清理。 |
| 归属待核实（shutemov.name） | [v7,2/2] iommu/arm-smmu-v3: Default queue depths to one page in a kdump kernel ------在崩溃转储捕获内核中，SMMUv3 实例的命令、事件和页请求三个队列原先都按硬件公布的最大深度分配，即使事件和页请求队列已被关闭，每个实例仍可能占用最多 12 兆字节的保留内存。现在检测到处于捕获模式时，三个队列深度都只分配一页条目；这些队列只承载命令和故障记录而非传输数据，因而不会影响保存转储所需设备的吞吐。 |
| EPAM | [v13,09/14] iommu/ipmmu-vmsa: Implement suspend/resume callbacks ------为瑞萨 IPMMU-VMSA 在 Xen 下实现系统挂起与恢复：保存活跃上下文和微 TLB 寄存器，恢复时先恢复根 IPMMU 的上下文，再恢复缓存 IPMMU 的微 TLB；否则缓存 IPMMU 会通过微 TLB 配置选中根上下文，提前恢复可能暴露过期或未初始化的上下文。目前仅在 H3ULCB（R-Car Gen3）上测试。 |
| NVIDIA | [v2,07/11] iommu: Let 32-bit ARM drivers opt into a DMA API default domain ------解除 32 位 ARM 平台上对默认域类型的强制身份域覆盖，让 IOMMU 驱动可以通过默认域类型回调自行选择真正的 DMA API 默认域；当通用 DMA 域实现未启用但 ARM DMA API 实现可用时，允许驱动显式请求的 DMA 域通过。普通路径仍不会自动回退到 DMA 域，因此现有 32 位 ARM 驱动在未设置回调或显式返回身份域时行为保持不变。 |
| Qualcomm | [PATCH] iommu: arm-smmu-qcom: Skip fault-info reads when suspended ------高通 Adreno GPU 的 IOMMU 故障信息回调在无运行时电源管理引用的情况下直接读取 SMMU 寄存器。故障虽在 SMMU 活跃时触发，但 GPU 可能在处理线程到达前撤销电源投票，使 SMMU 运行时挂起；此时访问寄存器不安全，可能使后续恢复运行时出现 NoC 错误和异步 SError。补丁在读取前尝试保持设备活跃，若挂起已经开始则跳过寄存器读取，避免破坏故障现场和触发后续错误。 |

---

## 已合入 Patches

暂无。

## 社区讨论中 Patches

### ◆ 子系统：ARM SMMUv3（18 patches）

**▸ 组织：Google**（6 patches）

**[SERIES] KVM: arm64: SMMUv3 driver for pKVM (trap and emulate)** （cover letter，19/19 个 patch 达到代码量阈值）

- 日期：2026-10-15
- 状态：社区讨论中
- 作者邮箱：Mostafa Saleh <smostafa@google.com>
- 概括：在受保护 KVM 下新增 EL2 端 ARM SMMUv3 驱动和主机端配套驱动：把 SMMU MMIO 捐赠给 hypervisor，对主机访问进行陷阱并模拟寄存器读写，使 hypervisor 拥有硬件并建立影子页表，从而提供 DMA 隔离。同时将队列、流表项、IDR 解析、无命中更新和范围失效等逻辑移入主机与 hypervisor 共享代码，并实现命令队列和流表影子、TLB 失效以及主机阶段二页表的同步更新。
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
- 概括：为 ARM SMMUv3 及 Tegra241 命令队列硬件实现运行时和系统休眠支持。挂起前在命令队列生产者索引中设置停止标志以阻止新命令提交，并排空命令队列和虚拟命令队列；恢复时从缓存重写消息中断配置并恢复队列读写指针。新增运行时电源管理及设备链接，确保硬件访问前唤醒设备，并补充单元测试，避免休眠挂起因未完成命令超时或硬件状态丢失而失败。
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
- 概括：为 Arm SMMUv3 增加跨内核热升级状态保持，利用内核交接框架把流表、上下文描述符表和事件队列内存保留到新内核，启动时直接接管这些硬件状态而不复位系统内存管理单元，并继承地址空间标识与虚拟机标识；关闭阶段只阻止未保留设备并保持翻译使能，使设备 DMA 在热升级切换过程中持续工作。
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
- 概括：修复 ARM SMMUv3 流表和上下文描述符发布顺序问题：在写 L1 指针前增加写屏障，确保已分配并零初始化的 L2 表对 SMMU 可见，避免硬件读到随机内容。配套测试修复上下文描述符被当作流表解析、缺失错误检查可能访问空指针、数组边界断言不停止导致越界，以及测试结构体缺少计数导致 UBSAN 越界报错。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/arm-smmu-v3: Ensure L2 tables are visible before L1 ptrs
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260924085616.300650-2-smostafa@google.com/

**[v10,08/15] iommu/arm-smmu-v3: Cache and restore MSI config**

- 日期：2026-09-08
- 状态：社区讨论中
- 作者邮箱：Pranjal Shrivastava <praan@google.com>
- 概括：针对 ARM SMMUv3 在系统掉电后恢复时 MSI 配置寄存器丢失、导致事件队列等中断无法继续使用的问题，首次写入 MSI 报文时缓存目标地址和数据，恢复阶段重写这些寄存器以恢复 MSI 投递；同时，MSI 初始化失败回退到有线中断时清除 MSI 能力标记，避免恢复阶段对不存在的 MSI 做无意义重配。这样挂起再唤醒后，事件、全局错误和页面请求中断仍能按原配置工作。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260908171712.356645-9-praan@google.com/

**iommu/arm-smmu-v3-sva: Relax ASID requirements**

- 日期：2026-09-07
- 状态：社区讨论中
- 作者邮箱：Mostafa Saleh <smostafa@google.com>
- 概括：ARM SMMUv3 的共享进程地址空间支持检查原先要求 SMMU 的 ASID 空间不小于 CPU，因为早期实现依赖分布式虚拟内存并复用 CPU 进程标识；后来该依赖已被移除，SMMU ASID 与 CPU 无需再匹配。补丁删除 CPU ASID 相关检查，并改为打印最大共享上下文数，避免 ASID 位数较小的 SMMU 被错误地判定为不支持共享地址空间。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260907154928.4012151-1-smostafa@google.com/

**▸ 组织：NVIDIA**（5 patches）

**[SERIES] iommu/arm-smmu-v3: Adopt the crashed kernel's stream table for kdump** （cover letter，8/11 个 patch 达到代码量阈值）

- 日期：2026-10-05
- 状态：社区讨论中
- 作者邮箱：Nicolin Chen <nicolinc@nvidia.com>
- 概括：在崩溃转储内核启动时不再复位 Arm SMMUv3，而是采纳崩溃内核的流表并保留其使能位，让飞行中的设备 DMA 继续按原页表翻译，避免全局中止或绕过导致致命错误和内存破坏；同时禁用事件队列与页请求队列，扫描并保留旧地址空间标识和虚拟机标识，防止新域命中旧缓存。
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
- 概括：在 ARM SMMUv3 使用共享进程地址空间时，连续页表项可能因硬件缺陷在范围失效被从中间拆分时漏失效，恶意用户可借助内存映射操作触发；原有范围失效也可能发出多达 512 条单条命令或多次范围命令，延迟较高。补丁将 SVA 失效改为一次覆盖整个连续项的范围命令，并预计算失效命令、整理参数，将普通范围失效控制在最多两次且可重叠覆盖，以降低延迟，同时为后续页表接管的失效流程做准备。
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
- 概括：在 ARM SMMUv3 上检测到 ATC 失效超时后隔离设备：通过命令队列错误位图将超时关联到发起者并返回失败，随后阻止该设备的 ATS 并保持在阻塞域，直到成功复位才恢复，防止陈旧 ATC 条目引发数据破坏。同时修正 PCI 重置探测阶段错误挂起 IOMMU 造成 DMA 中断的问题，并调整 PCI 和 CXL 探测逻辑。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/arm-smmu-v3: Thread arm_smmu_master_domain on a per-master list
  - iommu/arm-smmu-v3: Quarantine ATS after an ATC invalidation timeout
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/5ddbd81323f86d045072ebf410a6f87da4f2796f.1790188511.git.nicolinc@nvidia.com/

**[SERIES] iommu/arm-smmu-v3: Add PRI support** （cover letter，10/12 个 patch 达到代码量阈值）

- 日期：2026-09-15
- 状态：社区讨论中
- 作者邮箱：Nicolin Chen <nicolinc@nvidia.com>
- 概括：为 ARM SMMUv3 增加 PCI 页请求接口支持。在设备从域分离时，先排空硬件事件队列并刷新未完成的 I/O 页故障工作，避免旧域释放后工作引用已释放内存；仅在硬件支持停顿而无共享虚拟地址时也分配 I/O 页故障队列；对页请求事件提交对应响应命令。这些修改让支持页请求的 PCI 设备能安全使用缺页报告，并修复分离路径上的释放后使用风险。
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
- 概括：在 Arm CCA 机密虚拟机中，通过固件 RSI 命令探测并激活可信的 SMMUv3 实例，校验 ACPI 提供的寄存器范围与固件信息一致，避免替换攻击；同时将 IOMMU 标记为机密并使用私有内存分配队列和页表。针对 TDISP 设备双 DMA 流，把 T=1 可信流置于阻塞域，T=0 流走身份映射，并拒绝用户态域更改、驱动分组附加和 PASID 附加，防止两条流互相干扰。当前不支持机密虚拟机内的 T=0 SMMU。
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
- 概括：在 Stream ID 数量有限的 SoC 上允许多个设备共用同一 SID，通过共享同一个流对象和域级上下文描述符表，确保它们绑定到同一 IOMMU 域；共享设备被归入同一组，并且禁用共享标识下无法唯一归属故障的特性，如共享虚拟地址、进程地址空间标识、地址翻译服务和故障停顿，释放单个设备时不会破坏其他共享者 DMA。这样 NXP i.MX95 等平台的多设备共用流标识可正常探测。
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
- 概括：修复 ARM SMMUv3 在流标识数组存在相邻重复项时，移除主设备或插入失败回滚可能破坏红黑树一致性的问题。别名桥后的 PCI 设备可能产生重复流标识，插入阶段会静默丢弃未链接的重复节点，但删除路径仍无条件对所有数组项执行红黑树删除，导致对未初始化节点操作并损坏树。现在利用流标识已排序、重复项相邻的特点，在回滚和移除时跳过这些重复项，使删除操作与插入行为一致。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20261001-smmu-shared-sid-ver3-v4-1-06b34fb2e691@nxp.com/

**[RFC,v2,1/4] iommu/arm-smmu-v3: Convert streams from RB tree to XArray**

- 日期：2026-09-21
- 状态：社区讨论中
- 作者邮箱：Peng Fan <peng.fan@oss.nxp.com>
- 概括：将 ARM SMMUv3 中按流标识查找流对象的结构从红黑树改为 XArray，继续使用现有互斥锁串行化插入、删除和读取，避免依赖读侧 RCU 宽限期；由于部分路径持锁时会睡眠，保留互斥锁是必要的。改造移除了红黑树比较逻辑和节点成员，并简化了桥接 PCI 设备出现重复流标识时的处理。该改动不改变现有行为，目的是为后续共享流标识支持做准备。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260921-smmu-shared-sid-v2-1-4b656ce68178@nxp.com/

**▸ 组织：归属待核实（foxmail.com）**（1 patches）

**iommu/arm-smmu-v3: Skip unlinked duplicate stream nodes on removal**

- 日期：2026-09-21
- 状态：社区讨论中
- 作者邮箱：zhoumin <teczm@foxmail.com>
- 概括：修复 ARM SMMUv3 中重复流标识导致红黑树损坏的问题。别名桥后的 PCI 设备可能产生重复流标识，插入时若重复项属于同一主设备则被接受但不会链接到红黑树；删除和插入失败回滚时却无条件删除每个节点，误删未链接节点可能清除树根，破坏其他设备的流标识映射。现在对跳过的重复节点做清空标记，并在删除和回滚路径中跳过未链接节点，保持树结构一致。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/tencent_4392079B5C29406B923C037A7E66DD338005@qq.com/

**▸ 组织：Kernel.org**（1 patches）

**[v2,2/5] iommu/arm-smmu-v3: Switch to use acpi_bus_get_primary_device()**

- 日期：2026-09-30
- 状态：社区讨论中
- 作者邮箱：Rafael J. Wysocki (Intel) <rafael@kernel.org>
- 概括：调整 ARM SMMUv3 在 ACPI 下查找 Tegra241 命令队列伴随设备的方式，改用会持有设备引用的 ACPI 接口获取主设备，替换即将移除且返回后不持有引用的旧接口。旧接口在释放 ACPI 节点锁后返回的设备可能立即被移除，存在释放后使用风险；新接口通过引用计数保证返回设备在后续使用期间不会被释放，从而消除这一潜在问题。
- 来源：https://patchwork.kernel.org/project/alsa-devel/patch/3636226.QJadu78ljV@rafael.j.wysocki/

**▸ 组织：归属待核实（shutemov.name）**（1 patches）

**[SERIES] iommu/arm-smmu-v3: Make the queue depths tunable, and shrink them in a kdump kernel** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-09-25
- 状态：社区讨论中
- 作者邮箱：Kiryl Shutsemau <kirill@shutemov.name>
- 概括：为 ARM SMMUv3 增加按条目数对数指定命令队列深度的模块参数，默认维持原最大深度且不低于一页；在 kdump 捕获内核中，三个队列默认只分配一页大小的条目。此前队列按硬件通告最大值分配，每个实例可达数 MB，而捕获内核运行在很小的预留内存中且部分队列被禁用，造成浪费。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/arm-smmu-v3: Default queue depths to one page in a kdump kernel
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260925141532.1274962-3-kirill@shutemov.name/

**▸ 组织：Debian**（1 patches）

**[SERIES] iommu/arm-smmu-v3: SMMU hitting kdump mid-air** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-09-11
- 状态：社区讨论中
- 作者邮箱：Breno Leitao <leitao@debian.org>
- 概括：kdump 启动时，新内核不再完全重置 SMMU 并安装空白流表，而是在关闭 SMMU 前读取前一个内核的流表，复制一级描述符并继续使用其二级表，让仍在 DMA 的设备保持原有翻译，避免未驱动网卡继续访问时产生非法流 ID 故障而被固件复位；同时把设备默认域附加推迟到下次 DMA，以免探测时立即替换继承条目造成翻译故障。仅在 SMMU 已启用、几何一致且一致性满足时继承。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/arm-smmu-v3: inherit the previous kernel's stream table in kdump
  - iommu/arm-smmu-v3: defer attach in kdump so inherited entries survive probe
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260911-smmu_fix_aws-v1-1-75870bf9655b@debian.org/

---

### ◆ 子系统：IOMMUFD（13 patches）

**▸ 组织：Individual Contributor**（5 patches）

**[SERIES] guest_memfd: Export guest_memfd files to iommufd** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-10-27
- 状态：社区讨论中
- 作者邮箱：Fred Griffoul <griffoul@gmail.com>
- 概括：为虚拟机客户机内存文件增加导出接口，使分配给客户机的设备可通过输入输出内存管理单元用户态接口映射其共享内存，而不是长期锁定页面。原接口只固定锁定映射内容，无法在客户机内存文件撤销、转换或重新提供页面时同步；现在通过回调更新或解除受影响设备映射，只读物理帧不加写权限，未映射或重新映射失败的范围保持未映射并告警。物理帧号模式下还会把 KVM 映射块限制到与页属性对齐的范围，避免跨共享和私有页错误映射。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommufd: Map guest_memfd files
  - iommufd: Track the domains of revocable pages in struct iopt_pages
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261027154649.91571-10-griffoul@gmail.com/

**[SERIES] iommufd: harden DMA-BUF PAL setup and release** （cover letter，4/6 个 patch 达到代码量阈值）

- 日期：2026-10-20
- 状态：社区讨论中
- 作者邮箱：Karl Mehltretter <kmehltretter@gmail.com>
- 概括：加固iommufd对DMA-BUF物理地址列表的建立和释放路径，修复并发失效与释放之间的竞态：固定失败原被误报成功，现在保留实际错误；成功映射与撤销均在预留锁保护内完成，并在解除映射前清空指针、在解除DMA-BUF附加后再销毁互斥锁，避免失效回调访问无效状态，自测试覆盖失败清理。
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
- 概括：引入内存提供者抽象，让没有页结构或由驱动独占的内存文件能够同时支持虚拟客户机私有内存和 IOMMU 映射；客户机故障和输入输出页表填充按帧向提供者查询属性与物理地址，提供者撤销某个范围时所有消费者会同步解除映射。这样物理连续设备内存或与对端共享的内存不再需要固定使用页分配器，并支持只读页。
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
- 概括：为自测试补充对共享缓冲区在另一域中填充设备内存映射属性的检查。模拟页表原先无法区分该属性和普通缓存映射，现在包装映射与取消映射操作，按域记录以该属性建立的页，并增加检查命令验证指定范围。测试覆盖在同一地址空间新建第二个域和把共享缓冲区复制到另一地址空间已有域两种情况；没有前序修复时新增域检查会失败，修复后三类模拟域均通过。
- 来源：https://patchwork.kernel.org/project/linux-kselftest/patch/20261008125206.11990-3-parri.andrea@gmail.com/

**[SERIES] iommufd: Keep IOMMU_HWPT_GET_DIRTY_BITMAP within the user bitmap** （cover letter，2/4 个 patch 达到代码量阈值）

- 日期：2026-09-25
- 状态：社区讨论中
- 作者邮箱：Andrea Parri <parri.andrea@gmail.com>
- 概括：在 IOMMU 用户态接口的脏页位图查询中，当请求范围只覆盖一个大页的一部分时，硬件上报的整个大页会把位图之后的内存置位，零长度请求也会因长度下溢被接受并扫描整个地址空间。现在将记录范围裁剪到位图边界，并提前拒绝零长度请求，同时加入自测覆盖越界和零长度情况，防止内核写出用户缓冲区。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommufd/iova_bitmap: Clip recorded ranges to the bitmap
  - iommufd: Reject a zero-length dirty bitmap request
- 来源：https://patchwork.kernel.org/project/linux-kselftest/patch/20260925161142.189813-2-parri.andrea@gmail.com/

**▸ 组织：Alibaba**（3 patches）

**[SERIES] iommufd: Recommended reservations query and opt-in IOAS reservation** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-10-28
- 状态：社区讨论中
- 作者邮箱：Guanghui Feng <guanghuifeng@linux.alibaba.com>
- 概括：新增查询设备推荐保留IOVA范围的接口及可选的IOAS保留接口：内核报告PCI设备所在主机桥的MMIO窗口，因在这些范围内发起DMA可能被PCIe交换机当点到点流量误路由而不经IOMMU翻译；用户空间可查询后自行决定是否保留，保留后这些范围从可用IOVA范围和映射操作中排除，整个流程可选，不使用则行为不变。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommufd: Add IOMMU_GET_RECOMMENDED_RESERVATIONS ioctl
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261028090453.2392991-2-guanghuifeng@linux.alibaba.com/

**[v4,2/2] iommufd: Add IOMMU_GET_PCI_MMIO_WINDOWS ioctl**

- 日期：2026-10-25
- 状态：社区讨论中
- 作者邮箱：Guanghui Feng <guanghuifeng@linux.alibaba.com>
- 概括：为输入输出内存管理用户接口新增按设备查询命令，让用户态（如虚拟机监视器）获知设备所在 PCI 主机桥的内存映射窗口范围。此前用户态无法知道哪些地址可能被 PCIe 交换机误判为点对点 DMA 目标；现在内核只报告这些窗口而不保留或强制，用户态可自愿把 I/O 虚拟地址分配避开它们。若输出数组过小则返回长度不足错误。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261025133000.205508-3-guanghuifeng@linux.alibaba.com/

**[SERIES] iommu: Reserve PCI host bridge MMIO windows for IOVA** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-09-21
- 状态：社区讨论中
- 作者邮箱：Guanghui Feng <guanghuifeng@linux.alibaba.com>
- 概括：把 PCI 主机桥 MMIO 窗口纳入 IOMMU 组和 iommufd IOAS 的保留区域。此前这些窗口仅由 DMA IOVA 层保留，VFIO type1 和 iommufd 向用户态报告的可用 IOVA 可能落入桥窗口；当设备位于 PCIe 交换机后且 ACS 上游转发未完全启用时，这类 IOVA 的 DMA 可能被交换机当作点对点流量误路由到其他设备。现在组级保留包含这些窗口，用户态不再获得重叠地址。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu: Reserve PCI host bridge MMIO windows in group reserved regions
  - iommufd: Reserve PCI host bridge MMIO windows in IOAS reserved regions
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260921103922.1113752-2-guanghuifeng@linux.alibaba.com/

**▸ 组织：Kernel.org**（3 patches）

**[RFC,v2,03/13] iommufd: Support MMIO provider attachment to vDEVICEs**

- 日期：2026-10-17
- 状态：社区讨论中
- 作者邮箱：Aneesh Kumar K.V <aneesh.kumar@kernel.org>
- 概括：为虚拟设备增加设备内存映射提供者的附加与分离机制。设备提供者此前没有统一的附加路径；现在可在后端验证其与虚拟机关联后，把该提供者绑定到已存在的虚拟设备，并增加互斥锁串行化附加、分离与内存转换。提供者或后端可查询是否仍有私有内存映射范围，且虚拟设备及其上下文会保持存活直到提供者分离，避免释放后仍被访问。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261017073149.1303738-4-aneesh.kumar@kernel.org/

**[SERIES] iommufd: vIOMMUs and TSM guest requests for confidential guests** （cover letter，6/6 个 patch 达到代码量阈值）

- 日期：2026-10-08
- 状态：社区讨论中
- 作者邮箱：Aneesh Kumar K.V <aneesh.kumar@kernel.org>
- 概括：为机密客户机的 vIOMMU 增加客户机 TSM 请求分发：iommufd 现在关联 VFIO 设备的 KVM 文件并保留引用，通过新 ioctl 把客户机产生的 TSM 命令转发给管理受分配设备的 TEE 安全管理器，同时让 PCI TSM 后端可以为 vIOMMU 提供操作并校验设备与 vIOMMU 使用同一管理器，移除旧的 PCI 设备级请求通道。
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
- 概括：建立 vIOMMU 创建基础设施并引入外部 provider 注册机制：当物理 IOMMU 驱动不实现某 vIOMMU 类型时，改为查找注册的 provider，由其提供操作和私有数据。同时把 VFIO 对 KVM 的引用改为基于文件的生命周期管理，TSM 设备增加活动用户引用，最终使机密客户机可通过 iommufd vdevice 转发客户机 TSM 请求，并替换旧的 PCI/TSM 绑定接口。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommufd: Add vIOMMU provider support
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260917140159.1163281-6-aneesh.kumar@kernel.org/

**▸ 组织：NVIDIA**（1 patches）

**iommupt: Do not allow PTEs to be split when dirty logging**

- 日期：2026-10-15
- 状态：社区讨论中
- 作者邮箱：Jason Gunthorpe <jgg@nvidia.com>
- 概括：修复通用页表脏页跟踪中允许拆分单个页表项的错误。原先当单个页表项放不进当前位图时会被拆分，可能把脏内存报告为干净；清理范围也只覆盖匹配部分。现在按每个页表项的完整 I/O 虚拟地址范围更新位图和失效收集范围，位图对放不下的范围直接拒绝，失效收集范围始终合并。自测原先依赖该拆分缺陷，现将脏页测试页大小调整为系统页大小以保持覆盖整个页表项。
- 来源：https://patchwork.kernel.org/project/linux-kselftest/patch/0-v1-5bb926ff73ec+576-iommufd_dirty_jgg@nvidia.com/

**▸ 组织：Google**（1 patches）

**[SERIES] iommu: Introduce Page Table Observability Framework** （cover letter，2/5 个 patch 达到代码量阈值）

- 日期：2026-10-01
- 状态：社区讨论中
- 作者邮箱：Pranjal Shrivastava <praan@google.com>
- 概括：为传统虚拟化容器和 IOMMU 用户态接口新增页表内存占用观测，把页表分配归属到具体域并累计页数，再在进程文件描述信息中暴露该计数。使用通用页表库的驱动自动计入；如果相关域不提供计数则省略该字段，避免给出部分统计。解除映射后计数保持不变，以反映仍可回收的页表内存。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommupt: Enable per-domain IOPT attribution
  - iommufd: Expose IO page table usage via fdinfo
- 来源：https://patchwork.kernel.org/project/linux-kselftest/patch/20261001224531.765278-2-praan@google.com/

---

### ◆ 子系统：IOMMU Core（12 patches）

**▸ 组织：东南大学**（2 patches）

**iommu/exynos: quiesce SysMMU before requesting IRQ**

- 日期：2026-09-21
- 状态：社区讨论中
- 作者邮箱：Runyu Xiao <runyu.xiao@seu.edu.cn>
- 概括：针对 Exynos SysMMU 驱动在获取时钟和识别硬件版本之前就注册中断的问题，调整初始化顺序：先获取时钟并初始化软件状态，再在时钟使能期间识别版本、禁用 SysMMU 并清除其配置，最后才注册中断处理程序。这样发布中断处理程序时硬件已处于静默状态；同时在 SysMMU 未激活时直接忽略中断，防止虚假中断访问尚未初始化的故障状态或指针。该竞争目前仅为理论风险，尚未在实际运行中观测到。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260921120848.96215-1-runyu.xiao@seu.edu.cn/

**iommu/exynos: Initialize lock before requesting IRQ**

- 日期：2026-09-01
- 状态：社区讨论中
- 作者邮箱：Runyu Xiao <runyu.xiao@seu.edu.cn>
- 概括：三星 Exynos 平台 SysMMU 驱动中，自旋锁初始化发生在中断请求之后。由于中断处理程序在请求中断后即可运行，早期到达的中断可能使用尚未初始化的锁，造成并发访问异常。补丁将锁初始化移动到请求中断之前，确保中断处理程序首次运行前锁已就绪。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260901130527.3289245-1-runyu.xiao@seu.edu.cn/

**▸ 组织：Qualcomm**（2 patches）

**[SERIES] iommu: qcom: Fix the MSM GPU and display with DMA-address based mappings** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-10-30
- 状态：社区讨论中
- 作者邮箱：Dmitry Baryshkov <dmitry.baryshkov@oss.qualcomm.com>
- 概括：修复高通旧款 IOMMU 以及 ARM SMMU 高通扩展中 GPU 与显示设备的 DMA 地址映射问题。旧款 IOMMU 的全域 TLB 刷新只等待同步而不失效，导致 db410c 上 GPU 复用地址时因旧条目挂起；GPU/显示设备又未选择直通域，缓冲区被映射到无用的 IOMMU 地址，db410c 无法启动，db820c 上 MDP5 也因直通选择缺失导致复位。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/arm-smmu-qcom: Use identity default domains for MDP5
  - iommu/qcom: Use identity default domains for the MSM GPU and display
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20261031-msm-smmu-identity-v1-1-a2a70580eebd@oss.qualcomm.com/

**[SERIES] iommu/qcom+msm: Use identity domain for display/GPU** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-10-29
- 状态：社区讨论中
- 作者邮箱：Rob Clark <robin.clark@oss.qualcomm.com>
- 概括：为高通旧款 IOMMU 和 MSM IOMMU 驱动上的 Adreno GPU 与显示设备改用直通默认域。此前这些设备会由 IOMMU 核心分配默认翻译域，而 drm/msm 驱动需要自行附加并管理域，造成地址映射重复和干扰；现在按设备兼容标识为 GPU 和显示设备选择直通域，使 DMA 地址保持物理地址、不建立额外 IOMMU 映射，由 drm/msm 自行管理页表。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/qcom: Use identity domain for GPU and display
  - iommu/msm: Use identity domain for GPU and display
- 来源：https://patchwork.kernel.org/project/linux-arm-msm/patch/20261029212344.346069-2-robin.clark@oss.qualcomm.com/

**▸ 组织：归属待核实（jannau.net）**（1 patches）

**[v3,2/2] iommu: apple-dart: Support specifying the DMA aperture in the DT**

- 日期：2026-09-02
- 状态：社区讨论中
- 作者邮箱：Janne Grunau <j@jannau.net>
- 概括：苹果 DART 常直接连接只允许将部分地址空间用于 DMA 的设备，其他范围可能被映射到别的用途；原先 DART 的 DMA 窗口只能由自身能力决定。补丁允许设备在设备树 iommus 参数中指定 64 位起始和长度，且范围可以位于 DART 输入地址空间之外，由硬件截断地址，页表仅映射低位；但不能跨越输入地址空间边界或回绕。这样苹果平台设备可精确声明可用的 DMA 孔径。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260902-iommu-apple-dart-aperture-v3-2-252ce55b7001@jannau.net/

**▸ 组织：Individual Contributor**（1 patches）

**[v1,1/2] iommu: export iommu_get_dma_domain()**

- 日期：2026-09-28
- 状态：社区讨论中
- 作者邮箱：Jianfeng Liu <liujianfeng1994@gmail.com>
- 概括：导出获取设备 DMA 域的 IOMMU 接口，供模块化的 drm/msm 驱动使用。启用 dma-buf 调试功能时，导入的 dma-buf 所附散列表不携带物理页，msm 需要借助附加设备的 DMA 域把散列表中的 DMA 地址转换回物理地址，进而映射到自身页表；该接口导出后，模块化驱动可以直接调用完成这一地址恢复。
- 来源：https://patchwork.kernel.org/project/dri-devel/patch/20260928053901.7270-2-liujianfeng1994@gmail.com/

**▸ 组织：Kernel.org**（1 patches）

**[slab/for-next,09/14] iommu: specify SLAB_MAY_ACCOUNT for slab-backed page table caches**

- 日期：2026-10-21
- 状态：社区讨论中
- 作者邮箱：Harry Yoo <harry@kernel.org>
- 概括：为用户态设备直通路径（VFIO、iommufd 和 vhost-vdpa）使用的输入输出内存管理单元页表内核缓存补充允许内存控制组记账的属性。这些路径在建立映射时携带要求计入内存控制组的分配标志，但底层页表缓存原先未开放记账能力，导致页表内存无法归属对应内存控制组；修改后相关页表分配可被正确统计和限制。
- 来源：https://patchwork.kernel.org/project/linux-mm/patch/20261021-memalloc-prof-dont-waste-slabobj-ext-metadata-v1-9-096800aa3330@kernel.org/

**▸ 组织：EPAM**（1 patches）

**[v13,09/14] iommu/ipmmu-vmsa: Implement suspend/resume callbacks**

- 日期：2026-10-27
- 状态：社区讨论中
- 作者邮箱：Mykola Kvach <mykola_kvach@epam.com>
- 概括：为瑞萨 IPMMU-VMSA 在 Xen 下实现系统挂起与恢复：保存活跃上下文和微 TLB 寄存器，恢复时先恢复根 IPMMU 的上下文，再恢复缓存 IPMMU 的微 TLB；否则缓存 IPMMU 会通过微 TLB 配置选中根上下文，提前恢复可能暴露过期或未初始化的上下文。目前仅在 H3ULCB（R-Car Gen3）上测试。
- 来源：https://patchwork.kernel.org/project/xen-devel/patch/3f8f4ecf30d38d589c2d08f5b2676bda93f8d880.1793129971.git.mykola_kvach@epam.com/

**▸ 组织：归属待核实（chromium.org）**（1 patches）

**iommu/mediatek: Track first resume with a dedicated boolean flag**

- 日期：2026-10-28
- 状态：社区讨论中
- 作者邮箱：Chen-Yu Tsai <wenst@chromium.org>
- 概括：联发科 IOMMU 驱动原先依赖写长度控制寄存器在首次运行时恢复前是否为零来判断是否为首次恢复，该默认值非零使判断隐晦且容易误读。现改用专用布尔标志直接记录首次运行时恢复是否已完成：首次恢复仅开启时钟并置位标志，后续恢复再恢复已保存的寄存器。流程更清晰，不改变实际行为。
- 来源：https://patchwork.kernel.org/project/linux-mediatek/patch/20261028041651.3201911-1-wenst@chromium.org/

**▸ 组织：归属待核实（reactivated.net）**（1 patches）

**[SERIES] Add support for Broadcom BCM2712 IOMMU driver (Raspberry Pi 5)** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-09-27
- 状态：社区讨论中
- 作者邮箱：Daniel Drake <dan@reactivated.net>
- 概括：为树莓派 5 所用博通 BCM2712 芯片增加 IOMMU 驱动和对应两级页表格式，用于显示流水线及多媒体设备的内存地址翻译，并支持刷新该芯片共享的二级快表；同时修正页表边界测试地址，使其适配该芯片较窄的物理地址空间，并补充设备树节点以启用显示硬件视频缩放器后的 IOMMU。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/generic_pt: Add Broadcom BCM2712 page table format
  - iommu: Add Broadcom BCM2712 IOMMU driver
- 来源：https://patchwork.kernel.org/project/devicetree/patch/20260927-bcm2712-iommu-submit-v7-4-dfa2b975cbc9@reactivated.net/

**▸ 组织：Microsoft**（1 patches）

**[SERIES] Hyper-V: Add para-virtualized IOMMU support for Linux guests** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-09-30
- 状态：社区讨论中
- 作者邮箱：Yu Zhang <zhangyu1@linux.microsoft.com>
- 概括：为 Hyper-V Linux 客户机新增半虚拟化 IOMMU 驱动，基于超级调用在客户机内构建第一阶段地址翻译页表，管理设备域、设备附加和 IOTLB 失效；客户机页表与宿主第二阶段页表嵌套，映射操作可避免虚拟机退出，但解除映射后的 IOTLB 刷新仍会退出。同时增加逻辑设备编号注册表以标识 PCI 直通设备，并支持页选择 IOTLB 刷新，失败回退全域刷新。初始版本不支持客户机休眠和恢复。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/hyperv: Add para-virtualized IOMMU support for Hyper-V guest
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/20260930141409.437904-4-zhangyu1@linux.microsoft.com/

**▸ 组织：Amazon**（1 patches）

**[SERIES] iommu: Reduce iommu_probe_device_lock contention** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-09-11
- 状态：社区讨论中
- 作者邮箱：Sakac, Pavol <sakacpav@amazon.de>
- 概括：并行初始化虚拟功能时，IOMMU 设备探测的全局锁成为主要争用点，其中向 sysfs 发布成员链接和首次设置默认域占用了大量持锁时间。补丁将这两项工作移出全局锁：先在全局锁内完成组成员分配并持有组引用，释放全局锁后在组锁下发布链接、设置默认域；发布或设置失败时按现有失败语义回退。这样缩短全局锁持有时间，缓解大量设备并行探测时的锁竞争。
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu: split sysfs link publication out of iommu_group_alloc_device()
  - iommu: create device sysfs links outside iommu_probe_device_lock
  - iommu: set up the default domain outside iommu_probe_device_lock
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/20260911125907.67105-1-sakacpav@amazon.de/

---

### ◆ 子系统：RISC-V IOMMU（10 patches）

**▸ 组织：归属待核实（sanechips.com.cn）**（2 patches）

**[SERIES] iommu/riscv: Add nested translation (vIOMMU) support** （cover letter，3/9 个 patch 达到代码量阈值）

- 日期：2026-10-29
- 状态：社区讨论中
- 作者邮箱：Gong Shuai <gong.shuai@sanechips.com.cn>
- 概括：为RISC-V IOMMU增加嵌套翻译和vIOMMU支持，使虚拟机可经iommufd分配嵌套域，将客户机一级页表上下文与宿主二级父域组合，设备DMA经两级翻译；新增硬件能力查询与客户机缓存失效命令转发，转发前校验并替换隔离标识，防止客户机越权失效其他客户机的缓存，同时改用设备上下文有效位判断并传递完整设置。
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu/riscv: Add nested domain allocation
  - iommu/riscv: Use DC.tc.V as the device context valid bit
  - iommu/riscv: Add vIOMMU cache invalidation
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20261029061131.584453-6-gong.shuai@sanechips.com.cn/

**[RFC,11/12] iommu/riscv: Accept unpublished interrupt files in IRQ forwarding**

- 日期：2026-10-15
- 状态：社区讨论中
- 作者邮箱：Gong Shuai <gong.shuai@sanechips.com.cn>
- 概括：在 RISC-V 虚拟机使用虚拟 IOMMU 转发消息中断时，首个设备转发会安装整机消息中断表，但此时部分虚拟 CPU 的中断文件可能尚未发布，原有校验会因目标不完整而拒绝整个请求，导致整机失去中断旁路。现在跳过未发布的目标，只有解析到这些目标的消息中断会产生对应虚拟 CPU 的故障记录，使其余目标上的转发可继续建立。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261015065232.604503-12-gong.shuai@sanechips.com.cn/

**▸ 组织：Alibaba**（2 patches）

**[SERIES] iommu/riscv: Add irqbypass support without MSI page table** （cover letter，3/4 个 patch 达到代码量阈值）

- 日期：2026-10-14
- 状态：社区讨论中
- 作者邮箱：yu fangyu <fangyu.yu@linux.alibaba.com>
- 概括：为不具备平坦MSI页表能力的RISC-V IOMMU实现无需MSI页表的中断转发，将客户机IMSIC页面映射到宿主IMSIC物理地址，使设备MSI写直接到达vCPU中断文件；在vCPU迁移导致宿主页移动时，用原子替换页表叶子条目替代先解除再映射，避免窗口期内设备MSI写触发页故障。
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu/riscv: Support IRQ forwarding without MSI page tables
  - iommu/riscv: Extract IRQ forwarding payload validation
  - iommupt: Add replace_leaf to atomically swap a leaf OA
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20261014141124.48569-5-fangyu.yu@linux.alibaba.com/

**[SERIES] iommu/riscv: Fix command queue publishing races** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-09-01
- 状态：社区讨论中
- 作者邮箱：yu fangyu <fangyu.yu@linux.alibaba.com>
- 概括：修复 RISC-V IOMMU 命令队列发布的竞态。原先多个处理器并发写命令时，软件生产者状态可能在硬件尾指针更新前推进，导致队列状态不一致。现在增加原始自旋锁串行化命令发布，确保命令写入且硬件尾更新后才推进；队列满时在锁外等待硬件消耗，避免阻塞其他处理器；入队失败时不等待输入输出栅栏命令完成，避免产生误导性执行超时。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/riscv: Serialize command queue publishing
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20260901133920.14550-2-fangyu.yu@linux.alibaba.com/

**▸ 组织：Qualcomm**（2 patches）

**[SERIES] iommu/riscv: Add irqbypass support** （cover letter，7/10 个 patch 达到代码量阈值）

- 日期：2026-09-28
- 状态：社区讨论中
- 作者邮箱：Andrew Jones <andrew.jones@oss.qualcomm.com>
- 概括：为 RISC-V 输入输出内存管理单元增加中断旁路支持，使虚拟机的客户机中断控制器地址能够通过二级阶段的 MSI 页表转发给设备，而不是直接访问主机物理地址。新增 MSI 表分配、中断重映射域、转发请求校验与硬件编程，并且在设备仍有转发中断时拒绝直接替换二级域，避免中断状态指向已分离页表。
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
- 概括：64 位 RISC-V 上新打通消息中断重映射、设备 DMA 地址映射支持和 VFIO 直通：iommufd 中软件消息中断映射改为按需增长并支持物理地址列表的原子安装，IMSIC 提供所有可能 CPU 的中断页地址列表并由 IOMMU 映射为连续 I/O 虚拟地址范围；为 iommufd 保留每 CPU 一页的消息中断窗口，仅避开已知客户机布局，仍可能冲突；同时开启设备 DMA 地址映射支持、VFIO 与 KVM/VFIO 接口。
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
- 概括：RISC-V IOMMU 若具备硬件性能监视器能力，原先没有内核侧设备供性能监视驱动绑定。补丁在 IOMMU 初始化检测到该能力时注册一个辅助设备，作为硬件性能监视器的枚举入口；即使创建失败只记录警告，IOMMU 仍继续工作。该能力使 RISC-V 平台能够为 IOMMU 性能监视单元加载对应驱动并采集性能计数。
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20261006090327.309550-3-zong.li@sifive.com/

**▸ 组织：The Good Penguin**（1 patches）

**iommu/riscv: Use named initializers for acpi_device_id**

- 日期：2026-10-14
- 状态：社区讨论中
- 作者邮箱：Pawel Zalewski <pzalewski@thegoodpenguin.co.uk>
- 概括：将 RISC-V 输入输出内存管理单元的 ACPI 设备匹配表改为按字段名初始化，省略冗余的显式置零，并统一结尾项的括号空格和末尾逗号风格。这是纯代码可读性和一致性调整，使该列表与内核其他同类初始化写法保持一致，不影响设备匹配行为。
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20261014-acpi-iommu-v1-1-1744523fa658@thegoodpenguin.co.uk/

**▸ 组织：Linux Community**（1 patches）

**[SERIES] iommu/riscv: Enable MSI remapping and IOMMU_DMA** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-10-22
- 状态：社区讨论中
- 作者邮箱：Andrew Jones <andrew.jones@linux.dev>
- 概括：为 64 位 RISC-V 的 IMSIC 中断控制器增加消息中断目标地址列表支持，收集所有可能 CPU 的中断页物理地址，提供接口在首次调用时把它们映射到一个连续 I/O 虚拟地址范围并缓存基址，使中断亲和性变化时可在原子上下文中按逻辑 CPU 位置直接选择目标；同时开启 64 位 RISC-V 上的设备 DMA 地址映射支持，使内核 DMA 映射路径可用于该平台。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/dma: Prepare MSI physical address lists
  - iommu/dma: Enable IOMMU_DMA for 64-bit RISC-V
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20261022154603.1374754-2-andrew.jones@linux.dev/

**▸ 组织：Individual Contributor**（1 patches）

**[SERIES] iommu/riscv: Keep page table pages when IOTLB invalidation fails** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-10-20
- 状态：社区讨论中
- 作者邮箱：Yuho Choi <oss.patchbox@gmail.com>
- 概括：修复RISC-V IOMMU在IOTLB失效命令未能确认完成时仍释放页表页，使IOMMU可能继续使用缓存指向已释放页，后续写入被当作页表项遍历；现在命令发送与同步返回错误，未确认失效时保留页面并一次性告警，同时将命令队列停滞报错而非视为完成，避免误释放。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/riscv: Do not report a stalled command queue as completed
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20261020053435.1179054-5-oss.patchbox@gmail.com/

---

### ◆ 子系统：Intel VT-d（6 patches）

**▸ 组织：Intel**（4 patches）

**[SERIES] intel_iommu: Enable PRQ support for passthrough device** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-10-20
- 状态：社区讨论中
- 作者邮箱：Duan, Zhenzhong <zhenzhong.duan@intel.com>
- 概括：为 Intel 输入输出内存管理单元的直通设备新增页请求队列支持：客户机启用后，主机侧可恢复故障事件被接收并注入客户机，客户机的响应也能写回主机；客户机侧溢出或满错误时，低优先级页请求按丢弃后返回成功响应，其他错误返回无效请求。故障队列资源释放被推迟到底半部执行，避免因轮询尚未退出、文件仍持有引用而导致释放返回忙错误。
- 达到阈值的 patches（4 个，显示前 5）：
  - intel_iommu_accel: Add PRQ injection for passthrough device
  - intel_iommu_accel: Guard VTDAccelPASIDCacheEntry definition
  - intel_iommu_accel: Accept PRQ response for passthrough device
  - intel_iommu_accel: Teardown FAULTQ resources in bottom half
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20261020091955.1607161-5-zhenzhong.duan@intel.com/

**[v2,3/4] iommu/vt-d: Add an API for tdx-host when enabling trusted DMA**

- 日期：2026-10-15
- 状态：社区讨论中
- 作者邮箱：Baolu Lu <baolu.lu@linux.intel.com>
- 概括：为 Intel VT-d 驱动新增与 TDX 主机模块配合的接口，用于启用可信 DMA。初始化遍历支持可信 DMA 扩展的输入输出内存管理单元，先检查地址翻译、队列失效和可扩展模式等前提，避免之后再报出晦涩状态；再把域标识符空间限制到低半段，回调主机模块完成安全模式切换，失败时恢复并上报，成功后标记。处于安全模式的单元禁止热移除，因为 TDX 模块仍持有其资源。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261015010705.1973284-4-baolu.lu@linux.intel.com/

**[v8,6/6] intel_iommu_accel: teardown FAULTQ resources in bottom half**

- 日期：2026-10-09
- 状态：社区讨论中
- 作者邮箱：Duan, Zhenzhong <zhenzhong.duan@intel.com>
- 概括：在 Intel 输入输出内存管理单元直通设备中，当地址空间标识条目失效时，原先释放故障队列会立即关闭处理函数并释放队列编号，但存在一个窗口：轮询尚未退出时文件仍持有队列引用，可能使释放返回忙错误。现改为把故障队列及关联文件、队列编号的释放推迟到下半部回调执行，确保轮询退出并放下引用后再清理。
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20261009090737.3930000-7-zhenzhong.duan@intel.com/

**[SERIES] iommu/vt-d: Introduce trusted DMA initialization support** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-09-15
- 状态：社区讨论中
- 作者邮箱：Baolu Lu <baolu.lu@linux.intel.com>
- 概括：为 Intel TDX Connect 主机引入可信 DMA 初始化路径。检测支持扩展的 VT-d IOMMU，分配失效队列和元数据页后通过 TDX 模块将其切入安全模式，使 DMA 翻译和失效资源由 TDX 管理；同时将域 ID 高半区保留给 TDX 模块，宿主只使用低半区，并在切换前检查高半区无已分配域。不支持或返回无效操作数的 IOMMU 跳过，其他失败则回滚已初始化单元，适用于需要将设备可信分配给 TDX 客户机的场景。
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu/vt-d: Add interfaces for trusted DMA initialization
  - iommu/vt-d: Add helpers to set up and tear down TDX extensions
  - iommu/vt-d: Reserve MSB of domain ID space for TDX module
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260915074235.1219183-4-baolu.lu@linux.intel.com/

**▸ 组织：Red Hat**（1 patches）

**[SERIES] virtio: fix exit(1) on DMA mapping failure during migration restore** （cover letter，5/7 个 patch 达到代码量阈值）

- 日期：2026-09-11
- 状态：社区讨论中
- 作者邮箱：Michael S. Tsirkin <mst@redhat.com>
- 概括：修复 QEMU 的 virtio 迁移恢复路径：直接内存访问地址损坏导致映射失败时不再直接退出，改为清理并返回错误；配置长度恶意值不再造成 CPU 长时间空转，已启用队列的重复启用被拒绝。调整 Intel/AMD IOMMU 模拟，支持并发页故障与页请求接口，写页表时一次写入全部标志并仅在有写权限时标脏，移除 AMD 未实现的页请求和硬件错误扩展特性。
- 达到阈值的 patches（5 个，显示前 5）：
  - intel_iommu: Support concurrent page fault handling with PRI
  - intel_iommu: Always write all the flags passed to vtd_set_flag_in_pte
  - intel_iommu: Only set dirty bit when PTE exposes write permission
  - intel_iommu: Expose SMPWC when SVM is enabled
  - amd_iommu: Return empty efr for stub call
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/f19df1b13d1a0b5601b4b58067b8c2e91ae76ef3.1789117222.git.mst@redhat.com/

**▸ 组织：Google**（1 patches）

**[SERIES] iommu: Add live update state preservation** （cover letter，17/17 个 patch 达到代码量阈值）

- 日期：2026-10-25
- 状态：社区讨论中
- 作者邮箱：Samiullah Khawaja <skhawaja@google.com>
- 概括：新增 IOMMU live update 状态保存：在 kexec 切换内核时保留 iommufd 硬件页表、域和 VT-d 根表/上下文表/PASID 表等设备与 IOMMU 状态，新内核启动后恢复并重新附加到设备，同时标记页表为不可变以禁止映射变化。适用于需要内核更新期间不中断设备 DMA 的 live update 场景，当前由 VT-d 驱动实现。
- 达到阈值的 patches（17 个，显示前 5）：
  - iommu: Implement IOMMU Live update FLB callbacks
  - iommu/pages: Add APIs to preserve/unpreserve/restore iommu pages
  - iommupt: Implement preserve/unpreserve/restore callbacks
  - iommu/vt-d: Clear unpreserved context entries during shutdown
  - iommu: Add APIs to get iommu and device preserved state
  - ... 及其他 12 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261025021930.674647-2-skhawaja@google.com/

---

### ◆ 子系统：AMD IOMMU（5 patches）

**▸ 组织：AMD**（3 patches）

**[SERIES] Add support for AMD IOMMU GAPPI** （cover letter，4/5 个 patch 达到代码量阈值）

- 日期：2026-10-22
- 状态：社区讨论中
- 作者邮箱：Sairaj Kodilkar <sarunkod@amd.com>
- 概括：为AMD IOMMU新增GAPPI宿主唤醒通知机制，在AVIC模式下设备中断到达未运行vCPU时，由IOMMU按中断重映射条目中的目标字段向指定主机CPU直接发送物理APIC中断并携带唤醒向量，替代GA log唤醒KVM调度该vCPU；KVM将阻塞vCPU排到最近运行的CPU，未启用GAPPI时回退到原GA log路径。
- 达到阈值的 patches（4 个，显示前 5）：
  - iommu/amd: KVM: SVM: Rename cpu to apicid in IOMMU interface
  - iommu/amd: KVM: SVM: Rename ga_log_intr to wakeup_intr in IOMMU interface
  - iommu/amd: Program guest-mode IRTEs for GAPPI wakeup when IRTE[IsRun] = 0
  - iommu/amd: Provide kernel command line option to enable GAPPI
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261022140425.27465-2-sarunkod@amd.com/

**[SERIES] amd_iommu: Allow IOMMU to attach on non system bus** （cover letter，2/5 个 patch 达到代码量阈值）

- 日期：2026-10-14
- 状态：社区讨论中
- 作者邮箱：Sairaj Kodilkar <sarunkod@amd.com>
- 概括：允许AMD IOMMU连接到非系统总线（如扩展根端口），并以向上遍历得到的第一个根总线为边界只服务其下设备，从而隔离PCI子树；同时KVM按设备查找实际服务的IOMMU进行中断重映射，修复此前固定使用默认系统IOMMU导致设备不在范围内时中断重映射表项未编程的问题，并修正在禁用中断重映射时IOAPIC仍被分配IOMMU地址空间的问题。
- 达到阈值的 patches（2 个，显示前 5）：
  - amd_iommu: Assign ioapic_as only when interrupt remapping is supported.
  - amd_iommu: Allow IOMMU to attachment on non-system (pcie.0) bus
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20261014053433.24564-2-sarunkod@amd.com/

**[SERIES] iommu/amd: Implement live update state preservation** （cover letter，5/6 个 patch 达到代码量阈值）

- 日期：2026-10-05
- 状态：社区讨论中
- 作者邮箱：Ankit Soni <Ankit.Soni@amd.com>
- 概括：为 AMD 输入输出内存管理单元增加热升级状态保存与恢复，解决非崩溃转储启动中设备附加被错误延迟导致无法 DMA 的问题，并提前解析交接状态。升级关闭时阻止未保留设备并等待命令、事件等引擎空闲，随后保存设备表、域标识和 PASID 地址翻译表；新内核接管这些状态，继续让保留设备翻译，未保留设备则被阻断。
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
- 概括：整理 AMD IOMMU 设备探测和 ATS 初始化路径。移除探测失败时清空设备表项和反向查找表的旧处理，因为正常启动时表项本就未配置，而 kdump 启动中这样清表可能破坏尚在使用的翻译和中断重映射，且直接写表缺乏缓存刷新。现在 ATS 能力初始化失败会使设备探测失败，PCI ATS 准备接口也要求调用者先确认设备支持 ATS，不再静默忽略不支持设备。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/amd: Refactor device probe and capability initialization
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/20260910142655.3281464-2-praan@google.com/

**▸ 组织：Oracle**（1 patches）

**[SERIES] amd_iommu: Bugfix and Cleanup for IO Page Fault** （cover letter，5/5 个 patch 达到代码量阈值）

- 日期：2026-10-30
- 状态：社区讨论中
- 作者邮箱：Alejandro Jimenez <alejandro.j.jimenez@oracle.com>
- 概括：修复 QEMU 中 AMD IOMMU 仿真的 IO 页故障报告和寄存器语义：地址空间改用完整总线/设备/功能号，使根端口之后设备产生的页故障能归到正确请求者，不再误报为 00:00.0；初始化时避免重复创建 MSI 能力；将扩展特性寄存器设为只读，让功能位完全由 QEMU 控制；拒绝客户机对未产生的 GA 日志状态位进行写清除时锁存虚假溢出，从而避免客户机反复重启 GA 日志。
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
- 概括：高通 Adreno GPU 的 IOMMU 故障信息回调在无运行时电源管理引用的情况下直接读取 SMMU 寄存器。故障虽在 SMMU 活跃时触发，但 GPU 可能在处理线程到达前撤销电源投票，使 SMMU 运行时挂起；此时访问寄存器不安全，可能使后续恢复运行时出现 NoC 错误和异步 SError。补丁在读取前尝试保持设备活跃，若挂起已经开始则跳过寄存器读取，避免破坏故障现场和触发后续错误。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260912-priv_call_runtime_handlers-v1-1-fc0c3a17523f@oss.qualcomm.com/

**▸ 组织：归属待核实（brar.si）**（1 patches）

**[v2,2/2] iommu/arm-smmu-qcom: Skip PRR setup on SM7250 GPU SMMU**

- 日期：2026-10-23
- 状态：社区讨论中
- 作者邮箱：Ishu Brar <patches@brar.si>
- 概括：针对高通 SM7250 平台的 Adreno GPU SMMU，写入页请求相关寄存器时固件会将设备复位，首次创建每进程 GPU 页表即触发。现按 SM8250 同样方式，在 SM7250 上跳过安装页请求回调，避免设备复位，使 OnePlus Nord 上的 Vulkan 图形工作能正常创建页表。
- 来源：https://patchwork.kernel.org/project/linux-arm-msm/patch/20261023-smmu-sm7250-v2-2-8bb881ce19f5@brar.si/

**▸ 组织：Individual Contributor**（1 patches）

**[SERIES] Enable LPAC on a7xx series GPUs** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-10-29
- 状态：社区讨论中
- 作者邮箱：Anna Maniscalco <anna.maniscalco2000@gmail.com>
- 概括：为高通 Adreno 7xx 系列 GPU 引入低优先级异步计算队列。此前低优先级计算与主图形队列共用 SMMU 域和页表，无法独立更新映射，也不能单独提交任务；系列在 SMMU 中为低优先级设备分配独立上下文和拆分地址空间，通过设备树识别对应节点并配置固件孔径，新增独立环形队列和用户态提交接口，默认在 Adreno 750 上开启，其他目标由模块参数控制。这样低优先级计算可与主队列并行提交，故障时还能转储低优先级环状态。
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
- 概括：32 位 ARM 平台原本强制使用传统 ARM DMA 域，不允许 IOMMU 核心管理的默认 DMA 域；现在为大多数平台启用核心管理的默认 DMA 域，传统 ARM DMA 路径继续保留，部分兼容性尚不足的平台仍使用身份域。Tegra SMMU 对显示控制器保持旁路，直到驱动接管并设置最终域，避免开机扫描时的翻译故障；并按软件组为图形和主机设备启用 DMA 默认域，修复多设备同组探测问题。
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu/tegra-smmu: Defer display client translation to driver handover
  - iommu/tegra-smmu: Use a DMA API default domain per swgroup
  - iommu: Enable DMA default domains on (most) 32-bit ARM platforms
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20261026-b4-arm32-iommu-dma-cookie-v3-1-3901d74b1ff2@nvidia.com/

**[v2,07/11] iommu: Let 32-bit ARM drivers opt into a DMA API default domain**

- 日期：2026-10-16
- 状态：社区讨论中
- 作者邮箱：Mikko Perttunen <mperttunen@nvidia.com>
- 概括：解除 32 位 ARM 平台上对默认域类型的强制身份域覆盖，让 IOMMU 驱动可以通过默认域类型回调自行选择真正的 DMA API 默认域；当通用 DMA 域实现未启用但 ARM DMA API 实现可用时，允许驱动显式请求的 DMA 域通过。普通路径仍不会自动回退到 DMA 域，因此现有 32 位 ARM 驱动在未设置回调或显式返回身份域时行为保持不变。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20261016-b4-arm32-iommu-dma-cookie-v2-7-b06842a01938@nvidia.com/

**▸ 组织：Google**（1 patches）

**[SERIES] DMA_PMD: PMD_SIZE-backed IO buffer pools** （cover letter，12/12 个 patch 达到代码量阈值）

- 日期：2026-10-03
- 状态：社区讨论中
- 作者邮箱：Luigi Rizzo <lrizzo@google.com>
- 概括：为直接内存访问缓冲新增基于 2MB 物理连续大页的分配池，使输入输出内存管理单元能使用大页映射，降低输入输出旁路转换缓冲压力及映射、解映射和刷新开销。池会动态分配回收大页，并用全局上限和收缩器限制空闲内存；域销毁时清理存活映射，确保内存仅在输入输出内存管理单元映射移除并刷新后才归还伙伴分配器。
- 达到阈值的 patches（12 个，显示前 5）：
  - iommu/dma: introduce CONFIG_DMA_PMD and metadata table
  - iommu/dma: add DMA_PMD pool lifecycle and page recycle hook
  - iommu/dma: Global cap and shrinker for DMA_PMD pool memory
  - iommu/dma: add DMA_PMD pool block allocation
  - iommu/dma: reserve a per-domain IOVA window for DMA_PMD pages
  - ... 及其他 7 个 patch
- 来源：https://patchwork.kernel.org/project/linux-mm/patch/20261003212241.3432303-2-lrizzo@google.com/

---

### ◆ 子系统：IOMMU SVA/SVM（2 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[RFC,1/2] iommu: Add iommu_map_sgtable_dma()**

- 日期：2026-10-09
- 状态：社区讨论中
- 作者邮箱：Karl Mehltretter <kmehltretter@gmail.com>
- 概括：新增一个输入输出内存管理 DMA 辅助接口，用于把活动 DMA 映射的底层内存映射到另一个地址域。针对共享缓冲区导入方（如 Rockchip）只有 DMA 地址而现有映射需要 CPU 页的问题，该接口通过设备默认 DMA 域反查物理地址并建立目标映射，出错时回滚已建立的映射。当前仅支持非反弹的 IOMMU DMA 映射，其他 DMA 后端、总线地址和零转换都会返回不支持。
- 来源：https://patchwork.kernel.org/project/linux-rockchip/patch/20261009002114.67851-2-kmehltretter@gmail.com/

**▸ 组织：归属待核实（utexas.edu）**（1 patches）

**iommu/sva: Charge IOPF allocations to the faulting mm's memcg**

- 日期：2026-10-12
- 状态：社区讨论中
- 作者邮箱：Peizhe Liu <peizheliu@utexas.edu>
- 概括：修复设备缺页处理在工作队列中未设置活动内存控制组的问题：此前文件后端缺页产生的页缓存被计入根控制组，逃逸任务的内存上限。现在处理缺页前切换到故障进程所属的内存控制组，完成后恢复原值，使设备触发的页缓存分配正确归属并受内存限制约束。
- 来源：https://patchwork.kernel.org/project/linux-mm/patch/20261012200823.699316-1-peizheliu@utexas.edu/

---

### ◆ 子系统：IOMMU Page Table（1 patches）

**▸ 组织：Qualcomm**（1 patches）

**[v5] iommu/io-pgtable-arm: Add support for contiguous hint bit**

- 日期：2026-09-21
- 状态：社区讨论中
- 作者邮箱：Vijayanand Jitta <vijayanand.jitta@oss.qualcomm.com>
- 概括：为 ARM LPAE 页表引入连续提示位支持：当一组连续页表项映射自然对齐的连续内存块时，在相关页表项上设置连续提示，使硬件合并地址翻译并扩大 TLB 覆盖。支持的连续组大小通过页大小位图通告，调用者按正常页大小选择路径使用；对已标记连续组的部分取消映射在改动任何表项前直接拒绝，避免留下半取消状态。另提供兼容开关，便于有硬件缺陷的 SMMU 驱动关闭该功能。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260921-iommu_contig_hint-v5-1-e7fbd1c3774d@oss.qualcomm.com/

---

### ◆ 子系统：IOMMUPT（1 patches）

**▸ 组织：Google**（1 patches）

**[SERIES] iommupt: Introduce IO page table shrinker** （cover letter，2/5 个 patch 达到代码量阈值）

- 日期：2026-10-01
- 状态：社区讨论中
- 作者邮箱：Pranjal Shrivastava <praan@google.com>
- 概括：在通用页表库中加入内存压力驱动的页表收缩器，用叶条目引用计数识别完全空目录并登记到域的回收列表；收缩器在内存紧张时无锁切断这些空分支，等待宽限期后释放并刷新设备旁路缓存，从而自动回收稀疏解除映射残留的页表目录。映射路径与收缩器竞争失败时返回重试。
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

*报告由 Linux Patches Tracker 自动生成 | 2026-11-11 13:30:54*
