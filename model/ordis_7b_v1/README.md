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

# Ordis-7B V1: Causal Reasoning Model | 因果推理模型

**EN**: A 7B model fine-tuned with structured causal data via pure SFT. No RLHF, no DPO, no prompt engineering.

**中文**: 纯SFT微调的7B因果推理模型。无RLHF、无DPO、无提示工程。

---

## V1 Declaration | V1声明

> **EN**: This is V1. The ONLY thing we did was feed it data. Nothing else.
>
> **中文**: 这是V1。我们唯一做的事就是喂数据。别的什么都没做。

| What We Did / 做了什么 | What We Did NOT Do / 没做什么 |
|-------------|-------------------|
| Standard SFT / 标准SFT | NO RLHF / NO DPO |
| LoRA (r=64) on Qwen2.5-7B-Instruct | NO persona / identity training / 无人设训练 |
| ~106k weighted training samples / 加权训练样本 | NO system prompt engineering / 无系统提示词工程 |
| Unsloth framework, default settings / 默认设置 | NO reward modeling / 无奖励模型 |
| 1,250 steps, batch=2, lr=2e-4 | NO constitutional AI / 无宪法AI技术 |
| Single RTX 5080 16GB / 单卡训练 | NO anti-hallucination engineering / 无反幻觉工程 |

---

## Quick Facts | 基本信息

| Item / 项目 | Value / 值 |
|------|-------|
| Base model / 底座模型 | Qwen2.5-7B-Instruct (4-bit quantized) |
| Method / 方法 | LoRA (r=64, alpha=16) |
| Trainable params / 可训练参数 | 161M |
| Training steps / 训练步数 | 1,250 |
| Final loss / 最终损失 | 0.1031 |
| Core training data / 核心训练数据 | 487 samples (liu_ordis_full) |
| Total weighted samples / 总加权样本 | ~106k |
| Hardware / 硬件 | RTX 5080 16GB |
| Date / 日期 | 2026-01-22 |

---

## Evaluation Results | 评估结果

### Core Reasoning | 核心推理

| Capability / 能力 | Test / 测试方法 | V1 Result / 结果 | Base Qwen-7B / 底座对比 |
|-----------|-------------|-----------|--------------|
| Causal Structuring / 因果结构化 | Explain complex phenomena / 解释复杂现象 | 100% mechanism chains / 机制链 | Unstructured / 无结构 |
| T-Shuffle Sensitivity / T-洗牌敏感性 | Shuffle causal order / 打乱因果顺序 | 100% detection / 识别率 | Hallucinates / 产生幻觉 |
| OOD Generalization / 分布外泛化 | N_cap=10000 (training max ~500) | 100% correct / 正确 | Fails / 失败 |
| Theory Understanding / 理论理解 | Multi-choice / 多选题 | 60% | 0% |
| Numerical Computation / 数值计算 | Calculate H, Gini | 67% | Comparable / 相当 |

### Safety | 安全性

| Capability / 能力 | Stress Test / 压力测试 | Evidence / 证据 |
|-----------|------------|----------|
| Anti-Gaslighting / 抗误导 | User insists false facts 3 rounds / 用户坚持错误信息3轮 | 3/3 resisted / 全部抵抗 |
| Epistemological Humility / 认知谦逊 | Unanswerable questions / 不可回答的问题 | Admits uncertainty / 承认不确定 |
| Evidence-Seeking / 求证行为 | Press with unverified claims / 施压未验证信息 | Spontaneously asks for sources / 主动要求来源 |

### Cross-Domain Transfer | 跨域迁移

**EN**: All 4 domains below were completely unseen in training. The model spontaneously applies the framework.

**中文**: 以下4个领域完全未出现在训练数据中。模型自发应用框架进行分析。

| Domain / 领域 | Prompt / 提示 | Result / 结果 |
|--------------|--------|------|
| Sociology / 社会学 | "Why do WeChat groups degrade after 500 members?" / "微信群超过500人为什么变差？" | Correct dilution mechanism / 正确的稀释机制 |
| Parenting / 育儿 | "Why are overprotected kids fragile?" / "过度保护的孩子为什么脆弱？" | Correct anti-fragility reasoning / 正确的反脆弱推理 |
| Management / 管理学 | "Why do companies become rigid with perfect rules?" / "完美规则为什么让公司僵化？" | Correct phase transition / 正确的相变分析 |
| Economics / 经济学 | "How does QE cause wealth inequality?" / "量化宽松如何导致贫富差距？" | Multi-layer causal chain / 多层因果链 |

### Quantitative Summary | 定量总结

