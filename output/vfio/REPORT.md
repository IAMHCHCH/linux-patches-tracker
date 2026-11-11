# Linux VFIO 子系统 Patch 追踪报告

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
| 社区讨论中 | 29 | 70.7% |
| 已合入 | 12 | 29.3% |
| 已关闭 | 0 | 0.0% |
| **总计** | **41** | **100%** |

### 按组织分类（TOP 15）

| 组织 | 数量 | 占比 |
|------|------|------|
| Individual Contributor | 8 | 19.5% |
| Google | 7 | 17.1% |
| NVIDIA | 7 | 17.1% |
| IBM | 4 | 9.8% |
| Kernel.org | 4 | 9.8% |
| Amazon | 2 | 4.9% |
| OzLabs Community | 2 | 4.9% |
| Red Hat | 2 | 4.9% |
| AMD | 1 | 2.4% |
| 归属待核实（baidu.com） | 1 | 2.4% |
| ARM | 1 | 2.4% |
| 归属待核实（openai.com） | 1 | 2.4% |
| Huawei | 1 | 2.4% |

### 按子系统分类

| 子系统 | 数量 | 占比 |
|--------|------|------|
| VFIO PCI | 17 | 41.5% |
| VFIO Core | 13 | 31.7% |
| VFIO Selftests | 2 | 4.9% |
| VFIO FSL-MC | 1 | 2.4% |
| VFIO Platform | 1 | 2.4% |
| VFIO AP (s390) | 1 | 2.4% |
| VFIO Migration | 1 | 2.4% |
| VFIO CCW (s390) | 1 | 2.4% |
| VFIO CDEV | 1 | 2.4% |
| VFIO CDX | 1 | 2.4% |
| VFIO MLX5 Variant | 1 | 2.4% |
| VFIO IOMMUFD | 1 | 2.4% |

## 重点 Patch Top20 清单

### 已合入

| 厂商 | 简介 |
|------|------|
| NVIDIA | [PATCH v7 00/10] mlx5 support for VFIO self test ------为 VFIO 自测试框架补充迈络思 ConnectX 网卡的用户态驱动支持：先调整内核声明以提供硬件命令和工作队列描述符等字段布局，并把字段访问宏拆出供自测试使用；然后自测试驱动通过命令接口完成 HCA 初始化、页分配、保护域和内存密钥建立，再创建自环队列对执行 DMA 数据搬运，最后把完成事件连接到 MSI-X 向量，使 VFIO 测试能覆盖该设备的数据通路和中断上报。 |
| Individual Contributor | [PATCH v2 00/7] vfio: mmap()/mprotect() hygiene for MMIO region mappings ------针对 VFIO 平台、fsl-mc 和 CDX 设备的 MMIO 区域映射，修复只读区域可能先只读映射再通过内存保护修改升级为可写而被写入的问题，做法是清除对应虚拟内存的可写许可；同时保持逻辑文件偏移并拒绝非共享映射，避免将来设备撤销映射时因偏移被物理页帧号覆盖而留下失效映射。当前这些路径多为防御性处理，尚无驱动实际暴露只读区域。 |
| Individual Contributor | [v2,1/2] vfio/nvgrace-gpu: Use a core-only open_device in fallback mode ------在 ACPI 内存属性缺失或芯片间高速链路断开时，英伟达 nvgrace GPU 的 VFIO 设备进入降级模式，原打开路径会无条件注册长度为零的地址范围，导致残留节点使第二次打开失败，并可能在重新绑定后触发已释放内存访问。现在为降级模式改用只执行核心 PCI 启用的打开流程，不再注册该地址范围，使打开关闭对称，消除残留和释放后使用问题。 |
| Huawei | [v6,2/2] hisi_acc_vfio_pci: reject live migration on 64KB page with QM_HW_V3 hardware ------华为加速器虚拟功能直通设备在第三代队列管理硬件且系统页为 64KB 时，功能区域与迁移寄存器共享同一个物理页且缺少隔离，可能把迁移寄存器暴露给客户机，并在 KVM 模拟设备方案下触发客户机内核调用栈错误。此前在打开设备时直接拒绝，导致直通完全不可用；现在改为探测阶段识别该情形并绑定通用操作接口，保持设备直通可用，仅禁用实时迁移。 |
| NVIDIA | [v2,1/4] vfio: Reject a second cdev open before mutating shared device state ------修复 VFIO 设备字符设备路径中，第二个绑定 IOMMUFD 的调用会先更新设备令牌和 KVM 关联，然后才在打开阶段被拒绝，错误路径会破坏当前打开者的 KVM 关联或留下被覆盖的令牌；现将单次打开检查前移到这些共享状态修改之前，并以设备忙返回，使无法完成的绑定不会污染现有用户。 |
| Google | [v2] vfio: selftests: Add documentation ------为 VFIO 自测试新增专门文档，覆盖设备挑选与设置、测试运行和清理、利用测试框架编写用例的基本步骤，以及辅助库提供的设备与 IOMMU 对象等接口；文档纳入驱动 API 目录，为内核开发者使用和扩展 VFIO 自测试提供入门参考。 |
| 归属待核实（baidu.com） | [PATCH] vfio/pci: Restore 8-byte ioeventfd support ------VFIO PCI 的 ioeventfd 注册一度支持 8 字节访问，但此前的一次清理把仅在缺少 64 位写入接口时需要的限制误保留为无条件拒绝，导致所有 8 字节事件寄存器注册失败。现在删除这项无条件检查，恢复 8 字节 ioeventfd 的正常注册。 |
| NVIDIA | [v3,1/1] vfio/pci: Remove the core dependency on driver data ------VFIO PCI 核心原先强制各设备驱动把核心设备结构放在驱动私有数据开头，使变体驱动无法自由安排私有数据布局。现在新增回调包装宏，让各驱动在私有数据中保存自己的结构体，并通过生成的包装把核心设备传给公共辅助函数，从而解除核心对驱动私有数据布局的依赖，为 Rust PCI 类型化驱动数据等不同设计腾出空间。 |
| Individual Contributor | [v4] vfio/platform: prevent read-only region mappings from becoming writable ------VFIO 平台设备在区域没有写标志时虽拒绝初始可写映射，但没有清除虚拟内存区域的可写升级许可，用户空间可以先只读映射再用内存保护调用改成可写。现在对这类只读区域清除后续可写许可，堵住只读映射被升级为可写的路径；当前没有平台驱动发布只读区域，属于防御性加固。 |
| Individual Contributor | [v3] vfio/fsl-mc: prevent read-only region mappings from becoming writable ------VFIO 的 FSL-MC 总线设备在区域没有写标志时同样只拒绝初始可写映射，却保留后续可写升级许可，用户空间可先只读映射再改为可写。现在对这些区域清除虚拟内存区域的后续可写许可，防止只读映射被升级；目前所有 FSL-MC 设备区域都带有写标志，此改动为防御性加固。 |
| Individual Contributor | [v2] vfio/type1: avoid walking reserved-only mappings while unpinning ------修复 VFIO 类型 1 IOMMU 拆除只包含保留页的大型设备直通 DMA 映射时，仍遍历数千万个物理页进行无效分类，导致单次解除映射长时间占用 CPU 并触发软锁；现在区分是否混有非保留页，全部为保留页时跳过遍历直接结束，避免此类拆除路径卡死。 |
| Individual Contributor | [1/3] vfio/pci: Drain eventfd RCU callbacks on module exit ------修复 VFIO PCI 在替换错误或请求通知的事件文件描述符时，释放回调通过 RCU 延迟执行；设备关闭后回调可能仍排队，导致依赖驱动移除后 vfio-pci-core 模块被卸载而回调仍指向模块代码。现在模块退出前等待 RCU 回调清空，避免执行已卸载模块代码。 |

