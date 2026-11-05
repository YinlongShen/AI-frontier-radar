# AI 前沿雷达 · 2026-11-05

> 扫描 **1851** 条 → 入选 **36** 条 ｜ 关注名单命中 **16** 位研究者 ｜ 生成于 2026-11-05 03:21 UTC

**今日分布**：🧠 大模型 / LLM (6) ｜ 🤖 智能体 / Agent (8) ｜ 👁️ 计算机视觉 / CV (5) ｜ 🎨 多模态 / VLM (4) ｜ 🦾 VLA / 视觉-语言-动作 (2) ｜ 🚶 具身智能 / 机器人 (1) ｜ 🌍 世界模型 / World Models (1) ｜ 🎯 强化学习 / 持续学习 (8) ｜ 📌 其他值得一看 (1)


## ⭐ 今日必读

1. **[Stabilizing On-Policy Targeted Guidance in Agentic Reinforcement Learning](https://arxiv.org/abs/2611.05266)**
   Naive on-policy RL is often bottlenecked by the capabilities of the base model --- insufficient coverage can result in an inability to learn from certain rewards. At the same time…
   <sub>👤 **Sergey Levine · UC Berkeley / Physical Intelligence / Pieter Abbeel · UC Berkeley / Alexander M. Rush · Cornell / Cursor** | arXiv · 昨天</sub>

2. **[GSBR: Geometric Support Behavior Regularization for Online RL](https://arxiv.org/abs/2611.05295)**
   Regularizing online reinforcement learning (RL) toward a pretrained base policy can improve sample efficiency and learning stability, but regularization that is too restrictive li…
   <sub>👤 **Sergey Levine · UC Berkeley / Physical Intelligence** | arXiv · 昨天</sub>

3. **[Hybrid Particle-Voxel Dynamics for Multimodal 3D World Simulation](https://arxiv.org/abs/2611.04492)**
   Predicting how the world evolves in response to robot actions is central to policy learning, evaluation, and planning. However, many action-conditioned world models predict future…
   <sub>👤 **Tao Yu · HKU** | arXiv · 昨天</sub>

4. **[Suppressing Misaligned Behaviors in Language Models, Durably](https://arxiv.org/abs/2611.05358)**
   Undesired model behaviors can emerge or re-emerge at any stage of training. Once observed, how effectively can we suppress them? To study this question, we first construct two mod…
   <sub>👤 **Danqi Chen · Princeton** | arXiv · 昨天</sub>

5. **[Rubric Curriculum RL: Exploiting the Generation-Verification Gap in Non-Verifiable Domains](https://arxiv.org/abs/2611.06244)**
   Reinforcement learning with verifiable rewards (RLVR) has led to significant gains in math and code generation. Extending these gains to open-ended domains remains challenging: gr…
   <sub>👤 **Jakob Foerster · Oxford** | arXiv · 今天</sub>

6. **[PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations](https://arxiv.org/abs/2611.04870)**
   A robot world model that serves as a simulator must do more than generate plausible videos: it must faithfully follow commanded actions, maintain consistency across camera views,…
   <sub>👤 **Hao Dong · Peking University** | 🔥 9 | arXiv · 昨天</sub>

7. **[OneTrans-GSR: A Generative Slate Ranking Paradigm Unifying Reranking and Mix-Ranking with One Autoregressive Transformer](https://arxiv.org/abs/2611.04720)**
   Industrial recommender systems allocate substantial computation to pointwise candidate scoring, yet separate reranking and mix-ranking stages still assemble the final exposure sla…
   <sub>👤 **Ziwei Liu · NTU** | arXiv · 昨天</sub>

8. **[$τ$-Rec-Books: A Disclosure-Controlled Benchmark for Requirement Elicitation in Agentic Recommender Systems](https://arxiv.org/abs/2611.04459)**
   While conversational recommendation systems provide a more natural user interface, they face the challenge of progressively discovering a user's needs before they can recommend an…
   <sub>👤 **Karthik Narasimhan · Princeton / Sierra** | arXiv · 昨天</sub>

9. **[FloMo: 3D Scene Flow as a World Action Model Intermediate for Learning from Human Video](https://arxiv.org/abs/2611.05062)**
   Pretrained video generation models distill internet-scale motion priors into robot policies, but full video is a redundant signal for action prediction. We argue that dense 3D mot…
   <sub>👤 **Animesh Garg · Georgia Tech** | 💡 we argue | arXiv · 昨天</sub>

10. **[ReflexArc: Bottom-Up Integration of Instantaneous Tactile Reflexes into Whole-Body Humanoid Control](https://arxiv.org/abs/2611.04424)**
   Humanoid robots operating in cluttered environments must react to unexpected contacts before the first impact peak, which arrives within tens of milliseconds. Learned whole-body p…
   <sub>👤 **He Wang · Peking University** | arXiv · 昨天</sub>


---


## 🧠 大模型 / LLM

- **[Large Language Model-Assisted Adaptive Heuristic Search for Agile Earth Observation Satellite Scheduling](https://arxiv.org/abs/2611.04458)**
  Agile Earth observation satellites must coordinate imaging tasks within limited observation windows, while accounting for attitude maneuvering and onboard energy constraints. Comp…
  <sub>👤 **He Wang · Peking University** | arXiv · 昨天</sub>

- **[MESA: An Evaluation Framework for Compositional, Semantic, and Spatial Generalization in Robotics](https://arxiv.org/abs/2611.05567)**
  Despite growing interest in foundation models for robotic manipulation, systematic evaluation of their capabilities remains elusive. Existing benchmarks are either narrow and satu…
  <sub>👤 **Animesh Garg · Georgia Tech** | arXiv · 昨天</sub>

- **[Axion 1.0: Open Agent Foundation Models, Simplified](https://arxiv.org/abs/2611.03233)**
  We introduce Axion 1.0, a fully open agent foundation model that combines strong and broad agentic capabilities with a remarkably simple training recipe. Axion 1.0 is trained in o…
  <sub>🔥 40 | HF Papers · 3 天前</sub>

- **[Think Less, Locally: Local Preference Learning for Reasoning Compression](https://arxiv.org/abs/2611.04814)**
  Large reasoning models achieve strong performance on challenging tasks, but their long chain-of-thought often incurs substantial inference costs by continuing to deliberate after…
  <sub>🔥 65 | HF Papers · 2 天前</sub>

- **[Dory1.0-4B: A Looped Normalized-GPT](https://arxiv.org/abs/2611.03998)**
  We introduce Dory1.0-4B, a 4-billion-parameter looped (latent-recurrent) language model with elastic depth: a single checkpoint serves different inference compute budgets. Dory1.0…
  <sub>🔥 6 | HF Papers · 3 天前</sub>

- **[Every Token Needs Its Own Teacher: Multi-teacher Adaptive On-policy Self-distillation](https://arxiv.org/abs/2610.40574)**
  On-policy Self-distillation (OPSD) has proven effective for post-training large language models by constructing a teacher conditioned on privileged references. However, existing a…
  <sub>🔥 10 | 💡 we argue | HF Papers · 7 天前</sub>


## 🤖 智能体 / Agent

- **[$τ$-Rec-Books: A Disclosure-Controlled Benchmark for Requirement Elicitation in Agentic Recommender Systems](https://arxiv.org/abs/2611.04459)**
  While conversational recommendation systems provide a more natural user interface, they face the challenge of progressively discovering a user's needs before they can recommend an…
  <sub>👤 **Karthik Narasimhan · Princeton / Sierra** | arXiv · 昨天</sub>

- **[Zero-Shot Coordination among LLM Agents](https://arxiv.org/abs/2611.06409)**
  We study zero-shot coordination (ZSC), where independently developed agents must coordinate at test time. While ZSC has been well studied in the RL literature, far less is known a…
  <sub>👤 **Jakob Foerster · Oxford** | arXiv · 今天</sub>

- **[A Definition of Catastrophic Performance](https://arxiv.org/abs/2611.06219)**
  A central challenge in AI is specifying objectives that align with human preferences. While existing theoretical results elucidate how misspecification impacts performance, they t…
  <sub>👤 **Benjamin Van Roy · Stanford** | arXiv · 今天</sub>

- **[WebHarbor: Docking Real Websites for Evolving GUI Agent Environments](https://arxiv.org/abs/2611.03634)**
  GUI web agents require realistic and interactive environments that remain stable during both evaluation and training. Live website evaluation suffers from changing content, access…
  <sub>🔥 19 | arXiv · 2 天前</sub>

- **[Adversarial Speculative Reasoning Improves Long Horizon Agents](https://arxiv.org/abs/2611.05345)**
  Speculative decoding has been treated purely as a systems optimization that speeds up large language model decoding without changing the model behavior. Under this view, the growi…
  <sub>🔥 6 | 💡 we argue | HF Papers · 2 天前</sub>

- **[ToolSpace: Scaling Tool-Centric Environment Synthesis for Long-Horizon Agents](https://arxiv.org/abs/2611.05036)**
  Large language models are deployed as long-horizon agents that compose diverse tools across MCP services into executable workflows. Existing MCP environment-scaling methods are da…
  <sub>🔥 34 | HF Papers · 2 天前</sub>

- **[What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?](https://arxiv.org/abs/2611.06483)**
  While multi-turn agentic reinforcement learning (RL) excels on long-horizon tasks, its performance gains remain highly sensitive to interaction constraints. Evaluating across samp…
  <sub>💡 想法型 | arXiv · 今天</sub>

- **[HarnessFlow: MCTS-Guided Harness Optimization for LLM Agents](https://arxiv.org/abs/2611.06254)**
  The performance of large language model (LLM) agents depends on both the underlying model and the harness that governs interaction with tools and the environment. Yet harness desi…
  <sub>arXiv · 今天</sub>


## 👁️ 计算机视觉 / CV

- **[FloMo: 3D Scene Flow as a World Action Model Intermediate for Learning from Human Video](https://arxiv.org/abs/2611.05062)**
  Pretrained video generation models distill internet-scale motion priors into robot policies, but full video is a redundant signal for action prediction. We argue that dense 3D mot…
  <sub>👤 **Animesh Garg · Georgia Tech** | 💡 we argue | arXiv · 昨天</sub>

- **[Coordinating Humanoid Loco-Manipulation through Action-Conditioned Latent Foresight](https://arxiv.org/abs/2611.04839)**
  Humanoid loco-manipulation requires coordinated body motion and hand interaction over time, and a plausible-looking command sequence can still drop a held object or leave an inter…
  <sub>👤 **Ping Luo · HKU** | arXiv · 昨天</sub>

- **[Route Anything: A Study of Model and Policy Routing for General-Purpose AI Systems](https://arxiv.org/abs/2611.05275)**
  Artificial general intelligence (AGI) requires a method that can understand, generate, reason, and act across diverse domains and modalities. Rather than relying on a single model…
  <sub>🔥 86 | HF Papers · 2 天前</sub>

- **[DreamX: Video Diffusion Model is a Universal Latent Action Learner](https://arxiv.org/abs/2611.05377)**
  Learning a universal action representation from video requires modeling dynamics that are consistent across different executions of the same action yet invariant to changes in emb…
  <sub>🔥 51 | HF Papers · 2 天前</sub>

- **[Feature Puzzles: Single-Image Supervision for Multi-View 3D-Aware Segmentation](https://arxiv.org/abs/2611.05874)**
  Humans can easily recognize the same objects across different viewpoints of a 3D scene, whereas teaching models such multi-view-consistent perception typically requires videos or…
  <sub>arXiv · 昨天</sub>


## 🎨 多模态 / VLM

- **[Clips2Story: Training-Free Video Storyboarding and Editing Using Multimodal Retrieval-Embedded Generation](https://arxiv.org/abs/2611.05992)**
  Video editors often work with large collections of fragmented footage and must select and organize relevant clips into a coherent story. However, many existing video editing and s…
  <sub>👤 **Hao Dong · Peking University** | arXiv · 今天</sub>

- **[Entropogram-guided Visual Realignment Decoding: Capturing the Rhythm of Multimodal Reasoning](https://arxiv.org/abs/2611.06415)**
  Multimodal large language models (MLLMs) have demonstrated remarkable progress on cross-modal reasoning tasks, yet they continue to suffer from hallucinations in long-chain reason…
  <sub>💡 we argue | arXiv · 今天</sub>

- **[Factorized MLLM Embeddings for Composed Image Retrieval](https://arxiv.org/abs/2611.05193)**
  Composed Image Retrieval (CIR) aims to retrieve a target image given a reference image and a modification text. Although recent approaches leveraging Multimodal Large Language Mod…
  <sub>🔥 44 | 💡 we argue | HF Papers · 2 天前</sub>

- **[YANAMI: A Large-Scale Multimodal Dataset and Benchmark for Multiturn Stateful Interaction](https://arxiv.org/abs/2611.05280)**
  Unified Multimodal Models (UMMs) integrate visual understanding, generation, and editing within a single unified framework. However, existing unified multimodal datasets and bench…
  <sub>🔥 28 | arXiv · 昨天</sub>


## 🦾 VLA / 视觉-语言-动作

- **[PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations](https://arxiv.org/abs/2611.04870)**
  A robot world model that serves as a simulator must do more than generate plausible videos: it must faithfully follow commanded actions, maintain consistency across camera views,…
  <sub>👤 **Hao Dong · Peking University** | 🔥 9 | arXiv · 昨天</sub>

- **[DexHOT: Learning Hand-Object Configuration Transfer for Dexterous Manipulation](https://arxiv.org/abs/2611.05119)**
  Dexterous manipulation involves not only moving objects, but also arranging the hand around them to maintain useful contacts and enable subsequent actions. Yet many learning-based…
  <sub>👤 **Hao Dong · Peking University** | arXiv · 昨天</sub>


## 🚶 具身智能 / 机器人

- **[ReflexArc: Bottom-Up Integration of Instantaneous Tactile Reflexes into Whole-Body Humanoid Control](https://arxiv.org/abs/2611.04424)**
  Humanoid robots operating in cluttered environments must react to unexpected contacts before the first impact peak, which arrives within tens of milliseconds. Learned whole-body p…
  <sub>👤 **He Wang · Peking University** | arXiv · 昨天</sub>


## 🌍 世界模型 / World Models

- **[Hybrid Particle-Voxel Dynamics for Multimodal 3D World Simulation](https://arxiv.org/abs/2611.04492)**
  Predicting how the world evolves in response to robot actions is central to policy learning, evaluation, and planning. However, many action-conditioned world models predict future…
  <sub>👤 **Tao Yu · HKU** | arXiv · 昨天</sub>


## 🎯 强化学习 / 持续学习

- **[Stabilizing On-Policy Targeted Guidance in Agentic Reinforcement Learning](https://arxiv.org/abs/2611.05266)**
  Naive on-policy RL is often bottlenecked by the capabilities of the base model --- insufficient coverage can result in an inability to learn from certain rewards. At the same time…
  <sub>👤 **Sergey Levine · UC Berkeley / Physical Intelligence / Pieter Abbeel · UC Berkeley / Alexander M. Rush · Cornell / Cursor** | arXiv · 昨天</sub>

- **[GSBR: Geometric Support Behavior Regularization for Online RL](https://arxiv.org/abs/2611.05295)**
  Regularizing online reinforcement learning (RL) toward a pretrained base policy can improve sample efficiency and learning stability, but regularization that is too restrictive li…
  <sub>👤 **Sergey Levine · UC Berkeley / Physical Intelligence** | arXiv · 昨天</sub>

- **[Suppressing Misaligned Behaviors in Language Models, Durably](https://arxiv.org/abs/2611.05358)**
  Undesired model behaviors can emerge or re-emerge at any stage of training. Once observed, how effectively can we suppress them? To study this question, we first construct two mod…
  <sub>👤 **Danqi Chen · Princeton** | arXiv · 昨天</sub>

- **[Rubric Curriculum RL: Exploiting the Generation-Verification Gap in Non-Verifiable Domains](https://arxiv.org/abs/2611.06244)**
  Reinforcement learning with verifiable rewards (RLVR) has led to significant gains in math and code generation. Extending these gains to open-ended domains remains challenging: gr…
  <sub>👤 **Jakob Foerster · Oxford** | arXiv · 今天</sub>

- **[OneTrans-GSR: A Generative Slate Ranking Paradigm Unifying Reranking and Mix-Ranking with One Autoregressive Transformer](https://arxiv.org/abs/2611.04720)**
  Industrial recommender systems allocate substantial computation to pointwise candidate scoring, yet separate reranking and mix-ranking stages still assemble the final exposure sla…
  <sub>👤 **Ziwei Liu · NTU** | arXiv · 昨天</sub>

- **[On Convergence of Gradient Temporal-Difference Learning with Regularized Corrections and Eligibility Traces](https://arxiv.org/abs/2611.05869)**
  Temporal-difference (TD) learning underlies many prediction and control algorithms, but can diverge when combined with off-policy learning, bootstrapping, and function approximati…
  <sub>👤 **Martha White · U Alberta / Amii** | arXiv · 昨天</sub>

- **[Behind Video Generation: Observations and Insights on Multimodal Understanding from Kling](https://arxiv.org/abs/2611.04916)**
  Video generation has progressed from isolated clips to coherent short-form audiovisual sequences, and the bottleneck is shifting from rendering to semantic control. This report su…
  <sub>🔥 52 | 💡 we argue | HF Papers · 2 天前</sub>

- **[Mass Producing Training Data with Surprising Side Effects](https://arxiv.org/abs/2611.06324)**
  Training data can have unexpected side effects on language model behavior outside the training domain: insecure code data can induce broad misalignment, and outdated bird names ca…
  <sub>👤 **Jacob Steinhardt · UC Berkeley / Transluce** | arXiv · 今天</sub>


## 📌 其他值得一看

- **[Reconciling Privacy with Provenance for Language Model Watermarks](https://arxiv.org/abs/2611.06100)**
  Watermarking has great potential for regulating the use of language models (LMs), but its deployment has been marred by controversy, as many users argue that fine-grained tracking…
  <sub>👤 **Tatsunori Hashimoto · Stanford** | arXiv · 今天</sub>


---

<details>
<summary>📡 源状态与运行信息</summary>


**入选来源分布**：arXiv 26, HF Papers 10


**本轮出问题的源**（不影响其他源）：

- RSS Stanford AI Lab: 抓取失败 (https://ai.stanford.edu/blog/feed.xml)
- RSS MIT News - AI: 抓取失败 (https://news.mit.edu/rss/topic/artificial-intelligence2)
- RSS Import AI: 抓取失败 (https://importai.substack.com/feed)


**积压 3 条**（超出本期容量，未标记为已推送，会出现在后续几期）。


**模式**：daily　**LLM 摘要**：off（未检测到 ANTHROPIC_API_KEY，已降级为纯摘要截断）

</details>
