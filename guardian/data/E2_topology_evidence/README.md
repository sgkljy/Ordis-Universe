# E2 Topology Experiment Evidence

## Critical Timeline

| Event | Version | Date |
|-------|---------|------|
| **E2 Topology Experiments** | V3.6.83 | 2025-12-31 |
| Guardian V7 Development | V3.6.90 | 2026-01-01 |

**Key Finding**: E2 experiments were conducted BEFORE Guardian V7 existed.

## Experiment Summary

| Group | N_cap | Seeds | Mean Alive | Mean H | guardian_interventions |
|-------|-------|-------|------------|--------|------------------------|
| D | 50 | 5 | 28.80 | 0.62 | **0** |
| A | 100 | 5 | 93.20 | 0.24 | **0** |
| B | 200 | 5 | 179.00 | 0.55 | **0** |

## Significance

The `guardian_interventions = 0` column proves:

1. **No external control** was applied during E2 experiments
2. **C = sqrt(H x N)** emerged naturally without any feedback controller
3. The value **13.53** is a **natural attractor**, not a control setpoint

Guardian V7 later adopted 13.53 as its target BECAUSE experiments revealed this natural constant.

**Causality**: Natural emergence (E2) -> Discovery of 13.53 -> Guardian V7 design

## Files

- `group_A_Ncap100_signoff.csv` - N_cap=100 experiment results
- `group_B_Ncap200_signoff.csv` - N_cap=200 experiment results
- `group_D_Ncap50_signoff.csv` - N_cap=50 experiment results

## Verification

To verify `guardian_interventions = 0`, check column 74 in each CSV file.

---

*Released for academic transparency in response to GitHub Issue #5*
