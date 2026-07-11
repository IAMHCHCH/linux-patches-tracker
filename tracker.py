#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Linux Kernel Patches Tracker — Unified
One script to track patches for crypto, vfio, iommu, and more.

Usage:
  python3 tracker.py crypto              # Generate crypto report
  python3 tracker.py vfio                # Generate vfio report
  python3 tracker.py iommu               # Generate iommu report
  python3 tracker.py --all               # Generate all reports
  python3 tracker.py --list              # List available modules
  python3 tracker.py crypto --start 2026-02-01 --end 2026-05-06
"""

import json
import os
import re
import sys
import hashlib
import requests
import argparse
from datetime import datetime, date
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

# ============================================================
# Module Configurations
# ============================================================

# ---- Shared organization mapping ----
ORG_MAP = {
    'intel.com': 'Intel', 'linux.intel.com': 'Intel',
    'amd.com': 'AMD', 'amd.com.cn': 'AMD',
    'qualcomm.com': 'Qualcomm',
    'huawei.com': 'Huawei', 'hisilicon.com': 'HiSilicon',
    'google.com': 'Google',
    'kernel.org': 'Kernel.org',
    'linaro.org': 'Linaro',
    'redhat.com': 'Red Hat',
    'linux.dev': 'Linux Community',
    'baylibre.com': 'Baylibre',
    'amazon.com': 'Amazon', 'microsoft.com': 'Microsoft',
    'nvidia.com': 'NVIDIA',
    'fb.com': 'Meta', 'meta.com': 'Meta',
    'ibm.com': 'IBM', 'linux.ibm.com': 'IBM', 'de.ibm.com': 'IBM',
    'marvell.com': 'Marvell', 'nxp.com': 'NXP',
    'mediatek.com': 'MediaTek', 'samsung.com': 'Samsung',
    'arm.com': 'ARM', 'canonical.com': 'Canonical',
    'suse.com': 'SUSE', 'suse.de': 'SUSE',
    'oracle.com': 'Oracle',
    'xilinx.com': 'Xilinx (AMD)', 'amd.xilinx.com': 'Xilinx (AMD)',
    'pensando.io': 'Pensando (AMD)',
    'spacemit.com': 'SpacemiT', 'sifive.com': 'SiFive',
    'starfivetech.com': 'StarFive', 'ventanamicro.com': 'Ventana Micro',
    'rivosinc.com': 'Rivos',
    'bootlin.com': 'Bootlin', 'vayavyalabs.com': 'Vayavya Labs',
    'cornelisnetworks.com': 'Cornelis Networks',
    'debian.org': 'Debian', 'siemens.com': 'Siemens',
    'opensource.cirrus.com': 'Cirrus Logic',
    'gmail.com': 'Individual Contributor',
    '139.com': 'Individual Contributor',
    'qq.com': 'Individual Contributor',
    'protonmail.com': 'Individual Contributor',
    'proton.me': 'Individual Contributor',
    'outlook.com': 'Individual Contributor',
}

# ============================================================
# LLM (Large Language Model) Configuration
# ============================================================
# Set the environment variable LLM_API_KEY to enable LLM-based patch analysis.
# Supported providers:
#   - Anthropic:    LLM_API_KEY=sk-ant-...  (default)
#   - OpenAI:       LLM_API_KEY=sk-...   +  LLM_API_BASE=https://api.openai.com
#   - Ollama(local): LLM_API_KEY=sk-dummy  +  LLM_API_BASE=http://localhost:11434
LLM_API_KEY = os.environ.get('LLM_API_KEY', '')
LLM_MODEL = os.environ.get('LLM_MODEL', 'claude-sonnet-4-20250514')
LLM_API_BASE = os.environ.get('LLM_API_BASE', 'https://api.anthropic.com')

# In-memory & on-disk cache for LLM summaries (keyed by patch ID)
_SUMMARY_CACHE = {}
_SUMMARY_CACHE_PATH = None


def _load_llm_cache(output_dir):
    global _SUMMARY_CACHE, _SUMMARY_CACHE_PATH
    _SUMMARY_CACHE_PATH = os.path.join(output_dir, 'summary_cache.json')
    if os.path.exists(_SUMMARY_CACHE_PATH):
        with open(_SUMMARY_CACHE_PATH, 'r') as f:
            _SUMMARY_CACHE = json.load(f)
    else:
        _SUMMARY_CACHE = {}


def _save_llm_cache():
    if _SUMMARY_CACHE_PATH:
        with open(_SUMMARY_CACHE_PATH, 'w', encoding='utf-8') as f:
            json.dump(_SUMMARY_CACHE, f, ensure_ascii=False, indent=2)


def _call_llm_summary(title, diff_text, patch_id=None):
    """Generate a concise Chinese summary via LLM. Returns None on failure."""
    cache_key = str(patch_id) if patch_id else hashlib.md5(title.encode()).hexdigest()
    cached = _SUMMARY_CACHE.get(cache_key)
    if cached:
        return cached

    if not LLM_API_KEY or not diff_text:
        return None

    # Truncate diff to keep API calls fast
    truncated = diff_text[:6000] if len(diff_text) > 6000 else diff_text

    system_prompt = (
        '你是一个 Linux 内核 patch 分析专家。'
        '分析以下 patch 的标题和 diff 内容，用一句话概括其核心改动（不超过200字符）。'
        '要求：直接说明做了什么改动，保持技术准确性，不使用修饰性词语。'
    )

    try:
        resp = requests.post(
            f'{LLM_API_BASE}/v1/messages',
            headers={
                'x-api-key': LLM_API_KEY,
                'anthropic-version': '2023-06-01',
                'content-type': 'application/json',
            },
            json={
                'model': LLM_MODEL,
                'max_tokens': 500,
                'temperature': 0.1,
                'system': system_prompt,
                'messages': [{
                    'role': 'user',
                    'content': f'## 标题\n{title}\n\n## Diff\n```diff\n{truncated}\n```'
                }]
            },
            timeout=30
        )
        resp.raise_for_status()
        data = resp.json()
        # Iterate content blocks to find the first 'text' type
        summary = None
        for block in data.get('content', []):
            if block.get('type') == 'text':
                summary = block.get('text', '')
                break
            if block.get('type') == 'thinking':
                summary = block.get('thinking', '')
        if not summary:
            print(f'    [LLM] 响应中无 text/thinking 内容 (id={patch_id})')
            return None
        summary = summary.strip()[:200]
        _SUMMARY_CACHE[cache_key] = summary
        _save_llm_cache()
        return summary
    except Exception as e:
        print(f'    [LLM] 概括失败 (id={patch_id}): {e}')
        return None


def _batch_llm_task(args):
    """Wrapper for ThreadPoolExecutor — returns (patch_id, summary_or_None)."""
    title, diff_text, patch_id = args
    return patch_id, _call_llm_summary(title, diff_text, patch_id)


MODULES = {}

# ---- Crypto Module ----
MODULES['crypto'] = {
    'name': 'Linux Crypto 子系统',
    'output_dir': 'output/crypto',
    'default_start': '2026-01-01',
    'default_end': '2026-05-06',
    'patchwork': {
        'project_id': 151,
        'search_query': None,
        'url_template': (
            'https://patchwork.kernel.org/api/patches/'
            '?project={project_id}&since={since}&per_page=100'
        ),
    },
    'subject_whitelist': [
        'crypto', 'crypto/ccp', 'crypto/caam', 'crypto/qat', 'crypto/omap',
        'crypto/ccree', 'crypto/artpec', 'crypto/starfive', 'crypto/talitos',
        'crypto/atmel', 'crypto/inside-secure', 'crypto/marvell',
        'crypto/ti', 'crypto/spacc', 'crypto/scompress',
        'hwrng', 'hw_random', 'hw-rng', 'padata',
        'dt-bindings: crypto', 'x509', 'lib/crypto',
        'crypto/engine', 'crypto/jitterentropy', 'crypto/drbg',
        'crypto/ecc', 'crypto/ecdsa', 'crypto/ecrdsa',
        'crypto/aead', 'crypto/ahash', 'crypto/shash', 'crypto/skcipher',
        'crypto/akcipher', 'crypto/kpp',
        'crypto/testmgr', 'crypto/tcrypt',
        'crypto/authenc', 'crypto/krb5', 'crypto/asymmetric_keys',
        'crypto/rsa', 'crypto/rsa-pkcs1pad',
        'crypto/xts', 'crypto/gcm', 'crypto/ccm',
        'crypto/sha256', 'crypto/sha512', 'crypto/md5',
        'crypto/aes', 'crypto/des', 'crypto/sm2', 'crypto/sm3', 'crypto/sm4',
        'crypto/chacha', 'crypto/poly1305', 'crypto/curve25519',
        'crypto/ecdh', 'crypto/ecdsa',
        'crypto/virtio', 'crypto/ice', 'crypto/qce', 'crypto/qcom',
    ],
    'subject_blacklist': [
        'wifi', 'mac80211', 'mac802154', 'dmaengine',
        'sock', 'socket', 'net/', 'net:',
        'mm/', 'mm:', 'soc:', 'soc/',
        'sched', 'sched_ext', 'NFSD', 'nfsd', 'NFS:', 'nfs:',
        'workqueue', 'platform/x86', 'selftests/cgroup',
        'Documentation/tcp', 'Documentation/net',
        'block:', 'block/', 'fs/', 'fs:', 'fscrypt',
        'bpf:', 'bpf/', 'tty:', 'tty/', 'usb:', 'usb/',
        'drm/', 'drm:', 'sound/', 'sound:', 'media/', 'media:',
        'pci/', 'pci:', 'acpi/', 'acpi:', 'cpufreq', 'cpuidle',
        'kbuild', 'kconfig', 'scripts/', 'tools/', 'perf:', 'selftests/',
    ],
    'subsystem_patterns': [
        ('AF_ALG API', ['af_alg', 'algif_']),
        ('DRBG', ['drbg']),
        ('HWRNG', ['hwrng', 'hw_random']),
        ('ECC', ['ecdsa', 'ecrdsa', 'ecc']),
        ('QAT (Intel)', ['qat_']),
        ('CCP/SEV (AMD)', ['ccp_', 'sev_', 'snp_']),
        ('Talitos', ['talitos']),
        ('QCE (Qualcomm)', ['qce_']),
        ('ICE (Qualcomm)', ['ice_']),
        ('SPAcc', ['spacc']),
        ('CESA (Marvell)', ['cesa', 'safexcel']),
        ('VirtIO Crypto', ['virtio_crypto']),
        ('Crypto Engine', ['crypto/engine', 'engine.c']),
        ('Kerberos', ['krb5']),
        ('Asymmetric Keys', ['asymmetric', 'keyctl']),
        ('Public Key', ['public_key', 'pkcs']),
        ('Authenc', ['authenc', 'authencesn']),
        ('Shash', ['shash']),
        ('Ahash', ['ahash']),
        ('Skcipher', ['skcipher']),
        ('Aead', ['aead']),
        ('Test Manager', ['testmgr']),
        ('TCrypt', ['tcrypt']),
        ('JitterEntropy', ['jitterentropy']),
        ('CAAM (NXP)', ['caam']),
        ('ARM Crypto', ['arm_crypto']),
        ('POWER Crypto', ['powerpc/crypto', 'ppc_crypto']),
        ('General Crypto', ['crypto']),
    ],
    'report_intro': (
        '本项目用于追踪 Linux 内核 crypto（加密）子系统的 patch 提交情况。'
        'crypto 子系统涵盖硬件加密加速器驱动（QAT、CCP、CAAM、QCE 等）、'
        '加密算法实现（AES、SHA、ECC、SMx 等）、以及用户空间加密 API（AF_ALG）。'
    ),
    'subsystem_descriptions': [
        ('AF_ALG API', '用户空间加密 API（algif_skcipher、algif_hash 等）'),
        ('DRBG', '确定性随机比特生成器'),
        ('HWRNG', '硬件随机数生成器驱动'),
        ('ECC', '椭圆曲线密码学（ECDSA、ECRDSA）'),
        ('QAT (Intel)', 'Intel QuickAssist Technology 硬件加速器'),
        ('CCP/SEV (AMD)', 'AMD 安全协处理器 / 安全加密虚拟化'),
        ('CAAM (NXP)', 'NXP Cryptographic Acceleration and Assurance Module'),
        ('Talitos', 'NXP/Freescale Talitos 安全加速器'),
        ('QCE (Qualcomm)', 'Qualcomm Crypto Engine'),
        ('ICE (Qualcomm)', 'Qualcomm Inline Crypto Engine'),
        ('SPAcc', '安全算法硬件加速器'),
        ('CESA (Marvell)', 'Marvell Cryptographic Engine and Security Accelerator'),
        ('VirtIO Crypto', 'VirtIO 虚拟化加密设备'),
        ('Crypto Engine', '加密算法引擎框架'),
        ('Kerberos', 'Kerberos 5 加密支持'),
        ('Asymmetric Keys', '非对称密钥管理'),
        ('Public Key', '公钥加密（X.509、PKCS7）'),
        ('Authenc', '认证加密'),
        ('Shash', '同步哈希算法'),
        ('Ahash', '异步哈希算法'),
        ('Skcipher', '对称密钥加密'),
        ('Aead', '关联数据认证加密'),
        ('Test Manager', '加密算法测试管理器'),
        ('TCrypt', '加密速度测试模块'),
        ('JitterEntropy', 'Jitter 熵源 RNG'),
        ('General Crypto', '通用 crypto（不属于特定子模块）'),
    ],
}

# ---- VFIO Module ----
MODULES['vfio'] = {
    'name': 'Linux VFIO 子系统',
    'output_dir': 'output/vfio',
    'default_start': '2026-02-01',
    'default_end': '2026-05-06',
    'patchwork': {
        'project_id': 8,
        'search_query': 'vfio',
        'url_template': (
            'https://patchwork.kernel.org/api/patches/'
            '?project={project_id}&q={search_query}&since={since}&per_page=100'
        ),
    },
    'subject_whitelist': [
        'vfio', 'vfio/pci', 'vfio/platform', 'vfio/fsl-mc', 'vfio/cdx',
        'vfio/mdev', 'vfio/iommufd', 'iommufd',
    ],
    'subject_blacklist': [],
    'subsystem_patterns': [
        ('VFIO PCI', ['vfio/pci', 'vfio_pci', 'vfio-pci']),
        ('VFIO Platform', ['vfio/platform', 'vfio_platform', 'vfio-platform']),
        ('VFIO FSL-MC', ['vfio/fsl-mc', 'fsl_mc', 'vfio-fsl-mc']),
        ('VFIO CDX', ['vfio/cdx', 'vfio_cdx', 'vfio-cdx']),
        ('VFIO Mediated Device', ['mdev', 'mediated']),
        ('VFIO IOMMUFD', ['iommufd', 'iommu fd']),
        ('VFIO CCW (s390)', ['vfio_ccw', 'vfio-ccw', 'vfio/ccw']),
        ('VFIO AP (s390)', ['vfio_ap', 'vfio-ap', 'vfio/ap']),
        ('VFIO Migration', ['migration', 'live migration', 'dirty tracking']),
        ('VFIO MLX5 Variant', ['mlx5', 'mlx5-vfio', 'mlx5_vfio']),
        ('VFIO HiSilicon ACC', ['hisi_acc', 'hisi-acc', 'hisi acc']),
        ('VFIO PDS Variant', ['pds-vfio', 'pds_vfio', 'pds vfio']),
        ('VFIO CDEV', ['cdev']),
        ('VFIO Selftests', ['selftest', 'selftests/vfio']),
        ('VFIO Core', ['vfio']),
    ],
    'report_intro': (
        '本项目用于追踪 Linux 内核 VFIO (Virtual Function I/O) 子系统的 '
        'patch 提交情况。VFIO 允许用户空间程序直接访问硬件设备，'
        '主要应用于虚拟机设备直通（KVM/QEMU）和用户空间驱动（DPDK、SPDK）。'
    ),
    'subsystem_descriptions': [
        ('VFIO PCI', 'PCI 设备直通（vfio-pci 驱动，最常用的 VFIO 模块）'),
        ('VFIO Platform', '平台设备直通（vfio-platform 驱动）'),
        ('VFIO FSL-MC', 'NXP Freescale Management Complex 总线设备直通'),
        ('VFIO CDX', 'Xilinx CDX 总线设备直通'),
        ('VFIO Mediated Device', '中介设备框架（GPU/NIC 虚拟化切分）'),
        ('VFIO IOMMUFD', 'VFIO 与 IOMMUFD 框架的集成接口'),
        ('VFIO CCW (s390)', 'IBM s390 架构 Channel I/O 设备直通'),
        ('VFIO AP (s390)', 'IBM s390 架构 Adjunct Processor 设备直通'),
        ('VFIO Migration', '虚拟机热迁移中的 VFIO 设备状态迁移'),
        ('VFIO MLX5 Variant', 'NVIDIA MLX5 变体驱动（基于 vfio-pci 扩展）'),
        ('VFIO HiSilicon ACC', '华为海思加速器变体驱动'),
        ('VFIO PDS Variant', 'AMD Pensando 变体驱动'),
        ('VFIO CDEV', 'VFIO 字符设备接口（cdev ioctl 方式）'),
        ('VFIO Selftests', 'VFIO 内核自测试用例'),
        ('VFIO Core', 'VFIO 核心框架（设备发现、group/container 管理）'),
    ],
}

# ---- IOMMU Module ----
MODULES['iommu'] = {
    'name': 'Linux IOMMU 子系统',
    'output_dir': 'output/iommu',
    'default_start': '2026-02-01',
    'default_end': '2026-05-06',
    'patchwork': {
        'project_id': None,
        'search_query': 'iommu',
        'url_template': (
            'https://patchwork.kernel.org/api/patches/'
            '?q={search_query}&since={since}&per_page=100'
        ),
    },
    'subject_whitelist': [
        'iommu', 'iommu/amd', 'iommu/arm-smmu', 'iommu/arm-smmu-v3',
        'iommu/dma', 'iommu/intel', 'iommu/io-pgtable', 'iommu/pages',
        'iommu/riscv', 'iommu/s390', 'iommu/tegra241-cmdqv', 'iommu/vt-d',
        'iommufd', 'iommufd-lu', 'iommufd/selftest', 'iommupt',
        'intel_iommu', 'intel_iommu_accel',
        'amd_iommu',
        'arm-smmu', 'arm-smmu-v3',
        'iommu/fsl', 'iommu/omap', 'iommu/tegra', 'iommu/msm',
        'iommu/mtk', 'iommu/qcom', 'iommu/sprd', 'iommu/sun50i',
        'iommu/rockchip', 'iommu/exynos',
        'acpi/viot', 'dt-bindings: iommu',
        'smmu', 'smmuv3',
    ],
    'subject_blacklist': [
        'accel/tcg', 'backends/iommufd',
        'drm', 'drm/msm', 'drm/', 'gpu',
        'hw/', 'hw/arm', 'hw/core', 'hw/i386', 'hw/riscv',
        'tests/qtest', 'tests/qtest/libqos',
        'vfio', 'vfio/pci', 'vfio/iommufd',
        'drivers/perf', 'spacemit/t100',
        'acpi', 'acpi/', 'pci/', 'pci:',
        'net/', 'net:', 'kvm', 'kvm/',
        'xen/', 'xen:', 'dmaengine', 'dmaengine/',
        'media', 'media/',
        'of', 'of/', 'arm64', 'riscv/imsic',
        'sound/', 'sound:', 'usb/', 'usb:', 'tty/', 'tty:',
        'block/', 'block:', 'fs/', 'fs:', 'nfs', 'nfsd',
        'bpf/', 'bpf:', 'selftests/', 'selftests:',
        'mm/', 'mm:', 'sched', 'sched/',
        'scripts/', 'scripts:', 'perf/', 'perf:',
    ],
    'subsystem_patterns': [
        ('Intel VT-d', ['intel_iommu', 'iommu/vt-d', 'intel-iommu',
                        'vt-d', 'dmar']),
        ('AMD IOMMU', ['amd_iommu', 'iommu/amd', 'amd-iommu', 'amd-vi']),
        ('ARM SMMUv3', ['arm-smmu-v3', 'arm_smmu_v3', 'iommu/arm-smmu-v3',
                        'smmuv3', 'smmu-v3']),
        ('ARM SMMU (v1/v2)', ['arm-smmu', 'arm_smmu', 'iommu/arm-smmu',
                              'qcom_iommu', 'qcom-iommu']),
        ('ARM SMMU Acceleration', ['smmuv3-accel', 'smmu-accel',
                                   'tegra241-cmdqv', 'cmdqv']),
        ('RISC-V IOMMU', ['riscv/iommu', 'iommu/riscv', 'riscv-iommu']),
        ('IOMMUFD', ['iommufd', 'iommu fd', 'iommufd-lu']),
        ('IOMMU DMA-API', ['iommu/dma', 'iommu-dma', 'dma-iommu']),
        ('IOMMU Page Table', ['io-pgtable', 'iommu/io-pgtable', 'iopgtable']),
        ('IOMMU Pages', ['iommu/pages', 'iommu pages']),
        ('IOMMUPT', ['iommupt']),
        ('Intel IOMMU Accel', ['intel_iommu_accel', 'iommu_accel']),
        ('IOMMU SVA/SVM', ['sva', 'svm', 'pasid', 'pri']),
        ('IOMMU Core', ['iommu']),
    ],
    'report_intro': (
        '本项目用于追踪 Linux 内核 IOMMU (Input-Output Memory Management Unit) '
        '子系统的 patch 提交情况。IOMMU 提供设备-内存地址转换、内存保护和'
        '设备隔离功能，是设备直通/虚拟化的基础。由于 patchwork 无独立 IOMMU 项目，'
        '数据通过全局搜索获取并经过 subject prefix 白名单/黑名单精确过滤。'
    ),
    'subsystem_descriptions': [
        ('Intel VT-d', 'Intel 虚拟化技术定向 I/O（DMA remapping、IRQ remapping）'),
        ('AMD IOMMU', 'AMD I/O 虚拟化技术（AMD-Vi）'),
        ('ARM SMMUv3', 'ARM 系统 MMU 第三代（PCIe ATS/PRI 支持）'),
        ('ARM SMMU (v1/v2)', 'ARM 系统 MMU 第一/二代（含 Qualcomm 实现）'),
        ('ARM SMMU Acceleration', 'SMMUv3 硬件加速命令队列（NVIDIA Tegra241 CMDQV）'),
        ('RISC-V IOMMU', 'RISC-V 架构 IOMMU 驱动'),
        ('IOMMUFD', '基于文件描述符的 IOMMU 用户空间接口'),
        ('IOMMU DMA-API', 'IOMMU 与 DMA 映射 API 的集成层'),
        ('IOMMU Page Table', 'IOMMU 页表管理（io-pgtable 库）'),
        ('IOMMU Pages', '物理内存页分配与 IOMMU 映射管理'),
        ('IOMMUPT', 'IOMMU 页表遍历与操作框架'),
        ('Intel IOMMU Accel', 'Intel IOMMU 硬件加速器支持'),
        ('IOMMU SVA/SVM', '共享虚拟地址 / 共享虚拟内存（PASID、PRI）'),
        ('IOMMU Core', '通用 IOMMU 框架（不属于特定驱动）'),
    ],
}

# ============================================================
# Shared Utility Functions
# ============================================================

def extract_organization(email):
    if not email:
        return 'Individual Contributor'
    email_lower = email.lower()
    for domain, org in ORG_MAP.items():
        if domain in email_lower:
            return org
    return 'Individual Contributor'


def extract_version(title):
    patterns = [
        r'\[PATCH\s+v(\d+)\s*,\s*\d+/\d+\]',
        r'\[RFC\s+v(\d+)\s*,\s*\d+/\d+\]',
        r'\[RESEND\s+v(\d+)\s*,\s*\d+/\d+\]',
        r'\[PATCH\s+v(\d+)\]', r'\[PATCHv(\d+)\]',
        r'\[RFC\s+v(\d+)\]', r'\[RFCv(\d+)\]',
        r'\[RESEND\s+v(\d+)\]', r'\[RESENDv(\d+)\]',
        r'\[PATCH\s+.*?\s+v(\d+)\]',
        r'\[v(\d+)\s*,\s*\d+/\d+\]', r'\[v(\d+)\]',
    ]
    for pattern in patterns:
        match = re.search(pattern, title, re.IGNORECASE)
        if match:
            return int(match.group(1))
    return None


def extract_base_title(title):
    base = re.sub(
        r'^\s*\[(?:GIT\s*,\s*PULL|(?:PATCH|RFC|RESEND)[\s,]?'
        r'v?\d*(?:\s*,\s*\d+/\d+)?|v\d+(?:\s*,\s*\d+/\d+)?)\]\s*',
        '', title, flags=re.IGNORECASE)
    base = re.sub(r'^\s*\[(?:PATCH|RFC|RESEND),\s*v?\d*\s*,\s*\d+/\d+\]\s*',
                  '', base, flags=re.IGNORECASE)
    base = re.sub(r'^\s*\[\d+/\d+\]\s*', '', base)
    return base.strip()


def extract_subject_prefix(title):
    clean = re.sub(
        r'^\s*\[(?:GIT\s*,\s*PULL|(?:PATCH|RFC|RESEND)[\s,]?'
        r'v?\d*(?:\s*,\s*\d+/\d+)?|v\d+(?:\s*,\s*\d+/\d+)?)\]\s*',
        '', title, flags=re.IGNORECASE)
    clean = re.sub(r'^\s*\[(?:PATCH|RFC|RESEND),\s*v?\d*\s*,\s*\d+/\d+\]\s*',
                   '', clean, flags=re.IGNORECASE)
    clean = re.sub(r'^\s*\[\d+\.\d+(?:\.\w+)?\s*,\s*\d+/\d+\]\s*', '',
                   clean, flags=re.IGNORECASE)
    clean = re.sub(r'^\s*\[\d+/\d+\]\s*', '', clean)
    clean = re.sub(r'^\s*\[(?:net(?:-next)?|sched_ext[^\]]*)\]\s*', '',
                   clean, flags=re.IGNORECASE)
    match = re.match(r'^([a-zA-Z0-9_\-/\.]+):\s*', clean)
    if match:
        return match.group(1).lower()
    return None


def classify_subsystem(title, url, patterns):
    text = (title + ' ' + url).lower()
    for subsystem, sub_patterns in patterns:
        for pattern in sub_patterns:
            if pattern in text:
                return subsystem
    return patterns[-1][0] if patterns else 'General'


def is_module_related(title, url, config):
    """Check if a patch belongs to this module using config's whitelist/blacklist."""
    title_lower = title.lower()
    module_name = config['name'].split()[-1].lower()

    # Git pull requests mentioning the module
    if 'git' in title_lower and 'pull' in title_lower and module_name in title_lower:
        return True

    prefix = extract_subject_prefix(title)

    # Check blacklist first
    if prefix and config.get('subject_blacklist'):
        for blocked in config['subject_blacklist']:
            if prefix == blocked or prefix.startswith(blocked.rstrip('/') + '/'):
                return False

    # Check whitelist
    if prefix and config.get('subject_whitelist'):
        for allowed in config['subject_whitelist']:
            if prefix == allowed or prefix.startswith(allowed + '/'):
                return True

    # For modules with search_query (vfio, iommu), also check keyword match
    sq = config.get('patchwork', {}).get('search_query', '')
    if sq and sq in title_lower:
        # Additional check: for vfio, require vfio in prefix or subject
        if sq == 'vfio':
            clean_lower = extract_subject_prefix(title) or title_lower
            if clean_lower and clean_lower.startswith('vfio'):
                return True
            # Also accept patches with vfio keywords
            for kw in ['vfio-pci', 'vfio_pci', 'vfio/platform', 'vfio_platform',
                       'vfio/mdev', 'vfio/fsl-mc', 'vfio/cdx',
                       'vfio_ccw', 'vfio_ap', 'vfio/iommufd']:
                if kw in title_lower:
                    return True
        return False

    return False