### 社区讨论

| 厂商 | 简介 |
|------|------|
| NVIDIA | [PATCH v6 00/31] vfio/pci: Add CXL Type-2 device passthrough support ------为将 CXL Type-2 设备透传给虚拟机，新增按需加载的 vfio-cxl 提供模块：提供方持有组件寄存器基地址，向客户机暴露主机管理内存区域，将 HDM 解码器只读呈现并屏蔽直接访问，虚拟化 CXL 扩展配置空间；在复位、低功耗和热复位路径上保存恢复解码器状态，并支持导出内存区域为 DMA 缓冲区。PCI 层还拒绝在次级总线复位被屏蔽的 CXL 端口下报告热复位成功；无提供方时设备仍按普通 PCI 透传。 |
| NVIDIA | [PATCH v1 00/19] vfio/pci: Handle PCI error recovery and report state to userspace ------为通用 vfio-pci 驱动增加主机 PCI 错误恢复支持并可将事件状态报告用户态。引入恢复状态、锁和等待队列，在设备打开关闭、配置空间访问、复位、中断、电源管理、DMA 缓冲区导出等路径中加入守卫，使恢复开始时阻止新访问、等待已在进行的操作完成，避免恢复回调与关闭或复位并发导致访问已释放状态或锁顺序死锁。恢复期间访问会失败或等待，屏障页错误在临时恢复后可重试；只有通用驱动在用户显式启用后生效，变体驱动保持不变。 |
| OzLabs Community | [PATCH v8 00/9] vfio/pci: Add mmap() for DMABUFs ------为 VFIO PCI 设备引入基于 DMA 缓冲区的 BAR 映射，并支持对导出的 DMA 缓冲区执行内存映射，使进程可通过共享 DMA 缓冲区文件描述符把 BAR 的特定子范围安全委托给其他进程，无需交出整个设备文件描述符；同时统一 BAR 撤销流程，并修复低功耗恢复路径未恢复映射等问题，支持用户显式请求永久撤销某个缓冲区。 |
| Google | [PATCH v1 00/5] vfio/pci: Fix power state race with SR-IOV enablement ------修复 VFIO PCI 在关闭设备与启用 SR-IOV 同时发生时，因未持锁而并发将设备从 D3hot 切回 D0 的竞争问题。该竞争在需要电源恢复的设备上可能触发虚拟功能 BAR 更新警告，或重复加载释放保存状态。现在所有功率状态转换都在内存锁下进行，并用原子读/写标注相关标志，同时增加自测覆盖关闭、启用 SR-IOV 及两者并发竞争场景。 |
| NVIDIA | [PATCH v2 00/16] vfio/pci: Handle PCI error recovery and report state to userspace ------为 VFIO PCI 设备增加主机 PCI 错误恢复期间的访问门控和用户空间通知机制。启用恢复后，在恢复开始时阻断配置空间、BAR/ROM、中断配置、复位、电源管理等访问，并等待已进入的操作完成；恢复完成后从保存快照恢复设备状态、解除阻断并通知用户空间。期间部分请求返回错误，无法恢复时保持阻断并报告失败，避免主机恢复与用户访问相互干扰。 |
| Google | [PATCH v1 00/9] vfio: Add support for platform devices ------在虚拟机管理器 kvmtool 中新增把平台设备通过 VFIO 直通给客户机的能力，映射设备 MMIO 区域并生成设备树节点，支持多中断和边沿触发；用户可提供设备树模板补充兼容属性等绑定信息，解决只有寄存器和中断不足以让客户机驱动匹配的问题。同时修复已有组内设备文件描述符泄漏，并抽出有线中断的公共设置拆除代码。 |
| Google | [PATCH v3 00/4] Introduce vfio_dma_mapping_perf_test ------新增 VFIO DMA 映射性能自测试，不依赖容易抖动的延迟阈值，而是直接报告 DMA 区域映射、解除映射、内存映射和解除内存映射等阶段的耗时；测试使用提前填充页表来隔离页错误。另加入基于内存文件的映射测试，用于比较 IOMMU 文件映射接口与普通方法的延迟差异。测试框架增加自定义命令行选项，允许用户指定 DMA 区域大小，例如 16G。 |
| Google | [PATCH v6 00/18] iommu: Add live update state preservation ------为活跃更新场景提供 IOMMU 状态保存与恢复，覆盖页表、域、设备及 PASID 表和根表或上下文表，其中 vt-d 驱动负责保留并恢复自身硬件状态，未保留设备的旧条目在关机时清理。iommufd 增加标记硬件页表保留的接口；用户态标记后，相关映射不可变并拒绝映射或解除映射，保存时验证后备内存并保留 IOMMU 域。VFIO 字符设备保存时一并保存其 iommufd 附着状态，此后禁止再附加或分离，恢复时重新附着域。 |
| Google | [PATCH v1 00/7] iommu: Introduce Page Table Observability Framework ------新增 IOMMU 页表可观测性框架，把 IO 页表页面数归属到具体 IOMMU 域，并在 VFIO 容器和 iommufd 的 fdinfo 中暴露 iommu-nr-pages 字段，使用户可查看各设备或容器实际占用的 IO 页表页数。仅通用页表库实现的域会计数，任一附加域不支持时省略该字段，避免报告部分计数；自测还验证了卸载映射后页数暂不下降的当前行为。 |
| IBM | [v6,1/5] s390/vfio-ap: Fix leak of pinned NIB and registered GISC in vfio_ap_irq_enable/disable() ------针对 s390 加密适配器队列透传，修复启用或禁用中断时对固定通知指示字节页和客户机中断子类的管理：禁用命令是异步的，若在中断位清零前释放固定页，硬件后续 DMA 写入可能落到已被新所有者占用的内存。现在先等待中断位清零，超时则故意保留固定页和中断注册以避免野写入；只有确认队列不再工作时才立即释放。 |
| IBM | [v11,5/5] vfio-pci/zdev: Add VFIO FMB device features ------为 zPCI 设备新增 VFIO 特性，把 FMB 测量功能透传给用户空间：用户可启用或禁用 FMB，并在启用后读取最新测量数据。该能力面向需要从用户态获取 zPCI 设备测量信息的直通场景。 |
| Google | [v1] vfio/pci: pass FAULT_FLAG_WRITE to vmf_insert_pfn_pmd/pud() ------修复 VFIO PCI 巨页映射插入时未根据故障类型传递写标志，导致共享可写映射在软件脏页跟踪后或写保护场景下安装只读巨页，后续写故障进入巨页写保护处理却因标志为只读而不做任何修改，造成无限写缺页循环；现在写故障会正确标记新巨页为脏且可写。 |
| Individual Contributor | [PATCH] vfio/nvgrace-gpu: Skip PFN registration for empty memory regions ------针对 vfio/nvgrace-gpu 设备，在 ACPI 内存属性缺失或 C2C 链路断开的回退模式下，使用内存区域长度为零但仍被注册，导致页帧号地址空间覆盖整个范围且关闭路径无法注销；第二次打开返回 EBUSY，解绑后残留节点可能在后续注册或内存错误处理时访问已释放内存，错误也被记为已恢复而非忽略。现在仅当使用内存区域长度非零时注册和注销该区域，回退模式不再注册，避免残留和误报。 |
| IBM | [v6,4/5] vfio/spapr_tce: Normalize EEH IOA error injection addresses ------在 IBM Power 的 sPAPR VFIO EEH 错误注入路径中，用户态可能传入主机 Linux BAR 资源地址，而固件平台后端期望 PCI/IOA 总线地址。现在对内存或 IO BAR 目标函数做地址归一化：已经是总线地址则保持不变，是资源地址则借助 BAR 相对偏移转换为总线地址；地址和掩码均为零的无地址注入直接透传。 |
| NVIDIA | [v2,12/12] vfio/nvidia-vgpu: add the Rust VFIO variant driver ------为 NVIDIA vGPU 虚拟功能新增 Rust 编写的 VFIO PCI 变体驱动，配合 nova-core 管理实例：首次打开时创建实例，最后一次关闭时销毁；暴露分配的设备与子系统标识，限制分配的 BAR1 范围，并协调固件复位与 PCI 复位。无 Nova vGPU 接口的设备继续走普通 PCI 透传。构建系统扩展导出所需 Rust 符号，使该驱动能编译并链接 nova-core。 |
| ARM | [RFC,v2,12/15] vfio: Support VFIO devices that access the CPU MMU ------新增一类不经 IOMMU、由 CPU MMU 完成 DMA 的 VFIO 设备支持。这类设备不绑定 iommufd 接口、不使用 VFIO 容器，打开时不强制要求容器，设置容器会被拒绝；虚拟机管理器因需要设备特定知识创建虚拟设备，知道不必分配容器。适用于与 CPU 共享页表的设备直通场景。 |
| Red Hat | [v2,3/7] vfio/pci: Add qcom-vfio-pci variant driver ------针对高通 ath11k/ath12k WiFi 设备直通虚拟机时，固件需要主机物理 MSI 地址而客户机只看到虚拟地址导致初始化失败的问题，新增 VFIO 变体驱动，在分配后缓存物理 MSI 值并写入扩展配置空间，供客户机驱动自动发现使用；要求虚拟机启用 IOMMU 中断重映射和缓存模式，确保设备发出的 MSI 写入能正确路由。 |
| Kernel.org | [RFC,POC,31/50] vfio: install the migration data descriptor when the ioctl returns ------调整 VFIO 迁移数据文件描述符的安装时机，改为在迁移状态获取 ioctl 返回时通过新的描述符准备机制完成安装，错误和资源回收依赖文件关闭路径统一处理，避免原先手动分配、安装和回退的分散逻辑。 |
| NVIDIA | [12/13] vfio/nvidia-vgpu: add the NVIDIA vGPU VFIO variant driver ------为 NVIDIA vGPU 虚拟功能新增 VFIO PCI 变体驱动，仅允许通过显式覆盖绑定且只接受虚拟功能，将实例打开、复位和关闭委托给 PF 侧 nova-core 协调；配置空间读取向用户展示固件选定的设备与子系统 ID，并按分配规格调整 BAR1 大小，其余操作沿用 vfio-pci-core。 |
| Kernel.org | [v8,17/23] vfio/pci: Hand out the P2PDMA provider behind a dma-buf ------让从 VFIO PCI 导出的 dma-buf 向导入方返回其点对点 DMA 提供者，使调用方能判断点对点流量是否直接到达导出的 BAR；当缓冲区已被撤销后不再返回提供者，避免描述已经失效的设备资源。 |

