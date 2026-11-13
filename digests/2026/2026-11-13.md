# AI 前沿雷达 · 2026-11-13

> 扫描 **1773** 条 → 入选 **17** 条 ｜ 关注名单命中 **8** 位研究者 ｜ 生成于 2026-11-13 03:18 UTC

**今日分布**：🧠 大模型 / LLM (4) ｜ 🤖 智能体 / Agent (4) ｜ 🧰 Harness / 基建与评测 (1) ｜ 🦾 VLA / 视觉-语言-动作 (4) ｜ 🎯 强化学习 / 持续学习 (3) ｜ 🛡️ 安全 / 对齐 / 可解释 (1)


## ⭐ 今日必读

1. **[Evolving Infra: Agent-Adaptive LLM Serving at Scale](https://arxiv.org/abs/2611.12304)**
   Agentic workloads are a major source of LLM inference demand. Existing prefill--decode (PD) disaggregated serving systems offer limited flexibility for runtime adaptation of compu…
   <sub>👤 **Ion Stoica · UC Berkeley / Song Han · MIT / NVIDIA** | 🔥 10 | HF Papers · 4 天前</sub>

2. **[Learning Low-Latency Action Verification for Frozen Vision-Language-Action Models](https://arxiv.org/abs/2611.14834)**
   Vision-language-action (VLA) models have made significant progress in general-purpose robotic manipulation. However, sampled action sequences can be ineffective, while evaluating…
   <sub>👤 **Trevor Darrell · UC Berkeley** | arXiv · 2 天前</sub>

3. **[ActionCodec2: A Streaming Action Tokenizer](https://arxiv.org/abs/2611.15490)**
   Most action tokenizers for autoregressive vision language action (VLA) models compress motion into chunks that must be decoded in full before their actions become executable. We i…
   <sub>👤 **Hang Zhao · Tsinghua** | arXiv · 昨天</sub>

4. **[Generalized Inverse Kinematics via Conditional Flow](https://arxiv.org/abs/2611.15565)**
   Inverse kinematics (IK) is a foundational primitive in robotics, mapping the task-space objectives expressed by higher-level planners to robot configurations that realize them. Tr…
   <sub>👤 **Leslie Pack Kaelbling · MIT** | arXiv · 昨天</sub>

5. **[When Is Proof-Step Verification Worth Its Cost? Operating Requirements of Certify-or-Decline Verification for Open-Weight Mathematical Reasoning](https://arxiv.org/abs/2611.14794)**
   Proof-step verification rewrites a solver's answer into typed steps and uses LLM judges to certify or decline. We evaluate this pipeline on open-weight models across GPQA, AIME-20…
   <sub>👤 **Abhinav Gupta · CMU** | arXiv · 2 天前</sub>

6. **[Observations Drift, Structures Remain: Structural Pretraining with Time Alignment for Electromagnetic Signals](https://arxiv.org/abs/2611.15566)**
   Electromagnetic signal modeling is increasingly moving toward self-supervised pretraining on heterogeneous I/Q observations. However, an observed waveform is jointly shaped by sig…
   <sub>👤 **Maosong Sun · Tsinghua** | arXiv · 昨天</sub>

7. **[Expanding the Decision Space of Pretrained Models through Structured Re-Decoding](https://arxiv.org/abs/2611.15109)**
   Native decoders limit how pretrained models combine local predictions under new structural constraints. We introduce Structured Re-Decoding (SRD), a training-free framework that c…
   <sub>👤 **Chi Wang · Google DeepMind** | arXiv · 昨天</sub>

8. **[Towards Robust Vision-Language Reasoning: A Multi-Stage Optimization Pipeline with Masked Diffusion Model](https://arxiv.org/abs/2611.15238)**
   Discrete diffusion generation is emerging as a competitive alternative to autoregressive generation by denoising the entire token sequence through iterative refinement. Its global…
   <sub>💡 towards | arXiv · 昨天</sub>

9. **[What Makes a VLA Reactive? A Study of Execution Strategies for Dynamic Manipulation](https://arxiv.org/abs/2611.15491)**
   Vision-language-action (VLA) models predict chunks of future actions, and when objects move, those chunks go stale before they are executed. We study what makes a pretrained VLA r…
   <sub>💡 想法型 | arXiv · 昨天</sub>

10. **[How Amplitude ships product improvements in 1–2 days with OpenAI](https://openai.com/business/customer-stories/amplitude)**
   Built primarily on OpenAI models, Amplitude’s proactive product agent, Wave, identifies what to build, helps teams ship changes with coding agents, and measures the impact.
   <sub>🏛 OpenAI | 💡 想法型 | Blog · 今天</sub>


---


## 🧠 大模型 / LLM

- **[When Is Proof-Step Verification Worth Its Cost? Operating Requirements of Certify-or-Decline Verification for Open-Weight Mathematical Reasoning](https://arxiv.org/abs/2611.14794)**
  Proof-step verification rewrites a solver's answer into typed steps and uses LLM judges to certify or decline. We evaluate this pipeline on open-weight models across GPQA, AIME-20…
  <sub>👤 **Abhinav Gupta · CMU** | arXiv · 2 天前</sub>

- **[Towards Robust Vision-Language Reasoning: A Multi-Stage Optimization Pipeline with Masked Diffusion Model](https://arxiv.org/abs/2611.15238)**
  Discrete diffusion generation is emerging as a competitive alternative to autoregressive generation by denoising the entire token sequence through iterative refinement. Its global…
  <sub>💡 towards | arXiv · 昨天</sub>

- **[Incentivizing Self-Learning in Large Language Models via Reinforcement Learning](https://arxiv.org/abs/2610.39671)**
  Large language models (LLMs) draw on parametric knowledge and retrieval-augmented generation (RAG) to solve knowledge-intensive tasks. Yet problem solving in unfamiliar domains ca…
  <sub>🔥 28 | HF Papers · 15 天前</sub>

- **[Incentive-Responsive Agents: A Principal-Agent Framework, Metric Suite, and Runtime Architecture for Long-Lived Personal AI Agents](https://arxiv.org/abs/2611.15515)**
  Personal AI agents now persist: they hold accounts, mailboxes, long-term memory, and open-ended task streams, yet the dominant way to improve them remains capability-side: prompt…
  <sub>💡 we argue | arXiv · 昨天</sub>


## 🤖 智能体 / Agent

- **[How Amplitude ships product improvements in 1–2 days with OpenAI](https://openai.com/business/customer-stories/amplitude)**
  Built primarily on OpenAI models, Amplitude’s proactive product agent, Wave, identifies what to build, helps teams ship changes with coding agents, and measures the impact.
  <sub>🏛 OpenAI | 💡 想法型 | Blog · 今天</sub>

- **[DecArena: Evaluating Large-Scale Decentralized Multi-Agent Collaboration](https://arxiv.org/abs/2611.15521)**
  Emerging personal AI agents raise fundamental scalability and privacy concerns for centralized multi-agent systems (MASs), which rely on a global orchestrator with broad access to…
  <sub>arXiv · 昨天</sub>

- **[Microsoft Research Focus – Edition #98](https://www.microsoft.com/en-us/research/podcast/microsoft-research-focus-edition-98/)**
  What&#8217;s new in research? &nbsp; In this edition of Microsoft Research Focus , based on the Research Focus newsletter (opens in new tab) , host Anson Ho shares some of the lat…
  <sub>🏛 Microsoft Research | Blog · 今天</sub>

- **[SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering](https://arxiv.org/abs/2611.13410)**
  Low-bit quantization reduces the inference cost of LLM agents but can compromise task success. Examining failed rollouts, we find that quantized agents overlook task requirements…
  <sub>🔥 32 | HF Papers · 3 天前</sub>


## 🧰 Harness / 基建与评测

- **[Evolving Infra: Agent-Adaptive LLM Serving at Scale](https://arxiv.org/abs/2611.12304)**
  Agentic workloads are a major source of LLM inference demand. Existing prefill--decode (PD) disaggregated serving systems offer limited flexibility for runtime adaptation of compu…
  <sub>👤 **Ion Stoica · UC Berkeley / Song Han · MIT / NVIDIA** | 🔥 10 | HF Papers · 4 天前</sub>


## 🦾 VLA / 视觉-语言-动作

- **[Learning Low-Latency Action Verification for Frozen Vision-Language-Action Models](https://arxiv.org/abs/2611.14834)**
  Vision-language-action (VLA) models have made significant progress in general-purpose robotic manipulation. However, sampled action sequences can be ineffective, while evaluating…
  <sub>👤 **Trevor Darrell · UC Berkeley** | arXiv · 2 天前</sub>

- **[ActionCodec2: A Streaming Action Tokenizer](https://arxiv.org/abs/2611.15490)**
  Most action tokenizers for autoregressive vision language action (VLA) models compress motion into chunks that must be decoded in full before their actions become executable. We i…
  <sub>👤 **Hang Zhao · Tsinghua** | arXiv · 昨天</sub>

- **[Generalized Inverse Kinematics via Conditional Flow](https://arxiv.org/abs/2611.15565)**
  Inverse kinematics (IK) is a foundational primitive in robotics, mapping the task-space objectives expressed by higher-level planners to robot configurations that realize them. Tr…
  <sub>👤 **Leslie Pack Kaelbling · MIT** | arXiv · 昨天</sub>

- **[What Makes a VLA Reactive? A Study of Execution Strategies for Dynamic Manipulation](https://arxiv.org/abs/2611.15491)**
  Vision-language-action (VLA) models predict chunks of future actions, and when objects move, those chunks go stale before they are executed. We study what makes a pretrained VLA r…
  <sub>💡 想法型 | arXiv · 昨天</sub>


## 🎯 强化学习 / 持续学习

- **[Expanding the Decision Space of Pretrained Models through Structured Re-Decoding](https://arxiv.org/abs/2611.15109)**
  Native decoders limit how pretrained models combine local predictions under new structural constraints. We introduce Structured Re-Decoding (SRD), a training-free framework that c…
  <sub>👤 **Chi Wang · Google DeepMind** | arXiv · 昨天</sub>

- **[SimRec: Learning to Search, Ask, and Recommend from Simulated Interaction](https://arxiv.org/abs/2611.15426)**
  LLM-based recommendation agents can search catalogs, inspect products, ask users, and revise rejected recommendations. However, these behaviors are often governed by hand-designed…
  <sub>arXiv · 昨天</sub>

- **[Knowledge in the Harness, Reliability in the Weights: Teacher-Free Co-Evolution of an LLM Agent](https://arxiv.org/abs/2611.15268)**
  Small open models suit private customer-service deployments but trail frontier models in two ways: they miss what the written policy requires in a given situation, and they act in…
  <sub>arXiv · 昨天</sub>


## 🛡️ 安全 / 对齐 / 可解释

- **[Observations Drift, Structures Remain: Structural Pretraining with Time Alignment for Electromagnetic Signals](https://arxiv.org/abs/2611.15566)**
  Electromagnetic signal modeling is increasingly moving toward self-supervised pretraining on heterogeneous I/Q observations. However, an observed waveform is jointly shaped by sig…
  <sub>👤 **Maosong Sun · Tsinghua** | arXiv · 昨天</sub>


---

<details>
<summary>📡 源状态与运行信息</summary>


**入选来源分布**：arXiv 12, HF Papers 3, Blog 2


**本轮出问题的源**（不影响其他源）：

- RSS Stanford AI Lab: 抓取失败 (https://ai.stanford.edu/blog/feed.xml)
- RSS Import AI: 抓取失败 (https://importai.substack.com/feed)
- 页面监控 Physical Intelligence Blog: 抓取失败 (https://www.physicalintelligence.company/blog)


**模式**：daily　**LLM 摘要**：off（未检测到 ANTHROPIC_API_KEY，已降级为纯摘要截断）

</details>
