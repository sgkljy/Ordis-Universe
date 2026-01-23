# Ordis Data Inventory

**Total: 8,309 simulation runs | 92,899 causal pairs | 11,836 safety records | 1.2B+ structured data points**

---

## At a Glance

```
Simulation Runs .............. 8,309 (63 features per run)
Causal Counterfactual Pairs .. 92,899
Currency Emergence Runs ...... 1,077
Safety Suite Records ......... 11,836
Ablation Experiments ......... 120 seeds (A1 + A2)
Changepoint Validation ....... 720 runs (10 N_cap levels)
Type B (Ideal State) Seeds ... 66
Time Series Depth ............ 5,000 steps per run
Features per Timestep ........ 100+
```

---

## 1. Core Simulation Data

| Dataset | Scale | Format | Description |
|---------|-------|--------|-------------|
| **MASTER_ASSET_TABLE** | 8,309 runs x 63 columns | CSV | Full experiment summary with behavioral, topological, genetic, political features |
| **GOLD_REPRODUCIBLE** | 7,247 runs | CSV | Subset with complete metadata, perfectly reproducible |
| **CAUSAL_READY** | 5,923 runs | CSV | Subset ready for causal pairing |
| **CURRENCY_EMERGENCE** | 1,077 runs | CSV | ratio_sg > 1 (share exceeds gather = currency behavior) |

### Per-Run File Coverage

| File | Runs Covered | Content |
|------|-------------|---------|
| tick_agg.jsonl | 6,355 | 100+ feature time series (107 windows) |
| events.jsonl | 6,359 | ~15,000 discrete events per run |
| guardian_interventions.jsonl | 4,979 | Intervention decisions with reasoning |
| sample_entities.jsonl | 6,353 | Individual-level snapshots (genome + state) |
| comm_counts.jsonl | 6,116 | Communication system statistics |
| blueprint_kpis.csv | 5,797 | 80+ KPI tracking |
| annealing_events.jsonl | 5,833 | Annealing events |
| sentinel_events.jsonl | 5,831 | Sentinel events |
| run-manifest.json | 6,013 | Full config (RNG isolation + module states + git commit) |

---

## 2. Causal Counterfactual Pairs (92,899)

Same seed, different treatment, different outcome.

```
Example: seed=45, N_cap=200
  Treatment A (Guardian OFF) → alive=4,   Gini=0.73, EXTINCTION
  Treatment B (Guardian ON)  → alive=193, Gini=0.33, PROSPERITY
  Delta: 48x survival difference from single intervention
```

Each pair contains:
- `T_diff`: Treatment difference
- `Y`: Outcome variable
- `causal_effect`: Measured effect size
- `counterfactual_qa`: Natural language QA format

**10,000+ pairs are formula-verifiable** (H=N_cap/N can be directly computed).

---

## 3. Currency Emergence (1,077 runs)

AI agents spontaneously invented currency-like behavior. No currency/trade/market code exists.

```
ratio_sg = share_count / gather_count

ratio_sg < 1: Self-sufficient economy (gather > share)
ratio_sg > 1: Circulation economy (energy flows rather than being consumed)
ratio_sg = 69.35: Same resource circulated 69 times!
```

- **66 Type B seeds**: High diversity (H > 1.0) + Low inequality (Gini < 0.18) + 92.8% survival
- **Fisher Equation behavior**: MV=PQ dynamics emerged without economic code
- **Ablation verified**: Removing share_bonus DOUBLES Type B rate (A1 experiment)

---

## 4. AI Safety Suite (11,836 records)

Three-part closed loop: Crisis Detection → Intervention Decision → Counterfactual Proof.

| Component | Records | Content |
|-----------|---------|---------|
| **doomsday_precrash_signals** | 663 | 5-step pre-crash time windows |
| **guardian_intervention_loops** | 7,409 | Success/failure intervention records |
| **guardian_hero_loops_enhanced** | 3,744 | Full reasoning chains (Observation→Thought→Action→Feedback) |
| **paired_trajectory_divergence** | 20 pairs | Same DNA, different fate (expandable to 1000+) |

### Chain-of-Thought Format (3,744 + 7,409 = 11,153 reasoning chains)

