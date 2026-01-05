# Liu's Laws & Formulas of Emergent Intelligence

> **Ordis Project** - A Theoretical Framework for Emergence in Multi-Agent Systems
>
> Author: **Liu** | First Published: 2025-12 | DOI: [10.5281/zenodo.18087742](https://zenodo.org/records/18087742)

---

![Liu's Laws Formula Hierarchy](liu_laws_hierarchy.png)

---

## Overview

This document presents the complete formula system discovered through the Ordis simulation platform. These formulas describe the **conservation laws** and **emergence conditions** in complex adaptive systems.

**Total: 30+ Formulas** across multiple hierarchical layers, all empirically validated.

---

# Part I: Core Conservation Laws

## 1.1 Liu's Capacity Conservation (Layer 1) ⭐

$$C = \sqrt{H \times N} \approx 13.53$$

| Symbol | Meaning | Unit |
|--------|---------|------|
| C | System Capacity Constant | dimensionless |
| H | Shannon Entropy | nats |
| N | Population (alive) | count |

- **Tolerance**: ±5% (±0.68)
- **Validation**: R² = 0.9994, E2+E4+E5 triple verification

---

## 1.2 Topological Capacity Law

$$C = \sqrt{N_{cap}}$$

- **Exponent**: 0.5 (theoretical), 0.5623 (empirical)
- **Significance**: True scale-invariant law

---

## 1.3 Liu's Sigma Conservation (Layer 0)

$$\Sigma = H + \ln(N) \approx 6.27$$

- **CV**: 5.2%

---

## 1.4 LOIC Master Formula (Layer 2) ⭐⭐

$$I = H + \ln(N) + G \approx 6.65$$

| Symbol | Meaning | Range |
|--------|---------|-------|
| I | Integrated Information | ~6.65 |
| G | Gini Coefficient | [0, 1] |

- **CV**: 2.94% (k=1 weighting)
- **Sample**: n = 1,657 runs

**Sensitivity Analysis:**

| Form | k | CV |
|:-----|:--|:---|
| I = H + ln(N) | 0 | 3.44% |
| I = H + ln(N) + 0.5G | 0.5 | ~3.1% |
| **I = H + ln(N) + G** | **1** | **2.94%** ✓ |
| I = H + ln(N) + 2G | 2 | ~3.5% |

---

## 1.5 Liu's Omega Conservation (Layer 3)

$$\Omega = 3H - G + 3S \approx 3.85$$

- **CV**: 13.4%
- **Use**: Phase state indicator

### Omega Family Variants

| Formula | CV | Note |
|---------|-----|------|
| Ω = 3H - G + 3S | 11.0% | Official |
| Ω_simple = H + S | 9.2% | Simplest |
| Ω_top2 = 3H - G + 3τ | **2.13%** | Most stable ⭐ |

---

# Part II: Physical Constants

## 2.1 Core Constants Table

| Name | Symbol | Formula | Value | CV | Status |
|------|--------|---------|-------|-----|--------|
| **Gini Critical** | Φ | - | 1/3 = 0.333 | 0.07% | ✅ |
| **Heat Engine Efficiency** | κ | - | √2 = 1.414 | 0.6% | ✅ |
| **Complementary Product** | P | H×(1-G) | 0.61 | 20.7% | ✅ |
| **Phase Space Radius** | R | √(H²+G²) | 1.18 | 10.8% | ✅ |
| **Behavior Sum** | - | g + S | 49/50 = 0.98 | 1.1% | ✅ |
| **Capacity Balance** | - | s_eff + G | ~1.0 | 2.75% | ✅ |

---

## 2.2 Population-Inequality Power Law

$$G \times N^2 = K^2 \approx 11,464$$

- **Physical meaning**: Large societies must be more equal
- **Critical population**: N_crit ≈ 185

---

## 2.3 Liu's Ecological Niche Conservation

$$\sqrt{H} \times \sqrt{N} \approx 14.24$$

- **CV**: 6.1%
- **Status**: ✅ Validated and formally named

---

# Part III: Prime Code Signatures

## 3.1 Prime Codes

| Formula | Value | Factorization |
|---------|-------|---------------|
| e^I | ≈ 770 | 2 × 5 × 7 × 11 |
| e^Ω | ≈ 17 | Prime |

## 3.2 Prime Scaling Law

$$e^I = N_{cap}^{5/4}$$

- **Exponent**: 1.25 (encodes primes 2 and 5)
- **Cross-scale error**: < 1.5%

## 3.3 Prime Base Sequence

```
{7, 11, 17, 37}

7  - Base ratio (G/S = 7/3)
11 - Superfluid phase (GATHER = 9/11)
17 - Crystal phase
37 - Liquid behavior (GATHER = 37/50)
```

---

# Part IV: Behavior Laws

## 4.1 Liquid Phase Standard (37-12-49 System)

| Behavior | Fraction | Decimal |
|----------|----------|---------|
| GATHER | 37/50 | 0.74 |
| SHARE | 12/50 | 0.24 |
| G + S | 49/50 | 0.98 |
| G/S ratio | 7/3 | ~3:1 |

**Number Theory**: 37 is the 12th prime, 49 = 7²

---

## 4.2 Superfluid Phase (11 System)

| Equation | Value | Fraction | Error |
|----------|-------|----------|-------|
| GATHER | 0.8182 | 9/11 | 0.09% |
| 11 × SHARE | 1.7496 | 7/4 | **0.023%** ⭐ |

---

## 4.3 Cross-Phase Energy Conservation

$$(GATHER - SHARE) \times \beta = 2$$

| Phase | Calculation | Result |
|-------|-------------|--------|
| Liquid | (0.74 - 0.24) × 4.0 | 2.00 ✓ |
| Superfluid | (0.82 - 0.16) × 3.0 | 1.98 ✓ |

---

# Part V: Liu's Three Laws of Safe Emergence

## 5.1 First Law: M/R Law

$$Safety \propto \frac{Memory}{Reasoning}$$

> Safety is proportional to memory, inversely proportional to reasoning.

---

## 5.2 Second Law: Cognitive Arrogance ⭐⭐⭐

$$(M = 0) \land (R > 0) \Rightarrow Death$$

> No memory + active reasoning = hallucination fatality

**Evidence**:
- Memory=0, Reasoning=OFF → Alive=200 (frozen)
- Memory=0, Reasoning=ON → Alive=155 (**45 deaths!**)

**LLM Connection**: Explains why LLMs hallucinate - reasoning exceeds grounded knowledge.

---

## 5.3 Third Law: Gradual Emergence

$$k < 1 \quad (Logistic\ steepness)$$

> Emergence is gradual, not a phase transition.

**Evidence**: Pass rate varies only 6.6pp across 420 runs.

---

# Part VI: Derived Theorems

## 6.1 Information Efficiency Extremum

$$F(H) = H - \ln(H)$$
$$\frac{dF}{dH} = 0 \Rightarrow H^* = 1$$

- **Meaning**: H=1 is the mathematical optimum for information efficiency
- **Observed**: Liquid phase H_mean ≈ 0.75-1.08

---

## 6.2 Omega Equivalence Theorem

$$\Omega_{general} = \alpha H + \beta S + \gamma G$$

Where: α>0, β>0, γ≤0

**Minimal form**: Ω_min = H + S ≈ const

---

## 6.3 Dilution Formula

$$H = \frac{N_{cap}}{N}$$

When C = √N_cap is conserved, information density dilutes as population grows.

---

# Part VII: Hierarchical Audit Framework (V4.25)

```
Layer 0: Σ = H + ln(N)           ≈ 6.27   (±0.30)
    ↓
Layer 1: C = √(H×N)              ≈ 13.53  (±0.68)  [Core]
    ↓
Layer 2: I = H + ln(N) + G       ≈ 6.65   CV=2.94% [Master]
    ↓
Layer 3: Ω = 3H - G + 3S         ≈ 3.85   (±0.18)
    ↓
Prime:   e^I ≈ 770, e^Ω ≈ 17              [Signatures]
```

---

# Part VIII: Phase Boundaries

## 8.1 Seven Phase States

| Phase | H Range | Gini | Characteristic |
|-------|---------|------|----------------|
| **Liquid** | [0.8, 1.4] | < 0.33 | Healthy emergence ✅ |
| **Superfluid** | [0.7, 0.95] | < 0.20 | Low-temp ordered |
| **Crystal** | < 0.4 | - | Frozen, no innovation |
| **Chaos** | > 1.4 | - | Overheated collapse |
| **Oligarchy** | - | > 0.33 | Wealth concentration |
| **Dead** | - | - | Population collapse |
| **Frozen** | [0.4, 0.8] | - | Behavior rigidity |

## 8.2 Health Indicators

| Metric | Healthy Range |
|--------|---------------|
| omega_cv | [0.08, 0.12] |
| share_rate | < 70% |
| ratio_sg | < 2.0 |

---

# Part IX: Validation Summary

| Metric | Value |
|--------|-------|
| Total formulas | 30+ |
| Core conservation laws | 5 |
| Sample size (max) | n = 14,334 |
| Cross-scale validation | N_cap ∈ {50, 100, 200, 400} |
| Triple verification | E2 + E4 + E5 experiments |

**Data Repository**: [Zenodo](https://zenodo.org/records/18087742)

---

# Citation

```bibtex
@misc{liu2025ordis,
  author       = {Liu},
  title        = {Liu's Laws of Emergent Intelligence},
  year         = {2025},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.18087742},
  url          = {https://zenodo.org/records/18087742}
}
```

---

# Quick Reference Card

| # | Formula | Name | CV |
|---|---------|------|-----|
| 1 | C = √(H×N) | Capacity Conservation | 7.6% |
| 2 | C = √N_cap | Topological Capacity | - |
| 3 | Σ = H + ln(N) | Sigma Conservation | 5.2% |
| 4 | I = H + ln(N) + G | LOIC Master | **2.94%** |
| 5 | Ω = 3H - G + 3S | Omega Conservation | 13.4% |
| 6 | e^I ≈ 770 | Prime Code I | - |
| 7 | e^Ω ≈ 17 | Prime Code Ω | - |
| 8 | e^I = N^1.25 | Scaling Law | - |
| 9 | G×N² = K² | Population-Inequality | - |
| 10 | √H×√N ≈ 14.24 | Ecological Niche | 6.1% |
| 11 | (G-S)×β = 2 | Energy Conservation | - |
| 12 | g + S = 0.98 | Behavior Sum | 1.1% |
| 13 | Safety ∝ M/R | M/R Law | - |
| 14 | (M=0)∧(R>0)→Death | Cognitive Arrogance | - |
| 15 | k < 1 | Gradual Emergence | - |

---

*Last Updated: 2026-01-05*
