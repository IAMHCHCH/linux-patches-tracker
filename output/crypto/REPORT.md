# Linux Crypto 子系统 Patch 追踪报告

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
| 社区讨论中 | 55 | 57.9% |
| 已合入 | 36 | 37.9% |
| **总计** | **95** | **100%** |

### 按组织分类（TOP 15）

| 组织 | 数量 | 占比 |
|------|------|------|
| Individual Contributor | 32 | 33.7% |
| Linux Community | 17 | 17.9% |
| Kernel.org | 16 | 16.8% |
| Intel | 7 | 7.4% |
| Baylibre | 3 | 3.2% |
| Qualcomm | 3 | 3.2% |
| Bootlin | 3 | 3.2% |
| Amazon | 3 | 3.2% |
| AMD | 2 | 2.1% |
| NXP | 2 | 2.1% |
| StarFive | 2 | 2.1% |
| Huawei | 2 | 2.1% |
| Google | 1 | 1.1% |
| NVIDIA | 1 | 1.1% |
| SUSE | 1 | 1.1% |

### 按子系统分类

| 子系统 | 数量 | 占比 |
|--------|------|------|
| General Crypto | 53 | 55.8% |
| HWRNG | 11 | 11.6% |
| ICE (Qualcomm) | 6 | 6.3% |
| ECC | 6 | 6.3% |
| AF_ALG API | 4 | 4.2% |
| Skcipher | 4 | 4.2% |
| Talitos | 4 | 4.2% |
| CCP/SEV (AMD) | 2 | 2.1% |
| DRBG | 2 | 2.1% |
| Authenc | 1 | 1.1% |
| CESA (Marvell) | 1 | 1.1% |
| Test Manager | 1 | 1.1% |
## 已合入 Patches

### ◆ 子系统：General Crypto（20 patches）

**▸ 组织：Linux Community**（7 patches）

**crypto: powerpc/aes - use min in ppc_{ecb,cbc,ctr,xts}_crypt**

- 日期：2026-05-27
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260527141146.1230672-3-thorsten.blum@linux.dev/

**crypto: use two-argument strscpy where destination size is known**

- 日期：2026-05-25
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260525103038.825690-4-thorsten.blum@linux.dev/

**crypto: octeontx - use strscpy_pad in ucode_load_store**

- 日期：2026-05-20
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260520100031.246078-2-thorsten.blum@linux.dev/

**crypto: atmel-sha - use memcpy_and_pad to simplify hmac_setup**

- 日期：2026-05-16
- 状态：已合入
- 概括：简化代码逻辑，减少不必要的复杂度，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260516234211.1131137-2-thorsten.blum@linux.dev/

**crypto: atmel - use min3 to simplify atmel_sha_append_sg**

- 日期：2026-05-12
- 状态：已合入
- 概括：简化代码逻辑，减少不必要的复杂度，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260512145123.303311-3-thorsten.blum@linux.dev/

**crypto: use designated initializers for report structs**

- 日期：2026-05-08
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260508105717.472043-3-thorsten.blum@linux.dev/

**crypto: artpec6 - refactor crypto_setup_out_descr for readability**

- 日期：2026-05-06
- 状态：已合入
- 概括：重构重新组织代码结构以提升可读性和可维护性，提升代码的可读性和可维护性，为后续功能迭代奠定更清晰的基础
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260506091627.177426-3-thorsten.blum@linux.dev/

**▸ 组织：Intel**（4 patches）

**crypto: qat - add KPT support for GEN6 devices**

- 日期：2026-05-26
- 状态：已合入
- 概括：新增kpt support，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260526092839.432243-1-nitesh.venkatesh@intel.com/

**crypto: qat - use pci logging variants for PCI-specific messages**

- 日期：2026-05-20
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260520125150.211802-1-ahsan.atta@intel.com/

**[SERIES] crypto: qat - add sysfs PCI reset support for QAT devices** （cover letter，5/6 个 patch 达到代码量阈值）

- 日期：2026-05-13
- 状态：已合入
- 概括：新增sysfs pci reset support，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（5 个，显示前 5）：
  - crypto: qat - keep VFs enabled during reset
  - crypto: qat - centralize bus master enable
  - crypto: qat - skip restart for down devices
  - crypto: qat - factor out AER reset helpers
  - crypto: qat - handle sysfs-triggered reset callbacks
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/9d9faa95f1cea5e77afc7f570e478ff0cb9cdc98.1778685152.git.ahsan.atta@intel.com/

**[SERIES] crypto: qat - remove unused ioctl interface** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-05-11
- 状态：已合入
- 概括：移除unused ioctl interface，清理冗余或过时的代码，精简代码库规模，降低后续维护的复杂度和引入回归问题的风险
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: qat - remove unused character device and IOCTLs
  - crypto: qat - rename adf_ctl_drv.c to adf_module.c
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260511100854.29474-2-giovanni.cabiddu@intel.com/

