# Linux IOMMU 子系统 Patch 追踪报告

---

## 报告信息

| 项目 | 内容 |
|------|------|
| 数据来源 | patchwork.kernel.org |
| 生成日期 | 2026-09-11 |
| 报告区间 | 2026-07-01 至 2026-08-31 |
| 仓库 | [https://github.com/IAMHCHCH/linux-patches-tracker](https://github.com/IAMHCHCH/linux-patches-tracker) |

---

## 统计概览

### 按状态分类

| 状态 | 数量 | 占比 |
|------|------|------|
| 社区讨论中 | 56 | 93.3% |
| 已合入 | 0 | 0.0% |
| **总计** | **60** | **100%** |

### 按组织分类（TOP 15）

| 组织 | 数量 | 占比 |
|------|------|------|
| NVIDIA | 11 | 18.3% |
| Qualcomm | 8 | 13.3% |
| Google | 7 | 11.7% |
| ByteDance | 3 | 5.0% |
| 归属待核实（gahingwoo.com） | 3 | 5.0% |
| Individual Contributor | 3 | 5.0% |
| AMD | 3 | 5.0% |
| Kernel.org | 2 | 3.3% |
| Bull | 2 | 3.3% |
| Microsoft | 2 | 3.3% |
| Alibaba | 2 | 3.3% |
| Amazon | 1 | 1.7% |
| SiFive | 1 | 1.7% |
| 中国科学院软件研究所 | 1 | 1.7% |
| Linaro | 1 | 1.7% |

### 按子系统分类

| 子系统 | 数量 | 占比 |
|--------|------|------|
| IOMMU Core | 18 | 30.0% |
| ARM SMMUv3 | 14 | 23.3% |
| AMD IOMMU | 7 | 11.7% |
| RISC-V IOMMU | 6 | 10.0% |
| IOMMUFD | 4 | 6.7% |
| ARM SMMU (v1/v2) | 4 | 6.7% |
| Intel VT-d | 3 | 5.0% |
| ARM SMMU Acceleration | 2 | 3.3% |
| IOMMU DMA-API | 1 | 1.7% |
| IOMMU Page Table | 1 | 1.7% |

## 重点 Patch Top20 清单

### 已合入

暂无。

### 社区讨论

| 厂商 | 简介 |
|------|------|
| Google | [PATCH v4 00/18] iommu: Add live update state preservation ------为内核热更新保留设备的 IOMMU 页表、域标识和进程地址空间标识表，在新内核恢复地址转换并重新挂接设备；保留期间禁止修改映射或更换地址空间。已实现底层恢复，但面向用户的 IOMMU 文件接口恢复流程仍待补齐，并附带状态保留测试。 |
| Google | [PATCH v7 00/24] KVM: arm64: SMMUv3 driver for pKVM (trap and emulate) ------为受保护虚拟机场景实现运行在 EL2 的 SMMUv3 驱动，由虚拟机监控程序接管 SMMU 硬件并以陷入模拟方式向宿主内核呈现模拟设备。此前受保护模式下宿主可直接控制 SMMU，无法阻止宿主设备访问虚拟机内存。补丁让监控程序独占 SMMU 的 MMIO 和命令队列，建立影子流表、影子命令队列和影子页表，过滤并转发宿主的失效命令，从而为虚拟机建立 DMA 隔离；宿主内核侧驱动通过辅助总线探测模拟出的 SMMU，其余流程与普通驱动一致。 |
| NVIDIA | [PATCH v10 00/13] iommu/arm-smmu-v3: Adopt the crashed kernel's stream table for kdump ------在崩溃转储内核中保留原内核的地址转换和设备流表，让尚未完成的 DMA 继续使用旧映射，避免复位导致传输中断或绕过隔离而破坏内存；预留旧内核占用的地址空间标识，关闭事件与页请求队列以免错误消息刷屏。旧状态校验失败时仍回退到完整复位。 |
| Qualcomm | [PATCH v1 00/12] iommu: qcom_iommu: implement support for instances on MSM8974 ------为高通 MSM8974 上的 IOMMU 实例增加支持，使该代芯片的显示、Venus 和 GPU 等模块能正常使用 IOMMU。此前驱动只支持 MSM8916 风格实例，MSM8974 的 GPU IOMMU 不受安全世界管理，无人建立流映射，附加域后所有事务都无法匹配，GPU 首次访存即出错；这些实例还位于会掉电的电源域中，掉电后丢失全局和上下文寄存器状态。 |
| Google | [PATCH v9 00/12] iommu/arm-smmu-v3: Implement Runtime/System Sleep ops ------为 arm-smmu-v3 实现运行时电源管理和系统睡眠。挂起时先让 SMMU 中止新事务、关闭主翻译单元并排空命令队列，用停止标志阻止新的命令提交；恢复时还原 MSI 配置并复位设备。还修复了 Tegra241 虚拟命令队列恢复后生产/消费索引归零导致不再消费命令的问题，并补充了运行时电源管理的单元测试。 |
| Qualcomm | [PATCH v5 00/17] iommu/riscv: Enable MSI remapping, IOMMU_DMA and VFIO ------让 64 位 RISC-V 上的 IOMMU 支持 MSI 重映射、DMA 地址映射和 VFIO 设备直通。原先软件 MSI 映射数量受固定上限限制，无法为每个 CPU 建立映射，且缺少保留的 MSI 地址窗口。现在把映射表改为可增长、支持按物理地址列表建立连续映射并原子安装，为每个可能 CPU 预留一页 MSI 地址窗口，报告缓存一致性能力，并开启相关内核配置与自测。 |
| NVIDIA | [PATCH v6 00/5] iommufd: Iterate the cache invalidation array in the core ------把缓存失效请求数组的遍历从各驱动上移到 iommufd 核心，并收紧 Arm SMMUv3 对来宾失效命令的校验。此前每个驱动各自遍历整个数组并自行处理分批，SMMUv3 只校验虚拟机和流标识就把命令原样转发，来宾可设置宿主未打算转发的保留位，使命令被判为非法；转换失败时还会上报尚未真正下发的命令，导致用户空间跳过未执行的失效。 |
| NVIDIA | [PATCH v9 00/12] iommu/arm-smmu-v3: Adopt the crashed kernel's stream table for kdump ------在崩溃转储内核中保留原内核的地址转换和设备流表，让尚未完成的 DMA 继续使用旧映射，避免复位导致传输中断或绕过隔离而破坏内存；预留旧内核占用的地址空间标识，关闭事件与页请求队列以免错误消息刷屏。旧状态校验失败时仍回退到完整复位。 |
| NVIDIA | [PATCH v4 00/8] Organize the SMMUv3 invalidation flow so iommupt can use it ------重整 ARM SMMUv3 的失效流程，为后续接入通用页表失效方案做准备。把失效参数集中到结构体传递，把页粒度从失效描述中移出改为域属性，并预先算好失效命令、在调用链顶端填充描述。范围失效改为按延迟优先，尽量用单条命令覆盖整个区间，仅在检测到半虚拟化环境时才精确失效；同时支持 DS 扩展后 SCALE 上限提高到 39。 |
| Intel | [PATCH v5 00/6] intel_iommu: Enable PRQ support for passthrough device ------为直通设备启用 Intel VT-d 的页请求队列支持。此前客户机在虚拟 IOMMU 中开启页请求时，主机侧可恢复缺页事件无法回传客户机。现在分配故障队列对象并注册事件处理，把主机产生的可恢复缺页转发给客户机，再把客户机的响应写回主机，同时缓存每个故障组的标识；PASID 条目失效时在底半部释放故障队列资源，避免文件引用未释放导致释放失败。 |
| Oracle | [PATCH v2 00/5] amd_iommu: Do not create duplicate MSI capability ------修复 QEMU 中 AMD 虚拟 IOMMU 的若干问题：设备曾暴露两个 MSI 能力，现只保留一个；页错误日志此前只带设备功能号，位于根端口后的设备会被记成错误请求者，现改用完整总线号；扩展特性寄存器此前允许客户机改写第 4 位，现改为只读；客户机清除状态位时可能误置 GA 日志溢出位并反复重启 GA 日志，现不再锁存这些位。 |
| NVIDIA | [PATCH v9 00/4] iommu/arm-smmu-v3: Tegra264 invalidation workaround ------针对 Tegra264 的 SMMU，TLB 表项在与同一表项的并发访问竞争时可能躲过失效操作而残留。硬件建议的软件规避办法是把每条失效命令连同其同步命令各发两遍，本系列先搭好按需重复发送的基础设施，再按设备树匹配到该芯片时启用；同时向用户态上报这一缺陷，避免客户机自行处理后再被主机重复一遍而变成四次失效。 |
| 归属待核实（gahingwoo.com） | [PATCH v2 00/8] accel/rocket: RK3576 NPU (RKNN) enablement ------为瑞芯微 RK3576 的 NPU 增加上游支持，使其能在 Radxa ROCK 4D 上探测、上电并跑完提交的任务。此前该芯片的 NPU 无法使用：其 IOMMU 位于额外时钟门后，寄存器写入会被丢弃，且固件遗留的页错误会让停流等待超时。补丁让 IOMMU 取用设备树列出的全部时钟、在启用停流前先确认陈旧页错误，并给电源域加上上电稳定延时和复位脉冲；NPU 驱动按芯片区分时钟、复位、电源域和完成中断方式。 |
| Individual Contributor | [PATCH v1 00/4] IOMMU driver improvements for modern Exynos SysMMUs ------让 Exynos 的 IOMMU 驱动适配不实现 BLOCK 模式的新款 SysMMU（如 Exynos8835）。这类硬件写阻塞位不会停止转换，状态寄存器也从不报告已阻塞，导致使能时在页表尚未配置好就开始转换，可能用复位值或过期页表翻译主设备流量，且 TLB 失效因等待阻塞失败而被整体跳过。 |
| EPAM | [v12,08/13] iommu/ipmmu-vmsa: Implement suspend/resume callbacks ------为 R-Car H3 等平台上的 IPMMU 驱动实现系统挂起与恢复。挂起时保存活动的上下文寄存器和微 TLB 配置，恢复时先还原根 IPMMU 的上下文状态，再还原缓存 IPMMU 的微 TLB，避免缓存单元先于根上下文恢复而读到过期或未初始化的上下文状态。 |
| Qualcomm | [v4] iommu/arm-smmu: Use pm_runtime in fault handlers ------在 SMMU 位于电源域的系统上，故障处理函数会访问寄存器，而 Adreno SMMU 在故障风暴时关闭了停顿，SMMU 可能在掉电状态下产生故障，导致未上电的寄存器读取和 NoC 错误。现在故障处理前先获取运行时电源，未激活则忽略故障；挂起前关闭故障上报并同步中断，避免电平触发中断在掉电过程中反复触发。 |
| 归属待核实（gahingwoo.com） | [RFC,4/9] iommu/rockchip: skip orphaned-fault banks in rk_iommu_is_stall_active ------处理瑞芯微 IOMMU 中固件遗留的孤立页错误。启动固件可能在驱动配置分页前让某个 bank 处于页错误激活状态，此时该 bank 既不处于停流状态又已空闲，停流检查会据此把整个 IOMMU 判为未停流，使后续等待停流完成的轮询永远无法通过。补丁识别这种页错误激活但未停流且空闲的状态，在停流检查中跳过这些 bank，因为它们没有在途事务，本身已处于静止。 |
| 归属待核实（gahingwoo.com） | [RFC,5/9] iommu/rockchip: skip orphaned-fault banks in CMD_ENABLE_STALL dispatch ------处理瑞芯微 IOMMU 中向孤立页错误 bank 发送停流命令的问题。带有固件遗留页错误的 bank 会静默丢弃停流命令，而该命令在共享总线上还会拖慢其他 bank 进入停流状态，使其超出轮询超时。补丁在派发停流命令时跳过这类页错误激活但未停流且空闲的 bank，与停流检查中使用的跳过条件保持一致。 |
| NVIDIA | [v5,1/6] iommu/arm-smmu-v3: Support IDR5.DS and widen the TLBI SCALE field ------为支持扩展失效范围的 SMMU 增加识别：这类硬件把范围失效命令的规模字段从 5 位扩展到 6 位，最大值由 31 提高到 39，并允许 16KB 页粒度下的一种层级提示。驱动新增对应特性位并加宽该字段，但范围失效路径仍按原来的 5 位截断发出命令，行为不变；同时把该特性列入向用户态报告的硬件信息字段，便于虚拟机监视器判断能否透传给客户机。 |
| Qualcomm | [v4] iommu/io-pgtable-arm: Add support for contiguous hint bit ------为 ARM LPAE 页表增加连续提示位支持：当一组连续页表项映射自然对齐的连续内存时，硬件可将其合并为单个 TLB 项，减少 TLB 占用。各页粒度对应的连续块大小会通过页大小位图上报，便于调用方按这些大小对齐分配；对连续组的局部解映射会被拒绝，保证整组一起失效。硬件存在相关缺陷时，驱动可通过一个禁用标志在运行时关闭该特性。 |

---

## 已合入 Patches

暂无。

## 社区讨论中 Patches

### ◆ 子系统：IOMMU Core（16 patches）

**▸ 组织：Qualcomm**（3 patches）

**[SERIES] Fix GPU and display on ARM32 platforms using the MSM IOMMU** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-07-30
- 状态：社区讨论中
- 作者邮箱：Dmitry Baryshkov <dmitry.baryshkov@oss.qualcomm.com>
- 概括：修复 ARM32 上使用高通 MSM IOMMU 的 GPU 和显示无法工作的问题。此前一个设备跨多个 IOMMU 时，主设备记录会错乱并可能空指针崩溃；页表还通过被附加设备的 DMA 配置分配，在 ARM32 上会经它描述的 IOMMU 反复映射自身，导致释放时崩溃。现在按设备和 IOMMU 分别跟踪主设备，改用 IOMMU 设备分配页表，并在附加自有域前先解除架构层的 DMA 映射。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/msm: track a context master per device and IOMMU
  - iommu/msm: use the IOMMU device for page table allocation
- 来源：https://patchwork.kernel.org/project/linux-rockchip/patch/20260730-fix-qcom-smmu-v2-1-18e0daf2d836@oss.qualcomm.com/

**[3/8] iommu/fsl: use platform_device_set_fwnode()**

- 日期：2026-07-20
- 状态：社区讨论中
- 作者邮箱：Bartosz Golaszewski <bartosz.golaszewski@oss.qualcomm.com>
- 概括：在飞思卡尔 PAMU IOMMU 初始化中，把为动态分配平台设备设置设备树节点的方式从仅针对设备树的接口改为更通用的固件节点接口，行为不变，只是改用更高层的封装。
- 来源：https://patchwork.kernel.org/project/alsa-devel/patch/20260720-pdev-set-fwnode-instead-of-of-node-v1-3-2dee93f42c54@oss.qualcomm.com/

**[v3,09/20] iommu/fsl: use platform_device_set_of_node()**

- 日期：2026-07-06
- 状态：社区讨论中
- 作者邮箱：Bartosz Golaszewski <bartosz.golaszewski@oss.qualcomm.com>
- 概括：在飞思卡尔 PAMU IOMMU 初始化中，把动态分配平台设备时设置设备树节点的方式改为使用封装好的辅助接口，并借助自动清理机制管理节点引用，使驱动注册失败等错误路径不再需要手工释放节点引用，简化了初始化流程。
- 来源：https://patchwork.kernel.org/project/dri-devel/patch/20260706-pdev-fwnode-ref-v3-9-1ff028e33779@oss.qualcomm.com/

**▸ 组织：归属待核实（gahingwoo.com）**（3 patches）

**[SERIES] accel/rocket: RK3576 NPU (RKNN) enablement** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-07-18
- 状态：社区讨论中
- 作者邮箱：Jiaxing Hu <gahing@gahingwoo.com>
- 概括：为瑞芯微 RK3576 的 NPU 增加上游支持，使其能在 Radxa ROCK 4D 上探测、上电并跑完提交的任务。此前该芯片的 NPU 无法使用：其 IOMMU 位于额外时钟门后，寄存器写入会被丢弃，且固件遗留的页错误会让停流等待超时。补丁让 IOMMU 取用设备树列出的全部时钟、在启用停流前先确认陈旧页错误，并给电源域加上上电稳定延时和复位脉冲；NPU 驱动按芯片区分时钟、复位、电源域和完成中断方式。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/rockchip: take all DT clocks
  - iommu/rockchip: clear stale page faults before enabling stall
- 来源：https://patchwork.kernel.org/project/linux-rockchip/patch/20260718031146.3368811-5-gahing@gahingwoo.com/

**[RFC,4/9] iommu/rockchip: skip orphaned-fault banks in rk_iommu_is_stall_active**

- 日期：2026-07-17
- 状态：社区讨论中
- 作者邮箱：Jiaxing Hu <gahing@gahingwoo.com>
- 概括：处理瑞芯微 IOMMU 中固件遗留的孤立页错误。启动固件可能在驱动配置分页前让某个 bank 处于页错误激活状态，此时该 bank 既不处于停流状态又已空闲，停流检查会据此把整个 IOMMU 判为未停流，使后续等待停流完成的轮询永远无法通过。补丁识别这种页错误激活但未停流且空闲的状态，在停流检查中跳过这些 bank，因为它们没有在途事务，本身已处于静止。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260717085220.3212274-5-gahing@gahingwoo.com/

**[RFC,5/9] iommu/rockchip: skip orphaned-fault banks in CMD_ENABLE_STALL dispatch**

- 日期：2026-07-17
- 状态：社区讨论中
- 作者邮箱：Jiaxing Hu <gahing@gahingwoo.com>
- 概括：处理瑞芯微 IOMMU 中向孤立页错误 bank 发送停流命令的问题。带有固件遗留页错误的 bank 会静默丢弃停流命令，而该命令在共享总线上还会拖慢其他 bank 进入停流状态，使其超出轮询超时。补丁在派发停流命令时跳过这类页错误激活但未停流且空闲的 bank，与停流检查中使用的跳过条件保持一致。
- 来源：https://patchwork.kernel.org/project/linux-rockchip/patch/20260717085220.3212274-6-gahing@gahingwoo.com/

**▸ 组织：Amazon**（1 patches）

**[RFC,09/14] iommu: lazy-populate iommu_group reserved_regions/type attrs**

- 日期：2026-07-02
- 状态：社区讨论中
- 作者邮箱：Pavol Sakac <sakacpav@amazon.de>
- 概括：把 IOMMU 组的保留区域和类型两个属性文件改为按需创建。它们只在 VFIO 或 iommufd 的查询路径上被读取，而每个 SR-IOV 虚拟功能通常各自拥有一个 IOMMU 组，在虚拟功能数以千计的系统中，启动时会为每个组多建两个内核文件节点。现在改为首次访问时再生成，组名属性仍走原有单独路径，用户态接口不变。
- 来源：https://patchwork.kernel.org/project/kexec/patch/20260702175114.24659-5-sakacpav@amazon.de/

**▸ 组织：中国科学院软件研究所**（1 patches）

**iommu/msm: limit the per-master Machine ID list**

- 日期：2026-07-22
- 状态：社区讨论中
- 作者邮箱：Pengpeng Hou <pengpeng@iscas.ac.cn>
- 概括：高通 MSM IOMMU 在解析设备树中的流 ID 时，会向每个主控对象的固定大小数组追加条目，原先没有容量检查，可能越界写入。现在数组满时返回空间不足错误，不再写出数组边界。
- 来源：https://patchwork.kernel.org/project/linux-arm-msm/patch/20260722041619.17735-1-pengpeng@iscas.ac.cn/

**▸ 组织：归属待核实（jannau.net）**（1 patches）

**[v2,2/2] iommu: apple-dart: Support specifying the DMA aperture in the DT**

- 日期：2026-08-31
- 状态：社区讨论中
- 作者邮箱：Janne Grunau <j@jannau.net>
- 概括：Apple DART 通常只允许设备使用其地址空间的一部分做 DMA，此前无法在设备树中指定这段范围。现在可通过设备树参数给出 DMA 窗口的起始和长度，驱动据此设置域孔径并限制页表映射范围；窗口可以超出 DART 的地址宽度，但不能跨越地址宽度边界或回绕。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260831-iommu-apple-dart-aperture-v2-2-d16ce3770299@jannau.net/

**▸ 组织：EPAM**（1 patches）

**[v12,08/13] iommu/ipmmu-vmsa: Implement suspend/resume callbacks**

- 日期：2026-08-27
- 状态：社区讨论中
- 作者邮箱：Mykola Kvach <mykola_kvach@epam.com>
- 概括：为 R-Car H3 等平台上的 IPMMU 驱动实现系统挂起与恢复。挂起时保存活动的上下文寄存器和微 TLB 配置，恢复时先还原根 IPMMU 的上下文状态，再还原缓存 IPMMU 的微 TLB，避免缓存单元先于根上下文恢复而读到过期或未初始化的上下文状态。
- 来源：https://patchwork.kernel.org/project/xen-devel/patch/1f036e7ad5ad6efba635ca029b0fab133300603a.1787838455.git.mykola_kvach@epam.com/

**▸ 组织：归属待核实（reactivated.net）**（1 patches）

**[SERIES] Add support for Broadcom BCM2712 IOMMU driver (Raspberry Pi 5)** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-25
- 状态：社区讨论中
- 作者邮箱：Daniel Drake <dan@reactivated.net>
- 概括：为树莓派 5 所用的博通 BCM2712 芯片新增 IOMMU 驱动，让显示流水线和多媒体设备的内存访问能经 IOMMU 转换。此前该芯片没有上游驱动，相关设备无法使用 IOMMU。驱动采用两级页表格式，并处理全芯片共享的二级 TLB，在修改或解除映射时刷新它；同时补充设备树节点，使图形显示模块启用 IOMMU。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/generic_pt: Add Broadcom BCM2712 page table format
  - iommu: Add Broadcom BCM2712 IOMMU driver
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260825-bcm2712-iommu-submit-v3-3-7f143e7289b6@reactivated.net/

**▸ 组织：ByteDance**（1 patches）

**[SERIES] riscv: iommu: Add QoS ID support for resctrl device assignment** （cover letter，3/4 个 patch 达到代码量阈值）

- 日期：2026-07-14
- 状态：社区讨论中
- 作者邮箱：Zhanpeng Zhang <zhangzhanpeng.jasper@bytedance.com>
- 概括：为 RISC-V IOMMU 增加服务质量标识支持，让 resctrl 能把设备组分配到资源组并据此设置 RCID 和 MCID。此前 resctrl 只能管理任务，无法把外部设备请求方纳入资源控制。新增设备分配接口和每 IOMMU 全局标识的 sysfs 属性，分配前会校验所有成员，校验失败则不改动硬件。
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu: Add group lookup by ID
  - iommu/riscv: Program QoS IDs for assigned groups
  - iommu/riscv: Expose global QoS IDs in sysfs
- 来源：https://patchwork.kernel.org/project/linux-kselftest/patch/20260714130657.46963-2-zhangzhanpeng.jasper@bytedance.com/

**▸ 组织：Google**（1 patches）

**[SERIES] iommu: Add live update state preservation** （cover letter，16/16 个 patch 达到代码量阈值）

- 日期：2026-08-08
- 状态：社区讨论中
- 作者邮箱：Samiullah Khawaja <skhawaja@google.com>
- 概括：为内核热更新保留设备的 IOMMU 页表、域标识和进程地址空间标识表，在新内核恢复地址转换并重新挂接设备；保留期间禁止修改映射或更换地址空间。已实现底层恢复，但面向用户的 IOMMU 文件接口恢复流程仍待补齐，并附带状态保留测试。
- 达到阈值的 patches（16 个，显示前 5）：
  - iommu: Implement IOMMU Live update FLB callbacks
  - iommu/pages: Add APIs to preserve/unpreserve/restore iommu pages
  - iommupt: Implement preserve/unpreserve/restore callbacks
  - iommu: Implement IOMMU domain preservation
  - iommu: Implement device and IOMMU HW preservation
  - ... 及其他 11 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260808022723.3893618-3-skhawaja@google.com/

**▸ 组织：归属待核实（surriel.com）**（1 patches）

**[SERIES] iommu/iova: convert from rbtree to maple tree** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-08-18
- 状态：社区讨论中
- 作者邮箱：Rik van Riel <riel@surriel.com>
- 概括：把 IOMMU 的 IOVA 分配器从红黑树改为 maple tree，解决生产环境中多 CPU 同时线性遍历红黑树寻找空闲区间导致软锁死的问题，空闲区间查找变为对数复杂度；由于在原子上下文释放 IOVA 时树重平衡可能分配失败，改为先标记该区间再延后重试擦除，并新增 KUnit 测试覆盖对齐分配、碎片化空间和随机压力等场景。
- 达到阈值的 patches（3 个，显示前 5）：
  - iommu/iova: defer maple tree erase on GFP_ATOMIC failure
  - iommu/iova: convert from rbtree to maple tree
  - iommu/iova: add KUnit test suite
- 来源：https://patchwork.kernel.org/project/linux-mm/patch/20260818152505.1057922-3-riel@surriel.com/

**▸ 组织：Individual Contributor**（1 patches）

**[SERIES] IOMMU driver improvements for modern Exynos SysMMUs** （cover letter，2/4 个 patch 达到代码量阈值）

- 日期：2026-08-20
- 状态：社区讨论中
- 作者邮箱：Markuss Broks <markuss.broks@gmail.com>
- 概括：针对 Exynos8835 等不实现 BLOCK 模式的新款系统 MMU，原先使能时先写带使能位的阻塞寄存器，会在页表基址尚未配置好时就开始翻译，导致主设备事务被错误翻译；现在这类硬件保持关闭直到配置完成再一次性使能，TLB 失效不再等待阻塞状态而是直接写入失效寄存器，并在 v7 及以上故障报告中保留事务信息以区分同一主设备内多个 DMA 引擎。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/exynos: detect SysMMUs without BLOCK mode
  - iommu/exynos: decode the v7 fault transaction info
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260820-exynos-iommu-fixes-v1-1-6bbcd673bb15@gmail.com/

**▸ 组织：Rockchip**（1 patches）

**[SERIES] iommu/rockchip: turn rk_iommu_ops into data** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-25
- 状态：社区讨论中
- 作者邮箱：Simon Xue <xxm@rock-chips.com>
- 概括：针对 Rockchip IOMMU，原先各版本通过回调函数分别处理页表地址和表项编码，现改为按物理地址掩码在运行时选择布局，使版本操作结构只保留数据；同时新增检查，当地址超出硬件可寻址范围时直接拒绝映射，避免高位被静默截断而把设备指向错误页面。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/rockchip: Reject unsupported physical addresses
  - iommu/rockchip: Reduce rk_iommu_ops to pure data
- 来源：https://patchwork.kernel.org/project/linux-rockchip/patch/20260825092132.154150-3-xxm@rock-chips.com/

---

### ◆ 子系统：ARM SMMUv3（14 patches）

**▸ 组织：NVIDIA**（7 patches）

**[SERIES] iommu/arm-smmu-v3: Adopt the crashed kernel's stream table for kdump** （cover letter，10/13 个 patch 达到代码量阈值）

- 日期：2026-08-30
- 状态：社区讨论中
- 作者邮箱：Nicolin Chen <nicolinc@nvidia.com>
- 概括：让 kdump 内核接管崩溃内核的流表：崩溃时设备可能仍在 DMA，常规复位会中止在途传输或让其绕过 SMMU 破坏内存。现在保留 SMMU 使能位、不重写流表基址，改为映射并校验崩溃内核的流表和上下文描述符表，预留其中在用的地址空间标识，跳过保留内存区域旁路改写，并关闭事件队列和页请求队列，使在途 DMA 能继续按旧页表完成后再由驱动接管。
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
- 作者邮箱：Jason Gunthorpe <jgg@nvidia.com>
- 概括：让 ARM SMMUv3 改用通用 IOMMU 页表实现，替换原有的 io-pgtable-arm：新增 ARMv8 64 位页表格式，支持连续页、多级叶页、可变顶层、脏位跟踪和软件位，并补齐脏位回写与 IOMMU 专用接口。切换后失效改为通过收集器直接下发，取消单独的刷新回调，同时移除顶层项数校验和收集结构中的页大小字段。
- 达到阈值的 patches（5 个，显示前 5）：
  - iommu/arm-smmu-v3: Move the DMA API comment to flush_iotlb_all
  - iommu/arm-smmu-v3: Use the generic iommu page table
  - iommupt/armv8: Add DBM support
  - iommupt/armv8: Implement the iommu specific components
  - iommupt/armv8: Add the 64 bit ARMv8 page table format
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/1-v2-563ee63886f0+1209-iommupt_armv8_jgg@nvidia.com/

**[SERIES] Organize the SMMUv3 invalidation flow so iommupt can use it** （cover letter，8/8 个 patch 达到代码量阈值）

- 日期：2026-08-05
- 状态：社区讨论中
- 作者邮箱：Jason Gunthorpe <jgg@nvidia.com>
- 概括：重整 ARM SMMUv3 的失效流程，为后续接入通用页表失效方案做准备。把失效参数集中到结构体传递，把页粒度从失效描述中移出改为域属性，并预先算好失效命令、在调用链顶端填充描述。范围失效改为按延迟优先，尽量用单条命令覆盖整个区间，仅在检测到半虚拟化环境时才精确失效；同时支持 DS 扩展后 SCALE 上限提高到 39。
- 达到阈值的 patches（8 个，显示前 5）：
  - iommu/arm-smmu-v3: Keep track in the arm_smmu_invs if RIL is used
  - iommu/arm-smmu-v3: Precompute the invalidation commands
  - iommu/arm-smmu-v3: Support the DS expansion of RIL's SCALE
  - iommu/arm-smmu-v3: Populate the tlbi at the top of the call chain
  - iommu/arm-smmu-v3: Pass the parameters for the invalidation in a struct
  - ... 及其他 3 个 patch
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/4-v4-1802653d8886+492-smmu_tlbi_jgg@nvidia.com/

**[v5,1/6] iommu/arm-smmu-v3: Support IDR5.DS and widen the TLBI SCALE field**

- 日期：2026-07-28
- 状态：社区讨论中
- 作者邮箱：Nicolin Chen <nicolinc@nvidia.com>
- 概括：为支持扩展失效范围的 SMMU 增加识别：这类硬件把范围失效命令的规模字段从 5 位扩展到 6 位，最大值由 31 提高到 39，并允许 16KB 页粒度下的一种层级提示。驱动新增对应特性位并加宽该字段，但范围失效路径仍按原来的 5 位截断发出命令，行为不变；同时把该特性列入向用户态报告的硬件信息字段，便于虚拟机监视器判断能否透传给客户机。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/1b35fa8c417a21ac80a4a3f19db34d81ef6ca490.1785258826.git.nicolinc@nvidia.com/

**[SERIES] iommu/arm-smmu-v3: Tegra264 invalidation workaround** （cover letter，2/4 个 patch 达到代码量阈值）

- 日期：2026-07-26
- 状态：社区讨论中
- 作者邮箱：Ashish Mhetre <amhetre@nvidia.com>
- 概括：针对 Tegra264 的 SMMU 勘误：TLB 表项在并发访问下可能躲过失效操作，硬件建议每条失效命令连同同步命令执行两遍。现在新增重复执行机制，仅对失效类命令生效、不重复地址转换缓存命令，并在设备树匹配到该芯片时启用；同时向用户空间报告该勘误，使客户机自行处理失效时主机不再重复执行，避免同一失效被执行四次。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/arm-smmu-v3: Enable CFGI/TLBI-repeat workaround on Tegra264
  - iommu/arm-smmu-v3-iommufd: Report CFGI/TLBI-repeat erratum
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260726081904.1408859-2-amhetre@nvidia.com/

**[3/7] iommupt: Add the 64 bit ARMv8 page table format**

- 日期：2026-07-06
- 状态：社区讨论中
- 作者邮箱：Jason Gunthorpe <jgg@nvidia.com>
- 概括：为通用 IOMMU 页表框架新增 64 位 ARMv8 页表格式支持，覆盖连续页、多级叶页、可变顶层、脏页跟踪等特性，并实现 LPA、LVA、LPA2 等可选能力，在驱动实际需要前默认不编译；同时用与旧实现对比的测试验证各级页表结果一致。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/3-v1-807e2d1a5efb+e1-iommupt_armv8_jgg@nvidia.com/

**[SERIES] iommu/arm-smmu-v3: Quarantine device upon ATC invalidation timeout** （cover letter，4/12 个 patch 达到代码量阈值）

- 日期：2026-07-03
- 状态：社区讨论中
- 作者邮箱：Nicolin Chen <nicolinc@nvidia.com>
- 概括：这组补丁处理 ARM SMMUv3 在地址转换缓存失效超时后的设备隔离：重置探测不再无故挂起 IOMMU，重置失败时设备保持阻断而不恢复地址转换，避免残留缓存项造成内存破坏；同时修复流表节点误删、服务失败模式下继续处理其他错误、命令队列错误与同步超时的记录，并让超时命令能定位到对应设备以便隔离。
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
- 作者邮箱：Mostafa Saleh <smostafa@google.com>
- 概括：修复 Sashiko 报告的 ARM SMMUv3 问题：在写 L1 表指针前增加内存屏障，避免硬件先看到已分配但未写入描述符的表而读到随机数据；重复 StreamID 的节点初始化为空节点并在擦除前检查，防止红黑树被破坏；修正 VIOMMU 批量失效命令失败时返回给用户的已处理条目数；并修复单元测试中回调误用、缺少错误检查、越界读取和未设置数组计数导致的未定义行为报错。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommu/arm-smmu-v3: Ensure L2 tables are visible before L1 ptrs
  - iommu/arm-smmu-v3: Prevent rbtree corruption from duplicate streams
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260828125409.1921538-4-smostafa@google.com/

**iommu/arm-smmu-v3: Convert to use atomic poll timeout**

- 日期：2026-07-28
- 状态：社区讨论中
- 作者邮箱：Pranjal Shrivastava <praan@google.com>
- 概括：ARM SMMUv3 在发生全局错误进入服务失败模式时，会在硬中断上下文里关闭设备，而关闭流程中的寄存器同步等待可能睡眠，存在在硬中断中睡眠的问题。现改用不睡眠的原子轮询等待，使该路径在中断上下文中可以安全完成。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260728211123.1059708-1-praan@google.com/

**[SERIES] iommu/arm-smmu-v3: Implement Runtime/System Sleep ops** （cover letter，7/12 个 patch 达到代码量阈值）

- 日期：2026-07-28
- 状态：社区讨论中
- 作者邮箱：Pranjal Shrivastava <praan@google.com>
- 概括：为 ARM SMMUv3 实现运行时和系统休眠支持，使 SMMU 在空闲时可断电。挂起前先停止接受新命令并排空命令队列，处理待上报的全局错误，缓存并恢复 MSI 配置；恢复时重置设备并还原队列状态。对英伟达 Tegra241 的虚拟命令队列也做排空和状态恢复，并补充单元测试验证挂起期间的失效命令被正确省略。
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
- 作者邮箱：Mostafa Saleh <smostafa@google.com>
- 概括：为受保护虚拟机场景实现运行在 EL2 的 SMMUv3 驱动，由虚拟机监控程序接管 SMMU 硬件并以陷入模拟方式向宿主内核呈现模拟设备。此前受保护模式下宿主可直接控制 SMMU，无法阻止宿主设备访问虚拟机内存。补丁让监控程序独占 SMMU 的 MMIO 和命令队列，建立影子流表、影子命令队列和影子页表，过滤并转发宿主的失效命令，从而为虚拟机建立 DMA 隔离；宿主内核侧驱动通过辅助总线探测模拟出的 SMMU，其余流程与普通驱动一致。
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
- 作者邮箱：Kiryl Shutsemau <kas@kernel.org>
- 概括：在 kdump 捕获内核中把 ARM SMMUv3 的命令、事件和 PRI 队列都缩小到单页。这些队列原本按硬件上报的最大值分配，每个实例可达数兆字节，在 SMMU 实例较多的系统上会占用数十兆一致性 DMA 内存，而捕获内核只驱动少数设备保存转储，深队列没有意义。缩小后命令队列仍能容纳至少一个批次加一次同步，命令批处理不受影响，转储吞吐也不受影响。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260706084708.8072-1-kas@kernel.org/

**▸ 组织：Linaro**（1 patches）

**[2/2] iommu/arm-smmu-v3: Override for Inst/Data attribute**

- 日期：2026-07-24
- 状态：社区讨论中
- 作者邮箱：Peter Griffin <peter.griffin@linaro.org>
- 概括：在 ARM SMMUv3 上新增设备树属性，可把进入 SMMU 的流量统一按数据访问处理，覆盖原本的指令/数据属性。该选项写入所有流表项，若硬件不支持相应覆盖能力则探测失败并报错，适用于需要强制数据属性的平台。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260724-arm-smmu-v3-instcfg-override-v1-2-e7acf4a8a525@linaro.org/

**▸ 组织：Nebius**（1 patches）

**[RFC] iommu/arm-smmu-v3: Allow nested attach for PCI bridges without vDEVICE**

- 日期：2026-08-14
- 状态：社区讨论中
- 作者邮箱：Dmitry Malkin <dma@nebius.com>
- 概括：在 ARM SMMUv3 上，把直通设备及其宿主 PCI 桥一起做嵌套域附加时，由于桥没有对应的虚拟设备关联，整组附加会失败，导致 VFIO 设备无法附加到用户态 IOMMU。现在允许没有虚拟设备关联的 PCI 桥跳过该要求完成附加，端点设备仍必须提供虚拟设备关联，以保留虚拟流标识处理。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/PA1P190MB25578C482C8A3B06A4DCC6FDDBDA2@PA1P190MB2557.EURP190.PROD.OUTLOOK.COM/

---

### ◆ 子系统：AMD IOMMU（7 patches）

**▸ 组织：AMD**（3 patches）

**[v2] iommu/amd: Force identity mode for selected GPUs only**

- 日期：2026-08-24
- 状态：社区讨论中
- 作者邮箱：Vasant Hegde <vasant.hegde@amd.com>
- 概括：AMD 平台此前用 PASID 能力判断哪些设备必须走 IOMMU 直通模式，结果把所有支持 PASID 的设备都强制直通，范围过宽。现在改为只对 APU 中直连的 AMD 显示类 GPU 强制直通，其余支持 PASID 的设备在 DMA 转换模式下使用客户机页表，不支持 PASID 的设备使用主机页表；内存加密开启时这些 GPU 仍走重映射。
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/20260824085821.5422-1-vasant.hegde@amd.com/

**[SERIES] Add support for AMD IOMMU GAPPI** （cover letter，4/5 个 patch 达到代码量阈值）

- 日期：2026-08-21
- 状态：社区讨论中
- 作者邮箱：Sairaj Kodilkar <sarunkod@amd.com>
- 概括：为 AMD IOMMU 增加 GAPPI 唤醒机制：此前非运行状态 vCPU 的设备中断靠 GA 日志通知主机，现在可在支持该特性的硬件上改用物理 APIC 中断直接通知主机，同时仍更新客户机虚拟 APIC。为此把接口中的 CPU 字段改名为 APIC ID、把 GA 日志标志改名为唤醒标志，并显式传入 vCPU 运行状态；该功能默认关闭，需内核参数启用，未启用时回退到原有 GA 日志路径。
- 达到阈值的 patches（4 个，显示前 5）：
  - iommu/amd: Provide kernel command line option to enable GAPPI
  - iommu/amd: KVM: SVM: Rename cpu to apicid in IOMMU interface
  - iommu/amd: KVM: SVM: Rename ga_log_intr to wakeup_intr in IOMMU interface
  - iommu/amd: Program guest-mode IRTEs for GAPPI wakeup when IRTE[IsRun] = 0
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260821055611.27138-8-sarunkod@amd.com/

**[SERIES] acpi_build: Refactor and cleanup AMD IVRS build** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-08-07
- 状态：社区讨论中
- 作者邮箱：Sairaj Kodilkar <sarunkod@amd.com>
- 概括：整理 AMD IOMMU 的 ACPI 表构建：此前 IVRS 中的设备标识只用设备号和功能号，IOMMU 挂在非零总线时会写错；特性报告硬编码且缺少地址转换相关位，还向客户机公布了硬件并不支持的预取和硬件错误特性。现在用扩展特性寄存器生成报告，按实际能力更新地址宽度，并去掉不支持的特性。
- 达到阈值的 patches（1 个，显示前 5）：
  - amd_iommu: Return empty efr for stub call
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260807061250.27739-2-sarunkod@amd.com/

**▸ 组织：Individual Contributor**（1 patches）

**[1/2] amd_iommu: Honor DTE[IR] and DTE[IW] when DTE[Mode] is 0**

- 日期：2026-07-18
- 状态：社区讨论中
- 作者邮箱：Daniel Paziyski <danielpaziyski@gmail.com>
- 概括：AMD IOMMU 模拟在设备表项有效且模式为 0 的直通场景下，原先无条件放行读写，忽略了设备表项中的读、写权限位。现在按这些权限位决定是否启用直通内存区域，使直通访问也受读写权限约束，符合规范要求。
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260718175208.118721-2-danielpaziyski@gmail.com/

**▸ 组织：Red Hat**（1 patches）

**[SERIES] amd_iommu: Fix opcode reported in invalid command handling** （cover letter，4/6 个 patch 达到代码量阈值）

- 日期：2026-07-05
- 状态：社区讨论中
- 作者邮箱：Michael S. Tsirkin <mst@redhat.com>
- 概括：修正 AMD 与 Intel 虚拟化 IO 设备模拟中的若干缺陷：非法命令记录时取错命令字导致跟踪与事件日志中的操作码不符，Intel 设备把页表支持位放错寄存器，中断控制寄存器与中断重映射表项改用与主机字节序无关的方式解析，命令缓冲区与事件日志按小端读写，页表遍历辅助函数返回类型改为有符号整数以消除类型不匹配告警。
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
- 作者邮箱：Dongli Zhang <dongli.zhang@oracle.com>
- 概括：修复 QEMU 中 AMD 虚拟 IOMMU 的若干问题：设备曾暴露两个 MSI 能力，现只保留一个；页错误日志此前只带设备功能号，位于根端口后的设备会被记成错误请求者，现改用完整总线号；扩展特性寄存器此前允许客户机改写第 4 位，现改为只读；客户机清除状态位时可能误置 GA 日志溢出位并反复重启 GA 日志，现不再锁存这些位。
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
- 作者邮箱：Pranjal Shrivastava <praan@google.com>
- 概括：针对 AMD IOMMU 驱动，重构设备探测流程并修复 ATS 配置问题：原先清除设备表项时用整块清零，可能与硬件读取产生撕裂写，且先清查找表导致 DMA 别名无法清除；现在改为先清有效位再清高位并同步到别名，探测失败时区分初始化失败与配置失败以保留中断重映射所需的查找表项，ATS 配置失败时直接让探测失败，并要求调用方先确认设备支持 ATS 再配置。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu/amd: Refactor device probe and capability initialization
- 来源：https://patchwork.kernel.org/project/linux-pci/patch/20260824122347.1588592-2-praan@google.com/

---

### ◆ 子系统：RISC-V IOMMU（4 patches）

**▸ 组织：ByteDance**（2 patches）

**[v3] iommu/riscv: Use 32-bit MMIO accesses for 64-bit registers**

- 日期：2026-07-13
- 状态：社区讨论中
- 作者邮箱：Zhanpeng Zhang <zhangzhanpeng.jasper@bytedance.com>
- 概括：RISC-V IOMMU 规范允许 64 位寄存器用两次 32 位访问完成，且未规定 8 字节访问的原子性。驱动改用先高后低的 32 位访问方式读写普通 64 位寄存器，对 DDTP 先轮询低半部分的忙标志再读高半部分，避免依赖不保证的原子 64 位访问。
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20260713122903.9458-1-zhangzhanpeng.jasper@bytedance.com/

**[RFC,1/3] iommu/riscv: Complete MRIF MSI PTE setup**

- 日期：2026-07-01
- 状态：社区讨论中
- 作者邮箱：Zhanpeng Zhang <zhangzhanpeng.jasper@bytedance.com>
- 概括：补全 RISC-V IOMMU 的 MRIF 中断投递路径。此前该路径只能改写已有的 MSI 表项，无法正确安装新的 MRIF 表项，且用普通物理页号方式编码 MRIF 地址。现在新增专门的 MRIF 表项编码，新建和改写两条路径都使用它，普通 MSI 编码保持不变；写入时先发布通知信息再置有效位，改写活动表项时先清有效位，避免设备中断读到有效表项却看到过期的通知数据。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260701040017.42707-2-zhangzhanpeng.jasper@bytedance.com/

**▸ 组织：Qualcomm**（1 patches）

**[SERIES] iommu/riscv: Enable MSI remapping, IOMMU_DMA and VFIO** （cover letter，11/11 个 patch 达到代码量阈值）

- 日期：2026-08-31
- 状态：社区讨论中
- 作者邮箱：Andrew Jones <andrew.jones@oss.qualcomm.com>
- 概括：让 64 位 RISC-V 上的 IOMMU 支持 MSI 重映射、DMA 地址映射和 VFIO 设备直通。原先软件 MSI 映射数量受固定上限限制，无法为每个 CPU 建立映射，且缺少保留的 MSI 地址窗口。现在把映射表改为可增长、支持按物理地址列表建立连续映射并原子安装，为每个可能 CPU 预留一页 MSI 地址窗口，报告缓存一致性能力，并开启相关内核配置与自测。
- 达到阈值的 patches（11 个，显示前 5）：
  - iommufd: Convert struct iommufd_sw_msi_maps to a growable bitmap
  - iommu/dma: Enable IOMMU_DMA for 64-bit RISC-V
  - iommu/riscv: Reserve an MSI IOVA window for iommufd
  - iommu/riscv: Report cache coherency capability
  - iommu/dma: Prepare MSI physical address lists
  - ... 及其他 6 个 patch
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20260831145943.313726-3-andrew.jones@oss.qualcomm.com/

**▸ 组织：Alibaba**（1 patches）

**[SERIES] iommu/riscv: Add hardware dirty tracking for second-stage domains** （cover letter，4/7 个 patch 达到代码量阈值）

- 日期：2026-08-21
- 状态：社区讨论中
- 作者邮箱：yu fangyu <fangyu.yu@linux.alibaba.com>
- 概括：为 RISC-V IOMMU 的第二阶段（iohgatp）域增加硬件脏页跟踪，用于 KVM 下 VFIO 设备直通场景：新增 Sv39x4/Sv48x4/Sv57x4 页表格式与脏位读写操作，支持 GSCID 和 GVMA 失效命令，按分配标志选择第一阶段或第二阶段域，并在硬件支持原子操作时预使能脏位更新，使 iommufd 能通过脏页跟踪接口获取写访问信息。
- 达到阈值的 patches（4 个，显示前 5）：
  - iommu/riscv: use data structure instead of individual values
  - iommupt: Add RISC-V Second-stage (iohgatp) page table support
  - iommu/riscv: support GSCID and GVMA invalidation command
  - iommu/riscv: Pre-enable GADE for second-stage domains
- 来源：https://patchwork.kernel.org/project/linux-riscv/patch/20260821132749.82070-5-fangyu.yu@linux.alibaba.com/

---

### ◆ 子系统：IOMMUFD（4 patches）

**▸ 组织：NVIDIA**（2 patches）

**[SERIES] iommufd: Iterate the cache invalidation array in the core** （cover letter，5/5 个 patch 达到代码量阈值）

- 日期：2026-08-30
- 状态：社区讨论中
- 作者邮箱：Nicolin Chen <nicolinc@nvidia.com>
- 概括：把缓存失效请求数组的遍历从各驱动上移到 iommufd 核心，并收紧 Arm SMMUv3 对来宾失效命令的校验。此前每个驱动各自遍历整个数组并自行处理分批，SMMUv3 只校验虚拟机和流标识就把命令原样转发，来宾可设置宿主未打算转发的保留位，使命令被判为非法；转换失败时还会上报尚未真正下发的命令，导致用户空间跳过未执行的失效。
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
- 作者邮箱：Nicolin Chen <nicolinc@nvidia.com>
- 概括：修复 iommufd 虚拟设备分配的生命周期问题：驱动校验失败时未释放组锁，会让该组后续虚拟设备操作死锁；虚拟设备在驱动初始化成功前就加入查找表，并发的失效操作可能命中一个本应被拒绝的设备；ARM SMMUv3 把客户机虚拟流 ID 映射到设备首个物理流 ID，多流设备其余流不会被失效覆盖，无流设备则越界读取。现在修正解锁路径、初始化成功后再发布，并要求设备恰好一个流 ID。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommufd/viommu: Publish a vDEVICE only after vdevice_init() succeeds
  - iommu/arm-smmu-v3-iommufd: Require exactly one Stream ID for a vDEVICE
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/e903f775d491296a525097e2a90b3eb6a47cf2ef.1783311134.git.nicolinc@nvidia.com/

**▸ 组织：Google**（1 patches）

**[2/2] iommufd: Periodically reschedule when unmapping**

- 日期：2026-07-14
- 状态：社区讨论中
- 作者邮箱：Aaron Lewis <aaronlewis@google.com>
- 概括：在 iommufd 解除大范围 DMA 映射时，逐页处理可能长时间不让出 CPU，导致内核调度告警。现在每处理一定数量的页就主动让出调度，使解除映射过程不再长时间独占 CPU，缓解调度延迟问题。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260714210303.3967981-3-aaronlewis@google.com/

**▸ 组织：Infradead Community**（1 patches）

**[SERIES] KVM: selftests: sev_smoke_test: Only run VM types the host offers** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-07-20
- 状态：社区讨论中
- 作者邮箱：David Woodhouse <dwmw2@infradead.org>
- 概括：为 KVM 自测程序调整 SEV 相关用例的运行条件：原先只要处理器报告支持 SEV 就无条件执行普通 SEV 子测试，但当全部 SEV 标识符都分配给 SNP 时，内核并不提供该虚拟机类型，测试会在创建虚拟机时直接中止。现在改为依据内核实际提供的虚拟机类型来决定是否运行，并在类型不可用时干净跳过，使测试在仅支持 SNP 的主机上也能正常完成其余可用模式的检查。
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
- 作者邮箱：Dmitry Baryshkov <dmitry.baryshkov@oss.qualcomm.com>
- 概括：为 MSM8974 上的高通 IOMMU 实例增加支持，使该芯片的显示、视频和 GPU 能使用 IOMMU。这些实例不受可信执行环境管理，需要操作系统自行配置全局寄存器空间，且只支持短描述符页表，此前驱动硬编码 LPAE 格式导致访问全部出错。新增按实例配置、非安全模式编程、电源域崩溃后恢复上下文，并在编程上下文时暂停微 MMU 以避免与在途事务竞争。
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
- 作者邮箱：Prakash Gupta <prakash.gupta@oss.qualcomm.com>
- 概括：在 SMMU 位于电源域的系统上，故障处理函数会访问寄存器，而 Adreno SMMU 在故障风暴时关闭了停顿，SMMU 可能在掉电状态下产生故障，导致未上电的寄存器读取和 NoC 错误。现在故障处理前先获取运行时电源，未激活则忽略故障；挂起前关闭故障上报并同步中断，避免电平触发中断在掉电过程中反复触发。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260806-smmu-rpm-v4-1-8183d007331c@oss.qualcomm.com/

**[SERIES] iommu/qcom: Misc Fixes** （cover letter，4/6 个 patch 达到代码量阈值）

- 日期：2026-07-17
- 状态：社区讨论中
- 作者邮箱：Mukesh Ojha <mukesh.ojha@oss.qualcomm.com>
- 概括：修复高通 IOMMU 驱动的若干缺陷：故障上报判断写反导致已处理的故障被误报为未处理；探测时未检查运行时恢复返回值，可能在时钟未开时访问硬件；域初始化失败路径会永久泄漏页表；页表指针在解锁后才发布，并发映射可能拿到空指针而拒绝合法映射；上下文探测在时钟未开时读写寄存器。
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
- 作者邮箱：Anna Maniscalco <anna.maniscalco2000@gmail.com>
- 概括：为高通 a7xx 系列 GPU 启用 LPAC 低优先级队列：此前 GPU 的 SID 0 和 1 共用同一地址空间，LPAC 无法独立更新页表。现在把 SID 1 拆到独立的 LPAC 设备节点，为其分配独立上下文和地址空间，配置固件访问窗口，并新增 LPAC 环的初始化、提交队列接口和崩溃转储信息，使 GPU 能通过独立环提交低优先级任务。
- 达到阈值的 patches（1 个，显示前 5）：
  - iommu: arm-smmu-qcom: Configure lpac device with split address space
- 来源：https://patchwork.kernel.org/project/dri-devel/patch/20260705-descriptive-name-lpac-upstream-v1-1-01d50c3e0c99@gmail.com/

---

### ◆ 子系统：Intel VT-d（3 patches）

**▸ 组织：Bull**（2 patches）

**[v2] intel_iommu: Expose SMPWC when SVM is enabled**

- 日期：2026-08-08
- 状态：社区讨论中
- 作者邮箱：Clément MATHIEU--DRIF <clement.mathieu--drif@bull.com>
- 概括：QEMU 的 Intel 虚拟 IOMMU 在启用共享虚拟内存时，没有向客户机暴露可扩展模式一致性页表遍历能力，而 Linux 的共享虚拟内存依赖该能力。现在启用共享虚拟内存时一并暴露该能力，并在宿主 IOMMU 不支持时拒绝加速，避免客户机使用后出错。
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260808153626.873965-1-clement.mathieu--drif@bull.com/

**[v2] intel_iommu: Check address mask before using it in pasid-based iotlb invalidation**

- 日期：2026-07-24
- 状态：社区讨论中
- 作者邮箱：Clément MATHIEU--DRIF <clement.mathieu--drif@bull.com>
- 概括：在 Intel IOMMU 模拟中处理基于 PASID 的 IOTLB 失效描述符时，先检查地址掩码是否超出硬件允许的最大值，若非法则报错并拒绝执行，避免有缺陷的驱动触发格式错误的失效操作。
- 来源：https://patchwork.kernel.org/project/qemu-devel/patch/20260724111424.376680-1-clement.mathieu--drif@bull.com/

**▸ 组织：Intel**（1 patches）

**[SERIES] intel_iommu: Enable PRQ support for passthrough device** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-08-31
- 状态：社区讨论中
- 作者邮箱：Duan, Zhenzhong <zhenzhong.duan@intel.com>
- 概括：为直通设备启用 Intel VT-d 的页请求队列支持。此前客户机在虚拟 IOMMU 中开启页请求时，主机侧可恢复缺页事件无法回传客户机。现在分配故障队列对象并注册事件处理，把主机产生的可恢复缺页转发给客户机，再把客户机的响应写回主机，同时缓存每个故障组的标识；PASID 条目失效时在底半部释放故障队列资源，避免文件引用未释放导致释放失败。
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
- 作者邮箱：Nicolin Chen <nicolinc@nvidia.com>
- 概括：NVIDIA Tegra241 的命令队列分配中，虚拟命令队列基址寄存器只保存 48 位地址，而分配出的基址可能带更高位，掩码写入会静默截断，导致硬件从错误内存取命令。现在检测到超出 48 位的基址就告警并让队列初始化失败，避免静默截断；真实硬件不会出现该情况，只有虚拟机监控器给出不匹配的地址宽度时才可能触发。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260729220329.805417-1-nicolinc@nvidia.com/

**[SERIES] iommu/tegra241-cmdqv: Fix error-interrupt races and VINTF lifecycle bugs** （cover letter，5/11 个 patch 达到代码量阈值）

- 日期：2026-07-14
- 状态：社区讨论中
- 作者邮箱：Nicolin Chen <nicolinc@nvidia.com>
- 概括：针对 Tegra241 的 CMDQV 硬件，修复错误中断与虚拟接口生命周期之间的竞态：命令队列在完全初始化前就被发布，错误中断可能读到空指针或已释放对象；虚拟接口销毁与中断处理未同步，可能读到半清除的槽位或已释放对象；错误映射索引越界会读越界；探测阶段中断过早注册会遍历未初始化数组；移除时先拆虚拟接口后释放中断也会读到失效指针。
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
- 作者邮箱：Aneesh Kumar K.V <aneesh.kumar@kernel.org>
- 概括：修正 IOMMU DMA 分配中非阻塞、非一致性路径的失败判断。该路径调用原子池分配，成功时才填充 CPU 地址，原代码却依赖 CPU 地址判断是否失败。现在改为直接检查返回的页指针，为空即返回失败，避免在分配失败时继续用无效页做 IOMMU 映射。
- 来源：https://patchwork.kernel.org/project/linux-arm-kernel/patch/20260717180442.110954-4-aneesh.kumar@kernel.org/

---

### ◆ 子系统：IOMMU Page Table（1 patches）

**▸ 组织：Qualcomm**（1 patches）

**[v4] iommu/io-pgtable-arm: Add support for contiguous hint bit**

- 日期：2026-08-04
- 状态：社区讨论中
- 作者邮箱：Vijayanand Jitta <vijayanand.jitta@oss.qualcomm.com>
- 概括：为 ARM LPAE 页表增加连续提示位支持：当一组连续页表项映射自然对齐的连续内存时，硬件可将其合并为单个 TLB 项，减少 TLB 占用。各页粒度对应的连续块大小会通过页大小位图上报，便于调用方按这些大小对齐分配；对连续组的局部解映射会被拒绝，保证整组一起失效。硬件存在相关缺陷时，驱动可通过一个禁用标志在运行时关闭该特性。
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

*报告由 Linux Patches Tracker 自动生成 | 2026-09-11 18:21:35*