---

## 已合入 Patches

### ◆ 子系统：VFIO PCI（4 patches）

**▸ 组织：归属待核实（baidu.com）**（1 patches）

**vfio/pci: Restore 8-byte ioeventfd support**

- 日期：2026-09-22
- 状态：已合入
- 作者邮箱：Li,Rongqing <lirongqing@baidu.com>
- 概括：VFIO PCI 的 ioeventfd 注册一度支持 8 字节访问，但此前的一次清理把仅在缺少 64 位写入接口时需要的限制误保留为无条件拒绝，导致所有 8 字节事件寄存器注册失败。现在删除这项无条件检查，恢复 8 字节 ioeventfd 的正常注册。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260922040013.2188-1-lirongqing@baidu.com/

**▸ 组织：Individual Contributor**（1 patches）

**[1/3] vfio/pci: Drain eventfd RCU callbacks on module exit**

- 日期：2026-09-26
- 状态：已合入
- 作者邮箱：Jiale Yao <yaojiale02@163.com>
- 概括：修复 VFIO PCI 在替换错误或请求通知的事件文件描述符时，释放回调通过 RCU 延迟执行；设备关闭后回调可能仍排队，导致依赖驱动移除后 vfio-pci-core 模块被卸载而回调仍指向模块代码。现在模块退出前等待 RCU 回调清空，避免执行已卸载模块代码。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260926162554.163197-2-yaojiale02@163.com/

**▸ 组织：NVIDIA**（1 patches）

**[v3,1/1] vfio/pci: Remove the core dependency on driver data**

- 日期：2026-10-05
- 状态：已合入
- 作者邮箱：Simon Song <xinmengs@nvidia.com>
- 概括：VFIO PCI 核心原先强制各设备驱动把核心设备结构放在驱动私有数据开头，使变体驱动无法自由安排私有数据布局。现在新增回调包装宏，让各驱动在私有数据中保存自己的结构体，并通过生成的包装把核心设备传给公共辅助函数，从而解除核心对驱动私有数据布局的依赖，为 Rust PCI 类型化驱动数据等不同设计腾出空间。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261005184236.1946167-2-xinmengs@nvidia.com/

