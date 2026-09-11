# Linux Kernel Patches Tracker

一站式追踪 Linux 内核多个子系统的 patch 提交情况，自动生成分类、去重、按代码量过滤的中文报告。

支持模块：**Crypto** · **VFIO** · **IOMMU**（可扩展）。

## 快速开始

```bash
# 1. 安装依赖
pip install requests

# 2. 生成所有模块报告
python3 tracker.py --all
```

报告生成到 `output/{crypto,vfio,iommu}/REPORT.md`。

## 使用说明

```bash
# 列出所有模块
python3 tracker.py --list

# 只生成某个模块
python3 tracker.py crypto
python3 tracker.py vfio
python3 tracker.py iommu

# 指定日期范围
python3 tracker.py crypto --start 2026-03-01 --end 2026-04-30

# 强制重新获取数据（默认使用缓存）
python3 tracker.py --all --force-refetch

# 生成 2026 年 7-8 月三个模块报告
python3 tracker.py --all --force-refetch --start 2026-07-01 --end 2026-08-31
```

## 输出目录

```
output/
├── crypto/
│   ├── REPORT.md          # Crypto 子系统中文报告
│   ├── patches_data.json  # 处理后的完整数据
│   └── metadata.json      # 元数据
├── vfio/
│   ├── REPORT.md
│   ├── patches_data.json
│   └── metadata.json
└── iommu/
    ├── REPORT.md
    ├── patches_data.json
    └── metadata.json
```

## 处理流程

```
[1/6] 加载 patches 数据（或从 patchwork.kernel.org 获取）
[2/6] 过滤非目标模块相关 patch
[3/6] 跨 series 去重（相同基础标题只保留最新版本）
[4/6] 获取代码变更量并按阈值过滤小修改
[5/6] 应用 Cover Letter 逻辑
[6/6] 生成中文报告，并输出重点 Patch Top20 清单
```

## 功能特性

1. **模块过滤**: 通过 subject prefix 白名单/黑名单识别目标模块相关 patch
2. **多版本去重**: 按 base title 跨 series 去重，只保留最新版本
3. **代码量过滤**: 移除类 < 200 行、修复/新增类 < 100 行的小修改自动过滤
4. **Cover Letter 展示**: 多 patch 系列只要有一个达到代码阈值，就用 cover letter 代表
5. **按组织分类**: 按贡献者邮箱域名归类（NVIDIA、Intel、Google、AMD、Qualcomm 等）
6. **按子系统分类**: 按模块内部驱动模块细分（层次清晰的 ◆ 子系统 / ▸ 组织）
7. **中文概括**: 批量分析邮件正文和改动，说明使用场景、具体变化和直接影响；简介不列代码、文件名或函数名
8. **重点清单**: 每个模块输出已合入/社区讨论 Top20 表格，展示重点 patch；同一系列的多个重点 patch 合并为一行
9. **可扩展**: 通过 `--add-module` 加载自定义模块配置
10. **作者邮箱**: 已合入和社区讨论的正文详情展示作者邮箱，系列条目保留各成员作者；表格仍为厂商、简介两列

### 邮件分析与组织识别

设置 `LLM_API_KEY`、`LLM_API_BASE` 和 `LLM_MODEL` 后运行报告命令。
表格和正文均使用批量邮件分析，`LLM_TABLE_BATCH_SIZE` 控制每批条目数（默认 8），
不需要设置 `LLM_SUMMARIZE_ALL`。同一条目在表格和正文重复出现时复用分析结果。
正文摘录保留各封邮件的改动说明，邮件缓存位于忽略提交的 `patchwork_data/mail/`。
新摘要采用独立缓存版本，避免旧的代码式描述覆盖结果。
未配置模型或分析失败时明确标记为待分析，不用标题翻译冒充正文分析。

组织按邮箱的完整域名或子域名匹配，避免邮箱用户名或相似域名造成误判。
已知企业、高校、研究机构和社区单独归类；公共邮箱标为 `Individual Contributor`，
这只表示邮箱类型，不代表作者没有雇主。未知域名标为“归属待核实（域名）”，不默认归入个人贡献者。

## 添加自定义模块

创建 JSON 配置文件（如 `my_module.json`）：

```json
{
  "key": "my_module",
  "config": {
    "name": "Linux MyModule 子系统",
    "output_dir": "output/my_module",
    "default_start": "2026-02-01",
    "default_end": "2026-05-06",
    "patchwork": {
      "project_id": null,
      "search_query": "my_module",
      "url_template": "https://patchwork.kernel.org/api/patches/?q={search_query}&since={since}&per_page=100"
    },
    "subject_whitelist": ["my_module"],
    "subject_blacklist": [],
    "subsystem_patterns": [
      ["Core", ["my_module"]]
    ],
    "report_intro": "追踪 MyModule 子系统的 patch 提交情况。",
    "subsystem_descriptions": [
      ["Core", "MyModule 核心框架"]
    ]
  }
}
```

然后运行：

```bash
python3 tracker.py --add-module my_module.json my_module
```

字段说明：
- `patchwork.project_id`: patchwork 项目 ID（`null` 使用全局搜索）
- `patchwork.search_query`: 搜索关键词（`null` 不使用搜索过滤）
- `subject_whitelist`: 允许的 subject prefix 列表
- `subject_blacklist`: 排除的 subject prefix 列表
- `subsystem_patterns`: 二级分类规则 `[[名称, [关键词]], ...]`

## 模块说明

### Crypto

数据来源：patchwork project 151 (Linux Crypto)，直接按项目过滤。
涵盖硬件加密加速器驱动（QAT、CCP、CAAM 等）、加密算法实现（AES、SHA、ECC 等）
以及用户空间加密 API（AF_ALG）。

### VFIO

数据来源：patchwork project 8 (KVM)，通过 `q=vfio` 搜索。
涵盖 PCI 设备直通、平台设备直通、Mediated Device、IOMMUFD 集成、设备热迁移等。

### IOMMU

数据来源：patchwork 全局搜索 `q=iommu`，通过 subject prefix 白名单/黑名单精确过滤。
涵盖 Intel VT-d、AMD IOMMU、ARM SMMUv3、IOMMUFD、DMA-API 等。

## 依赖

- Python 3.6+
- `requests` 库

```bash
pip install requests
```

## 许可证

MIT
