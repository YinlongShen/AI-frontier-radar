# AI 前沿雷达 · ai-frontier-radar

> 每天早上一份三分钟能读完的简报，回答一个问题：**AI 各个方向上，值得我关注的人和实验室，最近放出了什么新想法？**


---

## 它解决的具体问题

常规的每日 arXiv 推送救不了这种情况 —— 它只看"今天新增的论文"。

| 机制 | 做法 |
|---|---|
| **双时间窗** | 普通领域扫描只看最近 1–2 天；**关注名单里的人开 180 天窗口**。配合 SQLite 记录"已经推送过什么"，只要这个人的工作你还没被推送过，五月的论文今天照样会出现在「今日必读」里。 |
| **补课模式** | `aidigest backfill --days 180` 一次性把名单里 126 位研究者近半年的工作全捞出来归档。之后每天只推增量。 |
| **页面差分** | 有些想法不发 arXiv 也没有 RSS（比如 Sutton 只在 incompleteideas.net 上贴）。这类页面抓链接存快照，出现新链接就报。 |
| **迟到的热度** | 已经推过但 HuggingFace 票数突然上涨的旧论文，会以「🕰️ 迟到的热度」重新浮出来。 |

---

## 输出长什么样

```markdown
# AI 前沿雷达 · 2026-08-26

> 扫描 412 条 → 入选 38 条 ｜ 关注名单命中 7 位研究者

**今日分布**：🧠 大模型 (6) ｜ 🤖 智能体 (5) ｜ 🦾 VLA (4) ｜ 🌍 世界模型 (3) …

## ⭐ 今日必读

1. **[Enactivism and the Nature of Intelligence](https://arxiv.org/abs/...)**
   把智能定义为「与环境的持续互动」而非「对世界的表征」，据此重构 RL 的目标函数。
   *→ Sutton 亲自给出的范式主张，不是增量工作*
   <sub>👤 **Richard S. Sutton · U Alberta / Amii** | 💡 position paper | arXiv · 05-14（104 天前）</sub>
```

按领域分组（CV / LLM / Agent / Harness / 多模态 / VLA / 世界模型 / 具身 / RL / 理论 / 安全），
末尾折叠一个「源状态」块，哪个源挂了一目了然。

---

## 快速开始

```bash
git clone <your-repo-url> && cd ai-frontier-radar
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
```

先确认各数据源在你的网络下都通：

```bash
.venv/bin/python -m aidigest check
```

第一次跑，建议先补课（会花几分钟，arXiv 要求请求间隔 3 秒）：

```bash
.venv/bin/python -m aidigest backfill --days 180
```

之后每天：

```bash
.venv/bin/python -m aidigest run
```

结果写到 `digests/2026/2026-08-26.md`，同时复制一份到 `digests/latest.md`。

### 用 Claude 生成中文速览（可选）

设了 `ANTHROPIC_API_KEY` 就会自动给入选条目写「一句话摘要 + 为什么值得看」，
并顺手纠正关键词分错的领域。**没设也能正常出结果**，只是摘要退化成截断的英文 abstract。

```bash
export ANTHROPIC_API_KEY=sk-ant-...
.venv/bin/python -m aidigest run
```

默认 `claude-opus-5`、`effort: medium`、每批 10 条、每天最多 60 条（和简报容量一致，
所以每条都有速览）。粗算一个月十块钱上下。想更省有三个旋钮：
把 `llm.max_items` 调小（超出的退化成截断的英文摘要）、把 `llm.effort` 降到 `low`、
或者把 `llm.model` 换成 `claude-haiku-4-5`。

---

## 命令

| 命令 | 用途 |
|---|---|
| `aidigest run` | 跑一轮，生成当日简报 |
| `aidigest run --dry-run` | 只打印不落盘、不记状态（调参时用） |
| `aidigest run --no-llm` | 跳过 Claude 摘要 |
| `aidigest run --source arxiv --source hf` | 只跑指定源 |
| `aidigest run --from-raw --dry-run` | 复用上次抓取的原始数据重跑，**不联网** —— 调打分权重时用 |
| `aidigest backfill --days 180` | 补课：关注名单近 N 天全捞 |
| `aidigest check` | 逐个源做连通性检查 |
| `aidigest stats` | 看积累了多少、各领域分布 |

---

## 配置

四个文件，都在 `config/`，改完不用动代码。

### `watchlist.yaml` —— 最重要的一个

126 位研究者 + 20 个机构。这是整个工具的信号来源，**建议按你自己的方向增删**：

```yaml
- {name: Richard S. Sutton, aliases: [Richard Sutton], affiliation: U Alberta / Amii,
   tags: [rl, theory], weight: 3.0}
```

- `weight`：3.0 = 出手必看，2.0 = 高度关注，1.5 = 常规关注
- `aliases`：署名变体。**昵称必须显式写**（"Rich Sutton" 不会自动匹配 "Richard Sutton"）
- `arxiv_query`：重名严重的人可以自定义查询，例如
  `au:"Yang Song" AND (cat:cs.LG OR cat:cs.CV)`
- `categories`：另一种收窄方式，只在指定 arXiv 分类下才算命中

