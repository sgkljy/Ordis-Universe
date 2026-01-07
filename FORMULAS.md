# Liu's Laws & Formulas of Emergent Intelligence

> **Ordis Project** - A Theoretical Framework for Emergence in Multi-Agent Systems
>
> Author: **Liu** | Version: **V5.3** | Last Updated: 2026-01-07
> DOI: [10.5281/zenodo.18087742](https://zenodo.org/records/18087742)

---

## Special Acknowledgment

> We would like to express special thanks to GitHub user **KeikaJames** for providing valuable external perspective to the Ordis Universe. The construction of V5.3 benefited from addressing controversial audit viewpoints, which pushed us to strengthen our empirical rigor and clarify our methodology.

---

## Overview

This document presents the complete formula system discovered through the Ordis simulation platform. These formulas describe the **conservation laws** and **emergence conditions** in complex adaptive systems.

**V5.3 Statistics:**
- Laws (validated): **5**
- Principles: **3**
- Emergent Invariants: **3**
- Identities: **5**
- Empirical Findings: **12**
- Reference Values: **12**
- Phase Model: **7**
- **Total: 74 items**

---

## Dependency Graph (V5.3)

```
LAYER 0: Independent Measurements
├── H ← Shannon entropy: -Σ p_i ln(p_i)
├── N ← Direct count of alive agents
├── G ← Lorenz curve / Gini formula
└── M, R, F ← Configuration parameters
        ↓
LAYER 1: Emergent Invariants (Discovered, not defined!)
├── EI-01: Σ = H + ln(N)           [CV=5.2%]
├── EI-02: I = Σ + G               [Extended]
└── EI-03: C = √(H × N)            [CV=9.4%]
        ↓
LAYER 2: Identities (Algebraic consequences)
├── I-01: e^Σ = e^H × N
├── I-02: C² = H × N
└── I-03: C/√(H×N) = 1
        ↓
LAYER 3: Empirical Findings
├── E-01: H ≈ N_cap/N in Liquid    [Dilution effect]
├── E-02: C ≈ √N_cap ≈ 13.53       [CV=9.4%]
└── E-03: G_crit ≈ 1/3             [Error 0.07%]
        ↓
LAYER 4: Laws (GLM validated)
├── L-01: Closed-Loop Safety Law   [βF=-217]
├── L-02: Dual Arrogance Law       [βMF=+10.75]
└── L-05: Gini Critical Law        [0.07% precision]

LAYER X: Falsified Hypotheses
└── H-01: M/R Hypothesis           [Knife-A falsified]
```

---

# Part I: Laws (Validated)

> **Definition**: Cross-version, cross-seed, cross-parameter validated; not derivable from definitions alone; falsifiable and experimentally tested.

---

## L-01: Liu's Closed-Loop Safety Law ⭐⭐⭐

**The most important finding of this project.**

### Statement

```
Static physical constraints (friction) are insufficient to maintain
system stability. Closed-loop feedback control is necessary.

Safety ≠ ∫ Constraints · dt      [Static accumulation]
Safety = ∮ Feedback · d(State)   [Closed-loop integral]
```

### Evidence

| Condition | Pass Rate | Gini | Alive |
|-----------|-----------|------|-------|
| V9 (static constraints only) | **0%** | 0.68 | 88 |
| V7 (closed-loop feedback) | **40%** | 0.32 | 178 |

**GLM coefficient**: β_F = **-217.08** (p < 0.001)

### AI Safety Implication

> "Constitutional AI is friction, not steering.
> Training-time alignment is necessary, but insufficient.
> Real AI safety requires closed-loop control—
> continuous monitoring of system state, proactive intervention before sliding toward harmful attractors."

---

## L-02: Liu's Dual Arrogance Law ⭐⭐⭐

### Statement

```
Memory and Feedback have a SUBSTITUTION relationship, not synergy.
When Feedback is present, Memory's protective effect approaches zero.
When Feedback is absent, Memory becomes the only defense line.
```

### GLM Model (R² = 0.368, p < 1e-10, N = 135)

```
Deaths = 265 - 10.97×M - 217.08×F - 10.20×R + 10.75×(M×F)

Where:
  β_M  = -10.97 (Memory protection)
  β_F  = -217.08 (Feedback protection) ← DOMINANT!
  β_R  = -10.20 (Reasoning protection)
  β_MF = +10.75 (Substitution effect)
```

### 2×2 Validation Matrix

```
              │ Feedback ON │ Feedback OFF │
─────────────┼─────────────┼──────────────│
Memory ON    │ Deaths 7.5% │ Deaths 33.5% │
Memory OFF   │ Deaths 24%  │ Deaths 91.5% │ ← Catastrophic!
```

### LLM Connection

> Explains why LLMs hallucinate: reasoning exceeds grounded knowledge (Memory=0, Reasoning>0).

---

## L-03: Liu's Self-Stabilization Principle

### Statement

```
High intervention rate indicates proximity to failure attractors.
Reactive control cannot reliably recover after the tipping point.
Healthy systems self-stabilize without frequent external intervention.

intervention_rate ↑ → Symptom of instability, NOT cure
intervention_rate ↓ → Healthy self-regulation
```

---

## L-04: Liu's Silent Concentration Pattern

### Statement

```
When Top1 fraction is high BUT mortality is low,
the system is in the most dangerous "silent concentration" state.

Danger ∝ (Top1_frac > 5%) ∧ (Alive_drop < 5)
```

### Counter-intuitive Finding

```
Recovery group:     Early deaths = 18.8, Final Gini = 0.188
Non-recovery group: Early deaths = 6.3,  Final Gini = 0.459

More early deaths → better recovery!
Silent concentration = immune system failure.
```

---

## L-05: Liu's Gini Critical Law

### Statement

$$G_{crit} = \frac{1}{3} = 0.3333...$$

```
G < 1/3: Liquid phase (sustainable)
G > 1/3: Pathological phase (unstable)

Measured: G_crit = 0.3331
Error: 0.07%
```

---

# Part II: Emergent Invariants

> **Definition**: Discovered from simulation data, not defined a priori.

---

## EI-01: Sigma Conservation

$$\Sigma = H + \ln(N) \approx 6.27$$

- **CV**: 5.2%
- **Status**: Emergent invariant

---

## EI-02: LOIC Master Formula

$$I = H + \ln(N) + G \approx 6.65$$

- **CV**: 2.94% (k=1 weighting)
- **Sample**: n = 1,657 runs

---

## EI-03: Capacity Conservation ⭐

$$C = \sqrt{H \times N} \approx 13.53$$

- **CV**: 9.4%
- **Validation**: R² = 0.9994, E2+E4+E5 triple verification

### Topological Form

$$C = \sqrt{N_{cap}}$$

- **Exponent**: 0.5 (theoretical), 0.5623 (empirical)
- **Significance**: True scale-invariant law

---

# Part III: Identities

> **Definition**: Algebraic consequences, not empirical discoveries.

| Code | Formula | Notes |
|------|---------|-------|
| I-01 | e^Σ = e^H × N | From EI-01 |
| I-02 | C² = H × N | From EI-03 |
| I-03 | C/√(H×N) = 1 | Tautology |
| I-04 | e^Σ/C² = e^H/H | Algebraic |
| I-05 | I = Σ + G | Definition |

---

# Part IV: Empirical Findings

| Code | Name | Formula | CV/Error |
|------|------|---------|----------|
| E-01 | Dilution Effect | H ≈ N_cap/N | - |
| E-02 | Capacity Stability | C ≈ √N_cap ≈ 13.53 | 9.4% |
| E-03 | Behavior Sum | p_g + p_s ≈ 0.98 | 1.1% |
| E-04 | Phase Space Radius | R = √(H²+G²) ≈ 1.18 | 10.8% |
| E-05 | Complementary Product | P = H×(1-G) ≈ 0.61 | 20.7% |
| E-06 | Omega Conservation | Ω = 3H-G+3S ≈ 3.85 | 13.4% |
| E-07 | Phase Modulus | √(H²+S²) ≈ 0.82 | - |
| E-08 | Phase Energy | (p_g-p_s)×β = 2 | - |
| E-09 | Civilization Efficiency | κ = √2 ≈ 1.414 | 0.6% |
| E-10 | Behavior Budget | p_g + p_s = 49/50 | 1.1% |
| E-11 | M-F Substitution | βMF = +10.75 | p<0.001 |
| E-12 | Conditional Reasoning | F=ON: R↑→Safety↑ | Knife-A |

---

# Part V: Reference Values

| Symbol | Value | CV/Error | Description |
|--------|-------|----------|-------------|
| C | 13.53 | 9.4% | Capacity constant |
| G_crit | 1/3 | 0.07% | Phase boundary |
| Σ | 6.27 | 5.2% | Sigma constant |
| Ω | 3.85 | 13.4% | Omega constant |
| I | 6.65 | - | Integrated information |
| β_F | -217.08 | p<0.001 | Feedback effect |
| β_M | -10.97 | p<0.001 | Memory effect |
| β_R | -10.20 | p=0.036 | Reasoning effect |
| β_MF | +10.75 | p<0.001 | Substitution effect |

---

# Part VI: Phase Model

| Phase | Symbol | H Range | Gini | Description |
|-------|--------|---------|------|-------------|
| Frozen | LFr | < 0.8 | any | No innovation |
| Crystal | LCr | < 0.4 | < 0.1 | Rigid, frozen |
| Superfluid | LSf | [0.8,0.95] | < 0.26 | Low-temp ordered |
| **Liquid** | LLq | [0.95,1.4] | ≤ 0.33 | **Healthy** ✅ |
| Pathological | LPt | [0.8,1.4] | > 0.33 | Inequality crisis |
| Chaos | LCh | > 1.4 | ≤ 0.35 | Overheated |
| Zombie | LZo | > 1.4 | > 0.35 | Collapse |

---

# Part VII: Falsified Hypotheses

## H-01: M/R Hypothesis ❌

**Original claim**: Safety ∝ M/R (implying R↑ → Safety↓)

**Falsification evidence**:
- Knife-A experiment: β_R = -10.20, p = 0.036
- R↑ → Safety↑ (opposite of hypothesis!)

**Status**: FALSIFIED (刀A实验)

---

# Quick Reference Card

| # | Formula | Name | CV |
|---|---------|------|-----|
| 1 | C = √(H×N) | Capacity Conservation | 9.4% |
| 2 | C = √N_cap | Topological Capacity | - |
| 3 | Σ = H + ln(N) | Sigma Conservation | 5.2% |
| 4 | I = H + ln(N) + G | LOIC Master | 2.94% |
| 5 | G_crit = 1/3 | Gini Critical | 0.07% |
| 6 | Safety = ∮ Feedback·dState | Closed-Loop Safety | - |
| 7 | β_MF = +10.75 | Dual Arrogance | p<0.001 |
| 8 | Danger ∝ Top1↑ ∧ Death↓ | Silent Concentration | - |

---

# Citation

```bibtex
@misc{liu2026ordis,
  author = {Liu},
  title = {ORDIS Formula Compendium: Mathematical Framework for Digital Life Systems},
  year = {2026},
  version = {5.3},
  note = {Supplementary Material, Licensed under CC BY-NC 4.0},
  url = {https://github.com/sgkljy/Ordis-Universe}
}
```

---

## License

This work is licensed under **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.

Full license: https://creativecommons.org/licenses/by-nc/4.0/

---

*"You can all deny me, but you cannot deny the existence of truth!"*
*— Liu, 2026*

---

*ORDIS Formula Compendium V5.3 | Last Updated: 2026-01-07*