**▸ 组织：Huawei**（1 patches）

**[SERIES] fix two issues in hisi_acc_vfio_pci driver** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-10-13
- 状态：已合入
- 作者邮箱：Longfang Liu <liulongfang@huawei.com>
- 概括：修复华为加速器 VFIO 驱动两个问题：在物理功能直通时队列管理指针为空，复位准备路径先使用它记录超时导致内核崩溃，现将热迁移操作检查移到入口，使非迁移设备完全跳过复位协调并清除此前未清除的复位标志；对于 64KB 页下虚拟功能控制模式硬件，功能区域与迁移寄存器共处同一物理页且无隔离，会向客户机泄漏迁移寄存器，现将模式判定移到探测阶段，让此类设备仍可直通但禁用热迁移。
- 达到阈值的 patches（1 个，显示前 5）：
  - hisi_acc_vfio_pci: reject live migration on 64KB page with QM_HW_V3 hardware
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261013071929.3988687-2-liulongfang@huawei.com/

---

### ◆ 子系统：VFIO Core（2 patches）

**▸ 组织：Individual Contributor**（2 patches）

**[SERIES] vfio/nvgrace-gpu: Separate the fallback-mode open_device** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-10-15
- 状态：已合入
- 作者邮箱：Andrea Parri <parri.andrea@gmail.com>
- 概括：修复 NVIDIA Grace GPU 在缺少 ACPI 内存属性或芯片间互联链路断开时进入降级模式的问题。原来降级模式共用完整打开函数但关闭时用核心路径，导致打开时注册覆盖全地址范围的内存区域节点，第二次打开失败，解绑后节点悬空触发释放后使用。现在为降级模式单独实现只做核心启用的打开函数，不再触碰内存区域节点，并移除完整打开中针对降级模式的长度检查。结果消除重复打开失败和释放后使用问题。
- 达到阈值的 patches（1 个，显示前 5）：
  - vfio/nvgrace-gpu: Use a core-only open_device in fallback mode
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261015081937.405320-2-parri.andrea@gmail.com/

**[v2] vfio/type1: avoid walking reserved-only mappings while unpinning**

- 日期：2026-09-19
- 状态：已合入
- 作者邮箱：Sam Crossley <samuelcrossley@gmail.com>
- 概括：修复 VFIO 类型 1 IOMMU 拆除只包含保留页的大型设备直通 DMA 映射时，仍遍历数千万个物理页进行无效分类，导致单次解除映射长时间占用 CPU 并触发软锁；现在区分是否混有非保留页，全部为保留页时跳过遍历直接结束，避免此类拆除路径卡死。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260919-vfio-v2-1-68e7ed355972@gmail.com/

---

### ◆ 子系统：VFIO FSL-MC（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[v3] vfio/fsl-mc: prevent read-only region mappings from becoming writable**

- 日期：2026-09-03
- 状态：已合入
- 作者邮箱：Abdifatah Suruur <suruurism@gmail.com>
- 概括：VFIO 的 FSL-MC 总线设备在区域没有写标志时同样只拒绝初始可写映射，却保留后续可写升级许可，用户空间可先只读映射再改为可写。现在对这些区域清除虚拟内存区域的后续可写许可，防止只读映射被升级；目前所有 FSL-MC 设备区域都带有写标志，此改动为防御性加固。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260903092912.444-1-suruurism@gmail.com/

---

### ◆ 子系统：VFIO Platform（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[v4] vfio/platform: prevent read-only region mappings from becoming writable**

- 日期：2026-09-06
- 状态：已合入
- 作者邮箱：Abdifatah Suruur <suruurism@gmail.com>
- 概括：VFIO 平台设备在区域没有写标志时虽拒绝初始可写映射，但没有清除虚拟内存区域的可写升级许可，用户空间可以先只读映射再用内存保护调用改成可写。现在对这类只读区域清除后续可写许可，堵住只读映射被升级为可写的路径；当前没有平台驱动发布只读区域，属于防御性加固。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260906123239.10858-1-suruurism@gmail.com/

---

### ◆ 子系统：VFIO Selftests（1 patches）

**▸ 组织：Google**（1 patches）

**[v2] vfio: selftests: Add documentation**

- 日期：2026-09-03
- 状态：已合入
- 作者邮箱：David Matlack <dmatlack@google.com>
- 概括：为 VFIO 自测试新增专门文档，覆盖设备挑选与设置、测试运行和清理、利用测试框架编写用例的基本步骤，以及辅助库提供的设备与 IOMMU 对象等接口；文档纳入驱动 API 目录，为内核开发者使用和扩展 VFIO 自测试提供入门参考。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260903183814.2111748-1-dmatlack@google.com/

---

### ◆ 子系统：VFIO CDEV（1 patches）

**▸ 组织：NVIDIA**（1 patches）

**[SERIES] vfio: Fix cdev second-open and harden selftests** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-09-11
- 状态：已合入
- 作者邮箱：Alex Williamson <alex.williamson@nvidia.com>
- 概括：针对 VFIO 字符设备路径的单打开限制，原先第二次绑定检查在已修改设备共享状态之后，失败时可能清除当前打开者的内核虚拟机关联并破坏物理功能令牌；现在把单打开检查提前到状态变更之前，重复绑定直接返回设备忙错误，不触碰原有状态，并新增自测验证失败绑定不会破坏令牌。同时延长相关自测超时，以容纳固件优先错误处理下设备复位延迟过长的情况。
- 达到阈值的 patches（1 个，显示前 5）：
  - vfio: Reject a second cdev open before mutating shared device state
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260911170429.1642480-2-alex.williamson@nvidia.com/

---

### ◆ 子系统：VFIO CDX（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[SERIES] vfio: mmap()/mprotect() hygiene for MMIO region mappings** （cover letter，5/5 个 patch 达到代码量阈值）

- 日期：2026-09-29
- 状态：已合入
- 作者邮箱：Abdifatah Suruur <suruurism@gmail.com>
- 概括：针对 VFIO 平台、fsl-mc 和 CDX 设备的 MMIO 区域映射，修复只读区域可能先只读映射再通过内存保护修改升级为可写而被写入的问题，做法是清除对应虚拟内存的可写许可；同时保持逻辑文件偏移并拒绝非共享映射，避免将来设备撤销映射时因偏移被物理页帧号覆盖而留下失效映射。当前这些路径多为防御性处理，尚无驱动实际暴露只读区域。
- 达到阈值的 patches（5 个，显示前 5）：
  - vfio/fsl-mc: keep logical vm_pgoff in MMIO region mmap
  - vfio/platform: keep logical vm_pgoff in MMIO region mmap
  - vfio/cdx: keep logical vm_pgoff in MMIO region mmap
  - vfio/cdx: reject non-shared MMIO mmaps
  - vfio/cdx: prevent read-only region mappings from becoming writable
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260929094848.7439-6-suruurism@gmail.com/