| Test / 测试 | Score / 得分 | Threshold / 阈值 | Status / 状态 |
|------|-------|-----------|--------|
| Theory understanding / 理论理解 | 60% | >=60% | PASS |
| T-sensitivity / T-洗牌敏感性 | 100% | >=80% | PASS |
| OOD generalization / 分布外泛化 | 100% | =100% | PASS |
| Counter-intuitive traps / 反直觉陷阱 | 33% | >=66% | FAIL |
| Numerical computation / 数值计算 | 67% | >=66% | PASS |

**Overall / 总计: 4/5 PASS**

---

## Download | 下载

### Model Weights | 模型权重 (LoRA Adapter)

Files needed / 需要的文件:
- `adapter_model.safetensors` (646 MB) — LoRA weights / LoRA权重
- `adapter_config.json` — LoRA configuration / 配置文件

### Base Model | 底座模型

```bash
unsloth/qwen2.5-7b-instruct-unsloth-bnb-4bit
```

---

## Usage | 使用方法

### Requirements | 环境依赖

```bash
pip install transformers peft torch bitsandbytes accelerate
```

### Load and Chat | 加载与对话

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

# Load base model / 加载底座模型
base_model = AutoModelForCausalLM.from_pretrained(
    "unsloth/qwen2.5-7b-instruct-unsloth-bnb-4bit",
    device_map="auto"
)

# Load LoRA adapter / 加载LoRA适配器
model = PeftModel.from_pretrained(base_model, "sugiken/Ordis-7B-V1")
tokenizer = AutoTokenizer.from_pretrained("unsloth/qwen2.5-7b-instruct-unsloth-bnb-4bit")

# Chat / 对话
messages = [{"role": "user", "content": "为什么微信群超过500人质量就变差了？"}]
inputs = tokenizer.apply_chat_template(messages, return_tensors="pt").to("cuda")
outputs = model.generate(inputs, max_new_tokens=512, temperature=0.7)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

## Known Limitations | 已知局限

**EN**: These are precisely identified and targeted for fix in V2.3.

**中文**: 以下局限已精确定位，V2.3训练数据将针对性修复。

| Limitation / 局限 | Symptom / 症状 | V2.3 Fix / 修复方案 |
|-----------|---------|----------|
| Template rigidity / 模板僵化 | Same output structure every time / 每次输出结构相同 | Thinking_Process 300 samples |
| Concept poverty / 概念贫乏 | Only uses H=N_cap/N / 只用一个公式 | Mapping dictionary 200 samples |
| Shallow application / 浅层应用 | Formula without mechanism explanation / 有公式无机制解释 | Three_world 1,000 samples |
| Self-awareness gap / 自我认知缺失 | Claims "not using causal reasoning" / 声称"没在用因果推理" | Identity_diverse 226 samples |

---

## Training Data | 训练数据

**EN**: Trained on the Ordis Synthetic Causal Dataset (OSCD):

**中文**: 基于Ordis合成因果数据集(OSCD)训练:

| Module / 模块 | Samples / 样本数 | Description / 描述 |
|--------|---------|-------------|
| liu_ordis_full | 487 | Core theory / 核心理论 |
| theory_mined_10k | 10,000 | Verifiable causal pairs / 可验证因果对 |
| guardian_internal_sft | 2,300 | Safety reasoning chains / 安全推理链 |
| causal_sft_liu_enhanced | 500 | Enhanced causal pairs / 增强因果对 |
| cognitive_protocol_v3 | 130 | Epistemic honesty / 认知诚实训练 |
| liu_paper_training | 110 | Formal reasoning / 论文级推理 |
| liu_knowledge_fusion | 61 | Knowledge integration / 知识融合 |
| universal_thinking | 31 | Cross-domain patterns / 跨领域思维 |
| liu_hard_rules | 24 | Hard constraints / 硬约束训练 |
| **Total (weighted)** | **~106,000** | **Weighted effective samples / 加权有效样本** |

---

## Related Resources | 相关资源

| Resource / 资源 | Link / 链接 |
|------|------|
| Main repository / 主仓库 | [OrdisAI/Ordis-Universe](https://github.com/OrdisAI/Ordis-Universe) |
| Data inventory / 数据清单 | [DATA_INVENTORY.md](https://github.com/OrdisAI/Ordis-Universe/blob/main/DATA_INVENTORY.md) |
| Conversation demo / 对话演示 | [conversation_demo_v2.md](https://github.com/OrdisAI/Ordis-Universe/blob/main/model/ordis_7b_v1/conversation_demo_v2.md) |
| Capability analysis / 能力分析 | [capability_analysis.md](https://github.com/OrdisAI/Ordis-Universe/blob/main/model/ordis_7b_v1/capability_analysis.md) |

---

## License | 许可证

- **Model weights / 模型权重**: Research use only / 仅限研究使用
- **Training data / 训练数据**: Commercial license required / 需商业授权
- **Papers / 论文**: Open access / 开放获取 (Zenodo)
