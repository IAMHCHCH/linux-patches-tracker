# Linux Crypto 子系统 Patch 追踪报告

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
| 社区讨论中 | 58 | 56.3% |
| 已合入 | 37 | 35.9% |
| **总计** | **103** | **100%** |

### 按组织分类（TOP 15）

| 组织 | 数量 | 占比 |
|------|------|------|
| Individual Contributor | 57 | 55.3% |
| Linux Community | 11 | 10.7% |
| Kernel.org | 11 | 10.7% |
| Red Hat | 8 | 7.8% |
| Canonical | 4 | 3.9% |
| Bootlin | 2 | 1.9% |
| Huawei | 2 | 1.9% |
| Intel | 2 | 1.9% |
| Qualcomm | 2 | 1.9% |
| Vayavya Labs | 1 | 1.0% |
| AMD | 1 | 1.0% |
| Oracle | 1 | 1.0% |
| SUSE | 1 | 1.0% |

### 按子系统分类

| 子系统 | 数量 | 占比 |
|--------|------|------|
| General Crypto | 63 | 61.2% |
| Public Key | 7 | 6.8% |
| AF_ALG API | 4 | 3.9% |
| HWRNG | 4 | 3.9% |
| Asymmetric Keys | 4 | 3.9% |
| Talitos | 3 | 2.9% |
| CAAM (NXP) | 3 | 2.9% |
| Aead | 3 | 2.9% |
| ECC | 2 | 1.9% |
| CESA (Marvell) | 2 | 1.9% |
| Kerberos | 2 | 1.9% |
| SPAcc | 1 | 1.0% |
| ICE (Qualcomm) | 1 | 1.0% |
| Ahash | 1 | 1.0% |
| Authenc | 1 | 1.0% |
| Skcipher | 1 | 1.0% |
| QCE (Qualcomm) | 1 | 1.0% |

## 重点 Patch Top20 清单

### 已合入

| 厂商 | 简介 |
|------|------|
| Red Hat | [PATCH v5 00/10] crypto: Provide a function for zeroizing crypto_aes_ctx ------围绕 Intel QAT 驱动的设备能力、复位、迁移或接口清理进行调整，提升硬件加速器在主线内核中的可维护性。 |
| Intel | [PATCH v2 00/5] crypto: iaa - Fixes for multi entry SG lists ------集中修复 crypto 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。 |
| Canonical | [PATCH v2 00/2] crypto: asymmetric_keys - fix OOB read in pefile_parse_binary ------集中修复 crypto 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。 |
| Kernel.org | [PATCH v1 00/3] crypto: af_alg_restrict cleanups ------清理 crypto 相关的旧接口、重复实现或风格问题，降低后续维护复杂度。 |
| Linux Community | [PATCH v1 00/4] crypto: atmel-tdes - simplify fast path in crypt_start ------清理 crypto 相关的旧接口、重复实现或风格问题，降低后续维护复杂度。 |
| Individual Contributor | [PATCH v1 00/2] crypto: keembay - use crypto_memneq() to compare GCM AEAD tags ------归纳 crypto 系列中的关联改动，重点调整核心接口、驱动流程和异常处理逻辑。 |
| Linux Community | [PATCH v1 00/2] crypto: qce - simplify devm_qce_register_algs ------归纳 crypto 系列中的关联改动，重点调整核心接口、驱动流程和异常处理逻辑。 |
| Linux Community | [PATCH v1 00/2] crypto: atmel-ecc - simplify control flow in atmel_ecdh_set_secret ------清理 crypto 相关的旧接口、重复实现或风格问题，降低后续维护复杂度。 |
| Kernel.org | [PATCH] crypto: af_alg - Allow additional ciphers for cryptsetup ------修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性 |
| Bootlin | [v5] hwrng: core - Stop/start hwrng_fillfn() kthread before/after suspend-resume ------修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性 |
| Bootlin | [v2,2/2] hwrng: omap: Enable on Renesas RZ/N1D ------启用之前被禁用或条件编译的功能特性，持续改进代码质量和功能完备性 |
| Linux Community | [PATCH] crypto: qce - simplify control flow in register functions ------简化代码逻辑，减少不必要的复杂度，持续改进代码质量和功能完备性 |
| Individual Contributor | [PATCH] crypto: octeontx2 - use crypto_memneq() to check HMAC for cipher_null authenc ------修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性 |
| Individual Contributor | [PATCH] crypto: octeontx - use crypto_memneq() to check HMAC ------修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性 |
| Individual Contributor | [PATCH] crypto: ccree - use crypto_memneq() to compare AEAD tag ------修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性 |
| Individual Contributor | [PATCH] crypto: amcc: pass core_dev to request_irq ------传递各层之间正确传递参数和状态信息，持续改进代码质量和功能完备性 |
| Individual Contributor | [PATCH] crypto: s5p-sss: pass s5p_aes_dev to irq handler ------传递各层之间正确传递参数和状态信息，持续改进代码质量和功能完备性 |
| Individual Contributor | [PATCH] crypto: rockchip: pass crypto_info to irq handler ------传递各层之间正确传递参数和状态信息，持续改进代码质量和功能完备性 |
| Individual Contributor | [PATCH] crypto: sa2ul - use crypto_memneq() to compare AEAD tag ------修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性 |
| Individual Contributor | [PATCH] crypto/krb5: use kfree_sensitive() for derived key buffers ------修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性 |

