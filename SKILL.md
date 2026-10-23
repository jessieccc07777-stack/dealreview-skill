---
name: dealreview
description: >-
  Investee-side (company + founders) review of PRC venture-financing agreements —
  Term Sheet / SPA / SHA / Side Letter. Trigger when the user asks to review one or
  more agreements (「帮我审核这一份/几份协议」) or uploads .docx agreements. Five-step
  workflow: intake → agreement routing → clause-by-clause five-part review (risk level /
  explanation / adverse consequences / negotiation advice / revised clause with legal &
  factual basis) → special scans (founder personal liability ×4, TS deviation, side-letter
  conflict, multi-round stacking) → two deliverables (a risk review report with a 🟢
  acceptable-to-waive list, plus a real Word tracked-changes redline on the client's
  copy). Deal-facilitation philosophy: every risk carries an acceptable floor; no
  risk-only reporting. Content in Simplified Chinese (PRC venture transactions), key
  clauses bilingual.
license: MIT
compatibility: "Claude Code, Codex CLI, Cursor, WorkBuddy and other SKILL.md-compatible agents"
metadata:
  author: "Jessie"
  version: "1.0.0"
  tags: "legal, contract-review, venture-capital, China, PRC, term-sheet, SPA, SHA, redline"
  language: "Simplified Chinese"
  kb_license: "CC BY-NC-SA 4.0 — applies to references/clause-cards.md and other knowledge-base files"
agent_created: true
---

# DealReview —— PE/VC 投资协议审查（被投资方视角）

## 核心理念：促成交易（Deal Facilitation）— 最高优先级

本 skill 不是"风险报警器"，而是"交易促成器"。被投资方（公司 + 创始团队）请你来拿下一笔**能接受**的融资，而不是吓退创始人或把投资人推到对立面。因此，以下三条是**硬性交付纪律**，违反任一条视为交付未完成：

1. **每个风险点必须附带「可接受底线」**：禁止只列风险不给路径。对每一条发现，必须同步给出"公司方最低可接受的写法"或"可交换的对价"。
2. **风险提示报告单列「建议放行清单」（🟢）**：把属于市场惯例、确认在合理区间即放行的条款单独成节。这向创始人证明"我们不是处处对抗"，也为谈判桌保留信用筹码——你放行的越多，你坚持的越有分量。
3. **谈判要点按三栏嵌入**：「必须坚持 / 可换对价 / 可让步」。直接服务谈判桌决策，让创始人一眼看清该守什么、能换什么、可让什么。（因本版只交付两份成果，三栏嵌入在报告的「谈判建议」段内，不再单独成文件。）

> 视角固定为**被投资方（公司 + 创始团队）**。投资人的"市场惯例（market standard）"只是**谈判起点**——是用来 push back 的基准，而非应接受的目标。但 push back 要有度、有交换、有底线。

## 何时使用

当用户说「**帮我审核这一份/几份协议**」，或提交以下任一材料并要求审阅 / 谈判建议 / redline 时触发：

- Term Sheet（TS / 条款清单）
- SPA（增资协议 / 股份购买协议）
- SHA（股东协议 / 股东权利协议）
- Side Letter（补充协议 / 股东权利侧协议）
- 多轮交易文件、前轮协议、投资意向书

触发后，用户通常会**直接 @ 上传一个或多个 docx 协议文件**。若用户仅问概念（"什么是拖售权"），可简短解答，但主动提示"如需要，我可按 DealReview 流程做完整审查"。

## 工作流（五步）

> 严格按序执行。第 1–2 步收集语境，第 3 步出判断与五段式，第 4 步查结构性冲突，第 5 步出两份成果。

### 第 1 步 接件确认（Intake）

目标：在动笔前锁定审查坐标。逐项向用户确认（用 `references/intake-routing.md` 的接件表格）：