**▸ 组织：Individual Contributor**（3 patches）

**crypto: rng - Free default RNG on module exit**

- 日期：2026-06-04
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/aiD_flpAvcwS4XnO@gondor.apana.org.au/

**crypto: amcc - convert irq_of_parse_and_map to platform_get_irq**

- 日期：2026-06-02
- 状态：已合入
- 概括：迁移irq_of_parse_and_map to platform_get_irq，适配新的接口规范
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260602014645.522137-1-rosenp@gmail.com/

**[v2] crypto: ccp: sev-dev-tsm: bail out early when pdev->bus is NULL**

- 日期：2026-05-07
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260507140608.8612-1-sozdayvek@gmail.com/

**▸ 组织：Kernel.org**（3 patches）

**crypto: exynos-rng - Remove exynos-rng driver**

- 日期：2026-05-31
- 状态：已合入
- 概括：移除exynos-rng driver，清理冗余或过时的代码，精简代码库规模，降低后续维护的复杂度和引入回归问题的风险
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260531175932.32171-1-ebiggers@kernel.org/

**crypto: loongson - Remove broken and unused loongson-rng**

- 日期：2026-05-29
- 状态：已合入
- 概括：修复and unused loongson-rng，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260529233208.8703-1-ebiggers@kernel.org/

**crypto: loongson - Select CRYPTO_RNG**

- 日期：2026-05-22
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260522022525.12976-1-ebiggers@kernel.org/

**▸ 组织：Google**（1 patches）

**crypto: ccp: Treat zero-length cert chain as query for blob lengths**

- 日期：2026-05-04
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260504222812.2339526-1-seanjc@google.com/

**▸ 组织：NVIDIA**（1 patches）

**[2/2] crypto: tegra - Don't touch bo refcount in host1x bo pin/unpin**

- 日期：2026-05-15
- 状态：已合入
- 概括：限制touch bo refcount，增加条件判断和安全保护逻辑，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260515-host1x-bocache-leak-v1-2-a0375f68aeab@nvidia.com/

**▸ 组织：Huawei**（1 patches）

**[SERIES] crypto: hisilicon/qm - support function reset and VF isolation** （cover letter，3/6 个 patch 达到代码量阈值）

- 日期：2026-05-18
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（3 个，显示前 5）：
  - crypto: hisilicon/qm - place the interrupt status interface after the PM usage counter
  - crypto: hisilicon/qm - allow VF devices to query hardware isolation status
  - crypto: hisilicon/qm - support doorbell enable control
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260518142956.3593934-6-wuzongyu1@huawei.com/

---

### ◆ 子系统：ICE (Qualcomm)（5 patches）

**▸ 组织：Baylibre**（2 patches）

**[SERIES] crypto - Rework i2c_device_id initialisation** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-05-20
- 状态：已合入
- 概括：重写重新设计部分实现，优化数据流和处理逻辑，持续改进代码质量和功能完备性
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: atmel-sha204a - Use named initializers for struct i2c_device_id
  - crypto: atmel-ecc - Use named initializers for struct i2c_device_id
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/d0fc3069860f9e31122c1af635a1114dd2c443cf.1779260113.git.u.kleine-koenig@baylibre.com/

**crypto: ccp - Define pci_device_ids using named initializers**

- 日期：2026-05-04
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260504152421.2147027-2-u.kleine-koenig@baylibre.com/

**▸ 组织：Qualcomm**（1 patches）

**crypto: Move MODULE_DEVICE_TABLE next to the table itself**

- 日期：2026-05-05
- 状态：已合入
- 概括：移动代码到更合适的位置，优化代码组织结构，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260505102948.191683-2-krzysztof.kozlowski@oss.qualcomm.com/

**▸ 组织：Intel**（1 patches）

**crypto: qat - protect service table iterations with service_lock**

- 日期：2026-05-20
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260520124155.211119-1-ahsan.atta@intel.com/

**▸ 组织：Linux Community**（1 patches）

**crypto: qat - simplify adf_service_mask_to_string helper**

- 日期：2026-05-27
- 状态：已合入
- 概括：简化代码逻辑，减少不必要的复杂度，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260527174655.1390543-3-thorsten.blum@linux.dev/

---

### ◆ 子系统：HWRNG（3 patches）

**▸ 组织：Kernel.org**（2 patches）

**[SERIES] Xilinx TRNG fix and simplification** （cover letter，2/4 个 patch 达到代码量阈值）

