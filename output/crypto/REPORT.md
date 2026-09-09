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
| 社区讨论中 | 57 | 55.3% |
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
| Red Hat | [PATCH v5 00/10] crypto: Provide a function for zeroizing crypto_aes_ctx ------新增 aes_zeroize_ctx() 等 AES 上下文清零封装，并让 aspeed、padlock、sa2ul、arm/arm64 aes-neonbs、qat、safexcel 等实现在操作结束后统一清除 crypto_aes_ctx 中的密钥材料。 |
| Intel | [PATCH v2 00/5] crypto: iaa - Fixes for multi entry SG lists ------在 IAA crypto 驱动中修复多 entry SG 列表：新增 deflate_generic_compress() 用于多 SG 压缩的软件回退，解压输入经 iaa_req_ctx.bounce_src 申请 iaa_bounce_pool 页拷贝为单 SG 后再提交硬件，并把解压字节统计移入非回退的硬件完成分支，软件回退前调用 iaa_unmap_src() 等解除 src/dst 的 DMA 映射。 |
| Kernel.org | [PATCH v1 00/3] crypto: af_alg_restrict cleanups ------清理 AF_ALG 限制列表逻辑：将 cbc(paes) 标记为非特权可用，并调整 af_alg_check_restriction() 的同名条目匹配流程，避免无特权时继续遍历后续 allowlist 项造成权限判断歧义。 |
| Individual Contributor | [PATCH v1 00/2] crypto: keembay - use crypto_memneq() to compare GCM AEAD tags ------keembay OCS 的 GCM 解密路径将 rctx->in_tag 与 rctx->out_tag 的比较改用 crypto_memneq，CCM 的 ccm_compare_tag_to_yr 函数中 tag 与 yr 的比较也改用 crypto_memneq，两者均在标签不匹配时返回 -EBADMSG，替代 memcmp 以消除时序泄露。 |
| Linux Community | [PATCH v1 00/2] crypto: qce - simplify devm_qce_register_algs ------在 Qualcomm crypto engine (qce) 驱动中简化两处逻辑：qce_handle_request() 遍历 qce_ops 时发现 type 匹配就直接 return ops->async_req_handle(async_req)，否则返回 -EINVAL。 |
| Canonical | [v2,2/2] crypto: asymmetric_keys - add KUnit tests for the PE parser ------为 asymmetric_keys 的 PE parser 增加 KUnit 覆盖，验证安全目录和 section 边界处理等异常输入，防止 pefile_parse_binary() 越界读问题回归。 |
| Kernel.org | [PATCH] crypto: af_alg - Allow additional ciphers for cryptsetup ------在 AF_ALG skcipher allowlist 中加入 cryptsetup 使用的 xts(camellia)、xts(serpent)、xts(twofish) 等算法条目，让用户态磁盘加密工具继续通过 AF_ALG socket 调用这些 cipher。 |
| Bootlin | [v5] hwrng: core - Stop/start hwrng_fillfn() kthread before/after suspend-resume ------在 hwrng core 中注册 PM notifier，系统 suspend/hibernate 前停止 hwrng_fillfn kthread 并记录停止状态，resume/restore 后再重新启动，避免休眠阶段后台线程继续触碰 RNG 设备。 |
| Bootlin | [v2,2/2] hwrng: omap: Enable on Renesas RZ/N1D ------在 drivers/char/hw_random/Kconfig 中将 HW_RANDOM_OMAP 的依赖列表加入 ARCH_RZN1，使 OMAP RNG 驱动可以在 Renesas RZ/N1D 平台上被配置和编译。 |
| Linux Community | [PATCH] crypto: qce - simplify control flow in register functions ------在 qce 的 aead.c、sha.c、skcipher.c 注册函数中，将寄存器循环内失败后的 goto err 分支改为立即调用 qce_aead_unregister()/qce_ahash_unregister()/qce_skcipher_unregister() 并 return ret，去掉共享的 err 标签和末尾回滚路径。 |
| Individual Contributor | [PATCH] crypto: octeontx2 - use crypto_memneq() to check HMAC for cipher_null authenc ------在 octeontx2 CPT 驱动的 validate_hmac_cipher_null() 中，将比较 rctx->fctx.hmac.s.hmac_calc 与 hmac_recv 的 memcmp 改为 crypto_memneq()，认证失败仍返回 -EBADMSG，以避免 HMAC 校验的时间侧信道泄漏。 |
| Individual Contributor | [PATCH] crypto: octeontx - use crypto_memneq() to check HMAC ------在 octeontx CPT 驱动的 validate_hmac_cipher_null() 中，把 memcmp 比较 hmac_calc 与 hmac_recv 替换为 crypto_memneq()，防止非恒定时间比较泄露 HMAC 信息。 |
| Individual Contributor | [PATCH] crypto: ccree - use crypto_memneq() to compare AEAD tag ------在 ccree 驱动 cc_aead_complete() 的解密分支中，将 mac_buf 与 icv_virt_addr 的 memcmp 比较改为 crypto_memneq()，认证失败时按原路径处理，消除标签校验的时序差异。 |
| Individual Contributor | [PATCH] crypto: amcc: pass core_dev to request_irq ------在 crypto4xx 驱动 probe/remove 的 request_irq/free_irq 中，把中断上下文数据由 struct device *dev 改为 struct crypto4xx_core_device *core_dev，中断处理函数 crypto4xx_interrupt_handler 直接使用 data 作为 core_dev 并去掉 dev_get_drvdata 转换。 |
| Individual Contributor | [PATCH] crypto: s5p-sss: pass s5p_aes_dev to irq handler ------在 s5p-sss 驱动中将 s5p_aes_interrupt 的 dev_id 参数由 platform_device 改为 s5p_aes_dev，并在 devm_request_threaded_irq 调用点直接传入 pdata，使中断回调不再通过 platform_get_drvdata 间接获取设备结构。 |
| Individual Contributor | [PATCH] crypto: rockchip: pass crypto_info to irq handler ------在 rk3288_crypto 驱动中将 rk_crypto_irq_handle 的 dev_id 参数由 platform_device 改为 rk_crypto_info，并在 devm_request_irq 调用点传入 crypto_info 而非 pdev，去掉中断处理中的 platform_get_drvdata 调用。 |
| Individual Contributor | [PATCH] crypto: sa2ul - use crypto_memneq() to compare AEAD tag ------在 sa2ul 驱动的 sa_aead_dma_in_callback 中，用 crypto_memneq 替换 memcmp 比较 AEAD 认证标签与 mdptr 偏移处的收尾 tag，标签不一致时返回 -EBADMSG 以避免时间侧信道。 |
| Individual Contributor | [PATCH] crypto/krb5: use kfree_sensitive() for derived key buffers ------在 crypto_krb5_prepare_encryption() 与 crypto_krb5_prepare_checksum() 的成功及错误路径中，将释放派生密钥缓冲区 keys.data 的 kfree() 改为 kfree_sensitive()，使缓冲区释放前被清零，避免敏感密钥数据残留。 |
| Individual Contributor | [PATCH] crypto: eip93 - use struct_size() and flexible array for ring allocation ------为 eip93 驱动把 struct eip93_device 末尾的 ring 指针改为灵活的 struct eip93_ring ring[] 数组成员，移除单独 devm_kcalloc() 分配 ring 的代码，在 eip93_crypto_probe() 中用 devm_kzalloc(... struct_size(eip93, ring, 1) ...) 一次性分配设备结构与单个 ring 对象。 |
| Individual Contributor | [PATCH] crypto: ccp - don't abuse kernel-doc comment format ------在 include/uapi/linux/psp-sfs.h 中把描述 AMD Seamless Firmware Support (SFS) 接口及 IOCTL 的注释起始符从 /** 改为 /*，避免被内核文档工具误当 kernel-doc 解析，注释内容本身不变。 |

