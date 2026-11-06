# AI 前沿雷达 · 2026-11-06

> 扫描 **1859** 条 → 入选 **30** 条 ｜ 关注名单命中 **12** 位研究者 ｜ 生成于 2026-11-06 03:19 UTC

**今日分布**：🧠 大模型 / LLM (6) ｜ 🤖 智能体 / Agent (8) ｜ 🧰 Harness / 基建与评测 (2) ｜ 👁️ 计算机视觉 / CV (2) ｜ 🎨 多模态 / VLM (1) ｜ 🦾 VLA / 视觉-语言-动作 (2) ｜ 🌍 世界模型 / World Models (1) ｜ 🎯 强化学习 / 持续学习 (6) ｜ 📌 其他值得一看 (2)


## ⭐ 今日必读

1. **[VABAR: A Variational Automation Benchmark for Agentic Robotics](https://arxiv.org/abs/2611.06881)**
   For robots to operate reliably in commercial and industrial applications, they must persistently perform specific tasks with known variations in object shape and pose. We call thi…
   <sub>👤 **Linxi Fan · NVIDIA GEAR / Yuke Zhu · UT Austin / NVIDIA / Ken Goldberg · UC Berkeley** | arXiv · 昨天</sub>

2. **[From Pixels to Actions - Towards Native Vision-Language-Action Policies](https://arxiv.org/abs/2611.06918)**
   Vision-language-action models are typically built on a simple premise: perception is first compressed by visual encoders, and action reasoning begins only afterwards. Yet manipula…
   <sub>👤 **Dahua Lin · CUHK / Shanghai AI Lab / Ziwei Liu · NTU** | 🔥 56 | arXiv · 昨天</sub>

3. **[MAC-v2: Long-horizon model-based value expansion from pixels](https://arxiv.org/abs/2611.07245)**
   We study whether \emph{long-horizon model-based value expansion} can serve as an effective framework in pixel-based offline reinforcement learning (RL). Long-horizon model-based v…
   <sub>👤 **Sergey Levine · UC Berkeley / Physical Intelligence** | arXiv · 昨天</sub>

4. **[Turns Matter: Advancing Streaming Video RL via Turn-Level Credit](https://arxiv.org/abs/2611.06728)**
   Streaming video understanding requires models to repeatedly decide whether to respond or continue observing. Recently, Group Relative Policy Optimization (GRPO) has been applied t…
   <sub>👤 **Yu Qiao · Shanghai AI Lab** | 🔥 83 | arXiv · 昨天</sub>

5. **[LifeVal: Evaluating AI Model Performance on Personalized Agentic Consumer Tasks](https://arxiv.org/abs/2611.06687)**
   We introduce LifeVal, a benchmark evaluating AI model performance on personalized agentic consumer tasks. LifeVal covers the most valuable life tasks that a personalized digital s…
   <sub>👤 **Noam Brown · OpenAI** | 💡 想法型 | arXiv · 昨天</sub>

6. **[Permanent and Transient Representations for Continual Reinforcement Learning](https://arxiv.org/abs/2611.07327)**
   Continual Reinforcement Learning (CRL) agents struggle to adapt to new situations while retaining prior knowledge, leading to a stability-plasticity trade-off. One approach to sol…
   <sub>👤 **Doina Precup · McGill / Mila / DeepMind** | arXiv · 昨天</sub>

7. **[ServerBench: How can your coding agents design specialized LLM serving systems?](https://arxiv.org/abs/2611.06841)**
   Large language model (LLM) coding agents develop software through experimentation, offering an opportunity to design the serving systems supporting their own operation. Effective…
   <sub>👤 **Beidi Chen · CMU** | arXiv · 昨天</sub>

8. **[CompressionBench: How can your coding agents compress LLMs?](https://arxiv.org/abs/2611.06858)**
   Recursive self-improvement requires AI systems to improve the models and infrastructure used by subsequent systems. LLM compression offers a concrete efficiency objective: retain…
   <sub>👤 **Beidi Chen · CMU** | arXiv · 昨天</sub>

9. **[Same Answer, Different Future: Matched Predictions Do Not Imply Matched Belief Updating in Language Models](https://arxiv.org/abs/2611.07913)**
   Language models can produce similar probabilistic predictions after observing outcomes, reading summaries, receiving instructions, or undergoing activation interventions. Whether…
   <sub>👤 **Xinlei Chen · Meta FAIR** | arXiv · 今天</sub>

10. **[Procedural Adversarial Learning](https://arxiv.org/abs/2611.06890)**
   For many computer vision tasks, neural networks can be trained to produce a low average error, yet they still fail on seemingly simple scenes. Reducing these failures requires fir…
   <sub>👤 **Jia Deng · Princeton** | arXiv · 昨天</sub>


---


## 🧠 大模型 / LLM

- **[Towards Foundation Decision Models: Drex](https://arxiv.org/abs/2611.07854)**
  Autoregressive approaches with large language models, such as long chain-of-thought reasoning, have become the default for new AI applications because they reach higher accuracy o…
  <sub>🔥 2 | 💡 towards | arXiv · 今天</sub>

- **[SAVeR$^2$: Reasoning-based Safety Alignment for Large Reasoning Models via Verifiable Rewards](https://arxiv.org/abs/2611.07482)**
  Large Reasoning Models (LRMs) have achieved impressive performance via explicit Chain-of-Thought (CoT) reasoning, yet this process introduces critical safety risks. We formalize L…
  <sub>💡 we argue | arXiv · 今天</sub>

- **[How I Aligned Your Model: Scaling Up Multilingual Safety Training with Templates](https://arxiv.org/abs/2610.40516)**
  Safety alignment for Large Language Models is heavily focused on English with limited multilingual representation, particularly damaging low-resource language performance. Related…
  <sub>🔥 7 | 💡 想法型 | HF Papers · 8 天前</sub>

- **[LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers](https://arxiv.org/abs/2611.05304)**
  Looped transformers are a parameter-efficient alternative to standard transformers for language modeling. By reapplying the same layers across multiple loop steps, recent looped l…
  <sub>🔥 8 | HF Papers · 2 天前</sub>

- **[Generate-then-Rank: Learning Symbolic Goal Interpretation for Embodied Agents](https://arxiv.org/abs/2611.07825)**
  Goal interpretation is to translate a natural language instruction into a formal symbolic goal that a planner can execute. It is critical for embodied agents because any error her…
  <sub>arXiv · 今天</sub>

- **[DeFT-RAG: Decomposing Multi-Hop Questions into Self-Contained Sub-Questions with Reusable Answers](https://arxiv.org/abs/2610.37826)**
  Retrieval-augmented generation (RAG) lets a large language model (LLM) answer questions by retrieving relevant passages from a large corpus. However, RAG struggles with multi-hop…
  <sub>🔥 13 | HF Papers · 7 天前</sub>


## 🤖 智能体 / Agent

- **[VABAR: A Variational Automation Benchmark for Agentic Robotics](https://arxiv.org/abs/2611.06881)**
  For robots to operate reliably in commercial and industrial applications, they must persistently perform specific tasks with known variations in object shape and pose. We call thi…
  <sub>👤 **Linxi Fan · NVIDIA GEAR / Yuke Zhu · UT Austin / NVIDIA / Ken Goldberg · UC Berkeley** | arXiv · 昨天</sub>

- **[LifeVal: Evaluating AI Model Performance on Personalized Agentic Consumer Tasks](https://arxiv.org/abs/2611.06687)**
  We introduce LifeVal, a benchmark evaluating AI model performance on personalized agentic consumer tasks. LifeVal covers the most valuable life tasks that a personalized digital s…
  <sub>👤 **Noam Brown · OpenAI** | 💡 想法型 | arXiv · 昨天</sub>

- **[ServerBench: How can your coding agents design specialized LLM serving systems?](https://arxiv.org/abs/2611.06841)**
  Large language model (LLM) coding agents develop software through experimentation, offering an opportunity to design the serving systems supporting their own operation. Effective…
  <sub>👤 **Beidi Chen · CMU** | arXiv · 昨天</sub>

- **[CompressionBench: How can your coding agents compress LLMs?](https://arxiv.org/abs/2611.06858)**
  Recursive self-improvement requires AI systems to improve the models and infrastructure used by subsequent systems. LLM compression offers a concrete efficiency objective: retain…
  <sub>👤 **Beidi Chen · CMU** | arXiv · 昨天</sub>

- **[Formally verifying agent-written full-stack web apps with PDD Kit](https://www.microsoft.com/en-us/research/blog/formally-verifying-agent-written-full-stack-web-apps-with-pdd-kit/)**
  At a glance Formal methods for everyday software. PDD Kit helps you turn your intent into a formal spec, then proves the code your agent writes for every input and uses tests wher…
  <sub>🏛 Microsoft Research | Blog · 今天</sub>

- **[Hybrid Computer Use: A Unified Programmatic, Semantic, and Visual Interface for General Agents](https://arxiv.org/abs/2610.41432)**
  Computer-use agents increasingly tackle tasks ranging from everyday desktop activities to long-horizon professional workflows. Yet interfaces centered on screenshots and mouse-and…
  <sub>🔥 10 | 💡 we argue | arXiv · 6 天前</sub>

- **[TAC-CoT: Tool-Empowered Implicit Chain-of-Thought via Interleaving Explicit Tokens](https://arxiv.org/abs/2611.01926)**
  LLM-based agentic systems are increasingly combined with CoT reasoning to solve tasks that require accurate reasoning, external knowledge, and multi-step deliberation. Yet, explic…
  <sub>🔥 14 | HF Papers · 4 天前</sub>

- **[PyRUA-DataFarm: LLM Agent as a Cost-Efficient Teleoperator for Real-Ready Robot Data](https://arxiv.org/abs/2611.05320)**
  Teleoperation remains the default way to collect robot demonstrations, but every episode costs robot and operator time, and every new task starts from scratch. We ask whether a co…
  <sub>🔥 23 | HF Papers · 2 天前</sub>


## 🧰 Harness / 基建与评测

- **[CacheGraft: Enhancing Retrieval-Augmented Generation via Latent-Space Document Enrichment](https://arxiv.org/abs/2611.07393)**
  Recent work in machine learning has demonstrated that transformer-based language model agents can communicate state not only through text, but also directly in latent space via ke…
  <sub>💡 we argue | arXiv · 今天</sub>

- **[SpecOPD: Branch-Parallel On-Policy Distillation for Speculative Decoding](https://arxiv.org/abs/2611.02846)**
  Speculative decoding (SD) accelerates large language model inference by reducing the sequential cost of token-by-token generation. Advanced SD methods reduce proposal cost with pa…
  <sub>🔥 13 | HF Papers · 4 天前</sub>


## 👁️ 计算机视觉 / CV

- **[Procedural Adversarial Learning](https://arxiv.org/abs/2611.06890)**
  For many computer vision tasks, neural networks can be trained to produce a low average error, yet they still fail on seemingly simple scenes. Reducing these failures requires fir…
  <sub>👤 **Jia Deng · Princeton** | arXiv · 昨天</sub>

- **[VA-TDM: A Unified View for Improving Few-Step Diffusion Models by Velocity Adversarial Distillation](https://arxiv.org/abs/2611.06796)**
  Few-step distillation offers efficient generation with diffusion and flow models, but preserving quality with only a few sampling steps remains challenging. Distribution-matching…
  <sub>🔥 12 | HF Papers · 2 天前</sub>


## 🎨 多模态 / VLM

- **[Are Frontier VLM Agents Ready to Be Robot Generalists? An Empirical Study with the Embodied Agent Arena](https://arxiv.org/abs/2610.00854)**
  A robot generalist must interpret a scene, act on it, and satisfy every condition of a task. How far do frontier vision-language models (VLMs) meet these demands? We introduce Emb…
  <sub>🔥 84 | HF Papers · 14 天前</sub>


## 🦾 VLA / 视觉-语言-动作

- **[From Pixels to Actions - Towards Native Vision-Language-Action Policies](https://arxiv.org/abs/2611.06918)**
  Vision-language-action models are typically built on a simple premise: perception is first compressed by visual encoders, and action reasoning begins only afterwards. Yet manipula…
  <sub>👤 **Dahua Lin · CUHK / Shanghai AI Lab / Ziwei Liu · NTU** | 🔥 56 | arXiv · 昨天</sub>

- **[Concertina: Embodying Manipulation and Cognition in One Diffusion Vision-Language Model](https://arxiv.org/abs/2611.07513)**
  Most vision-language-action (VLA) policies decouple manipulation from cognition by bolting an external action mechanism onto a vision-language model (VLM)--either quantizing actio…
  <sub>💡 we argue | arXiv · 今天</sub>


## 🌍 世界模型 / World Models

- **[MAC-v2: Long-horizon model-based value expansion from pixels](https://arxiv.org/abs/2611.07245)**
  We study whether \emph{long-horizon model-based value expansion} can serve as an effective framework in pixel-based offline reinforcement learning (RL). Long-horizon model-based v…
  <sub>👤 **Sergey Levine · UC Berkeley / Physical Intelligence** | arXiv · 昨天</sub>


## 🎯 强化学习 / 持续学习

- **[Turns Matter: Advancing Streaming Video RL via Turn-Level Credit](https://arxiv.org/abs/2611.06728)**
  Streaming video understanding requires models to repeatedly decide whether to respond or continue observing. Recently, Group Relative Policy Optimization (GRPO) has been applied t…
  <sub>👤 **Yu Qiao · Shanghai AI Lab** | 🔥 83 | arXiv · 昨天</sub>

- **[Permanent and Transient Representations for Continual Reinforcement Learning](https://arxiv.org/abs/2611.07327)**
  Continual Reinforcement Learning (CRL) agents struggle to adapt to new situations while retaining prior knowledge, leading to a stability-plasticity trade-off. One approach to sol…
  <sub>👤 **Doina Precup · McGill / Mila / DeepMind** | arXiv · 昨天</sub>

- **[EmoReward: Self-Evolving Reward Calibration for Emotional Video Generation RL](https://arxiv.org/abs/2611.06518)**
  Group Relative Policy Optimization (GRPO) has advanced generative model post-training in verifiable domains such as code and mathematics, but evaluating video quality, especially…
  <sub>🔥 22 | HF Papers · 2 天前</sub>

- **[On the Generalization Limitation of On-Policy Distillation for Post-RL Consolidation](https://arxiv.org/abs/2611.05609)**
  Multi-teacher on-policy distillation (MOPD) extends on-policy distillation (OPD) to consolidate capabilities from multiple teachers. Although prior work reports near-perfect in-di…
  <sub>🔥 16 | 💡 想法型 | HF Papers · 3 天前</sub>

- **[Provable Zeroth-Order Safe Exploration for Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2611.07561)**
  Safe reinforcement learning from human feedback (Safe-RLHF) seeks to improve helpfulness while satisfying harmlessness constraints. Existing primal-dual approaches can converge to…
  <sub>arXiv · 今天</sub>

- **[AttnSR: Attention Step Reward for Long-Horizon Agentic RL](https://arxiv.org/abs/2611.07932)**
  Long-horizon LLM agents make multi-step decisions, yet outcome-reward-only reinforcement learning provides little direct supervision for individual steps. We introduce AttnSR, a s…
  <sub>arXiv · 今天</sub>


## 📌 其他值得一看

- **[Same Answer, Different Future: Matched Predictions Do Not Imply Matched Belief Updating in Language Models](https://arxiv.org/abs/2611.07913)**
  Language models can produce similar probabilistic predictions after observing outcomes, reading summaries, receiving instructions, or undergoing activation interventions. Whether…
  <sub>👤 **Xinlei Chen · Meta FAIR** | arXiv · 今天</sub>

- **[how researchers use claude](https://www.anthropic.com/research/how-researchers-use-claude)**
  <sub>🏛 Anthropic | 💡 想法型 | 页面更新 · 新发现</sub>


---

<details>
<summary>📡 源状态与运行信息</summary>


**入选来源分布**：arXiv 18, HF Papers 10, 页面更新 1, Blog 1


**本轮出问题的源**（不影响其他源）：

- RSS Stanford AI Lab: 抓取失败 (https://ai.stanford.edu/blog/feed.xml)
- RSS MIT News - AI: 抓取失败 (https://news.mit.edu/rss/topic/artificial-intelligence2)
- RSS Import AI: 抓取失败 (https://importai.substack.com/feed)


**积压 2 条**（超出本期容量，未标记为已推送，会出现在后续几期）。


**模式**：daily　**LLM 摘要**：off（未检测到 ANTHROPIC_API_KEY，已降级为纯摘要截断）

</details>
