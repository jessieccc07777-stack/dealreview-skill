# DealReview

**Investee-side AI review of PRC venture-financing agreements — Term Sheet / SPA / SHA / Side Letter.**

一个面向**被投资方（公司 + 创始团队）**视角的 PE/VC 投资协议审查 AI Skill。把资深律师的十年投融资实务沉淀成可安装的 AI 助手技能，让早期创始人在没有大所预算的情况下，也能对融资协议做专业级初审。

> 核心理念：**促成交易（Deal Facilitation）**。它不是"风险报警器"，而是"交易促成器"——每个风险点必附可接受底线，报告单列 🟢 建议放行清单，谈判要点按「必须坚持 / 可换对价 / 可让步」三栏给出。

---

## What it does / 它做什么

Five-step workflow, two deliverables. 五步工作流，两份交付物：

1. **接件确认（Intake）** — 锁定协议类型、轮次、投资人类型、交易结构、前轮衔接
2. **协议识别与路由** — TS / SPA / SHA / Side Letter 各路由到对应条款卡
3. **逐条五段式审查** — 每条条款输出：风险等级（🔴🟠🟡🟢）/ 风险说明 / 不利后果 / 谈判建议 / 修订条款（拿来即用），并附**法律依据 + 事实依据**
4. **专项扫描** — 创始人个人责任四项（连带/质押/担保/配偶共债）、TS 偏离、Side Letter 冲突、多轮叠加
5. **双交付物**：
   - **风险审查报告**（md/docx）——五段式逐条 + 🟢 建议放行清单 + 创始人四项核查 + 专项扫描
   - **Word 修订模式 redline**（docx）——在客户上传协议副本上直接落真实 track-changes 修订标记

## Why it matters / 为什么有用

早期创始人、甚至公司管理层，都无法真正读完一套合计上百页的 SPA/SHA/补充协议，但其中的回购、反稀释、拖售、否决权条款决定公司命运。DealReview 把"数小时的专业阅读"变成"几分钟的结构化输出"。

## Installation / 安装

详见 [`docs/INSTALL.md`](docs/INSTALL.md)（含分步安装 SOP）。

- **Claude Code / Cursor / Codex**：把本仓库 skill 目录放入 `~/.claude/skills/`（或对应目录）
- **WorkBuddy**：放入 `~/.workbuddy/skills/`
- 一句话：下载本仓库 → 把 `dealreview-skill/` 整个文件夹放进你的 AI 助手的 skills 目录即可

## Quick start / 快速开始

1. 安装本 skill
2. 把你的协议 docx 上传给 AI，说一句：**"帮我审核这份协议"**
3. AI 按五步流程接件 → 审查 → 输出两份成果（风险审查报告 + Word 修订版）

示例输入与预期输出见 [`examples/`](examples/)（虚构数据）。

## Jurisdiction / 适用法域

本 skill 面向**中国大陆（PRC）创投交易**（含新《公司法》、九民纪要、法答网口径），交付物以简体中文为主，关键条款中英对照。方法论（五段式、可接受底线、三栏谈判）可迁移至其他法域与协议类型（雇佣、许可、BD 交易），但条款卡的法律依据当前以中国法为准。

## Repository layout / 目录结构

```
dealreview-skill/
├── SKILL.md                  # skill 定义（frontmatter + 五步工作流）
├── references/
│   ├── clause-cards.md       # 五段式条款卡库（审查主依据）· 知识库
│   ├── intake-routing.md     # 接件表格 + 协议类型路由
│   ├── risk-grading.md       # 四级风险分级 rubric
│   ├── special-scans.md      # 创始人四项 / 偏离 / 冲突 / 多轮叠加
│   ├── deliverables.md       # 两成果模板
│   └── redline-word.md       # redline 技术方法
├── scripts/
│   └── redline_word.py       # Word 修订模式生成器
├── examples/                 # 示例输入与预期输出（虚构）
└── docs/INSTALL.md           # 安装 SOP
```

## License / 许可

本仓库采用**双许可**，请按文件类型区分：

| 文件范围 | 许可 | 含义 |
|---|---|---|
| `SKILL.md`、`scripts/` 下的代码、`examples/`、`docs/` | **MIT** | 可自由使用、修改、分发，含商用 |
| `references/clause-cards.md` 等知识库文件 | **CC BY-NC-SA 4.0** | 署名 + 非商业 + 相同方式共享；不得用于商业产品 |

- 完整 MIT 文本见 [`LICENSE`](LICENSE)
- CC BY-NC-SA 4.0 说明与全文链接见 [`LICENSE-KB.md`](LICENSE-KB.md)

> 若你希望将条款卡库用于商业产品，请联系作者另行授权。

## Disclaimer / 免责声明

本 skill 提供**实务审查框架与谈判支撑**，**不构成法律意见**，不替代执业律师。签署前最终意见请咨询你聘用的执业律师。作者不对依赖本工具输出而产生的任何后果承担责任。

## Feedback & contribution / 反馈与贡献

欢迎提交 Issue 与 PR，或邮件联系 jessieccc0713@gmail.com。法律依据（新《公司法》、法答网、九民纪要判例）会按季度复核更新。

## Author / 作者

Jessie —— 前 PE/VC 从业者，十年投融资与资本市场法律实务经验。

反馈与联系：jessieccc0713@gmail.com

---

*First released 2026. Built with practitioner experience — responsible AI that widens access to legal expertise.*