def is_patch_series(title):
    return bool(re.search(r'\s+\d+/\d+\s', title))


# ============================================================
# Chinese Summary Generator
# ============================================================

def chinese_summary(title):
    """Generate detailed Chinese summary (>= 50 chars) from patch title."""
    title_clean = re.sub(
        r'^\s*\[(?:GIT\s*,\s*PULL|(?:PATCH|RFC|RESEND)[\s,]?'
        r'v?\d*(?:\s*,\s*\d+/\d+)?|v\d+(?:\s*,\s*\d+/\d+)?)\]\s*',
        '', title, flags=re.IGNORECASE)
    title_clean = re.sub(
        r'^\s*\[(?:PATCH|RFC|RESEND),\s*v?\d*\s*,\s*\d+/\d+\]\s*',
        '', title_clean, flags=re.IGNORECASE)
    title_clean = re.sub(r'^\s*\[\d+\.\d+(?:\.\w+)?\s*,\s*\d+/\d+\]\s*', '',
                         title_clean, flags=re.IGNORECASE)
    title_clean = re.sub(r'^\s*\[\d+/\d+\]\s*', '', title_clean)
    title_clean = re.sub(r'^\s*\[(?:net(?:-next)?|sched_ext[^\]]*)\]\s*', '',
                         title_clean, flags=re.IGNORECASE)
    title_lower = title_clean.lower()

    action = ''
    detail = ''

    # Security/vulnerability fixes (highest priority)
    if re.search(r'use-after-free|uaf', title_lower):
        action, detail = '修复', 'use-after-free 漏洞，防止在错误恢复路径中访问已释放的内存对象'
    elif re.search(r'out-of-bounds|oob\b', title_lower):
        action, detail = '修复', '越界访问漏洞，确保数组索引和数据缓冲区访问严格限定在分配范围内'
    elif re.search(r'null\s*ptr|null\s*pointer|NULL\s*ptr', title_lower):
        action, detail = '修复', '空指针解引用问题，在指针使用前增加有效性检查以避免内核崩溃'
    elif re.search(r'memory\s*leak|mem\s*leak|memleak', title_lower):
        action, detail = '修复', '内存泄漏问题，在错误处理路径和设备释放流程中正确释放已分配内存'
    elif re.search(r'buffer\s*overflow|overflow', title_lower) and 'stack' not in title_lower:
        action, detail = '修复', '缓冲区溢出问题，确保数据拷贝操作不超过目标缓冲区的容量限制'
    elif re.search(r'race\s*condition|race\s|concurrent', title_lower):
        action, detail = '修复', '竞态条件问题，通过增加锁保护或调整执行顺序消除并发访问冲突'
    elif re.search(r'deadlock', title_lower):
        action, detail = '修复', '死锁问题，重新设计锁的获取顺序或使用超时机制防止无限等待'
    elif re.search(r'double\s*free', title_lower):
        action, detail = '修复', 'double-free 漏洞，确保每个内存对象只被释放一次'
    elif re.search(r'info\s*leak|information\s*leak', title_lower):
        action, detail = '修复', '信息泄漏问题，防止内核栈或堆中的未初始化数据暴露给用户空间'
    elif re.search(r'dangling\s*pointer|dangling\s*ref', title_lower):
        action, detail = '修复', '悬空指针问题，在对象生命周期结束后清除相关引用避免非法访问'
    elif re.search(r'refcount\s*leak|reference\s*leak|ref\s*leak', title_lower):
        action, detail = '修复', '引用计数泄漏问题，确保每次获取的引用计数都有对应的释放操作'
    elif re.search(r'uninit|uninitialized', title_lower):
        action, detail = '修复', '未初始化变量使用问题，确保变量在使用前已正确初始化为合理值'
    elif any(k in title_lower for k in
             ['fix', 'bug', 'broken', 'incorrect', 'wrong', 'fail', 'error']):
        action = '修复'
        dm = re.search(
            r'(?:fix|bug|broken|incorrect|wrong)\s*:?\s*(.+?)'
            r'(?:$|in\s|on\s|for\s|when\s|during)', title_lower)
        if dm:
            detail = dm.group(1).strip().rstrip('.,;')
            detail = re.sub(r'^(a|an|the)\s+', '', detail)
        if not detail or len(detail) < 10:
            detail = '相关功能缺陷或逻辑错误，确保操作行为符合预期规范'

    # Security hardening
    elif re.search(r'validate|sanitize|check\s+.*\s+bound|verify\s+.*\s+input',
                   title_lower):
        action, detail = '安全加固', '增加输入验证和边界检查，防止恶意或异常数据导致系统异常行为'

    # New features
    if not action:
        if re.search(r'add\s+support\s+for', title_lower):
            action = '新增'
            target = re.sub(r'.*add\s+support\s+for\s+', '', title_lower).strip()
            detail = f'支持 {target}，扩展框架的硬件兼容性和功能覆盖范围'
        elif re.search(r'add\b', title_lower):
            action = '新增'
            dm = re.search(r'add\s*:?\s*(.+?)(?:$|in\s|on\s|for\s|when\s|to\s)',
                           title_lower)
            if dm:
                detail = dm.group(1).strip().rstrip('.,;') + '，扩展功能特性'
            else:
                detail = '新的功能特性，增强子系统的能力'
        elif re.search(r'implement', title_lower):
            action = '实现'
            dm = re.search(r'implement\s*:?\s*(.+?)(?:$|in\s|on\s|for\s|when\s)',
                           title_lower)
            if dm:
                detail = dm.group(1).strip().rstrip('.,;') + '，完善缺失的功能接口'
            else:
                detail = '缺失的功能接口或操作处理逻辑'
        elif re.search(r'introduce', title_lower):
            action = '引入'
            dm = re.search(r'introduce\s*:?\s*(.+?)(?:$|in\s+\w+\s|on\s+\w+\s|when\s+\w+)',
                           title_lower)
            if dm:
                detail = dm.group(1).strip().rstrip('.,;') + '，扩展框架的功能范围'
            else:
                detail = '新的功能模块或接口抽象，优化代码组织'

    # Removal
    if not action:
        if any(k in title_lower for k in
               ['remove', 'drop', 'delete', 'deprecate', 'eliminate']):
            action = '移除'
            dm = re.search(
                r'(?:remove|drop|delete|deprecate|eliminate)\s*:?\s*'
                r'(.+?)(?:$|in\s|on\s|for\s|from)', title_lower)
            if dm:
                detail = dm.group(1).strip().rstrip('.,;') + '，清理冗余或过时的代码'
            else:
                detail = '不再需要的代码或功能，降低维护负担'

    # Refactoring / optimization
    if not action:
        if re.search(r'refactor', title_lower):
            action, detail = '重构', '重新组织代码结构以提升可读性和可维护性'
        elif re.search(r'clean\s*up|cleanup', title_lower):
            action, detail = '清理', '代码中的风格问题和废弃的命名方式'
        elif re.search(r'simplify', title_lower):
            action, detail = '简化', '代码逻辑，减少不必要的复杂度'
        elif re.search(r'optimize|optimise', title_lower):
            action, detail = '优化', '关键路径的性能表现，降低延迟和提高吞吐量'
        elif re.search(r'improve', title_lower):
            action = '改进'
            dm = re.search(r'improve\s*:?\s*(.+?)(?:$|in\s|on\s|for\s|when\s)',
                           title_lower)
            if dm:
                detail = dm.group(1).strip().rstrip('.,;') + '，提升健壮性和性能'
            else:
                detail = '代码质量和运行时行为'
        elif re.search(r'rework|re-organize|reorganize', title_lower):
            action, detail = '重写', '重新设计部分实现，优化数据流和处理逻辑'

    # Update / modify
    if not action:
        if re.search(r'update', title_lower):
            action, detail = '更新', '相关的配置或实现以反映最新的内核标准'
        elif re.search(r'convert|switch\s+to|migrate', title_lower):
            action = '迁移'
            dm = re.search(
                r'(?:convert|switch\s+to|migrate)\s*:?\s*(.+?)(?:$|in\s|on\s|for\s)',
                title_lower)
            if dm:
                detail = dm.group(1).strip().rstrip('.,;') + '，适配新的接口规范'
            else:
                detail = '到新内核 API 或框架，保持与主线兼容'
        elif re.search(r'replace\s+.+?\s+with\b', title_lower):
            action = '替换'
            rm = re.search(
                r'replace\s+(.+?)\s+with\s+(.+?)(?:$|in\s|on\s|for\s|to\s|and\s)',
                title_lower)
            if rm:
                detail = f'将 {rm.group(1)} 替换为 {rm.group(2).strip().rstrip(".,;")}，采用更规范的实现'
            else:
                detail = '用更优的实现方式替换旧代码'
        elif re.search(r'replace\b', title_lower):
            action, detail = '更新', '相关配置项或代码引用'
        elif re.search(r'rename', title_lower):
            action, detail = '重命名', '符号或函数以更清晰地表达其用途和语义'
        elif re.search(r'move\b.*\bto\b|relocate', title_lower):
            action, detail = '移动', '代码到更合适的位置，优化代码组织结构'
        elif re.search(r'enable\b|activate', title_lower):
            action, detail = '启用', '之前被禁用或条件编译的功能特性'
        elif re.search(r'disable\b|deactivate', title_lower):
            action, detail = '禁用', '存在稳定性或安全性问题的功能'
        elif re.search(r'pass\b.*\bto\b|forward\b', title_lower):
            action, detail = '传递', '各层之间正确传递参数和状态信息'
        elif re.search(r'\bset\s+\S+\s+to\b', title_lower):
            action = '修改'
            dm = re.search(r'set\s+(\S+)\s+to\s+(\S+)', title_lower)
            if dm:
                detail = f'将 {dm.group(1)} 配置为 {dm.group(2)}，调整运行参数'
            else:
                detail = '配置参数或常量值'
        elif re.search(r'at\s+enable\s+time|during\s+enable|in\s+\w*enable\s*\(',
                       title_lower):
            action = '重构'
            dm = re.search(r'(?:request|map|setup|prepare|init|configure|bar|resource)'
                           r'\s*.+?(?:$|in\s|on\s)', title_lower)
            if dm:
                detail = dm.group(0).strip().rstrip('.,;') + '，调整设备启用流程中的操作顺序'
            else:
                detail = '设备启用流程中的操作顺序和资源管理逻辑'

    # Documentation
    if not action:
        if re.search(r'document|doc\b|Documentation', title_lower):
            action, detail = '编写', '使用文档和 API 说明，帮助开发者正确使用相关接口'
        elif re.search(r'correct\s+typo|typo|spelling', title_lower):
            action, detail = '修正', '代码和文档中的拼写错误'

    # Tests
    if not action:
        if re.search(r'test|selftest', title_lower):
            action, detail = '添加', '测试用例，验证关键功能的正确性和稳定性'

    # Revert
    if not action:
        if re.search(r'revert', title_lower):
            action, detail = '回退', '之前的修改，因引入了回归问题或发现根本性设计缺陷'

    # Other common actions
    if not action:
        if re.search(r'backport', title_lower):
            action, detail = '回合', '主线修复或功能到稳定版本内核'
        elif re.search(r'extend|enhance', title_lower):
            action, detail = '扩展', '现有功能，增加新的操作参数或接口能力'
        elif re.search(r'prepare\b|prep\b', title_lower):
            action, detail = '准备', '为后续重大修改做前置准备，进行接口调整或代码重组'
        elif re.search(r'align|sync|synchronize', title_lower):
            action, detail = '对齐', '实现与内核其他子系统的规范保持一致'
        elif re.search(r'\bdon\'t\b|\bdo not\b|\bshould not\b', title_lower):
            action = '限制'
            dm = re.search(
                r'(?:don\'t|do not|should not)\s*(.+?)(?:$|in\s|on\s|for\s|when\s)',
                title_lower)
            if dm:
                detail = dm.group(1).strip().rstrip('.,;') + '，增加条件判断和安全保护逻辑'
            else:
                detail = '增加访问限制或前置条件检查，防止在不满足条件时执行操作'

    if not action:
        action = '修改'
        detail = '对代码进行调整和优化，修正细节问题或适应内核框架的变更'

    # Assemble
    summary = f'{action}{detail}'

    # Ensure >= 50 chars
    if len(summary) < 50:
        pads = {
            '修复': '，提升子系统的稳定性和可靠性，防止潜在的内核异常或崩溃风险',
            '新增': '，增强框架的功能完整性和适用范围，满足更多使用场景的需求',
            '添加': '，增强框架的功能完整性和适用范围，满足更多使用场景的需求',
            '移除': '，精简代码库规模，降低后续维护的复杂度和引入回归问题的风险',
            '清理': '，精简代码库规模，降低后续维护的复杂度和引入回归问题的风险',
            '重构': '，提升代码的可读性和可维护性，为后续功能迭代奠定更清晰的基础',
            '优化': '，提升代码的可读性和可维护性，为后续功能迭代奠定更清晰的基础',
            '改进': '，提升代码的可读性和可维护性，为后续功能迭代奠定更清晰的基础',
            '更新': '，保持子系统与内核主线的兼容性，适应 API 和框架的演进方向',
            '迁移': '，保持子系统与内核主线的兼容性，适应 API 和框架的演进方向',
            '实现': '，完善子系统的功能完备性，确保与硬件平台和上层框架的正确协同',
            '引入': '，提升框架的抽象能力和代码可扩展性',
        }
        for key, pad in pads.items():
            if key in action:
                summary += pad
                break
        else:
            summary += '，持续改进代码质量和功能完备性'

    return summary