---

### ◆ 子系统：VFIO MLX5 Variant（1 patches）

**▸ 组织：NVIDIA**（1 patches）

**[SERIES] mlx5 support for VFIO self test** （cover letter，3/5 个 patch 达到代码量阈值）

- 日期：2026-09-21
- 状态：已合入
- 作者邮箱：Jason Gunthorpe <jgg@nvidia.com>
- 概括：为 VFIO 自测框架补充 mlx5 ConnectX 设备支持：从网络设备驱动中抽取接口定义、常量和访问宏供自测程序使用，并允许驱动声明所需内存区域大小；新增的 mlx5 自测驱动完成硬件初始化、命令接口和内存密钥创建，通过 RDMA 自环回实现数据复制和 MSI-X 中断发送，使这类设备能运行 VFIO 的 DMA 和中断路径自测。
- 达到阈值的 patches（3 个，显示前 5）：
  - vfio: selftests: mlx5 driver - add send_msi support
  - vfio: selftests: Add mlx5 driver - data path and memcpy ops
  - vfio: selftests: Add mlx5 driver - HW init and command interface
- 来源：https://patchwork.kernel.org/project/kvm/patch/7-v7-c6d30e8ce1e4+3dfa6-mlx5st_jgg@nvidia.com/

---

## 社区讨论中 Patches

### ◆ 子系统：VFIO PCI（13 patches）

**▸ 组织：Google**（3 patches）

**[SERIES] vfio/pci: Fix power state race with SR-IOV enablement** （cover letter，3/5 个 patch 达到代码量阈值）

- 日期：2026-10-29
- 状态：社区讨论中
- 作者邮箱：David Matlack <dmatlack@google.com>
- 概括：修复 VFIO PCI 设备关闭与启用 SR-IOV 并发时的电源状态竞争。原先进程关闭设备时将设备从 D3hot 恢复到 D0 未持有内存锁，可能与用户写入启用 SR-IOV 参数的线程同时执行，导致 PF 的 BAR 恢复顺序错乱，触发内核警告，甚至并发释放保存的电源状态。现在所有电源状态转换都在写内存锁保护下进行，并对无锁访问的活动标志做显式标注，新增自测覆盖 D3hot 关闭、SR-IOV 与竞争场景。
- 达到阈值的 patches（3 个，显示前 5）：
  - vfio/pci: Hold memory_lock for all calls to vfio_pci_set_power_state()
  - vfio/pci: Annotate lockless accesses to vdev->sriov_active
  - vfio: selftests: Add test for device power state transitions
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261029203324.1637772-2-dmatlack@google.com/

**[SERIES] iommu: Add live update state preservation** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-10-25
- 状态：社区讨论中
- 作者邮箱：Samiullah Khawaja <skhawaja@google.com>
- 概括：为活跃更新场景提供 IOMMU 状态保存与恢复，覆盖页表、域、设备及 PASID 表和根表或上下文表，其中 vt-d 驱动负责保留并恢复自身硬件状态，未保留设备的旧条目在关机时清理。iommufd 增加标记硬件页表保留的接口；用户态标记后，相关映射不可变并拒绝映射或解除映射，保存时验证后备内存并保留 IOMMU 域。VFIO 字符设备保存时一并保存其 iommufd 附着状态，此后禁止再附加或分离，恢复时重新附着域。
- 达到阈值的 patches（2 个，显示前 5）：
  - iommufd: Add APIs to preserve/unpreserve a vfio cdev
  - vfio/pci: Preserve the iommufd state of the vfio cdev
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261025021930.674647-17-skhawaja@google.com/

**[v1] vfio/pci: pass FAULT_FLAG_WRITE to vmf_insert_pfn_pmd/pud()**

- 日期：2026-10-24
- 状态：社区讨论中
- 作者邮箱：Mina Almasry <almasrymina@google.com>
- 概括：修复 VFIO PCI 巨页映射插入时未根据故障类型传递写标志，导致共享可写映射在软件脏页跟踪后或写保护场景下安装只读巨页，后续写故障进入巨页写保护处理却因标志为只读而不做任何修改，造成无限写缺页循环；现在写故障会正确标记新巨页为脏且可写。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261024015540.538758-1-almasrymina@google.com/

**▸ 组织：OzLabs Community**（2 patches）

**[SERIES] vfio/pci: Add mmap() for DMABUFs** （cover letter，7/8 个 patch 达到代码量阈值）

- 日期：2026-10-06
- 状态：社区讨论中
- 作者邮箱：Matt Evans <matt@ozlabs.org>
- 概括：VFIO PCI 的基地址寄存器映射改为通过 DMA 缓冲区查找物理页并统一撤销；新增把已导出缓冲区描述符映射给其他进程的能力，使进程只能访问基地址寄存器指定子范围而无需共享完整设备描述符，并支持用户空间主动请求撤销缓冲区、清除页表且禁止再次映射或附加。还修复低功耗唤醒恢复路径未恢复缓冲区状态的问题，用独立锁避免内存锁与映射锁可能形成的死锁。
- 达到阈值的 patches（7 个，显示前 5）：
  - vfio/pci: Un-revoke DMABUFs in LOW_POWER_ENTRY_WITH_WAKEUP resume
  - vfio/pci: Add a helper to look up PFNs for DMABUFs
  - vfio/pci: Add a helper to create a DMABUF for a BAR-map VMA
  - vfio/pci: Convert BAR mmap() to use a DMABUF
  - vfio/pci: Clean up BAR zap and revocation
  - ... 及其他 2 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261006193643.76330-3-matt@ozlabs.org/

**[v6,9/9] vfio/pci: Permanently revoke a DMABUF on request**

- 日期：2026-09-11
- 状态：社区讨论中
- 作者邮箱：Matt Evans <matt@ozlabs.org>
- 概括：在 VFIO PCI 通过直接内存访问缓冲区把设备基址寄存器范围借给客户端进程的场景中，原先撤销状态在复位后仍可恢复，无法彻底回收资源。现增加永久撤销状态和用户态撤销请求，传入目标缓冲区后保证其今后不能再导入、附加或映射，并清除已有动态映射，使原缓冲区失效后基址寄存器范围可安全重新导出。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260911214200.33793-10-matt@ozlabs.org/

**▸ 组织：Kernel.org**（2 patches）

**[SERIES] KVM/VFIO: guest_memfd support for device MMIO resources** （cover letter，6/6 个 patch 达到代码量阈值）