### 社区讨论

| 厂商 | 简介 |
|------|------|
| Individual Contributor | [PATCH v4 00/19] crypto: cmh - add Rambus CryptoManager Hub driver ------围绕 crypto 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。 |
| Kernel.org | [PATCH v2 00/13] Library APIs for AES encryption modes ------围绕 Library APIs for AES encryption modes 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。 |
| Qualcomm | [PATCH v24 00/14] crypto/dmaengine: qce: introduce BAM locking and use DMA for register I/O ------围绕 crypto/dmaengine 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。 |
| Qualcomm | [PATCH v6 00/8] crypto: qce - Fix crypto self-test failures ------集中修复 crypto 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。 |
| Individual Contributor | [PATCH v1 00/3] crypto: caam: Fix DMA mapping leak in the cbc(paes) job path ------集中修复 crypto 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。 |
| Kernel.org | [PATCH v2 00/5] lib/crypto: KUnit tests for AES-CCM and AES-GCM ------围绕 lib/crypto 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。 |
| Red Hat | [PATCH v1 00/11] libcrypto: Provide more __cleanup functions for zeroizing data ------清理 libcrypto 相关的旧接口、重复实现或风格问题，降低后续维护复杂度。 |
| Individual Contributor | [PATCH v3 00/5] crypto: talitos - fix rename first/last to first_desc/last_desc ------集中修复 crypto 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。 |
| Individual Contributor | [PATCH v1 00/4] crypto: introduce generic dynamic software fallback and EIP93 support ------围绕 crypto 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。 |
| Individual Contributor | [PATCH v2 00/5] crypto: eip93: fix request lifetime and completion handling ------集中修复 crypto 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。 |
| Individual Contributor | [PATCH v7 00/2] Add support for hashing algorithms in TI DTHE V2 ------围绕 Add support for hashing algorithms in TI DTHE V2 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。 |
| Red Hat | [PATCH v2 00/6] crypto: Add __cleanup functions for zeroizing aes_cmac_key & aes_cmac_ctx ------围绕 crypto 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。 |
| Kernel.org | [PATCH v1 00/3] lib/crypto: FIPS self-tests for AES encryption modes ------围绕 lib/crypto 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。 |
| Individual Contributor | [PATCH v2 00/7] Fix several issues in DTHEv2 driver ------集中修复 Fix several issues in DTHEv2 driver 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。 |
| Individual Contributor | [PATCH v1 00/5] lib/crypto: add HKDF and convert fscrypt and NVMe ------围绕 lib/crypto 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。 |
| Individual Contributor | [PATCH v1 00/2] crypto: rsassa-pkcs1: fix undersized key handling ------集中修复 crypto 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。 |
| Individual Contributor | [PATCH v1 00/3] Add X.509 CRL support ------围绕 Add X.509 CRL support 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。 |
| Individual Contributor | [PATCH v1 00/2] crypto: amlogic: Fix IRQ handler return value and fallthrough logic ------集中修复 crypto 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。 |
| Kernel.org | [PATCH v1 00/2] More padata cleanups ------清理 More padata cleanups 相关的旧接口、重复实现或风格问题，降低后续维护复杂度。 |
| Individual Contributor | [PATCH v1 00/2] crypto: img-hash: clean up probe ------集中修复 crypto 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。 |

---

## 已合入 Patches

### ◆ 子系统：General Crypto（20 patches）

**▸ 组织：Individual Contributor**（12 patches）

**crypto: octeontx - use crypto_memneq() to check HMAC**

- 日期：2026-08-15
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/aoCdOiyhQZZsFm5S@david.gall/

**crypto: amcc: pass core_dev to request_irq**

- 日期：2026-08-12
- 状态：已合入
- 概括：传递各层之间正确传递参数和状态信息，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260812191555.93423-1-rosenp@gmail.com/

**crypto: s5p-sss: pass s5p_aes_dev to irq handler**

- 日期：2026-08-11
- 状态：已合入
- 概括：传递各层之间正确传递参数和状态信息，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260811043358.136042-1-rosenp@gmail.com/

**crypto: rockchip: pass crypto_info to irq handler**

- 日期：2026-08-11
- 状态：已合入
- 概括：传递各层之间正确传递参数和状态信息，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260811044916.160856-1-rosenp@gmail.com/

**crypto: eip93 - use struct_size() and flexible array for ring allocation**

- 日期：2026-08-03
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260803224028.87631-1-rosenp@gmail.com/

**crypto: ccp - don't abuse kernel-doc comment format**

- 日期：2026-07-30
- 状态：已合入
- 概括：编写使用文档和 API 说明，帮助开发者正确使用相关接口，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260730051710.1412969-1-rdunlap@infradead.org/

**crypto: ccm - Set rfc4309 maxauthsize from child**