- 日期：2026-05-31
- 状态：已合入
- 概括：修复and simplification，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: xilinx-trng - Replace crypto_drbg_ctr_df() with HMAC-SHA512
  - hwrng: xilinx - Move xilinx-rng into drivers/char/hw_random/
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260531191738.55843-2-ebiggers@kernel.org/

**[SERIES] HiSilicon TRNG fix and simplification** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-05-30
- 状态：已合入
- 概括：修复and simplification，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: hisi-trng - Remove crypto_rng interface
  - hwrng: hisi-trng - Move hisi-trng into drivers/char/hw_random/
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260530202624.20768-2-ebiggers@kernel.org/

**▸ 组织：Linux Community**（1 patches）

**[SERIES] hwrng: core - drop unnecessary forward declarations** （cover letter，3/4 个 patch 达到代码量阈值）

- 日期：2026-05-05
- 状态：已合入
- 概括：移除unnecessary forward declarations，清理冗余或过时的代码，精简代码库规模，降低后续维护的复杂度和引入回归问题的风险
- 达到阈值的 patches（3 个，显示前 5）：
  - hwrng: core - use bool for wait parameter in rng_get_data
  - hwrng: core - use MAX to simplify RNG_BUFFER_SIZE
  - hwrng: core - use sysfs_emit_at in rng_available_show
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260505094555.158017-7-thorsten.blum@linux.dev/

---

### ◆ 子系统：DRBG（2 patches）

**▸ 组织：Kernel.org**（2 patches）

**crypto: drbg - Rename MAX_ADDTL => MAX_ADDTL_BYTES**

- 日期：2026-05-06
- 状态：已合入
- 概括：重命名符号或函数以更清晰地表达其用途和语义，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260506000217.70738-1-ebiggers@kernel.org/

**crypto: drbg - Remove support for "prediction resistance"**

- 日期：2026-05-06
- 状态：已合入
- 概括：移除support，清理冗余或过时的代码，精简代码库规模，降低后续维护的复杂度和引入回归问题的风险
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260506000258.70807-1-ebiggers@kernel.org/

---

### ◆ 子系统：Authenc（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[v2] crypto: authencesn - Use memcpy_from/to_sglist**

- 日期：2026-05-02
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/afWDVpH2ba-DVpkT@gondor.apana.org.au/

---

### ◆ 子系统：AF_ALG API（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: af_alg - Cap AEAD AD length to 0x80000000**

- 日期：2026-05-05
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/afmyNZxW3QB33LXi@gondor.apana.org.au/

---

### ◆ 子系统：ECC（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[v2] crypto: ecc - Unbreak the build on arm with CONFIG_KASAN_STACK=y**

- 日期：2026-05-06
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/7e3d64a53efb28740b32d1f934e78c10086208ab.1778073318.git.lukas@wunner.de/

---

### ◆ 子系统：CESA (Marvell)（1 patches）

**▸ 组织：Linux Community**（1 patches）

**crypto: cesa - use max to simplify mv_cesa_probe**

- 日期：2026-05-12
- 状态：已合入
- 概括：简化代码逻辑，减少不必要的复杂度，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260512133415.302370-3-thorsten.blum@linux.dev/

---

### ◆ 子系统：Talitos（1 patches）

**▸ 组织：Bootlin**（1 patches）

**[SERIES] crypto: talitos - fix several issues in the Freescale talitos crypto driver** （cover letter，6/11 个 patch 达到代码量阈值）

- 日期：2026-05-07
- 状态：已合入
- 概括：修复several issues，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（6 个，显示前 5）：
  - crypto: talitos - add chaining of arbitrary number of descriptor for the SEC1
  - crypto: talitos - move dma unmapping code in flush_channel() into a standalone dma_unmap_request() function
  - crypto: talitos - move dma mapping code in talitos_submit() into a standalone dma_map_request() function
  - crypto: talitos - move code in current_desc_hdr() into a standalone function
  - crypto: talitos/hash - use descriptor chaining for SEC1 instead of workqueue
  - ... 及其他 1 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260507-bootlin_test-7-1-rc1_sec_bugfix-v3-1-c98d7589b942@bootlin.com/

---

### ◆ 子系统：CCP/SEV (AMD)（1 patches）

**▸ 组织：Kernel.org**（1 patches）

**[SERIES] SEV re-initialization fixes** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-05-04
- 状态：已合入
- 概括：修复相关功能缺陷或逻辑错误，确保操作行为符合预期规范，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（4 个，显示前 5）：
  - crypto/ccp: Do not initialize SNP for SEV ioctls
  - crypto/ccp: Do not initialize SNP for ioctl(SNP_COMMIT)
  - crypto/ccp: Do not initialize SNP for ioctl(SNP_VLEK_LOAD)
  - crypto/ccp: Do not initialize SNP for ioctl(SNP_CONFIG)
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260504165147.1615643-2-tycho@kernel.org/