### 社区讨论

| 厂商 | 简介 |
|------|------|
| Individual Contributor | [PATCH v4 00/19] crypto: cmh - add Rambus CryptoManager Hub driver ------新增 Rambus CryptoManager Hub 平台驱动，向 crypto API 注册 HMAC-SHA2/SHA3、CSHAKE/KMAC、SHA-2/3/SM3、AES/SM4、ChaCha20-Poly1305、RSA、ECDH/X25519、ML-KEM/ML-DSA 以及 DRBG hwrng 能力。 |
| Kernel.org | [PATCH v2 00/13] Library APIs for AES encryption modes ------在 lib/crypto 中新增 AES 的 ECB、CBC/CBC-CTS、CTR/XCTR、XTS、GCM、CCM 库接口，并新增 include/crypto/aes-*.h 头文件和文档，同时让 crypto 层的对应算法模板改为调用这些库实现，并从 crypto/xts 中拆分出 __xts_verify_key() 辅助函数。 |
| Qualcomm | [PATCH v24 00/14] crypto/dmaengine: qce: introduce BAM locking and use DMA for register I/O ------QCE crypto 驱动将寄存器访问改为 BAM DMA：qce_write 改用新增 qce_write_dma() 命令码下发，probe 记录 base_phys/dma_size 并 dma_map_resource，devm_qce_dma_request() 为 BAM 配置 lock_scratchpad_addr=base_phys+REG_VERSION。 |
| Individual Contributor | [PATCH v3 00/5] crypto: talitos - fix rename first/last to first_desc/last_desc ------清理 talitos ahash 请求上下文字段命名，将 first/last 改为 first_desc/last_desc，并同步调整 ahash digest/init/finup 路径及 sha224 软件初始化处理。 |
| Individual Contributor | [PATCH v1 00/4] crypto: introduce generic dynamic software fallback and EIP93 support ------为 Crypto API 新增 CONFIG_CRYPTO_DYNAMIC_FALLBACK 与 crypto/fallback.c，提供依据 benchmark 结果动态切换软回退的机制；EIP93 驱动在 Kconfig 中 select CRYPTO_DYNAMIC_FALLBACK 及 AES/CBC/CTR/DES/ECB/HMAC 并新增 eip93-fallback.c。 |
| Individual Contributor | [PATCH v7 00/2] Add support for hashing algorithms in TI DTHE V2 ------TI DTHEV2 crypto 驱动新增哈希算法支持：Kconfig 选入 CRYPTO_SHA256/SHA512/CRYPTO_HMAC，Makefile 增加 dthev2-hash.o，新文件实现 SHA224/256/384/512 与 HMAC 的 ahash 注册。 |
| Individual Contributor | [PATCH v1 00/5] lib/crypto: add HKDF and convert fscrypt and NVMe ------在 lib/crypto 中新增 HKDF-SHA256/384/512 extract/expand 库接口和 KUnit 覆盖，并把 fscrypt 与 NVMe 的密钥派生逻辑迁移到统一 HKDF helper。 |
| Kernel.org | [PATCH v2 00/5] lib/crypto: KUnit tests for AES-CCM and AES-GCM ------为 lib/crypto 的 AES-CCM 与 AES-GCM 库接口新增 KUnit 测试，抽出 aead-test-template.h/test-utils.h 复用测试模板，并让 hash 测试改为每个用例独立分配缓冲区。 |
| Kernel.org | [PATCH v1 00/3] lib/crypto: FIPS self-tests for AES encryption modes ------为 lib/crypto/aes.c 增加 AES 模式 FIPS 启动自检，覆盖 ECB、GCM、CCM 等加解密向量校验，并将 fips.h 拆分为 fips-aes.h 与 fips-sha.h；自检失败时触发 panic。 |
| Individual Contributor | [RFC,RESEND,v6,1/1] crypto: atmel-ecc - fix multi-device use-after-free and registration races ------在 atmel-ecc.c 中引入 atmel_ecc_kpp_lock、kpp_refcnt 和 completion，让 atmel_ecc_remove() 等待 tfm_count 归零后才释放 i2c 客户端，而 atmel_ecc_probe() 在注册 kpp 前等待旧实例注销完成（超时返回 -ETIMEDOUT），修复多设备并发注册/注销时 i2c_priv 被释放后仍被 TFM 访问的 use-after-free。 |
| Kernel.org | [2/2] padata: Remove serialized job support ------从 padata 中删除 serialized job 支持，移除对应文档、serial cpumask 回调和 padata_do_parallel() 的串行作业路径，只保留并行 multithreaded job 机制。 |
| Individual Contributor | [v5,3/3] crypto: ti - Add support for HMAC in DTHEv2 Hashing Engine driver ------在 TI DTHEv2 hash 驱动的 Kconfig 中 select CRYPTO_HMAC，将 dthe_tfm_ctx 的 DTHE_MAX_KEYSIZE 由 AES-XTS 的 64 字节改为 SHA512_BLOCK_SIZE，并在 dthe_hash_req_ctx 增加 odigest 缓冲。 |
| Individual Contributor | [v3,2/4] crypto: rockchip: Add RK356x/RK3588 cryptographic offloader driver ------为 Rockchip RK356x/RK3588 新增加密 offloader 驱动，加入 CRYPTO_DEV_ROCKCHIP2 Kconfig/Makefile 条目和 rk2_crypto.c 平台驱动，接入这些 SoC 的硬件加密加速器。 |
| Individual Contributor | [2/3] x509: add CRL parser with indirect CRL support ------在 crypto/asymmetric_keys 的 X.509 解析器中新增 CRL 解析，加入 x509_crl.asn1 和 x509_idp.asn1，处理 IssuingDistributionPoint、certificateIssuer 与 CRLReason 扩展以支持 indirect CRL。 |
| Individual Contributor | [RFC] crypto: qat - zero the VF migration state buffer on save ------在 QAT gen4 VF 迁移保存路径中，adf_gen4_vfmig_save_setup() 使用 memset(mdev->state, 0, mdev->state_size) 清零整个状态缓冲，adf_gen4_vfmig_save_state() 再清零 setup 区之后的部分，然后才初始化 mstate_mgr，避免未初始化迁移状态被保存。 |
| Individual Contributor | [PATCH] crypto: talitos: pass talitos_private to irq handlers ------将 talitos1/2 中断处理程序的 request_irq() dev_id 从 struct device *dev 改为 struct talitos_private *priv，使回调宏直接以 data 作为 priv 使用，并在错误路径调用 talitos_error(priv->dev, ...)，替换原先的 dev_get_drvdata(dev) 间接查找。 |
| Individual Contributor | [PATCH] lib/crypto: x86/chacha: Add a 16-block AVX-512 variant ------在 lib/crypto/x86 中新增 chacha-avx512-x86_64.S 和 chacha_16block_xor_avx512()，利用 AVX-512 zmm 寄存器一次并行处理 16 个 ChaCha block 的加解密异或。 |