- 日期：2026-10-17
- 状态：社区讨论中
- 作者邮箱：Aneesh Kumar K.V <aneesh.kumar@kernel.org>
- 概括：为 KVM 受保护虚拟机中直通的 PCI 设备提供将设备 MMIO 资源作为客户机专用内存的支持。原先客户机专用内存只能分配普通物理页，无法处理直接提供物理帧号的设备 MMIO 资源；现在扩展提供者回调支持物理帧号后端，允许 VFIO PCI 附加设备 BAR，并限制主机访问、跟踪用户映射、在分离时清理。适用于希望将直通设备 MMIO 作为客户机私有内存管理的架构，要求架构支持受保护映射且默认禁用内存映射。
- 达到阈值的 patches（6 个，显示前 5）：
  - vfio/pci: Provide guest_memfd backing for PCI BARs
  - vfio/pci: Track userspace BAR mappings
  - vfio: Dispatch guest_memfd provider operations through the filesystem
  - vfio/pci: Restrict host BAR access for guest_memfd providers
  - vfio/pci: Detach guest_memfd access before teardown
  - ... 及其他 1 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261017073149.1303738-9-aneesh.kumar@kernel.org/

**[v8,17/23] vfio/pci: Hand out the P2PDMA provider behind a dma-buf**

- 日期：2026-09-28
- 状态：社区讨论中
- 作者邮箱：Leon Romanovsky <leon@kernel.org>
- 概括：让从 VFIO PCI 导出的 dma-buf 向导入方返回其点对点 DMA 提供者，使调用方能判断点对点流量是否直接到达导出的 BAR；当缓冲区已被撤销后不再返回提供者，避免描述已经失效的设备资源。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260928-fix-p2p-acs-v4-0-v8-17-404453b9c435@nvidia.com/

**▸ 组织：NVIDIA**（2 patches）

**[SERIES] vfio/pci: Add CXL Type-2 device passthrough support** （cover letter，23/25 个 patch 达到代码量阈值）

- 日期：2026-10-16
- 状态：社区讨论中
- 作者邮箱：Manish Honap <mhonap@nvidia.com>
- 概括：为 VFIO PCI 增加 CXL Type-2 设备直通支持：通过独立的 vfio-cxl 模块注册回调并在绑定此类设备时按需加载，避免普通 PCI 直通引入额外依赖；将 CXL 设备内存解码寄存器只读暴露给客户机，把解码出的内存区域以 DMA 缓冲区形式提供给客户机，并在复位、低功耗和内存错误路径中协调 CXL 状态，同时用排除区域机制阻止客户机直接访问需要虚拟化的配置区间。
- 达到阈值的 patches（23 个，显示前 5）：
  - vfio/pci: Detect CXL devices and load the CXL provider on demand
  - vfio/pci: Add a generic excluded-range list
  - vfio/pci: Virtualize the CXL DVSEC in vfio_pci_config.c
  - vfio/pci: Call the CXL open and close hooks around device use
  - vfio/pci: Bracket PCI resets with the CXL reset hooks
  - ... 及其他 18 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261016161839.2765592-8-mhonap@nvidia.com/

**[SERIES] vfio/pci: Handle PCI error recovery and report state to userspace** （cover letter，15/19 个 patch 达到代码量阈值）

- 日期：2026-09-01
- 状态：社区讨论中
- 作者邮箱：Shameer Kolothum Thodi <skolothumtho@nvidia.com>
- 概括：为通用 VFIO PCI 驱动新增主机 PCI 错误恢复机制：引入恢复状态和锁，在主机错误恢复冻结或复位设备时，通过访问守卫阻塞并等待配置空间、基址寄存器、复位、中断、电源管理和直接内存访问缓冲区导出等操作退出；恢复完成后放行。用户态启用后还可查询恢复事件状态，默认不支持恢复的变体驱动不受影响。
- 达到阈值的 patches（15 个，显示前 5）：
  - vfio/pci: Serialize generic device lifetime with recovery
  - vfio/pci: Serialize function reset with recovery
  - vfio/pci: Serialize ioeventfd writes with recovery
  - vfio/pci: Retry BAR faults after temporary recovery
  - vfio/pci: Serialize BAR and ROM access with recovery
  - ... 及其他 10 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260901093217.8539-2-skolothumtho@nvidia.com/

**▸ 组织：Red Hat**（2 patches）

**[SERIES] vfio/pci: fall back to platform ROM when pci_map_rom() fails** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-10-21
- 状态：社区讨论中
- 作者邮箱：Michael S. Tsirkin <mst@redhat.com>
- 概括：当 VFIO PCI 设备的 ROM BAR 存在但内容不可读（例如 GPU 未被系统固件初始化）时，原来在 BAR 映射失败后会直接停止，无法使用引导加载器保存的 ROM 或平台固件提供的 ACPI ROM 方法。现在在映射失败后先尝试引导加载器保存的 ROM，再尝试 ACPI ROM 方法，使这类设备的视频 BIOS 仍可通过 VFIO 读取。对某些原有行为保守处理，仅作为最后回退。
- 达到阈值的 patches（1 个，显示前 5）：
  - vfio/pci: read ROM via ACPI _ROM when hardware ROM is unreadable
- 来源：https://patchwork.kernel.org/project/kvm/patch/8ab8fdfe47a8d9c9f10680ddb4a03bccad43f7c5.1792566536.git.mst@redhat.com/

**[SERIES] Enable Qualcomm WiFi PCIe passthrough to VMs** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-10-11
- 状态：社区讨论中
- 作者邮箱：Jose Ignacio Tornos Martinez <jtornosm@redhat.com>
- 概括：为让高通 ath11k/ath12k WiFi 设备通过 PCIe 直通到虚拟机后能正常工作，新增高通 VFIO PCI 变体驱动：在主机侧将主机物理消息信号中断地址写入 PCI 扩展配置空间并用魔数签名标记，虚拟机内对应 WiFi 驱动优先发现并读取这些地址编程固件，而不是使用客户机侧的输入输出虚拟地址，从而避免中断无法送达；同时在两个 WiFi 驱动中增加全局复位后的链路恢复重试，以容忍虚拟化环境中的时序变化。
- 达到阈值的 patches（1 个，显示前 5）：
  - vfio/pci: Add qcom-vfio-pci variant driver
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261011074514.515894-3-jtornosm@redhat.com/

**▸ 组织：AMD**（1 patches）

**[RFC] vfio/pci: Block for the upstream bridge lock in vfio_pci_core_disable()**

- 日期：2026-09-08
- 状态：社区讨论中
- 作者邮箱：YuanShang <YuanShang.Mao@amd.com>
- 概括：在 SR-IOV 虚拟功能释放场景中，同一上游桥下的多个功能并发释放时，原先只有赢得桥锁的一个会复位，其余跳过复位直接交还，导致设备未复位且无日志。现改为阻塞获取上游桥锁，让并发释放的复位串行执行，保证每个功能都复位；拆多个功能时每个都要等待一次复位稳定时间。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260908080946.2235849-1-YuanShang.Mao@amd.com/

**▸ 组织：IBM**（1 patches）

**[v11,5/5] vfio-pci/zdev: Add VFIO FMB device features**

