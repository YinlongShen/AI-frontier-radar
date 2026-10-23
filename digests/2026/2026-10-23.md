# AI 前沿雷达 · 2026-10-23

> 扫描 **620** 条 → 入选 **33** 条 ｜ 关注名单命中 **8** 位研究者 ｜ 生成于 2026-10-23 01:54 UTC

**今日分布**：🧠 大模型 / LLM (2) ｜ 🤖 智能体 / Agent (8) ｜ 🧰 Harness / 基建与评测 (6) ｜ 👁️ 计算机视觉 / CV (7) ｜ 🎨 多模态 / VLM (3) ｜ 🦾 VLA / 视觉-语言-动作 (3) ｜ 🚶 具身智能 / 机器人 (1) ｜ 🎯 强化学习 / 持续学习 (3)


## ⭐ 今日必读

1. **[Agentic World Action Models](https://arxiv.org/abs/2610.30136)**
   Recent world action models provide visual foresight and future prediction for robot manipulation, but lack explicit mechanisms for compositional skill reuse. Agentic robotics comb…
   <sub>👤 **Yuke Zhu · UT Austin / NVIDIA / Linxi Fan · NVIDIA GEAR / Ken Goldberg · UC Berkeley +1** | 🔥 11 | HF Papers · 2 天前</sub>

2. **[DONIC: Generalist Dexterous Bimanual Tracking Control from Human Demonstrations](https://arxiv.org/abs/2610.29997)**
   Despite recent progress in dexterous reference tracking, existing models focus primarily on single-hand manipulation and a limited range of interactions, leaving the bimanual dext…
   <sub>👤 **Ziwei Liu · NTU** | 🔥 129 | HF Papers · 2 天前</sub>

3. **[DeXplicit: Making Physical State Explicit in Dexterous Manipulation World Models](https://arxiv.org/abs/2610.30781)**
   Before acting on an object, a robot needs to anticipate how its hand motion will change the physical world and what the resulting scene will look like. Existing approaches typical…
   <sub>👤 **Ziwei Liu · NTU** | arXiv · 今天</sub>

4. **[LocoManiLab: A Unified Testbed for Data, Policies, Controllers, and Deployment in Humanoid Loco-Manipulation](https://arxiv.org/abs/2610.30876)**
   Humanoid robots must coordinate locomotion and manipulation in everyday environments, yet progress is difficult to assess across differing policies, controllers, and task settings…
   <sub>👤 **Ping Luo · HKU** | arXiv · 今天</sub>

5. **[UniFlowWAM: A Unified World-Action Model with Visual Semantics and 4D Geometry](https://arxiv.org/abs/2610.30991)**
   Robot demonstrations record what the robot saw and what it did. They do not specify how the 3D world changed in between. Scene-level 3D flow describes it by tracking 3D scene poin…
   <sub>👤 **Cewu Lu · SJTU** | arXiv · 今天</sub>

6. **[Evolving with Open Worlds: Towards Recursive Self-Improvement for Future Forecasting](https://arxiv.org/abs/2610.29784)**
   Most contemporary artificial intelligence (AI) systems are released with frozen parameters and improve through external updates, whereas an ideal system would keep improving from…
   <sub>👤 **Jia Deng · Princeton** | 🔥 11 | HF Papers · 2 天前</sub>

7. **[Cache Engineering for Agents](https://arxiv.org/abs/2610.28577)**
   Large Language Model (LLM) agents can handle increasingly complex tasks, navigating long trajectories of observations and actions. As these trajectories grow, key-value (KV) cache…
   <sub>🔥 113 | HF Papers · 3 天前</sub>

8. **[Can AI Co-Design Structures? An AI Agent for Early-Stage Structural Design](https://arxiv.org/abs/2610.31113)**
   Recent advances in large language models and agentic workflows offer a new paradigm to early-stage structural design translating design intent into structural models. Although tex…
   <sub>💡 a new paradigm | arXiv · 今天</sub>

9. **[Agent World Model in the Wild: Computer-Use Agent Environment Synthesis](https://arxiv.org/abs/2610.26828)**
   Agent learning is shifting from learning from human data toward learning through interaction with the world. However, scaling such learning directly in real-world computer systems…
   <sub>🔥 64 | HF Papers · 4 天前</sub>

10. **[Looking Ahead: Modeling Future Evolution in Autoregressive Video Generation](https://arxiv.org/abs/2610.29989)**
   Autoregressive video diffusion models generate videos chunk by chunk, yet producing plausible continuations does not guarantee that they capture how scenes evolve. Under teacher f…
   <sub>🔥 118 | HF Papers · 2 天前</sub>


---


## 🧠 大模型 / LLM

- **[ULME: Predictive Coupling for Mutually Reinforcing Embedding and Language Modeling](https://arxiv.org/abs/2610.30705)**
  Text embedding and text generation are two of the most useful capabilities of modern large language models, yet they are typically provided by separate specialized models (an embe…
  <sub>💡 we argue | arXiv · 今天</sub>

- **[Answering in the User's Variety: Calibrated Accommodation Pairs for Post-Training](https://arxiv.org/abs/2610.28474)**
  People adapt how they talk to the person in front of them. However, chat models tend to respond in Standard English regardless of the dialect used by the user. A uniform answer ca…
  <sub>🔥 8 | HF Papers · 3 天前</sub>


## 🤖 智能体 / Agent

- **[Evolving with Open Worlds: Towards Recursive Self-Improvement for Future Forecasting](https://arxiv.org/abs/2610.29784)**
  Most contemporary artificial intelligence (AI) systems are released with frozen parameters and improve through external updates, whereas an ideal system would keep improving from…
  <sub>👤 **Jia Deng · Princeton** | 🔥 11 | HF Papers · 2 天前</sub>

- **[Can AI Co-Design Structures? An AI Agent for Early-Stage Structural Design](https://arxiv.org/abs/2610.31113)**
  Recent advances in large language models and agentic workflows offer a new paradigm to early-stage structural design translating design intent into structural models. Although tex…
  <sub>💡 a new paradigm | arXiv · 今天</sub>

- **[Agent World Model in the Wild: Computer-Use Agent Environment Synthesis](https://arxiv.org/abs/2610.26828)**
  Agent learning is shifting from learning from human data toward learning through interaction with the world. However, scaling such learning directly in real-world computer systems…
  <sub>🔥 64 | HF Papers · 4 天前</sub>

- **[Right Screen, Wrong Transition: World Models as Verifiers for GUI Agents](https://arxiv.org/abs/2610.11942)**
  A login screen that appears after a tap on Sign in is expected; the same screen after a tap on View order is an attack. For GUI agents, safety is therefore a property of the trans…
  <sub>🔥 96 | 💡 we argue | HF Papers · 15 天前</sub>

- **[AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics](https://arxiv.org/abs/2610.28589)**
  Agentic robotics systems combine planners with robot harnesses to perform complex manipulation tasks. Recent work improves these systems through better harnesses and external memo…
  <sub>🔥 21 | HF Papers · 3 天前</sub>

- **[Donating Agent Skills to the Agentic AI Foundation](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)**
  <sub>🏛 Anthropic | 页面更新 · 新发现</sub>

- **[DeLoop: Repeated Actions as Self-Supervision for Long-Horizon Agents](https://arxiv.org/abs/2610.19376)**
  Language-model agents that run long tasks often redo work they have already done: they re-issue a tool call they made earlier and get back exactly the same observation, a step tha…
  <sub>🏛 Qwen / Alibaba | 🔥 17 | HF Papers · 9 天前</sub>

- **[Memory-Centric Continual Learning for AI Agents](https://arxiv.org/abs/2610.29357)**
  Autonomous agents powered by foundation models can reason, plan, and use tools, but their fixed weights and context limits hinder sustained learning from experience over long-term…
  <sub>🔥 19 | HF Papers · 2 天前</sub>


## 🧰 Harness / 基建与评测

- **[Cache Engineering for Agents](https://arxiv.org/abs/2610.28577)**
  Large Language Model (LLM) agents can handle increasingly complex tasks, navigating long trajectories of observations and actions. As these trajectories grow, key-value (KV) cache…
  <sub>🔥 113 | HF Papers · 3 天前</sub>

- **[AstroBench: Benchmarking Free-Floating Capture and Space Robotic Manipulation](https://arxiv.org/abs/2610.31064)**
  Capturing a loose object inside a spacecraft requires a robot to approach a target that can translate and rotate, and whose motion changes when contact is made. These conditions m…
  <sub>👤 **Jia Deng · Princeton** | arXiv · 今天</sub>

- **[Retrieval Augmented Generation Compositionality](https://arxiv.org/abs/2610.29722)**
  Retrieval Augmented Generation (RAG) grounds large language models in external knowledge. Modern pipelines combine embedding, chunking, retrieval, reranking, query augmentation, c…
  <sub>🔥 27 | HF Papers · 2 天前</sub>

- **[Donating Agent Skills to the Agentic AI Foundation](https://simonwillison.net/2026/Oct/22/donating-agent-skills/)**
  Donating Agent Skills to the Agentic AI Foundation News today from Anthropic: We’re committed to keeping Agent Skills open, community-driven, and vendor-neutral. Today, we are don…
  <sub>🏛 — / OpenAI | Blog · 今天</sub>

- **[CoEvo-RSI: When Harnesses Evolve, Which Models Should Follow?](https://arxiv.org/abs/2610.25078)**
  Model--harness co-evolution has emerged as a prominent paradigm for recursive self-improving (RSI) agents, jointly evolving their execution scaffolds and intrinsic capabilities. W…
  <sub>🔥 116 | HF Papers · 5 天前</sub>

- **[DiffResearch: Accelerating Deep Research with Diffusion Language Models](https://arxiv.org/abs/2610.28909)**
  Deep research systems iteratively plan, gather evidence, synthesize, and revise, making end-to-end latency a key bottleneck for interactive use. Almost all production systems are…
  <sub>🔥 6 | HF Papers · 3 天前</sub>


## 👁️ 计算机视觉 / CV

- **[DeXplicit: Making Physical State Explicit in Dexterous Manipulation World Models](https://arxiv.org/abs/2610.30781)**
  Before acting on an object, a robot needs to anticipate how its hand motion will change the physical world and what the resulting scene will look like. Existing approaches typical…
  <sub>👤 **Ziwei Liu · NTU** | arXiv · 今天</sub>

- **[UniFlowWAM: A Unified World-Action Model with Visual Semantics and 4D Geometry](https://arxiv.org/abs/2610.30991)**
  Robot demonstrations record what the robot saw and what it did. They do not specify how the 3D world changed in between. Scene-level 3D flow describes it by tracking 3D scene poin…
  <sub>👤 **Cewu Lu · SJTU** | arXiv · 今天</sub>

- **[Looking Ahead: Modeling Future Evolution in Autoregressive Video Generation](https://arxiv.org/abs/2610.29989)**
  Autoregressive video diffusion models generate videos chunk by chunk, yet producing plausible continuations does not guarantee that they capture how scenes evolve. Under teacher f…
  <sub>🔥 118 | HF Papers · 2 天前</sub>

- **[StreamEval: Evaluating Interactive Streaming Video Generation Models](https://arxiv.org/abs/2610.28402)**
  As streaming video generation advances, enabling real-time interaction with generated video is becoming increasingly important. We introduce StreamEval, a unified benchmark for in…
  <sub>🔥 360 | HF Papers · 3 天前</sub>

- **[ALPS: Visual State Encoders for World Models](https://arxiv.org/abs/2610.30120)**
  World models turn visual representations into predictions and actions. We argue that their visual foundation should combine physical-state information, native language alignment,…
  <sub>🔥 18 | 💡 we argue | HF Papers · 2 天前</sub>

- **[PVBench: Quantifying Physical Plausibility in Video Generation with Object-Level Physical Measurements](https://arxiv.org/abs/2610.26711)**
  Recent video generation models produce visually compelling outputs, yet their physical plausibility remains poorly measured. Physical plausibility asks whether generated objects o…
  <sub>🔥 7 | HF Papers · 4 天前</sub>

- **[FineSplat: Fine Patches, Local Groups, Detailed Splats](https://arxiv.org/abs/2610.25011)**
  Feed-forward 3D Gaussian Splatting (3DGS) promises instant scene reconstruction with high-quality novel-view synthesis. Yet, fine-grained geometry and appearance remain difficult…
  <sub>🔥 29 | HF Papers · 5 天前</sub>


## 🎨 多模态 / VLM

- **[DONIC: Generalist Dexterous Bimanual Tracking Control from Human Demonstrations](https://arxiv.org/abs/2610.29997)**
  Despite recent progress in dexterous reference tracking, existing models focus primarily on single-hand manipulation and a limited range of interactions, leaving the bimanual dext…
  <sub>👤 **Ziwei Liu · NTU** | 🔥 129 | HF Papers · 2 天前</sub>

- **[SpatialScout: Can VLM Agents Actively Explore and Map 3D Scenes?](https://arxiv.org/abs/2610.26659)**
  Spatial intelligence requires agents to actively acquire visual evidence and integrate observations into a coherent representation of the three-dimensional world. Yet spatial ques…
  <sub>🔥 129 | HF Papers · 4 天前</sub>

- **[Qwen-Audio-3.1-ASR Technical Report](https://arxiv.org/abs/2610.28711)**
  We present Qwen-Audio-3.1-ASR, a family of audio-language models that builds upon its predecesor Qwen-Audio-3.0-ASR with improved speech recognition and expanded capabilities in s…
  <sub>🏛 Qwen / Alibaba | 🔥 12 | HF Papers · 3 天前</sub>


## 🦾 VLA / 视觉-语言-动作

- **[Agentic World Action Models](https://arxiv.org/abs/2610.30136)**
  Recent world action models provide visual foresight and future prediction for robot manipulation, but lack explicit mechanisms for compositional skill reuse. Agentic robotics comb…
  <sub>👤 **Yuke Zhu · UT Austin / NVIDIA / Linxi Fan · NVIDIA GEAR / Ken Goldberg · UC Berkeley +1** | 🔥 11 | HF Papers · 2 天前</sub>

- **[From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation](https://arxiv.org/abs/2610.29560)**
  Vision-language-action (VLA) models achieve strong performance across embodied manipulation tasks by unifying visual understanding, language conditioning, and action generation. H…
  <sub>🔥 10 | HF Papers · 2 天前</sub>

- **[SmolVLA-MoE: Sparse Mixture-of-Experts for Efficient Multi-Task Robotic Manipulation](https://arxiv.org/abs/2610.30732)**
  Vision-Language-Action (VLA) models have shown promising results in multi-task robotic manipulation by leveraging visual and language understanding for action generation. However,…
  <sub>arXiv · 今天</sub>


## 🚶 具身智能 / 机器人

- **[LocoManiLab: A Unified Testbed for Data, Policies, Controllers, and Deployment in Humanoid Loco-Manipulation](https://arxiv.org/abs/2610.30876)**
  Humanoid robots must coordinate locomotion and manipulation in everyday environments, yet progress is difficult to assess across differing policies, controllers, and task settings…
  <sub>👤 **Ping Luo · HKU** | arXiv · 今天</sub>


## 🎯 强化学习 / 持续学习

- **[Language Models Learn to Improve Language Models](https://arxiv.org/abs/2610.23344)**
  Large language models (LLMs) are increasingly used to automate AI research, including language-model (LM) development, offering a potential path toward recursive self-improvement.…
  <sub>🔥 5 | HF Papers · 7 天前</sub>

- **[DRILL: Training World Models to Improve Policies, Not Predict Pixels](https://arxiv.org/abs/2610.30814)**
  World models are increasingly used to reduce environment interaction when post-training vision-language-action (VLA) policies with reinforcement learning. Yet they are typically t…
  <sub>arXiv · 今天</sub>

- **[EAU: Environment-Agent-User Co-evolution for Training User-Centric Agents](https://arxiv.org/abs/2610.16523)**
  Training LLM agents to interact with users over multiple turns is challenging because the learning signal depends not only on the agent, but also on the user simulator and environ…
  <sub>🔥 17 | HF Papers · 11 天前</sub>


---

<details>
<summary>📡 源状态与运行信息</summary>


**入选来源分布**：HF Papers 23, arXiv 8, 页面更新 1, Blog 1


**本轮出问题的源**（不影响其他源）：

- RSS Stanford AI Lab: 抓取失败 (https://ai.stanford.edu/blog/feed.xml)
- RSS MIT News - AI: 抓取失败 (https://news.mit.edu/rss/topic/artificial-intelligence2)
- RSS Import AI: 抓取失败 (https://importai.substack.com/feed)


**积压 3 条**（超出本期容量，未标记为已推送，会出现在后续几期）。


**模式**：daily　**LLM 摘要**：off（未检测到 ANTHROPIC_API_KEY，已降级为纯摘要截断）

</details>