---

## 已合入 Patches

### ◆ 子系统：General Crypto（20 patches）

**▸ 组织：Individual Contributor**（12 patches）

**crypto: octeontx - use crypto_memneq() to check HMAC**

- 日期：2026-08-15
- 状态：已合入
- 概括：在 crypto 中改用 crypto_memneq() to check HMAC。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/aoCdOiyhQZZsFm5S@david.gall/

**crypto: amcc: pass core_dev to request_irq**

- 日期：2026-08-12
- 状态：已合入
- 概括：在 crypto: amcc 中传递 core_dev to request_irq。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260812191555.93423-1-rosenp@gmail.com/

**crypto: s5p-sss: pass s5p_aes_dev to irq handler**

- 日期：2026-08-11
- 状态：已合入
- 概括：在 crypto: s5p-sss 中传递 s5p_aes_dev to irq handler。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260811043358.136042-1-rosenp@gmail.com/

**crypto: rockchip: pass crypto_info to irq handler**

- 日期：2026-08-11
- 状态：已合入
- 概括：在 crypto: rockchip 中传递 crypto_info to irq handler。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260811044916.160856-1-rosenp@gmail.com/

**crypto: eip93 - use struct_size() and flexible array for ring allocation**

- 日期：2026-08-03
- 状态：已合入
- 概括：在 crypto 中为 ring allocation 改用 struct_size() and flexible array。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260803224028.87631-1-rosenp@gmail.com/

**crypto: ccp - don't abuse kernel-doc comment format**

- 日期：2026-07-30
- 状态：已合入
- 概括：在 crypto 中避免 abuse kernel-doc comment format。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260730051710.1412969-1-rdunlap@infradead.org/

**crypto: ccm - Set rfc4309 maxauthsize from child**

- 日期：2026-07-20
- 状态：已合入
- 概括：在 crypto 中设置 rfc4309 maxauthsize from child。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/al17HaL8wNd_fuDc@gondor.apana.org.au/

**crypto: hisilicon/sec: use devm_platform_ioremap_resource in sec_map_io**

- 日期：2026-07-15
- 状态：已合入
- 概括：在 crypto: hisilicon/sec 中改用 devm_platform_ioremap_resource in sec_map_io。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260715011533.1278258-1-rosenp@gmail.com/

**crypto: omap-aes: use devm_platform_get_and_ioremap_resource**

- 日期：2026-07-15
- 状态：已合入
- 概括：在 crypto: omap-aes 中改用 devm_platform_get_and_ioremap_resource。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260715215848.410011-1-rosenp@gmail.com/