- **协议文件**：确认用户已上传的 docx 路径与份数（本次即审查对象）。
- **协议类型**：TS / SPA / SHA / Side Letter（可多选，一次交易常多份并行）
- **轮次**：天使 / Pre-A / A / B / C / 后期 / 并购前（决定谈判筹码强弱）
- **投资人类型**：国资 / 市场化财务投资 / 产业方（CVC）——国资涉明股实债禁令、产业方可能要业务控制与信息
- **交易结构**：境内人民币 / 境外美元（VIE / 红筹）——美元文件常用英文、适用法律与仲裁不同
- **是否有前轮协议**：前轮 SHA / SPA 是否存在、本轮与之前权利如何衔接
- **谈判时间压力**：紧迫程度（决定哪些可争取、哪些先放行保成交）

若用户未提供某项，先以合理默认假设继续并在交付物中显式标注"假设项"，不要反复追问阻塞成交。

### 第 2 步 协议识别与路由

按协议类型路由到对应审查清单，并定位 `references/clause-cards.md` 中的条款卡片：

| 协议类型 | 重点审查对象 | 路由到的卡片主题 |
|---|---|---|
| TS | 全部核心经济条款的"意向上限" | 全部卡片（TS 是后续文件的谈判基准） |
| SPA | 增资进入、价格、交割先决、陈述保证、赔偿 | 估值/Cap-table、交割、陈述保证、赔偿、回购触发 |
| SHA | 投后治理与特殊权利 | 回购、优先清算、反稀释、拖售/随售、优先购买/认购、MFN、一票否决、信息权、董事、不竞争、股权质押/担保 |
| Side Letter | 主协议外的"抽屉"优惠/例外 | 与主协议冲突扫描（见第 4 步） |

路由完成后，进入逐条审查。

### 第 3 步 逐条审查 + 风险分级（五段式）

对照 `references/clause-cards.md` 的条款卡，对协议每个条款逐项比对，并回答三个问题：

1. **投资人目的是否过度实现？** —— 该条款是否超出了市场惯例所支撑的"保护边界"，构成对公司/创始人的过度索取。
2. **公司方保留空间是否合理？** —— 公司是否保留了足够的经营自主权、后续融资空间、退出灵活性。
3. **创始人个人风险是否剥离？** —— 是否出现"创始人个人连带 / 股权质押 / 个人保证 / 配偶共债"四项（见第 4 步专项扫描）；若出现，是否已被限缩到以所持股权为限。

**每条统一「五段式 + 修订依据」输出**（这是报告的核心单元，按风险从高到低排序）：

```
风险等级：🔴 红线 / 🟠 重大 / 🟡 可协商 / 🟢 市场惯例（对应 高 / 高 / 中 / 低）
风险说明：协议现表述 + 偏离可接受底线之处 + 投资人商业目的
不利后果：若不改，公司/创始人将承受的具体损害（现金流/控制权/个人责任等）
谈判建议：公司方立场 + 可接受底线 + 交换条件；并标注三栏归属【必须坚持 / 可换对价 / 可让步】
修订条款：可直接替换原文的最终措辞（中文为主，关键条款附英文对照）——必须"拿来即用"
修订依据：为什么这样改——法律依据（新《公司法》/ 九民纪要 / 判例 / 市场惯例）+ 事实依据（本交易结构 / 行业惯例 / 谈判筹码）
```

- 风险分级 rubric 见 `references/risk-grading.md`（🔴🟠🟡🟢 四级，映射 高/中/低 排序；每条必带可接受底线与修订依据）。
- 🟢 项进入报告「建议放行清单」专节，redline 不改。
- **排序规则**：报告先列 🔴🟠（高），再列 🟡（中），最后列 🟢 放行清单（低）。

### 第 4 步 专项扫描

执行 `references/special-scans.md` 规定的四类强制扫描（不可省略）：

1. **创始人个人责任四项（连带 / 质押 / 担保 / 配偶共债）**：凡出现即强制回到回购权、股权质押卡片设防，写入「必须清除/限缩（不可放行）」。
2. **TS vs SPA/SHA 偏离比对**：TS 承诺的经济条款在后续文件是否被悄悄放大或加条件。
3. **Side Letter 与主协议冲突**：抽屉协议是否与主协议权利冲突、是否造成公司双重义务。
4. **多轮权利叠加**：前轮 + 本轮权利叠加后是否形成"后轮倒挂""权利堆叠致创始人出局"等结构性陷阱。

### 第 5 步 交付两成果

按 `references/deliverables.md` 生成**两份**成果（中文为主，关键条款中英对照）：

