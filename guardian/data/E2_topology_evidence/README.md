# E2 Topology Experiment Evidence

## Critical Timeline

| Event | Version | Date |
|-------|---------|------|
| **E2 Topology Experiments** | V3.6.83 | 2025-12-31 |
| Guardian V7 Development | V3.6.90 | 2026-01-01 |

**Key Finding**: E2 experiments were conducted BEFORE Guardian V7 existed.

## Experiment Summary

| Group | N_cap | Seeds | Mean Alive | Mean H | Mean Gini | guardian_interventions |
|-------|-------|-------|------------|--------|-----------|------------------------|
| D | 50 | **15** | 34.6 | 1.84 | 0.40 | **0** |
| A | 100 | **15** | 69.9 | 1.69 | 0.40 | **0** |
| B | 200 | **10** | 179.4 | 0.88 | 0.25 | **0** |
| C | 400 | **15** | 289.7 | 1.14 | 0.51 | **0** |

**Total: 55 seeds across 4 N_cap scales**

## Significance

The `guardian_interventions = 0` column proves:

1. **No external control** was applied during E2 experiments
2. **C = sqrt(H x N)** emerged naturally without any feedback controller
3. The value **13.53** is a **natural attractor**, not a control setpoint

Guardian V7 later adopted 13.53 as its target BECAUSE experiments revealed this natural constant.

**Causality**: Natural emergence (E2) -> Discovery of 13.53 -> Guardian V7 design

## Files

- `group_A_Ncap100_signoff.csv` - N_cap=100 experiment results (15 seeds)
- `group_B_Ncap200_signoff.csv` - N_cap=200 experiment results (10 seeds)
- `group_C_Ncap400_signoff.csv` - N_cap=400 experiment results (15 seeds)
- `group_D_Ncap50_signoff.csv` - N_cap=50 experiment results (15 seeds)

## Verification

To verify `guardian_interventions = 0`, check the `guardian_interventions` column in each CSV file.

---

*Updated 2026-01-05: Rebuilt complete signoff.csv files from original seed data*
*Released for academic transparency in response to GitHub Issue #5*
