# AI 前沿雷达 · 2026-10-15

> 扫描 **1741** 条 → 入选 **60** 条 ｜ 关注名单命中 **33** 位研究者 ｜ 生成于 2026-10-15 01:19 UTC

**今日分布**：🧠 大模型 / LLM (6) ｜ 🤖 智能体 / Agent (18) ｜ 🧰 Harness / 基建与评测 (1) ｜ 👁️ 计算机视觉 / CV (8) ｜ 🎨 多模态 / VLM (2) ｜ 🦾 VLA / 视觉-语言-动作 (8) ｜ 🚶 具身智能 / 机器人 (3) ｜ 🌍 世界模型 / World Models (3) ｜ 🎯 强化学习 / 持续学习 (8) ｜ 💡 理论 / 新范式 (1) ｜ 📌 其他值得一看 (2)


## ⭐ 今日必读

1. **[Robota-Embed: Unified VLA Embeddings for Robot In-Context Learning and Evolution](https://arxiv.org/abs/2610.19495)**
   Retrieving useful context for a robot requires matching its task, execution stage, and the continuation that should follow. We introduce Robota-Embed, to our knowledge the first v…
   <sub>👤 **Yuke Zhu · UT Austin / NVIDIA / Linxi Fan · NVIDIA GEAR / Trevor Darrell · UC Berkeley +1** | arXiv · 今天</sub>

2. **[FACT: A Multimodal Force-Action-Track Foundation Model for Human-to-Robot Dexterity](https://arxiv.org/abs/2610.19155)**
   Human demonstrations offer a scalable alternative to costly robot data collection for dexterous manipulation, but most human datasets lack force measurements. Dexterous manipulati…
   <sub>👤 **Fei-Fei Li · Stanford / World Labs / Yejin Choi · Stanford / NVIDIA** | arXiv · 昨天</sub>

3. **[Reinforcement Learning via Advantage Guidance](https://arxiv.org/abs/2610.19783)**
   Reinforcement learning (RL) holds the promise of learning a policy that can outperform what is shown in the data. However, in practice, such systems suffer from instability and hy…
   <sub>👤 **Sergey Levine · UC Berkeley / Physical Intelligence** | arXiv · 今天</sub>

4. **[The Agentic Scientist: Orchestrating Coding Agents for Automated Scientific (Co-)Discovery](https://arxiv.org/abs/2610.18933)**
   Modern coding agents are fundamentally reshaping the role of human input for computational research: they write code, launch in silico experiments, analyze their results, and auto…
   <sub>👤 **David Ha · Sakana AI** | arXiv · 昨天</sub>

5. **[Mixture of GFlowNets](https://arxiv.org/abs/2610.17007)**
   Generative Flow Networks (GFlowNets) learn a policy that samples compositional objects in proportion to an unnormalized reward $R(x)$. This makes them useful wherever many diverse…
   <sub>👤 **Yoshua Bengio · Mila / U Montreal** | arXiv · 2 天前</sub>

6. **[ActionOPD: Distilling Decisions, Not Tokens](https://arxiv.org/abs/2610.19820)**
   Distilling capable language-model agents into smaller models requires aligning the student's behavior with the teacher's. This raises a fundamental question: at which states and a…
   <sub>👤 **Xinlei Chen · Meta FAIR** | 💡 we argue | arXiv · 今天</sub>

7. **[Tev: Scaling Long-Horizon Agentic Environments with Dense Progress Rewards](https://arxiv.org/abs/2610.18868)**
   Long-horizon agents have drawn growing attention for their ability to work autonomously -- from hours to days -- on economically valuable tasks, a capability essential to automate…
   <sub>👤 **Yong Jae Lee · UW-Madison** | 🔥 95 | arXiv · 昨天</sub>

8. **[Scaling Online Optimal Transport Minibatches for Flow Matching](https://arxiv.org/abs/2610.18838)**
   A central challenge in scaling flow models is maintaining stability in training and integration. In flow matching, this stability depends critically on how source samples are pair…
   <sub>👤 **Sergey Levine · UC Berkeley / Physical Intelligence** | arXiv · 昨天</sub>

9. **[LeHami: Symplectic Latent Dynamics for World Models](https://arxiv.org/abs/2610.15267)**
   Joint-embedding predictive architectures (JEPAs) learn world models directly in latent space, but unconstrained autoregressive predictors may contract the latent distribution over…
   <sub>👤 **Yann LeCun · NYU** | arXiv · 3 天前</sub>

10. **[Steertuning Policies from a Few Human Videos](https://arxiv.org/abs/2610.18711)**
   Current recipes for robot learning require massive amounts of robot demonstrations to obtain robust and adaptive policies. In this work, we introduce Steertuning, a system that en…
   <sub>👤 **Lerrel Pinto · NYU** | arXiv · 昨天</sub>


## 🕰️ 迟到的热度

*旧内容，但最近热度明显上涨 —— 之前可能被你错过。*

- **[DiffusionART: Efficient, Stable and Scalable Reinforcement of Diffusion Models](https://arxiv.org/abs/2610.12572)**
  Online reinforcement learning (RL) fine-tunes diffusion models with black-box rewards, but reverse-process methods such as Flow-GRPO are limited in efficiency by poor credit assig…
  <sub>🔥 314 | HF Papers · 7 天前</sub>


---


## 🧠 大模型 / LLM

- **[The Smart Buildings Challenge: Learning Foundation Models for Real-World Optimization at Scale](https://arxiv.org/abs/2610.18511)**
  Buildings cause nearly 40\% of carbon emissions in the US. Of total building emissions, HVAC systems are responsible for approximately 40-60\% and account for 15\% of global energ…
  <sub>👤 **Yoshua Bengio · Mila / U Montreal** | arXiv · 昨天</sub>

- **[History Replays Itself: Unleashing Long-Context Capability in Linear Attention](https://arxiv.org/abs/2610.15715)**
  Linear attention promises the efficiency needed for long-context language modelling, yet its fixed-size recurrent state must simultaneously support ongoing computation and preserv…
  <sub>👤 **Jurgen Schmidhuber · KAUST / IDSIA** | arXiv · 3 天前</sub>

- **[A Self-Defining Operator for Distributed Applications](https://arxiv.org/abs/2610.14547)**
  To operate distributed applications with high availability, operators must rapidly diagnose and mitigate any incident. LLM-based agents can help, but unlike experienced human oper…
  <sub>👤 **Luke Zettlemoyer · UW / Meta** | arXiv · 4 天前</sub>

- **[Vela: User Behavior as Supervision Sparks LLM Intelligence](https://arxiv.org/abs/2610.14709)**
  Large language models are increasingly deployed in applications that act on users' long-term behavior histories, from personal assistants to recommendation and advertising systems…
  <sub>🔥 69 | HF Papers · 5 天前</sub>

- **[VideoJev: System One Model for Video Understanding and Interaction](https://arxiv.org/abs/2610.18615)**
  Visual agents must turn video observations into timely decisions to track progress and choose what to do next. Building on the emerging System One paradigm, we introduce VideoJev,…
  <sub>🔥 194 | HF Papers · 2 天前</sub>

- **[How Third Moment Research runs 10,000 agents for 36+ hours](https://openai.com/index/third-moment-research)**
  With GPT-6 Astra and GPT-6.1 Sol, Codex, and Daybreak for cybersecurity, this AI lab builds agents that focus for days and improve with use.
  <sub>🏛 OpenAI | 💡 想法型 | Blog · 今天</sub>


## 🤖 智能体 / Agent

- **[The Agentic Scientist: Orchestrating Coding Agents for Automated Scientific (Co-)Discovery](https://arxiv.org/abs/2610.18933)**
  Modern coding agents are fundamentally reshaping the role of human input for computational research: they write code, launch in silico experiments, analyze their results, and auto…
  <sub>👤 **David Ha · Sakana AI** | arXiv · 昨天</sub>

- **[ActionOPD: Distilling Decisions, Not Tokens](https://arxiv.org/abs/2610.19820)**
  Distilling capable language-model agents into smaller models requires aligning the student's behavior with the teacher's. This raises a fundamental question: at which states and a…
  <sub>👤 **Xinlei Chen · Meta FAIR** | 💡 we argue | arXiv · 今天</sub>

- **[Tev: Scaling Long-Horizon Agentic Environments with Dense Progress Rewards](https://arxiv.org/abs/2610.18868)**
  Long-horizon agents have drawn growing attention for their ability to work autonomously -- from hours to days -- on economically valuable tasks, a capability essential to automate…
  <sub>👤 **Yong Jae Lee · UW-Madison** | 🔥 95 | arXiv · 昨天</sub>

- **[JevGPT: Thinking Fast and Slow in Autonomous Research](https://arxiv.org/abs/2610.18272)**
  Autonomous research agents must acquire and reason over evidence within a limited budget. Yet relevant sources can remain uninspected or unused, leaving a gap between retrieval co…
  <sub>👤 **Jurgen Schmidhuber · KAUST / IDSIA** | 🔥 20 | arXiv · 昨天</sub>

- **[Into the Unknown: Benchmarking AI agents on open scientific research problems](https://arxiv.org/abs/2610.19159)**
  Can AI agents carry out research on open scientific problems? We introduce Into the Unknown, a benchmark that provides an agent with a science paper along with a research directio…
  <sub>👤 **Graham Neubig · CMU / All Hands AI** | arXiv · 昨天</sub>

- **[Davinci-Tool: Scaling Agentic Tool-Use Supervision with Verifiable Executable Environments](https://arxiv.org/abs/2610.16867)**
  Reliable agentic tool use requires training data that pair diverse multi-step workflows with executable evidence that the requested outcomes were achieved. Scaling either trajecto…
  <sub>👤 **Yu Qiao · Shanghai AI Lab** | arXiv · 2 天前</sub>

- **[VideoHarness-SRSI: Structured Recursive Self-Improvement for Video Understanding Harness](https://arxiv.org/abs/2610.19424)**
  LLM system capabilities depend not only on model parameters but also on the executable harnesses that organize information acquisition, tool use, reasoning, and memory. Recursive…
  <sub>👤 **Yang Song** | arXiv · 今天</sub>

- **[Interaction-as-a-Judge](https://arxiv.org/abs/2610.17895)**
  Coding agents are tasked with producing sophisticated interactive applications such as websites, desktop applications, and games. While humans assess these applications interactiv…
  <sub>👤 **Ion Stoica · UC Berkeley** | arXiv · 昨天</sub>

- **[DuoDiscover: Scaling Autonomous Discovery Beyond the Evaluation Bottleneck](https://arxiv.org/abs/2610.17184)**
  Evaluation has been central to advances in AI, and it is equally critical to autonomous discovery. Yet scaling autonomous discovery to real-world engineering challenges faces a fu…
  <sub>👤 **Ion Stoica · UC Berkeley** | arXiv · 2 天前</sub>

- **[RoboSimStudio: An Interactive Toolkit for Rapid Real2Sim of Robot Manipulation Tasks](https://arxiv.org/abs/2610.18835)**
  It is difficult to accurately model the physics of the interaction between a robot and the objects it manipulates, including contact mechanics, coupled contact dynamics, deformati…
  <sub>👤 **Ken Goldberg · UC Berkeley** | arXiv · 昨天</sub>

- **[I3L: Iterative Interactive Imitation Learning for Whole-Body Mobile Manipulation](https://arxiv.org/abs/2610.17748)**
  Policies trained offline from teleoperated demonstrations can degrade outside their training distribution. This gap is particularly acute in long-horizon whole-body mobile manipul…
  <sub>👤 **Fei-Fei Li · Stanford / World Labs** | arXiv · 昨天</sub>

- **[CryptoFlowBench: Benchmarking Multi-Hop Reasoning on Blockchains for Cryptocurrency Fund Tracing](https://arxiv.org/abs/2610.16449)**
  Pseudonymous accounts and complex smart-contract ecosystems substantially hinder the tracing of illicit cryptocurrency fund flows. Existing Graph Neural Networks (GNNs) have achie…
  <sub>👤 **Yang Gao · Tsinghua** | arXiv · 2 天前</sub>

- **[Agent-Reflex: Teaching Language Agents to Act Reflectively](https://arxiv.org/abs/2610.17953)**
  Large language models have evolved from single-turn chatbots into interactive agents capable of long-horizon reasoning. In real deployments, MCP tool services can return noisy fee…
  <sub>🔥 194 | HF Papers · 2 天前</sub>

- **[Belief Embedding Tree Search](https://arxiv.org/abs/2610.15046)**
  Beliefs in a Partially Observable Markov Decision Process (POMDP) are posterior distributions over the hidden state given the agent's history of actions and observations. They sum…
  <sub>👤 **Michael Bowling · U Alberta** | arXiv · 4 天前</sub>

- **[When Does an ASR Error Matter? Task-Role Diagnostics for Tool-Using Voice Agents](https://arxiv.org/abs/2610.17619)**
  In cascaded voice agents, ASR errors can have markedly different downstream consequences: a small transcription error may leave a tool call unchanged or alter its intent or argume…
  <sub>👤 **Xiaolong Wang · UCSD** | arXiv · 昨天</sub>

- **[Empowering Edge Agents: A Systematic Analysis of Edge-Cloud Collaboration in LLM Agent Execution](https://arxiv.org/abs/2610.17816)**
  Edge-cloud collaboration combines the lower inference overhead and greater data locality of edge-side execution with the stronger capabilities of cloud-hosted models. However, as…
  <sub>👤 **Maosong Sun · Tsinghua** | arXiv · 昨天</sub>

- **[Urbex: Agentic Spatial Grounding for City-Scale 3D Scenes](https://arxiv.org/abs/2610.18356)**
  City-scale 3D grounding is commonly formulated as candidate ranking, which requires precomputed instance proposals and becomes inefficient in large outdoor scenes. We propose Urbe…
  <sub>🔥 110 | HF Papers · 2 天前</sub>

- **[Verifier-Harness Co-Evolution for Training-Free Self-Improvement on Open-Ended Tasks](https://arxiv.org/abs/2610.17609)**
  Training-free self-improvement lets an agent use feedback to revise the response it is about to return and to update the harness state that shapes how it handles later tasks. On o…
  <sub>👤 **Qingyun Wu · Penn State / AG2** | arXiv · 昨天</sub>


## 🧰 Harness / 基建与评测

- **[Optimization for One, Feasibility for Most: Decoupling Optimization from Feasibility in Chance-Constrained Programs](https://arxiv.org/abs/2610.19027)**
  Chance-constrained stochastic programs (CCSPs) require solutions that satisfy uncertain constraints with high probability. Standard approaches either embed scenarios directly into…
  <sub>👤 **Shunyu Yao · Anthropic** | arXiv · 昨天</sub>


## 👁️ 计算机视觉 / CV

- **[Scaling Online Optimal Transport Minibatches for Flow Matching](https://arxiv.org/abs/2610.18838)**
  A central challenge in scaling flow models is maintaining stability in training and integration. In flow matching, this stability depends critically on how source samples are pair…
  <sub>👤 **Sergey Levine · UC Berkeley / Physical Intelligence** | arXiv · 昨天</sub>

- **[CineMem: Attention-Aligned Fine-grained Memory Retrieval for Multi-Shot Long Video Generation](https://arxiv.org/abs/2610.17926)**
  Autoregressive video generation relies on memory retrieval to model long-range dependencies. This capability becomes particularly critical for multi-shot generation, where models…
  <sub>👤 **Yu Qiao · Shanghai AI Lab** | arXiv · 昨天</sub>

- **[Data-Centric Recursive Self-Improvement for Navigation via Policy-Synchronized Language-Action Dual Bootstrapping](https://arxiv.org/abs/2610.15782)**
  Vision-language navigation requires agents to follow natural-language instructions to reach target locations, making high-quality language supervision essential. Since human annot…
  <sub>👤 **Yu Qiao · Shanghai AI Lab** | 🔥 25 | arXiv · 3 天前</sub>

- **[IsoVRBench: Video Reward Modeling Without Human Feedback](https://arxiv.org/abs/2610.17234)**
  Video reward models are trained and evaluated on human preferences between videos that often differ simultaneously on properties such as prompt alignment, visual fidelity, motion,…
  <sub>👤 **Luke Zettlemoyer · UW / Meta** | arXiv · 2 天前</sub>

- **[Sparse All-Layer Connector for Domain Generalised Semantic Segmentation](https://arxiv.org/abs/2610.15660)**
  Domain generalised semantic segmentation (DGSS) has recently benefited from combining multiple foundation models, such as vision-language and vision foundation models, to leverage…
  <sub>👤 **Yang Song** | arXiv · 3 天前</sub>

- **[CineRecon: Benchmarking Frontier Models for Agentic Cinematic Reconstruction](https://arxiv.org/abs/2610.16577)**
  Reconstructing reference videos as editable dynamic 3D scenes is an important path toward controllable video generation for filmmaking: these scenes provide modifiable, renderable…
  <sub>🔥 21 | HF Papers · 3 天前</sub>

- **[LeWAM: End-to-End World and Action Modeling with JEPAs](https://arxiv.org/abs/2610.12818)**
  Joint-embedding predictive architectures (JEPAs) learn compact latent world models without pixel reconstruction. Existing JEPA pipelines typically train visual representations and…
  <sub>🔥 63 | HF Papers · 7 天前</sub>

- **[GAD: Geometry Attention Distillation for Consistent Video Generation](https://arxiv.org/abs/2610.18779)**
  Video diffusion models generate visually compelling short-term sequences but often struggle to preserve scene geometry and object structure over time. In this paper, we first demo…
  <sub>💡 we argue | arXiv · 昨天</sub>


## 🎨 多模态 / VLM

- **[AesCode: Aesthetic Code Generation with Decoupled Cross-Modal Rewards](https://arxiv.org/abs/2610.18860)**
  Generating information-rich visual artifacts such as slides, posters, and dashboards as code is appealing because the outputs are structured, editable, and verifiable. Yet code mo…
  <sub>🔥 80 | HF Papers · 2 天前</sub>

- **[Learning How to Remember: Memory Modality Selection for GUI Agents](https://arxiv.org/abs/2610.17928)**
  Recent advances in vision-language models (VLMs) have substantially improved the capabilities of GUI agents, while memory augmentation has emerged as a promising approach for reus…
  <sub>🔥 41 | HF Papers · 2 天前</sub>


## 🦾 VLA / 视觉-语言-动作

- **[Robota-Embed: Unified VLA Embeddings for Robot In-Context Learning and Evolution](https://arxiv.org/abs/2610.19495)**
  Retrieving useful context for a robot requires matching its task, execution stage, and the continuation that should follow. We introduce Robota-Embed, to our knowledge the first v…
  <sub>👤 **Yuke Zhu · UT Austin / NVIDIA / Linxi Fan · NVIDIA GEAR / Trevor Darrell · UC Berkeley +1** | arXiv · 今天</sub>

- **[FACT: A Multimodal Force-Action-Track Foundation Model for Human-to-Robot Dexterity](https://arxiv.org/abs/2610.19155)**
  Human demonstrations offer a scalable alternative to costly robot data collection for dexterous manipulation, but most human datasets lack force measurements. Dexterous manipulati…
  <sub>👤 **Fei-Fei Li · Stanford / World Labs / Yejin Choi · Stanford / NVIDIA** | arXiv · 昨天</sub>

- **[Steertuning Policies from a Few Human Videos](https://arxiv.org/abs/2610.18711)**
  Current recipes for robot learning require massive amounts of robot demonstrations to obtain robust and adaptive policies. In this work, we introduce Steertuning, a system that en…
  <sub>👤 **Lerrel Pinto · NYU** | arXiv · 昨天</sub>

- **[Coordi-pi: Coordination-Aware Dual-Hand Action Representation for Bimanual Dexterous Manipulation](https://arxiv.org/abs/2610.19753)**
  Vision-language-action (VLA) models have shown strong potential for general-purpose robotic manipulation, but extending them to bimanual dexterous manipulation introduces a high-d…
  <sub>👤 **Ping Luo · HKU** | arXiv · 今天</sub>

- **[Force-Modulated Dexterity: Unified Compliance for Contact-Rich Manipulation](https://arxiv.org/abs/2610.17161)**
  Teleoperation is widely used to collect high-quality demonstrations for robot learning. Dexterous manipulation, however, requires coordinated control of motion and contact forces.…
  <sub>👤 **Jitendra Malik · UC Berkeley** | arXiv · 2 天前</sub>

- **[EqC: Equilibrium Energy Control for Introspective Lifelong Robot Learning](https://arxiv.org/abs/2610.18790)**
  Long-term robot autonomy depends on more than effective action generation: a policy must recognize when its behavior is no longer sufficiently supported and use assistance to impr…
  <sub>👤 **Hang Zhao · Tsinghua** | arXiv · 昨天</sub>

- **[WAVE-0: Bridging VLA Policies and WAMs with Lightweight Latent Future Prediction](https://arxiv.org/abs/2610.18568)**
  Vision-language-action (VLA) policies excel at generalist robotic manipulation but generate actions without explicitly modeling their environmental consequences. World action mode…
  <sub>🔥 22 | HF Papers · 2 天前</sub>

- **[GreenWAM: A World Foundation Model for Robotics](https://arxiv.org/abs/2610.18774)**
  A robot needs a world model that predicts how its actions will change the scene and a policy that chooses those actions. Models are usually built and evaluated for only one of the…
  <sub>🔥 82 | HF Papers · 2 天前</sub>


## 🚶 具身智能 / 机器人

- **[Contact-UAN: Unsupervised Actuator Networks as a Residual World Model for Humanoid Control](https://arxiv.org/abs/2610.18991)**
  Humanoid policies trained in simulation can transfer qualitatively to hardware while failing to transfer the force interactions learned during training, compromising torque effici…
  <sub>👤 **Pulkit Agrawal · MIT** | arXiv · 昨天</sub>

- **[Contact Trajectory Prompting: In-Context Transfer of Contact-Rich Behaviors from a Single Demonstration](https://arxiv.org/abs/2610.18848)**
  In-context robot learning enables robots to acquire new behaviors from demonstrations without test-time parameter updates. However, visual and kinematic specifications alone may n…
  <sub>👤 **Cewu Lu · SJTU** | arXiv · 昨天</sub>

- **[DexNinja: Learning Robust Dexterous Cutting Policy with a Real-to-Sim-to-Real Data Engine](https://arxiv.org/abs/2610.17208)**
  Cutting a piece of food looks effortless in human hands. For a robot, however, every cut is a high-contact interaction with a deformable, elasto-plastic object whose behavior chan…
  <sub>👤 **Hang Zhao · Tsinghua** | arXiv · 2 天前</sub>


## 🌍 世界模型 / World Models

- **[LeHami: Symplectic Latent Dynamics for World Models](https://arxiv.org/abs/2610.15267)**
  Joint-embedding predictive architectures (JEPAs) learn world models directly in latent space, but unconstrained autoregressive predictors may contract the latent distribution over…
  <sub>👤 **Yann LeCun · NYU** | arXiv · 3 天前</sub>

- **[WorldOracle: Benchmarking Action-Conditioned World Models against Real-World Executions](https://arxiv.org/abs/2610.18826)**
  We introduce WorldOracle, a benchmark specifically designed to evaluate action-conditioned world models (ACWMs) against paired real-world executions. Given the same initial observ…
  <sub>👤 **Yuke Zhu · UT Austin / NVIDIA** | arXiv · 昨天</sub>

- **[ForceWAM: Decoupling Future and Response Learning from Demo and Play Data for Contact-Rich Manipulation](https://arxiv.org/abs/2610.18852)**
  Expert demonstrations show how to complete contact-rich tasks, but provide limited coverage of how interaction forces respond to different actions. Task-agnostic play provides bro…
  <sub>👤 **Cewu Lu · SJTU** | arXiv · 昨天</sub>


## 🎯 强化学习 / 持续学习

- **[Reinforcement Learning via Advantage Guidance](https://arxiv.org/abs/2610.19783)**
  Reinforcement learning (RL) holds the promise of learning a policy that can outperform what is shown in the data. However, in practice, such systems suffer from instability and hy…
  <sub>👤 **Sergey Levine · UC Berkeley / Physical Intelligence** | arXiv · 今天</sub>

- **[Mixture of GFlowNets](https://arxiv.org/abs/2610.17007)**
  Generative Flow Networks (GFlowNets) learn a policy that samples compositional objects in proportion to an unnormalized reward $R(x)$. This makes them useful wherever many diverse…
  <sub>👤 **Yoshua Bengio · Mila / U Montreal** | arXiv · 2 天前</sub>

- **[FlashVSR+: Efficient Video Super-Resolution via Hybrid Attention and Reward-Yield Distribution Matching](https://arxiv.org/abs/2610.17552)**
  Recent video super-resolution (VSR) models achieve efficient one-step generation through diffusion distillation. However, high-resolution inference remains costly, and distilled m…
  <sub>👤 **Yu Qiao · Shanghai AI Lab** | 🔥 30 | arXiv · 昨天</sub>

- **[DiffusionART: Efficient, Stable and Scalable Reinforcement of Diffusion Models](https://arxiv.org/abs/2610.12572)**
  Online reinforcement learning (RL) fine-tunes diffusion models with black-box rewards, but reverse-process methods such as Flow-GRPO are limited in efficiency by poor credit assig…
  <sub>🔥 314 | HF Papers · 7 天前</sub>

- **[HarnessTTT: Learn to Optimize Harness at Test-Time for Scientific Discovery](https://arxiv.org/abs/2610.17370)**
  Scientific discovery with language models requires finding the best valid solution within a finite computational budget. We study how feedback from this search can improve the pro…
  <sub>👤 **Yejin Choi · Stanford / NVIDIA** | arXiv · 2 天前</sub>

- **[Inference on the Value of Policy Improvement in Adaptive Experiments](https://arxiv.org/abs/2610.15789)**
  In this paper, we develop an asymptotically normal estimator for the value of policy improvement (VPI) under adaptively collected data. This value, which is defined as the gap bet…
  <sub>👤 **Emma Brunskill · Stanford** | arXiv · 3 天前</sub>

- **[X-Ragent: Tool-Augmented Reinforcement Learning for Evidence-Grounded Chest X-Ray Reasoning](https://arxiv.org/abs/2610.16811)**
  Chest X-ray (CXR) interpretation often requires integrating visual findings with task-specific evidence rather than relying on direct visual recognition alone. While tool-augmente…
  <sub>🔥 66 | HF Papers · 3 天前</sub>

- **[Oct 14, 2026 Policy Preparing for the 2026 US midterms](https://www.anthropic.com/news/2026-us-midterms)**
  <sub>🏛 Anthropic | 页面更新 · 新发现</sub>


## 💡 理论 / 新范式

- **[Jeva: System One Models from First Principles](https://arxiv.org/abs/2610.18773)**
  System one models enable direct, low-latency decision-making. Yet recent practice of predicting an answer from serialized text does not, by itself, respect the structure of a deci…
  <sub>🔥 267 | 💡 we argue | HF Papers · 2 天前</sub>


## 📌 其他值得一看

- **[SchemaPose: RGB-Based Category-Level Pose Estimation with Parametric Category Schema](https://arxiv.org/abs/2610.18374)**
  RGB-based category-level 9D pose estimation remains highly challenging because a monocular system must generalize across unseen object instances while jointly inferring 3D transla…
  <sub>👤 **Cewu Lu · SJTU** | arXiv · 昨天</sub>

- **[Pushback in a Haystack: Language Models Respond to Factual Errors Ambiguously and Ineffectively](https://arxiv.org/abs/2610.17703)**
  The sycophancy of language models, or their failure to push back against faulty user input, is now widely studied. However, if LMs do push back, is sycophancy solved? We show that…
  <sub>👤 **Noah A. Smith · UW / AI2** | arXiv · 昨天</sub>


---

<details>
<summary>📡 源状态与运行信息</summary>


**入选来源分布**：arXiv 45, HF Papers 13, 页面更新 1, Blog 1


**本轮出问题的源**（不影响其他源）：

- RSS MIT News - AI: 抓取失败 (https://news.mit.edu/rss/topic/artificial-intelligence2)
- RSS Import AI: 抓取失败 (https://importai.substack.com/feed)


**积压 24 条**（超出本期容量，未标记为已推送，会出现在后续几期）。


**模式**：daily　**LLM 摘要**：off（未检测到 ANTHROPIC_API_KEY，已降级为纯摘要截断）

</details>