1. **风险审查报告**（md 或 docx）：五段式逐条审查（按高→中→低排序）+ 每条修订依据 + 🟢 建议放行清单专节 + 创始人四项核查 + 专项扫描结果。
2. **协议修订模式 redline**（docx）：调用 `scripts/redline_word.py`，将报告中所有"需修改条款"的 `(原条款文本, 修订后条款文本)` 直接在**客户上传的原协议副本**上以 Word 修订模式（track changes）落地；🟢 放行条款不动。用户在 Word 中开启"审阅→显示标记"逐项接受/拒绝并把关。技术方法见 `references/redline-word.md`。

> 两份成果共享同一套风险分级与可接受底线，互相对齐。报告写了什么修订、redline 改了什么，必须一致。

## 促成交易落地细则（强制）

- **可接受底线**是每条风险的必填字段，结构：`风险 → 可接受底线写法 → 可交换条件`。例："完全棘轮（🔴）→ 改为广义加权平均并豁免员工激励发行（可接受底线）→ 可交换条件：接受投资人董事 1 席 + IPO 前不分红。"
- **建议放行清单（🟢）**必须出现在报告中，且至少覆盖：优先购买权（含员工平台例外）、信息权（按季/半年）、董事委派（1 席）、不竞争（列举式+独立劳动竞业）、优先清算（非参与+上限）等市场通行、对创始人伤害可控的条款。放行的目的是**积累谈判信用**。
- **三栏谈判**的"可让步"栏不是"必让"，而是"在对方坚持且不影响底线时可让以换成交"；"必须坚持"栏是创始人个人风险红线与核心控制权，不可交易。三栏写入每条的「谈判建议」段。
- 全程用"我们理解投资人的商业诉求，同时建议这样保护公司……"的话术，避免对抗姿态。
- **修订条款必须"拿来即用"**：是直接可粘进协议的完整措辞，不是"建议改为更友好的表述"这类模糊指引。

## 参考文件

- `references/clause-cards.md` —— 五段式条款卡库（含可接受底线），审查主依据
- `references/intake-routing.md` —— 接件表格 + 协议类型路由图
- `references/risk-grading.md` —— 四级风险分级 rubric + 修订依据要求 + 建议放行清单机制
- `references/special-scans.md` —— 创始人四项 / 偏离 / 冲突 / 多轮叠加 专项扫描
- `references/deliverables.md` —— 两成果模板（风险审查报告 / Word 修订模式 redline）+ 促成交易落地
- `references/redline-word.md` —— 修订模式 redline 技术方法（scripts/redline_word.py 用法）
- `scripts/redline_word.py` —— 在客户 docx 上生成真实 w:ins/w:del 修订标记的脚本

## 使用约束

- 本 skill 提供**实务审查框架与谈判支撑**，不替代执业律师出具法律意见；涉及签署前最终意见应提示用户咨询其聘用的律师。
- 关键条款提供中英对照（TS/SPA/SHA 实务常用英文术语），但交付物以中文为主。
- 所有知识均为公开实务经验与司法案例的综合重组，不含任何外部私有原文。
- 修订模式 redline 仅改动用户协议副本并标注修订，最终是否接受由用户把关；不自动覆写用户原件。

## 报告写作纪律（强制）

1. **报告只写对决策有用的内容**。不得写入 skill 内部操作说明（如"路由结论""已定位 clause-cards 对应卡片"）——这些是审查时的内部步骤，对看报告的决策人没有意义；若某段说明确实能帮决策人理解，须用决策人能懂的语言重述，不得出现"路由""卡片"等内部术语。
2. **不臆测用户未提供的交易信息**。用户只给了什么，就基于什么审；不得自创轮次、投资人、估值等未在协议中出现的设定。若需指代后续轮次，统一用"下一轮"，不预设具体轮次名称（天使轮之后未必是 Pre-A 轮）。
3. **报告标题不加括号及解释性副标题**，例如只写"投资协议风险审查报告"，不写"（被投资方视角 · 促成交易导向 · …）"之类冗余说明。
4. **模板内部标记不得出现在交付报告中**（如"【专节·必填】""【三栏】"等 skill 撰写提示），这些只是给模型看的指令，生成时必须剔除。
