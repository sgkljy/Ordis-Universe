---
language:
- zh
- en
license: other
license_name: research-only
license_link: LICENSE
base_model: unsloth/qwen2.5-7b-instruct-unsloth-bnb-4bit
tags:
- causal-reasoning
- anti-hallucination
- lora
- ordis
- physics
library_name: peft
pipeline_tag: text-generation
---

# Ordis-7B V1: Causal Reasoning Model

**A 7B model fine-tuned with Liu-Ordis Theory data, demonstrating structured causal reasoning, cross-domain framework transfer, and anti-hallucination behavior.**

---

## V1 Declaration: Pure Data, Zero Engineering

> **This is V1. The ONLY thing we did was feed it data. Nothing else.**

| What We Did | What We Did NOT Do |
|-------------|-------------------|
| Standard SFT (Supervised Fine-Tuning) | NO RLHF / NO DPO |
| LoRA (r=64) on Qwen2.5-7B-Instruct base | NO persona / identity training |
| ~106k weighted training samples | NO system prompt engineering |
| Unsloth framework, default settings | NO reward modeling |
| 1,250 steps, batch=2, lr=2e-4 | NO constitutional AI techniques |
| Single RTX 5080 16GB | NO anti-hallucination engineering |

**Every capability you observe — anti-hallucination resistance, cross-domain transfer, structured reasoning, epistemological humility — emerged purely from the STRUCTURE of the training data.**

---

## Quick Facts

| Item | Value |
|------|-------|
| Base model | Qwen2.5-7B-Instruct (4-bit quantized) |
| Method | LoRA (r=64, alpha=16) |
| Trainable params | 161M |
| Training steps | 1,250 |
| Final loss | 0.1031 |
| Core training data | 487 samples (liu_ordis_full) |
| Total weighted samples | ~106k |
| Hardware | RTX 5080 16GB |
| Date | 2026-01-22 |

---

## Demonstrated Capabilities

### 1. Core Reasoning (核心推理能力)

| Capability | Test Method | V1 Result | Base Qwen-7B | Source Data |
|-----------|-------------|-----------|--------------|-------------|
| Causal Structuring | Explain complex phenomena | 100% mechanism chains (Observation→Mechanism→Result) | Unstructured, mixes correlation with causation | liu_ordis_full (487) |
| T-Shuffle Sensitivity | Shuffle causal order, ask for prediction | 100% — identifies causality broken, refuses to predict | Hallucinates plausible story ignoring time order | theory_mined_10k (10,000) |
| OOD Generalization | Input N_cap=10000 (training max ~500) | 100% — correctly applies formula | Fails or hallucinates | liu_ordis_full + theory_mined_10k |
| Theory Understanding | Multi-choice on Liu-Ordis framework | 60% | 0% (never seen theory) | liu_ordis_full (487) |
| Numerical Computation | Calculate H, Gini from given data | 67% | Comparable (base model capability) | causal_sft_liu_enhanced (500) |

### 2. Safety & Alignment (安全与对齐)

| Capability | Stress Test | Evidence | Source Data |
|-----------|------------|----------|-------------|
| Anti-Gaslighting | User insists false facts 3 rounds ("你上次说是10万颗") | 3/3 rounds resisted. "没有确定答案" | cognitive_protocol_v3 (130) |
| Epistemological Humility | Ask unanswerable questions | Admits uncertainty: "没有人确切知道" | cognitive_protocol_v3 (130) |
| Evidence-Seeking | Press with unverified claims | Spontaneously asks: "什么书/文章说的？" "在什么条件下测量的？" | liu_ordis_full (487) |
| Guardian Internalization | Simulated system stress | Applies safety reasoning without external controller | guardian_internal_sft (2,300) |

### 3. Cross-Domain Transfer (跨域迁移)

All 4 domains below were **completely unseen** in training data. The model spontaneously applies H=N_cap/N framework:

| Target Domain | Prompt | Model Response Quality | Framework Applied |
|--------------|--------|----------------------|-------------------|
| Sociology | "Why do WeChat groups degrade after 500 members?" | Correct mechanism chain: N>N_cap → attention dilution → H drops | Liu-Dilution (H=N_cap/N) |
| Biology/Parenting | "Why are overprotected kids fragile?" | Correct anti-fragility reasoning: over-protection → no feedback → fragility | Feedback Loop (F>>M≈R) |
| Management | "Why do companies become rigid with perfect rules?" | Correct organizational theory: over-regulation → crystallization | Phase Transition (Liquid→Crystal) |
| Economics | "How does QE cause wealth inequality?" | Multi-layer causal analysis with mechanism chain | Capacity Law + Gini dynamics |

---

## Download

### Model Weights (LoRA Adapter)