- 日期：2026-07-20
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/al17HaL8wNd_fuDc@gondor.apana.org.au/

**crypto: hisilicon/sec: use devm_platform_ioremap_resource in sec_map_io**

- 日期：2026-07-15
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260715011533.1278258-1-rosenp@gmail.com/

**crypto: omap-aes: use devm_platform_get_and_ioremap_resource**

- 日期：2026-07-15
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260715215848.410011-1-rosenp@gmail.com/

**crypto: omap-sham: use devm_platform_get_and_ioremap_resource**

- 日期：2026-07-15
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260715220013.416122-1-rosenp@gmail.com/

**crypto: keembay - Initialize completion before requesting IRQ**

- 日期：2026-07-14
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260714033015.367735-1-lilinmao@kylinos.cn/

**crypto: keembay - publish OF module alias for OCS AES/SM4**

- 日期：2026-07-14
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260714131442.153699-1-pengcan@kylinos.cn/

**▸ 组织：Linux Community**（6 patches）

**crypto: qce - simplify control flow in register functions**

- 日期：2026-08-15
- 状态：已合入
- 概括：简化代码逻辑，减少不必要的复杂度，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260815150946.12142-3-thorsten.blum@linux.dev/

**crypto: starfive - use scatterlist length before DMA mapping**

- 日期：2026-07-25
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260725090609.315812-2-thorsten.blum@linux.dev/

**crypto: octeontx - simplify get_{eng,ucode}_type_str helpers**

- 日期：2026-07-23
- 状态：已合入
- 概括：简化代码逻辑，减少不必要的复杂度，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260723163326.163043-2-thorsten.blum@linux.dev/

**crypto: powerpc/aes - use bool for encryption/decryption flag**

- 日期：2026-07-11
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260711145216.747128-3-thorsten.blum@linux.dev/

**crypto: atmel-sha204a - clear RNG data from memory**

- 日期：2026-07-08
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260708150359.545852-2-thorsten.blum@linux.dev/

**[SERIES] crypto: atmel-tdes - simplify fast path in crypt_start** （cover letter，2/4 个 patch 达到代码量阈值）

- 日期：2026-07-06
- 状态：已合入
- 概括：清理 crypto 相关的旧接口、重复实现或风格问题，降低后续维护复杂度。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: atmel-tdes - simplify fast path in crypt_start
  - crypto: atmel-tdes - use __get_free_page in buff_init
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260706150404.382209-5-thorsten.blum@linux.dev/

**▸ 组织：Intel**（1 patches）

**[SERIES] crypto: iaa - Fixes for multi entry SG lists** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-08-05
- 状态：已合入
- 概括：集中修复 crypto 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。
- 达到阈值的 patches（4 个，显示前 5）：
  - crypto: iaa - avoid counting fallback decompression bytes
  - crypto: iaa - fall back to software for multi-entry scatterlists
  - crypto: iaa - use bounce buffer for multi-sg decompress input
  - crypto: iaa - unmap dst before software fallback on decompress
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260805-iaa-crypto-fixes-zswap-v2-3-55c02694f499@intel.com/

**▸ 组织：Red Hat**（1 patches）

**[SERIES] crypto: Provide a function for zeroizing crypto_aes_ctx** （cover letter，8/10 个 patch 达到代码量阈值）

- 日期：2026-08-10
- 状态：已合入
- 概括：围绕 Intel QAT 驱动的设备能力、复位、迁移或接口清理进行调整，提升硬件加速器在主线内核中的可维护性。
- 达到阈值的 patches（8 个，显示前 5）：
  - crypto: aspeed - clear the crypto_aes_ctx when done
  - crypto: padlock-aes - clear the crypto_aes_ctx when done
  - crypto: sa2ul - clear the crypto_aes_ctx when done
  - crypto: arm/aes-neonbs - clear the crypto_aes_ctx when done
  - crypto: arm64/aes-neonbs - clear the crypto_aes_ctx when done
  - ... 及其他 3 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260810093009.608090-3-thuth@redhat.com/

---

### ◆ 子系统：AF_ALG API（3 patches）

**▸ 组织：Kernel.org**（2 patches）

**[SERIES] crypto: af_alg_restrict cleanups** （cover letter，2/3 个 patch 达到代码量阈值）

- 日期：2026-08-02
- 状态：已合入
- 概括：清理 crypto 相关的旧接口、重复实现或风格问题，降低后续维护复杂度。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: af_alg - Make cbc(paes) privileged-only
  - crypto: af_alg - Stop after finding name in allowlist
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260802230055.100746-2-ebiggers@kernel.org/

**crypto: af_alg - Allow additional ciphers for cryptsetup**

- 日期：2026-07-05
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260705184419.40762-1-ebiggers@kernel.org/

**▸ 组织：Individual Contributor**（1 patches）

**crypto: af_alg: Allow cbc(paes)**

- 日期：2026-07-26
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260726192716.2351505-1-richard@nod.at/

---

### ◆ 子系统：Aead（3 patches）

**▸ 组织：Individual Contributor**（3 patches）

**crypto: ccree - use crypto_memneq() to compare AEAD tag**

