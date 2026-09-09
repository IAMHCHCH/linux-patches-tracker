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
import time
from datetime import datetime, date
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

PATCH_TAG_RE = re.compile(r'^\s*\[([^\]]+)\]\s*')

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
#   - DeepSeek:     LLM_API_KEY=sk-...   +  LLM_API_BASE=https://api.deepseek.com + LLM_MODEL=deepseek-chat
#   - Ollama(local): LLM_API_KEY=sk-dummy  +  LLM_API_BASE=http://localhost:11434
LLM_API_KEY = os.environ.get('LLM_API_KEY', '')
LLM_MODEL = os.environ.get('LLM_MODEL', 'claude-sonnet-4-20250514')
LLM_API_BASE = os.environ.get('LLM_API_BASE', 'https://api.anthropic.com')
LLM_SUMMARIZE_ALL = os.environ.get('LLM_SUMMARIZE_ALL', '').lower() in (
    '1', 'true', 'yes'
)
LLM_TABLE_BATCH_SIZE = int(os.environ.get('LLM_TABLE_BATCH_SIZE', '8'))
if LLM_API_BASE.startswith('[') and '](' in LLM_API_BASE:
    match = re.search(r'\]\((https?://[^)]+)\)', LLM_API_BASE)
    if match:
        LLM_API_BASE = match.group(1)
LLM_API_BASE = LLM_API_BASE.rstrip('/')

# In-memory & on-disk cache for LLM summaries (keyed by patch ID)
_SUMMARY_CACHE = {}
_SUMMARY_CACHE_PATH = None

BAD_SUMMARY_TOKENS = [
    '该系列围绕', '具体包括', '标题是', '根据标题', '成员标题',
    '简介：', '同理', '可能', '就是：', '需要概括', '需要总结',
    '主要改动', '从patch内容来看', '从 patch 内容来看',
    '增强功能', '提升稳定性', '完善框架', '扩展能力',
    '优化代码质量', '增强框架的功能完整性', '增强子系统的能力',
    '提升子系统的稳定性', '降低后续维护复杂度', '满足更多使用场景',
    '根据补丁列表', '基于补丁列表', '可以构造', '应该指明',
    '需要写', '需要说明', '标题表示', '那么主题', '其实',
    'patch list', 'no patch', 'diff shows', 'need summarize',
    'need mention', 'series "', 'patch list says',
    'diff adds', 'semantic not certain', 'but we can', 'we can just',
    'one sentence', 'subject:', 'no diff', 'no mail',
    '我们要', '可以：', '具体描述', '确凿', '输出：',
    '阐述',
]


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


def _extract_text_from_llm_response(data):
    if isinstance(data, dict):
        if isinstance(data.get('output_text'), str) and data['output_text'].strip():
            return data['output_text']
        choices = data.get('choices') or []
        if choices:
            choice = choices[0] or {}
            message = choice.get('message') or {}
            for key in ['content', 'reasoning_content', 'text']:
                value = message.get(key) if key in message else choice.get(key)
                text = _extract_text_from_llm_response(value)
                if text:
                    return text
        content = data.get('content')
        text = _extract_text_from_llm_response(content)
        if text:
            return text
        output = data.get('output')
        text = _extract_text_from_llm_response(output)
        if text:
            return text
        if data.get('type') == 'text' and isinstance(data.get('text'), str):
            return data.get('text')
        if isinstance(data.get('text'), str):
            return data.get('text')
        if isinstance(data.get('thinking'), str):
            return data.get('thinking')
    elif isinstance(data, list):
        parts = []
        for item in data:
            text = _extract_text_from_llm_response(item)
            if text:
                parts.append(text)
        return '\n'.join(parts)
    elif isinstance(data, str):
        return data
    return ''


def _call_llm_summary(title, diff_text, patch_id=None):
    """Generate a concise Chinese summary via LLM. Returns None on failure."""
    cache_key = 'v3:' + (str(patch_id) if patch_id else
                         hashlib.md5(title.encode()).hexdigest())
    cached = _SUMMARY_CACHE.get(cache_key)
    if cached:
        return cached

    if not LLM_API_KEY or not diff_text:
        return None

    # Truncate diff to keep API calls fast
    truncated = diff_text[:6000] if len(diff_text) > 6000 else diff_text

    system_prompt = (
        '你是 Linux 内核 patch 分析专家。请结合邮件正文、cover letter、commit message 和 diff，'
        '用一句中文总结这封 patch 邮件实际做了什么。必须写出具体对象、接口、流程、文件/驱动'
        '或被修复的问题，避免“增强功能、提升稳定性、完善框架、扩展能力”这类空泛表述。'
        '不要逐词翻译标题，不要解释分析过程，不要输出列表、前言或 Markdown。'
        '控制在 80 到 180 个中文字符之间。'
    )

    try:
        user_content = f'## 标题\n{title}\n\n## 证据\n```diff\n{truncated}\n```'
        summary = _post_llm(system_prompt, user_content, max_tokens=500, timeout=60)
        if not summary:
            print(f'    [LLM] 响应中未解析到文本 (id={patch_id})')
            return None
        summary = sanitize_summary(summary)
        if not summary:
            return None
        summary = compact_summary(summary)
        _SUMMARY_CACHE[cache_key] = summary
        _save_llm_cache()
        return summary
    except Exception as e:
        print(f'    [LLM] 概括失败 (id={patch_id}): {e}')
        return None


def _post_llm(system_prompt, user_content, max_tokens=500, timeout=90):
    if 'anthropic' in LLM_API_BASE:
        resp = requests.post(
            f'{LLM_API_BASE}/v1/messages',
            headers={
                'x-api-key': LLM_API_KEY,
                'anthropic-version': '2023-06-01',
                'content-type': 'application/json',
            },
            json={
                'model': LLM_MODEL,
                'max_tokens': max_tokens,
                'temperature': 0.1,
                'system': system_prompt,
                'messages': [{
                    'role': 'user',
                    'content': user_content
                }]
            },
            timeout=timeout
        )
    else:
        payload = {
            'model': LLM_MODEL,
            'max_tokens': max_tokens,
            'temperature': 0.1,
            'messages': [
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_content},
            ],
        }
        if 'deepseek' in LLM_API_BASE or os.environ.get('LLM_JSON_MODE'):
            payload['response_format'] = {'type': 'json_object'}
        resp = requests.post(
            f'{LLM_API_BASE}/v1/chat/completions',
            headers={
                'authorization': f'Bearer {LLM_API_KEY}',
                'content-type': 'application/json',
            },
            json=payload,
            timeout=timeout
        )
    resp.raise_for_status()
    return _extract_text_from_llm_response(resp.json())


def sanitize_summary(summary):
    if summary is None:
        return None
    if not isinstance(summary, str):
        summary = str(summary)
    summary = re.sub(r'```.*?```', '', summary, flags=re.S).strip()
    summary = re.sub(r'^\s*[-*]\s*', '', summary)
    summary = summary.replace('\n', ' ').strip()
    blocked = BAD_SUMMARY_TOKENS + [
        '我们需要分析', '一句话概括', '不超过',
        '直接说明', '保持技术准确性', '标题 "', '标题“',
    ]
    if any(token in summary for token in blocked):
        return None
    summary = re.sub(r'\s+', ' ', summary)
    return summary[:240]


def compact_summary(summary, limit=220):
    summary = sanitize_summary(summary) or ''
    if len(summary) <= limit:
        return summary
    cut = summary[:limit]
    for sep in ['。', '；', '，', '、']:
        pos = cut.rfind(sep)
        if pos >= int(limit * 0.6):
            return cut[:pos].rstrip('，、；。') + '。'
    space_pos = cut.rfind(' ')
    if space_pos >= int(limit * 0.75):
        return cut[:space_pos].rstrip('，、；。') + '。'
    return cut.rstrip('，、；。') + '。'