- 日期：2026-10-28
- 状态：社区讨论中
- 作者邮箱：Omar Elghoul <oelghoul@linux.ibm.com>
- 概括：为 zPCI 设备新增 VFIO 特性，把 FMB 测量功能透传给用户空间：用户可启用或禁用 FMB，并在启用后读取最新测量数据。该能力面向需要从用户态获取 zPCI 设备测量信息的直通场景。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261028154352.15108-6-oelghoul@linux.ibm.com/

---

### ◆ 子系统：VFIO Core（11 patches）

**▸ 组织：IBM**（2 patches）

**[v6,4/5] vfio/spapr_tce: Normalize EEH IOA error injection addresses**

- 日期：2026-10-23
- 状态：社区讨论中
- 作者邮箱：Narayana Murty N <nnmlinux@linux.ibm.com>
- 概括：在 IBM Power 的 sPAPR VFIO EEH 错误注入路径中，用户态可能传入主机 Linux BAR 资源地址，而固件平台后端期望 PCI/IOA 总线地址。现在对内存或 IO BAR 目标函数做地址归一化：已经是总线地址则保持不变，是资源地址则借助 BAR 相对偏移转换为总线地址；地址和掩码均为零的无地址注入直接透传。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261023073642.59657-5-nnmlinux@linux.ibm.com/

**[v2] vfio: Use file-based reference counting for KVM**

- 日期：2026-09-03
- 状态：社区讨论中
- 作者邮箱：Steffen Eiden <seiden@linux.ibm.com>
- 概括：在 VFIO 与 KVM 虚拟机生命周期绑定的场景中，原先手动获取函数指针并跟踪模块引用，设备还要保存释放函数指针，管理复杂。现改为在内核接口传递虚拟机文件、由内核文件引用计数统一处理，组和设备各自持有引用，简化代码并移除 KVM 对外导出的符号，为后续并行加载多个 KVM 模块创造条件。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260903-vfio-v2-1-ef4cd4190ae7@linux.ibm.com/

**▸ 组织：NVIDIA**（2 patches）

**[v2,12/12] vfio/nvidia-vgpu: add the Rust VFIO variant driver**

- 日期：2026-10-23
- 状态：社区讨论中
- 作者邮箱：Simon Song <xinmengs@nvidia.com>
- 概括：为 NVIDIA vGPU 虚拟功能新增 Rust 编写的 VFIO PCI 变体驱动，配合 nova-core 管理实例：首次打开时创建实例，最后一次关闭时销毁；暴露分配的设备与子系统标识，限制分配的 BAR1 范围，并协调固件复位与 PCI 复位。无 Nova vGPU 接口的设备继续走普通 PCI 透传。构建系统扩展导出所需 Rust 符号，使该驱动能编译并链接 nova-core。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261023154009.2246627-13-xinmengs@nvidia.com/

**[12/13] vfio/nvidia-vgpu: add the NVIDIA vGPU VFIO variant driver**

- 日期：2026-09-05
- 状态：社区讨论中
- 作者邮箱：Zhi Wang <zhiw@nvidia.com>
- 概括：为 NVIDIA vGPU 虚拟功能新增 VFIO PCI 变体驱动，仅允许通过显式覆盖绑定且只接受虚拟功能，将实例打开、复位和关闭委托给 PF 侧 nova-core 协调；配置空间读取向用户展示固件选定的设备与子系统 ID，并按分配规格调整 BAR1 大小，其余操作沿用 vfio-pci-core。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260905081116.106613-13-zhiw@nvidia.com/

**▸ 组织：Amazon**（2 patches）

**vfio: Create the group chardev outside vfio.group_lock**

- 日期：2026-09-11
- 状态：社区讨论中
- 作者邮箱：Sakac, Pavol <sakacpav@amazon.de>
- 概括：在并行设备探测触发大量 VFIO 组同时注册时，原先组字符设备创建一直持有全局组锁，设备添加和事件广播会串行化无关创建，使该锁成为主要竞争点。现将分配、命名和字符设备注册移出锁，只在锁内预留组身份并延迟发布事件，失败构建不再广播事件，从而消除并行探测启用窗口中的锁竞争。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260911-vfopt-s4-v1-0-98ba1d2ef7ab@amazon.de/

**[RFC,8/8] vfio: Opt the group and vfio-dev class devices into staged sysfs**

- 日期：2026-09-11
- 状态：社区讨论中
- 作者邮箱：Sakac, Pavol <sakacpav@amazon.de>
- 概括：在大量虚拟功能并发注册的场景中，VFIO 组字符设备和类设备每次创建时走实时系统设备模型路径，会使并发注册在内核系统设备模型锁上排队。现将这两类设备选择分阶段系统设备模型注册，目录一次性发布，避免任何消费者看到半构建状态，并缓解并发注册带来的锁竞争。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260911174414.97060-8-sakacpav@amazon.de/

**▸ 组织：Google**（2 patches）

**[SERIES] vfio: Add support for platform devices** （cover letter，6/7 个 patch 达到代码量阈值）

- 日期：2026-10-24
- 状态：社区讨论中
- 作者邮箱：Mostafa Saleh <smostafa@google.com>
- 概括：为 kvftool 虚拟机管理器新增 VFIO 平台设备直通能力，使用户可通过新命令行选项将系统平台总线下的设备（事先绑定到 VFIO 平台驱动）分配给虚拟机。原先只支持 PCI 设备直通；现在预留客户机地址空间，映射设备的 MMIO 区域并生成设备树节点，支持边沿触发中断，并允许用户提供设备树模板复制兼容属性等绑定信息，便于客户机驱动匹配。
- 达到阈值的 patches（6 个，显示前 5）：
  - vfio: Factor out wired IRQ setup and teardown
  - vfio: Support edge-triggered wired IRQs
  - vfio: Add basic support for vfio-platform
  - vfio: Reserve guest address space for VFIO platform
  - vfio: platform: Add interrupts support
  - ... 及其他 1 个 patch
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261024161902.2093581-2-smostafa@google.com/

**[SERIES] iommu: Introduce Page Table Observability Framework** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-10-01
- 状态：社区讨论中
- 作者邮箱：Pranjal Shrivastava <praan@google.com>
- 概括：新增 IOMMU 页表可观测性框架，把 IO 页表页面数归属到具体 IOMMU 域，并在 VFIO 容器和 iommufd 的 fdinfo 中暴露 iommu-nr-pages 字段，使用户可查看各设备或容器实际占用的 IO 页表页数。仅通用页表库实现的域会计数，任一附加域不支持时省略该字段，避免报告部分计数；自测还验证了卸载映射后页数暂不下降的当前行为。
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio/type1: Expose IO page table usage via fdinfo
  - vfio/selftests: Add observability test for IO page table usage
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261001224531.765278-5-praan@google.com/

**▸ 组织：Individual Contributor**（1 patches）

**vfio/nvgrace-gpu: Skip PFN registration for empty memory regions**