- 日期：2026-08-15
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/aoCdZiqJjb5XDHHz@david.gall/

**crypto: sa2ul - use crypto_memneq() to compare AEAD tag**

- 日期：2026-08-07
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/anX9UKJ66Aak4ICV@fudgebox/

**[SERIES] crypto: keembay - use crypto_memneq() to compare GCM AEAD tags** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-07
- 状态：已合入
- 概括：归纳 crypto 系列中的关联改动，重点调整核心接口、驱动流程和异常处理逻辑。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: keembay - use crypto_memneq() to compare GCM AEAD tags
  - crypto: keembay - use crypto_memneq() to compare CCM AEAD tags
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/anYEQOzunX0Lm3N1@david.gall/

---

### ◆ 子系统：HWRNG（2 patches）

**▸ 组织：Bootlin**（2 patches）

**[v5] hwrng: core - Stop/start hwrng_fillfn() kthread before/after suspend-resume**

- 日期：2026-08-04
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260804-hw-random-fix-hwrng-fillfn-crash-suspend-resume-v5-1-c4769b3c007b@bootlin.com/

**[v2,2/2] hwrng: omap: Enable on Renesas RZ/N1D**

- 日期：2026-07-10
- 状态：已合入
- 概括：启用之前被禁用或条件编译的功能特性，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260710-schneider-v7-2-rc1-eip76-upstream-v2-2-4eab557b0e70@bootlin.com/

---

### ◆ 子系统：ICE (Qualcomm)（1 patches）

**▸ 组织：Linux Community**（1 patches）

**crypto: qat - use strscpy_pad to simplify adf_service_string_to_mask**

- 日期：2026-07-05
- 状态：已合入
- 概括：简化代码逻辑，减少不必要的复杂度，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260705133842.241401-3-thorsten.blum@linux.dev/

---

### ◆ 子系统：CESA (Marvell)（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: cesa: manage SRAM teardown with devm**

- 日期：2026-07-17
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260717231742.1174221-1-rosenp@gmail.com/

---

### ◆ 子系统：Ahash（1 patches）

**▸ 组织：Linux Community**（1 patches）

**crypto: bcm - use memcpy_and_pad in ahash_hmac_setkey**

- 日期：2026-07-20
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260720232249.117992-3-thorsten.blum@linux.dev/

---

### ◆ 子系统：CAAM (NXP)（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: caam: simplify probe resource and IRQ handling**

- 日期：2026-07-30
- 状态：已合入
- 概括：简化代码逻辑，减少不必要的复杂度，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260730204722.1101805-1-rosenp@gmail.com/

---

### ◆ 子系统：Kerberos（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto/krb5: use kfree_sensitive() for derived key buffers**

- 日期：2026-08-03
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260803192621.329577-1-linux@jaseg.de/

---

### ◆ 子系统：Authenc（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: octeontx2 - use crypto_memneq() to check HMAC for cipher_null authenc**

- 日期：2026-08-15
- 状态：已合入
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/aoCdBZ-kLQ0rciFi@david.gall/

---

### ◆ 子系统：ECC（1 patches）

**▸ 组织：Linux Community**（1 patches）

**[SERIES] crypto: atmel-ecc - simplify control flow in atmel_ecdh_set_secret** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-07-28
- 状态：已合入
- 概括：清理 crypto 相关的旧接口、重复实现或风格问题，降低后续维护复杂度。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: atmel-ecc - simplify control flow in atmel_ecdh_set_secret
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260728205825.471233-3-thorsten.blum@linux.dev/

---

### ◆ 子系统：QCE (Qualcomm)（1 patches）

**▸ 组织：Linux Community**（1 patches）

**[SERIES] crypto: qce - simplify devm_qce_register_algs** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-07-31
- 状态：已合入
- 概括：归纳 crypto 系列中的关联改动，重点调整核心接口、驱动流程和异常处理逻辑。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: qce - simplify qce_handle_request
  - crypto: qce - simplify devm_qce_register_algs
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260731102532.742739-4-thorsten.blum@linux.dev/

---

### ◆ 子系统：Asymmetric Keys（1 patches）

**▸ 组织：Canonical**（1 patches）

**[SERIES] crypto: asymmetric_keys - fix OOB read in pefile_parse_binary** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-08-15
- 状态：已合入
- 概括：集中修复 crypto 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: asymmetric_keys - add KUnit tests for the PE parser
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/fcbc6b4d5855ba42a0fccf335b2604ef0b36f092.1786802052.git.fabrice.derepas@canonical.com/

---

## 社区讨论中 Patches

### ◆ 子系统：General Crypto（40 patches）

**▸ 组织：Individual Contributor**（19 patches）

**[v2] crypto: ccp: Initialize DBC ioctl mutex before registering device**

- 日期：2026-08-30
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260830015104.2040153-1-runyu.xiao@seu.edu.cn/

**crypto: arm64/aes-neonbs: transition to kmalloc_obj()**

- 日期：2026-08-30
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260830101714.625728-3-manuelebnerli@mailbox.org/

**crypto: atmel-tdes - zero-initialize device state**

