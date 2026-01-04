# Guardian V7 Pseudocode
## Dual-Loop Controller for Multi-Agent System Homeostasis

**Version**: 7.0.0
**Purpose**: Maintain system health by monitoring behavioral and physical signals
**Key Insight**: Over-sharing collapse can occur even when physical metrics appear healthy

---

## 1. Core Constants

```
Q_TARGET      = 13.53    # Liu's Capacity Constant: √(H × N)
Q_TOLERANCE   = 0.05     # ±5% deviation threshold

# Behavioral thresholds (Fast Loop)
SHARE_RATE_DANGER = 0.70   # SHARE action ratio > 70% triggers intervention
RATIO_SG_DANGER   = 2.0    # SHARE/GATHER ratio > 2.0 triggers intervention

# Do-Not-Disturb zone (Healthy state)
DND_GINI_MAX = 0.28
DND_H_MIN    = 0.90
DND_H_MAX    = 1.35
DND_N_MIN    = 140

COOLDOWN_STEPS = 100  # Minimum steps between interventions
```

---

## 2. Main Algorithm

```
FUNCTION check_and_act(metrics):
    INPUT:
        metrics.alive       : int    # Number of surviving agents
        metrics.H           : float  # Shannon entropy of behavior distribution
        metrics.gini        : float  # Gini coefficient of resource distribution
        metrics.share_rate  : float  # Fraction of agents performing SHARE action
        metrics.gather_rate : float  # Fraction of agents performing GATHER action

    OUTPUT:
        action    : string  # 'AUSTERITY' | 'STIMULATE' | 'COOL_DOWN' | None
        magnitude : float   # Intervention strength [0, 1]
        signals   : dict    # Diagnostic information

    # Step 0: Check cooldown
    IF cooldown_timer > 0:
        cooldown_timer -= 1
        RETURN (None, 0.0, "in cooldown")

    # Step 1: Compute derived metrics
    ratio_sg = share_rate / max(gather_rate, 0.01)
    Q = sqrt(H * alive)
    Q_deviation = (Q - Q_TARGET) / Q_TARGET

    # =========================================
    # FAST LOOP (Behavioral) - HIGHEST PRIORITY
    # Bypasses DND check! Pathological behavior
    # must be corrected immediately.
    # =========================================

    # Step 2: Check for behavioral pathology
    behavior_pathological = (ratio_sg > RATIO_SG_DANGER) OR
                           (share_rate > SHARE_RATE_DANGER)

    IF behavior_pathological:
        # Over-sharing detected → AUSTERITY intervention
        # This triggers EVEN IF system looks healthy!
        RETURN do_austerity()

    # =========================================
    # DND CHECK (Only for physical loop)
    # =========================================

    # Step 3: Check if system is in healthy "Do Not Disturb" zone
    in_dnd_zone = (gini < DND_GINI_MAX) AND
                  (DND_H_MIN <= H <= DND_H_MAX) AND
                  (alive >= DND_N_MIN)

    IF in_dnd_zone:
        RETURN (None, 0.0, "healthy, no intervention needed")

    # =========================================
    # SLOW LOOP (Physical) - Q-value regulation
    # Only reaches here if behavior is healthy
    # =========================================

    # Step 4: Q-value too low → System needs stimulation
    IF Q_deviation < -Q_TOLERANCE:
        RETURN do_stimulate()

    # Step 5: Q-value too high → System overheating
    IF Q_deviation > Q_TOLERANCE * 2:
        RETURN do_cooldown()

    # Step 6: Everything normal
    RETURN (None, 0.0, "normal operation")
```

---

## 3. Intervention Functions

```
FUNCTION do_austerity():
    """
    Behavioral correction: Reduce over-sharing incentive

    MECHANISM:
        - Decrease share_bonus by 0.2
        - This reduces the utility gain from SHARE action
        - Agents naturally shift toward GATHER

    NOTE: Does NOT kill agents or force behavior changes.
          Only adjusts incentive parameters.
    """
    cooldown_timer = COOLDOWN_STEPS
    RETURN ('AUSTERITY', 0.5, {share_bonus_delta: -0.2})


FUNCTION do_stimulate():
    """
    Resource injection: Help struggling system recover

    MECHANISM:
        - Increase resource_regen by 0.1
        - More resources available in environment
        - Only triggers when behavior is healthy but Q is low

    NOTE: Does NOT directly modify agent states.
          Only adjusts environmental parameters.
    """
    cooldown_timer = COOLDOWN_STEPS
    RETURN ('STIMULATE', 0.3, {regen_boost: 0.1})


FUNCTION do_cooldown():
    """
    Overheating correction: Dampen excessive activity

    MECHANISM:
        - Reduce environmental stimulation
        - Allow system to naturally settle

    NOTE: Passive intervention, no direct agent manipulation.
    """
    cooldown_timer = COOLDOWN_STEPS
    RETURN ('COOL_DOWN', 0.2, {})
```

---

## 4. Key Design Principles

### 4.1 No Direct Agent Manipulation
Guardian V7 **never**:
- Kills agents (`if entropy > x then kill agent`)
- Forces specific behaviors
- Directly modifies agent internal states

Guardian V7 **only**:
- Adjusts environmental parameters (resource regen)
- Modifies incentive signals (share_bonus)
- These changes propagate through agent decision-making naturally

### 4.2 Dual-Loop Priority
```
Fast Loop (Behavioral) > DND Check > Slow Loop (Physical)
```

The behavioral loop can bypass the "Do Not Disturb" check because:
- Over-sharing collapse can occur even when H, N, Gini look healthy
- By the time physical metrics degrade, it's often too late

### 4.3 Cooldown Mechanism
- All interventions share a 100-step cooldown
- Prevents oscillation and over-correction
- Allows system to respond naturally to each intervention

---

## 5. Empirical Validation

| Metric | V7 OFF | V7 ON | Change |
|--------|--------|-------|--------|
| Pass Rate | 5% | 45% | +40pp |
| Avg Alive | 102.7 | 175.6 | +71% |
| Behavior Triggers | - | 49 | - |
| Physics Triggers | - | 7 | - |

**Observation**: Most interventions (49/56 = 88%) are behavioral (AUSTERITY),
confirming that over-sharing is the primary failure mode.

---

## 6. Source Code Reference

Full implementation: `ordis_guardian_v7.py`
Lines: 343 (including tests and documentation)
Dependencies: numpy, dataclasses, typing, collections

---

*Document generated: 2026-01-04*
*For academic review in response to GitHub Issue #5 (KeikaJames)*