# ============================================================
# Core Processing Pipeline
# ============================================================

def process_patches(patches_data, config):
    """Process raw patches: filter, classify, enrich."""
    processed = []
    filtered_count = 0

    for patch in patches_data:
        title = patch.get('name', patch.get('title', ''))
        url = patch.get('web_url', patch.get('url', ''))

        if not is_module_related(title, url, config):
            filtered_count += 1
            continue

        date = patch.get('date', '')[:10] if patch.get('date') else ''
        state = patch.get('state', 'unknown')
        submitter = patch.get('submitter', {})
        email = submitter.get('email', '') if isinstance(submitter, dict) else ''

        organization = extract_organization(email)
        subsystem = classify_subsystem(title, url,
                                       config['subsystem_patterns'])
        version = extract_version(title)
        summary = chinese_summary(title)

        if state in ['accepted', 'merged']:
            status = '已合入'
        elif state in ['declined', 'superseded', 'invalid']:
            status = '已关闭'
        else:
            status = '社区讨论中'

        series_info = patch.get('series', [{}])[0] if patch.get('series') else {}
        series_id = series_info.get('id') or patch.get('series_id')
        series_name = series_info.get('name') or patch.get('series_name')

        processed.append({
            'id': patch.get('id'),
            'title': title,
            'url': url,
            'date': date,
            'organization': organization,
            'subsystem': subsystem,
            'status': status,
            'state': state,
            'submitter': submitter.get('name', '')
            if isinstance(submitter, dict) else str(submitter),
            'email': email,
            'version': version,
            'summary': summary,
            'series_id': series_id,
            'series_name': series_name or title,
        })

    return processed, filtered_count