- 日期：2026-08-29
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260829035821.67220-1-kmehltretter@gmail.com/

**[SERIES] Add support for hashing algorithms in TI DTHE V2** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-27
- 状态：社区讨论中
- 概括：围绕 Add support for hashing algorithms in TI DTHE V2 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: ti - Add support for SHA224/256/384/512 in DTHEv2 driver
  - crypto: ti - Add support for HMAC in DTHEv2 driver
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260827133542.619717-2-t-pratham@ti.com/

**[SERIES] Fix several issues in DTHEv2 driver** （cover letter，2/7 个 patch 达到代码量阈值）

- 日期：2026-08-27
- 状态：社区讨论中
- 概括：集中修复 Fix several issues in DTHEv2 driver 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: ti - Trim scatterlists to correct length in AES
  - crypto: ti - Use list_first_entry_or_null() in dthe_get_dev()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260827132318.613876-5-t-pratham@ti.com/

**[SERIES] crypto: cmh - add Rambus CryptoManager Hub driver** （cover letter，15/15 个 patch 达到代码量阈值）

- 日期：2026-08-25
- 状态：社区讨论中
- 概括：围绕 crypto 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。
- 达到阈值的 patches（15 个，显示前 5）：
  - crypto: cmh - add HMAC ahash
  - crypto: cmh - add ML-KEM/ML-DSA (QSE)
  - crypto: cmh - add DRBG hwrng
  - crypto: cmh - add CSHAKE/KMAC ahash
  - crypto: cmh - add SHA-2/SHA-3/SHAKE ahash
  - ... 及其他 10 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260825221539.255951-6-aousherovitch@rambus.com/

**[SERIES] Add X.509 CRL support** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-08-22
- 状态：社区讨论中
- 概括：围绕 Add X.509 CRL support 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。
- 达到阈值的 patches（1 个，显示前 5）：
  - x509: add CRL parser with indirect CRL support
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260822082642.48936-3-tnovikov@astralinux.ru/

**[SERIES] crypto: amlogic: Fix IRQ handler return value and fallthrough logic** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-08-21
- 状态：社区讨论中
- 概括：集中修复 crypto 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: amlogic: Use devm APIs for clock and engine management
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260821151243.8125-1-raizudeen.kerneldev@gmail.com/

**[RFC] crypto: qat - zero the VF migration state buffer on save**

- 日期：2026-08-17
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260817042613.19855-1-kmehltretter@gmail.com/

**[v3,2/4] crypto: rockchip: Add RK356x/RK3588 cryptographic offloader driver**

- 日期：2026-08-16
- 状态：社区讨论中
- 概括：新增rk356x/rk3588 cryptographic offloader driver，扩展功能特性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260816194112.552100-3-dawidro@gmail.com/

**crypto: amcc: trng: use devm_of_iomap()**

- 日期：2026-08-12
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260812185747.79173-1-rosenp@gmail.com/

**[v2,12/13] crypto: api - wipe tfm contexts before kdump**

- 日期：2026-08-11
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260811-crash-zeroize-rework-v2-12-9561d13c2340@jaseg.de/

**[SERIES] crypto: img-hash: clean up probe** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-08-11
- 状态：社区讨论中
- 概括：集中修复 crypto 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: img-hash: fetch resources into locals before probe body
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260811212030.20057-2-rosenp@gmail.com/

**crypto: amcc: get irq and ioremap resource first**

- 日期：2026-07-30
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260730204915.1102403-1-rosenp@gmail.com/

**[SERIES] crypto: introduce generic dynamic software fallback and EIP93 support** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-07-28
- 状态：社区讨论中
- 概括：围绕 crypto 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。
- 达到阈值的 patches（4 个，显示前 5）：
  - crypto: move cycle benchmark helpers out of tcrypt
  - crypto: introduce dynamic software fallback
  - crypto: eip93 - add dynamic software fallback support
  - crypto: eliminate fallback proxy overhead while disabled
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/e0ce93088c1d9772e928fcbd113a446b7fb7442f.1785226804.git.hurryman2212@gmail.com/

**lib/crypto: x86/chacha: Add a 16-block AVX-512 variant**

- 日期：2026-07-22
- 状态：社区讨论中
- 概括：新增a 16-block avx-512 variant，扩展功能特性，增强框架的功能完整性和适用范围，满足更多使用场景的需求
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260722153247.630519-1-martin@strongswan.org/

**[SERIES] lib/crypto: add HKDF and convert fscrypt and NVMe** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-07-21
- 状态：社区讨论中
- 概括：围绕 lib/crypto 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。
- 达到阈值的 patches（2 个，显示前 5）：
  - lib/crypto: tests: add HKDF KUnit tests
  - lib/crypto: add HKDF-SHA{256,384,512}
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260721140644.780006-3-marco@mandelbit.com/

**crypto: verify_pefile - Use constant-time digest comparison**

- 日期：2026-07-20
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260720031815.204237-1-yijiangshan@kylinos.cn/

**[SERIES] crypto: eip93: fix request lifetime and completion handling** （cover letter，4/5 个 patch 达到代码量阈值）

