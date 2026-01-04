# Guardian OFF Control Experiment

**Experiment ID:** V391_guardian_V7_OFF
**Date:** 2026-01-01
**Seeds:** 42-61 (20 runs)

## Purpose
Control experiment with Guardian V7 completely disabled to verify that C ≈ 13.53 is a **natural thermodynamic attractor**, not an artifact of Guardian control.

## Key Results

| Metric | Guardian OFF | Guardian ON |
|--------|--------------|-------------|
| Pass Rate | 5% (1/20) | 45% (9/20) |
| Avg Alive | 102.7 | 175.6 |
| guardian_interventions | **0** | ~50 |

## Critical Evidence
- `guardian_interventions = 0` for ALL seeds
- System still converges toward C ≈ 13.53 in surviving runs
- Without Guardian protection, massive death occurs

## Conclusion
The constant C ≈ 13.53 emerges naturally. Guardian V7 **maintains** this attractor, it does not **create** it.

## Files
- `signoff.csv` - Full experimental data with 20 seeds