def deduplicate_by_series(processed_patches):
    """Dedup by base title across series, keep latest version."""
    by_base_title = {}
    for patch in processed_patches:
        base = extract_base_title(patch['title'])
        if base not in by_base_title:
            by_base_title[base] = []
        by_base_title[base].append(patch)

    final = []
    for base, patches in by_base_title.items():
        if len(patches) == 1:
            final.append(patches[0])
        else:
            versions = [p.get('version') for p in patches if p.get('version')]
            if versions:
                final.append(max(patches, key=lambda p: p.get('version') or 0))
            else:
                final.append(max(patches, key=lambda p: p['date']))
    return final


def _fetch_one_diff(patch_id):
    try:
        resp = requests.get(
            f'https://patchwork.kernel.org/api/patches/{patch_id}/', timeout=15)
        if resp.status_code == 200:
            diff = resp.json().get('diff', '')
            if diff:
                added = len([l for l in diff.split('\n')
                             if l.startswith('+') and not l.startswith('+++')])
                removed = len([l for l in diff.split('\n')
                               if l.startswith('-') and not l.startswith('---')])
                return patch_id, added + removed, diff[:8000]
        return patch_id, 0, ''
    except Exception:
        return patch_id, 0, ''


def fetch_line_counts(patch_ids, max_workers=8):
    """Returns (line_counts_dict, diff_map_dict)."""
    line_counts = {}
    diff_map = {}
    total = len(patch_ids)
    done = 0
    print(f"    正在获取 {total} 个 patch 的代码量...")
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        futures = {ex.submit(_fetch_one_diff, pid): pid for pid in patch_ids}
        for f in as_completed(futures):
            pid, count, diff_text = f.result()
            line_counts[pid] = count
            if diff_text:
                diff_map[pid] = diff_text
            done += 1
            if done % 50 == 0 or done == total:
                print(f"      进度: {done}/{total}")
    return line_counts, diff_map


