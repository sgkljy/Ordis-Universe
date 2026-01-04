# Guardian V7: Dual-Loop Controller

## Overview

Guardian V7 is a homeostatic controller for the Ordis multi-agent simulation system. It maintains system health through **parameter adjustment only** - it does NOT directly manipulate agent states or behaviors.

## Files

| File | Description |
|------|-------------|
| `Guardian_V7_Pseudocode.md` | Algorithm logic in readable pseudocode |
| `ordis_guardian_v7.py` | Complete Python source code (343 lines) |

## Key Design Principle: No Hardcoded Rules

Guardian V7 **never**:
- Kills agents (`if entropy > x then kill agent`)
- Forces specific behaviors
- Directly modifies agent internal states

Guardian V7 **only**:
- Adjusts environmental parameters (resource regeneration rate)
- Modifies incentive signals (share_bonus)
- Changes propagate through agent decision-making naturally

## Algorithm Summary

```
Dual-Loop Architecture:

┌─────────────────────────────────────────────────┐
│  FAST LOOP (Behavioral) - Highest Priority      │
│  ─────────────────────────────────────────────  │
│  IF share_rate > 70% OR ratio_sg > 2.0:         │
│      → AUSTERITY (reduce share_bonus by 0.2)    │
│      → Bypasses DND check!                      │
├─────────────────────────────────────────────────┤
│  DND CHECK (Do Not Disturb)                     │
│  ─────────────────────────────────────────────  │
│  IF system is healthy (Gini < 0.28, H ∈ [0.9,   │
│     1.35], alive ≥ 140):                        │
│      → No intervention                          │
├─────────────────────────────────────────────────┤
│  SLOW LOOP (Physical) - Q-value regulation      │
│  ─────────────────────────────────────────────  │
│  Q = √(H × N), target = 13.53                   │
│  IF Q too low:  → STIMULATE (boost regen)       │
│  IF Q too high: → COOL_DOWN (reduce activity)   │
└─────────────────────────────────────────────────┘
```

## Intervention Mechanisms

| Action | Trigger | Mechanism |
|--------|---------|-----------|
| AUSTERITY | Over-sharing detected | `share_bonus -= 0.2` |
| STIMULATE | Q below target | `resource_regen += 0.1` |
| COOL_DOWN | Q above target | Reduce environmental stimulation |

## Empirical Results

| Metric | V7 OFF | V7 ON | Change |
|--------|--------|-------|--------|
| Pass Rate | 5% | 45% | +40pp |
| Avg Alive | 102.7 | 175.6 | +71% |

## Citation

If you use this controller or adapt its design, please cite:

```
Liu-Ordis Framework (2026)
https://zenodo.org/records/18145700
```

## License

Released for academic review and research purposes.

---

*Released in response to GitHub Issue #5 for algorithmic transparency.*
