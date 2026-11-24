# AI 前沿雷达 · 2026-11-24

> 扫描 **1772** 条 → 入选 **29** 条 ｜ 关注名单命中 **14** 位研究者 ｜ 生成于 2026-11-24 06:51 UTC

**今日分布**：🧠 大模型 / LLM (6) ｜ 🤖 智能体 / Agent (6) ｜ 🧰 Harness / 基建与评测 (4) ｜ 👁️ 计算机视觉 / CV (2) ｜ 🎨 多模态 / VLM (4) ｜ 🦾 VLA / 视觉-语言-动作 (1) ｜ 🌍 世界模型 / World Models (1) ｜ 🎯 强化学习 / 持续学习 (4) ｜ 💡 理论 / 新范式 (1)


## ⭐ 今日必读

1. **[Visual-RFT++: Extending Visual Reinforcement Fine-Tuning to Multimodal Tool Use](https://arxiv.org/abs/2611.30193)**
   Reinforcement Fine-Tuning (RFT) has recently become a central paradigm for advancing Large Reasoning Models (LRMs), as demonstrated by systems such as OpenAI's o3 and the R1 serie…
   <sub>👤 **Dahua Lin · CUHK / Shanghai AI Lab** | arXiv · 今天</sub>

2. **[From Reward Engineering to Data-Centric Reinforcement Learning for Effective Agentic Visual Tool Use](https://arxiv.org/abs/2611.28558)**
   Multimodal large language models (MLLMs) increasingly use external visual tools to acquire evidence during reasoning, yet learning when to invoke these tools remains challenging.…
   <sub>👤 **Hao Dong · Peking University** | 💡 we argue | arXiv · 3 天前</sub>

3. **[On Adaptive Step Sizes for Eligibility Traces in Deep Reinforcement Learning](https://arxiv.org/abs/2611.29178)**
   Many deep reinforcement learning (RL) algorithms store agent-environment interactions in a replay buffer and later learn by sampling transitions from it. However, this approach ca…
   <sub>👤 **Martha White · U Alberta / Amii** | arXiv · 2 天前</sub>

4. **[Rethinking the Evaluation of Contrastive Decoding for Hallucination Mitigation in Multimodal Large Language Models](https://arxiv.org/abs/2611.30460)**
   Contrastive decoding (CD) mitigates object hallucination in multimodal large language models (MLLMs) by contrasting token distributions under different conditions to adjust token…
   <sub>👤 **Ting Chen · Google DeepMind** | 💡 rethinking | arXiv · 今天</sub>

5. **[OWE-Bench: A long-horizon benchmark for measuring real-world engineering](https://arxiv.org/abs/2611.30017)**
   We present OWE-Bench (OpenWorldEngineer-Bench), a benchmark of 26 long-horizon engineering tasks written by domain experts in software engineering, physical engineering, machine l…
   <sub>👤 **Jason Wei · OpenAI** | arXiv · 昨天</sub>

6. **[Your Diffusion-Based Driving Planner Only Needs a Nudge](https://arxiv.org/abs/2611.29123)**
   Diffusion-based planners capture the multimodality of human driving behavior well, yet covariate shift in closed-loop driving can lead them to generate trajectories that result in…
   <sub>👤 **Jakob Foerster · Oxford** | arXiv · 2 天前</sub>

7. **[Bridging Teacher-Student Capability Gaps with Recurrent Computation](https://arxiv.org/abs/2611.28603)**
   Knowledge distillation transfers capabilities from large language models to smaller students, yet stronger teachers do not always yield better students. Recent studies report dimi…
   <sub>👤 **Yong Jae Lee · UW-Madison** | arXiv · 3 天前</sub>

8. **[SANA-Robot: Efficient World Action Model with Hybrid Memory](https://arxiv.org/abs/2611.28943)**
   World action models (WAMs) leverage the world knowledge of video generation models to improve action generation by aligning visual prediction with action prediction. However, thei…
   <sub>👤 **Song Han · MIT / NVIDIA** | arXiv · 2 天前</sub>

9. **[MoMa-NMP: Scene-Scale Neural Motion Planning for Mobile Manipulators](https://arxiv.org/abs/2611.29913)**
   Mobile manipulators operating in homes and other complex environments must coordinate their base and arm over long horizons, navigating around obstacles, through narrow passages,…
   <sub>👤 **Deepak Pathak · CMU / Skild AI** | arXiv · 昨天</sub>

10. **[Tool-to-Self: Internalizing Visual Tool Capabilities via Scaffolded Reinforcement Learning](https://arxiv.org/abs/2611.28564)**
   Vision-language models (VLMs) increasingly rely on external visual tools to access fine-grained visual evidence, but repeated tool execution incurs substantial inference overhead…
   <sub>👤 **Hao Dong · Peking University** | arXiv · 3 天前</sub>


---


## 🧠 大模型 / LLM

- **[Rethinking the Evaluation of Contrastive Decoding for Hallucination Mitigation in Multimodal Large Language Models](https://arxiv.org/abs/2611.30460)**
  Contrastive decoding (CD) mitigates object hallucination in multimodal large language models (MLLMs) by contrasting token distributions under different conditions to adjust token…
  <sub>👤 **Ting Chen · Google DeepMind** | 💡 rethinking | arXiv · 今天</sub>

- **[OWE-Bench: A long-horizon benchmark for measuring real-world engineering](https://arxiv.org/abs/2611.30017)**
  We present OWE-Bench (OpenWorldEngineer-Bench), a benchmark of 26 long-horizon engineering tasks written by domain experts in software engineering, physical engineering, machine l…
  <sub>👤 **Jason Wei · OpenAI** | arXiv · 昨天</sub>

- **[Bridging Teacher-Student Capability Gaps with Recurrent Computation](https://arxiv.org/abs/2611.28603)**
  Knowledge distillation transfers capabilities from large language models to smaller students, yet stronger teachers do not always yield better students. Recent studies report dimi…
  <sub>👤 **Yong Jae Lee · UW-Madison** | arXiv · 3 天前</sub>

- **[RumiFold: Teaching an LLM to Natively Fold Proteins and Reason About Their Function](https://arxiv.org/abs/2611.29444)**
  Can we teach a general-purpose language model to fold proteins? And if so, what does learning to fold enable beyond structure prediction itself? We introduce RumiFold, a pretraine…
  <sub>👤 **David Bau · Northeastern** | arXiv · 昨天</sub>

- **[A Glimpse of Training VLMs as Foundation Models for Robotic Manipulation](https://arxiv.org/abs/2611.29338)**
  Recently, GPT-6 Astra demonstrates strong generalization in robot control, yet limited disclosure of its training leaves open how such capabilities can be reproduced. We introduce…
  <sub>🔥 11 | HF Papers · 2 天前</sub>

- **[RUIBench: What Makes a Good Robot-Use Interface?](https://arxiv.org/abs/2611.31115)**
  Foundation models can reason about complex physical tasks, yet translating this intelligence into reliable robot execution remains challenging. We argue that a critical, often ove…
  <sub>🔥 1 | 💡 we argue | HF Papers · 昨天</sub>


## 🤖 智能体 / Agent

- **[Visual-RFT++: Extending Visual Reinforcement Fine-Tuning to Multimodal Tool Use](https://arxiv.org/abs/2611.30193)**
  Reinforcement Fine-Tuning (RFT) has recently become a central paradigm for advancing Large Reasoning Models (LRMs), as demonstrated by systems such as OpenAI's o3 and the R1 serie…
  <sub>👤 **Dahua Lin · CUHK / Shanghai AI Lab** | arXiv · 今天</sub>

- **[From Reward Engineering to Data-Centric Reinforcement Learning for Effective Agentic Visual Tool Use](https://arxiv.org/abs/2611.28558)**
  Multimodal large language models (MLLMs) increasingly use external visual tools to acquire evidence during reasoning, yet learning when to invoke these tools remains challenging.…
  <sub>👤 **Hao Dong · Peking University** | 💡 we argue | arXiv · 3 天前</sub>

- **[DeepDOSReasoner: Physics-Grounded Reasoning for Density-of-States Prediction and Materials Discovery](https://arxiv.org/abs/2611.29132)**
  Predicting a material's behavior from its atomic structure is a longstanding goal of the physical sciences. The electronic and phonon densities of states (eDOS and phDOS) govern k…
  <sub>👤 **Tao Yu · HKU** | arXiv · 2 天前</sub>

- **[How to build and maintain an agentic evaluation](https://huggingface.co/blog/agentic-evals)**
  <sub>🏛 HuggingFace | 💡 想法型 | Blog · 昨天</sub>

- **[3AGameFactory-Motion: Agentic Rigging and Reliable Complex Motion Generation for Diverse 3D Assets](https://arxiv.org/abs/2611.30013)**
  Animating arbitrary 3D assets from instructions requires both structural inference and motion control, yet existing motion benchmarks mostly cover conventional human or animal ske…
  <sub>🔥 33 | HF Papers · 昨天</sub>

- **[mini-psych-agent: Evaluating Human-Like Behavior in LLM Agents through Interactive Psychological Environments](https://arxiv.org/abs/2611.30365)**
  A Large Language Model (LLM), its harness, and the test-time compute budget jointly determine its behavior. Consequently, the same underlying model, embedded in different agentic…
  <sub>arXiv · 今天</sub>


## 🧰 Harness / 基建与评测

- **[MoMa-NMP: Scene-Scale Neural Motion Planning for Mobile Manipulators](https://arxiv.org/abs/2611.29913)**
  Mobile manipulators operating in homes and other complex environments must coordinate their base and arm over long horizons, navigating around obstacles, through narrow passages,…
  <sub>👤 **Deepak Pathak · CMU / Skild AI** | arXiv · 昨天</sub>

- **[PixelOne: From Options to Pixels in a Single Forward for GUI Grounding](https://arxiv.org/abs/2611.30235)**
  GUI grounding requires precise clicks at low latency. Recent models such as GUI-Decisions and GUI-Swift predict coordinates in one forward pass using fixed global bins with local…
  <sub>👤 **Yu Qiao · Shanghai AI Lab** | arXiv · 今天</sub>

- **[IteraSong: LLM-Guided Iterative Symbolic Music Creation in a Web DAW](https://arxiv.org/abs/2611.29225)**
  Music creation is inherently iterative, yet many symbolic generation systems still center on producing or regenerating isolated outputs. We present IteraSong, an interactive web-b…
  <sub>👤 **Maosong Sun · Tsinghua** | arXiv · 2 天前</sub>

- **[MemOnce: A Scalable Memory Architecture for Large Language Models](https://arxiv.org/abs/2611.27973)**
  Deploying large language models (LLMs) in long-horizon and continual interactions requires maintaining reusable memory states for future inference, posing challenges for existing…
  <sub>🔥 22 | HF Papers · 4 天前</sub>


## 👁️ 计算机视觉 / CV

- **[SANA-Robot: Efficient World Action Model with Hybrid Memory](https://arxiv.org/abs/2611.28943)**
  World action models (WAMs) leverage the world knowledge of video generation models to improve action generation by aligning visual prediction with action prediction. However, thei…
  <sub>👤 **Song Han · MIT / NVIDIA** | arXiv · 2 天前</sub>

- **[NNS-GS: Non-Local Neural Scattering for Relightable Gaussian Splatting](https://arxiv.org/abs/2611.30351)**
  Creating relightable 3D assets of translucent objects is challenging because changing the illumination at one surface location can affect the appearance elsewhere through subsurfa…
  <sub>👤 **Yang Gao · Tsinghua** | arXiv · 今天</sub>


## 🎨 多模态 / VLM

- **[Towards Agentic Video Corpus Moment Retrieval](https://arxiv.org/abs/2611.29877)**
  Video corpus moment retrieval (VCMR) requires finding the video and time interval that match a text query in a corpus of videos. We present RELAY, a training-free framework for VC…
  <sub>💡 towards | arXiv · 昨天</sub>

- **[Learning Video Foresight Reasoning from Unlabeled Videos via On-Policy Self-Distillation](https://arxiv.org/abs/2611.26954)**
  Video foresight reasoning requires vision-language models to anticipate future events or next actions from currently observed videos. Existing methods fit future captions, rationa…
  <sub>🔥 42 | HF Papers · 4 天前</sub>

- **[Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation](https://arxiv.org/abs/2611.27689)**
  Vision-language model (VLM)-based agents offer a promising approach to robotic manipulation, yet remain limited by inadequate memory organization, uncertain failure attribution, a…
  <sub>🔥 6 | arXiv · 3 天前</sub>

- **[Learning Multimodal Representations from Partially Paired, Small-Scale Data](https://arxiv.org/abs/2611.30601)**
  Modeling multimodal data from partially paired samples is critical for advancing domains like biomedicine, where vast unimodal datasets and foundation models exist but paired data…
  <sub>arXiv · 今天</sub>


## 🦾 VLA / 视觉-语言-动作

- **[Beyond Which: Where, How, and When in Vision-Language-Action Models](https://arxiv.org/abs/2611.30291)**
  Vision-language-action (VLA) models typically rely on vision-language model (VLM) features as the primary perceptual source for action prediction, showing strong generalization ac…
  <sub>💡 想法型 | arXiv · 今天</sub>


## 🌍 世界模型 / World Models

- **[Non-penetrating World Models](https://arxiv.org/abs/2611.27963)**
  We study a new problem of preventing object penetration in interactive video world models. To understand how existing models handle this, we introduce NoPeBench, a benchmark that…
  <sub>🔥 55 | HF Papers · 4 天前</sub>


## 🎯 强化学习 / 持续学习

- **[On Adaptive Step Sizes for Eligibility Traces in Deep Reinforcement Learning](https://arxiv.org/abs/2611.29178)**
  Many deep reinforcement learning (RL) algorithms store agent-environment interactions in a replay buffer and later learn by sampling transitions from it. However, this approach ca…
  <sub>👤 **Martha White · U Alberta / Amii** | arXiv · 2 天前</sub>

- **[Your Diffusion-Based Driving Planner Only Needs a Nudge](https://arxiv.org/abs/2611.29123)**
  Diffusion-based planners capture the multimodality of human driving behavior well, yet covariate shift in closed-loop driving can lead them to generate trajectories that result in…
  <sub>👤 **Jakob Foerster · Oxford** | arXiv · 2 天前</sub>

- **[Tool-to-Self: Internalizing Visual Tool Capabilities via Scaffolded Reinforcement Learning](https://arxiv.org/abs/2611.28564)**
  Vision-language models (VLMs) increasingly rely on external visual tools to access fine-grained visual evidence, but repeated tool execution incurs substantial inference overhead…
  <sub>👤 **Hao Dong · Peking University** | arXiv · 3 天前</sub>

- **[Object Count Generalization Is an Interface Problem: Warping a Frozen Skill Instead of Retraining It](https://arxiv.org/abs/2611.30765)**
  Reinforcement learning policies for robot manipulation degrade when the number of objects N in the scene grows beyond the training range. This is a covariate shift that also chang…
  <sub>arXiv · 今天</sub>


## 💡 理论 / 新范式

- **[PopMelodyGen: A Copyright-Aware Platform for Controllable Pop-Melody Generation](https://arxiv.org/abs/2611.28686)**
  Large-scale redistributable symbolic pop-melody data remain scarce due to copyright restrictions, creating a bottleneck for both practical deployment and reproducible research in…
  <sub>👤 **Maosong Sun · Tsinghua** | arXiv · 2 天前</sub>


---

<details>
<summary>📡 源状态与运行信息</summary>


**入选来源分布**：arXiv 22, HF Papers 6, Blog 1


**本轮出问题的源**（不影响其他源）：

- RSS Import AI: 抓取失败 (https://importai.substack.com/feed)
- 页面监控 Physical Intelligence Blog: 抓取失败 (https://www.physicalintelligence.company/blog)


**模式**：daily　**LLM 摘要**：off（未检测到 ANTHROPIC_API_KEY，已降级为纯摘要截断）

</details>