---

## 社区讨论中 Patches

### ◆ 子系统：General Crypto（33 patches）

**▸ 组织：Individual Contributor**（16 patches）

**[SERIES] crypto: cmh - add CRI CryptoManager Hub driver** （cover letter，15/15 个 patch 达到代码量阈值）

- 日期：2026-06-25
- 状态：社区讨论中
- 概括：新增cri cryptomanager hub driver，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（15 个，显示前 5）：
  - crypto: cmh - add ECDH/X25519 kpp
  - crypto: cmh - add AES skcipher/aead/cmac
  - crypto: cmh - add SHA-2/SHA-3/SHAKE ahash
  - crypto: cmh - add DRBG hwrng
  - crypto: cmh - add ECDSA/SM2 sig
  - ... 及其他 10 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260625173328.1140487-15-skrishnamoorthy@rambus.com/

**[v2] crypto: virtio - bound the akcipher result length**

- 日期：2026-06-22
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260622-b4-disp-3a2c09a8-v2-1-d1a809281db4@proton.me/

**crypto: virtio - bound the device-reported akcipher result**

- 日期：2026-06-21
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260620-b4-disp-27caeeac-v1-1-956e8f9c4f01@proton.me/

**crypto: amcc: move ioremapping up**

- 日期：2026-06-14
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260614012917.70772-1-rosenp@gmail.com/

**[SERIES] crypto: qat - bound the live migration import parser** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-06-14
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: qat - add KUnit coverage for the migration import parser
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260614130619.2519534-2-michael.bommarito@gmail.com/

**crypto: ti - Use list_first_entry_or_null() in dthe_get_dev()**

- 日期：2026-06-13
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260613085858.32580-1-mertsftl@gmail.com/

**crypto: s5p-sss - correct CONFIG_CRYPTO_DEV_EXYNOS_RNG macro name in comment**

- 日期：2026-06-13
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260613223648.119694-1-enelsonmoore@gmail.com/

**crypto: amcc - embed pdr_uinfo as flexible array in crypto4xx_device**

- 日期：2026-06-13
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260613234559.20934-1-rosenp@gmail.com/

**crypto: amcc - check ppc4xx_trng_probe() return value**

- 日期：2026-06-02
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260602014553.522044-1-rosenp@gmail.com/

**[2/4] crypto: rockchip: Add RK356x/RK3588 cryptographic offloader driver**

- 日期：2026-05-30
- 状态：社区讨论中
- 概括：新增rk356x/rk3588 cryptographic offloader driver，扩展功能特性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260530160704.3453555-3-dawidro@gmail.com/

**[SERIES] Add support for hashing algorithms in TI DTHE V2** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-05-26
- 状态：社区讨论中
- 概括：新增支持 hashing algorithms in ti dthe v2，扩展框架的硬件兼容性和功能覆盖范围
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: ti - Add support for SHA224/256/384/512 in DTHEv2 driver
  - crypto: ti - Add support for HMAC in DTHEv2 Hashing Engine driver
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260526094355.555712-2-t-pratham@ti.com/

**[SERIES] crypto: eip93: fix request lifetime and completion handling** （cover letter，4/6 个 patch 达到代码量阈值）

- 日期：2026-05-24
- 状态：社区讨论中
- 概括：修复request lifetime and completi，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（4 个，显示前 5）：
  - crypto: eip93: reject HMAC requests before setkey
  - crypto: eip93: order result descriptor reads after PE_READY
  - crypto: eip93: use request-local SA records for cipher requests
  - crypto: eip93: handle request ID exhaustion
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260524194528.3666383-2-hurryman2212@gmail.com/

**[2/3] crypto: inside-secure: add EIP93 ESP packet backend**

- 日期：2026-05-23
- 状态：社区讨论中
- 概括：新增eip93 esp packet backend，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260523121522.3023992-3-hurryman2212@gmail.com/

**[1/2] crypto: Delete Qualcomm crypto engine driver**

- 日期：2026-05-23
- 状态：社区讨论中
- 概括：移除qualcomm crypto engine driver，清理冗余或过时的代码，精简代码库规模，降低后续维护的复杂度和引入回归问题的风险
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260523-delete-qce-v1-1-86105cd7f406@gmail.com/

**[SERIES] crypto: atmel - introduce shared i2c core client management and capability-based selection framework** （cover letter，8/12 个 patch 达到代码量阈值）