姓名匹配规则：忽略中间名，变音符号归一（Schmidhuber ≡ Schmidhuber），
大小写无关；**只有缩写对上**（`R. S. Sutton`）算 0.7 置信度，显示时带 `?`。

### `topics.yaml` —— 领域定义

每个领域一组 `strong`（权重 3.0）和 `weak`（权重 1.0）关键词，支持正则。
得分最高的领域作主领域。想加新方向直接加一个 topic 块即可。

### `sources.yaml` —— 数据源

- `arxiv`：分类、两个时间窗、请求间隔
- `hf_papers`：HuggingFace Daily Papers，以及「迟到的热度」的票数阈值
- `rss`：15 个实验室 / 个人博客
- `pagewatch`：7 个没有 RSS 的重要页面（Sutton 主页、Anthropic Research、Physical Intelligence、Meta AI Blog…）

### `config.yaml` —— 打分权重与输出

```yaml
scoring:
  weights:
    watchlist_author: 6.0   # 命中名单作者（× 该作者 weight）
    lab: 2.0
    hf_upvotes: 1.2         # log1p(票数)
    idea_signal: 2.5        # "Rethinking…" / "position paper" 这类大想法句式
    recency: 1.5
  min_score: 9.0                      # 低于此分不进简报
  min_name_confidence: 1.0            # 见下方「姓名误匹配」
  max_authors_for_author_match: 30    # 超过这个作者数的论文不参与名单加分

output:
  max_items_per_topic: 8
  max_items_total: 60     # 超出的**不标记为已推送**，会排进后续几期
```

**命中关注名单的条目不受 `min_score` 限制，永远保留** —— 这是工具存在的理由。

调权重的正确姿势：先 `aidigest run --dry-run` 抓一次（原始数据会缓存到
`.state/last_raw.json`），之后反复 `aidigest run --from-raw --dry-run` 离线重算，
一秒一轮，不用每次等 4 分钟网络请求、也不会被 arXiv 限流。

---

## 自动化：GitHub Actions

`.github/workflows/daily.yml` 每天 UTC 23:00（北京时间 07:00）自动跑：

1. 生成简报并提交到 `digests/`
2. 开一个 GitHub Issue，标题是当天日期，正文是整份简报 —— **这样 GitHub 会直接把简报发到你邮箱/手机**

需要配置：

- 仓库 Settings → Secrets → Actions 加 `ANTHROPIC_API_KEY`（不加也能跑，只是没有中文摘要）
- 不想收 Issue 通知：Settings → Variables 加 `CREATE_ISSUE=false`
- 建一个叫 `digest` 的 label（可选，没有也不会失败）

> **`.state/seen.sqlite3` 是故意提交进仓库的。** Actions 每次都是全新容器，
> 不把去重状态带上，你会每天收到一模一样的内容。

---

## 设计上的几个取舍

**为什么不做机构（affiliation）自动识别？**
arXiv 的 API 不返回作者单位，摘要里也基本不写。所以机构信号只来自三处：博客 feed 自带的 lab 标记、论文 comment 字段的弱匹配、以及关注名单里作者自己填的 affiliation。`watchlist.yaml` 里的 affiliation 字段**只用于展示，可能过时**，匹配完全按姓名做。

**为什么单个源失败不中断？**
每个源独立抓取，失败记进 `errors` 列表，渲染到简报末尾的「📡 源状态」折叠块里。一个 feed 改版不该让你今天收不到简报。

**为什么 LLM 是可选的？**
关键词分类 + 打分排序在没有任何 API key 的情况下就能用。LLM 负责的是「把英文摘要压成一句中文」和「纠正分错的领域」—— 是增强，不是依赖。

**姓名误匹配是这类工具最大的坑。**
第一版跑出来，「今日必读」前五条全是 BESIII 和 LHCb 的高能物理论文 —— 那种论文有
四五百位作者，里面的 `K. He`、`L. Fan`、`F. Li` 被匹配成了何恺明、Jim Fan、李飞飞。
现在有三道防线：

1. 作者扫描的 arXiv 查询限定在 CS / stat 分类内（`author_scan_categories`）
2. 姓名必须**全名**对上，缩写不算（`min_name_confidence: 1.0`）
3. 作者数超过 30 的论文一律不参与名单加分（`max_authors_for_author_match`）

代价是署名写成 `R. S. Sutton` 的论文会漏掉 —— 但 CS 方向的 arXiv 元数据基本都是全名，
这个交换是划算的。`tests/test_core.py` 里有三个回归测试钉住了这个行为。

**其他已知弱点：**
- 常见中文姓名（Yang Song、He Wang…）误匹配率偏高，用 `arxiv_query` 或 `categories` 收窄
- `pagewatch` 抓到的链接没有可靠日期，只能按"发现时间"排序
- 首次监控一个页面时只建立基线、不报告（否则一次涌出上百条历史链接）；`backfill` 模式下会报最多 15 条

---

## 测试

```bash
.venv/bin/python -m pytest tests/ -q
```

20 个不联网的单元测试，覆盖姓名匹配、领域分类、打分逻辑、页面链接提取和渲染。
其中 `test_old_watchlist_paper_still_kept` 直接钉住了本文开头那个需求。
