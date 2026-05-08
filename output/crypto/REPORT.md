# Linux Crypto 子系统 Patch 追踪报告

---

## 报告信息

| 项目 | 内容 |
|------|------|
| 数据来源 | patchwork.kernel.org |
| 生成日期 | 2026-05-08 |
| 报告区间 | 2026-01-01 至 2026-05-06 |
| 仓库 | [https://github.com/IAMHCHCH/linux-patches-tracker](https://github.com/IAMHCHCH/linux-patches-tracker) |

---

## 统计概览

### 按状态分类

| 状态 | 数量 | 占比 |
|------|------|------|
| 社区讨论中 | 66 | 46.8% |
| 已合入 | 69 | 48.9% |
| **总计** | **141** | **100%** |

### 按组织分类（TOP 15）

| 组织 | 数量 | 占比 |
|------|------|------|
| Individual Contributor | 47 | 33.3% |
| Kernel.org | 34 | 24.1% |
| Linux Community | 21 | 14.9% |
| Intel | 7 | 5.0% |
| Bootlin | 5 | 3.5% |
| Huawei | 4 | 2.8% |
| Google | 3 | 2.1% |
| Qualcomm | 3 | 2.1% |
| Red Hat | 3 | 2.1% |
| Amazon | 3 | 2.1% |
| AMD | 2 | 1.4% |
| Oracle | 2 | 1.4% |
| IBM | 2 | 1.4% |
| Baylibre | 1 | 0.7% |
| Linaro | 1 | 0.7% |

### 按子系统分类

| 子系统 | 数量 | 占比 |
|--------|------|------|
| General Crypto | 76 | 53.9% |
| Authenc | 13 | 9.2% |
| HWRNG | 11 | 7.8% |
| AF_ALG API | 7 | 5.0% |
| CCP/SEV (AMD) | 6 | 4.3% |
| DRBG | 4 | 2.8% |
| CESA (Marvell) | 4 | 2.8% |
| Ahash | 3 | 2.1% |
| Public Key | 3 | 2.1% |
| ICE (Qualcomm) | 2 | 1.4% |
| CAAM (NXP) | 2 | 1.4% |
| ECC | 2 | 1.4% |
| QCE (Qualcomm) | 2 | 1.4% |
| Talitos | 2 | 1.4% |
| Skcipher | 1 | 0.7% |
| TCrypt | 1 | 0.7% |
| JitterEntropy | 1 | 0.7% |
| SPAcc | 1 | 0.7% |
## 已合入 Patches

### ◆ 子系统：General Crypto（33 patches）

**▸ 组织：Linux Community**（8 patches）

**crypto: starfive - use list_first_entry_or_null to simplify cryp_find_dev**

- 日期：2026-04-27
- 状态：已合入
- 概括：简化代码逻辑，减少不必要的复杂度，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260427213504.420377-3-thorsten.blum@linux.dev/

**[SERIES] crypto: img-hash - use list_first_entry_or_null to simplify digest** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-03-28
- 状态：已合入
- 概括：简化代码逻辑，减少不必要的复杂度，持续改进代码质量和功能完备性
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: img-hash - use list_first_entry_or_null to simplify digest
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260328102043.85271-4-thorsten.blum@linux.dev/

**[SERIES] crypto: stm32 - use list_first_entry_or_null to simplify hash_find_dev** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-03-20
- 状态：已合入
- 概括：简化代码逻辑，减少不必要的复杂度，持续改进代码质量和功能完备性
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: stm32 - use list_first_entry_or_null to simplify hash_find_dev
  - crypto: stm32 - use list_first_entry_or_null to simplify cryp_find_dev
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260320084914.7180-3-thorsten.blum@linux.dev/

**crypto: nx - annotate struct nx842_crypto_header with __counted_by**

- 日期：2026-03-17
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260317201804.1393389-3-thorsten.blum@linux.dev/

**crypto: artpec6 - use memcpy_and_pad to simplify prepare_hash**

- 日期：2026-03-09
- 状态：已合入
- 概括：简化代码逻辑，减少不必要的复杂度，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260309211119.81778-3-thorsten.blum@linux.dev/

**crypto: atmel - use list_first_entry_or_null to simplify find_dev**

- 日期：2026-03-08
- 状态：已合入
- 概括：简化代码逻辑，减少不必要的复杂度，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260308232230.544209-3-thorsten.blum@linux.dev/

**crypto: rng - Use unregister_rngs in register_rngs**

- 日期：2026-01-26
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260126175018.237812-2-thorsten.blum@linux.dev/

**crypto: omap - Use sysfs_emit in sysfs show functions**

- 日期：2026-01-09
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260109123640.170491-1-thorsten.blum@linux.dev/

**▸ 组织：Individual Contributor**（8 patches）

**[v2] crypto: inside-secure/eip93 - correct ecb(des-eip93) typo**

- 日期：2026-03-21
- 状态：已合入
- 概括：修正代码和文档中的拼写错误，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/e0090aea-45f9-48b6-99a7-7ad8666dce59@yahoo.com/

**crypto: inside-secure/eip93 - make it selectable for ECONET**

- 日期：2026-03-20
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260320211931.829476-1-olek2@wp.pl/

**[SERIES] Add support for more AES modes in TI DTHEv2** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-03-20
- 状态：已合入
- 概括：新增支持 more aes modes in ti dthev2，扩展框架的硬件兼容性和功能覆盖范围
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: ti - Add support for AES-CCM in DTHEv2 driver
  - crypto: ti - Add support for AES-GCM in DTHEv2 driver
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260320105052.3931552-3-t-pratham@ti.com/

**crypto: tegra - Disable softirqs before finalizing request**

- 日期：2026-03-10
- 状态：已合入
- 概括：禁用存在稳定性或安全性问题的功能，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/aa_kPXrFeOmhydP6@gondor.apana.org.au/

**[v10,1/3] crypto: ti - Add support for AES-CTR in DTHEv2 driver**

- 日期：2026-02-26
- 状态：已合入
- 概括：新增支持 aes-ctr in dthev2 driver，扩展框架的硬件兼容性和功能覆盖范围，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260226125441.3559664-2-t-pratham@ti.com/

**crypto: acomp: acompress.h: repair kernel-doc warnings**

- 日期：2026-02-25
- 状态：已合入
- 概括：编写使用文档和 API 说明，帮助开发者正确使用相关接口，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260225014500.41938-1-rdunlap@infradead.org/

**crypto: virtio: Convert from tasklet to BH workqueue**

- 日期：2026-02-07
- 状态：已合入
- 概括：迁移from tasklet to bh workqueue，适配新的接口规范，保持子系统与内核主线的兼容性，适应 API 和框架的演进方向
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260207182001.2242836-1-patso@likewhatevs.io/

**crypto: inside-secure/eip93 - unregister only available algorithm**

- 日期：2026-01-11
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260111132531.2232417-1-olek2@wp.pl/

**▸ 组织：Intel**（6 patches）

**[SERIES] crypto: qat - add support for zstd** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-03-28
- 状态：已合入
- 概括：新增支持 zstd，扩展框架的硬件兼容性和功能覆盖范围，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: qat - add support for zstd
  - crypto: qat - use swab32 macro
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260328223445.39445-3-giovanni.cabiddu@intel.com/

**crypto: qat - disable 4xxx AE cluster when lead engine is fused off**

- 日期：2026-03-24
- 状态：已合入
- 概括：禁用存在稳定性或安全性问题的功能，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260324111112.227158-1-ahsan.atta@intel.com/

**crypto: qat - disable 420xx AE cluster when lead engine is fused off**

- 日期：2026-03-24
- 状态：已合入
- 概括：禁用存在稳定性或安全性问题的功能，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260324111234.227329-1-ahsan.atta@intel.com/

**crypto: qat - use acomp_tfm_ctx()**

- 日期：2026-03-24
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260324165221.114280-1-giovanni.cabiddu@intel.com/

**[v2] crypto: qat - add anti-rollback support for GEN6 devices**

- 日期：2026-03-19
- 状态：已合入
- 概括：新增anti-rollback support，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260319110331.248189-1-suman.kumar.chakraborty@intel.com/

**crypto: qat - add wireless mode support for QAT GEN6**

- 日期：2026-03-11
- 状态：已合入
- 概括：新增wireless mode support，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260311082245.3466672-1-george.abraham.p@intel.com/

**▸ 组织：Kernel.org**（4 patches）

**crypto: sun8i-ss - avoid hash and rng references**

- 日期：2026-04-23
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260423065600.2081989-1-arnd@kernel.org/

**[SERIES] Fix some bugs in the CCP driver** （cover letter，1/4 个 patch 达到代码量阈值）

- 日期：2026-04-08
- 状态：已合入
- 概括：修复相关功能缺陷或逻辑错误，确保操作行为符合预期规范，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto/ccp: Initialize data during __sev_snp_init_locked()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260408143259.602767-2-tycho@kernel.org/

**[SERIES] Stop pulling DRBG code into non-FIPS kernels** （cover letter，9/10 个 patch 达到代码量阈值）

- 日期：2026-03-26
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（9 个，显示前 5）：
  - crypto: dh - Use crypto_stdrng_get_bytes()
  - crypto: ecc - Use crypto_stdrng_get_bytes()
  - crypto: geniv - Use crypto_stdrng_get_bytes()
  - crypto: hisilicon/hpre - Use crypto_stdrng_get_bytes()
  - crypto: intel/keembay-ocs-ecc - Use crypto_stdrng_get_bytes()
  - ... 及其他 4 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260326001507.66500-2-ebiggers@kernel.org/

**[SERIES] crypto: Remove arch-optimized des and des3_ede code** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-03-26
- 状态：已合入
- 概括：移除arch-optimized des and des3_ede code，清理冗余或过时的代码，精简代码库规模，降低后续维护的复杂度和引入回归问题的风险
- 达到阈值的 patches（3 个，显示前 5）：
  - crypto: s390 - Remove des and des3_ede code
  - crypto: sparc - Remove des and des3_ede code
  - crypto: x86 - Remove des and des3_ede code
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260326201246.57544-2-ebiggers@kernel.org/

**▸ 组织：Huawei**（4 patches）

**crypto: hisilicon/sec2 - prevent req used-after-free for sec**

- 日期：2026-03-21
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260321070038.2023844-1-huangchenghai2@huawei.com/

**crypto:hisilicon - add device load query functionality to debugfs**

- 日期：2026-03-13
- 状态：已合入
- 概括：修复相关功能缺陷或逻辑错误，确保操作行为符合预期规范，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260313094039.3390686-1-wuzongyu1@huawei.com/

**[V2] crypto: hisilicon/trng - support tfms sharing the device**

- 日期：2026-01-17
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260117071821.1786428-1-huangchenghai2@huawei.com/

**[SERIES] crypto: hisilicon/qm - fix several mailbox issues** （cover letter，3/4 个 patch 达到代码量阈值）

- 日期：2026-01-17
- 状态：已合入
- 概括：修复several mailbox issues，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（3 个，显示前 5）：
  - crypto: hisilicon/qm - move the barrier before writing to the mailbox register
  - crypto: hisilicon/qm - increase wait time for mailbox
  - crypto: hisilicon/qm - obtain the mailbox configuration at one time
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260117101806.2172918-3-huangchenghai2@huawei.com/

**▸ 组织：Oracle**（1 patches）

**[v2] padata: Put CPU offline callback in ONLINE section to allow failure**

- 日期：2026-03-13
- 状态：已合入
- 概括：修复相关功能缺陷或逻辑错误，确保操作行为符合预期规范，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260313152433.504992-1-daniel.m.jordan@oracle.com/

**▸ 组织：Qualcomm**（1 patches）

**crypto: nx - Simplify with scoped for each OF child loop**

- 日期：2026-01-02
- 状态：已合入
- 概括：简化代码逻辑，减少不必要的复杂度，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260102125011.65046-2-krzysztof.kozlowski@oss.qualcomm.com/

**▸ 组织：IBM**（1 patches）

**[SERIES] Paes and Phmac: Refuse clear key material by default** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-01-15
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: s390/phmac - Refuse clear key material by default
  - crypto: s390/paes - Refuse clear key material by default
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260115120026.4286-4-freude@linux.ibm.com/

---

### ◆ 子系统：Authenc（9 patches）

**▸ 组织：Individual Contributor**（9 patches）

**[v2] crypto: authencesn - Use memcpy_from/to_sglist**

- 日期：2026-05-02
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/afWDVpH2ba-DVpkT@gondor.apana.org.au/

**[v2] crypto: authencesn - Do not place hiseq at end of dst for out-of-place decryption**

- 日期：2026-03-27
- 状态：已合入
- 概括：限制place hiseq at end of dst，增加条件判断和安全保护逻辑，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/acYd4c4CBbtvl7Mi@gondor.apana.org.au/

**crypto: testmgr - Add test vectors for authenc(hmac(md5),rfc3686(ctr(aes)))**

- 日期：2026-03-19
- 状态：已合入
- 概括：新增test vectors，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260319171128.10566-1-olek2@wp.pl/

**crypto: inside-secure/eip93 - register hash before authenc algorithms**

- 日期：2026-03-06
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260306221742.1801119-1-olek2@wp.pl/

**[SERIES] crypto: testmgr - Add test vectors for authenc(hmac(sha1),rfc3686(ctr(aes)))** （cover letter，5/5 个 patch 达到代码量阈值）

- 日期：2026-03-05
- 状态：已合入
- 概括：新增test vectors，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（5 个，显示前 5）：
  - crypto: testmgr - Add test vectors for authenc(hmac(sha1),rfc3686(ctr(aes)))
  - crypto: testmgr - Add test vectors for authenc(hmac(sha224),rfc3686(ctr(aes)))
  - crypto: testmgr - Add test vectors for authenc(hmac(sha384),rfc3686(ctr(aes)))
  - crypto: testmgr - Add test vectors for authenc(hmac(sha512),rfc3686(ctr(aes)))
  - crypto: testmgr - Add test vectors for authenc(hmac(sha256),rfc3686(ctr(aes)))
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260305201036.63280-1-olek2@wp.pl/

**[v4] crypto: testmgr - Add test vectors for authenc(hmac(md5),cbc(aes))**

- 日期：2026-03-03
- 状态：已合入
- 概括：新增test vectors，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260303184916.69132-1-olek2@wp.pl/

**crypto: tesmgr - allow authenc(hmac(sha224/sha384),cbc(aes)) in fips mode**

- 日期：2026-02-06
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260206192732.478178-1-olek2@wp.pl/

**[v2] crypto: testmgr - Add test vectors for authenc(hmac(sha384),cbc(aes))**

- 日期：2026-01-31
- 状态：已合入
- 概括：新增test vectors，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260131173902.3487-1-olek2@wp.pl/

**[v2] crypto: testmgr - Add test vectors for authenc(hmac(sha224),cbc(aes))**

- 日期：2026-01-31
- 状态：已合入
- 概括：新增test vectors，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260131174353.4053-1-olek2@wp.pl/

---

### ◆ 子系统：HWRNG（5 patches）

**▸ 组织：Individual Contributor**（4 patches）

**[v4,3/3] hwrng: mtk - add support for hw access via SMCC**

- 日期：2026-04-20
- 状态：已合入
- 概括：新增支持 hw access via smcc，扩展框架的硬件兼容性和功能覆盖范围，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/e12b133a762f68628e29ac358a3a0605731ab7bd.1776702734.git.daniel@makrotopia.org/

**hwrng: hw_random.h: avoid kernel-doc warnings**

- 日期：2026-03-12
- 状态：已合入
- 概括：编写使用文档和 API 说明，帮助开发者正确使用相关接口，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260312051323.679913-1-rdunlap@infradead.org/

**[v4] hwrng: core - use RCU and work_struct to fix race condition**

- 日期：2026-01-29
- 状态：已合入
- 概括：修复竞态条件问题，通过增加锁保护或调整执行顺序消除并发访问冲突，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260129215016.3042874-1-karin0.zst@gmail.com/

**hwrng: airoha set rng quality to 900**

- 日期：2026-01-05
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260105204204.2430571-1-olek2@wp.pl/

**▸ 组织：Linaro**（1 patches）

**[2/3] hwrng: optee - simplify OP-TEE context match**

- 日期：2026-01-26
- 状态：已合入
- 概括：简化代码逻辑，减少不必要的复杂度，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260126-optee-simplify-context-match-v1-2-d4104e526cb6@linaro.org/

---

### ◆ 子系统：CESA (Marvell)（4 patches）

**▸ 组织：Individual Contributor**（2 patches）

**crypto: cesa: allocate engines with main struct**

- 日期：2026-04-25
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260425023247.475233-1-rosenp@gmail.com/

**[SERIES] crypto: safexcel - Group authenc ciphersuites** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-02-03
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: safexcel - Group authenc ciphersuites
  - crypto: safexcel - Add support for authenc(hmac(md5),*) suites
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260203182610.8672-1-olek2@wp.pl/

**▸ 组织：Linux Community**（2 patches）

**crypto: marvell/cesa - use memcpy_and_pad in mv_cesa_ahash_export**

- 日期：2026-03-17
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260317165258.1304521-2-thorsten.blum@linux.dev/

**crypto: cesa - Simplify return statement in mv_cesa_dequeue_req_locked**

- 日期：2026-01-31
- 状态：已合入
- 概括：简化代码逻辑，减少不必要的复杂度，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260131214249.533350-2-thorsten.blum@linux.dev/

---

### ◆ 子系统：AF_ALG API（3 patches）

**▸ 组织：Kernel.org**（1 patches）

**crypto: af_alg - Document the deprecation of AF_ALG**

- 日期：2026-04-30
- 状态：已合入
- 概括：编写使用文档和 API 说明，帮助开发者正确使用相关接口，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260430011544.31823-1-ebiggers@kernel.org/

**▸ 组织：Individual Contributor**（1 patches）

**[v2] crypto: af_alg: limit RX SG extraction by receive buffer budget**

- 日期：2026-04-02
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/7094f2ac73594db6f240466220a0fb8fb85b898b.1775051536.git.ldy3087146292@gmail.com/

**▸ 组织：Linux Community**（1 patches）

**crypto: af_alg - use sock_kmemdup in alg_setkey_by_key_serial**

- 日期：2026-04-05
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260405194940.990619-3-thorsten.blum@linux.dev/

---

### ◆ 子系统：Ahash（3 patches）

**▸ 组织：Linux Community**（2 patches）

**crypto: img-hash - Use unregister_ahashes in img_{un}register_algs**

- 日期：2026-02-01
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260201175632.662976-2-thorsten.blum@linux.dev/

**crypto: atmel - Use unregister_{aeads,ahashes,skciphers}**

- 日期：2026-01-26
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260126174704.237141-1-thorsten.blum@linux.dev/

**▸ 组织：Bootlin**（1 patches）

**crypto: aspeed/hash: Use memcpy_from_sglist() in aspeed_ahash_dma_prepare()**

- 日期：2026-03-27
- 状态：已合入
- 概括：准备为后续重大修改做前置准备，进行接口调整或代码重组，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260327092418.10476-1-paul.louvel@bootlin.com/

---

### ◆ 子系统：CAAM (NXP)（2 patches）

**▸ 组织：Linux Community**（2 patches）

**[1/2] crypto: caam - use print_hex_dump_devel to guard key hex dumps**

- 日期：2026-04-27
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260427163937.337966-3-thorsten.blum@linux.dev/

**[v3,2/2] crypto: caam - guard HMAC key hex dumps in hash_digest_key**

- 日期：2026-03-19
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260319092932.208939-4-thorsten.blum@linux.dev/

---

### ◆ 子系统：ECC（2 patches）

**▸ 组织：Individual Contributor**（2 patches）

**crypto: ecc - Unbreak the build on arm with CONFIG_KASAN_STACK=y**

- 日期：2026-04-08
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/abfaede9ab2e963d784fb70598ed74935f7f8d93.1775628469.git.lukas@wunner.de/

**crypto: ecc - correct kernel-doc format**

- 日期：2026-02-25
- 状态：已合入
- 概括：编写使用文档和 API 说明，帮助开发者正确使用相关接口，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260225014528.45199-1-rdunlap@infradead.org/

---

### ◆ 子系统：QCE (Qualcomm)（2 patches）

**▸ 组织：Linux Community**（2 patches）

**crypto: qce - simplify qce_xts_swapiv()**

- 日期：2026-03-30
- 状态：已合入
- 概括：简化代码逻辑，减少不必要的复杂度，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260330173923.479407-3-thorsten.blum@linux.dev/

**crypto: qce - use memcpy_and_pad in qce_aead_setkey**

- 日期：2026-03-21
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260321131439.40149-2-thorsten.blum@linux.dev/

---

### ◆ 子系统：CCP/SEV (AMD)（2 patches）

**▸ 组织：Kernel.org**（2 patches）

**[1/2] crypto: ccp - simplify sev_update_firmware()**

- 日期：2026-03-02
- 状态：已合入
- 概括：简化代码逻辑，减少不必要的复杂度，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260302150224.786118-1-tycho@kernel.org/

**[SERIES] crypto: ccp - Fix a case where SNP_SHUTDOWN is missed** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-01-05
- 状态：已合入
- 概括：修复case where snp_shutdown is missed，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto/ccp: narrow scope of snp_range_list
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260105172218.39993-1-tycho@kernel.org/

---

### ◆ 子系统：Skcipher（1 patches）

**▸ 组织：Kernel.org**（1 patches）

**crypto: simd - Remove unused skcipher support**

- 日期：2026-03-14
- 状态：已合入
- 概括：移除unused skcipher support，清理冗余或过时的代码，精简代码库规模，降低后续维护的复杂度和引入回归问题的风险
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260314213720.91525-1-ebiggers@kernel.org/

---

### ◆ 子系统：TCrypt（1 patches）

**▸ 组织：Oracle**（1 patches）

**crypto: tcrypt: clamp num_mb to avoid divide-by-zero**

- 日期：2026-03-02
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260302235916.769942-1-saeed.mirzamohammadi@oracle.com/

---

### ◆ 子系统：DRBG（1 patches）

**▸ 组织：Kernel.org**（1 patches）

**[SERIES] Fix and simplify the NIST DRBG implementation** （cover letter，23/38 个 patch 达到代码量阈值）

- 日期：2026-04-20
- 状态：已合入
- 概括：修复and simplify the nist drbg implementation，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（23 个，显示前 5）：
  - crypto: drbg - Fold include/crypto/drbg.h into crypto/drbg.c
  - crypto: drbg - Remove support for CTR_DRBG
  - crypto: drbg - Remove support for HASH_DRBG
  - crypto: drbg - Flatten the DRBG menu
  - crypto: testmgr - Add test for drbg_pr_hmac_sha512
  - ... 及其他 18 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260420063422.324906-2-ebiggers@kernel.org/

---

### ◆ 子系统：Talitos（1 patches）

**▸ 组织：Bootlin**（1 patches）

**[SERIES] talitos SEC1 ahash 32k request limitation** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-03-30
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: talitos - fix SEC1 32k ahash request limitation
  - crypto: talitos - rename first/last to first_desc/last_desc
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260330102820.29914-2-paul.louvel@bootlin.com/

---

## 社区讨论中 Patches

### ◆ 子系统：General Crypto（42 patches）

**▸ 组织：Kernel.org**（18 patches）

**[v2] lib/crypto: powerpc/md5: Drop powerpc optimized MD5 code**

- 日期：2026-05-06
- 状态：社区讨论中
- 概括：移除powerpc optimized md5 code，清理冗余或过时的代码，精简代码库规模，降低后续维护的复杂度和引入回归问题的风险
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260506030005.9698-1-ebiggers@kernel.org/

**[SERIES] Implement SNP DOWNLOAD_FIRMWARE_EX support** （cover letter，4/6 个 patch 达到代码量阈值）

- 日期：2026-04-30
- 状态：社区讨论中
- 概括：实现snp download_firmware_ex support，完善缺失的功能接口，完善子系统的功能完备性，确保与硬件平台和上层框架的正确协同
- 达到阈值的 patches（4 个，显示前 5）：
  - crypto/ccp: Hoist kernel part of SNP_PLATFORM_STATUS
  - crypto/ccp: Allow snp_get_platform_data() after SNP init
  - crypto/ccp: Reclaim command buffer when the PSP dies
  - crypto/ccp: Implement SNP firmware live update
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260430160716.1120553-2-tycho@kernel.org/

**[v2,2/2] lib/crypto: docs: Add rst documentation to Documentation/crypto/**

- 日期：2026-04-18
- 状态：社区讨论中
- 概括：新增rst documentati，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260418192138.15556-3-ebiggers@kernel.org/

**lib/crypto: arm64: Assume a little-endian kernel**

- 日期：2026-04-01
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260401003331.144065-1-ebiggers@kernel.org/

**lib/crypto: aescfb: Don't disable IRQs during AES block encryption**

- 日期：2026-03-31
- 状态：社区讨论中
- 概括：禁用存在稳定性或安全性问题的功能，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260331024414.51545-1-ebiggers@kernel.org/

**lib/crypto: aesgcm: Don't disable IRQs during AES block encryption**

- 日期：2026-03-31
- 状态：社区讨论中
- 概括：禁用存在稳定性或安全性问题的功能，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260331024430.51755-1-ebiggers@kernel.org/

**lib/crypto: Include <crypto/utils.h> instead of <crypto/algapi.h>**

- 日期：2026-03-31
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260331024438.51783-1-ebiggers@kernel.org/

**lib/crypto: tests: Migrate ChaCha20Poly1305 self-test to KUnit**

- 日期：2026-03-27
- 状态：社区讨论中
- 概括：迁移chacha20poly1305 self-test to kunit，适配新的接口规范，保持子系统与内核主线的兼容性，适应 API 和框架的演进方向
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260327224229.137532-1-ebiggers@kernel.org/

**lib/crypto: chacha - Zeroize permuted_state before it leaves scope**

- 日期：2026-03-26
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260326032920.39408-1-ebiggers@kernel.org/

**[SERIES] SM3 library** （cover letter，8/12 个 patch 达到代码量阈值）

- 日期：2026-03-21
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（8 个，显示前 5）：
  - crypto: sm3 - Fold sm3_init() into its caller
  - crypto: sm3 - Rename CRYPTO_SM3_GENERIC to CRYPTO_SM3
  - lib/crypto: sm3: Add SM3 library API
  - lib/crypto: tests: Add KUnit tests for SM3
  - crypto: sm3 - Replace with wrapper around library
  - ... 及其他 3 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260321040935.410034-2-ebiggers@kernel.org/

**[SERIES] GHASH library** （cover letter，15/19 个 patch 达到代码量阈值）

- 日期：2026-03-19
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（15 个，显示前 5）：
  - lib/crypto: gf128hash: Rename polyval module to gf128hash
  - lib/crypto: gf128hash: Support GF128HASH_ARCH without all POLYVAL functions
  - lib/crypto: gf128hash: Add GHASH support
  - crypto: arm/ghash - Make the "ghash" crypto_shash NEON-only
  - crypto: arm/ghash - Move NEON GHASH assembly into its own file
  - ... 及其他 10 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260319061723.1140720-2-ebiggers@kernel.org/

**[21/21] crypto: remove HKDF library**

- 日期：2026-03-02
- 状态：社区讨论中
- 概括：移除hkdf library，清理冗余或过时的代码，精简代码库规模，降低后续维护的复杂度和引入回归问题的风险
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260302075959.338638-22-ebiggers@kernel.org/

**[SERIES] AES-CMAC library** （cover letter，5/7 个 patch 达到代码量阈值）

- 日期：2026-02-18
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（5 个，显示前 5）：
  - lib/crypto: aes: Add support for CBC-based MACs
  - crypto: aes - Add cmac, xcbc, and cbcmac algorithms using library
  - lib/crypto: arm64/aes: Move assembly code for AES modes into libaes
  - lib/crypto: arm64/aes: Migrate optimized CBC-based MACs into library
  - lib/crypto: tests: Add KUnit tests for CBC-based MACs
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260218213501.136844-2-ebiggers@kernel.org/

**lib/crypto: mldsa: Clarify the documentation for mldsa_verify() slightly**

- 日期：2026-02-02
- 状态：社区讨论中
- 概括：编写使用文档和 API 说明，帮助开发者正确使用相关接口，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260202221552.174341-1-ebiggers@kernel.org/

**[SERIES] Fixes for PMF and CCP drivers after S4** （cover letter，1/4 个 patch 达到代码量阈值）

- 日期：2026-01-16
- 状态：社区讨论中
- 概括：修复相关功能缺陷或逻辑错误，确保操作行为符合预期规范，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: ccp - Factor out ring destroy handling to a helper
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260116041132.153674-3-superm1@kernel.org/

**[SERIES] AES library improvements** （cover letter，28/31 个 patch 达到代码量阈值）

- 日期：2026-01-12
- 状态：社区讨论中
- 概括：改进ments，提升健壮性和性能，提升代码的可读性和可维护性，为后续功能迭代奠定更清晰的基础
- 达到阈值的 patches（28 个，显示前 5）：
  - crypto: powerpc/aes - Rename struct aes_key
  - lib/crypto: aes: Introduce improved AES library
  - crypto: arm/aes-neonbs - Use AES library for single blocks
  - crypto: arm/aes - Switch to aes_enc_tab[] and aes_dec_tab[]
  - crypto: arm64/aes - Switch to aes_enc_tab[] and aes_dec_tab[]
  - ... 及其他 23 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260112192035.10427-2-ebiggers@kernel.org/

**lib/crypto: mldsa: Add FIPS cryptographic algorithm self-test**

- 日期：2026-01-07
- 状态：社区讨论中
- 概括：新增fips cryptographic algorithm self-test，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260107044215.109930-1-ebiggers@kernel.org/

**lib/crypto: nh: Restore dependency of arch code on !KMSAN**

- 日期：2026-01-05
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260105053652.1708299-1-ebiggers@kernel.org/

**▸ 组织：Individual Contributor**（9 patches）

**[SERIES] backport to fix a race condition/UAF in the** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-04-28
- 状态：社区讨论中
- 概括：修复use-after-free 漏洞，防止在错误恢复路径中访问已释放的内存对象，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（1 个，显示前 5）：
  - [5.15.y,1/2] padata: Fix pd UAF once and for all
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260428050800.10488-2-lanbincn@139.com/

**[SERIES] backport to fix a race condition/UAF in the padata subsystem** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-04-28
- 状态：社区讨论中
- 概括：修复use-after-free 漏洞，防止在错误恢复路径中访问已释放的内存对象，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（1 个，显示前 5）：
  - [5.10.y,1/2] padata: Fix pd UAF once and for all
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260428085701.1480-3-lanbincn@139.com/

**[SERIES] backport to fix a race condition/UAF in padata_reorder** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-04-25
- 状态：社区讨论中
- 概括：修复use-after-free 漏洞，防止在错误恢复路径中访问已释放的内存对象，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（1 个，显示前 5）：
  - [6.12.y,1/2] padata: Fix pd UAF once and for all
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260425081433.2763-3-lanbincn@139.com/

**[v2] crypto: zstd - fix segmented acomp streaming paths**

- 日期：2026-03-20
- 状态：社区讨论中
- 概括：修复segmented acomp streaming paths，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260320215124.389938-1-atwellwea@gmail.com/

**[SERIES] lib/crypto: x86/sha: Add PHE Extensions support** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-03-13
- 状态：社区讨论中
- 概括：新增phe extensions support，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: padlock-sha - Disable for Zhaoxin processor
  - lib/crypto: x86/sha256: PHE Extensions optimized SHA256 transform function
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260313080150.9393-2-AlanSong-oc@zhaoxin.com/

**[v2] crypto: arm64/aes-neonbs - Move key expansion off the stack**

- 日期：2026-03-06
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260306064254.2079274-1-yphbchou0911@gmail.com/

**[SERIES] Add support for hashing algorithms in TI DTHE V2** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-02-26
- 状态：社区讨论中
- 概括：新增支持 hashing algorithms in ti dthe v2，扩展框架的硬件兼容性和功能覆盖范围
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: ti - Add support for HMAC in DTHEv2 Hashing Engine driver
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260226131103.3560884-2-t-pratham@ti.com/

**[V2] crypto: aegis128: Add RISC-V vector SIMD implementation**

- 日期：2026-01-26
- 状态：社区讨论中
- 概括：新增risc-v vector simd implementation，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260126092411.243237-1-zhangchunyan@iscas.ac.cn/

**[v3,2/3] lib/crypto: x86/sha1: PHE Extensions optimized SHA1 transform function**

- 日期：2026-01-16
- 状态：社区讨论中
- 概括：优化关键路径的性能表现，降低延迟和提高吞吐量，提升代码的可读性和可维护性，为后续功能迭代奠定更清晰的基础
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260116071513.12134-3-AlanSong-oc@zhaoxin.com/

**▸ 组织：Google**（3 patches）

**crypto: ccp: Treat zero-length cert chain as query for blob lengths**

- 日期：2026-05-04
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260504222812.2339526-1-seanjc@google.com/

**[SERIES] KVM: SEV: Don't advertise unusable VM types** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-04-16
- 状态：社区讨论中
- 概括：限制advertise unusable vm types，增加条件判断和安全保护逻辑，持续改进代码质量和功能完备性
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto/ccp: hoist kernel part of SNP_PLATFORM_STATUS
  - crypto/ccp: export firmware supported vm types
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260416232329.3408497-2-seanjc@google.com/

**[v2,2/5] crypto: aegis128 - Use neon-intrinsics.h on ARM too**

- 日期：2026-03-31
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260331074940.55502-9-ardb+git@google.com/

**▸ 组织：Amazon**（3 patches）

**[SERIES] crypto: Standalone crypto module** （cover letter，4/8 个 patch 达到代码量阈值）

- 日期：2026-04-18
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（4 个，显示前 5）：
  - crypto: add pluggable interface for module symbols referenced by the main kernel
  - crypto: dedicated ELF sections for collected crypto initcalls
  - crypto/algapi.c: skip crypto_check_module_sig() for the standalone crypto module
  - crypto: convert exported symbols in architecture-independent crypto to pluggable symbols
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260418002032.2877-2-wanjay@amazon.com/

**[06/17] crypto: add pluggable interface for builtin crypto modules**

- 日期：2026-02-12
- 状态：社区讨论中
- 概括：新增pluggable interface，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260212024228.6267-7-wanjay@amazon.com/

**[SERIES] crypto: Standalone crypto module (Series 2/4): Arch-independent crypto** （cover letter，106/106 个 patch 达到代码量阈值）

- 日期：2026-02-12
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（106 个，显示前 5）：
  - crypto: convert exported crypto symbol into pluggable interface for CONFIG_ASYNC_XOR crypto
  - crypto: convert exported crypto symbol into pluggable interface for CONFIG_ASYNC_PQ crypto
  - crypto: convert exported crypto symbol into pluggable interface for CONFIG_ASYNC_RAID6_RECOV crypto
  - crypto: convert exported crypto symbol into pluggable interface for CONFIG_CRYPTO_KDF800108_CTR crypto
  - crypto: convert exported crypto symbol into pluggable interface for CONFIG_CRYPTO_KRB5 crypto
  - ... 及其他 101 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260212024725.11264-97-wanjay@amazon.com/

**▸ 组织：Linux Community**（2 patches）

**crypto: artpec6 - refactor crypto_setup_out_descr for readability**

- 日期：2026-05-06
- 状态：社区讨论中
- 概括：重构重新组织代码结构以提升可读性和可维护性，提升代码的可读性和可维护性，为后续功能迭代奠定更清晰的基础
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260506091627.177426-3-thorsten.blum@linux.dev/

**[SERIES] crypto: blake2b - use memcpy_and_pad in __blake2b_init** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-04-14
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: blake2b - use memcpy_and_pad in __blake2b_init
  - crypto: blake2s - use memcpy_and_pad in __blake2s_init
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260414154902.344182-3-thorsten.blum@linux.dev/

**▸ 组织：Red Hat**（2 patches）

**x509: select CONFIG_CRYPTO_LIB_SHA256**

- 日期：2026-02-17
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/1015832.1771316809@warthog.procyon.org.uk/

**[SERIES] x509, pkcs7, crypto: Add ML-DSA signing** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-02-02
- 状态：社区讨论中
- 概括：新增ml-dsa signing，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: Add ML-DSA crypto_sig support
  - x509: Separately calculate sha256 for blacklist
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260202170216.2467036-2-dhowells@redhat.com/

**▸ 组织：IBM**（1 patches）

**[v2,1/1] lib/crypto: tests: Add KUnit tests for AES**

- 日期：2026-01-19
- 状态：社区讨论中
- 概括：新增kunit tests，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260119121210.2662-2-dengler@linux.ibm.com/

**▸ 组织：NXP**（1 patches）

**[v3,9/9] crypto: atmel: Use dmaengine_prep_config_single() API**

- 日期：2026-01-05
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260105-dma_prep_config-v3-9-a8480362fd42@nxp.com/

**▸ 组织：Qualcomm**（1 patches）

**[SERIES] crypto/dmaengine: qce: introduce BAM locking and use DMA for register I/O** （cover letter，6/7 个 patch 达到代码量阈值）

- 日期：2026-04-27
- 状态：社区讨论中
- 概括：引入bam locking and use dma for register i/o，扩展框架的功能范围
- 达到阈值的 patches（6 个，显示前 5）：
  - crypto: qce - Include algapi.h in the core.h header
  - crypto: qce - Simplify arguments of devm_qce_dma_request()
  - crypto: qce - Use existing devres APIs in devm_qce_dma_request()
  - crypto: qce - Map crypto memory for DMA
  - crypto: qce - Add BAM DMA support for crypto register I/O
  - ... 及其他 1 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260427-qcom-qce-cmd-descr-v16-6-945fd1cafbbc@oss.qualcomm.com/

**▸ 组织：AMD**（1 patches）

**[SERIES] crypto: zynqmp-aes-gcm: Bug fixes and sha3-384 support** （cover letter，3/5 个 patch 达到代码量阈值）

- 日期：2026-03-03
- 状态：社区讨论中
- 概括：修复fixes and sha3-384 support，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（3 个，显示前 5）：
  - crypto: zynqmp-sha: Change algo type from shash to ahash
  - crypto: zynqmp-sha: Save dma bit mask value in driver context
  - crypto: zynqmp-sha: Add sha3-384 support for AMD/Xilinx Versal device
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260303071953.149252-2-h.jain@amd.com/

**▸ 组织：Intel**（1 patches）

**[SERIES] zswap compression batching with optimized iaa_crypto driver** （cover letter，17/22 个 patch 达到代码量阈值）

- 日期：2026-01-25
- 状态：社区讨论中
- 概括：优化关键路径的性能表现，降低延迟和提高吞吐量，提升代码的可读性和可维护性，为后续功能迭代奠定更清晰的基础
- 达到阈值的 patches（17 个，显示前 5）：
  - crypto: iaa - Reorganize the iaa_crypto driver code.
  - crypto: iaa - Simplify, consistency of function parameters, minor stats bug fix.
  - crypto: iaa - New architecture for IAA device WQ [de]comp usage & core mapping.
  - crypto: iaa - Descriptor allocation timeouts with mitigations.
  - crypto: iaa - iaa_wq uses percpu_refs for get/put reference counting.
  - ... 及其他 12 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260125033537.334628-2-kanchana.p.sridhar@intel.com/

---

### ◆ 子系统：CCP/SEV (AMD)（4 patches）

**▸ 组织：Kernel.org**（3 patches）

**[SERIES] SEV re-initialization fixes** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-05-04
- 状态：社区讨论中
- 概括：修复相关功能缺陷或逻辑错误，确保操作行为符合预期规范，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（4 个，显示前 5）：
  - crypto/ccp: Do not initialize SNP for SEV ioctls
  - crypto/ccp: Do not initialize SNP for ioctl(SNP_COMMIT)
  - crypto/ccp: Do not initialize SNP for ioctl(SNP_VLEK_LOAD)
  - crypto/ccp: Do not initialize SNP for ioctl(SNP_CONFIG)
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260504165147.1615643-2-tycho@kernel.org/

**[SERIES] Allow disabling RAPL during SNP initialization** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-04-27
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto/ccp: Pass init_args to __sev_snp_init_locked()
  - crypto/ccp: Support setting RAPL_DIS in SNP_INIT_EX
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260427204847.112899-2-tycho@kernel.org/

**[3/4] crypto/ccp: support setting RAPL_DIS in SNP_INIT_EX**

- 日期：2026-02-23
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260223162900.772669-4-tycho@kernel.org/

**▸ 组织：AMD**（1 patches）

**[RFC,v2] crypto/ccp: Introduce SNP_VERIFY_MITIGATION command**

- 日期：2026-05-01
- 状态：社区讨论中
- 概括：引入snp_verify_mitigation command，扩展框架的功能范围，提升框架的抽象能力和代码可扩展性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260501152051.17469-1-prsampat@amd.com/

---

### ◆ 子系统：AF_ALG API（4 patches）

**▸ 组织：Individual Contributor**（2 patches）

**crypto: af_alg - Cap AEAD AD length to 0x80000000**

- 日期：2026-05-05
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/afmyNZxW3QB33LXi@gondor.apana.org.au/

**[SERIES] crypto: algif_aead - snapshot IV for async AEAD requests** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-04-19
- 状态：社区讨论中
- 概括：对齐实现与内核其他子系统的规范保持一致，持续改进代码质量和功能完备性
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: ccm - keep a private IV for auth and CTR state
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/7f569774b437b9056985db1fec58aff337a41a4d.1776578475.git.enjou1224@outlook.com/

**▸ 组织：Linux Community**（1 patches）

**[SERIES] sock: add sock_kzalloc helper** （cover letter，5/5 个 patch 达到代码量阈值）

- 日期：2026-04-27
- 状态：社区讨论中
- 概括：新增sock_kzalloc helper，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（5 个，显示前 5）：
  - crypto: af_alg - use sock_kzalloc in af_alg_alloc_areq
  - crypto: algif_aead - use sock_kzalloc in aead_accept_parent_nokey
  - crypto: af_alg - use sock_kzalloc in alloc_result + accept_parent_nokey
  - crypto: algif_rng - use sock_kzalloc in rng_accept_parent
  - crypto: algif_skcipher - use sock_kzalloc in accept_parent_nokey
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260427104129.309982-8-thorsten.blum@linux.dev/

**▸ 组织：Kernel.org**（1 patches）

**[SERIES] AF_ALG fixes** （cover letter，4/10 个 patch 达到代码量阈值）

- 日期：2026-04-30
- 状态：社区讨论中
- 概括：修复相关功能缺陷或逻辑错误，确保操作行为符合预期规范，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（4 个，显示前 5）：
  - [5.10,02/10] crypto: scatterwalk - Backport memcpy_sglist()
  - [5.10,03/10] crypto: algif_aead - use memcpy_sglist() instead of null skcipher
  - [5.10,06/10] crypto: authenc - use memcpy_sglist() instead of null skcipher
  - [5.10,07/10] crypto: authencesn - Do not place hiseq at end of dst for out-of-place decryption
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260430070128.219863-2-ebiggers@kernel.org/

---

### ◆ 子系统：HWRNG（4 patches）

**▸ 组织：Bootlin**（2 patches）

**[RFC] hwrng: core - Set hwrng_fillfn() kernel thread freezable**

- 日期：2026-04-27
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260427-hw-random-set-hwrng-fillfn-kthread-freezable-v1-1-9bbe4f88b43a@bootlin.com/

**[SERIES] Add support for Inside-Secure EIP-150 crypto block** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-03-27
- 状态：社区讨论中
- 概括：新增支持 inside-secure eip-150 crypto block，扩展框架的硬件兼容性和功能覆盖范围
- 达到阈值的 patches（2 个，显示前 5）：
  - hwrng: omap: Enable on Renesas RZ/N1D
  - crypto: eip28: Add support for SafeXcel EIP-28 Public Key Accelerator
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260327-schneider-v7-0-rc1-crypto-v1-13-5e6ff7853994@bootlin.com/

**▸ 组织：Individual Contributor**（1 patches）

**[v2] hwrng: virtio: clamp device-reported used.len at copy_data()**

- 日期：2026-04-18
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260418150613.3522589-1-michael.bommarito@gmail.com/

**▸ 组织：Linux Community**（1 patches）

**[SERIES] hwrng: core - drop unnecessary forward declarations** （cover letter，3/4 个 patch 达到代码量阈值）

- 日期：2026-05-05
- 状态：社区讨论中
- 概括：移除unnecessary forward declarations，清理冗余或过时的代码，精简代码库规模，降低后续维护的复杂度和引入回归问题的风险
- 达到阈值的 patches（3 个，显示前 5）：
  - hwrng: core - use bool for wait parameter in rng_get_data
  - hwrng: core - use MAX to simplify RNG_BUFFER_SIZE
  - hwrng: core - use sysfs_emit_at in rng_available_show
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260505094555.158017-7-thorsten.blum@linux.dev/

---

### ◆ 子系统：DRBG（3 patches）

**▸ 组织：Kernel.org**（2 patches）

**crypto: drbg - Rename MAX_ADDTL => MAX_ADDTL_BYTES**

- 日期：2026-05-06
- 状态：社区讨论中
- 概括：重命名符号或函数以更清晰地表达其用途和语义，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260506000217.70738-1-ebiggers@kernel.org/

**crypto: drbg - Remove support for "prediction resistance"**

- 日期：2026-05-06
- 状态：社区讨论中
- 概括：移除support，清理冗余或过时的代码，精简代码库规模，降低后续维护的复杂度和引入回归问题的风险
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260506000258.70807-1-ebiggers@kernel.org/

**▸ 组织：Individual Contributor**（1 patches）

**[v2] crypto: drbg - convert to guard(mutex)**

- 日期：2026-03-01
- 状态：社区讨论中
- 概括：迁移to guard(mutex)，适配新的接口规范，保持子系统与内核主线的兼容性，适应 API 和框架的演进方向
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260301120743.27041-1-rajveer.chaudhari.linux@gmail.com/

---

### ◆ 子系统：Public Key（3 patches）

**▸ 组织：Individual Contributor**（2 patches）

**[SERIES] pkcs7: better handling of signed attributes** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-03-19
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: pkcs7: add ability to extract signed attributes by OID
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260319191208.831-2-James.Bottomley@HansenPartnership.com/

**[v3,3/5] crypto: pkcs7: allow pkcs7_digest() to be called from pkcs7_trust**

- 日期：2026-02-25
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260225211907.7368-4-James.Bottomley@HansenPartnership.com/

**▸ 组织：Meta**（1 patches）

**crypto: pkcs7 - use constant-time digest comparison**

- 日期：2026-02-01
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260201035503.3945067-1-hodgesd@meta.com/

---

### ◆ 子系统：ICE (Qualcomm)（2 patches）

**▸ 组织：Baylibre**（1 patches）

**crypto: ccp - Define pci_device_ids using named initializers**

- 日期：2026-05-04
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260504152421.2147027-2-u.kleine-koenig@baylibre.com/

**▸ 组织：Qualcomm**（1 patches）

**crypto: Move MODULE_DEVICE_TABLE next to the table itself**

- 日期：2026-05-05
- 状态：社区讨论中
- 概括：移动代码到更合适的位置，优化代码组织结构，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260505102948.191683-2-krzysztof.kozlowski@oss.qualcomm.com/

---

### ◆ 子系统：Authenc（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: authencesn - Copy high sequence number from src after out-of-place decryption**

- 日期：2026-03-25
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/acOpDrnN3cVfiASk@gondor.apana.org.au/

---

### ◆ 子系统：JitterEntropy（1 patches）

**▸ 组织：Kernel.org**（1 patches）

**[v7] crypto: jitterentropy - Use SHA-3 library**

- 日期：2026-02-26
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260226010005.43528-1-ebiggers@kernel.org/

---

### ◆ 子系统：Talitos（1 patches）

**▸ 组织：Bootlin**（1 patches）

**[SERIES] crypto: talitos - fix several issues in the Freescale talitos crypto driver** （cover letter，6/12 个 patch 达到代码量阈值）

- 日期：2026-05-05
- 状态：社区讨论中
- 概括：修复several issues，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 达到阈值的 patches（6 个，显示前 5）：
  - crypto: talitos - add chaining of arbitrary number of descriptor for the SEC1
  - crypto: talitos - move dma unmapping code in flush_channel() into a standalone dma_unmap_request() function
  - crypto: talitos - move dma mapping code in talitos_submit() into a standalone dma_map_request() function
  - crypto: talitos - move code in current_desc_hdr() into a standalone function
  - crypto: talitos/hash - use descriptor chaining for SEC1 instead of workqueue
  - ... 及其他 1 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260505-bootlin_test-7-1-rc1_sec_bugfix-v2-12-5818064bd190@bootlin.com/

---

### ◆ 子系统：SPAcc（1 patches）

**▸ 组织：Vayavya Labs**（1 patches）

**[SERIES] crypto: spacc - Add SPAcc Crypto Driver** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-04-16
- 状态：社区讨论中
- 概括：新增spacc cryp，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: spacc - Add SPAcc ahash support
  - crypto: spacc - Add SPAcc AUTODETECT Support
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260416064451.99886-3-pavitrakumarm@vayavyalabs.com/

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

*报告由 Linux Patches Tracker 自动生成 | 2026-05-08 15:36:37*