**crypto: omap-sham: use devm_platform_get_and_ioremap_resource**

- 日期：2026-07-15
- 状态：已合入
- 概括：在 crypto: omap-sham 中改用 devm_platform_get_and_ioremap_resource。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260715220013.416122-1-rosenp@gmail.com/

**crypto: keembay - Initialize completion before requesting IRQ**

- 日期：2026-07-14
- 状态：已合入
- 概括：在 crypto 中Initialize completion（在 requesting IRQ 前）。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260714033015.367735-1-lilinmao@kylinos.cn/

**crypto: keembay - publish OF module alias for OCS AES/SM4**

- 日期：2026-07-14
- 状态：已合入
- 概括：在 crypto 中publish OF module alias for OCS AES/SM4。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260714131442.153699-1-pengcan@kylinos.cn/

**▸ 组织：Linux Community**（6 patches）

**crypto: qce - simplify control flow in register functions**

- 日期：2026-08-15
- 状态：已合入
- 概括：在 crypto 中simplify control flow in register functions。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260815150946.12142-3-thorsten.blum@linux.dev/

**crypto: starfive - use scatterlist length before DMA mapping**

- 日期：2026-07-25
- 状态：已合入
- 概括：在 crypto 中改用 scatterlist length（在 DMA mapping 前）。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260725090609.315812-2-thorsten.blum@linux.dev/

**crypto: octeontx - simplify get_{eng,ucode}_type_str helpers**

- 日期：2026-07-23
- 状态：已合入
- 概括：在 crypto 中simplify get_{eng,ucode}_type_str helpers。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260723163326.163043-2-thorsten.blum@linux.dev/

**crypto: powerpc/aes - use bool for encryption/decryption flag**

- 日期：2026-07-11
- 状态：已合入
- 概括：在 crypto 中为 encryption/decryption flag 改用 bool。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260711145216.747128-3-thorsten.blum@linux.dev/

**crypto: atmel-sha204a - clear RNG data from memory**

- 日期：2026-07-08
- 状态：已合入
- 概括：在 crypto 中清除 RNG data from memory。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260708150359.545852-2-thorsten.blum@linux.dev/

**[SERIES] crypto: atmel-tdes - simplify fast path in crypt_start** （cover letter，2/4 个 patch 达到代码量阈值）

- 日期：2026-07-06
- 状态：已合入
- 概括：simplify fast path in crypt_start、改用 __get_free_page in buff_init、删除 redundant return variable in crypt_pdc_stop，并删除 redundant if check in crypt_dma_stop。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: atmel-tdes - simplify fast path in crypt_start
  - crypto: atmel-tdes - use __get_free_page in buff_init
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260706150404.382209-5-thorsten.blum@linux.dev/

**▸ 组织：Intel**（1 patches）

**[SERIES] crypto: iaa - Fixes for multi entry SG lists** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-08-05
- 状态：已合入
- 概括：避免 counting fallback decompression bytes、fall back to software for multi-entry scatterlists、为 multi-sg decompress input 改用 bounce buffer，并unmap dst（在 software fallback on decompress 前）。
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
- 概括：新增 aes_zeroize_ctx() 等 AES 上下文清零封装，并让 aspeed、padlock、sa2ul、arm/arm64 aes-neonbs、qat、safexcel 等实现在操作结束后统一清除 crypto_aes_ctx 中的密钥材料。
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
- 概括：清理 AF_ALG 限制列表逻辑：将 cbc(paes) 标记为非特权可用，并调整 af_alg_check_restriction() 的同名条目匹配流程，避免无特权时继续遍历后续 allowlist 项造成权限判断歧义。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: af_alg - Make cbc(paes) privileged-only
  - crypto: af_alg - Stop after finding name in allowlist
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260802230055.100746-2-ebiggers@kernel.org/

**crypto: af_alg - Allow additional ciphers for cryptsetup**

- 日期：2026-07-05
- 状态：已合入
- 概括：在 AF_ALG skcipher allowlist 中加入 cryptsetup 使用的 xts(camellia)、xts(serpent)、xts(twofish) 等算法条目，让用户态磁盘加密工具继续通过 AF_ALG socket 调用这些 cipher。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260705184419.40762-1-ebiggers@kernel.org/

**▸ 组织：Individual Contributor**（1 patches）

**crypto: af_alg: Allow cbc(paes)**

- 日期：2026-07-26
- 状态：已合入
- 概括：在 crypto: af_alg 中允许 cbc(paes)。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260726192716.2351505-1-richard@nod.at/

---

### ◆ 子系统：Aead（3 patches）

**▸ 组织：Individual Contributor**（3 patches）

**crypto: ccree - use crypto_memneq() to compare AEAD tag**

- 日期：2026-08-15
- 状态：已合入
- 概括：在 crypto 中改用 crypto_memneq() to compare AEAD tag。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/aoCdZiqJjb5XDHHz@david.gall/

**crypto: sa2ul - use crypto_memneq() to compare AEAD tag**

- 日期：2026-08-07
- 状态：已合入
- 概括：在 crypto 中改用 crypto_memneq() to compare AEAD tag。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/anX9UKJ66Aak4ICV@fudgebox/

**[SERIES] crypto: keembay - use crypto_memneq() to compare GCM AEAD tags** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-07
- 状态：已合入
- 概括：改用 crypto_memneq() to compare GCM AEAD tags，并改用 crypto_memneq() to compare CCM AEAD tags。
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
- 概括：在 hwrng core 中注册 PM notifier，系统 suspend/hibernate 前停止 hwrng_fillfn kthread 并记录停止状态，resume/restore 后再重新启动，避免休眠阶段后台线程继续触碰 RNG 设备。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260804-hw-random-fix-hwrng-fillfn-crash-suspend-resume-v5-1-c4769b3c007b@bootlin.com/

