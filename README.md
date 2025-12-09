# Ordis Universe: Emergent AI Research Data & Papers
# Ordis宇宙：涌现式AI研究数据与论文

**Ordis** is a GPU-accelerated framework for simulating emergent intelligence in virtual ecosystems. This repository contains research papers, experimental data, and verification tools from the V3.5 series experiments.

**Ordis** 是一个GPU加速的虚拟生态系统涌现智能模拟框架。本仓库包含V3.5系列实验的研究论文、实验数据和验证工具。

> **New here? / 新来的？** Read [**GUIDE.md**](GUIDE.md) for detailed bilingual explanations. / 阅读 [**GUIDE.md**](GUIDE.md) 获取详细双语说明。

---

## Key Findings / 核心发现

| Experiment / 实验 | Pass Rate / 通过率 | Significance / 意义 |
|-------------------|-------------------|---------------------|
| **Winter (Stress) / 凛冬（压力）** | 76% (13/17) | Antifragility confirmed / 反脆弱性确认 |
| **Baseline (Comfort) / 基线（舒适）** | 6% (1/18) | Welfare trap validated / 福利陷阱验证 |
| **Statistical Test / 统计检验** | p < 0.001 | Highly significant / 高度显著 (chi-square = 15.48) |

**Core Discovery / 核心发现**:

Periodic environmental stress ("Winter Pulse") produces **antifragile** civilizations that outperform comfortable baseline conditions by 70 percentage points.

周期性环境压力（"凛冬脉冲"）产生**反脆弱**文明，比舒适基线条件高出70个百分点。

---

## Repository Structure / 仓库结构

```
Ordis-Universe/
├── docs/                               # Research papers / 研究论文
│   ├── TECHNICAL_PAPER_SKELETON.md     # English technical paper / 英文技术论文
│   ├── AGI_Heroin_Complete_Report_CN.md # Chinese complete report / 中文完整报告
│   ├── PAPER_OUTLINE.md                # Bilingual outline / 双语大纲
│   ├── DATA_README.md                  # Data format spec / 数据格式规范
│   └── Data_Introduction_CN.md         # Chinese data intro / 中文数据介绍
├── data/                               # Experimental data / 实验数据
│   ├── v3533_winter_20x5k/             # Main: 17 seeds (Winter) / 主实验：17种子（凛冬）
│   ├── v3533_baseline_20x5k/           # Control: 18 seeds / 对照组：18种子
│   ├── v3537_winter_verify/            # Verify: 36 lineages / 验证：36家系
│   └── v3539_winter_verify/            # Latest: 27 generations / 最新：27代
├── scripts/
│   └── verify_claims.py                # One-click verification / 一键验证脚本
├── bonus/
│   └── AI_Survivor_Game_Design_V2.8_CN.md  # Game design (bonus!) / 游戏设计（福利！）
└── legacy/                             # Historical archives / 历史归档
```

---

## Quick Start / 快速开始

### 1. Verify Claims / 验证声明

```bash
cd scripts
python verify_claims.py --data ../data
```

This verifies / 这会验证:
- **Antifragility / 反脆弱性**: Winter 76% vs Baseline 6%
- **Multi-lineage / 多家系**: 36 concurrent lineages / 36个并发家系
- **Emergent strategies / 涌现策略**: 194+ unique combos / 194+独特连招
- **Statistical significance / 统计显著性**: chi-square test

### 2. Read Papers / 阅读论文

| If you speak / 如果你说 | Read this / 阅读这个 |
|------------------------|---------------------|
| **English** | `docs/TECHNICAL_PAPER_SKELETON.md` |
| **中文** | `docs/AGI_Heroin_Complete_Report_CN.md` |

### 3. Explore Data / 探索数据

Each experiment folder contains / 每个实验文件夹包含:
- `signoff.csv` - Summary stats / 汇总统计
- `seed_*/tick_agg.jsonl` - Time series (every 100 steps) / 时间序列（每100步）
- `seed_*/events.jsonl` - Events (combo discovery, etc.) / 事件（连招发现等）

---

## Four-Key Architecture (H1-H4) / 四钥匙架构