- 日期：2026-05-22
- 状态：社区讨论中
- 概括：引入shared i2c core client management and capability-based selection framework，扩展框架的功能范围
- 达到阈值的 patches（8 个，显示前 5）：
  - crypto: atmel-ecc - rename driver_data before moving it into atmel-i2c
  - crypto: atmel - rename atmel_ecc_driver_data to atmel_i2c_client_mgmt
  - crypto: atmel-sha204a - switch to module_i2c_driver
  - crypto: atmel-ecc - switch to module_i2c_driver
  - crypto: atmel-ecc - fix multi-device kpp registration
  - ... 及其他 3 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260522230134.32414-5-l.rubusch@gmail.com/

**[SERIES] crypto: atmel - refactor common i2c support and add SHA256 ahash support** （cover letter，8/12 个 patch 达到代码量阈值）

- 日期：2026-05-12
- 状态：社区讨论中
- 概括：新增sha256 ahash support，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（8 个，显示前 5）：
  - crypto: atmel - move capability-based client allocation into i2c core
  - crypto: atmel - add per-device timing and match-data driven configuration
  - crypto: atmel - move RNG support into common i2c core
  - crypto: atmel - move EEPROM access support into common i2c core
  - crypto: atmel - expose CONFIG zone through sysfs
  - ... 及其他 3 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260512224349.64621-2-l.rubusch@gmail.com/

**▸ 组织：Kernel.org**（6 patches）

**[SERIES] x86: Remove cpu_has_xfeatures() and add AVX-512 xor_gen()** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-06-26
- 状态：社区讨论中
- 概括：新增avx-512 xor_gen()，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: x86 - Stop using cpu_has_xfeatures()
  - lib/crypto: x86: Stop using cpu_has_xfeatures()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260626043731.319287-4-ebiggers@kernel.org/

