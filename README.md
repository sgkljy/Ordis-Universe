# Ordis Universe: Emergent AI Research Data & Papers

**Ordis** is a GPU-accelerated framework for simulating emergent intelligence in virtual ecosystems. This repository contains research papers, experimental data, and verification tools from the V3.5 series experiments.

## Key Findings

| Experiment | Pass Rate | Significance |
|------------|-----------|--------------|
| **Winter (Stress)** | 76% (13/17) | Antifragility confirmed |
| **Baseline (Comfort)** | 6% (1/18) | Welfare trap validated |
| **Statistical Test** | p < 0.001 | Highly significant (chi-square = 15.48) |

**Core Discovery**: Periodic environmental stress ("Winter Pulse") produces **antifragile** civilizations that outperform comfortable baseline conditions by 70 percentage points.

---

## Repository Structure

```
Ordis-Universe/
├── docs/                           # Research papers & documentation
│   ├── TECHNICAL_PAPER_SKELETON.md # English technical paper (IMRaD format)
│   ├── PAPER_OUTLINE.md            # Bilingual paper outline
│   ├── DATA_README.md              # Data format specification
│   ├── AGI_Heroin_Complete_Report_CN.md  # Chinese complete report
│   └── Data_Introduction_CN.md     # Chinese data introduction
├── data/                           # Experimental data
│   ├── v3533_winter_20x5k/         # Main experiment: 17 seeds, 5000 steps (Winter)
│   ├── v3533_baseline_20x5k/       # Control group: 18 seeds, 5000 steps (Baseline)
│   ├── v3537_winter_verify/        # Verification: 36 lineages, 7 generations
│   └── v3539_winter_verify/        # Latest: 6 lineages, 27 generations
├── scripts/
│   └── verify_claims.py            # One-click claim verification script
├── bonus/
│   └── AI_Survivor_Game_Design_V2.8_CN.md  # Game design document (Chinese)
└── legacy/                         # Historical content from previous releases
```

---

## Four-Key Architecture (H1-H4)

| Key | Component | Function |
|-----|-----------|----------|
| **H1** | Meta-Rules | Agents vote to modify world parameters |
| **H2** | Combo System | UCB exploration + significance testing for strategy discovery |
| **H3** | OIMS-V2 | Heritable cultural and trend memory |
| **H4** | Communication | Symbolic messaging with mutual information tracking |

## Four-Layer Memory (L0-L3)

| Layer | Name | Scope |
|-------|------|-------|
| **L0** | World Field | Environmental traces (physical layer) |
| **L1** | OIMS-V1 | Individual memory |
| **L2** | Ordis-DNA | Lineage inheritance |
| **L3** | TDS/DVS | Civilization-level institutions |

---

## Quick Verification

```bash
cd scripts
python verify_claims.py --data ../data
```

This script verifies all major claims in the paper:
- Antifragility: Winter 76% vs Baseline 6%
- Multi-lineage structure: 36 concurrent lineages
- Emergent strategies: 194+ unique combos
- Statistical significance: chi-square test

---

## Data Format

Each experiment directory contains:
- `signoff.csv` - Summary statistics for all seeds
- `seed_*/tick_agg.jsonl` - Time series data (every 100 steps)
- `seed_*/events.jsonl` - Discrete events (combo discovery, phase transitions)
- `run-manifest.json` - Experiment metadata and configuration

See [DATA_README.md](docs/DATA_README.md) for detailed field specifications.

---

## Academic Lineage

Emergent AI builds upon established research traditions:

| Field | Representative Works | Ordis Extension |
|-------|---------------------|-----------------|
| **Artificial Life (ALife)** | Tierra (Ray, 1991), Avida | +GPU acceleration, +social interaction |
| **Multi-Agent Systems (MAS)** | Game Theory, MARL | +adaptive meta-rules |
| **Complex Adaptive Systems (CAS)** | Santa Fe Institute (Holland, 1992) | +quantifiable verification |

---

## Bonus: Game Design Document

The `bonus/` folder contains the complete game design document for **AI Survivor** - a planned game that will use Ordis V3.5 as its AI engine. This document demonstrates how emergent AI technology can be applied to interactive entertainment.

---

## Citation

If you use this data or methodology in your research, please cite:

```bibtex
@misc{ordis2024emergent,
  title={Pressure Forges Progress: Antifragility and Emergent Civilization in Multi-Agent Simulations},
  author={Ordis Research Team},
  year={2024},
  howpublished={\url{https://github.com/[your-username]/Ordis-Universe}}
}
```

---

## License

Research data and documentation: CC BY-NC-SA 4.0
Verification scripts: MIT License

---

## Contact

For questions or collaboration inquiries, please open an issue or contact the research team.

---

**Last Updated**: 2024-12-09
**Engine Version**: V3.5.39
**Data Version**: V3.5.33 (20x5k experiments)