**[v2,2/2] hwrng: omap: Enable on Renesas RZ/N1D**

- 日期：2026-07-10
- 状态：已合入
- 概括：在 hwrng: omap 中启用 on Renesas RZ/N1D。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260710-schneider-v7-2-rc1-eip76-upstream-v2-2-4eab557b0e70@bootlin.com/

---

### ◆ 子系统：ICE (Qualcomm)（1 patches）

**▸ 组织：Linux Community**（1 patches）

**crypto: qat - use strscpy_pad to simplify adf_service_string_to_mask**

- 日期：2026-07-05
- 状态：已合入
- 概括：在 crypto 中改用 strscpy_pad to simplify adf_service_string_to_mask。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260705133842.241401-3-thorsten.blum@linux.dev/

---

### ◆ 子系统：CESA (Marvell)（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: cesa: manage SRAM teardown with devm**

- 日期：2026-07-17
- 状态：已合入
- 概括：在 crypto: cesa 中manage SRAM teardown（携带 devm）。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260717231742.1174221-1-rosenp@gmail.com/

---

### ◆ 子系统：Ahash（1 patches）

**▸ 组织：Linux Community**（1 patches）

**crypto: bcm - use memcpy_and_pad in ahash_hmac_setkey**

- 日期：2026-07-20
- 状态：已合入
- 概括：在 crypto 中改用 memcpy_and_pad in ahash_hmac_setkey。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260720232249.117992-3-thorsten.blum@linux.dev/

---

### ◆ 子系统：CAAM (NXP)（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: caam: simplify probe resource and IRQ handling**

- 日期：2026-07-30
- 状态：已合入
- 概括：在 crypto: caam 中simplify probe resource and IRQ handling。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260730204722.1101805-1-rosenp@gmail.com/

---

### ◆ 子系统：Kerberos（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto/krb5: use kfree_sensitive() for derived key buffers**

- 日期：2026-08-03
- 状态：已合入
- 概括：在 crypto/krb5 中为 derived key buffers 改用 kfree_sensitive()。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260803192621.329577-1-linux@jaseg.de/

---

### ◆ 子系统：Authenc（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: octeontx2 - use crypto_memneq() to check HMAC for cipher_null authenc**

- 日期：2026-08-15
- 状态：已合入
- 概括：在 crypto 中为 cipher_null authenc 改用 crypto_memneq() to check HMAC。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/aoCdBZ-kLQ0rciFi@david.gall/

---

### ◆ 子系统：ECC（1 patches）

**▸ 组织：Linux Community**（1 patches）

**[SERIES] crypto: atmel-ecc - simplify control flow in atmel_ecdh_set_secret** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-07-28
- 状态：已合入
- 概括：simplify control flow in atmel_ecdh_set_secret，并删除 redundant return variable。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: atmel-ecc - simplify control flow in atmel_ecdh_set_secret
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260728205825.471233-3-thorsten.blum@linux.dev/

---

### ◆ 子系统：QCE (Qualcomm)（1 patches）

**▸ 组织：Linux Community**（1 patches）

**[SERIES] crypto: qce - simplify devm_qce_register_algs** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-07-31
- 状态：已合入
- 概括：simplify qce_handle_request，并simplify devm_qce_register_algs。
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
- 概括：修复 asymmetric_keys 中 pefile_parse_binary() 对 PE 安全目录和 section 范围校验不足导致的越界读，并补充 PE parser KUnit 用例覆盖异常输入。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: asymmetric_keys - add KUnit tests for the PE parser
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/fcbc6b4d5855ba42a0fccf335b2604ef0b36f092.1786802052.git.fabrice.derepas@canonical.com/

---

## 社区讨论中 Patches

### ◆ 子系统：General Crypto（39 patches）

**▸ 组织：Individual Contributor**（18 patches）

**[v2] crypto: ccp: Initialize DBC ioctl mutex before registering device**

- 日期：2026-08-30
- 状态：社区讨论中
- 概括：在 crypto: ccp 中Initialize DBC ioctl mutex（在 registering device 前）。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260830015104.2040153-1-runyu.xiao@seu.edu.cn/

**crypto: arm64/aes-neonbs: transition to kmalloc_obj()**

- 日期：2026-08-30
- 状态：社区讨论中
- 概括：在 crypto: arm64/aes-neonbs 中transition to kmalloc_obj()。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260830101714.625728-3-manuelebnerli@mailbox.org/

**crypto: atmel-tdes - zero-initialize device state**

- 日期：2026-08-29
- 状态：社区讨论中
- 概括：在 crypto 中zero-initialize device state。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260829035821.67220-1-kmehltretter@gmail.com/

**[SERIES] Add support for hashing algorithms in TI DTHE V2** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-27
- 状态：社区讨论中
- 概括：crypto 中增加 SHA224/256/384/512 in DTHEv2 driver 支持，并crypto 中增加 HMAC in DTHEv2 driver 支持。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: ti - Add support for SHA224/256/384/512 in DTHEv2 driver
  - crypto: ti - Add support for HMAC in DTHEv2 driver
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260827133542.619717-2-t-pratham@ti.com/

**[SERIES] Fix several issues in DTHEv2 driver** （cover letter，2/7 个 patch 达到代码量阈值）

- 日期：2026-08-27
- 状态：社区讨论中
- 概括：crypto 中Trim scatterlists to correct length in AES、crypto 中修复 use-after-free of dev_data on DTHEv2 driver removal、crypto 中改用 list_first_entry_or_null() in dthe_get_dev()。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: ti - Trim scatterlists to correct length in AES
  - crypto: ti - Use list_first_entry_or_null() in dthe_get_dev()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260827132318.613876-5-t-pratham@ti.com/