- 日期：2026-07-07
- 状态：社区讨论中
- 概括：集中修复 crypto 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。
- 达到阈值的 patches（4 个，显示前 5）：
  - crypto: eip93: reject HMAC requests before setkey
  - crypto: eip93: use request-local SA records for cipher requests
  - crypto: eip93: order result descriptor reads after PE_READY
  - crypto: eip93: handle request ID exhaustion
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260707171537.467608-2-hurryman2212@gmail.com/

**▸ 组织：Kernel.org**（7 patches）

**[SERIES] lib/crypto: KUnit tests for AES-CCM and AES-GCM** （cover letter，5/5 个 patch 达到代码量阈值）

- 日期：2026-08-02
- 状态：社区讨论中
- 概括：围绕 lib/crypto 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。
- 达到阈值的 patches（5 个，显示前 5）：
  - lib/crypto: tests: Create test-utils.h
  - lib/crypto: tests: Use per-test-case buffers in hash tests
  - lib/crypto: tests: Add KUnit test suite for AES-CCM
  - lib/crypto: tests: Add KUnit test suite for AES-GCM
  - lib/crypto: tests: Add aead-test-template.h
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260802233005.161467-2-ebiggers@kernel.org/

**[SERIES] lib/crypto: FIPS self-tests for AES encryption modes** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-08-02
- 状态：社区讨论中
- 概括：围绕 lib/crypto 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。
- 达到阈值的 patches（3 个，显示前 5）：
  - lib/crypto: fips: Split fips.h into fips-aes.h and fips-sha.h
  - lib/crypto: aes: Add FIPS self-tests for unauthenticated modes
  - lib/crypto: aes: Add FIPS self-tests for GCM and CCM
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260802222408.91757-2-ebiggers@kernel.org/

**crypto: qce - Replace with stub driver**

- 日期：2026-07-31
- 状态：社区讨论中
- 概括：更新相关配置项或代码引用，保持子系统与内核主线的兼容性，适应 API 和框架的演进方向
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260731050838.158825-1-ebiggers@kernel.org/

**[SERIES] More padata cleanups** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-07-17
- 状态：社区讨论中
- 概括：清理 More padata cleanups 相关的旧接口、重复实现或风格问题，降低后续维护复杂度。
- 达到阈值的 patches（2 个，显示前 5）：
  - padata: Free the padata_works when they're no longer needed
  - padata: Mark remaining code as __init and data as __initdata
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260717171831.27994-3-ebiggers@kernel.org/

**[SERIES] Library APIs for AES encryption modes** （cover letter，12/13 个 patch 达到代码量阈值）

- 日期：2026-07-15
- 状态：社区讨论中
- 概括：围绕 Library APIs for AES encryption modes 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。
- 达到阈值的 patches（12 个，显示前 5）：
  - crypto: xts - Split out __xts_verify_key() helper
  - lib/crypto: aes: Add ECB support
  - lib/crypto: aes: Add CBC and CBC-CTS support
  - lib/crypto: aes: Add CTR and XCTR support
  - lib/crypto: aes: Add XTS support
  - ... 及其他 7 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260715221153.246410-2-ebiggers@kernel.org/

**[2/2] padata: Remove serialized job support**

- 日期：2026-07-13
- 状态：社区讨论中
- 概括：移除serialized job support，清理冗余或过时的代码，精简代码库规模，降低后续维护的复杂度和引入回归问题的风险
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260713223234.24812-3-ebiggers@kernel.org/

**lib/crypto: docs: Improve introduction sentence**

- 日期：2026-07-09
- 状态：社区讨论中
- 概括：改进introducti，提升健壮性和性能，提升代码的可读性和可维护性，为后续功能迭代奠定更清晰的基础
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260709022747.44635-1-ebiggers@kernel.org/

**▸ 组织：Red Hat**（6 patches）

**[v3] crypto: inside-secure - Zeroize temporary arrays on stack with sensitive data**

- 日期：2026-08-19
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260819151845.835768-1-thuth@redhat.com/

**lib/crypto: chacha20poly1305: Clear chacha_state in xchacha20poly1305_decrypt()**

- 日期：2026-08-13
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260813130147.949545-1-thuth@redhat.com/

**[SERIES] libcrypto: Provide more __cleanup functions for zeroizing data** （cover letter，7/7 个 patch 达到代码量阈值）

- 日期：2026-08-13
- 状态：社区讨论中
- 概括：清理 libcrypto 相关的旧接口、重复实现或风格问题，降低后续维护复杂度。
- 达到阈值的 patches（7 个，显示前 5）：
  - lib/crypto: aes: Provide a wrapper function for zeroizing crypto_aes_ctx
  - lib/crypto: aes: Use aes_zeroize_*key() instead of memzero_explicit()
  - lib/crypto: aes: Provide functions for zeroizing aes_key and aes_enckey
  - lib/crypto: md5: Use hmac_md5_zeroize_ctx() instead of memzero_explicit()
  - lib/crypto: sha1: Provide a wrapper for zeroizing hmac_sha1_ctx
  - ... 及其他 2 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260813134953.979481-2-thuth@redhat.com/