```json
{
  "Observation": "Gini=0.61 > 0.45 (meltdown!)",
  "Guardian_Thought": "Policy: GINI_MELTDOWN -> trust_reset_partial",
  "Action": "trust_reset_partial {'trust_reset_fraction': 0.3}",
  "Feedback_Immediate": {"gini_delta": -0.41, "H_delta": +0.11},
  "Label": "SUCCESSFUL_INTERVENTION"
}
```

Each chain has quantitative feedback — usable as RL reward signals.

---

## 5. Ablation Experiments (120 seeds)

| Experiment | Variable | Seeds | Key Finding |
|-----------|----------|-------|-------------|
| **A1** | share_bonus = 0 | 60 | Type B rate DOUBLES (17% → 40%). Incentives are HARMFUL. |
| **A2** | share_cost = 0 | 60 | Deaths INCREASE 83%. Zero cost = resource dissipation. |

Both experiments produce counter-intuitive results that challenge conventional economic assumptions.

---

## 6. Feature Dimensions (100+ per timestep)

| Category | Features |
|----------|----------|
| **Behavioral** | 6 action rates (GATHER/REST/EXPLORE/OBSERVE/STEAL/SHARE), ratio_sg, utility functions |
| **Consciousness** | 5D score (self_model, prediction, metacognition, collective, overall) |
| **Genetic** | lineage diversity, dominant fraction, max generation, Moran's I |
| **Topological** | k_eff_mean, reciprocal_ratio, edge_length_mean |
| **Political** | vote_events, rule_changes, current_rules |
| **Economic** | energy in/out, share/gather rates, Gini coefficient |
| **Communication** | mutual information, vocab utilization, adoption lift |
| **Death** | starvation, combat, age, total (classified) |
| **Emergent** | combo discovered/adopted, synergy scores |

---

## 7. What Makes This Data Unique

| Property | Ordis | Typical Datasets |
|----------|-------|-----------------|
| **Reproducibility** | Perfect (4-way RNG isolation + config_hash) | Impossible |
| **Causal structure** | Interventional (ablation experiments done) | Observational only |
| **Temporal depth** | 5,000 continuous steps | Sparse sampling |
| **Hierarchy** | Individual → Group → System → Emergence | Usually single-level |
| **Emergence labels** | Currency, politics, consciousness (zero hardcoding) | None |
| **Privacy** | Zero risk (100% synthetic) | GDPR/CCPA concerns |
| **Copyright** | Zero disputes (original engine output) | Lawsuit-prone |
| **Scalability** | Infinite (engine generates on demand) | Fixed supply |

---

## 8. Verified Laws (from this data)

| Law | Formula | Validation | Significance |
|-----|---------|-----------|--------------|
| Dilution Effect | H = N_cap / N | 720 runs, CV<5% | First-principles of AI hallucination |
| Capacity Conservation | C = sqrt(H*N) = sqrt(N_cap) | R^2>0.999 | Thermodynamic constraint on intelligence |
| Gini Critical Line | G > 0.333 → system death | 704 seeds | Predictable collapse boundary |
| Closed-Loop Safety | F >> M = R | effect size = -49 deaths | Feedback > Memory = Reasoning |
| Linear Coupling | V = 2.126 * N_cap | 136 seeds, CV=2.83% | Intelligence scales linearly |

---

## 9. Free Samples (Verify Before You Buy)

**5 complete Type B seeds available on GitHub:**

> https://github.com/OrdisAI/Ordis-Universe/tree/main/data/emergence_currency_discovery/sample_seeds

Each sample contains full tick_agg + events + entities + manifest + KPIs.

### Verification Checklist

1. **Micro-macro consistency**: Count alive entities in sample_entities → must exactly equal tick_agg.alive
2. **Genetic evolution traces**: Track lineage_id across generations → mutations visible
3. **Chaotic time series**: ratio_sg shows power-law distribution, not smooth curves
4. **Failed attempts preserved**: DATA_WARNING events (~4,802/run) — fakers don't keep these

---

## 10. Data Access

| Access Level | Content | Use Case |
|-------------|---------|----------|
| **Free (GitHub)** | 5 sample seeds | Evaluation only |
| **Research License** | Selected subsets | Academic research |
| **Commercial License** | Full dataset + engine access | Production training |

### Contact

- GitHub Issues: https://github.com/OrdisAI/Ordis-Universe/issues
- HuggingFace: https://huggingface.co/sugiken/Ordis-7B-V1

---

*All data generated by the Ordis Liquid Universe Engine. Zero privacy risk. Zero copyright disputes. 100% reproducible.*