**[SERIES] crypto: cmh - add Rambus CryptoManager Hub driver** （cover letter，15/15 个 patch 达到代码量阈值）

- 日期：2026-08-25
- 状态：社区讨论中
- 概括：新增 Rambus CryptoManager Hub 平台驱动，向 crypto API 注册 HMAC-SHA2/SHA3、CSHAKE/KMAC、SHA-2/3/SM3、AES/SM4、ChaCha20-Poly1305、RSA、ECDH/X25519、ML-KEM/ML-DSA 以及 DRBG hwrng 能力。
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
- 概括：x509 中新增 CRL parser（携带 indirect CRL support），并x509 中新增 CRL signature verification support。
- 达到阈值的 patches（1 个，显示前 5）：
  - x509: add CRL parser with indirect CRL support
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260822082642.48936-3-tnovikov@astralinux.ru/

**[RFC] crypto: qat - zero the VF migration state buffer on save**

- 日期：2026-08-17
- 状态：社区讨论中
- 概括：在 crypto 中zero the VF migration state buffer on save。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260817042613.19855-1-kmehltretter@gmail.com/

**[v3,2/4] crypto: rockchip: Add RK356x/RK3588 cryptographic offloader driver**

- 日期：2026-08-16
- 状态：社区讨论中
- 概括：为 Rockchip RK356x/RK3588 新增加密 offloader 驱动，加入 CRYPTO_DEV_ROCKCHIP2 Kconfig/Makefile 条目和 rk2_crypto.c 平台驱动，接入这些 SoC 的硬件加密加速器。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260816194112.552100-3-dawidro@gmail.com/

**crypto: amcc: trng: use devm_of_iomap()**

- 日期：2026-08-12
- 状态：社区讨论中
- 概括：在 crypto: amcc: trng 中改用 devm_of_iomap()。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260812185747.79173-1-rosenp@gmail.com/

**[v2,12/13] crypto: api - wipe tfm contexts before kdump**

- 日期：2026-08-11
- 状态：社区讨论中
- 概括：在 crypto 中wipe tfm contexts（在 kdump 前）。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260811-crash-zeroize-rework-v2-12-9561d13c2340@jaseg.de/

**[SERIES] crypto: img-hash: clean up probe** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-08-11
- 状态：社区讨论中
- 概括：fetch resources into locals（在 probe body 前），并修复 IRQ teardown ordering and fetch clocks early。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: img-hash: fetch resources into locals before probe body
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260811212030.20057-2-rosenp@gmail.com/

**crypto: amcc: get irq and ioremap resource first**

- 日期：2026-07-30
- 状态：社区讨论中
- 概括：在 crypto: amcc 中get irq and ioremap resource first。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260730204915.1102403-1-rosenp@gmail.com/

**[SERIES] crypto: introduce generic dynamic software fallback and EIP93 support** （cover letter，4/4 个 patch 达到代码量阈值）

- 日期：2026-07-28
- 状态：社区讨论中
- 概括：move cycle benchmark helpers out of tcrypt、引入 dynamic software fallback、新增 dynamic software fallback support，并eliminate fallback proxy overhead while disabled。
- 达到阈值的 patches（4 个，显示前 5）：
  - crypto: move cycle benchmark helpers out of tcrypt
  - crypto: introduce dynamic software fallback
  - crypto: eip93 - add dynamic software fallback support
  - crypto: eliminate fallback proxy overhead while disabled
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/e0ce93088c1d9772e928fcbd113a446b7fb7442f.1785226804.git.hurryman2212@gmail.com/

**lib/crypto: x86/chacha: Add a 16-block AVX-512 variant**

- 日期：2026-07-22
- 状态：社区讨论中
- 概括：在 lib/crypto/x86 中新增 chacha-avx512-x86_64.S 和 chacha_16block_xor_avx512()，利用 AVX-512 zmm 寄存器一次并行处理 16 个 ChaCha block 的加解密异或。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260722153247.630519-1-martin@strongswan.org/

**[SERIES] lib/crypto: add HKDF and convert fscrypt and NVMe** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-07-21
- 状态：社区讨论中
- 概括：在 lib/crypto 中新增 HKDF-SHA256/384/512 extract/expand 库接口和 KUnit 覆盖，并把 fscrypt 与 NVMe 的密钥派生逻辑迁移到统一 HKDF helper。
- 达到阈值的 patches（2 个，显示前 5）：
  - lib/crypto: tests: add HKDF KUnit tests
  - lib/crypto: add HKDF-SHA{256,384,512}
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260721140644.780006-3-marco@mandelbit.com/

**crypto: verify_pefile - Use constant-time digest comparison**

- 日期：2026-07-20
- 状态：社区讨论中
- 概括：在 crypto 中改用 constant-time digest comparison。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260720031815.204237-1-yijiangshan@kylinos.cn/

**[SERIES] crypto: eip93: fix request lifetime and completion handling** （cover letter，4/5 个 patch 达到代码量阈值）

- 日期：2026-07-07
- 状态：社区讨论中
- 概括：guard DMA cleanup on uninitialized mappings、拒绝 HMAC requests（在 setkey 前）、为 cipher requests 改用 request-local SA records、order result descriptor reads（在 PE_READY 后），并handle request ID exhaustion。
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
- 概括：为 lib/crypto 的 AES-CCM 与 AES-GCM 库接口新增 KUnit 测试，抽出 aead-test-template.h/test-utils.h 复用测试模板，并让 hash 测试改为每个用例独立分配缓冲区。
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
- 概括：为 lib/crypto/aes.c 增加 AES 模式 FIPS 启动自检，覆盖 ECB、GCM、CCM 等加解密向量校验，并将 fips.h 拆分为 fips-aes.h 与 fips-sha.h；自检失败时触发 panic。
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
- 概括：Free the padata_works（当 they're no longer needed 时），并Mark remaining code as __init and data as __initdata。
- 达到阈值的 patches（2 个，显示前 5）：
  - padata: Free the padata_works when they're no longer needed
  - padata: Mark remaining code as __init and data as __initdata
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260717171831.27994-3-ebiggers@kernel.org/