**[SERIES] Finish removing crypto_rng from drivers/crypto/** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-06-15
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（3 个，显示前 5）：
  - crypto: sun8i-ce - Remove crypto_rng interface
  - crypto: sun8i-ss - Remove crypto_rng interface
  - crypto: caam - Remove crypto_rng interface
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260615224131.69370-6-ebiggers@kernel.org/

**lib/crypto: gf128hash: mark clmul32() as noinline_for_stack**

- 日期：2026-06-11
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260611125952.3387258-1-arnd@kernel.org/

**[SERIES] ML-KEM and X-Wing support** （cover letter，5/5 个 patch 达到代码量阈值）

- 日期：2026-05-25
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（5 个，显示前 5）：
  - lib/crypto: mlkem: Add ML-KEM-768 and ML-KEM-1024 support
  - lib/crypto: xwing: Add support for X-Wing KEM
  - lib/crypto: mlkem: Add KUnit tests for ML-KEM
  - lib/crypto: xwing: Add KUnit tests for X-Wing KEM
  - lib/crypto: mlkem: Add FIPS 140-3 tests
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260525184403.101818-2-ebiggers@kernel.org/

**[v8,2/3] crypto: Migrate TPMKey ASN.1 objects from trusted-keys**

- 日期：2026-05-24
- 状态：社区讨论中
- 概括：迁移tpmkey asn.1 objects from trusted-keys，适配新的接口规范，保持子系统与内核主线的兼容性，适应 API 和框架的演进方向
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260524051519.3708075-3-jarkko@kernel.org/

**[v2] lib/crypto: powerpc/md5: Drop powerpc optimized MD5 code**

- 日期：2026-05-06
- 状态：社区讨论中
- 概括：移除powerpc optimized md5 code，清理冗余或过时的代码，精简代码库规模，降低后续维护的复杂度和引入回归问题的风险
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260506030005.9698-1-ebiggers@kernel.org/

**▸ 组织：Linux Community**（4 patches）

**[v2] crypto: atmel-tdes - use scatterlist length before DMA mapping**

- 日期：2026-06-11
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260611103633.458381-3-thorsten.blum@linux.dev/

**[SERIES] crypto: use 2-arg strscpy where destination size is known** （cover letter，6/6 个 patch 达到代码量阈值）

- 日期：2026-06-05
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（6 个，显示前 5）：
  - crypto: use 2-arg strscpy where destination size is known
  - crypto: cavium - use 2-arg strscpy where destination size is known
  - crypto: hisilicon - use 2-arg strscpy where destination size is known
  - crypto: ccp - use 2-arg strscpy where destination size is known
  - crypto: octeontx - use 2-arg strscpy where destination size is known
  - ... 及其他 1 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260605231056.1622060-9-thorsten.blum@linux.dev/

**crypto: omap - use min3 to simplify omap_crypto_copy_data**

- 日期：2026-06-04
- 状态：社区讨论中
- 概括：简化代码逻辑，减少不必要的复杂度，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260604001035.1256238-3-thorsten.blum@linux.dev/

**crypto: atmel-tdes - use min3 to simplify sg_copy and crypt_start**

- 日期：2026-05-25
- 状态：社区讨论中
- 概括：简化代码逻辑，减少不必要的复杂度，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260525092927.818586-2-thorsten.blum@linux.dev/

**▸ 组织：NXP**（2 patches）

**[v7,9/9] crypto: atmel: Use dmaengine_prep_config_sg() API**

- 日期：2026-05-21
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260521-dma_prep_config-v7-9-1f73f4899883@nxp.com/

**[v5,9/9] crypto: atmel: Use dmaengine_prep_config_single() API**

- 日期：2026-05-12
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260512-dma_prep_config-v5-9-26865bf7d935@nxp.com/

**▸ 组织：Intel**（2 patches）

**crypto: qat - cancel work on re-enable SR-IOV timeout**

- 日期：2026-06-08
- 状态：社区讨论中
- 概括：启用之前被禁用或条件编译的功能特性，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260608150104.135313-1-giovanni.cabiddu@intel.com/

**crypto: qat - clear AES key schedule from stack**

- 日期：2026-06-08
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260608150441.136014-1-giovanni.cabiddu@intel.com/

**▸ 组织：Qualcomm**（2 patches）

**[SERIES] crypto/dmaengine: qce: introduce BAM locking and use DMA for register I/O** （cover letter，6/8 个 patch 达到代码量阈值）

- 日期：2026-06-29
- 状态：社区讨论中
- 概括：引入bam locking and use dma for register i/o，扩展框架的功能范围
- 达到阈值的 patches（6 个，显示前 5）：
  - crypto: qce - Cancel work on device detach
  - crypto: qce - Include algapi.h in the core.h header
  - crypto: qce - Simplify arguments of devm_qce_dma_request()
  - crypto: qce - Use existing devres APIs in devm_qce_dma_request()
  - crypto: qce - Map crypto memory for DMA
  - ... 及其他 1 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260629-qcom-qce-cmd-descr-v20-7-56f67da84c05@oss.qualcomm.com/

**[SERIES] crypto: qce - Fix crypto self-test failures** （cover letter，5/8 个 patch 达到代码量阈值）

- 日期：2026-06-22
- 状态：社区讨论中
- 概括：修复crypto self-test failures，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（5 个，显示前 5）：
  - crypto: qce - Remove unsafe/deprecated algorithms
  - crypto: qce - Reject empty messages for AES-XTS
  - crypto: qce - Use a fallback for AES-CTR with a partial final block
  - crypto: qce - Use a fallback for CCM with a partial final block
  - crypto: qce - Use fallback for CCM with a fragmented payload
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260622-qce-fix-self-tests-v4-1-4f82ffa716c6@oss.qualcomm.com/

**▸ 组织：Huawei**（1 patches）

**[SERIES] crypto: hisilicon - improve backlog handling** （cover letter，3/5 个 patch 达到代码量阈值）

- 日期：2026-05-28
- 状态：社区讨论中
- 概括：改进backlog handling，提升健壮性和性能，提升代码的可读性和可维护性，为后续功能迭代奠定更清晰的基础
- 达到阈值的 patches（3 个，显示前 5）：
  - crypto: hisilicon/zip - add backlog support for zip
  - crypto: hisilicon/hpre - implement full backlog support for hpre driver
  - crypto: hisilicon/sec2 - restore iv for ctr mode
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260528115531.174593-2-wuzongyu1@huawei.com/

---

### ◆ 子系统：HWRNG（7 patches）

**▸ 组织：Individual Contributor**（3 patches）

**hwrng: xilinx-trng: propagate timeout before any data is read**

- 日期：2026-06-23
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260623060728.18906-1-pengpeng@iscas.ac.cn/

**[v4] hwrng: virtio: clamp device-reported used.len at copy_data()**

- 日期：2026-06-14
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260614164000.3343777-1-michael.bommarito@gmail.com/

**hwrng: omap - balance runtime PM and clocks on probe-defer paths**

- 日期：2026-06-05
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260605192842.372935-1-william@theesfeld.net/

**▸ 组织：Bootlin**（1 patches）

**[v2] hwrng: core - Do not read data during PM sleep transition**

- 日期：2026-06-01
- 状态：社区讨论中
- 概括：限制read data during pm sleep transition，增加条件判断和安全保护逻辑
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260601-hw-random-fix-hwrng-fillfn-crash-suspend-resume-v2-1-667ce5da32ee@bootlin.com/

**▸ 组织：StarFive**（1 patches）

**[v5,2/2] hwrng: starfive: rework clk/reset teardown order for JHB100**

- 日期：2026-06-29
- 状态：社区讨论中
- 概括：重写重新设计部分实现，优化数据流和处理逻辑，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260629083658.300191-3-lianfeng.ouyang@starfivetech.com/

**▸ 组织：SUSE**（1 patches）

**[23/32] hw_random/via-rng: Stop using 32-bit MSR interfaces**

- 日期：2026-06-29
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260629060526.3638272-24-jgross@suse.com/

**▸ 组织：Kernel.org**（1 patches）

**[SERIES] qcom-rng fixes and cleanups** （cover letter，3/4 个 patch 达到代码量阈值）

- 日期：2026-06-08
- 状态：社区讨论中
- 概括：修复es and cleanups，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（3 个，显示前 5）：
  - crypto: qcom-rng - Enable clock in hwrng case
  - crypto: qcom-rng - Allow zero as a random number
  - hwrng: qcom - Move qcom-rng.c into drivers/char/hw_random/
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260608175848.2045229-2-ebiggers@kernel.org/

---

### ◆ 子系统：ECC（4 patches）

**▸ 组织：Linux Community**（2 patches）

**crypto: atmel-ecc - reject hardware ECDH without a public key**

- 日期：2026-06-11
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260611213617.463552-2-thorsten.blum@linux.dev/

**[SERIES] crypto: atmel-i2c - improve comment in atmel_i2c_init_ecdh_cmd** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-06-09
- 状态：社区讨论中
- 概括：改进comment，提升健壮性和性能，提升代码的可读性和可维护性，为后续功能迭代奠定更清晰的基础
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: atmel-i2c - improve comment in atmel_i2c_init_ecdh_cmd
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260609100552.233494-3-thorsten.blum@linux.dev/

**▸ 组织：Individual Contributor**（1 patches）

**crypto: ecc - Optimize vli additive operations using compiler builtins**

- 日期：2026-06-07
- 状态：社区讨论中
- 概括：优化关键路径的性能表现，降低延迟和提高吞吐量，提升代码的可读性和可维护性，为后续功能迭代奠定更清晰的基础
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260607112435.42804-1-fabianblatter09@gmail.com/

**▸ 组织：AMD**（1 patches）

**[v8,3/7] crypto/ccp: Disable CPU hotplug while SNP is active**

- 日期：2026-06-15
- 状态：社区讨论中
- 概括：禁用存在稳定性或安全性问题的功能，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/1feccf6e2a56d949b30f403c0ca7949f580e5982.1781419998.git.ashish.kalra@amd.com/

---

### ◆ 子系统：Skcipher（3 patches）

**▸ 组织：Individual Contributor**（2 patches）

**crypto: hisilicon - Use more common code in sec_alg_skcipher_crypto()**

- 日期：2026-06-17
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/e6aa4d9d-fe05-481c-be31-17033a60dc4c@web.de/

**crypto: ctr - Convert from skcipher to lskcipher**

- 日期：2026-05-10
- 状态：社区讨论中
- 概括：迁移from skcipher to lskcipher，适配新的接口规范，保持子系统与内核主线的兼容性，适应 API 和框架的演进方向
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260510230901.1772949-1-knecht.alexandre@gmail.com/

**▸ 组织：Amazon**（1 patches）

**[SERIES] crypto: skcipher - per-tfm multi-data-unit batching** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-06-01
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（3 个，显示前 5）：
  - crypto: xts - support multiple data units per request in template
  - crypto: skcipher - add per-tfm data_unit_size for batched requests
  - crypto: testmgr - exercise multi-data-unit path for skcipher
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260601085644.13026-3-lravich@amazon.com/

---

### ◆ 子系统：Talitos（3 patches）

**▸ 组织：Individual Contributor**（2 patches）

**crypto: talitos: replace in_be32/out_be32 with ioread32be/iowrite32be**

- 日期：2026-06-03
- 状态：社区讨论中
- 概括：替换将 in_be32/out_be32 替换为 ioread32be/iowrite32be，采用更规范的实现
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260603193300.7695-1-rosenp@gmail.com/

**[SERIES] crypto: talitos - fix rename first/last to first_desc/last_desc** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-05-23
- 状态：社区讨论中
- 概括：修复rename first/last to first_desc/last_desc，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（3 个，显示前 5）：
  - crypto: talitos - stop using crypto_ahash::init
  - crypto: talitos - fix SEC1 32k ahash request limitation
  - crypto: talitos - rename first/last to first_desc/last_desc
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260523151048.14914-4-ggoerisch@gmail.com/

**▸ 组织：Bootlin**（1 patches）

**[SERIES] crypto: talitos - Driver cleanup** （cover letter，15/19 个 patch 达到代码量阈值）

- 日期：2026-06-11
- 状态：社区讨论中
- 概括：清理代码中的风格问题和废弃的命名方式，精简代码库规模，降低后续维护的复杂度和引入回归问题的风险
- 达到阈值的 patches（15 个，显示前 5）：
  - crypto: talitos/hash - Use CRYPTO_AHASH_BLOCK_ONLY API
  - crypto: talitos - Move driver into dedicated directory
  - crypto: talitos - Prepare crypto implementation file splitting
  - crypto: talitos/hwrng - Move into separate file
  - crypto: talitos/skcipher - Move into separate file
  - ... 及其他 10 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260611-7-1-rc1_talitos_cleanup-v2-1-aa4a813ce69b@bootlin.com/

---

### ◆ 子系统：AF_ALG API（3 patches）

**▸ 组织：Kernel.org**（1 patches）

**crypto: af_alg - Add af_alg_restrict sysctl, defaulting to 1**

- 日期：2026-06-22
- 状态：社区讨论中
- 概括：新增af_alg_restrict sysctl, defaulting，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260622234803.6982-1-ebiggers@kernel.org/

**▸ 组织：Individual Contributor**（1 patches）

**crypto: algif_aead - stop recvmsg looping after a completed request**

- 日期：2026-06-28
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/OwDrEgL--F-9@tutanota.com/

**▸ 组织：Linux Community**（1 patches）

**[SERIES] sock: add sock_kzalloc helper** （cover letter，5/5 个 patch 达到代码量阈值）

- 日期：2026-05-27
- 状态：社区讨论中
- 概括：新增sock_kzalloc helper，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（5 个，显示前 5）：
  - crypto: af_alg - use sock_kzalloc in af_alg_alloc_areq
  - crypto: algif_aead - use sock_kzalloc in aead_accept_parent_nokey
  - crypto: af_alg - use sock_kzalloc in alloc_result + accept_parent_nokey
  - crypto: algif_rng - use sock_kzalloc in rng_accept_parent
  - crypto: algif_skcipher - use sock_kzalloc in accept_parent_nokey
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260527082509.1133816-9-thorsten.blum@linux.dev/

---

### ◆ 子系统：CCP/SEV (AMD)（1 patches）

**▸ 组织：AMD**（1 patches）

**[v5] crypto/ccp: Introduce SNP_VERIFY_MITIGATION command**

- 日期：2026-06-15
- 状态：社区讨论中
- 概括：引入snp_verify_mitigation command，扩展框架的功能范围，提升框架的抽象能力和代码可扩展性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/682e46e778b7394fb679591c9b6e4d9aeafa9462.1781533471.git.prsampat@amd.com/

---

### ◆ 子系统：Test Manager（1 patches）

**▸ 组织：Amazon**（1 patches）

**[SERIES] crypto: skcipher - multi-data-unit dispatch as a template** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-06-30
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: dun - data-unit-number dispatch template
  - crypto: testmgr - test dun() dispatch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260630083431.2772-2-lravich@amazon.com/

---

---
## 子系统说明

- **AF_ALG API**：用户空间加密 API（algif_skcipher、algif_hash 等）
- **DRBG**：确定性随机比特生成器
- **HWRNG**：硬件随机数生成器驱动
- **ECC**：椭圆曲线密码学（ECDSA、ECRDSA）
- **QAT (Intel)**：Intel QuickAssist Technology 硬件加速器
- **CCP/SEV (AMD)**：AMD 安全协处理器 / 安全加密虚拟化
- **CAAM (NXP)**：NXP Cryptographic Acceleration and Assurance Module
- **Talitos**：NXP/Freescale Talitos 安全加速器
- **QCE (Qualcomm)**：Qualcomm Crypto Engine
- **ICE (Qualcomm)**：Qualcomm Inline Crypto Engine
- **SPAcc**：安全算法硬件加速器
- **CESA (Marvell)**：Marvell Cryptographic Engine and Security Accelerator
- **VirtIO Crypto**：VirtIO 虚拟化加密设备
- **Crypto Engine**：加密算法引擎框架
- **Kerberos**：Kerberos 5 加密支持
- **Asymmetric Keys**：非对称密钥管理
- **Public Key**：公钥加密（X.509、PKCS7）
- **Authenc**：认证加密
- **Shash**：同步哈希算法
- **Ahash**：异步哈希算法
- **Skcipher**：对称密钥加密
- **Aead**：关联数据认证加密
- **Test Manager**：加密算法测试管理器
- **TCrypt**：加密速度测试模块
- **JitterEntropy**：Jitter 熵源 RNG
- **General Crypto**：通用 crypto（不属于特定子模块）

---

## 项目说明

本项目用于追踪 Linux 内核 crypto（加密）子系统的 patch 提交情况。crypto 子系统涵盖硬件加密加速器驱动（QAT、CCP、CAAM、QCE 等）、加密算法实现（AES、SHA、ECC、SMx 等）、以及用户空间加密 API（AF_ALG）。

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

*报告由 Linux Patches Tracker 自动生成 | 2026-07-03 15:40:18*
