# Guardian V7 Comparison Experiment

**Experiment ID:** V391_guardian_V7
**Date:** 2026-01-01
**Seeds:** 42-61 (20 runs each condition)
**N_cap:** 200

## Purpose

Control experiment to verify that Guardian V7 **maintains** the natural thermodynamic attractor C ≈ 13.53, rather than **creating** it.

## Key Results

| Metric | Guardian OFF | Guardian ON | Delta |
|--------|--------------|-------------|-------|
| Pass Rate | 5% (1/20) | 45% (9/20) | **+40%** |
| Avg Alive | 102.7 | 175.6 | **+72.9** |
| guardian_interventions | **0** | 23.8 | - |

## Critical Evidence

1. `guardian_interventions = 0` for ALL 20 seeds in OFF condition
2. System still converges toward C ≈ 13.53 in surviving runs (OFF condition)
3. Without Guardian protection, massive death occurs but the attractor remains

## Conclusion

The constant C ≈ 13.53 emerges naturally (proven by E2 experiments and OFF condition).
Guardian V7 **maintains** this natural attractor, it does not **create** it.

Guardian V7's role:
- Prevents population collapse (alive: 102.7 → 175.6)
- Increases Pass rate (5% → 45%)
- Achieves this through ~24 interventions per run on average

## Files

- `guardian_OFF_signoff.csv` - Guardian V7 disabled (20 seeds)
- `guardian_ON_signoff.csv` - Guardian V7 enabled (20 seeds)

## Paired Design

Same seeds (42-61) used for both conditions, enabling direct comparison.

---

*Released for academic transparency in response to GitHub Issue #5*