**[SERIES] lib/crypto: Provide a function for zeroizing hmac_sha1_ctx** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-12
- 状态：社区讨论中
- 概括：归纳 lib/crypto 系列中的关联改动，重点调整核心接口、驱动流程和异常处理逻辑。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: Provide a wrapper for zeroizing hmac_sha1_ctx
  - lib/crypto: sha1: Use hmac_sha1_zeroize_ctx() instead of memzero_explicit()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260812163336.3103835-2-thuth@redhat.com/

**[SERIES] crypto: Add __cleanup functions for zeroizing aes_cmac_key & aes_cmac_ctx** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-08-07
- 状态：社区讨论中
- 概括：围绕 crypto 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: Provide wrapper functions for zeroizing aes_cmac_key and aes_cmac_ctx
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260807125845.1477067-2-thuth@redhat.com/

**[RFC] crypto: pcrypt - Disallow nesting of the pcrypt wrapper**

- 日期：2026-07-01
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260701143947.944593-1-thuth@redhat.com/

**▸ 组织：Huawei**（2 patches）

**crypto: hisilicon/zip - enable auto clock gating for DAE**

- 日期：2026-08-29
- 状态：社区讨论中
- 概括：启用之前被禁用或条件编译的功能特性，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260829094924.2191402-1-huangchenghai2@huawei.com/

**[v2] crypto: hisilicon/sec - remove SEC crypto block cipher accelerator**

- 日期：2026-08-19
- 状态：社区讨论中
- 概括：移除sec crypto block cipher accelerator，清理冗余或过时的代码，精简代码库规模，降低后续维护的复杂度和引入回归问题的风险
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260819075353.94500-1-huangchenghai2@huawei.com/

**▸ 组织：Qualcomm**（2 patches）

**[SERIES] crypto/dmaengine: qce: introduce BAM locking and use DMA for register I/O** （cover letter，7/8 个 patch 达到代码量阈值）

- 日期：2026-07-23
- 状态：社区讨论中
- 概括：围绕 crypto/dmaengine 增加新的硬件、UAPI 或框架能力，扩展子系统可支持的设备和虚拟化使用场景。
- 达到阈值的 patches（7 个，显示前 5）：
  - crypto: qce - Cancel work on device detach
  - crypto: qce - Include algapi.h in the core.h header
  - crypto: qce - Simplify arguments of devm_qce_dma_request()
  - crypto: qce - Use existing devres APIs in devm_qce_dma_request()
  - crypto: qce - Map crypto memory for DMA
  - ... 及其他 2 个 patch
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260723-qcom-qce-cmd-descr-v24-7-4f87bb4d9938@oss.qualcomm.com/

**[SERIES] crypto: qce - Fix crypto self-test failures** （cover letter，5/8 个 patch 达到代码量阈值）

- 日期：2026-07-17
- 状态：社区讨论中
- 概括：集中修复 crypto 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。
- 达到阈值的 patches（5 个，显示前 5）：
  - crypto: qce - Reject empty messages for AES-XTS
  - crypto: qce - Use a fallback for AES-CTR with a partial final block
  - crypto: qce - Use a fallback for CCM with a partial final block
  - crypto: qce - Use fallback for CCM with a fragmented payload
  - crypto: qce - Use fallback for fragmented skcipher payloads
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260717-qce-fix-self-tests-v6-1-455775fe5f6c@oss.qualcomm.com/

**▸ 组织：AMD**（1 patches）

**[3/3] crypto: xilinx: zynqmp-aes-gcm: Send firmware decoded code instead of EBADMSG**

- 日期：2026-07-06
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260706110254.2427551-4-h.jain@amd.com/

**▸ 组织：Oracle**（1 patches）

**padata: Replace bottom-half spinlock variants**

- 日期：2026-07-17
- 状态：社区讨论中
- 概括：更新相关配置项或代码引用，保持子系统与内核主线的兼容性，适应 API 和框架的演进方向
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260717205028.63847-1-daniel.m.jordan@oracle.com/

**▸ 组织：Intel**（1 patches）

**[1/2] crypto: qat - allow KPT disable when service is not asym**

- 日期：2026-08-31
- 状态：社区讨论中
- 概括：禁用存在稳定性或安全性问题的功能，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260831063355.668528-2-nitesh.venkatesh@intel.com/

**▸ 组织：Linux Community**（1 patches）

**[SERIES] crypto: zstd - avoid initializing the workspace twice** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-25
- 状态：社区讨论中
- 概括：归纳 crypto 系列中的关联改动，重点调整核心接口、驱动流程和异常处理逻辑。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: zstd - Avoid redundant cstream initialization
  - crypto: zstd - Avoid redundant dstream initialization
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260825220616.3842633-2-usama.arif@linux.dev/

---

### ◆ 子系统：Public Key（6 patches）

**▸ 组织：Individual Contributor**（6 patches）

**[SERIES] crypto: rsassa-pkcs1: fix undersized key handling** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-26
- 状态：社区讨论中
- 概括：集中修复 crypto 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: rsassa-pkcs1: reject undersized keys when signing
  - crypto: rsassa-pkcs1: reject undersized keys when verifying
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260826103744.1554131-2-Jeremy.Jean@oss.cyber.gouv.fr/