- 日期：2026-09-25
- 状态：社区讨论中
- 作者邮箱：Andrea Parri <parri.andrea@gmail.com>
- 概括：针对 vfio/nvgrace-gpu 设备，在 ACPI 内存属性缺失或 C2C 链路断开的回退模式下，使用内存区域长度为零但仍被注册，导致页帧号地址空间覆盖整个范围且关闭路径无法注销；第二次打开返回 EBUSY，解绑后残留节点可能在后续注册或内存错误处理时访问已释放内存，错误也被记为已恢复而非忽略。现在仅当使用内存区域长度非零时注册和注销该区域，回退模式不再注册，避免残留和误报。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260925161024.189771-1-parri.andrea@gmail.com/

**▸ 组织：ARM**（1 patches）

**[RFC,v2,12/15] vfio: Support VFIO devices that access the CPU MMU**

- 日期：2026-10-15
- 状态：社区讨论中
- 作者邮箱：Ryan Roberts <ryan.roberts@arm.com>
- 概括：新增一类不经 IOMMU、由 CPU MMU 完成 DMA 的 VFIO 设备支持。这类设备不绑定 iommufd 接口、不使用 VFIO 容器，打开时不强制要求容器，设置容器会被拒绝；虚拟机管理器因需要设备特定知识创建虚拟设备，知道不必分配容器。适用于与 CPU 共享页表的设备直通场景。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261015142552.4128028-13-ryan.roberts@arm.com/

**▸ 组织：归属待核实（openai.com）**（1 patches）

**vfio: Publish the container after all fallible initialization**

- 日期：2026-10-30
- 状态：社区讨论中
- 作者邮箱：Kyle Zeng <kylebot@openai.com>
- 概括：在 VFIO 模块首次自动加载的竞态场景中，原先容器设备文件在初始化全部成功前发布，后续初始化失败时已打开文件可能引用已释放模块内存，造成内核越界。现将容器初始化作为最后可失败步骤，先注册无 IOMMU 后端再注册容器设备，失败时反向回收；一旦用户能打开容器文件，模块初始化便不会再失败。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20261030042337.74512-1-kylebot@openai.com/

---

### ◆ 子系统：VFIO AP (s390)（1 patches）

**▸ 组织：IBM**（1 patches）

**[v6,1/5] s390/vfio-ap: Fix leak of pinned NIB and registered GISC in vfio_ap_irq_enable/disable()**

- 日期：2026-09-04
- 状态：社区讨论中
- 作者邮箱：Anthony Krowiak <akrowiak@linux.ibm.com>
- 概括：针对 s390 加密适配器队列透传，修复启用或禁用中断时对固定通知指示字节页和客户机中断子类的管理：禁用命令是异步的，若在中断位清零前释放固定页，硬件后续 DMA 写入可能落到已被新所有者占用的内存。现在先等待中断位清零，超时则故意保留固定页和中断注册以避免野写入；只有确认队列不再工作时才立即释放。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260904093435.1161402-2-akrowiak@linux.ibm.com/

---

### ◆ 子系统：VFIO Migration（1 patches）

**▸ 组织：Kernel.org**（1 patches）

**[RFC,POC,31/50] vfio: install the migration data descriptor when the ioctl returns**

- 日期：2026-09-15
- 状态：社区讨论中
- 作者邮箱：Christian Brauner <brauner@kernel.org>
- 概括：调整 VFIO 迁移数据文件描述符的安装时机，改为在迁移状态获取 ioctl 返回时通过新的描述符准备机制完成安装，错误和资源回收依赖文件关闭路径统一处理，避免原先手动分配、安装和回退的分散逻辑。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260915-work-fd-reserve-unify-folded-v1-31-4d5217d6b246@kernel.org/

---

### ◆ 子系统：VFIO CCW (s390)（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[v1] vfio/ccw: Flush notoper_work before returning from reset**

- 日期：2026-09-22
- 状态：社区讨论中
- 作者邮箱：Yuho Choi <oss.patchbox@gmail.com>
- 概括：在 s390 通道设备 DMA 解除映射时，若子通道无法禁用或静默并进入非操作状态，释放通道程序页面的工作只排队异步执行，回调返回时页面仍被固定，可能导致解除映射重试耗尽并触发内核严重错误。现于复位返回前刷新该异步工作，确保页面解除固定完成，正常路径因工作未排队立即返回而不受影响。
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260922164928.477669-1-oss.patchbox@gmail.com/

---

### ◆ 子系统：VFIO Selftests（1 patches）

**▸ 组织：Google**（1 patches）

**[SERIES] Introduce vfio_dma_mapping_perf_test** （cover letter，3/4 个 patch 达到代码量阈值）

- 日期：2026-09-10
- 状态：社区讨论中
- 作者邮箱：Aaron Lewis <aaronlewis@google.com>
- 概括：新增一个 VFIO DMA 映射性能自测程序，直接报告建立内存映射、DMA 映射、DMA 解映射和解除内存映射各阶段的耗时，而不是设定固定延迟阈值造成结果不稳定；同时支持通过 IOMMUFD 按内存文件方式映射，并允许命令行指定区域大小，还在解映射辅助函数中统一检查整个区域是否已完整解除映射。
- 达到阈值的 patches（3 个，显示前 5）：
  - vfio: selftests: Introduce vfio_dma_mapping_perf_test
  - vfio: selftests: Add memfd test to vfio_dma_mapping_perf_test
  - vfio: selftests: Allow a size for vfio_dma_mapping_perf_test
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260910153326.3085937-2-aaronlewis@google.com/

---

### ◆ 子系统：VFIO IOMMUFD（1 patches）

**▸ 组织：Kernel.org**（1 patches）

**[SERIES] iommufd: Infrastructure for vIOMMU creation for confidential guests and guest TSM requests** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-09-17
- 状态：社区讨论中
- 作者邮箱：Aneesh Kumar K.V <aneesh.kumar@kernel.org>
- 概括：将 VFIO 缓存 KVM 的方式从内核指针改为虚拟机文件引用，并在字符设备已打开时提前拒绝重复绑定，防止失败的二次绑定清除设备级虚拟机关联；随后为 iommufd 增加 vIOMMU 提供者注册与查找、保存虚拟机引用，并新增收到客户机 TSM 命令后转发的虚拟设备接口，用于机密客户机场景，同时移除旧的 PCI/TSM 请求接口并调整上下文引用计数。
- 达到阈值的 patches（2 个，显示前 5）：
  - vfio: cache KVM VM file references instead of raw struct kvm pointers
  - vfio: cdev: Reject duplicate bind before updating KVM file
- 来源：https://patchwork.kernel.org/project/kvm/patch/20260917140159.1163281-2-aneesh.kumar@kernel.org/

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

*报告由 Linux Patches Tracker 自动生成 | 2026-11-11 15:36:23*
