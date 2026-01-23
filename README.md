# Ordis Universe

<h3 align="center">The Liu-Ordis Framework for Emergence Physics</h3>

<div align="center">

**8,309 simulation runs | 92,899 causal pairs | 11,836 safety records | 1.2B+ structured data points**

[![Model](https://img.shields.io/badge/HuggingFace-Ordis--7B--V1-yellow)](https://huggingface.co/sugiken/Ordis-7B-V1)
[![Paper](https://img.shields.io/badge/Zenodo-Paper%20III-blue)](https://zenodo.org/records/18222486)
[![License](https://img.shields.io/badge/License-Research-green)](#license)

</div>

---

## What Is This?

A complete simulation universe where AI agents are born, evolve, cooperate, betray, and die — across 5,000 time steps per run. No rules are hardcoded for cooperation, currency, or politics. Everything emerges from 6 primitive actions.

**We coded 6 actions. They invented economics, politics, and currency.**

---

## What We Have

### Data (1.2B+ structured data points)

| Dataset | Scale | What It Contains |
|---------|-------|-----------------|
| Core Simulation | 8,309 runs × 63 features | Behavioral, genetic, topological, political, economic time series |
| Causal Pairs | 92,899 counterfactual pairs | Same seed, different treatment, measured causal effects |
| Currency Emergence | 1,077 runs | Agents spontaneously invented currency (ratio_sg > 1) |
| Safety Suite | 11,836 records | Crisis detection → Intervention → Counterfactual proof |
| Ablation Experiments | 120 seeds | Counter-intuitive findings (incentives are HARMFUL) |
| Type B (Ideal State) | 66 seeds | High diversity + Low inequality + 92.8% survival |

Each run contains 5,000 timesteps × 100+ features = **500,000+ data points per run**.

**[Full Data Inventory →](./DATA_INVENTORY.md)**

### Model: Ordis-7B-V1

A 7B model fine-tuned with only 487 core theory samples, demonstrating capabilities typically requiring 100B+ parameters:

| Capability | Result | How |
|-----------|--------|-----|
| Anti-Hallucination | 3/3 rounds resisted gaslighting | Pure SFT, no RLHF |
| Cross-Domain Transfer | 4 unseen domains | Framework transfer at 7B scale |
| T-Shuffle Sensitivity | 100% detection | Real causal reasoning, not pattern matching |
| OOD Generalization | 100% on unseen N_cap | Formula applied beyond training range |

**No RLHF. No DPO. No prompt engineering. Just structured causal data.**

Download: [sugiken/Ordis-7B-V1](https://huggingface.co/sugiken/Ordis-7B-V1) (LoRA adapter, 646 MB)

### Verified Laws (from this data)

| Law | Formula | Validation |
|-----|---------|-----------|
| Dilution Effect | H = N_cap / N | 720 runs, CV<5% |
| Capacity Conservation | C = sqrt(H×N) = sqrt(N_cap) | R²>0.999 |
| Gini Critical Line | G > 0.333 → system death | 704 seeds |
| Closed-Loop Safety | F >> M ≈ R | effect size = -49 deaths |
| Linear Coupling | V = 2.126 × N_cap | 136 seeds, CV=2.83% |

---

## Key Discovery: Agents Invented Money

During a 720-run experiment, 9.5% of civilizations spontaneously evolved "Type B" (Ideal State):

- High behavioral diversity (H > 1.0)
- Low inequality (Gini < 0.18)
- **92.8% survival rate**
- Energy circulates faster than it's gathered (ratio_sg > 1.6)

This is pure bottom-up emergence of currency-like circulation — Fisher equation (MV=PQ) behavior with zero economic code.

**[Full Report & Data →](./data/emergence_currency_discovery/)**

### Ablation Proof: Incentives Are Harmful

| Experiment | Variable | Finding |
|-----------|----------|---------|
| A1: Remove sharing bonus | share_bonus = 0 | Type B rate DOUBLES (17% → 40%) |
| A2: Remove sharing cost | share_cost = 0 | Deaths INCREASE 83% |

Both results are counter-intuitive and challenge conventional economic assumptions.

---

## Publications

### The Liu-Ordis Trilogy

| Paper | Title | DOI |
|-------|-------|-----|
| **Paper III** | **Final Verdict: 22 Constraints on AI** | [10.5281/zenodo.18222486](https://zenodo.org/records/18222486) |
| Paper II | First Principles of AI Hallucination | [10.5281/zenodo.18169555](https://zenodo.org/records/18169555) |
| Paper I | The Verdict on AGI (Capacity Law) | [10.5281/zenodo.18113532](https://zenodo.org/records/18113532) |

### Earlier Works

| Paper | DOI |
|-------|-----|
| Liu-Ordis Capacity Law V2.0 | [10.5281/zenodo.18145700](https://zenodo.org/records/18145700) |
| The Emergence Formula V1.0 | [10.5281/zenodo.18087742](https://zenodo.org/records/18087742) |
| Black Hole Hypothesis V3.6 | [10.5281/zenodo.18068526](https://zenodo.org/records/18068526) |

---

## Repository Structure

```
Ordis-Universe/
├── DATA_INVENTORY.md          # Complete data asset inventory
├── PUBLICATIONS.md            # Full publication list
├── data/
│   └── emergence_currency_discovery/  # Currency emergence (704 seeds, sample data)
├── guardian/                   # Guardian V7 controller (pseudocode + source)
└── model/
    └── ordis_7b_v1/           # Model card, demos, capability analysis
```

---

## What Makes This Data Unique

| Property | Ordis | Typical Datasets |
|----------|-------|-----------------|
| Reproducibility | Perfect (4-way RNG isolation + config_hash) | Impossible |
| Causal structure | Interventional (ablation done) | Observational only |
| Temporal depth | 5,000 continuous steps | Sparse sampling |
| Hierarchy | Individual → Group → System → Emergence | Single-level |
| Emergence labels | Currency, politics, consciousness (zero hardcoding) | None |
| Privacy risk | Zero (100% synthetic) | GDPR/CCPA concerns |
| Copyright | Zero disputes (original engine output) | Lawsuit-prone |

---

## Try It Yourself

**5 complete Type B seeds available for free evaluation:**

[`data/emergence_currency_discovery/sample_seeds/`](./data/emergence_currency_discovery/sample_seeds/)

Each sample contains full tick_agg + events + entities + manifest + KPIs.

### Verification Checklist

1. Count alive entities in sample_entities → must equal tick_agg.alive
2. Track lineage_id across generations → mutations visible
3. ratio_sg shows power-law distribution, not smooth curves
4. DATA_WARNING events (~4,802/run) — fakers don't keep these

---

## Access

| Level | Content | Use Case |
|-------|---------|----------|
| Free (GitHub) | 5 sample seeds + model adapter | Evaluation |
| Research License | Selected subsets | Academic research |
| Commercial License | Full dataset + engine | Production training |

### Contact

- GitHub Issues: [OrdisAI/Ordis-Universe](https://github.com/OrdisAI/Ordis-Universe/issues)
- HuggingFace: [sugiken/Ordis-7B-V1](https://huggingface.co/sugiken/Ordis-7B-V1)

---

## License

- **Sample data (GitHub)**: CC BY-NC 4.0
- **Model weights**: Research use only
- **Full dataset**: Commercial license required
- **Papers**: Open access (Zenodo)

---

*All data generated by the Ordis Liquid Universe Engine. Zero privacy risk. Zero copyright disputes. 100% reproducible.*