**crypto: rsassa-pkcs1 - Use constant-time digest comparison**

- 日期：2026-07-20
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260720021322.122784-1-yijiangshan@kylinos.cn/

**crypto: pkcs7 - Use constant-time message digest comparison**

- 日期：2026-07-20
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260720032316.210113-1-yijiangshan@kylinos.cn/

**[6.1/6.6/6.12.y] crypto: rsa-pkcs1pad: Don't WARN on an empty digest**

- 日期：2026-07-20
- 状态：社区讨论中
- 概括：限制warn，增加条件判断和安全保护逻辑，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260720191525.15450-1-doruk@0sec.ai/

**crypto: rsassa-pkcs1: use constant-time comparison for digest and signature verification**

- 日期：2026-07-10
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/alEr_e-G0L2nxxv-@fudgebox/

**crypto: pkcs7_verify: use constant-time comparison for digest and signature verification**

- 日期：2026-07-10
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/alEsSl8i1_FpoU0f@fudgebox/

---

### ◆ 子系统：CAAM (NXP)（2 patches）

**▸ 组织：Individual Contributor**（2 patches）

**crypto: caam - reject overlong RSA CRT parameters**

- 日期：2026-08-10
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260810154024.3178145-1-Jeremy.Jean@oss.cyber.gouv.fr/

**[SERIES] crypto: caam: Fix DMA mapping leak in the cbc(paes) job path** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-07-26
- 状态：社区讨论中
- 概括：集中修复 crypto 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: caam: Map the paes protected key once per tfm
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260726081504.2182951-2-richard@nod.at/

---

### ◆ 子系统：Talitos（2 patches）

**▸ 组织：Individual Contributor**（2 patches）

**crypto: talitos: pass talitos_private to irq handlers**

- 日期：2026-08-11
- 状态：社区讨论中
- 概括：传递各层之间正确传递参数和状态信息，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260811043953.150589-1-rosenp@gmail.com/

**[SERIES] crypto: talitos - fix rename first/last to first_desc/last_desc** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-07-09
- 状态：社区讨论中
- 概括：集中修复 crypto 相关的错误处理、生命周期或并发问题，降低异常路径触发崩溃和资源泄漏的风险。
- 达到阈值的 patches（3 个，显示前 5）：
  - crypto: talitos - stop using crypto_ahash::init
  - crypto: talitos - fix SEC1 32k ahash request limitation
  - crypto: talitos - rename first/last to first_desc/last_desc
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260709193956.15619-4-ggoerisch@gmail.com/

---

### ◆ 子系统：HWRNG（2 patches）

**▸ 组织：SUSE**（1 patches）

**[v2,07/13] hw_random/via-rng: Stop using 32-bit MSR interfaces**

- 日期：2026-08-19
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260819102314.1499258-8-jgross@suse.com/

**▸ 组织：Individual Contributor**（1 patches）

**hwrng: imx-rngc: check clk_prepare_enable() return value**

- 日期：2026-08-28
- 状态：社区讨论中
- 概括：启用之前被禁用或条件编译的功能特性，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260828025423.2149304-1-dayou5941@163.com/

---

### ◆ 子系统：AF_ALG API（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[5.10/5.15] crypto: af_alg - Set merge to zero early in af_alg_sendmsg**

- 日期：2026-07-01
- 状态：社区讨论中
- 概括：修改将 merge 配置为 zero，调整运行参数，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260701160121.100720-1-mdmitrichenko@astralinux.ru/

---

### ◆ 子系统：ECC（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[RFC,RESEND,v6,1/1] crypto: atmel-ecc - fix multi-device use-after-free and registration races**

- 日期：2026-07-12
- 状态：社区讨论中
- 概括：修复use-after-free 漏洞，防止在错误恢复路径中访问已释放的内存对象，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260712200203.47764-1-l.rubusch@gmail.com/

---

### ◆ 子系统：CESA (Marvell)（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: cesa: check for sram_dma NULL**

- 日期：2026-07-13
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260713050740.3687230-1-rosenp@gmail.com/

---

### ◆ 子系统：Kerberos（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: krb5 - Use constant-time checksum comparison**

- 日期：2026-07-20
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260720031304.198172-1-yijiangshan@kylinos.cn/

---

### ◆ 子系统：Asymmetric Keys（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: asymmetric_keys: copy X.509 TBS for data signature algorithms**

- 日期：2026-08-21
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260821192502.3942767-2-Jeremy.Jean@oss.cyber.gouv.fr/

---

### ◆ 子系统：Skcipher（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: mxs-dcp: handle zero-length skcipher requests**

- 日期：2026-08-28
- 状态：社区讨论中
- 概括：修改对代码进行调整和优化，修正细节问题或适应内核框架的变更，持续改进代码质量和功能完备性
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260828093209.3179074-1-lilinmao@kylinos.cn/

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

*报告由 Linux Patches Tracker 自动生成 | 2026-09-08 14:59:09*