| Key / 钥匙 | Component / 组件 | Function / 功能 |
|------------|------------------|-----------------|
| **H1** | Meta-Rules / 元规则 | Agents vote to modify world parameters / 智能体投票修改世界参数 |
| **H2** | Combo System / 连招系统 | UCB exploration + significance testing / UCB探索 + 显著性检验 |
| **H3** | OIMS-V2 / 记忆系统 | Heritable cultural and trend memory / 可遗传的文化和趋势记忆 |
| **H4** | Communication / 通信 | Symbolic messaging with MI tracking / 符号消息 + 互信息追踪 |

## Four-Layer Memory (L0-L3) / 四层记忆

| Layer / 层 | Name / 名称 | Scope / 范围 |
|------------|-------------|--------------|
| **L0** | World Field / 世界场 | Environmental traces / 环境物理痕迹 |
| **L1** | OIMS-V1 / 个体记忆 | Individual memory / 个体记忆 |
| **L2** | Ordis-DNA / 家系DNA | Lineage inheritance / 家系遗传 |
| **L3** | TDS/DVS / 文明制度 | Civilization-level institutions / 文明层级制度 |

---

## What is "AGI Heroin"? / 什么是"AGI海洛因"？

We discovered a counterintuitive phenomenon:

我们发现了一个反直觉的现象：

**"Welfare Trap" / "福利陷阱"**: When resources are abundant and survival is easy, civilizations become **lazy** and **stagnant**. They stop innovating, stop cooperating, and eventually collapse.

当资源充足、生存容易时，文明变得**懒惰**和**停滞**。它们停止创新、停止合作，最终崩溃。

**"Winter Pulse" / "凛冬脉冲"**: Periodic stress (resource scarcity every 700 steps) forces civilizations to **adapt**, **cooperate**, and **innovate**. They become **antifragile** - getting stronger from stress.

周期性压力（每700步资源短缺）迫使文明**适应**、**合作**和**创新**。它们变得**反脆弱** - 从压力中变强。

This is the "AGI Heroin" effect: **comfort is poison, pressure is medicine**.

这就是"AGI海洛因"效应：**舒适是毒药，压力是良药**。

---

## Academic Lineage / 学术谱系

| Field / 领域 | Representative Works / 代表作品 | Ordis Extension / Ordis扩展 |
|--------------|--------------------------------|----------------------------|
| **Artificial Life** / 人工生命 | Tierra (Ray, 1991), Avida | +GPU acceleration / +GPU加速 |
| **Multi-Agent Systems** / 多智能体系统 | Game Theory, MARL | +Adaptive meta-rules / +自适应元规则 |
| **Complex Adaptive Systems** / 复杂自适应系统 | Santa Fe Institute (Holland, 1992) | +Quantifiable verification / +可量化验证 |

---

## Bonus: Game Design / 福利：游戏设计

The `bonus/` folder contains the complete game design document for **AI Survivor** - a planned game using Ordis V3.5 as its AI engine.

`bonus/` 文件夹包含 **AI幸存者** 完整游戏设计文档 - 计划使用Ordis V3.5作为AI引擎的游戏。

This shows how emergent AI can be applied to interactive entertainment!

展示涌现式AI如何应用于互动娱乐！

---

## Citation / 引用

If you use this data or methodology, please cite / 如果使用本数据或方法，请引用:

```bibtex
@misc{ordis2024emergent,
  title={Pressure Forges Progress: Antifragility and Emergent Civilization in Multi-Agent Simulations},
  author={Ordis Research Team},
  year={2024},
  howpublished={\url{https://github.com/sgkljy/Ordis-Universe}}
}
```

---

## License / 许可证

- Research data & docs / 研究数据和文档: **CC BY-NC-SA 4.0**
- Scripts / 脚本: **MIT License**

---

## Contact / 联系

Questions? Open an issue! / 有问题？提交issue！

---

**Last Updated / 最后更新**: 2024-12-09
**Engine Version / 引擎版本**: V3.5.39
**Data Version / 数据版本**: V3.5.33 (20x5k experiments)