**[SERIES] Library APIs for AES encryption modes** （cover letter，12/13 个 patch 达到代码量阈值）

- 日期：2026-07-15
- 状态：社区讨论中
- 概括：crypto 中拆分 out __xts_verify_key() helper、lib/crypto: aes 中新增 ECB support、lib/crypto: aes 中新增 CBC and CBC-CTS support、lib/crypto: aes 中新增 CTR and XCTR support，并lib/crypto: aes 中新增 XTS support。
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
- 概括：从 padata 中删除 serialized job 支持，移除对应文档、serial cpumask 回调和 padata_do_parallel() 的串行作业路径，只保留并行 multithreaded job 机制。
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
- 概括：在 crypto 中Zeroize temporary arrays on stack（携带 sensitive data）。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260819151845.835768-1-thuth@redhat.com/

**lib/crypto: chacha20poly1305: Clear chacha_state in xchacha20poly1305_decrypt()**

- 日期：2026-08-13
- 状态：社区讨论中
- 概括：在 lib/crypto: chacha20poly1305 中清除 chacha_state in xchacha20poly1305_decrypt()。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260813130147.949545-1-thuth@redhat.com/

**[SERIES] libcrypto: Provide more __cleanup functions for zeroizing data** （cover letter，7/7 个 patch 达到代码量阈值）

- 日期：2026-08-13
- 状态：社区讨论中
- 概括：新增 aes_zeroize_ctx() 等 AES 上下文清零封装，并让 aspeed、padlock、sa2ul、arm/arm64 aes-neonbs、qat、safexcel 等实现在操作结束后统一清除 crypto_aes_ctx 中的密钥材料。
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
- 概括：提供 a wrapper for zeroizing hmac_sha1_ctx，并lib/crypto: sha1 中改用 hmac_sha1_zeroize_ctx() instead of memzero_explicit()。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: Provide a wrapper for zeroizing hmac_sha1_ctx
  - lib/crypto: sha1: Use hmac_sha1_zeroize_ctx() instead of memzero_explicit()
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260812163336.3103835-2-thuth@redhat.com/

**[SERIES] crypto: Add __cleanup functions for zeroizing aes_cmac_key & aes_cmac_ctx** （cover letter，1/2 个 patch 达到代码量阈值）

- 日期：2026-08-07
- 状态：社区讨论中
- 概括：提供 wrapper functions for zeroizing aes_cmac_key and aes_cmac_ctx，并lib/crypto: aes 中为 aes_cmac_key instead of memzero_explicit() 改用 __cleanup()。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: Provide wrapper functions for zeroizing aes_cmac_key and aes_cmac_ctx
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260807125845.1477067-2-thuth@redhat.com/

**[RFC] crypto: pcrypt - Disallow nesting of the pcrypt wrapper**

- 日期：2026-07-01
- 状态：社区讨论中
- 概括：在 crypto 中Disallow nesting of the pcrypt wrapper。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260701143947.944593-1-thuth@redhat.com/

**▸ 组织：Huawei**（2 patches）

**crypto: hisilicon/zip - enable auto clock gating for DAE**

- 日期：2026-08-29
- 状态：社区讨论中
- 概括：在 crypto 中启用 auto clock gating for DAE。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260829094924.2191402-1-huangchenghai2@huawei.com/

**[v2] crypto: hisilicon/sec - remove SEC crypto block cipher accelerator**

- 日期：2026-08-19
- 状态：社区讨论中
- 概括：在 crypto 中移除 SEC crypto block cipher accelerator。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260819075353.94500-1-huangchenghai2@huawei.com/

**▸ 组织：Qualcomm**（2 patches）

**[SERIES] crypto/dmaengine: qce: introduce BAM locking and use DMA for register I/O** （cover letter，7/8 个 patch 达到代码量阈值）

- 日期：2026-07-23
- 状态：社区讨论中
- 概括：取消 work on device detach、Include algapi.h in the core.h header、移除 unused ignore_buf、Simplify arguments of devm_qce_dma_request()，并改用 existing devres APIs in devm_qce_dma_request()。
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
- 概括：修复 HMAC self-test failures for empty messages、拒绝 empty messages for AES-XTS、修复 CTR-AES for partial block requests、为 AES-CTR（携带 a partial final block 改用 a fallback），并为 CCM（携带 a partial final block 改用 a fallback）。
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
- 概括：在 crypto: xilinx: zynqmp-aes-gcm 中Send firmware decoded code instead of EBADMSG。
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
- 概括：在 crypto 中允许 KPT disable（当 service is not asym 时）。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260831063355.668528-2-nitesh.venkatesh@intel.com/

**▸ 组织：Linux Community**（1 patches）

**[SERIES] crypto: zstd - avoid initializing the workspace twice** （cover letter，2/2 个 patch 达到代码量阈值）

- 日期：2026-08-25
- 状态：社区讨论中
- 概括：避免 redundant cstream initialization，并避免 redundant dstream initialization。
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
- 概括：拒绝 undersized keys（当 signing 时），并拒绝 undersized keys（当 verifying 时）。
- 达到阈值的 patches（2 个，显示前 5）：
  - crypto: rsassa-pkcs1: reject undersized keys when signing
  - crypto: rsassa-pkcs1: reject undersized keys when verifying
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260826103744.1554131-2-Jeremy.Jean@oss.cyber.gouv.fr/

**crypto: rsassa-pkcs1 - Use constant-time digest comparison**