def filter_by_code_lines(patches, line_counts):
    filtered, removed = [], []
    for p in patches:
        pid = p.get('id')
        summary = p.get('summary', '')
        lines = line_counts.get(pid, -1)
        if lines < 0:
            filtered.append(p)
            continue
        if any(k in summary for k in
               ['移除', '删除', 'remove', 'drop', 'deprecate', '回退']):
            if lines < 200:
                removed.append((p, lines))
                continue
        elif any(k in summary for k in
                 ['修复', '新增', '添加', '实现', '引入', '重写', '安全加固']):
            if lines < 100:
                removed.append((p, lines))
                continue
        filtered.append(p)
    return filtered, removed


def apply_cover_letters(surviving, code_filtered, pre_filter_patches):
    """Replace multi-patch series with cover letter if any patch qualifies."""
    all_by_series = defaultdict(list)
    for p in pre_filter_patches:
        sid = p.get('series_id')
        if sid:
            all_by_series[sid].append(p)

    filtered_by_series = defaultdict(list)
    for p, lines in code_filtered:
        sid = p.get('series_id')
        if sid:
            filtered_by_series[sid].append((p, lines))

    final, covered = [], set()
    series_count = 0

    for p in surviving:
        sid = p.get('series_id')
        if not sid:
            final.append(p)
            continue
        all_in = all_by_series.get(sid, [p])
        if len(all_in) <= 1:
            final.append(p)
            continue
        if sid in covered:
            continue

        survived_in = [sp for sp in surviving if sp.get('series_id') == sid]
        filtered_in = filtered_by_series.get(sid, [])
        num_surv = len(survived_in)
        num_total = num_surv + len(filtered_in)

        series_name = all_in[0].get('series_name', '')
        if not series_name:
            first = all_in[0].get('title', '')
            pm = re.match(r'^([^:]+):', first)
            series_name = (pm.group(1) + ': series') if pm else first
        series_name = extract_base_title(series_name)

        statuses = [sp.get('status', '社区讨论中') for sp in all_in]
        subsystems = [sp.get('subsystem', 'General') for sp in all_in]
        orgs = [sp.get('organization', 'Individual Contributor') for sp in all_in]
        dates = [sp.get('date', '') for sp in all_in if sp.get('date')]

        qualified_titles = [sp.get('title', '') for sp in survived_in]

        cover = {
            'id': None, 'title': series_name,
            'url': all_in[0].get('url', ''),
            'date': min(dates) if dates else '',
            'date_end': max(dates) if dates else '',
            'organization': max(set(orgs), key=orgs.count),
            'subsystem': max(set(subsystems), key=subsystems.count),
            'status': max(set(statuses), key=statuses.count),
            'state': 'series',
            'submitter': all_in[0].get('submitter', ''),
            'version': all_in[0].get('version'),
            'summary': chinese_summary(series_name),
            'is_cover_letter': True,
            'series_id': sid,
            'patch_count': num_total,
            'qualified_count': num_surv,
            'qualified_titles': qualified_titles[:5],
            'qualified_has_more': len(qualified_titles) > 5,
        }
        final.append(cover)
        covered.add(sid)
        series_count += 1

    # Dedup cover letters by title
    cl_by_title = {}
    non_cover = []
    for p in final:
        if p.get('is_cover_letter'):
            t = p['title']
            if t not in cl_by_title:
                cl_by_title[t] = p
            elif (p['qualified_count'] + p['patch_count'] >
                  cl_by_title[t]['qualified_count'] +
                  cl_by_title[t]['patch_count']):
                cl_by_title[t] = p
        else:
            non_cover.append(p)

    result = non_cover + list(cl_by_title.values())
    print(f"    Cover letter 替换: {len(cl_by_title)} 个 series")
    return result, len(cl_by_title)