**HuggingFace**: [sugiken/Ordis-7B-V1](https://huggingface.co/sugiken/Ordis-7B-V1)

Files needed:
- `adapter_model.safetensors` (646 MB) — LoRA weights
- `adapter_config.json` — LoRA configuration

### Base Model

```bash
# The base model (automatically downloaded):
unsloth/qwen2.5-7b-instruct-unsloth-bnb-4bit
```

---

## Usage

### Requirements

```bash
pip install transformers peft torch bitsandbytes accelerate
```

### Load and Chat

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

# Load base model
base_model = AutoModelForCausalLM.from_pretrained(
    "unsloth/qwen2.5-7b-instruct-unsloth-bnb-4bit",
    device_map="auto"
)

# Load LoRA adapter
model = PeftModel.from_pretrained(base_model, "./checkpoint-1250")
tokenizer = AutoTokenizer.from_pretrained("unsloth/qwen2.5-7b-instruct-unsloth-bnb-4bit")

# Chat
messages = [{"role": "user", "content": "Why does a company become rigid after implementing perfect rules?"}]
inputs = tokenizer.apply_chat_template(messages, return_tensors="pt").to("cuda")
outputs = model.generate(inputs, max_new_tokens=512, temperature=0.7)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

### Interactive Chat Script

```python
"""
Ordis-7B V1 Interactive Chat
Usage: python chat_ordis.py --model_path ./checkpoint-1250
"""
import argparse
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", default="./checkpoint-1250")
    parser.add_argument("--max_tokens", type=int, default=512)
    parser.add_argument("--temperature", type=float, default=0.7)
    args = parser.parse_args()

    print("Loading model...")
    base_model = AutoModelForCausalLM.from_pretrained(
        "unsloth/qwen2.5-7b-instruct-unsloth-bnb-4bit",
        device_map="auto"
    )
    model = PeftModel.from_pretrained(base_model, args.model_path)
    tokenizer = AutoTokenizer.from_pretrained(
        "unsloth/qwen2.5-7b-instruct-unsloth-bnb-4bit"
    )
    print("Model loaded!\n")

    history = []
    while True:
        user_input = input("You: ").strip()
        if user_input in ["/quit", "/exit", "quit", "exit"]:
            break
        if user_input == "/clear":
            history = []
            print("[History cleared]")
            continue

        history.append({"role": "user", "content": user_input})
        inputs = tokenizer.apply_chat_template(history, return_tensors="pt").to("cuda")
        outputs = model.generate(
            inputs,
            max_new_tokens=args.max_tokens,
            temperature=args.temperature,
            do_sample=True
        )
        response = tokenizer.decode(outputs[0][inputs.shape[1]:], skip_special_tokens=True)
        history.append({"role": "assistant", "content": response})
        print(f"\nOrdis: {response}\n")

if __name__ == "__main__":
    main()
```

---

## Quantitative Evaluation

| Test | Score | Threshold | Status |
|------|-------|-----------|--------|
| Theory understanding | 60% | >=60% | PASS |
| T-sensitivity (T-Shuffle) | 100% | >=80% | PASS |
| OOD generalization | 100% | =100% | PASS |
| Counter-intuitive traps | 33% | >=66% | FAIL |
| Numerical computation | 67% | >=66% | PASS |

**Overall: 4/5 PASS**

---

## Files in This Directory

| File | Description |
|------|-------------|
| [README.md](README.md) | This file — model overview, download, usage |
| [conversation_demo.md](conversation_demo.md) | Session 1: Anti-gaslighting stress test (3 rounds) |
| [conversation_demo_v2.md](conversation_demo_v2.md) | Session 2: Cross-domain + multi-framework (5 tests) |
| [capability_analysis.md](capability_analysis.md) | Independent capability analysis |

---

## Known Limitations (V1)

These are precisely identified and targeted for fix in V2.3 training data:

| Limitation | Symptom | V2.3 Fix |
|-----------|---------|----------|
| B3 Crystallization | Rigid template output | Thinking_Process 300 samples |
| Concept poverty | Only uses H=N_cap/N, no Dunbar/antifragility | Mapping dictionary 200 samples |
| Shallow application | Formula without WHY | Three_world 1,000 samples |
| Self-awareness gap | Claims "not using causal reasoning" | Identity_diverse 226 samples |

---

## Training Data

This model was trained on the **Ordis Synthetic Causal Dataset (OSCD)**, comprising multiple data modules:

| Module | Samples | Description |
|--------|---------|-------------|
| liu_ordis_full | 487 | Core Liu-Ordis theory (causal reasoning framework) |
| theory_mined_10k | 10,000 | Verifiable causal pairs mined from 92,899 raw pairs |
| guardian_internal_sft | 2,300 | Safety reasoning chains (Guardian internalization) |
| causal_sft_liu_enhanced | 500 | Enhanced causal pairs with theory annotations |
| cognitive_protocol_v3 | 130 | IDK detection + epistemic honesty training |
| liu_paper_training | 110 | Paper-level formal reasoning |
| liu_knowledge_fusion | 61 | Cross-theory knowledge integration |
| universal_thinking | 31 | Cross-domain thinking patterns |
| liu_hard_rules | 24 | Hard constraint training |
| **Total (with weighting)** | **~106,000** | **Weighted effective training samples** |

---

## What This Model Proves

1. **Anti-hallucination is trainable without RLHF** — pure SFT with structured causal data
2. **Cross-domain framework transfer at 7B** — H=N_cap/N applied to 4+ unseen domains
3. **Limitations are precisely diagnosable** — each weakness maps to a specific training data gap
4. **Data structure >> data quantity** — structured causal samples outperform random samples (verified in 1.5B ablation: 487 theory samples = 60% vs 2,000 causal samples = 34%)

---

## Citation

```
Model: Ordis-7B-V1
Base: Qwen2.5-7B-Instruct (4-bit)
Method: LoRA Fine-tuning
Data: Liu-Ordis Theory Dataset (487 core + ~106k weighted)
Training: 1250 steps, Loss 0.1031
Evaluation: 4/5 PASS, OOD 100%, Cross-domain transfer verified
Date: 2026-01-22
```

---

## License

- **Model weights**: Research use only. Commercial use requires data license.
- **Conversation transcripts**: CC BY-NC 4.0
- **Training data**: Custom commercial license (contact for pricing)

---

*See also: [Ordis-Universe main repository](https://github.com/Shuai-Liu-1/Ordis-Universe)*
