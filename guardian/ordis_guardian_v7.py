# -*- coding: utf-8 -*-
"""
Guardian V7: Dual-Loop Controller (Minimal Viable Version)
===========================================================
Dual-Loop Controller - Physical Loop + Behavioral Loop

Core improvements (vs V6):
  - Fast loop (Behavioral): Monitor SHARE/GATHER ratio, intervene before Q collapse
  - Slow loop (Physical): Maintain Q = sqrt(H * N) = 13.53

Key discovery source:
  - V6 postmortem: "Over-sharing collapse" (SHARE>90%, GATHER<5%)
  - Failed seed signals: ratio_sg > 2.0, share_rate > 0.70

Design constraints:
  - V7 is the final Guardian version
  - Minimal design, not too complex
  - Success criteria: Pass+15% or crash rate-50%

Author: Gemini + GPT-5.2 + Claude + Claude Code
Version: 7.0.0-dual-loop-minimal
Date: 2026-01-01

Released for academic review - GitHub Issue #5 (KeikaJames)
"""
import numpy as np
from dataclasses import dataclass
from typing import Optional, Dict, Any, Tuple
from collections import deque


# =============================================================================
# Version Constants
# =============================================================================
VERSION = "7.0.0-dual-loop-minimal"
VERSION_TAG = "V391"


@dataclass
class GuardianV7Config:
    """V7 Configuration Dataclass"""
    enabled: bool = True

    # Slow loop (Physical) - LOIC parameters
    Q_target: float = 13.53          # Liu's Capacity Constant (empirically validated)
    Q_tolerance: float = 0.05        # ±5%

    # Fast loop (Behavioral) - NEW!
    share_rate_danger: float = 0.70  # SHARE ratio > 70% triggers
    ratio_sg_danger: float = 2.0     # SHARE/GATHER > 2.0 triggers
    gather_rate_warning: float = 0.20  # GATHER < 20% warning

    # DND (Do Not Disturb) parameters
    dnd_gini_max: float = 0.28
    dnd_h_min: float = 0.90
    dnd_h_max: float = 1.35
    dnd_n_min: int = 140

    # Intervention parameters
    cooldown_steps: int = 100
    observe_steps: int = 50

    # AUSTERITY parameters (minimal version, only mild measures)
    share_bonus_delta: float = -0.2   # Reduce sharing incentive

    # STIMULATE parameters
    stimulate_regen_boost: float = 0.1