- 日期：2026-07-20
- 状态：社区讨论中
- 概括：在 crypto 中改用 constant-time digest comparison。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260720021322.122784-1-yijiangshan@kylinos.cn/

**crypto: pkcs7 - Use constant-time message digest comparison**

- 日期：2026-07-20
- 状态：社区讨论中
- 概括：在 crypto 中改用 constant-time message digest comparison。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260720032316.210113-1-yijiangshan@kylinos.cn/

**[6.1/6.6/6.12.y] crypto: rsa-pkcs1pad: Don't WARN on an empty digest**

- 日期：2026-07-20
- 状态：社区讨论中
- 概括：在 crypto: rsa-pkcs1pad 中避免 WARN on an empty digest。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260720191525.15450-1-doruk@0sec.ai/

**crypto: rsassa-pkcs1: use constant-time comparison for digest and signature verification**

- 日期：2026-07-10
- 状态：社区讨论中
- 概括：在 crypto: rsassa-pkcs1 中为 digest and signature verification 改用 constant-time comparison。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/alEr_e-G0L2nxxv-@fudgebox/

**crypto: pkcs7_verify: use constant-time comparison for digest and signature verification**

- 日期：2026-07-10
- 状态：社区讨论中
- 概括：在 crypto: pkcs7_verify 中为 digest and signature verification 改用 constant-time comparison。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/alEsSl8i1_FpoU0f@fudgebox/

---

### ◆ 子系统：CAAM (NXP)（2 patches）

**▸ 组织：Individual Contributor**（2 patches）

**crypto: caam - reject overlong RSA CRT parameters**

- 日期：2026-08-10
- 状态：社区讨论中
- 概括：在 crypto 中拒绝 overlong RSA CRT parameters。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260810154024.3178145-1-Jeremy.Jean@oss.cyber.gouv.fr/

**[SERIES] crypto: caam: Fix DMA mapping leak in the cbc(paes) job path** （cover letter，1/3 个 patch 达到代码量阈值）

- 日期：2026-07-26
- 状态：社区讨论中
- 概括：Map the paes protected key once per tfm、Validate the protected key header in setkey，并修复 DMA mapping leak in the cbc(paes) job path。
- 达到阈值的 patches（1 个，显示前 5）：
  - crypto: caam: Map the paes protected key once per tfm
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260726081504.2182951-2-richard@nod.at/

---

### ◆ 子系统：Talitos（2 patches）

**▸ 组织：Individual Contributor**（2 patches）

**crypto: talitos: pass talitos_private to irq handlers**

- 日期：2026-08-11
- 状态：社区讨论中
- 概括：在 crypto: talitos 中传递 talitos_private to irq handlers。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260811043953.150589-1-rosenp@gmail.com/

**[SERIES] crypto: talitos - fix rename first/last to first_desc/last_desc** （cover letter，3/3 个 patch 达到代码量阈值）

- 日期：2026-07-09
- 状态：社区讨论中
- 概括：清理 talitos ahash 请求上下文字段命名，将 first/last 改为 first_desc/last_desc，并同步调整 ahash digest/init/finup 路径及 sha224 软件初始化处理。
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
- 概括：在 hw_random/via-rng 中Stop using 32-bit MSR interfaces。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260819102314.1499258-8-jgross@suse.com/

**▸ 组织：Individual Contributor**（1 patches）

**hwrng: imx-rngc: check clk_prepare_enable() return value**

- 日期：2026-08-28
- 状态：社区讨论中
- 概括：在 hwrng: imx-rngc 中检查 clk_prepare_enable() return value。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260828025423.2149304-1-dayou5941@163.com/

---

### ◆ 子系统：AF_ALG API（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[5.10/5.15] crypto: af_alg - Set merge to zero early in af_alg_sendmsg**

- 日期：2026-07-01
- 状态：社区讨论中
- 概括：在 crypto 中设置 merge to zero early in af_alg_sendmsg。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260701160121.100720-1-mdmitrichenko@astralinux.ru/

---

### ◆ 子系统：ECC（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**[RFC,RESEND,v6,1/1] crypto: atmel-ecc - fix multi-device use-after-free and registration races**

- 日期：2026-07-12
- 状态：社区讨论中
- 概括：在 crypto 中修复 multi-device use-after-free and registration races。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260712200203.47764-1-l.rubusch@gmail.com/

---

### ◆ 子系统：CESA (Marvell)（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: cesa: check for sram_dma NULL**

- 日期：2026-07-13
- 状态：社区讨论中
- 概括：在 crypto: cesa 中检查 for sram_dma NULL。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260713050740.3687230-1-rosenp@gmail.com/

---

### ◆ 子系统：Kerberos（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: krb5 - Use constant-time checksum comparison**

- 日期：2026-07-20
- 状态：社区讨论中
- 概括：在 crypto 中改用 constant-time checksum comparison。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260720031304.198172-1-yijiangshan@kylinos.cn/

---

### ◆ 子系统：Asymmetric Keys（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: asymmetric_keys: copy X.509 TBS for data signature algorithms**

- 日期：2026-08-21
- 状态：社区讨论中
- 概括：在 crypto: asymmetric_keys 中copy X.509 TBS for data signature algorithms。
- 来源：https://patchwork.kernel.org/project/linux-crypto/patch/20260821192502.3942767-2-Jeremy.Jean@oss.cyber.gouv.fr/

---

### ◆ 子系统：Skcipher（1 patches）

**▸ 组织：Individual Contributor**（1 patches）

**crypto: mxs-dcp: handle zero-length skcipher requests**

- 日期：2026-08-28
- 状态：社区讨论中
- 概括：在 crypto: mxs-dcp 中handle zero-length skcipher requests。
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

*报告由 Linux Patches Tracker 自动生成 | 2026-09-08 21:26:40*