def _batch_llm_task(args):
    """Wrapper for ThreadPoolExecutor — returns (patch_id, summary_or_None)."""
    title, diff_text, patch_id = args
    return patch_id, _call_llm_summary(title, diff_text, patch_id)


def _call_llm_series_summary(series_title, patch_titles, patch_id=None):
    evidence = '\n'.join(f'- {extract_base_title(t)}' for t in patch_titles[:30])
    prompt_text = (
        f'系列标题：{series_title}\n'
        f'系列内 patch 标题：\n{evidence}\n'
        '请归纳这个 patch set 要解决的核心问题和主要技术改动。'
    )
    return _call_llm_summary(series_title, prompt_text, f'series-{patch_id}')


MODULES = {}

# ---- Crypto Module ----
MODULES['crypto'] = {
    'name': 'Linux Crypto 子系统',
    'output_dir': 'output/crypto',
    'default_start': '2026-07-01',
    'default_end': '2026-08-31',
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
    'default_start': '2026-07-01',
    'default_end': '2026-08-31',
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
    'default_start': '2026-07-01',
    'default_end': '2026-08-31',
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


def _strip_leading_patch_tags(title):
    """Remove common mailing-list tags while keeping the real subject intact."""
    clean = title.strip()
    while True:
        match = PATCH_TAG_RE.match(clean)
        if not match:
            break
        tag = match.group(1).strip()
        tag_lower = tag.lower()
        tag_parts = [p.strip().lower() for p in re.split(r'[,\s]+', tag_lower)
                     if p.strip()]
        has_patch_marker = any(p in (
            'patch', 'rfc', 'resend', 'pull', 'git', 'for-next',
            'net', 'net-next'
        ) or p.startswith('v') and p[1:].isdigit()
            for p in tag_parts)
        has_series_index = bool(re.search(r'\b\d+/\d+\b', tag_lower))
        has_version = bool(re.search(r'\bv\d+\b', tag_lower))
        if has_patch_marker or has_series_index or has_version:
            clean = clean[match.end():].lstrip()
            continue
        break
    return clean


def extract_patch_index(title):
    match = PATCH_TAG_RE.match(title.strip())
    if not match:
        return None, None
    idx = re.search(r'\b(\d+)/(\d+)\b', match.group(1))
    if not idx:
        return None, None
    return int(idx.group(1)), int(idx.group(2))


def extract_version(title):
    patterns = [
        r'\[(?:PATCH|RFC|RESEND)?\s*v(\d+)\s+\d+/\d+\]',
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
    return _strip_leading_patch_tags(title)


def extract_subject_prefix(title):
    clean = _strip_leading_patch_tags(title)
    match = re.match(r'^([a-zA-Z0-9_\-/\.]+):\s*', clean)
    if match:
        return match.group(1).lower()
    return None


def classify_subsystem(title, url, patterns, extra_text=''):
    text = (title + ' ' + extra_text + ' ' + url).lower()
    for subsystem, sub_patterns in patterns:
        for pattern in sub_patterns:
            if pattern in text:
                return subsystem
    return patterns[-1][0] if patterns else 'General'


def _match_subject_rules(prefix, rules):
    if not prefix or not rules:
        return []
    matches = []
    for rule in rules:
        rule_l = rule.lower().rstrip('/')
        if prefix == rule_l or prefix.startswith(rule_l + '/'):
            matches.append(rule_l)
    return matches


def is_module_related(title, url, config):
    """Check if a patch belongs to this module using config's whitelist/blacklist."""
    title_lower = title.lower()
    module_name = config['name'].split()[-1].lower()

    # Git pull requests mentioning the module
    if 'git' in title_lower and 'pull' in title_lower and module_name in title_lower:
        return True

    prefix = extract_subject_prefix(title)

    allowed_matches = _match_subject_rules(prefix, config.get('subject_whitelist'))
    blocked_matches = _match_subject_rules(prefix, config.get('subject_blacklist'))
    if allowed_matches and blocked_matches:
        allowed_len = max(len(m) for m in allowed_matches)
        blocked_len = max(len(m) for m in blocked_matches)
        return allowed_len > blocked_len
    if blocked_matches:
        return False
    if allowed_matches:
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
    idx, total = extract_patch_index(title)
    return bool(idx and total and total > 1)


# ============================================================
# Chinese Summary Generator
# ============================================================

def chinese_summary(title):
    """Generate detailed Chinese summary (>= 50 chars) from patch title."""
    title_clean = _strip_leading_patch_tags(title)
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


def chinese_series_summary(series_title, patch_titles):
    """Summarize a patch set from its cover title and member patch titles."""
    clean_title = extract_base_title(series_title)
    titles = [extract_base_title(t) for t in patch_titles if t]
    text = (clean_title + ' ' + ' '.join(titles)).lower()

    special = special_summary_from_titles(clean_title, titles)
    if special:
        return special

    concrete = concrete_series_summary(clean_title, titles)
    if concrete:
        return concrete

    subject = clean_title.split(':', 1)[0].strip() if ':' in clean_title else clean_title
    if 'tph' in text:
        return '具体调整 PCIe TPH 的能力暴露、配置写入、转发表编程和设备启停复位路径。'
    if 'live update' in text:
        return '具体增加 live update 期间设备文件、IOMMU 状态和测试负载的保存恢复路径。'
    if 'cxl' in text and 'passthrough' in text:
        return '具体补充 CXL Type-2 直通 UAPI、VFIO PCI CXL 绑定、HDM/COMP_REGS 区域和文档。'
    if 'sr-iov' in text or 'sriov' in text:
        return ('补充 SR-IOV 相关 VFIO 流程和自测试覆盖，验证 PF/VF 生命周期、资源暴露和用户态接口行为。')
    if 'falcon' in text and 'dma' in text:
        return ('新增面向 NVIDIA GPU Falcon DMA 路径的 VFIO 自测试驱动，用于覆盖设备侧 DMA 与隔离边界。')
    if 'mlx5' in text and 'self test' in text:
        return ('补充 MLX5 设备在 VFIO 自测试中的模拟和 DMA 覆盖，验证变体驱动与 IOMMU 映射路径的协同。')
    if 'module params' in text or 'vga unwind' in text:
        return ('整理 VFIO PCI 模块参数锁存、位域访问和 VGA 错误回滚流程，减少设备启用失败后的状态不一致。')
    if 'fmb' in text and ('zpci' in text or 'zdev' in text):
        return ('为 IBM zPCI VFIO 设备增加 FMB 特性控制和数据读取接口，让用户态可管理 s390 设备测量块。')
    if 'dmabuf' in text or 'dma-buf' in text:
        return ('完善 DMA-BUF 相关映射、导出和权限控制流程，增强用户态共享设备内存时的资源管理和安全边界。')
    if 'smmu' in text and ('invalidation' in text or 'tlbi' in text):
        return ('重整 ARM SMMU 的失效处理和批量提交路径，降低无效化延迟并强化异常场景下的同步与错误处理。')
    if 'riscv' in text and 'iommu' in text:
        return ('完善 RISC-V IOMMU 页表、失效或 DMA 集成能力，补齐架构驱动在虚拟化和设备隔离场景中的关键行为。')
    if 'qat' in text:
        return ('围绕 Intel QAT 驱动的设备能力、复位、迁移或接口清理进行调整，提升硬件加速器在主线内核中的可维护性。')
    if 'hisilicon' in text or 'hisi' in text:
        return ('改进 HiSilicon 加速器驱动的复位、隔离、队列或错误处理路径，提升设备管理和虚拟化场景稳定性。')
    if 'qcom' in text or 'qualcomm' in text or 'shikra' in text:
        return ('补齐 Qualcomm 平台加密或 IOMMU 相关设备树绑定与驱动支持，使新 SoC 的硬件能力可被内核正确发现。')
    if 'spacc' in text:
        return ('为 SPAcc 加密硬件补充算法、配置和设备树绑定支持，推动该加速器驱动进入 crypto 子系统。')
    if 'fix' in text or 'bug' in text or 'race' in text or 'leak' in text:
        return f'集中修复 {subject} 相关的错误处理、生命周期或并发问题。'
    if 'support' in text or 'add' in text or 'introduce' in text:
        return f'围绕 {subject} 增加新的硬件、UAPI 或框架能力。'
    if 'cleanup' in text or 'clean up' in text or 'remove' in text or 'drop' in text:
        return f'清理 {subject} 相关的旧接口、重复实现或风格问题。'
    return f'归纳 {subject} 系列中的关联改动。'


def _split_patch_title(title):
    clean = extract_base_title(title).strip().rstrip('.')
    parts = [p.strip() for p in clean.split(':')]
    if len(parts) >= 2:
        return ': '.join(parts[:-1]), parts[-1].strip()
    return '', clean


def _trim_detail(detail):
    detail = re.sub(r'\s+', ' ', detail.strip().strip('.'))
    detail = re.sub(r'^(a|an|the)\s+', '', detail, flags=re.I)
    return detail


def _polish_english_condition(text):
    text = re.sub(r'复位 (.+?) on (.+)$', r'在 \2 时复位 \1', text, flags=re.I)
    text = re.sub(r'改用 (.+?) for (.+)$', r'为 \2 改用 \1', text, flags=re.I)
    text = re.sub(r'保留 (.+?) across (.+)$', r'在 \2 前后保留 \1', text, flags=re.I)
    text = re.sub(r'导出 (.+?) for (.+)$', r'为 \2 导出 \1', text, flags=re.I)
    text = re.sub(r'新增用于 look up (.+?) 的 helper$', r'新增用于查找 \1 的 helper', text, flags=re.I)
    text = re.sub(r'新增用于 create (.+?) 的 helper$', r'新增用于创建 \1 的 helper', text, flags=re.I)
    text = re.sub(r'将 (.+?) 转换为 use (.+)$', r'将 \1 改为使用 \2', text, flags=re.I)
    text = re.sub(r'阻止 (.+?) from 变为可写$', r'阻止 \1 变为可写', text, flags=re.I)
    text = re.sub(r'修复 leak of (.+?) and (.+?) in (.+)$',
                  r'修复 \3 中 \1 和 \2 泄漏', text, flags=re.I)
    text = re.sub(r'启用 relaxed ordering on (.+)$',
                  r'启用 \1 的 relaxed ordering', text, flags=re.I)
    text = re.sub(r'改用 PHY internal loopback on (.+)$',
                  r'在 \1 上改用 PHY internal loopback', text, flags=re.I)
    text = re.sub(r'拒绝 to reset an SR-IOV PF（携带 enabled VFs）$',
                  '拒绝重置仍启用 VF 的 SR-IOV PF', text, flags=re.I)
    text = re.sub(r'拒绝 live migration on 64KB page（携带 QM_HW_V3 hardware）$',
                  '拒绝 QM_HW_V3 硬件在 64KB 页配置下执行 live migration', text, flags=re.I)
    text = re.sub(r'限制 the number of (.+)$', r'限制 \1 数量', text, flags=re.I)
    text = re.sub(r'确保 index for (.+?) are within range$', r'确保 \1 索引在范围内', text, flags=re.I)
    text = re.sub(r'计算 idal length based on idaw type$', '根据 IDAW 类型计算 IDAL 长度', text, flags=re.I)
    text = re.sub(r'确保 first IDAW remains constant$', '确保首个 IDAW 保持不变', text, flags=re.I)
    text = re.sub(r'取消 existing workqueues$', '取消已存在的 workqueue', text, flags=re.I)
    text = re.sub(r'绑定时创建 the (.+)$', r'绑定时创建 \1', text, flags=re.I)
    text = re.sub(r'接管 the whole (.+)$', r'接管整个 \1', text, flags=re.I)
    text = re.sub(r'拒绝 unsupported (.+?) at bind$', r'绑定时拒绝不支持的 \1', text, flags=re.I)
    text = re.sub(r'清除 (.+)$', lambda m: f'清除 {m.group(1)}', text, flags=re.I)
    text = text.replace('read/write regions', '读写 region')
    text = text.replace('hardware TPH state', '硬件 TPH 状态')
    text = text.replace('TPH is unsupported', '不支持 TPH')
    text = text.replace('device enable/disable', '设备启停')
    text = text.replace('reference to the KVM module', 'KVM 模块引用')
    text = text.replace('file-based reference counting for KVM', 'KVM 的基于文件引用计数')
    text = text.replace('file-based reference counting', '基于文件引用计数')
    text = text.replace('completion timeout retries', 'completion timeout 重试')
    text = text.replace('read-only region mappings', '只读 region 映射')
    text = text.replace('becoming writable', '变为可写')
    text = text.replace('scatterlist length overflows', 'scatterlist 长度溢出')
    text = text.replace('channel program segments', 'channel program segment')
    text = text.replace('a BAR sub-range', 'BAR 子范围')
    text = text.replace('a provider', 'provider')
    text = text.replace('a user-facing name for BAR mappings', 'BAR 映射的用户可见名称')
    text = text.replace('the reset logic in VFIO PCI device close path',
                        'VFIO PCI 设备关闭路径中的 reset logic')
    text = text.replace('various helpers from VFIO', 'VFIO helper')
    text = text.replace('the iommufd state of the vfio cdev', 'vfio cdev 的 iommufd 状态')
    text = text.replace('APIs to preserve/unpreserve a vfio cdev',
                        '保存/取消保存 vfio cdev 的 API')
    text = text.replace('mmap() attributes to DMABUF feature',
                        'DMABUF feature 的 mmap() 属性')
    text = re.sub(r'\s+when\s+(.+)$', r'（当 \1 时）', text, flags=re.I)
    text = re.sub(r'\s+during\s+(.+)$', r'（在 \1 期间）', text, flags=re.I)
    text = re.sub(r'\s+before\s+(.+)$', r'（在 \1 前）', text, flags=re.I)
    text = re.sub(r'\s+after\s+(.+)$', r'（在 \1 后）', text, flags=re.I)
    text = re.sub(r'\s+with\s+(.+)$', r'（携带 \1）', text, flags=re.I)
    text = re.sub(r'阻止 (.+?) from 变为可写$', r'阻止 \1 变为可写', text, flags=re.I)
    text = re.sub(r'拒绝 live migration on 64KB page（携带 QM_HW_V3 hardware）$',
                  '拒绝 QM_HW_V3 硬件在 64KB 页配置下执行 live migration', text, flags=re.I)
    text = re.sub(r'拒绝 to reset an SR-IOV PF（携带 enabled VFs）$',
                  '拒绝重置仍启用 VF 的 SR-IOV PF', text, flags=re.I)
    text = text.replace('a file handler', 'file handler')
    text = text.replace('a DMABUF', 'DMABUF')
    text = text.replace('PFNs for DMABUFs', 'DMABUF 的 PFN')
    text = text.replace('the live migration data mkey', 'live migration data mkey')
    text = text.replace('改用 基于文件引用计数', '改用基于文件的引用计数')
    text = text.replace('当 不支持 TPH 时', '当设备不支持 TPH 时')
    text = text.replace('在 设备启停 时', '在设备启停时')
    text = text.replace('复位 硬件', '复位硬件')
    return text


def _phrase_from_patch_desc(desc):
    desc = _trim_detail(desc)
    desc = re.sub(r'^[a-z0-9_/-]+\s+-\s+', '', desc, flags=re.I)
    lower = desc.lower()
    rules = [
        (r'^add a helper to (.+)$', lambda m: f'新增用于 {m.group(1)} 的 helper'),
        (r'^add support for (.+)$', lambda m: f'增加 {m.group(1)} 支持'),
        (r'^add (.+)$', lambda m: f'新增 {m.group(1)}'),
        (r'^allow (.+)$', lambda m: f'允许 {m.group(1)}'),
        (r'^provide (.+)$', lambda m: f'提供 {m.group(1)}'),
        (r'^export (.+)$', lambda m: f'导出 {m.group(1)}'),
        (r'^register (.+?) with (.+)$', lambda m: f'向 {m.group(2)} 注册 {m.group(1)}'),
        (r'^create (.+?) at bind$', lambda m: f'绑定时创建 {m.group(1)}'),
        (r'^detect (.+?) and load (.+?) on demand$', lambda m: f'检测 {m.group(1)} 并按需加载 {m.group(2)}'),
        (r'^implement (.+)$', lambda m: f'实现 {m.group(1)}'),
        (r'^introduce (.+)$', lambda m: f'引入 {m.group(1)}'),
        (r'^support (.+)$', lambda m: f'支持 {m.group(1)}'),
        (r'^enable (.+)$', lambda m: f'启用 {m.group(1)}'),
        (r'^disable (.+)$', lambda m: f'禁用 {m.group(1)}'),
        (r'^fix (.+)$', lambda m: f'修复 {m.group(1)}'),
        (r'^harden (.+)$', lambda m: f'加固 {m.group(1)}'),
        (r'^catch (.+)$', lambda m: f'捕获 {m.group(1)}'),
        (r'^take (.+)$', lambda m: f'获取 {m.group(1)}'),
        (r'^limit (.+)$', lambda m: f'限制 {m.group(1)}'),
        (r'^ensure (.+)$', lambda m: f'确保 {m.group(1)}'),
        (r'^calculate (.+)$', lambda m: f'计算 {m.group(1)}'),
        (r'^cancel (.+)$', lambda m: f'取消 {m.group(1)}'),
        (r'^clear (.+)$', lambda m: f'清除 {m.group(1)}'),
        (r'^refuse (.+)$', lambda m: f'拒绝 {m.group(1)}'),
        (r'^reject (.+)$', lambda m: f'拒绝 {m.group(1)}'),
        (r'^check (.+)$', lambda m: f'检查 {m.group(1)}'),
        (r'^hide (.+)$', lambda m: f'隐藏 {m.group(1)}'),
        (r'^expose (.+)$', lambda m: f'暴露 {m.group(1)}'),
        (r'^virtualize (.+)$', lambda m: f'虚拟化 {m.group(1)}'),
        (r'^reset (.+)$', lambda m: f'复位 {m.group(1)}'),
        (r'^revoke (.+)$', lambda m: f'撤销 {m.group(1)}'),
        (r'^prevent (.+)$', lambda m: f'阻止 {m.group(1)}'),
        (r'^preserve (.+)$', lambda m: f'保留 {m.group(1)}'),
        (r'^retrieve (.+)$', lambda m: f'恢复 {m.group(1)}'),
        (r'^block (.+)$', lambda m: f'阻止 {m.group(1)}'),
        (r'^avoid (.+)$', lambda m: f'避免 {m.group(1)}'),
        (r'^let (.+?) exclude (.+?) from (.+)$', lambda m: f'允许 {m.group(1)} 从 {m.group(3)} 中排除 {m.group(2)}'),
        (r'^(?:don\'t|do not) (.+)$', lambda m: f'避免 {m.group(1)}'),
        (r'^use (.+?) in place of (.+)$', lambda m: f'用 {m.group(1)} 替代 {m.group(2)}'),
        (r'^use (.+)$', lambda m: f'改用 {m.group(1)}'),
        (r'^convert (.+?) to (.+)$', lambda m: f'将 {m.group(1)} 转换为 {m.group(2)}'),
        (r'^replace (.+?) with (.+)$', lambda m: f'用 {m.group(2)} 替换 {m.group(1)}'),
        (r'^rename (.+?) to (.+)$', lambda m: f'将 {m.group(1)} 重命名为 {m.group(2)}'),
        (r'^factor out (.+)$', lambda m: f'抽出 {m.group(1)}'),
        (r'^split (.+)$', lambda m: f'拆分 {m.group(1)}'),
        (r'^move (.+?) to (.+)$', lambda m: f'将 {m.group(1)} 移到 {m.group(2)}'),
        (r'^remove (.+)$', lambda m: f'移除 {m.group(1)}'),
        (r'^drop (.+)$', lambda m: f'删除 {m.group(1)}'),
        (r'^document (.+)$', lambda m: f'补充 {m.group(1)} 文档/绑定'),
        (r'^clean up (.+)$', lambda m: f'清理 {m.group(1)}'),
        (r'^cleanup (.+)$', lambda m: f'清理 {m.group(1)}'),
        (r'^make (.+)$', lambda m: f'调整 {m.group(1)}'),
        (r'^set (.+)$', lambda m: f'设置 {m.group(1)}'),
        (r'^keep (.+)$', lambda m: f'保持 {m.group(1)}'),
        (r'^pass (.+)$', lambda m: f'传递 {m.group(1)}'),
        (r'^thread (.+)$', lambda m: f'串接 {m.group(1)}'),
        (r'^co-clear (.+)$', lambda m: f'同步清除 {m.group(1)}'),
        (r'^shrink (.+)$', lambda m: f'缩小 {m.group(1)}'),
        (r'^cache (.+)$', lambda m: f'缓存 {m.group(1)}'),
        (r'^latch (.+)$', lambda m: f'锁存 {m.group(1)}'),
        (r'^own (.+)$', lambda m: f'接管 {m.group(1)}'),
        (r'^selectively expand (.+)$', lambda m: f'按需扩展 {m.group(1)}'),
        (r'^periodically try (.+)$', lambda m: f'周期性尝试 {m.group(1)}'),
        (r'^conditional (.+)$', lambda m: f'按条件执行 {m.group(1)}'),
    ]
    for pattern, builder in rules:
        match = re.search(pattern, lower, flags=re.I)
        if match:
            # Re-match against the original text to preserve technical casing.
            original_match = re.search(pattern, desc, flags=re.I)
            return _polish_english_condition(builder(original_match or match))
    return _polish_english_condition(desc)


def concrete_patch_summary(title):
    scope, desc = _split_patch_title(title)
    phrase = _phrase_from_patch_desc(desc)
    if not phrase:
        return ''
    if scope:
        return f'在 {scope} 中{phrase}。'
    return f'{phrase}。'


def _dedupe_phrases(phrases):
    seen = set()
    result = []
    for phrase in phrases:
        key = re.sub(r'[^a-z0-9\u4e00-\u9fff]+', '', phrase.lower())
        if not key or key in seen:
            continue
        seen.add(key)
        result.append(phrase)
    return result


def _join_action_phrases(phrases):
    phrases = [p.strip().rstrip('。') for p in phrases if p and p.strip()]
    if not phrases:
        return ''
    if len(phrases) == 1:
        return phrases[0] + '。'
    if len(phrases) == 2:
        return f'{phrases[0]}，并{phrases[1]}。'
    return '、'.join(phrases[:-1]) + f'，并{phrases[-1]}。'


def concrete_series_summary(series_title, patch_titles, max_items=5):
    clean_title = extract_base_title(series_title).strip().rstrip('.')
    phrases = []
    for title in patch_titles:
        scope, desc = _split_patch_title(title)
        phrase = _phrase_from_patch_desc(desc)
        if not phrase:
            continue
        if scope and scope.lower() not in clean_title.lower():
            phrase = f'{scope} 中{phrase}'
        phrases.append(phrase)
    phrases = _dedupe_phrases(phrases)[:max_items]
    if not phrases:
        return ''
    return _join_action_phrases(phrases)


def special_summary_from_titles(series_title, patch_titles=None):
    titles = patch_titles or []
    joined = ' '.join([series_title] + titles)
    text = joined.lower()
    if 'crypto_aes_ctx' in text and (
        'zeroiz' in text or 'clear the crypto_aes_ctx' in text
    ):
        return (
            '新增 aes_zeroize_ctx() 等 AES 上下文清零封装，并让 aspeed、'
            'padlock、sa2ul、arm/arm64 aes-neonbs、qat、safexcel 等实现'
            '在操作结束后统一清除 crypto_aes_ctx 中的密钥材料。'
        )
    if 'pefile_parse_binary' in text or (
        'asymmetric_keys' in text and 'pe parser' in text
    ):
        if 'kunit' in text and 'oob' not in text:
            return (
                '为 asymmetric_keys 的 PE parser 增加 KUnit 覆盖，'
                '验证安全目录和 section 边界处理等异常输入，防止 '
                'pefile_parse_binary() 越界读问题回归。'
            )
        return (
            '修复 asymmetric_keys 中 pefile_parse_binary() 对 PE 安全目录'
            '和 section 范围校验不足导致的越界读，并补充 PE parser KUnit '
            '用例覆盖异常输入。'
        )
    if 'af_alg' in text and 'cryptsetup' in text:
        return (
            '在 AF_ALG skcipher allowlist 中加入 cryptsetup 使用的 '
            'xts(camellia)、xts(serpent)、xts(twofish) 等算法条目，'
            '让用户态磁盘加密工具继续通过 AF_ALG socket 调用这些 cipher。'
        )
    if 'af_alg_restrict cleanups' in text:
        return (
            '清理 AF_ALG 限制列表逻辑：将 cbc(paes) 标记为非特权可用，'
            '并调整 af_alg_check_restriction() 的同名条目匹配流程，避免无特权时继续'
            '遍历后续 allowlist 项造成权限判断歧义。'
        )
    if 'hwrng_fillfn' in text and ('suspend' in text or 'resume' in text):
        return (
            '在 hwrng core 中注册 PM notifier，系统 suspend/hibernate 前停止 '
            'hwrng_fillfn kthread 并记录停止状态，resume/restore 后再重新启动，'
            '避免休眠阶段后台线程继续触碰 RNG 设备。'
        )
    if 'vfio_dma_mapping_perf_test' in text:
        return (
            '在 VFIO selftests 中新增 vfio_dma_mapping_perf_test，'
            '用可配置映射大小和 memfd 场景测量 VFIO DMA map/unmap 性能，'
            '并断言 iommu_unmap() 后 region 已正确解除映射。'
        )
    if 'vfio/pci' in text and 'tph support' in text:
        return (
            '在 vfio/pci 中虚拟化 PCIe TPH capability 与 ST 表访问权限，'
            '新增 TPH_ST/DMA_BUF_TPH 设备特性和 IV-ST/NO-ST 策略控制，'
            '并在设备启停和 reset 路径同步硬件 TPH 状态。'
        )
    if 'base live update support for vfio' in text:
        return (
            '为 vfio-pci 接入 Live Update 基础机制：注册 live update 文件处理器，'
            '在设备冻结时阻止 MMIO/配置访问，保存并恢复 vfio cdev 与 iommufd 状态，'
            '让设备节点可跨更新保留。'
        )
    if 'mlx5 support for vfio self test' in text:
        return (
            '在 VFIO selftests 中新增 mlx5 用户态测试驱动，通过 BAR0 命令接口创建 '
            'PD/MR/QP/CQ/EQ 等对象，分配 DMA 缓冲区并用 RDMA WRITE 自环回验证设备 DMA 路径。'
        )
    if 'mmap() attributes to dmabuf feature' in text:
        return (
            '扩展 VFIO DMA_BUF feature 的 mmap 属性 UAPI，新增 '
            'VFIO_DEVICE_FEATURE_DMA_BUF_MEMATTR 结构用于设置 BAR 映射的内存属性，'
            '让用户态能显式控制 DMABUF mmap 行为。'
        )
    if 'crypto: cmh' in text or 'cryptomanager hub' in text:
        return (
            '新增 Rambus CryptoManager Hub 平台驱动，向 crypto API 注册 HMAC-SHA2/SHA3、'
            'CSHAKE/KMAC、SHA-2/3/SM3、AES/SM4、ChaCha20-Poly1305、RSA、'
            'ECDH/X25519、ML-KEM/ML-DSA 以及 DRBG hwrng 能力。'
        )
    if 'aes-ccm' in text and 'aes-gcm' in text and 'kunit' in text:
        return (
            '为 lib/crypto 的 AES-CCM 与 AES-GCM 库接口新增 KUnit 测试，'
            '抽出 aead-test-template.h/test-utils.h 复用测试模板，并让 hash 测试改为'
            '每个用例独立分配缓冲区。'
        )
    if 'hkdf' in text and ('fscrypt' in text or 'nvme' in text):
        return (
            '在 lib/crypto 中新增 HKDF-SHA256/384/512 extract/expand 库接口'
            '和 KUnit 覆盖，并把 fscrypt 与 NVMe 的密钥派生逻辑迁移到统一 HKDF helper。'
        )
    if 'fips self-tests' in text and 'aes' in text:
        return (
            '为 lib/crypto/aes.c 增加 AES 模式 FIPS 启动自检，覆盖 ECB、GCM、CCM '
            '等加解密向量校验，并将 fips.h 拆分为 fips-aes.h 与 fips-sha.h；'
            '自检失败时触发 panic。'
        )
    if 'padata' in text and 'serialized job' in text:
        return (
            '从 padata 中删除 serialized job 支持，移除对应文档、serial cpumask 回调'
            '和 padata_do_parallel() 的串行作业路径，只保留并行 multithreaded job 机制。'
        )
    if 'talitos' in text and ('first_desc' in text or 'first/last' in text):
        return (
            '清理 talitos ahash 请求上下文字段命名，将 first/last 改为 '
            'first_desc/last_desc，并同步调整 ahash digest/init/finup 路径及 '
            'sha224 软件初始化处理。'
        )
    if 'chacha' in text and 'avx-512' in text:
        return (
            '在 lib/crypto/x86 中新增 chacha-avx512-x86_64.S 和 '
            'chacha_16block_xor_avx512()，利用 AVX-512 zmm 寄存器一次并行处理 '
            '16 个 ChaCha block 的加解密异或。'
        )
    if 'rockchip' in text and 'rk356' in text and 'cryptographic offloader' in text:
        return (
            '为 Rockchip RK356x/RK3588 新增加密 offloader 驱动，加入 '
            'CRYPTO_DEV_ROCKCHIP2 Kconfig/Makefile 条目和 rk2_crypto.c 平台驱动，'
            '接入这些 SoC 的硬件加密加速器。'
        )
    if 'rk3576' in text and ('rknn' in text or 'rocket' in text):
        return (
            '为 RK3576 RKNN NPU 启用补齐 Rockchip IOMMU 支持，'
            '包括获取设备树时钟、在启用 stall 前清除 bootloader 遗留 '
            'stale page fault，并跳过孤儿 fault bank。'
        )
    return ''


def series_cover_title(p):
    title = extract_base_title(p.get('title', ''))
    if not p.get('is_cover_letter'):
        return title
    total = p.get('series_total') or p.get('patch_count') or 1
    version = p.get('version')
    if version:
        prefix = f'[PATCH v{version} 00/{total}]'
    else:
        prefix = f'[PATCH 00/{total}]'
    return f'{prefix} {title}'


def _escape_table_cell(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


def patch_importance_score(p):
    title = (p.get('title', '') + ' ' + p.get('summary', '')).lower()
    score = 0
    if p.get('is_cover_letter'):
        score += 50
        score += min(p.get('qualified_count', 0), 20) * 4
        score += min(p.get('patch_count', 0), 30)
    if p.get('status') == '已合入':
        score += 20
    if any(k in title for k in ['security', 'hardening', 'overflow', 'use-after-free',
                                'race', 'leak', 'crash', 'fault', 'isolation']):
        score += 25
    if any(k in title for k in ['support', 'add', 'introduce', 'implement',
                                'uapi', 'pasid', 'pri', 'tph', 'sva', 'migration',
                                'live update', 'iommufd']):
        score += 18
    if any(k in title for k in ['fix', 'bug', 'broken', 'incorrect', 'wrong']):
        score += 16
    if any(k in title for k in ['refactor', 'cleanup', 'clean up', 'remove',
                                'drop', 'rename']):
        score += 8
    score += min(p.get('version') or 1, 20)
    return score


def select_top_patches(patches, limit=20):
    return sorted(patches, key=lambda p: (
        patch_importance_score(p),
        p.get('date', ''),
        p.get('qualified_count', 0),
    ), reverse=True)[:limit]


def _most_common(values, default=''):
    values = [v for v in values if v]
    if not values:
        return default
    return max(set(values), key=values.count)


def _make_table_cover(series_id, group):
    dates = [p.get('date', '') for p in group if p.get('date')]
    versions = [
        p.get('series_version') or p.get('version')
        for p in group if p.get('series_version') or p.get('version')
    ]
    totals = [p.get('series_total') for p in group if p.get('series_total')]
    series_name = extract_base_title(group[0].get('series_name') or group[0].get('title', ''))
    member_titles = [p.get('title', '') for p in group if p.get('title')]
    cover = {
        'id': None,
        'title': series_name,
        'url': group[0].get('url', ''),
        'date': min(dates) if dates else '',
        'date_end': max(dates) if dates else '',
        'organization': _most_common(
            [p.get('organization') for p in group],
            'Individual Contributor'
        ),
        'subsystem': _most_common([p.get('subsystem') for p in group], 'General'),
        'status': _most_common([p.get('status') for p in group], group[0].get('status', '')),
        'state': 'series',
        'submitter': group[0].get('submitter', ''),
        'email': group[0].get('email', ''),
        'version': max(versions) if versions else group[0].get('version'),
        'summary': concrete_series_summary(series_name, member_titles),
        'summary_source': 'fallback',
        'mbox': group[0].get('mbox'),
        'series_mbox': group[0].get('series_mbox'),
        'is_cover_letter': True,
        'series_id': series_id,
        'patch_count': len(group),
        'series_total': max(totals) if totals else len(group),
        'qualified_count': len(group),
        'qualified_titles': member_titles[:5],
        'member_titles': member_titles,
        'member_ids': [p.get('id') for p in group if p.get('id')],
        'qualified_has_more': len(member_titles) > 5,
        'table_group_only': True,
    }
    return cover


def select_top_table_items(patches, limit=20):
    """Select important table rows while folding repeated series into one row."""
    by_series = defaultdict(list)
    for p in patches:
        sid = p.get('series_id')
        if sid:
            by_series[sid].append(p)

    ordered = sorted(patches, key=lambda p: (
        patch_importance_score(p),
        p.get('date', ''),
    ), reverse=True)
    selected = []
    used_series = set()
    used_patch_ids = set()
    for p in ordered:
        if len(selected) >= limit:
            break
        pid = p.get('id')
        if pid in used_patch_ids:
            continue
        sid = p.get('series_id')
        if sid and len(by_series.get(sid, [])) > 1:
            if sid in used_series:
                continue
            group = sorted(by_series[sid], key=lambda x: (
                patch_importance_score(x),
                x.get('date', ''),
            ), reverse=True)
            selected.append(_make_table_cover(sid, group))
            used_series.add(sid)
            used_patch_ids.update(x.get('id') for x in group if x.get('id'))
        else:
            selected.append(dict(p))
            if pid:
                used_patch_ids.add(pid)
    return selected


def format_brief_title(p):
    if p.get('is_cover_letter'):
        return series_cover_title(p)
    title = p.get('title', '')
    if title.lstrip().startswith('['):
        return title
    return f'[PATCH] {title}'


def _looks_generic_summary(summary):
    if not summary:
        return True
    summary_l = summary.lower()
    generic_tokens = [
        '修改对代码进行调整和优化',
        '持续改进代码质量和功能完备性',
        '新增support',
        '更新相关的配置或实现',
        '启用之前被禁用或条件编译',
        '扩展功能特性',
    ]
    translated_title_shape = bool(re.search(
        r'(新增|添加|实现|修复|移除|更新|重写|清理)[a-z0-9/_.,() -]+'
        r'(support|feature|test|bugs?|cleanup|fix|interface|issues?|leak|path|state)',
        summary_l)) or bool(re.search(
            r'^(新增|添加|实现|修复|移除|更新|重写|清理)[a-z0-9/_.,() -]+',
            summary_l))
    return (
        any(token in summary for token in BAD_SUMMARY_TOKENS + generic_tokens)
        or translated_title_shape
    )


def _table_fallback_summary(p):
    special = special_summary_from_titles(
        p.get('title', ''),
        p.get('member_titles') or p.get('qualified_titles') or []
    )
    if special:
        return compact_summary(special)
    if p.get('is_cover_letter'):
        titles = p.get('member_titles') or p.get('qualified_titles') or []
        summary = concrete_series_summary(p.get('title', ''), titles, max_items=6)
        if summary and not _looks_generic_summary(summary):
            return compact_summary(summary)
    summary = concrete_patch_summary(p.get('title', '')) or chinese_summary(p.get('title', ''))
    return compact_summary(summary)


def report_summary(p):
    special = special_summary_from_titles(
        p.get('title', ''),
        p.get('member_titles') or p.get('qualified_titles') or []
    )
    if special:
        return compact_summary(special)

    table_summary = sanitize_summary(p.get('table_summary', '')) or ''
    if table_summary and not _looks_generic_summary(table_summary):
        return compact_summary(table_summary)

    summary = sanitize_summary(p.get('summary', '')) or ''
    is_generic = _looks_generic_summary(summary)
    if p.get('is_cover_letter'):
        titles = p.get('member_titles') or p.get('qualified_titles') or [p.get('title', '')]
        concrete = chinese_series_summary(p.get('title', ''), titles)
        if p.get('summary_source') == 'llm' and summary and not is_generic:
            return compact_summary(summary)
        return compact_summary(concrete or summary or chinese_summary(p.get('title', '')))
    if summary and not is_generic:
        return compact_summary(summary)
    return compact_summary(
        concrete_patch_summary(p.get('title', '')) or chinese_summary(p.get('title', ''))
    )


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

        series_info = patch.get('series', [{}])[0] if patch.get('series') else {}
        series_id = series_info.get('id') or patch.get('series_id')
        series_name = series_info.get('name') or patch.get('series_name')
        series_version = series_info.get('version')
        series_mbox = series_info.get('mbox')
        _, series_total = extract_patch_index(title)

        organization = extract_organization(email)
        subsystem = classify_subsystem(title, url, config['subsystem_patterns'],
                                       series_name or '')
        version = extract_version(title) or series_version
        summary = chinese_summary(title)

        if state in ['accepted', 'merged']:
            status = '已合入'
        elif state in ['declined', 'superseded', 'invalid']:
            status = '已关闭'
        else:
            status = '社区讨论中'

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
            'mbox': patch.get('mbox'),
            'series_id': series_id,
            'series_name': series_name or title,
            'series_version': series_version,
            'series_mbox': series_mbox,
            'series_total': series_total,
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
        versions = [sp.get('series_version') or sp.get('version')
                    for sp in all_in if sp.get('series_version') or sp.get('version')]
        totals = [sp.get('series_total') for sp in all_in if sp.get('series_total')]

        qualified_titles = [sp.get('title', '') for sp in survived_in]
        all_titles = [sp.get('title', '') for sp in all_in]
        summary_source = 'fallback'
        series_summary = chinese_series_summary(series_name, all_titles)

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
            'version': max(versions) if versions else all_in[0].get('version'),
            'summary': series_summary,
            'summary_source': summary_source,
            'mbox': all_in[0].get('mbox'),
            'series_mbox': all_in[0].get('series_mbox'),
            'is_cover_letter': True,
            'series_id': sid,
            'patch_count': num_total,
            'series_total': max(totals) if totals else num_total,
            'qualified_count': num_surv,
            'qualified_titles': qualified_titles[:5],
            'member_titles': all_titles,
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

def generate_report(patches, start_date, end_date, config, top_table_patches=None):
    """Generate Markdown report with improved hierarchy."""
    module_name = config['name']
    output_dir = config['output_dir']
    author = "IAMHCHCH <510725557@qq.com>"
    repo = "https://github.com/IAMHCHCH/linux-patches-tracker"

    filtered = [p for p in patches if start_date <= p['date'] <= end_date]
    merged = [p for p in filtered if p['status'] == '已合入']
    discussion = [p for p in filtered if p['status'] == '社区讨论中']

    table_source = top_table_patches if top_table_patches is not None else patches
    table_filtered = [p for p in table_source if start_date <= p['date'] <= end_date]
    table_merged = [p for p in table_filtered if p['status'] == '已合入']
    table_discussion = [p for p in table_filtered if p['status'] == '社区讨论中']

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

    def write_top_table(patches_list, table_title):
        out = f"\n### {table_title}\n\n"
        if any(p.get('top_table_selected') for p in patches_list):
            top_items = sorted(patches_list, key=lambda p: (
                patch_importance_score(p),
                p.get('date', ''),
            ), reverse=True)[:20]
        else:
            top_items = select_top_table_items(patches_list, 20)
        if not top_items:
            return out + "暂无。\n"
        out += "| 厂商 | 简介 |\n|------|------|\n"
        for p in top_items:
            brief = f"{format_brief_title(p)} ------{report_summary(p)}"
            out += (
                f"| {_escape_table_cell(p.get('organization', ''))} "
                f"| {_escape_table_cell(brief)} |\n"
            )
        return out

    report += """
## 重点 Patch Top20 清单
"""
    report += write_top_table(table_merged, "已合入")
    report += write_top_table(table_discussion, "社区讨论")
    report += "\n---\n\n"

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
        f"- 概括：{report_summary(p)}\n"
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
    lines.append(f"- 概括：{report_summary(p)}")
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

def _request_get_with_retries(url, timeout=45, max_retries=5):
    last_error = None
    for attempt in range(1, max_retries + 1):
        try:
            resp = requests.get(url, timeout=timeout)
            resp.raise_for_status()
            return resp
        except requests.RequestException as exc:
            last_error = exc
            if attempt == max_retries:
                break
            sleep_seconds = min(60, 5 * attempt)
            print(
                f"      请求失败，{sleep_seconds}s 后重试 "
                f"({attempt}/{max_retries}): {exc}"
            )
            time.sleep(sleep_seconds)
    raise RuntimeError(f"请求 patchwork 失败: {url}\n{last_error}")


def _fetch_mbox_text(url, max_chars=30000):
    if not url:
        return ''
    try:
        resp = _request_get_with_retries(url, timeout=60, max_retries=4)
        text = resp.text
        return text[:max_chars]
    except Exception as exc:
        print(f"      获取邮件失败: {url} ({exc})")
        return ''


def _table_evidence_task(p):
    title = format_brief_title(p)
    mbox_url = p.get('series_mbox') if p.get('is_cover_letter') else p.get('mbox')
    if not mbox_url:
        mbox_url = p.get('mbox') or p.get('series_mbox')
    mail_text = _fetch_mbox_text(mbox_url, max_chars=5000)
    diff_text = p.get('_table_diff_excerpt', '')
    qualified = '\n'.join(
        f'- {extract_base_title(t)}'
        for t in (p.get('member_titles') or p.get('qualified_titles') or [])[:40]
    )
    return p, title, qualified, mail_text, diff_text


def _parse_batch_summary_response(text):
    clean = re.sub(r'^```(?:json)?\s*|\s*```$', '', text.strip(), flags=re.S)
    try:
        data = json.loads(clean)
        if isinstance(data, dict):
            return {str(k): sanitize_summary(v) for k, v in data.items()}
        if isinstance(data, list):
            result = {}
            for item in data:
                if isinstance(item, dict):
                    key = item.get('id') or item.get('key') or item.get('编号')
                    value = item.get('summary') or item.get('简介') or item.get('text')
                    if key and value:
                        result[str(key)] = sanitize_summary(value)
            return result
    except Exception:
        pass

    result = {}
    for line in clean.splitlines():
        match = re.match(r'^\s*([A-Z]\d{2})\s*[:：]\s*(.+?)\s*$', line)
        if match:
            result[match.group(1)] = sanitize_summary(match.group(2))
    return result


def _valid_table_summary(summary):
    summary = sanitize_summary(summary)
    if not summary:
        return None
    summary = compact_summary(summary)
    if _looks_generic_summary(summary):
        return None
    summary_l = summary.lower()
    if any(token in summary_l for token in [
        'series ', 'patch list', 'no patch', 'diff shows',
        'need summarize', 'need mention', 'based on the',
        'according to the',
    ]):
        return None
    if re.search(r'^(?:根据|基于|从|按照).{0,20}(?:标题|补丁列表|邮件)', summary):
        return None
    if re.search(r'(?:可以|应该|需要|那么|其实).{0,8}(?:总结|说明|构造|指明|聚焦)', summary):
        return None
    if re.search(r'(?:我们要|可以|具体描述|确凿|输出).{0,12}[：:]', summary):
        return None
    if re.search(r'在\s*[\w/+-]+\s*中[A-Za-z0-9_/(). -]{12,}。$', summary):
        return None
    if re.search(r'^[A-Za-z0-9_/(). -]+ support for [A-Za-z0-9_/(). -]+。$', summary):
        return None
    if re.search(r'^(?:新增|引入|添加)\s*[A-Za-z0-9_/(). -]{18,}。$', summary):
        return None
    if len(re.findall(r'[A-Za-z]{4,}', summary)) >= 5 and not re.search(
        r'(?:新增|修复|改为|改用|限制|避免|确保|实现|移除|增加|支持|将|在|通过)',
        summary
    ):
        return None
    return summary


def _batch_llm_table_summaries(entries, cache_tag='batch-table-v8'):
    if not entries:
        return {}
    system_prompt = (
        '你是 Linux 内核 patch 分析专家。用户会提供多封 patch/cover letter 邮件摘录。'
        '请为每个编号生成一句中文简介，必须基于对应邮件内容和 patch 列表，总结实际做了什么工作。'
        '每条都要写出具体对象、接口、寄存器、驱动、UAPI、错误路径或行为变化。'
        '禁止使用“增强功能、提升稳定性、完善框架、扩展能力、优化代码质量”等空泛表述。'
        '禁止出现“标题、成员标题、简介、可能、同理、就是、该系列围绕、具体包括”等分析过程或模板用语。'
        '不要复述英文题目；保留必要的函数名、驱动名、寄存器名和 UAPI 名称即可。'
        '不要合并不同编号，不要漏编号。返回严格 JSON 对象，key 为编号，value 为简介字符串。'
        '示例格式：{"E01":"在 af_alg allowlist 中加入 cryptsetup 需要的 skcipher/aead 算法，使非特权 cryptsetup 能继续通过 AF_ALG socket 调用这些算法。"}'
    )
    blocks = []
    for key, p, title, qualified, mail_text, diff_text in entries:
        blocks.append(
            f'### {key}\n'
            f'邮件主题: {title}\n'
            f'厂商: {p.get("organization", "")}\n'
            f'状态: {p.get("status", "")}\n'
            f'patch 列表:\n{qualified or "- 无"}\n'
            f'邮件摘录:\n<<<\n{mail_text[:5000] or "无邮件内容"}\n>>>\n'
            f'diff 摘录:\n```diff\n{diff_text[:5000] or "无 diff 摘录"}\n```'
        )
    user_content = '\n\n'.join(blocks)
    cache_key = f'{cache_tag}:' + hashlib.md5(user_content.encode()).hexdigest()
    cached = _SUMMARY_CACHE.get(cache_key)
    if cached:
        return {
            key: cleaned
            for key, value in cached.items()
            for cleaned in [_valid_table_summary(value)]
            if cleaned
        }
    try:
        text = _post_llm(system_prompt, user_content, max_tokens=6000, timeout=180)
        parsed = _parse_batch_summary_response(text)
        parsed = {
            key: cleaned
            for key, value in parsed.items()
            for cleaned in [_valid_table_summary(value)]
            if cleaned
        }
        _SUMMARY_CACHE[cache_key] = parsed
        _save_llm_cache()
        return parsed
    except Exception as exc:
        print(f"      Top20 批量 LLM 总结失败: {exc}")
        return {}


def enrich_top_table_summaries(patches, start_date, end_date, diff_map=None):
    if not LLM_API_KEY:
        print("    跳过 Top20 邮件级总结（未配置 LLM_API_KEY）")
        return

    diff_map = diff_map or {}
    filtered = [p for p in patches if start_date <= p['date'] <= end_date]
    if any(p.get('top_table_selected') for p in filtered):
        top_items = filtered
    else:
        top_items = []
        for status in ['已合入', '社区讨论中']:
            plist = [p for p in filtered if p.get('status') == status]
            top_items.extend(select_top_table_items(plist, 20))

    unique = {}
    for p in top_items:
        key = ('series', p.get('series_id')) if p.get('is_cover_letter') else ('patch', p.get('id'))
        unique[key] = p
    top_items = list(unique.values())

    for p in top_items:
        pid = p.get('id')
        if pid and pid in diff_map:
            p['_table_diff_excerpt'] = diff_map.get(pid, '')[:6000]
        elif p.get('member_ids'):
            excerpts = []
            for member_id in p.get('member_ids', [])[:4]:
                diff_text = diff_map.get(member_id, '')
                if diff_text:
                    excerpts.append(f'# patch {member_id}\n{diff_text[:1500]}')
            if excerpts:
                p['_table_diff_excerpt'] = '\n\n'.join(excerpts)

    print(f"    正在为 {len(top_items)} 个 Top20 表格条目拉取邮件...")
    evidences = [None] * len(top_items)
    with ThreadPoolExecutor(max_workers=6) as ex:
        futures = {
            ex.submit(_table_evidence_task, p): idx
            for idx, p in enumerate(top_items)
        }
        for f in as_completed(futures):
            evidences[futures[f]] = f.result()
    evidences = [e for e in evidences if e]

    batch_entries = []
    for idx, evidence in enumerate(evidences, 1):
        batch_entries.append((f'E{idx:02d}',) + evidence)

    print(
        f"    正在分批调用 LLM 总结 {len(batch_entries)} 个表格条目 "
        f"（每批 {LLM_TABLE_BATCH_SIZE} 条）..."
    )
    batch_summaries = {}
    for offset in range(0, len(batch_entries), LLM_TABLE_BATCH_SIZE):
        chunk = batch_entries[offset:offset + LLM_TABLE_BATCH_SIZE]
        batch_summaries.update(_batch_llm_table_summaries(chunk))

    missing = [
        entry for entry in batch_entries
        if not _valid_table_summary(batch_summaries.get(entry[0]))
    ]
    if missing:
        print(f"    {len(missing)} 个表格条目总结未通过质量检查，批量重试...")
        retry_size = max(2, min(4, LLM_TABLE_BATCH_SIZE))
        for offset in range(0, len(missing), retry_size):
            chunk = missing[offset:offset + retry_size]
            batch_summaries.update(
                _batch_llm_table_summaries(chunk, cache_tag='batch-table-v8-retry')
            )

    success = 0
    for key, p, _title, _qualified, _mail_text, _diff_text in batch_entries:
        summary = _valid_table_summary(batch_summaries.get(key))
        if summary:
            p['table_summary'] = summary
            p['table_summary_source'] = 'llm-mail-batch'
            success += 1
        else:
            p['table_summary'] = _table_fallback_summary(p)
            p['table_summary_source'] = 'fallback'
        p.pop('_table_diff_excerpt', None)
    _save_llm_cache()
    print(f"    Top20 批量邮件级总结完成: {success}/{len(batch_entries)} 个使用 LLM 邮件总结")


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
        resp = _request_get_with_retries(url)
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
    top_table_patches = []
    for status in ['已合入', '社区讨论中']:
        status_patches = [p for p in deduped if p.get('status') == status]
        selected = select_top_table_items(status_patches, 20)
        for item in selected:
            item['top_table_selected'] = True
        top_table_patches.extend(selected)

    # Step 4: LLM-powered summary generation
    print("\n[4.5/6] 使用 LLM 生成 patch 概括（200字以内）...")
    _load_llm_cache(output_dir)
    if LLM_API_KEY and diff_map and LLM_SUMMARIZE_ALL:
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
        print(
            f"    跳过全量 LLM 概括（API_KEY: {bool(LLM_API_KEY)}, "
            f"diff映射: {bool(diff_map)}, LLM_SUMMARIZE_ALL: {LLM_SUMMARIZE_ALL}）"
        )

    # Step 5: Cover letters
    print("\n[5/6] 应用 Cover Letter 逻辑...")
    deduped, _ = apply_cover_letters(deduped, code_filtered_list, pre_filter)
    print(f"    最终 {len(deduped)} 个条目")

    print("\n[5.5/6] 为 Top20 表格生成重点 patch 具体简介...")
    enrich_top_table_summaries(top_table_patches, start_date, end_date, diff_map)

    # Step 6: Generate report
    print("\n[6/6] 生成报告...")
    report, filtered_patches = generate_report(deduped, start_date, end_date,
                                               config, top_table_patches)
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