class OrdisGuardianV7:
    """
    Guardian V7: Dual-Loop Controller

    Architecture:
        Fast loop (Behavioral): Monitor share_rate / gather_rate
            - Higher priority than physical loop
            - Detect "over-sharing collapse" precursors
            - Trigger: ratio_sg > 2.0 or share_rate > 0.70

        Slow loop (Physical): Monitor Q = sqrt(H * N)
            - Only STIMULATE when behavior is healthy
            - Target Q = 13.53 (natural comfort zone)

    Intervention types:
        AUSTERITY: Behavior correction (reduce share_bonus)
        STIMULATE: Resource injection (increase regen, only when behavior healthy)
        COOL_DOWN: Overheating reduction (reduce std)
        DO_NOTHING: Do not disturb

    IMPORTANT: This controller does NOT directly kill agents or force behaviors.
    It only adjusts environmental parameters and incentive signals.
    """

    VERSION = VERSION

    def __init__(self, config: Optional[Dict] = None):
        """Initialize Guardian V7"""
        config = config or {}

        # Parse configuration
        if isinstance(config, dict):
            self.enabled = config.get('enabled', True)
            self.Q_target = config.get('Q_target', 13.53)
            self.Q_tolerance = config.get('Q_tolerance', 0.05)
            self.share_rate_danger = config.get('share_rate_danger', 0.70)
            self.ratio_sg_danger = config.get('ratio_sg_danger', 2.0)
            self.gather_rate_warning = config.get('gather_rate_warning', 0.20)
            self.dnd_gini_max = config.get('dnd_gini_max', 0.28)
            self.dnd_h_min = config.get('dnd_h_min', 0.90)
            self.dnd_h_max = config.get('dnd_h_max', 1.35)
            self.dnd_n_min = config.get('dnd_n_min', 140)
            self.cooldown_steps = config.get('cooldown_steps', 100)
            self.share_bonus_delta = config.get('share_bonus_delta', -0.2)
            self.stimulate_regen_boost = config.get('stimulate_regen_boost', 0.1)
        else:
            # Use defaults
            cfg = GuardianV7Config()
            self.enabled = cfg.enabled
            self.Q_target = cfg.Q_target
            self.Q_tolerance = cfg.Q_tolerance
            self.share_rate_danger = cfg.share_rate_danger
            self.ratio_sg_danger = cfg.ratio_sg_danger
            self.gather_rate_warning = cfg.gather_rate_warning
            self.dnd_gini_max = cfg.dnd_gini_max
            self.dnd_h_min = cfg.dnd_h_min
            self.dnd_h_max = cfg.dnd_h_max
            self.dnd_n_min = cfg.dnd_n_min
            self.cooldown_steps = cfg.cooldown_steps
            self.share_bonus_delta = cfg.share_bonus_delta
            self.stimulate_regen_boost = cfg.stimulate_regen_boost

        # State tracking
        self.cooldown_timer = 0
        self.last_action = None
        self.behavior_history = deque(maxlen=10)

        # Statistics
        self.stats = {
            'interventions': 0,
            'austerity_count': 0,
            'stimulate_count': 0,
            'cooldown_count': 0,
            'behavior_triggers': 0,  # Behavioral loop trigger count
            'physics_triggers': 0,   # Physical loop trigger count
        }

    def check_and_act(self, metrics: Dict[str, Any]) -> Tuple[Optional[str], float, Dict]:
        """
        Dual-loop detection and decision

        Args:
            metrics: State metrics dictionary, must contain:
                - alive: Number of surviving agents
                - shannon_H_mean or H: Entropy
                - gini_mean or gini: Inequality index
                - share_rate: SHARE action ratio (required!)
                - gather_rate: GATHER action ratio (required!)

        Returns:
            (action, magnitude, signals)
            action: 'AUSTERITY' | 'STIMULATE' | 'COOL_DOWN' | None
            magnitude: Intervention strength 0-1
            signals: Diagnostic information dictionary
        """
        if not self.enabled:
            return None, 0.0, {'diagnosis': 'disabled'}

        # Extract metrics
        alive = metrics.get('alive', 0)
        H = metrics.get('shannon_H_mean', metrics.get('H', 0))
        gini = metrics.get('gini_mean', metrics.get('gini', 0))
        share_rate = metrics.get('share_rate', 0)
        gather_rate = metrics.get('gather_rate', 0)

        # Calculate behavior ratio
        ratio_sg = share_rate / max(gather_rate, 0.01)

        # Calculate Q value
        Q = np.sqrt(H * alive) if alive > 0 and H > 0 else 0
        Q_dev = (Q - self.Q_target) / self.Q_target if self.Q_target > 0 else 0

        # Build signal dictionary
        signals = {
            'Q_val': Q,
            'Q_target': self.Q_target,
            'Q_dev': Q_dev,
            'share_rate': share_rate,
            'gather_rate': gather_rate,
            'ratio_sg': ratio_sg,
            'H': H,
            'gini': gini,
            'alive': alive,
        }

        # Cooldown check (all interventions share cooldown)
        if self.cooldown_timer > 0:
            self.cooldown_timer -= 1
            signals['diagnosis'] = f'cooldown ({self.cooldown_timer} steps left)'
            return None, 0.0, signals

        # =========================================
        # FAST LOOP (Behavioral) - Bypasses DND!
        # Pathological behavior must be corrected immediately
        # =========================================
        behavior_pathological = (
            ratio_sg > self.ratio_sg_danger or
            share_rate > self.share_rate_danger
        )

        if behavior_pathological:
            # Pathological behavior → AUSTERITY (bypass DND, regardless of Q)
            self.stats['behavior_triggers'] += 1
            signals['diagnosis'] = f'BEHAVIOR_PATHOLOGICAL (ratio={ratio_sg:.2f}, share={share_rate:.2f}, bypass_DND=True)'
            return self._do_austerity(signals)

        # DND check (only applies to physical loop)
        if self._is_do_not_disturb(H, gini, alive):
            signals['diagnosis'] = 'DND (healthy, behavior_ok)'
            return None, 0.0, signals

        # =========================================
        # SLOW LOOP (Physical) - Only when behavior healthy and not DND
        # =========================================
        self.stats['physics_triggers'] += 1

        # Q too low → STIMULATE (because behavior is healthy, can boost)
        if Q_dev < -self.Q_tolerance:
            signals['diagnosis'] = f'Q_LOW (Q={Q:.2f}, dev={Q_dev:.2%})'
            return self._do_stimulate(signals)

        # Q too high → COOL_DOWN
        if Q_dev > self.Q_tolerance * 2:  # More lenient overheat threshold
            signals['diagnosis'] = f'Q_HIGH (Q={Q:.2f}, dev={Q_dev:.2%})'
            return self._do_cooldown(signals)

        # Q normal → no intervention
        signals['diagnosis'] = 'NORMAL'
        return None, 0.0, signals

    def _is_do_not_disturb(self, H: float, gini: float, alive: int) -> bool:
        """Check if in Do Not Disturb zone"""
        return (
            gini < self.dnd_gini_max and
            self.dnd_h_min <= H <= self.dnd_h_max and
            alive >= self.dnd_n_min
        )

    def _do_austerity(self, signals: Dict) -> Tuple[str, float, Dict]:
        """Execute AUSTERITY intervention (behavior correction)"""
        self.stats['interventions'] += 1
        self.stats['austerity_count'] += 1
        self.cooldown_timer = self.cooldown_steps
        self.last_action = 'AUSTERITY'

        signals['action'] = 'AUSTERITY'
        signals['share_bonus_delta'] = self.share_bonus_delta

        return 'AUSTERITY', 0.5, signals

    def _do_stimulate(self, signals: Dict) -> Tuple[str, float, Dict]:
        """Execute STIMULATE intervention (resource injection)"""
        self.stats['interventions'] += 1
        self.stats['stimulate_count'] += 1
        self.cooldown_timer = self.cooldown_steps
        self.last_action = 'STIMULATE'

        signals['action'] = 'STIMULATE'
        signals['regen_boost'] = self.stimulate_regen_boost

        return 'STIMULATE', 0.3, signals

    def _do_cooldown(self, signals: Dict) -> Tuple[str, float, Dict]:
        """Execute COOL_DOWN intervention (overheating reduction)"""
        self.stats['interventions'] += 1
        self.stats['cooldown_count'] += 1
        self.cooldown_timer = self.cooldown_steps
        self.last_action = 'COOL_DOWN'

        signals['action'] = 'COOL_DOWN'

        return 'COOL_DOWN', 0.2, signals

    def get_stats(self) -> Dict:
        """Get statistics"""
        return {
            **self.stats,
            'version': self.VERSION,
            'Q_target': self.Q_target,
            'share_rate_danger': self.share_rate_danger,
            'ratio_sg_danger': self.ratio_sg_danger,
        }