# ============================================================
# Report Generation
# ============================================================

def generate_report(patches, start_date, end_date, config):
    """Generate Markdown report with improved hierarchy."""
    module_name = config['name']
    output_dir = config['output_dir']
    author = "IAMHCHCH <510725557@qq.com>"
    repo = "https://github.com/IAMHCHCH/linux-patches-tracker"

    filtered = [p for p in patches if start_date <= p['date'] <= end_date]
    merged = [p for p in filtered if p['status'] == '已合入']
    discussion = [p for p in filtered if p['status'] == '社区讨论中']

    total = len(filtered)
    disc_pct = len(discussion) * 100 / total if total > 0 else 0
    merged_pct = len(merged) * 100 / total if total > 0 else 0

    # Organization stats
    org_stats = defaultdict(list)
    for p in filtered:
        org_stats[p['organization']].append(p)

    # Subsystem stats
    subsys_stats = defaultdict(list)
    for p in filtered:
        subsys_stats[p['subsystem']].append(p)

    report = f"""# {module_name} Patch 追踪报告

---

## 报告信息

| 项目 | 内容 |
|------|------|
| 数据来源 | patchwork.kernel.org |
| 生成日期 | {datetime.now().strftime('%Y-%m-%d')} |
| 报告区间 | {start_date} 至 {end_date} |
| 仓库 | [{repo}]({repo}) |

---

## 统计概览

### 按状态分类

| 状态 | 数量 | 占比 |
|------|------|------|
| 社区讨论中 | {len(discussion)} | {disc_pct:.1f}% |
| 已合入 | {len(merged)} | {merged_pct:.1f}% |
| **总计** | **{total}** | **100%** |

### 按组织分类（TOP 15）

| 组织 | 数量 | 占比 |
|------|------|------|
"""
    top_orgs = sorted(org_stats.items(), key=lambda x: len(x[1]), reverse=True)[:15]
    for org, plist in top_orgs:
        pct = len(plist) * 100 / total if total > 0 else 0
        report += f"| {org} | {len(plist)} | {pct:.1f}% |\n"

    report += f"""
### 按子系统分类

| 子系统 | 数量 | 占比 |
|--------|------|------|
"""
    for sub, plist in sorted(subsys_stats.items(),
                             key=lambda x: len(x[1]), reverse=True):
        pct = len(plist) * 100 / total if total > 0 else 0
        report += f"| {sub} | {len(plist)} | {pct:.1f}% |\n"

    # Helper to write a section
    def write_section(patches_list, section_title):
        out = f"## {section_title}\n\n"
        if not patches_list:
            out += "暂无。\n\n"
            return out

        by_subsys = defaultdict(list)
        for p in patches_list:
            by_subsys[p['subsystem']].append(p)

        for sub in sorted(by_subsys.keys(),
                          key=lambda x: len(by_subsys[x]), reverse=True):
            sub_patches = by_subsys[sub]
            out += f"### ◆ 子系统：{sub}（{len(sub_patches)} patches）\n\n"

            by_org = defaultdict(list)
            for p in sub_patches:
                by_org[p['organization']].append(p)

            for org in sorted(by_org.keys(),
                              key=lambda x: len(by_org[x]), reverse=True):
                org_patches = by_org[org]
                out += f"**▸ 组织：{org}**（{len(org_patches)} patches）\n\n"

                for p in sorted(org_patches, key=lambda x: x['date'],
                                reverse=True):
                    if p.get('is_cover_letter'):
                        out += _fmt_cover(p)
                    else:
                        out += _fmt_patch(p)
            out += "---\n\n"
        return out

    # Merged section
    report += write_section(merged, "已合入 Patches")

    # Discussion section
    report += write_section(discussion, "社区讨论中 Patches")

    # Subsystem descriptions
    if config.get('subsystem_descriptions'):
        report += """---
## 子系统说明

"""
        for sub_name, sub_desc in config['subsystem_descriptions']:
            report += f"- **{sub_name}**：{sub_desc}\n"

    # Footer
    report += f"""
---

## 项目说明

{config.get('report_intro', '')}

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
python3 tracker.py {module_name.split()[-1].lower()}

# 指定日期范围
python3 tracker.py {module_name.split()[-1].lower()} --start 2026-03-01 --end 2026-04-30
```

---

*报告由 Linux Patches Tracker 自动生成 | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
    return report, filtered


def _fmt_patch(p):
    return (
        f"**{p['title']}**\n\n"
        f"- 日期：{p['date']}\n"
        f"- 状态：{p['status']}\n"
        f"- 概括：{p['summary']}\n"
        f"- 来源：{p['url']}\n\n"
    )


def _fmt_cover(p):
    lines = [
        f"**[SERIES] {p['title']}** "
        f"（cover letter，{p['qualified_count']}/{p['patch_count']} 个 patch 达到代码量阈值）\n",
        f"- 日期：{p['date']}",
    ]
    if p.get('date_end') and p['date_end'] != p['date']:
        lines.append(f"- 截止日期：{p['date_end']}")
    lines.append(f"- 状态：{p['status']}")
    lines.append(f"- 概括：{p['summary']}")
    if p.get('qualified_titles'):
        lines.append(f"- 达到阈值的 patches（{p['qualified_count']} 个，显示前 5）：")
        for t in p['qualified_titles']:
            lines.append(f"  - {extract_base_title(t)}")
        if p.get('qualified_has_more'):
            lines.append(f"  - ... 及其他 {p['qualified_count'] - 5} 个 patch")
    lines.append(f"- 来源：{p['url']}")
    return '\n'.join(lines) + '\n\n'


# ============================================================
# Data Fetching & Saving
# ============================================================

def fetch_patches(config, since_date):
    """Fetch all patches for a module from patchwork."""
    pw = config['patchwork']
    url = pw['url_template'].format(
        project_id=pw.get('project_id', ''),
        search_query=pw.get('search_query', ''),
        since=since_date,
    )
    # Clean up double slashes (not in https://)
    url = re.sub(r'(?<!:)//+', '/', url)

    all_patches = []
    page = 0
    while url:
        page += 1
        print(f"    第 {page} 页... (已获取 {len(all_patches)} 个 patch)")
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        all_patches.extend(data)
        link = resp.headers.get('Link', '')
        m = re.search(r'<([^>]+)>;\s*rel="next"', link)
        url = m.group(1) if m else None

    return all_patches


def save_data(patches, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    with open(f'{output_dir}/patches_data.json', 'w', encoding='utf-8') as f:
        json.dump(patches, f, indent=2, ensure_ascii=False)
    with open(f'{output_dir}/metadata.json', 'w', encoding='utf-8') as f:
        json.dump({
            'total': len(patches),
            'generated_at': datetime.now().isoformat(),
            'source': 'patchwork.kernel.org',
        }, f, indent=2, ensure_ascii=False)


# ============================================================
# Main Pipeline Runner
# ============================================================

def run_pipeline(module_key, config, start_date, end_date, force_refetch=False):
    """Run the full processing pipeline for one module."""
    output_dir = config['output_dir']
    cache_file = f'patchwork_data/{module_key}_patches.json'

    print(f"\n{'='*60}")
    print(f"  {config['name']} Patch 追踪")
    print(f"{'='*60}")

    # Step 0: Fetch or load
    if (not os.path.exists(cache_file)) or force_refetch:
        print(f"\n[1/6] 从 patchwork.kernel.org 获取数据...")
        since = f"{start_date}T00:00:00"
        raw = fetch_patches(config, since)
        os.makedirs('patchwork_data', exist_ok=True)
        with open(cache_file, 'w') as f:
            json.dump(raw, f)
        if raw:
            dates = [p.get('date', '')[:10] for p in raw if p.get('date')]
            print(f"    完成: {len(raw)} 个 patch，日期 {min(dates)} 至 {max(dates)}")
    else:
        print(f"\n[1/6] 加载缓存数据 ({cache_file})...")
        with open(cache_file, 'r') as f:
            raw = json.load(f)

    patches = raw if isinstance(raw, list) else raw.get('patches', [])
    print(f"    共 {len(patches)} 个原始 patches")

    # Step 1: Filter
    print(f"\n[2/6] 过滤非 {module_key} 相关 patch...")
    processed, filtered = process_patches(patches, config)
    print(f"    {len(processed)} 个相关（过滤 {filtered} 个）")

    # Step 2: Dedup
    print("\n[3/6] 版本去重...")
    deduped = deduplicate_by_series(processed)
    print(f"    去重后 {len(deduped)} 个")

    # Step 3: Code line filtering
    print("\n[4/6] 获取代码量并过滤小修改...")
    pre_filter = list(deduped)
    ids = [p['id'] for p in deduped if p.get('id')]
    code_filtered_list = []
    if ids:
        line_counts, diff_map = fetch_line_counts(ids)
        deduped, code_filtered_list = filter_by_code_lines(deduped, line_counts)
        print(f"    过滤后 {len(deduped)} 个（过滤 {len(code_filtered_list)} 个小修改）")
    else:
        line_counts, diff_map = {}, {}
        print("    无 patch ID，跳过")

    # Step 4: LLM-powered summary generation
    print("\n[4.5/6] 使用 LLM 生成 patch 概括（200字以内）...")
    _load_llm_cache(output_dir)
    if LLM_API_KEY and diff_map:
        llm_tasks = [
            (p['title'], diff_map.get(p.get('id'), ''), p.get('id'))
            for p in deduped if p.get('id') and p.get('id') in diff_map
        ]
        success = 0
        with ThreadPoolExecutor(max_workers=3) as ex:
            futures = {ex.submit(_batch_llm_task, t): t[2] for t in llm_tasks}
            for f in as_completed(futures):
                pid, summary = f.result()
                if summary:
                    success += 1
                    for p in deduped:
                        if p.get('id') == pid:
                            p['summary'] = summary
                            break
        _save_llm_cache()
        print(f"    LLM 概括完成: {success}/{len(llm_tasks)} 个 patch")
    else:
        print(f"    跳过 LLM 概括（API_KEY: {bool(LLM_API_KEY)}, diff映射: {bool(diff_map)}）")

    # Step 5: Cover letters
    print("\n[5/6] 应用 Cover Letter 逻辑...")
    deduped, _ = apply_cover_letters(deduped, code_filtered_list, pre_filter)
    print(f"    最终 {len(deduped)} 个条目")

    # Step 6: Generate report
    print("\n[6/6] 生成报告...")
    report, filtered_patches = generate_report(deduped, start_date, end_date,
                                               config)
    save_data(deduped, output_dir)
    with open(f'{output_dir}/REPORT.md', 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"    报告: {output_dir}/REPORT.md ({len(filtered_patches)} 条目)")

    return len(deduped)


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description='Linux Kernel Patches Tracker - Unified')
    parser.add_argument('module', nargs='?',
                        help='Module to track (crypto, vfio, iommu) or --all')
    parser.add_argument('--all', action='store_true',
                        help='Generate reports for all modules')
    parser.add_argument('--list', action='store_true',
                        help='List available modules')
    parser.add_argument('--start', help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end', help='End date (YYYY-MM-DD)')
    parser.add_argument('--force-refetch', action='store_true',
                        help='Force re-fetch data from patchwork')
    parser.add_argument('--add-module', help='Path to JSON file for custom module config')
    args = parser.parse_args()

    if args.list:
        print("Available modules:")
        for key, cfg in MODULES.items():
            print(f"  {key:8s} — {cfg['name']}")
        return

    if args.add_module:
        with open(args.add_module, 'r') as f:
            custom = json.load(f)
        key = custom['key']
        MODULES[key] = custom['config']
        print(f"Added custom module: {key}")

    if args.all:
        modules_to_run = list(MODULES.keys())
    elif args.module and args.module in MODULES:
        modules_to_run = [args.module]
    elif args.module:
        print(f"Unknown module: {args.module}")
        print(f"Available: {', '.join(MODULES.keys())}")
        sys.exit(1)
    else:
        parser.print_help()
        return

    total_entries = 0
    for mod_key in modules_to_run:
        cfg = MODULES[mod_key]
        start = args.start or cfg['default_start']
        end = args.end or cfg['default_end']
        n = run_pipeline(mod_key, cfg, start, end, force_refetch=args.force_refetch)
        total_entries += n

    print(f"\n{'='*60}")
    print(f"全部完成！共生成 {len(modules_to_run)} 份报告，{total_entries} 个条目")
    print(f"报告目录: output/")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