# =============================================================================
# Test Code
# =============================================================================
if __name__ == '__main__':
    print(f"Guardian V7 Version: {VERSION}")
    print(f"Version Tag: {VERSION_TAG}")
    print()

    guardian = OrdisGuardianV7()

    # Test 1: Healthy state
    metrics_healthy = {
        'alive': 180,
        'H': 1.05,
        'gini': 0.25,
        'share_rate': 0.35,
        'gather_rate': 0.45,
    }
    action, mag, signals = guardian.check_and_act(metrics_healthy)
    print(f"[Healthy] Action: {action}, Diagnosis: {signals['diagnosis']}")
    print(f"  Q={signals['Q_val']:.2f}, ratio_sg={signals['ratio_sg']:.2f}")

    # Test 2: Over-sharing collapse
    metrics_over_share = {
        'alive': 150,
        'H': 0.80,
        'gini': 0.50,
        'share_rate': 0.85,  # Dangerous!
        'gather_rate': 0.05,  # Almost no one gathering!
    }
    guardian.cooldown_timer = 0  # Reset cooldown
    action, mag, signals = guardian.check_and_act(metrics_over_share)
    print(f"\n[Over-Share] Action: {action}, Diagnosis: {signals['diagnosis']}")
    print(f"  Q={signals['Q_val']:.2f}, ratio_sg={signals['ratio_sg']:.2f}")

    # Test 3: Q low but behavior healthy
    metrics_q_low = {
        'alive': 100,
        'H': 0.90,
        'gini': 0.35,
        'share_rate': 0.30,
        'gather_rate': 0.50,
    }
    guardian.cooldown_timer = 0
    action, mag, signals = guardian.check_and_act(metrics_q_low)
    print(f"\n[Q Low] Action: {action}, Diagnosis: {signals['diagnosis']}")
    print(f"  Q={signals['Q_val']:.2f}, ratio_sg={signals['ratio_sg']:.2f}")

    # Print stats
    print(f"\n[Stats] {guardian.get_stats()}")
